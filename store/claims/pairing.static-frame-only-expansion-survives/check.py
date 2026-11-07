"""pairing.static-frame-only-expansion-survives: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)) with the labels (t, r, theta, phi) as background coordinates;
static Schwarzschild field hb^{-1}(e_mu) = sum_a theta^a_mu gamma_a (theta^0 = sqrt f dt, theta^1 = dr/sqrt f,
theta^2 = r dtheta, theta^3 = r sin(theta) dphi) with the rotation-gauge field of the premise Fact
(pairing.imported-schwarzschild-connection-curvature), Omega(e_c) := Omega(hb(gamma_c)). Exact first-order
jets at rational points (sqrt f, sin, cos rational). pv(B) = <B . l, m>, l = e0 + e1, m = e2 + i e3
(unnormalised), n = e0 - e1, complex values as Gaussian rationals. Computed:
(1) the field is torsion-free, and (e_c . D) e_b = Omega(e_c) . e_b equals omega^a_b(e_c) e_a for all 16
    pairs (b, c), against the hand table of the connection forms;
(2) pv(Omega(e_c)) = (0, 0, -sqrt f/r, -i sqrt f/r); on the tetrad pv(Omega(l)) = pv(Omega(n)) =
    pv(Omega(m)) = 0 and pv(Omega(mbar)) = -2 sqrt f/r; the screen trace of A -> (A . D) l is the
    expansion 2 sqrt f/r;
(3) (l . D) l = (f'/2 sqrt f) l; Omega(e0) is a multiple of e01 (zero class) and Omega(e1) = 0;
(4) with M = 1/2 the transverse class is the polynomial -F(1 - F^2) in F = sqrt f, which vanishes at
    F = 0; at F = 3/5 (r = 25/16) it is -48/125.
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


SAMPLES = [(F(3, 5), F(3, 5), F(4, 5), F(1, 2)), (F(4, 5), F(5, 13), F(12, 13), F(1, 2)),
           (F(5, 13), F(4, 5), F(3, 5), F(3, 2)), (F(12, 13), F(8, 17), F(15, 17), F(1, 3))]
LV = [F(1), F(1), F(0), F(0)]


def static_field(F0, s0, c0, M):
    """The premise's static Schwarzschild field with sqrt(f) = F0 at the point; returns (field, r0)."""
    r0 = 2 * M / (1 - F0 * F0)
    return gtg.schwarzschild_static(M, r0, s0, c0), r0


def const_vec(i):
    return vec([J(1 if k == i else 0) for k in range(4)])


def unit(i):
    return [F(1) if k == i else F(0) for k in range(4)]


def omc(fld, c):
    return fld.omega(c)


def check_omega_reproduces_covariant_derivatives():
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        acc, k, ct = (2 * M / r0 ** 2) / (2 * F0), F0 / r0, (c0 / s0) / r0
        table = {(0, 0): [0, acc, 0, 0], (1, 0): [acc, 0, 0, 0], (1, 2): [0, 0, k, 0], (2, 2): [0, -k, 0, 0],
                 (1, 3): [0, 0, 0, k], (2, 3): [0, 0, 0, ct], (3, 3): [0, -k, -ct, 0]}
        ok = ok and fld.torsion_free()
        for c in range(4):
            for b in range(4):
                got = field_cov(fld, unit(c), const_vec(b))
                want = vec([F(x) for x in table.get((b, c), [0, 0, 0, 0])])
                ok = ok and GA.eq(got, {kk: v for kk, v in want.items() if v})
    _tp_rv = (ok); assert _tp_rv is not False, "check_omega_reproduces_covariant_derivatives"; return _tp_rv


def check_pairing_classes_and_optical_scalars():
    premise("pairing.imported-spin-coefficients-null-tetrad")
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        k = F0 / r0
        cls = [pv(omc(fld, c)) for c in range(4)]
        ok = ok and cls == [GA.QI(0), GA.QI(0), GA.QI(-k), GA.QI(0, -k)]
        om_l = GA.add(omc(fld, 0), omc(fld, 1))
        om_n = GA.sub(omc(fld, 0), omc(fld, 1))
        om_m = (omc(fld, 2), omc(fld, 3))
        om_mb = (omc(fld, 2), GA.neg(omc(fld, 3)))
        ok = ok and pv(om_l) == 0 and pv(om_n) == 0 and pv(om_m) == 0 and pv(om_mb) == GA.QI(-2 * k)
        lfield = vec([J(1), J(1), J(0), J(0)])
        theta = -sum(GA.dot(GA.gen(j), field_cov(fld, unit(j), lfield), S13) for j in (2, 3))
        ok = ok and theta == 2 * k
    _tp_rv = (ok); assert _tp_rv is not False, "check_pairing_classes_and_optical_scalars"; return _tp_rv


