# Formato del entregable

## Índice
1. Estructura general
2. Parte A — Backlog narrativo (plantillas)
3. Parte B — Configuration Manifest (tablas de esquema fijo)
4. Cierre: BUILD ORDER, SEED FILES, REHEARSAL & RESET, SUPUESTOS, CHANGELOG
5. Variante: prompt para el IDE
6. Ejemplo completo

El validador (`scripts/validate_backlog.py`) depende de estas convenciones: respeta encabezados,
prefijos de ID y columnas. Ejemplo completo y validado en `assets/ejemplo-backlog.md`: léelo una vez
para calibrar tono y densidad.

---

## 1. Estructura general

```
# DEMO BACKLOG — <Cliente> — <Nube ancla> [+ apoyo] — v<N>
(cabecera, restricciones fijas, skills usadas, mapa)
# PARTE A — BACKLOG NARRATIVO
## ÉPICA 1 — …
### HU-1.1 — …
# PARTE B — CONFIGURATION MANIFEST
### ORG — Org & Licenses
### SET — Setup & Features
… (solo las tablas que apliquen, en el orden de la sección 3)
## BUILD ORDER
## SEED FILES
## REHEARSAL & RESET
## SUPUESTOS
## CHANGELOG   (solo v2+)
```

Parte A en español de España. Parte B, Gherkin y todos los nombres técnicos en inglés, con nombres
reales de la plataforma. Sin duraciones, minutos ni tiempos por escena.

---

## 2. Parte A — Backlog narrativo

### Cabecera

```markdown
# DEMO BACKLOG — <Cliente> — <Nube ancla> + <apoyo> — v<N>

**Sector:** … · **Tamaño:** … · **Zona fiscal:** Península (IVA 21%)
**Protagonista:** <Nombre Apellido>, <rol>
**Audiencia negocio:** <roles> · **Audiencia técnica:** <roles>
**Nube ancla:** … · **Nubes de apoyo:** …
**Org objetivo:** <tipo de org> (ver ORG)
**Pitch:** <la promesa de la demo en una frase, en lenguaje del cliente>

**RESTRICCIONES FIJAS (del SE, no negociables en ninguna versión):**
- <literal del SE> · o "Ninguna indicada"

**Skills usadas:** nespon-demo-builder · <revenue-cloud-demo / salesforce-skill> — <para qué>

| Dolor del cliente | Épica | Audiencia | WOW |
|---|---|---|---|
| … | Épica 1 — … | Negocio | ⭐ … |

**WOW:** ⭐ <WOW 1 — dónde> · ⭐ <WOW 2 — dónde>
**Clasificación:** 🟢 n · 🔵 n · 🟠 n
```

### Épica (= acto)

```markdown
## ÉPICA <N> — <TÍTULO DEL ACTO>
**Dolor:** <concreto, con coste o riesgo si se conoce>
**Rol narrativo:** Problema | Giro | Resultado · **Audiencia principal:** Negocio | Técnica
```

### Historia de usuario (bloque compacto, siempre este formato)

```markdown
### HU-<N>.<M> — <título corto>
- **Historia:** Como <rol>, quiero <capacidad>, para <resultado de negocio>.
- **Dolor:** <dolor> · **WOW:** ⭐ <momento> | — · **Clasificación:** 🟢 | 🔵 | 🟠 — Justificación: <por qué no basta lo declarativo>
- **Done (Gherkin, EN):** Given <precondición con datos semilla> · When <acción> · Then <resultado observable>
- **Plan B:** <solo si la HU tiene WOW: qué enseñar si falla>
- **Config refs:** <IDs del manifiesto, p. ej. FLD-1, FLW-1, UI-2, DAT-3>
- **Depende de:** <HU-x.y | —>
```

La configuración nunca se describe en la historia; se referencia por ID.

---

## 3. Parte B — Configuration Manifest

Una tabla por tipo, en este orden, solo si aplica. Primera columna siempre `ID` con el prefijo del
tipo y numeración correlativa. Última columna `Class` con 🟢/🔵/🟠 (salvo `ORG`). Cada componente
aparece **una sola vez** en todo el manifiesto.

