# Playbook — Field Service

## Org y licencias
Trial de Field Service o SDO. Una Developer Edition normal no trae el paquete gestionado de Field
Service ni sus permission set licenses. Pre-flight: `PackageLicense` con namespace `FSL` y
`PermissionSetLicense` que contenga "Field Service". Si no están, **para**.

## Escenas canónicas (elige 3-5)
| # | Escena | Qué enseña | Wow | Plan B |
|---|---|---|---|---|
| 1 | **Del caso a la orden de trabajo** | El cliente reporta una avería; un clic crea la Work Order con el activo | El técnico ya sabe qué equipo es | WO ya creada |
| 2 | **Consola del despachador** | Gantt con técnicos, citas y huecos; programar con un clic según skills y zona | ⭐ la cita cae en el técnico correcto sola | Cita ya programada |
| 3 | **App móvil del técnico** | Agenda del día, historial del activo, checklist y piezas | ⭐ el técnico ve el histórico antes de entrar | Capturas del móvil en el ensayo |
| 4 | **Cierre con firma** | Informe de servicio con firma del cliente generado en el móvil | El cliente recibe el informe al momento | PDF de ejemplo |
| 5 | **Mantenimiento preventivo** | Maintenance Plan que genera las órdenes futuras | Adiós al "llaman cuando se rompe" | Enseñar el plan y sus WO |

Demo básica: **1 → 2 → 3 → 4**.

## Por CLI
- Permission sets de FSL (Admin, Dispatcher, Resource) asignados; el paquete trae los suyos:
  búscalos en `PermissionSet` por label "Field Service" y asígnalos.
- Datos (spec escrita tras `sf sobject describe` de cada objeto): OperatingHours + TimeSlots,
  ServiceTerritory (Murcia, Alicante), ServiceResource (3 técnicos ligados a usuarios), ServiceTerritoryMember,
  Skill/ServiceResourceSkill si existen en la org, WorkType ("Revisión caldera", "Avería
  climatización"), Account/Contact/Asset (equipos con número de serie e instalación hace años),
  Cases y 6-8 WorkOrder + ServiceAppointment repartidas en `TODAY` y `TODAY+1`.
- Direcciones reales de calle (no de personas) para que el Gantt y el mapa las ubiquen.

## Manual
- Field Service Admin → Field Service Settings: ejecutar la optimización/ajustes iniciales que pida
  el paquete (Scheduling policies por defecto).
- Instalar la app móvil Field Service en el móvil del SE y loguearse con el técnico demo.
- Usuarios técnicos: crear 2-3 usuarios (llegará un email de activación a la dirección del SE).

## Verificación
- `SELECT COUNT() FROM ServiceAppointment WHERE SchedStartTime = TODAY` ≥ 3 (si programadas).
- Abrir la consola del despachador y ver territorios y citas.

## Trampas
Territorio sin Operating Hours o miembros → Gantt vacío. Direcciones sin geocodificar → no hay
mapa. Probar el login móvil el día antes.
