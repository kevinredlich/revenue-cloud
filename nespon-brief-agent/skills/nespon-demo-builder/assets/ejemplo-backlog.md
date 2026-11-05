# DEMO BACKLOG — Frutas del Levante — Sales Cloud + Agentforce — v1

**Sector:** Distribución mayorista de fruta · **Tamaño:** 180 empleados, 14 comerciales · **Zona fiscal:** Península (IVA 21%; fruta al 4%)
**Protagonista:** Lucía Ortega, Jefa de Ventas Zona Sur
**Audiencia negocio:** Director Comercial, CEO · **Audiencia técnica:** Responsable de Sistemas
**Nube ancla:** Sales Cloud · **Nubes de apoyo:** Agentforce
**Org objetivo:** Developer Edition vacía con Agentforce (ver ORG)
**Pitch:** Que Lucía sepa cada lunes qué operaciones se le escapan y que ningún distribuidor espere a que abra la oficina para saber dónde está su pedido.

**RESTRICCIONES FIJAS (del SE, no negociables en ninguna versión):**
- Sin CPQ ni Revenue Cloud.

**Skills usadas:** nespon-demo-builder · salesforce-skill — confirmar tipos de Flow y metadata de Agentforce

| Dolor del cliente | Épica | Audiencia | WOW |
|---|---|---|---|
| El forecast vive en un Excel que se actualiza tarde; las operaciones grandes se pierden sin aviso | Épica 1 — El pipeline invisible | Negocio | ⭐ dashboard de riesgo |
| El seguimiento depende de la memoria de cada comercial | Épica 2 — La tarea que se crea sola | Técnica | |
| Los distribuidores llaman fuera de horario para saber el estado del pedido | Épica 3 — El distribuidor que nunca espera | Negocio | ⭐ agente con el pedido real |

**WOW:** ⭐ 3 operaciones en rojo en el dashboard de Lucía (Épica 1) · ⭐ el agente responde con el pedido real a las 22:00 (Épica 3)
**Clasificación:** 🟢 9 · 🔵 7 · 🟠 0

# PARTE A — BACKLOG NARRATIVO

## ÉPICA 1 — EL PIPELINE INVISIBLE
**Dolor:** Lucía reconstruye el forecast a mano cada lunes y se entera tarde de las operaciones paradas; el trimestre pasado se perdió una renovación de 85.000 €.
**Rol narrativo:** Problema · **Audiencia principal:** Negocio

### HU-1.1 — Pipeline y riesgo en un dashboard
- **Historia:** Como Jefa de Ventas, quiero ver mi pipeline y las operaciones estancadas en un dashboard, para dejar de reconstruir el forecast en Excel.
- **Dolor:** Forecast manual sin visibilidad de riesgo · **WOW:** ⭐ el dashboard marca en rojo 3 operaciones paradas más de 30 días · **Clasificación:** 🔵
- **Done (Gherkin, EN):** Given 12 open Opportunities with 3 having Stage_Entered_Date__c older than 30 days · When Lucía opens dashboard "Pipeline y Riesgo" · Then pipeline by stage is shown AND exactly 3 deals appear flagged "En riesgo" in red
- **Plan B:** abrir la list view "Operaciones en riesgo" (UI-3), que muestra las mismas 3 filas
- **Config refs:** FLD-1, FLD-2, FLW-3, UI-1, UI-2, UI-3, UI-4, DAT-1, DAT-2, DAT-3
- **Depende de:** —

## ÉPICA 2 — LA TAREA QUE SE CREA SOLA
**Dolor:** Si el comercial no apunta el seguimiento, nadie lo hace; el Responsable de Sistemas teme que automatizar implique desarrollo que luego no pueda mantener.
**Rol narrativo:** Giro · **Audiencia principal:** Técnica

### HU-2.1 — Seguimiento automático al entrar en riesgo
- **Historia:** Como comercial, quiero que se me cree una tarea cuando una operación entra en riesgo, para no depender de mi memoria.
- **Dolor:** Seguimientos olvidados · **WOW:** — · **Clasificación:** 🔵
- **Done (Gherkin, EN):** Given Opportunity "Mercados Ruiz - Ampliación" with Stage_Entered_Date__c = TODAY-31 · When Lucía saves the record · Then a Task "Revisar operación en riesgo" due tomorrow is assigned to the Owner
- **Config refs:** FLW-1, FLD-2, DAT-3
- **Depende de:** HU-1.1

### HU-2.2 — Enseñar a Sistemas que es configuración
- **Historia:** Como Responsable de Sistemas, quiero ver cómo está construida la automatización, para saber que mi equipo puede mantenerla sin código.
- **Dolor:** Miedo a desarrollo a medida inmantenible · **WOW:** — · **Clasificación:** 🟢
- **Done (Gherkin, EN):** Given FLW-1 is active · When the SE opens it in Flow Builder · Then all elements are declarative and no Apex class exists in the org
- **Config refs:** FLW-1, PS-1
- **Depende de:** HU-2.1

