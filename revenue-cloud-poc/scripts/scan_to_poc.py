#!/usr/bin/env python3
"""Convierte un ScanResult de CPQ Scout (JSON de /api/scan) en el manifiesto que toque, según
el punto del flujo unificado en el que se use. Dos modos (--modalidad):

  intake (por defecto) → MANIFIESTO-NECESIDADES.md: NEC-n + semáforo 🟢/🟡/🔴 + modalidad
    propuesta (DEMO / POC / Migración, con justificación). Es el PRIMER documento que se genera
    a partir de los datos del cliente (aquí, un scan; con un brief escrito a mano lo hace el
    agente directamente). No decide nada por sí solo: el SE o el cliente confirma la modalidad
    sobre este documento antes de seguir.

  poc (tras confirmar modalidad = POC o Migración) → PRE-BORRADOR de MANIFIESTO-POC.md (formato
    de references/manifiesto-poc.md): añade las secciones 2 (Hipótesis y experimento) a partir
    de las mismas filas ya clasificadas. Las secciones 3-8 (Componentes, Tareas de persona,
    Datos, Orden, Supuestos, Registro de cambios) se dejan como plantilla: requieren diseño
    humano/agente. Por eso el resultado de este modo NO pasa validate_manifest_poc.py tal cual —
    hay que completarlo antes.

  Si la modalidad confirmada es DEMO, no se usa este script: se pasa a nespon-brief-to-demo con
  el MANIFIESTO-NECESIDADES.md como brief de entrada (las NEC-n ya extraídas sustituyen la
  lectura manual del documento del cliente).

Uso:
  python3 scan_to_poc.py scan-result.json --cliente "Bodegas Altiplano SA" \
      --sector "Vino (bodega)" --zona-fiscal "Península (IVA 21%)" \
      --out poc-bodegas-altiplano/MANIFIESTO-NECESIDADES.md
  # tras confirmar modalidad:
  python3 scan_to_poc.py scan-result.json --cliente "Bodegas Altiplano SA" --modalidad poc \
      --out poc-bodegas-altiplano/MANIFIESTO-POC.md

El JSON de entrada es el campo "result" de ScanStatusResponse, o el ScanResult directo si
/api/scan lo devuelve sin envolver.
"""
import argparse
import json
import os
import sys
from datetime import date

RISK_TO_HIP = {"medium", "high"}
MIGRATION_TYPE_TO_HIP = {"Rediseño", "Reescritura"}


def load_scan(path):
    data = json.load(open(path, encoding="utf-8"))
    # Acepta tanto ScanStatusResponse completo como el ScanResult desnudo.
    if "result" in data and isinstance(data["result"], dict):
        return data["result"]
    return data


def pick_uncertain_rows(inventory):
    """Filas del inventario que merecen una hipótesis: riesgo medio/alto o migración no directa."""
    out = []
    for row in inventory:
        risk = (row.get("risk") or "").lower()
        mtype = row.get("migration_type") or ""
        if risk in RISK_TO_HIP or mtype in MIGRATION_TYPE_TO_HIP:
            out.append(row)
    return out


def pick_confirmed_rows(inventory):
    """Filas de migración directa y riesgo bajo: no necesitan hipótesis, solo quedan listadas."""
    out = []
    for row in inventory:
        risk = (row.get("risk") or "").lower()
        mtype = row.get("migration_type") or ""
        if risk == "low" and mtype == "Directa":
            out.append(row)
    return out


def _semaforo_row(row):
    """Clasifica una fila del inventario en 🟢/🟡/🔴 para el manifiesto de intake."""
    risk = (row.get("risk") or "").lower()
    mtype = row.get("migration_type") or ""
    if risk == "high" or mtype == "Reescritura":
        return "🔴"
    if risk == "medium" or mtype == "Rediseño":
        return "🟡"
    return "🟢"


def esc(value):
    """Texto seguro para una celda de tabla markdown (el scan trae texto libre con '|' y saltos)."""
    return str(value if value is not None else "?").replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


