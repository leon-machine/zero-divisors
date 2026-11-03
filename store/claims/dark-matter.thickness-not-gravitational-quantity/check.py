"""dark-matter.thickness-not-gravitational-quantity: exact checks of the computable part.

(1) Inverse cube below the extent: on scales below L a metric fifth direction makes space
    four-dimensional, where the Newtonian potential is 1/r^2: its Laplacian in R^4, computed as the
    sum of exact second derivatives (GA.RF) of 1/|p + t e_i|^2 at t = 0, vanishes at sample points,
    and |grad(1/r^2)|^2 r^6 = 4, so the force falls as 2/r^3. Control: in R^3 the same potential has
    Laplacian 2/r^4, not zero.
(2) The two extents, from the record (Planck 2018: Omega_b h^2 = 0.02237, H_0 = 67.36 km/s/Mpc,
    Omega_Lambda = 0.6847; G, m_p, c and the megaparsec from CODATA/IAU): n_b = Omega_b h^2
    3 H_100^2/(8 pi G m_p) rounds to 0.25 m^-3; d_b = (3/(4 pi n_b))^(1/3) lies in (0.95, 1.02) (the
    script's bracket) and rounds to 0.98 m; l = sqrt(3/Lambda), Lambda = 3 Omega_Lambda H_0^2/c^2,
    lies in [10^26, 10^27) m (1.7 x 10^26 m).
(3) Both exceed the 50 micrometre bound of the imported short-range test (and the 40 micrometre
    extra-dimension bound) by a factor above 10^4: d_b by about 2.0 (2.5) x 10^4, l by about
    3.3 (4.1) x 10^30.
pi is bracketed by rationals; roots by integer roots; a rounded value is checked as both ends of
the computed interval rounding to it. Not computable:
the reading of P1 and the statements about what the series does not supply.
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)
OMEGA_B_H2 = F(2237, 100000)
H0_KMS_MPC = F(6736, 100)
OMEGA_L = F(6847, 10000)
G_NEWTON = F(667430, 10 ** 5) * F(1, 10 ** 11)          # m^3 kg^-1 s^-2
M_P = F(167262192, 10 ** 8) * F(1, 10 ** 27)             # kg
C_LIGHT = F(299792458)                                    # m/s
MPC = F(30856775814913673, 10 ** 16) * 10 ** 22           # m
POINTS4 = [[F(1), F(2), F(-1), F(3)], [F(1, 2), F(0), F(2, 3), F(-5)], [F(7), F(1), F(1), F(1)]]


def potential_along(p, i):
    """1/|p + t e_i|^2 as a rational function of t"""
    s0 = sum(x * x for x in p)
    return GA.RF([F(1)], [s0, 2 * p[i], F(1)])


def laplacian(p):
    total = F(0)
    for i in range(len(p)):
        g = potential_along(p, i)
        total += g.deriv().deriv().eval(0)
    return total


def grad_sq(p):
    return sum(potential_along(p, i).deriv().eval(0) ** 2 for i in range(len(p)))


def check_inverse_cube_below_extent():
    for p in POINTS4:
        r2 = sum(x * x for x in p)
        assert laplacian(p) == 0
        assert grad_sq(p) * r2 ** 3 == 4
        q = p[:3]
        rq2 = sum(x * x for x in q)
        assert laplacian(q) * rq2 ** 2 == 2
    return True


def extents():
    h100 = F(100000) / MPC                                   # 100 km/s/Mpc in s^-1
    rho_lo = OMEGA_B_H2 * 3 * h100 ** 2 / (8 * PI_HI * G_NEWTON)
    rho_hi = OMEGA_B_H2 * 3 * h100 ** 2 / (8 * PI_LO * G_NEWTON)
    nb = (rho_lo / M_P, rho_hi / M_P)
    db3 = (3 / (4 * PI_HI * nb[1]), 3 / (4 * PI_LO * nb[0]))
    H0 = H0_KMS_MPC * 1000 / MPC
    lam = 3 * OMEGA_L * H0 ** 2 / C_LIGHT ** 2
    l2 = 3 / lam
    return nb, db3, l2


def iroot(q, k):
    """rational (lo, hi), multiples of 10^-12, bracketing the k-th root of q > 0"""
    return series.iroot_bracket(q, k, 10 ** 12)


def rounded(iv, scale):
    """the common value of both ends of an interval rounded to a multiple of 1/scale, else None"""
    a, b = round(iv[0] * scale), round(iv[1] * scale)
    return F(a, scale) if a == b else None


def lengths():
    nb, db3, l2 = extents()
    db = (iroot(db3[0], 3)[0], iroot(db3[1], 3)[1])
    l = (iroot(l2, 2)[0], iroot(l2, 2)[1])
    return nb, db, l


def check_the_two_extents():
    nb, db, l = lengths()
    assert rounded(nb, 100) == F(25, 100)
    assert F(95, 100) < db[0] and db[1] < F(102, 100)
    assert rounded(db, 100) == F(98, 100)
    assert 10 ** 26 <= l[0] and l[1] < 10 ** 27
    assert rounded((l[0] / 10 ** 26, l[1] / 10 ** 26), 10) == F(17, 10)
    return True


def check_both_exceed_the_short_range_bound():
    premise("dark-matter.imported-inverse-square-law-short-range")
    nb, db, l = lengths()
    bound, extra = F(50, 10 ** 6), F(40, 10 ** 6)
    for b, d_ratio, l_ratio in ((bound, 20, F(33, 10)), (extra, 25, F(41, 10))):
        assert db[0] / b > 10 ** 4 and l[0] / b > 10 ** 4
        assert rounded((db[0] / b / 1000, db[1] / b / 1000), 1) == d_ratio
        assert rounded((l[0] / b / 10 ** 30, l[1] / b / 10 ** 30), 10) == l_ratio
    return True
