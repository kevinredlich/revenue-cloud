# Reglas obligatorias de modelado de catálogo en Revenue Cloud (RLM)

> Referencia de la skill `revenue-cloud-poc`. La enforcement automática (fuentes consultadas, tabla de verificación de API, valores de API incorrectos conocidos) está en `scripts/validate_manifest_poc.py`.

**Aplica siempre** que se pida configurar, migrar o generar ficheros de carga de productos, atributos, selling models, listas de precio, ajustes de precio o bundles. Léelo ANTES de diseñar y ANTES de entregar.

**Principio rector.** Durante el diseño NO hay acceso a la org. La solución se diseña a partir de la **documentación oficial** (Help 264 y `rlm-skill`) y debe ser realista y cargable sin errores en un entorno de Revenue Cloud. La org valida **después** (IDE/pre-flight); nunca es una precondición para diseñar ni una fuente que sustituya a la documentación.

## 0. Regla cero (obligatoria, sin excepciones)

**Para diseñar cualquier solución técnica o funcional de Revenue Cloud (catálogo, atributos, selling models, pricing, bundles/configurador, transacciones, DRO, billing, usage, renovaciones, documentos), SIEMPRE se consulta primero `rlm-skill`** para obtener la documentación oficial y las reglas de configuración. No se diseña de memoria ni con el link genérico de Salesforce Help.

Procedimiento, en este orden y dejando constancia de cada paso:
1. Leer `rlm-skill/SKILL.md` y elegir el/los sub-skills que toquen (tabla de abajo).
2. Leer la `guide.md` del sub-skill y los ficheros que cite (dominio del modelo de datos, referencias de APIs, dataset de referencia).
3. Buscar y leer el artículo concreto de Help 264 de cada objeto o feature que intervenga (`salesforce-help/264/help/<área>.md`, con `grep -n "^title:"` y `grep -n "<término>"`).
4. Diseñar solo con lo leído y citar en la tabla de verificación (sección 3) la fuente de cada decisión: sub-skill o artículo.
5. Si `rlm-skill` no está disponible en la sesión: decirlo al usuario al principio y marcar todo lo técnico como SUPUESTO; no presentarlo como diseño validado.

| Necesidad | Sub-skill de `rlm-skill` |
|---|---|
| Objetos, campos, relaciones | `revenue-cloud-data-model` (+ `domains/<dominio>.md`, `cross-domain-relationships.md`) |
| Cómo funciona una feature, terminología, existencia en la release | `revenue-cloud-docs` + `salesforce-help/264/` |
| Endpoints REST/Connect | `rlm-business-apis` → `references/apis/*.md` |
| Context Definitions, mappings, tags | `context-service` |
| Expression Sets (pricing, qualification, discovery, rating) | `expression-sets` |
| Decision Tables | `decision-tables` |
| Cambios de pricing: recipes, procedure plans | `pricing-wiring` |
| Reglas de bundle/configurador con CML | `constraint-models` |
| Plantillas .docx OmniStudio, DocumentTemplate | `document-generation` |
| Quotes multi-año con ramp, uplift | `ramped-quotes` |
| Assets para renovación | `renewal-asset-creation` |
| Usage, commitments, rating, drawdown | `usage-consumption` |
| Guion de demo QuantumBit | `qb-demo-script` |

Esto aplica también al diseño **funcional** (flujo de venta, estructura de catálogo, reglas de negocio): primero se contrasta con lo que RLM soporta según `rlm-skill`, y solo después se propone.

## 1. Qué falló (catálogo Telnova, 23-oct-2026)

El IDE con acceso a la org rechazó el documento. Causas y regla que las evita:

