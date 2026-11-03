"""`tp context` builds one compact bundle per entity from the fixture store."""
import io
import json
import os
import shutil
import tempfile
import time
import unittest
from contextlib import redirect_stderr, redirect_stdout

import yaml

from tests.fixture_store import build
from tp import context as C
from tp.model import dump_entity, parse_entity_text

LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GTG_ENTITY = {"id": "fx.grav.pg-field", "kind": "claim", "version": 1,
              "title": "The PG field", "status": "conjectured",
              "proposed_by": {"kind": "human"}, "ai_involved": "no", "subject": "algebra"}
GTG_LEVELS = {"formal": r"The gauge field $\hb = 1 - \beta P$ has a horizon at $\beta = 1$.",
              "technical": "pending", "lay": "pending", "one-liner": "PG field"}


class ContextBundle(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(os.path.join(self.tmp, "store"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # ---- helpers -----------------------------------------------------------------
    def edit(self, sub, eid, **meta):
        p = os.path.join(self.root, sub, eid, "entity.md")
        with open(p) as fh:
            m, lv, _ = parse_entity_text(fh.read())
        m.update(meta)
        with open(p, "w") as fh:
            fh.write(dump_entity(m, lv))

    def add(self, sub, meta, levels):
        d = os.path.join(self.root, sub, meta["id"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "entity.md"), "w") as fh:
            fh.write(dump_entity(meta, levels))
        return d

    def runs(self, runs):
        os.makedirs(os.path.join(self.tmp, "site"), exist_ok=True)
        with open(os.path.join(self.tmp, "site", "check_runs.json"), "w") as fh:
            json.dump({"python": "3", "runs": runs}, fh)

    @staticmethod
    def run_rec(*fns, ok=True):
        return {"functions": [{"name": f, "ok": ok, "ms": 3, "touched": [], "error":
                               None if ok else "AssertionError", "stdout": ""} for f in fns],
                "load_error": None, "ran_at": "2026-10-23 12:00 UTC"}

    def ctx(self):
        return C.Context(self.root)

    # ---- tests -------------------------------------------------------------------
    def test_sections_in_order_for_check(self):
        text, info = self.ctx().bundle("fx.thermo.temperature", "check")
        heads = [l for l in text.splitlines() if l.startswith("## ")]
        self.assertEqual(heads, ["## Statement", "## Derivation", "## Conventions",
                                 "## Shared library (lib/, on the path for checks)",
                                 "## Existing evidence", "## Example check (house conventions)",
                                 "## Rules a check must satisfy"])
        self.assertTrue(text.startswith("# Context: `fx.thermo.temperature`"))
        self.assertIn("kind: claim; status: proved", text)
        self.assertIn("subject: thermal (Thermality)", text)
        # premise lines carry status, version and one-liner, and (check) the full formal
        self.assertIn("`fx.thermo.two-state@1` [claim, proved, v1]: "
                      "The thermometer is a two-state system", text)
        self.assertIn("`fx.thermo.period-premise@1` [claim, postulate, v1]", text)
        self.assertIn("formal: One modular period equals one rapidity period", text)
        self.assertIn("assumes:", text)
        self.assertIn("Match one modular period to one rapidity period.", text)   # the proof
        self.assertIn("- proof: derivation `from-period` (not machine-checked)", text)
        self.assertEqual(info["cuts"], [])
        self.assertNotIn("\u2014", text)                                     # no em dashes

    def test_read_mode_gives_one_liners_and_no_example(self):
        text, _ = self.ctx().bundle("fx.thermo.temperature", "read")
        self.assertIn("`fx.thermo.two-state@1` [claim, proved, v1]", text)
        self.assertNotIn("formal: One modular period", text)
        self.assertNotIn("## Example check", text)
        self.assertNotIn("## Rules a check must satisfy", text)
        restate, _ = self.ctx().bundle("fx.thermo.temperature", "restate")
        self.assertIn("formal: One modular period", restate)
        self.assertNotIn("## Example check", restate)

    def test_stale_pin_is_reported(self):
        self.edit("claims", "fx.boost.sigma", version=2)
        text, _ = self.ctx().bundle("fx.boost.sigma-square", "check")
        self.assertIn("STALE PIN: pinned v1, current v2", text)
        text, _ = self.ctx().bundle("fx.boost.sigma", "check")
        self.assertNotIn("STALE", text)

    def test_macros_and_gravity_digest(self):
        text, info = self.ctx().bundle("fx.thermo.temperature", "check")
        self.assertIn("- `\\TH` = `T_{\\mathrm{H}}`", text)
        self.assertFalse(info["gravity"])
        self.assertNotIn("GTG conventions", text)
        with open(os.path.join(self.root, "notation.yaml"), "a") as fh:
            fh.write("hb: \\bar{h}\n")
        self.add("claims", GTG_ENTITY, GTG_LEVELS)
        text, info = self.ctx().bundle("fx.grav.pg-field", "check")
        self.assertTrue(info["gravity"])
        self.assertIn("- `\\hb` = `\\bar{h}`", text)
        self.assertIn("GTG conventions", text)
        self.assertIn("beta = -rH", text)
        self.assertIn("calR(B) := -R(\\hb(B))", text)
        self.assertIn("gtg-dictionary.md", text)
        self.assertLess(len(C.GTG_DIGEST.encode()), 1536)

    def test_library_read_with_ast_and_absent_modules_skipped(self):
        lib = os.path.join(self.tmp, "lib")
        os.makedirs(lib)
        shutil.copy(os.path.join(LAB, "lib", "GA.py"), lib)
        with open(os.path.join(lib, "gtg.py"), "w") as fh:
            fh.write('import does_not_exist\n\n\ndef curvature(omega, hb, x=0):\n'
                     '    """Store-sign curvature calR of a GTG field.\n\n    More."""\n\n\n'
                     'def _private():\n    pass\n\n\nclass Field:\n'
                     '    """A pair (hb, Omega)."""\n    def __init__(self, hb, omega):\n'
                     '        pass\n')
        with open(os.path.join(lib, "fock.py"), "w") as fh:
            fh.write("def broken(:\n")
        self.add("claims", GTG_ENTITY, GTG_LEVELS)
        text, _ = self.ctx().bundle("fx.grav.pg-field", "check")      # gravity-facing: gtg
        self.assertIn("### lib/GA.py (`import GA`)", text)
        self.assertIn("- `sig(p, q, r=0)`: Signature tuple", text)
        self.assertIn("### lib/gtg.py (`import gtg`)", text)
        self.assertIn("- `curvature(omega, hb, x=0)`: Store-sign curvature calR of a GTG field.",
                      text)
        self.assertIn("- `class Field(hb, omega)`: A pair (hb, Omega).", text)
        self.assertNotIn("_private", text)
        self.assertIn("- lib/fock.py: (could not read", text)  # not relevant, and does not parse
        self.assertNotIn("lib/series.py", text)               # absent: skipped quietly
        text, _ = self.ctx().bundle("fx.witt.car", "check")   # a CAR result: fock, not gtg
        self.assertIn("### lib/fock.py (`import fock`)", text)
        self.assertIn("- lib/gtg.py: curvature, Field", text)
        restate, _ = self.ctx().bundle("fx.witt.car", "restate")
        self.assertIn("- lib/gtg.py: curvature, Field", restate)
        self.assertNotIn("### lib/GA.py", restate)

    def test_evidence_coverage_and_last_run(self):
        d = os.path.join(self.root, "claims", "fx.null.no-inverse")
        with open(os.path.join(d, "coverage.yaml"), "w") as fh:
            yaml.safe_dump({"functions": {"test_no_inverse": {"kind": "exact",
                                                              "clauses": ["whole"]}}}, fh)
        self.runs({"fx.null.no-inverse": self.run_rec("test_no_inverse")})
        text, _ = self.ctx().bundle("fx.null.no-inverse", "check")
        self.assertIn("Own check: store/claims/fx.null.no-inverse/check.py", text)
        self.assertIn("- `test_no_inverse`", text)
        self.assertIn("Coverage (store/claims/fx.null.no-inverse/coverage.yaml)", text)
        self.assertIn("kind: exact", text)
        self.assertIn("Last recorded run (site/check_runs.json, 2026-10-23 12:00 UTC)", text)
        self.assertIn("- `test_no_inverse`: pass, 3 ms", text)
        self.edit("claims", "fx.null.no-inverse",
                  checked_by=[{"kind": "legacy", "script": "verify_T01.py", "tags": ["num:2.1"]}])
        text, _ = self.ctx().bundle("fx.null.no-inverse", "check")
        self.assertIn("- legacy: verify_T01.py tags num:2.1", text)

    def test_example_is_shortest_passing_check_of_same_subject(self):
        ctx = self.ctx()                      # no recorded runs: any qualifying check
        text, _ = ctx.bundle("fx.witt.car", "check")
        # algebra subject; checks with premise() and asserts: no-inverse, sigma, sigma-square,
        # minimal-completion; the shortest of them is the model
        sizes = {eid: os.path.getsize(os.path.join(self.root, "claims", eid, "check.py"))
                 for eid in ("fx.null.no-inverse", "fx.boost.sigma", "fx.boost.sigma-square",
                             "fx.ascent.minimal-completion")}
        best = min(sizes, key=lambda k: (sizes[k], k))
        self.assertIn(f"`store/claims/{best}/check.py` (for `{best}`; same subject", text)
        self.assertIn("```python\nimport GA as g", text)
        # a failing recorded run disqualifies it; the entity itself is never its own example
        self.runs({best: self.run_rec("test_x", ok=False),
                   **{k: self.run_rec("test_x") for k in sizes if k != best}})
        text, _ = self.ctx().bundle("fx.witt.car", "check")
        self.assertNotIn(f"(for `{best}`", text)
        text, _ = self.ctx().bundle(sorted(set(sizes) - {best})[0], "check")
        self.assertNotIn(f"(for `{sorted(set(sizes) - {best})[0]}`", text)

    def test_open_problems_notes_and_quantities(self):
        with open(os.path.join(self.root, "open_problems.yaml"), "w") as fh:
            yaml.safe_dump([{"id": "op.angle", "title": "Derive the angle", "status": "open",
                             "difficulty": "frontier", "entities": ["fx.boost.sigma"]}], fh)
        self.add("notes", {"id": "note.fx.sigma-remark", "kind": "note", "version": 1,
                           "title": "A remark on sigma", "status": "remark",
                           "proposed_by": {"kind": "human"}, "ai_involved": "no",
                           "comments_on": ["fx.boost.sigma"]},
                 {"formal": r"The boost $\sigma$ is the commutator of the pair.",
                  "one-liner": "pending"})
        self.add("quantities", {"id": "q.fx.kappa", "kind": "quantity", "version": 1,
                                "title": "Surface gravity", "status": "measured",
                                "proposed_by": {"kind": "human"}, "ai_involved": "no",
                                "quantity": {"symbol": "\\kappa", "value": "0.25",
                                             "uncertainty": "0.01", "units": "1/M",
                                             "source": {"citation": "Fixture data"}}},
                 {"formal": "The surface gravity.", "one-liner": "kappa"})
        self.edit("claims", "fx.boost.sigma", quantities=["q.fx.kappa@1"])
        text, _ = self.ctx().bundle("fx.boost.sigma", "check")
        self.assertIn("## Quantities", text)
        self.assertIn("| `q.fx.kappa@1` | \\kappa | 0.25 | 0.01 | 1/M | Fixture data |", text)
        self.assertIn("- open problem `op.angle` [open, frontier]: Derive the angle", text)
        self.assertIn("- note `note.fx.sigma-remark` (remark): A remark on sigma", text)
        self.assertLess(text.index("## Quantities"), text.index("## Conventions"))
        note, _ = self.ctx().bundle("note.fx.sigma-remark", "check")
        self.assertIn("Comments on:", note)
        self.assertNotIn("## Example check", note)           # nothing to check in a note
        q, _ = self.ctx().bundle("q.fx.kappa", "read")
        self.assertIn("| `q.fx.kappa` | \\kappa | 0.25", q)

    def test_imported_and_prediction(self):
        text, _ = self.ctx().bundle("fx.qi.kms", "restate")
        self.assertIn("Imported from:", text)
        self.assertIn("citation: Bratteli and Robinson, Operator Algebras II; locator: Thm 5.3.30",
                      text)
        self.assertIn("No derivation: the result is imported.", text)
        text, _ = self.ctx().bundle("fx.pred.single-temperature", "read")
        self.assertIn("Kill condition: threshold: two modes at different temperatures", text)
        self.assertIn("tests: `fx.thermo.two-state@1`", text)

    def test_trimmed_to_budget_least_important_first(self):
        os.makedirs(os.path.join(self.tmp, "lib"))
        shutil.copy(os.path.join(LAB, "lib", "GA.py"), os.path.join(self.tmp, "lib"))
        ctx = self.ctx()
        full, info = ctx.bundle("fx.thermo.temperature", "check", max_kb=100)
        self.assertEqual(info["cuts"], [])
        self.assertGreater(info["bytes"], 5 * 1024)
        text, info = ctx.bundle("fx.thermo.temperature", "check", max_kb=4)
        self.assertLessEqual(info["bytes"], 4 * 1024)
        self.assertLess(info["bytes"], len(full.encode()))
        self.assertTrue(info["cuts"])
        self.assertIn("> Trimmed to fit 4 KB; cut, least important first: ", text)
        order = [w for s in C.Context.CUTS["check"] for w in [C.Context.WHAT[s]]]
        self.assertEqual(info["cuts"], [w for w in order if w in info["cuts"]])
        # the formal statement is never cut
        self.assertIn("Under the period premise", text)
        # an impossible budget still returns the statement and says so
        text, info = ctx.bundle("fx.thermo.temperature", "check", max_kb=0.5)
        self.assertIn("Still", text)
        self.assertIn("Under the period premise", text)

    def test_cli_stdout_file_dir_and_unknown_id(self):
        out = io.StringIO()
        with redirect_stdout(out):
            rc = C.main(["context", "fx.witt.car", "--store", self.root, "--for", "read"])
        self.assertEqual(rc, 0)
        self.assertIn("# Context: `fx.witt.car`", out.getvalue())
        f = os.path.join(self.tmp, "b.md")
        err = io.StringIO()
        with redirect_stderr(err):
            rc = C.main(["context", "fx.witt.car", "--store", self.root, "--out", f])
        self.assertEqual(rc, 0)
        with open(f) as fh:
            self.assertTrue(fh.read().startswith("# Context: `fx.witt.car`"))
        d = os.path.join(self.tmp, "many")
        with redirect_stderr(io.StringIO()):
            rc = C.main(["context", "fx.witt.car", "fx.boost.sigma", "--store", self.root,
                         "--out", d])
        self.assertEqual(sorted(os.listdir(d)), ["fx.boost.sigma.md", "fx.witt.car.md"])
        err = io.StringIO()
        with redirect_stderr(err):
            rc = C.main(["context", "fx.retired.old-claim", "--store", self.root])
        self.assertEqual(rc, 2)
        self.assertIn("no entity", err.getvalue())

    def test_fast_and_baseline(self):
        ctx = self.ctx()
        t0 = time.perf_counter()
        for eid in ctx.store.entities:
            ctx.bundle(eid, "check")
        self.assertLess((time.perf_counter() - t0) / len(ctx.store.entities), 0.5)
        files, total = ctx.baseline_files("fx.thermo.temperature")
        self.assertIn(os.path.join(self.root, "claims", "fx.thermo.two-state", "entity.md"), files)
        self.assertIn(os.path.join(self.root, "notation.yaml"), files)
        self.assertGreater(total, 0)

    def test_fast_loader_matches_model_loader(self):
        from tp.model import load_store
        a, b = load_store(self.root), C.load_store_fast(self.root)
        self.assertEqual(sorted(a.entities), sorted(b.entities))
        for k in a.entities:
            self.assertEqual(a.entities[k].meta, b.entities[k].meta)
            self.assertEqual(a.entities[k].levels, b.entities[k].levels)
        import yaml as y
        from tp import model
        self.assertIs(model.yaml, y)                         # the patch is undone


if __name__ == "__main__":
    unittest.main()
