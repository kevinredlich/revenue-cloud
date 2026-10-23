# revenue-cloud-poc

Skill de Claude Code / Agentforce Vibes para convertir una necesidad de negocio (o un scan
técnico de una org con Salesforce CPQ) en una **POC de Salesforce Revenue Cloud**: un manifiesto
que separa lo que construye la IA de lo que debe hacer una persona, y un informe de viabilidad que
concluye si la hipótesis queda validada, con evidencias.

No sustituye una implementación completa de Revenue Cloud: entrega un experimento acotado para
responder **"¿se puede hacer esto en Revenue Cloud, y bajo qué condiciones?"**.

## Relación con otras skills

Esta skill **extiende** `nespon-brief-to-demo` (reutiliza su reparto IA/IA+Revisión/Persona,
niveles de impacto 🟢/🔵/🟠, generador de datos de prueba `fill_data.py`) y se apoya en
`nespon-demo-builder` para el playbook de objetos de Revenue Cloud y la ejecución real en org.
Si `rlm-skill` está instalada en el proyecto, es la fuente técnica autoritativa para verificar
cualquier afirmación de una hipótesis o componente (modelo de datos, pricing, decision tables,
expression sets); si no está, se cae al artículo de Salesforce Help y se marca
`PENDIENTE DE VALIDACIÓN`.

Hace falta tener cargadas (en el mismo proyecto/repo de skills): `nespon-brief-to-demo`,
`nespon-demo-builder` y, si existe, `rlm-skill`.

## Estructura de la skill

```
revenue-cloud-poc/
├── SKILL.md                                  # instrucciones de la skill (todas las fases)
├── references/
│   ├── manifiesto-necesidades.md             # formato exacto de MANIFIESTO-NECESIDADES.md (Fase 0)
│   ├── manifiesto-poc.md                     # formato exacto de MANIFIESTO-POC.md (Fase 1)
│   └── informe-viabilidad.md                 # formato del informe de resultado (Fase 3)
├── assets/
│   ├── ejemplo-MANIFIESTO-POC.md             # ejemplo completo y válido (Bodegas Altiplano)
│   └── ejemplo-INFORME-VIABILIDAD.md
├── ejemplos/
│   └── poc-prosegur-cpq/                     # caso real completo (FASE 0 + FASE 1 APROBADO)
└── scripts/
    ├── scan_to_poc.py                        # genera manifiestos a partir de un scan de CPQ Scout
    └── validate_manifest_poc.py              # valida MANIFIESTO-POC.md (diseño y puerta de ejecución)
```

Requiere Python 3 (sin dependencias de terceros — solo `argparse`, `json`, `re`, `datetime` de
librería estándar). Para la Fase 3 real sobre una org hace falta además `sf` (Salesforce CLI).

## Flujo completo

```
Documento/scan → FASE 0: MANIFIESTO-NECESIDADES.md → confirmar modalidad
     → FASE 1: MANIFIESTO-POC.md (diseño) → validar
     → FASE 2: revisión del SE → APROBADO
     → FASE 3: ejecutar en una org real → INFORME-VIABILIDAD.md
```

### FASE 0 — Intake unificado (antes de decidir DEMO / POC / Migración)

Nunca se decide la modalidad mirando solo el documento del cliente. Primero se generan las
necesidades clasificadas con semáforo y una modalidad **propuesta** (nunca una aprobación del
cliente):

- **Origen = brief escrito a mano:** el agente lee el documento y extrae las `NEC-n` directamente
  en la conversación, siguiendo `references/manifiesto-necesidades.md`.
- **Origen = scan de CPQ Scout** (JSON de `/api/scan`):
  ```bash
  python3 scripts/scan_to_poc.py scan-result.json --cliente "Bodegas Altiplano SA" \
      --sector "Vino (bodega)" --zona-fiscal "Península (IVA 21%)" \
      --out poc-bodegas-altiplano/MANIFIESTO-NECESIDADES.md
  ```
  Cada fila del inventario del scan se convierte en `NEC-n` con semáforo (🟢 migración directa y
  riesgo bajo, 🟡 riesgo medio o rediseño, 🔴 riesgo alto o reescritura), y el script propone DEMO
  (si todo es 🟢) o POC/migración (si hay 🟡/🔴), con justificación.

