import json
import os
import re
import tempfile
import unittest

from tests.helpers import REPO, ROOT, load, read, run_script

SCAN = os.path.join(REPO, "sample-scan.json")
S2P = load("scan_to_poc")
CMP = load("compare_results")


class Scan(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.intake = os.path.join(self.d, "n.md")
        self.poc = os.path.join(self.d, "p.md")
        self.assertEqual(run_script("scan_to_poc.py", SCAN, "--cliente", "X", "--out", self.intake).returncode, 0)
        self.assertEqual(run_script("scan_to_poc.py", SCAN, "--cliente", "X", "--modalidad", "poc",
                                    "--out", self.poc).returncode, 0)

    def test_misma_numeracion_nec_en_ambos_modos(self):
        a = re.findall(r"\| (NEC-\d+) \| `?(SBQQ__\w+)", read(self.intake))
        b = re.findall(r"\| (NEC-\d+) \| (SBQQ__\w+)", read(self.poc))
        self.assertEqual(sorted(a), sorted(b))

    def test_cada_hip_cita_nec_existente(self):
        t = read(self.poc)
        necs = set(re.findall(r"^\| (NEC-\d+) \|", t, re.M))
        for line in t.splitlines():
            if line.startswith("| HIP-"):
                refs = set(re.findall(r"NEC-\d+", line.split("|")[3]))
                self.assertTrue(refs and refs <= necs, line[:80])

    def test_no_sobrescribe_sin_force(self):
        self.assertEqual(run_script("scan_to_poc.py", SCAN, "--cliente", "X", "--out", self.intake).returncode, 1)
        self.assertEqual(run_script("scan_to_poc.py", SCAN, "--cliente", "X", "--force", "--out", self.intake).returncode, 0)

    def test_pre_borrador_no_pasa_el_validador(self):
        self.assertEqual(run_script("validate_manifest_poc.py", self.poc).returncode, 1)

    def test_celdas_escapan_barras(self):
        row = {"sbqq_object": "A|B", "notes": "x | y\nz", "rca_equivalent": "Q", "migration_type": "Directa"}
        self.assertNotIn("|", S2P.esc(row["notes"]).replace("\\|", ""))

    def test_filas_de_riesgo_siempre_incluidas(self):
        inv = [{"sbqq_object": f"G{i}", "risk": "low", "migration_type": "Directa"} for i in range(30)]
        inv.append({"sbqq_object": "R", "risk": "high", "migration_type": "Reescritura"})
        nums, omitidas = S2P.numbered_rows(inv)
        self.assertEqual(nums[0][1]["sbqq_object"], "R")
        self.assertEqual(len(nums), S2P.MAX_NEC)
        self.assertEqual(omitidas, 31 - S2P.MAX_NEC)


class Comparar(unittest.TestCase):
    CASOS = [{"id": "CASO-1", "esperado": "80 €"}, {"id": "CASO-2", "esperado": "Rechazado"}]

    def test_veredictos(self):
        v = lambda obs: CMP.veredicto(CMP.compare(self.CASOS, obs))
        self.assertEqual(v({"CASO-1": "80,00", "CASO-2": "rechazado"}), "VALIDADA")
        self.assertEqual(v({"CASO-1": "81", "CASO-2": "Rechazado"}), "PARCIALMENTE VALIDADA")
        self.assertEqual(v({"CASO-1": "1", "CASO-2": "otro"}), "NO VALIDADA")
        self.assertEqual(v({}), "NO EJECUTADA")

    def test_caso_sin_ejecutar_no_da_validada(self):
        self.assertNotEqual(CMP.veredicto(CMP.compare(self.CASOS, {"CASO-1": "80"})), "VALIDADA")

    def test_cli(self):
        d = tempfile.mkdtemp()
        c, r = os.path.join(d, "c.json"), os.path.join(d, "r.json")
        with open(c, "w", encoding="utf-8") as fh:
            json.dump(self.CASOS, fh)
        with open(r, "w", encoding="utf-8") as fh:
            json.dump({"CASO-1": "99", "CASO-2": "Rechazado"}, fh)
        self.assertEqual(run_script("compare_results.py", c, r).returncode, 1)


class Deps(unittest.TestCase):
    def test_python_ok(self):
        res = load("check_deps").check()
        self.assertTrue(next(x for x in res if x["nombre"] == "python")["ok"])

    def test_cli_sale_0_sin_exigir_sf(self):
        self.assertEqual(run_script("check_deps.py").returncode, 0)


if __name__ == "__main__":
    unittest.main()
