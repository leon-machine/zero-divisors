"""interior.schwarzschild-lines-exactly: exact checks in Gauge Theory Gravity.

The Schwarzschild interior field (labels (r, t, theta, phi), 2M = 1) of the premise Lemmas, with Omega in the
Definition's sign: Omega(e_3) = -sigma_3 B_3 + (cot(theta)/r) R_23, B_3 = e_0 ^ e_3, R_23 = e_2 ^ e_3, computed
as the torsion-free field. The Hubble-normalised generator on the unit direction e_3 is therefore
tau Omega(e_3) = -(2/3 + delta) B_3 + epsilon R_23, the statement's G, with model -(2/3) B_3. The norms, the
series and the bound do not depend on the sign of the B_3 term.
(1) Constancy along a phi-line: every jet of the field (coframe and Omega) has zero phi-derivative, the unit
    tangent e_3 = g_phi/|g_phi| has phi-independent components, and Omega(e_3) has exactly the two entries
    -sigma_3 on B_3 and cot(theta)/r on R_23; the transport is one exponential.
(2) Series: S(r) = 1 + (3/10) r + (9/56) r^2 + (5/48) r^3 + ...; delta = (2/3) S sqrt(1 - r) - 2/3 =
    -(2/15) r - (8/105) r^2 - (16/315) r^3 - ..., every coefficient through r^8 negative; epsilon =
    tau cot(theta)/r = (2/3) cot(theta) r^{1/2} S(r) at cot(theta) = 3/4 (built from tau(rho) by a second route).
(3) The comparison: e^X - e^Y = int_0^1 e^{(1-t)X} (X - Y) e^{tY} dt holds coefficient by coefficient in
    lambda through order 7 for X = lambda G, Y = lambda (2/3) B_3 (matrices on physical vectors, both signs of
    the B_3 term); ||B_3|| = ||R_23|| = 1 (B^T B a nonzero projector) and ||delta B_3 + epsilon R_23||^2 <=
    (|delta| + |epsilon|)^2 (the difference of Gram matrices is positive semidefinite, exact congruence signature).
(4) Rates: delta starts at rho^2 and epsilon at rho^1 against tau at rho^3: O(tau^{2/3}) and O(tau^{1/3}).
"""
from fractions import Fraction as F

import GA
import gtg
import series
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (jets, multivectors with jet coefficients, Field, torsion) ----
m_val, bdot, gbiv = gtg.m_val, gtg.bdot, gtg.biv
# the Schwarzschild(-de Sitter) interior field in synchronous gauge, labels (r, t, theta, phi), 2M = 1:
# interior_field(r0, w, s0, c0) -> (field, Lambda, (r, A, sA, s1, s2, sn, cs))
interior_field = gtg.sync_interior_field
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


lead = series.ps_valuation                 # first nonzero index
# ---- end of series ----

SAMPLES = [(F(1, 2), F(1), F(3, 5), F(4, 5)), (F(1, 5), F(2), F(5, 13), F(12, 13))]
NR = 8
DE = [(F(-1, 10), F(1, 4)), (F(-1, 50), F(-1, 7)), (F(-2, 15), F(3, 5))]