| # | Error cometido | Causa raíz | Regla |
|---|---|---|---|
| 1 | Precios en MXN que la org no tenía activo | Fijé la moneda a partir del origen de los datos (CSV de un operador mexicano) en vez de hacer el diseño independiente de la moneda | R2, R8 |
| 2 | Atributos enlazados directamente a cada producto, sin `ProductClassification` | No modelé clasificaciones, aunque la Help dice que los atributos se asignan con la clasificación ("Based On") | R3 |
| 3 | Ajustes por atributo sin fecha de inicio/fin, sin regla ni condición | Inventé una hoja plana sin leer el artículo "Create Attribute Based Adjustments" (exige rango de fechas y condición); la API de pricing marca `effectiveFrom` como obligatorio | R4, R9 |
| 4 | Nombres de programas de ajuste inventados | La Help habla de programas predefinidos ("Standard Attribute Based Adjustment", "Standard Bundle Based Adjustment"); debí usarlos | R4 |
| 5 | `Month`, `Year`, "Last pricing period" y `AdjustmentAmount` | Copié etiquetas de UI e inventé un valor. **Los valores correctos ya estaban en el kit** (`Months`, `Annual`, `percentage/amount/override`); no los busqué | R1, R5 |
| 6 | Hoja de "valores permitidos" por producto | RLM modela **exclusiones** (`AttrPicklistExcludedValue`, "Include or Exclude Picklist Values") | R3 |
| 7 | Valores de `Product2.Family` inexistentes | Asumí valores de un picklist estándar sin declararlos como prerrequisito de alta | R2 |
| 8 | Objetos/columnas con nombres propios (p. ej. `ProductAttributeAllowedValue`) | Nombré cosas sin comprobar que existieran en la documentación | R5 |
| 9 | Dudas relegadas a una hoja "Sin verificar" al final | Las traté como nota, no como parte del diseño | R6 |
| 10 | Un selling model por duración (Plazo 12, Plazo 18…) | RLM no admite dos selling models con el mismo tipo, plazo y unidad, y la duración se fija en la línea de la cotización, no en el selling model; además ningún elemento estándar del procedimiento de precios lee ajustes por duración | R10, R12 |
| 11 | Ajustes por atributo sueltos y sumados (Tipo CRM + Contactos) con importes que faltaban | Una regla de ajuste exige condiciones sobre **todos** los atributos que afectan al precio; cada combinación necesita su regla e importe | R11, R12 |
| 12 | Entregué un diseño que el motor no puede ejecutar como estaba planteado | No comprobé la **viabilidad estándar** de cada requisito contra los artículos de límites/consideraciones de la Help antes de diseñar | R12 |
| 13 | No se exigía comparar alternativas ni elegir el mejor diseño | El proceso validaba nombres y viabilidad, pero no que la solución fuera la mejor ni coherente con el resto | R13 |
| 14 | La ruta de demo y los playbooks de otras skills no pasaban por las mismas reglas; el generador de pre-borradores emitía el formato antiguo | Las reglas solo estaban enganchadas a la ruta POC | R14 |

## 2. Reglas

**R1 · Jerarquía de fuentes.** (1) Documentación oficial obtenida **a través de `rlm-skill` (Regla cero)**: Help 264 y `rlm-skill` (modelo de datos, `references/apis/*`, dataset de referencia `references/enablement/master/qb-scenario-reference.md`). (2) Si la doc solo da la etiqueta de UI, derivar el valor de API **siguiendo los ejemplos del kit** y marcarlo DERIVADO. Una fuente externa (referencia de objetos de Salesforce, una copia de terceros) solo puede dar un DERIVADO si se contrasta **cada nombre con la etiqueta de la Help** y se cita esa contrastación; sin ella es SUPUESTO, y nunca DOC. (3) La org solo valida después; si el IDE corrige algo, se anota en la sección 4. Mi memoria, el "suele ser así" y las etiquetas de UI no son fuente. Sección 6 = dónde buscar cada tipo de valor.

**R2 · Diseño portable, prerrequisitos explícitos.** No se bloquea el diseño por falta de datos de la org ni se asumen valores ajenos al origen. Lo dependiente de la org se **parametriza** con el valor por defecto que respalda la documentación, y se entrega una sección **"Prerrequisitos de la org"** con (a) los altas necesarios (p. ej. valores de `Product2.Family`, monedas, programas de ajuste si no existen) y (b) consultas read-only de pre-flight que el usuario/IDE ejecuta antes de cargar (existencia de selling models, `PriceAdjustmentSchedule`, clasificaciones, valores de picklist, moneda corporativa).

**R3 · Atributos como los documenta RLM.** Picklist y valores → definición de atributo (y categoría si procede) → **clasificación de producto con sus atributos** → producto "Based On" esa clasificación → overrides a nivel de producto solo cuando hagan falta. Restringir valores se hace con **exclusiones**, nunca con listas de permitidos. Verificar el orden en `subskills/revenue-cloud-data-model/domains/pcm.md` y en la Help de PCM.

**R4 · Ajustes de precio como los documenta RLM.** Usar los objetos reales (`AttributeBasedAdjRule`, `AttributeAdjustmentCondition`, `AttributeBasedAdjustment`, `BundleBasedAdjustment`, `PriceAdjustmentSchedule`/`PriceAdjustmentTier`). Partir de los programas predefinidos que cita la Help y no inventar nombres. Todo ajuste lleva fecha efectiva de inicio (obligatoria en la API) y de fin si aplica, producto, selling model, tipo (`percentage` | `amount` | `override`), valor y condición de atributo; los de bundle, root bundle y parent. El programa se desactiva para editarlo, se activa al final y se refrescan las decision tables.

