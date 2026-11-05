# Impacto: la escalera y el catálogo de momentos vistosos

## La escalera de impacto
Sube un escalón solo si el de abajo no consigue el efecto que busca la escena.

| Nivel | Qué es | Ejemplos | Marca |
|---|---|---|---|
| 0 · Default | La plataforma tal cual, con buenos datos | Pipeline Kanban, related lists, búsqueda global, app móvil | 🟢 |
| 1 · Configuración | Ajustes estándar que cambian la experiencia | Path con guía, Dynamic Forms, Highlights panel, compact layouts, list views, report charts, formato condicional, dashboards, tema y logo del cliente, utility bar | 🟢 |
| 2 · Automatización visible | La plataforma actúa delante del cliente | Record-triggered Flow que crea tareas o avisa, notificaciones en la campana o en Slack, Screen Flow guiado, aprobaciones, email automático (al SE), Agentforce, prompt templates, scoring | 🔵 |
| 3 · Custom | Lo estándar no da el efecto | LWC visual (tarjeta 360, timeline, mapa embebido, gamificación), Apex invocable para un cálculo concreto | 🟠 |

Regla: **una demo ganadora suele ser 70-80% niveles 0-1, 20-30% nivel 2 y 0-10% nivel 3.** Si el
manifiesto tiene más custom, revisa si es por impacto o por costumbre.

Un 🟠 es aceptable cuando cumple las tres condiciones: (1) produce un wow que la audiencia
recordará, (2) no hay equivalente estándar con efecto parecido, (3) es pequeño y la IA lo puede
construir y probar con fiabilidad. Se justifica en la columna *Motivo* por el impacto.

## Catálogo de momentos vistosos (elige por necesidad, no por moda)

**Visibilidad (para Dirección)**
- Dashboard con 3-5 componentes, formato condicional rojo/verde y filtro por comercial.
- Report con gráfico embebido en la página de la cuenta.
- Kanban de oportunidades arrastrando una tarjeta de etapa.

**En movimiento (la plataforma actúa sola)**
- Cambiar un campo → aparece una tarea, una notificación en la campana y un post en Chatter, en
  directo. Usa *custom notification* para que se vea en pantalla.
- Screen Flow que guía un proceso de varios pasos en una pantalla con lógica condicional.
- Aprobación de descuento: el manager aprueba desde el móvil o la notificación.
- Email automático que llega al buzón del SE durante la demo.

**Inteligencia**
- Agentforce respondiendo con datos de un registro real de la demo.
- Prompt template: resumen de la cuenta o borrador de email con un clic.
- Lead scoring o recomendación visible en el registro.

**Experiencia 360**
- Página de registro con Highlights, Path, pestañas, related lists y componentes condicionales.
- El mismo registro en la app móvil.

**Marca del cliente**
- Tema con colores y logo del cliente y app con su nombre. Barato y muy eficaz: el cliente se ve
  a sí mismo.

## Señales de que una escena no impacta
- Se enseña una pantalla sin que nada cambie.
- Hay campos vacíos o listas con un solo registro.
- El wow necesita explicación para entenderse.
- Se enseña Setup a una audiencia de negocio.
