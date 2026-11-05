# Playbook — Agentforce

## Org y licencias
Org con Agentforce provisionado: SDO de Partner Learning Camp o Developer Edition con Agentforce.
Comprobar en pre-flight licencias que contengan "Agent", "Einstein" o "Generative". Si no hay,
**para**: Agentforce no se puede simular con desarrollo.

## Escenas canónicas (elige 3-4)
| # | Escena | Qué enseña | Wow | Plan B |
|---|---|---|---|---|
| 1 | **Agente de servicio con datos reales** | El cliente pregunta por su pedido y el agente responde con el registro exacto | ⭐ responde con el dato del cliente, no con un texto genérico | Conversación ensayada + registro |
| 2 | **Handoff a humano** | Si la pregunta sale del alcance, pasa a un agente humano con el resumen | El humano no pregunta dos veces | Caso creado con el resumen |
| 3 | **Prompt template en el registro** | Botón que genera un resumen de la cuenta o un email de seguimiento | ⭐ el comercial prepara la reunión con un clic | Resumen ya generado |
| 4 | **Cómo está hecho** (audiencia técnica) | Topic, instrucciones y action sobre un Flow declarativo | Sin código, gobernado y auditable | Enseñar el Flow en Flow Builder |

Demo básica recomendada: **1 → 2 → 3**, con **4** si hay alguien de IT.

## Por CLI
- Campo `Order.Expected_Delivery__c` (Date); valor "Enviado" en `Order.Status` con categoría
  Draft (para poder cargarlo).
- Flow autolaunched `Get_Order_Status` (entrada: número de pedido en texto; busca `Order` por
  `Name = "Pedido " + entrada`; salidas: Status, Expected_Delivery__c).
- Datos: cuentas, pedidos con nombre "Pedido 000NN", fechas relativas.
- Agente: si `sf agent --help` muestra `generate agent-spec` y `create`, genera la spec del agente
  (rol, empresa, tono, topic "Estado de pedido") y créalo por CLI; si no, guía la creación en
  Agent Builder con los textos exactos. Prueba con `sf agent preview` si está disponible.

## Manual
- Activar Einstein / Agentforce en Setup si no lo está.
- En Agent Builder: vincular la action al Flow, revisar instrucciones, activar el agente.
- Prompt Builder: crear el template de resumen de cuenta (el agente redacta el prompt con merge
  fields) y añadir el botón a la record page.

## Verificación
- Preguntar en el preview "¿Dónde está mi pedido 00012?" y comprobar estado y fecha.
- Preguntar algo fuera de alcance y comprobar el handoff.

## Trampas
- Respuestas no deterministas: ensayar las frases exactas de la demo y dejarlas en la guía.
- `OrderNumber` es autonumérico y no se puede cargar: buscar por `Name`.
- Data Cloud grounding sin datos reales: no lo metas en una demo rápida.
