---
name: nespon-brief-to-demo
description: >
  Convierte el brief de un cliente en un paquete de demo Salesforce listo para revisar y construir:
  manifiesto de desarrollo que separa lo que construye la IA de lo que debe hacer una persona, pitch
  para defender la demo ante el cliente ligando cada escena a una necesidad, y datos de demo
  ficticios y coherentes (cuentas, contactos, oportunidades, casos, actividades, campos rellenos).
  Prioriza configuración estándar, dinámica y vistosa, y escala a custom solo cuando hace falta para
  impactar. Tras la aprobación del manifiesto, ejecuta la construcción en la org con sf CLI desde
  Agentforce Vibes o Claude Code. Úsala SIEMPRE que el usuario comparta un brief, un correo, unas
  notas o una petición de un cliente para montar una demo, pida un manifiesto de desarrollo, un pitch
  o speech de demo, datos ficticios para Salesforce, o quiera construir un manifiesto ya aprobado.
---

# Nespon — del brief a la demo

Conviertes el brief de un cliente en **tres entregables** que el SE revisa, y después en una **org
construida**. Trabajas en tres fases separadas por una revisión humana:

```
FASE 1 · DISEÑO (no toca la org)  →  FASE 2 · REVISIÓN (el SE)  →  FASE 3 · CONSTRUCCIÓN (IDE + sf CLI)
MANIFIESTO.md · PITCH.md · datos/       Estado: APROBADO              org lista + GUIA-DEMO.md + reset.sh
```

Esta skill trae el conocimiento nuevo (brief, impacto, IA vs persona, pitch, datos). Para la
construcción y para el detalle de cada nube usa la skill **`nespon-demo-builder`** (playbooks en
`references/nubes/`, ejecución en `references/ejecucion-en-org.md`, `scripts/build_seed.py`).

## Principios de una demo que gusta

1. **Impacto con lo estándar.** Lo más default posible, pero vistoso y en movimiento. Sube en la
   escalera de impacto (`references/impacto.md`) solo lo necesario: default → configuración →
   automatización visible → custom. Lo custom se acepta cuando produce un wow que lo estándar no da,
   y se justifica por el impacto.
2. **Cada escena responde a una necesidad del brief.** Sin necesidad, no hay escena.
3. **Dinámica, no estática.** El cliente debe ver la plataforma *hacer* cosas: un cambio dispara una
   notificación, un flujo guía, un agente responde, un dashboard se mueve.
4. **Los datos cuentan la historia.** Registros protagonistas con nombre, campos visibles siempre
   rellenos, totales que cuadran con el relato, fechas relativas.
5. **Honestidad en el reparto.** Lo que la IA no puede hacer de forma fiable (asistentes de UI,
   credenciales, licencias, aceptación de términos, juicio comercial) se asigna a una persona con
   instrucciones claras.

---

## FASE 1 — Diseño (solo ficheros; no se escribe en la org)

### 1.1 Analizar el brief
Lee `references/brief.md`. Extrae cliente, sector, zona fiscal, audiencias, necesidades (`NEC-n`),
nubes, restricciones y fecha de la demo. Lo que falte → **Supuesto**. Pregunta solo si falta la nube
o no hay ninguna necesidad identificable (una tanda, mínima). Si hay org conectada, puedes hacer el
pre-flight de solo lectura de `nespon-demo-builder` para saber qué licencias hay.

### 1.2 Diseñar historia y escenas
Protagonista con nombre, 3-6 escenas (`ESC-n`), cada una ligada a ≥1 `NEC`, al menos 2 con wow ⭐.
Usa el catálogo de `references/impacto.md` y el playbook de la nube de `nespon-demo-builder`.

### 1.3 Descomponer en componentes y repartir IA / persona
Cada escena → componentes (`CMP-n`) con nivel 🟢/🔵/🟠 y responsable **IA**, **IA+Revisión** o
**Persona**, según `references/ia-vs-persona.md`. Cada tarea de persona lleva instrucciones paso a paso.

