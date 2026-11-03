"""singularity.solution-where-divergence-lies: exact checks in Gauge Theory Gravity.

The PG gravitational field (hb, Omega) of singularity.connection-bivector-computed on flat spacetime
(Cl(1,3), signature (+,-,-,-)), physical frame g_mu = hb^{-1}(e_mu) = sum_a theta^a_mu gamma_a, the
stated rotation-gauge field, exact first-order jets at six rational points (horizon included). The
background field strength R(e_mu ^ e_nu) = d_mu Omega(e_nu) - d_nu Omega(e_mu) + Omega(e_mu) x Omega(e_nu)
(LDG sign) and the store's operator calR(B) = -R(hb(B)) (DICTIONARY C5-C6), computed on all six frame
planes from the gauge fields alone (the engine is lib/gtg.py, not the premise's exports, so this
module's exports do not route through the premise). sigma_r = gamma_1 gamma_0.
(1) Radial curvature: nothing depends on t, Omega(e_t) and Omega(e_r) commute, and
    R(e_t ^ e_r) = (2M/r^3) sigma_r; since g_t ^ g_r = -sigma_r, calR(sigma_r) = +2M/r^3 sigma_r; and
    -d/dr (M/r^2) = 2M/r^3 as a rational-function identity.
(2) Vacuum: every frame plane is an eigenplane of calR, with eigenvalue magnitudes
    (2, 1, 1, 1, 1, 2) M/r^3 in the order (01, 02, 03, 12, 13, 23), calR equals the closed form
    (M/2r^3)(B + 3 sigma_r B sigma_r), and the Ricci contraction gamma^a . calR(gamma_a ^ b) vanishes for
    every b: computed in the PG gauge directly, so no carry-over from the static chart is needed.
(3) Unimodularity, as identities in beta: det hb = 1 (matrix of a -> a - beta (a.e_t) e_r computed
    with GA.dot, determinant over Q(beta)), (hb - 1)^2 = 0 with hb - 1 nonzero, the derived metric's
    (t,r) block is [[1 - beta^2, -beta], [-beta, -1]] with determinant -1; meanwhile the squared
    coefficient of Omega(e_r) and the radial curvature grow along r = 8, 1/2, 1/32 (M = 1).
EXPORTS: the engine with curvature(fld), apply_op, closed_form, ricci, SIG_R, PLANES, POINTS.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

S13 = gtg.S13
ETA = gtg.ETA
# sample points (M, beta, sin theta, cos theta); r = 2M/beta^2
POINTS = [(F(1), F(1, 2), F(3, 5), F(4, 5)), (F(3, 2), F(1), F(5, 13), F(12, 13)),
          (F(1), F(2), F(4, 5), F(3, 5)), (F(2, 3), F(3, 5), F(8, 17), F(15, 17)),
          (F(5), F(7, 3), F(12, 13), F(-5, 13)), (F(1, 2), F(1, 3), F(3, 5), F(-4, 5))]


# jets and jet multivectors: lib/gtg.py
J = gtg.J
m_add = gtg.m_add
m_comm = gtg.comm                         # (xy - yx)/2
m_val = gtg.m_val


def omega_bivector(spec):
    """Bivector with Omega x gamma_b = sum_a w gamma_a for each (a, b, w) with omega^a_b = w (a != b),
    extended by metric compatibility: the term is w eta_bb gamma_a gamma_b."""
    out = {}
    for a, b, w in spec:
        blade, sgn = ((a, b), 1) if a < b else ((b, a), -1)
        out = m_add(out, {blade: w * (ETA[b] * sgn)})
    return out


def pg_field(M, beta, s, c, coeffs=(-1, -1, 1, 1)):
    """The PG gauge field and the stated connection at a point. coeffs = (c10, c20, c21, c32) are the
    numerical factors of omega^1_0 = c10 beta' theta^1, omega^{2,3}_0 = c20 (beta/r) theta^{2,3},
    omega^{2,3}_1 = c21 (1/r) theta^{2,3}, omega^3_2 = c32 (cot theta / r) theta^3."""
    c10, c20, c21, c32 = coeffs
    r0 = 2 * M / (beta * beta)
    t, r = J.var(0, 0), J.var(1, r0)
    sn = J(s, (0, 0, c, 0))
    cs = J(c, (0, 0, -s, 0))
    b = (2 * M / r).sqrt()
    assert b.v == beta
    bp = -b / (2 * r)
    TH = [[J(1), J(0), J(0), J(0)],
          [b, J(1), J(0), J(0)],
          [J(0), J(0), r, J(0)],
          [J(0), J(0), J(0), r * sn]]
    g = [{(a,): TH[a][mu] for a in range(4)} for mu in range(4)]
    Om = []
    for mu in range(4):
        th = [TH[a][mu] for a in range(4)]
        spec = [(1, 0, c10 * bp * th[1]),
                (2, 0, c20 * b / r * th[2]), (3, 0, c20 * b / r * th[3]),
                (2, 1, c21 / r * th[2]), (3, 1, c21 / r * th[3]),
                (3, 2, c32 * cs / sn / r * th[3])]
        Om.append(omega_bivector(spec))
    return {"M": M, "r": r0, "beta": b, "bp": bp, "TH": TH, "g": g, "Om": Om}


def as_field(fld):
    """The gtg.Field of a pg_field dict (coframe TH, background Omega(e_mu))."""
    return gtg.Field(fld["TH"], Om=fld["Om"])


def strength(fld, mu, nu):
    """Background field strength R(e_mu ^ e_nu) = d_mu Omega(e_nu) - d_nu Omega(e_mu)
    + Omega(e_mu) x Omega(e_nu) (LDG sign), value."""
    return as_field(fld).strength(mu, nu)


def curvature(fld):
    """The store's operator on the physical frame planes: calR(gamma_a ^ gamma_b) = -R(hb(gamma_a) ^ hb(gamma_b))."""
    return as_field(fld).curvature()


