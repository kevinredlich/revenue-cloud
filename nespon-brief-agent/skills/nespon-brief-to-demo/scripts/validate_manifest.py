#!/usr/bin/env python3
"""Valida MANIFIESTO.md (formato de references/manifiesto.md).

Uso:
  python3 validate_manifest.py MANIFIESTO.md          # validación de diseño (Fase 1)
  python3 validate_manifest.py MANIFIESTO.md --gate   # además exige APROBADO (Fase 3)
Sale con 1 si hay errores.
"""
import re
import sys

RESP = {"IA", "IA+Revisión", "Persona"}
NIVEL = {"🟢", "🔵", "🟠"}
ESTADO = {"Pendiente", "Hecho", "Bloqueado", "Persona pendiente"}
SYSTEM_FIELDS = ["LastStageChangeDate", "IsClosed", "IsWon", "HasOpenActivity", "LastActivityDate",
                 "LastViewedDate", "SystemModstamp", "IsEscalated", "ClosedDate"]
ABS_DATE = re.compile(r"\b20\d\d-\d\d-\d\d\b|\b\d{1,2}/\d{1,2}/20\d\d\b")
ID = lambda p: re.compile(r"\b" + p + r"-\d+\b")


def rows(text, prefix):
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and re.fullmatch(prefix + r"-\d+", cells[0]):
            out.append(cells)
    return out


