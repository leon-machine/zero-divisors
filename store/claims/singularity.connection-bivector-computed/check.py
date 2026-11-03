"""singularity.connection-bivector-computed: exact checks in Gauge Theory Gravity.

Flat spacetime: the vectors of Cl(1,3) (GA.py, signature (+,-,-,-)), with background labels
x = (t, r, theta, phi). The Painleve-Gullstrand gauge field hb = 1 - beta P, beta^2 = 2M/r, is given
by its physical frame g_mu = hb^{-1}(e_mu) = sum_a theta^a_mu gamma_a (gamma_a the constant
orthonormal generators, the coframe of the statement): theta^0 = dt, theta^1 = beta dt + dr,
theta^2 = r dtheta, theta^3 = r sin(theta) dphi. The rotation-gauge field Omega(e_mu) is assembled from
the stated one-forms omega^a_b so that Omega(e_mu) x gamma_b = sum_a omega^a_b(e_mu) gamma_a (GTG sign,
D_a M = a.grad M + Omega(a) x M; checked on every gamma_b), and sigma_r = gamma_1 gamma_0 = e_r e_t.
Scalars are exact first-order jets (value and gradient in the four labels) at rational points
(M, beta, sin theta, cos theta), r = 2M/beta^2, beta obtained as the exact square root of 2M/r.
(1) In Q(r)[beta] with beta^2 = 2M/r (two values of M), as exact identities: beta' = -beta/2r,
    beta beta' = -M/r^2, (beta')^2 = M/(2 r^3); and at every sample point the jet derivative of beta
    equals -beta/2r.
(2) Torsion: D_mu g_nu = D_nu g_mu for all six pairs at six sample points (horizon beta = 1
    included), with the stated forms; the torsion map Omega -> (Omega(e_mu) x g_nu - Omega(e_nu) x g_mu)
    has rank 24 on the 24-dimensional space of bivector-valued Omega, so the stated Omega is the
    unique solution; a control with omega^2_0 perturbed is not torsion-free.
(3) On the background directions e_t, e_r: Omega(e_t) = (M/r^2) sigma_r = -beta beta' sigma_r and
    Omega(e_r) = (beta/2r) sigma_r = -beta' sigma_r, whose coefficient squares to M/(2 r^3).
EXPORTS: J, multivector helpers, pg_field(M, beta, s, c, coeffs) for the dependent checks.
"""
from fractions import Fraction as F

import GA
import gtg

S13 = gtg.S13
ETA = gtg.ETA
# sample points (M, beta, sin theta, cos theta); r = 2M/beta^2
POINTS = [(F(1), F(1, 2), F(3, 5), F(4, 5)), (F(3, 2), F(1), F(5, 13), F(12, 13)),
          (F(1), F(2), F(4, 5), F(3, 5)), (F(2, 3), F(3, 5), F(8, 17), F(15, 17)),
          (F(5), F(7, 3), F(12, 13), F(-5, 13)), (F(1, 2), F(1, 3), F(3, 5), F(-4, 5))]


# jets and jet multivectors: lib/gtg.py
J = gtg.J
m_add = gtg.m_add
m_scal = gtg.m_scal
m_mul = gtg.m_mul
m_comm = gtg.comm                         # (xy - yx)/2
m_d = gtg.m_d
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


def torsion(fld, mu, nu):
    """D_{e_mu} g_nu - D_{e_nu} g_mu (value)."""
    return as_field(fld).torsion(mu, nu)


def torsion_rank(fld):
    """Rank of the linear map Omega -> torsion at the point (values), on all 24 unknowns."""
    return as_field(fld).torsion_rank()


EXPORTS = {"J": J, "m_add": m_add, "m_scal": m_scal, "m_mul": m_mul, "m_comm": m_comm,
           "m_d": m_d, "m_val": m_val, "pg_field": pg_field, "torsion": torsion, "POINTS": POINTS}


