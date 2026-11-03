"""Every entity says who did what, and names a model only on evidence (tp/credit.py)."""
import glob
import os
import unittest

import yaml

from tp import credit

LAB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CreditTest(unittest.TestCase):
    def test_deposited_paper_names_its_disclosed_model(self):
        c = credit.for_paper("T05", LAB)
        self.assertEqual(c[0]["name"], credit.AUTHOR)
        self.assertEqual(c[1]["name"], "Claude Fable 5")
        self.assertIn("deposited version", c[1]["source"])

    def test_no_model_without_evidence(self):
        c = credit.for_paper("QG notes", LAB)
        self.assertEqual(c[1]["name"], credit.UNRECORDED)
        self.assertNotIn("source", c[1])

    def test_every_entity_carries_credit(self):
        for path in glob.glob(os.path.join(LAB, "store", "*", "*", "entity.md")):
            with open(path, encoding="utf-8") as fh:
                meta = yaml.safe_load(fh.read().split("---")[1]) or {}
            cr = meta.get("credit") or []
            self.assertTrue(cr, path)
            for c in cr:
                self.assertTrue(c.get("name") and c.get("role"), path)
                named = c["name"].startswith("Claude ") and c["name"] != credit.UNRECORDED
                if named and meta.get("proposed_by", {}).get("kind") != "human":
                    self.assertTrue(c.get("source"), f"{path}: a model named without a source")


if __name__ == "__main__":
    unittest.main()
