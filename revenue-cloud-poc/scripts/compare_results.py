#!/usr/bin/env python3
"""Compara los resultados observados de la Fase 3 con los valores esperados de los CASO-n.

Evita "calcular a ojo": los esperados salen del manifiesto aprobado y los observados del log de
ejecución; el veredicto por hipótesis sale de la comparación, no de una impresión.

  python3 validate_manifest_poc.py M.md --export-cases casos.json
  # tras ejecutar, el agente/SE escribe resultados.json: {"CASO-1": "80", "CASO-2": 103.0, ...}
  python3 compare_results.py casos.json resultados.json [--tol 0.01] [--json]

Regla de comparación: si el esperado contiene un número, se compara el primer número con tolerancia
--tol (por defecto 0,01, absoluta); si no, se compara el texto sin distinguir mayúsculas ni espacios.
Un CASO sin observado es NO EJECUTADO (nunca se da por bueno). Veredicto global de las hipótesis:
todos OK -> VALIDADA; mezcla -> PARCIALMENTE VALIDADA; todos mal -> NO VALIDADA; ninguno
ejecutado -> NO EJECUTADA. Los casos no cubren por sí solos las hipótesis sin CASO-n.
Sale con 1 si algún caso ejecutado no coincide.
"""
import argparse
import json
import re
import sys

NUM = re.compile(r"[-+]?\d+(?:[.,]\d+)?")


def to_num(s):
    m = NUM.search(str(s).replace(" ", ""))
    return float(m.group(0).replace(",", ".")) if m else None


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().lower()


def compare(cases, observed, tol=0.01):
    rows = []
    for c in cases:
        cid = c["id"]
        if cid not in observed or observed[cid] in (None, ""):
            rows.append({"id": cid, "estado": "NO EJECUTADO", "esperado": c["esperado"], "observado": None})
            continue
        obs = observed[cid]
        exp_n, obs_n = to_num(c["esperado"]), to_num(obs)
        if exp_n is not None:
            ok = obs_n is not None and abs(exp_n - obs_n) <= tol + 1e-9
        else:
            ok = norm(c["esperado"]) == norm(obs)
        rows.append({"id": cid, "estado": "OK" if ok else "NO COINCIDE",
                     "esperado": c["esperado"], "observado": obs})
    return rows


def veredicto(rows):
    ejec = [r for r in rows if r["estado"] != "NO EJECUTADO"]
    if not ejec:
        return "NO EJECUTADA"
    bien = sum(r["estado"] == "OK" for r in ejec)
    if bien == len(ejec) == len(rows):
        return "VALIDADA"
    if bien == 0:
        return "NO VALIDADA"
    return "PARCIALMENTE VALIDADA"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("casos")
    ap.add_argument("resultados")
    ap.add_argument("--tol", type=float, default=0.01)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    cases = json.load(open(args.casos, encoding="utf-8"))
    observed = json.load(open(args.resultados, encoding="utf-8"))
    rows = compare(cases, observed, args.tol)
    v = veredicto(rows)
    if args.json:
        print(json.dumps({"veredicto": v, "casos": rows}, ensure_ascii=False, indent=2))
    else:
        for r in rows:
            print(f"{r['estado']:<13} {r['id']}: esperado {r['esperado']!r} · observado {r['observado']!r}")
        print(f"Veredicto sobre los casos: {v}")
    return 1 if any(r["estado"] == "NO COINCIDE" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