### ORG — Org & Licenses
```markdown
| ID | Item | Requirement | Status | Notes |
|----|------|-------------|--------|-------|
| ORG-1 | Org type | Developer Edition (empty) | Required | Locale es_ES, currency EUR, TZ Europe/Madrid |
| ORG-2 | License | Agentforce provisioned | Verify | Without it, drop Épica 3 |
```

### SET — Setup & Features
```markdown
| ID | Setup Area | Setting | Value | Class |
|----|-----------|---------|-------|-------|
| SET-1 | Forecasts Settings | Enable Forecasts; Forecast Type = Opportunity Revenue | On | 🟢 |
| SET-2 | User Interface | Enable "Set Audit Fields upon Record Creation" | On | 🟢 |
```

### OBJ — Objects (solo custom)
```markdown
| ID | API Name | Label | Sharing (OWD) | Purpose | Class |
|----|----------|-------|---------------|---------|-------|
```

### FLD — Fields
Tipos con parámetros, para crearlos literalmente: `Text(80)`, `TextArea`, `LongTextArea(32768)`,
`Picklist[v1;v2;v3]`, `MultiPicklist[v1;v2]`, `Number(18,0)`, `Currency(16,2)`, `Percent(3,0)`,
`Date`, `DateTime`, `Checkbox(default=false)`, `Email`, `Phone`, `URL`,
`Formula(Return=Text|Number|Currency|Percent|Checkbox|Date)`, `Lookup(Object)`,
`MasterDetail(Object)`, `RollupSummary(COUNT|SUM|MIN|MAX, Child.Field, filter)`.
```markdown
| ID | Object | API Name | Label | Type | Spec (values / formula / ref) | Req | Purpose | Class |
|----|--------|----------|-------|------|-------------------------------|-----|---------|-------|
```

### RT — Record Types (y valores de picklist por record type)
```markdown
| ID | Object | DeveloperName | Label | Picklist values / Page layout | Class |
|----|--------|---------------|-------|-------------------------------|-------|
```

### QUE — Queues & Groups
```markdown
| ID | Type | DeveloperName | Objects | Members | Class |
|----|------|---------------|---------|---------|-------|
```

### PS — Permission Sets
```markdown
| ID | Permission Set | Grants (objects CRUD, fields FLS, apps, system perms) | Assigned to | Class |
|----|----------------|-------------------------------------------------------|-------------|-------|
```

### USR — Demo Users
```markdown
| ID | Full Name | Username pattern | Profile | License | Permission Sets | Role in story | Class |
|----|-----------|------------------|---------|---------|-----------------|---------------|-------|
```
Username único: `<nombre>.<slug>@demo-<slug>.example`.

### VR — Validation Rules
```markdown
| ID | Object | Name | Error condition (formula) | Error message (ES) | Class |
|----|--------|------|---------------------------|--------------------|-------|
```

### FLW — Flows
Tipos: `Record-Triggered Flow`, `Screen Flow`, `Scheduled Flow`, `Autolaunched Flow`,
`Platform Event-Triggered Flow`. Indica siempre timing (Before/After save), condición de entrada y
acciones ordenadas con valores literales.
```markdown
| ID | API Name | Type | Object | Trigger | Entry condition | Actions (ordered) | Class |
|----|----------|------|--------|---------|-----------------|-------------------|-------|
```

### APR — Approval Processes
```markdown
| ID | Object | Name | Entry criteria | Approver | On approve / On reject | Class |
|----|--------|------|----------------|----------|------------------------|-------|
```

