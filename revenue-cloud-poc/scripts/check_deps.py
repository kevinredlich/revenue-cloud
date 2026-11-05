#!/usr/bin/env python3
"""Comprueba las dependencias del entorno ANTES de la Fase 3 (ejecución del experimento).

No toca ninguna org ni la red: solo mira el PATH y la versión de Python.

  python3 check_deps.py            # informe legible
  python3 check_deps.py --json     # para CI / CPQ Scout

Requisitos
  Obligatorios (validar, generar y comparar manifiestos): Python >= 3.9, solo biblioteca estándar.
  Para ejecutar contra una org (Fase 3): Salesforce CLI (`sf`) y, para el pre-vuelo y las
  consultas de verificación, una org ya autenticada (`sf org list`). El script no autentica nada.
Sale con 1 si falta algo obligatorio; lo opcional solo avisa (usa --require-sf para exigirlo).
"""
import argparse
import json
import shutil
import subprocess
import sys

MIN_PY = (3, 9)


def check(require_sf=False):
    res = []
    ok_py = sys.version_info >= MIN_PY
    res.append({"nombre": "python", "ok": ok_py, "obligatorio": True,
                "detalle": f"{sys.version.split()[0]} (mínimo {MIN_PY[0]}.{MIN_PY[1]})"})
    sf = shutil.which("sf")
    detalle = "no encontrado en PATH (necesario solo para la Fase 3 contra una org)"
    if sf:
        try:
            out = subprocess.run([sf, "--version"], capture_output=True, text=True, timeout=30)
            detalle = (out.stdout or out.stderr).strip().splitlines()[0] if (out.stdout or out.stderr) else sf
        except (OSError, subprocess.TimeoutExpired):
            detalle = f"{sf} (no se pudo ejecutar --version)"
    res.append({"nombre": "sf (Salesforce CLI)", "ok": bool(sf), "obligatorio": require_sf, "detalle": detalle})
    git = shutil.which("git")
    res.append({"nombre": "git", "ok": bool(git), "obligatorio": False,
                "detalle": git or "no encontrado (opcional)"})
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--require-sf", action="store_true", help="exigir Salesforce CLI (Fase 3)")
    args = ap.parse_args(argv)
    res = check(args.require_sf)
    fallo = any(r["obligatorio"] and not r["ok"] for r in res)
    if args.json:
        print(json.dumps({"ok": not fallo, "dependencias": res}, ensure_ascii=False, indent=2))
    else:
        for r in res:
            marca = "OK   " if r["ok"] else ("FALTA" if r["obligatorio"] else "aviso")
            print(f"{marca} {r['nombre']}: {r['detalle']}")
        print("Listo para validar/generar manifiestos." if not fallo else "Faltan dependencias obligatorias.")
    return 1 if fallo else 0


if __name__ == "__main__":
    sys.exit(main())