### 1.4 Diseñar los datos de demo
Sigue `references/datos-demo.md`: registros protagonistas escritos a mano (los que sostienen cada
wow) + relleno generado con `scripts/fill_data.py`. Resultado: `datos/seed-spec.json` y
`datos/HISTORIA-DATOS.md` (quién es quién en los datos).

### 1.5 Escribir el pitch
Sigue `references/pitch.md`: necesidad → qué se ve → valor, wows, objeciones y speech por escena.

### 1.6 Validar y entregar para revisión
```bash
python3 <skill-dir>/scripts/validate_manifest.py demo-<slug>/MANIFIESTO.md
```
Corrige los errores. Deja el manifiesto en `Estado de revisión: BORRADOR` y presenta un resumen
corto: escenas y wows, % de componentes que hace la IA, tareas de persona, supuestos y preguntas
abiertas. **Para aquí.** No construyas nada.

Formato exacto de los tres entregables: `references/manifiesto.md` y `references/pitch.md`.
Ejemplo completo: `assets/ejemplo-MANIFIESTO.md` y `assets/ejemplo-PITCH.md`.

## FASE 2 — Revisión (la hace el SE)

El SE revisa y edita. Si pide cambios: nueva versión (`v2`…) con entrada en `Registro de cambios`;
las restricciones del SE se mantienen en todas las versiones. El manifiesto queda aprobado cuando
el SE escribe en la cabecera `Estado de revisión: APROBADO` con su nombre, o lo confirma
explícitamente en la conversación (y entonces lo anotas tú).

## FASE 3 — Construcción (Agentforce Vibes o Claude Code, con sf CLI)

Sigue `references/construccion.md`. En resumen:
1. **Puerta:** sin `APROBADO` en el manifiesto, no se escribe en la org. Sin excepciones.
2. Pre-flight de `nespon-demo-builder` (org de demo confirmada, licencias, locale).
3. Componentes **IA** en el orden de construcción; **IA+Revisión** se construyen y se piden revisar;
   **Persona** se guían paso a paso cuando les toca en el orden.
4. Datos: `fill_data.py` (si hace falta regenerar) → `build_seed.py` → `sf data import tree`.
5. Actualiza la columna `Estado` del manifiesto a medida que avanzas (Hecho / Bloqueado / Persona pendiente).
6. Verifica cada escena y entrega `GUIA-DEMO.md` y `reset.sh` (formatos de `nespon-demo-builder`),
   con el speech del pitch integrado en cada escena.

---

## Ficheros que genera (en `demo-<cliente-slug>/`)

| Fichero | Fase | Para quién |
|---|---|---|
| `MANIFIESTO.md` | 1 | El SE (revisión) y el agente constructor |
| `PITCH.md` | 1 | El SE, para defender la demo |
| `datos/seed-spec.json`, `datos/HISTORIA-DATOS.md` | 1 | Carga y ensayo |
| `GUIA-DEMO.md`, `reset.sh` | 3 | Presentar y refrescar |

## Referencias

| Archivo | Cuándo |
|---|---|
| `references/brief.md` | 1.1: qué extraer del brief y cómo tratar huecos |
| `references/impacto.md` | 1.2: escalera de impacto y catálogo de momentos vistosos |
| `references/ia-vs-persona.md` | 1.3: criterios de reparto y tareas típicas de persona |
| `references/datos-demo.md` | 1.4: reglas de datos ficticios creíbles y `fill_data.py` |
| `references/manifiesto.md` | 1.3-1.6: formato exacto del manifiesto |
| `references/pitch.md` | 1.5: formato del pitch y del speech |
| `references/construccion.md` | Fase 3: ejecución tras la aprobación |

| Script | Para qué |
|---|---|
| `scripts/validate_manifest.py` | Valida el manifiesto antes de entregarlo y antes de construir |
| `scripts/fill_data.py` | Genera relleno realista (cuentas, contactos, oportunidades, casos, tareas) y lo une a los registros protagonistas |
