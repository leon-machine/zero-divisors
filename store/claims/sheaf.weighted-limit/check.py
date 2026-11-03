"""sheaf.weighted-limit: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)), 2M = 1. The Schwarzschild interior field in synchronous gauge is
taken from the premise check interior.interior-connection-exactly (EXPORTS: labels (r, t, theta, phi),
hb^{-1}(e_r) = N gamma0 with N = sqrt(r/(1 - r)), hb^{-1}(e_t) = sqrt(A) gamma1, A = (1 - r)/r, angular
r gamma2, r sin(theta) gamma3; exact first-order jets at rational points). Computed:
(1) the derived metric g(e_mu, e_nu) = hb^{-1}(e_mu) . hb^{-1}(e_nu) is diag(r/(1 - r), -A, -r^2,
    -r^2 sin^2(theta)), i.e. d tau^2 - A dt^2 - r^2 dOmega^2 with d tau = N dr; the exact series
    tau = int_0^r sqrt(s/(1 - s)) ds = (2/3) r^{3/2} (1 + (3/10) r + O(r^2));
(2) the frame is exactly D-parallel along g_tau (Omega(e_0) = 0, so (e_0 . D) e_a = 0), the field is
    torsion-free, and Omega(e_i) = sigma_i e_i ^ e_0 plus the sphere term (cot(theta)/r) e_2 ^ e_3 on e_3
    (the boost sign as in the Definition's convention; see the premise check);
(3) Hubble-normalised rates as exact series in u = sqrt(r): tau sigma_1 = -1/3 - (4/15) r + O(r^2),
    tau sigma_2 = 2/3 - (2/15) r + O(r^2), only even powers, and R = (3 tau/2)^{2/3} = r + O(r^2), so the
    stated expansions in R hold;
(4) the admissible class, on its exactly solvable member and at the values level: the Kasner field with
    (-1/3, 2/3, 2/3) (and permutations) is Ricci-flat (Einstein with Lambda = 0), torsion-free, with
    tau Omega(e_i) = p_i e_i ^ e_0 exactly (E_tau = 0), and for every constant triple with all p_i != 0 in a
    grid the values p_i B_i generate a Lie algebra of dimension 6 = dim so(1,3) (3 with one zero, 1 with
    two zeros). The existence of the limit for the general admissible field (the integrability argument)
    and the extension of the parallel tractor are cited (T6 Thm 5.6) and not recomputed.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13
J = gtg.J
gbiv = gtg.biv                          # gamma_a gamma_b


def m_val(x):
    """Values of a jet multivector. Local (not gtg.m_val) because the fields come from the premise's EXPORTS,
    whose jets may be the premise's own class until that check is migrated."""
    return {b: c.v for b, c in x.items() if c.v != 0}
# ---- end of engine ----


# ---- the synchronous diagonal (Kasner) field on flat spacetime ----
def kasner_field(p, t0):
    """hb^{-1}(e_t) = gamma0, hb^{-1}(e_i) = t^{p_i} gamma_i (labels (t, x1, x2, x3)) at t = t0, with the rotation-gauge
    field Omega(e_i) = (p_i/t) e_i ^ e_0 of the Definition's convention (gtg.synchronous_field)."""
    t = J.var(0, t0, 4, 2)
    return gtg.synchronous_field([t.pw(x) for x in p])


def ricci(Rc, b):
    """calR(gamma_b) = sum_a gamma^a . calR(gamma_a ^ gamma_b), b a frame index."""
    return gtg.ricci(Rc, GA.gen(b))


# ---- exact series of the Schwarzschild interior (2M = 1) in u = sqrt(r) ----
NS = 8


def interior_series(N=NS):
    """tau(u) = int_0^r sqrt(s/(1-s)) ds = int 2 v^2 (1 - v^2)^{-1/2} dv; returns (tau, tau sigma_1,
    tau sigma_2, R/u^2, tau/r) as coefficient lists in u, with sigma_1 = -(1/2) r^{-3/2} (1 - r)^{-1/2},
    sigma_2 = r^{-3/2} (1 - r)^{1/2}, R = (3 tau/2)^{2/3}."""
    w = GA.ps_pow_rat([F(1), F(0), F(-1)], F(-1, 2), N)
    tau = GA.ps_int(GA.ps_mul([F(0), F(0), F(2)], w, N))
    t3 = GA.ps_trunc(tau[3:], N)
    ts1 = [-c / 2 for c in GA.ps_mul(w, t3, N)]
    ts2 = GA.ps_mul(GA.ps_pow_rat([F(1), F(0), F(-1)], F(1, 2), N), t3, N)
    Ru2 = GA.ps_pow_rat([F(3, 2) * c for c in t3], F(2, 3), N)
    tau_over_r = [F(0)] + t3[:N]
    return tau, ts1, ts2, Ru2, tau_over_r


