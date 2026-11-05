# Narrativa, audiencias y WOW

Una demo no es una lista de funciones: es un protagonista que pasa de un "antes" doloroso a un
"después" que le cambia el día. Diseña el arco antes de escribir historias; las épicas salen de él.

---

## El arco

1. **El antes.** Presenta al protagonista y su día malo, sin nombrar Salesforce. La audiencia debe
   reconocer su propio problema. Abre con el dolor que tenga coste (horas, euros, clientes perdidos)
   o riesgo (regulatorio, reputacional).
2. **El durante.** Cada acto ataca un dolor y muestra la plataforma en movimiento (un registro que
   cambia y dispara algo), no en estático. Aquí viven los WOW.
3. **El después.** Cierra en el mundo transformado: el dashboard que antes no existía, el tiempo
   recuperado. La audiencia debe poder resumir en una frase qué ha cambiado.

3-5 actos. Más de 5 diluye. Épica = acto; su orden es el orden de construcción y de presentación.

## El protagonista

- Nombre propio y rol ("Lucía Ortega, Jefa de Ventas Zona Sur"). Se empatiza con personas.
- Su dolor personal manda sobre el corporativo.
- Puede tener un aliado (su manager aprueba, el agente de servicio recibe el caso), pero el hilo
  lo lleva una persona.

## Dos audiencias, una historia

| Audiencia | Qué quiere ver | Cómo se le da su momento |
|---|---|---|
| **Negocio** (Dirección, comercial, CFO) | Resultado, visibilidad, tiempo y dinero | Dashboards, antes/después cuantificado, un proceso de 5 pasos convertido en 1 |
| **Técnica** (IT, Sistemas, arquitectura) | Mantenibilidad, seguridad, integración, esfuerzo | Enseñar que el Flow es declarativo, el permission set que aísla datos, el modelo estándar sin objetos a medida, dónde entraría su ERP |

En la cabecera del backlog, cada acto indica a qué audiencia habla sobre todo. Al menos un momento
es para la técnica; si no, esa persona sale sin argumentos para defender la compra por dentro.

## Fabricar el WOW (mínimo 2)

Un buen WOW:
- **Cae justo después de nombrar un dolor** — el contraste es el motor.
- **Se apoya en datos semilla concretos** — las 3 oportunidades en rojo existen, con sus valores.
- **Es inevitable** — la configuración y los datos lo garantizan.
- **Es robusto** — preferentemente estándar; nada que dependa de una integración en vivo.
- **Tiene plan B** — si falla (la IA responde raro, el Flow tarda), qué se enseña en su lugar
  (registro ya procesado, conversación ensayada, captura en una pestaña preparada).

Patrones fiables:
- Dashboard que revela lo invisible (riesgo, ranking, tendencia) con filtros del protagonista.
- Automatización visible: cambias un campo y aparece la tarea, el caso, la alerta o la aprobación.
- Agentforce respondiendo con el contexto real de un registro concreto.
- Móvil: el técnico o comercial ve el historial antes de entrar a la visita.
- Un clic que sustituye cinco pasos y tres sistemas.

Coloca uno pronto (engancha) y otro al final (cierra).

## Mapear dolores → actos

1. Lista los dolores (máx. 5-6).
2. Ordénalos por impacto para el protagonista, no por orden técnico.
3. Agrupa los que comparten pantalla o flujo.
4. Asigna a cada acto rol narrativo (problema / giro / resultado) y audiencia principal.
5. Coloca los WOW y su plan B.

Ejemplo (distribución, Sales + Agentforce):

| Acto | Dolor | Rol | Audiencia | WOW |
|---|---|---|---|---|
| 1 — El pipeline invisible | Forecast en Excel, sin riesgo visible | Problema | Negocio | ⭐ dashboard de riesgo |
| 2 — La tarea que se crea sola | Seguimientos que dependen de la memoria | Giro | Técnica | |
| 3 — El distribuidor que nunca espera | Consultas fuera de horario | Resultado | Negocio | ⭐ agente con el pedido real |

## Errores narrativos

- Tour de producto menú a menú.
- Empezar por "esto es Sales Cloud" en vez de por el problema de Lucía.
- WOW con la pantalla vacía.
- Terminar en una pantalla cualquiera en lugar de en el "después".
- Olvidar a la audiencia técnica.