## ÉPICA 3 — EL DISTRIBUIDOR QUE NUNCA ESPERA
**Dolor:** Un 30% de las llamadas de distribuidores son "¿dónde está mi pedido?", muchas fuera de horario (Supuesto: cifra orientativa, confirmar con el cliente).
**Rol narrativo:** Resultado · **Audiencia principal:** Negocio

### HU-3.1 — El agente responde con el pedido real
- **Historia:** Como distribuidor, quiero preguntar por mi pedido a cualquier hora, para no esperar a que abra la oficina.
- **Dolor:** Consultas fuera de horario sin respuesta · **WOW:** ⭐ el agente responde con estado y fecha del pedido 00012 · **Clasificación:** 🔵
- **Done (Gherkin, EN):** Given Order "Pedido 00012" with Status "Enviado" and Expected_Delivery__c = TODAY+1 · When the user asks "¿Dónde está mi pedido 00012?" · Then the agent answers in Spanish with status "Enviado" and tomorrow's date
- **Plan B:** abrir la conversación ensayada en la pestaña del agente y enseñar el registro DAT-4
- **Config refs:** AGT-1, AGT-2, AGT-3, FLW-2, FLD-3, DAT-4
- **Depende de:** —

# PARTE B — CONFIGURATION MANIFEST

### ORG — Org & Licenses
| ID | Item | Requirement | Status | Notes |
|----|------|-------------|--------|-------|
| ORG-1 | Org type | Developer Edition, empty | Required | Locale es_ES, currency EUR, TZ Europe/Madrid |
| ORG-2 | License | Agentforce / Einstein provisioned | Verify | If missing, Épica 3 out of scope |

### SET — Setup & Features
| ID | Setup Area | Setting | Value | Class |
|----|-----------|---------|-------|-------|
| SET-1 | Einstein Setup | Turn on Einstein; enable Agentforce | On | 🟢 |
| SET-2 | Orders Settings | Enable Orders; Order.Status add value "Enviado" (Status Category = Draft, so seed can insert it) | On | 🟢 |
| SET-3 | Deliverability | Access level | System email only | 🟢 |

### FLD — Fields
| ID | Object | API Name | Label | Type | Spec (values / formula / ref) | Req | Purpose | Class |
|----|--------|----------|-------|------|-------------------------------|-----|---------|-------|
| FLD-1 | Opportunity | Stage_Entered_Date__c | Fecha entrada en etapa | Date | set by seed; FLW-3 updates on StageName change | – | Loadable stage age | 🔵 |
| FLD-2 | Opportunity | Risk_Level__c | Nivel de riesgo | Formula(Return=Text) | IF(AND(NOT(IsClosed), TODAY()-Stage_Entered_Date__c>30),"En riesgo","En plazo") | – | Flag stalled deals | 🔵 |
| FLD-3 | Order | Expected_Delivery__c | Entrega prevista | Date | – | – | Answer for agent | 🔵 |

### PS — Permission Sets
| ID | Permission Set | Grants (objects CRUD, fields FLS, apps, system perms) | Assigned to | Class |
|----|----------------|-------------------------------------------------------|-------------|-------|
| PS-1 | Demo_Sales_User | Opportunity/Order/Task CRUD; FLS FLD-1..3 read/edit; app UI-1 | USR-1 | 🔵 |

### USR — Demo Users
| ID | Full Name | Username pattern | Profile | License | Permission Sets | Role in story | Class |
|----|-----------|------------------|---------|---------|-----------------|---------------|-------|
| USR-1 | Lucía Ortega | lucia.ortega@demo-frutas-levante.example | Standard User | Salesforce | PS-1 | Protagonist | 🟢 |
| USR-2 | Demo Loader | loader@demo-frutas-levante.example | System Administrator | Salesforce | – | Loads seed; reset by CreatedById | 🟢 |

### FLW — Flows
| ID | API Name | Type | Object | Trigger | Entry condition | Actions (ordered) | Class |
|----|----------|------|--------|---------|-----------------|-------------------|-------|
| FLW-1 | Create_Risk_Followup_Task | Record-Triggered Flow | Opportunity | After save (create, update) | Risk_Level__c = "En riesgo" AND no open Task with Subject "Revisar operación en riesgo" | 1) Create Task (Subject "Revisar operación en riesgo", OwnerId = Opportunity.OwnerId, ActivityDate = TODAY()+1, WhatId = Opportunity.Id) | 🔵 |
| FLW-2 | Get_Order_Status | Autolaunched Flow | Order | Invoked by AGT-3 | input OrderNumber (Text) | 1) Get Order where Name = "Pedido " + input; 2) output Status, Expected_Delivery__c | 🔵 |
| FLW-3 | Stamp_Stage_Entered_Date | Record-Triggered Flow | Opportunity | Before save (update) | ISCHANGED(StageName) | 1) Set Stage_Entered_Date__c = TODAY() | 🔵 |

