"""The language of the graph is geometric algebra (tp/galang.py)."""
import unittest
from types import SimpleNamespace as NS

from tp import galang


def ent(formal="", proofs=None, meta=None):
    return NS(levels={"formal": formal}, proofs=proofs or {}, meta=meta or {})


class GaLanguageTest(unittest.TestCase):
    def test_stand_ins_are_found(self):
        self.assertEqual(galang.scan(ent("the Pauli matrices")), ["Pauli matrices"])
        self.assertEqual(galang.scan(ent("", {"p.tex": "the Dirac gamma matrices"})), ["Dirac matrices"])
        self.assertEqual(galang.scan(ent("$\\mathbf{a} \\times \\mathbf{b}$")), ["a cross product"])
        self.assertEqual(galang.scan(ent("$z \\in \\mathbb{C}$")), ["the complex field"])

    def test_geometric_algebra_and_ordinary_maths_pass(self):
        for t in ("$e_1 e_2 e_1 e_2 = -1$", "the Fermi-Dirac matrix", "a Dirac mass matrix $M$",
                  "$[R_i, R_j] = \\epsilon_{ijk} R_k$", "$F = F^{\\mu\\nu}\\gamma_\\mu\\gamma_\\nu$",
                  "the Gram matrix $\\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}$", "$3 \\times 4 = 12$"):
            self.assertEqual(galang.scan(ent(t)), [], t)

    def test_declaration(self):
        self.assertTrue(galang.declared(ent(meta={"outside_ga": {"kind": "imported", "why": "stated as in the source"}})))
        self.assertFalse(galang.declared(ent(meta={"outside_ga": {"kind": "whim", "why": "x"}})))


if __name__ == "__main__":
    unittest.main()