**R5 · Nombres y valores de API.** Cada objeto, campo y valor de picklist de un fichero de carga debe ser el de API según la documentación, nunca la etiqueta de la UI ni un nombre inventado. Si no existe un campo para algo, se dice y se propone alternativa; no se inventa la columna. Todo queda en la tabla de la sección 3.

**R6 · Clasificación de cada dato y supuestos en la primera página.** Cada nombre/valor/decisión se etiqueta **DOC** (literal en Help/kit, con referencia), **DERIVADO** (deducido de ejemplos del kit o de una fuente externa contrastada con la Help; la referencia nombra el ejemplo o la contrastación, y si es externa se confirma con describe en el pre-vuelo de la sección 7 del manifiesto) o **SUPUESTO** (no respaldado; hay que minimizarlos eligiendo la alternativa que sí respalda la doc). La tabla de supuestos va en la **primera página** del documento, no al final. El documento es cargable si todo está en DOC/DERIVADO y el pre-flight de R2 está incluido; cada SUPUESTO restante se declara como riesgo con su consulta de validación.

**R7 · La org valida, no diseña.** Cuando el IDE o la org corrige un valor, se corrige el documento, se anota en la sección 4 y se revisa por qué la documentación no lo preveía, para ajustar la fuente de R1.

**R8 · Los datos de origen no deciden la configuración de la org.** País, moneda, idioma o nombres del origen no fijan la configuración destino. La moneda se trata como parámetro: si la org no es multimoneda no se informa `CurrencyIsoCode` (comportamiento estándar de Salesforce; comprobar en el pre-flight).

**R9 · Leer el artículo, no solo el índice.** Antes de generar el fichero de un objeto, leer su artículo de Help (p. ej. "Create Attribute Based Adjustments", "Create a Proration Policy for a Subscription", "Define Product Selling Models") y copiar sus campos obligatorios.

**R10 · Selling models: tipo de cobro, no duración.** Un selling model = tipo (`OneTime`/`TermDefined`/`Evergreen`) + plazo + unidad, **único en la org**. Antes de crear uno, consultar los existentes y reutilizarlos. La duración concreta de un contrato `TermDefined` se fija en la línea, no multiplicando selling models. No crear un selling model por cada duración comercial.

**R11 · Ajustes por atributo = matriz completa.** Cada `AttributeBasedAdjRule` lleva una `AttributeAdjustmentCondition` por **cada** atributo marcado como que afecta al precio. Dos atributos con precio implican una regla por cada combinación de valores permitidos (N x M), con su importe (suma o el que corresponda). Contar las combinaciones **antes** de diseñar. Si son demasiadas, reducir atributos de precio, agruparlos o pasar a una alternativa de R12. Más límites (Help "Attribute-Based Pricing Limits"): valores numéricos con `.0`, sin picklist Booleano, solo atributos de la clasificación directa del producto, sin atributos con contexto de bundle sobrescrito.

**R12 · Nunca entregar un diseño que no calce en Revenue Cloud.** Para **cada requisito** del usuario, antes de entregar, decidir y declarar su vía de implementación:
1. **ESTÁNDAR**: lo soporta RLM tal cual, con cita de la Help o del kit (y revisados sus artículos de límites/consideraciones).
2. **ESTÁNDAR A VALIDAR**: encaja con una limitación conocida o un matiz; se declara el matiz y la prueba de validación.
3. **CUSTOM REAL**: RLM no lo hace de forma estándar. Se ofrece un diseño custom **construido con piezas reales de la plataforma** (expression sets / pricing procedures, decision tables, context definitions, constraint models, flows, Apex, campos o objetos propios, etc.), indicando qué objetos y elementos se tocan, el esfuerzo y el impacto en lo existente.
Está **prohibido** (a) inventar objetos, campos o valores para que el requisito "quepa", (b) dar por soportado algo sin haber leído su artículo, (c) esconder una limitación en una nota. Si un requisito no es estándar, se dice en la primera página y se ofrece la opción estándar más cercana **y** el diseño custom real, con sus pros y contras, para que decida el usuario. Si no se puede garantizar ninguna vía, se dice "no verificado" y no se carga.

