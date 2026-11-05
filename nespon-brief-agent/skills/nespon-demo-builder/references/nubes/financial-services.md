# Playbook — Financial Services Cloud

## Org y licencias
Trial de FSC o SDO. Pre-flight: `PermissionSetLicense` con "Financial Services". Comprobar si el
modelo de datos es el estándar de plataforma (objetos como `FinancialAccount`) o el del paquete
(namespace `FinServ__`) con `sf sobject list --target-org <alias> | grep -i financial`, y escribe la
spec con los nombres que existan.

## Escenas canónicas
| # | Escena | Qué enseña | Wow | Plan B |
|---|---|---|---|---|
| 1 | **Vista 360 del cliente** | Persona y su unidad familiar con cuentas, productos, objetivos y relaciones | ⭐ el patrimonio completo en una pantalla | Record page con componentes |
| 2 | **Relaciones** | Actionable Relationship Center: familia, empresa, asesores | Quién influye en la decisión | Captura del mapa |
| 3 | **Onboarding con Action Plan** | Plan de alta con tareas y plazos (KYC, documentación) | El proceso se vuelve visible y medible | Plan ya iniciado |
| 4 | **Oportunidad de producto** | Pipeline de hipotecas/seguros/inversión | Siguiente mejor acción para el gestor | List view de oportunidades |
| 5 | **Resumen con IA** (si hay Agentforce) | Resumen del cliente antes de la reunión | ⭐ el gestor prepara la cita con un clic | Resumen generado en el ensayo |

Demo básica: **1 → 3 → 4**, más **5** si hay Agentforce.

## Por CLI
Datos: Person Accounts (o Account + Contact según org), household/grupo, 3-4 cuentas financieras
por cliente (corriente, hipoteca, fondo, seguro) con saldos creíbles, 2 objetivos financieros, un
Action Plan Template (si es metadata en la org) y oportunidades. Record page del cliente con los
componentes FSC si hay que ajustarla.

## Manual
Activar Person Accounts si el modelo lo requiere (irreversible: solo en org de demo). ARC:
configurar tipos de relación visibles.

## Trampas
Mezclar el modelo del paquete y el de plataforma. Datos regulatorios reales: todo sintético.
Mencionar MiFID II / IDD / DORA solo si encaja con la audiencia.