### AGT — Agentforce
| ID | Component | API Name | Parent | Definition | Demo utterance → expected answer (DAT ref) | Class |
|----|-----------|----------|--------|------------|---------------------------------------------|-------|
| AGT-1 | Agent | Distributor_Service_Agent | – | Service agent, Spanish, friendly tone, handoff to human on anything outside topics | – | 🟢 |
| AGT-2 | Topic | Order_Status | AGT-1 | Scope: order status and expected delivery. Instructions: answer in Spanish; always repeat the order number; never invent dates | "¿Dónde está mi pedido 00012?" → "Enviado", delivery tomorrow (DAT-4) | 🔵 |
| AGT-3 | Action | Get_Order_Status | AGT-2 | Invokes FLW-2 (in OrderNumber; out Status, Expected_Delivery__c) | – | 🔵 |

### UI — Apps, pages, list views, reports, dashboards
| ID | Type | Name | Details | Class |
|----|------|------|---------|-------|
| UI-1 | Lightning App | Ventas Levante | Tabs: Accounts, Opportunities, Orders, Tasks, Dashboards | 🟢 |
| UI-2 | Report | Operaciones abiertas por etapa | Type Opportunities; filter IsClosed = false; group StageName; cols Name, Account, Amount, CloseDate, Risk_Level__c | 🟢 |
| UI-3 | List View | Operaciones en riesgo | Opportunity; filter Risk_Level__c = "En riesgo"; cols Name, Amount, Stage_Entered_Date__c, Owner | 🟢 |
| UI-4 | Dashboard | Pipeline y Riesgo | Running user Lucía; Comp1 bar Sum(Amount) by StageName from UI-2; Comp2 table from UI-2 filtered Risk_Level__c = "En riesgo", conditional red | 🟢 |

### DAT — Demo Data (seed)
| ID | Object | Ref | Records | Key values | Feeds | Class |
|----|--------|-----|---------|------------|-------|-------|
| DAT-1 | Account | ACC-FILL | 10 | Spanish fruit retailers and wholesalers, Murcia/Alicante/Valencia; includes ACC1 "Frutas del Levante Clientes SL", ACC2 "Mercados Ruiz SA" | context | 🟢 |
| DAT-2 | Opportunity | OPP-FILL | 9 | Owner USR-1; stages Prospecting..Proposal; Stage_Entered_Date__c TODAY-2..TODAY-20; CloseDate TODAY+5..TODAY+25 | HU-1.1 | 🟢 |
| DAT-3 | Opportunity | OPP1, OPP2, OPP3 | 3 | OPP1 "Frutas del Levante - Renovación" 85000, Negotiation/Review, Stage_Entered_Date__c TODAY-45; OPP2 "Mercados Ruiz - Ampliación" 42000, Proposal/Price Quote, TODAY-31; OPP3 "Hortícola Segura - Nuevo" 27500, Qualification, TODAY-38; all CloseDate TODAY+15, Owner USR-1 | HU-1.1 ⭐, HU-2.1 | 🟢 |
| DAT-4 | Order | ORD12 | 1 | Name "Pedido 00012" (OrderNumber is auto-number and not loadable, so the agent matches by Name); AccountId @ACC2; Status "Enviado"; EffectiveDate TODAY-2; Expected_Delivery__c TODAY+1 | HU-3.1 ⭐ | 🟢 |

## BUILD ORDER
ORG-1, ORG-2 → SET-1, SET-2, SET-3 → FLD-1, FLD-2, FLD-3 → PS-1 → USR-1, USR-2 → FLW-3, FLW-1, FLW-2 → AGT-1, AGT-2, AGT-3 → UI-1, UI-2, UI-3, UI-4 → DAT-1, DAT-2, DAT-3, DAT-4

## SEED FILES
Spec: seed-frutas-levante-v1/seed-spec.json · Generar: scripts/build_seed.py · Cargar: sf data import tree --plan seed-frutas-levante-v1/seed-plan.json --target-org frutas-demo · Usuario de carga: USR-2
Nota: FLW-1 y FLW-3 se activan después de la carga para que la semilla no dispare tareas ni reescriba Stage_Entered_Date__c.

## REHEARSAL & RESET
| WOW | Pantalla | Registro | Qué debe verse | Plan B |
|-----|----------|----------|----------------|--------|
| ⭐ Riesgo | Dashboard UI-4 | DAT-3 | 3 filas en rojo, 85.000 € arriba | List view UI-3 |
| ⭐ Agente | Agent preview AGT-1 | DAT-4 | "Enviado", entrega mañana | Conversación ensayada + registro DAT-4 |

Reset: borrar Opportunity, Order, Task y Account con CreatedById = USR-2 y recargar semilla con fechas frescas. Antes de cada demo: recargar semilla y borrar las tareas creadas en el ensayo.

## SUPUESTOS
- Agentforce disponible en la org (ORG-2); si no, la Épica 3 sale del alcance.
- Porcentaje de llamadas por estado de pedido orientativo; confirmar con el cliente.
- Los distribuidores hablarían con el agente por un canal web; el canal concreto no se demuestra.
