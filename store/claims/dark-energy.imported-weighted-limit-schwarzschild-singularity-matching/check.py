"""dark-energy.imported-weighted-limit-schwarzschild-singularity-matching: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)), 2M = 1. The Schwarzschild interior field in synchronous gauge comes
from the premise check interior.interior-connection-exactly (EXPORTS; exact first-order jets at rational
points); the interior functions are also expanded as exact series in u = sqrt(r). Computed:
(1) the adapted orthonormal frame is D-parallel along g_tau (Omega(e_0) = 0, torsion-free field);
    omega(e_i) = sigma_i e_i ^ e_0 (boost block) plus the sphere term (cot(theta)/r) e_2 ^ e_3 (rotation
    block); Hubble-normalised: tau sigma_i -> p_i = (-1/3, 2/3, 2/3) with corrections c_i r, r = R + O(R^2),
    R = (3 tau/2)^{2/3}, i.e. O(tau^{2/3}); the rotation block tau/r = (2/3) u + O(u^3) with
    u^3 = (3/2) tau (1 + O(u^2)), i.e. O(tau^{1/3});
(2) Schwarzschild-de Sitter (f = 1 - 1/r - Lambda r^2/3): A_SdS/A_S - 1 = Lambda r^3/(3(1 - r)) exactly at
    sample points, and as series its ratio to Lambda tau^2 tends to 3/4: a relative O(Lambda tau^2)
    correction with the same leading exponents;
(3) sum p_i^2 = 1 (and sum p_i = 1); the total residue B_w = sum p_i e_0 ^ e_i is a unit boost: B_w^2 = 1,
    and its action on vectors M (x -> B_w . x) satisfies M^3 = M with tr M^2 = 2 (characteristic
    polynomial lambda^4 - lambda^2);
(4) the forced exceptional weights (a_t, a_theta, a_phi) = (-1/2, 1, 1) in r are the exponents in proper
    time tau ~ r^{3/2}: (2/3)(-1/2, 1, 1) = (-1/3, 2/3, 2/3).
The transport-level clauses (tangential curves, phi-lines at rate tau^{1/3}) are cited from T6 and not
recomputed.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (multivectors with jet coefficients) ----
S13 = gtg.S13
m_val, bdot, gbiv = gtg.m_val, gtg.bdot, gtg.biv


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


SAMPLES = [(F(1, 2), F(3, 5), F(4, 5)), (F(2), F(5, 13), F(12, 13))]
LAMBDAS = [F(3), F(-6, 5)]
RS = [F(1, 5), F(1, 2), F(2, 7)]
FORCED = (F(-1, 2), F(1), F(1))


def check_parallel_frame_and_leading_kasner_connection():
    premise("interior.interior-connection-exactly")
    premise("interior.exact-parallelism-convergence-rate")
    premise("interior.weighted-limit-theorem")
    field = premise("interior.interior-connection-exactly")["interior_field"]
    ok = True
    for k, s0, c0 in SAMPLES:
        fld, r0, (r, N, sA, s1, s2, cs, sn) = field(k, s0, c0)
        ok = ok and fld.torsion_free() and m_val(fld.om[0]) == {}
        ok = ok and GA.eq(m_val(fld.om[1]), GA.scal(-s1.v, gbiv(0, 1)))
        ok = ok and m_val(fld.om[3]).get((2, 3)) == c0 / (s0 * r0)
    tau, ts1, ts2, Ru2, tor = interior_series()
    ok = ok and (ts1[0], ts2[0]) == (F(-1, 3), F(2, 3)) and ts1[1] == ts2[1] == 0
    ok = ok and ts1[2] != 0 and ts2[2] != 0 and Ru2[:2] == [1, 0]
    ok = ok and tor[:4] == [0, F(2, 3), 0, F(1, 5)] and tau[3] == F(2, 3)
    _tp_rv = (ok); assert _tp_rv is not False, "check_parallel_frame_and_leading_kasner_connection"; return _tp_rv


def check_schwarzschild_de_sitter_relative_correction():
    premise("interior.schwarzschild-de-sitter-weighted-limit")
    ok = True
    for L in LAMBDAS:
        for r0 in RS:
            AS = 1 / r0 - 1
            ASdS = -(1 - 1 / r0 - L * r0 * r0 / 3)
            ok = ok and ASdS / AS - 1 == L * r0 ** 3 / (3 * (1 - r0))
        # (A_SdS - A_S)/A_S with A_S = (1 - u^2)/u^2, A_SdS - A_S = Lambda u^4/3, as a series in u
        diff_u4 = [F(0)] * 4 + [L / 3]
        AS_inv_u2 = GA.ps_inv([F(1), F(0), F(-1)], NS)              # u^2/(1 - u^2) = u^2 * this
        rel = GA.ps_mul([F(0)] * 2 + diff_u4, AS_inv_u2, NS)
        tau, ts1, ts2, Ru2, tor = interior_series()
        tau2_lead = tau[3] * tau[3]                              # tau^2 = (4/9) u^6 (1 + O(u^2))
        ok = ok and rel[6] / (L * tau2_lead) == F(3, 4) and all(c == 0 for c in rel[:6])
    _tp_rv = (ok); assert _tp_rv is not False, "check_schwarzschild_de_sitter_relative_correction"; return _tp_rv


def check_unit_boost_residue():
    premise("sheaf.matching-fibre")
    tau, ts1, ts2, Ru2, tor = interior_series()
    p = (ts1[0], ts2[0], ts2[0])
    Bw = GA.add(*[GA.scal(p[i], gbiv(0, i + 1)) for i in range(3)])
    ok = sum(x * x for x in p) == 1 and sum(p) == 1 and GA.eq(GA.mul(Bw, Bw, S13), GA.sc(1))
    Mx = [[bdot(Bw, GA.gen(j)).get((i,), F(0)) for j in range(4)] for i in range(4)]
    M2 = GA.mat_mul(Mx, Mx)
    ok = ok and GA.mat_eq(GA.mat_mul(M2, Mx), Mx) and sum(M2[i][i] for i in range(4)) == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_unit_boost_residue"; return _tp_rv


def check_weights_are_the_exponents():
    premise("sheaf.weights-are-forced-are-kasner-exponents")
    tau, ts1, ts2, Ru2, tor = interior_series()
    p = (ts1[0], ts2[0], ts2[0])
    ok = tau[3] != 0 and all(c == 0 for c in tau[:3])          # tau ~ r^{3/2}
    _tp_rv = (ok and tuple(F(2, 3) * a for a in FORCED) == p); assert _tp_rv is not False, "check_weights_are_the_exponents"; return _tp_rv
