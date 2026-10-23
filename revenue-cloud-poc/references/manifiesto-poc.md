# Formato del MANIFIESTO-POC.md

El validador (`scripts/validate_manifest_poc.py`) depende de estos encabezados, prefijos de ID y
columnas. Español de España; nombres técnicos y API names en inglés. Tamaño en S/M/L, no horas.
Ejemplo completo en `assets/ejemplo-MANIFIESTO-POC.md`.

```markdown
# MANIFIESTO DE DESARROLLO (POC) — <Cliente o tema> — v<N>

**Estado de revisión:** BORRADOR
**Revisado por:** — · **Fecha de aprobación:** —
**Cliente:** … · **Sector:** … · **Zona fiscal:** Península (IVA 21%)
**Nube ancla:** Revenue Cloud (RLM) · **Nubes de apoyo:** … · **Org objetivo:** …
**Incertidumbre:** <la pregunta técnica o de negocio que hay que responder, en una frase>
**Fuentes consultadas (rlm-skill):** <sub-skills y artículos de Help 264 consultados> | no disponible
**Restricciones del SE:** <literal> | Ninguna
**Reparto:** IA <n> (<x>%) · IA+Revisión <n> · Persona <n> · **Niveles:** 🟢 <n> · 🔵 <n> · 🟠 <n>

## 1. Contexto y necesidad de origen
| ID | Necesidad / duda del cliente | Origen |
|----|-------------------------------|--------|
| NEC-1 | <en lenguaje del cliente> | Brief |
| NEC-2 | … | Supuesto |

## 2. Hipótesis y experimento
**Hipótesis en una frase:** <qué creemos que es viable y bajo qué condición>

| ID | Hipótesis | Necesidad | Criterio de éxito | Si no se cumple / no concluyente |
|----|-----------|-----------|--------------------|-----------------------------------|
| HIP-1 | <enunciado verificable> | NEC-1 | <resultado observable y medible> | <qué evidencia haría falta en su lugar> |

| ID | Paso del experimento | Hipótesis | Entrada | Resultado esperado | Evidencia requerida |
|----|------------------------|-----------|---------|----------------------|------------------------|
| EXP-1 | <acción concreta a probar> | HIP-1 | <datos/condición de partida> | <qué debería pasar si la hipótesis es cierta> | <consulta, log, captura> |
| EXP-2 | … | HIP-1 | … | … | … |

## 3. Componentes
| ID | Paso | Componente | Tipo | Origen | Especificación | Nivel | Responsable | Motivo | Tamaño | Estado |
|----|------|------------|------|--------|----------------|-------|-------------|--------|--------|--------|
| CMP-1 | EXP-1 | <nombre> | PricingRule | Estándar RLM | <condición y fórmula> | 🔵 | IA | — | S | Pendiente |
| CMP-2 | EXP-2 | Activar Revenue Cloud | Setup | N/A | Provisión/licencia en la org | 🟢 | Persona | Requiere licencia/provisión | S | Pendiente |
| CMP-3 | EXP-2 | <objeto a medida> | CustomObject__c | Custom object | <qué guarda y por qué no hay estándar que lo cubra, según lo verificado contra la documentación oficial / rlm-skill> | 🟠 | IA | Sin equivalente estándar verificado | M | Pendiente |

## 3.2 Viabilidad por requisito
| Requisito | Vía | Referencia | Matiz / prueba o diseño custom real |
|-----------|-----|------------|--------------------------------------|
| <requisito del cliente> | ESTÁNDAR | `salesforce-help/264/help/<área>.md` (artículo y su sección de límites) | — |

## 3.3 Decisiones de diseño (mejor alternativa)
| Decisión | Alternativa elegida | Alternativas descartadas | Motivo (encaje RLM, jerarquía, coherencia, mantenimiento, esfuerzo) |
|----------|---------------------|---------------------------|----------------------------------------------------------------------|
| <p. ej. precio según duración> | <la elegida> | <al menos otra real> | <por qué es la mejor> |

## 3.1 Verificación de nombres y valores de API
| Objeto | Campo / valor | Valor usado | Clase | Referencia |
|--------|---------------|-------------|-------|------------|
| PriceAdjustmentTier | LowerBound | `LowerBound` | DOC | `subskills/revenue-cloud-data-model/domains/pricing.md` |
```
Reglas de la tabla (idénticas a `nespon-brief-to-demo/references/manifiesto.md`, con una columna
añadida):
- `Origen`: **Estándar SF** (objeto/funcionalidad de la plataforma, no específica de Revenue
  Cloud — p. ej. `Account`, `Report`, `PermissionSet`) · **Estándar RLM** (objeto o mecanismo
  propio de Revenue Cloud/RLM — p. ej. `Asset`, `PriceAdjustmentSchedule`, Decision Table,
  Expression Set) · **Custom object** (hay que crearlo — objeto custom (`__c`), campo custom sobre
  un objeto estándar, o automatización a medida) **solo cuando se ha verificado contra la
  documentación oficial / `rlm-skill` que no existe equivalente estándar** — no por comodidad ni
  por suposición. Si esa verificación no se ha hecho todavía, no se marca `Custom object`: se deja
  como `Estándar RLM`/`Estándar SF` con el componente en modo exploratorio (como en HIP-EXP de una
  POC) y se documenta la incertidumbre en vez de asumir que hace falta desarrollo · **N/A** (tareas
  de Setup/licencia que no son un objeto a crear ni usar). Esta columna es lo primero que mira
  quien ejecuta la Fase 3: le dice de un vistazo qué usar tal cual y qué construir desde cero, sin
  tener que inferirlo de la especificación.
