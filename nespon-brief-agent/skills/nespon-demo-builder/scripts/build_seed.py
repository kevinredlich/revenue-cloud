#!/usr/bin/env python3
"""Genera ficheros `sf data import tree` a partir de una especificación con fechas relativas.

Uso:
  python3 build_seed.py seed-spec.json --out <carpeta> [--today YYYY-MM-DD]

Especificación (JSON):
  {"client_slug": "...", "objects": [
     {"sobject": "Account", "records": [{"ref": "ACC1", "Name": "..."}]},
     {"sobject": "Opportunity", "records": [{"ref": "OPP1", "AccountId": "@ACC1",
        "CloseDate": "TODAY+20"}]}]}

- Offsets: TODAY, TODAY±N (Date) · NOW, NOW±N{m,h,d} (DateTime, UTC)
- Lookups: "@REF" a un registro de un objeto anterior en la lista
- Variables: "{{SE_EMAIL}}" se sustituye con --var SE_EMAIL=ana@nespon.com (repetible)
- --today fija el día de referencia (por defecto, hoy) para regenerar de forma reproducible
Salida: <sobject>-<n>.json (≤200 registros) + seed-plan.json
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

SYSTEM_FIELDS = {
    "LastStageChangeDate", "IsClosed", "IsWon", "HasOpenActivity", "HasOverdueTask",
    "LastActivityDate", "LastViewedDate", "LastReferencedDate", "SystemModstamp",
    "IsEscalated", "ClosedDate", "Id",
}
AUDIT_FIELDS = {"CreatedDate", "CreatedById", "LastModifiedDate", "LastModifiedById"}
DATE_RE = re.compile(r"^TODAY(?:([+-])(\d+))?$")
DATETIME_RE = re.compile(r"^NOW(?:([+-])(\d+)([mhd]))?$")
ABS_RE = re.compile(r"^20\d\d-\d\d-\d\d")
CHUNK = 200


def resolve(value, today, now):
    if not isinstance(value, str):
        return value
    m = DATE_RE.match(value)
    if m:
        sign, n = m.groups()
        delta = dt.timedelta(days=int(n or 0)) * (-1 if sign == "-" else 1)
        return (today + delta).isoformat()
    m = DATETIME_RE.match(value)
    if m:
        sign, n, unit = m.groups()
        kw = {"m": "minutes", "h": "hours", "d": "days"}.get(unit, "days")
        delta = dt.timedelta(**{kw: int(n or 0)}) * (-1 if sign == "-" else 1)
        return (now + delta).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--out", required=True)
    ap.add_argument("--today")
    ap.add_argument("--var", action="append", default=[], help="NOMBRE=valor para {{NOMBRE}}")
    a = ap.parse_args()
    variables = dict(v.split("=", 1) for v in a.var)

    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    now = dt.datetime.combine(today, dt.datetime.now(dt.timezone.utc).time())
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    errors, warnings, plan, seen_refs = [], [], [], set()
    for obj in spec.get("objects", []):
        sob = obj["sobject"]
        records = []
        for r in obj.get("records", []):
            ref = r.get("ref")
            if not ref:
                errors.append(f"{sob}: registro sin 'ref'")
                continue
            if ref in seen_refs:
                errors.append(f"ref duplicada: {ref}")
            rec = {"attributes": {"type": sob, "referenceId": ref}}
            for k, v in r.items():
                if k == "ref":
                    continue
                if k in SYSTEM_FIELDS:
                    errors.append(f"{ref}: '{k}' lo calcula el sistema y no se puede cargar")
                if k in AUDIT_FIELDS:
                    warnings.append(f"{ref}: '{k}' requiere Set Audit Fields activado y asignado al usuario de carga")
                if isinstance(v, str) and ABS_RE.match(v):
                    warnings.append(f"{ref}.{k}: fecha absoluta '{v}'; mejor TODAY±N")
                if isinstance(v, str) and v.startswith("@") and v[1:] not in seen_refs:
                    errors.append(f"{ref}.{k}: referencia {v} no definida antes (ordena padres primero)")
                if isinstance(v, str):
                    for name, val in variables.items():
                        v = v.replace("{{" + name + "}}", val)
                    if "{{" in v:
                        errors.append(f"{ref}.{k}: variable sin valor en '{v}' (usa --var)")
                rec[k] = resolve(v, today, now)
            seen_refs.add(ref)
            records.append(rec)
        files = []
        for i in range(0, len(records), CHUNK):
            name = f"{sob}-{i // CHUNK + 1}.json"
            (out / name).write_text(json.dumps({"records": records[i:i + CHUNK]}, ensure_ascii=False, indent=2), encoding="utf-8")
            files.append(name)
        if files:
            plan.append({"sobject": sob, "saveRefs": True, "resolveRefs": True, "files": files})

    (out / "seed-plan.json").write_text(json.dumps(plan, indent=2), encoding="utf-8")
    for w in warnings:
        print("AVISO  ", w)
    for e in errors:
        print("ERROR  ", e)
    total = sum(len(json.loads((out / f).read_text())["records"]) for p in plan for f in p["files"])
    print(f"{total} registros en {len(plan)} objetos · referencia {today.isoformat()} · {out}/seed-plan.json")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
