"""The structured edit commands (tp bump, note, wire-check, restate, sign) and
tp accept --update, on a temporary copy of the fixture store.

Run:  python3 -m unittest discover -s tests -t .
"""
import contextlib
import io
import json
import os
import shutil
import tempfile
import unittest

import yaml

from tests.fixture_store import build
from tp import edit
from tp.__main__ import main as tp_main
from tp.model import load_store, parse_entity_text, write_lock

E = os.path.join
LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# a frozen copy of a real entity (singularity.unipotent-ray at version 2), so later edits to the
# store do not change what these tests compare against
REAL = E(LAB, "tests", "data", "realstyle", "singularity.unipotent-ray")


class EditCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(E(self.tmp, "store"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def folder(self, eid):
        return edit.find_folder(self.root, eid)

    def text(self, eid):
        with open(E(self.folder(eid), "entity.md"), newline="") as fh:
            return fh.read()

    @staticmethod
    def read(path):
        with open(path) as fh:
            return fh.read()

    def meta(self, eid):
        return parse_entity_text(self.text(eid))[0]

    def levels(self, eid):
        return parse_entity_text(self.text(eid))[1]

    def run_tp(self, *argv, store=True):
        argv = list(argv) + (["--store", self.root] if store else [])
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = tp_main(argv)
        return rc, buf.getvalue()

    def ok(self, *argv):
        rc, out = self.run_tp(*argv)
        self.assertEqual(rc, 0, out)
        self.assertEqual(len(out.strip().splitlines()), 1, out)
        return out

    def refused(self, *argv):
        rc, out = self.run_tp(*argv)
        self.assertEqual(rc, 1, out)
        return out

    def assertKeepsOtherLines(self, old, new, changed_at_most):
        """Every line of old survives in new, except at most n of them."""
        o, n = old.splitlines(), set(new.splitlines())
        lost = [ln for ln in o if ln not in n]
        self.assertLessEqual(len(lost), changed_at_most, lost)


class Bump(EditCase):
    ID = "fx.null.square-zero"

    def test_bump_twice_same_day(self):
        old = self.text(self.ID)
        out = self.ok("bump", self.ID, "--note", "First change", "--date", "2026-10-23")
        self.assertIn("version 1 -> 2", out)
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 2)
        n = m["extraction"]["maintainer_pass"]
        self.assertEqual(n["by"], "maintainer-2026-10-23")
        self.assertEqual(n["date"], "2026-10-23")
        self.assertEqual(n["note"], "First change. Version 1 -> 2.")
        self.assertIn("date: '2026-10-23'", self.text(self.ID))
        self.assertKeepsOtherLines(old, self.text(self.ID), 1)   # only the version line
        self.assertEqual(self.levels(self.ID), parse_entity_text(old)[1])
        out = self.ok("bump", self.ID, "--note", "Second change.", "--date", "2026-10-23")
        self.assertIn("version 2 kept", out)
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 2)
        self.assertEqual(list(m["extraction"]), ["maintainer_pass"])
        self.assertEqual(m["extraction"]["maintainer_pass"]["note"],
                         "First change. Version 1 -> 2. Second change.")

    def test_bump_on_a_new_day(self):
        self.ok("bump", self.ID, "--note", "Day one", "--date", "2026-10-23")
        self.ok("bump", self.ID, "--note", "Day two", "--date", "2026-10-24",
                "--by", "maintainer-2026-10-24-x")
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 3)
        self.assertEqual(list(m["extraction"]), ["maintainer_pass_2", "maintainer_pass"])
        self.assertEqual(m["extraction"]["maintainer_pass_2"],
                         {"by": "maintainer-2026-10-24-x", "date": "2026-10-24",
                          "note": "Day two. Version 2 -> 3."})

    def test_quotes_and_house_style(self):
        self.ok("bump", self.ID, "--note", "It's a test: a # b", "--date", "2026-10-23")
        self.assertEqual(self.meta(self.ID)["extraction"]["maintainer_pass"]["note"],
                         "It's a test: a # b. Version 1 -> 2.")
        before = self.text(self.ID)
        self.refused("bump", self.ID, "--note", "bad — dash", "--date", "2026-10-23")
        self.refused("bump", self.ID, "--note", "to be honest", "--date", "2026-10-23")
        self.assertEqual(self.text(self.ID), before)

    def test_note_keeps_version_then_bump_still_bumps(self):
        out = self.ok("note", self.ID, "Typing pass", "--date", "2026-10-23")
        self.assertIn("version 1 kept", out)
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 1)
        self.assertEqual(m["extraction"]["maintainer_pass"]["note"],
                         "Typing pass. Version kept at 1.")
        # a note-only entry does not count as today's change: the next bump bumps
        self.ok("bump", self.ID, "--note", "Real change", "--date", "2026-10-23")
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 2)
        self.assertEqual(m["extraction"]["maintainer_pass"]["note"],
                         "Typing pass. Version kept at 1. Real change. Version 1 -> 2.")
        self.ok("note", self.ID, "Afterthought", "--date", "2026-10-23")
        self.assertEqual(self.meta(self.ID)["version"], 2)

    def test_unknown_id_refused(self):
        self.refused("bump", "fx.no.such", "--note", "x")


