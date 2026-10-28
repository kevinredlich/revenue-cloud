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
`rlm-skill` es **obligatoria para diseñar**: es la fuente técnica autoritativa de Revenue Cloud
(modelo de datos, pricing, decision tables, expression sets, nombres y valores de API) y se
consulta SIEMPRE primero (Regla cero de `references/reglas-modelado-catalogo-rlm.md`). Cada
objeto, campo y valor de API del manifiesto se registra en la tabla 3.1 con su clase
(`DOC` / `DERIVADO` / `SUPUESTO`) y su referencia. Si `rlm-skill` no está disponible, el manifiesto
lo declara en `Fuentes consultadas` y todo lo técnico queda como `SUPUESTO`: no es un diseño validado.
La org valida después (describe, consultas de pre-flight), pero no sustituye a la documentación.

Hace falta tener cargadas (en el mismo proyecto/repo de skills): `nespon-brief-to-demo`,
`nespon-demo-builder` y `rlm-skill`.

## Estructura de la skill

```
revenue-cloud-poc/
├── SKILL.md                                  # instrucciones de la skill (todas las fases)
├── references/
│   ├── manifiesto-necesidades.md             # formato exacto de MANIFIESTO-NECESIDADES.md (Fase 0)
│   ├── manifiesto-poc.md                     # formato exacto de MANIFIESTO-POC.md (Fase 1)
│   ├── reglas-modelado-catalogo-rlm.md       # Regla cero (rlm-skill), R1-R14, checklist y valores de API
│   ├── informe-viabilidad.md                 # formato del informe de resultado (Fase 3)
│   └── api-correcciones.json                 # valores de API incorrectos conocidos (los lee el validador)
├── assets/
│   ├── ejemplo-MANIFIESTO-POC.md             # ejemplo de diseño en BORRADOR (Bodegas Altiplano)
│   ├── ejemplo-MANIFIESTO-POC-APROBADO.md    # el mismo, aprobado con --approve (pasa --gate)
│   └── ejemplo-INFORME-VIABILIDAD.md
├── ejemplos/
│   ├── poc-prueba-scan/                      # salida de scan_to_poc.py sobre ../sample-scan.json
│   └── legacy-v1/poc-prosegur-cpq/           # caso real anterior al endurecimiento (NO pasa --gate)
├── scripts/
│   ├── scan_to_poc.py                        # genera manifiestos a partir de un scan de CPQ Scout
│   ├── validate_manifest_poc.py              # valida, aprueba (--approve) y abre la puerta (--gate)
│   ├── compare_results.py                    # compara casos esperados con observados (Fase 3)
│   └── check_deps.py                         # comprueba Python y Salesforce CLI
└── tests/                                    # python3 -m unittest discover -s tests -t .
```

Requiere Python 3.9 o superior (sin dependencias de terceros: solo biblioteca estándar). Para la
Fase 3 real sobre una org hace falta además `sf` (Salesforce CLI) con la org ya autenticada;
`python3 scripts/check_deps.py` lo comprueba.

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
"Registro de cambios") y aprueba con el validador, que exige un manifiesto sin errores en modo
estricto y escribe la cabecera por él:

```bash
python3 scripts/validate_manifest_poc.py poc-<cliente>/MANIFIESTO-POC.md --approve "Nombre Apellido"
```

```
**Estado de revisión:** APROBADO
**Revisado por:** Nombre Apellido · **Fecha de aprobación:** 2026-10-28
**Hash de aprobación:** sha256:<64 hex>
```

El hash cubre todo el contenido salvo esas tres líneas: si alguien edita el manifiesto después,
`--gate` falla hasta que se vuelva a aprobar. Editar a mano `APROBADO` ya no abre la puerta. El
hash detecta modificaciones; no prueba la identidad de quien aprobó.

### FASE 3 — Ejecución del experimento (solo con una org real conectada)

1. **Puerta obligatoria** antes de tocar nada:
   ```bash
   python3 scripts/validate_manifest_poc.py poc-<cliente>/MANIFIESTO-POC.md --gate --org <alias>
   ```
   Sin `APROBADO` con hash válido, o si `Org objetivo` no declara sandbox/scratch/SDO ni contiene el
   alias, el validador falla y **no se construye nada en la org**. Es una comprobación de lo que el
   manifiesto declara, no una verificación contra la org real.
2. Pre-flight: confirmar la org y las licencias de Revenue Cloud/Asset Lifecycle Management.
3. Construir los componentes en el orden de la sección 6 del manifiesto, respetando el reparto
   IA / IA+Revisión / Persona.
4. Cargar los datos de prueba (`fill_data.py` → `sf data import tree`, o el flujo equivalente).
5. Ejecutar cada paso del experimento y registrar el resultado real observado frente al esperado,
   con su evidencia (consulta SOQL, captura, log). Los `CASO-n` se exportan con `--export-cases` y
   `scripts/compare_results.py` los compara con lo observado.
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