def section(text, title_start):
    m = re.search(r"^## " + re.escape(title_start) + r".*?$(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def main(path, gate):
    text = open(path, encoding="utf-8").read()
    E, W = [], []

    m = re.search(r"\*\*Estado de revisión:\*\*\s*([A-ZÁÉÍÓÚ]+)", text)
    estado = m.group(1) if m else None
    if estado not in ("BORRADOR", "APROBADO"):
        E.append("Cabecera: 'Estado de revisión' debe ser BORRADOR o APROBADO")
    if estado == "APROBADO":
        rv = re.search(r"\*\*Revisado por:\*\*\s*([^·\n]+)", text)
        if not rv or rv.group(1).strip() in ("—", "-", ""):
            E.append("APROBADO sin 'Revisado por'")
    if gate and estado != "APROBADO":
        E.append("PUERTA: el manifiesto no está APROBADO; no se puede construir")

    nec = rows(text, "NEC")
    nec_ids = {r[0] for r in nec}
    if not nec:
        E.append("No hay necesidades (NEC-n)")
    for r in nec:
        if len(r) < 3 or r[2] not in ("Brief", "Supuesto"):
            W.append(f"{r[0]}: Origen debería ser 'Brief' o 'Supuesto'")

    esc = rows(text, "ESC")
    esc_ids = {r[0] for r in esc}
    covered = set()
    wow = []
    for r in esc:
        refs = set(ID("NEC").findall(r[2] if len(r) > 2 else ""))
        if not refs:
            E.append(f"{r[0]}: no responde a ninguna necesidad")
        for x in refs - nec_ids:
            E.append(f"{r[0]}: cita {x}, que no existe")
        covered |= refs
        if len(r) > 4 and "⭐" in r[4]:
            wow.append(r[0])
            if len(r) < 6 or r[5] in ("—", "-", ""):
                W.append(f"{r[0]}: wow sin plan B")
    for x in sorted(nec_ids - covered):
        W.append(f"{x}: ninguna escena la cubre")
    if len(wow) < 2:
        E.append(f"Solo {len(wow)} escena(s) con wow ⭐; mínimo 2")

    cmp_rows = rows(text, "CMP")
    cmp_ids = [r[0] for r in cmp_rows]
    for d in {x for x in cmp_ids if cmp_ids.count(x) > 1}:
        E.append(f"{d} definido varias veces")
    tareas = section(text, "4.")
    by_esc = set()
    lvl = {"🟢": 0, "🔵": 0, "🟠": 0}
    resp = {"IA": 0, "IA+Revisión": 0, "Persona": 0}
    for r in cmp_rows:
        if len(r) < 10:
            E.append(f"{r[0]}: faltan columnas (esperadas 10)")
            continue
        _, e, _, _, spec, nivel, rsp, motivo, tam, est = r[:10]
        for x in ID("ESC").findall(e):
            by_esc.add(x)
            if x not in esc_ids:
                E.append(f"{r[0]}: escena {x} no existe")
        nv = next((n for n in NIVEL if n in nivel), None)
        if not nv:
            E.append(f"{r[0]}: nivel debe ser 🟢/🔵/🟠")
        else:
            lvl[nv] += 1
        if rsp not in RESP:
            E.append(f"{r[0]}: responsable '{rsp}' no válido (IA | IA+Revisión | Persona)")
        else:
            resp[rsp] += 1
        sin_motivo = motivo in ("—", "-", "")
        if rsp in ("Persona", "IA+Revisión") and sin_motivo:
            E.append(f"{r[0]}: {rsp} sin motivo")
        if nv == "🟠" and sin_motivo:
            E.append(f"{r[0]}: 🟠 sin motivo de impacto")
        if rsp == "Persona" and not re.search(r"^### " + re.escape(r[0]) + r"\b", tareas, re.M):
            E.append(f"{r[0]}: es Persona y no tiene bloque en '4. Tareas de persona'")
        if tam not in ("S", "M", "L"):
            W.append(f"{r[0]}: tamaño debería ser S, M o L")
        if est not in ESTADO:
            W.append(f"{r[0]}: estado '{est}' no reconocido")
        if spec in ("—", "-", ""):
            E.append(f"{r[0]}: sin especificación")
    for x in sorted(esc_ids - by_esc):
        W.append(f"{x}: ninguna fila de componentes la construye")

    dat = rows(text, "DAT")
    dat_esc = set()
    for r in dat:
        line = " | ".join(r)
        for f in SYSTEM_FIELDS:
            if re.search(r"\b" + f + r"\b", line):
                E.append(f"{r[0]}: usa campo de sistema '{f}'")
        if ABS_DATE.search(line):
            E.append(f"{r[0]}: fecha absoluta; usa TODAY±N")
        dat_esc |= set(ID("ESC").findall(r[-1]))
    for x in wow:
        if x not in dat_esc:
            E.append(f"{x}: tiene wow pero ningún DAT lo alimenta")

    orden = section(text, "6.")
    if not orden.strip():
        E.append("Falta '## 6. Orden de construcción'")
    else:
        en_orden = set(ID("CMP").findall(orden)) | set(ID("DAT").findall(orden))
        for x in sorted(set(cmp_ids) | {r[0] for r in dat}):
            if x not in en_orden:
                E.append(f"{x} no aparece en el orden de construcción")

    total = sum(resp.values()) or 1
    hdr = re.search(r"\*\*Reparto:\*\*\s*IA (\d+).*?IA\+Revisión (\d+).*?Persona (\d+)", text)
    if hdr and tuple(map(int, hdr.groups())) != (resp["IA"], resp["IA+Revisión"], resp["Persona"]):
        W.append(f"Cabecera 'Reparto' no cuadra con la tabla: IA {resp['IA']} · IA+Revisión {resp['IA+Revisión']} · Persona {resp['Persona']}")
    if lvl["🟠"] / total > 0.10:
        W.append(f"{lvl['🟠']} componentes 🟠 ({lvl['🟠'] * 100 // total}%): más del 10% custom; revisa si es por impacto")
    if not section(text, "7.").strip():
        W.append("Falta '## 7. Supuestos y preguntas abiertas'")

    print(f"Estado: {estado} · Necesidades {len(nec)} · Escenas {len(esc)} (wow {len(wow)}) · "
          f"Componentes {len(cmp_rows)} · IA {resp['IA']} ({resp['IA'] * 100 // total}%) · "
          f"IA+Revisión {resp['IA+Revisión']} · Persona {resp['Persona']} · "
          f"🟢 {lvl['🟢']} · 🔵 {lvl['🔵']} · 🟠 {lvl['🟠']}")
    for w in W:
        print("AVISO  ", w)
    for e in E:
        print("ERROR  ", e)
    print("OK" if not E else f"{len(E)} error(es)")
    return 1 if E else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(args[0], "--gate" in sys.argv))
