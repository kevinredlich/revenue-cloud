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
  explícitamente una POC en vez de una demo.
---

# Revenue Cloud — del brief/incertidumbre a la POC

Esta skill **extiende** `nespon-brief-to-demo`: una POC responde **"¿es viable este comportamiento y
bajo qué condiciones?"**, no "¿cómo gusta esto al cliente?". Antes de usarla, ten cargadas:

- `nespon-brief-to-demo` — de ahí reutilizas tal cual: `references/ia-vs-persona.md` (reparto),
  `references/impacto.md` (niveles 🟢/🔵/🟠), `references/datos-demo.md` y `scripts/fill_data.py`
  (datos de prueba).
- `nespon-demo-builder` — playbook `references/nubes/revenue-cloud.md` (objetos y escenas
  canónicas de RLM) y, para la Fase 3 real, `references/ejecucion-en-org.md`.
- **`rlm-skill`** — fuente técnica autoritativa de RLM (modelo de datos, APIs, pricing, decision
  tables, expression sets, constraint models...). **Úsala en vez del link genérico de Salesforce
  Help** para verificar cualquier afirmación técnica de una hipótesis o un componente: antes de dar
  una hipótesis por viable en el diseño, consulta el sub-skill que toque (p. ej.
  `subskills/revenue-cloud-data-model/domains/pricing.md` para dudas de modelo de datos de pricing,
  `subskills/pricing-wiring/guide.md` para cómo se conectan recipes/procedure plans, o
  `references/apis/*.md` para endpoints). Si `rlm-skill` no está instalada en el proyecto, cae al
  link de `nespon-demo-builder` y marca la afirmación como `PENDIENTE DE VALIDACIÓN`.

## FASE 0 — Intake unificado (antes de decidir DEMO / POC / Migración)
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
- **DEMO** → `nespon-brief-to-demo`, usando `MANIFIESTO-NECESIDADES.md` como brief de entrada (las
  `NEC-n` ya clasificadas sustituyen la lectura manual del documento original).
- **POC o Migración** (migración = POC cuya incertidumbre viene de un scan, no un workflow
  distinto) → continúa con la FASE 1 de esta misma skill, reutilizando las `NEC-n` ya confirmadas
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
manifiesto aprobado", sea el mecanismo `sf CLI` o la propia API de CPQ Scout. CPQ Scout ahora exige
`manifest_path` en esas dos llamadas cuando escribe de verdad y rechaza con 403 si el fichero no
existe o no contiene `Estado de revisión: APROBADO` — pero quien use esta skill sigue
responsabilizándose de pasar la ruta correcta; si no puede verificar que el gate está conectado,
lo dice explícitamente en vez de asumirlo.

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
Corrige los errores. Deja `Estado de revisión: BORRADOR` y presenta un resumen corto: hipótesis,
pasos, % de componentes IA, tareas de persona, supuestos. **Para aquí. No construyas nada.**

Formato exacto: `references/manifiesto-poc.md`. Ejemplo: `assets/ejemplo-MANIFIESTO-POC.md`.

## FASE 2 — Revisión (el SE)
Igual que en `nespon-brief-to-demo`: el SE revisa, puede pedir cambios (nueva versión con registro
de cambios), y aprueba poniendo `Estado de revisión: APROBADO` con su nombre, o confirmándolo en la
conversación.

## FASE 3 — Ejecución del experimento (solo con org y sf CLI — Claude Code / Vibes)

1. **Puerta:** `validate_manifest_poc.py --gate`; sin `APROBADO` no se toca la org.
2. Pre-flight de `nespon-demo-builder` (org confirmada, licencias de Revenue Cloud/RLM).
3. Construye los componentes en el orden del manifiesto (IA / IA+Revisión / Persona, igual que
   `construccion.md` de `nespon-brief-to-demo`).
4. Carga los datos de prueba (`fill_data.py` → `build_seed.py` → `sf data import tree`).
5. **Ejecuta cada paso del experimento** y registra el resultado real observado frente al esperado,
   con su evidencia (consulta, captura, log).
6. Clasifica cada hipótesis (ver abajo) y genera `INFORME-VIABILIDAD.md`
   (`references/informe-viabilidad.md`).

Si no hay org conectada, la Fase 3 no se ejecuta: entrega el diseño con estado **PREPARADA, NO
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
| `references/informe-viabilidad.md` | Fase 3: formato del informe de resultado |
| (de `nespon-brief-to-demo`) `references/ia-vs-persona.md`, `impacto.md`, `datos-demo.md` | 1.4–1.5 |
| (de `nespon-demo-builder`) `references/nubes/revenue-cloud.md`, `ejecucion-en-org.md` | diseño y Fase 3 |
| (de `rlm-skill`, si está instalada) `SKILL.md` (enrutador a 13 sub-skills + 1.131 artículos de Help) | verificar cualquier hipótesis o componente técnico antes de darlo por viable |

| Script | Para qué |
|---|---|
| `scripts/scan_to_poc.py` | Fase 0 (`--modalidad intake`, por defecto) y Fase 1 con origen scan (`--modalidad poc`) |
| `scripts/validate_manifest_poc.py` | Valida `MANIFIESTO-POC.md` antes de entregarlo y antes de ejecutar |
