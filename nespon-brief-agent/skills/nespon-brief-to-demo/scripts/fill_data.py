#!/usr/bin/env python3
"""Genera datos de demo ficticios y realistas (España) y los une a los registros protagonistas.

Uso:
  python3 fill_data.py datos/fill-config.json --out datos/seed-spec.json

Salida: seed-spec.json (formato de build_seed.py, fechas relativas) + RESUMEN-RELLENO.md al lado.
Determinista: misma config y mismo "seed" -> mismos datos.
"""
import argparse
import json
import random
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

NOMBRES = ["Lucía", "Javier", "Marta", "Carlos", "Elena", "Pablo", "Sara", "Diego", "Laura", "Andrés",
           "Nuria", "Raúl", "Irene", "Sergio", "Paula", "Álvaro", "Carmen", "Hugo", "Rocío", "Iván",
           "Cristina", "Alberto", "Beatriz", "Fernando", "Patricia", "Jorge", "Silvia", "Manuel",
           "Alicia", "Rubén", "Natalia", "Óscar", "Inés", "Tomás", "Lorena", "Adrián"]
APELLIDOS = ["García", "Martínez", "López", "Sánchez", "Pérez", "Gómez", "Ruiz", "Díaz", "Moreno",
             "Navarro", "Torres", "Ramos", "Gil", "Serrano", "Molina", "Ortega", "Castro", "Rubio",
             "Marín", "Sanz", "Iglesias", "Medina", "Garrido", "Cortés", "Castillo", "Santos",
             "Lozano", "Guerrero", "Cano", "Prieto", "Méndez", "Cruz", "Calvo", "Gallego"]
LUGARES = ["del Levante", "Mediterráneo", "Ibérica", "del Segura", "Costa Cálida", "Altamira",
           "Montesol", "Sierra Espuña", "del Sureste", "Valdelobos", "Puerto Azul", "Los Almendros",
           "La Vega", "Tres Mares", "Peñarrubia", "El Mirador"]
PALABRAS_EMPRESA = ["Distribuciones", "Comercial", "Grupo", "Industrias", "Servicios", "Logística",
                    "Suministros", "Soluciones", "Talleres", "Hermanos"]
CARGOS = [("Gerente", "Dirección"), ("Director Comercial", "Ventas"), ("Directora de Compras", "Compras"),
          ("Responsable de Marketing", "Marketing"), ("Director Financiero", "Finanzas"),
          ("Jefa de Operaciones", "Operaciones"), ("Responsable de IT", "Sistemas"),
          ("Técnico de Compras", "Compras"), ("Key Account Manager", "Ventas")]
CIUDADES = ["Murcia", "Cartagena", "Alicante", "Elche", "Valencia", "Madrid", "Málaga", "Almería",
            "Sevilla", "Zaragoza", "Barcelona", "Bilbao"]
INDUSTRIAS = ["Food & Beverage", "Retail", "Hospitality", "Manufacturing", "Transportation",
              "Construction", "Healthcare", "Technology"]
TAREAS = ["Llamada de seguimiento", "Enviar propuesta revisada", "Reunión de presentación",
          "Revisar condiciones con compras", "Demo de producto", "Confirmar fecha de entrega",
          "Visita a instalaciones"]
CASOS = ["Pedido entregado incompleto", "Duda sobre factura", "Cambio de dirección de envío",
         "Producto dañado en transporte", "Solicitud de documentación", "Retraso en entrega",
         "Alta de nuevo usuario", "Consulta sobre garantía"]
LEAD_STATUS = ["Open - Not Contacted", "Working - Contacted"]
SOURCES = ["Web", "Phone Inquiry", "Partner Referral", "Other"]
CLOSED = {"Closed Won", "Closed Lost"}
SECTOR_ES = {"Food & Beverage": "alimentación y bebidas", "Retail": "distribución minorista",
             "Hospitality": "hostelería", "Manufacturing": "industria", "Transportation": "transporte",
             "Construction": "construcción", "Healthcare": "salud", "Technology": "tecnología",
             "Education": "educación", "Finance": "finanzas", "Energy": "energía"}


def random_fields(rng, spec):
    """{"Campo__c": ["v1","v2"]} -> un valor al azar por registro."""
    return {k: rng.choice(v) for k, v in (spec or {}).items()}


def slug(text):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return "".join(c if c.isalnum() else "-" for c in t).strip("-").replace("--", "-")


def cif(rng, forma):
    letra = "A" if forma == "SA" else "B"
    digits = [rng.randint(0, 9) for _ in range(7)]
    even = sum(digits[i] for i in (1, 3, 5))
    odd = sum(sum(divmod(digits[i] * 2, 10)) for i in (0, 2, 4, 6))
    control = (10 - (even + odd) % 10) % 10
    return letra + "".join(map(str, digits)) + str(control)


def phone(rng, mobile=False):
    first = "6" if mobile else "9"
    n = first + "".join(str(rng.randint(0, 9)) for _ in range(8))
    return f"+34 {n[:3]} {n[3:6]} {n[6:]}"


