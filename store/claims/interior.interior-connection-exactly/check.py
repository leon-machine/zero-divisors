"""interior.interior-connection-exactly: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)) with labels (r, t, theta, phi) as background coordinates, 2M = 1.
The Schwarzschild interior field in synchronous gauge: hb^{-1}(e_r) = N gamma0 with N = sqrt(r/(1 - r))
(so the physical displacement along r is d tau gamma0), hb^{-1}(e_t) = sqrt(A) gamma1, A = (1 - r)/r,
hb^{-1}(e_theta) = r gamma2, hb^{-1}(e_phi) = r sin(theta) gamma3; e_a := gamma_a is the parallel frame of
the premise Lemma (e0 = g_tau). Exact first-order jets at rational points with N, sqrt(A), sin, cos
rational; sigma_1 = d_tau log sqrt(A) = -1/(2 r (1 - r) N), sigma_2 = sigma_3 = d_tau log r = 1/(r N),
checked against the jet derivatives. Omega(e_c) := Omega(hb(gamma_c)), and D_a M = a . nabla M +
Omega(a) x M (Definition).
(1) The proof's connection forms omega^i_0 = sigma_i theta^i, omega^3_2 = (cot(theta)/r) theta^3 assemble to
    Omega(e_i) = sigma_i e_i ^ e_0 (i = 1, 2), Omega(e_3) = sigma_3 e_3 ^ e_0 + (cot(theta)/r) e_2 ^ e_3,
    Omega(e_0) = 0; these satisfy the torsion equation exactly, and the torsion map is injective at the
    point (rank 24), so they are the rotation-gauge field. The boost terms carry the sign
    sigma_i e_i ^ e_0 = -sigma_i B_i with B_i = e_0 ^ e_i: the assembly with +sigma_i B_i (the earlier
    display) fails the torsion equation, which is why the statement displays -sigma_i B_i.
(2) The frame is D-parallel along g_tau: (e_0 . D) e_a = 0 for all a; the full table (e_c . D) e_b = Omega(e_c) . e_b
    is checked against the connection forms (16 pairs).
(3) The rotation coefficient is (cot(theta)/r): r times it is the same at two radii with the same theta.
EXPORTS: interior_field(k, s0, c0) (the field at r = k^2/(1 + k^2)) for the dependent checks.
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (first-order jets, multivectors with jet coefficients, Field, torsion) ----
S13 = gtg.S13
J, omega_forms, m_val, vec = gtg.J, gtg.omega_forms, gtg.m_val, gtg.vec


SAMPLES = [(F(1, 2), F(3, 5), F(4, 5)), (F(1), F(5, 13), F(12, 13)), (F(2), F(4, 5), F(3, 5)),
           (F(1, 3), F(8, 17), F(15, 17))]


def interior_field(k, s0, c0, boost_sign=-1):
    """Interior field at r0 = k^2/(1 + k^2) (N = k); boost_sign = -1 gives Omega(e_i) = sigma_i e_i ^ e_0.
    gtg.sync_interior_field at w = sqrt(A(r0)) = 1/k (Lambda = 0), returned in this check's layout
    (field, r0, (r, N, sA, s1, s2, cs, sn)) with N = 1/sqrt(A)."""
    fld, lam, (r, A, sA, s1, s2, sn, cs) = gtg.sync_interior_field(k * k / (1 + k * k), 1 / k, s0, c0,
                                                                   boost_sign=boost_sign)
    return fld, r.v, (r, 1 / sA, sA, s1, s2, cs, sn)


EXPORTS = {"interior_field": interior_field}


def check_rotation_gauge_field_from_torsion():
    premise("interior.exact-parallelism-convergence-rate")
    ok = True
    for k, s0, c0 in SAMPLES:
        fld, r0, (r, N, sA, s1, s2, cs, sn) = interior_field(k, s0, c0)
        ok = ok and (sA.d(0) / sA).v / N.v == s1.v and (1 / r.v) / N.v == s2.v
        forms = omega_forms([(1, 1, 0, s1), (2, 2, 0, s2), (3, 3, 0, s2), (3, 3, 2, (cs / sn) / r)])
        ok = ok and all(GA.eq(m_val(forms[c]), m_val(fld.om[c])) for c in range(4))
        want = {1: {(0, 1): -s1.v}, 2: {(0, 2): -s2.v}, 3: {(0, 3): -s2.v, (2, 3): c0 / (s0 * r0)}}
        ok = ok and m_val(fld.om[0]) == {} and all(GA.eq(m_val(fld.om[c]), want[c]) for c in (1, 2, 3))
        ok = ok and fld.torsion_free() and fld.torsion_rank() == 24
        printed, _, _ = interior_field(k, s0, c0, boost_sign=1)
        ok = ok and not printed.torsion_free()
    _tp_rv = (ok); assert _tp_rv is not False, "check_rotation_gauge_field_from_torsion"; return _tp_rv


def check_frame_parallel_along_free_fall():
    premise("interior.exact-parallelism-convergence-rate")
    ok = True
    for k, s0, c0 in SAMPLES:
        fld, r0, (r, N, sA, s1, s2, cs, sn) = interior_field(k, s0, c0)
        ct = c0 / (s0 * r0)
        # (e_c . D) e_b = sum_a w[(b, c)][a] e_a, from the connection forms (metric compatibility fixes partners)
        table = {(0, 1): [0, s1.v, 0, 0], (1, 1): [s1.v, 0, 0, 0], (0, 2): [0, 0, s2.v, 0], (2, 2): [s2.v, 0, 0, 0],
                 (0, 3): [0, 0, 0, s2.v], (2, 3): [0, 0, 0, ct], (3, 3): [s2.v, 0, -ct, 0]}
        for c in range(4):
            for b in range(4):
                got = fld.cov_phys([F(1) if i == c else F(0) for i in range(4)], vec([J(1 if i == b else 0) for i in range(4)]))
                want = {(a,): F(x) for a, x in enumerate(table.get((b, c), [0, 0, 0, 0])) if x}
                ok = ok and GA.eq(got, want)
        ok = ok and GA.dot(m_val(fld.g[0]), m_val(fld.g[0]), S13) == r0 / (1 - r0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_frame_parallel_along_free_fall"; return _tp_rv


def check_sphere_coefficient_scales_as_one_over_r():
    ok = True
    vals = {}
    for k, s0, c0 in SAMPLES + [(F(3), F(3, 5), F(4, 5))]:
        fld, r0, _ = interior_field(k, s0, c0)
        coef = m_val(fld.om[3]).get((2, 3), F(0))
        ok = ok and coef == c0 / (s0 * r0)
        get_or_set(vals, (s0, c0), set()).add(r0 * coef)
    _tp_rv = (ok and len(vals[(F(3, 5), F(4, 5))]) == 1 and vals[(F(3, 5), F(4, 5))] == {F(4, 3)}); assert _tp_rv is not False, "check_sphere_coefficient_scales_as_one_over_r"; return _tp_rv
