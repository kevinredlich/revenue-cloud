#!/usr/bin/env python3
"""Valida un demo-backlog generado con nespon-demo-builder.

Uso: python3 validate_backlog.py demo-backlog-<slug>-v<N>.md

Sale con código 1 si hay errores. Los avisos no bloquean.
"""
import re
import sys
from collections import Counter

PREFIXES = ["ORG", "SET", "OBJ", "FLD", "RT", "QUE", "PS", "USR", "VR", "FLW", "APR", "AGT", "UI", "DAT"]
ID_RE = re.compile(r"\b(" + "|".join(PREFIXES) + r")-\d+\b")
HU_RE = re.compile(r"^###\s+(HU-\d+\.\d+)\b")

# Campos que el sistema calcula y no admiten carga
SYSTEM_FIELDS = [
    "LastStageChangeDate", "IsClosed", "IsWon", "HasOpenActivity", "HasOverdueTask",
    "LastActivityDate", "LastViewedDate", "LastReferencedDate", "SystemModstamp",
    "IsEscalated", "ClosedDate",
]
AUDIT_FIELDS = ["CreatedDate", "CreatedById", "LastModifiedDate", "LastModifiedById"]
ABS_DATE_RE = re.compile(r"\b20\d\d-\d\d-\d\d\b|\b\d{1,2}/\d{1,2}/20\d\d\b")
TIMING_RE = re.compile(r"\b\d+\s*(min|mins|minutos|minuto)\b", re.IGNORECASE)


def parse(text):
    lines = text.splitlines()
    defined = []          # (id, line_no)
    dat_rows = []         # (id, line)
    hus = {}              # hu_id -> list of lines
    current_hu = None
    build_order = ""
    in_build = False
    section = None
    for i, line in enumerate(lines, 1):
        if line.startswith("# PARTE B"):
            section = "B"
        elif line.startswith("# PARTE A"):
            section = "A"
        m = HU_RE.match(line)
        if m:
            current_hu = m.group(1)
            hus[current_hu] = []
            continue
        if line.startswith("#"):
            current_hu = None
            in_build = line.strip().upper().startswith("## BUILD ORDER")
            continue
        if current_hu:
            hus[current_hu].append(line)
        if in_build:
            build_order += " " + line
        # filas de tabla del manifiesto: primera celda es un ID
        if line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and re.fullmatch(r"(" + "|".join(PREFIXES) + r")-\d+", cells[0]):
                defined.append((cells[0], i))
                if cells[0].startswith("DAT-"):
                    dat_rows.append((cells[0], line))
    return defined, dat_rows, hus, build_order, section


def main(path):
    text = open(path, encoding="utf-8").read()
    errors, warnings = [], []
    defined, dat_rows, hus, build_order, _ = parse(text)

    ids = [d for d, _ in defined]
    for dup, n in Counter(ids).items():
        if n > 1:
            errors.append(f"{dup} definido {n} veces (define-once)")
    id_set = set(ids)

    if "# PARTE B" not in text:
        errors.append("Falta '# PARTE B — CONFIGURATION MANIFEST'")
    if not hus:
        errors.append("No se encontraron historias '### HU-N.M'")

    # Config refs en HUs
    referenced = set()
    wow_hus = []
    for hu, body in hus.items():
        joined = "\n".join(body)
        refs_line = next((l for l in body if "Config refs" in l), None)
        if not refs_line:
            errors.append(f"{hu}: falta 'Config refs'")
        else:
            for r in ID_RE.finditer(refs_line):
                rid = r.group(0)
                referenced.add(rid)
                if rid not in id_set:
                    errors.append(f"{hu}: Config ref {rid} no está definido en el manifiesto")
        if "Done" not in joined or "Given" not in joined or "Then" not in joined:
            errors.append(f"{hu}: falta criterio Done en Gherkin (Given/When/Then)")
        cls_line = next((l for l in body if "Clasificación" in l), "")
        if not any(e in cls_line for e in ("🟢", "🔵", "🟠")):
            errors.append(f"{hu}: falta clasificación 🟢/🔵/🟠")
        if "🟠" in cls_line and "Justific" not in cls_line:
            errors.append(f"{hu}: 🟠 sin justificación")
        if "⭐" in joined:
            wow_hus.append(hu)
            if "Plan B" not in joined:
                warnings.append(f"{hu}: tiene WOW pero no Plan B")
            has_dat = refs_line and re.search(r"\bDAT-\d+\b", refs_line)
            if not has_dat:
                errors.append(f"{hu}: WOW sin datos semilla (ningún DAT en Config refs)")

    if len(wow_hus) < 2:
        errors.append(f"Solo {len(wow_hus)} historia(s) con WOW ⭐; mínimo 2")

    # BUILD ORDER
    if not build_order.strip():
        errors.append("Falta '## BUILD ORDER'")
    else:
        in_bo = {m.group(0) for m in ID_RE.finditer(build_order)}
        for missing in sorted(id_set - in_bo):
            errors.append(f"{missing} no aparece en BUILD ORDER")
        for ghost in sorted(in_bo - id_set):
            errors.append(f"BUILD ORDER cita {ghost}, que no está definido")
        # orden por tipo
        seq = [m.group(1) for m in ID_RE.finditer(build_order)]
        rank = [PREFIXES.index(p) for p in seq]
        for a, b, pa, pb in zip(rank, rank[1:], seq, seq[1:]):
            if b < a:
                warnings.append(f"BUILD ORDER: {pb} aparece después de {pa}; revisa dependencias")
                break

    # Componentes definidos pero no usados por ninguna HU (excepto infra)
    infra = ("ORG-", "SET-", "PS-", "USR-", "QUE-")
    for i in sorted(id_set - referenced):
        if not i.startswith(infra):
            warnings.append(f"{i} no lo referencia ninguna historia (¿sobra?)")

    # Datos semilla
    for did, row in dat_rows:
        for f in SYSTEM_FIELDS:
            if re.search(r"\b" + f + r"\b", row):
                errors.append(f"{did}: usa campo de sistema no cargable '{f}'")
        for f in AUDIT_FIELDS:
            if re.search(r"\b" + f + r"\b", row) and "Set Audit Fields" not in text:
                errors.append(f"{did}: usa '{f}' sin habilitar Set Audit Fields en SET")
        if ABS_DATE_RE.search(row):
            errors.append(f"{did}: fecha absoluta; usa offsets TODAY±N / NOW±Nh")

    if TIMING_RE.search(text):
        errors.append("Aparecen duraciones o minutos; la demo se ordena por actos, no por reloj")

    orange = sum(1 for l in text.splitlines() if l.lstrip().startswith("|") and "🟠" in l)
    if orange > 2:
        warnings.append(f"{orange} filas 🟠 en el manifiesto; ¿se puede bajar alguna a 🔵/🟢?")

    for sec in ("## SUPUESTOS", "## REHEARSAL & RESET"):
        if sec not in text:
            warnings.append(f"Falta sección '{sec}'")
    if "RESTRICCIONES FIJAS" not in text:
        warnings.append("Falta bloque 'RESTRICCIONES FIJAS' en la cabecera")
    m = re.search(r"-v(\d+)\.md$", path)
    if m and int(m.group(1)) > 1 and "## CHANGELOG" not in text:
        warnings.append("Versión > 1 sin '## CHANGELOG'")

    print(f"Componentes: {len(id_set)} · Historias: {len(hus)} · WOW: {len(wow_hus)}")
    for w in warnings:
        print("AVISO  ", w)
    for e in errors:
        print("ERROR  ", e)
    print("OK" if not errors else f"{len(errors)} error(es)")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
