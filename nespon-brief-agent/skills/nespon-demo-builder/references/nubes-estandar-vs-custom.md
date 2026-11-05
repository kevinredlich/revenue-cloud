# Nubes: estándar vs custom, licencias y trampas de demo

## Índice
1. Regla de decisión
2. Siempre estándar (cualquier nube)
3. Por nube: Sales · Service · Agentforce · Revenue Cloud · Field Service · FSC · Health ·
   Marketing · Data Cloud · Experience · Maps · Analytics · MuleSoft
4. Combinaciones multi-nube habituales
5. Anti-patterns

> Las licencias y nombres comerciales cambian con cada release. Lo que aquí se dice de licencias es
> orientativo: si dudas si una org vacía trae una función, **decláralo en `ORG` como requisito a
> verificar** y en Supuestos. Para nombres exactos de objetos/metadata, confirma con `salesforce-skill`.

---

## 1. Regla de decisión (a cada historia y a cada fila del manifiesto)

1. ¿Se resuelve con objetos, campos o funciones **estándar** activables en Setup? → 🟢
2. ¿Se resuelve **sin código** (campo/objeto custom, Flow, validation rule, record type, Lightning
   page, report type, permission set, approval, prompt template)? → 🔵
3. Solo si lo declarativo es **funcionalmente incapaz** (no "más cómodo en código") → 🟠 con
   justificación en la historia.

Record Types y valores de picklist nuevos sobre campos estándar son 🟢 de bajo esfuerzo. Un campo
o un objeto nuevo es siempre 🔵.

## 2. Siempre estándar

Account, Contact, Lead, Opportunity, Case, Campaign, Task, Event, Product2, Pricebook2, Quote,
Order, Contract, Asset. Page layouts, compact layouts, list views, Path, Dynamic Forms. Reports y
dashboards. Web-to-Lead, Web-to-Case, Email-to-Case, Assignment/Escalation/Auto-Response Rules,
Queues, Public Groups, Omni-Channel, Collaborative Forecasting, Chatter, Approval Processes (su
definición es 🔵, la función es estándar).

---

## 3. Por nube

### Sales Cloud
- 🟢 Pipeline, stages, Path con guidance, Forecasting, conversión de Lead, Products & Pricebooks,
  Quotes estándar, dashboards de embudo, Opportunity Contact Roles, Opportunity Teams.
- 🔵 Campos de calificación, fecha propia de entrada en etapa (`Stage_Entered_Date__c`) para medir
  estancamiento, validation rules, Flows de tareas/alertas, approval de descuento.
- 🟠 Casi nunca.
- **Trampa:** WOW basado en `LastStageChangeDate`, `LastActivityDate` o `Age`: no se pueden cargar
  (ver `org-y-datos-semilla.md`). **Trampa:** Forecasting sin activar ni configurar tipos → pantalla
  vacía; va en `SET`.

### Service Cloud
- 🟢 Cases, Queues, Assignment/Escalation Rules, Email-to-Case, Macros, Omni-Channel, Service
  Console, Path de caso.
- 🔵 Entitlements & Milestones (SLAs), Knowledge (artículos y data categories), Flows de escalado,
  Case record types por canal.
- 🟠 CTI a medida.
- **Licencia:** Service Console, Knowledge y Omni-Channel requieren licencia Service Cloud y a
  veces activar la función (`SET`). **Trampa:** Milestones que "vencen" requieren tiempo real;
  para el WOW, crea el caso con fecha de apertura pasada (audit fields) o usa un milestone corto.

### Agentforce
- 🟢 Agente con Topics y Actions estándar sobre datos que ya viven en la org; handoff a humano.
- 🔵 Topics e instrucciones a medida, Actions que invocan Flows (`Autolaunched Flow`), Prompt
  Templates con merge fields de registros, Knowledge como grounding.
- 🟠 Actions que invocan Apex invocable o APIs externas.
- **Licencia:** requiere que Agentforce/Einstein esté provisionado y activado en la org (`ORG` +
  `SET`); una org vacía cualquiera puede no traerlo.
- **Trampa:** el agente responde bien solo si los datos semilla contienen exactamente lo que se le
  preguntará. Especifica en `AGT` la pregunta de demo y el registro (`DAT`) que la responde.
  **Trampa:** respuestas no deterministas → el plan B es tener la conversación ensayada y un
  registro que se pueda enseñar directamente.

### Revenue Cloud (RLM)
- Carga `revenue-cloud-demo`: define objetos RLM, catálogo, selling models, pricing y patrones WOW.
- Regla de suficiencia: para catálogos pequeños sin configuración (< ~15 productos, sin bundles ni
  reglas) Quotes estándar de Sales Cloud (🟢) bastan; no metas RLM "porque impresiona".
- **Licencia:** RLM necesita org provisionada con Revenue Cloud; declara en `ORG`.

