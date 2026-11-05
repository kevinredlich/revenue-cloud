# MANIFIESTO DE DESARROLLO (POC) — Bodegas Altiplano — v1

**Estado de revisión:** BORRADOR
**Revisado por:** — · **Fecha de aprobación:** —
**Cliente:** Bodegas Altiplano SA · **Sector:** Vino (bodega) · **Zona fiscal:** Península (IVA 21%)
**Nube ancla:** Revenue Cloud (RLM) · **Nubes de apoyo:** — · **Org objetivo:** SDO con Revenue Cloud provisionado
**Incertidumbre:** ¿El motor de pricing estándar de Revenue Cloud puede aplicar un descuento por volumen escalonado (no plano) sin desarrollo a medida?
**Fuentes consultadas (rlm-skill):** `subskills/revenue-cloud-data-model/domains/pricing.md`; `references/schema-diff/264-schema.json`; `references/apis/pricing-business-apis-v68.md`; `references/revenue-cloud-permissions.md`; Help 264 "Create Price Adjustment Tiers for Volume Discounts" y "Volume and Tier Based Discounts"
**Restricciones del SE:** Solo mecanismos estándar de Pricing; nada de Apex para el cálculo
**Supuestos clave:** La org tiene Revenue Cloud (RLM) provisionado; el tipo de ajuste `Percentage` se confirma con describe (sección 7); los tramos y el precio base son los del ejemplo
**Reparto:** IA 8 (72%) · IA+Revisión 0 · Persona 3 · **Niveles:** 🟢 6 · 🔵 5 · 🟠 0

## 1. Contexto y necesidad de origen
| ID | Necesidad / duda del cliente | Origen |
|----|-------------------------------|--------|
| NEC-1 | El comercial da descuentos por volumen "a ojo" en Excel; quieren que el sistema los calcule solo | Brief |
| NEC-2 | El descuento no es un % fijo: crece por tramos de cantidad | Brief |

## 2. Hipótesis y experimento
**Hipótesis en una frase:** El motor de pricing estándar puede resolver un descuento escalonado por tramos de cantidad sin código.

| ID | Hipótesis | Necesidad | Criterio de éxito | Si no se cumple / no concluyente |
|----|-----------|-----------|--------------------|-----------------------------------|
| HIP-1 | Un Price Adjustment Schedule con tramos por cantidad calcula el descuento correcto sin Apex | NEC-1, NEC-2 | Un pedido de 150 unidades aplica el tramo de descuento correspondiente y el total coincide con el cálculo manual | Si el motor no soporta tramos por cantidad en esta edición, queda NO VALIDADA y se documenta la alternativa (desarrollo o proceso manual) |

| ID | Paso del experimento | Hipótesis | Entrada | Resultado esperado | Evidencia requerida |
|----|------------------------|-----------|---------|----------------------|------------------------|
| EXP-1 | Configurar Price Adjustment Schedule con 3 tramos (1-49 / 50-99 / 100+) sobre un producto de prueba | HIP-1 | Producto "Vino Reserva Caja 6u" con precio base 42 (moneda de la org) | El schedule queda activo (`IsActive`) con sus 3 tramos | Captura del schedule activo en la app Price Management |
| EXP-2 | Generar una Quote Line de 150 unidades del producto de prueba | HIP-1 | Quote con el producto y cantidad 150 | Tras el cálculo de precios de la quote, el precio unitario neto de la línea corresponde al tramo 100+ | Consulta SOQL de `Quantity`, `NetUnitPrice` y `TotalPrice` de la línea |
| EXP-3 | Comparar el total calculado por el sistema contra el cálculo manual del tramo 100+ | HIP-1 | Mismos datos que EXP-2 | El total coincide (±0,01 por redondeo) | Captura con ambos cálculos lado a lado |

