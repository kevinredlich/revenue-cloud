# Playbook — Experience Cloud

## Org y licencias
Developer Edition suele traer pocas licencias de comunidad; compruébalo en `UserLicense`
(Customer Community, Customer Community Plus, Partner Community). Sin licencia externa, no hay login
de portal: **para** o usa una SDO.

## Escenas canónicas
| # | Escena | Qué enseña | Wow | Plan B |
|---|---|---|---|---|
| 1 | **Portal con la marca del cliente** | Sitio de autoservicio con colores y logo | Parece su web, no Salesforce | Captura del sitio |
| 2 | **Autoservicio** | El cliente se loguea, busca en Knowledge y abre un caso | ⭐ el caso aparece al instante en la consola interna | Caso de ejemplo |
| 3 | **Mis datos** | El cliente ve solo sus casos, pedidos o facturas | Seguridad: cada uno ve lo suyo | Login como otro cliente |
| 4 | **Portal de partners** (si aplica) | Registro de oportunidades y leads compartidos | El canal indirecto dentro del CRM | Oportunidad registrada |

Demo básica: **1 → 2 → 3**.

## Por CLI
- Datos: 2 cuentas cliente con Contacts, casos y artículos (si hay Knowledge).
- Usuarios externos: `User` con ProfileId del perfil de comunidad, `ContactId` del contacto, email
  del SE con alias (`se+cliente1@...` si su correo lo admite), tras crear el sitio.
- Sharing set y permission set para que el usuario externo vea sus casos.

## Manual
Setup → Digital Experiences → activar y **crear el sitio desde plantilla** (Customer Service /
Help Center). Branding en Experience Builder (colores y logo del cliente). Añadir perfiles como
miembros y publicar. Crear el sitio a mano es más fiable que desplegar un ExperienceBundle desde
cero.

## Trampas
Olvidar publicar el sitio, o añadir el perfil a miembros. Probar el login externo en ventana
de incógnito antes de la demo.
