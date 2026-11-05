# Ejecución en la org con sf CLI

## Índice
1. Conexión
2. Pre-flight (seguridad, licencias, locale)
3. Proyecto y despliegue de metadata
4. Permisos y usuarios
5. Datos de ejemplo
6. Verificación
7. Reset
8. Errores frecuentes

Todos los comandos usan `--target-org <alias>` explícito, aunque haya org por defecto: evita
escribir en la org equivocada. Usa `--json` cuando necesites leer el resultado.

---

## 1. Conexión

- **Agentforce Vibes IDE** (lanzado desde Setup de la org): la org ya está autenticada. Obtén el
  alias con `sf org list`.
- **Agentforce Vibes / Claude Code en VS Code local**: si hay org por defecto, úsala; si no, pide al
  usuario que ejecute (requiere navegador):
  `sf org login web --alias demo-<slug> --set-default`
  En SDO o dominios propios: añade `--instance-url https://<mi-dominio>.my.salesforce.com`.

Nunca pidas ni escribas contraseñas en el chat ni en ficheros.

## 2. Pre-flight

### 2.1 ¿Es una org de demo?
```bash
sf data query --target-org <alias> --json --query \
 "SELECT Name, OrganizationType, IsSandbox, TrialExpirationDate, DefaultLocaleSidKey, LanguageLocaleKey, TimeZoneSidKey, DefaultCurrencyIsoCode FROM Organization"
```
- `OrganizationType = 'Developer Edition'`, `IsSandbox = true` o `TrialExpirationDate` no nulo →
  org de demo, adelante.
- Cualquier otra (típico de una SDO: Enterprise/Unlimited sin fecha de expiración) → **pregunta al
  usuario** "¿Confirmas que <Name> es una org de demo y no producción de un cliente?" y no
  escribas nada hasta que lo confirme.
- Scratch org: `sf org display --target-org <alias>` muestra si es scratch.

### 2.2 Licencias y funciones
```bash
sf data query --target-org <alias> --query "SELECT MasterLabel, DeveloperName, TotalLicenses, UsedLicenses FROM PermissionSetLicense ORDER BY MasterLabel"
sf data query --target-org <alias> --query "SELECT Name, TotalLicenses, UsedLicenses FROM UserLicense"
sf data query --target-org <alias> --query "SELECT Name, NamespacePrefix FROM PackageLicense"
```
Contrasta con la tabla de licencias del playbook. Los nombres exactos cambian entre releases:
busca por coincidencia parcial (p. ej. "Marketing", "Agent", "Einstein", "Data Cloud", "FSL") y, si
no aparece, márcalo como **no disponible** y explica qué org hace falta.

### 2.3 Usuario de demo
```bash
sf org display user --target-org <alias>
```
En una demo rápida el SE suele presentar con el propio usuario administrador; está bien. Si el
playbook pide un segundo usuario (manager, agente), créalo (sección 4).

### 2.4 Idioma, moneda, zona horaria
Si el usuario de demo no está en español/EUR/Europe/Madrid, actualízalo:
```bash
sf data update record --target-org <alias> --sobject User --where "Username='<user>'" \
 --values "LanguageLocaleKey=es LocaleSidKey=es_ES TimeZoneSidKey=Europe/Madrid"
```
Los valores por defecto de la organización (Company Information) y la moneda de la org son pasos
manuales en Setup; añádelos a la guía si no coinciden.

## 3. Proyecto y despliegue de metadata

```bash
sf project generate --name demo-<slug> --manifest
cd demo-<slug>
```

**Retrieve → modificar → deploy.** Para settings y metadata existente, descarga primero la versión
de la org y modifícala: así el XML tiene el esquema exacto de esa release.
```bash
sf project retrieve start --target-org <alias> --metadata "Settings:Forecasting"
# editar force-app/main/default/settings/Forecasting.settings-meta.xml
sf project deploy start --target-org <alias> --source-dir force-app --dry-run   # validar
sf project deploy start --target-org <alias> --source-dir force-app             # desplegar
```

Qué se despliega bien como metadata en una demo rápida: CustomField, ListView, Report,
Dashboard, ReportType, FlexiPage, Layout, PathAssistant, PermissionSet, Flow, CustomApplication,
Queue, EmailTemplate, CustomLabel, Settings. Crea solo lo que alguna escena usa.

Dashboards y reports: carpeta propia (`DemoNespon`) desplegada con ellos; el dashboard con
`runningUser` = usuario de demo o tipo `LoggedInUser`.

