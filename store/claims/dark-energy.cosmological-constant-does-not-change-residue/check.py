"""dark-energy.cosmological-constant-does-not-change-residue: exact checks in Gauge Theory Gravity.

(1) The field equations of the diagonal Bianchi I field. Flat background Cl(1,3), labels (tau, x1, x2, x3);
    hb^{-1}(e_tau) = gamma0, hb^{-1}(e_i) = a_i(tau) gamma_i; Omega(gamma_i) = -H_i gamma_0 ^ gamma_i,
    Omega(gamma_0) = 0 (the Definition's sign). At random rational jets (a_i, H_i = a_i'/a_i, H_i'), Omega is the
    torsion-free field (rank 24), and the store's curvature calR(B) = -R(hb(B)) computed from Omega has Ricci
    calR(gamma_i) = (H_i' + H_i sum_j H_j) gamma_i and calR(gamma_0) = (sum H_i' + sum H_i^2) gamma_0, so
    calR(a) = Lambda a is exactly the three evolution equations plus the 00 equation, and
    sum_i (evolution_i) - (00 equation) = 2 sum_{i<j} H_i H_j: given the evolution equations, the 00 equation is
    the constraint sum_{i<j} H_i H_j = Lambda. de Sitter data (H_i = H, 3H^2 = Lambda) give calR(a) = Lambda a.
(2) The formal series H_i = p_i/tau + sum_n h_{i,n} tau^{2n-1}, solved by the proof's recursion with Lambda an
    indeterminate (rational functions, GA.RF), at five rational Kasner points: h_{i,1} = Lambda (1 - p_i)/2;
    h_{i,2} is a polynomial in Lambda (degree 2); the residuals of the evolution equations and of the constraint
    vanish identically through tau^4 (the constraint is not imposed); at (-1/3, 2/3, 2/3) with Lambda = 3,
    h_{i,1} = (2, 1/2, 1/2) and h_{i,2} = (-33/20, -3/40, -3/40). Uniqueness and oddness: the order-n system
    2n h + p sum h has determinant (2n)^2 (2n + 1) != 0 and the even-power system (2n+1) c + p sum c has
    determinant (2n+1)^2 (2n+2) != 0 (computed). Constraint propagation: d/dtau C = 2S(Lambda - C) under the
    evolution equations (polynomial identity, checked on a 4^4 grid, degree <= 3 in each variable).
(3) The Schwarzschild-de Sitter wall: with c = Lambda/3 at three values the interior rates tau sigma_i have the
    same tau^0 coefficients (-1/3, 2/3) as at Lambda = 0, which satisfy the Kasner relations: the residue is the
    Kasner boost of the Lambda = 0 approach.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (jets, multivectors with jet coefficients, Field, torsion, curvature) ----
J, Field = gtg.J, gtg.Field


def ricci(Rc, b):
    """calR(gamma_b) = sum_a gamma^a . calR(gamma_a ^ gamma_b) (b an index)."""
    return gtg.ricci(Rc, GA.gen(b))
# ---- exact series of the (Schwarzschild-de Sitter) interior in rho = sqrt(r), 2M = 1 ----
NS = 12


def tau_series(c, N=NS):
    """tau(rho) = int_0^r A^{-1/2} du, A = (1 - u + c u^3)/u (c = Lambda/3), as a series in rho = sqrt(r):
    d tau = 2 rho^2 (1 - rho^2 + c rho^6)^{-1/2} d rho."""
    fac = [F(1), F(0), F(-1), F(0), F(0), F(0), F(c)]
    half = GA.ps_pow_rat(fac, F(-1, 2), N)
    return GA.ps_int(GA.ps_mul([F(0), F(0), F(2)], half, N))[:N + 1]


def rate_series(c, tau, N=NS):
    """(tau sigma_1, tau sigma_2) as series in rho, sigma_1 = d_tau log sqrt(A) = A'/(2 sqrt A),
    sigma_2 = d_tau log r = sqrt(A)/r."""
    fac = [F(1), F(0), F(-1), F(0), F(0), F(0), F(c)]
    inv_sqrt = GA.ps_pow_rat(fac, F(-1, 2), N)
    t3 = GA.ps_trunc([tau[3 + k] for k in range(N - 2)], N)
    ts1 = GA.ps_mul(GA.ps_mul(t3, [F(-1, 2), F(0), F(0), F(0), F(0), F(0), F(c)], N), inv_sqrt, N)
    ts2 = GA.ps_mul(t3, GA.ps_pow_rat(fac, F(1, 2), N), N)
    return ts1, ts2


def r_of_R(tau, N=NS):
    """R = (3 tau/2)^{2/3} as a series in rho (R = rho^2 (1 + ...))."""
    U = [tau[3 + k] * F(3, 2) for k in range(N - 2)]
    return GA.ps_trunc([F(0), F(0)] + GA.ps_pow_rat(GA.ps_trunc(U, N), F(2, 3), N), N)


def peel_in_R(ts, Rser, N=NS):
    """(c0, c1, residual) with ts = c0 + c1 R + c2 R^2 + residual, by exact division against R(rho)."""
    Rsq = GA.ps_mul(Rser, Rser, N)
    c0 = ts[0]
    r1 = [ts[k] - (c0 if k == 0 else F(0)) for k in range(N + 1)]
    c1 = r1[2] / Rser[2]
    r2 = [r1[k] - c1 * Rser[k] for k in range(N + 1)]
    c2 = r2[4] / Rsq[4]
    r3 = [r2[k] - c2 * Rsq[k] for k in range(N + 1)]
    return c0, c1, r3

# ---- end of series ----

JETS = [((F(2), F(3), F(1, 2)), (F(1, 3), F(-2), F(5, 4)), (F(7), F(1, 5), F(-3))),
        ((F(1), F(5, 2), F(4)), (F(-1, 2), F(2, 3), F(1)), (F(0), F(-4), F(2, 7)))]
KASNER_T = [F(1), F(2), F(1, 2), F(-3), F(5, 3)]
GRID = [F(-1), F(0), F(1, 2), F(3)]


def bianchi_field(a, H, Hd):
    TH = [[J(0)] * 4 for _ in range(4)]
    TH[0][0] = J(1)
    om = [{}]
    for i in range(3):
        TH[i + 1][i + 1] = J(a[i], (a[i] * H[i], 0, 0, 0))
        om.append({(0, i + 1): J(-H[i], (-Hd[i], 0, 0, 0))})
    return Field(TH, om)


def kasner_point(t):
    d = 1 + t * t + t
    return [-t / d, (1 + t) / d, t * (1 + t) / d]


def K(x):
    return GA.RF.const(x)


def bianchi_series(p, lam, order):
    """H_i as {power: coefficient}; coefficients rational functions of the indeterminate (or constant) lam."""
    zero = K(0)
    H = [{-1: K(p[i])} for i in range(3)]
    for n in range(1, order + 1):
        k = 2 * n - 1
        known = []
        for i in range(3):
            tot = zero
            for a, ca in H[i].items():
                for j in range(3):
                    for b, cb in H[j].items():
                        if a + b == k - 1:
                            tot = tot + ca * cb
            known.append(tot)
        rhs = [(lam if k == 1 else zero) - known[i] for i in range(3)]
        Hn = (rhs[0] + rhs[1] + rhs[2]) * K(F(1, k + 2))
        for i in range(3):
            H[i][k] = (rhs[i] - Hn * K(p[i])) * K(F(1, k + 1))
    return H


def residuals(H, lam, maxpow):
    zero = K(0)
    res = []
    for i in range(3):
        r = {}
        for a, ca in H[i].items():
            if a != 0:
                r[a - 1] = r.get(a - 1, zero) + ca * K(a)
            for j in range(3):
                for b, cb in H[j].items():
                    r[a + b] = r.get(a + b, zero) + ca * cb
        r[0] = r.get(0, zero) - lam
        res.append([k for k, v in r.items() if k <= maxpow and not v.is_zero()])
    C = {}
    for i in range(3):
        for j in range(i + 1, 3):
            for a, ca in H[i].items():
                for b, cb in H[j].items():
                    C[a + b] = C.get(a + b, zero) + ca * cb
    C[0] = C.get(0, zero) - lam
    return res, [k for k, v in C.items() if k <= maxpow and not v.is_zero()]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def check_field_equations_of_the_bianchi_field():
    ok = True
    for a, H, Hd in JETS:
        fld = bianchi_field(a, H, Hd)
        ok = ok and fld.torsion_free() and fld.torsion_rank() == 24
        Rc = fld.curvature()
        S = sum(H)
        ric = [ricci(Rc, b) for b in range(4)]
        c0 = sum(Hd) + sum(h * h for h in H)
        ci = [Hd[i] + H[i] * S for i in range(3)]
        ok = ok and GA.eq(ric[0], GA.scal(c0, GA.gen(0)))
        ok = ok and all(GA.eq(ric[i + 1], GA.scal(ci[i], GA.gen(i + 1))) for i in range(3))
        ok = ok and sum(ci) - c0 == 2 * (H[0] * H[1] + H[0] * H[2] + H[1] * H[2])
    for Hh, lam in ((F(1), F(3)), (F(2, 3), F(4, 3))):
        fld = bianchi_field((F(1), F(2), F(3)), (Hh, Hh, Hh), (F(0), F(0), F(0)))
        Rc = fld.curvature()
        ok = ok and all(GA.eq(ricci(Rc, b), GA.scal(lam, GA.gen(b))) for b in range(4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_field_equations_of_the_bianchi_field"; return _tp_rv


def check_unique_odd_formal_solution():
    lamv = GA.RF.var()
    ok = True
    for t in KASNER_T:
        p = kasner_point(t)
        ok = ok and sum(p) == 1 and sum(x * x for x in p) == 1
        H = bianchi_series(p, lamv, 3)
        ok = ok and all(H[i][1].eqrf(lamv * GA.RF.const((1 - p[i]) / 2)) for i in range(3))
        ok = ok and all(len(H[i][3].den) == 1 and len(H[i][3].num) <= 3 for i in range(3))
        res, C = residuals(H, lamv, 4)
        ok = ok and all(r == [] for r in res) and C == []
        for n in (1, 2, 3):
            Mo = [[(2 * n if i == j else 0) + p[i] for j in range(3)] for i in range(3)]
            Me = [[(2 * n + 1 if i == j else 0) + p[i] for j in range(3)] for i in range(3)]
            ok = ok and det3(Mo) == (2 * n) ** 2 * (2 * n + 1) and det3(Me) == (2 * n + 1) ** 2 * (2 * n + 2)
    Hs = bianchi_series([F(-1, 3), F(2, 3), F(2, 3)], GA.RF.const(3), 2)
    ok = ok and [Hs[i][1].eval(0) for i in range(3)] == [F(2), F(1, 2), F(1, 2)]
    ok = ok and [Hs[i][3].eval(0) for i in range(3)] == [F(-33, 20), F(-3, 40), F(-3, 40)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_unique_odd_formal_solution"; return _tp_rv


def check_constraint_propagates():
    ok = True
    for h1 in GRID:
        for h2 in GRID:
            for h3 in GRID:
                for lam in GRID:
                    H = (h1, h2, h3)
                    S = sum(H)
                    Hd = [lam - h * S for h in H]
                    Cd = sum(Hd[i] * H[j] + H[i] * Hd[j] for i in range(3) for j in range(i + 1, 3))
                    C = H[0] * H[1] + H[0] * H[2] + H[1] * H[2]
                    ok = ok and Cd == 2 * S * (lam - C)
    _tp_rv = (ok); assert _tp_rv is not False, "check_constraint_propagates"; return _tp_rv


def check_schwarzschild_de_sitter_residue_unchanged():
    premise("interior.schwarzschild-de-sitter-weighted-limit")
    premise("dark-energy.imported-weighted-limit-schwarzschild-singularity-matching")
    s10, s20 = rate_series(0, tau_series(0))
    ok = (s10[0], s20[0]) == (F(-1, 3), F(2, 3))
    for c in (F(1), F(-2), F(5, 7)):
        s1, s2 = rate_series(c, tau_series(c))
        p = (s1[0], s2[0], s2[0])
        ok = ok and p == (s10[0], s20[0], s20[0]) and sum(p) == 1 and sum(x * x for x in p) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_schwarzschild_de_sitter_residue_unchanged"; return _tp_rv
