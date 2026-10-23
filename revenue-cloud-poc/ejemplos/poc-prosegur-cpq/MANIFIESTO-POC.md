# MANIFIESTO DE DESARROLLO (POC) — Prosegur Alarms — v1

**Estado de revisión:** APROBADO
**Revisado por:** Kevin · **Fecha de aprobación:** 2026-10-20
**Cliente:** Prosegur Alarms · **Sector:** Seguridad / Alarmas · **Zona fiscal:** Península (IVA 21%) — caso de prueba en España; multi-país (Portugal/LATAM) queda fuera de esta POC
**Nube ancla:** Revenue Cloud (RLM) · **Nubes de apoyo:** — · **Org objetivo:** <completar — SDO/sandbox con Revenue Cloud y Asset Lifecycle Management provisionados>
**Incertidumbre:** ¿Existe un mecanismo estándar en Revenue Cloud (más allá del reembolso por cancelación ya documentado) que calcule y aplique una penalización configurable por baja anticipada, parametrizada desde el catálogo, sin desarrollo a medida?
**Restricciones del SE:** Solo mecanismos declarativos (Price Rules, Decision Tables, Expression Sets, Attribute-Based Pricing); nada de Apex para el cálculo de la penalización — si resulta imprescindible, la hipótesis queda NO VALIDADA y se documenta como desarrollo
**Reparto:** IA 5 (71%) · IA+Revisión 1 · Persona 1 · **Niveles:** 🟢 3 · 🔵 4 · 🟠 0

<!-- Origen: NEC-17 de MANIFIESTO-NECESIDADES.md (RFQ "Proyecto CPQ Alarmas" de Prosegur, hoja
"CPQ"). Modalidad confirmada por el cliente el 2026-10-20, acotada a esta única incertidumbre
entre las 4 marcadas en rojo. Verificación previa: la documentación oficial de Revenue Cloud
revisada (Trailhead "Manage Customer Asset Renewals and Cancellations") solo describe un
reembolso de la parte no usada al cancelar un asset — no documenta ningún campo/objeto estándar
de penalización. Esto es lo que esta POC comprueba de forma acotada; no sustituye una revisión
completa de Salesforce Help / rlm-skill, que sigue PENDIENTE DE VALIDACIÓN. -->

## 1. Contexto y necesidad de origen
| ID | Necesidad / duda del cliente | Origen |
|----|-------------------------------|--------|
| NEC-1 | Gestión de penalizaciones por baja anticipada, parametrizada desde el catálogo (sin fórmula ni regla de cálculo conocida) | Brief |

## 2. Hipótesis y experimento
**Hipótesis en una frase:** Un mecanismo declarativo de pricing de Revenue Cloud puede calcular una
penalización por baja anticipada sobre el valor restante del contrato, sin Apex.

| ID | Hipótesis | Necesidad | Criterio de éxito | Si no se cumple / no concluyente |
|----|-----------|-----------|--------------------|-----------------------------------|
| HIP-1 | Una Price Rule / Decision Table estándar puede calcular un cargo de penalización basado en el tiempo restante de contrato y el valor contratado, sin código | NEC-1 | Al cancelar un asset antes de fin de contrato se genera una línea de cargo cuyo importe coincide con el cálculo manual de la fórmula de prueba (50% del valor restante) | Si el flujo de cancelación solo genera el reembolso documentado y ningún mecanismo estándar añade un cargo, queda NO VALIDADA y se documenta que requiere desarrollo (Apex/Flow) o proceso manual |

| ID | Paso del experimento | Hipótesis | Entrada | Resultado esperado | Evidencia requerida |
|----|------------------------|-----------|---------|----------------------|------------------------|
| EXP-1 | Configurar en el catálogo un mecanismo de penalización (Price Rule/Decision Table/Attribute-Based Pricing, el que resulte viable) sobre un producto de prueba con contrato de 24 meses | HIP-1 | Producto "Alarma Residencial Básica — Contrato 24m", 29 €/mes | El mecanismo queda guardado y activo en el Price Book Entry del producto | Captura de la configuración de Pricing en Setup |
| EXP-2 | Simular la cancelación de un asset con 12 de 24 meses transcurridos usando el flujo estándar de cancelación (cotización de cancelación) | HIP-1 | Asset activo "Alarma Residencial Básica" con 12 meses restantes, valor 29 €/mes | Si el mecanismo estándar lo soporta: aparece una línea de cargo de penalización además del reembolso ya documentado; si no, solo aparece el reembolso | Quote/Order de cancelación con sus líneas, consulta SOQL |
| EXP-3 | Comparar el importe de la línea de penalización (si existe) contra el cálculo manual de la fórmula de prueba (50% × 12 × 29 € = 174 €) | HIP-1 | Mismos datos que EXP-2 | El importe coincide (±0,01 €) si la hipótesis es cierta | Tabla comparativa: cálculo del sistema vs. cálculo manual |