Flows: despliégalos **inactivos** (`<status>Draft</status>`) si dispararían con la carga de datos;
actívalos después de cargar (cambiando a `Active` y redeploy).

## 4. Permisos y usuarios

```bash
sf org assign permset --target-org <alias> --name <PermSetApiName> [--on-behalf-of <username>]
sf org assign permsetlicense --target-org <alias> --name <PSLDeveloperName> [--on-behalf-of <username>]
```
Segundo usuario (solo si una escena lo necesita): `sf org create user` en scratch orgs; en el resto,
créalo con `sf data create record --sobject User` (ProfileId de Standard User, username único
`<nombre>.<slug>@demo-<slug>.example`, email del SE) y avisa de que llegará un correo de activación.

## 5. Datos de ejemplo

1. Escribe la spec en `seed/seed-spec.json` (formato en `org-y-datos-semilla.md`; ejemplos en
   `assets/`). Fechas relativas, emails `@example.com`, padres antes que hijos.
2. Genera y carga:
```bash
python3 <skill-dir>/scripts/build_seed.py seed/seed-spec.json --out seed/out
sf data import tree --target-org <alias> --plan seed/out/seed-plan.json --json > seed/import-result.json
```
3. Guarda `seed/import-result.json`: lo usa el reset.

Picklists: usa valores que existan en la org (compruébalo con
`sf sobject describe --sobject <Obj> --target-org <alias>` si dudas). Un valor inexistente falla la
carga del fichero entero.

## 6. Verificación

Por cada escena del playbook, la consulta que prueba que tiene contenido, p. ej.:
```bash
sf data query --target-org <alias> --query "SELECT COUNT() FROM Opportunity WHERE IsClosed = false"
sf org list metadata --target-org <alias> --metadata-type Dashboard --folder DemoNespon
```
Resultado por escena: ✅ lista · ⚠️ pendiente de paso manual · ❌ no disponible (motivo).

## 7. Reset

`reset.sh` borra lo cargado (hijos primero) y recarga con fechas frescas. Plantilla:

```bash
#!/usr/bin/env bash
set -euo pipefail
ORG="${1:?uso: ./reset.sh <alias>}"
cd "$(dirname "$0")"
# 1) borrar registros cargados, en orden inverso al plan
python3 - <<'PY'
import json, collections, pathlib
res = json.load(open("seed/import-result.json"))
rows = res.get("result", [])
rows = rows if isinstance(rows, list) else rows.get("records", [])
by = collections.OrderedDict()
for r in rows:
    by.setdefault(r["type"], []).append(r["id"])
out = pathlib.Path("seed/delete"); out.mkdir(exist_ok=True)
order = list(by)[::-1]
for t in order:
    (out / f"{t}.csv").write_text("Id\n" + "\n".join(by[t]) + "\n")
(out / "order.txt").write_text("\n".join(order))
PY
while read -r OBJ; do
  sf data delete bulk --target-org "$ORG" --sobject "$OBJ" --file "seed/delete/$OBJ.csv" --wait 10
done < seed/delete/order.txt
# 2) recargar con fechas del día
python3 <skill-dir>/scripts/build_seed.py seed/seed-spec.json --out seed/out
sf data import tree --target-org "$ORG" --plan seed/out/seed-plan.json --json > seed/import-result.json
echo "Reset completado"
```
Sustituye `<skill-dir>` por la ruta real al generar el fichero. Registros creados *durante* el
ensayo (tareas de un Flow, casos de un formulario) no están en el resultado: añade al reset un
borrado por consulta específica si el playbook lo indica.

## 8. Errores frecuentes

| Síntoma | Causa habitual | Qué hacer |
|---|---|---|
| `INVALID_OR_NULL_FOR_RESTRICTED_PICKLIST` | Valor de picklist que no existe | Describe el objeto y usa un valor válido |
| `FIELD_INTEGRITY_EXCEPTION` en Order/Contract | Estado no permitido al crear | Crear en estado borrador y actualizar después |
| `INVALID_FIELD_FOR_INSERT_UPDATE` | Campo de sistema o auditoría | Quitarlo o activar Set Audit Fields |
| Deploy de Settings falla | XML no coincide con la release | Retrieve de nuevo y editar sobre lo descargado |
| Dashboard vacío | Running user sin acceso o datos fuera de filtro de fechas | Revisar running user y fechas relativas |
| `sf` pide login | Sesión caducada | `sf org login web --alias <alias>` (lo hace el usuario) |
