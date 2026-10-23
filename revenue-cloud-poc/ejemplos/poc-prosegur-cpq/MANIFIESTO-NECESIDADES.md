# MANIFIESTO DE NECESIDADES — Prosegur Alarms (RFQ Proyecto CPQ) — v1

**Estado de revisión:** BORRADOR
**Cliente:** Prosegur Alarms · **Sector:** Seguridad / Alarmas · **Zona fiscal:** España, Portugal y LATAM (multi-país, multi-impuesto)
**Origen:** RFQ — hoja "CPQ" del documento `01 - RFQ Proyecto CPQ Alarmas - Requerimientos Técnicos y Funcionales.xlsx` (25 requisitos, `Orden.Req` 1-22 en "Funcionalidades Generales" y 1-3 en "Integración") · **Org objetivo:** <completar — SDO/sandbox con Revenue Cloud provisionado>

<!-- La hoja "Aspectos Generales" del mismo RFQ (178 filas) NO está incluida aquí: son criterios de
plataforma/seguridad/GDPR/soporte/presencia de mercado con columnas de respuesta de RFP
(Valoración, Descripción Respuesta, SKU, Esfuerzo), no necesidades de negocio para una DEMO/POC.
Es un tipo de entregable distinto (respuesta a RFP), fuera del alcance de esta skill hoy. -->

## 1. Necesidades (NEC-n) y semáforo
| Estado | ID | Necesidad | Relevancia RFQ | Información pendiente | Fuente |
|--------|-----|-----------|-----------------|------------------------|--------|
| 🟢 | NEC-1 | Gestión de catálogo de productos: alta, baja, modificación (ABM) | Crítico | Ninguna | CPQ Orden.Req 1 |
| 🟢 | NEC-2 | Relaciones jerárquicas entre productos: bundles con elementos obligatorios y opcionales | Muy Importante | Ninguna | CPQ Orden.Req 2 |
| 🟢 | NEC-3 | Generar cotizaciones ligadas a una oportunidad | Crítico | Ninguna | CPQ Orden.Req 3 |
| 🟢 | NEC-4 | Gestionar listas de precios | Muy Importante | Ninguna | CPQ Orden.Req 4 |
| 🟡 | NEC-5 | Filtrar listas de precios | Muy Importante | Falta el criterio de filtrado (¿por canal, país, segmento de cliente?) | CPQ Orden.Req 5 |
| 🟢 | NEC-6 | Aplicar descuentos tanto en bundles como en productos individuales | Muy Importante | Ninguna | CPQ Orden.Req 6 |
| 🟡 | NEC-7 | Controlar el margen de ganancia, de la cotización total y por producto | Importante | Falta cómo se calcula el coste/margen (¿viene de un campo de coste del producto, de una integración?) | CPQ Orden.Req 7 |
| 🟢 | NEC-8 | Soporte de procesos de aprobación | Deseable | Ninguna (falta la regla de negocio exacta — ver NEC-21 y el caso de descuento con aprobación) | CPQ Orden.Req 8 |
| 🟢 | NEC-9 | Gestión de promociones y descuentos (ABM) | Crítico | Ninguna | CPQ Orden.Req 9 |
| 🟡 | NEC-10 | Filtrado y recomendación de promociones/descuentos según variables y condiciones dinámicas | Muy Importante | Falta qué variables/condiciones concretas (¿volumen, cliente, producto, fecha?) | CPQ Orden.Req 10 |
| 🟢 | NEC-11 | Aplicación de promociones dentro de cotizaciones | Crítico | Ninguna | CPQ Orden.Req 11 |
| 🟢 | NEC-12 | Gestionar reglas de precios (ABM) | Muy Importante | Ninguna | CPQ Orden.Req 12 |
| 🟡 | NEC-13 | Aplicación automática de reglas de precio cuando se cumplan condiciones dinámicas | Importante | Falta qué condiciones concretas disparan cada regla | CPQ Orden.Req 13 |
| 🟢 | NEC-14 | Gestionar productos con precio recurrente (evergreen) y productos de precio único (one-time) | Crítico | Ninguna | CPQ Orden.Req 14 |
| 🟢 | NEC-15 | Generar documento PDF de oferta, basado en plantilla | Importante | Ninguna | CPQ Orden.Req 15 |
| 🟡 | NEC-16 | Gestión de multi-impuestos | Crítico | Falta el detalle de impuestos por país (IVA España/Portugal, impuestos LATAM) | CPQ Orden.Req 16 |
| 🔴 | NEC-17 | Gestión de penalizaciones por baja anticipada, parametrizadas desde el catálogo | Muy Importante | Falta la fórmula/regla de cálculo de la penalización y qué la dispara | CPQ Orden.Req 17 |
| 🟢 | NEC-18 | Capacidad de extracción de datos | Importante | Ninguna (genérico — confirmar destino/formato si es relevante para una POC) | CPQ Orden.Req 18 |
| 🟢 | NEC-19 | Las cotizaciones solo pueden ser vistas por su propietario | Importante | Ninguna | CPQ Orden.Req 19 |
| 🟡 | NEC-20 | Gestionar incompatibilidades entre promociones/descuentos | Importante | Falta qué combinaciones son incompatibles | CPQ Orden.Req 20 |
| 🟡 | NEC-21 | Gestión de cambios en el ciclo de vida: amends, up-selling, cross-selling, cancelaciones | Crítico | Se entiende el concepto; falta la regla de negocio por tipo de cambio | CPQ Orden.Req 21 |
| 🟡 | NEC-22 | Capacidad de procesar un alto volumen de cotizaciones | Muy Importante | Falta la cifra de volumen esperado (cotizaciones/mes o pico) | CPQ Orden.Req 22 |
| 🔴 | NEC-23 | Capacidad de usar omnicanalidad | Muy Importante | Término muy amplio: no se especifica qué canales concretos (web, app, email, WhatsApp...) | CPQ Integración Orden.Req 1 |
| 🔴 | NEC-24 | Integración con el sistema crediticio de cada país (España, Portugal, LATAM) para cotización y cierre de oportunidad | Crítico | No se especifica qué sistema(s) crediticio(s) ni protocolo/API | CPQ Integración Orden.Req 2 |
| 🔴 | NEC-25 | Integración con distintos facturadores | Crítico | No se especifica qué facturador(es) ni mecanismo de integración | CPQ Integración Orden.Req 3 |