### AGT — Agentforce (agente, topics, actions, instrucciones, prompt templates)
```markdown
| ID | Component | API Name | Parent | Definition | Demo utterance → expected answer (DAT ref) | Class |
|----|-----------|----------|--------|------------|---------------------------------------------|-------|
| AGT-1 | Agent | Distributor_Service_Agent | – | Service agent, ES language, handoff to QUE-1 | – | 🟢 |
| AGT-2 | Topic | Order_Status | AGT-1 | Scope: order status and delivery date. Instructions: answer in Spanish, always cite order number | "¿Dónde está mi pedido 00012?" → status + delivery date of DAT-4 | 🔵 |
| AGT-3 | Action | Get_Order_Status | AGT-2 | Invokes FLW-3 (input OrderNumber, output Status, DeliveryDate) | – | 🔵 |
```

### UI — Apps, pages, list views, reports, dashboards
Reports: report type, filtros, agrupación, columnas. Dashboards: componente, fuente, tipo de
gráfico, formato condicional. Record pages: componentes y visibilidad.
```markdown
| ID | Type | Name | Details | Class |
|----|------|------|---------|-------|
```

### DAT — Demo Data (seed)
Registros WOW: una fila por registro con `Ref` y valores exactos. Relleno: fila agregada. Fechas
siempre relativas (`TODAY-40`, `NOW-3h`). Nunca campos de sistema.
```markdown
| ID | Object | Ref | Records | Key values | Feeds | Class |
|----|--------|-----|---------|------------|-------|-------|
| DAT-1 | Account | ACC-FILL | 15 | Spanish distribution companies, Murcia/Valencia, mix sizes | context | 🟢 |
| DAT-2 | Opportunity | OPP1 | 1 | Name "Frutas del Levante - Renovación"; Account @ACC1; StageName Negotiation/Review; Amount 85000; CloseDate TODAY+20; Stage_Entered_Date__c TODAY-45 | HU-1.1 ⭐ | 🟢 |
```

---

## 4. Cierre

```markdown
## BUILD ORDER
ORG-1 → SET-1, SET-2 → FLD-1 → PS-1 → USR-1 → FLW-1 → UI-1, UI-2 → DAT-1, DAT-2
(orden por tipo: ORG → SET → OBJ → FLD → RT → QUE → PS → USR → VR → FLW → APR → AGT → UI → DAT;
dentro de un tipo, respeta dependencias. Todos los IDs del manifiesto deben aparecer.)

## SEED FILES
Spec: seed-<slug>-v<N>/seed-spec.json · Generar: scripts/build_seed.py · Cargar:
sf data import tree --plan seed-<slug>-v<N>/seed-plan.json --target-org <alias>
Usuario de carga: Demo Loader (USR-x)

## REHEARSAL & RESET
| WOW | Pantalla | Registro | Qué debe verse | Plan B |
|-----|----------|----------|----------------|--------|
Reset: <borrar lo creado por Demo Loader y recargar / recrear scratch org>. Antes de cada demo: recargar semilla.

## SUPUESTOS
- <todo lo asumido; nunca como dato del cliente>

## CHANGELOG
- v<N>: <qué cambió respecto a v<N-1> y por qué>
```

---

## 5. Variante: prompt para el IDE

Cuando el usuario pida "el prompt para el IDE", emite solo esto (sin narrativa):

```
You are configuring a Salesforce demo org that starts EMPTY. Build EXACTLY the components below,
in the BUILD ORDER given. Do not add anything not listed. Use standard objects and fields unless a
row defines a custom one. Use the exact API names, types and parameters in each row.

Rules:
- Rows in ORG with Status "Verify": check first and STOP reporting if the license/feature is missing.
- Do not set system fields. Audit fields only if SET enables them.
- Seed dates are relative to today: TODAY-40 means 40 days before the load date.
- After building, generate and load the seed data, then run the REHEARSAL checks and report,
  per row, built / not built (and why).

[pegar aquí Parte B completa: tablas + BUILD ORDER + SEED FILES + REHEARSAL & RESET]
```

---

## 6. Ejemplo completo

Ver `assets/ejemplo-backlog.md` (Sales Cloud + Agentforce, distribución, península). Observa:
historias de 6 líneas, una fila por componente, WOW anclados en filas `DAT` fila a fila, fechas
relativas, campo propio de fecha de etapa en lugar de `LastStageChangeDate`, y todos los IDs en el
BUILD ORDER.