lie_dim = gtg.lie_dim                    # dimension of the generated Lie algebra


SAMPLES = [(F(1, 2), F(3, 5), F(4, 5)), (F(1), F(5, 13), F(12, 13)), (F(2), F(4, 5), F(3, 5))]
KASNER = [(F(-1, 3), F(2, 3), F(2, 3)), (F(2, 3), F(-1, 3), F(2, 3)), (F(2, 3), F(2, 3), F(-1, 3))]
TIMES = [F(8), F(1, 27), F(64)]
GRID = [F(-2), F(-1, 3), F(1, 2), F(2, 3), F(3)]


def check_synchronous_derived_metric_and_tau():
    premise("interior.kasner-form-interior")
    field = premise("interior.interior-connection-exactly")["interior_field"]
    ok = True
    for k, s0, c0 in SAMPLES:
        fld, r0, _ = field(k, s0, c0)
        A = (1 - r0) / r0
        gram = [[GA.dot(m_val(fld.g[m]), m_val(fld.g[n]), S13) for n in range(4)] for m in range(4)]
        ok = ok and gram == [[r0 / (1 - r0), 0, 0, 0], [0, -A, 0, 0], [0, 0, -r0 * r0, 0], [0, 0, 0, -r0 * r0 * s0 * s0]]
    tau = interior_series()[0]
    _tp_rv = (ok and tau[:6] == [0, 0, 0, F(2, 3), 0, F(2, 3) * F(3, 10)]); assert _tp_rv is not False, "check_synchronous_derived_metric_and_tau"; return _tp_rv


def check_frame_parallel_and_connection_shape():
    premise("interior.exact-parallelism-convergence-rate")
    field = premise("interior.interior-connection-exactly")["interior_field"]
    ok = True
    for k, s0, c0 in SAMPLES:
        fld, r0, (r, N, sA, s1, s2, cs, sn) = field(k, s0, c0)
        ok = ok and fld.torsion_free() and m_val(fld.om[0]) == {}
        for i, s in ((1, s1), (2, s2)):
            ok = ok and GA.eq(m_val(fld.om[i]), GA.scal(-s.v, gbiv(0, i)))
        ok = ok and GA.eq(m_val(fld.om[3]), GA.add(GA.scal(-s2.v, gbiv(0, 3)), GA.scal(c0 / (s0 * r0), gbiv(2, 3))))
    _tp_rv = (ok); assert _tp_rv is not False, "check_frame_parallel_and_connection_shape"; return _tp_rv


def check_hubble_normalised_rates():
    premise("interior.exact-parallelism-convergence-rate")
    tau, ts1, ts2, Ru2, tor = interior_series()
    ok = ts1[0] == F(-1, 3) and ts1[2] == F(-4, 15) and ts2[0] == F(2, 3) and ts2[2] == F(-2, 15)
    ok = ok and all(ts1[j] == 0 and ts2[j] == 0 for j in range(1, NS, 2))
    _tp_rv = (ok and Ru2[0] == 1 and Ru2[1] == 0); assert _tp_rv is not False, "check_hubble_normalised_rates"; return _tp_rv


def check_weighted_limit_and_values_level_holonomy():
    premise("interior.weighted-limit-theorem")
    premise("interior.boosts-generate-exactly-levi-factor")
    ok = True
    for p in KASNER:
        ok = ok and sum(p) == 1 and sum(x * x for x in p) == 1
        for t0 in TIMES:
            fld = kasner_field(p, t0)
            ok = ok and fld.torsion_free() and all(ricci(fld.curvature(), b) == {} for b in range(4))
            for i in range(3):
                ok = ok and GA.eq(GA.scal(t0, m_val(fld.om[i + 1])), GA.scal(-p[i], gbiv(0, i + 1)))
    boosts = [gbiv(0, i) for i in (1, 2, 3)]
    for a in GRID:
        for b in GRID:
            for c in GRID:
                ok = ok and lie_dim([GA.scal(x, B) for x, B in zip((a, b, c), boosts)], S13) == 6
    ok = ok and lie_dim([boosts[0], boosts[1]], S13) == 3 and lie_dim([boosts[2]], S13) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_weighted_limit_and_values_level_holonomy"; return _tp_rv
