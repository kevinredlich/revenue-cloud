# Reparto: qué construye la IA y qué hace una persona

## Regla de decisión
Asigna **IA** si se cumplen las tres:
1. Se puede hacer con sf CLI (metadata desplegable, datos, asignaciones) sin interfaz.
2. El resultado se puede **verificar** con una consulta, un deploy correcto o una prueba.
3. No requiere credenciales, aceptar términos legales, comprar o activar licencias, ni juicio
   comercial o estético del cliente.

**IA+Revisión** si la IA lo puede construir pero el resultado necesita una mirada humana (estética,
tono, comportamiento no determinista). **Persona** si falla la 1 o la 3.

## Tabla de referencia

| Componente | Responsable | Por qué |
|---|---|---|
| Campos, objetos, picklists, record types, validation rules | IA | Metadata desplegable y verificable |
| Page layouts, compact layouts, Lightning record pages, Dynamic Forms, Path | IA | Metadata (FlexiPage, PathAssistant) |
| List views, reports, report types | IA | Metadata |
| Dashboards | IA+Revisión | Se despliegan bien; la estética la revisa el SE |
| Apps Lightning, utility bar, tema y logo (BrandingSet, ContentAsset) | IA+Revisión | Desplegable; colores y logo los valida el SE |
| Permission sets, asignaciones, queues, grupos | IA | CLI |
| Flows record-triggered y autolaunched sencillos | IA | Metadata; se prueban con datos |
| Screen Flows y Flows con lógica compleja | IA+Revisión | Se revisa la experiencia en Flow Builder |
| Custom notifications, email templates, aprobaciones | IA | Metadata |
| Apex y LWC (solo nivel 3) | IA+Revisión | Con tests; el SE revisa el resultado visual |
| Prompt templates, instrucciones y topics de Agentforce | IA+Revisión | No deterministas: ensayar |
| Datos de demo | IA | Generados, cargados y verificados |
| Activar Einstein / Agentforce / Data Cloud, aceptar términos | Persona | Aceptación legal y provisión en la interfaz |
| Asistentes de Setup sin metadata (Marketing Cloud, Data Cloud streams, tienda de Commerce, sitio de Experience desde plantilla) | Persona | Solo existen en la interfaz |
| Licencias, paquetes gestionados, orgs, trials | Persona | Compra / provisión |
| Credenciales, Named Credentials con secretos, Connected Apps, conectar Slack o sistemas externos | Persona | Secretos y autorización |
| Usuarios que requieren activación por email | Persona (la IA los crea; la persona activa) | Requiere el buzón |
| Geocodificación, optimización de Field Service, índices de búsqueda | Persona (o IA si el paquete expone un comando) | Procesos del paquete |
| Logo del cliente, nombres reales, precios reales | Persona | Juicio comercial |
| Ensayo de la demo | Persona | Siempre |

## Cómo escribir una tarea de persona
Cada componente **Persona** tiene su bloque en *Tareas de persona* del manifiesto con:
- Ruta en la interfaz (Setup → … → …), avisando de que el nombre del menú puede variar por release.
- Valores exactos a introducir.
- Cómo comprobar que está bien.
- Qué componentes IA esperan a que esté hecha.
