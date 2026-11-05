#!/usr/bin/env python3
"""Valida MANIFIESTO-POC.md (formato de references/manifiesto-poc.md) y gestiona su aprobación.

Adaptación de nespon-brief-to-demo/scripts/validate_manifest.py para la ruta POC:
sustituye NEC/ESC (necesidad/escena, con wow obligatorio) por NEC/HIP/EXP
(necesidad/hipótesis/paso de experimento, sin wow). CMP y DAT se validan igual.

Uso:
  python3 validate_manifest_poc.py M.md                      # validación de diseño (Fase 1)
  python3 validate_manifest_poc.py M.md --strict             # además aplica las reglas de calidad como ERROR
  python3 validate_manifest_poc.py M.md --gate [--org ALIAS] # puerta de ejecución (Fase 3)
  python3 validate_manifest_poc.py M.md --approve "Nombre"   # el SE aprueba: escribe estado, fecha y hash
  python3 validate_manifest_poc.py M.md --json               # salida legible por máquina (CPQ Scout, CI)
  python3 validate_manifest_poc.py M.md --export-cases C.json  # casos de prueba (CASO-n) a JSON

Niveles de exigencia
  Siempre ERROR: estructura, trazabilidad NEC->HIP->EXP->CMP, Fuentes consultadas (rlm-skill), tablas
  3.1 y 3.2 con filas válidas, 3.3 si hay filas ESTÁNDAR A VALIDAR / CUSTOM REAL, valores de API
  conocidos como incorrectos, DOC/DERIVADO sin fuente, y DOC/DERIVADO cuando rlm-skill no estaba
  disponible (sin consulta, todo es SUPUESTO).
  AVISO (ERROR con --strict, --gate o --approve): marcadores <completar>, falta de pre-vuelo (R2),
  falta de casos de prueba con valor esperado (R14), CUSTOM REAL sin alternativa estándar (R12),
  moneda fijada por el origen (R8, solo AVISO) y fuentes externas sin confirmar con describe.

Aprobación (--approve / --gate)
  --approve exige un manifiesto sin errores en modo estricto, pone Estado de revisión: APROBADO,
  Revisado por: <nombre> y Fecha, y escribe 'Hash de aprobación' = sha256 del contenido sin esas
  tres líneas. --gate falla si el estado no es APROBADO o si el contenido cambió tras aprobarse.
  El hash detecta ediciones posteriores; NO prueba quién aprobó. Solo el SE ejecuta --approve
  (o lo pide en el chat con su nombre); un agente nunca inventa el nombre.

--org ALIAS comprueba que el alias aparezca en 'Org objetivo' del manifiesto y que la cabecera la
declare sandbox/scratch/SDO/demo y no producción. Es una comprobación de la declaración, no una
verificación contra la org real.

Sale con 1 si hay errores.
"""
import argparse
import hashlib
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
API_FIX_FILE = os.path.join(HERE, "..", "references", "api-correcciones.json")

RESP = {"IA", "IA+Revisión", "Persona"}
NIVEL = {"🟢", "🔵", "🟠"}
ORIGEN = {"Estándar SF", "Estándar RLM", "Custom object", "N/A"}
ESTADO = {"Pendiente", "Hecho", "Bloqueado", "Persona pendiente"}
CLASE = {"DOC", "DERIVADO", "SUPUESTO"}
VIA = {"ESTÁNDAR", "ESTÁNDAR A VALIDAR", "CUSTOM REAL"}
SYSTEM_FIELDS = ["LastStageChangeDate", "IsClosed", "IsWon", "HasOpenActivity", "LastActivityDate",
                 "LastViewedDate", "SystemModstamp", "IsEscalated", "ClosedDate"]
ABS_DATE = re.compile(r"\b20\d\d-\d\d-\d\d\b|\b\d{1,2}/\d{1,2}/20\d\d\b")
KIT_REF = re.compile(r"references/|subskills/|salesforce-help/|\bHelp\b|rlm-skill")
EXTERNAL = re.compile(r"soft-builder|https?://|www\.", re.I)
PLACEHOLDER = re.compile(r"<[A-Za-zÁÉÍÓÚáéíóúñÑ/][^<>\n]*>")
CURRENCY = re.compile(r"\b(?:MXN|USD|EUR|GBP|COP|CLP|ARS|PEN|BRL|CHF)\b|€")
PREFLIGHT = re.compile(r"pre-?vuelo|pre-?flight|prerrequisitos de la org", re.I)
ORG_OK = re.compile(r"sandbox|scratch|\bsdo\b|demo|developer", re.I)
ORG_PROD = re.compile(r"producci[oó]n|production|\bprod\b", re.I)
HASH_LINE = re.compile(r"^\*\*Hash de aprobación:\*\*\s*sha256:([0-9a-f]{64})\s*$", re.M)


