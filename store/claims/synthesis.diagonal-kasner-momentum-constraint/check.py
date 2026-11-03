"""synthesis.diagonal-kasner-momentum-constraint: exact checks (Fractions and GA linear algebra).

(a) Route independent of the derivation: the full coordinate Ricci tensor of
    g = dtau^2 - sum_i a_i^2 tau^(2 p_i) (dx^i)^2 at a point, from the metric's value and its
    first and second derivatives (exact Fractions), with L = log tau an independent symbol value;
    it must equal tau R_0i = d_i p_i + sum_j (p_i - p_j)(d_i b_j + L d_i p_j), b = log a, and the
    L-coefficient must vanish on the Kasner circle. The test points are fixed rational data; the
    values of tau R_0i at them are also pinned, so the data cannot drift unnoticed. Off the circle
    the formula fails (control).
(b) The tangent of the circle is t = (p_3 - p_2, p_1 - p_3, p_2 - p_1); with a = 1 the constraint is
    s_i t_i = 0, and t_i = 0 exactly at the collisions.
(c) Exponent fields depending on one coordinate: the explicit scale functions solve the constraint.
(d) The wall counterterm's scale factor a1 a2 a3.
"""
from fractions import Fraction as F
from GA import field_solve, field_rank
from tp_premise import premise

# fixed second derivatives (they must not enter R_0i); module level, not test data
DDP = [[[F(1, 3), F(-2), F(5, 7)], [F(2, 9), F(1), F(-1, 4)], [F(3, 2), F(0), F(1, 5)]],
       [[F(2, 9), F(1), F(-1, 4)], [F(-1), F(2, 3), F(4)], [F(1, 6), F(-3, 5), F(2)]],
       [[F(3, 2), F(0), F(1, 5)], [F(1, 6), F(-3, 5), F(2)], [F(7, 3), F(-1, 2), F(1, 8)]]]
DDB = [[[F(-1, 2), F(3), F(1, 9)], [F(4, 5), F(-2, 7), F(1)], [F(0), F(5, 3), F(-1)]],
       [[F(4, 5), F(-2, 7), F(1)], [F(2), F(1, 3), F(-6, 5)], [F(3, 4), F(1, 2), F(-2, 9)]],
       [[F(0), F(5, 3), F(-1)], [F(3, 4), F(1, 2), F(-2, 9)], [F(-5, 6), F(1, 7), F(3)]]]


def kasner(u):
    d = 1 + u + u * u
    return [-u / d, (1 + u) / d, u * (1 + u) / d]


def dkasner(u):
    d = 1 + u + u * u
    dd = 1 + 2 * u
    nums = [-u, 1 + u, u * (1 + u)]
    dnums = [F(-1), F(1), 1 + 2 * u]
    return [(dn * d - n * dd) / (d * d) for n, dn in zip(nums, dnums)]


def tangent(p):
    return [p[2] - p[1], p[0] - p[2], p[1] - p[0]]


def inv4(M):
    cols = [field_solve(M, [F(int(i == j)) for i in range(4)]) for j in range(4)]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def ricci(g, dg, ddg):
    n = 4
    gi = inv4(g)
    dgi = [[[-sum(gi[a][e] * dg[c][e][f] * gi[f][b] for e in range(n) for f in range(n))
             for b in range(n)] for a in range(n)] for c in range(n)]
    G1 = [[[(dg[a][l][b] + dg[b][l][a] - dg[l][a][b]) / 2 for b in range(n)] for a in range(n)] for l in range(n)]
    dG1 = [[[[(ddg[c][a][l][b] + ddg[c][b][l][a] - ddg[c][l][a][b]) / 2 for b in range(n)]
             for a in range(n)] for l in range(n)] for c in range(n)]
    Gam = [[[sum(gi[k][l] * G1[l][a][b] for l in range(n)) for b in range(n)] for a in range(n)] for k in range(n)]
    dGam = [[[[sum(dgi[c][k][l] * G1[l][a][b] + gi[k][l] * dG1[c][l][a][b] for l in range(n))
               for b in range(n)] for a in range(n)] for k in range(n)] for c in range(n)]
    return [[sum(dGam[k][k][a][b] - dGam[b][k][a][k] for k in range(n))
             + sum(Gam[k][k][l] * Gam[l][a][b] - Gam[k][b][l] * Gam[l][a][k] for k in range(n) for l in range(n))
             for b in range(n)] for a in range(n)]