def act(B):
    cols = []
    for j in range(4):
        v = bdot(B, GA.gen(j))
        cols.append([v.get((i,), F(0)) for i in range(4)])
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def madd(A, B, c=1):
    return [[a + c * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def meye():
    return [[F(1 if i == j else 0) for j in range(4)] for i in range(4)]


def check_phi_line_generator_constant():
    premise("interior.interior-connection-exactly")
    ok = True
    for r0, w, s0, c0 in SAMPLES:
        fld, lam, (r, A, sA, s1, s2, sn, cs) = interior_field(r0, w, s0, c0)
        ok = ok and fld.torsion_free() and fld.torsion_rank() == 24
        ok = ok and all(c.g[3] == 0 for row in fld.TH for c in row)
        ok = ok and all(c.g[3] == 0 for om in fld.om for c in om.values())
        ok = ok and m_val(fld.g[3]) == {(3,): r0 * s0}
        ok = ok and m_val(fld.om[3]) == {(0, 3): -s2.v, (2, 3): c0 / (s0 * r0)}
        ok = ok and s2.v * s2.v * r0 ** 3 == 1 - r0
    _tp_rv = (ok); assert _tp_rv is not False, "check_phi_line_generator_constant"; return _tp_rv


def check_delta_epsilon_series():
    premise("interior.kasner-form-interior")
    premise("interior.exact-parallelism-convergence-rate")
    inv_sqrt = GA.ps_pow_rat([F(1), F(-1)], F(-1, 2), NR)
    S = [F(3, 2) * inv_sqrt[k] / (k + F(3, 2)) for k in range(NR + 1)]
    ok = S[:4] == [F(1), F(3, 10), F(9, 56), F(5, 48)]
    d = [F(2, 3) * c for c in GA.ps_mul(S, GA.ps_pow_rat([F(1), F(-1)], F(1, 2), NR), NR)]
    d[0] -= F(2, 3)
    ok = ok and d[0] == 0 and d[1:4] == [F(-2, 15), F(-8, 105), F(-16, 315)]
    ok = ok and all(d[k] < 0 for k in range(1, NR + 1))
    cot = F(3, 4)
    tau = tau_series(0)
    eps_rho = [cot * tau[k + 2] for k in range(len(tau) - 2)]
    ok = ok and eps_rho[0] == 0 and all(eps_rho[2 * k] == 0 for k in range(4))
    ok = ok and all(eps_rho[2 * k + 1] == F(2, 3) * cot * S[k] for k in range(4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_delta_epsilon_series"; return _tp_rv


def check_exponential_comparison():
    premise("interior.transport-level-convergence-along-tangential-curves")
    B3, R23 = act(gbiv(0, 3)), act(gbiv(2, 3))
    ok = True
    for M in (B3, R23):
        X = GA.mat_mul([list(r) for r in zip(*M)], M)
        ok = ok and GA.mat_mul(X, X) == X and X != [[F(0)] * 4 for _ in range(4)]
    N = 7
    for dl, ep in DE:
        diff = madd([[dl * x for x in r] for r in B3], [[ep * x for x in r] for r in R23])
        Xd = GA.mat_mul([list(r) for r in zip(*diff)], diff)
        bound = (abs(dl) + abs(ep)) ** 2
        ok = ok and GA.congruence_signature(madd([[bound * x for x in r] for r in meye()], Xd, -1))[1] == 0
        for sgn in (1, -1):
            G0 = [[sgn * F(2, 3) * x for x in r] for r in B3]
            G = madd(G0, diff if sgn == 1 else madd([[-dl * x for x in r] for r in B3],
                                                       [[ep * x for x in r] for r in R23]))
            Gp, G0p = [meye()], [meye()]
            for k in range(N):
                Gp.append(GA.mat_mul(G, Gp[-1]))
                G0p.append(GA.mat_mul(G0, G0p[-1]))
            fact = [1]
            for k in range(1, N + 2):
                fact.append(fact[-1] * k)
            D = madd(G, G0, -1)
            for n in range(1, N + 1):
                lhs = [[x / fact[n] for x in r] for r in madd(Gp[n], G0p[n], -1)]
                rhs = [[F(0)] * 4 for _ in range(4)]
                for a in range(n):
                    b = n - 1 - a
                    beta = F(fact[a] * fact[b], fact[a + b + 1])          # int_0^1 (1-t)^a t^b dt
                    term = GA.mat_mul(GA.mat_mul(Gp[a], D), G0p[b])
                    rhs = madd(rhs, [[beta * x / (fact[a] * fact[b]) for x in r] for r in term])
                ok = ok and lhs == rhs
    _tp_rv = (ok); assert _tp_rv is not False, "check_exponential_comparison"; return _tp_rv


def check_rates_in_tau():
    premise("interior.kasner-form-interior")
    tau = tau_series(0)
    ts1, ts2 = rate_series(0, tau)
    d = [ts2[k] - (F(2, 3) if k == 0 else 0) for k in range(len(ts2))]
    eps = [tau[k + 2] for k in range(len(tau) - 2)]
    ok = lead(tau) == 3 and F(lead(d), lead(tau)) == F(2, 3) and F(lead(eps), lead(tau)) == F(1, 3)
    _tp_rv = (ok); assert _tp_rv is not False, "check_rates_in_tau"; return _tp_rv