### 1. Validador sobre los ejemplos incluidos (sin tocar ninguna org)

```bash
cd revenue-cloud-poc
python3 scripts/validate_manifest_poc.py assets/ejemplo-MANIFIESTO-POC.md
# → "OK" (0 errores), BORRADOR
python3 scripts/validate_manifest_poc.py assets/ejemplo-MANIFIESTO-POC-APROBADO.md --gate
# → "OK": APROBADO, hash válido y casos de prueba con valor esperado
python3 scripts/validate_manifest_poc.py assets/ejemplo-MANIFIESTO-POC.md --gate
# → falla: el borrador no está aprobado
python3 -m unittest discover -s tests -t .
```

### 2. Caso real anterior (Prosegur Alarms) — `ejemplos/legacy-v1/`

Se conserva sin tocar como muestra de un manifiesto de la primera versión del formato. **No pasa
el validador actual** (no tiene `Fuentes consultadas`, ni las tablas 3.1 y 3.2, ni hash, y conserva
un marcador `<completar>`). Sirve para ver qué falla un manifiesto sin evidencia técnica, no como
modelo a seguir:

```bash
python3 scripts/validate_manifest_poc.py ejemplos/legacy-v1/poc-prosegur-cpq/MANIFIESTO-POC.md --gate
```

Puntos de interés de su contenido (no de su validación):
- Separa las 25 necesidades reales del RFQ de las 178 filas de "Aspectos Generales" (respuesta a
  RFP, no necesidades de negocio).
- La incertidumbre (NEC-17, penalización por baja anticipada) está en 🔴 por falta de fórmula
  real del cliente; el manifiesto la sustituye por un supuesto explícito (50% del valor restante).
- Ningún componente es `Custom object`: la hipótesis se diseñó solo con mecanismos declarativos.

### 3. Probar la generación desde un scan sintético (sin CPQ Scout real)

Incluido `sample-scan.json` en la raíz del repositorio. Para probar `scan_to_poc.py` sin un scan
real (no sobrescribe un fichero existente salvo `--force`):

```bash
python3 scripts/scan_to_poc.py ../sample-scan.json --cliente "Cliente de prueba" \
    --out ejemplos/poc-prueba-scan/MANIFIESTO-NECESIDADES.md
python3 scripts/scan_to_poc.py ../sample-scan.json --cliente "Cliente de prueba" \
    --modalidad poc --out ejemplos/poc-prueba-scan/MANIFIESTO-POC.md
```
El segundo comando genera un **pre-borrador**: no pasará `validate_manifest_poc.py` hasta
completar a mano las secciones 3-8 (componentes, tablas 3.1–3.3 de verificación de API, viabilidad y decisiones de diseño, datos, orden, supuestos). Los `NEC-n` del pre-borrador coinciden con los del manifiesto de necesidades generado del mismo scan, y cada `HIP-n` cita su `NEC-n`.

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
2. **CPQ Scout** (si se usa como motor de ejecución): según su documentación, los endpoints
   `/api/migration/accelerate` y `/api/migration/accelerate/batch/execute` exigen `manifest_path` y
   responden `403` si el fichero no existe o no contiene `Estado de revisión: APROBADO`. Ese control
   no se ha verificado desde este repositorio y solo mira el texto, no el hash: ejecuta siempre
   antes `validate_manifest_poc.py --gate`, y verifica el gate contra un servidor real antes de
   depender de él.

## Limitaciones conocidas

- `scan_to_poc.py --modalidad poc` solo genera un pre-borrador (secciones 1-2 y plantillas); las
  secciones 3-8 siempre requieren completarse a mano antes de validar.
- El hash de aprobación detecta ediciones posteriores pero no autentica a quien aprueba; para eso
  haría falta una firma externa (por ejemplo, un commit firmado o la aprobación de un PR).
- `--org` comprueba lo que el manifiesto declara; no consulta la org. La verificación real
  (`sf org display`, pre-vuelo con `describe`) la hace quien ejecuta la Fase 3.
- El gate de CPQ Scout no se ha probado contra un servidor real ni una org real.
- Las reglas de modelado (`references/reglas-modelado-catalogo-rlm.md`) mezclan reglas y notas de
  post-mortem; conviene separarlas en el futuro.

## Entregables por fase

| Fichero | Fase | Para quién |
|---|---|---|
| `MANIFIESTO-NECESIDADES.md` | 0 | El SE/cliente: confirma modalidad antes de seguir |
| `MANIFIESTO-POC.md` | 1 | El SE (revisión) y quien ejecute la Fase 3 |
| `datos/seed-spec.json`, `datos/HISTORIA-DATOS.md` | 1 | Carga y pruebas |
| `INFORME-VIABILIDAD.md` | 3 | El SE y el cliente técnico: resultado de cada hipótesis con evidencias |
