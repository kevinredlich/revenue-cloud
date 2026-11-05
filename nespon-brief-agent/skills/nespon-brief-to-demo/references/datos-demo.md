# Datos de demo ficticios que cuentan la historia

Los datos son la mitad de la demo. Un dashboard espectacular con cuatro registros parece de juguete;
una ficha con campos vacíos parece a medio hacer.

## Dos capas

| Capa | Qué es | Quién la escribe |
|---|---|---|
| **Protagonistas** | Los registros que sostienen cada wow y cada escena: la cuenta estrella, la oportunidad en riesgo, el caso urgente, el contacto que enseñas en el móvil | Tú, a mano, valor a valor, en `datos/heroes.json` |
| **Relleno** | Volumen creíble alrededor: más cuentas, contactos, oportunidades en varias etapas, casos, actividad reciente | `scripts/fill_data.py` desde `datos/fill-config.json` |

`fill_data.py` une ambas capas en `datos/seed-spec.json`, que luego carga `build_seed.py` de
`nespon-demo-builder`. Además escribe `datos/RESUMEN-RELLENO.md` con los totales (pipeline por
etapa, casos por estado) para que el pitch use cifras que de verdad salen en pantalla.

## Reglas
1. **Cada campo visible en una escena está relleno** en los protagonistas: si la página enseña
   Sector, Teléfono, Web, Descripción y Próximo paso, todos tienen valor.
2. **Relaciones completas**: cuenta → contactos → oportunidades → tareas/casos. Nada huérfano.
3. **Las cifras cuadran con el relato**: si el pitch dice "1,2 M€ de pipeline y 3 operaciones en
   riesgo", los datos suman eso. Ajusta los protagonistas, no el discurso.
4. **Fechas relativas** (`TODAY-40`, `NOW-3h`), nunca fijas. Actividad en los últimos 90 días.
   Oportunidades cerradas con fecha pasada; abiertas con fecha futura dentro del trimestre si hay forecast.
5. **Nunca campos de sistema** (`LastStageChangeDate`, `IsWon`, `LastActivityDate`…); ver
   `nespon-demo-builder/references/org-y-datos-semilla.md`.
6. **Realismo español**: nombres y apellidos variados, empresas con forma jurídica (SL, SA), CIF con
   formato y dígito de control válidos pero inventados, teléfonos `+34 9…` (fijos) y `+34 6…`
   (móviles), ciudades reales, importes en euros.
7. **Seguridad**: emails en dominios reservados que nunca entregan (`@<empresa>.example` o
   `@example.com`); el único email real es el del SE (`{{SE_EMAIL}}`). Nunca datos de personas reales.
8. **Picklists válidos**: usa valores que existan en la org (describe el objeto si dudas). País como
   `Spain` (funciona con y sin picklists de país/estado).
9. **Propietarios**: si un dashboard compara comerciales, reparte el relleno entre varios usuarios con
   `"owners": ["{{OWNER_1}}","{{OWNER_2}}"]` y pasa sus Id con `--var` al generar.

## `datos/fill-config.json`
```json
{
  "seed": 7,
  "heroes": "datos/heroes.json",
  "owners": [],
  "accounts": {"count": 25, "industries": ["Food & Beverage", "Retail", "Hospitality"],
               "cities": ["Murcia", "Alicante", "Valencia", "Madrid"],
               "company_words": ["Distribuciones", "Bodegas", "Conservas", "Comercial"],
               "cif_field": "AccountNumber"},
  "contacts_per_account": [1, 3],
  "opportunities": {"per_account": [0, 3],
                    "stages": {"Prospecting": 3, "Qualification": 3, "Needs Analysis": 2,
                               "Proposal/Price Quote": 2, "Negotiation/Review": 1,
                               "Closed Won": 3, "Closed Lost": 1},
                    "amount": [6000, 90000],
                    "products": ["Renovación anual", "Ampliación", "Proyecto nuevo"],
                    "extra_fields": {}},
  "tasks_per_opportunity": [0, 2],
  "cases": {"count": 0},
  "leads": {"count": 8}
}
```
Bloques opcionales: pon `count: 0` o elimínalos. En `accounts` y `opportunities`,
`extra_fields` añade valores fijos a todo el relleno y `random_fields` reparte valores al azar
(`{"Canal__c": ["Distribuidor", "HORECA"]}`): así los campos custom de la demo nunca quedan vacíos.

## `datos/heroes.json`
Mismo formato que la spec de `build_seed.py` (`{"objects":[{"sobject":…,"records":[…]}]}`), con
`ref` legibles (`ACC-ESTRELLA`, `OPP-RIESGO-1`). El relleno puede referenciarlos: las tareas y
contactos de relleno nunca se cuelgan de protagonistas para no ensuciar sus pantallas.

## `datos/HISTORIA-DATOS.md`
Una tabla corta para el SE: registro protagonista → qué representa → en qué escena aparece → qué
hay que señalar. Es lo que permite ensayar sin buscar.

## Documentos adjuntos (opcional)
Si una escena enseña ficheros (una propuesta, un contrato), genera PDFs sencillos y súbelos como
Files del registro (`sf data create file --file <pdf> --parent-id <id>` si la versión de sf lo
incluye; si no, tarea de persona). Contenido ficticio y coherente con los datos.
