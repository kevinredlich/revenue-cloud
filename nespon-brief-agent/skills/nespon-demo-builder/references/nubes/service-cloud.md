# Playbook — Service Cloud

## Org y licencias
Developer Edition suele traer lo necesario para una demo básica. Comprobar: que el usuario de demo
puede usar Service Cloud (`UserPermissionsSupportUser` en User o feature license equivalente) y si
Knowledge está disponible (`UserPermissionsKnowledgeUser`).

## Escenas canónicas (elige 3-5)
| # | Escena | Qué enseña | Wow | Plan B |
|---|---|---|---|---|
| 1 | **Service Console** | Caso con cliente, historial y casos relacionados en una sola pantalla | ⭐ todo el contexto sin cambiar de sistema | Caso ya abierto en pestaña |
| 2 | **Entrada multicanal** | Un caso entra por formulario web o email y se asigna a la cola correcta | Asignación automática por tipo | Caso de ejemplo ya asignado |
| 3 | **SLA visible** | Entitlement con milestone y cuenta atrás en el caso | ⭐ el agente ve cuánto le queda antes de incumplir | Caso con milestone ya en rojo |
| 4 | **Knowledge** | Artículo sugerido al abrir el caso | Respuesta sin buscar | Buscar el artículo a mano |
| 5 | **Macro** | Un clic responde al cliente, cambia estado y registra | Cinco pasos en uno | Enseñar la macro sin ejecutar |
| 6 | **Dashboard de servicio** | Casos por estado, SLA en riesgo, carga por agente | Visión del supervisor | Report de casos abiertos |

Demo básica recomendada: **1 → 2 → 3 → 6**.

## Por CLI
- StandardValueSet `CaseType` con valores "Incidencia", "Consulta", "Solicitud" (retrieve → editar → deploy; los datos los usan).
- Queue "Soporte Nivel 1" (Case) y AssignmentRules de Case: Type = "Incidencia" y Priority = "High" → cola.
- CustomApplication de consola "Servicio Nespon" (navType Console) con Cases, Accounts, Contacts.
- EntitlementSettings (activar), EntitlementProcess con un milestone "Primera respuesta"; los
  Entitlements de las cuentas se cargan como datos.
- Web-to-Case: activar en settings; el formulario HTML lo genera el agente como fichero local para
  abrir en el navegador durante la demo.
- Report y dashboard en `DemoNespon`.
- Datos: `assets/seed-service-cloud.json`. Tras desplegar el EntitlementProcess, obtén su Id
  (`SELECT Id FROM SlaProcess WHERE Name = '...'`) y pásalo con `--var SLA_PROCESS_ID=<Id>`. Para que el SLA salga en rojo, activar Set Audit Fields
  y cargar `CreatedDate` de 2-3 casos como `NOW-26h`.

## Manual
- Omni-Channel (si se quiere enseñar enrutamiento en tiempo real): presencia y canales en Setup.
- Knowledge: activar en Setup si no lo está, y crear 2 artículos (el agente redacta el texto).
- Macros: se crean en la consola (el agente da los pasos exactos).

## Verificación
- `SELECT COUNT() FROM Case WHERE IsClosed = false` ≥ 8; `SELECT COUNT() FROM Entitlement` ≥ 1.
- Abrir un caso en la consola y ver el milestone.

## Trampas
- Milestones calculados desde `CreatedDate`: sin audit fields todo sale "en plazo".
- Web-to-Case con email real de respuesta automática: desactivar auto-response o usar @example.com.