- **Sección 3.1** (obligatoria): un registro por cada objeto, campo o valor de picklist de API usado en
  la sección 3. `Clase`: **DOC** (literal en Help/`rlm-skill`) · **DERIVADO** (deducido de ejemplos del
  kit; indica el ejemplo) · **SUPUESTO** (no respaldado; se declara también en la sección 7 con su
  consulta de validación). `Referencia` es obligatoria en DOC y DERIVADO (fichero del kit o artículo
  de Help). Nunca se escribe la etiqueta de la UI ni un nombre inventado como valor de API.
- **Sección 3.2** (obligatoria, R12): una fila por requisito, con su vía: **ESTÁNDAR** (lo soporta RLM
  tal cual; referencia al artículo y a sus límites) · **ESTÁNDAR A VALIDAR** (encaja con un matiz
  o limitación; se declara el matiz y la prueba) · **CUSTOM REAL** (RLM no lo hace de forma estándar;
  se describe un diseño custom con piezas reales de la plataforma —expression sets, decision tables,
  context definitions, constraint models, flows, Apex, objetos o campos propios—, esfuerzo e impacto, y
  se ofrece junto a la opción estándar más cercana). Prohibido inventar objetos, campos o valores
  para que un requisito "quepa". Sin vía verificada, el requisito no se carga.
- **Sección 3.3** (obligatoria, R13): una fila por decisión de diseño no trivial, con la alternativa
  elegida, **al menos una descartada** y el motivo según los criterios de R13 (encaje con RLM,
  jerarquía estándar > configuración > declarativo > código > objeto propio, coherencia con el
  resto del modelo, mantenimiento, esfuerzo). Obligatoria si hay filas `ESTÁNDAR A VALIDAR` o
  `CUSTOM REAL` en 3.2. Un diseño custom es válido cuando es la mejor opción real y está justificado.
- `Nivel`: 🟢 default/config · 🔵 automatización o custom declarativo · 🟠 código.
- `Responsable`: `IA` | `IA+Revisión` | `Persona` (criterios en `ia-vs-persona.md`).
- `Motivo`: obligatorio si el responsable no es IA o el nivel es 🟠.
- `Tamaño`: S | M | L. `Estado`: Pendiente | Hecho | Bloqueado | Persona pendiente.

```markdown
## 4. Tareas de persona
### CMP-2 — Activar Revenue Cloud
- **Ruta:** Setup → … (el nombre del menú puede variar).
- **Valores:** —
- **Comprobar:** …
- **Desbloquea:** CMP-1

## 5. Datos de prueba
Spec: `datos/seed-spec.json` (generada con `fill_data.py`) · Qué representa cada caso: `datos/HISTORIA-DATOS.md`

| ID | Objeto | Registros | Contenido / valores clave | Pasos |
|----|--------|-----------|---------------------------|-------|
| DAT-1 | Product2 | 2 protagonistas + relleno | … | EXP-1 |

## 6. Orden de construcción
CMP-2 → CMP-1 → DAT-1 → ejecutar EXP-1 → ejecutar EXP-2

## 7. Supuestos y preguntas abiertas
- Supuesto: …
- Pregunta para el SE: …

## 8. Registro de cambios
- v1: versión inicial a partir del brief del <fecha>.
```

Aprobación: el SE cambia `Estado de revisión` a `APROBADO` y rellena `Revisado por` y
`Fecha de aprobación`. Sin eso la Fase 3 no arranca. La sección 9 (Resultado) la añade la Fase 3,
no se incluye en el borrador porque todavía no hay evidencia.