MAX_NEC = 15


def numbered_rows(inventory, limit=MAX_NEC):
    """Filas del inventario con su NEC-n, IGUAL en intake y poc (la trazabilidad no se rompe entre
    documentos). Orden 🔴→🟡→🟢; todas las filas de riesgo se incluyen siempre, las 🟢 rellenan hasta
    el límite. Devuelve (lista[(nec_id, fila, semáforo)], filas_omitidas)."""
    ranked = sorted(inventory, key=lambda r: {"🔴": 0, "🟡": 1, "🟢": 2}.get(_semaforo_row(r), 1))
    risky = [r for r in ranked if _semaforo_row(r) != "🟢"]
    greens = [r for r in ranked if _semaforo_row(r) == "🟢"]
    shown = risky + greens[:max(0, limit - len(risky))]
    out = [(f"NEC-{i}", r, _semaforo_row(r)) for i, r in enumerate(shown, start=2)]
    return out, len(inventory) - len(shown)


def build_intake_manifest(scan, cliente, sector, zona_fiscal, org_objetivo):
    """
    MANIFIESTO-NECESIDADES.md: primer documento del flujo, antes de decidir modalidad.
    Clasifica cada mecanismo detectado (NEC-n + semáforo) y propone una modalidad —
    el SE/cliente confirma sobre este documento antes de generar el manifiesto definitivo.
    """
    org = scan.get("org", {})
    scores = scan.get("scores", {})
    catalog = scan.get("catalog", {})
    inventory = scan.get("inventory", [])
    risk_level = (scores.get("risk_level") or "").lower()

    uncertain = pick_uncertain_rows(inventory)
    confirmed = pick_confirmed_rows(inventory)

    nec_lines = [
        f"| 🟡 | NEC-1 | Migrar de Salesforce CPQ a Revenue Cloud: "
        f"{catalog.get('total_products', '?')} productos activos, {catalog.get('bundles', '?')} "
        f"bundles, {scan.get('transactions', {}).get('total_quotes', '?')} quotes históricas | "
        f"Necesidad global, se concreta en las filas siguientes | Confirmar prioridades con el "
        f"cliente | Scan CPQ Scout |"
    ]
    numbered, resto = numbered_rows(inventory)
    for nec_id, row, sem in numbered:
        pend = "Ninguna" if sem == "🟢" else (
            "Confirmar si el mecanismo detectado es correcto y si hace falta reproducirlo exacto"
            if sem == "🟡" else
            "Confirmar impacto en negocio; probablemente requiere desarrollo o rediseño de proceso"
        )
        nec_lines.append(
            f"| {sem} | {nec_id} | `{esc(row.get('sbqq_object'))}` "
            f"({esc(row.get('record_count'))} registros) → {esc(row.get('rca_equivalent'))} "
            f"[{esc(row.get('migration_type'))}] | {esc(row.get('notes') or 'Sin notas del scan')} | "
            f"{pend} | Scan CPQ Scout |"
        )
    if resto > 0:
        nec_lines.append(
            f"<!-- + {resto} fila(s) más del inventario, omitidas aquí por brevedad: "
            f"ver detalle completo en el scan_id {scan.get('scan_id', '?')} -->"
        )

    verdes = sum(1 for r in inventory if _semaforo_row(r) == "🟢")
    amarillos = sum(1 for r in inventory if _semaforo_row(r) == "🟡")
    rojos = sum(1 for r in inventory if _semaforo_row(r) == "🔴")

    preguntas = []
    if amarillos or rojos:
        preguntas.append(
            "| 🔴 | NEC-1 | ¿Los mecanismos marcados 🟡/🔴 son los prioritarios para el cliente, "
            "o hay procesos manuales fuera de CPQ que también haya que cubrir? | Decide el alcance "
            "mínimo de la modalidad elegida |"
        )
    if rojos:
        preguntas.append(
            f"| 🟡 | NEC (🔴) | De los {rojos} mecanismo(s) en rojo, ¿cuáles son imprescindibles "
            "para una primera entrega y cuáles se pueden dejar fuera de alcance explícitamente? | "
            "Evita que una POC de migración intente cubrir todo el proyecto |"
        )
    if not preguntas:
        preguntas.append(
            "| 🟡 | NEC-1 | El scan no detectó mecanismos de riesgo medio/alto: ¿el cliente confirma "
            "que no hay procesos de pricing/configurador fuera de lo escaneado (p. ej. manuales o en "
            "otra org)? | Si se confirma, probablemente no hace falta una POC, solo una DEMO |"
        )

    # Modalidad propuesta — heurística: si hay mecanismos 🟡/🔴, la incertidumbre técnica manda
    # (POC); si todo es 🟢 el objetivo es mostrar el recorrido de migración ya resuelto (DEMO).
    if rojos:
        modalidad, estado_poc, justificacion_poc = (
            "POC (migración)", "🟡",
            f"Hay {rojos} mecanismo(s) de riesgo alto (`Reescritura` o `risk=high`) cuya "
            "equivalencia en RLM no es obvia: antes de prometer nada hay que comprobarlo.",
        )
    elif amarillos:
        modalidad, estado_poc, justificacion_poc = (
            "POC (migración)", "🟢",
            f"Hay {amarillos} mecanismo(s) de riesgo medio (`Rediseño` o `risk=medium`): "
            "alcance acotado y claro para una POC.",
        )
    else:
        modalidad, estado_poc, justificacion_poc = (
            "DEMO", "🟢",
            "Todos los mecanismos detectados migran de forma directa (`Directa`, `risk=low`): "
            "no hay incertidumbre técnica que comprobar, el valor está en mostrar el recorrido.",
        )

    md = f"""# MANIFIESTO DE NECESIDADES — {cliente} — v1 (desde scan de CPQ Scout)

**Estado de revisión:** BORRADOR
**Cliente:** {cliente} · **Sector:** {sector} · **Zona fiscal:** {zona_fiscal}
**Origen:** Scan de CPQ Scout · **Org objetivo:** {org_objetivo}

<!-- Generado automáticamente desde scan_id {scan.get('scan_id', '?')} de CPQ Scout
     (org {org.get('org_name', '?')}, {org.get('org_id', '?')}, escaneado {scan.get('scanned_at', '?')}).
     Complexity score: {scores.get('overall', '?')}/100, riesgo {risk_level or '?'}.
     Este documento NO decide nada por sí mismo: el SE o el cliente confirma la modalidad antes
     de pasar al manifiesto definitivo (MANIFIESTO.md de nespon-brief-to-demo si es DEMO, o
     MANIFIESTO-POC.md de esta skill con --modalidad poc si es POC/Migración). -->

## 1. Necesidades (NEC-n) y semáforo
| Estado | ID | Necesidad | Situación / nota del scan | Información pendiente | Fuente |
|--------|-----|-----------|----------------------------|------------------------|--------|
{chr(10).join(nec_lines)}

### Resumen
🟢 Claros: {verdes} · 🟡 Parciales: {amarillos} · 🔴 Indefinidos/bloqueantes: {rojos} ·
Total: {len(inventory)}

## 2. Preguntas de refinamiento
| Prioridad | Requisito | Pregunta | Motivo |
|-----------|-----------|----------|--------|
{chr(10).join(preguntas)}

## 3. Modalidad propuesta
| Modalidad | Estado | Justificación | Pendientes |
|-----------|--------|----------------|------------|
| DEMO | {"🟢" if modalidad == "DEMO" else "🟡"} | {"Recorrido comercial del catálogo migrado." if modalidad == "DEMO" else "Posible como segunda entrega tras validar la POC."} | Confirmar escenario con el cliente |
| POC (migración) | {estado_poc if modalidad.startswith("POC") else "🟡"} | {justificacion_poc if modalidad.startswith("POC") else "Disponible si aparece una duda técnica concreta más adelante."} | Confirmar alcance mínimo con el SE |

**Propuesta:** **{modalidad}**. {justificacion_poc if modalidad.startswith("POC") else "Ver justificación en la tabla."}
Esta es una propuesta técnica, no una aprobación del cliente — confirmar antes de generar el
manifiesto definitivo.

## 4. Decisión (a rellenar tras confirmar)
**Modalidad confirmada:** — · **Confirmado por:** — · **Fecha:** —
**Alcance mínimo acordado:** <completar tras confirmación>
"""
    return md