class LockRule(EditCase):
    """With a lock, "already bumped" means version > the locked version: one bump per
    session between locks, whatever the dates."""
    ID = "fx.null.square-zero"

    def setUp(self):
        super().setUp()
        write_lock(load_store(self.root))

    def test_session_spanning_midnight_bumps_once(self):
        out = self.ok("bump", self.ID, "--note", "Evening", "--date", "2026-10-23")
        self.assertIn("version 1 -> 2", out)
        out = self.ok("bump", self.ID, "--note", "After midnight", "--date", "2026-10-24")
        self.assertIn("version 2 kept (already changed since the lock (version 1))", out)
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 2)
        self.assertEqual(m["extraction"]["maintainer_pass_2"]["note"], "After midnight.")
        self.assertEqual(m["extraction"]["maintainer_pass"]["note"], "Evening. Version 1 -> 2.")

    def test_new_lock_allows_a_new_bump_the_same_day(self):
        self.ok("bump", self.ID, "--note", "First", "--date", "2026-10-23")
        write_lock(load_store(self.root))          # the maintainer accepts version 2
        out = self.ok("bump", self.ID, "--note", "Second", "--date", "2026-10-23")
        self.assertIn("version 2 -> 3", out)
        self.assertEqual(self.meta(self.ID)["extraction"]["maintainer_pass"]["note"],
                         "First. Version 1 -> 2. Second. Version 2 -> 3.")

    def test_lock_overrides_a_dated_note(self):
        # a note dated today does not stop the bump when the version equals the lock's
        self.ok("note", "fx.witt.car", "Typing pass", "--date", "2026-10-23")
        p = E(self.folder("fx.witt.car"), "entity.md")
        with open(p) as fh:
            t = fh.read()
        with open(p, "w") as fh:
            fh.write(t.replace("Version kept at 1.", "Reviewed."))
        out = self.ok("bump", "fx.witt.car", "--note", "Change", "--date", "2026-10-23")
        self.assertIn("version 1 -> 2", out)

    def test_wire_check_and_restate_follow_the_lock(self):
        self.ok("bump", self.ID, "--note", "First", "--date", "2026-10-23")
        with open(E(self.folder(self.ID), "check.py"), "w") as fh:
            fh.write("import GA as g\n\n\ndef check_one():\n    assert True\n")
        out = self.ok("wire-check", self.ID, "--date", "2026-10-25")
        self.assertIn("version 2 kept", out)
        self.assertEqual(self.meta(self.ID)["version"], 2)

    def test_signoff_still_forces_a_bump(self):
        self.ok("bump", self.ID, "--note", "First", "--date", "2026-10-23")
        self.ok("sign", self.ID, "--level", "human-read", "--date", "2026-10-23")
        out = self.ok("bump", self.ID, "--note", "Second", "--date", "2026-10-23")
        self.assertIn("version 2 -> 3, trust human-read -> ai-proposed", out)

    def test_entity_missing_from_lock_uses_the_date_rule(self):
        p = E(self.root, ".tp-lock.json")
        with open(p) as fh:
            lock = json.load(fh)
        del lock[self.ID]
        with open(p, "w") as fh:
            json.dump(lock, fh)
        self.ok("bump", self.ID, "--note", "Day one", "--date", "2026-10-23")
        out = self.ok("bump", self.ID, "--note", "Day two", "--date", "2026-10-24")
        self.assertIn("version 2 -> 3", out)
        out = self.ok("bump", self.ID, "--note", "Same day", "--date", "2026-10-24")
        self.assertIn("version 3 kept (already changed today)", out)


