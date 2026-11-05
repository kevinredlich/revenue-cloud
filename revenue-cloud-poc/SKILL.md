---
name: revenue-cloud-poc
description: >
  Convierte el brief o la duda técnica de un cliente sobre Salesforce Revenue Cloud en una POC:
  manifiesto de desarrollo que separa lo que construye la IA de lo que debe hacer una persona, y un
  informe de viabilidad que concluye si la hipótesis queda validada, con evidencias. Reutiliza el
  método de `nespon-brief-to-demo` (reparto IA/IA+Revisión/Persona, niveles 🟢/🔵/🟠, datos de prueba
  ficticios) pero sustituye escenas-y-wow por pasos de experimento ligados a una hipótesis, y el
  pitch por un informe de viabilidad. Úsala SIEMPRE que el usuario quiera comprobar si algo "se
  puede hacer" en Revenue Cloud, validar una hipótesis técnica o de pricing/configurador, o pida
  explícitamente una POC en vez de una demo. También cuando se pida diseñar o configurar una demo
  de Revenue Cloud (catálogo, atributos, precios, bundles): el diseño técnico pasa por las mismas
  reglas (rlm-skill obligatoria, viabilidad estándar vs custom real, mejor diseño).
---

# Revenue Cloud — del brief/incertidumbre a la POC

Esta skill **extiende** `nespon-brief-to-demo`: una POC responde **"¿es viable este comportamiento y
bajo qué condiciones?"**, no "¿cómo gusta esto al cliente?". Antes de usarla, ten cargadas:

- `nespon-brief-to-demo` — de ahí reutilizas tal cual: `references/ia-vs-persona.md` (reparto),
  `references/impacto.md` (niveles 🟢/🔵/🟠), `references/datos-demo.md` y `scripts/fill_data.py`
  (datos de prueba).
- `nespon-demo-builder` — playbook `references/nubes/revenue-cloud.md` (objetos y escenas
  canónicas de RLM) y, para la Fase 3 real, `references/ejecucion-en-org.md`.
- **`rlm-skill` — OBLIGATORIA para diseñar.** Es la fuente técnica autoritativa de RLM (modelo de
  datos, APIs, pricing, decision tables, expression sets, constraint models...). **Para diseñar
  cualquier solución técnica o funcional de Revenue Cloud se consulta SIEMPRE primero**, en este
  orden: (1) `SKILL.md` de `rlm-skill` y elegir sub-skill; (2) su `guide.md` y los ficheros que
  cite (p. ej. `subskills/revenue-cloud-data-model/domains/pricing.md`,
  `subskills/pricing-wiring/guide.md`, `references/apis/*.md`); (3) el artículo de Help 264 de cada
  objeto o feature que intervenga; (4) citar la fuente de cada decisión en la tabla 3.1 del
  manifiesto. No se diseña de memoria ni con el link genérico de Salesforce Help. Si `rlm-skill` no
  está disponible en la sesión, se dice al principio, el campo `Fuentes consultadas` del manifiesto
  indica "no disponible" y **todo lo técnico se marca `SUPUESTO`**: el diseño no se presenta como
  validado.
- **`references/reglas-modelado-catalogo-rlm.md`** — reglas obligatorias de modelado (Regla cero,
  R1–R14), checklist de pre-entrega y correcciones conocidas de nombres y valores de API. Léelo antes
  de diseñar y antes de entregar.

## FASE 0 — Intake unificado (antes de decidir DEMO / POC / Migración)
> La Fase 0 y el enrutado los orquesta la skill `revenue-intake` (`flujo-revenue/`): genera
> `BRIEF-CLIENTE.md` y `MANIFIESTO-NECESIDADES.md`, espera la decisión del SE y deriva al agente de demos
> o al de POC. **En ambos caminos `rlm-skill` es obligatoria y `rlm-verifier` revisa el resultado.**

**Esto va primero, siempre, venga el origen de un brief escrito a mano o de un scan de CPQ Scout.**
No se decide DEMO ni POC mirando solo el documento del cliente: primero se genera un
`MANIFIESTO-NECESIDADES.md` con las necesidades clasificadas (`NEC-n` + semáforo 🟢/🟡/🔴) y una
modalidad **propuesta** (no decidida unilateralmente), y solo después de que el SE o el cliente
confirme esa modalidad se genera el manifiesto definitivo.

- **Origen = brief escrito a mano:** el agente extrae las `NEC-n` directamente del documento
  (contexto, necesidades, reglas, restricciones — igual que la Fase 1 de `nespon-brief-to-demo`,
  pero clasificando cada necesidad con el semáforo antes de elegir modalidad).