## 3. Componentes
| ID | Paso | Componente | Tipo | Origen | Especificación | Nivel | Responsable | Motivo | Tamaño | Estado |
|----|------|------------|------|--------|----------------|-------|-------------|--------|--------|--------|
| CMP-1 | EXP-1 | Verificar licencia y permisos de pricing | Setup | N/A | Comprobar la PermissionSetLicense `CorePricingDesignTime` disponible y asignar los permission sets `CorePricingDesignTimeUser` y `CorePricingAdmin` al usuario de la prueba | 🟢 | Persona | Licencias y asignación de permisos solo visibles en Setup | S | Pendiente |
| CMP-2 | EXP-1 | Producto de prueba | Product2 | Estándar SF | "Vino Reserva Caja 6u" | 🟢 | IA | — | S | Pendiente |
| CMP-3 | EXP-1 | Precio de lista | PricebookEntry | Estándar SF | `UnitPrice` 42 (moneda de la org, sin fijar `CurrencyIsoCode`) en el Standard Price Book para CMP-2 y el selling model de CMP-4 | 🟢 | IA | — | S | Pendiente |
| CMP-4 | EXP-1 | Modelo de venta | ProductSellingModel | Estándar RLM | Reutilizar un selling model `OneTime` existente (consulta de pre-vuelo); crear uno solo si no existe (R10) | 🟢 | IA | — | S | Pendiente |
| CMP-5 | EXP-1 | Programa de ajuste por volumen | PriceAdjustmentSchedule | Estándar RLM | `ScheduleType` = `Volume`, `AdjustmentMethod` = `Range`; inactivo hasta cargar los tramos | 🔵 | IA | — | S | Pendiente |
| CMP-6 | EXP-1 | Tramos de descuento | PriceAdjustmentTier | Estándar RLM | 3 registros sobre CMP-2, CMP-4 y CMP-5: `TierType` = `AdjustmentPercentage`; `TierValue` 0 / 5 / 12; `LowerBound`-`UpperBound` 1-49 / 50-99 / 100+; misma fecha efectiva, tramos consecutivos y sin solape | 🔵 | IA | — | M | Pendiente |
| CMP-7 | EXP-1 | Activar programa y refrescar tabla | Setup | Estándar RLM | Activar CMP-5 (`IsActive`) y refrescar la decision table "Volume Discount Entries" en Lookup Tables | 🔵 | Persona | Pantallas de la app Price Management y Lookup Tables | S | Pendiente |
| CMP-8 | EXP-2 | Pricing procedure con elemento de descuento por volumen | Pricing procedure | Estándar RLM | Elemento Volume Discount con la constante `VolumePriceAdjustmentScheduleId` apuntando a CMP-5 y la decision table refrescada en CMP-7 | 🔵 | Persona | Se construye en el Pricing Procedure Builder (interfaz) | M | Pendiente |
| CMP-9 | EXP-2 | Quote de prueba | Quote | Estándar SF | `Pricebook2Id` = Standard Price Book; `OpportunityId` de la oportunidad de DAT-1 | 🔵 | IA | — | S | Pendiente |
| CMP-10 | EXP-2 | Líneas de prueba | QuoteLineItem | Estándar SF | `Quantity` 30 / 75 / 150 sobre CMP-2, con `PricebookEntryId` de CMP-3 y `ProductSellingModelId` de CMP-4; precios calculados con la API de cálculo de precios (`references/apis/pricing-business-apis-v68.md`) | 🟢 | IA | — | S | Pendiente |
| CMP-11 | EXP-3 | Consulta de verificación | Query | Estándar SF | SOQL sobre `QuoteLineItem`: `Quantity`, `ListPrice`, `NetUnitPrice`, `TotalPrice` | 🟢 | IA | — | S | Pendiente |

## 3.1 Verificación de nombres y valores de API
| Objeto | Campo / valor | Valor usado | Clase | Referencia |
|--------|---------------|-------------|-------|------------|
| PriceAdjustmentSchedule | ScheduleType | `Volume` | DOC | `references/schema-diff/264-schema.json` (PriceAdjustmentSchedule.ScheduleType: Volume, Term, Attribute, Bundle, Custom) |
| PriceAdjustmentSchedule | AdjustmentMethod | `Range` | DOC | `references/schema-diff/264-schema.json` (PriceAdjustmentSchedule.AdjustmentMethod: Range, Slab); `salesforce-help/264/dev-guide/salesforce-pricing.md` |
| PriceAdjustmentSchedule | IsActive | `IsActive` | DOC | `references/schema-diff/264-schema.json` (PriceAdjustmentSchedule.IsActive) |
| PriceAdjustmentTier | LowerBound, UpperBound | `LowerBound`, `UpperBound` | DOC | `subskills/revenue-cloud-data-model/domains/pricing.md` (PriceAdjustmentTier) |
| PriceAdjustmentTier | TierType | `AdjustmentPercentage` | DOC | `references/schema-diff/264-schema.json` (PriceAdjustmentTier.TierType: AdjustmentPercentage, AdjustmentAmount, OverrideAmount); Help 264 "Create Price Adjustment Tiers for Volume Discounts" |
| PriceAdjustmentTier | TierValue | `TierValue` | DOC | `references/schema-diff/264-schema.json` (PriceAdjustmentTier.TierValue) |
| PriceAdjustmentTier | Product2Id, ProductSellingModelId, PriceAdjustmentScheduleId | `Product2Id`, `ProductSellingModelId`, `PriceAdjustmentScheduleId` | DOC | `references/schema-diff/264-schema.json` (PriceAdjustmentTier); Help 264 "Create Price Adjustment Tiers for Volume Discounts" |
| PricebookEntry | UnitPrice | `UnitPrice` | DOC | `subskills/revenue-cloud-data-model/domains/pricing.md` (PriceBookEntry) |
| QuoteLineItem | Quantity, NetUnitPrice, TotalPrice | `Quantity`, `NetUnitPrice`, `TotalPrice` | DOC | `references/schema-diff/264-schema.json` (QuoteLineItem) |