def metric_jets(tau, L, p, dp, db, w):
    def dpsi(mu, i):
        return p[i] / tau if mu == 0 else db[mu - 1][i] + L * dp[mu - 1][i]

    def ddpsi(mu, nu, i):
        if mu == 0 and nu == 0:
            return -p[i] / (tau * tau)
        if mu == 0 or nu == 0:
            return dp[(nu if mu == 0 else mu) - 1][i] / tau
        return DDB[mu - 1][nu - 1][i] + L * DDP[mu - 1][nu - 1][i]

    g = [[F(0)] * 4 for _ in range(4)]
    g[0][0] = F(1)
    dg = [[[F(0)] * 4 for _ in range(4)] for _ in range(4)]
    ddg = [[[[F(0)] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for i in range(3):
        g[i + 1][i + 1] = -w[i]
        for mu in range(4):
            dg[mu][i + 1][i + 1] = -2 * w[i] * dpsi(mu, i)
            for nu in range(4):
                ddg[mu][nu][i + 1][i + 1] = -w[i] * (4 * dpsi(mu, i) * dpsi(nu, i) + 2 * ddpsi(mu, nu, i))
    return g, dg, ddg


def tau_R0(u, s, db, tau, w, L, dp=None):
    """tau R_0i (i = 1..3) from the full Ricci tensor; dp defaults to s (x) dp/du (on the circle)."""
    p = kasner(u)
    if dp is None:
        t = dkasner(u)
        dp = [[s[k] * t[i] for i in range(3)] for k in range(3)]
    R = ricci(*metric_jets(tau, L, p, dp, db, w))
    return p, dp, [tau * R[0][i + 1] for i in range(3)]


def formula(p, dp, db, L):
    return [dp[i][i] + sum((p[i] - p[j]) * (db[i][j] + L * dp[i][j]) for j in range(3)) for i in range(3)]


def check_momentum_constraint_formula():
    premise("dark-energy.variable-exponents-residue-pointwise-corrections-are")
    cases = [
        (F(2, 3), [F(1), F(-2), F(1, 2)], [[F(1, 3), F(-1), F(2)], [F(0), F(1, 2), F(-3)], [F(5), F(1, 4), F(1)]],
         F(1, 2), [F(2), F(3), F(1, 5)]),
        (F(-3, 5), [F(-1, 3), F(4), F(2)], [[F(2), F(1, 7), F(0)], [F(-1, 2), F(3), F(1)], [F(1), F(-4), F(2, 3)]],
         F(3), [F(1, 2), F(4), F(7, 3)]),
    ]
    pinned = []
    for u, s, db, tau, w in cases:
        for L in (F(0), F(-5, 2)):
            p, dp, val = tau_R0(u, s, db, tau, w, L)
            assert val == formula(p, dp, db, L)
            pinned.append(val)
            for i in range(3):     # the log tau coefficient vanishes on the circle
                assert sum((p[i] - p[j]) * dp[i][j] for j in range(3)) == 0
    # pinned values (L-independent, as the cancellation requires)
    assert pinned[0] == pinned[1] and pinned[2] == pinned[3]
    assert pinned[0] == [F(-254, 361), F(3, 361), F(6363, 1444)]
    assert pinned[2] == [F(3085, 7581), F(4903, 722), F(567, 361)]
    # a = 1: tau R_0i = d_i p_i, for two values of L
    zero = [[F(0)] * 3 for _ in range(3)]
    for L in (F(1), F(-7, 3)):
        p, dp, val = tau_R0(F(1, 4), [F(3), F(-1), F(2)], zero, F(5, 2), [F(1), F(2), F(3)], L)
        assert val == [dp[i][i] for i in range(3)]
        assert val == [F(-80, 49), F(16, 49), F(256, 147)]
    # control: derivatives off the circle break the formula
    off = [[F(1), F(1), F(1)], [F(0), F(2), F(-1)], [F(3), F(0), F(1)]]
    p, dp, val = tau_R0(F(2, 3), None, cases[0][2], F(1, 2), [F(2), F(3), F(1, 5)], F(-5, 2), dp=off)
    assert val != formula(p, dp, cases[0][2], F(-5, 2))
    return True


def check_tangent_and_collisions():
    premise("dark-energy.variable-exponents-residue-pointwise-corrections-are")
    premise("sheaf.collision-census")
    for u in (F(-3), F(-1), F(-1, 2), F(0), F(1, 3), F(1), F(5, 2)):
        p = kasner(u)
        assert sum(p) == 1 and sum(x * x for x in p) == 1
        assert field_rank([[F(1), F(1), F(1)], p]) == 2            # (1,1,1) and p independent
        t, dp = tangent(p), dkasner(u)
        i0 = next(i for i in range(3) if t[i] != 0)
        assert all(dp[i] * t[i0] == dp[i0] * t[i] for i in range(3))  # dp/du parallel to t
    # t_i = 0 exactly at the collisions: u = -1/2, 1, -2 give the Schwarzschild-type points,
    # u = 0, -1 the flat ones (excluded from the open circle)
    assert sorted(kasner(F(-1, 2))) == [F(-1, 3), F(2, 3), F(2, 3)] and tangent(kasner(F(-1, 2)))[2] == 0
    assert sorted(kasner(F(1))) == [F(-1, 3), F(2, 3), F(2, 3)] and tangent(kasner(F(1)))[0] == 0
    assert sorted(kasner(F(-2))) == [F(-1, 3), F(2, 3), F(2, 3)] and tangent(kasner(F(-2)))[1] == 0
    assert kasner(F(0)) == [F(0), F(1), F(0)] and kasner(F(-1)) == [F(1), F(0), F(0)]
    # away from collisions no t_i vanishes
    assert all(x != 0 for x in tangent(kasner(F(1, 3))))
    assert tangent(kasner(F(1, 3))) == [F(-8, 13), F(-7, 13), F(15, 13)]
    return True


def check_one_coordinate_fields():
    premise("dark-energy.variable-exponents-residue-pointwise-corrections-are")
    premise("sheaf.collision-census")
    # p = kasner(u(x1)), d_1 u = s1; d_1 b_j = d_1 p_1 (p_j - p_1)/D, D = (p2-p1)^2 + (p3-p1)^2
    for u, s1 in ((F(-1, 2), F(3)), (F(2), F(-5, 4)), (F(1, 3), F(1))):
        p = kasner(u)
        dp1 = [s1 * x for x in dkasner(u)]
        D = (p[1] - p[0]) ** 2 + (p[2] - p[0]) ** 2
        assert D > 0
        db = [F(0), dp1[0] * (p[1] - p[0]) / D, dp1[0] * (p[2] - p[0]) / D]
        assert dp1[0] == sum((p[j] - p[0]) * db[j] for j in range(3))
        # and the full Ricci component confirms R_01 = 0 with these scale functions
        dp = [dp1, [F(0)] * 3, [F(0)] * 3]
        dbm = [db, [F(0)] * 3, [F(0)] * 3]
        _, _, val = tau_R0(u, None, dbm, F(7, 2), [F(1), F(2), F(1, 3)], F(4), dp=dp)
        assert val == [F(0), F(0), F(0)]
    return True


def check_counterterm_scale_factor():
    premise("dark-energy.variable-exponents-residue-pointwise-corrections-are")
    premise("dark-energy.wall-counterterm")
    # cubic boost-block term ~ prod_i (p_i / tau) e^i with e^i = a_i tau^{p_i} dx^i: tau-exponent
    # sum(p) - 3 = -2, coefficient p1 p2 p3 a1 a2 a3 (the Lemma's 8 p1p2p3 at a = 1)
    for u, a, expected in ((F(1, 2), (F(1), F(1), F(1)), F(-36, 343)),
                           (F(1, 2), (F(2), F(1, 3), F(5, 7)), F(-120, 2401)),
                           (F(-3), (F(3), F(1), F(1)), F(-108, 343))):
        p = kasner(u)
        assert sum(p) - 3 == -2
        assert p[0] * p[1] * p[2] * a[0] * a[1] * a[2] == expected
    return True
