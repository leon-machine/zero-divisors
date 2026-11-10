"""Release notes say what changed between releases (tp/releases.py)."""
import json
import os
import shutil
import tempfile
import unittest

from tests.fixture_store import build
from tp import releases
from tp.model import load_store, lock_entry


class ReleaseNotesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = build(os.path.join(self.tmp, "store"))
        st = load_store(self.root)
        self.lock = {eid: lock_entry(e) for eid, e in st.entities.items()}

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def edit(self, sub, eid, old, new):
        p = os.path.join(self.root, sub, eid, "entity.md")
        with open(p, encoding="utf-8") as fh:
            s = fh.read()
        self.assertIn(old, s)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(s.replace(old, new, 1))

    def test_nothing_changed(self):
        ch = releases.changes(self.lock, load_store(self.root))
        self.assertFalse(any(ch.values()))
        md = releases.notes("v1.1.0", "2026-12-01", load_store(self.root), ch, "v1.0.0")
        self.assertIn("No results were added, corrected or retired.", md)

    def test_correction_added_and_retired(self):
        self.edit("claims", "fx.boost.sigma", "ai_involved: 'no'\n",
                  "ai_involved: 'no'\namendments:\n- version: 2\n  kind: correction\n"
                  "  defect: the second step divides by a null vector\ncredit:\n"
                  "- name: Ada Lovelace\n  role: correction\n  version: 2\n")
        self.edit("claims", "fx.boost.sigma", "version: 1", "version: 2")
        self.edit("claims", "fx.thermo.entropy-tick", "version: 1", "version: 3")
        lock = dict(self.lock, **{"fx.gone.claim": {"version": 1, "credit": []}})
        del lock["fx.parity.grading"]
        st = load_store(self.root)
        ch = releases.changes(lock, st, {"fx.gone.claim": {"id": "fx.gone.claim", "reason": "a duplicate"}})
        self.assertEqual(ch["added"], ["fx.parity.grading"])
        self.assertEqual([(r["id"], r["version"], r["by"]) for r in ch["corrected"]],
                         [("fx.boost.sigma", 2, ["Ada Lovelace"])])
        self.assertEqual(ch["revised"], [{"id": "fx.thermo.entropy-tick", "from": 1, "to": 3}])
        self.assertEqual(ch["retired"][0]["id"], "fx.gone.claim")
        self.assertIn("Ada Lovelace", ch["contributors"])
        md = releases.notes("v1.1.0", "2026-12-01", st, ch, "v1.0.0")
        for s in ("## Results added", "`fx.parity.grading`", "## Corrections",
                  "the second step divides by a null vector (by Ada Lovelace)",
                  "## Other revisions", "## Results retired", "a duplicate",
                  "## Credited for the first time"):
            self.assertIn(s, md)

    def test_first_release_gives_counts(self):
        md = releases.notes("v1.0.0", "2026-11-10", load_store(self.root))
        self.assertIn("The first release of the Physics Graph", md)
        self.assertNotIn("## Results added", md)

    def test_zenodo_contributors(self):
        self.edit("claims", "fx.boost.sigma", "ai_involved: 'no'\n",
                  "ai_involved: 'no'\ncredit:\n- name: Leon Butler\n  role: idea\n"
                  "- name: Ada Lovelace\n  role: correction\n  version: 2\n  orcid: 0000-0002-1825-0097\n"
                  "- name: Claude Opus 5.5\n  role: drafting\n  version: 2\n"
                  "- name: GPT-5\n  role: drafting\n"
                  "- name: Claude Shannon\n  role: review\n  kind: person\n"
                  "- name: Ludwig van Beethoven\n  role: review\n")
        path = os.path.join(self.tmp, ".zenodo.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"title": "t", "creators": [{"name": "Butler, Leon"}],
                       "contributors": [{"name": "Noether, Emmy", "type": "Other"}]}, fh)
        st = load_store(self.root)
        added = releases.update_zenodo(self.tmp, st)
        self.assertEqual(added, ["Lovelace, Ada", "Shannon, Claude", "Ludwig van Beethoven"])
        with open(path, encoding="utf-8") as fh:
            meta = json.load(fh)
        self.assertEqual(meta["title"], "t")
        self.assertEqual(meta["contributors"], [
            {"name": "Noether, Emmy", "type": "Other"},
            {"name": "Lovelace, Ada", "type": "Researcher", "orcid": "0000-0002-1825-0097"},
            {"name": "Shannon, Claude", "type": "Researcher"},
            {"name": "Ludwig van Beethoven", "type": "Researcher"}])
        self.assertEqual(releases.update_zenodo(self.tmp, st), [])
        self.assertIsNone(releases.update_zenodo(os.path.join(self.tmp, "nowhere"), st))

    def test_is_model(self):
        for n in ("Claude Opus 5.5", "Claude Fable 5", "Claude (model not recorded)", "GPT-5",
                  "o3", "Gemini 3 Pro", "DeepSeek-R1", "Grok 4"):
            self.assertTrue(releases.is_model({"name": n}), n)
        for n in ("Ada Lovelace", "Claude Monet", "Grokhov Petr", "Olga Ivanova"):
            self.assertFalse(releases.is_model({"name": n}), n)
        self.assertFalse(releases.is_model({"name": "Claude Opus", "kind": "person"}))
        self.assertTrue(releases.is_model({"name": "Sage", "kind": "ai"}))

    def test_tag_order(self):
        self.assertGreater(releases.tag_key("v1.10.0"), releases.tag_key("v1.9.3"))


if __name__ == "__main__":
    unittest.main()