class RealStyle(EditCase):
    """An entity written the way the store writes them: extraction block, quoted dates,
    multi-line notes. Everything not edited stays byte for byte."""
    ID = "singularity.unipotent-ray"

    def setUp(self):
        super().setUp()
        if not os.path.isdir(REAL):
            self.skipTest("the real store is not beside the tests")
        shutil.copytree(REAL, E(self.root, "claims", self.ID))

    def test_same_day_appends_to_todays_note_only(self):
        old = self.text(self.ID)
        self.ok("bump", self.ID, "--note", "Another sentence", "--date", "2026-10-23")
        new = self.text(self.ID)
        ol, nl = old.splitlines(True), new.splitlines(True)
        self.assertEqual(len(ol), len(nl))
        diff = [i for i, (a, b) in enumerate(zip(ol, nl)) if a != b]
        self.assertEqual(len(diff), 1)
        self.assertTrue(nl[diff[0]].startswith("    note: 'Own exact check added"))
        self.assertTrue(nl[diff[0]].rstrip().endswith("Version 1 -> 2. Another sentence.'"))
        self.assertEqual(self.meta(self.ID)["version"], 2)

    def test_new_day_inserts_at_top_of_extraction(self):
        old = self.text(self.ID)
        self.ok("bump", self.ID, "--note", "Later", "--date", "2026-11-01")
        new = self.text(self.ID)
        self.assertEqual(self.meta(self.ID)["version"], 3)
        self.assertIn("extraction:\n  maintainer_pass:\n    by: maintainer-2026-11-01\n"
                      "    date: '2026-11-01'\n    note: 'Later. Version 2 -> 3.'\n"
                      "  maintainer_pass_tests:\n", new)
        self.assertEqual(new.replace("version: 3", "version: 2", 1).replace(
            "  maintainer_pass:\n    by: maintainer-2026-11-01\n    date: '2026-11-01'\n"
            "    note: 'Later. Version 2 -> 3.'\n", ""), old)

    def test_sign_inserts_trust_after_review(self):
        self.ok("sign", self.ID, "--level", "human-read", "--date", "2026-10-23")
        new = self.text(self.ID)
        self.assertIn("review: typed\ntrust: human-read\nsignoffs:\n- by: leon\n"
                      "  date: '2026-10-23'\n  version: 2\n  level: human-read\nderivations:",
                      new)


