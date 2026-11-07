"""pairing.curvature-which-loops-move-vacuum: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)), labels (t, r, theta, phi) as background coordinates, the static
Schwarzschild field of the premise Fact (pairing.imported-schwarzschild-connection-curvature) at rational
points (sqrt f, sin, cos rational), exact first-order jets. The field strength R(e_mu ^ e_nu) is computed
from Omega by d_mu Omega_nu - d_nu Omega_mu + Omega_mu x Omega_nu; the curvature bivector of the loop of
physical vectors (u, v) is R(u, v) = R(hb(u ^ v)) = -calR(u ^ v) (LDG sign), extended complex-bilinearly.
pv(B) = <B . l, m>, l = e0 + e1, n = e0 - e1, m = e2 + i e3, mbar = e2 - i e3. Computed:
(1) the six frame-plane classes: 0, 0, M/r^3, -M/r^3, i M/r^3, -i M/r^3;
(2) R(l, e2) = (M/r^3) l e2, a null rotation about l ((l e2)^2 = 0, (l e2) . l = 0) of zero class;
    R(n, e2) has class 2M/r^3;
(3) the complex loops: (l, m), (l, mbar), (m, mbar), (n, m) have class 0, (n, mbar) has 4M/r^3, (l, n) has 0;
(4) as a linear functional on the six tetrad bivectors the class is supported on n ^ mbar alone, so it
    vanishes on every loop in the null hypersurface spanned by l, m, mbar;
(5) the proof's GTG computation: Omega solved from the torsion equation of the static gauge field, omega(gamma_c),
    and the field strength on the six background planes against the proof's closed forms, the frame-loop
    bivectors and their classes recomputed from those closed forms.
The complex unit of m is I5 (central in Cl(2,3)); GA.QI carries span{1, I5} as pairs (re, im).
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13
apply_op = gtg.apply_op
bdot = gtg.bdot


L_OUT = (GA.add(GA.gen(0), GA.gen(1)), {})
M_TR = (GA.gen(2), GA.gen(3))


def pv(B, l=L_OUT, m=M_TR):
    """Pairing class pv(B) = <B . l, m> (real bivector B or complex pair), m = e2 + i e3."""
    if isinstance(B, dict):
        B = (B, {})
    return gtg.cdot(gtg.cbdot(B, l), m)
# ---- end of engine ----


SAMPLES = [(F(3, 5), F(3, 5), F(4, 5), F(1, 2)), (F(4, 5), F(5, 13), F(12, 13), F(1, 2)),
           (F(5, 13), F(4, 5), F(3, 5), F(3, 2))]
E = [GA.gen(i) for i in range(4)]
LC = (GA.add(E[0], E[1]), {})
NC = (GA.sub(E[0], E[1]), {})
MC = (E[2], E[3])
MBC = (E[2], GA.neg(E[3]))
TETRAD = {"l": LC, "n": NC, "m": MC, "mb": MBC}


def static_field(F0, s0, c0, M):
    """The premise's static Schwarzschild field with sqrt(f) = F0 at the point; returns (field, r0)."""
    r0 = 2 * M / (1 - F0 * F0)
    return gtg.schwarzschild_static(M, r0, s0, c0), r0


def cwedge(u, v):
    """Complex wedge of complex vectors (re, im)."""
    w = gtg.wedge
    return (GA.sub(w(u[0], v[0]), w(u[1], v[1])), GA.add(w(u[0], v[1]), w(u[1], v[0])))


def loop(Rc, u, v):
    """R(u, v) = -calR(u ^ v), complex-bilinear."""
    B = cwedge(u, v)
    return (GA.neg(apply_op(Rc, B[0])), GA.neg(apply_op(Rc, B[1])))


def check_frame_plane_classes():
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        ok = ok and fld.torsion_free()
        Rc = fld.curvature()
        k = M / r0 ** 3
        want = {(0, 1): GA.QI(0), (2, 3): GA.QI(0), (0, 2): GA.QI(k), (1, 2): GA.QI(-k), (0, 3): GA.QI(0, k),
                (1, 3): GA.QI(0, -k)}
        for (a, b), w in want.items():
            ok = ok and pv(GA.neg(Rc[(a, b)])) == w
    _tp_rv = (ok); assert _tp_rv is not False, "check_frame_plane_classes"; return _tp_rv


def check_null_rotation_about_l_and_radial_loop():
    premise("pairing.imported-schwarzschild-connection-curvature")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        Rc = fld.curvature()
        k = M / r0 ** 3
        le2 = GA.mul(LC[0], E[2], S13)
        Rl = loop(Rc, LC, (E[2], {}))
        ok = ok and GA.eq(Rl[0], GA.scal(k, le2)) and Rl[1] == {}
        ok = ok and GA.mul(le2, le2, S13) == {} and bdot(le2, LC[0]) == {} and pv(Rl) == 0
        ok = ok and pv(loop(Rc, NC, (E[2], {}))) == GA.QI(2 * k)
    _tp_rv = (ok); assert _tp_rv is not False, "check_null_rotation_about_l_and_radial_loop"; return _tp_rv


