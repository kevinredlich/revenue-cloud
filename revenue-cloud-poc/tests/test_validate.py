import json
import os
import re
import tempfile
import unittest

from tests.helpers import ROOT, SCRIPTS, load, read, run_script

V = load("validate_manifest_poc")
BORRADOR = os.path.join(ROOT, "assets", "ejemplo-MANIFIESTO-POC.md")
APROBADO = os.path.join(ROOT, "assets", "ejemplo-MANIFIESTO-POC-APROBADO.md")
LEGACY = os.path.join(ROOT, "ejemplos", "legacy-v1", "poc-prosegur-cpq", "MANIFIESTO-POC.md")


def tmp(text):
    f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
    f.write(text)
    f.close()
    return f.name


class Ejemplos(unittest.TestCase):
    def test_borrador_valida_sin_avisos_en_estricto(self):
        r = V.analyze(read(BORRADOR), strict=True)
        self.assertEqual(r["E"], [])
        self.assertEqual(r["W"], [])

    def test_borrador_no_pasa_la_puerta(self):
        r = V.analyze(read(BORRADOR), require_approved=True, strict=True)
        self.assertTrue(any("no está APROBADO" in e for e in r["E"]))

    def test_aprobado_pasa_la_puerta(self):
        r = V.analyze(read(APROBADO), require_approved=True, strict=True, org="SDO")
        self.assertEqual(r["E"], [])
        self.assertTrue(r["info"]["hash_ok"])

    def test_legacy_falla_la_puerta(self):
        r = V.analyze(read(LEGACY), require_approved=True, strict=True)
        self.assertGreaterEqual(len(r["E"]), 4)


class Puerta(unittest.TestCase):
    def test_aprobar_a_mano_no_abre_la_puerta(self):
        t = read(BORRADOR).replace("**Estado de revisión:** BORRADOR", "**Estado de revisión:** APROBADO")
        r = V.analyze(t, require_approved=True, strict=True)
        self.assertTrue(any("Hash" in e or "Revisado por" in e for e in r["E"]))

    def test_editar_tras_aprobar_invalida_el_hash(self):
        t = read(APROBADO).replace("Distribuidor Test SL", "Otro SL")
        r = V.analyze(t, require_approved=True, strict=True)
        self.assertTrue(any("hash no coincide" in e for e in r["E"]))

    def test_dos_lineas_de_estado_es_error(self):
        t = read(BORRADOR) + "\n**Estado de revisión:** APROBADO\n"
        self.assertTrue(any("más de una línea" in e for e in V.analyze(t)["E"]))

    def test_org_debe_coincidir_y_no_ser_produccion(self):
        t = read(APROBADO)
        self.assertTrue(any("no coincide" in e for e in V.analyze(t, org="OTRA")["E"]))
        prod = t.replace("SDO con Revenue Cloud provisionado", "Producción CLIENTE")
        errs = V.analyze(prod, org="CLIENTE")["E"]
        self.assertTrue(any("producción" in e for e in errs))

    def test_approve_cli_escribe_hash_y_luego_pasa_la_puerta(self):
        p = tmp(read(BORRADOR))
        try:
            self.assertEqual(run_script("validate_manifest_poc.py", p, "--approve", "Ana Pérez").returncode, 0)
            self.assertEqual(run_script("validate_manifest_poc.py", p, "--gate").returncode, 0)
            self.assertIn("Ana Pérez", read(p))
        finally:
            os.unlink(p)

    def test_approve_rechaza_nombre_vacio_y_manifiesto_con_errores(self):
        p = tmp(read(BORRADOR))
        q = tmp(read(BORRADOR).replace("| CASO-", "| XXX-"))
        try:
            self.assertEqual(run_script("validate_manifest_poc.py", p, "--approve", "").returncode, 1)
            self.assertEqual(run_script("validate_manifest_poc.py", q, "--approve", "Ana").returncode, 1)
            self.assertIn("BORRADOR", read(q))
        finally:
            os.unlink(p)
            os.unlink(q)


