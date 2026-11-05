DICTAMEN: CON RESERVAS

# Informe del rlm-verifier — ejemplo-MANIFIESTO-POC.md (Bodegas Altiplano)

Cuarta pasada independiente (las tres anteriores dieron RECHAZADO, RECHAZADO y CON RESERVAS; cada una se corrigió contra rlm-skill antes de repetir).

**Resumen:** ninguna afirmación contradice rlm-skill; valores de API, permisos, cálculos y orden de carga cuadran. Hallazgos bloqueantes: ninguno. Los dos SUPUESTO de la sección 7 están declarados como tales.

## Leído en rlm-skill
`SKILL.md`; `subskills/pricing-wiring/guide.md` (1-60, 130-185, 280-294); `subskills/revenue-cloud-data-model/domains/pricing.md` (10-12, 54-59); `references/schema-diff/264-schema.json` (PriceAdjustmentSchedule, PriceAdjustmentTier, ProductSellingModel, QuoteLineItem, Quote); `references/apis/transaction-management-apis-reference.md` (14-30, 134); `references/apis/pricing-business-apis-v68.md` (38-60); `references/revenue-cloud-permissions.md` (19, 129-132, 174-175); `salesforce-help/264/help/pricing.md` (414-520, 1633, 1691-1790, 2025-2050, 2814-2900); `salesforce-help/264/dev-guide/salesforce-pricing.md` (16751).

## Afirmaciones
| # | Afirmación | Resultado | Evidencia |
|---|---|---|---|
| 1 | ScheduleType=Volume; AdjustmentMethod=Range (Slab alternativa) | CONFIRMADO | 264-schema.json; salesforce-pricing.md:16751; pricing.md:2840-2850 |
| 2 | IsActive, Name, EffectiveFrom del schedule | CONFIRMADO | 264-schema.json; pricing.md:1727-1734 |
| 3 | TierType=AdjustmentPercentage, TierValue, Lower/UpperBound, tramo 100+ sin UpperBound | CONFIRMADO | 264-schema.json; pricing.md:1722-1733; domains/pricing.md:12 |
| 4 | Límites inclusivos, tramos consecutivos | CONFIRMADO | pricing.md:2893-2905 |
| 5 | SellingModelType=OneTime; reutilizar selling model | CONFIRMADO | 264-schema.json |
| 6 | QuoteLineItem.ProductSellingModelId no creable; NetUnitPrice/TotalPrice/ListPrice solo lectura | CONFIRMADO | 264-schema.json (createable=false) |
| 7 | Place Sales Transaction: graph Quote+QuoteLineItem, pricingPref Force/Skip/System | CONFIRMADO | transaction-management-apis-reference.md:21-23 |
| 8 | /connect/core-pricing/pricing solo devuelve precios | CONFIRMADO POR DERIVACIÓN | pricing-business-apis-v68.md:40-50 |
| 9 | PSL CorePricingDesignTime y permission sets | CONFIRMADO | revenue-cloud-permissions.md:19,129,132,175 |
| 10 | Pricing procedure: Pricing Setting, List Price, Volume Discount; constante VolumePriceAdjustmentScheduleId | CONFIRMADO | pricing.md:1741-1790 |
| 11 | Clonar el procedure por defecto | CONFIRMADO POR DERIVACIÓN | pricing-wiring/guide.md:52-54 |
| 12 | Refrescar «Volume Discount Entries» | CONFIRMADO | pricing.md:2032-2045 |
| 13 | No activar justo tras refrescar | CONFIRMADO | pricing.md:2026 |
| 14 | Programa «Standard Price Adjustment Tier» | CONFIRMADO | pricing.md:2828-2834 |
| 15 | Licencia Growth o Advanced | CONFIRMADO | pricing.md:1695-1696 |
| 16 | «Tier Discount añade lógica acumulada» | NO ENCONTRADO (redacción) | pricing.md:414-440 |
| 17 | SUPUESTO: pricingPref persiste el precio en la línea | NO ENCONTRADO, declarado SUPUESTO | transaction-management-apis-reference.md:23 solo da valores |
| 18 | SUPUESTO: enlace procedure clonado ↔ plan de la quote | NO RESPALDADO, declarado SUPUESTO | pricing-wiring/guide.md:130-185 |
| 19 | Viabilidad: ESTÁNDAR + ESTÁNDAR A VALIDAR | CONFIRMADO (clasificación correcta) | pricing.md:461, 2865 |
| 21 | Coherencia interna (IDs, reparto, orden de construcción) | CONFIRMADO | recuento propio |

## Reservas (no bloqueantes) — pendientes de que el SE las resuelva o acepte
1. Los dos SUPUESTO (sección 7) carecen de una consulta de validación real; el pre-vuelo es de solo lectura. Fijar un valor concreto de `pricingPref` en CMP-10 y un criterio NO CONCLUYENTE en EXP-2 si `NetUnitPrice` queda en 42,00.
2. Falta el refresco de la decision table «Price Book Entries» (o Sync Pricing Data) antes de usar List Price (pricing.md:1038, 1098, 1633; pricing-wiring/guide.md:280-286).
3. Reformular el motivo de descarte de Tier Discount con la definición del Help (Volume = un precio para todas las unidades; Tier = precio por rango); quitar «acumulada».
4. Menores: alinear la cabecera (TierType/AdjustmentMethod «se confirman con describe») con 3.1 (DOC); añadir a 3.1 `ListPrice`, `PricebookEntryId`, `EffectiveFrom`; «IA 8 (72%)» sería 73% (8/11 = 72,7%); `TierValue` 0 en el primer tramo sin respaldo literal.

## Cálculos recomprobados
CASO-1 30×42,00 = 1.260,00 · CASO-2 42×0,95 = 39,90 → ×75 = 2.992,50 · CASO-3 42×0,88 = 36,96 → ×150 = 5.544,00 (modo Range: descuento del tramo a toda la cantidad).

## Validador
`validate_manifest_poc.py --strict`: único error, la falta de la línea «Verificación de coherencia (rlm-verifier)» (esperado antes de registrar este dictamen).