El resultado se para en la sección 4 del documento ("Decisión"), a la espera de que el SE o el
cliente confirmen la modalidad. Solo entonces:

- **DEMO** → se pasa a `nespon-brief-to-demo`, usando `MANIFIESTO-NECESIDADES.md` como brief de
  entrada.
- **POC o Migración** (la migración es una POC cuya incertidumbre viene de un scan, no un
  workflow distinto) → se sigue con la Fase 1 de esta skill. Con origen scan, se vuelve a correr
  el mismo script sobre el mismo JSON con `--modalidad poc`:
  ```bash
  python3 scripts/scan_to_poc.py scan-result.json --cliente "Bodegas Altiplano SA" \
      --modalidad poc --out poc-bodegas-altiplano/MANIFIESTO-POC.md
  ```
  Esto genera un **pre-borrador**: la cabecera y las secciones 1-2 (necesidades e hipótesis) salen
  del scan, pero las secciones 3-8 (componentes, datos, orden, supuestos) quedan como plantilla —
  requieren diseño humano/agente y el resultado **no pasa el validador tal cual**.

### FASE 1 — Diseño (no toca ninguna org)

Con las `NEC-n` ya confirmadas:

1. Identificar la incertidumbre concreta a comprobar.
2. Formular una o varias hipótesis verificables (`HIP-n`) — nunca dar una por probada porque la
   documentación mencione "algo relacionado".
3. Diseñar los pasos del experimento (`EXP-n`), cada uno ligado a ≥1 hipótesis, con entrada,
   acción y **resultado esperado observable**.
4. Completar la tabla de componentes (sección 3): para cada uno, nivel de impacto (🟢/🔵/🟠),
   responsable (IA / IA+Revisión / Persona) y la columna **Origen** (ver más abajo).
5. Definir los datos de prueba (sección 5, mismo generador `fill_data.py` de
   `nespon-brief-to-demo`: siempre ficticios, `@example.com`, fechas relativas).
6. Validar:
   ```bash
   python3 scripts/validate_manifest_poc.py poc-<cliente>/MANIFIESTO-POC.md
   ```
   Corregir todo lo que salga como `ERROR`. El documento queda en `Estado de revisión: BORRADOR`.
   **Aquí se para — no se construye nada todavía.**

Formato exacto de cada sección: `references/manifiesto-poc.md`. Ejemplo completo y válido:
`assets/ejemplo-MANIFIESTO-POC.md`.

### FASE 2 — Revisión del SE

El SE revisa el `MANIFIESTO-POC.md`, puede pedir cambios (nueva versión + entrada en el
"Registro de cambios"), y aprueba cambiando la cabecera a:

```
**Estado de revisión:** APROBADO
**Revisado por:** <nombre> · **Fecha de aprobación:** <fecha>
```

Esta línea literal (`Estado de revisión: APROBADO`) es la única señal que el resto del flujo
reconoce como aprobación — no basta con decirlo en el chat sin escribirla en el documento.

### FASE 3 — Ejecución del experimento (solo con una org real conectada)

1. **Puerta obligatoria** antes de tocar nada:
   ```bash
   python3 scripts/validate_manifest_poc.py poc-<cliente>/MANIFIESTO-POC.md --gate
   ```
   Sin `Estado de revisión: APROBADO`, el validador falla y **no se construye nada en la org**.
2. Pre-flight: confirmar la org y las licencias de Revenue Cloud/Asset Lifecycle Management.
3. Construir los componentes en el orden de la sección 6 del manifiesto, respetando el reparto
   IA / IA+Revisión / Persona.
4. Cargar los datos de prueba (`fill_data.py` → `sf data import tree`, o el flujo equivalente).
5. Ejecutar cada paso del experimento y registrar el resultado real observado frente al esperado,
   con su evidencia (consulta SOQL, captura, log).