def ID(p):
    return re.compile(r"\b" + p + r"-\d+\b")


def load_bad_api():
    with open(API_FIX_FILE, encoding="utf-8") as f:
        return json.load(f)["incorrectos"]


def split_row(line):
    """Divide una fila de tabla markdown respetando `\\|` y las barras dentro de `código`.
    Devuelve None si la línea no es una fila de tabla."""
    s = line.strip()
    if not s.startswith("|"):
        return None
    s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    track_code = s.count("`") % 2 == 0  # con backticks desbalanceados no se confía en ellos
    cells, cur, in_code, i = [], [], False, 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if ch == "`" and track_code:
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append("".join(cur).strip())
    return cells


def rows(text, prefix):
    out = []
    for line in text.splitlines():
        cells = split_row(line)
        if cells and re.fullmatch(prefix + r"-\d+", cells[0]):
            out.append(cells)
    return out


def table_rows(block, header_first_cell):
    """Filas de datos de una tabla (sin cabecera ni separador)."""
    out = []
    for line in block.splitlines():
        cells = split_row(line)
        if not cells or cells[0].lower() == header_first_cell or re.fullmatch(r"[-: ]*", cells[0]):
            continue
        out.append(cells)
    return out


def origen_custom_hint(text):
    return any(len(r) >= 5 and r[4] == "Custom object" for r in rows(text, "CMP"))


