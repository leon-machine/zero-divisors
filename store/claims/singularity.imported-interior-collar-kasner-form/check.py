"""singularity.imported-interior-collar-kasner-form: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)), 2M = 1; the Schwarzschild interior field in synchronous gauge
from the premise check interior.interior-connection-exactly (EXPORTS; labels (r, t, theta, phi),
hb^{-1}(e_r) = N gamma0, N = sqrt(r/(1 - r)), hb^{-1}(e_t) = sqrt(A) gamma1, angular r gamma2,
r sin(theta) gamma3; exact first-order jets at rational points). Computed:
(1) the derived metric is d tau^2 - A dt^2 - r^2 dOmega^2 with A = 1/r - 1 (d tau = N dr), and the exact
    series tau = (2/3) r^{3/2}(1 + (3/10) r + O(r^2));
(2) the frame (e_0 = g_tau, e_1, e_2, e_3) is D-parallel along g_tau; on e_1 the rotation-gauge field is
    sigma_1 times the unit boost of the (t, r) plane, with sigma_1 = d_tau log sqrt(A) equal to the jet
    derivative (1/N) d_r log sqrt(A); the boost appears as sigma_1 e_1 ^ e_0 in the Definition's
    convention D_a = a . nabla + Omega(a) x (as the statement displays it, -sigma_1 B_1);
(3) tau sigma_1 = -1/3 - (4/15) R + O(R^2), tau sigma_2 = tau sigma_3 = 2/3 - (2/15) R + O(R^2) with
    R = (3 tau/2)^{2/3} = r + O(r^2) (exact series in sqrt r); the limits (-1/3, 2/3, 2/3) satisfy
    sum p = sum p^2 = 1;
(4) the three limiting boosts p_i B_i generate a Lie algebra of dimension 6 (so(1,3)) and pairwise do not
    commute ([B_i, B_j] is the rotation e_i e_j up to sign).
The exceptional-set clause is a description of the blow-up (T6 Def. 5.5) and is not computed.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13
gbiv = gtg.biv                          # gamma_a gamma_b


def m_val(x):
    """Values of a jet multivector. Local (not gtg.m_val) because the fields come from the premise's EXPORTS,
    whose jets may be the premise's own class until that check is migrated."""
    return {b: c.v for b, c in x.items() if c.v != 0}
# ---- end of engine ----


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


SAMPLES = [(F(1, 2), F(3, 5), F(4, 5)), (F(1, 3), F(5, 13), F(12, 13)), (F(3), F(4, 5), F(3, 5))]


def check_derived_metric_and_tau():
    premise("interior.kasner-form-interior")
    field = premise("interior.interior-connection-exactly")["interior_field"]
    ok = True
    for k, s0, c0 in SAMPLES:
        fld, r0, _ = field(k, s0, c0)
        g = [[GA.dot(m_val(fld.g[m]), m_val(fld.g[n]), S13) for n in range(4)] for m in range(4)]
        ok = ok and g[0][0] == r0 / (1 - r0) and g[1][1] == -(1 / r0 - 1) and g[2][2] == -r0 * r0
        ok = ok and g[3][3] == -(r0 * s0) ** 2 and all(g[m][n] == 0 for m in range(4) for n in range(4) if m != n)
    tau = interior_series()[0]
    _tp_rv = (ok and tau[3] == F(2, 3) and tau[5] / tau[3] == F(3, 10) and tau[4] == 0); assert _tp_rv is not False, "check_derived_metric_and_tau"; return _tp_rv


def check_parallel_frame_and_t_line_connection():
    premise("interior.exact-parallelism-convergence-rate")
    field = premise("interior.interior-connection-exactly")["interior_field"]
    ok = True
    for k, s0, c0 in SAMPLES:
        fld, r0, (r, N, sA, s1, s2, cs, sn) = field(k, s0, c0)
        ok = ok and fld.torsion_free() and m_val(fld.om[0]) == {}
        ok = ok and (sA.d(0) / sA).v / N.v == s1.v == -1 / (2 * r0 * (1 - r0) * N.v)
        plane = GA.mul(m_val(fld.g[0]), m_val(fld.g[1]), S13)
        unitB = gbiv(0, 1)
        ok = ok and GA.eq(plane, GA.scal(N.v * sA.v, unitB)) and GA.eq(GA.mul(unitB, unitB, S13), GA.sc(1))
        ok = ok and GA.eq(m_val(fld.om[1]), GA.scal(-s1.v, unitB))
    _tp_rv = (ok); assert _tp_rv is not False, "check_parallel_frame_and_t_line_connection"; return _tp_rv


def check_rates_and_kasner_limits():
    premise("interior.exact-parallelism-convergence-rate")
    tau, ts1, ts2, Ru2, tor = interior_series()
    p = (ts1[0], ts2[0], ts2[0])
    ok = ts1[2] == F(-4, 15) and ts2[2] == F(-2, 15) and Ru2[:2] == [1, 0]
    _tp_rv = (ok and p == (F(-1, 3), F(2, 3), F(2, 3)) and sum(p) == 1 and sum(x * x for x in p) == 1); assert _tp_rv is not False, "check_rates_and_kasner_limits"; return _tp_rv


def check_limiting_boosts_generate_so13():
    premise("interior.weighted-limit-theorem")
    tau, ts1, ts2, Ru2, tor = interior_series()
    p = (ts1[0], ts2[0], ts2[0])
    Bs = [GA.scal(p[i], gbiv(0, i + 1)) for i in range(3)]
    ok = lie_dim(Bs, S13) == 6
    for i in range(3):
        for j in range(i + 1, 3):
            cm = GA.scal(F(1, 2), GA.sub(GA.mul(gbiv(0, i + 1), gbiv(0, j + 1), S13), GA.mul(gbiv(0, j + 1), gbiv(0, i + 1), S13)))
            ok = ok and (GA.eq(cm, gbiv(i + 1, j + 1)) or GA.eq(cm, GA.neg(gbiv(i + 1, j + 1))))
    _tp_rv = (ok); assert _tp_rv is not False, "check_limiting_boosts_generate_so13"; return _tp_rv