6. Clasificar cada hipótesis y generar `INFORME-VIABILIDAD.md` (formato en
   `references/informe-viabilidad.md`):
   - 🟢 **VALIDADA** — evidencia suficiente de cumplimiento.
   - 🟡 **PARCIALMENTE VALIDADA** — se cumple con limitaciones documentadas.
   - 🔴 **NO VALIDADA** — evidencia de incumplimiento.
   - **NO EJECUTADA** — no se ha realizado el experimento (p. ej. sin org conectada).
   - **NO CONCLUYENTE** — evidencia insuficiente para decidir.

   Nunca se marca una hipótesis como validada solo por haber generado documentación o código.

Si no hay una org conectada, la Fase 3 no se ejecuta: el entregable queda como
**PREPARADA, NO EJECUTADA**.

## La columna "Origen" de los componentes

La tabla de componentes (sección 3 del manifiesto) tiene, entre `Tipo` y `Especificación`, una
columna `Origen` con cuatro valores posibles:

| Valor | Significa |
|---|---|
| `Estándar SF` | Objeto/funcionalidad estándar de Salesforce (p. ej. `Product2`, `Report`, `PermissionSet`) |
| `Estándar RLM` | Objeto/funcionalidad estándar de Revenue Cloud/RLM (p. ej. `Asset`, `Quote`, `PricingRule`) |
| `Custom object` | Hay que crearlo: objeto custom (`__c`), campo custom sobre un objeto estándar, o automatización a medida |
| `N/A` | No es un componente de metadata (una verificación manual, una comprobación de licencia, etc.) |

**Regla importante:** `Custom object` solo se marca cuando se ha **verificado contra la
documentación oficial de Salesforce o `rlm-skill` que no existe un equivalente estándar** — nunca
por comodidad ni por suposición. Si esa verificación todavía no se ha hecho, el componente se deja
como `Estándar RLM`/`Estándar SF` en modo exploratorio, y la ambigüedad se documenta en la
sección 7 (Supuestos y preguntas abiertas) en vez de decidirla sobre la marcha.

Esto existe para que quien ejecute la Fase 3 sepa, de un vistazo y sin tener que inferirlo de la
especificación, qué puede usar tal cual y qué tiene que construir desde cero.

## Cómo probarlo

### 1. Validador sobre el ejemplo incluido (sin tocar ninguna org)

```bash
cd revenue-cloud-poc
python3 scripts/validate_manifest_poc.py assets/ejemplo-MANIFIESTO-POC.md
# → debe terminar en "OK" (0 errores)
python3 scripts/validate_manifest_poc.py assets/ejemplo-MANIFIESTO-POC.md --gate
# → también "OK": el ejemplo ya está "Estado de revisión: APROBADO"
```

### 2. Caso real de referencia (Prosegur Alarms, POC "penalización por baja anticipada")

Incluido en `ejemplos/poc-prosegur-cpq/`. Ya ejecutado una vez como prueba de extremo a extremo de
esta skill (FASE 0 → FASE 1 → FASE 2), sin FASE 3 por no haber org conectada en esa sesión. Sirve
como referencia de qué debe salir:

```bash
python3 scripts/validate_manifest_poc.py ejemplos/poc-prosegur-cpq/MANIFIESTO-POC.md --gate
```

Salida esperada (resumen):
```
Estado: APROBADO · Necesidades 1 · Hipótesis 1 · Pasos 3 · Componentes 7 ·
IA 5 (71%) · IA+Revisión 1 · Persona 1 · 🟢 3 · 🔵 4 · 🟠 0 ·
Estándar SF 3 · Estándar RLM 3 · Custom object 0 · N/A 1
OK
```

Puntos a verificar al reproducirlo:
- `MANIFIESTO-NECESIDADES.md` separa las 25 necesidades reales del RFQ (hoja "CPQ") de las 178
  filas de la hoja "Aspectos Generales" (esas son una respuesta a RFP, no necesidades de negocio
  — quedan explícitamente fuera en la sección 5 del manifiesto de necesidades).