- **Origen = scan de CPQ Scout** (herramienta read-only que detecta uso de Salesforce CPQ/SBQQ y
  calcula un complexity score): corre
  ```bash
  python3 <skill-dir>/scripts/scan_to_poc.py scan-result.json --cliente "<cliente>" \
      --out poc-<slug>/MANIFIESTO-NECESIDADES.md
  ```
  Cada fila del inventario se convierte en `NEC-n` con semáforo (🟢 `risk=low`+`Directa`, 🟡
  `risk=medium` o `Rediseño`, 🔴 `risk=high` o `Reescritura`), y el script propone modalidad
  (DEMO si todo es 🟢, POC/migración si hay 🟡/🔴) con justificación.

**Modalidad propuesta vs. confirmada:** la propuesta (sección 3 del manifiesto de necesidades) es
una recomendación técnica, nunca una aprobación del cliente. Se para ahí y se presenta un resumen
corto (semáforo, modalidad propuesta, preguntas de refinamiento). Solo tras la confirmación
(sección 4, o en conversación) se activa el workflow correspondiente:
- **DEMO** → **se delega en el agente `demo-brief-architect`** (`nespon-brief-agent/`, con sus skills
  `nespon-brief-to-demo`, `nespon-demo-builder` y `rlm-skill`), pasándole `BRIEF-CLIENTE.md` y
  `MANIFIESTO-NECESIDADES.md` y la modalidad confirmada. Esta skill no diseña ni construye la demo. Lo
  orquesta la skill `revenue-intake` (`flujo-revenue/`), que además pasa el resultado por `rlm-verifier`.
  Si el agente no está disponible, se dice y se entrega el brief; no se improvisa una demo aquí.
- **POC o Migración** (migración = POC cuya incertidumbre viene de un scan, no un workflow
  distinto) → `revenue-intake` lanza el agente `poc-architect`, que continúa con la FASE 1 de esta misma skill, reutilizando las `NEC-n` ya confirmadas
  en vez de re-derivarlas desde cero. Con origen scan, vuelve a correr `scan_to_poc.py` con
  `--modalidad poc` sobre el mismo JSON para obtener el pre-borrador de `MANIFIESTO-POC.md` con las
  hipótesis (`HIP-n`) ya planteadas.

Formato exacto del manifiesto de necesidades: `references/manifiesto-necesidades.md`.

## Cuándo POC y no DEMO
Señal de que la modalidad confirmada es POC (y no DEMO): hay `NEC-n` en 🟡/🔴, o el cliente pide
explícitamente comprobar algo — "¿se puede calcular el precio con...?", "¿el configurador
soporta...?", "necesitamos comprobar si...", una dependencia técnica dudosa, un modelo de pricing
no estándar. Si todo es 🟢 y el objetivo es que el cliente vea el recorrido, es DEMO.

## Línea roja de ejecución real (válida para POC y para Migración)
El endpoint `/api/migration/accelerate` (y `/api/migration/accelerate/batch/execute`) de CPQ Scout
escriben en una org real (no una org de demo ficticia). Nunca se invocan como parte de esta skill
sin que el `MANIFIESTO-POC.md` correspondiente esté `APROBADO` por el SE — el gate de
`nespon-brief-to-demo` (pensado para orgs de demo) se extiende aquí a "ninguna escritura real sin
manifiesto aprobado", sea el mecanismo `sf CLI` o la propia API de CPQ Scout. Según la documentación de
CPQ Scout, esas dos llamadas exigen `manifest_path` y rechazan con 403 si el fichero no existe o no
contiene `Estado de revisión: APROBADO`; ese control no se ha verificado desde este repositorio y
solo mira el texto, no el hash. Quien use esta skill ejecuta antes `validate_manifest_poc.py --gate`
y, si no puede verificar que el gate de CPQ Scout está conectado, lo dice explícitamente en vez de
asumirlo.

## FASE 1 — Diseño (no toca la org)

### 1.1 Identificar la incertidumbre
Qué aspecto concreto hay que comprobar (`references/brief.md` de `nespon-brief-to-demo` para extraer
el resto del contexto: cliente, sector, zona fiscal, restricciones).

### 1.2 Formular hipótesis (`HIP-n`)
Una frase verificable por hipótesis. "El mecanismo de pricing estándar permite calcular el precio
usando características del producto y coste de instalación." Nunca la des por probada porque la
documentación mencione una capacidad relacionada.

### 1.3 Diseñar los pasos del experimento (`EXP-n`)
Cada paso liga a ≥1 `HIP`, con condición de entrada, acción y **resultado esperado observable**
(no "funciona correctamente"). Excluye expresamente: interfaces comerciales completas innecesarias,
migraciones de datos completas, todo lo que no sirva para comprobar la hipótesis.

