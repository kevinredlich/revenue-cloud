# Formato del PITCH.md

El pitch sirve para **defender la demo**: explicar qué se va a ver, por qué responde a lo que el
cliente pidió y cómo contestar a las objeciones. Lo lee el SE antes de la reunión y lo usa como
guion de apoyo. Español de España, en lenguaje del cliente, sin jerga de Setup. Ejemplo en
`assets/ejemplo-PITCH.md`.

```markdown
# PITCH — <Cliente> — <Nube ancla>

## En una frase
<Lo que el cliente va a poder hacer y que hoy no puede. Sin "Salesforce permite…".>

## Lo que nos pidieron
<2-3 frases con el reto del cliente tal como lo cuenta el brief. Cita su lenguaje.>

## Qué vamos a enseñar y por qué
| Escena | Necesidad que responde | Lo que verán | Valor para ellos |
|--------|------------------------|--------------|------------------|
| ESC-1 <título> | NEC-1 <resumida> | <pantalla y acción> | <tiempo, dinero, riesgo o control que ganan> |

## Los momentos que tienen que recordar
- ⭐ <wow 1>: <qué ven y la frase que lo remata>
- ⭐ <wow 2>: …

## Por qué así (para la audiencia técnica)
- <cuánto es estándar y configuración vs desarrollo, con los números del reparto>
- <mantenimiento: lo pueden cambiar ellos sin programar>
- <seguridad y datos: permisos, quién ve qué>
- <integración: dónde entraría su ERP u otros sistemas, sin prometer lo que no se enseña>

## Speech por escena
### ESC-1 — <título>
**Entrada:** "<frase para presentar la escena desde el problema del cliente>"
**Mientras se ve:** "<1-2 frases que acompañan la acción en pantalla>"
**Remate:** "<la frase de valor que cierra la escena>"

## Objeciones probables
| Objeción | Respuesta |
|----------|-----------|
| "Esto es una demo, en nuestra empresa será distinto" | <respuesta concreta: qué es configuración y se adapta> |
| "¿Cuánto cuesta / cuánto se tarda en implantar?" | <redirigir a un taller de alcance; no inventar cifras> |

## Cierre y siguiente paso
**Cierre:** "<antes → después en una frase>"
**Siguiente paso propuesto:** <taller de discovery, demo a medida, POC acotado…>
```

Reglas:
- Cada escena del manifiesto aparece en la tabla y en el speech, en el mismo orden.
- Las cifras del pitch salen de los datos de demo (`RESUMEN-RELLENO.md` y protagonistas).
- No prometas precios, plazos de implantación ni funciones que no estén en la demo.
- Si una escena depende de una tarea de persona pendiente, el speech incluye el plan B.