def check_transport_along_l_and_the_stabiliser():
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        fprime = 2 * M / r0 ** 2
        lfield = vec([J(1), J(1), J(0), J(0)])
        ok = ok and GA.eq(field_cov(fld, LV, lfield), GA.scal(fprime / (2 * F0), m_val(lfield)))
        o0, o1 = omc(fld, 0), omc(fld, 1)
        ok = ok and list(o0) == [(0, 1)] and o1 == {} and pv(o0) == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_transport_along_l_and_the_stabiliser"; return _tp_rv


def check_horizon_limit_and_sample_value():
    ok = True
    for F0, s0, c0, M in SAMPLES:
        if M != F(1, 2):
            continue
        fld, r0 = static_field(F0, s0, c0, M)
        ok = ok and pv(omc(fld, 2)) == GA.QI(-F0 * (1 - F0 * F0))
    poly = [F(0), F(-1), F(0), F(1)]                  # -F + F^3
    ok = ok and GA.peval(poly, F(0)) == 0
    fld, r0 = static_field(F(3, 5), F(3, 5), F(4, 5), F(1, 2))
    ok = ok and r0 == F(25, 16) and pv(omc(fld, 2)) == GA.QI(F(-48, 125)) and GA.peval(poly, F(3, 5)) == F(-48, 125)
    _tp_rv = (ok); assert _tp_rv is not False, "check_horizon_limit_and_sample_value"; return _tp_rv


# ---- GTG derivation (maintainer pass 2026-11-07, GTG proofs) ----
# The connection is solved from the torsion equation of the definition (lib/gtg.py Field with no om: the
# exact linear solve of D_mu g_nu = D_nu g_mu), not taken from the forms; the classes are computed in the odd
# extension Cl(2,3) (generator 4 = e, Q(e) = +1) with the central unit I_5 = I_4 e and m = e2 + I_5 e3, the
# bilinear extension of the scalar product being the symmetric product (vm + mv)/2 (I_5 is central).
S23 = (1, -1, -1, -1, 1)
I5 = {(0, 1, 2, 3, 4): F(1)}


def i5_pair(x, y):
    """(xy + yx)/2 in Cl(2,3): the span{1, I_5}-bilinear scalar product of complexified vectors."""
    return gtg.sym(x, y, S23)


def i5_class(B, l, m):
    """<B . l, m> in Cl(2,3) for a bivector B with coefficients in span{1, I_5}."""
    return i5_pair(gtg.comm(B, l, S23), m)


def solved_static(F0, s0, c0, M):
    """The static gauge's coframe, with Omega solved from the torsion equation alone."""
    r0 = 2 * M / (1 - F0 * F0)
    return gtg.Field(gtg.schwarzschild_static(M, r0, s0, c0).TH), r0


def check_gtg_torsion_solution_is_the_stated_gauge_field():
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = solved_static(F0, s0, c0, M)
        ok = ok and fld.torsion_free() and fld.torsion_rank() == 24
        acc, k, ct = (2 * M / r0 ** 2) / (2 * F0), F0 / r0, (c0 / s0) / r0
        want = [GA.scal(acc, gtg.biv(1, 0)), {}, GA.scal(k, gtg.biv(1, 2)),
                GA.add(GA.scal(k, gtg.biv(1, 3)), GA.scal(ct, gtg.biv(2, 3)))]
        ok = ok and all(GA.eq(fld.omega(c), want[c]) for c in range(4))
    assert ok
    return ok


def check_gtg_classes_with_the_central_unit_of_cl23():
    premise("pairing.imported-schwarzschild-connection-curvature")
    premise("pairing.imported-spin-coefficients-null-tetrad")
    ok = GA.eq(GA.mul(I5, I5, S23), GA.sc(-1)) and all(GA.commutes(I5, GA.gen(j), S23) for j in range(5))
    l = GA.add(GA.gen(0), GA.gen(1))
    m = GA.add(GA.gen(2), GA.mul(I5, GA.gen(3), S23))
    mb = GA.sub(GA.gen(2), GA.mul(I5, GA.gen(3), S23))
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = solved_static(F0, s0, c0, M)
        k = F0 / r0
        om = [fld.omega(c) for c in range(4)]
        cls = [i5_class(om[c], l, m) for c in range(4)]
        ok = ok and cls[0] == {} and cls[1] == {} and GA.eq(cls[2], GA.sc(-k)) and GA.eq(cls[3], GA.scal(-k, I5))
        om_m = GA.add(om[2], GA.mul(I5, om[3], S23))
        om_mb = GA.sub(om[2], GA.mul(I5, om[3], S23))
        ok = ok and i5_class(GA.add(om[0], om[1]), l, m) == {} and i5_class(GA.sub(om[0], om[1]), l, m) == {}
        ok = ok and i5_class(om_m, l, m) == {} and GA.eq(i5_class(om_mb, l, m), GA.sc(-2 * k))
        ok = ok and GA.eq(i5_pair(mb, m), GA.sc(-2))
    fld, r0 = solved_static(F(3, 5), F(3, 5), F(4, 5), F(1, 2))
    ok = ok and r0 == F(25, 16) and GA.eq(i5_class(fld.omega(2), l, m), GA.sc(F(-48, 125)))
    assert ok
    return ok
