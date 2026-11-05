# Playbook — Analítica (CRM Analytics / Tableau)

## Org y licencias
Licencias de CRM Analytics o Tableau (Next) en la org o SDO. Pre-flight: `PermissionSetLicense`
con "Analytics" o "Tableau". Si no hay, los dashboards estándar de Salesforce suelen bastar para una
demo de visibilidad: dilo.

## Escenas canónicas
| # | Escena | Qué enseña | Wow |
|---|---|---|---|
| 1 | **Dashboard de dirección** | KPIs comerciales o de servicio con drill-down | ⭐ del total al registro en dos clics |
| 2 | **Pregunta en lenguaje natural** | Preguntar a los datos y obtener el gráfico | La Dirección se sirve sola |
| 3 | **Predicción** | Probabilidad de cierre / riesgo de baja con factores explicados | Saber por qué, no solo qué |
| 4 | **En el flujo de trabajo** | El gráfico dentro de la ficha de cuenta | Analítica donde se decide |

## Por CLI
Datos con **volumen e histórico** (100-300 oportunidades o casos repartidos en los últimos 12
meses con offsets): sin historia, la analítica no luce. Usa la spec de Sales/Service ampliada.

## Manual
Crear la app/dashboard desde plantilla o lens, programar el dataflow/recipe y esperar a que corra.

## Trampas
Dataset sin refrescar tras recargar datos. Programar el refresco tras cada reset.
