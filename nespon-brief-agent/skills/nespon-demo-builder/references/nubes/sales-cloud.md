# Playbook — Sales Cloud

## Org y licencias
Developer Edition vacía basta. Comprobar: licencia Salesforce, y para la escena de forecast, que el
usuario pueda activarse como usuario de forecasting (campo `ForecastEnabled` en User).

## Escenas canónicas (elige 3-5)
| # | Escena | Qué enseña | Wow | Plan B |
|---|---|---|---|---|
| 1 | **Del lead a la oportunidad** | Lead con actividad → conversión en cuenta, contacto y oportunidad en un clic | Todo el contexto viaja sin reescribir nada | Lead ya convertido |
| 2 | **Path de oportunidad** | Etapas con guía de venta y campos clave por etapa | El comercial sabe qué hacer en cada paso | Enseñar el Path en otra oportunidad |
| 3 | **Dashboard de pipeline y riesgo** | Pipeline por etapa y oportunidades estancadas en rojo | ⭐ lo invisible se ve de un vistazo | List view "Operaciones en riesgo" |
| 4 | **Tarea automática** | Flow que crea el seguimiento cuando una oportunidad entra en riesgo | La plataforma actúa sola, sin código | Tarea ya creada en el ensayo |
| 5 | **Forecast** | Previsión por comercial y por mes con ajuste del manager | ⭐ el forecast deja de vivir en Excel | Report de pipeline por CloseDate |
| 6 | **Móvil** | La misma oportunidad y el dashboard en la app Salesforce | Trabajo en la calle | Captura de la app |

Demo básica recomendada: **1 → 2 → 3 → 4**, más **5** si la audiencia es Dirección.

## Por CLI
- CustomField `Opportunity.Stage_Entered_Date__c` (Date) y `Opportunity.Risk_Level__c`
  (Formula Text: `IF(AND(NOT(IsClosed), TODAY()-Stage_Entered_Date__c>30),"En riesgo","En plazo")`).
- Flow before-save que pone `Stage_Entered_Date__c = TODAY()` al cambiar `StageName` (desplegar
  **inactivo**, activar tras la carga).
- Flow after-save que crea la Task "Revisar operación en riesgo" (inactivo hasta después de cargar).
- PathAssistant de Opportunity con guidance en español por etapa.
- Report "Operaciones abiertas por etapa", list view "Operaciones en riesgo", dashboard
  "Pipeline y Riesgo" en carpeta `DemoNespon`.
- ForecastingSettings (retrieve → activar tipo Opportunity Revenue → deploy) y
  `ForecastEnabled = true` en el usuario de demo. Si el forecast exige jerarquía de roles, crea un
  rol "Dirección Comercial" y asígnalo.
- Datos: `assets/seed-sales-cloud.json` (cuentas, contactos, 12 oportunidades con 3 estancadas,
  2 leads calientes).

## Manual
- Ajustar la jerarquía de forecast en Setup si el deploy no la deja completa.
- Añadir el dashboard a la página de inicio de la app (opcional).

## Verificación
- `SELECT COUNT() FROM Opportunity WHERE Risk_Level__c = 'En riesgo'` = 3.
- `SELECT COUNT() FROM Lead WHERE IsConverted = false` ≥ 2.
- Dashboard presente en `DemoNespon`; Flows en estado Active tras la carga.

## Trampas
- `LastStageChangeDate` no se puede cargar: por eso el campo propio de fecha de etapa.
- CloseDate fuera del trimestre en curso → forecast vacío. Usar offsets cortos.
