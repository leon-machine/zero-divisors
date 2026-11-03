from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def sys2(sq):
    """The 2x2 system of Cl(1,1) inside an algebra whose first two generators square to +1, -1."""
    f = GA.mul(GA.gen(0), GA.gen(1), sq)
    ep = GA.scal(F(1, 2), GA.add(GA.sc(1), f))
    em = GA.scal(F(1, 2), GA.sub(GA.sc(1), f))
    e1 = GA.gen(0)
    return [[ep, GA.mul(ep, e1, sq)], [GA.mul(em, e1, sq), em]]


def sys4(sq):
    """A 4x4 system in Cl(2,2) (generators +, +, -, -): two commuting 2x2 systems."""
    def two(a, b, x):
        f = GA.mul(GA.gen(a), GA.gen(b), sq)
        ep = GA.scal(F(1, 2), GA.add(GA.sc(1), f))
        em = GA.scal(F(1, 2), GA.sub(GA.sc(1), f))
        return [[ep, GA.mul(ep, x, sq)], [GA.mul(em, x, sq), em]]
    A = two(0, 2, GA.gen(0))
    X2 = GA.mul(GA.mul(GA.gen(1), GA.gen(0), sq), GA.gen(2), sq)
    B = two(1, 3, X2)
    E = [[None] * 4 for _ in range(4)]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    E[2 * a + c][2 * b + d] = GA.mul(A[a][b], B[c][d], sq)
    return E


CASES = [((1, 1, 0), sys2), ((1, 1, 1), sys2), ((2, 2, 0), sys4)]


def check_matrix_units_and_isomorphism():
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.blade-basis")
    ok = True
    corner_dims = []
    products = 0
    for (p, q, r), build in CASES:
        sq = GA.sig(p, q, r)
        n = len(sq)
        E = build(sq)
        m = len(E)
        ok = ok and GA.eq(GA.add(*[E[i][i] for i in range(m)]), GA.sc(1))
        for i in range(m):
            for j in range(m):
                for k in range(m):
                    for l in range(m):
                        exp = E[i][l] if j == k else {}
                        ok = ok and GA.eq(GA.mul(E[i][j], E[k][l], sq), exp)
                        products += 1
        corner = [GA.mul(GA.mul(E[0][0], {b: F(1)}, sq), E[0][0], sq) for b in GA.all_blades(n)]
        corner_dims.append(S.span_rank(corner, n))

        def Phi(b):
            return [[GA.mul(GA.mul(E[0][i], b, sq), E[j][0], sq) for j in range(m)] for i in range(m)]

        a, b = S.sample(n, 1), S.sample(n, 2)
        Pa, Pb, Pab = Phi(a), Phi(b), Phi(GA.mul(a, b, sq))
        for i in range(m):
            for j in range(m):
                s = GA.add(*[GA.mul(Pa[i][k], Pb[k][j], sq) for k in range(m)])
                ok = ok and GA.eq(s, Pab[i][j])
        back = GA.add(*[GA.mul(GA.mul(E[i][0], Pa[i][j], sq), E[0][j], sq) for i in range(m) for j in range(m)])
        ok = ok and GA.eq(back, a)
    ok = ok and corner_dims == [1, 2, 1]
    ok = ok and products == 16 + 16 + 256
    GA.check("matrix units in Cl(1,1), Cl(1,1,1), Cl(2,2); corners of dimension 1, 2, 1; Phi multiplicative and inverted", ok)
    return ok
