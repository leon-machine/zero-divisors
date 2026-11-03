"""Tests for the page build helpers added in run 2026-10-23-roadmap (A6). Proposed for tests/test_site.py:
    python3 -m unittest tests.test_site   (from the lab root)"""
import os
import tempfile
import unittest
from types import SimpleNamespace

from tp import site


def ent(meta, path="", kind="claim", levels=None):
    return SimpleNamespace(meta=meta, path=path, kind=kind, levels=levels or {}, status=meta.get("status", ""),
                           title=meta.get("title", "t"), version=meta.get("version", 1))


class TestSiteHelpers(unittest.TestCase):
    def test_weak_coverage(self):
        f = lambda *ks: {"functions": {f"check_{i}": {"kind": k} for i, k in enumerate(ks)}}
        self.assertIsNone(site._weak_coverage(None))
        self.assertIsNone(site._weak_coverage(f("exact", "sampled")))
        self.assertIsNone(site._weak_coverage(f("complete")))
        self.assertEqual(site._weak_coverage(f("sampled", "sampled")), "sampled")
        self.assertEqual(site._weak_coverage(f("sampled", "partial")), "partial")
        self.assertIsNone(site._weak_coverage(f(None)))

    def test_coverage_file(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(site._coverage(ent({}, d)))
            with open(os.path.join(d, "coverage.yaml"), "w") as fh:
                fh.write("functions:\n  check_a:\n    kind: sampled\n    clauses: ['(1)']\n    omits: general n\n"
                         "  check_b:\n    kind: bogus\njudge: {by: x, date: '2026-10-23', verdict: overclaims, note: n}\n")
            c = site._coverage(ent({}, d))
            self.assertEqual(c["functions"]["check_a"], {"kind": "sampled", "clauses": ["(1)"], "omits": "general n"})
            self.assertIsNone(c["functions"]["check_b"]["kind"])
            self.assertEqual(c["judge"]["verdict"], "overclaims")
            self.assertEqual(site._weak_coverage(c), "sampled")

    def test_trust(self):
        self.assertEqual(site._trust(ent({"trust": "human-read"})), "human-read")
        self.assertEqual(site._trust(ent({"ai_involved": "unknown"})), "ai-proposed")
        self.assertEqual(site._trust(ent({})), "ai-proposed")
        self.assertIsNone(site._trust(ent({"ai_involved": "no"})))

    def test_programmes_shapes(self):
        self.assertEqual(site._programmes({}), [])
        self.assertEqual([p["id"] for p in site._programmes({"programmes": ["a", "b"]})], ["a", "b"])
        self.assertEqual(site._programmes({"programmes": {"tp": "Transport Papers"}})[0]["title"], "Transport Papers")
        self.assertEqual(site._programmes({"programmes": [{"id": "x", "title": "X"}]})[0], {"id": "x", "title": "X", "about": ""})

    def test_history(self):
        e = ent({"extraction": {"maintainer_pass": {"by": "m", "date": "2026-10-23", "note": "Fixed. Version 3 -> 4."},
                                "maintainer_pass_2026_10_22": {"by": "m2", "note": "x"},
                                "typing": {"by": "t", "note": "no date"}}})
        rows = site._entity_history(e, [["abc1234", "2026-10-21", "a commit"]])
        # commits are not shown: only the recorded passes, newest first
        self.assertEqual([r["date"] for r in rows], ["2026-10-23", "2026-10-22"])
        self.assertEqual(rows[0]["v"], 4)
        self.assertFalse(any(r.get("commit") for r in rows))

    def test_search_index(self):
        x = site._search_index([("n", "a.b", "Hawking Hawking temperature"), ("t", "note.a", "temperature x")])
        self.assertEqual(x["N"], 2)
        self.assertEqual(x["post"]["hawking"], [0, 2])
        self.assertEqual(x["post"]["temperature"], [0, 1, 1, 1])
        self.assertEqual(x["docs"][0], ["n", "a.b", 3])

    def test_data_chunk_names(self):
        self.assertEqual(site._data_chunk_of("dark-matter"), "dark-matter")
        self.assertEqual(site._data_chunk_of(None), "unplaced")
        self.assertEqual(site._data_chunk_of("search"), "subject-search")

    def test_browser_lib_order(self):
        with tempfile.TemporaryDirectory() as d:
            for name, src in {"GA.py": "x = 1\n", "tp_premise.py": "", "gtg.py": "import GA\nimport series\n",
                              "series.py": "import GA\n", "fock.py": "import GA\nd = {}\nd.setdefault(1, 2)\n"}.items():
                with open(os.path.join(d, name), "w") as fh:
                    fh.write(src)
            got = site._browser_lib(d)
            names = [m for m, _ in got]
            self.assertEqual(sorted(names), ["fock", "gtg", "series"])
            self.assertLess(names.index("series"), names.index("gtg"))
            self.assertIn("_tp_setdefault(d, 1, 2)", dict(got)["fock"])

    def test_note_words(self):
        self.assertNotIn("claimref", site._note_words(r"see \claimref{a.b} and \cite[p. 3]{x} \emph{word}"))


if __name__ == "__main__":
    unittest.main()