- La incertidumbre elegida (NEC-17, penalización por baja anticipada) está marcada 🔴 porque falta
  la fórmula de cálculo real del cliente — el manifiesto la sustituye por un supuesto explícito
  (50% del valor restante) y lo marca como tal en la sección 7, no como dato confirmado.
- Ningún componente quedó como `Custom object`: la hipótesis se diseñó para probarse solo con
  mecanismos declarativos (Price Rules/Decision Tables), sin Apex, tal como pide la cabecera
  `Restricciones del SE`.

### 3. Probar la generación desde un scan sintético (sin CPQ Scout real)

Incluido `sample-scan.json` en la raíz del paquete (ver más abajo). Para probar `scan_to_poc.py`
sin un scan real:

```bash
python3 scripts/scan_to_poc.py ../sample-scan.json --cliente "Cliente de prueba" \
    --out ejemplos/poc-prueba-scan/MANIFIESTO-NECESIDADES.md
python3 scripts/scan_to_poc.py ../sample-scan.json --cliente "Cliente de prueba" \
    --modalidad poc --out ejemplos/poc-prueba-scan/MANIFIESTO-POC.md
```
El segundo comando genera un **pre-borrador**: no pasará `validate_manifest_poc.py` hasta
completar a mano las secciones 3-8 (componentes, datos, orden, supuestos).

### 4. Prueba conversacional completa (Claude Code o Claude Desktop/Projects)

La forma más realista de probar la skill completa es dentro de una sesión de Claude con esta
skill cargada:

1. Pega o adjunta un documento de necesidades (o un brief escrito a mano).
2. Pide explícitamente activar `revenue-cloud-poc` si no se dispara solo.
3. Sigue el flujo: revisa el `MANIFIESTO-NECESIDADES.md`, confirma modalidad, revisa el
   `MANIFIESTO-POC.md`, apruébalo.
4. Si hay una org conectada (Claude Code + `sf` CLI, o un conector Salesforce autorizado), pide
   la Fase 3; si no, confirma que el agente se detiene en "PREPARADA, NO EJECUTADA" y no inventa
   resultados de construcción ni de hipótesis.

## Gate de ejecución real

Dos capas, no solo una:

1. **La skill misma**: nunca invoca una escritura real en Salesforce (`sf` CLI, o los endpoints
   de CPQ Scout) sin que el `MANIFIESTO-POC.md` correspondiente tenga
   `Estado de revisión: APROBADO`.
2. **CPQ Scout** (si se usa como motor de ejecución): los endpoints `/api/migration/accelerate` y
   `/api/migration/accelerate/batch/execute` exigen un parámetro `manifest_path`, abren ese
   fichero y responden `403` si no existe o no contiene el marcador `Estado de revisión:
   APROBADO`. Esto se probó de forma aislada (no contra un `uvicorn` corriendo ni una org real) —
   si vas a depender de este gate en producción, verifícalo una vez contra un servidor real antes
   de confiar en él sin más.

## Limitaciones conocidas

- El validador solo acepta `Origen` de una `NEC-n` como `Brief` o `Supuesto`; un manifiesto
  generado desde un scan usa `Scan CPQ Scout`, lo que produce un `AVISO` (no bloqueante) en vez de
  pasar limpio. Pendiente de ajustar si se usa `scan_to_poc.py` con frecuencia.
- `scan_to_poc.py --modalidad poc` solo genera un pre-borrador (secciones 1-2); las secciones 3-8
  siempre requieren completarse a mano antes de validar.
- El gate de CPQ Scout (`manifest_path` + `require_approved_manifest`) no se ha probado todavía
  contra un servidor real ni una org real.

## Entregables por fase

| Fichero | Fase | Para quién |
|---|---|---|
| `MANIFIESTO-NECESIDADES.md` | 0 | El SE/cliente: confirma modalidad antes de seguir |
| `MANIFIESTO-POC.md` | 1 | El SE (revisión) y quien ejecute la Fase 3 |
| `datos/seed-spec.json`, `datos/HISTORIA-DATOS.md` | 1 | Carga y pruebas |
| `INFORME-VIABILIDAD.md` | 3 | El SE y el cliente técnico: resultado de cada hipótesis con evidencias |
