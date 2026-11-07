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

    def test_bare_imaginary_unit_is_found(self):
        for t in ("$e^{i\\theta}$", "$\\Delta^{it}$", "$x = a + ib$", "$\\pm i$", "$\\alpha_{i\\beta}(x)$",
                  "$(x + i0)^{-1}$", "$e^{-iHt}$", "$W = i$", "$\\exp(it K)$", "$2\\pi i$", "$(3+4i)/5$", "$(x - i)^{-1}$"):
            self.assertEqual(galang.scan(ent(t)), ["a bare imaginary unit"], t)

    def test_index_letters_and_pseudoscalars_pass(self):
        for t in ("$e_i e_j$", "$\\sum_i x_i$", "$i = 1, \\dots, n$", "clause (i) holds", "$R^{i0}$",
                  "$B^{il}_{\\Lambda}$", "$g^{ij}$", "$\\bar Z_{i\\alpha}$", "$S \\setminus i$", "$i \\notin K$",
                  "$\\ket{i}$", "$i^{+}$", "$p = (i, A)$", "$(-1)^{n-i}$", "$C_{0i}{}^{0i}$", "$i - 1$",
                  "$l \\ne i$", "$s = i/300$", "$\\mathbf{i} = e_3 e_2$", "$\\omega^{i\\,a}$",
                  "$e^{I_{4}\\theta}$", "$\\psi I_{6}$", "$e^{-I_{4}k\\cdot x}$", "$i^{\\mp}$",
                  "$(i+1)(d-1-i) - i(d-i)$", "$e_{k-i}$"):
            self.assertEqual(galang.scan(ent(t)), [], t)

    def test_a_declaration_does_not_excuse_a_bare_unit(self):
        decl = {"outside_ga": {"kind": "complex-analysis", "why": "a contour argument stated as in the source"}}
        self.assertEqual(galang.unexcused(ent("$e^{i\\theta}$ and the Pauli matrices", meta=decl)),
                         ["a bare imaginary unit"])
        self.assertEqual(galang.unexcused(ent("the Pauli matrices", meta=decl)), [])
        self.assertEqual(galang.unexcused(ent("$e^{I_{4}\\theta}$")), [])

    def test_declaration(self):
        self.assertTrue(galang.declared(ent(meta={"outside_ga": {"kind": "imported", "why": "stated as in the source"}})))
        self.assertFalse(galang.declared(ent(meta={"outside_ga": {"kind": "whim", "why": "x"}})))


if __name__ == "__main__":
    unittest.main()