### 1.4 Componentes y reparto
Antes de especificar un componente, aplica la Regla cero de `references/reglas-modelado-catalogo-rlm.md`
(consultar `rlm-skill`). Cada objeto, campo y valor de picklist de la especificación debe ser el nombre
y valor de API reales (nunca la etiqueta de la UI ni un nombre inventado) y queda registrado en la
tabla **3.1** del manifiesto con su clase (`DOC` / `DERIVADO` / `SUPUESTO`) y su referencia.
**Nunca se entrega un diseño que no calce en Revenue Cloud (R12):** cada requisito se clasifica en la
tabla **3.2** como `ESTÁNDAR`, `ESTÁNDAR A VALIDAR` o `CUSTOM REAL`, tras leer el artículo de Help y
sus límites. Si no se puede de forma estándar, se ofrece un diseño custom real (con piezas reales de
la plataforma) junto a la opción estándar más cercana; no se inventan objetos, campos ni valores.
**El objetivo es el mejor diseño real, no el más corto (R13):** cada decisión no trivial compara al
menos dos alternativas y queda en la tabla **3.3** con la elegida, las descartadas y el motivo
(encaje con RLM, jerarquía estándar > configuración > declarativo > código > objeto propio,
coherencia, mantenimiento, esfuerzo). Un custom bien justificado es correcto; un custom
injustificado o un estándar forzado que no funciona no lo son.

Igual que en `nespon-brief-to-demo`: tabla de componentes con nivel 🟢/🔵/🟠 y responsable
IA / IA+Revisión / Persona (`references/ia-vs-persona.md`), tareas de persona con ruta, valores,
comprobación y qué desbloquean.

### 1.5 Datos de prueba
Sigue `references/datos-demo.md` de `nespon-brief-to-demo`, pero el foco es que cada caso de prueba
tenga los datos exactos que el experimento necesita, no "contar una historia". Mismo generador
(`fill_data.py`), mismas reglas (ficticios, `@example.com`, fechas relativas).

### 1.6 Validar y entregar para revisión
```bash
python3 <skill-dir>/scripts/validate_manifest_poc.py poc-<slug>/MANIFIESTO-POC.md
```
Corrige los errores. Los AVISOS de calidad (sin pre-vuelo, sin casos de prueba con valor esperado,
marcadores `<completar>`, fuente externa sin confirmar) pasan a ERROR en `--strict`, `--gate` y
`--approve`: se corrigen antes de pedir la aprobación. Deja `Estado de revisión: BORRADOR` y presenta
un resumen corto: hipótesis, pasos, % de componentes IA, tareas de persona, supuestos. **Para aquí.
No construyas nada.**

Los valores de API que ya se han escrito mal alguna vez (etiqueta de UI en vez de valor de API)
están en `references/api-correcciones.json`; el validador los rechaza si aparecen entre `backticks`.

Formato exacto: `references/manifiesto-poc.md`. Ejemplo: `assets/ejemplo-MANIFIESTO-POC.md`.

## FASE 2 — Revisión (el SE)
Igual que en `nespon-brief-to-demo`: el SE revisa, puede pedir cambios (nueva versión con registro
de cambios), y aprueba **solo mediante el validador**, que comprueba el manifiesto en modo estricto y escribe estado,
nombre, fecha y un hash sha256 del contenido:
```bash
python3 <skill-dir>/scripts/validate_manifest_poc.py poc-<slug>/MANIFIESTO-POC.md --approve "Nombre Apellido"
```
Si el SE aprueba en la conversación, el agente ejecuta ese comando con el nombre que el SE da; nunca
inventa el nombre ni edita a mano la línea `Estado de revisión`. Cualquier cambio posterior al
contenido invalida el hash y el manifiesto vuelve a requerir `--approve`. El hash detecta ediciones,
no prueba quién aprobó.

## FASE 3 — Ejecución del experimento (solo con org y sf CLI — Claude Code / Vibes)

1. **Puerta:** `validate_manifest_poc.py --gate --org <alias>`; sin `APROBADO`, sin hash válido o
   con una `Org objetivo` que no sea sandbox/scratch/SDO y no coincida con el alias, no se toca la
   org. Antes, `scripts/check_deps.py --require-sf` confirma que el entorno puede ejecutar.
2. Pre-flight de `nespon-demo-builder` (org confirmada, licencias de Revenue Cloud/RLM) y
   checklist de pre-entrega de `references/reglas-modelado-catalogo-rlm.md`: la org valida lo
   diseñado (describe, consultas de pre-flight) pero no sustituye a la documentación; cada
   corrección que la org obligue a hacer se anota en la sección 4 de ese documento.
   Si un pre-flight falla o la org contradice el diseño, **se para y se corrige el diseño**
   (documento y tablas 3.1–3.3); no se parchea la org para que "cuadre".
