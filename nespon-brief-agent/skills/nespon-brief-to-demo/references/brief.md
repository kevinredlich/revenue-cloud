# Analizar el brief

Un brief puede ser un correo, unas notas de reunión, un RFP, un mensaje o tres líneas del
comercial. Léelo entero (y sus adjuntos) antes de diseñar.

## Qué extraer

| Dato | Ejemplo | Si falta |
|---|---|---|
| Cliente y sector | "Bodegas Altiplano, vino, 120 empleados" | Empresa ficticia del sector indicado |
| Zona fiscal | Península, Canarias, Portugal… | Península (IVA 21%), como supuesto |
| Fecha de la demo | "el jueves 15" | Sin fecha: no condiciona nada |
| Audiencia de negocio | Dirección, comercial, marketing | "Dirección" como supuesto |
| Audiencia técnica | IT, sistemas | Asume que habrá alguien de IT |
| Necesidades (`NEC-n`) | "no saben qué distribuidor vende más" | Deducir del sector con `nespon-demo-builder/references/dolores-por-sector.md`, marcadas como Supuesto |
| Nubes | "Sales y algo de marketing" | Deducir de las necesidades |
| Restricciones | "nada de Agentforce", "solo estándar" | Ninguna |
| Sistemas actuales | ERP, Excel, otro CRM | Solo si una escena los toca (simulados con datos) |
| Lo que les preocupa | precio, complejidad, adopción | Prepara la objeción en el pitch |

## Cómo escribir las necesidades
- En lenguaje del cliente, con el problema y, si se conoce, su coste: *"Los comerciales pierden
  la mañana del lunes preparando el forecast en Excel"*.
- Máximo 6. Si hay más, agrupa o prioriza por lo que más duele a la audiencia de negocio.
- Cada necesidad se marca como **Brief** (está escrita) o **Supuesto** (la deduces tú).

## Cuándo preguntar
Solo si falta la nube y no se deduce, o si no hay ninguna necesidad identificable. Una sola tanda
de preguntas, mínima. Todo lo demás se asume y se lista en *Supuestos y preguntas abiertas* del
manifiesto para que el SE lo corrija en la revisión.