class BR(object):
    """Elements a + b beta of Q(r)[beta], beta^2 = 2M/r (a, b rational functions of r)."""

    def __init__(self, M, ev=None, od=None):
        self.M = M
        self.ev = ev if ev is not None else GA.RF0
        self.od = od if od is not None else GA.RF0

    def __add__(self, o):
        return BR(self.M, self.ev + o.ev, self.od + o.od)

    def __sub__(self, o):
        return BR(self.M, self.ev - o.ev, self.od - o.od)

    def __mul__(self, o):
        b2 = GA.RF.const(2 * self.M) / GA.RF.var()
        return BR(self.M, self.ev * o.ev + self.od * o.od * b2, self.ev * o.od + self.od * o.ev)

    def deriv(self):
        """d/dr, with beta' read off d(beta^2)/dr = -2M/r^2: beta' = -(M/r^2)/beta = -beta/(2r)."""
        r = GA.RF.var()
        # d(od * beta) = od' beta + od beta', beta' = -(M/(r^2)) beta / beta^2 = -(M/r^2) (r/2M) beta
        bprime_over_beta = -(GA.RF.const(self.M) / (r * r)) * (r / GA.RF.const(2 * self.M))
        return BR(self.M, self.ev.deriv(), self.od.deriv() + self.od * bprime_over_beta)

    def eq(self, o):
        return (self - o).ev.is_zero() and (self - o).od.is_zero()


def check_beta_identities_in_q_r_beta():
    for M in (F(3, 2), F(5)):
        r = GA.RF.var()
        b = BR(M, GA.RF0, GA.RF1)
        bp = b.deriv()
        assert bp.eq(BR(M, GA.RF0, -(GA.RF.const(F(1, 2)) / r)))
        assert (b * bp).eq(BR(M, -(GA.RF.const(M) / (r * r))))
        assert (bp * bp).eq(BR(M, GA.RF.const(M) / (GA.RF.const(2) * r * r * r)))
    for M, beta, s, c in POINTS:
        fld = pg_field(M, beta, s, c)
        r = fld["r"]
        assert fld["beta"].g[1] == -beta / (2 * r)
        assert fld["beta"].v * fld["beta"].g[1] == -M / (r * r)
    return True


def check_stated_connection_solves_torsion_uniquely():
    for M, beta, s, c in POINTS:
        fld = pg_field(M, beta, s, c, (-1, -1, 1, 1))
        # assembly: Omega(e_mu) x gamma_b = sum_a omega^a_b(e_mu) gamma_a on the spot check e_t, gamma_0
        Ot = m_val(fld["Om"][0])
        lhs = GA.scal(F(1, 2), GA.sub(GA.mul(Ot, GA.gen(0), S13), GA.mul(GA.gen(0), Ot, S13)))
        assert GA.eq(lhs, GA.scal(-fld["bp"].v * fld["beta"].v, GA.gen(1)))
        for mu in range(4):
            for nu in range(mu + 1, 4):
                assert torsion(fld, mu, nu) == {}, (M, beta, mu, nu)
        assert torsion_rank(fld) == 24
        bad = pg_field(M, beta, s, c, (-1, 1, 1, 1))
        assert any(torsion(bad, mu, nu) for mu in range(4) for nu in range(mu + 1, 4))
    return True


def check_connection_on_radial_plane():
    sig_r = GA.mul(GA.gen(1), GA.gen(0), S13)
    for M, beta, s, c in POINTS:
        fld = pg_field(M, beta, s, c)
        r = fld["r"]
        Ot, Or = m_val(fld["Om"][0]), m_val(fld["Om"][1])
        assert GA.eq(Ot, GA.scal(M / r ** 2, sig_r))
        assert GA.eq(Ot, GA.scal(-fld["beta"].v * fld["bp"].v, sig_r))
        assert GA.eq(Or, GA.scal(beta / (2 * r), sig_r))
        assert GA.eq(Or, GA.scal(-fld["bp"].v, sig_r))
        coef = Or[(0, 1)] * -1          # Or = coef * gamma_1 gamma_0 = -coef * gamma_0 gamma_1
        assert coef > 0 and coef * coef == M / (2 * r ** 3)
    return True