**R13 · El mejor diseño, no el primero que funciona.** Para cada decisión de diseño no trivial (cómo modelar un precio, un atributo, un bundle, una regla, una excepción) se comparan **al menos dos alternativas reales** y se elige la mejor con estos criterios, por este orden: (1) **encaje con RLM**: soportada y documentada, sin forzar objetos ni campos; (2) **jerarquía de solución**: estándar nativo > configuración nativa > declarativo (flow, expression set, decision table, constraint model) > código (Apex/LWC) > objeto o campo propio; subir un escalón solo con motivo escrito; (3) **coherencia** con el resto del modelo (mismas convenciones, una sola fuente de verdad por dato, sin duplicar reglas entre catálogo, precios y transacción); (4) **mantenibilidad y actualizaciones**: que no se rompa con una release, sin dependencias frágiles; (5) esfuerzo y riesgo. **Un diseño custom es correcto cuando es la mejor opción real**, no hay que evitarlo a toda costa: lo que está prohibido es el custom injustificado o el estándar forzado que luego no funciona. La decisión queda en la sección 3.3 del manifiesto (elegida, descartadas y motivo).

**R14 · Misma exigencia en demo y en POC; rlm-skill manda sobre cualquier playbook.** Los diseños para **demo** de Revenue Cloud pasan por la Regla cero, R1–R13 y las tablas 3.1–3.3 igual que una POC. Si un playbook de otra skill (p. ej. `nespon-demo-builder`, `nespon-brief-to-demo`) contradice a `rlm-skill` o a la Help 264, prevalece `rlm-skill` y se anota la discrepancia. Ningún diseño se entrega sin **prueba funcional con valores esperados** (por ejemplo, el precio exacto que debe salir para cada combinación): hasta que se ejecuta en una org, el estado es PREPARADA, NO EJECUTADA y no se afirma que funciona.

## 3. Tabla de verificación (obligatoria en cada entrega)

| Objeto | Campo / valor | Valor usado | Clase (DOC / DERIVADO / SUPUESTO) | Referencia (artículo Help o fichero del kit) |
|---|---|---|---|---|

## 4. Correcciones conocidas (feedback del IDE sobre la org de Roger, 23-oct-2026)

| Concepto | Incorrecto | Correcto | Respaldo en la documentación |
|---|---|---|---|
| Unidad de plazo del selling model | `Month` | `Months` | Kit: `qb-scenario-reference.md` (tabla de selling models: "1 Months") |
| Unidad de plazo anual | `Year` | `Annual` | Kit: ídem ("1 Annual"; también `Quarterly`, `Semi-Annual`) |
| Tipo de ajuste por importe | `AdjustmentAmount` | `Amount` (valor de picklist del objeto, confirmado por el IDE; el parámetro `adjustmentType` del Business API usa minúsculas: `percentage`/`amount`/`override`) | Help "Create Attribute Based Adjustments" (Percentage / Amount / Override) y `pricing-business-apis-v68.md`; la capitalización del picklist se valida con describe |
| Estrategia de resto de la proration policy | "Last pricing period" | `AddToLast` | El kit solo da la etiqueta de UI ("primer o último periodo"); el valor de API lo confirmó el IDE (DERIVADO hasta tener fuente) |
| Restricción de valores de picklist | lista de permitidos (`ProductAttributeAllowedValue`, que no existe) | exclusiones (`AttrPicklistExcludedValue`) | Help PCM "Include or Exclude Picklist Values" |
| Selling model de componente en un bundle configurable | informar `ParentSellingModelId`/`ChildSellingModelId` | dejarlos vacíos | Help PCM, campos adicionales del componente: "Don't select a component selling model for configurable bundles" |
| Duración del contrato | un selling model por duración | un selling model por tipo+plazo+unidad, reutilizando los existentes; la duración va en la línea | Error de la org (duplicado) y modelo de selling models |
| Regla de ajuste con varios atributos | ajustes independientes sumados | una regla por combinación, con condición por atributo | Help "Calculate Attribute-Based Discounts" y "Create Attribute Based Adjustments" |

Los valores de la columna «Incorrecto» que son tokens de API (`Month`, `Year`, `AdjustmentAmount`, "Last pricing period", `ProductAttributeAllowedValue`) están también en `api-correcciones.json`, que lee el validador para rechazarlos si aparecen entre `backticks` en un manifiesto. Al añadir una corrección aquí, añádela allí (hay un test que comprueba que ambos coinciden).

Otros fallos del incidente por corregir en el diseño: moneda parametrizada, clasificaciones de producto, fecha de inicio de los ajustes, programas de ajuste predefinidos, alta de valores de `Product2.Family`.

## 5. Checklist de pre-entrega

