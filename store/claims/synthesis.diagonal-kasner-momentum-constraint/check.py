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
(e) The proof's GTG route: the synchronous gauge field hb^{-1}(e_tau) = e0, hb^{-1}(e_i) = A_i e_i built from
    exact jets (lib/gtg.py), Omega solved from the torsion equation against its closed form, the boost row of
    the field strength and R_0i = -g_0 . calR(g_i) from the engine's Ricci map; and t = -I3 ((1,1,1) ^ p).
"""
from fractions import Fraction as F
from GA import field_solve, field_rank
from tp_premise import premise
import GA
import gtg

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


# (e) data for the GTG route: exponent fields on the circle through the parametrisation p(u), u = u(x) a jet
GTG_DATA = [
    # (tau0, L, u0, du (3), ddu (3x3 upper), db (3x3: db[k][j] = d_j b_k), ddb, A values)
    (F(2), F(3, 5), F(1, 2), [F(1, 3), F(-2), F(1, 4)], [F(1, 2), F(0), F(-1, 3), F(2), F(1, 5), F(0)],
     [[F(1, 2), F(-1), F(2, 3)], [F(0), F(3, 4), F(-1, 5)], [F(2), F(1, 7), F(1)]],
     [F(1, 3), F(-1, 2), F(2), F(0), F(1, 4), F(-3)], [F(2), F(1, 3), F(5, 4)]),
    (F(1, 3), F(-7, 4), F(-3, 2), [F(2, 5), F(1), F(-1, 2)], [F(0), F(1, 3), F(2), F(-1), F(0), F(1, 2)],
     [[F(-1, 3), F(0), F(1)], [F(2, 5), F(-2), F(1, 3)], [F(0), F(1, 2), F(-3, 4)]],
     [F(0), F(2), F(-1, 3), F(1, 5), F(0), F(1)], [F(3, 7), F(2), F(1)]),
]


def _quad(c0, lin, qd, X, x0):
    """c0 + sum lin_j (x_j - x0_j) + upper-triangular quadratic qd, as a jet in the labels X."""
    out = gtg.Jet.const(c0, 4)
    for j in range(3):
        out = out + lin[j] * (X[j + 1] - x0[j])
    idx = [(a, b) for a in range(3) for b in range(a, 3)]
    for (a, b), c in zip(idx, qd):
        out = out + c * (X[a + 1] - x0[a]) * (X[b + 1] - x0[b])
    return out


def check_gtg_rotation_gauge_field_and_mixed_ricci():
    """The proof's GTG route: for hb^{-1}(e_tau) = e0, hb^{-1}(e_i) = A_i e_i with A_k = a_k tau^{p_k}, p on the
    Kasner circle (p = p(u(x)) exactly) and log tau an independent symbol value L: the torsion equation gives
    Omega(e_tau) = 0, Omega(e_{x^i}) = -d_tau A_i B_i - sum_j (d_j A_i / A_j) e_i ^ e_j; the boost row of the
    field strength gives e0 . calR(e_i) = sum_k (1/A_k) d_tau(d_i A_k / A_i); and tau R_0i = -tau A_i e0 .
    calR(e_i) equals d_i p_i + sum_j (p_i - p_j) d_i b_j for two values of L (the log tau terms cancel)."""
    premise("synthesis.imported-gtg-dictionary")
    premise("dark-energy.variable-exponents-residue-pointwise-corrections-are")
    ok = True
    x0 = [F(1, 2), F(-1, 3), F(2)]
    for (tau0, L, u0, du, ddu, db, ddb, Avals) in GTG_DATA:
        results = []
        for Lv in (L, L + 1):
            X = [gtg.Jet.var(0, tau0, 4, 2)] + [gtg.Jet.var(i + 1, x0[i], 4, 2) for i in range(3)]
            u = _quad(u0, du, ddu, X, x0)
            den = 1 + u + u * u
            p = [(F(0) - u) / den, (1 + u) / den, (u + u * u) / den]
            dt = X[0] - tau0
            logt = Lv + dt / tau0 - dt * dt / (2 * tau0 * tau0)
            A = []
            for k in range(3):
                b = _quad(F(0), db[k], ddb, X, x0)
                A.append(gtg.jexp(b + p[k] * logt, Avals[k]))
            TH = [[F(0)] * 4 for _ in range(4)]
            TH[0][0] = F(1)
            for k in range(3):
                TH[k + 1][k + 1] = A[k]
            fld = gtg.Field(TH)
            ok = ok and fld.torsion_free() and fld.Omega(0) == {}
            for i in range(3):
                want = GA.scal(F(0) - A[i].d(0).v, gtg.biv(0, i + 1))
                for j in range(3):
                    if j != i:
                        want = GA.add(want, GA.scal(F(0) - A[i].d(j + 1).v / A[j].v, gtg.biv(i + 1, j + 1)))
                ok = ok and GA.eq(fld.Omega(i + 1), want)
            Rc = fld.curvature()
            row = []
            for i in range(3):
                e0R = GA.dot(GA.gen(0), gtg.ricci(Rc, GA.gen(i + 1)), gtg.S13)
                ratio = [(A[k].d(i + 1) / A[i]) for k in range(3)]
                boost = sum(((ratio[k].d(0)).v / A[k].v for k in range(3) if k != i), F(0))
                ok = ok and e0R == boost
                tR = F(0) - tau0 * A[i].v * e0R                 # tau R_0i, round-sphere-positive sign
                pv = [x.v for x in p]
                dpi = [x.d(i + 1).v for x in p]
                want = dpi[i] + sum((pv[i] - pv[j]) * db[j][i] for j in range(3))
                ok = ok and tR == want
                row.append(tR)
            results.append(row)
            ok = ok and sum(x.v for x in p) == 1 and sum(x.v * x.v for x in p) == 1
        ok = ok and results[0] == results[1] and any(x != 0 for x in results[0])
    # (i) the tangent t = (1,1,1) x p is the dual -I3 ((1,1,1) ^ p) in Cl(3,0)
    sq3 = GA.sig(3, 0)
    I3 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), sq3), GA.gen(2), sq3)
    for pr in ((F(-1, 3), F(2, 3), F(2, 3)), (F(-2, 7), F(3, 7), F(6, 7))):
        uvec = GA.add(GA.gen(0), GA.gen(1), GA.gen(2))
        pvec = GA.add(*[GA.scal(pr[k], GA.gen(k)) for k in range(3)])
        w = GA.scal(F(1, 2), GA.sub(GA.mul(uvec, pvec, sq3), GA.mul(pvec, uvec, sq3)))
        t = GA.neg(GA.mul(I3, w, sq3))
        ok = ok and GA.eq(t, GA.add(GA.scal(pr[2] - pr[1], GA.gen(0)), GA.scal(pr[0] - pr[2], GA.gen(1)),
                                    GA.scal(pr[1] - pr[0], GA.gen(2))))
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_rotation_gauge_field_and_mixed_ricci"; return _tp_rv