class WireCheck(EditCase):
    ID = "fx.null.square-zero"

    def write_check(self, eid, names):
        body = "import GA as g\n\n\ndef helper():\n    return 1\n"
        for n in names:
            body += f"\n\ndef {n}():\n    assert helper() == 1\n"
        with open(E(self.folder(eid), "check.py"), "w") as fh:
            fh.write(body)

    def refs(self, eid):
        return [(e["kind"], e.get("ref") or e.get("derivation"))
                for e in self.meta(eid)["checked_by"]]

    def test_add_and_remove(self):
        self.write_check(self.ID, ["check_square_zero", "check_nonzero"])
        out = self.ok("wire-check", self.ID, "--date", "2026-10-23")
        self.assertIn("+2 -1", out)
        self.assertEqual(self.refs(self.ID), [("check", "check.py::check_square_zero"),
                                              ("check", "check.py::check_nonzero")])
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 2)
        self.assertIn("Check entries synced with check.py: +2, -1",
                      m["extraction"]["maintainer_pass"]["note"])
        # unchanged: nothing written
        before = self.text(self.ID)
        out = self.ok("wire-check", self.ID, "--date", "2026-10-23")
        self.assertIn("no change", out)
        self.assertEqual(self.text(self.ID), before)
        # remove one, same day: version kept, note extended
        self.write_check(self.ID, ["check_nonzero"])
        self.ok("wire-check", self.ID, "--date", "2026-10-23")
        self.assertEqual(self.refs(self.ID), [("check", "check.py::check_nonzero")])
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 2)
        self.assertIn("+0, -1 (removed check_square_zero)",
                      m["extraction"]["maintainer_pass"]["note"])

    def test_keeps_proof_entries_first(self):
        eid = "fx.parity.even"
        self.write_check(eid, ["check_even", "test_also"])
        self.ok("wire-check", eid, "--date", "2026-10-23")
        self.assertEqual(self.refs(eid), [("proof", "direct"),
                                          ("check", "check.py::check_even"),
                                          ("check", "check.py::test_also")])

    def test_helper_called_by_a_check_is_not_wired(self):
        with open(E(self.folder(self.ID), "check.py"), "w") as fh:
            fh.write("import GA as g\n\n\ndef check_part():\n    assert True\n    return True\n"
                     "\n\ndef check_whole():\n    assert check_part()\n\n\n"
                     "def run():\n    return check_part() and check_whole()\n")
        self.ok("wire-check", self.ID, "--date", "2026-10-23")
        self.assertEqual(self.refs(self.ID), [("check", "check.py::check_whole")])

    def test_no_check_file_refused(self):
        self.refused("wire-check", "fx.thermo.two-state")


class Restate(EditCase):
    ID = "fx.algebra.dimension"

    def src(self, text):
        p = E(self.tmp, "new.tex")
        with open(p, "w") as fh:
            fh.write(text)
        return p

    def test_formal(self):
        old = self.text(self.ID)
        lv = self.levels(self.ID)
        self.ok("restate", self.ID, "--level", "formal", "--from",
                self.src("$\\dim \\Cl(1,1) = 2^2 = 4$.\n\nA second paragraph.\n"),
                "--note", "Stated as a power of two", "--date", "2026-10-23")
        new_lv = self.levels(self.ID)
        self.assertEqual(new_lv["formal"], "$\\dim \\Cl(1,1) = 2^2 = 4$.\n\nA second paragraph.")
        for k in ("technical", "lay", "one-liner"):
            self.assertEqual(new_lv[k], lv[k])
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 2)
        self.assertEqual(m["extraction"]["maintainer_pass"]["note"],
                         "The formal level restated: Stated as a power of two. Version 1 -> 2.")
        # the other sections are byte-identical
        self.assertEqual(old.split("## technical", 1)[1], self.text(self.ID).split("## technical", 1)[1])

    def test_title(self):
        self.ok("restate", self.ID, "--level", "title", "--from",
                self.src("Cl(1,1): dimension four\n"), "--note", "Shorter", "--date", "2026-10-23")
        self.assertEqual(self.meta(self.ID)["title"], "Cl(1,1): dimension four")

    def test_bad_text_restores_file(self):
        before = self.text(self.ID)
        out = self.refused("restate", self.ID, "--level", "formal", "--from",
                           self.src("Dimension — four."), "--note", "x", "--date", "2026-10-23")
        self.assertIn("E112", out)
        self.assertEqual(self.text(self.ID), before)
        out = self.refused("restate", self.ID, "--level", "lay", "--from",
                           self.src("Uses \\undeclaredmacro here."), "--note", "x")
        self.assertIn("E111", out)
        self.assertEqual(self.text(self.ID), before)


