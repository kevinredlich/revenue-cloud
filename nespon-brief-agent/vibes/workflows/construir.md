# /construir — Construir un manifiesto aprobado

Uso: `/construir demo-<slug>`

1. Ejecuta `validate_manifest.py demo-<slug>/MANIFIESTO.md --gate`. Si falla, explica qué falta y para.
2. Pre-flight de `nespon-demo-builder`: org de demo confirmada, licencias, locale.
3. Recorre el orden de construcción: IA → construye y verifica; IA+Revisión → construye y apúntalo
   para revisar; Persona → muestra su bloque de tareas y espera confirmación. Actualiza `Estado`.
4. Datos: `fill_data.py` → `build_seed.py` → `sf data import tree`; activa los Flows indicados.
5. Verifica cada escena y genera `GUIA-DEMO.md` (con el speech de `PITCH.md`) y `reset.sh`.
6. Resume: escenas ✅/⚠️/❌, lo que hay que revisar y las tareas de persona pendientes.