def check_complex_loops():
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        Rc = fld.curvature()
        k = M / r0 ** 3
        want = {("l", "m"): 0, ("l", "mb"): 0, ("m", "mb"): 0, ("n", "m"): 0, ("n", "mb"): 4 * k, ("l", "n"): 0}
        for (u, v), w in want.items():
            ok = ok and pv(loop(Rc, TETRAD[u], TETRAD[v])) == GA.QI(w)
    _tp_rv = (ok); assert _tp_rv is not False, "check_complex_loops"; return _tp_rv


def check_class_supported_on_n_wedge_mbar():
    premise("pairing.imported-schwarzschild-connection-curvature")
    ok = True
    pairs = [("l", "n"), ("l", "m"), ("l", "mb"), ("n", "m"), ("n", "mb"), ("m", "mb")]
    for F0, s0, c0, M in SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        Rc = fld.curvature()
        support = [p for p in pairs if pv(loop(Rc, TETRAD[p[0]], TETRAD[p[1]])) != 0]
        ok = ok and support == [("n", "mb")]
        # the tetrad bivectors span the complexified bivector space (rank 6 over Q(i))
        rows = []
        for u, v in pairs:
            B = cwedge(TETRAD[u], TETRAD[v])
            rows.append([GA.QI(B[0].get(bl, F(0)), B[1].get(bl, F(0)))
                         for bl in [(a, b) for a in range(4) for b in range(a + 1, 4)]])
        ok = ok and GA.field_rank(rows) == 6
        hyper = [p for p in pairs if "n" not in p]
        ok = ok and len(hyper) == 3 and all(pv(loop(Rc, TETRAD[u], TETRAD[v])) == 0 for u, v in hyper)
    _tp_rv = (ok); assert _tp_rv is not False, "check_class_supported_on_n_wedge_mbar"; return _tp_rv


def check_gtg_connection_and_field_strength():
    """The proof's GTG computation: Omega from the torsion equation of the static gauge field and the field
    strength R(a ^ b) on the background planes, against the closed forms of the proof; then the frame-loop
    bivectors R(e_c, e_d) = -calR(e_c ^ e_d) and their classes recomputed from the closed forms alone."""
    premise("pairing.imported-schwarzschild-connection-curvature")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for F0, s0, c0, M in SAMPLES:
        fld, r = static_field(F0, s0, c0, M)
        solved = gtg.Field(fld.TH)                     # Omega solved from the torsion equation alone
        b = gtg.biv
        want_Om = [GA.scal(-M / r ** 2, b(0, 1)), {}, GA.scal(F0, b(1, 2)),
                   GA.add(GA.scal(F0 * s0, b(1, 3)), GA.scal(c0, b(2, 3)))]
        for mu in range(4):
            ok = ok and GA.eq(solved.Omega(mu), want_Om[mu]) and GA.eq(fld.Omega(mu), want_Om[mu])
        want_om = [GA.scal(M / (r ** 2 * F0), GA.mul(E[1], E[0], S13)), {}, GA.scal(F0 / r, b(1, 2)),
                   GA.add(GA.scal(F0 / r, b(1, 3)), GA.scal((c0 / s0) / r, b(2, 3)))]
        for c in range(4):
            ok = ok and GA.eq(solved.omega(c), want_om[c])
        want_R = {(0, 1): GA.scal(-2 * M / r ** 3, b(0, 1)), (0, 2): GA.scal(M * F0 / r ** 2, b(0, 2)),
                  (0, 3): GA.scal(M * F0 * s0 / r ** 2, b(0, 3)), (1, 2): GA.scal(M / (r ** 2 * F0), b(1, 2)),
                  (1, 3): GA.scal(M * s0 / (r ** 2 * F0), b(1, 3)), (2, 3): GA.scal(-2 * M * s0 / r, b(2, 3))}
        for (mu, nu), w in want_R.items():
            ok = ok and GA.eq(solved.strength(mu, nu), w)
        # frame loops R(e_c, e_d) = -calR(e_c ^ e_d), and the classes from these closed forms
        k = M / r ** 3
        loopR = {(0, 1): GA.scal(-2 * k, b(0, 1)), (2, 3): GA.scal(-2 * k, b(2, 3)), (0, 2): GA.scal(k, b(0, 2)),
                 (0, 3): GA.scal(k, b(0, 3)), (1, 2): GA.scal(k, b(1, 2)), (1, 3): GA.scal(k, b(1, 3))}
        Rc = solved.curvature()
        for pl, w in loopR.items():
            ok = ok and GA.eq(GA.neg(Rc[pl]), w)
        cls = {(0, 1): GA.QI(0), (2, 3): GA.QI(0), (0, 2): GA.QI(k), (1, 2): GA.QI(-k), (0, 3): GA.QI(0, k),
               (1, 3): GA.QI(0, -k)}
        ok = ok and all(pv(loopR[pl]) == w for pl, w in cls.items())
        # bilinearity: R(u, v) = k u ^ v across the planes, -2k u ^ v within the radial and angular planes
        ok = ok and GA.eq(GA.add(loopR[(0, 2)], loopR[(1, 2)]), GA.scal(k, GA.mul(LC[0], E[2], S13)))
        ok = ok and GA.eq(GA.scal(-2, loopR[(0, 1)]), GA.scal(-2 * k, gtg.wedge(LC[0], NC[0])))
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_connection_and_field_strength"; return _tp_rv
