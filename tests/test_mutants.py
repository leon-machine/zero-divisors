"""tp mutants: the mutation half of layer 4 for one entity, with surviving literals located."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

from tests import fixture_store
from tp import evidence, mutants

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class MutantsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="mutants-test-")
        cls.store = os.path.join(cls.tmp, "store")
        fixture_store.build(cls.store)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def run_tp(self, *args):
        return subprocess.run([sys.executable, "-m", "tp", "mutants", *args, "--store", self.store],
                              capture_output=True, text=True, cwd=ROOT)

    def test_literals_match_the_mutator(self):
        src = "def check_a():\n    x = [1, 2, 3]\n    assert sum(x) == 6\n    return True\n"
        found = mutants.literals(src, "check_a")
        self.assertEqual(len(found), evidence.int_literal_count(src, "check_a"))
        self.assertEqual([v for _, _, v in found], [1, 2, 3, 6])
        self.assertEqual(found[3][0], 3)                   # line of the asserted value

    def test_sampling_matches_the_full_check(self):
        self.assertEqual(mutants.sampled(5), [0, 1, 2, 3, 4])
        self.assertEqual(mutants.sampled(22), sorted({round(i * 21 / 7) for i in range(8)}))
        self.assertEqual(len(mutants.sampled(100)), 8)

    def test_fixture_entity_reports_survivors_with_lines(self):
        r = self.run_tp("fx.null.square-zero", "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        res = json.loads(r.stdout)[0]
        f = res["functions"][0]
        self.assertEqual(f["tried"], len(f["rows"]))
        self.assertEqual(f["survived"], sum(row["survived"] for row in f["rows"]))
        self.assertTrue(all(row["line"] > 0 and row["text"] for row in f["rows"]))
        self.assertTrue(all(row["killed_by"] for row in f["rows"] if not row["survived"]))
        self.assertTrue(all(row["sampled"] for row in f["rows"]))
        self.assertEqual(f["verdict"], "ok")

    def test_a_check_that_pins_nothing_is_e408(self):
        folder = os.path.join(self.store, "claims", "fx.null.square-zero")
        path = os.path.join(folder, "check.py")
        with open(path, encoding="utf-8") as fh:
            orig = fh.read()
        func = mutants.wired_functions(__import__("tp.model", fromlist=["load_entity"])
                                       .load_entity(folder))[0][1]
        weak = orig + f"\n\ndef {func}():\n    n = 1 + 2\n    assert n == n\n    return True\n"
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(weak)
            r = self.run_tp("fx.null.square-zero", "--json")
            self.assertEqual(r.returncode, 1)
            self.assertEqual(json.loads(r.stdout)[0]["functions"][0]["verdict"], "E408")
        finally:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(orig)

    def test_a_failing_check_is_e406_not_ok(self):
        folder = os.path.join(self.store, "claims", "fx.null.square-zero")
        path = os.path.join(folder, "check.py")
        with open(path, encoding="utf-8") as fh:
            orig = fh.read()
        func = mutants.wired_functions(__import__("tp.model", fromlist=["load_entity"])
                                       .load_entity(folder))[0][1]
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(orig + f"\n\ndef {func}():\n    assert 1 == 2\n    return True\n")
            r = self.run_tp("fx.null.square-zero", "--json")
            self.assertEqual(r.returncode, 1)
            self.assertEqual(json.loads(r.stdout)[0]["functions"][0]["verdict"], "E406")
        finally:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(orig)


if __name__ == "__main__":
    unittest.main()
