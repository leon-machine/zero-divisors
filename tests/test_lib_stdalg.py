"""Tests for lib/stdalg.py, the helpers of the algebra core's checks."""
import os
import sys
import unittest
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib"))
import GA  # noqa: E402
import stdalg as S  # noqa: E402


class StdAlgTests(unittest.TestCase):
    def test_signatures(self):
        sigs = S.signatures(3)
        self.assertEqual(len(sigs), 3 + 6 + 10)
        self.assertIn((1, 1, 1), sigs)
        self.assertEqual(len(S.signatures(3, degenerate=False)), 2 + 3 + 4)

    def test_outer_and_contraction(self):
        sq = GA.sig(3, 0)
        a, b = S.vec([1, 2, 0]), S.vec([0, 1, 3])
        ab = GA.mul(a, b, sq)
        self.assertTrue(GA.eq(ab, GA.add(S.lc(a, b, sq), S.outer(a, b, sq))))
        self.assertEqual(S.grades(S.outer(a, b, sq)), [2])

    def test_centre(self):
        self.assertEqual(len(S.centre_basis(GA.sig(2, 0))), 1)
        cb = S.centre_basis(GA.sig(3, 0))
        self.assertEqual(len(cb), 2)
        self.assertEqual(S.span_rank(cb + [GA.sc(1), S.pseudoscalar(3)], 3), 2)

    def test_matrix_rep_pauli(self):
        i = GA.QI(0, 1)
        s1 = S.mat([[0, 1], [1, 0]])
        s2 = [[GA.QI(0), -i], [i, GA.QI(0)]]
        s3 = S.mat([[1, 0], [0, -1]])
        self.assertTrue(S.check_matrix_rep([s1, s2, s3], GA.sig(3, 0), 8))
        self.assertFalse(S.check_matrix_rep([s1, s1, s3], GA.sig(3, 0), 8))

    def test_samples_differ_and_vectors_independent(self):
        for n in range(2, 6):
            xs = [S.sample(n, s) for s in range(1, 6)]
            self.assertEqual(len({tuple(sorted(x.items())) for x in xs}), 5)
            self.assertEqual(S.span_rank([S.sample_vec(n, s) for s in range(1, n + 1)], n), n)

    def test_nullspace(self):
        ns = S.nullspace([[1, 1, 0], [0, 0, 1]])
        self.assertEqual(len(ns), 1)
        self.assertEqual(ns[0], [F(-1), F(1), F(0)])

    def test_left_matrix_is_a_representation(self):
        sq = GA.sig(1, 1, 1)
        x, y = S.sample(3, 1), S.sample(3, 2)
        L = S.left_matrix(GA.mul(x, y, sq), sq)
        self.assertEqual(L, GA.mat_mul(S.left_matrix(x, sq), S.left_matrix(y, sq)))


if __name__ == "__main__":
    unittest.main()
