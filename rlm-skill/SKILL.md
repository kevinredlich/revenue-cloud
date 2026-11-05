---
name: rlm-skill
description: 'Punto de entrada único para Salesforce Revenue Cloud / Revenue Lifecycle Management (RLM, Agentforce Revenue Management), release 264 (v68.0), fiel al repo oficial SalesforceLabs/revenue-cloud-foundations. Enruta a 13 sub-skills, 1.131 artículos de Salesforce Help y 1.972 páginas de la Developer Guide 264 (objetos, campos, APIs, invocable actions, CML, BRE, OmniStudio): modelo de datos RLM (263 objetos: PCM, Pricing, Rates, Configurator, Transactions, DRO, Usage, Billing, Approvals), Expression Sets, Decision Tables, pricing recipes y procedure plans, Constraint Models, document generation, ramp deals, renovaciones de assets, usage/rating/drawdown y demo QuantumBit. Úsalo SIEMPRE que se mencione Revenue Cloud, RLM, Revenue Management, quote-to-order, PCM, catálogo, precios, bundles, configurador, DRO, billing, usage, ramp, renovaciones, SOQL sobre objetos RLM, o para verificar cómo funciona una feature de Revenue Cloud, aunque no se diga "RLM".'
---

# RLM skill — Revenue Cloud (release 264)

