# MANIFIESTO DE DESARROLLO (POC) — Cliente de prueba — v1 (PRE-BORRADOR desde scan)

**Estado de revisión:** BORRADOR
**Revisado por:** — · **Fecha de aprobación:** —
**Cliente:** Cliente de prueba · **Sector:** <completar> · **Zona fiscal:** Península (IVA 21%)
**Nube ancla:** Revenue Cloud (RLM) · **Nubes de apoyo:** — · **Org objetivo:** <completar — SDO/sandbox con Revenue Cloud provisionado>
**Incertidumbre:** Migración de Salesforce CPQ a Revenue Cloud — ver hipótesis por mecanismo detectado
**Restricciones del SE:** <completar>
**Reparto:** IA 0 (0%) · IA+Revisión 0 · Persona 0 · **Niveles:** 🟢 0 · 🔵 0 · 🟠 0

<!-- Generado automáticamente desde scan_id scan-sample-0001 de CPQ Scout
     (org Cliente de prueba (sandbox), 00D000000000SAMPLE, escaneado 2026-10-23T10:00:00Z).
     Complexity score: 42/100, riesgo medium.
     ESTE ES UN PRE-BORRADOR: las secciones 3-8 son plantilla y hay que completarlas antes de
     pasar validate_manifest_poc.py. El Reparto y Niveles de la cabecera están a 0 porque todavía
     no hay componentes definidos; recalcúlalos al rellenar la sección 3. -->

## 1. Contexto y necesidad de origen
| ID | Necesidad / duda del cliente | Origen |
|----|-------------------------------|--------|
| NEC-1 | Migrar de Salesforce CPQ a Revenue Cloud: 180 productos activos, 12 bundles, 950 quotes históricas | Scan CPQ Scout |
| NEC-2 | SBQQ__Quote__c (950 registros) migra de forma directa a Quote | Scan CPQ Scout |
| NEC-3 | SBQQ__QuoteLine__c (4200 registros) migra de forma directa a QuoteLineItem | Scan CPQ Scout |
| NEC-4 | SBQQ__DiscountSchedule__c (6 registros) migra de forma directa a PriceAdjustmentSchedule | Scan CPQ Scout |

## 2. Hipótesis y experimento
**Hipótesis en una frase:** Los mecanismos de CPQ detectados con riesgo medio/alto tienen
equivalente estándar en Revenue Cloud sin desarrollo a medida.

| ID | Hipótesis | Necesidad | Criterio de éxito | Si no se cumple / no concluyente |
|----|-----------|-----------|--------------------|-----------------------------------|
| HIP-1 | ¿El mecanismo de `SBQQ__ProductOption__c` (Jerarquía de bundles usa reglas de opción no triviales; requiere revisar equivalencia con Product Relationship Type en RLM) tiene equivalente estándar en RLM (`ProductRelationship`) sin desarrollo a medida? | NEC-1 | Se reproduce el comportamiento observado en origen usando solo configuración estándar de ProductRelationship | Si no hay equivalente estándar, queda NO VALIDADA y se documenta si hace falta desarrollo o rediseño de proceso |
| HIP-2 | ¿El mecanismo de `SBQQ__PriceRule__c` (2 price rules invocan Apex (lookup de coste externo); el resto son condiciones estándar) tiene equivalente estándar en RLM (`PricingRule / DecisionTable`) sin desarrollo a medida? | NEC-1 | Se reproduce el comportamiento observado en origen usando solo configuración estándar de PricingRule / DecisionTable | Si no hay equivalente estándar, queda NO VALIDADA y se documenta si hace falta desarrollo o rediseño de proceso |
| HIP-3 | ¿El mecanismo de `SBQQ__QuoteProcess__c (QCP personalizado)` (Script QCP calcula margen combinando coste de un sistema externo (no visible en la org); no hay integración documentada equivalente en RLM) tiene equivalente estándar en RLM (`Sin equivalente estándar identificado`) sin desarrollo a medida? | NEC-1 | Se reproduce el comportamiento observado en origen usando solo configuración estándar de Sin equivalente estándar identificado | Si no hay equivalente estándar, queda NO VALIDADA y se documenta si hace falta desarrollo o rediseño de proceso |
| HIP-4 | El pricing con Apex/QCP detectado (2 price rules con Apex, 1 scripts QCP) tiene un equivalente estándar en RLM (expression sets / decision tables) sin reescribir lógica | NEC-1 | El resultado del cálculo coincide con el de origen para los casos de prueba | Si la lógica depende de código a medida irreproducible en estándar, queda NO VALIDADA y pasa a desarrollo |
| HIP-5 | Las dependencias de Apex detectadas sobre objetos SBQQ (3 triggers, 5 clases) no tienen equivalente bloqueante en RLM que impida la migración de ese flujo | NEC-1 | Se identifica para cada trigger/clase si su función la cubre RLM estándar o requiere migrarlo/reescribirlo | Si bloquea, se documenta como dependencia y pasa a desarrollo, no a esta POC |

