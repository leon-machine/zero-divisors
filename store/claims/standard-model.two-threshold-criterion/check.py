"""standard-model.two-threshold-criterion: exact checks.

With L = ln(M_U/M_Z) = 2 pi x, f = ln(M_U/M_I)/L and f' = ln(M_U/M_I')/L, the one-loop equations
are a_i = a_U + x (b_i + f Dl_i + f' Dl'_i). For each (f, f') the two unknowns (a_U, x) solve the
three equations iff the augmented rank is 2; the check confirms that this happens exactly on the
stated line P f + Q f' = C (P = Dl_12 - R Dl_23, Q = Dl'_12 - R Dl'_23, C = R b_23 - b_12), on a
grid of (f, f') in the triangle for four supersymmetric splits and a hand instance, and that
x = (a_1 - a_2)/(b_12 + f Dl_12 + f' Dl'_12) then solves the system. The segment's endpoints are
computed as exact rationals (hand instance: (1/2, 0) and (1, 1/5), x = 2 and 5/3). Reductions:
f' = f gives the one-threshold f of Dl + Dl', f' = 0 the one-threshold f of Dl. Complete
multiplets, Dl -> Dl + c(1,1,1) at either threshold, leave P, Q, C unchanged.
The conversion of x to GeV is not part of the claim's exact content and is not checked.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def record(aem_inv, s2, as_inv):
    a2 = s2 * aem_inv
    return (F(3, 5) * (aem_inv - a2), a2, as_inv)


def diffs(v):
    return v[0] - v[1], v[1] - v[2]


def line(A, b, d, dp):
    D12, D23 = diffs(A)
    R = D12 / D23
    b12, b23 = diffs(b)
    return (diffs(d)[0] - R * diffs(d)[1], diffs(dp)[0] - R * diffs(dp)[1], R * b23 - b12)


def consistent(A, b, d, dp, f, fp):
    """Ranks of the (a_U, x) system and its augmentation."""
    M = [[F(1), b[i] + f * d[i] + fp * dp[i]] for i in range(3)]
    Aug = [row + [A[i]] for i, row in enumerate(M)]
    return GA.mat_rank(M), GA.mat_rank(Aug)


def segment(A, b, d, dp):
    """Exact endpoints of {P f + Q f' = C} inside 0 <= f' <= f <= 1."""
    P, Q, C = line(A, b, d, dp)
    pts = set()
    if P != 0 and 0 <= C / P <= 1:
        pts.add((C / P, F(0)))
    if Q != 0 and 0 <= (C - P) / Q <= 1:
        pts.add((F(1), (C - P) / Q))
    if P + Q != 0 and 0 <= C / (P + Q) <= 1:
        pts.add((C / (P + Q), C / (P + Q)))
    return sorted(pts)


def one_threshold_f(A, b, d):
    D12, D23 = diffs(A)
    R = D12 / D23
    b12, b23 = diffs(b)
    return (R * b23 - b12) / (diffs(d)[0] - R * diffs(d)[1])


B_SM = (F(41, 10), F(-19, 6), F(-7))
A_T12 = record(F(128), F(2312, 10000), F(500, 59))
GAUGINOS, HIGGSINOS = (F(0), F(4, 3), F(2)), (F(2, 5), F(2, 3), F(0))
H2, SFERM = (F(1, 10), F(1, 6), F(0)), (F(2), F(2), F(2))
GLUINO, WINO = (F(0), F(0), F(2)), (F(0), F(4, 3), F(0))


def add(*vs):
    return tuple(sum(c) for c in zip(*vs))


FAMILIES = [(add(GAUGINOS, HIGGSINOS), add(SFERM, H2)),
            (HIGGSINOS, add(GAUGINOS, SFERM, H2)),
            (add(HIGGSINOS, H2), add(GAUGINOS, SFERM)),
            (add(WINO, HIGGSINOS), add(GLUINO, SFERM, H2))]
GRID = [(F(i, 12), F(j, 12)) for i in range(13) for j in range(i + 1)]
HAND = ((F(6), F(3), F(1)), (F(2), F(1), F(0)), (F(1), F(0), F(0)), (F(0), F(1), F(0)))
C_SHIFTS = (F(1), F(-2), F(5, 3), F(4, 3))
NONUNIFORM = (F(1), F(0), F(0))


def check_level_line_is_the_meeting_condition():
    ok = True
    A, b, d, dp = HAND
    # hand: R = 3/2, P = 1, Q = -5/2, C = 1/2; segment (1/2, 0) -- (1, 1/5)
    ok = ok and line(A, b, d, dp) == (F(1), F(-5, 2), F(1, 2))
    ok = ok and segment(A, b, d, dp) == [(F(1, 2), F(0)), (F(1), F(1, 5))]
    ok = ok and [diffs(A)[0] / (diffs(b)[0] + f * diffs(d)[0] + fp * diffs(dp)[0])
                 for f, fp in segment(A, b, d, dp)] == [F(2), F(5, 3)]
    on = off = 0
    for (A, b, d, dp) in [HAND] + [(A_T12, B_SM, d, dp) for d, dp in FAMILIES]:
        P, Q, C = line(A, b, d, dp)
        for f, fp in GRID:
            rk = consistent(A, b, d, dp, f, fp)
            on_line = P * f + Q * fp == C
            ok = ok and (rk == (2, 2)) == on_line
            off += 1
        # points exactly on the line: f' solved from f
        for f in (F(0), F(1, 3), F(1, 2), F(1), F(3, 2), F(-1)):
            fp = (C - P * f) / Q
            x = diffs(A)[0] / (diffs(b)[0] + f * diffs(d)[0] + fp * diffs(dp)[0])
            aU = A[0] - x * (b[0] + f * d[0] + fp * dp[0])
            ok = ok and all(A[i] == aU + x * (b[i] + f * d[i] + fp * dp[i]) for i in range(3))
            on += 1
    ok = ok and on == 30 and off == 455
    GA.check("two thresholds: the system is solvable exactly on P f + Q f' = C, with x from a_1 - a_2", ok)
    return ok


def check_segment_and_reductions():
    ok = True
    # four supersymmetric splits: (a), (b), (c) miss the triangle, (d) has a segment whose
    # endpoints (0.438, 0) and (1, 0.991) are exact rationals
    segs = [segment(A_T12, B_SM, d, dp) for d, dp in FAMILIES]
    ok = ok and [len(s) for s in segs] == [0, 0, 0, 2]
    (fa, fpa), (fb, fpb) = segs[3]
    ok = ok and fpa == 0 and F(437, 1000) < fa < F(438, 1000) and fb == 1 and F(990, 1000) < fpb < F(992, 1000)
    for f, fp in segs[3]:
        ok = ok and diffs(A_T12)[0] / (diffs(B_SM)[0] + f * diffs(FAMILIES[3][0])[0]
                                      + fp * diffs(FAMILIES[3][1])[0]) > 0
    # reductions to one threshold
    for (A, b, d, dp) in [HAND] + [(A_T12, B_SM, d, dp) for d, dp in FAMILIES]:
        P, Q, C = line(A, b, d, dp)
        if P + Q != 0:
            ok = ok and C / (P + Q) == one_threshold_f(A, b, add(d, dp))
        if P != 0:
            ok = ok and C / P == one_threshold_f(A, b, d)
    # the full supersymmetric content at f' = f: the one-threshold f = 1.0116
    P, Q, C = line(A_T12, B_SM, *FAMILIES[0])
    ok = ok and F(1011, 1000) < C / (P + Q) < F(1012, 1000)
    GA.check("two thresholds: exact segment endpoints, and reductions at f' = f and f' = 0", ok)
    return ok


def check_complete_multiplets_inert_at_either_threshold():
    premise("standard-model.complete-multiplets-shift-all-three-coefficients")
    ok = True
    n = 0
    A, b, d, dp = HAND
    for c in C_SHIFTS:
        sh = (c, c, c)
        # hand instance: the line stays (P, Q, C) = (1, -5/2, 1/2)
        ok = ok and line(A, b, add(d, sh), dp) == (F(1), F(-5, 2), F(1, 2))
        ok = ok and line(A, b, d, add(dp, sh)) == (F(1), F(-5, 2), F(1, 2))
    for (A, b, d, dp) in [HAND] + [(A_T12, B_SM, d, dp) for d, dp in FAMILIES]:
        base = line(A, b, d, dp)
        for c in C_SHIFTS:
            sh = (c, c, c)
            ok = ok and line(A, b, add(d, sh), dp) == base and line(A, b, d, add(dp, sh)) == base
            n += 1
        # a shift not along (1,1,1) moves the line
        ok = ok and line(A, b, add(d, NONUNIFORM), dp) != base
    ok = ok and n == 20
    GA.check("two thresholds: a complete multiplet at either threshold leaves the line unchanged", ok)
    return ok