3. Construye los componentes en el orden del manifiesto (IA / IA+Revisión / Persona, igual que
   `construccion.md` de `nespon-brief-to-demo`).
4. Carga los datos de prueba (`fill_data.py` → `build_seed.py` → `sf data import tree`).
   Tras cargar, **prueba funcional con valores esperados** para cada regla de precio, atributo o
   bundle (por ejemplo: simular el pricing o crear una cotización y comparar el precio exacto con el
   calculado en el diseño). Una carga sin errores no prueba que el motor aplique lo cargado.
5. **Ejecuta cada paso del experimento** y registra el resultado real observado frente al esperado,
   con su evidencia (consulta, captura, log). Los casos `CASO-n` se exportan con
   `validate_manifest_poc.py --export-cases casos.json`, los observados se anotan en un JSON
   `{"CASO-1": "…"}` y `scripts/compare_results.py casos.json resultados.json` da la comparación
   exacta (un caso sin ejecutar nunca cuenta como bueno).
6. Clasifica cada hipótesis (ver abajo) y genera `INFORME-VIABILIDAD.md`
   (`references/informe-viabilidad.md`).

Si no hay org conectada, o `sf` no está instalado, la Fase 3 no se ejecuta: entrega el diseño con estado **PREPARADA, NO
EJECUTADA** y nunca afirmes un resultado de hipótesis sin haberla ejecutado.

## Resultado de cada hipótesis
- 🟢 **VALIDADA** — evidencia suficiente de cumplimiento.
- 🟡 **PARCIALMENTE VALIDADA** — se cumple con limitaciones documentadas.
- 🔴 **NO VALIDADA** — evidencia de incumplimiento.
- **NO EJECUTADA** — no se ha realizado el experimento (p. ej. sin org).
- **NO CONCLUYENTE** — evidencia insuficiente para decidir.

Nunca clasifiques como validada una hipótesis por el mero hecho de haber generado documentación o
código. Este resultado es distinto del nivel 🟢/🔵/🟠 de los componentes (eso mide cuánto es custom,
no si la hipótesis se cumple).

## Ficheros que genera (en `poc-<cliente-o-tema-slug>/`)
| Fichero | Fase | Para quién |
|---|---|---|
| `MANIFIESTO-NECESIDADES.md` | 0 | El SE/cliente: confirma modalidad antes de seguir |
| `MANIFIESTO-POC.md` | 1 | El SE (revisión) y quien ejecute la Fase 3 |
| `datos/seed-spec.json`, `datos/HISTORIA-DATOS.md` | 1 | Carga y pruebas |
| `INFORME-VIABILIDAD.md` | 3 | El SE y el cliente técnico: resultado de cada hipótesis con evidencias |

## Referencias
| Archivo | Cuándo |
|---|---|
| `references/manifiesto-necesidades.md` | Fase 0: formato exacto del manifiesto de intake |
| `references/manifiesto-poc.md` | 1.2–1.6: formato exacto del manifiesto de POC |
| `references/reglas-modelado-catalogo-rlm.md` | Siempre antes de diseñar y de entregar: Regla cero, R1–R14 (viabilidad estándar vs custom real), checklist, valores de API |
| `references/informe-viabilidad.md` | Fase 3: formato del informe de resultado |
| `references/api-correcciones.json` | Valores de API incorrectos conocidos que el validador rechaza |
| (de `nespon-brief-to-demo`) `references/ia-vs-persona.md`, `impacto.md`, `datos-demo.md` | 1.4–1.5 |
| (de `nespon-demo-builder`) `references/nubes/revenue-cloud.md`, `ejecucion-en-org.md` | diseño y Fase 3 |
| (de `rlm-skill`, obligatoria) `SKILL.md` (enrutador a 13 sub-skills + 1.131 artículos de Help) | diseñar y verificar cualquier hipótesis o componente técnico antes de darlo por viable |

| Script | Para qué |
|---|---|
| `scripts/scan_to_poc.py` | Fase 0 (`--modalidad intake`, por defecto) y Fase 1 con origen scan (`--modalidad poc`) |
| `scripts/validate_manifest_poc.py` | Valida `MANIFIESTO-POC.md`; `--strict`, `--gate [--org]`, `--approve`, `--json`, `--export-cases` |
| `scripts/compare_results.py` | Fase 3: compara los `CASO-n` esperados con los observados |
| `scripts/check_deps.py` | Fase 3: comprueba Python y Salesforce CLI antes de ejecutar |