| ID | Paso del experimento | Hipótesis | Entrada | Resultado esperado | Evidencia requerida |
|----|------------------------|-----------|---------|----------------------|------------------------|
| EXP-1 | Configurar `ProductRelationship` para reproducir `SBQQ__ProductOption__c` con un caso representativo del origen | HIP-1 | <caso de prueba extraído del origen — completar> | <qué resultado confirmaría la hipótesis — completar> | <consulta/captura/log — completar> |
| EXP-2 | Configurar `PricingRule / DecisionTable` para reproducir `SBQQ__PriceRule__c` con un caso representativo del origen | HIP-2 | <caso de prueba extraído del origen — completar> | <qué resultado confirmaría la hipótesis — completar> | <consulta/captura/log — completar> |
| EXP-3 | Configurar `Sin equivalente estándar identificado` para reproducir `SBQQ__QuoteProcess__c (QCP personalizado)` con un caso representativo del origen | HIP-3 | <caso de prueba extraído del origen — completar> | <qué resultado confirmaría la hipótesis — completar> | <consulta/captura/log — completar> |
| EXP-4 | Reproducir uno de los price rules/QCP con Expression Sets / Decision Tables de RLM | HIP-4 | <caso de prueba del price rule/QCP real — completar> | <resultado numérico esperado — completar> | <comparación numérica, consulta — completar> |
| EXP-5 | Revisar cada trigger/clase Apex referenciado y clasificar: cubre RLM estándar / requiere migración / requiere reescritura | HIP-5 | Lista de triggers/clases del scan (`details` si está disponible) | Clasificación completa sin triggers sin revisar | Tabla de clasificación con motivo |

## 3. Componentes
<!-- PLANTILLA: completar un componente por cada paso EXP-n antes de validar. -->
| ID | Paso | Componente | Tipo | Especificación | Nivel | Responsable | Motivo | Tamaño | Estado |
|----|------|------------|------|----------------|-------|-------------|--------|--------|--------|
| CMP-1 | EXP-1 | <nombre> | <Tipo> | <especificación suficiente para construir sin preguntar> | 🟢/🔵/🟠 | IA/IA+Revisión/Persona | <motivo si no es IA> | S/M/L | Pendiente |

## 4. Tareas de persona
<!-- PLANTILLA: un bloque "### CMP-n — <nombre>" por cada componente con Responsable = Persona. -->

## 5. Datos de prueba
<!-- PLANTILLA: ver references/datos-demo.md de nespon-brief-to-demo. -->
| ID | Objeto | Registros | Contenido / valores clave | Pasos |
|----|--------|-----------|---------------------------|-------|
| DAT-1 | <completar> | <completar> | <completar> | <completar> |

## 6. Orden de construcción
<!-- PLANTILLA: completar tras definir los componentes de la sección 3. -->

## 7. Supuestos y preguntas abiertas
- Generado automáticamente desde el scan scan-sample-0001; revisar con el SE antes de dar
  por buena ninguna fila.
- Supuesto: la org objetivo (<completar — SDO/sandbox con Revenue Cloud provisionado>) tiene Revenue Cloud (RLM) provisionado.
- Pregunta para el SE: ¿los 3 mecanismo(s) de riesgo medio/alto detectados por el
  scan son los prioritarios, o hay otros del cliente que no aparecen en CPQ (p. ej. procesos
  manuales)?

## 8. Registro de cambios
- v1: pre-borrador generado automáticamente el 2026-10-23 desde el scan de CPQ Scout
  (scan_id scan-sample-0001). Pendiente de completar secciones 3-8 y revisión del SE.