def weighted(rng, weights):
    items = list(weights.items())
    return rng.choices([k for k, _ in items], weights=[w for _, w in items])[0]


def rint(rng, pair):
    return rng.randint(pair[0], pair[1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    cfg_path = Path(a.config)
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    rng = random.Random(cfg.get("seed", 7))
    owners = cfg.get("owners") or []

    objects = OrderedDict()

    def add(sobject, rec):
        objects.setdefault(sobject, []).append(rec)

    def owner(rec, i):
        if owners:
            rec["OwnerId"] = owners[i % len(owners)]
        return rec

    # Protagonistas primero
    heroes_file = cfg.get("heroes")
    if heroes_file:
        hp = Path(heroes_file)
        if not hp.is_absolute() and not hp.exists():
            hp = cfg_path.parent / Path(heroes_file).name
        if hp.exists():
            for obj in json.loads(hp.read_text(encoding="utf-8")).get("objects", []):
                for r in obj["records"]:
                    add(obj["sobject"], r)
        else:
            print(f"AVISO   no encuentro heroes '{heroes_file}'; sigo solo con relleno")

    used_names = {r.get("Name") for r in objects.get("Account", [])}
    acc_cfg = cfg.get("accounts", {})
    industries = acc_cfg.get("industries") or INDUSTRIAS
    cities = acc_cfg.get("cities") or CIUDADES
    words = acc_cfg.get("company_words") or PALABRAS_EMPRESA
    cif_field = acc_cfg.get("cif_field")
    extra_acc = acc_cfg.get("extra_fields", {})
    accounts = []
    for i in range(acc_cfg.get("count", 0)):
        for _ in range(50):
            forma = rng.choice(["SL", "SL", "SL", "SA"])
            name = f"{rng.choice(words)} {rng.choice(LUGARES + APELLIDOS)} {forma}"
            if name not in used_names:
                break
        used_names.add(name)
        city = rng.choice(cities)
        domain = slug(name.rsplit(" ", 1)[0])
        industry = rng.choice(industries)
        rec = {"ref": f"F-ACC{i + 1}", "Name": name, "Industry": industry,
               "Type": rng.choice(["Customer - Direct", "Customer - Direct", "Prospect"]),
               "BillingCity": city, "BillingCountry": "Spain", "Phone": phone(rng),
               "Website": f"https://www.{domain}.example",
               "NumberOfEmployees": rng.choice([12, 25, 40, 60, 85, 120, 250, 400]),
               "AnnualRevenue": rng.choice([800000, 1500000, 3200000, 6500000, 12000000, 25000000]),
               "Description": f"Cliente de {city}, sector {SECTOR_ES.get(industry, 'servicios')}."}
        if cif_field:
            rec[cif_field] = cif(rng, forma)
        rec.update(extra_acc)
        rec.update(random_fields(rng, acc_cfg.get("random_fields")))
        owner(rec, i)
        add("Account", rec)
        accounts.append((rec, domain, city))

    contacts_by_acc = {}
    cpa = cfg.get("contacts_per_account", [0, 0])
    n = 0
    for rec, domain, city in accounts:
        for _ in range(rint(rng, cpa)):
            n += 1
            fn, ln = rng.choice(NOMBRES), rng.choice(APELLIDOS)
            title, dept = rng.choice(CARGOS)
            c = {"ref": f"F-CON{n}", "FirstName": fn, "LastName": ln, "AccountId": "@" + rec["ref"],
                 "Title": title, "Department": dept, "Email": f"{slug(fn)}.{slug(ln)}@{domain}.example",
                 "Phone": phone(rng), "MobilePhone": phone(rng, True), "MailingCity": city,
                 "MailingCountry": "Spain", "LeadSource": rng.choice(SOURCES)}
            add("Contact", c)
            contacts_by_acc.setdefault(rec["ref"], []).append(c)

    opp_cfg = cfg.get("opportunities", {})
    stage_w = opp_cfg.get("stages", {"Prospecting": 3, "Qualification": 3, "Proposal/Price Quote": 2,
                                     "Negotiation/Review": 1, "Closed Won": 2, "Closed Lost": 1})
    amount = opp_cfg.get("amount", [5000, 60000])
    products = opp_cfg.get("products", ["Proyecto"])
    extra_opp = opp_cfg.get("extra_fields", {})
    opps = []
    n = 0
    for i, (rec, _, _) in enumerate(accounts):
        for _ in range(rint(rng, opp_cfg.get("per_account", [0, 0]))):
            n += 1
            stage = weighted(rng, stage_w)
            amt = round(rng.randint(amount[0], amount[1]) / 500) * 500
            close = f"TODAY-{rng.randint(5, 150)}" if stage in CLOSED else f"TODAY+{rng.randint(5, 85)}"
            o = {"ref": f"F-OPP{n}", "Name": f"{rec['Name'].rsplit(' ', 1)[0]} - {rng.choice(products)}",
                 "AccountId": "@" + rec["ref"], "StageName": stage, "Amount": amt, "CloseDate": close,
                 "Type": rng.choice(["New Customer", "Existing Customer - Upgrade", "Existing Customer - Replacement"]),
                 "LeadSource": rng.choice(SOURCES),
                 "NextStep": "" if stage in CLOSED else rng.choice(TAREAS)}
            if not o["NextStep"]:
                del o["NextStep"]
            o.update(extra_opp)
            o.update(random_fields(rng, opp_cfg.get("random_fields")))
            owner(o, i)
            add("Opportunity", o)
            opps.append(o)

    tpo = cfg.get("tasks_per_opportunity", [0, 0])
    n = 0
    for o in opps:
        acc_ref = o["AccountId"][1:]
        for _ in range(rint(rng, tpo)):
            n += 1
            t = {"ref": f"F-TSK{n}", "Subject": rng.choice(TAREAS), "WhatId": "@" + o["ref"],
                 "Status": "Completed", "Priority": rng.choice(["Normal", "Normal", "High"]),
                 "ActivityDate": f"TODAY-{rng.randint(1, 60)}",
                 "Description": "Seguimiento registrado por el comercial."}
            cons = contacts_by_acc.get(acc_ref)
            if cons:
                t["WhoId"] = "@" + rng.choice(cons)["ref"]
            add("Task", t)

    case_cfg = cfg.get("cases", {})
    for i in range(case_cfg.get("count", 0)):
        if not accounts:
            break
        rec = rng.choice(accounts)[0]
        c = {"ref": f"F-CASE{i + 1}", "Subject": rng.choice(CASOS), "AccountId": "@" + rec["ref"],
             "Status": rng.choice(["New", "Working", "Working", "Escalated", "Closed"]),
             "Priority": rng.choice(["Low", "Medium", "Medium", "High"]),
             "Origin": rng.choice(["Web", "Email", "Phone"]),
             "Description": "El cliente contacta para resolver la incidencia descrita en el asunto."}
        cons = contacts_by_acc.get(rec["ref"])
        if cons:
            c["ContactId"] = "@" + rng.choice(cons)["ref"]
        c.update(case_cfg.get("extra_fields", {}))
        add("Case", c)

    lead_cfg = cfg.get("leads", {})
    for i in range(lead_cfg.get("count", 0)):
        fn, ln = rng.choice(NOMBRES), rng.choice(APELLIDOS)
        company = f"{rng.choice(words)} {rng.choice(LUGARES)} SL"
        title, _ = rng.choice(CARGOS)
        l = {"ref": f"F-LEAD{i + 1}", "FirstName": fn, "LastName": ln, "Company": company, "Title": title,
             "Email": f"{slug(fn)}.{slug(ln)}@{slug(company.rsplit(' ', 1)[0])}.example",
             "Phone": phone(rng, True), "Status": rng.choice(LEAD_STATUS), "LeadSource": rng.choice(SOURCES),
             "Rating": rng.choice(["Hot", "Warm", "Warm", "Cold"]), "Industry": rng.choice(industries),
             "City": rng.choice(cities), "Country": "Spain"}
        owner(l, i)
        add("Lead", l)

    order = ["Account", "Contact", "Lead", "Opportunity", "Case", "Task", "Event"]
    names = sorted(objects, key=lambda s: order.index(s) if s in order else len(order))
    spec = {"client_slug": cfg.get("client_slug", ""), "objects": [{"sobject": s, "records": objects[s]} for s in names]}
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")

    # Resumen para el pitch
    all_opps = objects.get("Opportunity", [])
    open_opps = [o for o in all_opps if o.get("StageName") not in CLOSED]
    by_stage = Counter()
    amt_stage = Counter()
    for o in all_opps:
        by_stage[o.get("StageName")] += 1
        amt_stage[o.get("StageName")] += o.get("Amount", 0) or 0
    lines = ["# Resumen de los datos de demo", "",
             "| Objeto | Registros |", "|---|---|"]
    lines += [f"| {s} | {len(objects[s])} |" for s in names]
    if all_opps:
        pipe = sum(o.get("Amount", 0) or 0 for o in open_opps)
        won = amt_stage.get("Closed Won", 0)
        lines += ["", f"**Pipeline abierto:** {pipe:,.0f} € en {len(open_opps)} oportunidades".replace(",", "."),
                  f"**Ganado:** {won:,.0f} €".replace(",", "."), "",
                  "| Etapa | Oportunidades | Importe (€) |", "|---|---|---|"]
        for s, c in by_stage.most_common():
            lines.append(f"| {s} | {c} | {amt_stage[s]:,.0f} |".replace(",", "."))
    if objects.get("Case"):
        lines += ["", "| Estado de caso | Casos |", "|---|---|"]
        lines += [f"| {k} | {v} |" for k, v in Counter(c.get("Status") for c in objects["Case"]).most_common()]
    (out.parent / "RESUMEN-RELLENO.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    total = sum(len(v) for v in objects.values())
    print(f"{total} registros · " + " · ".join(f"{s} {len(objects[s])}" for s in names) + f" · {out}")


if __name__ == "__main__":
    main()
