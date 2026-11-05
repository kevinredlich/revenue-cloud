---
name: revenue-intake
description: >
  Puerta de entrada del flujo de Revenue Cloud de Nespon. Úsala SIEMPRE que el usuario aporte
  requerimientos, notas, un correo, un RFP, un documento o un scan de CPQ Scout de un cliente de
  Revenue Cloud / RLM y todavía no se haya decidido si va a ser DEMO o POC. Genera el brief del
  cliente y la recomendación DEMO/POC, espera la decisión del SE, deriva al agente correcto
  (demo-brief-architect o poc-architect), hace pasar su resultado por el verificador independiente
  rlm-verifier contra rlm-skill y no deja avanzar sin ese visto bueno.
---

# Revenue intake — del requerimiento a la decisión DEMO / POC y a su ejecución

Esta skill **orquesta desde la conversación principal**: es quien lanza los agentes, porque un
subagente no puede lanzar a otros. No diseña la demo ni la POC: prepara el terreno, enruta y verifica.

## Regla obligatoria
**`rlm-skill` se consulta siempre**, en el intake y en cada agente que se invoque, para toda definición
funcional o técnica. Y **todo lo que entreguen los agentes lo revisa `rlm-verifier`**, un revisor
independiente, antes de que el SE lo vea como bueno. Sin `rlm-skill` disponible no hay diseño validado:
todo lo técnico va como SUPUESTO y se dice desde el principio.

## Pasos
1. **Recoger la información.** Documento, correo, notas o scan (`revenue-cloud-poc/scripts/scan_to_poc.py`
   para el JSON de CPQ Scout). Una sola tanda de preguntas como mucho, y solo si falta el cliente o no
   hay ninguna necesidad.
2. **Consultar `rlm-skill`** para clasificar la viabilidad de cada necesidad (Regla cero) y anotar qué
   se leyó.
3. **Generar dos ficheros** en `poc-<slug>/` (o `demo-<slug>/`):
   - `MANIFIESTO-NECESIDADES.md` (`revenue-cloud-poc/references/manifiesto-necesidades.md`): `NEC-n`
     con semáforo 🟢/🟡/🔴 y preguntas.
   - `BRIEF-CLIENTE.md` (`flujo-revenue/references/brief-cliente.md`): una página con contexto,
     necesidades, supuestos y la **recomendación DEMO o POC** con motivo.
4. **Verificar el intake.** Lanza el agente `rlm-verifier` con las rutas de esos dos ficheros. Si el
   dictamen es RECHAZADO o NO VERIFICABLE, corrige y repite; no presentes el brief como bueno.
5. **Presentar y parar.** Resumen corto: brief, semáforo, recomendación y dictamen del verificador.
   **Decide el SE** (DEMO o POC). No sigas sin su respuesta; no la decidas tú.
6. **Derivar** según la decisión, pasando `MANIFIESTO-NECESIDADES.md` y `BRIEF-CLIENTE.md` como brief:
   - **DEMO** → agente `demo-brief-architect` (skills `nespon-brief-to-demo`, `nespon-demo-builder`,
     `rlm-skill`). Genera manifiesto de demo, pitch y datos.
   - **POC / Migración** → agente `poc-architect` (skills `revenue-cloud-poc`, `rlm-skill`). Genera
     hipótesis, `MANIFIESTO-POC.md`, datos e informe de viabilidad.
   Si el agente no está disponible en la sesión, dilo y entrega el brief; no improvises el diseño aquí.
7. **Verificar el resultado del agente.** Cuando devuelva su diseño, lanza `rlm-verifier` sobre todos
   sus artefactos (manifiesto, pitch, datos, informe). Si hay hallazgos bloqueantes, devuélvelos al
   agente para que corrija y vuelve a verificar. Máximo 3 vueltas; si persiste, lleva el desacuerdo al SE.
8. **Registrar el dictamen** en el manifiesto con una línea de cabecera y guardar el informe como
   `VERIFICACION-RLM.md` junto a él:
   `**Verificación de coherencia (rlm-verifier):** APROBADO | CON RESERVAS · <fecha> · VERIFICACION-RLM.md`
   Para una demo, comprueba con `python3 flujo-revenue/scripts/check_verificacion.py <manifiesto>`.
   El validador de la POC (`--approve`, `--gate`) lo exige por sí mismo.
9. **Aprobación del SE** y solo entonces construcción/ejecución. Si el diseño cambia después de la
   verificación, se verifica otra vez antes de construir.

## No hagas
Decidir DEMO/POC por el SE · dar por bueno un diseño sin dictamen APROBADO o CON RESERVAS declaradas ·
inventar objetos, campos o valores · ejecutar nada en una org sin manifiesto aprobado.