def build_manifest(scan, cliente, sector, zona_fiscal, org_objetivo):
    org = scan.get("org", {})
    scores = scan.get("scores", {})
    pricing = scan.get("pricing", {})
    apex = scan.get("apex", {})
    catalog = scan.get("catalog", {})
    inventory = scan.get("inventory", [])

    uncertain = pick_uncertain_rows(inventory)
    confirmed = pick_confirmed_rows(inventory)

    nec_lines = []
    nec_lines.append(
        f"| NEC-1 | Migrar de Salesforce CPQ a Revenue Cloud: {catalog.get('total_products', '?')} "
        f"productos activos, {catalog.get('bundles', '?')} bundles, "
        f"{scan.get('transactions', {}).get('total_quotes', '?')} quotes históricas | Scan CPQ Scout |"
    )
    numbered, resto = numbered_rows(inventory)  # misma numeración que el MANIFIESTO-NECESIDADES.md
    nec_of = {}
    for nec_id, row, sem in numbered:
        nec_of[id(row)] = nec_id
        mecanismo = ("migra de forma directa a" if sem == "🟢" else "→ equivalente RLM a comprobar:")
        nec_lines.append(
            f"| {nec_id} | {esc(row.get('sbqq_object'))} ({esc(row.get('record_count'))} registros) "
            f"{mecanismo} {esc(row.get('rca_equivalent'))} [{esc(row.get('migration_type'))}] | Scan CPQ Scout |"
        )
    if resto > 0:
        nec_lines.append(
            f"<!-- + {resto} fila(s) más del inventario (migración directa/riesgo bajo), "
            f"omitidas aquí por brevedad: ver detalle completo en el scan_id {scan.get('scan_id', '?')} -->"
        )

    hip_lines = []
    exp_lines = []
    h = 1
    for row in uncertain:
        nec_ref = nec_of.get(id(row), "NEC-1")
        obj, eq = esc(row.get("sbqq_object")), esc(row.get("rca_equivalent"))
        hip_lines.append(
            f"| HIP-{h} | ¿El mecanismo de `{obj}` "
            f"({esc(row.get('notes') or 'sin notas del scan')}) tiene equivalente estándar en RLM "
            f"({eq}) o requiere un diseño custom real? | NEC-1, {nec_ref} | "
            f"Se reproduce el comportamiento observado en origen usando solo configuración estándar "
            f"de {eq} | Si no hay equivalente estándar, queda NO VALIDADA "
            f"y se documenta en 3.2 como CUSTOM REAL con el mejor diseño (R12/R13) o rediseño de proceso |"
        )
        exp_lines.append(
            f"| EXP-{h} | Configurar {eq} para reproducir "
            f"`{obj}` con un caso representativo del origen | HIP-{h} | "
            f"<caso de prueba extraído del origen — completar> | <qué resultado confirmaría la "
            f"hipótesis — completar> | <consulta/captura/log — completar> |"
        )
        h += 1

    if pricing.get("price_rules_with_apex", 0) or pricing.get("qcp_scripts", 0):
        hip_lines.append(
            f"| HIP-{h} | El pricing con Apex/QCP detectado ({pricing.get('price_rules_with_apex', 0)} "
            f"price rules con Apex, {pricing.get('qcp_scripts', 0)} scripts QCP) tiene un equivalente "
            f"estándar en RLM (expression sets / decision tables) sin reescribir lógica | "
            f"{', '.join(['NEC-1'] + sorted({nec_of[id(r)] for r in uncertain if id(r) in nec_of and any(k in str(r.get('sbqq_object', '')) for k in ('PriceRule', 'QCP', 'QuoteProcess'))}))} | "
            f"El resultado del cálculo coincide con el de origen para los casos de prueba | "
            f"Si la lógica depende de código a medida irreproducible en estándar, queda NO VALIDADA "
            f"y pasa a desarrollo |"
        )
        exp_lines.append(
            f"| EXP-{h} | Reproducir uno de los price rules/QCP con Expression Sets / Decision Tables "
            f"de RLM | HIP-{h} | <caso de prueba del price rule/QCP real — completar> | "
            f"<resultado numérico esperado — completar> | <comparación numérica, consulta — completar> |"
        )
        h += 1

    if apex.get("apex_triggers_on_sbqq", 0) or apex.get("apex_classes_referencing_sbqq", 0):
        hip_lines.append(
            f"| HIP-{h} | Las dependencias de Apex detectadas sobre objetos SBQQ "
            f"({apex.get('apex_triggers_on_sbqq', 0)} triggers, "
            f"{apex.get('apex_classes_referencing_sbqq', 0)} clases) no tienen equivalente bloqueante "
            f"en RLM que impida la migración de ese flujo | NEC-1 | Se identifica para cada "
            f"trigger/clase si su función la cubre RLM estándar o requiere migrarlo/reescribirlo | "
            f"Si bloquea, se documenta como dependencia y pasa a desarrollo, no a esta POC |"
        )
        exp_lines.append(
            f"| EXP-{h} | Revisar cada trigger/clase Apex referenciado y clasificar: "
            f"cubre RLM estándar / requiere migración / requiere reescritura | HIP-{h} | "
            f"Lista de triggers/clases del scan (`details` si está disponible) | "
            f"Clasificación completa sin triggers sin revisar | Tabla de clasificación con motivo |"
        )
        h += 1

    if not hip_lines:
        hip_lines.append(
            "| HIP-1 | <el scan no detectó mecanismos de riesgo medio/alto; formular la hipótesis "
            "a mano si de todas formas se necesita una POC — si no, esto es más bien una DEMO> | "
            "NEC-1 | <completar> | <completar> |"
        )
        exp_lines.append("| EXP-1 | <completar> | HIP-1 | <completar> | <completar> | <completar> |")

    total_cmp_placeholder = (
        "| CMP-1 | EXP-1 | <nombre> | <Tipo> | Estándar SF/Estándar RLM/Custom object/N/A | "
        "<especificación suficiente para construir sin preguntar> | 🟢/🔵/🟠 | "
        "IA/IA+Revisión/Persona | <motivo si no es IA> | S/M/L | Pendiente |"
    )

    hdr_reparto = "IA 0 (0%) · IA+Revisión 0 · Persona 0"
    hdr_niveles = "🟢 0 · 🔵 0 · 🟠 0"

    md = f"""# MANIFIESTO DE DESARROLLO (POC) — {cliente} — v1 (PRE-BORRADOR desde scan)

**Estado de revisión:** BORRADOR
**Revisado por:** — · **Fecha de aprobación:** —
**Cliente:** {cliente} · **Sector:** {sector} · **Zona fiscal:** {zona_fiscal}
**Nube ancla:** Revenue Cloud (RLM) · **Nubes de apoyo:** — · **Org objetivo:** {org_objetivo}
**Incertidumbre:** Migración de Salesforce CPQ a Revenue Cloud — ver hipótesis por mecanismo detectado
**Fuentes consultadas (rlm-skill):** <completar: sub-skills y artículos de Help 264 consultados, o "no disponible">
**Restricciones del SE:** <completar>
**Verificación de coherencia (rlm-verifier):** <pendiente — la rellena el flujo tras pasar el verificador>
**Supuestos clave:** Org objetivo con Revenue Cloud (RLM) provisionado; resto por completar (ver sección 7)
**Reparto:** {hdr_reparto} · **Niveles:** {hdr_niveles}

<!-- Generado automáticamente desde scan_id {scan.get('scan_id', '?')} de CPQ Scout
     (org {org.get('org_name', '?')}, {org.get('org_id', '?')}, escaneado {scan.get('scanned_at', '?')}).
     Complexity score: {scores.get('overall', '?')}/100, riesgo {scores.get('risk_level', '?')}.
     ESTE ES UN PRE-BORRADOR: las secciones 3-8 son plantilla y hay que completarlas antes de
     pasar validate_manifest_poc.py. El Reparto y Niveles de la cabecera están a 0 porque todavía
     no hay componentes definidos; recalcúlalos al rellenar la sección 3. -->

## 1. Contexto y necesidad de origen
| ID | Necesidad / duda del cliente | Origen |
|----|-------------------------------|--------|
{chr(10).join(nec_lines)}

## 2. Hipótesis y experimento
**Hipótesis en una frase:** Los mecanismos de CPQ detectados con riesgo medio/alto tienen
equivalente estándar en Revenue Cloud sin desarrollo a medida.

| ID | Hipótesis | Necesidad | Criterio de éxito | Si no se cumple / no concluyente |
|----|-----------|-----------|--------------------|-----------------------------------|
{chr(10).join(hip_lines)}

| ID | Paso del experimento | Hipótesis | Entrada | Resultado esperado | Evidencia requerida |
|----|------------------------|-----------|---------|----------------------|------------------------|
{chr(10).join(exp_lines)}

## 3. Componentes
<!-- PLANTILLA: completar un componente por cada paso EXP-n antes de validar. -->
| ID | Paso | Componente | Tipo | Origen | Especificación | Nivel | Responsable | Motivo | Tamaño | Estado |
|----|------|------------|------|--------|----------------|-------|-------------|--------|--------|--------|
{total_cmp_placeholder}

## 3.1 Verificación de nombres y valores de API
<!-- PLANTILLA (Regla cero): un registro por cada objeto, campo o valor de API usado. Clase DOC | DERIVADO | SUPUESTO. -->
| Objeto | Campo / valor | Valor usado | Clase | Referencia |
|--------|---------------|-------------|-------|------------|
| <completar> | <completar> | <completar> | <DOC / DERIVADO / SUPUESTO> | <fichero del kit o artículo de Help> |

## 3.2 Viabilidad por requisito
<!-- PLANTILLA (R12): una fila por requisito/hipótesis. Vía = ESTÁNDAR | ESTÁNDAR A VALIDAR | CUSTOM REAL.
     Leer antes el artículo de Help 264 y sus límites vía rlm-skill. CUSTOM REAL = diseño con piezas
     reales de la plataforma + 'Alternativa estándar' más cercana. -->
| Requisito | Vía | Referencia | Matiz / prueba o diseño custom real |
|-----------|-----|------------|--------------------------------------|
| <completar> | <ESTÁNDAR / ESTÁNDAR A VALIDAR / CUSTOM REAL> | <artículo Help o fichero del kit> | <completar> |

## 3.3 Decisiones de diseño (mejor alternativa)
<!-- PLANTILLA (R13): comparar al menos dos alternativas reales y elegir la mejor. -->
| Decisión | Alternativa elegida | Alternativas descartadas | Motivo (encaje RLM, jerarquía, coherencia, mantenimiento, esfuerzo) |
|----------|---------------------|---------------------------|----------------------------------------------------------------------|
| <completar> | <completar> | <completar> | <completar> |

## 4. Tareas de persona
<!-- PLANTILLA: un bloque "### CMP-n — <nombre>" por cada componente con Responsable = Persona. -->

## 5. Datos de prueba
<!-- PLANTILLA: ver references/datos-demo.md de nespon-brief-to-demo. -->
| ID | Objeto | Registros | Contenido / valores clave | Pasos |
|----|--------|-----------|---------------------------|-------|
| DAT-1 | <completar> | <completar> | <completar> | <completar> |

## 6. Orden de construcción
<!-- PLANTILLA: completar tras definir los componentes de la sección 3. -->

## 7. Supuestos y preguntas abiertas
- Generado automáticamente desde el scan {scan.get('scan_id', '?')}; revisar con el SE antes de dar
  por buena ninguna fila.
- Supuesto: la org objetivo ({org_objetivo}) tiene Revenue Cloud (RLM) provisionado.
- Pre-vuelo (Prerrequisitos de la org, R2): <completar — altas y consultas de solo lectura que confirman licencias, permisos y objetos antes de cargar datos>
- Pregunta para el SE: ¿los {len(uncertain)} mecanismo(s) de riesgo medio/alto detectados por el
  scan son los prioritarios, o hay otros del cliente que no aparecen en CPQ (p. ej. procesos
  manuales)?

## 8. Registro de cambios
- v1: pre-borrador generado automáticamente el {date.today().isoformat()} desde el scan de CPQ Scout
  (scan_id {scan.get('scan_id', '?')}). Pendiente de completar secciones 3-8 y revisión del SE.
"""
    return md


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scan_json", help="Fichero JSON con el ScanResult (o ScanStatusResponse) de CPQ Scout")
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--sector", default="<completar>")
    ap.add_argument("--zona-fiscal", default="Península (IVA 21%)")
    ap.add_argument("--org-objetivo", default="<completar — SDO/sandbox con Revenue Cloud provisionado>")
    ap.add_argument("--modalidad", choices=["intake", "poc"], default="intake",
                     help="intake (por defecto): MANIFIESTO-NECESIDADES.md, antes de decidir modalidad. "
                          "poc: PRE-BORRADOR de MANIFIESTO-POC.md, tras confirmar modalidad=POC/Migración.")
    ap.add_argument("--force", action="store_true", help="sobrescribir --out si ya existe")
    ap.add_argument("--out", required=True,
                     help="Ruta de salida: poc-<slug>/MANIFIESTO-NECESIDADES.md (intake) o "
                          "poc-<slug>/MANIFIESTO-POC.md (poc)")
    args = ap.parse_args()

    scan = load_scan(args.scan_json)

    if os.path.exists(args.out) and not args.force:
        print(f"ERROR: {args.out} ya existe; no se sobrescribe (puede tener trabajo del SE). Usa --force.",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)

    if args.modalidad == "intake":
        md = build_intake_manifest(scan, args.cliente, args.sector, args.zona_fiscal, args.org_objetivo)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        inventory = scan.get("inventory", [])
        rojos = sum(1 for r in inventory if _semaforo_row(r) == "🔴")
        amarillos = sum(1 for r in inventory if _semaforo_row(r) == "🟡")
        print(f"MANIFIESTO-NECESIDADES.md escrito en {args.out}")
        print(f"  Semáforo: 🟢 {len(inventory) - rojos - amarillos} · 🟡 {amarillos} · 🔴 {rojos} "
              f"(total {len(inventory)})")
        print("  Modalidad propuesta: ver sección 3 del documento (DEMO o POC/migración).")
        print("  PENDIENTE: confirmar modalidad con el SE/cliente (sección 4) antes de generar el "
              "manifiesto definitivo. Si es POC/Migración, vuelve a correr este script con "
              "--modalidad poc sobre el mismo scan.")
        return 0
    else:
        md = build_manifest(scan, args.cliente, args.sector, args.zona_fiscal, args.org_objetivo)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        uncertain = pick_uncertain_rows(scan.get("inventory", []))
        print(f"Pre-borrador de MANIFIESTO-POC.md escrito en {args.out}")
        print(f"  Hipótesis generadas: {max(1, len(uncertain))}")
        print(f"  Riesgo global del scan: {scan.get('scores', {}).get('risk_level', '?')} "
              f"({scan.get('scores', {}).get('overall', '?')}/100)")
        print("  Los NEC-n coinciden con los del MANIFIESTO-NECESIDADES.md generado del mismo scan.")
        print("  PENDIENTE: completar secciones 3-8 (componentes, datos, orden, supuestos) antes de "
              "pasar validate_manifest_poc.py y de pedir aprobación al SE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
