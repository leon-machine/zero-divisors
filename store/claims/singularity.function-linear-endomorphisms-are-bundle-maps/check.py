"""singularity.function-linear-endomorphisms-are-bundle-maps: exact checks of the finite core.

The lemma is analytic (C^inf(E)-linearity on smooth sections, proved with a bump function). Its finite
core is checked: over a finite base X = {x1, x2, x3}, a trivial bundle of rank r (r = 1, 2) has
sections Q^(3r), and the functions Q^3 act by pointwise multiplication. To avoid a point-adapted
presentation, the module of sections is written in a mixed basis (a fixed invertible matrix Q), so
multiplication by f is Q M_f Q^{-1}, not diagonal.
(1) The function-linear endomorphisms (the common kernel of D -> [D, Q M_f Q^{-1}] for two functions
    f, solved exactly by GA.field_kernel on the (3r)^2 unknowns) form a space of dimension 3 r^2; back
    in the point-adapted basis every one of them is block diagonal, so (Ds)(x) depends only on s(x):
    D is a bundle map {a_x}; for r = 1 it is multiplication by a function (diagonal).
(2) The bump mechanism: for every D in that space and every section s with s(x) = 0 (one per point),
    (Ds)(x) = 0.
(3) Controls: a difference operator (Ds)(x_j) = s(x_{j+1}) - s(x_j) is linear over constants but not
    function-linear, and moves a section vanishing at x into one that does not; on polynomial sections
    of the trivial line bundle over R, d/dx has the Leibniz defect D(fs) - f D(s) = f' s != 0, while a
    bundle map a(x) has none.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

NPTS = 3
QMIX = {1: [[1, 1, 0], [0, 1, 2], [1, 0, 1]],
        2: [[1, 0, 1, 0, 0, 2], [0, 1, 0, 1, 0, 0], [1, 0, 2, 0, 1, 2],
            [0, 0, 1, 2, 0, 1], [2, 0, 2, 0, 1, 4], [0, 1, 0, 1, 1, 1]]}
FUNCS = ((F(1), F(2), F(5)), (F(0), F(1), F(0)))
POLY_F = [F(1), F(-2), F(3)]          # f(x) = 1 - 2x + 3x^2
POLY_S = [F(4), F(0), F(-1), F(1)]    # s(x)
POLY_A = [F(2), F(1)]                 # a(x) = 2 + x
DIFF = [[F(-1), F(1), F(0)], [F(0), F(-1), F(1)], [F(1), F(0), F(-1)]]   # (Ds)(x_j) = s(x_{j+1}) - s(x_j)
S_VANISH = [F(0), F(3), F(0)]


mm = GA.mat_mul


def inverse(A):
    n = len(A)
    cols = [GA.field_solve([[F(x) for x in row] for row in A], [F(int(i == j)) for i in range(n)])
            for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def mult(f, r):
    return [[f[i // r] if i == j else F(0) for j in range(NPTS * r)] for i in range(NPTS * r)]


def commutant(mats, d):
    rows = []
    for M in mats:
        for i in range(d):
            for j in range(d):
                row = [F(0)] * (d * d)
                for t in range(d):
                    row[i * d + t] += M[t][j]       # (D M)_ij
                    row[t * d + j] -= M[i][t]       # (M D)_ij
                rows.append(row)
    return [[[v[i * d + j] for j in range(d)] for i in range(d)] for v in GA.field_kernel(rows)]


def function_linear(r):
    d = NPTS * r
    Q = [[F(x) for x in row] for row in QMIX[r]]
    Qi = inverse(Q)
    mats = [mm(mm(Q, mult(f, r)), Qi) for f in FUNCS]
    return [mm(mm(Qi, D), Q) for D in commutant(mats, d)]   # back to the point-adapted basis


def check_function_linear_maps_are_fibrewise():
    ok = True
    for r in (1, 2):
        Ds = function_linear(r)
        ok = ok and len(Ds) == NPTS * r * r
        for D in Ds:
            ok = ok and all(D[i][j] == 0 for i in range(NPTS * r) for j in range(NPTS * r) if i // r != j // r)
        ok = ok and GA.rank_of_vectors([[x for row in D for x in row] for D in Ds]) == NPTS * r * r
    ok = ok and all(D[i][j] == 0 for D in function_linear(1) for i in range(NPTS) for j in range(NPTS) if i != j)
    GA.check("function-linear endomorphisms: dimension 3 r^2, block diagonal (bundle maps), diagonal for r = 1", ok)
    return ok


def check_value_at_x_depends_only_on_s_at_x():
    ok = True
    for r in (1, 2):
        Ds = function_linear(r)
        for x in range(NPTS):
            s = [F(0) if i // r == x else F(i + 1) for i in range(NPTS * r)]
            for D in Ds:
                Ds_ = [sum((D[i][j] * s[j] for j in range(NPTS * r)), F(0)) for i in range(NPTS * r)]
                ok = ok and all(Ds_[i] == 0 for i in range(NPTS * r) if i // r == x)
    GA.check("s(x) = 0 implies (Ds)(x) = 0 for every function-linear D", ok)
    return ok


def check_controls_are_not_function_linear():
    ok = True
    f = mult(FUNCS[0], 1)
    ok = ok and mm(DIFF, f) != mm(f, DIFF)
    out = [sum((DIFF[i][j] * S_VANISH[j] for j in range(NPTS)), F(0)) for i in range(NPTS)]
    ok = ok and out == [3, -3, 0] and S_VANISH[0] == 0
    comm = [[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(mm(DIFF, f), mm(f, DIFF))]
    ok = ok and comm == [[0, 1, 0], [0, 0, 3], [-4, 0, 0]]
    fs = GA.pmul(POLY_F, POLY_S)
    defect = GA.padd(GA.pderiv(fs), GA.pneg(GA.pmul(POLY_F, GA.pderiv(POLY_S))))
    ok = ok and defect == GA.pmul(GA.pderiv(POLY_F), POLY_S) and defect != []
    ok = ok and GA.pmul(POLY_A, fs) == GA.pmul(POLY_F, GA.pmul(POLY_A, POLY_S))
    GA.check("controls: a difference operator and d/dx are not function-linear (Leibniz defect f' s)", ok)
    return ok