def section(text, title_start):
    m = re.search(r"^## " + re.escape(title_start) + r".*?$(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def content_hash(text):
    """sha256 del manifiesto sin las líneas de aprobación (Estado, Revisado por, Hash)."""
    text = text.replace("\r\n", "\n")
    kept = [ln.rstrip() for ln in text.split("\n")
            if not ln.startswith(("**Estado de revisión:**", "**Revisado por:**", "**Hash de aprobación:**"))]
    norm = "\n".join(kept).strip() + "\n"
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def analyze(text, require_approved=False, strict=False, org=None):
    """Devuelve dict con errores (E), avisos (W) y datos de resumen (info)."""
    text = text.replace("\r\n", "\n")
    E, W = [], []

    def quality(msg):  # regla de calidad: aviso en diseño, error en modo estricto
        (E if strict else W).append(msg)

    info = {"hash_ok": None}

    # --- Estado y aprobación ---------------------------------------------------------------
    n_estado = len(re.findall(r"^\*\*Estado de revisión:\*\*", text, re.M))
    if n_estado > 1:
        E.append("Cabecera: hay más de una línea 'Estado de revisión' (ambigüedad en la aprobación)")
    m = re.search(r"^\*\*Estado de revisión:\*\*\s*([A-ZÁÉÍÓÚ]+)", text, re.M)
    estado = m.group(1) if m else None
    info["estado"] = estado
    if estado not in ("BORRADOR", "APROBADO"):
        E.append("Cabecera: 'Estado de revisión' debe ser BORRADOR o APROBADO")
    if not re.search(r"^\*\*Revisado por:\*\*", text, re.M):
        E.append("Cabecera: falta la línea 'Revisado por' / 'Fecha de aprobación'")
    if estado == "APROBADO":
        rv = re.search(r"^\*\*Revisado por:\*\*\s*([^·\n]+)", text, re.M)
        if not rv or rv.group(1).strip() in ("—", "-", ""):
            E.append("APROBADO sin 'Revisado por'")
        hm = HASH_LINE.search(text)
        if not hm:
            (E if require_approved else W).append(
                "APROBADO sin 'Hash de aprobación': aprobación sin ligar al contenido; "
                "reaprobar con --approve")
            info["hash_ok"] = False
        elif hm.group(1) != content_hash(text):
            (E if require_approved else W).append(
                "El manifiesto se modificó después de aprobarse (el hash no coincide); "
                "hay que revisarlo y reaprobar con --approve")
            info["hash_ok"] = False
        else:
            info["hash_ok"] = True
    if require_approved and estado != "APROBADO":
        E.append("PUERTA: el manifiesto no está APROBADO; no se puede ejecutar el experimento")

    # --- Org objetivo (solo con --org) ------------------------------------------------------
    if org:
        om = re.search(r"\*\*Org objetivo:\*\*\s*([^\n]*)", text)
        decl = om.group(1).strip() if om else ""
        if not decl or PLACEHOLDER.search(decl):
            E.append("PUERTA: 'Org objetivo' vacía o sin completar; no se ejecuta sin una org declarada")
        else:
            if not re.search(r"(?<![\w-])" + re.escape(org) + r"(?![\w-])", decl, re.I):
                E.append(f"PUERTA: la org '{org}' no coincide con la 'Org objetivo' del manifiesto ({decl[:60]})")
            if ORG_PROD.search(decl):
                E.append("PUERTA: la 'Org objetivo' está marcada como producción; la Fase 3 de una POC solo "
                         "se ejecuta en sandbox, scratch o SDO")
            elif not ORG_OK.search(decl):
                E.append("PUERTA: 'Org objetivo' no declara sandbox, scratch, SDO o demo")

    if not re.search(r"\*\*Incertidumbre:\*\*\s*\S", text):
        E.append("Cabecera: falta 'Incertidumbre' (la pregunta que hay que responder)")

    # --- Regla cero: Fuentes consultadas ----------------------------------------------------
    fu = re.search(r"\*\*Fuentes consultadas \(rlm-skill\):\*\*\s*([^\n]*)", text)
    fuentes = fu.group(1).strip() if fu else ""
    fuentes_no = False
    if not fu:
        E.append("Cabecera: falta 'Fuentes consultadas (rlm-skill)' (Regla cero: consultar rlm-skill antes de diseñar)")
    elif re.search(r"no disponible|ninguna|^[—-]$|^$|<", fuentes, re.I):
        fuentes_no = True
        W.append("rlm-skill no consultada o no disponible: el diseño técnico no está validado; "
                 "todo debe constar como SUPUESTO en 3.1")

    # --- Valores de API conocidos como incorrectos --------------------------------------------
    bad_api = load_bad_api()
    for tok in re.findall(r"`([^`\n]+)`", text):
        if tok in bad_api:
            E.append(f"Valor de API incorrecto `{tok}`: usar {bad_api[tok]} "
                     "(references/api-correcciones.json y sección 4 de las reglas)")

    sec7 = section(text, "7.")

    # --- 3.1 Verificación de nombres y valores de API ---------------------------------------
    ver = section(text, "3.1")
    clases = {"DOC": 0, "DERIVADO": 0, "SUPUESTO": 0}
    externas = 0
    for cells in table_rows(ver, "objeto"):
        if len(cells) < 5:
            E.append(f"3.1: fila con {len(cells)} columnas (esperadas 5: Objeto | Campo | Valor | Clase | Referencia)")
            continue
        obj, campo, valor, clase, ref = cells[:5]
        if clase not in CLASE:
            E.append(f"3.1 {obj}/{campo}: Clase '{clase}' no válida (DOC | DERIVADO | SUPUESTO)")
            continue
        clases[clase] += 1
        if clase in ("DOC", "DERIVADO"):
            if ref in ("—", "-", ""):
                E.append(f"3.1 {obj}/{campo}: {clase} sin referencia (fichero del kit o artículo de Help)")
            elif EXTERNAL.search(ref):
                externas += 1
                if clase == "DOC":
                    E.append(f"3.1 {obj}/{campo}: DOC con fuente externa; una fuente de terceros solo "
                             "puede ser DERIVADO (contrastada con la Help) o SUPUESTO")
                elif not re.search(r"\bHelp\b", ref):
                    E.append(f"3.1 {obj}/{campo}: DERIVADO de fuente externa sin contrastar con la "
                             "etiqueta de la Help; sin ese contraste es SUPUESTO")
            elif not KIT_REF.search(ref):
                E.append(f"3.1 {obj}/{campo}: {clase} sin fuente reconocible (ruta del kit rlm-skill o "
                         "artículo de la Help)")
    info["clases"] = clases
    if not ver.strip():
        E.append("Falta '## 3.1 Verificación de nombres y valores de API' (nombres y valores de API sin respaldo documental)")
    elif sum(clases.values()) == 0:
        E.append("3.1 no tiene filas válidas: registra cada objeto, campo y valor de API usado en la sección 3")
    if fuentes_no and (clases["DOC"] or clases["DERIVADO"]):
        E.append("Con rlm-skill no disponible no puede haber filas DOC/DERIVADO en 3.1: sin consulta, todo es SUPUESTO")
    if clases["SUPUESTO"] and not re.search(r"supuesto", sec7, re.I):
        W.append(f"3.1 tiene {clases['SUPUESTO']} SUPUESTO(s) que no se declaran en la sección 7 con su consulta de validación")
    if externas:
        if re.search(r"describe", sec7, re.I):
            W.append(f"3.1 tiene {externas} fila(s) con fuente externa: no son DOC hasta confirmarse con describe en el pre-vuelo")
        else:
            quality(f"3.1 tiene {externas} fila(s) con fuente externa y la sección 7 no declara el describe "
                    "de confirmación en el pre-vuelo")

    # --- 3.2 Viabilidad por requisito (R12) -------------------------------------------------
    via = section(text, "3.2")
    vias = {v: 0 for v in VIA}
    for cells in table_rows(via, "requisito"):
        if len(cells) < 4:
            E.append(f"3.2: fila con {len(cells)} columnas (esperadas 4)")
            continue
        req, v, ref, det = cells[:4]
        if v not in VIA:
            E.append(f"3.2 {req}: Vía '{v}' no válida (ESTÁNDAR | ESTÁNDAR A VALIDAR | CUSTOM REAL)")
            continue
        vias[v] += 1
        if v in ("ESTÁNDAR", "ESTÁNDAR A VALIDAR") and ref in ("—", "-", ""):
            E.append(f"3.2 {req}: {v} sin referencia (artículo de Help o fichero del kit, incluidos sus límites)")
        if v in ("ESTÁNDAR A VALIDAR", "CUSTOM REAL") and det in ("—", "-", ""):
            E.append(f"3.2 {req}: {v} sin matiz/prueba o sin diseño custom real (objetos reales, esfuerzo, impacto)")
        if v == "CUSTOM REAL" and not re.search(r"alternativa", det, re.I):
            quality(f"3.2 {req}: CUSTOM REAL sin 'Alternativa estándar' más cercana (R12: ofrecer ambas)")
    info["vias"] = vias
    if not via.strip():
        E.append("Falta '## 3.2 Viabilidad por requisito' (R12: cada requisito con vía ESTÁNDAR / ESTÁNDAR A VALIDAR / CUSTOM REAL)")
    elif sum(vias.values()) == 0:
        E.append("3.2 no tiene filas válidas: declara la vía de implementación de cada requisito")

    # --- 3.3 Decisiones de diseño (R13) -----------------------------------------------------
    dec = section(text, "3.3")
    n_dec = 0
    for cells in table_rows(dec, "decisión"):
        n_dec += 1
        if len(cells) < 4:
            E.append(f"3.3: fila con {len(cells)} columnas (esperadas 4)")
            continue
        d, elegida, descartadas, motivo = cells[:4]
        if descartadas in ("—", "-", "") or motivo in ("—", "-", ""):
            E.append(f"3.3 {d}: falta alternativa descartada o motivo (R13: comparar al menos dos alternativas reales)")
    info["decisiones"] = n_dec
    if not dec.strip():
        if vias["ESTÁNDAR A VALIDAR"] + vias["CUSTOM REAL"] > 0:
            E.append("Falta '## 3.3 Decisiones de diseño' (obligatoria con filas ESTÁNDAR A VALIDAR o CUSTOM REAL en 3.2)")
        else:
            W.append("Falta '## 3.3 Decisiones de diseño' (R13: alternativas comparadas y mejor elegida)")

    if origen_custom_hint(text) and vias["CUSTOM REAL"] == 0:
        E.append("Hay componentes con Origen 'Custom object' pero ninguna fila CUSTOM REAL en 3.2 (R12: justificar el custom con diseño real)")

    # --- NEC / HIP / EXP -------------------------------------------------------------------
    nec = rows(text, "NEC")
    nec_ids = {r[0] for r in nec}
    if not nec:
        W.append("No hay necesidades/dudas de origen (NEC-n)")
    for r in nec:
        if len(r) < 3 or r[2] not in ("Brief", "Supuesto", "Scan CPQ Scout"):
            W.append(f"{r[0]}: Origen debería ser 'Brief', 'Supuesto' o 'Scan CPQ Scout'")

    hip = rows(text, "HIP")
    hip_ids = {r[0] for r in hip}
    if not hip:
        E.append("No hay hipótesis (HIP-n)")
    nec_cubiertas = set()
    for r in hip:
        if len(r) < 4 or r[3] in ("—", "-", ""):
            E.append(f"{r[0]}: sin criterio de éxito")
        if len(r) < 5 or r[4] in ("—", "-", ""):
            W.append(f"{r[0]}: sin condición de 'si no se cumple / no concluyente'")
        refs = set(ID("NEC").findall(r[2] if len(r) > 2 else ""))
        if not refs:
            W.append(f"{r[0]}: no cita ninguna necesidad (NEC-n)")
        for x in refs - nec_ids:
            E.append(f"{r[0]}: cita {x}, que no existe en la sección 1")
        nec_cubiertas |= refs
    for x in sorted(nec_ids - nec_cubiertas):
        W.append(f"{x}: ninguna hipótesis la cubre")

    exp = rows(text, "EXP")
    exp_ids = {r[0] for r in exp}
    exp_to_hip = {}
    covered = set()
    for r in exp:
        refs = set(ID("HIP").findall(r[2] if len(r) > 2 else ""))
        exp_to_hip[r[0]] = refs
        if not refs:
            E.append(f"{r[0]}: no se liga a ninguna hipótesis")
        for x in refs - hip_ids:
            E.append(f"{r[0]}: cita {x}, que no existe")
        covered |= refs
        if len(r) < 6 or r[4] in ("—", "-", "") or r[5] in ("—", "-", ""):
            E.append(f"{r[0]}: falta 'Resultado esperado' o 'Evidencia requerida'")
    for x in sorted(hip_ids - covered):
        E.append(f"{x}: ninguna hipótesis tiene pasos de experimento (EXP) que la prueben")
    if not exp:
        E.append("No hay pasos de experimento (EXP-n)")

    # --- CMP -------------------------------------------------------------------------------
    cmp_rows = rows(text, "CMP")
    cmp_ids = [r[0] for r in cmp_rows]
    for d in {x for x in cmp_ids if cmp_ids.count(x) > 1}:
        E.append(f"{d} definido varias veces")
    tareas = section(text, "4.")
    by_exp = set()
    lvl = {"🟢": 0, "🔵": 0, "🟠": 0}
    resp = {"IA": 0, "IA+Revisión": 0, "Persona": 0}
    origen_count = {"Estándar SF": 0, "Estándar RLM": 0, "Custom object": 0, "N/A": 0}
    for r in cmp_rows:
        if len(r) < 11:
            E.append(f"{r[0]}: faltan columnas (esperadas 11, con 'Origen' tras 'Tipo')")
            continue
        _, e, _, _, origen, spec, nivel, rsp, motivo, tam, est = r[:11]
        for x in ID("EXP").findall(e):
            by_exp.add(x)
            if x not in exp_ids:
                E.append(f"{r[0]}: paso {x} no existe")
        if origen not in ORIGEN:
            E.append(f"{r[0]}: Origen '{origen}' no válido (Estándar SF | Estándar RLM | Custom object | N/A)")
        else:
            origen_count[origen] += 1
        if origen == "Custom object" and nivel == "🟢":
            W.append(f"{r[0]}: Origen Custom object con nivel 🟢 (default/config) es inusual — revisa si el nivel o el origen están bien puestos")
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
    for x in sorted(exp_ids - by_exp):
        W.append(f"{x}: ningún componente lo construye")
    info.update(resp=resp, lvl=lvl, origen=origen_count)

    # --- DAT y CASO (R14) ------------------------------------------------------------------
    dat = rows(text, "DAT")
    for r in dat:
        line = " | ".join(r)
        for f in SYSTEM_FIELDS:
            if re.search(r"\b" + f + r"\b", line):
                E.append(f"{r[0]}: usa campo de sistema '{f}'")
        if ABS_DATE.search(line):
            E.append(f"{r[0]}: fecha absoluta; usa TODAY±N")

    casos = rows(text, "CASO")
    casos_cubren = set()
    cases_out = []
    for r in casos:
        if len(r) < 5:
            E.append(f"{r[0]}: faltan columnas (esperadas 5: ID | Caso | Entrada | Resultado esperado | Pasos)")
            continue
        cid, caso, entrada, esperado, pasos = r[:5]
        line = " | ".join(r)
        if ABS_DATE.search(line):
            E.append(f"{cid}: fecha absoluta; usa TODAY±N")
        if esperado in ("—", "-", ""):
            E.append(f"{cid}: sin resultado esperado (R14: valores esperados, p. ej. el precio exacto)")
            continue
        pasos_ids = ID("EXP").findall(pasos)
        for x in pasos_ids:
            if x not in exp_ids:
                E.append(f"{cid}: paso {x} no existe")
            casos_cubren |= exp_to_hip.get(x, set())
        cases_out.append({"id": cid, "caso": caso, "entrada": entrada, "esperado": esperado,
                          "pasos": pasos_ids})
    info["casos"] = len(cases_out)
    info["cases"] = cases_out
    if not casos:
        quality("No hay casos de prueba (CASO-n) con valores esperados (R14: sin ellos no hay prueba funcional)")
    else:
        for x in sorted(hip_ids - casos_cubren):
            quality(f"{x}: ningún caso de prueba (CASO-n) con valor esperado la cubre (R14)")

    # --- Orden de construcción ---------------------------------------------------------------
    orden = section(text, "6.")
    if not orden.strip():
        E.append("Falta '## 6. Orden de construcción'")
    else:
        en_orden = set(ID("CMP").findall(orden)) | set(ID("DAT").findall(orden)) | set(ID("EXP").findall(orden))
        for x in sorted(set(cmp_ids) | {r[0] for r in dat}):
            if x not in en_orden:
                E.append(f"{x} no aparece en el orden de construcción")
        for x in sorted(exp_ids):
            if x not in en_orden:
                W.append(f"{x}: el paso no aparece explícitamente en el orden de construcción")

    # --- Reparto / niveles / secciones finales -------------------------------------------------
    total = sum(resp.values()) or 1
    hdr = re.search(r"\*\*Reparto:\*\*\s*IA (\d+).*?IA\+Revisión (\d+).*?Persona (\d+)", text)
    if hdr and tuple(map(int, hdr.groups())) != (resp["IA"], resp["IA+Revisión"], resp["Persona"]):
        W.append(f"Cabecera 'Reparto' no cuadra con la tabla: IA {resp['IA']} · IA+Revisión {resp['IA+Revisión']} · Persona {resp['Persona']}")
    if lvl["🟠"] / total > 0.10:
        W.append(f"{lvl['🟠']} componentes 🟠 ({lvl['🟠'] * 100 // total}%): más del 10% custom; revisa si es imprescindible para probar la hipótesis")
    if not sec7.strip():
        W.append("Falta '## 7. Supuestos y preguntas abiertas'")
    elif not PREFLIGHT.search(sec7):
        quality("La sección 7 no incluye el pre-vuelo / 'Prerrequisitos de la org' (R2: altas y consultas de solo lectura antes de cargar)")
    if (clases["SUPUESTO"] or re.search(r"supuesto", sec7, re.I)) and not re.search(r"^\*\*Supuestos clave:\*\*", text, re.M):
        W.append("R6: hay supuestos y la cabecera no tiene '**Supuestos clave:**' (los supuestos van en la primera página)")

    # --- Moneda (R8) y marcadores sin completar -------------------------------------------------
    for r in rows(text, "CMP") + rows(text, "EXP") + dat + casos:
        if CURRENCY.search(" | ".join(r)):
            W.append(f"{r[0]}: menciona una moneda concreta; R8: la moneda es un parámetro de la org, no del origen")
            break
    limpio = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    limpio = re.sub(r"`[^`\n]*`", "", limpio)
    marcas = PLACEHOLDER.findall(limpio)
    if marcas:
        quality(f"Hay {len(marcas)} marcador(es) sin completar (p. ej. {marcas[0][:50]!r}); "
                "un manifiesto no se aprueba ni se ejecuta con placeholders")

    info.update(n_nec=len(nec), n_hip=len(hip), n_exp=len(exp), n_cmp=len(cmp_rows), vias=vias, total=total)
    return {"E": E, "W": W, "info": info}


def summary_line(info):
    resp, lvl, org, cl, vi = info["resp"], info["lvl"], info["origen"], info["clases"], info["vias"]
    total = info["total"]
    return (f"Estado: {info['estado']} · Necesidades {info['n_nec']} · Hipótesis {info['n_hip']} · "
            f"Pasos {info['n_exp']} · Componentes {info['n_cmp']} · IA {resp['IA']} ({resp['IA'] * 100 // total}%) · "
            f"IA+Revisión {resp['IA+Revisión']} · Persona {resp['Persona']} · "
            f"🟢 {lvl['🟢']} · 🔵 {lvl['🔵']} · 🟠 {lvl['🟠']} · "
            f"Estándar SF {org['Estándar SF']} · Estándar RLM {org['Estándar RLM']} · "
            f"Custom object {org['Custom object']} · N/A {org['N/A']} · "
            f"API: DOC {cl['DOC']} · DERIVADO {cl['DERIVADO']} · SUPUESTO {cl['SUPUESTO']} · "
            f"Vía: ESTÁNDAR {vi['ESTÁNDAR']} · A VALIDAR {vi['ESTÁNDAR A VALIDAR']} · CUSTOM REAL {vi['CUSTOM REAL']} · "
            f"Decisiones 3.3: {info['decisiones']} · Casos {info['casos']} · "
            f"Hash: {'ok' if info['hash_ok'] else ('sin verificar' if info['hash_ok'] is None else 'NO válido')}")


def approve(path, por):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    por = (por or "").strip()
    if por in ("", "—", "-"):
        print("ERROR   --approve necesita el nombre real de quien aprueba (--approve \"Nombre Apellido\")")
        return 1
    res = analyze(text, require_approved=False, strict=True)
    if res["E"]:
        for e in res["E"]:
            print("ERROR  ", e)
        print(f"No se puede aprobar: {len(res['E'])} error(es) en modo estricto")
        return 1
    h = content_hash(text)
    out = []
    for ln in text.split("\n"):
        if ln.startswith("**Estado de revisión:**"):
            out.append("**Estado de revisión:** APROBADO")
        elif ln.startswith("**Revisado por:**"):
            out.append(f"**Revisado por:** {por} · **Fecha de aprobación:** {date.today().isoformat()}")
            out.append(f"**Hash de aprobación:** sha256:{h}")
        elif ln.startswith("**Hash de aprobación:**"):
            continue
        else:
            out.append(ln)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    check = analyze("\n".join(out), require_approved=True, strict=True)
    if check["E"]:  # no debería pasar: defensa contra un bug de reescritura
        for e in check["E"]:
            print("ERROR  ", e)
        return 1
    print(f"APROBADO por {por} el {date.today().isoformat()} · sha256:{h[:16]}…")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifiesto")
    ap.add_argument("--strict", action="store_true", help="reglas de calidad como ERROR")
    ap.add_argument("--gate", action="store_true", help="puerta de ejecución: APROBADO + hash + estricto")
    ap.add_argument("--org", help="alias de la org donde se va a ejecutar (con --gate)")
    ap.add_argument("--approve", metavar="NOMBRE", help="aprobar el manifiesto como NOMBRE")
    ap.add_argument("--json", action="store_true", help="salida JSON")
    ap.add_argument("--export-cases", metavar="FICHERO", help="escribir los casos CASO-n a JSON")
    args = ap.parse_args(argv)

    if args.approve is not None:
        return approve(args.manifiesto, args.approve)

    text = open(args.manifiesto, encoding="utf-8").read()
    res = analyze(text, require_approved=args.gate, strict=args.strict or args.gate,
                  org=args.org)
    E, W, info = res["E"], res["W"], res["info"]

    if args.export_cases:
        with open(args.export_cases, "w", encoding="utf-8") as f:
            json.dump(info["cases"], f, ensure_ascii=False, indent=2)

    if args.json:
        slim = {k: v for k, v in info.items() if k != "cases"}
        print(json.dumps({"archivo": args.manifiesto, "ok": not E, "estado": info["estado"],
                          "hash_ok": info["hash_ok"], "errores": E, "avisos": W, "resumen": slim},
                         ensure_ascii=False, indent=2))
    else:
        print(summary_line(info))
        for w in W:
            print("AVISO  ", w)
        for e in E:
            print("ERROR  ", e)
        print("OK" if not E else f"{len(E)} error(es)")
    return 1 if E else 0


if __name__ == "__main__":
    sys.exit(main())
