"""Integridad del repo: enlaces de .claude, skills precargadas, reglas obligatorias presentes y
referencias de rutas que existen. Evita que un renombrado deje el flujo roto sin que nadie lo vea."""
import os
import re
import tempfile
import unittest

from tests.helpers import REPO, load, read



def _load_check():
    import importlib.util
    spec = importlib.util.spec_from_file_location("check_verificacion", os.path.join(REPO, "flujo-revenue", "scripts", "check_verificacion.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


CHECK = _load_check()
AGENTES = {
    "demo-brief-architect": os.path.join(REPO, "nespon-brief-agent", "claude-code", "agents", "demo-brief-architect.md"),
    "poc-architect": os.path.join(REPO, "flujo-revenue", "agents", "poc-architect.md"),
    "rlm-verifier": os.path.join(REPO, "flujo-revenue", "agents", "rlm-verifier.md"),
}


def frontmatter_skills(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    assert m, "sin frontmatter"
    bloque = re.search(r"^skills:\n((?:  - .+\n?)+)", m.group(1) + "\n", re.M)
    return [x.strip()[2:].strip() for x in bloque.group(1).splitlines()] if bloque else []


class Enlaces(unittest.TestCase):
    def test_enlaces_de_claude_resuelven(self):
        base = os.path.join(REPO, ".claude")
        for sub in ("agents", "skills"):
            for nombre in os.listdir(os.path.join(base, sub)):
                self.assertTrue(os.path.exists(os.path.join(base, sub, nombre)), f".claude/{sub}/{nombre} roto")

    def test_cada_agente_esta_enlazado(self):
        for nombre in AGENTES:
            self.assertTrue(os.path.exists(os.path.join(REPO, ".claude", "agents", nombre + ".md")), nombre)

    def test_skills_precargadas_existen(self):
        for nombre, ruta in AGENTES.items():
            for sk in frontmatter_skills(read(ruta)):
                self.assertTrue(os.path.isfile(os.path.join(REPO, ".claude", "skills", sk, "SKILL.md")),
                                f"{nombre} precarga '{sk}' que no está en .claude/skills")

    def test_skill_de_entrada_y_poc_existen(self):
        for sk in ("revenue-intake", "revenue-cloud-poc", "rlm-skill", "nespon-brief-to-demo", "nespon-demo-builder"):
            self.assertTrue(os.path.isfile(os.path.join(REPO, ".claude", "skills", sk, "SKILL.md")), sk)


class ReglasObligatorias(unittest.TestCase):
    def test_agentes_de_diseno_precargan_rlm_skill(self):
        for nombre in ("demo-brief-architect", "poc-architect", "rlm-verifier"):
            self.assertIn("rlm-skill", frontmatter_skills(read(AGENTES[nombre])), nombre)

    def test_agentes_de_diseno_exigen_verificacion_independiente(self):
        for nombre in ("demo-brief-architect", "poc-architect"):
            self.assertIn("rlm-verifier", read(AGENTES[nombre]), nombre)
        vibes = read(os.path.join(REPO, "nespon-brief-agent", "vibes", "rules", "demo-brief-architect.md"))
        self.assertIn("rlm-verifier", vibes)
        self.assertIn("rlm-skill", vibes)

    def test_entrada_enruta_a_los_dos_agentes_y_verifica(self):
        t = read(os.path.join(REPO, "flujo-revenue", "skills", "revenue-intake", "SKILL.md"))
        for clave in ("demo-brief-architect", "poc-architect", "rlm-verifier", "rlm-skill", "Decide el SE"):
            self.assertIn(clave, t)

    def test_verificador_no_puede_editar(self):
        m = re.search(r"^tools:\s*(.+)$", read(AGENTES["rlm-verifier"]), re.M)
        herramientas = {x.strip() for x in m.group(1).split(",")}
        self.assertFalse(herramientas & {"Write", "Edit", "NotebookEdit"})


class Referencias(unittest.TestCase):
    RAIZ = ("revenue-cloud-poc/", "flujo-revenue/", "nespon-brief-agent/")

    def test_rutas_citadas_existen(self):
        ficheros = [
            os.path.join(REPO, "revenue-cloud-poc", "SKILL.md"),
            os.path.join(REPO, "flujo-revenue", "skills", "revenue-intake", "SKILL.md"),
            AGENTES["poc-architect"], AGENTES["demo-brief-architect"], AGENTES["rlm-verifier"],
        ]
        for f in ficheros:
            for ruta in re.findall(r"`((?:revenue-cloud-poc|flujo-revenue|nespon-brief-agent)/[\w./-]+)`", read(f)):
                if "<" in ruta or ruta.endswith("/"):
                    continue
                self.assertTrue(os.path.exists(os.path.join(REPO, ruta)), f"{os.path.relpath(f, REPO)} cita {ruta}")

    def test_rlm_skill_tiene_su_skill_md(self):
        self.assertTrue(os.path.isfile(os.path.join(REPO, "rlm-skill", "SKILL.md")))


class CheckVerificacion(unittest.TestCase):
    def _manifiesto(self, linea, informe=None):
        d = tempfile.mkdtemp()
        m = os.path.join(d, "M.md")
        with open(m, "w", encoding="utf-8") as f:
            f.write("# M\n\n**Estado de revisión:** BORRADOR\n" + (linea + "\n" if linea else ""))
        if informe is not None:
            with open(os.path.join(d, "VERIFICACION-RLM.md"), "w", encoding="utf-8") as f:
                f.write(informe)
        return m

    def test_ok(self):
        m = self._manifiesto("**Verificación de coherencia (rlm-verifier):** APROBADO · 2026-11-05 · VERIFICACION-RLM.md",
                             "DICTAMEN: APROBADO\nResumen: ok\n")
        self.assertEqual(CHECK.check(m)[0], [])

    def test_falta_linea(self):
        self.assertTrue(CHECK.check(self._manifiesto(""))[0])

    def test_rechazado_bloquea(self):
        m = self._manifiesto("**Verificación de coherencia (rlm-verifier):** RECHAZADO · 2026-11-05 · VERIFICACION-RLM.md",
                             "DICTAMEN: RECHAZADO\n")
        self.assertTrue(CHECK.check(m)[0])

    def test_informe_inexistente_o_discrepante(self):
        linea = "**Verificación de coherencia (rlm-verifier):** APROBADO · 2026-11-05 · VERIFICACION-RLM.md"
        self.assertTrue(CHECK.check(self._manifiesto(linea))[0])
        self.assertTrue(CHECK.check(self._manifiesto(linea, "DICTAMEN: CON RESERVAS\n"))[0])


if __name__ == "__main__":
    unittest.main()
