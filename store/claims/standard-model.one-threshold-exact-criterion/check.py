"""standard-model.one-threshold-exact-criterion: exact checks.

The one-loop system is a_i = a_U + b_i x + D_i y (i = 1, 2, 3), unknowns (a_U, x, y), with
D_12 = a_1 - a_2, D_23 = a_2 - a_3 the record differences, R = D_12 / D_23,
r_0 = b_12 / b_23 and r_D = (b_12 + Dl_12) / (b_23 + Dl_23).

(i) For a hand-solved instance (b = (2, 1, 0), Dl = (1, 0, 0), a = (6, 3, 1)) the closed forms give
x = 2, y = 1, a_U = 1, f = 1/2; for every sample spectrum (the eleven content rows of the table,
from their Dl values, and synthetic ones) at three record points the closed forms solve the three
equations exactly, f = y/x equals the R form, and the 3 x 3 system has rank 3 (uniqueness). In the
singular case (Dl_12, Dl_23) parallel to (b_12, b_23) the system is inconsistent unless R = r_0, and
consistent (with a one-parameter family) when the record is moved to R = r_0.
(ii) Dl -> Dl + c(1,1,1) leaves x, y, f unchanged and lowers a_U by c y, for several c; the
complete-multiplet shift of the lemma is of this form, so with y > 0 it lowers a_U.
(iii) 0 <= f <= 1 iff R lies between r_0 and r_D, on a grid of 400 spectra at three record points;
then x > 0. The Moebius derivative r'(t) = (Dl_12 b_23 - Dl_23 b_12)/(b_23 + t Dl_23)^2 is checked
as a rational-function identity, and monotonicity at ninths.

The logarithmic conversion to GeV is not part of this claim and is not checked here. Exports the
solver for the dependent claims.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# generic machinery (module level: not mutated)
# ---------------------------------------------------------------------------


def record(aem_inv, s2, as_inv):
    """(a_1, a_2, a_3) at M_Z from alpha_em^-1, sin^2 theta_W, alpha_s^-1 (GUT normalisation)."""
    a2 = s2 * aem_inv
    return (F(3, 5) * (aem_inv - a2), a2, as_inv)


def diffs(v):
    return v[0] - v[1], v[1] - v[2]


def solve(A, b, d):
    """Closed forms of the claim: (x, y, a_U, f) or None when the determinant vanishes."""
    D12, D23 = diffs(A)
    b12, b23 = diffs(b)
    d12, d23 = diffs(d)
    det = b12 * d23 - b23 * d12
    if det == 0:
        return None
    x = (D12 * d23 - D23 * d12) / det
    y = (b12 * D23 - b23 * D12) / det
    aU = A[2] - b[2] * x - d[2] * y
    return x, y, aU, y / x


def f_R_form(A, b, d):
    D12, D23 = diffs(A)
    b12, b23 = diffs(b)
    d12, d23 = diffs(d)
    R = D12 / D23
    return (R * b23 - b12) / (d12 - R * d23)


def r_of(b, d, t):
    b12, b23 = diffs(b)
    d12, d23 = diffs(d)
    return (b12 + t * d12) / (b23 + t * d23)


def system_ranks(A, b, d):
    """Rank of the coefficient matrix of (a_U, x, y) and of the augmented matrix."""
    M = [[F(1), b[i], d[i]] for i in range(3)]
    Aug = [[F(1), b[i], d[i], A[i]] for i in range(3)]
    return GA.mat_rank(M), GA.mat_rank(Aug)


B_SM = (F(41, 10), F(-19, 6), F(-7))
B_ALT = (F(3), F(-1, 2), F(-4))
RECORDS = [record(F(128), F(2312, 10000), F(500, 59)),
           record(F(127951, 1000), F(23122, 100000), F(10000, 1180)),
           record(F(130), F(22, 100), F(9))]
# the content rows of the table (Dl above M_I), and synthetic spectra
SPECTRA = [(F(0), F(0), F(2)), (F(0), F(4, 3), F(2)), (F(2, 5), F(2, 3), F(0)),
           (F(1, 10), F(1, 6), F(0)), (F(2, 5), F(2), F(2)), (F(1, 2), F(13, 6), F(2)),
           (F(5, 2), F(25, 6), F(4)), (F(0), F(4, 3), F(0)), (F(2, 5), F(2), F(0)),
           (F(5, 2), F(25, 6), F(2)), (F(1, 3), F(-1, 7), F(5, 2)), (F(-2, 9), F(3, 4), F(1, 5))]
GRID = [(F(i, 3), F(j, 2), F(k, 4)) for i in range(-2, 3) for j in range(0, 8) for k in range(0, 10)]
C_SHIFTS = (F(1), F(-2), F(7, 3), F(2, 3) * F(2))


def admissible_pairs():
    for A in RECORDS:
        for b in (B_SM, B_ALT):
            for d in SPECTRA:
                yield A, b, d


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------


def check_closed_form_solution_and_uniqueness():
    ok = True
    # hand-solved instance: b12 = b23 = 1, Dl12 = 1, Dl23 = 0, D12 = 3, D23 = 2, det = -1
    x, y, aU, f = solve((F(6), F(3), F(1)), (F(2), F(1), F(0)), (F(1), F(0), F(0)))
    ok = ok and (x, y, aU, f) == (F(2), F(1), F(1), F(1, 2))
    n = 0
    for A, b, d in admissible_pairs():
        s = solve(A, b, d)
        if s is None:
            continue
        x, y, aU, f = s
        ok = ok and all(A[i] == aU + b[i] * x + d[i] * y for i in range(3))
        ok = ok and f == f_R_form(A, b, d)
        ok = ok and system_ranks(A, b, d) == (3, 3)
        n += 1
    ok = ok and n == 72
    # the singular case: (Dl12, Dl23) parallel to (b12, b23), here Dl = 2 b + 5 (1,1,1)
    for A in RECORDS:
        d = tuple(2 * B_SM[i] + 5 for i in range(3))
        R = diffs(A)[0] / diffs(A)[1]
        r0 = diffs(B_SM)[0] / diffs(B_SM)[1]
        ok = ok and solve(A, B_SM, d) is None and R != r0
        ok = ok and system_ranks(A, B_SM, d) == (2, 3)
        # move the record onto R = r0 (keep a_2, a_3; set a_1 = a_2 + r0 (a_2 - a_3))
        A0 = (A[1] + r0 * (A[1] - A[2]), A[1], A[2])
        ok = ok and system_ranks(A0, B_SM, d) == (2, 2)
    GA.check("one threshold (i): closed forms, R form of f, uniqueness; singular case", ok)
    return ok


def check_complete_multiplets_inert():
    premise("standard-model.complete-multiplets-shift-all-three-coefficients")
    ok = True
    n = 0
    for A, b, d in admissible_pairs():
        s = solve(A, b, d)
        if s is None:
            continue
        x, y, aU, f = s
        for c in C_SHIFTS:
            s2 = solve(A, b, tuple(v + c for v in d))
            ok = ok and s2[0] == x and s2[1] == y and s2[3] == f
            ok = ok and s2[2] == aU - c * y
            # a complete multiplet (c > 0) at an admissible threshold (y > 0) lowers a_U
            if c > 0 and y > 0:
                ok = ok and s2[2] < aU
            n += 1
    ok = ok and n == 288
    # hand instance: shifting Dl = (1,0,0) by 3 lowers a_U = 1 by 3 y = 3
    s = solve((F(6), F(3), F(1)), (F(2), F(1), F(0)), (F(4), F(3), F(3)))
    ok = ok and s[:2] == (F(2), F(1)) and s[2] == F(-2)
    GA.check("one threshold (ii): Dl + c(1,1,1) leaves x, y, f and lowers a_U by c y", ok)
    return ok


def check_interval_criterion_and_monotonicity():
    ok = True
    # hand instances: r_0 = 1, R = 3/2; Dl = (1,0,0) gives r_D = 2, f = 1/2 (inside);
    # Dl = (0,1,0) gives r_D = 0, f = -1/5 (outside)
    A, b = (F(6), F(3), F(1)), (F(2), F(1), F(0))
    ok = ok and r_of(b, (F(1), F(0), F(0)), F(1)) == F(2) and solve(A, b, (F(1), F(0), F(0)))[3] == F(1, 2)
    ok = ok and r_of(b, (F(0), F(1), F(0)), F(1)) == F(0) and solve(A, b, (F(0), F(1), F(0)))[3] == F(-1, 5)
    inside = outside = 0
    for A in RECORDS:
        D12, D23 = diffs(A)
        R = D12 / D23
        ok = ok and D12 > 0 and D23 > 0
        for b in (B_SM, B_ALT):
            b12, b23 = diffs(b)
            r0 = b12 / b23
            for d in GRID:
                d12, d23 = diffs(d)
                if not (b23 > 0 and b23 + d23 > 0):
                    continue
                s = solve(A, b, d)
                if s is None:
                    continue
                x, y, aU, f = s
                rD = r_of(b, d, F(1))
                between = min(r0, rD) <= R <= max(r0, rD)
                ok = ok and ((0 <= f <= 1) == between)
                if between:
                    ok = ok and x > 0
                    inside += 1
                else:
                    outside += 1
    ok = ok and inside > 0 and outside > 0
    # the Moebius derivative, as an identity of rational functions in t, and monotonicity
    t = GA.RF.var()
    for b in (B_SM, B_ALT):
        b12, b23 = diffs(b)
        for d in SPECTRA:
            d12, d23 = diffs(d)
            r = (GA.RF.const(b12) + GA.RF.const(d12) * t) / (GA.RF.const(b23) + GA.RF.const(d23) * t)
            den = GA.RF.const(b23) + GA.RF.const(d23) * t
            ok = ok and r.deriv().eqrf(GA.RF.const(d12 * b23 - d23 * b12) / (den * den))
            sgn = d12 * b23 - d23 * b12
            vals = [r_of(b, d, F(k, 8)) for k in range(9)]
            if sgn != 0:
                ok = ok and all((vals[k + 1] - vals[k]) * sgn > 0 for k in range(8))
            else:
                ok = ok and len(set(vals)) == 1
    GA.check("one threshold (iii): 0 <= f <= 1 iff R between r_0 and r_D, then x > 0; monotone r(t)", ok)
    return ok


EXPORTS = {"record": record, "solve": solve, "r_of": r_of, "diffs": diffs, "B_SM": B_SM}