## 3.2 Viabilidad por requisito
| Requisito | Vía | Referencia | Matiz / prueba o diseño custom real |
|-----------|-----|------------|--------------------------------------|
| Descuento por volumen con tramos de cantidad | ESTÁNDAR | Help 264 "Create Price Adjustment Tiers for Volume Discounts" y "Volume and Tier Based Discounts" (`salesforce-help/264/help/pricing.md`) | Límites inclusivos y tramos consecutivos sin solape; el schedule debe ser de tipo Volume y estar activo |
| El precio de la línea refleja el tramo al calcular la quote | ESTÁNDAR A VALIDAR | Help 264 "Volume and Tier Based Discounts" (`salesforce-help/264/help/pricing.md`) | Solo si el pricing procedure incluye el elemento Volume Discount y la decision table "Volume Discount Entries" está refrescada; se prueba en EXP-2 |

## 3.3 Decisiones de diseño (mejor alternativa)
| Decisión | Alternativa elegida | Alternativas descartadas | Motivo (encaje RLM, jerarquía, coherencia, mantenimiento, esfuerzo) |
|----------|---------------------|---------------------------|----------------------------------------------------------------------|
| Cómo se aplica el descuento sobre la línea | `AdjustmentMethod` = `Range` (toda la cantidad recibe el descuento de su tramo) | `Slab` (cada tramo descuenta solo sus unidades) | El cliente describe "descuento por volumen" sobre el pedido completo; Range es estándar y coincide con el cálculo manual de los CASO-n. Slab daría otros totales |
| Elemento del pricing procedure | Volume Discount | Tier Discount | El requisito es un descuento por tramos de cantidad ya cubierto por el elemento Volume Discount y sus decision tables; Tier Discount añade lógica acumulada que no se pide |

## 4. Tareas de persona
### CMP-1 — Verificar licencia y permisos de pricing
- **Ruta:** Setup → Permission Set Licenses y Permission Sets (el nombre del menú puede variar).
- **Valores:** licencia `CorePricingDesignTime`; permission sets `CorePricingDesignTimeUser` y `CorePricingAdmin`.
- **Comprobar:** la licencia aparece disponible y el usuario de la prueba tiene los permission sets asignados.
- **Desbloquea:** CMP-6

### CMP-7 — Activar programa y refrescar tabla
- **Ruta:** app Price Management → Price Adjustment Schedules → CMP-5 → Active; después Lookup Tables → "Volume Discount Entries" → Refresh.
- **Valores:** —
- **Comprobar:** el programa figura activo y la fecha de último refresco de la tabla es posterior a la creación de los tramos.
- **Desbloquea:** CMP-8

### CMP-8 — Pricing procedure con elemento de descuento por volumen
- **Ruta:** Pricing Procedure Builder → añadir el elemento Volume Discount (el nombre del menú puede variar).
- **Valores:** constante `VolumePriceAdjustmentScheduleId` = Id de CMP-5.
- **Comprobar:** el procedure se guarda y se activa sin errores.
- **Desbloquea:** CMP-10

## 5. Datos de prueba
Spec: `datos/seed-spec.json` (generada con `fill_data.py`) · Qué representa cada caso: `datos/HISTORIA-DATOS.md`

| ID | Objeto | Registros | Contenido / valores clave | Pasos |
|----|--------|-----------|---------------------------|-------|
| DAT-1 | Account, Opportunity | 1 protagonista | Cuenta de prueba "Distribuidor Test SL" con una oportunidad abierta | EXP-2 |

Casos de prueba con valor esperado (R14): precio unitario y total de la línea con el schedule de CMP-5 en modo `Range` sobre el precio base 42.

| ID | Caso | Entrada | Resultado esperado | Pasos |
|----|------|---------|--------------------|-------|
| CASO-1 | Tramo 1-49 (sin descuento) | Cantidad 30 | Precio unitario 42,00; total 1.260,00 | EXP-2, EXP-3 |
| CASO-2 | Tramo 50-99 (5%) | Cantidad 75 | Precio unitario 39,90; total 2.992,50 | EXP-2, EXP-3 |
| CASO-3 | Tramo 100+ (12%) | Cantidad 150 | Precio unitario 36,96; total 5.544,00 | EXP-2, EXP-3 |

## 6. Orden de construcción
CMP-1 → CMP-2 → CMP-4 → CMP-3 → CMP-5 → CMP-6 → CMP-7 → CMP-8 → DAT-1 → CMP-9 → CMP-10 → CMP-11 → ejecutar EXP-1 → ejecutar EXP-2 → ejecutar EXP-3

## 7. Supuestos y preguntas abiertas
- Supuesto: la org objetivo tiene Revenue Cloud (RLM) provisionado con la licencia Growth o Advanced, no solo Sales Cloud con CPQ heredado.
- Pre-vuelo (Prerrequisitos de la org, R2): consulta de solo lectura de la `PermissionSetLicense` `CorePricingDesignTime`, de los selling models `OneTime` existentes, de un Standard Price Book con productos, y `describe` de `PriceAdjustmentSchedule` y `PriceAdjustmentTier`; moneda corporativa de la org (el diseño no la fija).
- Pregunta para el SE: ¿los tramos reales son los de este ejemplo o el cliente los ha definido en el brief?

## 8. Registro de cambios
- v1: versión inicial a partir de la duda planteada por el comercial.
- v1.1: corregido tras la revisión independiente contra rlm-skill (`ScheduleType`, `TierType`, `AdjustmentMethod`, `PricebookEntry`, pricing procedure, licencias y citas de Help).
