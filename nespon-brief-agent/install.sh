#!/usr/bin/env bash
# Instala el agente de demos por brief de Nespon.
#   ./install.sh <ruta-proyecto>   -> Claude Code + Agentforce Vibes en ese proyecto
#   ./install.sh --global          -> Claude Code para todos tus proyectos (~/.claude)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SKILLS="nespon-brief-to-demo nespon-demo-builder"

copy_skills() { for s in $SKILLS; do rm -rf "$1/$s"; cp -r "$HERE/skills/$s" "$1/"; done; }

if [[ "${1:-}" == "--global" ]]; then
  mkdir -p ~/.claude/agents ~/.claude/skills
  cp "$HERE/claude-code/agents/demo-brief-architect.md" ~/.claude/agents/
  copy_skills ~/.claude/skills
  echo "Instalado en ~/.claude (Claude Code, todos los proyectos)."; exit 0
fi

P="${1:?uso: ./install.sh <ruta-proyecto> | --global}"
mkdir -p "$P/.claude/agents" "$P/.claude/skills" "$P/.vibes/rules" "$P/.vibes/skills" "$P/.vibes/workflows"
cp "$HERE/claude-code/agents/demo-brief-architect.md" "$P/.claude/agents/"
copy_skills "$P/.claude/skills"
cp "$HERE/vibes/rules/demo-brief-architect.md" "$P/.vibes/rules/"
cp "$HERE/vibes/workflows/"*.md "$P/.vibes/workflows/"
copy_skills "$P/.vibes/skills"
if [[ -d "$P/.a4drules" ]]; then
  mkdir -p "$P/.a4drules/workflows"
  cp "$HERE/vibes/rules/demo-brief-architect.md" "$P/.a4drules/"
  cp "$HERE/vibes/workflows/"*.md "$P/.a4drules/workflows/"
fi
echo "Instalado en $P (Claude Code: .claude/ · Agentforce Vibes: .vibes/)."
