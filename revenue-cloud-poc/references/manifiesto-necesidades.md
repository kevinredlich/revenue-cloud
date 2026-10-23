# Formato — MANIFIESTO-NECESIDADES.md (Fase 0, intake unificado)

Primer documento del flujo: se genera a partir de los datos del cliente (brief escrito a mano, o
scan de CPQ Scout vía `scripts/scan_to_poc.py`) **antes** de decidir si la entrega es DEMO, POC o
Migración (Migración = POC con origen scan, no es un cuarto formato). No construye nada ni decide
modalidad por sí solo — propone, y el SE/cliente confirma.

## Cabecera obligatoria
```
# MANIFIESTO DE NECESIDADES — <Cliente> — v<n>

**Estado de revisión:** BORRADOR | APROBADO
**Cliente:** <cliente> · **Sector:** <sector> · **Zona fiscal:** <zona fiscal>
**Origen:** Brief del cliente | Scan de CPQ Scout · **Org objetivo:** <org o "pendiente">
```

## 1. Necesidades (NEC-n) y semáforo
Tabla: `Estado | ID | Necesidad | Situación / nota | Información pendiente | Fuente`.

Semáforo (igual criterio que el resto del método):
- 🟢 **Claro** — necesidad expresada o confirmada, sin información pendiente relevante.
- 🟡 **Parcial** — se entiende la necesidad general pero faltan parámetros o hay supuestos sin
  confirmar.
- 🔴 **Indefinido/bloqueante** — falta información esencial o hay contradicciones.

Con origen scan: 🟢 = `risk=low` + `migration_type=Directa`; 🟡 = `risk=medium` o
`migration_type=Rediseño`; 🔴 = `risk=high` o `migration_type=Reescritura`.

Cierra con el resumen: `🟢 Claros: X · 🟡 Parciales: X · 🔴 Indefinidos/bloqueantes: X · Total: X`
(calculado de la tabla, nunca inventado).

## 2. Preguntas de refinamiento
Tabla: `Prioridad (🔴 alta / 🟡 media) | Requisito | Pregunta | Motivo`. En lenguaje de negocio,
nunca preguntando por objetos ni APIs de Salesforce. Agrupa preguntas relacionadas.

## 3. Modalidad propuesta
Tabla: `Modalidad (DEMO / POC-migración) | Estado 🟢/🟡/🔴 | Justificación | Pendientes`,
evaluando cada modalidad respecto a su propio alcance mínimo, no al proyecto completo. Cierra con
una frase: **Propuesta: <DEMO|POC (migración)>.** + justificación de una línea. Esto es una
propuesta técnica, no una aprobación del cliente.

## 4. Decisión (se rellena tras confirmar)
```
**Modalidad confirmada:** — · **Confirmado por:** — · **Fecha:** —
**Alcance mínimo acordado:** <completar>
```

## Qué pasa después
- Si la modalidad confirmada es **DEMO**: pasa el documento a `nespon-brief-to-demo` como brief de
  entrada — las `NEC-n` ya clasificadas sustituyen la lectura manual del brief original.
- Si es **POC o Migración**: continúa con la FASE 1 de `revenue-cloud-poc`, reutilizando las
  `NEC-n` confirmadas (no las re-deriva desde cero). Con origen scan, vuelve a correr
  `scan_to_poc.py --modalidad poc` sobre el mismo JSON.