Kit técnico de Revenue Cloud derivado del repo oficial
[`SalesforceLabs/revenue-cloud-foundations`](https://github.com/SalesforceLabs/revenue-cloud-foundations)
(tag `264.4.11`, commit `c850652`, 16/09/2026), empaquetado como un único skill. Todo el
contenido es copia fiel de ese repo; solo se han adaptado rutas y agrupado los artículos
de documentación en ficheros por área. Este fichero solo enruta: lee la sub-guía que toque
y, desde ella, las referencias que cite.

## Cómo resolver rutas

Todas las rutas que empiezan por `subskills/`, `references/` o `salesforce-help/`
son **relativas a la raíz de este skill** (la carpeta donde está este SKILL.md),
estén donde estén citadas. Léelas con `view` anteponiendo esa raíz.

Equivalencias con el repo original, por si el usuario lo tiene clonado:
`subskills/<x>/guide.md` ↔ `.claude/skills/<x>/SKILL.md` · `references/apis/` ↔ `postman/docs/` ·
`references/guides/` ↔ `docs/guides/` · `references/enablement/` ↔ `docs/enablement/` ·
`references/schema-diff/` ↔ `scripts/erd/schema_diff/` · `references/` ↔ `docs/references/` ·
`salesforce-help/` ↔ `docs/salesforce/`.

## Enrutado — qué sub-guía leer

Lee `subskills/<nombre>/guide.md` y, si la guía lo indica, sus ficheros hermanos.
Varias pueden aplicar a la vez (p. ej. pricing suele combinar `pricing-wiring` +
`expression-sets` + `decision-tables`).

| Necesidad | Sub-skill / fuente |
|---|---|
| Objetos, campos, relaciones, SOQL, "¿qué objeto guarda X?" | `revenue-cloud-data-model` (luego `domains/<dominio>.md` y `cross-domain-relationships.md`); enums y tipos exactos en `references/schema-diff/264-schema.json` |
| Verificar cómo funciona una feature, labels, terminología, existencia en la release | `revenue-cloud-docs` + Help `salesforce-help/264/help/` |
| Referencia de desarrollador: object/field reference, invocable actions, Metadata/Tooling API, Apex, CML | Developer Guide `salesforce-help/264/dev-guide/` |
| BRE (Expression Sets, Decision Tables), Context Service, OmniStudio, Discovery Framework, DPE: referencia de plataforma | Developer Guide Industries `salesforce-help/264/dev-guide-industries/` |
| Endpoints REST / Connect de PCM, Discovery, Configurator, Pricing, Rates, Transactions, Usage, Billing, Context | `rlm-business-apis` → `references/apis/*.md`; payloads detallados en `salesforce-help/264/dev-guide/` (artículos `connect_*`) |
| Context Definitions, mappings, tags, hidratar/consultar contextos | `context-service` |
| Expression Sets (BRE): pricing, qualification, discovery, rating, overlays, activación | `expression-sets` |
| Decision Tables: datos desfasados, refresh, CSV, comparar orgs | `decision-tables` |
| Cambios de pricing que cruzan recipes, recipe-table mappings, procedure plans | `pricing-wiring` |
| Reglas de bundle / configurador con CML (.ffxblob), por qué no cambia el comportamiento | `constraint-models` |
| Plantillas .docx OmniStudio, tokens, DocumentTemplate, data mappers, imágenes dinámicas | `document-generation` |
| Quotes multi-año con ramp por grupos, uplift / compound uplift | `ramped-quotes` |
| Assets listos para renovación, historial Renewal/Upsell/Downsell | `renewal-asset-creation` |
| Productos de consumo: usage, commitments, rating, drawdown, rated summaries a cero | `usage-consumption` |
| Guion de demo QuantumBit por release (click-paths, talk tracks) | `qb-demo-script` |

## Referencias disponibles

- `references/apis/` — referencias de Business APIs v68 por dominio (billing, pricing, PCM, configurator, discovery, rates, transactions, usage, context service).
- `references/` — Context Service (utility, patch shapes), Decision Tables (API + ejemplos), Expression Set Connect API, overlays de ejemplo, permisos de Revenue Cloud (`revenue-cloud-permissions.md`).
- `references/guides/` — setup de constraints y docgen, runbook de usage/consumo, escenarios demo de consumo QuantumBit, guía de build `prepare-rlm-org-build-guide.md` y `local-installation.md`.
- `references/enablement/` — guion demo QB 262, README 264, referencia maestra de escenarios QB, `coverage-matrix.md` y plantilla de ejercicios (`_template/`).
- `references/schema-diff/` — `262-vs-264-diff.md` / `.json` (qué cambió entre releases), `260-vs-262-diff.md` (histórico), esquemas completos `264-schema.json` y `262-schema.json` (~2 MB cada uno: consúltalos con `grep` o un script, nunca con `view` entero) y los scripts `extract_schema.py` / `diff_schemas.py` (requieren org y el repo para ejecutarse).
- `salesforce-help/264/feature-index.md` — índice de features 264.
- **Help 264** — `salesforce-help/264/help/index.md` (índice por área), `salesforce-help/264/help/<área>.md` (1.131 artículos agrupados: agents, approvals, billing, configurator, dro, pcm, pricing, rating, transaction_mgmt, usage), `article-index.md` (mapa `article_id` → fichero + líneas) y `manifest.json`.
- **Developer Guide 264 (Revenue Management)** — `salesforce-help/264/dev-guide/index.md` (índice por sección del TOC), 1.403 páginas en `salesforce-help/264/dev-guide/<sección>.md` (advanced-approvals, billing-1..3, dynamic-revenue-orchestrator, product-catalog-management-1..2, product-configurator, rate-management, revenue-management-associated-objects, revenue-management-deployment, revenue-management-settings, salesforce-pricing, transaction-management-1..2, usage-management, get-started…) y `article-index.md`.
- **Developer Guide 264 (Industries Common Resources)** — `salesforce-help/264/dev-guide-industries/index.md`, 569 páginas en `<sección>.md` (business-rules-engine, context-service, omnistudio, discovery-framework, data-processing-engine…, decision-explainer, collections-and-recovery, action-launcher, timeline) y `article-index.md`.
- `salesforce-help/262/dev-guide/expression-set-business-apis-links.md` — índice de enlaces externos de Expression Set Business APIs (único fichero del corpus 262 incluido).

### Cómo leer los corpus de documentación (formato agrupado)

Los artículos NO están en ficheros sueltos: cada uno vive dentro de su fichero de área o
sección, precedido por la línea `=== ARTICLE: <article_id> ===` y con su frontmatter
original (incluye `source_url` al portal oficial). Cualquier guía que cite
`salesforce-help/{release}/help/articles/<id>.md`, `.../dev-guide/articles/<id>.md` o
`.../dev-guide-industries/articles/<id>.md` se refiere a ese artículo dentro del fichero
agrupado correspondiente.

- Buscar un término: `grep -n "<término>" salesforce-help/264/help/*.md` (o `dev-guide/*.md`, `dev-guide-industries/*.md`, o solo el fichero que toque) y luego `view` con un rango de líneas alrededor del resultado.
- Leer un artículo concreto: busca su `article_id` en el `article-index.md` de ese corpus y haz `view` del fichero indicado con ese rango de líneas.
- Listar los artículos de un fichero: `grep -n "^=== ARTICLE" <fichero>.md`.
- Nunca hagas `view` de un fichero agrupado entero: son grandes (hasta ~800 KB).
- Regla práctica: **Help = cómo usa la feature un admin o vendedor; Developer Guide = objetos, campos, APIs y CML contra los que se construye.**

El `article_id` sigue mapeando 1:1 al portal: `ind.billing.htm` ↔ `help.salesforce.com/s/articleView?id=ind.billing.htm`; las páginas de la Developer Guide llevan su URL de `developer.salesforce.com` en `source_url`.

Los artículos de la Developer Guide 264 llevan el aviso de *preview* de Salesforce: se capturaron antes del GA de Winter '27. Si el usuario trabaja en una org 264 ya en GA, la org es la fuente de verdad ante cualquier discrepancia.

## Lo que NO viene en el kit (léelo antes de proponer comandos)

Las guías se escribieron para el repo y citan material que aquí no está:

- Tareas CumulusCI (`cci task run ...`, `cumulusci.yml`, `tasks/*.py`), scripts Python/Apex (`scripts/...`, salvo los dos de `references/schema-diff/`), datasets SFDMU (`datasets/...`) y metadata (`force-app/`, `unpackaged/`).
- Sub-skills del repo no incluidas: `odt-authoring`, `release-enablement`, `troubleshooting`, `sfdmu-data-plans`, `txn-data-harness`, `schema-validation`, `cci-orchestration`, `doc-consistency`, `repo-integration` (y las de operación del repo: `apex-security-hardening`, `audit-review`, `build-harness`, `df-workshop-setup`, `inapp-framework`, `pde-org-build`, `pmos-integration`, `robot-testing`, `skill-authoring`, `todo-tracker`).
- Corpus de la release 262 (`salesforce-help/262/help/`, `salesforce-help/262/dev-guide/` salvo el fichero de enlaces), los `manifest.json` de la Developer Guide y `260-schema.json`.

Cuando una guía remita a algo de esta lista: usa el conocimiento de la guía (secuencias,
reglas, "DO NOT", endpoints, objetos) y tradúcelo a pasos ejecutables sin el repo —
Setup, Workbench / Developer Console, SOQL, `sf` CLI o llamadas Connect/REST documentadas
en `references/apis/` y en la Developer Guide. Si el usuario tiene el repo clonado, entonces
sí puede ejecutar las tareas tal cual. Nunca presentes una ruta faltante como si existiera.

## Reglas de trabajo

1. **Fundamenta antes de afirmar.** Para cualquier afirmación de producto (qué hace una feature, nombre de objeto/campo, disponibilidad en 264), comprueba en el modelo de datos, el Help o la Developer Guide. La memoria sobre Revenue Cloud envejece rápido: Salesforce renombra objetos y features entre releases (p. ej. "Revenue Cloud" → "Revenue Management").
2. **Estándar y declarativo primero.** Casi todo en RLM es configurable (PCM, Pricing Procedures, Decision Tables, Context Definitions, DRO, CML). Apex solo cuando no hay alternativa.
3. **Respeta el orden de dependencias** que marcan las guías (p. ej. catálogo → pricing/decision tables → procedure plans → context), sobre todo en pricing.
4. **Release.** Todo está fijado a 264 (Winter '27, v68.0). Si el usuario trabaja en otra release, avísalo y usa `references/schema-diff/262-vs-264-diff.md` para detectar diferencias.
5. **Idioma.** Las guías y la documentación están en inglés; responde en el idioma del usuario manteniendo en inglés los nombres de objetos, campos, APIs y labels de Salesforce.

## Relación con otros skills

Si el trabajo es preventa (demo, propuesta, backlog), el formato del entregable lo marca
el skill correspondiente (p. ej. `salesforce-demo-builder` o `revenue-cloud-demo`); este
skill aporta la profundidad técnica y la verificación contra documentación oficial.