class Sign(EditCase):
    ID = "fx.witt.car"

    def test_sign_raises_trust(self):
        before = self.meta(self.ID)
        out = self.ok("sign", self.ID, "--level", "human-read", "--date", "2026-10-23")
        self.assertIn("trust unset -> human-read", out)
        m = self.meta(self.ID)
        self.assertEqual(m["trust"], "human-read")
        self.assertEqual(m["version"], before["version"])
        self.assertEqual(m["signoffs"], [{"by": "leon", "date": "2026-10-23", "version": 1,
                                          "level": "human-read"}])
        self.ok("sign", self.ID, "--level", "human-checked", "--note", "Checked the CAR by hand",
                "--date", "2026-10-24")
        m = self.meta(self.ID)
        self.assertEqual(m["trust"], "human-checked")
        self.assertEqual(len(m["signoffs"]), 2)
        self.assertEqual(m["signoffs"][1]["note"], "Checked the CAR by hand")
        # a later human-read on the same version does not lower it
        self.ok("sign", self.ID, "--level", "human-read", "--date", "2026-10-25")
        self.assertEqual(self.meta(self.ID)["trust"], "human-checked")

    def test_older_version_signoff_does_not_raise(self):
        self.ok("sign", self.ID, "--level", "human-checked", "--date", "2026-10-23")
        # the bump voids the version-1 sign-off: trust falls to the floor (E120 otherwise)
        out = self.ok("bump", self.ID, "--note", "Changed", "--date", "2026-10-24")
        self.assertIn("trust human-checked -> ai-proposed", out)
        m = self.meta(self.ID)
        self.assertEqual(m["trust"], "ai-proposed")
        self.assertIn("Trust lowered from human-checked to ai-proposed",
                      m["extraction"]["maintainer_pass"]["note"])
        out = self.ok("sign", self.ID, "--level", "human-read", "--date", "2026-10-24")
        m = self.meta(self.ID)
        self.assertEqual(m["version"], 2)
        self.assertEqual(m["trust"], "human-read")
        self.assertIn("ai-proposed -> human-read", out)
        self.assertEqual([s["version"] for s in m["signoffs"]], [1, 2])


    def test_change_after_todays_signoff_bumps_again(self):
        self.ok("bump", self.ID, "--note", "Morning change", "--date", "2026-10-23")
        self.ok("sign", self.ID, "--level", "human-read", "--date", "2026-10-23")
        out = self.ok("bump", self.ID, "--note", "Afternoon change", "--date", "2026-10-23")
        self.assertIn("version 2 -> 3, trust human-read -> ai-proposed", out)
        self.ok("note", self.ID, "Typo", "--date", "2026-10-23")
        m = self.meta(self.ID)
        self.assertEqual(m["extraction"]["maintainer_pass"]["note"],
                         "Morning change. Version 1 -> 2. Afternoon change. Version 2 -> 3. "
                         "Trust lowered from human-read to ai-proposed: the sign-offs are for "
                         "version 2. Typo.")

    def test_signoff_of_older_version_in_file_is_ignored(self):
        p = E(self.folder(self.ID), "entity.md")
        t = self.text(self.ID).replace("version: 1", "version: 3", 1).replace(
            "ai_involved: 'no'\n", "ai_involved: 'no'\nsignoffs:\n- by: leon\n  date: '2026-10-01'\n"
            "  version: 2\n  level: human-checked\n", 1)
        with open(p, "w") as fh:
            fh.write(t)
        self.assertEqual(self.meta(self.ID)["signoffs"][0]["version"], 2)
        out = self.ok("sign", self.ID, "--level", "human-read", "--date", "2026-10-23")
        self.assertEqual(self.meta(self.ID)["trust"], "human-read")
        self.assertIn("unset -> human-read", out)


