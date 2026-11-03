"""tower.ladder-pairs-satisfy-car-vectors: exact checks.

Floor T_k = Cl(p+k, q+k) in GA.py's blade engine with the tower layout (ground generators first,
then plane j as e_j (square +1), f_j (square -1)); the normalised null pair of plane j is
v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2. For every ground (p,q) with n <= 3 and every k <= 3:
(1) the CAR hold as vector identities: v_i v_j + v_j v_i = 0, w_i w_j + w_j w_i = 0,
    v_i w_j + w_j v_i = delta_ij, for all i, j <= k; the inputs behind them are computed too:
    Q(v_i) = Q(w_i) = 0, <v_i, w_i> = 1/2, vectors of distinct planes orthogonal;
(2) adding a rung: in T_{k+1} the new pair anticommutes with every ground generator and every
    generator of the earlier planes (it is orthogonal to them), and every relation among the first
    k pairs, recomputed in T_{k+1}, gives the same element as in T_k.
No representation is used: every relation is a product of multivectors.
"""
from fractions import Fraction as F

import GA

GROUNDS = [(p, n - p) for n in range(4) for p in range(n + 1)]
KMAX = 3


def floor(p, q, k):
    return tuple([1] * p + [-1] * q + [1, -1] * k)


def pairs(n, k):
    vs, ws = [], []
    for j in range(k):
        e, f = GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1)
        vs.append(GA.scal(F(1, 2), GA.add(e, f)))
        ws.append(GA.scal(F(1, 2), GA.sub(e, f)))
    return vs, ws


def anti(a, b, S):
    return GA.add(GA.mul(a, b, S), GA.mul(b, a, S))


def check_car_as_vectors():
    for p, q in GROUNDS:
        n = p + q
        for k in range(1, KMAX + 1):
            S = floor(p, q, k)
            vs, ws = pairs(n, k)
            for i in range(k):
                assert GA.dot(vs[i], vs[i], S) == 0 and GA.dot(ws[i], ws[i], S) == 0
                assert GA.dot(vs[i], ws[i], S) == F(1, 2)
                for j in range(k):
                    assert GA.is_zero(anti(vs[i], vs[j], S))
                    assert GA.is_zero(anti(ws[i], ws[j], S))
                    want = GA.sc(1) if i == j else {}
                    assert GA.eq(anti(vs[i], ws[j], S), want), ((p, q), k, i, j)
                    if i != j:
                        for a in (vs[i], ws[i]):
                            for b in (vs[j], ws[j]):
                                assert GA.dot(a, b, S) == 0
    return True


def check_new_rung_touches_nothing():
    for p, q in GROUNDS:
        n = p + q
        for k in range(KMAX):
            S, S1 = floor(p, q, k), floor(p, q, k + 1)
            vs, ws = pairs(n, k)
            vs1, ws1 = pairs(n, k + 1)
            vn, wn = vs1[k], ws1[k]
            earlier = [GA.gen(i) for i in range(n + 2 * k)]
            for g in earlier:
                assert GA.is_zero(anti(vn, g, S1)) and GA.is_zero(anti(wn, g, S1))
            assert GA.eq(anti(vn, wn, S1), GA.sc(1))
            for i in range(k):
                for j in range(k):
                    for a, b in ((vs[i], vs[j]), (ws[i], ws[j]), (vs[i], ws[j])):
                        assert GA.eq(anti(a, b, S), anti(a, b, S1))
    return True