apply_op = gtg.apply_op                  # extend calR linearly to a bivector


SIG_R = GA.mul(GA.gen(1), GA.gen(0), S13)
PLANES = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def closed_form(M, r):
    """(M/2r^3)(B + 3 sigma_r B sigma_r), the stored Schwarzschild operator (store sign)."""
    def op(B):
        return GA.scal(M / (2 * r ** 3), GA.add(B, GA.scal(3, GA.mul(GA.mul(SIG_R, B, S13), SIG_R, S13))))
    return op


def ricci(Rc, b):
    """calR(b) = sum_a gamma^a . calR(gamma_a ^ b) (vector part), b a frame index."""
    return gtg.ricci(Rc, GA.gen(b))


EXPORTS = {"J": J, "m_val": m_val, "pg_field": pg_field, "curvature": curvature, "apply_op": apply_op,
           "closed_form": closed_form, "ricci": ricci, "SIG_R": SIG_R, "PLANES": PLANES,
           "POINTS": POINTS, "S13": S13, "strength": strength}


def check_radial_curvature_from_gauge_field():
    premise("singularity.connection-bivector-computed")
    for M, beta, s, c in POINTS:
        fld = pg_field(M, beta, s, c)
        r = fld["r"]
        Om = fld["Om"]
        # nothing depends on t, and the two radial-plane values commute (both along sigma_r)
        assert all(x.g[0] == 0 for mu in range(4) for x in Om[mu].values())
        assert m_val(m_comm(Om[0], Om[1])) == {}
        # d_t Omega(e_r) - d_r Omega(e_t) = -d_r(M/r^2) sigma_r = (2M/r^3) sigma_r
        Rtr = strength(fld, 0, 1)
        assert GA.eq(Rtr, GA.scal(2 * M / r ** 3, SIG_R))
        # store sign: calR(g_t ^ g_r) = -R(e_t ^ e_r), and g_t ^ g_r = gamma_0 ^ gamma_1 = -sigma_r
        gt, gr = m_val(fld["g"][0]), m_val(fld["g"][1])
        wedge = GA.scal(F(1, 2), GA.sub(GA.mul(gt, gr, S13), GA.mul(gr, gt, S13)))
        assert GA.eq(wedge, GA.neg(SIG_R))
        assert GA.eq(apply_op(curvature(fld), SIG_R), GA.scal(2 * M / r ** 3, SIG_R))
    rv = GA.RF.var()
    for M in (F(3, 2), F(5)):
        assert (-(GA.RF.const(M) / (rv * rv)).deriv()).eqrf(GA.RF.const(2 * M) / (rv * rv * rv))
    return True