### Field Service
- 🟢 Work Orders, Service Appointments, Service Resources, Territories, Operating Hours, app móvil,
  Assets, Dispatcher Console, scheduling policies estándar.
- 🔵 Flow Case → Work Order, campos custom de WO, work types a medida.
- 🟠 Optimización custom, integración de stock en tiempo real.
- **Licencia:** paquete gestionado de Field Service + permission sets de FSL; no está en una org
  vacía estándar. **Trampa:** el Gantt vacío por falta de Operating Hours/Territory Members en `DAT`.

### Financial Services Cloud
- 🟢 Modelo FSC (financial accounts, policies, goals, household/relationship groups), Actionable
  Relationship Center, Action Plans.
- 🔵 Campos regulatorios (IDD, MiFID II), Flows de onboarding, validation rules de compliance.
- 🟠 Core bancario/asegurador real.
- **Licencia:** org FSC específica. En España, cita DORA/IDD solo si el cliente es del sector.

### Health Cloud / Life Sciences
- 🟢 Modelo de paciente, care plans, timeline.
- 🔵 Care programs a medida, Flows de derivación.
- **Licencia:** org específica. Nunca datos reales de salud: todo sintético (categoría especial RGPD).

### Marketing (Account Engagement / Marketing Cloud)
- 🟢 Account Engagement: formularios, listas, plantillas, Engagement Studio, scoring & grading,
  conector con Sales Cloud. Para B2B mid-market suele ser la opción.
- 🔵 Campos de prospect, automation rules.
- 🟠 AMPscript/SSJS complejo, integraciones de datos.
- **Licencia:** cuenta de marketing separada; normalmente no se monta desde cero en una demo corta.
  Alternativa creíble: Campaigns + Campaign Members + Flow en la org core, dicho en Supuestos.

### Data Cloud
- 🟢/🔵 Data streams, DMOs, identity resolution, calculated insights, segments, activations.
- 🟠 Transformaciones con código.
- **Trampa principal:** un CDP sin datos de varias fuentes no genera WOW, genera dudas. Solo entra si
  el dolor es fragmentación real y hay datos semilla de ≥2 fuentes (p. ej. CSV de "e-commerce" y
  "tienda") preparados para ingestión.

### Experience Cloud
- 🟢 Sitio con plantilla estándar, self-service de casos y Knowledge, sharing sets.
- 🔵 Componentes configurados, Flows embebidos, branding.
- 🟠 LWC propio.
- **Trampa:** el usuario externo (login de portal) requiere licencia de comunidad, contact asociado
  y perfil; va en `USR`. Si no se ensaya el login, falla en directo.

### Salesforce Maps
- 🟢 Capas desde datos de la org, rutas, check-in.
- **Licencia:** paquete gestionado. **Trampa:** cuentas sin geocodificar → mapa vacío; los datos
  semilla necesitan direcciones reales y verificables (calles reales, nunca de clientes reales).

### CRM Analytics / Tableau
- 🟢 Dashboards estándar suelen bastar para demo. CRM Analytics/Tableau solo si el dolor es
  analítico de dirección y la audiencia lo pide. Licencia aparte.

### MuleSoft / integración
- 🟢 En demo, **simula** el resultado de la integración con datos semilla y dilo en Supuestos.
- 🔵 Named Credential + External Service + HTTP Callout en Flow para una integración simple y fiable.
- 🟠 MuleSoft real o Apex de integración, solo si la integración ES la demo.

---

## 4. Combinaciones multi-nube habituales

| Combinación | Ancla | Cómo se cose la historia |
|---|---|---|
| Sales + Revenue | Sales | Oportunidad → presupuesto en un clic; el WOW es el precio correcto y aprobado al instante |
| Service + Agentforce | Service | El agente resuelve lo simple; el caso complejo llega al humano con contexto completo |
| Sales + Maps | Sales | Del pipeline en riesgo a la ruta de visitas de hoy |
| Service + Field Service | Service | Caso → orden de trabajo → técnico con historial del activo en el móvil |
| Sales + Account Engagement | Sales | El lead caliente llega puntuado y con historial; el comercial sabe qué decir |
| FSC + Agentforce | FSC | El gestor prepara la reunión con un resumen generado del cliente |

---

## 5. Anti-patterns (detéctalos y corrígelos)

- **Coder's trap:** Apex/LWC para lo que un Flow resuelve.
- **Custom object fever:** objetos "Cliente__c"/"Pedido__c" cuando Account/Order valen.
- **Stack de escaparate:** Data Cloud, MuleSoft o RLM sin un dolor que los pida.
- **WOW frágil:** momento estrella dependiente de código, integración en vivo o IA sin ensayar.
- **Historia sin dato:** dashboard, mapa o Gantt vacío por falta de datos semilla.
- **Dependencia invisible:** la historia funciona en la org del SE pero no en una org vacía
  (función no activada, licencia no asignada, geocodificación pendiente, campo de sistema).
