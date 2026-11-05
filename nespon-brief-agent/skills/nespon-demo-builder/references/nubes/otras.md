# Playbook — Slack, MuleSoft y otras

## Slack + Salesforce
Org: workspace de Slack de pruebas conectado a la org (app de Salesforce para Slack). Escenas:
alerta de oportunidad o caso en un canal · aprobar desde Slack · canal de cuenta con registro
vinculado · agente de Agentforce en Slack. Por CLI: datos y el Flow que publica el mensaje (acción
de Slack en Flow). Manual: instalar la app en Slack y conectar la org. Trampa: workspace real de la
empresa; usar uno de pruebas.

## MuleSoft / integración
Una demo rápida **no** monta MuleSoft real. Opciones: (a) simular el resultado con datos semilla
(el pedido "llega" del ERP) y decirlo; (b) si la integración es la demo, cuenta de Anypoint de
prueba y una API simple ya publicada; el agente prepara la llamada desde Flow con Named Credential
+ External Service. Escenas: dato del ERP visible en el CRM · pedido de CRM enviado al ERP ·
monitorización de la API.

## Cualquier otra nube
Usa `_plantilla.md`: define org y licencias, 3-5 escenas con wow y plan B, qué va por CLI, qué es
manual, verificación y trampas. Apóyate en `salesforce-skill` para nombres exactos de objetos y
metadata. Ofrece al usuario guardar el playbook nuevo en la skill.