class Evidencia(unittest.TestCase):
    def test_sin_fuentes_consultadas_es_error_siempre(self):
        t = re.sub(r"\*\*Fuentes consultadas[^\n]*\n", "", read(BORRADOR))
        self.assertTrue(any("Fuentes consultadas" in e for e in V.analyze(t)["E"]))

    def test_secciones_31_y_32_obligatorias_siempre(self):
        t = read(BORRADOR)
        sin31 = t.replace("## 3.1 Verificación", "## 9. Verificación")
        sin32 = t.replace("## 3.2 Viabilidad", "## 9. Viabilidad")
        self.assertTrue(any("3.1" in e for e in V.analyze(sin31)["E"]))
        self.assertTrue(any("3.2" in e for e in V.analyze(sin32)["E"]))

    def test_valor_de_api_incorrecto_en_backticks(self):
        t = read(BORRADOR).replace("`OneTime`", "`Month`", 1)
        self.assertTrue(any("Month" in e for e in V.analyze(t)["E"]))

    def test_doc_con_fuente_externa_es_error(self):
        t = read(BORRADOR).replace(
            "| DOC | `subskills/revenue-cloud-data-model/domains/pricing.md` (PriceAdjustmentTier) |",
            "| DOC | soft-builder.com/objeto |")
        self.assertTrue(any("fuente externa" in e for e in V.analyze(t)["E"]))

    def test_derivado_externo_sin_help_es_error(self):
        t = read(BORRADOR).replace(
            "| DOC | `references/schema-diff/264-schema.json` (PriceAdjustmentTier.TierValue) |",
            "| DERIVADO | https://ejemplo.com/obj \"TierValue\" |")
        self.assertTrue(any("sin contrastar" in e for e in V.analyze(t)["E"]))

    def test_derivado_sin_referencia_es_error(self):
        t = read(BORRADOR).replace("| DOC | `subskills/revenue-cloud-data-model/domains/pricing.md` (PriceAdjustmentTier) |",
                                   "| DOC | — |")
        self.assertTrue(any("sin referencia" in e for e in V.analyze(t)["E"]))

    def test_sin_rlm_skill_no_hay_doc_ni_derivado(self):
        t = re.sub(r"(\*\*Fuentes consultadas \(rlm-skill\):\*\*)[^\n]*", r"\1 no disponible", read(BORRADOR))
        r = V.analyze(t)
        self.assertTrue(any("no disponible" in e for e in r["E"]))


class Calidad(unittest.TestCase):
    def test_sin_casos_es_aviso_en_diseno_y_error_en_estricto(self):
        t = read(BORRADOR).replace("| CASO-", "| XXX-")
        self.assertTrue(any("CASO" in w for w in V.analyze(t)["W"]))
        self.assertTrue(any("CASO" in e for e in V.analyze(t, strict=True)["E"]))

    def test_placeholder_bloquea_en_estricto(self):
        t = read(BORRADOR).replace("Distribuidor Test SL", "<nombre>")
        self.assertTrue(any("sin completar" in e for e in V.analyze(t, strict=True)["E"]))
        self.assertFalse(any("sin completar" in e for e in V.analyze(t)["E"]))

    def test_moneda_fijada_es_aviso(self):
        t = read(BORRADOR).replace("precio base 42 (moneda de la org", "precio base 42 EUR (moneda de la org")
        self.assertTrue(any("moneda" in w for w in V.analyze(t)["W"]))

    def test_hip_cita_nec_inexistente(self):
        t = read(BORRADOR).replace("| NEC-1, NEC-2 |", "| NEC-1, NEC-9 |")
        self.assertTrue(any("NEC-9" in e for e in V.analyze(t)["E"]))

    def test_fecha_absoluta_en_caso(self):
        t = read(BORRADOR).replace("| Cantidad 30 |", "| Cantidad 30 el 2026-10-01 |")
        self.assertTrue(any("fecha absoluta" in e for e in V.analyze(t)["E"]))

    def test_exp_sin_hipotesis_valida(self):
        t = read(BORRADOR).replace("| EXP-3 | Comparar", "| EXP-3 | Comparar").replace(
            "calculado por el sistema contra el cálculo manual del tramo 100+ | HIP-1 |",
            "calculado por el sistema contra el cálculo manual del tramo 100+ | HIP-7 |")
        self.assertTrue(any("HIP-7" in e for e in V.analyze(t)["E"]))


class Parser(unittest.TestCase):
    def test_barra_escapada_y_en_codigo(self):
        self.assertEqual(V.split_row("| a \\| b | `x|y` | c |"), ["a | b", "`x|y`", "c"])

    def test_no_fila(self):
        self.assertIsNone(V.split_row("texto"))

    def test_hash_ignora_lineas_de_aprobacion_y_crlf(self):
        t = read(APROBADO)
        self.assertEqual(V.content_hash(t), V.content_hash(t.replace("\n", "\r\n")))

    def test_json_y_export_cases(self):
        out = tempfile.mktemp(suffix=".json")
        try:
            r = run_script("validate_manifest_poc.py", BORRADOR, "--json", "--export-cases", out)
            self.assertEqual(r.returncode, 0)
            self.assertTrue(json.loads(r.stdout)["ok"])
            with open(out, encoding="utf-8") as fh:
                cases = json.load(fh)
            self.assertEqual([c["id"] for c in cases], ["CASO-1", "CASO-2", "CASO-3"])
        finally:
            if os.path.exists(out):
                os.unlink(out)


class Correcciones(unittest.TestCase):
    def test_cada_correccion_esta_documentada_en_las_reglas(self):
        reglas = read(os.path.join(ROOT, "references", "reglas-modelado-catalogo-rlm.md"))
        for clave in V.load_bad_api():
            self.assertIn(clave, reglas, f"{clave} falta en la sección 4 de las reglas")


if __name__ == "__main__":
    unittest.main()
