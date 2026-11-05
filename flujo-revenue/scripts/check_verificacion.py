#!/usr/bin/env python3
"""Comprueba que un manifiesto (de demo o de POC) lleva el dictamen de rlm-verifier.

  python3 check_verificacion.py <MANIFIESTO.md> [--json]

Exige en la cabecera `**Verificación de coherencia (rlm-verifier):** APROBADO | CON RESERVAS · fecha ·
fichero` y que el fichero de informe (por defecto VERIFICACION-RLM.md, al lado del manifiesto) exista y
su línea `DICTAMEN:` coincida. Sale con 1 si falta o si el dictamen es RECHAZADO / NO VERIFICABLE.
No prueba que el verificador se ejecutó de verdad: comprueba que el rastro existe y es coherente.
"""
import argparse
import json
import os
import re
import sys

OK = ("APROBADO", "CON RESERVAS")
LINE = re.compile(r"^\*\*Verificación de coherencia \(rlm-verifier\):\*\*\s*(.+)$", re.M)


def check(path):
    errs = []
    with open(path, encoding="utf-8") as fh:
        text = fh.read().replace("\r\n", "\n")
    m = LINE.search(text)
    if not m:
        return ["falta la línea 'Verificación de coherencia (rlm-verifier)' en la cabecera"], None
    valor = m.group(1).strip()
    partes = [p.strip() for p in valor.split("·")]
    dictamen = partes[0]
    if dictamen not in OK:
        errs.append(f"dictamen '{dictamen}' no válido (APROBADO | CON RESERVAS); RECHAZADO, NO VERIFICABLE o sin completar bloquean")
    informe = partes[2] if len(partes) > 2 and partes[2] else "VERIFICACION-RLM.md"
    ruta = os.path.join(os.path.dirname(os.path.abspath(path)), informe)
    if not os.path.isfile(ruta):
        errs.append(f"no existe el informe {informe} junto al manifiesto")
    else:
        with open(ruta, encoding="utf-8") as fh:
            rep = fh.read()
        d = re.search(r"^DICTAMEN:\s*([A-ZÁÉÍÓÚ ]+?)\s*(?:\||$)", rep, re.M)
        if not d:
            errs.append(f"{informe} no contiene una línea 'DICTAMEN:'")
        elif d.group(1).strip() != dictamen:
            errs.append(f"el dictamen del informe ({d.group(1).strip()}) no coincide con el de la cabecera ({dictamen})")
    return errs, dictamen


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifiesto")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    errs, dictamen = check(a.manifiesto)
    if a.json:
        print(json.dumps({"ok": not errs, "dictamen": dictamen, "errores": errs}, ensure_ascii=False, indent=2))
    else:
        for e in errs:
            print("ERROR  ", e)
        print("OK" if not errs else f"{len(errs)} error(es)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
