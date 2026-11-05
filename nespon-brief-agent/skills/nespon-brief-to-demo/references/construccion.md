# Fase 3 — Construcción tras la aprobación

Se ejecuta en Agentforce Vibes o Claude Code, con sf CLI conectado a la org de demo. Los comandos
concretos están en `nespon-demo-builder/references/ejecucion-en-org.md`; aquí está el orden y las reglas.

## 1. Puerta de aprobación
```bash
python3 <skill-dir>/scripts/validate_manifest.py demo-<slug>/MANIFIESTO.md --gate
```
Si devuelve error (no está `APROBADO`, falta el revisor o hay errores de validación), **no se
construye**. Explica qué falta. La aprobación verbal del SE en la conversación vale: anótala tú en
la cabecera (`APROBADO`, su nombre, la fecha) y vuelve a pasar la puerta.

Si el SE pide cambios durante la construcción, se crea una nueva versión del manifiesto y vuelve a
pasar por aprobación antes de construir lo cambiado.

## 2. Pre-flight
El de `nespon-demo-builder`: org confirmada como de demo, licencias de las nubes del manifiesto,
locale. Si falta una licencia, marca como `Bloqueado` los componentes afectados y avisa.

## 3. Construir en el orden del manifiesto
Recorre la sección *Orden de construcción*:

| Responsable | Qué haces |
|---|---|
| IA | Construyes (retrieve → modificar → deploy, o datos), verificas y marcas `Hecho` |
| IA+Revisión | Construyes, verificas, marcas `Hecho` y lo añades a la lista "para revisar" del cierre, con dónde verlo |
| Persona | Cuando le toca en el orden, presentas su bloque de *Tareas de persona* y esperas a que el SE confirme; marcas `Hecho` o, si no puede hacerlo ahora, `Persona pendiente` y sigues con lo que no dependa de ella |

Actualiza la columna `Estado` del manifiesto tras cada componente (es el registro de avance).
Si algo falla y no se puede resolver: `Bloqueado` con el motivo en una línea, y sigues.

## 4. Datos
```bash
python3 <skill-dir>/scripts/fill_data.py demo-<slug>/datos/fill-config.json --out demo-<slug>/datos/seed-spec.json
python3 <builder-dir>/scripts/build_seed.py demo-<slug>/datos/seed-spec.json --out demo-<slug>/datos/out --var SE_EMAIL=<email> [--var OWNER_1=<Id> …]
sf data import tree --target-org <alias> --plan demo-<slug>/datos/out/seed-plan.json --json > demo-<slug>/datos/import-result.json
```
Activa después los Flows marcados para activarse tras la carga.

## 5. Verificar y entregar
- Una comprobación por escena (consulta, preview o screenshot de la página si el IDE lo permite).
- `GUIA-DEMO.md` con el formato de `nespon-demo-builder/references/guia-demo.md`, usando el speech
  de `PITCH.md` en el "Qué dices" de cada escena.
- `reset.sh` de `nespon-demo-builder`.
- Resumen final: escenas ✅ / ⚠️ / ❌, componentes IA+Revisión para revisar, tareas de persona pendientes.