class AcceptUpdate(EditCase):
    ID = "fx.parity.grading"

    def propose(self, version, formal=None, files=None):
        src = E(self.tmp, "proposals", self.ID)
        os.makedirs(src, exist_ok=True)
        with open(E(src, "proposal.json"), "w") as fh:
            json.dump({"author": "ai", "status": "proposed", "kind": "claim"}, fh)
        text = self.text(self.ID).replace("version: 1", f"version: {version}", 1)
        if formal:
            meta, levels, _ = parse_entity_text(text)
            text = text.replace(levels["formal"], formal, 1)
        with open(E(src, "entity.md"), "w") as fh:
            fh.write(text)
        for name, body in (files or {}).items():
            with open(E(src, name), "w") as fh:
                fh.write(body)
        return src

    def stored_extra(self):
        with open(E(self.folder(self.ID), "orig-proof-main.tex"), "w") as fh:
            fh.write("the original proof\n")

    def test_refuses_without_update_and_equal_version(self):
        self.propose(2)
        self.assertIn("refusing", self.refused("accept", self.ID))
        self.propose(1)
        self.assertIn("not above", self.refused("accept", self.ID, "--update"))

    def test_update_keeps_stored_files(self):
        self.stored_extra()
        src = self.propose(2, formal=r"The $\mathbb{Z}_2$ grading of the mode algebra is "
                                     r"the Clifford grading, by degree mod two.",
                           files={"proof-direct.tex": "Generators are odd; so are their "
                                                      "odd products.\n"})
        out = self.ok("accept", self.ID, "--update")
        self.assertIn("version 1 -> 2", out)
        self.assertIn("orig-proof-main.tex", out)
        f = self.folder(self.ID)
        self.assertEqual(self.meta(self.ID)["version"], 2)
        self.assertIn("by degree mod two", self.levels(self.ID)["formal"])
        self.assertEqual(self.read(E(f, "orig-proof-main.tex")), "the original proof\n")
        self.assertIn("odd products", self.read(E(f, "proof-direct.tex")))
        self.assertFalse(os.path.exists(src))

    def test_update_rolls_back_on_error(self):
        self.stored_extra()
        before = self.text(self.ID)
        proof_before = self.read(E(self.folder(self.ID), "proof-direct.tex"))
        src = self.propose(2, formal="The grading — Clifford.",
                           files={"proof-direct.tex": "changed\n", "extra.txt": "new file\n"})
        out = self.refused("accept", self.ID, "--update")
        self.assertIn("E112", out)
        f = self.folder(self.ID)
        self.assertEqual(self.text(self.ID), before)
        self.assertEqual(self.read(E(f, "proof-direct.tex")), proof_before)
        self.assertFalse(os.path.exists(E(f, "extra.txt")))
        self.assertTrue(os.path.exists(E(f, "orig-proof-main.tex")))
        self.assertTrue(os.path.exists(src))


class BumpLintGuard(unittest.TestCase):
    """tp bump refuses to record a change while the entity's own check fails."""

    def test_guard_refuses_a_failing_check(self):
        import tempfile, shutil
        from tests import fixture_store
        from tp import edit
        tmp = tempfile.mkdtemp(prefix="bump-guard-")
        try:
            store = os.path.join(tmp, "store")
            fixture_store.build(store)
            folder = os.path.join(store, "claims", "fx.null.square-zero")
            edit._lint_before_bump(store, folder)            # passes as built
            with open(os.path.join(folder, "check.py"), "a", encoding="utf-8") as fh:
                fh.write("\n\ndef test_square_zero():\n    assert 1 == 2\n    return True\n")
            with self.assertRaises(edit.Refused):
                edit._lint_before_bump(store, folder)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
