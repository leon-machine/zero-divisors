"""pairing.regular-frame-class-vanishes-horizon-changes: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)) with labels (T, r, theta, phi) as background coordinates. The
Painleve-Gullstrand field: hb^{-1}(e_T) = gamma0 + beta gamma1, hb^{-1}(e_r) = gamma1 (the radial block of
hb^{-1} = 1 + beta P, P(a) = (a . e_t) e_r, computed on Cl(1,3)), hb^{-1}(e_theta) = r gamma2,
hb^{-1}(e_phi) = r sin(theta) gamma3, beta = sqrt(2M/r); the rotation-gauge field along the frame,
Omega(e_c) := Omega(hb(gamma_c)), from the stated connection forms with beta' = -beta^3/4M. Exact
first-order jets at rational points (beta, sin, cos rational), outside, on and inside the horizon locus.
pv(B) = <B . l, m>, l = e0 + e1, m = e2 + i e3; for the ingoing vacuum <B . n, m>, n = e0 - e1. Computed:
(1) the coframe is the component set of hb^{-1}; the stated forms satisfy the torsion equation exactly
    (also at beta = 1 and beta = 2), and beta' = -beta/2r = -beta^3/4M;
(2) outgoing classes (0, 0, -(1 - beta)/r, -i(1 - beta)/r), negative, zero, positive for beta < 1, = 1,
    > 1; the screen trace of A -> (A . D) l is 2(1 - beta)/r; (l . D) l = (beta^3/4M) l;
(3) ingoing classes +(1 + beta)/r and +i(1 + beta)/r, equal to 144/125, 2, 12 at beta = 4/5, 1, 2 (M = 1/2);
(4) the static frame built inside the same gauge, e0_s = (gamma0 + beta gamma1)/F, e1_s = (gamma1 +
    beta gamma0)/F (F = sqrt(1 - beta^2)), with l_s = e0_s + e1_s: <(e2 . D) l_s, m> = -F/r computed with
    the derivative term of D, and pv_PG = (F/(1 + beta)) pv_static; at (F, beta) = (3/5, 4/5),
    -16/125 = (1/3)(-48/125);
(5) the store's curvature operator calR(B) = -R(hb(B)) in the regular frame: 2M/r^3 on the radial and
    angular planes, -M/r^3 on the mixed ones; the class of the loop (n, e2), pv(R(n ^ e2)) with
    R = -calR, is 2M/r^3, equal to 1 on the horizon locus at M = 1/2.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13
J = gtg.J
m_val = gtg.m_val
vec = gtg.vec
gbiv = gtg.biv                          # gamma_a gamma_b
apply_op = gtg.apply_op
ip = gtg.cdot                            # complex-bilinear product of (re, im) vectors


def field_cov(fld, A, V):
    """(A . D) V = D_{hb(A)} V for constant physical components A and a jet vector field V (value)."""
    return fld.cov_phys(A, V)


L_OUT = (GA.add(GA.gen(0), GA.gen(1)), {})
M_TR = (GA.gen(2), GA.gen(3))


def pv(B, l=L_OUT, m=M_TR):
    """Pairing class pv(B) = <B . l, m> (real bivector B or complex pair), m = e2 + i e3."""
    if isinstance(B, dict):
        B = (B, {})
    return gtg.cdot(gtg.cbdot(B, l), m)
# ---- end of engine ----


PG_SAMPLES = [(F(4, 5), F(3, 5), F(4, 5), F(1, 2)), (F(1), F(5, 13), F(12, 13), F(1, 2)),
              (F(2), F(4, 5), F(3, 5), F(1, 2)), (F(1, 3), F(8, 17), F(15, 17), F(3, 2)),
              (F(3, 5), F(3, 5), F(4, 5), F(2))]
OUTSIDE = [(F(4, 5), F(3, 5)), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]     # (beta, F)
LV = [F(1), F(1), F(0), F(0)]
NV_ = [F(1), F(-1), F(0), F(0)]
N_IN = (GA.sub(GA.gen(0), GA.gen(1)), {})


def pg_field(b0, s0, c0, M):
    """Schwarzschild in the PG gauge with beta = b0 at the point; returns (field, r0, beta jet)."""
    r0 = 2 * M / (b0 * b0)
    fld = gtg.schwarzschild_pg(M, r0, s0, c0)
    return fld, r0, fld.TH[1][0]


def omc(fld, c):
    return fld.omega(c)


def unit(i):
    return [F(1) if k == i else F(0) for k in range(4)]


def check_regular_frame_connection_is_torsion_free():
    ok = True
    et, er = GA.gen(0), GA.gen(1)
    for b0, s0, c0, M in PG_SAMPLES:
        fld, r0, be = pg_field(b0, s0, c0, M)
        ok = ok and fld.torsion_free()
        hbi = [GA.add(GA.gen(i), GA.scal(b0 * GA.dot(GA.gen(i), et, S13), er)) for i in range(2)]
        ok = ok and GA.eq(m_val(fld.g[0]), hbi[0]) and GA.eq(m_val(fld.g[1]), hbi[1])
        ok = ok and (-be * be * be / (4 * M)).v == -b0 / (2 * r0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_regular_frame_connection_is_torsion_free"; return _tp_rv


def check_outgoing_classes_expansion_and_acceleration():
    premise("pairing.pairing-class-transverse-derivative-null-direction")
    premise("pairing.imported-spin-coefficients-null-tetrad")
    ok = True
    for b0, s0, c0, M in PG_SAMPLES:
        fld, r0, be = pg_field(b0, s0, c0, M)
        k = (1 - b0) / r0
        ok = ok and [pv(omc(fld, c)) for c in range(4)] == [GA.QI(0), GA.QI(0), GA.QI(-k), GA.QI(0, -k)]
        sign = (-k > 0) - (-k < 0)
        ok = ok and sign == ((b0 > 1) - (b0 < 1))
        lfield = vec([J(1), J(1), J(0), J(0)])
        theta = -sum(GA.dot(GA.gen(j), field_cov(fld, unit(j), lfield), S13) for j in (2, 3))
        ok = ok and theta == 2 * k
        ok = ok and GA.eq(field_cov(fld, LV, lfield), GA.scal(b0 ** 3 / (4 * M), m_val(lfield)))
    _tp_rv = (ok); assert _tp_rv is not False, "check_outgoing_classes_expansion_and_acceleration"; return _tp_rv


def check_ingoing_classes_one_signed():
    ok = True
    vals = {}
    for b0, s0, c0, M in PG_SAMPLES:
        fld, r0, be = pg_field(b0, s0, c0, M)
        k = (1 + b0) / r0
        got = [pv(omc(fld, c), N_IN) for c in (2, 3)]
        ok = ok and got == [GA.QI(k), GA.QI(0, k)] and k > 0
        if M == F(1, 2):
            vals[b0] = got[0].re
    _tp_rv = (ok and vals == {F(4, 5): F(144, 125), F(1): F(2), F(2): F(12)}); assert _tp_rv is not False, "check_ingoing_classes_one_signed"; return _tp_rv


def check_static_and_regular_frames_agree():
    premise("pairing.two-frames-share-vacuum-selected-transport")
    ok = True
    for b0, F0 in OUTSIDE:
        fld, r0, be = pg_field(b0, F(3, 5), F(4, 5), F(1, 2))
        Fj = (1 - be * be).pw(F(1, 2))
        ok = ok and Fj.v == F0
        ls = vec([(1 + be) / Fj, (1 + be) / Fj, J(0), J(0)])
        cls_static = ip((field_cov(fld, unit(2), ls), {}), M_TR)
        cls_pg = pv(omc(fld, 2))
        ok = ok and cls_static == GA.QI(-F0 / r0) and cls_pg == GA.QI(F0 / (1 + b0)) * cls_static
        cls_static3 = ip((field_cov(fld, unit(3), ls), {}), M_TR)
        ok = ok and pv(omc(fld, 3)) == GA.QI(F0 / (1 + b0)) * cls_static3
    fld, r0, be = pg_field(F(4, 5), F(3, 5), F(4, 5), F(1, 2))
    ok = ok and pv(omc(fld, 2)) == GA.QI(F(-16, 125)) and F(-16, 125) == F(1, 3) * F(-48, 125)
    _tp_rv = (ok); assert _tp_rv is not False, "check_static_and_regular_frames_agree"; return _tp_rv


def check_curvature_classes_do_not_vanish_on_the_horizon():
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    for b0, s0, c0, M in PG_SAMPLES:
        fld, r0, be = pg_field(b0, s0, c0, M)
        Rc = fld.curvature()
        k = M / r0 ** 3
        for (a, b), val in Rc.items():
            lam = 2 * k if (a, b) in ((0, 1), (2, 3)) else -k
            ok = ok and GA.eq(val, GA.scal(lam, gbiv(a, b)))
        nb = GA.mul(N_IN[0], GA.gen(2), S13)
        ok = ok and pv(GA.neg(apply_op(Rc, nb))) == GA.QI(2 * k)
        if b0 == 1 and M == F(1, 2):
            ok = ok and pv(GA.neg(apply_op(Rc, nb))) == GA.QI(1)
    _tp_rv = (ok); assert _tp_rv is not False, "check_curvature_classes_do_not_vanish_on_the_horizon"; return _tp_rv


# ---- GTG derivation (maintainer pass 2026-11-07, GTG proofs) ----
# The rotation-gauge field is solved from the torsion equation of the definition (lib/gtg.py Field with no om:
# the exact linear solve of D_mu g_nu = D_nu g_mu from the coframe alone); the classes are computed in the odd
# extension Cl(2,3) (generator 4 = e, Q(e) = +1), I_5 = I_4 e central, m = e2 + I_5 e3, the span{1, I_5}-bilinear
# scalar product being the symmetric product (vm + mv)/2.
S23 = (1, -1, -1, -1, 1)
I5 = {(0, 1, 2, 3, 4): F(1)}


def i5_class(B, l, m):
    """<B . l, m> = sym(B . l, m) in Cl(2,3)."""
    return gtg.sym(gtg.comm(B, l, S23), m, S23)


def solved_pg(b0, s0, c0, M):
    """The PG coframe of the stored gauge with Omega solved from the torsion equation alone."""
    r0 = 2 * M / (b0 * b0)
    return gtg.Field(gtg.schwarzschild_pg(M, r0, s0, c0).TH), r0


def check_gtg_torsion_solution_is_the_pg_gauge_field():
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    for b0, s0, c0, M in PG_SAMPLES:
        fld, r0 = solved_pg(b0, s0, c0, M)
        ok = ok and fld.torsion_free() and fld.torsion_rank() == 24
        bp = -b0 ** 3 / (4 * M)
        u = GA.add(GA.scal(b0, GA.gen(0)), GA.gen(1))
        want = [{}, GA.scal(-bp, gbiv(1, 0)), GA.scal(1 / r0, gtg.wedge(u, GA.gen(2))),
                GA.add(GA.scal(1 / r0, gtg.wedge(u, GA.gen(3))), GA.scal((c0 / s0) / r0, gbiv(2, 3)))]
        ok = ok and all(GA.eq(fld.omega(c), want[c]) for c in range(4))
    assert ok
    return ok


def check_gtg_classes_and_loop_class_in_cl23():
    premise("pairing.pairing-class-transverse-derivative-null-direction")
    premise("std-algebra.complexification-is-the-odd-extension")   # the central unit I_5 of Cl(2,3)
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = GA.eq(GA.mul(I5, I5, S23), GA.sc(-1)) and all(GA.commutes(I5, GA.gen(j), S23) for j in range(5))
    l = GA.add(GA.gen(0), GA.gen(1))
    n = GA.sub(GA.gen(0), GA.gen(1))
    m = GA.add(GA.gen(2), GA.mul(I5, GA.gen(3), S23))
    seen = {}
    for b0, s0, c0, M in PG_SAMPLES:
        fld, r0 = solved_pg(b0, s0, c0, M)
        ko, ki = (1 - b0) / r0, (1 + b0) / r0
        om = [fld.omega(c) for c in range(4)]
        out = [i5_class(om[c], l, m) for c in range(4)]
        ok = ok and out[0] == {} and out[1] == {} and GA.eq(out[2], GA.sc(-ko)) and GA.eq(out[3], GA.scal(-ko, I5))
        inn = [i5_class(om[c], n, m) for c in (2, 3)]
        ok = ok and GA.eq(inn[0], GA.sc(ki)) and GA.eq(inn[1], GA.scal(ki, I5))
        acc = gtg.bdot(GA.add(om[0], om[1]), l)
        ok = ok and GA.eq(acc, GA.scal(b0 ** 3 / (4 * M), l))
        Rc = fld.curvature()
        loop = GA.neg(gtg.apply_op(Rc, GA.mul(n, GA.gen(2), S13)))
        ok = ok and GA.eq(i5_class(loop, l, m), GA.sc(2 * M / r0 ** 3))
        if M == F(1, 2):
            seen[b0] = inn[0].get((), F(0))
    ok = ok and seen == {F(4, 5): F(144, 125), F(1): F(2), F(2): F(12)}
    assert ok
    return ok
