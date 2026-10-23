# MANIFIESTO DE NECESIDADES — Cliente de prueba — v1 (desde scan de CPQ Scout)

**Estado de revisión:** BORRADOR
**Cliente:** Cliente de prueba · **Sector:** <completar> · **Zona fiscal:** Península (IVA 21%)
**Origen:** Scan de CPQ Scout · **Org objetivo:** <completar — SDO/sandbox con Revenue Cloud provisionado>

<!-- Generado automáticamente desde scan_id scan-sample-0001 de CPQ Scout
     (org Cliente de prueba (sandbox), 00D000000000SAMPLE, escaneado 2026-10-23T10:00:00Z).
     Complexity score: 42/100, riesgo medium.
     Este documento NO decide nada por sí mismo: el SE o el cliente confirma la modalidad antes
     de pasar al manifiesto definitivo (MANIFIESTO.md de nespon-brief-to-demo si es DEMO, o
     MANIFIESTO-POC.md de esta skill con --modalidad poc si es POC/Migración). -->

## 1. Necesidades (NEC-n) y semáforo
| Estado | ID | Necesidad | Situación / nota del scan | Información pendiente | Fuente |
|--------|-----|-----------|----------------------------|------------------------|--------|
| 🟡 | NEC-1 | Migrar de Salesforce CPQ a Revenue Cloud: 180 productos activos, 12 bundles, 950 quotes históricas | Necesidad global, se concreta en las filas siguientes | Confirmar prioridades con el cliente | Scan CPQ Scout |
| 🔴 | NEC-2 | `SBQQ__QuoteProcess__c (QCP personalizado)` (1 registros) → Sin equivalente estándar identificado [Reescritura] | Script QCP calcula margen combinando coste de un sistema externo (no visible en la org); no hay integración documentada equivalente en RLM | Confirmar impacto en negocio; probablemente requiere desarrollo o rediseño de proceso | Scan CPQ Scout |
| 🟡 | NEC-3 | `SBQQ__ProductOption__c` (310 registros) → ProductRelationship [Rediseño] | Jerarquía de bundles usa reglas de opción no triviales; requiere revisar equivalencia con Product Relationship Type en RLM | Confirmar si el mecanismo detectado es correcto y si hace falta reproducirlo exacto | Scan CPQ Scout |
| 🟡 | NEC-4 | `SBQQ__PriceRule__c` (18 registros) → PricingRule / DecisionTable [Rediseño] | 2 price rules invocan Apex (lookup de coste externo); el resto son condiciones estándar | Confirmar si el mecanismo detectado es correcto y si hace falta reproducirlo exacto | Scan CPQ Scout |
| 🟢 | NEC-5 | `SBQQ__Quote__c` (950 registros) → Quote [Directa] | Mapeo 1:1, sin lógica custom detectada | Ninguna | Scan CPQ Scout |
| 🟢 | NEC-6 | `SBQQ__QuoteLine__c` (4200 registros) → QuoteLineItem [Directa] | Mapeo 1:1 | Ninguna | Scan CPQ Scout |
| 🟢 | NEC-7 | `SBQQ__DiscountSchedule__c` (6 registros) → PriceAdjustmentSchedule [Directa] | Tramos simples por cantidad, sin código | Ninguna | Scan CPQ Scout |

### Resumen
🟢 Claros: 3 · 🟡 Parciales: 2 · 🔴 Indefinidos/bloqueantes: 1 ·
Total: 6

## 2. Preguntas de refinamiento
| Prioridad | Requisito | Pregunta | Motivo |
|-----------|-----------|----------|--------|
| 🔴 | NEC-1 | ¿Los mecanismos marcados 🟡/🔴 son los prioritarios para el cliente, o hay procesos manuales fuera de CPQ que también haya que cubrir? | Decide el alcance mínimo de la modalidad elegida |
| 🟡 | NEC (🔴) | De los 1 mecanismo(s) en rojo, ¿cuáles son imprescindibles para una primera entrega y cuáles se pueden dejar fuera de alcance explícitamente? | Evita que una POC de migración intente cubrir todo el proyecto |

## 3. Modalidad propuesta
| Modalidad | Estado | Justificación | Pendientes |
|-----------|--------|----------------|------------|
| DEMO | 🟡 | Posible como segunda entrega tras validar la POC. | Confirmar escenario con el cliente |
| POC (migración) | 🟡 | Hay 1 mecanismo(s) de riesgo alto (`Reescritura` o `risk=high`) cuya equivalencia en RLM no es obvia: antes de prometer nada hay que comprobarlo. | Confirmar alcance mínimo con el SE |

**Propuesta:** **POC (migración)**. Hay 1 mecanismo(s) de riesgo alto (`Reescritura` o `risk=high`) cuya equivalencia en RLM no es obvia: antes de prometer nada hay que comprobarlo.
Esta es una propuesta técnica, no una aprobación del cliente — confirmar antes de generar el
manifiesto definitivo.

## 4. Decisión (a rellenar tras confirmar)
**Modalidad confirmada:** — · **Confirmado por:** — · **Fecha:** —
**Alcance mínimo acordado:** <completar tras confirmación>
