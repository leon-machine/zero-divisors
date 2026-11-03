"""tp lint: the fast rules, on a copy of the fixture store broken one thing at a time."""
import contextlib
import io
import json
import os
import shutil
import subprocess
import tempfile
import unittest

from tests import fixture_store
from tp import lint, validate
from tp.model import load_store, parse_entity_text, dump_entity

CLEAN = None          # built once, copied per test


def setUpModule():
    global CLEAN
    CLEAN = tempfile.mkdtemp(prefix="lint-fixture-")
    fixture_store.build(os.path.join(CLEAN, "store"))


def tearDownModule():
    shutil.rmtree(CLEAN, ignore_errors=True)


DIRS = {"fx.null.square-zero": "claims", "fx.null.no-inverse": "claims",
        "fx.algebra.dimension": "claims", "fx.witt.car": "claims",
        "fx.boost.sigma": "claims", "fx.ascent.minimal-completion": "claims",
        "fx.thermo.two-state": "claims"}


class LintTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="lint-test-")
        self.store = os.path.join(self.tmp, "store")
        shutil.copytree(os.path.join(CLEAN, "store"), self.store)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # helpers -------------------------------------------------------------
    def folder(self, eid):
        return os.path.join(self.store, DIRS.get(eid, "claims"), eid)

    def edit_entity(self, eid, meta_fn=None, levels_fn=None):
        path = os.path.join(self.folder(eid), "entity.md")
        with open(path) as fh:
            meta, levels, _ = parse_entity_text(fh.read())
        if meta_fn:
            meta_fn(meta)
        if levels_fn:
            levels_fn(levels)
        with open(path, "w") as fh:
            fh.write(dump_entity(meta, levels))

    def write_check(self, eid, src):
        with open(os.path.join(self.folder(eid), "check.py"), "w") as fh:
            fh.write(src)

    def lint(self, *args, run=False):
        argv = ["lint", *args, "--store", self.store, "--json"]
        if not run:
            argv.append("--no-run")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = lint.main(argv)
        return code, json.loads(buf.getvalue())

    def codes(self, res, severity=None):
        return [f["code"] for f in res["findings"]
                if severity is None or f["severity"] == severity]

    # the clean store ----------------------------------------------------
    def test_clean_store_static(self):
        code, res = self.lint("--all")
        self.assertEqual(code, 0, res["findings"])
        self.assertEqual(self.codes(res, "error"), [])
        self.assertEqual(res["summary"]["entities"], 7)
        self.assertEqual(res["summary"]["functions"], 7)

    def test_clean_entity_run(self):
        code, res = self.lint("fx.boost.sigma", run=True)
        self.assertEqual(code, 0, res["findings"])
        self.assertIn("I400", self.codes(res))
        self.assertEqual(res["entities"][0]["stats"]["ran"], 1)

    # evidence rules -------------------------------------------------------
    def test_no_assert_is_e408(self):
        self.write_check("fx.null.square-zero", fixture_store.SQUARE_ZERO_CHECK
                         .replace("assert g.is_zero(g.mul(v, v, SQ))", "g.is_zero(g.mul(v, v, SQ))")
                         .replace("assert not g.is_zero(v)", "x = not g.is_zero(v)"))
        code, res = self.lint("fx.null.square-zero")
        self.assertEqual(code, 1)
        self.assertIn("E408", self.codes(res, "error"))

    def test_setdefault_is_l402(self):
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK
                         + "rows = {}\nrows.setdefault(1, []).append(2)\n")
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 0)                       # a warning, not an error
        self.assertIn("L402", self.codes(res, "warning"))
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK)
        code, res = self.lint("fx.algebra.dimension")
        self.assertNotIn("L402", self.codes(res))

    def test_float_math_division_and_ga_import(self):
        cases = {"x = 0.5\n": "E402", "import math\n": "E402", "y = 1 / 2\n": "E402",
                 "z = float(3)\n": "E402"}
        for line, want in cases.items():
            self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK + line)
            code, res = self.lint("fx.algebra.dimension")
            self.assertEqual(code, 1, line)
            self.assertIn(want, self.codes(res, "error"), line)
        self.write_check("fx.algebra.dimension",
                         "def test_dimension():\n    assert 2 ** 2 == 4\n")
        code, res = self.lint("fx.algebra.dimension")
        self.assertIn("E403", self.codes(res, "error"))

    def test_unparsable_check_is_e401(self):
        self.write_check("fx.algebra.dimension", "import GA\ndef test_dimension(:\n")
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 1)
        self.assertIn("E401", self.codes(res, "error"))

    def test_no_integer_literal_is_w408(self):
        code, res = self.lint("fx.algebra.dimension")
        self.assertNotIn("W408", self.codes(res))
        # literals only at module level: nothing inside the function to perturb
        self.write_check("fx.algebra.dimension", "import GA as g\nN = g.all_blades(2)\nM = N\n\n\n"
                         "def test_dimension():\n    assert N == M\n")
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 0)
        self.assertIn("W408", self.codes(res, "warning"))

    def test_entry_without_function_is_e401(self):
        self.edit_entity("fx.algebra.dimension", lambda m: m["checked_by"].append(
            {"kind": "check", "ref": "check.py::test_missing"}))
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 1)
        msgs = [f["message"] for f in res["findings"] if f["code"] == "E401"]
        self.assertTrue(any("test_missing" in m for m in msgs), msgs)

    def test_missing_check_file_is_e401(self):
        os.remove(os.path.join(self.folder("fx.algebra.dimension"), "check.py"))
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 1)
        self.assertIn("E401", self.codes(res, "error"))

    def test_unwired_function_is_l401_but_helpers_are_not(self):
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK + '''

def check_extra():
    assert len(test_helper()) == 4


def test_helper():
    import GA as g
    return g.all_blades(2)
''')
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 0, res["findings"])
        l401 = [f["message"] for f in res["findings"] if f["code"] == "L401"]
        self.assertEqual(len(l401), 1)
        self.assertIn("check_extra", l401[0])
        self.assertNotIn("test_helper", l401[0])

    def test_unwired_function_still_gets_static_rules(self):
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK +
                         "\n\ndef check_extra():\n    x = 3\n")
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 1)
        self.assertIn("E408", self.codes(res, "error"))

    def test_undeclared_premise_static_and_run(self):
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK.replace(
            "def test_dimension():\n",
            "from tp_premise import premise\n\n\ndef test_dimension():\n"
            "    premise(\"fx.witt.car\")\n"))
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 1)
        self.assertIn("E404", self.codes(res, "error"))
        code, res = self.lint("fx.algebra.dimension", run=True)
        self.assertEqual(code, 1)
        msgs = [f["message"] for f in res["findings"] if f["code"] == "E404"]
        self.assertTrue(msgs and "static" not in msgs[0], msgs)

    def test_declared_untouched_is_one_info_line(self):
        self.edit_entity("fx.algebra.dimension", lambda m: m["derivations"][0].update(
            uses=["fx.witt.car@1", "fx.null.square-zero@1"]))
        code, res = self.lint("fx.algebra.dimension", run=True)
        self.assertEqual(code, 0, res["findings"])
        i405 = [f for f in res["findings"] if f["code"] == "I405"]
        self.assertEqual(len(i405), 1)
        self.assertIn("fx.witt.car", i405[0]["message"])
        self.assertIn("fx.null.square-zero", i405[0]["message"])
        self.assertEqual(i405[0]["severity"], "info")

    def test_failing_check_is_e406(self):
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK.replace("== 4", "== 5"))
        code, res = self.lint("fx.algebra.dimension", run=True)
        self.assertEqual(code, 1)
        self.assertIn("E406", self.codes(res, "error"))
        # the static pass does not run it
        code, res = self.lint("fx.algebra.dimension")
        self.assertEqual(code, 0)

    def test_slow_function_is_l409(self):
        old = lint.SLOW_SECONDS
        lint.SLOW_SECONDS = 0.0
        try:
            code, res = self.lint("fx.algebra.dimension", run=True)
        finally:
            lint.SLOW_SECONDS = old
        self.assertEqual(code, 0)
        self.assertIn("L409", self.codes(res, "warning"))

    def test_timeout_is_e409(self):
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK.replace(
            "    assert", "    while True:\n        pass\n    assert"))
        code, res = self.lint("fx.algebra.dimension", "--timeout", "2", run=True)
        self.assertEqual(code, 1)
        self.assertIn("E409", self.codes(res, "error"))

    # layer 1 and house style ----------------------------------------------
    def test_house_style(self):
        cases = [
            (lambda lv: lv.update(lay="A null vector — squares to zero."), "E112"),
            (lambda lv: lv.update(lay="To be honest, it squares to zero."), "E113"),
            (lambda lv: lv.update(lay=r"It squares to zero in $\Foo$."), "E111"),
            (lambda lv: lv.update(lay="This premise is load-bearing."), "L113"),
            (lambda lv: lv.update(lay=r"Unclosed $v^2."), "E110"),
            (lambda lv: lv.pop("lay"), "E114"),
        ]
        for fn, want in cases:
            shutil.rmtree(self.store)
            shutil.copytree(os.path.join(CLEAN, "store"), self.store)
            self.edit_entity("fx.null.square-zero", levels_fn=fn)
            code, res = self.lint("fx.null.square-zero")
            self.assertEqual(code, 1, want)
            self.assertIn(want, self.codes(res, "error"), (want, res["findings"]))

    def test_note_house_style(self):
        def note(text):
            return lambda m: m.setdefault("extraction", {}).update(
                maintainer_pass={"by": "maintainer-2026-10-23", "date": "2026-10-23", "note": text})
        for text, want in [("Fixed — the sign.", "E112"), ("Honestly a typo.", "E113"),
                           ("The premise is load-bearing here.", "L113")]:
            shutil.rmtree(self.store)
            shutil.copytree(os.path.join(CLEAN, "store"), self.store)
            self.edit_entity("fx.null.square-zero", meta_fn=note(text))
            code, res = self.lint("fx.null.square-zero")
            self.assertEqual(code, 1, want)
            self.assertIn(want, self.codes(res, "error"), (want, res["findings"]))
        shutil.rmtree(self.store)
        shutil.copytree(os.path.join(CLEAN, "store"), self.store)
        self.edit_entity("fx.null.square-zero", meta_fn=note("Sign fixed; a plain note."))
        code, res = self.lint("fx.null.square-zero")
        self.assertEqual(code, 0, res["findings"])

    def test_proof_file_house_style(self):
        with open(os.path.join(self.folder("fx.null.square-zero"), "proof-direct.tex"), "w") as fh:
            fh.write("Expand — it vanishes.")
        code, res = self.lint("fx.null.square-zero")
        self.assertIn("E112", self.codes(res, "error"))

    def test_layer1_shape(self):
        self.edit_entity("fx.null.square-zero", lambda m: m.update(status="maybe"))
        code, res = self.lint("fx.null.square-zero")
        self.assertEqual(code, 1)
        self.assertTrue({"E105", "E116"} & set(self.codes(res, "error")), res["findings"])

    def test_broken_yaml_is_e101(self):
        path = os.path.join(self.folder("fx.null.square-zero"), "entity.md")
        with open(path) as fh:
            text = fh.read().replace("title:", "title: [unclosed", 1)
        with open(path, "w") as fh:
            fh.write(text)
        code, res = self.lint("fx.null.square-zero")
        self.assertEqual(code, 1)
        self.assertIn("E101", self.codes(res, "error"))

    # payload ---------------------------------------------------------------
    def test_payload(self):
        self.edit_entity("fx.witt.car", lambda m: m.update(payload=[
            {"kind": "identity", "python": "g.eq(g.add(g.mul(v, w, SQ), g.mul(w, v, SQ)), g.sc(1))",
             "clause": "(1)"},
            {"kind": "value", "python": "len(SQ) == 2"}]))
        code, res = self.lint("fx.witt.car")
        self.assertEqual(code, 0, res["findings"])
        self.edit_entity("fx.witt.car", lambda m: m.update(payload=[
            {"kind": "identity", "python": "g.eq(g.mul(v, w, SQ), g.sc(1))", "clause": "(2)"},
            {"kind": "value", "python": "len(SQ)", "clause": "(3)"},
            {"kind": "value", "python": "undefined_name == 1"}]))
        code, res = self.lint("fx.witt.car")
        self.assertEqual(code, 1)
        msgs = [f["message"] for f in res["findings"] if f["code"] == "L501"]
        self.assertEqual(len(msgs), 3, msgs)
        self.assertIn("clause (2)", msgs[0])
        self.assertIn("not True", msgs[1])          # 2 is truthy but not True
        self.assertIn("NameError", msgs[2])

    def test_payload_without_check(self):
        self.edit_entity("fx.thermo.two-state", lambda m: m.update(payload=[
            {"kind": "value", "python": "True"}]))
        code, res = self.lint("fx.thermo.two-state")
        self.assertEqual(code, 1)
        self.assertIn("L501", self.codes(res, "error"))

    # targets and output ------------------------------------------------------
    def test_targets(self):
        code, res = self.lint("fx.no.such-entity")
        self.assertEqual(code, 1)
        self.assertEqual(self.codes(res), ["L000"])
        code, res = self.lint(os.path.join(self.folder("fx.witt.car"), "check.py"),
                              self.folder("fx.witt.car"), "fx.witt.car")
        self.assertEqual(code, 0)
        self.assertEqual(res["summary"]["entities"], 1)

    def test_check_file_outside_store(self):
        """A copy of an entity folder elsewhere lints against the store's premises."""
        copy = os.path.join(self.tmp, "elsewhere", "fx.boost.sigma")
        shutil.copytree(self.folder("fx.boost.sigma"), copy)
        code, res = self.lint(os.path.join(copy, "check.py"), run=True)
        self.assertEqual(code, 0, res["findings"])

    def test_text_output(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = lint.main(["lint", "fx.algebra.dimension", "fx.witt.car",
                              "--store", self.store, "--no-run"])
        out = buf.getvalue()
        self.assertEqual(code, 0)
        self.assertIn("fx.algebra.dimension", out)
        self.assertIn("tp lint: 2 entities, 2 check functions; 0 error(s)", out)

    def test_changed(self):
        if shutil.which("git") is None:
            self.skipTest("no git")
        g = ["git", "-C", self.tmp, "-c", "user.email=t@t", "-c", "user.name=t"]
        subprocess.run(g + ["init", "-q"], check=True)
        subprocess.run(g + ["add", "-A"], check=True)
        subprocess.run(g + ["commit", "-qm", "fixture"], check=True)
        code, res = self.lint("--changed")
        self.assertEqual(code, 0)
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK + "x = 0.5\n")
        with open(os.path.join(self.folder("fx.witt.car"), "coverage.yaml"), "w") as fh:
            fh.write("functions: {}\n")
        code, res = self.lint("--changed")
        self.assertEqual(code, 1)
        ids = sorted(e["id"] for e in res["entities"])
        self.assertEqual(ids, ["fx.algebra.dimension", "fx.witt.car"])

    # agreement with the full check ---------------------------------------------
    def test_lint_catches_every_static_error_of_layer4(self):
        """Every error the evidence layer reports (without the mutation run) on a
        broken store, lint reports too, with the same code, for the same entity."""
        self.write_check("fx.null.square-zero", fixture_store.SQUARE_ZERO_CHECK
                         .replace("assert ", "_ = "))
        self.write_check("fx.algebra.dimension", fixture_store.DIM_CHECK + "x = 0.5\n")
        self.write_check("fx.boost.sigma", fixture_store.SIGMA_CHECK.replace("import GA as g\n", "import GA as g\nimport math\n"))
        self.write_check("fx.witt.car", fixture_store.CAR_CHECK.replace("import GA as g\n", "from GA import *\nimport GA as g\n").replace("SQ = g.sig(1, 1)", "SQ = g.sig(1, 1)\nZ = 7 / 2"))
        self.edit_entity("fx.null.no-inverse", lambda m: m["checked_by"].append(
            {"kind": "check", "ref": "check.py::test_gone"}))
        self.write_check("fx.ascent.minimal-completion", fixture_store.MINIMAL_CHECK.replace(
            'premise("fx.transport.principle")', 'premise("fx.transport.principle")\n'
            '    premise("fx.witt.car")'))
        os.environ["TP_L4_CACHE"] = os.path.join(self.tmp, "l4.json")
        try:
            store = load_store(self.store)
            rep = validate.Report()
            validate.layer4(store, rep, run_mutants=False, incremental=False)
        finally:
            os.environ.pop("TP_L4_CACHE", None)
        full = {(f.entity, f.code) for f in rep.errors()}
        self.assertTrue(full)
        for run in (False, True):
            _, res = self.lint("--all", run=run)
            mine = {(f["entity"], f["code"]) for f in res["findings"]
                    if f["severity"] == "error"}
            self.assertLessEqual(full - {(e, c) for e, c in full if c in ("E406", "E407")
                                         and not run}, mine, (run, full, mine))


if __name__ == "__main__":
    unittest.main()
