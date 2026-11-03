"""interior.exact-parallelism-convergence-rate: exact checks in Gauge Theory Gravity.

The Schwarzschild interior field of the premise Lemma (synchronous gauge, labels (r, t, theta, phi), 2M = 1):
hb^{-1}(e_r) = A^{-1/2} gamma0, hb^{-1}(e_t) = sqrt(A) gamma1, hb^{-1}(e_theta) = r gamma2,
hb^{-1}(e_phi) = r sin(theta) gamma3, A = 1/r - 1; e_0 = g_tau = gamma0 and (e_1, e_2, e_3) = (gamma1, gamma2,
gamma3) are the normalised g_t, g_theta, g_phi. Omega in the Definition's sign. Exact jets at rational points.
(1) Omega satisfies the torsion equation (rank 24: unique) and (e_0 . D) e_b = 0 for b = 0..3 at every sample
    radius (several tau): the frame is exactly D-parallel along the free-fall worldlines; control: it is not
    parallel along e_1 ((e_1 . D) e_0 != 0). sigma_1 = d_tau log sqrt(A) = d_r sqrt(A) and sigma_2 = sqrt(A)/r
    from the jets equal -(1/2) r^{-3/2} (1 - r)^{-1/2} and r^{-3/2} sqrt(1 - r), and Omega(e_1) = -sigma_1 e_0 ^ e_1.
(2) tau sigma_1 = -1/3 - (4/15) R + O(R^2) and tau sigma_2 = 2/3 - (2/15) R + O(R^2), peeled by exact series
    division against R(rho) (residual starts at rho^6, i.e. R^3).
(3) One rate: the relative deviations from the Kasner model, as series in rho = sqrt(r) (tau ~ rho^3), all start
    at rho^2 (O(tau^{2/3})) with nonzero, hence one-signed, leading coefficients: scale factors
    sqrt(1 - r) S^{1/3} - 1 (coefficient -2/5) and S^{-2/3} - 1 (-1/5), with S = tau/((2/3) r^{3/2}); rates
    tau sigma_1 + 1/3 (-4/15) and tau sigma_2 - 2/3 (-2/15); sphere curvature r^{-2} against tau^{-2}:
    tau^2/r^2 (4/9). The sphere rotation coefficient Hubble-normalised, tau cot(theta)/r, starts at rho^1:
    O(tau^{1/3}).
"""
from fractions import Fraction as F

import GA
import gtg
import series
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (jets, multivectors with jet coefficients, Field, torsion, curvature) ----
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
           (F(4, 5), F(1, 2), F(4, 5), F(3, 5)), (F(1, 10), F(3), F(3, 5), F(4, 5))]


def check_frame_exactly_parallel():
    premise("interior.kasner-form-interior")
    ok = True
    for r0, w, s0, c0 in SAMPLES:
        fld, lam, (r, A, sA, s1, s2, sn, cs) = interior_field(r0, w, s0, c0)
        ok = ok and lam == 0 and fld.torsion_free() and fld.torsion_rank() == 24
        for b in range(4):
            ok = ok and fld.cov_phys([F(1), F(0), F(0), F(0)], {(b,): J(1)}) == {}
        ok = ok and fld.cov_phys([F(0), F(1), F(0), F(0)], {(0,): J(1)}) != {}
        # sigma_1 = d_tau log sqrt(A) = sqrt(A) d_r sqrt(A)/sqrt(A) = d_r sqrt(A); closed forms (exact squares)
        ok = ok and s1.v == sA.g[0]
        ok = ok and (4 * s1.v * s1.v) * r0 ** 3 * (1 - r0) == 1 and s1.v < 0
        ok = ok and s2.v * s2.v * r0 ** 3 == 1 - r0 and s2.v > 0
        ok = ok and m_val(fld.om[1]) == {(0, 1): -s1.v}
    _tp_rv = (ok); assert _tp_rv is not False, "check_frame_exactly_parallel"; return _tp_rv


def check_rates_converge_to_kasner_exponents():
    premise("interior.kasner-form-interior")
    tau = tau_series(0)
    ts1, ts2 = rate_series(0, tau)
    R = r_of_R(tau)
    a0, a1, ra = peel_in_R(ts1, R)
    b0, b1, rb = peel_in_R(ts2, R)
    ok = (a0, a1, b0, b1) == (F(-1, 3), F(-4, 15), F(2, 3), F(-2, 15))
    ok = ok and all(ra[k] == 0 for k in range(6)) and ra[6] != 0
    ok = ok and all(rb[k] == 0 for k in range(6)) and rb[6] != 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_rates_converge_to_kasner_exponents"; return _tp_rv


def check_one_uniform_rate():
    premise("interior.kasner-form-interior")
    tau = tau_series(0)
    lt = lead(tau)
    S = GA.ps_trunc([F(3, 2) * tau[3 + k] for k in range(NS - 2)], NS)          # S(rho), S(0) = 1
    sq1 = GA.ps_pow_rat([F(1), F(0), F(-1)], F(1, 2), NS)
    dev_a1 = GA.ps_mul(sq1, GA.ps_pow_rat(S, F(1, 3), NS), NS)
    dev_a2 = GA.ps_pow_rat(S, F(-2, 3), NS)
    ts1, ts2 = rate_series(0, tau)
    curv = GA.ps_mul([F(0), F(0), F(4, 9)], GA.ps_mul(S, S, NS), NS)          # tau^2/r^2 = (4/9) r S^2
    devs = [(dev_a1, 1, F(-2, 5)), (dev_a2, 1, F(-1, 5)), (ts1, F(-1, 3), F(-4, 15)), (ts2, F(2, 3), F(-2, 15)),
            (curv, 0, F(4, 9))]
    ok = True
    for ser, base, c in devs:
        d = [ser[k] - (base if k == 0 else 0) for k in range(len(ser))]
        ok = ok and lead(d) == 2 and d[2] == c and F(lead(d), lt) == F(2, 3)
    rot = [F(0)] + S[:NS]                     # tau/r = (2/3) rho S: times cot(theta), leading order rho^1
    ok = ok and lead(rot) == 1 and F(lead(rot), lt) == F(1, 3)
    _tp_rv = (ok); assert _tp_rv is not False, "check_one_uniform_rate"; return _tp_rv
