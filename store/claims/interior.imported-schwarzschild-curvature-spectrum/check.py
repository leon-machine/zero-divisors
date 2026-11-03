"""interior.imported-schwarzschild-curvature-spectrum: exact checks in Gauge Theory Gravity.

Flat background: the vectors of Cl(1,3) (GA.py, signature (+,-,-,-)); labels (t, r, theta, phi) are
background coordinates. A gravitational field is hb^{-1}(e_mu) = sum_a TH[a][mu] gamma_a (gamma_a the
constant physical orthonormal frame) with the rotation-gauge field Omega(hb(gamma_c)) in the GTG sign
(D_a M = a.grad M + Omega(a) x M). Scalars are exact first-order jets at rational sample points with
sqrt(f), sin(theta), cos(theta) rational. The field strength is R(e_mu ^ e_nu) = d_mu Omega_nu -
d_nu Omega_mu + Omega_mu x Omega_nu and the store-sign curvature operator is calR(B) = -R(hb(B)).
(1) Static gauge: the connection is the torsion-free one (D_{e_mu} g_nu = D_{e_nu} g_mu) and the derived
    metric g_mu . g_nu is diag(f, -1/f, -r^2, -r^2 sin^2) with f = 1 - 2M/r.
(2) Static gauge spectrum: calR is diagonal on the six static frame planes, 2M/r^3 on sigma_r = gamma_1
    gamma_0 and on gamma_2 gamma_3 = +-I sigma_r, -M/r^3 on the four mixed planes; Ricci contraction 0.
(3) The same spectrum from the Painleve-Gullstrand field hb = 1 - beta P (the gauge field of the
    premise): Omega(e_t) = (M/r^2) sigma_r, radial eigenvalue 2M/r^3, and the whole operator agrees
    with the static one, also inside the horizon (beta > 1) where the static gauge does not exist.
(4) The 2M/r^3 eigenspace is exactly span{sigma_r, I sigma_r} (kernel dimension 2), sigma_r^2 = +1.
The provenance sentence (papers cited) is not computable and is not tested.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (L12 names; jets, fields (hb, Omega), store-sign curvature, Ricci and Schouten
# ---- maps, Cl(2,4) tractors with generators 0..3 spacetime, 4 = e+, 5 = e-) ----
S13, m_val, static_field, fv = gtg.S13, gtg.m_val, gtg.static_field, GA.gen
fb, apply_op, ricci = gtg.biv, gtg.apply_op, gtg.ricci


def pg_field(r0, s0, c0, M):
    """Schwarzschild in the Painleve-Gullstrand gauge hb = 1 - beta P, beta = sqrt(2M/r)."""
    return gtg.schwarzschild_pg(M, r0, s0, c0)

# (sqrt f, sin theta, cos theta, M) at static sample points; r0 = 2M/(1 - f)
STATIC = [(F(3, 5), F(3, 5), F(4, 5), F(1)), (F(4, 5), F(5, 13), F(12, 13), F(1, 2)),
          (F(5, 13), F(4, 5), F(3, 5), F(3, 2)), (F(12, 13), F(8, 17), F(15, 17), F(2))]
# (r0, sin, cos, M) for the PG gauge: beta^2 = 2M/r0 rational squares, inside and outside the horizon
PG = [(F(1, 2), F(3, 5), F(4, 5), F(1)), (F(9, 2), F(5, 13), F(12, 13), F(1)),
      (F(8), F(4, 5), F(3, 5), F(1, 4)), (F(1, 8), F(8, 17), F(15, 17), F(9, 4))]
PLANES = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def schw(F0, s0, c0, M):
    r0 = 2 * M / (1 - F0 * F0)
    return static_field(r0, s0, c0, lambda r: 1 - 2 * M / r), r0


def check_static_gauge_field_is_torsion_free_with_static_metric():
    ok = True
    for F0, s0, c0, M in STATIC:
        fld, r0 = schw(F0, s0, c0, M)
        f = 1 - 2 * M / r0
        gram = [[GA.dot(m_val(fld.g[m]), m_val(fld.g[n]), S13) for n in range(4)] for m in range(4)]
        want = [[f, 0, 0, 0], [0, -1 / f, 0, 0], [0, 0, -r0 * r0, 0], [0, 0, 0, -r0 * r0 * s0 * s0]]
        ok = ok and fld.torsion_free() and gram == want
    # first sample by hand: sqrt f = 3/5, M = 1 gives r0 = 25/8 and g_tt = 9/25
    fld, r0 = schw(*STATIC[0])
    ok = ok and r0 == F(25, 8) and GA.dot(m_val(fld.g[0]), m_val(fld.g[0]), S13) == F(9, 25)
    _tp_rv = (ok); assert _tp_rv is not False, "check_static_gauge_field_is_torsion_free_with_static_metric"; return _tp_rv


def check_static_spectrum_on_frame_planes():
    premise("interior.imported-equivalence-einstein-equations")
    ok = True
    for F0, s0, c0, M in STATIC:
        fld, r0 = schw(F0, s0, c0, M)
        Rc = fld.curvature()
        k = M / r0 ** 3
        for (a, b) in PLANES:
            lam = 2 * k if (a, b) in ((0, 1), (2, 3)) else -k
            ok = ok and GA.eq(Rc[(a, b)], GA.scal(lam, fb(a, b)))
        # vacuum: the Ricci contraction vanishes (GTG vacuum = Ricci-flat derived metric)
        ok = ok and all(GA.is_zero(ricci(Rc, fv(a))) for a in range(4))
    fld, r0 = schw(*STATIC[0])
    ok = ok and fld.curvature()[(0, 1)] == {(0, 1): F(1024, 15625)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_static_spectrum_on_frame_planes"; return _tp_rv


def check_painleve_gullstrand_gauge_gives_the_same_spectrum():
    premise("singularity.solution-where-divergence-lies")
    premise("interior.imported-equivalence-einstein-equations")
    ok = True
    sig_r = fb(1, 0)
    for r0, s0, c0, M in PG:
        fld = pg_field(r0, s0, c0, M)
        ok = ok and fld.torsion_free()
        ok = ok and GA.eq(m_val(fld.Om[0]), GA.scal(M / r0 ** 2, sig_r))      # Omega(e_t) = (M/r^2) sigma_r
        Rc = fld.curvature()
        k = M / r0 ** 3
        ok = ok and GA.eq(apply_op(Rc, sig_r), GA.scal(2 * k, sig_r))
        for (a, b) in PLANES:
            lam = 2 * k if (a, b) in ((0, 1), (2, 3)) else -k
            ok = ok and GA.eq(Rc[(a, b)], GA.scal(lam, fb(a, b)))
        ok = ok and all(GA.is_zero(ricci(Rc, fv(a))) for a in range(4))
    # one sample inside the horizon: r0 = 1/2, M = 1, beta = 2: radial eigenvalue 16
    fld = pg_field(*PG[0])
    ok = ok and apply_op(fld.curvature(), sig_r) == {(0, 1): F(-16)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_painleve_gullstrand_gauge_gives_the_same_spectrum"; return _tp_rv


def check_top_eigenspace_is_sigma_r_and_its_dual():
    ok = True
    I4 = GA.mul(fb(0, 1), fb(2, 3), S13)
    sig_r = fb(1, 0)
    Isr = GA.mul(I4, sig_r, S13)
    ok = ok and GA.eq(GA.mul(sig_r, sig_r, S13), GA.sc(1)) and GA.eq(GA.mul(Isr, Isr, S13), GA.sc(-1))
    ok = ok and GA.eq(Isr, GA.neg(fb(2, 3)))
    for F0, s0, c0, M in STATIC[:2]:
        fld, r0 = schw(F0, s0, c0, M)
        Rc = fld.curvature()
        top, low = 2 * M / r0 ** 3, -M / r0 ** 3
        for lam, dim in ((top, 2), (low, 4)):
            mat = [[(Rc[bl].get(row, F(0)) - (lam if bl == row else 0)) for bl in PLANES] for row in PLANES]
            ok = ok and len(GA.field_kernel(mat)) == dim
        for B in (sig_r, Isr):
            ok = ok and GA.eq(apply_op(Rc, B), GA.scal(top, B))
    _tp_rv = (ok); assert _tp_rv is not False, "check_top_eigenspace_is_sigma_r_and_its_dual"; return _tp_rv
