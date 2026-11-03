"""sheaf.uniqueness-weighted-module: exact checks.

Schwarzschild in Painleve-Gullstrand form, u = sqrt(r), 2M = m^2, everything a rational-function identity in u.
(1) The weighted Gram of W on (rho, dt, mu1, mu2), rho = u dr, mu1 = r dtheta, mu2 = r sin dphi, derived from the
inverse of the PG metric block, is [[m^2 - r, -m], [-m, 1]] + diag(-1, -1) with det G_W = -r: tame, corank one at
the boundary with radical k = rho + m dt (the premise).
(2) A rain-bounded extension M is given by a transition A (rows: an M-frame in the W-frame, entries polynomial in
u). For six transitions, det G_M = (det A)^2 det G_W as an identity, and the boundary behaviour is as the proof
says: when A(0) is invertible M = W and det G_M / r tends to -(det A(0))^2 != 0 (first order); when A(0) is
singular, (T2d) or (T3d) fails: either the boundary corank exceeds one, or it is one with a nonzero 3 x 3 boundary
minor while det G_M / r -> 0, so the dying eigenvalue is o(r). Expected outcomes are written out per transition.
EXPORTS weighted_gram(m), congruence(A, G) and dying_order(det) for dependants.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

U = GA.RF.var()
R = U * U


def C(x):
    return GA.RF.const(F(x))


def weighted_gram(m):
    """Weighted Gram of W from the PG cometric, frame (rho, dt, mu1, mu2), equator."""
    beta = C(m) / U
    g_tt, g_tr, g_rr = GA.RF1 - beta * beta, -beta, C(-1)
    det = g_tt * g_rr - g_tr * g_tr
    Ctt, Ctr, Crr = g_rr / det, -g_tr / det, g_tt / det          # inverse of the metric block
    Cang = C(-1) / (R * R)                                       # G(dtheta, dtheta) at the equator
    Z = GA.RF0
    return [[U * U * Crr, U * Ctr, Z, Z],
            [U * Ctr, Ctt, Z, Z],
            [Z, Z, R * R * Cang, Z],
            [Z, Z, Z, R * R * Cang]]


def congruence(A, G):
    n = len(A)
    out = [[GA.RF0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc = GA.RF0
            for a in range(n):
                if A[i][a].is_zero():
                    continue
                for b in range(n):
                    if not A[j][b].is_zero():
                        acc = acc + A[i][a] * G[a][b] * A[j][b]
            out[i][j] = acc
    return out


def dying_order(det):
    """Order in r of an RF in u that vanishes at u = 0 to even order: smallest j with det/r^j nonzero at 0."""
    j, cur = 0, det
    while cur.eval(F(0)) == 0 and j < 6:
        cur = cur / R
        j += 1
    return j, cur.eval(F(0))


EXPORTS = {"weighted_gram": weighted_gram, "congruence": congruence, "dying_order": dying_order}

MASSES = (F(1), F(3))


def at0(M):
    return [[e.eval(F(0)) for e in row] for row in M]


def check_weighted_gram_is_tame_normal_form():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        W = weighted_gram(m)
        want = [[C(m * m) - R, C(-m), GA.RF0, GA.RF0], [C(-m), GA.RF1, GA.RF0, GA.RF0],
                [GA.RF0, GA.RF0, C(-1), GA.RF0], [GA.RF0, GA.RF0, GA.RF0, C(-1)]]
        ok = ok and all(W[i][j].eqrf(want[i][j]) for i in range(4) for j in range(4))
        ok = ok and GA.rf_mat_det(W).eqrf(-R)
        W0 = at0(W)
        ok = ok and GA.mat_rank(W0) == 3 and GA.congruence_signature(W0) == (1, 2, 1)
        k = [F(1), m, F(0), F(0)]
        ok = ok and all(sum(W0[i][j] * k[j] for j in range(4)) == 0 for i in range(4))
    GA.check("W: Gram polynomial in r, det G_W = -r, corank one at E with radical rho + m dt", ok)
    return ok


def transitions(m):
    """Six rain-bounded transitions A (rows: an M-frame in the W-frame)."""
    Z, O = GA.RF0, GA.RF1
    k_row = [O, C(m), Z, Z]
    return [
        [[U, Z, Z, Z], [O + C(2), C(m), Z, Z], [Z, Z, O, Z], [Z, Z, Z, O]],
        [[U, Z, Z, Z], [O + C(F(1, 3)), C(m), Z, Z], [Z, Z, O, Z], [Z, Z, Z, O]],
        [[O, Z, Z, Z], [Z, U, Z, Z], [Z, Z, O, Z], [Z, Z, Z, O]],
        [[O, Z, Z, Z], [Z, O, Z, Z], [Z, Z, U, Z], [Z, Z, Z, O]],
        [[O, O, Z, Z], [Z, O, Z, Z], [Z, Z, O, U], [Z, Z, Z, O]],
        [[C(2), Z, Z, Z], k_row, [Z, Z, O, Z], [Z, Z, Z, O]],
    ]


def check_singular_transitions_violate_tameness():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        W = weighted_gram(m)
        detW = GA.rf_mat_det(W)
        # expected (boundary rank of G_M, order in r of det G_M, leading coefficient), worked out by hand:
        # M_c (c = 2, 1/3): det A = m u; u dt: det A = u; u mu1: corank two; unimodular: det A = 1; (2 rho, k): 2m
        expect = [(3, 2, -m * m), (3, 2, -m * m), (3, 2, -1), (2, 2, -1), (3, 1, -1), (3, 1, -4 * m * m)]
        for A, (rank0, order, lead) in zip(transitions(m), expect):
            GM = congruence(A, W)
            detA = GA.rf_mat_det(A)
            detM = GA.rf_mat_det(GM)
            ok = ok and detM.eqrf(detA * detA * detW)
            G0 = at0(GM)
            ok = ok and GA.mat_rank(G0) == rank0
            ok = ok and dying_order(detM) == (order, lead)
            invertible = detA.eval(F(0)) != 0
            if invertible:
                # M = W near the boundary, first-order dying eigenvalue
                ok = ok and order == 1 and lead == -(detA.eval(F(0)) ** 2)
            elif rank0 == 3:
                # corank one: a nonzero 3 x 3 boundary minor, so the dying eigenvalue is det / unit = o(r)
                minors = []
                for drop in range(4):
                    keep = [i for i in range(4) if i != drop]
                    minors.append(GA.mat_rank([[G0[i][j] for j in keep] for i in keep]) == 3)
                ok = ok and any(minors) and order >= 2
            else:
                ok = ok and rank0 < 3
    GA.check("every rain-bounded extension with singular transition breaks (T2d) or (T3d); invertible ones are W", ok)
    return ok
