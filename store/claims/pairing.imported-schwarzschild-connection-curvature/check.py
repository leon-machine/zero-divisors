"""pairing.imported-schwarzschild-connection-curvature: exact checks in Gauge Theory Gravity.

The background is flat spacetime: the vectors of Cl(1,3) (GA.py, signature (+,-,-,-)) with the labels
x = (t, r, theta, phi) taken as background coordinates (a position gauge). The gravitational field is
given by hb^{-1}(e_mu) = g_mu = sum_a theta^a_mu gamma_a, with gamma_a the orthonormal generators, and by
the rotation-gauge field along the physical frame, Omega(hb(gamma_c)) = sum_{a<b} omega^a_b(gamma_c)
eta_bb gamma_a gamma_b, so that (gamma_c . D) gamma_b = omega^a_b(gamma_c) gamma_a. Scalars are exact
first-order jets (value and gradient, Fractions) at rational sample points with sqrt(f), sin(theta) and
cos(theta) rational; the background derivative acts on the jets. Computed:
(1) static gauge: the stated connection forms satisfy the torsion equation D_{e_mu} g_nu = D_{e_nu} g_mu
    exactly; the torsion map is injective on bivector-valued Omega at the point (rank 24), so they are
    the rotation-gauge field; the derived metric g(e_mu, e_nu) = g_mu . g_nu is diag(f, -1/f, -r^2,
    -r^2 sin^2).
(2) the field strength R(e_mu ^ e_nu) = d_mu Omega_nu - d_nu Omega_mu + Omega_mu x Omega_nu, and the store's
    curvature operator calR(B) = -R(hb(B)): diagonal on the six coordinate planes, 2M/r^3 on the radial
    and angular planes, -M/r^3 on the four mixed planes; equal to the closed form
    (M/2r^3)(B + 3 sigma_r B sigma_r) of the premise shape decoupling.
(3) the top eigenspace is exactly span{sigma_r, I sigma_r} (kernel dimension 2), sigma_r^2 = +1,
    (I sigma_r)^2 = -1, I sigma_r = e2 e3 up to sign.
(4) Painleve-Gullstrand gauge hb = 1 - beta P, P(a) = (a . e_t) e_r, computed on Cl(1,3): P^2 = 0,
    hb^{-1} = 1 + beta P (also at beta = 1 and beta > 1), and the derived metric on the radial plane is
    g_TT = 1 - beta^2, g_Tr = -beta, g_rr = -1 (the line element dT^2 - (dr + beta dT)^2 - r^2 dOmega^2).
The flag-bit sentence is a convention of the series (initial data) and is not tested.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13
J = gtg.J
sincos = gtg.sincos
omega_forms = gtg.omega_forms
Field = gtg.Field
m_val = gtg.m_val
gbiv = gtg.biv                          # gamma_a gamma_b
apply_op = gtg.apply_op
# ---- end of engine ----


STATIC_SAMPLES = [(F(3, 5), F(3, 5), F(4, 5), F(1, 2)), (F(4, 5), F(5, 13), F(12, 13), F(1, 2)),
                  (F(5, 13), F(4, 5), F(3, 5), F(3, 2))]
BETAS = [F(1, 3), F(4, 5), F(1), F(7, 3)]


def static_field(F0, s0, c0, M):
    """Static Schwarzschild field with sqrt(f) = F0 at the sample point; returns (field, r0)."""
    r0 = 2 * M / (1 - F0 * F0)
    r = J.var(1, r0)
    f = 1 - 2 * M / r
    sf = f.pw(F(1, 2))
    sn, cs = sincos(2, s0, c0)
    TH = [[J(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][1], TH[2][2], TH[3][3] = sf, 1 / sf, r, r * sn
    fp = 2 * M / (r * r)
    om = omega_forms([(0, 0, 1, fp / (2 * sf)), (2, 2, 1, sf / r), (3, 3, 1, sf / r), (3, 3, 2, (cs / sn) / r)])
    return Field(TH, om), r0


def torsion_rank(fld):
    """Rank of the algebraic part Omega -> (Omega_mu . g_nu - Omega_nu . g_mu) of the torsion map at the point."""
    return fld.torsion_rank()


def check_static_connection_is_the_torsion_free_field():
    ok = True
    for F0, s0, c0, M in STATIC_SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        ok = ok and fld.torsion_free() and torsion_rank(fld) == 24
        f = 1 - 2 * M / r0
        gram = [[GA.dot(m_val(fld.g[m]), m_val(fld.g[n]), S13) for n in range(4)] for m in range(4)]
        want = [[f, 0, 0, 0], [0, -1 / f, 0, 0], [0, 0, -r0 * r0, 0], [0, 0, 0, -r0 * r0 * s0 * s0]]
        ok = ok and gram == want
    _tp_rv = (ok); assert _tp_rv is not False, "check_static_connection_is_the_torsion_free_field"; return _tp_rv


def check_curvature_eigenvalues_on_coordinate_planes():
    premise("singularity.curvature-gauge-field-exact-shape-decoupling")
    ok = True
    sig_r = gbiv(0, 1)
    for F0, s0, c0, M in STATIC_SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        Rc = fld.curvature()
        k = M / r0 ** 3
        for (a, b), val in Rc.items():
            lam = 2 * k if (a, b) in ((0, 1), (2, 3)) else -k
            ok = ok and GA.eq(val, GA.scal(lam, gbiv(a, b)))
            B = gbiv(a, b)
            closed = GA.scal(k / 2, GA.add(B, GA.scal(3, GA.mul(GA.mul(sig_r, B, S13), sig_r, S13))))
            ok = ok and GA.eq(val, closed)
    _tp_rv = (ok); assert _tp_rv is not False, "check_curvature_eigenvalues_on_coordinate_planes"; return _tp_rv


def check_extreme_pair_and_sign_of_square():
    ok = True
    I4 = GA.mul(gbiv(0, 1), gbiv(2, 3), S13)
    blades = [(a, b) for a in range(4) for b in range(a + 1, 4)]
    for F0, s0, c0, M in STATIC_SAMPLES:
        fld, r0 = static_field(F0, s0, c0, M)
        Rc = fld.curvature()
        lam = 2 * M / r0 ** 3
        mat = [[(Rc[bl].get(row, F(0)) - (lam if bl == row else 0)) for bl in blades] for row in blades]
        ker = GA.field_kernel(mat)
        ok = ok and len(ker) == 2
        sig_r = GA.mul(GA.gen(1), GA.gen(0), S13)
        Isr = GA.mul(I4, sig_r, S13)
        ok = ok and GA.eq(GA.mul(sig_r, sig_r, S13), GA.sc(1)) and GA.eq(GA.mul(Isr, Isr, S13), GA.sc(-1))
        ok = ok and (GA.eq(Isr, gbiv(2, 3)) or GA.eq(Isr, GA.neg(gbiv(2, 3))))
        for B in (sig_r, Isr):
            ok = ok and GA.eq(apply_op(Rc, B), GA.scal(lam, B))
    _tp_rv = (ok); assert _tp_rv is not False, "check_extreme_pair_and_sign_of_square"; return _tp_rv


def check_painleve_gullstrand_gauge_field():
    et, er = GA.gen(0), GA.gen(1)
    ok = True
    for beta in BETAS:
        def P(a):
            return GA.scal(GA.dot(a, et, S13), er)

        def hb(a):
            return GA.sub(a, GA.scal(beta, P(a)))

        def hbi(a):
            return GA.add(a, GA.scal(beta, P(a)))
        for i in range(4):
            e = GA.gen(i)
            ok = ok and P(P(e)) == {} and GA.eq(hb(hbi(e)), e) and GA.eq(hbi(hb(e)), e)
        g = [[GA.dot(hbi(GA.gen(m)), hbi(GA.gen(n)), S13) for n in range(2)] for m in range(2)]
        ok = ok and g == [[1 - beta * beta, -beta], [-beta, -1]]
    _tp_rv = (ok); assert _tp_rv is not False, "check_painleve_gullstrand_gauge_field"; return _tp_rv