## 3. Componentes
| ID | Paso | Componente | Tipo | Origen | Especificación | Nivel | Responsable | Motivo | Tamaño | Estado |
|----|------|------------|------|--------|----------------|-------|-------------|--------|--------|--------|
| CMP-1 | EXP-1 | Producto de prueba | Product2 | Estándar SF | "Alarma Residencial Básica — Contrato 24m", 29 €/mes, término de contrato 24 meses | 🟢 | IA | — | S | Pendiente |
| CMP-2 | EXP-1 | Verificar licencia Revenue Cloud / Asset Lifecycle Management | Setup | N/A | PermissionSetLicense activa con Asset/Revenue Lifecycle Management | 🟢 | Persona | Provisión/licencia, solo visible en Setup | S | Pendiente |
| CMP-3 | EXP-1 | Mecanismo de penalización (exploratorio) | PricingRule / DecisionTable | Estándar RLM | Fórmula de prueba: 50% del valor restante del contrato; se construye con Price Rule/Decision Table estándar de RLM — si ninguna lo permite sin código, la hipótesis queda NO VALIDADA (no se marca como Custom object sin antes verificarlo contra la documentación oficial / rlm-skill, y no se crea nada a medida como alternativa dentro de esta POC) | 🔵 | IA | — | M | Pendiente |
| CMP-4 | EXP-2 | Asset de prueba con 12/24 meses transcurridos | Asset | Estándar RLM | Fecha de inicio retroactiva (TODAY-12 meses), término 24 meses, ligado a CMP-1 | 🔵 | IA | — | S | Pendiente |
| CMP-5 | EXP-2 | Cotización de cancelación | Quote | Estándar RLM | Generada por el flujo estándar de cancelación sobre CMP-4 | 🟢 | IA | — | S | Pendiente |
| CMP-6 | EXP-3 | Consulta de verificación | Report | Estándar SF | Report sobre las líneas de la Quote de cancelación: tipo de línea, importe | 🔵 | IA+Revisión | Confirmar que el filtro y las columnas distinguen reembolso de penalización correctamente | S | Pendiente |
| CMP-7 | EXP-1 | Permisos de prueba | PermissionSet | Estándar SF | CRUD sobre Product2, Asset, Quote; acceso a Pricing y Asset Lifecycle Management | 🔵 | IA | — | S | Pendiente |

## 4. Tareas de persona
### CMP-2 — Verificar licencia Revenue Cloud / Asset Lifecycle Management
- **Ruta:** Setup → Company Settings → Permission Set Licenses (el nombre del menú puede variar).
- **Valores:** —
- **Comprobar:** hay una licencia con "Revenue" o "Asset Lifecycle Management" activa y asignada.
- **Desbloquea:** CMP-3, CMP-4

## 5. Datos de prueba
Spec: `datos/seed-spec.json` (generada con `fill_data.py`) · Qué representa cada caso: `datos/HISTORIA-DATOS.md`

| ID | Objeto | Registros | Contenido / valores clave | Pasos |
|----|--------|-----------|---------------------------|-------|
| DAT-1 | Account, Asset | 1 protagonista | Cuenta de prueba "Distribuidor Test SL" con un Asset activo de 24 meses, 12 transcurridos | EXP-2 |

## 6. Orden de construcción
CMP-2 → CMP-7 → CMP-1 → CMP-3 → DAT-1 → CMP-4 → CMP-5 → CMP-6 → ejecutar EXP-1 → ejecutar EXP-2 → ejecutar EXP-3

## 7. Supuestos y preguntas abiertas
- Supuesto: la fórmula de prueba es 50% del valor restante del contrato — NEC-17 del RFQ no
  especifica la fórmula real de Prosegur. Sustituir en cuanto el cliente la confirme.
- Supuesto: la org objetivo tiene Revenue Cloud con Asset Lifecycle Management provisionado, no
  solo Sales Cloud.
- Verificación pendiente: contrastar contra Salesforce Help / `rlm-skill` (no disponible en esta
  sesión de Claude Desktop) si existe algún objeto/campo estándar de penalización que la
  documentación de Trailhead revisada no mencionó, antes de dar la hipótesis por probable en
  ninguna dirección.
- Pregunta para el SE/cliente: ¿Prosegur calcula hoy esta penalización en algún sistema o hoja de
  cálculo? Un ejemplo real sustituiría el supuesto del 50%.
- Pregunta para el SE/cliente: de los otros tres 🔴 del RFQ (integraciones crédito/facturador,
  omnicanalidad), ¿se abre una POC adicional tras esta, o se posponen?

## 8. Registro de cambios
- v1: versión inicial a partir de NEC-17 del RFQ "Proyecto CPQ Alarmas" de Prosegur Alarms, tras
  confirmar modalidad POC y acotar el alcance a esta única incertidumbre (2026-10-20).
- v1 — APROBADO por Kevin el 2026-10-20, sin cambios sobre el contenido técnico (fórmula del 50%
  y alcance confirmados tal cual).
