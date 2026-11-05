# flujo-revenue — del requerimiento a la demo o la POC de Revenue Cloud

Puerta de entrada única. El SE aporta requerimientos o información de un cliente; el flujo devuelve un
**brief del cliente**, una **recomendación DEMO o POC** y, tras la decisión del SE, deriva al agente
correspondiente. En los dos caminos `rlm-skill` es obligatoria y un verificador independiente revisa el resultado.

```
requerimientos / correo / RFP / scan CPQ Scout
        │
        ▼
 skill revenue-intake ── consulta rlm-skill ──► BRIEF-CLIENTE.md + MANIFIESTO-NECESIDADES.md
        │                                        └─► rlm-verifier revisa el intake
        ▼
   Decide el SE ─────────────────┬───────────────────────────┐
                                 ▼                           ▼
                        DEMO: demo-brief-architect   POC / Migración: poc-architect
                        (nespon-brief-to-demo,       (revenue-cloud-poc,
                         nespon-demo-builder,         rlm-skill, ...)
                         rlm-skill)                   
                                 │                           │
                                 └──────────┬────────────────┘
                                            ▼
                         rlm-verifier revisa el diseño contra rlm-skill
                         (nada inventado) → VERIFICACION-RLM.md
                                            ▼
                         Aprobación del SE → construcción / ejecución en org de demo
```

| Pieza | Dónde |
|---|---|
| Skill de entrada y orquestación | `flujo-revenue/skills/revenue-intake/` |
| Agente de POC | `flujo-revenue/agents/poc-architect.md` |
| Agente de demos | `nespon-brief-agent/` (agente + skills `nespon-brief-to-demo`, `nespon-demo-builder`) |
| Verificador independiente | `flujo-revenue/agents/rlm-verifier.md` (solo lectura) |
| Conocimiento técnico obligatorio | `rlm-skill/` (Revenue Cloud release 264) |
| Reglas de modelado R1–R14 | `revenue-cloud-poc/references/reglas-modelado-catalogo-rlm.md` |
| Formato del brief | `flujo-revenue/references/brief-cliente.md` |
| Comprobación del dictamen | `flujo-revenue/scripts/check_verificacion.py` (demos) · `validate_manifest_poc.py` (POC, lo exige solo) |

## Cómo usarlo
Abre Claude Code en la raíz de este repo (`.claude/` ya enlaza agentes y skills) y pega los requerimientos.
La skill `revenue-intake` se activa sola; si no, pídela por su nombre.

## Qué garantiza y qué no
- **Garantiza (mecánico):** un manifiesto de POC no se aprueba ni se ejecuta sin el dictamen del
  verificador (APROBADO o CON RESERVAS) en su cabecera; para demos lo comprueba `check_verificacion.py`.
  Esto lo cubren los tests (`python3 -m unittest discover -s tests -t .` en `revenue-cloud-poc/`).
- **No garantiza:** que el verificador se haya ejecutado de verdad (el script comprueba el rastro, no la
  ejecución), ni que el diseño funcione en una org: eso solo lo demuestra la Fase 3.
- Un subagente no puede lanzar a otro: la orquestación vive en la skill `revenue-intake`, en la sesión principal.
