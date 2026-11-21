"""Every validator rule has a test that makes it fire.

Each test builds the 21-entity fixture store, breaks one thing, and asserts
the expected code.  Run:  python -m unittest discover -s tests -t .
"""
import os
import re
import shutil
import tempfile
import unittest

import yaml

from tests.fixture_store import build
from tp import evidence, validate as V
from tp.model import load_store, write_lock

E = os.path.join


class StoreCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(E(self.tmp, "store"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # helpers -------------------------------------------------------------
    def folder(self, eid):
        for sub in ("claims", "objects", "predictions", "questions", "notes"):
            p = E(self.root, sub, eid)
            if os.path.isdir(p):
                return p
        raise KeyError(eid)

    def edit(self, eid, old, new, fname="entity.md"):
        p = E(self.folder(eid), fname)
        s = open(p).read()
        self.assertIn(old, s, f"fixture text not found in {eid}/{fname}")
        open(p, "w").write(s.replace(old, new, 1))

    def set_formal(self, eid, text):
        p = E(self.folder(eid), "entity.md")
        s = open(p).read()
        s = re.sub(r"## formal\n.*?\n\n## technical", "## formal\n" + text.replace("\\", "\\\\")
                   + "\n\n## technical", s, flags=re.S)
        open(p, "w").write(s)

    def write(self, eid, fname, text):
        open(E(self.folder(eid), fname), "w").write(text)

    def run_layers(self, layers=(1, 2, 3), **kw):
        return V.validate(load_store(self.root), layers=layers, keep_going=True, **kw)

    def codes(self, rep):
        return {f.code for f in rep.findings}

    def assertFires(self, code, layers=(1, 2, 3), **kw):
        rep = self.run_layers(layers, **kw)
        self.assertIn(code, self.codes(rep),
                      "\n".join(f.render() for f in rep.findings))
        return rep


class Baseline(StoreCase):
    def test_fixture_is_clean(self):
        rep = self.run_layers((1, 2, 3, 4, 5, 6), author="leon")
        self.assertEqual(rep.errors(), [], "\n".join(f.render() for f in rep.errors()))
        self.assertEqual(len(load_store(self.root).entities), 21)

    def test_derived_state(self):
        rep = self.run_layers((1, 2, 3))
        self.assertEqual(rep.ledger["fx.thermo.two-state"], "essential")
        self.assertEqual(rep.ledger["fx.boost.sigma"], "absent")
        self.assertEqual(rep.eff["fx.thermo.entropy-tick"], "conjectured")
        self.assertIn("fx.null.square-zero", rep.past["fx.thermo.two-state"])


class Layer1Shape(StoreCase):
    def test_E101_bad_yaml(self):
        self.edit("fx.witt.car", "version: 1", "version: [1")
        self.assertFires("E101")

    def test_E102_missing_required(self):
        self.edit("fx.witt.car", "ai_involved: 'no'\n", "")
        self.assertFires("E102")

    def test_E103_bad_id(self):
        self.edit("fx.witt.car", "id: fx.witt.car", "id: FX_witt")
        self.assertFires("E103")

    def test_E124_title_states_the_result(self):
        self.edit("fx.witt.car", "title: ", "title: " + "a title that runs on and on " * 4)
        self.assertFires("E124", (1,))

    def test_E125_orcid_check_digit(self):
        self.edit("fx.witt.car", "ai_involved: 'no'\n",
                  "ai_involved: 'no'\ncredit:\n- name: Ada Lovelace\n  role: idea\n  orcid: 0000-0002-1825-0098\n")
        self.assertFires("E125", (1,))

    def test_orcid_well_formed(self):
        self.edit("fx.witt.car", "ai_involved: 'no'\n",
                  "ai_involved: 'no'\ncredit:\n- name: Ada Lovelace\n  role: idea\n  orcid: https://orcid.org/0000-0002-1825-0097\n")
        self.assertFires("E116", (1,))

    def test_E104_bad_kind(self):
        self.edit("fx.witt.car", "kind: claim", "kind: lemma")
        self.assertFires("E104")

    def test_E105_bad_status(self):
        self.edit("fx.witt.car", "status: proved", "status: probably")
        self.assertFires("E105")

    def test_E106_derived_field(self):
        self.edit("fx.witt.car", "version: 1", "version: 1\neffective_status: proved")
        self.assertFires("E106")

    def test_E107_proved_without_evidence(self):
        self.edit("fx.algebra.dimension", "checked_by:", "unused_checked_by:")
        rep = self.run_layers()
        self.assertIn("E107", self.codes(rep))

    def test_E107_imported_without_source(self):
        self.edit("fx.qi.kms", "imported_from:", "x_imported_from:")
        self.assertFires("E107")

    def test_E108_imported_with_derivation(self):
        self.edit("fx.qi.kms", "imported_from:",
                  "derivations:\n- name: mine\nimported_from:")
        self.assertFires("E108")

    def test_E109_prediction_without_registration(self):
        self.edit("fx.pred.single-temperature", "registered: '2026-10-20'", "")
        self.assertFires("E109")

    def test_E110_unbalanced_maths(self):
        self.edit("fx.witt.car", "## formal\n", "## formal\n$\\frac{1}{2 ")
        self.assertFires("E110")

    def test_E111_undeclared_macro(self):
        self.edit("fx.witt.car", "## formal\n", "## formal\n$\\Witt(v)$ ")
        self.assertFires("E111")

    def test_E112_em_dash(self):
        self.edit("fx.witt.car", "## formal\n", "## formal\nNote — ")
        self.assertFires("E112")

    def test_E113_banned_word(self):
        self.edit("fx.witt.car", "## formal\n", "## formal\nTo be honest, ")
        self.assertFires("E113")

    def test_E114_missing_level(self):
        self.edit("fx.witt.car", "## lay\npending\n", "")
        self.assertFires("E114")

    def test_E115_malformed_pin(self):
        self.edit("fx.boost.sigma", "fx.witt.car@1", "fx.witt.car@latest")
        self.assertFires("E115")

    def test_E116_unknown_field(self):
        self.edit("fx.witt.car", "version: 1", "version: 1\nconfidence: high")
        self.assertFires("E116")


class Layer2References(StoreCase):
    def test_E201_unknown_target(self):
        self.edit("fx.boost.sigma", "fx.witt.car@1", "fx.witt.cars@1")
        self.assertFires("E201")

    def test_E202_pin_ahead(self):
        self.edit("fx.boost.sigma", "fx.witt.car@1", "fx.witt.car@4")
        self.assertFires("E202")

    def test_E203_assumes_non_postulate(self):
        self.edit("fx.ascent.minimal-completion", "fx.transport.principle@1",
                  "fx.witt.car@1")
        self.assertFires("E203")

    def test_E203_uses_postulate(self):
        self.edit("fx.boost.sigma", "fx.witt.car@1", "fx.transport.principle@1")
        self.assertFires("E203")

    def test_E204_promoted_by_citing_a_conjecture(self):
        self.edit("fx.parity.even", "fx.witt.car@1", "fx.thermo.entropy-tick@1")
        rep = self.assertFires("E204")
        msg = [f for f in rep.findings if f.code == "E204"][0].message
        self.assertIn("fx.thermo.entropy-tick@1 (conjectured)", msg)

    def test_E204_conditional_derivation(self):
        self.edit("fx.parity.even", "- name: direct", "- name: direct\n  conditional: true")
        self.assertFires("E204")

    def test_E204_propagates_down_a_chain(self):
        # weaken a premise two steps up: sigma-square must also fall
        self.edit("fx.witt.car", "status: proved", "status: conjectured")
        self.edit("fx.witt.car", "version: 1", "version: 1\nlineage:\n  motivated_by:\n  - fx.q.angle")
        self.edit("fx.witt.car", "  proof: proof-direct.tex\n", "")
        rep = self.run_layers()
        hit = {f.entity.split("@")[0] for f in rep.findings if f.code == "E204"}
        self.assertTrue({"fx.boost.sigma", "fx.boost.sigma-square"} <= hit, hit)

    def test_E205_retired_id(self):
        self.edit("fx.boost.sigma", "fx.witt.car@1", "fx.retired.old-claim@1")
        self.assertFires("E205")

    def test_E206_substantive_change_without_bump(self):
        write_lock(load_store(self.root))
        self.edit("fx.witt.car", "## formal\n", "## formal\nRestated: ")
        self.assertFires("E206")

    def test_E206_cosmetic_change_is_free(self):
        write_lock(load_store(self.root))
        self.edit("fx.witt.car", "## lay\npending", "## lay\nTwo null directions pair up.")
        rep = self.run_layers()
        self.assertNotIn("E206", self.codes(rep))

    def test_E207_duplicate_id(self):
        src = self.folder("fx.witt.car")
        shutil.copytree(src, src + "-copy")
        self.assertFires("E207")

    def test_E208_unknown_subject(self):
        self.edit("fx.witt.car", "subject: algebra", "subject: geometry")
        self.assertFires("E208")

    def test_W210_missing_subject(self):
        self.edit("fx.witt.car", "subject: algebra\n", "")
        self.assertFires("W210")

    def test_subject_change_needs_no_version_bump(self):
        write_lock(load_store(self.root))
        self.edit("fx.witt.car", "subject: algebra", "subject: thermal")
        self.assertNotIn("E206", self.codes(self.run_layers()))

    def test_W209_uses_an_object(self):
        self.edit("fx.boost.sigma", "  - fx.witt.car@1", "  - fx.witt.car@1\n  - obj.cl11@1")
        self.assertFires("W209")


class Layer3WholeStore(StoreCase):
    def test_E301_cycle(self):
        self.edit("fx.null.square-zero", "- name: direct",
                  "- name: direct\n  uses:\n  - fx.null.no-inverse@1")
        rep = self.assertFires("E301")
        # and a cycle cannot support itself
        self.assertEqual(rep.eff["fx.null.no-inverse"], "unsupported")

    def test_E302_postdiction(self):
        self.edit("fx.thermo.two-state", "version: 1",
                  "version: 1\nfitted_to:\n- data.analogue-horizons")
        self.assertFires("E302")

    def test_E303_proved_claims_contradict(self):
        self.edit("fx.parity.even", "version: 1",
                  "version: 1\ncontradicts:\n- fx.parity.grading@1")
        self.assertFires("E303")

    def test_E307_rests_on_contradicting_postulates(self):
        self.edit("fx.transport.principle", "version: 1",
                  "version: 1\ncontradicts:\n- fx.thermo.period-premise@1")
        rep = self.assertFires("E307")
        # two incompatible hypotheses are not an inconsistent store; the error
        # is on the results that rest on both
        self.assertNotIn("E303", self.codes(rep))
        self.assertIn("fx.thermo.temperature",
                      {f.entity for f in rep.findings if f.code == "E307"})
        self.assertNotIn("fx.transport.principle",
                         {f.entity for f in rep.findings if f.code == "E307"})

    def test_E304_declared_ledger_mismatch(self):
        self.edit("fx.boost.sigma", "version: 1", "version: 1\nledger: essential")
        self.assertFires("E304")

    def test_I305_impact_report(self):
        write_lock(load_store(self.root))
        self.edit("fx.witt.car", "version: 1", "version: 2")
        self.edit("fx.witt.car", "## formal\n", "## formal\nRestated: ")
        rep = self.assertFires("I305")
        self.assertIn("fx.boost.sigma-square", rep.impact["affected_claims"])


L4 = (1, 2, 3, 4)


class Layer4Evidence(StoreCase):
    def test_E401_missing_check_file(self):
        os.remove(E(self.folder("fx.algebra.dimension"), "check.py"))
        self.assertFires("E401", L4, run_mutants=False)

    def test_E402_float(self):
        self.edit("fx.algebra.dimension", "== 4", "== 4.0", "check.py")
        self.assertFires("E402", L4, run_mutants=False)

    def test_E402_math_module(self):
        self.edit("fx.algebra.dimension", "import GA as g", "import GA as g\nimport math",
                  "check.py")
        self.assertFires("E402", L4, run_mutants=False)

    def test_E403_no_GA(self):
        self.write("fx.algebra.dimension", "check.py",
                   "def test_dimension():\n    assert len([(), (0,), (1,), (0, 1)]) == 4\n")
        self.assertFires("E403", L4, run_mutants=False)

    def test_E404_undeclared_premise(self):
        self.edit("fx.algebra.dimension", "def test_dimension():",
                  "from tp_premise import premise\n\ndef test_dimension():\n"
                  "    premise('fx.witt.car')", "check.py")
        self.assertFires("E404", L4, run_mutants=False)

    def test_W405_declared_but_untouched(self):
        self.edit("fx.boost.sigma-square", '    premise("fx.boost.sigma")\n', "",
                  "check.py")
        self.assertFires("W405", L4, run_mutants=False)

    def test_E406_failing_check(self):
        self.edit("fx.algebra.dimension", "== 4", "== 5", "check.py")
        self.assertFires("E406", L4, run_mutants=False)

    def test_E406_failure_makes_dependants_stale(self):
        from tp import derive
        self.edit("fx.witt.car", "g.sc(1)", "g.sc(2)", "check.py")
        st = load_store(self.root)
        rep = V.validate(st, layers=L4, keep_going=True, run_mutants=False)
        st_info = derive.staleness(st, rep.check_failed)
        self.assertIn("fx.boost.sigma", st_info["stale"])

    def test_E407_nondeterministic(self):
        calls = {"n": 0}
        real = evidence.run_check

        def flaky(*a, **k):
            r = real(*a, **k)
            calls["n"] += 1
            if calls["n"] % 2 == 0:
                r = dict(r, touched=["fx.surprise"])
            return r
        evidence.run_check = flaky
        try:
            self.assertFires("E407", L4, run_mutants=False)
        finally:
            evidence.run_check = real

    def test_E408_asserts_nothing(self):
        self.write("fx.algebra.dimension", "check.py",
                   "import GA as g\n\ndef test_dimension():\n    g.all_blades(2)\n")
        self.assertFires("E408", L4, run_mutants=False)

    def test_E408_mutation_survives(self):
        self.write("fx.algebra.dimension", "check.py",
                   "import GA as g\n\ndef test_dimension():\n"
                   "    assert len(g.all_blades(2)) >= 0\n")
        self.assertFires("E408", L4, run_mutants=True)

    def test_W408_nothing_to_perturb(self):
        self.write("fx.algebra.dimension", "check.py",
                   "import GA as g\nTWO = len('ab')\n\ndef test_dimension():\n"
                   "    assert len(g.all_blades(TWO)) == TWO * TWO\n")
        self.assertFires("W408", L4, run_mutants=True)

    def test_E408_good_check_survives_mutation_testing(self):
        rep = self.run_layers(L4, run_mutants=True)
        self.assertNotIn("E408", self.codes(rep))

    def test_E409_sandbox(self):
        self.write("fx.algebra.dimension", "check.py",
                   "import GA as g\nimport socket\n\ndef test_dimension():\n"
                   "    socket.create_connection(('example.com', 80), 1)\n"
                   "    assert len(g.all_blades(2)) == 4\n")
        self.assertFires("E409", L4, run_mutants=False)

    def test_legacy_pass_fail_and_untagged(self):
        legacy = E(self.root, "legacy")
        os.makedirs(legacy)
        open(E(legacy, "verify_TX.py"), "w").write(
            "import GA as g\n"
            "g.check('[Prop 1.1] blades of Cl(1,1)', len(g.all_blades(2)) == 4)\n"
            "g.check('[Prop 1.2] deliberately wrong', len(g.all_blades(2)) == 5)\n")
        cfg = yaml.safe_load(open(E(self.root, "config.yaml")))
        cfg["legacy_scripts_dir"] = "legacy"
        yaml.safe_dump(cfg, open(E(self.root, "config.yaml"), "w"))
        self.edit("fx.parity.grading", "- kind: proof\n  derivation: direct",
                  "- kind: legacy\n  script: verify_TX.py\n  tags:\n  - num:1.1")
        self.edit("fx.parity.even", "- kind: proof\n  derivation: direct",
                  "- kind: legacy\n  script: verify_TX.py\n  tags:\n  - num:1.2")
        self.edit("fx.thermo.two-state", "- kind: proof\n  derivation: via-descent",
                  "- kind: legacy\n  script: verify_TX.py\n  tags:\n  - num:9.9")
        rep = self.run_layers(L4, run_mutants=False)
        by = {(f.code, f.entity) for f in rep.findings}
        self.assertIn(("I410", "fx.parity.grading"), by)
        self.assertIn(("E406", "fx.parity.even"), by)
        self.assertIn(("E412", "fx.thermo.two-state"), by)

    def test_W411_lean(self):
        self.edit("fx.parity.grading", "- kind: proof\n  derivation: direct",
                  "- kind: lean\n  ref: Transport.grading")
        self.assertFires("W411", L4, run_mutants=False)


class Layer5Meaning(StoreCase):
    def test_W501_duplicate(self):
        text = ("For one fermionic mode the KMS state at inverse temperature beta is "
                "the Gibbs state of the number operator with the boost dynamics")
        self.set_formal("fx.qi.kms", text)
        self.set_formal("fx.parity.grading", text)
        self.assertFires("W501", (1, 2, 3, 5))

    def test_I502_judge_skipped(self):
        self.assertFires("I502", (5,))


class Fixes(StoreCase):
    def test_E107_blank_proof_file_is_no_proof(self):
        self.write("fx.algebra.dimension", "proof-count.tex", "\n")
        self.assertFires("E107")

    def test_specialises_spreads_staleness(self):
        from tp import derive
        self.edit("fx.parity.even", "version: 1", "version: 1\nspecialises:\n- fx.parity.grading@1")
        self.edit("fx.parity.grading", "version: 1", "version: 2")
        st = load_store(self.root)
        self.assertIn("fx.parity.even", derive.staleness(st, set())["stale"])

    def test_cycle_descendants_keep_ledger_and_staleness(self):
        from tp import derive
        self.edit("fx.null.square-zero", "- name: direct",
                  "- name: direct\n  uses:\n  - fx.null.no-inverse@1")
        st = load_store(self.root)
        led = derive.ledger(st)
        self.assertIn("fx.thermo.two-state", led)
        self.assertEqual(led["fx.thermo.two-state"], "essential")

    def test_conditions_list_postulates(self):
        from tp import derive
        st = load_store(self.root)
        g = derive.logical_graph(st)
        past, _ = derive.cones(g, st.entities.keys())
        c = derive.conditions(st, past)
        self.assertEqual(c["fx.thermo.temperature"],
                         ["fx.thermo.period-premise", "fx.transport.principle"])

    def test_foundation_postulates_are_not_conditions(self):
        from tp import derive
        self.edit("fx.transport.principle", "status: postulate",
                  "status: postulate\nfoundation: true")
        st = load_store(self.root)
        g = derive.logical_graph(st)
        past, _ = derive.cones(g, st.entities.keys())
        self.assertEqual(derive.conditions(st, past)["fx.thermo.temperature"],
                         ["fx.thermo.period-premise"])
        self.assertEqual(derive.foundation_of(st, past)["fx.thermo.temperature"],
                         ["fx.transport.principle"])


class Repin(StoreCase):
    def test_repin_clears_stale_edges(self):
        from tp import derive
        from tp.repin import repin
        self.edit("fx.witt.car", "version: 1", "version: 2")
        st = load_store(self.root)
        self.assertTrue(derive.staleness(st, set())["stale_edges"])
        self.assertEqual(repin(self.root, ["fx.boost.sigma"]), 1)
        st = load_store(self.root)
        self.assertNotIn("fx.boost.sigma", {e.src for e in derive.staleness(st, set())["stale_edges"]})

    def test_repin_needs_no_version_bump(self):
        from tp.repin import repin
        write_lock(load_store(self.root))
        self.edit("fx.witt.car", "version: 1", "version: 2")
        self.edit("fx.witt.car", "## formal\n", "## formal\nRevised. ")
        write_lock(load_store(self.root))
        repin(self.root, ["fx.boost.sigma"])
        rep = self.run_layers((1, 2, 3))
        self.assertNotIn("E206", self.codes(rep))

    def test_E206_check_file_edit_needs_a_bump(self):
        write_lock(load_store(self.root))
        self.edit("fx.algebra.dimension", "== 4", "== 4 or True", "check.py")
        self.assertFires("E206")


class Hardening(StoreCase):
    def test_W413_weak_check(self):
        self.write("fx.algebra.dimension", "check.py",
                   "import GA as g\n\n\ndef test_dimension():\n    a, b, c = 7, 9, 11\n"
                   "    assert len(g.all_blades(2)) == 4\n")
        self.assertFires("W413", L4, run_mutants=True)

    def test_forged_result_line_is_not_accepted(self):
        from tp import evidence
        src = ("import GA, json\n\ndef t():\n    print('@@RESULT@@' + json.dumps("
               "{'ok': True, 'touched': []}))\n    assert 1 == 2\n")
        r = evidence.run_check(self.root, self.folder("fx.algebra.dimension"), src, "t")
        self.assertFalse(r["ok"])

    def test_sandbox_refuses_os_level_writes_and_spawns(self):
        from tp import evidence
        target = E(self.tmp, "outside.txt")
        for body in (f"fd = os.open({target!r}, os.O_WRONLY | os.O_CREAT)",
                     f"os.remove({E(self.root, 'config.yaml')!r})",
                     "os.posix_spawn('/bin/true', ['true'], {})",
                     "import sys; sys._getframe(1)"):
            src = f"import GA, os\n\ndef t():\n    {body}\n    assert 1 == 1\n"
            r = evidence.run_check(self.root, self.folder("fx.algebra.dimension"), src, "t")
            self.assertFalse(r["ok"], body)
        self.assertFalse(os.path.exists(target))
        self.assertTrue(os.path.exists(E(self.root, "config.yaml")))

    def test_E401_legacy_script_must_be_a_name(self):
        self.edit("fx.algebra.dimension", "checked_by:\n",
                  "checked_by:\n- kind: legacy\n  script: ../../evil.py\n  tags: [num:1]\n")
        self.assertFires("E401", L4, run_mutants=False)

    def test_E111_forbidden_macro_even_if_declared(self):
        self.set_formal("fx.algebra.dimension", r"See \input{/etc/passwd} here.")
        self.assertFires("E111")

    def test_E111_title_is_checked(self):
        self.edit("fx.algebra.dimension", "title: ", "title: \\href{x}{y} ")
        self.assertFires("E111")


class StalenessThroughSpecialisation(StoreCase):
    def _add(self, meta):
        from tp.model import dump_entity
        m = {"version": 1, "proposed_by": {"kind": "human"}, "ai_involved": "no",
             "subject": "algebra", "kind": "claim", "status": "proved",
             "checked_by": [{"kind": "proof"}]}
        m.update(meta)
        f = E(self.root, "claims", m["id"])
        os.makedirs(f)
        open(E(f, "entity.md"), "w").write(dump_entity(m, {
            "formal": "x.", "technical": "pending", "lay": "pending", "one-liner": "x"}))
        open(E(f, "p.tex"), "w").write("trivial.")

    def test_dependant_of_a_stale_specialisation_is_stale(self):
        from tp import derive
        self._add({"id": "fx.x.spec", "title": "X", "specialises": ["fx.boost.sigma@1"],
                   "derivations": [{"name": "d", "proof": "p.tex"}]})
        self._add({"id": "fx.z.user", "title": "Z",
                   "derivations": [{"name": "d", "uses": ["fx.x.spec@1"], "proof": "p.tex"}]})
        self.edit("fx.witt.car", "version: 1", "version: 2")
        st = derive.staleness(load_store(self.root), set())
        self.assertIn("fx.x.spec", st["stale"])
        self.assertIn("fx.z.user", st["stale"])


class ConditionsInLevels(StoreCase):
    def test_W503_lay_drops_the_condition(self):
        self.set_formal("fx.boost.sigma", r"Under Hypothesis (S), the boost squares to one.")
        p = E(self.folder("fx.boost.sigma"), "entity.md")
        txt = open(p).read()
        txt = re.sub(r"## lay\n.*?\n\n## one-liner", "## lay\nThe boost squares to one.\n\n## one-liner",
                     txt, flags=re.S)
        open(p, "w").write(txt)
        self.assertFires("W503", (5,))


class Killed(StoreCase):
    def test_W306_killed_prediction_flags_its_basis(self):
        self.edit("fx.pred.single-temperature", "status: live", "status: killed")
        rep = self.assertFires("W306")
        from tp import derive
        eff = derive.effective_status(load_store(self.root))
        self.assertEqual(eff["fx.pred.single-temperature"], "killed")


class Layer6People(StoreCase):
    def test_E601_new_imported_entity_by_contributor(self):
        write_lock(load_store(self.root))
        shutil.copytree(self.folder("fx.qi.kms"), E(self.root, "claims", "fx.qi.kms-two"))
        self.edit("fx.qi.kms-two", "id: fx.qi.kms", "id: fx.qi.kms-two")
        self.assertFires("E601", (6,), author="contributor")

    def test_github_login_counts_as_maintainer(self):
        write_lock(load_store(self.root))
        cfg = E(self.root, "config.yaml")
        s = open(cfg).read()
        open(cfg, "w").write(s.replace("maintainers:", "github_logins: [leon-gh]\n  maintainers:", 1))
        self.edit("fx.thermo.entropy-tick", "status: conjectured", "status: imported")
        rep = self.run_layers((6,), author="leon-gh")
        self.assertNotIn("E601", self.codes(rep))

    def test_E602_no_author(self):
        self.assertFires("E602", (6,))

    def test_E601_status_to_imported(self):
        write_lock(load_store(self.root))
        self.edit("fx.thermo.entropy-tick", "status: conjectured", "status: imported")
        self.assertFires("E601", (6,), author="contributor")

    def test_E601_remove_assumes(self):
        write_lock(load_store(self.root))
        self.edit("fx.ascent.minimal-completion", "  assumes:\n  - fx.transport.principle@1\n", "")
        self.assertFires("E601", (6,), author="contributor")

    def test_E601_non_maintainer_adds_assumes(self):
        write_lock(load_store(self.root))
        self.edit("fx.boost.sigma", "  proof: proof-direct.tex",
                  "  assumes:\n  - fx.transport.principle@1\n  proof: proof-direct.tex")
        self.edit("fx.boost.sigma", "version: 1", "version: 2")
        self.assertFires("E601", (6,), author="contributor")

    def test_E601_maintainer_may(self):
        write_lock(load_store(self.root))
        self.edit("fx.boost.sigma", "  proof: proof-direct.tex",
                  "  assumes:\n  - fx.transport.principle@1\n  proof: proof-direct.tex")
        rep = self.run_layers((6,), author="leon")
        self.assertNotIn("E601", self.codes(rep))

    CREDIT = ("ai_involved: 'no'\ncredit:\n- name: Original Author\n  role: the result\n")

    def credited(self, eid="fx.thermo.entropy-tick"):
        self.edit(eid, "ai_involved: 'no'\n", self.CREDIT)
        write_lock(load_store(self.root))

    def test_E603_amendment_drops_original_credit(self):
        self.credited()
        self.edit("fx.thermo.entropy-tick", "- name: Original Author\n  role: the result\n",
                  "- name: Amender\n  role: correction\n  version: 2\n")
        self.edit("fx.thermo.entropy-tick", "version: 1", "version: 2")
        self.assertFires("E603", (6,), author="contributor")
        self.assertFires("W220", (1, 2))

    def test_E604_amendment_without_own_credit(self):
        self.credited()
        self.edit("fx.thermo.entropy-tick", "## formal\n", "## formal\nCorrected: ")
        self.edit("fx.thermo.entropy-tick", "version: 1", "version: 2")
        self.assertFires("E604", (6,), author="contributor")
        self.assertFires("W221", (1, 2))

    def test_amendment_that_adds_its_credit_passes(self):
        self.credited()
        self.edit("fx.thermo.entropy-tick", "  role: the result\n",
                  "  role: the result\n- name: Amender\n  role: correction\n  version: 2\n"
                  + self.RESTATED)
        self.edit("fx.thermo.entropy-tick", "## formal\n", "## formal\nCorrected: ")
        self.edit("fx.thermo.entropy-tick", "version: 1", "version: 2")
        rep = self.run_layers((1, 2, 6), author="contributor")
        bad = {"E603", "E604", "E605", "E606", "E607", "E608", "W220", "W221"} & self.codes(rep)
        self.assertFalse(bad, "\n".join(f.render() for f in rep.findings))

    # every person a contributor credits gives an ORCID iD (E610)
    def test_E610_new_entity_credit_without_orcid(self):
        write_lock(load_store(self.root))
        shutil.copytree(self.folder("fx.boost.sigma"), E(self.root, "claims", "fx.boost.sigma-two"))
        self.edit("fx.boost.sigma-two", "id: fx.boost.sigma", "id: fx.boost.sigma-two")
        self.edit("fx.boost.sigma-two", "ai_involved: 'no'\n",
                  "ai_involved: 'no'\ncredit:\n- name: New Person\n  role: the result\n"
                  "- name: Claude Opus 5.5\n  role: drafting\n")
        rep = self.assertFires("E610", (6,), author="contributor")
        self.assertEqual(sum(f.code == "E610" for f in rep.findings), 1)    # the model is exempt

    def test_E610_orcid_given_passes(self):
        write_lock(load_store(self.root))
        shutil.copytree(self.folder("fx.boost.sigma"), E(self.root, "claims", "fx.boost.sigma-two"))
        self.edit("fx.boost.sigma-two", "id: fx.boost.sigma", "id: fx.boost.sigma-two")
        self.edit("fx.boost.sigma-two", "ai_involved: 'no'\n",
                  "ai_involved: 'no'\ncredit:\n- name: New Person\n  role: the result\n"
                  "  orcid: 0000-0002-1825-0097\n")
        self.assertNotIn("E610", self.codes(self.run_layers((6,), author="contributor")))

    def test_E610_amendment_credit_needs_orcid_earlier_entries_do_not(self):
        self.credited()
        self.edit("fx.thermo.entropy-tick", "  role: the result\n",
                  "  role: the result\n- name: Amender\n  role: correction\n  version: 2\n"
                  + self.RESTATED)
        self.edit("fx.thermo.entropy-tick", "## formal\n", "## formal\nCorrected: ")
        self.edit("fx.thermo.entropy-tick", "version: 1", "version: 2")
        rep = self.assertFires("E610", (6,), author="contributor")
        self.assertEqual([f.message.split(" gives")[0] for f in rep.findings if f.code == "E610"],
                         ["credit: Amender"])

    def test_E610_maintainer_exempt(self):
        write_lock(load_store(self.root))
        shutil.copytree(self.folder("fx.boost.sigma"), E(self.root, "claims", "fx.boost.sigma-two"))
        self.edit("fx.boost.sigma-two", "id: fx.boost.sigma", "id: fx.boost.sigma-two")
        self.edit("fx.boost.sigma-two", "ai_involved: 'no'\n",
                  "ai_involved: 'no'\ncredit:\n- name: New Person\n  role: the result\n")
        self.assertNotIn("E610", self.codes(self.run_layers((6,), author="leon")))

    # amendments say what they fix (tp/amend.py)
    RESTATED = ("amendments:\n- version: 2\n  kind: restatement\n"
                "  defect: the stated rate holds only for a non-rotating hole\n")

    def amend(self, eid, block, version=2):
        self.edit(eid, "ai_involved: 'no'\n", "ai_involved: 'no'\n" + block)
        self.edit(eid, "version: 1", f"version: {version}")

    def test_E605_amendment_without_declaration(self):
        write_lock(load_store(self.root))
        self.edit("fx.thermo.entropy-tick", "## formal\n", "## formal\nCorrected: ")
        self.edit("fx.thermo.entropy-tick", "version: 1", "version: 2")
        self.assertFires("E605", (6,), author="contributor")

    def test_E606_wording_change_keeps_the_version(self):
        write_lock(load_store(self.root))
        self.edit("fx.thermo.entropy-tick", "## lay\npending", "## lay\nIt ticks.")
        self.amend("fx.thermo.entropy-tick", self.RESTATED)
        self.assertFires("E606", (6,), author="contributor")

    def test_E607_correction_that_changes_the_statement(self):
        write_lock(load_store(self.root))
        self.edit("fx.thermo.entropy-tick", "## formal\n", "## formal\nCorrected: ")
        self.amend("fx.thermo.entropy-tick", self.RESTATED.replace("restatement", "correction"))
        self.assertFires("E607", (6,), author="contributor")

    def test_E607_restatement_that_keeps_the_statement(self):
        write_lock(load_store(self.root))
        self.write("fx.boost.sigma", "proof-direct.tex", "A corrected second step.\n")
        self.amend("fx.boost.sigma", self.RESTATED)
        self.assertFires("E607", (6,), author="contributor")

    def test_E608_evidence_is_not_a_check(self):
        write_lock(load_store(self.root))
        self.write("fx.boost.sigma", "proof-direct.tex", "A corrected second step.\n")
        self.amend("fx.boost.sigma", self.RESTATED.replace("restatement", "correction")
                   + "  evidence: check.py::test_missing\n")
        self.assertFires("E608", (6,), author="contributor")

    def test_correction_with_evidence_passes(self):
        write_lock(load_store(self.root))
        self.write("fx.boost.sigma", "proof-direct.tex", "A corrected second step.\n")
        self.amend("fx.boost.sigma", self.RESTATED.replace("restatement", "correction")
                   + "  evidence: check.py::test_sigma\n")
        rep = self.run_layers((6,), author="contributor")
        self.assertFalse({"E605", "E606", "E607", "E608"} & self.codes(rep),
                         "\n".join(f.render() for f in rep.findings))

    def test_maintainer_amendment_needs_no_declaration(self):
        write_lock(load_store(self.root))
        self.edit("fx.thermo.entropy-tick", "## formal\n", "## formal\nCorrected: ")
        self.edit("fx.thermo.entropy-tick", "version: 1", "version: 2")
        self.assertNotIn("E605", self.codes(self.run_layers((6,), author="leon")))

    # the language is geometric algebra (tp/galang.py)
    def test_E609_change_outside_ga_undeclared(self):
        write_lock(load_store(self.root))
        self.edit("fx.thermo.entropy-tick", "## formal\n", "## formal\nIn the Pauli matrices, ")
        self.edit("fx.thermo.entropy-tick", "version: 1", "version: 2")
        self.assertFires("E609", (6,), author="contributor")
        self.assertFires("W222", (1, 2))

    def test_E609_new_entity_outside_ga(self):
        write_lock(load_store(self.root))
        shutil.copytree(self.folder("fx.thermo.entropy-tick"), E(self.root, "claims", "fx.thermo.entropy-two"))
        self.edit("fx.thermo.entropy-two", "id: fx.thermo.entropy-tick", "id: fx.thermo.entropy-two")
        self.edit("fx.thermo.entropy-two", "## formal\n", "## formal\nOver $\\mathbb{C}$, ")
        self.assertFires("E609", (6,), author="contributor")

    def test_outside_ga_declared_passes(self):
        write_lock(load_store(self.root))
        self.edit("fx.thermo.entropy-tick", "## formal\n", "## formal\nIn the Pauli matrices, ")
        self.edit("fx.thermo.entropy-tick", "ai_involved: 'no'\n",
                  "ai_involved: 'no'\noutside_ga:\n  kind: bridge\n"
                  "  why: it states the result in the matrix form physicists use\n")
        self.edit("fx.thermo.entropy-tick", "version: 1", "version: 2")
        rep = self.run_layers((1, 2, 6), author="contributor")
        self.assertFalse({"E609", "W222"} & self.codes(rep), "\n".join(f.render() for f in rep.findings))

    def test_E601_removal_without_tombstone(self):
        write_lock(load_store(self.root))
        shutil.rmtree(self.folder("fx.parity.grading"))
        self.assertFires("E601", (6,), author="contributor")


NOTE = """---
id: {id}
kind: note
version: 1
title: A remark on the null vector
status: {status}
proposed_by: {{kind: human, author: fixture}}
ai_involved: 'no'
subject: algebra
comments_on: [{on}]
---

## formal
The remark: $v^2 = 0$ although $v \\neq 0$.

## technical
pending

## lay
pending

## one-liner
pending
"""


class Notes(StoreCase):
    def add_note(self, eid="note.fx.remark", status="remark", on="fx.null.no-inverse"):
        d = E(self.root, "notes", eid)
        os.makedirs(d, exist_ok=True)
        open(E(d, "entity.md"), "w").write(NOTE.format(id=eid, status=status, on=on))

    def test_a_note_is_valid(self):
        self.add_note()
        rep = self.run_layers()
        self.assertEqual([f.render() for f in rep.findings if f.code.startswith("E")], [])
        self.assertEqual(rep.eff["note.fx.remark"], "remark")

    def test_note_status(self):
        self.add_note(status="proved")
        self.assertFires("E105")

    def test_nothing_may_use_a_note(self):
        self.add_note()
        self.edit("fx.null.no-inverse", "fx.null.square-zero@1",
                  "fx.null.square-zero@1\n  - note.fx.remark@1")
        self.assertFires("E203")

    def test_a_note_comments_on_results_not_notes(self):
        self.add_note()
        self.add_note("note.fx.second", on="note.fx.remark")
        self.assertFires("E203")

    def test_note_target_must_exist(self):
        self.add_note(on="fx.no-such-claim")
        self.assertFires("E201")


class LabelRegistry(unittest.TestCase):
    REG = {"T01:sec:x": {"section": "Totality of the reciprocal"},
           "T01:rem:y": {"entity": "note.t.y"},
           "T01:eq:z": {"display": "X(x)^2 = 0 ,", "near": "t.a"},
           "T01:eq:long": {"display": "a" * 200, "near": "t.a"},
           "T01:tab:t": {"table": "The algorithm", "near": "t.alg"},
           "T01:fig:f": {"kind": "figure"},
           "T01:thm:w": {"entity": "t.w"}}

    def r(self, text, entities=("note.t.y", "t.a", "t.alg", "t.w")):
        from tp import labels
        return labels.resolve(text, "T01", self.REG, entities=set(entities), plain=True)

    def test_section_becomes_its_title(self):
        self.assertEqual(self.r(r"see Section~\ref{sec:x}"),
                         "see the section \u201cTotality of the reciprocal\u201d")

    def test_result_word_kept_for_entities(self):
        self.assertEqual(self.r(r"Remark~\ref{rem:y}"), r"Remark~\claimref{note.t.y}")
        self.assertEqual(self.r(r"Theorem \ref{thm:w}"), r"Theorem \claimref{t.w}")

    def test_short_equation_written_out(self):
        self.assertEqual(self.r(r"by \eqref{eq:z}"), r"by $X(x)^2 = 0$")
        self.assertEqual(self.r(r"(\eqref{eq:z})"), r"($X(x)^2 = 0$)")

    def test_long_equation_points_to_its_result(self):
        self.assertEqual(self.r(r"\eqref{eq:long}"),
                         r"the relation displayed with \claimref{t.a}")

    def test_table_and_figure(self):
        self.assertEqual(self.r(r"Table~\ref{tab:t}"), r"the table accompanying \claimref{t.alg}")
        self.assertEqual(self.r(r"Figure \ref{fig:f}"), "a figure of the original")

    def test_unknown_label_is_left_alone(self):
        self.assertEqual(self.r(r"\ref{nope}"), r"\ref{nope}")

    def test_missing_entity_is_not_linked(self):
        self.assertEqual(self.r(r"Remark \ref{rem:y}", entities=()), r"Remark \ref{rem:y}")


class Tags(StoreCase):
    def vocab(self, tags):
        yaml.safe_dump(tags, open(E(self.root, "tags.yaml"), "w"))

    def test_unknown_tag(self):
        self.vocab([{"id": "witt", "title": "Witt", "group": "structures", "about": "x"}])
        self.edit("fx.null.no-inverse", "subject: algebra", "subject: algebra\ntags: [witt, nope]")
        rep = self.assertFires("E211")
        self.assertNotIn("W212", self.codes(rep))

    def test_unused_tag(self):
        self.vocab([{"id": "witt", "title": "Witt", "group": "structures", "about": "x"}])
        self.assertFires("W212")


class PremisesCited(StoreCase):
    def test_uncited_premise_warns(self):
        # the fixture's no-inverse proof does not \claimref its premise
        self.assertFires("W215", layers=(1, 2))

    def test_cited_premise_is_quiet(self):
        self.write("fx.null.no-inverse", "proof-direct.tex",
                   r"By \claimref{fx.null.square-zero}, $v = u v^2 = 0$.")
        rep = self.run_layers((1, 2))
        self.assertNotIn("fx.null.no-inverse",
                         [f.entity for f in rep.findings if f.code == "W215"])


class ClaimrefTargets(StoreCase):
    def test_unknown_claimref(self):
        self.set_formal("fx.null.no-inverse", r"See \claimref{fx.no-such-result}.")
        self.assertFires("E214", layers=(1, 2))


class SubjectFit(unittest.TestCase):
    def test_bridge_is_reported(self):
        from types import SimpleNamespace as NS
        ents = {"a": NS(meta={"subject": "x"}), "b": NS(meta={"subject": "y"}),
                "c": NS(meta={"subject": "y"}), "d": NS(meta={"subject": "y"}),
                "e": NS(meta={"subject": "x"}), "f": NS(meta={"subject": "y"})}
        store = NS(entities=ents)
        fit = V.subject_fit(store, {"a": {"b", "c", "d", "f"}, "e": {"a"}})
        self.assertIn("a", fit)                       # I213: 1 of 5 neighbours shares x
        self.assertEqual(fit["a"][2], "y")


# W510, I510: tested in tests/test_quantity.py (Contradictions)
# E130 E131 E132 E133 E134 E135 E136 E137 E138: review records, tested in tests/test_reviews.py
class RuleCoverage(unittest.TestCase):
    def test_every_code_has_a_test(self):
        here = open(__file__).read()
        src = "".join(open(E(os.path.dirname(V.__file__), f)).read()
                      for f in ("validate.py", "evidence.py"))
        codes = set(re.findall(r'"([EWI]\d{3})"', src)) | set(re.findall(r"\(\"([EWI]\d{3})\"", src))
        tested = set(re.findall(r"[EWI]\d{3}", here))
        missing = sorted(codes - tested)
        self.assertEqual(missing, [], f"codes without a test: {missing}")


if __name__ == "__main__":
    unittest.main()


class OpenProblems(StoreCase):
    GOOD = """- id: op.fixture-problem
  title: A fixture problem
  area: {area}
  kind: research
  difficulty: tractable
  status: open
  statement: Settle \\\\claimref{{fx.null.square-zero}}.
  entities: [fx.null.square-zero]
"""

    def area(self):
        return load_store(self.root).subjects[0]["id"]

    def write_ops(self, text):
        open(E(self.root, "open_problems.yaml"), "w").write(text)

    def test_clean_registry(self):
        self.write_ops(self.GOOD.format(area=self.area()))
        codes = self.codes(self.run_layers((1, 2)))
        self.assertNotIn("E216", codes)
        self.assertNotIn("E217", codes)

    def test_E216_unknown_entity(self):
        self.write_ops(self.GOOD.format(area=self.area()).replace(
            "entities: [fx.null.square-zero]", "entities: [fx.no-such]"))
        self.assertFires("E216", layers=(1, 2))

    def test_E216_unknown_claimref(self):
        self.write_ops(self.GOOD.format(area=self.area()).replace(
            "claimref{fx.null.square-zero}", "claimref{fx.nothing}"))
        self.assertFires("E216", layers=(1, 2))

    def test_E217_malformed(self):
        self.write_ops(self.GOOD.format(area=self.area()).replace("difficulty: tractable",
                                                                   "difficulty: easy"))
        self.assertFires("E217", layers=(1, 2))


# ---------------------------------------------------------------------------
# roadmap items 4, 5, 7, 8, 10, 12: quieter W405, parallel layer 4, records
# ---------------------------------------------------------------------------

from tp.model import dump_entity  # noqa: E402

OTHER_FUNC = '''

def test_other():
    SQ = g.sig(1, 1)
    assert g.eq(g.mul(g.gen(0), g.gen(0), SQ), g.sc(1))
'''


class QuietPremises(StoreCase):
    def w405(self, rep, eid=None):
        return [f for f in rep.findings if f.code == "W405"
                and (eid is None or f.entity == eid)]

    def i405(self, rep, eid=None):
        return [f for f in rep.findings if f.code == "I405"
                and (eid is None or f.entity == eid)]

    def add_check(self, eid, func="test_other", body=OTHER_FUNC):
        p = E(self.folder(eid), "check.py")
        open(p, "a").write(body)
        self.edit(eid, "checked_by:\n", f"checked_by:\n- kind: check\n  ref: check.py::{func}\n")

    def test_touched_by_a_sibling_check_is_quiet(self):
        # sigma-square gets a second check that does not touch its premise: the first
        # one does, so the premise is exercised and nothing is reported
        self.add_check("fx.boost.sigma-square")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertEqual(rep.errors(), [], "\n".join(f.render() for f in rep.errors()))
        self.assertEqual(self.w405(rep), [])

    def test_W405_once_per_premise(self):
        self.edit("fx.boost.sigma-square", '    premise("fx.boost.sigma")\n', "", "check.py")
        self.add_check("fx.boost.sigma-square")
        rep = self.run_layers(L4, run_mutants=False)
        ws = self.w405(rep, "fx.boost.sigma-square")
        self.assertEqual(len(ws), 1)
        self.assertIn("none of the entity's 2 check function(s)", ws[0].message)

    def test_I405_external_literature_entry(self):
        lit = E(self.root, "claims", "fx.lit.textbook-external")
        os.makedirs(lit)
        meta = {"id": "fx.lit.textbook-external", "kind": "claim", "version": 1,
                "title": "A textbook fact", "status": "imported", "subject": "algebra",
                "proposed_by": {"kind": "human"}, "ai_involved": "no",
                "imported_from": [{"citation": "Lounesto, Clifford Algebras and Spinors"}]}
        open(E(lit, "entity.md"), "w").write(dump_entity(
            meta, {"formal": "Every Clifford algebra has a basis of blades.",
                   "technical": "pending", "lay": "pending", "one-liner": "Blades."}))
        self.edit("fx.algebra.dimension", "- name: count\n",
                  "- name: count\n  uses:\n  - fx.lit.textbook-external@1\n")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertEqual(self.w405(rep), [])
        msgs = [f.message for f in self.i405(rep, "fx.algebra.dimension")]
        self.assertTrue(any("-external" in m for m in msgs), msgs)

    def test_I405_restatement(self):
        self.edit("fx.boost.sigma-square", '    premise("fx.boost.sigma")\n', "", "check.py")
        self.edit("fx.boost.sigma-square", "checked_by:",
                  "equivalent_to:\n- fx.boost.sigma@1\nchecked_by:")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertEqual(self.w405(rep), [])
        self.assertIn("restatement", self.i405(rep, "fx.boost.sigma-square")[0].message)

    def test_I405_other_derivation(self):
        # a standard route nobody's check belongs to: its premise is not expected
        self.edit("fx.boost.sigma-square", "checked_by:",
                  "- name: standard-route\n  uses:\n  - fx.witt.car@1\nchecked_by:")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertEqual(self.w405(rep), [])
        m = self.i405(rep, "fx.boost.sigma-square")[0].message
        self.assertIn("fx.witt.car", m)
        self.assertIn("standard-route", m)

    def test_check_belonging_to_a_named_derivation(self):
        # the check names the standard route: the other derivation's premise goes quiet
        self.edit("fx.boost.sigma-square", '    premise("fx.boost.sigma")\n',
                  '    premise("fx.witt.car")\n', "check.py")
        self.edit("fx.boost.sigma-square", "checked_by:",
                  "- name: standard-route\n  uses:\n  - fx.witt.car@1\nchecked_by:")
        self.edit("fx.boost.sigma-square", "ref: check.py::test_sigma_square",
                  "ref: check.py::test_sigma_square\n  derivation: standard-route")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertEqual(self.w405(rep), [])
        self.assertIn("fx.boost.sigma", self.i405(rep, "fx.boost.sigma-square")[0].message)

    def test_I405_untouched_postulate_from_coverage(self):
        self.edit("fx.ascent.minimal-completion", '    premise("fx.transport.principle")\n',
                  "", "check.py")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertEqual(len(self.w405(rep, "fx.ascent.minimal-completion")), 1)
        self.write("fx.ascent.minimal-completion", "coverage.yaml",
                   "functions:\n  test_minimal: {kind: exact, clauses: [whole], omits: none}\n"
                   "untouched_premises:\n  fx.transport.principle: a hypothesis, "
                   "nothing to compute\n")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertEqual(self.w405(rep), [])
        self.assertIn("coverage.yaml: a hypothesis",
                      self.i405(rep, "fx.ascent.minimal-completion")[0].message)

    def test_I405_coverage_excuses_a_proved_premise(self):
        self.edit("fx.ascent.minimal-completion", '    premise("fx.null.no-inverse")\n',
                  "", "check.py")
        self.write("fx.ascent.minimal-completion", "coverage.yaml",
                   "untouched_premises:\n  fx.null.no-inverse: its content is checked in "
                   "that entity\n")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertEqual(self.w405(rep), [])
        self.assertNotIn("W127", self.codes(rep))
        self.assertIn("coverage.yaml: its content is checked in that entity",
                      self.i405(rep, "fx.ascent.minimal-completion")[0].message)

    def test_W127_undeclared_or_without_reason(self):
        self.edit("fx.ascent.minimal-completion", '    premise("fx.null.no-inverse")\n',
                  "", "check.py")
        self.write("fx.ascent.minimal-completion", "coverage.yaml",
                   "untouched_premises:\n  fx.null.no-inverse: ''\n"
                   "  fx.witt.car: not declared at all\n")
        rep = self.assertFires("W127", L4, run_mutants=False)
        self.assertEqual(sorted(f.message for f in rep.findings if f.code == "W127"),
                         ["untouched_premises gives no reason for fx.null.no-inverse",
                          "untouched_premises names fx.witt.car, which no derivation declares"])
        self.assertNotIn("E122", self.codes(rep))
        self.assertEqual(len(self.w405(rep, "fx.ascent.minimal-completion")), 1)


class ParallelLayer4(StoreCase):
    def findings(self, jobs, incremental=False):
        st = load_store(self.root)
        rep = V.Report()
        V.layer4(st, rep, run_mutants=True, incremental=incremental, jobs=jobs)
        return rep

    def test_parallel_equals_serial(self):
        self.edit("fx.boost.sigma-square", '    premise("fx.boost.sigma")\n', "", "check.py")
        self.edit("fx.algebra.dimension", "== 4", "== 5", "check.py")
        a, b = self.findings(1), self.findings(2)
        self.assertEqual([(f.code, f.entity, f.message) for f in a.findings],
                         [(f.code, f.entity, f.message) for f in b.findings])
        self.assertEqual(a.check_results, b.check_results)
        self.assertEqual(a.check_failed, b.check_failed)
        self.assertEqual(b.l4_stats["jobs"], 2)
        self.assertIn("W405", {f.code for f in b.findings})
        self.assertIn("E406", {f.code for f in b.findings})

    def test_tp_jobs_environment(self):
        old = os.environ.get("TP_JOBS")
        try:
            os.environ["TP_JOBS"] = "3"
            self.assertEqual(V.l4_jobs(), 3)
            os.environ["TP_JOBS"] = "0"
            self.assertEqual(V.l4_jobs(), max(1, os.cpu_count() or 1))
        finally:
            if old is None:
                os.environ.pop("TP_JOBS", None)
            else:
                os.environ["TP_JOBS"] = old

    def test_replay_recomputes_premise_findings(self):
        self.edit("fx.ascent.minimal-completion", '    premise("fx.transport.principle")\n',
                  "", "check.py")
        first = self.findings(2, incremental=True)
        self.assertEqual(first.l4_stats["replayed"], 0)
        self.assertIn("W405", {f.code for f in first.findings})
        # coverage.yaml is not a layer-4 input: the run replays, and the premise rule
        # is applied afresh to the recorded touched sets
        self.write("fx.ascent.minimal-completion", "coverage.yaml",
                   "untouched_premises:\n  fx.transport.principle: a hypothesis\n")
        second = self.findings(2, incremental=True)
        self.assertEqual(second.l4_stats["ran"], 0)
        codes = {f.code for f in second.findings}
        self.assertNotIn("W405", codes)
        self.assertIn("I405", codes)

    def test_key_follows_the_lib_modules_a_check_imports(self):
        lib = E(self.tmp, "lib")
        os.makedirs(lib)
        for m in ("GA.py", "tp_premise.py"):
            shutil.copy(E(evidence.LIB, m), E(lib, m))
        open(E(lib, "gtg.py"), "w").write("import GA\nX = 1\n")
        open(E(lib, "fock.py"), "w").write("Y = 1\n")
        self.edit("fx.algebra.dimension", "import GA as g\n", "import GA as g\nimport gtg\n",
                  "check.py")
        old = evidence.LIB
        try:
            evidence.LIB = lib

            def keys():
                st = load_store(self.root)
                tc = V._l4_toolchain()
                return {eid: V._l4_key(st, e, eid, tc, None, True, {})
                        for eid, e in st.entities.items()}
            k0 = keys()
            open(E(lib, "fock.py"), "w").write("Y = 2\n")
            self.assertEqual(keys(), k0)                 # nobody imports fock
            open(E(lib, "gtg.py"), "w").write("import GA\nX = 2\n")
            k1 = keys()
            changed = sorted(e for e in k0 if k0[e] != k1[e])
            self.assertEqual(changed, ["fx.algebra.dimension"])
            # gtg starts importing fock: a fock change now reaches gtg's users
            open(E(lib, "gtg.py"), "w").write("import GA\nimport fock\nX = 2\n")
            k2 = keys()
            open(E(lib, "fock.py"), "w").write("Y = 3\n")
            k3 = keys()
            self.assertEqual(sorted(e for e in k2 if k2[e] != k3[e]), ["fx.algebra.dimension"])
            # GA is imported by every check (and the driver): it reruns everything
            open(E(lib, "GA.py"), "a").write("\n# changed\n")
            k4 = keys()
            self.assertTrue(all(k3[e] != k4[e] for e in k3))
        finally:
            evidence.LIB = old

    def test_premise_check_imports_reach_dependants(self):
        # sigma-square runs sigma's check.py through premise(): sigma's lib imports
        # are inputs of sigma-square's key too
        lib = E(self.tmp, "lib")
        os.makedirs(lib)
        for m in ("GA.py", "tp_premise.py"):
            shutil.copy(E(evidence.LIB, m), E(lib, m))
        open(E(lib, "series.py"), "w").write("Z = 1\n")
        self.edit("fx.witt.car", "import GA as g\n", "import GA as g\nimport series\n",
                  "check.py")
        old = evidence.LIB
        try:
            evidence.LIB = lib
            st = load_store(self.root)
            tc = V._l4_toolchain()
            k0 = {eid: V._l4_key(st, e, eid, tc, None, True, {}) for eid, e in st.entities.items()}
            open(E(lib, "series.py"), "w").write("Z = 2\n")
            k1 = {eid: V._l4_key(st, e, eid, tc, None, True, {}) for eid, e in st.entities.items()}
            changed = sorted(e for e in k0 if k0[e] != k1[e])
            # witt.car and everything whose past cone runs its check.py
            self.assertEqual(changed, ["fx.boost.sigma", "fx.boost.sigma-square",
                                       "fx.parity.even", "fx.pred.single-temperature",
                                       "fx.thermo.temperature", "fx.thermo.two-state",
                                       "fx.witt.car"])
            self.assertIn("fx.witt.car", changed)
            self.assertIn("fx.boost.sigma-square", changed)
            self.assertNotIn("fx.null.square-zero", changed)
        finally:
            evidence.LIB = old


QTY = {"id": "fx.const.half", "kind": "quantity", "version": 1, "title": "One half",
       "status": "defined", "subject": "algebra", "proposed_by": {"kind": "human"},
       "ai_involved": "no",
       "quantity": {"symbol": "h", "value": "0.5", "units": "1",
                    "source": {"citation": "definition"}}}


class Quantities(StoreCase):
    def add_quantity(self, **over):
        meta = dict(QTY, **over)
        folder = E(self.root, "quantities", meta["id"])
        os.makedirs(folder, exist_ok=True)
        open(E(folder, "entity.md"), "w").write(dump_entity(
            meta, {"formal": "The number one half.", "technical": "pending",
                   "lay": "pending", "one-liner": "One half."}))

    def use_quantity(self):
        self.edit("fx.algebra.dimension", "import GA as g\n",
                  "import GA as g\nfrom fractions import Fraction\n"
                  "from tp_premise import quantity\n", "check.py")
        self.edit("fx.algebra.dimension", "== 4",
                  "== 4\n    assert quantity('fx.const.half') == Fraction(1, 2)", "check.py")

    def test_exact_values(self):
        for ok in ("0.5", "1.22089e19", "-3/4", "7", "0.51099895"):
            V.exact_value(ok)
        for bad in ("nan", "inf", "1/0", "0x10", "one", 1.5, True, ""):
            with self.assertRaises(ValueError):
                V.exact_value(bad)
        import sys
        sys.path.insert(0, evidence.LIB)
        try:
            import tp_premise
            from fractions import Fraction
            self.assertEqual(tp_premise.exact_value("1.25e2"), Fraction(125))
            with self.assertRaises(ValueError):
                tp_premise.exact_value(0.5)
        finally:
            sys.path.remove(evidence.LIB)

    def test_clean_quantity_entity(self):
        self.add_quantity()
        rep = self.run_layers((1, 2, 3))
        self.assertEqual(rep.errors(), [], "\n".join(f.render() for f in rep.errors()))

    def test_E117_missing_block(self):
        self.add_quantity(quantity=None)
        p = E(self.root, "quantities", "fx.const.half", "entity.md")
        s = open(p).read().replace("quantity: null\n", "")
        open(p, "w").write(s)
        self.assertFires("E117", (1,))

    def test_E117_block_on_a_claim(self):
        self.edit("fx.witt.car", "checked_by:",
                  "quantity:\n  symbol: x\n  value: '1'\n  units: '1'\n  source:\n"
                  "    citation: none\nchecked_by:")
        self.assertFires("E117", (1,))

    def test_E118_inexact_value(self):
        self.add_quantity(quantity=dict(QTY["quantity"], value="about 0.5"))
        self.assertFires("E118", (1,))

    def test_E105_quantity_status(self):
        self.add_quantity(status="guessed")
        self.assertFires("E105", (1,))

    def test_E219_quantity_pin(self):
        self.edit("fx.witt.car", "checked_by:", "quantities:\n- fx.null.square-zero@1\nchecked_by:")
        self.assertFires("E219", (1, 2))

    def test_W414_unlisted_quantity_and_listed_is_quiet(self):
        self.add_quantity()
        self.use_quantity()
        rep = self.assertFires("W414", L4, run_mutants=False)
        self.assertEqual(rep.check_results["fx.algebra.dimension"], "pass")
        self.edit("fx.algebra.dimension", "checked_by:",
                  "quantities:\n- fx.const.half@1\nchecked_by:")
        rep = self.run_layers(L4, run_mutants=False)
        self.assertNotIn("W414", self.codes(rep))
        self.assertEqual(rep.errors(), [], "\n".join(f.render() for f in rep.errors()))

    def test_quantity_value_is_a_layer4_input(self):
        self.add_quantity()
        self.use_quantity()
        st = load_store(self.root)
        tc = V._l4_toolchain()
        e = st.entities["fx.algebra.dimension"]
        k0 = V._l4_key(st, e, e.id, tc, None, True, {})
        self.add_quantity(quantity=dict(QTY["quantity"], value="0.25"))
        st = load_store(self.root)
        k1 = V._l4_key(st, st.entities[e.id], e.id, tc, None, True, {})
        self.assertNotEqual(k0, k1)
        rep = self.run_layers(L4, run_mutants=False)
        self.assertIn("E406", self.codes(rep))      # the check now reads 1/4


class TrustAndSignoffs(StoreCase):
    """Human trust is earned through reviews (tests/test_reviews.py), never set by hand."""
    def sign(self, eid, text):
        self.edit(eid, "checked_by:", text + "checked_by:")

    def test_E119_front_matter_signoffs_are_retired(self):
        self.sign("fx.witt.car", "signoffs:\n- {by: leon, date: '2026-10-23', version: 1, "
                  "level: human-read}\n")
        self.assertFires("E119", (1,))

    def test_E120_human_trust_set_by_hand(self):
        for t in ("human-read", "human-checked"):
            self.edit("fx.witt.car", "checked_by:", f"trust: {t}\nchecked_by:")
            self.assertFires("E120", (1,))
            self.edit("fx.witt.car", f"trust: {t}\n", "")

    def test_ai_and_published_are_fine(self):
        for t in ("ai-proposed", "ai-refereed", "published"):
            self.edit("fx.witt.car", "checked_by:", f"trust: {t}\nchecked_by:")
            self.assertFalse({"E119", "E120"} & self.codes(self.run_layers((1,))))
            self.edit("fx.witt.car", f"trust: {t}\n", "")


class Programmes(StoreCase):
    def config(self, **kw):
        p = E(self.root, "config.yaml")
        cfg = yaml.safe_load(open(p))
        cfg.update(kw)
        yaml.safe_dump(cfg, open(p, "w"))

    REG = {"transport-papers": {"title": "The Transport Papers", "about": "the series"},
           "other": {"title": "Another programme", "about": "x"}}

    def test_off_without_registry(self):
        self.edit("fx.witt.car", "checked_by:", "programme: anything\nchecked_by:")
        self.assertNotIn("E218", self.codes(self.run_layers((1, 2))))

    def test_default_programme_is_clean(self):
        self.config(programmes=self.REG, default_programme="transport-papers")
        self.edit("fx.witt.car", "checked_by:", "programme: other\nchecked_by:")
        self.assertNotIn("E218", self.codes(self.run_layers((1, 2))))

    def test_E218_unregistered(self):
        self.config(programmes=self.REG, default_programme="transport-papers")
        self.edit("fx.witt.car", "checked_by:", "programme: nope\nchecked_by:")
        rep = self.assertFires("E218", (1, 2))
        self.assertEqual([f.entity for f in rep.findings if f.code == "E218"], ["fx.witt.car"])

    def test_E218_no_default(self):
        self.config(programmes=self.REG)
        rep = self.assertFires("E218", (1, 2))
        self.assertEqual(sum(f.code == "E218" for f in rep.findings), 21)

    def test_E218_subject_programme(self):
        self.config(programmes=self.REG, default_programme="transport-papers")
        subs = yaml.safe_load(open(E(self.root, "subjects.yaml")))
        subs[0]["programme"] = "missing"
        yaml.safe_dump(subs, open(E(self.root, "subjects.yaml"), "w"))
        self.assertFires("E218", (1, 2))


class CoverageRecords(StoreCase):
    def cov(self, text, eid="fx.algebra.dimension"):
        self.write(eid, "coverage.yaml", text)

    def test_clean_record_and_I126_counts(self):
        self.cov("functions:\n  test_dimension: {kind: complete, clauses: [whole], "
                 "omits: nothing}\njudge: {by: fixture, date: '2026-10-23', verdict: agrees}\n")
        rep = self.run_layers((1,))
        self.assertFalse({"E122", "E123", "W124", "W125"} & self.codes(rep))
        info = [f for f in rep.findings if f.code == "I126"]
        self.assertEqual(len(info), 1)
        self.assertIn("1 check function(s) in 1 entities (exact 0, complete 1", info[0].message)

    def test_E122_bad_kind_and_keys(self):
        self.cov("functions:\n  test_dimension: {kind: proof, clauses: whole}\nextra: 1\n")
        rep = self.assertFires("E122", (1,))
        self.assertEqual(sum(f.code == "E122" for f in rep.findings), 3)

    def test_E122_unparsable(self):
        self.cov("functions: [unclosed\n")
        self.assertFires("E122", (1,))

    def test_E123_unknown_function(self):
        self.cov("functions:\n  test_dimension: {kind: exact}\n  test_gone: {kind: exact}\n")
        self.assertFires("E123", (1,))

    def test_W124_missing_record(self):
        self.cov("judge: {by: fixture, date: '2026-10-23', verdict: agrees}\n")
        self.assertFires("W124", (1,))

    def test_W125_judge_overclaims(self):
        self.cov("functions:\n  test_dimension: {kind: exact}\n"
                 "judge: {by: fixture, date: '2026-10-23', verdict: overclaims, "
                 "note: the statement says more}\n")
        rep = self.assertFires("W125", (1,))
        self.assertEqual([f.entity for f in rep.findings if f.code == "W125"],
                         ["fx.algebra.dimension"])


class Summary(unittest.TestCase):
    def test_ranked(self):
        rep = V.Report()
        for _ in range(5):
            rep.add("W405", "a.b", "x")
        rep.add("W405", "c.d", "x")
        rep.add("W413", "e.f", "weak")
        rep.add("W408", "e.f", "no literal")
        rep.add("E406", "g.h", "fails")
        rep.add("I405", "a.b", "expected")
        out = V.summarise(rep)
        order = [l.split()[0] for l in out.splitlines()[1:] if l.startswith("  ")
                 and l.split()[0][:1] in "EWI" and l.split()[0][1:].isdigit()]
        self.assertEqual(order, ["E406", "W413", "W408", "W405", "I405"])
        self.assertIn("1 error(s), 8 warning(s), 1 information", out)
        self.assertIn("a.b (5), c.d", out)


class UnparsableCheck(StoreCase):
    def test_syntax_error_with_def_text_is_E401_not_a_crash(self):
        self.write("fx.algebra.dimension", "check.py",
                   "import GA as g\n\ndef test_dimension(:\n    assert True\n")
        rep = self.assertFires("E401", L4, run_mutants=False)
        self.assertEqual(rep.check_results["fx.algebra.dimension"], "fail")
        self.assertFalse(evidence.has_assertion("def f(:\n", "f"))
