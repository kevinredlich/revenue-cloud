# Playbook — Salesforce Maps

## Org y licencias
Paquete gestionado de Maps con licencias asignadas (namespace `maps`). Pre-flight en
`PackageLicense`. Suele combinarse con Sales o Field Service.

## Escenas canónicas
| # | Escena | Qué enseña | Wow |
|---|---|---|---|
| 1 | **Mapa de cuentas** | Clientes coloreados por facturación o riesgo | ⭐ el pipeline se ve sobre el territorio |
| 2 | **Ruta del día** | Ruta optimizada con las visitas de hoy | Menos kilómetros, más visitas |
| 3 | **Check-in** | Registro de visita desde el móvil | Actividad real, no declarada |
| 4 | **Territorios** | Reparto equilibrado de cuentas entre comerciales | Territorios justos con datos |

## Por CLI
Datos: 30-40 Accounts con **direcciones reales de calles comerciales** en 2-3 ciudades (nunca
domicilios de personas), campo de facturación anual y Owner. Tareas/visitas en `TODAY`.

## Manual
Geocodificar las cuentas (proceso del paquete), crear capas guardadas (marker layers) y la
plantilla de ruta.

## Trampas
Cuentas sin geocodificar → mapa vacío. Lanzar la geocodificación justo tras cargar datos.
