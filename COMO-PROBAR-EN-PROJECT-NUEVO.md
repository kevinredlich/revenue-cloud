# Cómo probar `revenue-cloud-poc` en un Project aparte de Claude

Este paquete contiene todo lo necesario para probar la skill `revenue-cloud-poc` en un Project de
Claude distinto de "Revenue Cloud Factory" (por ejemplo, para que la pruebe otra persona del
equipo sin tocar el Project original, o para validar la skill de forma aislada antes de subirla al
repo de GitHub).

## Contenido del paquete

```
revenue-cloud-poc/
├── SKILL.md                                  # instrucciones completas de la skill (todas las fases)
├── README.md                                 # documentación de la skill (cómo funciona, cómo probarla)
├── references/
│   ├── manifiesto-necesidades.md             # formato de MANIFIESTO-NECESIDADES.md (Fase 0)
│   ├── manifiesto-poc.md                     # formato de MANIFIESTO-POC.md (Fase 1)
│   ├── reglas-modelado-catalogo-rlm.md       # Regla cero (rlm-skill), R1-R9, checklist y valores de API
│   └── informe-viabilidad.md                 # formato del informe de resultado (Fase 3)
├── assets/
│   ├── ejemplo-MANIFIESTO-POC.md             # ejemplo válido (Bodegas Altiplano) — ya pasa el validador
│   └── ejemplo-INFORME-VIABILIDAD.md
├── ejemplos/
│   ├── poc-prosegur-cpq/                     # caso real completo: FASE 0 + FASE 1 APROBADO
│   └── poc-prueba-scan/                      # generado aquí mismo desde sample-scan.json, de ejemplo
└── scripts/
    ├── scan_to_poc.py                        # genera manifiestos desde un scan de CPQ Scout
    └── validate_manifest_poc.py              # valida MANIFIESTO-POC.md

sample-scan.json                              # scan sintético de prueba, para scan_to_poc.py
```

Todo este contenido ya se validó antes de empaquetarlo: los dos ejemplos pasan
`validate_manifest_poc.py` (y `--gate` donde corresponde), y `scan_to_poc.py` se corrió en los dos
modos (`intake` y `poc`) sobre `sample-scan.json` sin errores de ejecución.

## Paso 1 — Crear el Project nuevo en claude.ai

1. En claude.ai, crea un Project nuevo (distinto de "Revenue Cloud Factory").
2. En sus **Project instructions** (instrucciones personalizadas), pega el contenido de
   `revenue-cloud-poc/SKILL.md`. Esto hace que el propio Claude del Project conozca el método sin
   depender de que alguien lo active por nombre — equivalente a tener la skill "cargada" en una
   sesión de Claude Code.
   - Alternativa más fiel al uso real en Claude Code: pega solo un resumen corto pidiendo que siga
     el método descrito en los documentos adjuntos, y sube `SKILL.md` como uno de los documentos
     del Project (ver paso 2). Cualquiera de las dos formas funciona para probar el flujo
     conversacional.
3. Sube como **documentos del Project** (Project knowledge) todos los ficheros de
   `revenue-cloud-poc/` (mantén la estructura de nombres, p. ej.
   `references/manifiesto-poc.md`, `assets/ejemplo-MANIFIESTO-POC.md`, etc. — si el Project no
   permite subcarpetas, sube cada fichero con ese prefijo en el nombre, p. ej.
   `references-manifiesto-poc.md`).
4. Si quieres poder ejecutar los scripts de verdad (`scan_to_poc.py`,
   `validate_manifest_poc.py`) dentro de la propia conversación — no solo que Claude describa el
   formato — necesitas una sesión con ejecución de código (Claude Code, o un Project con el
   bridge/contenedor habilitado, como esta sesión). En un Project de claude.ai "normal" (solo
   chat), Claude puede seguir el método y escribir los manifiestos como texto/artefactos, pero no
   correrá los `.py` — en ese caso, la validación la haces tú mismo copiando los scripts a tu
   máquina (ver Paso 3).

## Paso 2 — Probar el flujo conversacional (Fase 0 → Fase 2)

Dentro del Project nuevo, en una conversación:

1. Pega o adjunta un documento de necesidades de un cliente (puede ser ficticio, o reutilizar el
   caso de ejemplo de `ejemplos/poc-prosegur-cpq/` pidiéndole a Claude que "reconstruya" el brief a
   partir del `MANIFIESTO-NECESIDADES.md` ya incluido, para no reexponer el documento real del
   cliente).