### Resumen
🟢 Claros: 13 · 🟡 Parciales: 8 · 🔴 Indefinidos/bloqueantes: 4 · Total: 25

## 2. Preguntas de refinamiento
| Prioridad | Requisito | Pregunta | Motivo |
|-----------|-----------|----------|--------|
| 🔴 | NEC-24, NEC-25 | ¿Qué sistema(s) crediticio(s) y qué facturador(es) hay que integrar en cada país? ¿Hay ya una API o solo acceso manual? | Sin esto no se puede diseñar ni demostrar el cierre de oportunidad real; probablemente son dependencias técnicas fuera del alcance de una primera DEMO/POC |
| 🔴 | NEC-23 | "Omnicanalidad" es muy amplio — ¿qué canal concreto es prioritario para el primer alcance (web self-service, app de comerciales, WhatsApp...)? | Decide si esto entra en el alcance mínimo o se deja fuera explícitamente |
| 🔴 | NEC-17 | ¿Cómo se calcula hoy la penalización por baja anticipada (fórmula, qué la dispara, sobre qué base)? | Sin la fórmula no se puede ni diseñar ni simular con datos ficticios creíbles |
| 🟡 | NEC-5, NEC-10, NEC-13, NEC-20 | Para el pricing dinámico (filtros de lista de precios, reglas y promociones condicionales, incompatibilidades): ¿puedes dar 2-3 ejemplos reales de reglas que usan hoy (aunque sea en Excel o de memoria)? | Sin ejemplos concretos, el diseño usa condiciones ficticias que pueden no representar el caso real del cliente |
| 🟡 | NEC-7 | ¿De dónde viene el coste para calcular el margen (campo de coste en el producto, integración con otro sistema)? | Decide si el cálculo de margen es estándar o necesita una fuente de datos adicional |
| 🟡 | NEC-16 | ¿Qué impuestos concretos aplican por país (tipos, cuándo varían)? | Define si el motor de impuestos estándar de Revenue Cloud cubre el caso o hace falta algo adicional |
| 🟡 | NEC-21 | De los 4 tipos de cambio de ciclo de vida (amends, up-sell, cross-sell, cancelaciones), ¿cuál es el más urgente de demostrar primero? | Evita que el alcance mínimo intente cubrir los 4 a la vez |
| 🟡 | NEC-22 | ¿Qué volumen de cotizaciones simultáneas/mensuales maneja hoy Prosegur? | Decide si hace falta diseñar o solo mencionar la capacidad (no se puede "demostrar" volumen alto en una DEMO de datos ficticios) |

