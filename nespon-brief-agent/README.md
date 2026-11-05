# Agente de demos por brief — Nespon

Recibe el brief de un cliente y prepara su demo de Salesforce en tres fases:

| Fase | Quién | Resultado |
|---|---|---|
| 1 · Diseño | El agente (sin tocar la org) | `MANIFIESTO.md` (qué construye la IA y qué una persona), `PITCH.md` (cómo defender la demo), `datos/` (datos ficticios coherentes) |
| 2 · Revisión | El SE | Manifiesto marcado `APROBADO` |
| 3 · Construcción | El agente en Vibes o Claude Code, con sf CLI | Org lista, `GUIA-DEMO.md` y `reset.sh` |

## Contenido
| Pieza | Qué es |
|---|---|
| `claude-code/agents/demo-brief-architect.md` | El agente para Claude Code (precarga las dos skills) |
| `vibes/rules/demo-brief-architect.md` | El mismo agente para Agentforce Vibes (regla de workspace) |
| `vibes/workflows/brief.md`, `construir.md` | Comandos `/brief` y `/construir` en Vibes |
| `skills/nespon-brief-to-demo/` | Método: brief, impacto, reparto IA/persona, manifiesto, pitch, datos y scripts |
| `skills/nespon-demo-builder/` | Playbooks de 15 nubes, ejecución en la org y generador de carga |

## Integración con `revenue-cloud-poc`
En el flujo de Revenue Cloud, tras el intake (`MANIFIESTO-NECESIDADES.md`) y la confirmación de
modalidad, **si es DEMO la skill `revenue-cloud-poc` delega en este agente** pasándole ese manifiesto
como brief; si es POC o Migración sigue su propio flujo. Para Revenue Cloud el agente consulta además
`rlm-skill` y aplica las reglas R1–R14. En este repo, `.claude/` ya enlaza agente y skills: abrir
Claude Code en la raíz del repo basta, sin ejecutar `install.sh`.

## Instalar
```bash
./install.sh ~/ruta/demos-nespon   # Claude Code + Agentforce Vibes en un proyecto de demos
./install.sh --global              # o Claude Code en todos tus proyectos
```

## Usar
1. **Diseño:** pega el brief ("prepárame la demo de este cliente: …") o usa `/brief` en Vibes.
2. **Revisión:** abre `demo-<cliente>/MANIFIESTO.md`, ajusta lo que quieras y cambia
   `Estado de revisión` a `APROBADO` con tu nombre (o díselo al agente).
3. **Construcción:** con la org de demo conectada (`sf org login web --alias <alias> --set-default`),
   pide "construye la demo de <cliente>" o usa `/construir demo-<cliente>`.

La Fase 1 también se puede hacer en claude.ai subiendo la skill `nespon-brief-to-demo`; después
copia la carpeta `demo-<cliente>/` al proyecto del IDE para construir.

Ejemplo completo (brief, manifiesto, pitch y datos) en `skills/nespon-brief-to-demo/assets/`.