2. Pide explícitamente: *"Activa la skill revenue-cloud-poc"* o *"Sigue el método de
   revenue-cloud-poc con este documento"* si no se dispara solo.
3. Verifica que el resultado sigue la Fase 0: genera primero un `MANIFIESTO-NECESIDADES.md` con
   `NEC-n` + semáforo 🟢/🟡/🔴, preguntas de refinamiento, y una modalidad **propuesta** (no
   decidida) — y que se detiene ahí a esperar confirmación.
4. Confirma la modalidad (POC) y verifica que genera un `MANIFIESTO-POC.md` siguiendo
   exactamente el formato de `references/manifiesto-poc.md` (cabecera completa, NEC/HIP/EXP/CMP/DAT,
   la columna `Origen` en la tabla de componentes, orden de construcción, supuestos).
5. Pide que lo valide — si tienes ejecución de código, corriendo
   `validate_manifest_poc.py`; si no, pidiéndole a Claude que revise manualmente cada regla del
   validador contra el documento que acaba de escribir.
6. Simula la aprobación del SE y verifica que cambia la cabecera a
   `Estado de revisión: APROBADO` con `Revisado por` y `Fecha de aprobación`.
7. Pide la Fase 3 sin org conectada y verifica que **se detiene explícitamente** diciendo
   "PREPARADA, NO EJECUTADA" — nunca debe inventar un resultado de hipótesis sin haber corrido el
   experimento.

## Paso 3 — Probar los scripts de verdad (con ejecución de código)

Si el Project nuevo tiene ejecución de código disponible (Claude Code, o esta misma clase de
sesión), sube también `sample-scan.json` y reproduce exactamente lo que ya se verificó al armar
este paquete:

```bash
# Validar el ejemplo incluido (debe dar "OK")
python3 revenue-cloud-poc/scripts/validate_manifest_poc.py revenue-cloud-poc/assets/ejemplo-MANIFIESTO-POC.md

# Validar el caso real de Prosegur con la puerta de aprobación (debe dar "OK", está APROBADO)
python3 revenue-cloud-poc/scripts/validate_manifest_poc.py revenue-cloud-poc/ejemplos/poc-prosegur-cpq/MANIFIESTO-POC.md --gate

# Generar el manifiesto de necesidades desde un scan sintético
python3 revenue-cloud-poc/scripts/scan_to_poc.py sample-scan.json --cliente "Cliente de prueba" \
    --out revenue-cloud-poc/ejemplos/poc-prueba-scan/MANIFIESTO-NECESIDADES.md

# Generar el pre-borrador de POC desde el mismo scan (tras "confirmar" modalidad)
python3 revenue-cloud-poc/scripts/scan_to_poc.py sample-scan.json --cliente "Cliente de prueba" \
    --modalidad poc --out revenue-cloud-poc/ejemplos/poc-prueba-scan/MANIFIESTO-POC.md

# Confirmar que el pre-borrador NO pasa el validador todavía (comportamiento esperado:
# salen 3 errores porque faltan las secciones 3-8, hay que completarlas a mano)
python3 revenue-cloud-poc/scripts/validate_manifest_poc.py revenue-cloud-poc/ejemplos/poc-prueba-scan/MANIFIESTO-POC.md
```

## Qué NO vas a poder probar aquí (fuera de alcance de un Project aislado)

- **Fase 3 real** (construcción en una org Salesforce): necesita Claude Code con `sf` CLI
  conectado a una org, o el conector Salesforce de claude.ai autorizado. Un Project nuevo sin
  ejecución de código ni conector no puede escribir en ninguna org — y no debe fingir que lo hizo.
- **`rlm-skill`**: no está incluida en este paquete (es grande, ~6.7 MB, y es propia del equipo,
  no de esta skill), pero **es obligatoria para diseñar** una solución real de Revenue Cloud (Regla
  cero de `references/reglas-modelado-catalogo-rlm.md`). Sin ella el manifiesto declara "no
  disponible" en `Fuentes consultadas` y todo lo técnico se marca `SUPUESTO`: sirve para probar el
  flujo y el formato, no como diseño validado.
- **`nespon-brief-to-demo` / `nespon-demo-builder`**: tampoco incluidas aquí. Son necesarias para
  el camino DEMO y para los recursos compartidos (`ia-vs-persona.md`, `impacto.md`,
  `datos-demo.md`, `fill_data.py`). Si el Project nuevo no las tiene, el camino POC descrito arriba
  funciona igual, pero el camino DEMO y la generación real de datos de prueba no se podrán probar
  de extremo a extremo.
