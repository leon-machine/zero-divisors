"""mass.chart-form-spin-isomorphism: exact checks.

T11's twistor model (as in mass.imported-flat-model-twistor-chart-infinity): CS = C^4 over Q(i), omega-plane
span(e1, e2) (indices 0, 1), pi-plane span(e3, e4) (indices 2, 3); V_C = Lambda^2 CS with <U, U'> = eps(U ^ U');
n_inf = e1 ^ e2, n0 = e3 ^ e4; x = sum x^{aa'} e_a ^ e_a'. A bivector U ^ V of V_C acts on V_C by
R(W) = <U, W> V - <V, W> U, and A(U ^ V) is the unique traceless 4x4 matrix whose action on Lambda^2 CS,
A . (u ^ v) = Au ^ v + u ^ Av, is R (solved exactly: the action map has rank 15 on gl(4), kernel the scalars).
The expected matrices are built from the displayed formulas with eps_12 = eps_34 = +1:
(1) A(n_inf ^ n0) = diag(-1/2, -1/2, 1/2, 1/2);
(2) A(x ^ n_inf) has only the upper-right block b_x, (b_x pi)^a = x^{aa'} eps_{a'b'} pi^{b'};
(3) A(x ^ n0) has only the lower-left block c_x, (c_x omega)^{a'} = -x^{ba'} eps_{ba} omega^a;
for the four basis x and for real and Gaussian samples (A is linear in x).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

QI = GA.QI
Z0, ONE = QI(0), QI(1)
PAIRS4 = list(combinations(range(4), 2))
XS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 2, -1, 3), (QI(0, 1), F(1, 2), QI(1, 1), -2)]


def q(x):
    return x if isinstance(x, QI) else QI(x)


def wedge2(z1, z2):
    return [z1[i] * z2[j] - z1[j] * z2[i] for (i, j) in PAIRS4]


def psign(idx):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if idx[i] > idx[j]:
                s = -s
    return s


def pair(P, Qv):
    tot = Z0
    for a, (i, j) in enumerate(PAIRS4):
        for b, (k, l) in enumerate(PAIRS4):
            if len({i, j, k, l}) == 4:
                tot = tot + QI(psign((i, j, k, l))) * P[a] * Qv[b]
    return tot


def biv(i, j):
    return [ONE if p == (i, j) else Z0 for p in PAIRS4]


def vadd(*vs):
    return [sum((v[k] for v in vs), Z0) for k in range(len(vs[0]))]


def vscal(c, v):
    return [q(c) * a for a in v]


NINF, N0 = biv(0, 1), biv(2, 3)
BASIS = [biv(i, j) for (i, j) in PAIRS4]
XIDX = [(0, 2), (0, 3), (1, 2), (1, 3)]


def rot(U, V, Wv):
    return vadd(vscal(pair(U, Wv), V), vscal(-pair(V, Wv), U))


def act(A, P):
    out = [Z0] * 6
    for a, (i, j) in enumerate(PAIRS4):
        if P[a]:
            Ai = [A[r][i] for r in range(4)]
            Aj = [A[r][j] for r in range(4)]
            ei = [ONE if r == i else Z0 for r in range(4)]
            ej = [ONE if r == j else Z0 for r in range(4)]
            out = vadd(out, vscal(P[a], vadd(wedge2(Ai, ej), wedge2(ei, Aj))))
    return out


UNITS = [[[ONE if (i, j) == (r, c) else Z0 for j in range(4)] for i in range(4)] for r in range(4) for c in range(4)]


def spin_preimage(U, V):
    rows, rhs = [], []
    acts = [[act(Am, B) for B in BASIS] for Am in UNITS]
    for b in range(6):
        target = rot(U, V, BASIS[b])
        for comp in range(6):
            rows.append([acts[k][b][comp] for k in range(16)] + [-target[comp]])
    rows.append([ONE if k in (0, 5, 10, 15) else Z0 for k in range(16)] + [Z0])
    ker = GA.field_kernel(rows)
    sols = [s for s in ker if s[16]]
    assert len(ker) == 1 and len(sols) == 1
    s = sols[0]
    return [[s[4 * r + c] / s[16] for c in range(4)] for r in range(4)]


def xvec(co):
    return vadd(*[vscal(c, biv(*ij)) for c, ij in zip(co, XIDX)])


def xmat(co):
    """x^{a a'} with a in {0, 1}, a' in {2, 3}."""
    return {ij: q(c) for c, ij in zip(co, XIDX)}


EPS_P = {(2, 3): 1, (3, 2): -1}
EPS_O = {(0, 1): 1, (1, 0): -1}


def check_grading_element():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    A = spin_preimage(NINF, N0)
    half = QI(F(1, 2))
    assert A == [[-half if i == j and i < 2 else (half if i == j else Z0) for j in range(4)] for i in range(4)]
    return True


def check_translations_block():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    for co in XS:
        x, X = xvec(co), xmat(co)
        assert pair(x, N0) == Z0 and pair(x, NINF) == Z0
        A = spin_preimage(x, NINF)
        expect = [[Z0] * 4 for _ in range(4)]
        for a in (0, 1):
            for bp in (2, 3):
                expect[a][bp] = sum((X[(a, ap)] * QI(EPS_P.get((ap, bp), 0)) for ap in (2, 3)), Z0)
        assert A == expect
    return True


def check_special_conformal_block():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    for co in XS:
        x, X = xvec(co), xmat(co)
        A = spin_preimage(x, N0)
        expect = [[Z0] * 4 for _ in range(4)]
        for ap in (2, 3):
            for a in (0, 1):
                expect[ap][a] = -sum((X[(b, ap)] * QI(EPS_O.get((b, a), 0)) for b in (0, 1)), Z0)
        assert A == expect
    return True