- [ ] Decisiones de diseño con ≥2 alternativas comparadas y la mejor elegida con motivo (R13, sección 3.3)
- [ ] Pruebas funcionales con valores esperados definidas para precios, atributos y bundles (R14)
- [ ] Si es demo, mismas tablas 3.1–3.3 que una POC (R14)
- [ ] Viabilidad por requisito: cada uno marcado ESTÁNDAR / ESTÁNDAR A VALIDAR / CUSTOM REAL con cita; ningún requisito sin vía (R12)
- [ ] Selling models reutilizados o únicos por tipo+plazo+unidad (R10)
- [ ] Reglas de ajuste: condiciones sobre todos los atributos de precio y combinaciones contadas (R11)
- [ ] `rlm-skill` consultado antes de diseñar: SKILL.md → sub-skills → artículos Help, citados en la tabla de la sección 3 (Regla cero)
- [ ] Artículos de Help de cada objeto leídos (R9)
- [ ] Atributos vía clasificaciones y exclusiones (R3)
- [ ] Ajustes con fechas, condiciones y programas predefinidos (R4)
- [ ] Todos los valores de API respaldados por doc o derivados con ejemplo del kit (R1, R5)
- [ ] Tabla de verificación completa (sección 3), con clase y referencia en cada fila
- [ ] Supuestos al principio del documento y minimizados (R6)
- [ ] Moneda parametrizada, no fijada por el origen (R8)
- [ ] Sección "Prerrequisitos de la org" con altas y consultas de pre-flight (R2)
- [ ] Orden de carga respetando dependencias
- [ ] Coherencia referencial entre hojas comprobada por script

## 6. Dónde buscar nombres y valores de API en el kit `rlm-skill`

| Qué | Dónde |
|---|---|
| Objetos y campos clave | `subskills/revenue-cloud-data-model/domains/<dominio>.md` |
| Valores reales de selling models (tipos, `Months`/`Annual`/`Quarterly`/`Semi-Annual`) y ejemplos de ajustes | `references/enablement/master/qb-scenario-reference.md` |
| Valores de API de pricing (`adjustmentType`, `effectiveFrom`…) | `references/apis/pricing-business-apis-v68.md` |
| Valores de PCM, prorrateo (`ProrationPolicyType`, `ArePartialPeriodsAllowed`) | `references/apis/pcm-business-apis-reference.md`, `references/apis/product-discovery-apis-reference.md` |
| Valores de picklist añadidos por release | `references/schema-diff/262-vs-264-diff.md` |
| Nombres de API de campos que el kit no trae (p. ej. cardinalidad de bundles) | Referencia de objetos de Salesforce. Las páginas de developer.salesforce.com son SPA y WebFetch no las lee: buscar con WebSearch una copia de la página del objeto y leerla. Contrastar **cada nombre con la etiqueta de la Help** y marcar DERIVADO citando esa contrastación; confirmar con describe en el pre-vuelo (no bloquea el diseño). Sin contrastar con la Help es SUPUESTO; nunca DOC |
| Procedimiento y campos obligatorios de cada objeto | `salesforce-help/264/help/<área>.md` (buscar con `grep -n "^title:"`) |

## 7. Nombres de API verificados (bundles configurables)

Obtenidos de la referencia de objetos de Salesforce y contrastados con las etiquetas de la Help 264 ("Manage Local Cardinality", "Add Components to a Configurable Product Bundle"). Clase DERIVADO; confirmar con describe.

| Objeto | Etiqueta de la Help | Nombre de API |
|---|---|---|
| ProductRelatedComponent | Require this component | `IsComponentRequired` |
| ProductRelatedComponent | Include component by default | `IsDefaultComponent` |
| ProductRelatedComponent | Allow quantity changes | `IsQuantityEditable` |
| ProductRelatedComponent | Price includes component | `DoesBundlePriceIncludeChild` |
| ProductRelatedComponent | Quantity Scaling Method (None, Constant, Proportional) | `QuantityScaleMethod` |
| ProductRelatedComponent | Min Quantity / Max Quantity / Quantity | `MinQuantity` / `MaxQuantity` / `Quantity` |
| ProductRelatedComponent | Group | `ProductComponentGroupId` |
| ProductRelatedComponent | Child product / Parent product | `ChildProductId` / `ParentProductId` |
| ProductComponentGroup | Min Number of Components / Max Number of Components | `MinBundleComponents` / `MaxBundleComponents` |
| ProductComponentGroup | Group Name | `Name` |
| Product2 | Configure During Sale | `ConfigureDuringSale` |

Reglas de cardinalidad de grupo que valida la Help ("Manage Validations for Product Bundles", "Group Cardinality Examples"): los productos de un grupo deben ser al menos el mínimo del grupo; los componentes obligatorios del grupo no pueden superar su máximo.
