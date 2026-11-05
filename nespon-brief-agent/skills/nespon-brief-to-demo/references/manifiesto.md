# Formato del MANIFIESTO.md

El validador (`scripts/validate_manifest.py`) depende de estos encabezados, prefijos de ID y
columnas. Español de España; nombres técnicos y API names en inglés. Sin duraciones en horas:
el tamaño va en S / M / L. Ejemplo completo en `assets/ejemplo-MANIFIESTO.md`.

```markdown
# MANIFIESTO DE DESARROLLO — <Cliente> — v<N>

**Estado de revisión:** BORRADOR
**Revisado por:** — · **Fecha de aprobación:** —
**Cliente:** … · **Sector:** … · **Zona fiscal:** Península (IVA 21%)
**Nube ancla:** … · **Nubes de apoyo:** … · **Org objetivo:** …
**Protagonista:** <Nombre Apellido>, <rol>
**Audiencia negocio:** … · **Audiencia técnica:** …
**Restricciones del SE:** <literal> | Ninguna
**Reparto:** IA <n> (<x>%) · IA+Revisión <n> · Persona <n> · **Niveles:** 🟢 <n> · 🔵 <n> · 🟠 <n>

## 1. Necesidades del cliente
| ID | Necesidad | Origen |
|----|-----------|--------|
| NEC-1 | <en lenguaje del cliente, con coste si se conoce> | Brief |
| NEC-2 | … | Supuesto |

## 2. Historia y escenas
**Historia en una frase:** <protagonista, su problema y cómo termina la demo>

| ID | Escena | Necesidades | Qué ve el cliente | Wow | Plan B |
|----|--------|-------------|-------------------|-----|--------|
| ESC-1 | <título> | NEC-1 | <qué pasa en pantalla> | ⭐ <el momento> | <qué enseñar si falla> |
| ESC-2 | <título> | NEC-2 | … | — | — |

## 3. Componentes
| ID | Escena | Componente | Tipo | Especificación | Nivel | Responsable | Motivo | Tamaño | Estado |
|----|--------|------------|------|----------------|-------|-------------|--------|--------|--------|
| CMP-1 | ESC-1 | <nombre> | CustomField | Opportunity.Stage_Entered_Date__c Date | 🔵 | IA | — | S | Pendiente |
| CMP-2 | ESC-1 | <nombre> | Dashboard | <componentes, fuente, formato condicional> | 🟢 | IA+Revisión | Estética a validar | M | Pendiente |
| CMP-3 | ESC-3 | Activar Agentforce | Setup | Einstein Setup → On; Agentforce → On | 🟢 | Persona | Aceptación de términos en la interfaz | S | Pendiente |
```
Reglas de la tabla:
- `Tipo`: tipo de metadata (CustomField, FlexiPage, Flow, Report, Dashboard, PermissionSet,
  BrandingSet, LightningComponentBundle, ApexClass…) o `Setup`, `Datos`, `Externo`.
- `Especificación`: suficiente para construirlo sin preguntar (API name, tipo con parámetros,
  fórmula, condición de entrada y acciones del Flow, componentes del dashboard).
- `Nivel`: 🟢 default/config · 🔵 automatización o custom declarativo · 🟠 código.
- `Responsable`: `IA` | `IA+Revisión` | `Persona` (criterios en `ia-vs-persona.md`).
- `Motivo`: obligatorio (no `—`) si el responsable no es IA o el nivel es 🟠. En 🟠, el motivo es el
  impacto que justifica el custom.
- `Tamaño`: S | M | L. `Estado`: Pendiente | Hecho | Bloqueado | Persona pendiente.

```markdown
## 4. Tareas de persona
### CMP-3 — Activar Agentforce
- **Ruta:** Setup → Einstein Setup → activar; Setup → Agentforce Agents → activar (el nombre del menú puede variar).
- **Valores:** —
- **Comprobar:** aparece Agentforce Agents en Setup y se puede crear un agente.
- **Desbloquea:** CMP-9, CMP-10

## 5. Datos de demo
Spec: `datos/seed-spec.json` (generada con `fill_data.py`) · Historia de los datos: `datos/HISTORIA-DATOS.md`

| ID | Objeto | Registros | Contenido / valores clave | Escenas |
|----|--------|-----------|---------------------------|---------|
| DAT-1 | Account | 1 protagonista + 25 relleno | ACC-ESTRELLA "Bodegas Altiplano SA", Jumilla, todos los campos visibles rellenos | ESC-1, ESC-2 |
| DAT-2 | Opportunity | 3 protagonistas + ~40 relleno | OPP-RIESGO-1..3 con Stage_Entered_Date__c TODAY-35..TODAY-50 | ESC-1 |

## 6. Orden de construcción
CMP-3 → CMP-1 → CMP-2 → … → DAT-1 → DAT-2 → CMP-<flows que se activan tras la carga>
(Persona primero cuando desbloquea; metadata antes que datos; Flows que se dispararían con la carga, después.)

## 7. Supuestos y preguntas abiertas
- Supuesto: …
- Pregunta para el SE: …

## 8. Registro de cambios
- v1: versión inicial a partir del brief del <fecha>.
```

Aprobación: el SE cambia `Estado de revisión` a `APROBADO` y rellena `Revisado por` y
`Fecha de aprobación`. Sin eso la Fase 3 no arranca.