def check_vacuum_curvature_spectrum():
    premise("singularity.connection-bivector-computed")
    for M, beta, s, c in POINTS:
        fld = pg_field(M, beta, s, c)
        r = fld["r"]
        Rc = curvature(fld)
        k = M / r ** 3
        mags = []
        for (a, b) in PLANES:
            B = GA.mul(GA.gen(a), GA.gen(b), S13)
            img = Rc[(a, b)]
            assert list(img.keys()) == [(a, b)]             # each frame plane is an eigenplane
            lam = img[(a, b)] / B[(a, b)]
            mags.append(abs(lam) / k)
            assert GA.eq(img, closed_form(M, r)(B))
        assert mags == [2, 1, 1, 1, 1, 2]
        for b in range(4):
            assert ricci(Rc, b) == {}
    return True


def check_gauge_field_unimodular():
    bt = GA.RF.var()
    et, er = GA.gen(0), GA.gen(1)
    frame = [GA.gen(i) for i in range(4)]
    # matrix of P(a) = (a . e_t) e_r on the frame (columns = images), from GA
    Pm = [[GA.dot(frame[j], et, S13) * er.get((i,), F(0)) for j in range(4)] for i in range(4)]
    hb = [[GA.RF.const(F(1 if i == j else 0)) - bt * GA.RF.const(Pm[i][j]) for j in range(4)]
          for i in range(4)]
    assert GA.rf_mat_det(hb).eqrf(GA.RF1)
    N = [[hb[i][j] - GA.RF.const(F(1 if i == j else 0)) for j in range(4)] for i in range(4)]
    NN = [[sum((N[i][k] * N[k][j] for k in range(4)), GA.RF0) for j in range(4)] for i in range(4)]
    assert all(x.is_zero() for row in NN for x in row) and not all(x.is_zero() for row in N for x in row)
    hinv = [[GA.RF.const(F(1 if i == j else 0)) + bt * GA.RF.const(Pm[i][j]) for j in range(4)]
            for i in range(4)]
    g = [[sum((hinv[k][i] * GA.RF.const(F(ETA[k])) * hinv[k][j] for k in range(4)), GA.RF0)
          for j in range(4)] for i in range(4)]
    det2 = g[0][0] * g[1][1] - g[0][1] * g[1][0]
    assert det2.eqrf(GA.RF.const(-1))
    assert g[0][0].eqrf(GA.RF1 - bt * bt) and g[0][1].eqrf(-bt) and g[1][1].eqrf(GA.RF.const(-1))
    # the divergence sits in Omega and the curvature: their coefficients grow without bound as r -> 0
    vals = []
    for M, beta, s, c in [(F(1), F(1, 2), F(3, 5), F(4, 5)), (F(1), F(2), F(3, 5), F(4, 5)),
                          (F(1), F(8), F(3, 5), F(4, 5))]:
        fld = pg_field(M, beta, s, c)
        vals.append((m_val(fld["Om"][1])[(0, 1)] ** 2, curvature(fld)[(0, 1)][(0, 1)]))
    assert vals[0][0] < vals[1][0] < vals[2][0] and abs(vals[0][1]) < abs(vals[1][1]) < abs(vals[2][1])
    return True