## 3. Modalidad propuesta
| Modalidad | Estado | Justificación | Pendientes |
|-----------|--------|----------------|------------|
| DEMO | 🟡 | Hay un recorrido claro y de alto impacto con los 🟢 (catálogo → bundle → cotización → descuento/promoción → aprobación → PDF) que ya se puede mostrar con datos ficticios | Acotar qué 🟡 se representan con supuestos explícitos y cuáles quedan fuera |
| POC | 🟡 | Los 4 🔴 son candidatos reales a POC: integraciones (crediticio, facturador), omnicanalidad y la fórmula de penalización — son incertidumbres técnicas/de negocio concretas, no solo falta de "impacto" | Formular una hipótesis por cada 🔴 que se quiera comprobar, y confirmar cuál se prioriza primero |

**Propuesta:** dos entregas separadas, no una sola. **DEMO** primero — recorrido comercial completo
con los 13 requisitos 🟢 y los 🟡 resolubles con supuestos (precio escalonado, aprobación, ciclo de
vida básico), que ya demuestra la mayor parte del valor de Revenue Cloud sin tocar los puntos
indefinidos. **POC** después, acotada a 1-2 de los 🔴 que Prosegur priorice (probablemente las
integraciones de crédito/facturación, que son las más bloqueantes y menos "estándar" para
verificar contra la documentación oficial / `rlm-skill` antes de prometer nada). Mezclar ambas en
un primer entregable sería demasiado alcance para una primera vuelta.

## 4. Decisión
**Modalidad confirmada:** POC · **Confirmado por:** Kevin · **Fecha:** 2026-10-20
**Alcance mínimo acordado:** pendiente de elegir qué incertidumbre(s) 🔴 prioriza la POC (ver
pregunta abierta en el chat). No se confirma DEMO como entrega separada por ahora — foco en POC.

## 4bis. Contexto adicional del cliente (de "Aspectos Generales", no son NEC-n)
Relevante para diseñar la POC, aunque no es una necesidad funcional de CPQ en sí:
- **Multi-país**: plataforma debe operar en varios países (coherente con NEC-24: integración
  crediticia distinta por país — España/Portugal/LATAM).
- **Multi-moneda**: tanto dentro de un país como entre países/organizaciones — relevante si la
  POC toca pricing o integraciones que muevan importes.
- **Multi-empresa**: Prosegur Alarms puede operar como varias entidades/organizaciones dentro de
  la misma plataforma.
- **Movilidad con app nativa offline para técnicos de instalación** — contexto de negocio (hay
  técnicos de campo), aunque no es parte de las 25 necesidades de CPQ ya listadas.
- **Integración con sistemas on-premise y cloud vía APIs/servicios web** — confirma que las
  integraciones de NEC-24 (crediticio) y NEC-25 (facturador) son plausibles técnicamente a nivel
  de plataforma; sigue faltando CUÁL sistema concreto en cada caso.
- **Alta disponibilidad / centro de respaldo** — si la POC toca algo transaccional (cotización →
  cierre), puede ser relevante como limitación a documentar, no como objeto de la hipótesis.

## 5. Fuera de alcance de este manifiesto
La hoja "Aspectos Generales" del mismo RFQ (178 requisitos de plataforma, seguridad, GDPR, soporte,
presencia de mercado, con columnas de respuesta `Valoración`/`SKU`/`Esfuerzo`) es una **respuesta a
RFP**, no una necesidad de negocio para una DEMO/POC. No se ha clasificado aquí. Si Prosegur la
necesita respondida, es un entregable distinto — decide si quieres que lo trabajemos aparte.
