"""interior.kasner-form-interior: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)), labels (r, t, theta, phi) as background coordinates, 2M = 1.
The Schwarzschild interior field in synchronous position gauge: hb^{-1}(e_r) = A^{-1/2} gamma0 (so the physical
displacement along r is d tau gamma0), hb^{-1}(e_t) = sqrt(A) gamma1, hb^{-1}(e_theta) = r gamma2,
hb^{-1}(e_phi) = r sin(theta) gamma3, A = 1/r - 1 = -f with f = 1 - 2M/r the static function of the premise;
Omega in the Definition's sign. Exact first-order jets at rational points where sqrt(A), sin, cos are rational.
(1) The derived metric g_mu . g_nu is diag(1/A, -A, -r^2, -r^2 sin^2 theta): d tau^2 - A dt^2 - r^2 dOmega^2 with
    d tau = A^{-1/2} dr; Omega satisfies the torsion equation and the torsion map has rank 24 (so it is the
    rotation-gauge field); the velocity hb^{-1}(x') = gamma0 of the worldlines of constant (t, theta, phi) has
    Q = 1 and is D-parallel along itself, (gamma0 . D) gamma0 = 0.
(2) tau(r) = int_0^r A^{-1/2} as an exact series in rho = sqrt(r): (2/3) rho^3 + (1/5) rho^5 + (3/28) rho^7 + ...,
    so tau = (2/3) r^{3/2}(1 + (3/10) r + O(r^2)); R = (3 tau/2)^{2/3} = r (1 + r/5 + O(r^2)) and
    r = R - R^2/5 + O(R^3) (residual starts at rho^6).
(3) Exponents: sqrt(A) has leading order rho^{-1} and r has rho^2 against tau's rho^3, so sqrt(A) ~ tau^{-1/3}
    and r ~ tau^{2/3}; the computed rate limits tau d_tau log a_i are (-1/3, 2/3, 2/3), with sum 1 and sum of
    squares 1.
"""
from fractions import Fraction as F

import GA
import gtg
import series
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (jets, multivectors with jet coefficients, Field, torsion, curvature) ----
S13 = gtg.S13
J, m_val = gtg.J, gtg.m_val
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

SAMPLES = [(F(1, 2), F(1), F(3, 5), F(4, 5)), (F(1, 5), F(2), F(5, 13), F(12, 13)),
           (F(4, 5), F(1, 2), F(4, 5), F(3, 5))]


def check_synchronous_derived_metric_and_free_fall():
    premise("interior.imported-schwarzschild-curvature-spectrum")
    ok = True
    for r0, w, s0, c0 in SAMPLES:
        fld, lam, (r, A, sA, s1, s2, sn, cs) = interior_field(r0, w, s0, c0)
        ok = ok and lam == 0 and A.v == 2 * F(1, 2) / r0 - 1
        f = 1 - 2 * F(1, 2) / r0
        gram = [[GA.dot(m_val(fld.g[m]), m_val(fld.g[n]), S13) for n in range(4)] for m in range(4)]
        want = [[-1 / f, 0, 0, 0], [0, f, 0, 0], [0, 0, -r0 * r0, 0], [0, 0, 0, -r0 * r0 * s0 * s0]]
        ok = ok and gram == want
        ok = ok and fld.torsion_free() and fld.torsion_rank() == 24
        g0 = {(0,): J(1)}
        ok = ok and GA.dot(m_val(g0), m_val(g0), S13) == 1
        ok = ok and fld.cov_phys([F(1), F(0), F(0), F(0)], g0) == {}
    _tp_rv = (ok); assert _tp_rv is not False, "check_synchronous_derived_metric_and_free_fall"; return _tp_rv


def check_tau_series_and_inversion():
    tau = tau_series(0)
    ok = tau[3] == F(2, 3) and tau[5] == F(1, 5) and tau[7] == F(3, 28)
    ok = ok and all(tau[k] == 0 for k in (0, 1, 2, 4, 6))
    ok = ok and tau[5] / tau[3] == F(3, 10)
    R = r_of_R(tau)
    ok = ok and R[2] == 1 and R[3] == 0 and R[4] == F(1, 5)
    R2_ = GA.ps_mul(R, R, NS)
    resid = [R[k] - F(1, 5) * R2_[k] - (1 if k == 2 else 0) for k in range(NS + 1)]
    ok = ok and all(resid[k] == 0 for k in range(6)) and resid[6] != 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_tau_series_and_inversion"; return _tp_rv


def check_kasner_exponents_of_the_approach():
    premise("interior.imported-schwarzschild-curvature-spectrum")
    tau = tau_series(0)
    # rho * sqrt(A) = sqrt(1 - rho^2) and r = rho^2: leading orders -1 and 2 against tau's 3
    rhoA = GA.ps_pow_rat([F(1), F(0), F(-1)], F(1, 2), NS)
    lt = lead(tau)
    pA, pr = F(-1 + lead(rhoA), lt), F(2, lt)
    ts1, ts2 = rate_series(0, tau)
    p = (ts1[0], ts2[0], ts2[0])
    ok = (pA, pr, pr) == p == (F(-1, 3), F(2, 3), F(2, 3))
    ok = ok and sum(p) == 1 and sum(x * x for x in p) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_kasner_exponents_of_the_approach"; return _tp_rv
