"""one-relation.two-presentations: exact checks (GA.py with Gaussian-rational coefficients, GA.QI).

Orthogonal bases e_a of Cl(1,1), Cl(1,3) and Cl(2,4) (GA.py order: squares +1 first, then -1). Witt bases of
the complexification: real null pairs w = (e_a + e_b)/2, wbar = (e_a - e_b)/2 for e_a^2 = 1, e_b^2 = -1, and
on a negative-definite block (e, e') the complex pair w = (e + i e')/2, wbar = -(e - i e')/2.
(1) The orthogonal reading: {e_a, e_b} = 2 g_ab on all pairs.
(2) The Witt reading: {w_i, w_j} = 0, {wbar_i, wbar_j} = 0, {w_i, wbar_j} = delta_ij for all i, j, with
    1, 2, 3 pairs in Cl(1,1), Cl(1,3)_C, Cl(2,4)_C (the boost-plane pair real, the anisotropic-kernel pair
    complex); the cross pairing is 1/2 delta_ij; the change of basis from (e_a) to (w_i, wbar_i) is
    invertible over Q(i) (rank d).
(3) The Fock module: Omega = wbar_1 ... wbar_r is nonzero, killed by every wbar_j; the span of
    w_K Omega over subsets K has dimension 2^r over Q(i) (2, 4, 8) and is closed under left multiplication
    by every generator; the vectors v with v Omega = 0 form a space of dimension r (the vacuum's
    annihilator is the isotropic W-bar).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

QI = GA.QI
CASES = [((1, 1), [(0, 1)], []), ((1, 3), [(0, 1)], [(2, 3)]), ((2, 4), [(0, 2), (1, 3)], [(4, 5)])]


def cs(c, x):
    return {b: c * v for b, v in x.items() if c * v != 0}


def cadd(*xs):
    out = {}
    for x in xs:
        for b, v in x.items():
            out[b] = out.get(b, QI(0)) + v
    return {b: v for b, v in out.items() if v != 0}


def g(i):
    return {(i,): QI(1)}


def anti(x, y, S):
    return cadd(GA.mul(x, y, S), GA.mul(y, x, S))


def is_scalar(x, val):
    val = QI(val)
    if val == 0:
        return x == {}
    return set(x) == {()} and x[()] == val


def witt_pairs(real, cplx):
    pairs = []
    half = QI(F(1, 2))
    for a, b in real:
        pairs.append((cs(half, cadd(g(a), g(b))), cs(half, cadd(g(a), cs(QI(-1), g(b))))))
    for a, b in cplx:
        pairs.append((cs(half, cadd(g(a), cs(QI(0, 1), g(b)))), cs(QI(F(-1, 2)), cadd(g(a), cs(QI(0, -1), g(b))))))
    return pairs


def cplx_rank(xs, n):
    bl = GA.all_blades(n)
    return GA.field_rank([[x.get(b, QI(0)) for b in bl] for x in xs])


def check_orthogonal_reading_is_the_metric():
    ok = True
    for (p, q), real, cplx in CASES:
        S = GA.sig(p, q)
        n = p + q
        for a in range(n):
            for b in range(n):
                ok = ok and is_scalar(anti(g(a), g(b), S), 2 * S[a] if a == b else 0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_orthogonal_reading_is_the_metric"; return _tp_rv


def check_witt_reading_is_the_car():
    premise("one-relation.imported-pure-spinors-incidence-chart")
    ok = True
    counts = []
    for (p, q), real, cplx in CASES:
        S = GA.sig(p, q)
        n = p + q
        P = witt_pairs(real, cplx)
        r = len(P)
        for i in range(r):
            for j in range(r):
                ok = ok and is_scalar(anti(P[i][0], P[j][0], S), 0) and is_scalar(anti(P[i][1], P[j][1], S), 0)
                ok = ok and is_scalar(anti(P[i][0], P[j][1], S), 1 if i == j else 0)
        vecs = [w for pr in P for w in pr]
        ok = ok and GA.field_rank([[v.get((a,), QI(0)) for a in range(n)] for v in vecs]) == n
        counts.append(r)
    ok = ok and counts == [1, 2, 3]
    _tp_rv = (ok); assert _tp_rv is not False, "check_witt_reading_is_the_car"; return _tp_rv


def check_fock_module_from_the_vacuum():
    premise("one-relation.imported-pure-spinors-incidence-chart")
    ok = True
    dims = []
    for (p, q), real, cplx in CASES:
        S = GA.sig(p, q)
        n = p + q
        P = witt_pairs(real, cplx)
        r = len(P)
        Om = {(): QI(1)}
        for _, wb in P:
            Om = GA.mul(Om, wb, S)
        ok = ok and Om != {} and all(GA.mul(wb, Om, S) == {} for _, wb in P)
        states = []
        for k in range(r + 1):
            for K in combinations(range(r), k):
                x = Om
                for i in reversed(K):
                    x = GA.mul(P[i][0], x, S)
                states.append(x)
        rk = cplx_rank(states, n)
        ok = ok and rk == 2 ** r
        ok = ok and all(cplx_rank(states + [GA.mul(g(a), s, S)], n) == rk for a in range(n) for s in states)
        bl = GA.all_blades(n)
        cols = [[GA.mul(g(a), Om, S).get(b, QI(0)) for b in bl] for a in range(n)]
        ann = GA.field_kernel([list(rw) for rw in zip(*cols)])
        ok = ok and len(ann) == r
        dims.append(rk)
    ok = ok and dims == [2, 4, 8]
    _tp_rv = (ok); assert _tp_rv is not False, "check_fock_module_from_the_vacuum"; return _tp_rv
