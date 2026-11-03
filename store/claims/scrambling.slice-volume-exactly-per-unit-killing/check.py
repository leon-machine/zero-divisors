"""scrambling.slice-volume-exactly-per-unit-killing: exact checks in Gauge Theory Gravity.

The Schwarzschild field in the Painleve-Gullstrand gauge on flat spacetime Cl(1,3): hb = 1 - beta P,
P(a) = (a . e_t) e_r, beta = sqrt(2M/r), hb^{-1} = 1 + beta P; frame e_t, e_r, e_theta, e_phi (gamma0..gamma3).
Volumes carry the factor pi symbolically: the checks compare the rational coefficient of pi.
(1) Induced geometry of the background slice r = r_c inside the horizon (beta > 1): the tangent vectors d_t, d_theta,
    d_phi sit over e_t, r e_theta, r sin(theta) e_phi; the Gram matrix -Q(hb^{-1}(.)) on them is
    diag(f, r^2, r^2 sin^2 theta) with f = 2M/r - 1 > 0 (Q(hb^{-1}(e_t)) = 1 - beta^2 = -f), so
    ds_3^2 = f dt^2 + r_c^2 dOmega^2 and the volume per unit t is 4 pi r_c^2 sqrt(f) (sqrt(det) = sqrt(f) r^2 sin(theta),
    and int sin(theta) dtheta dphi = 4 pi). Samples with beta, sqrt(f), sin rational; hb hb^{-1} = 1 checked.
(2) The cutoff r_c = (2M)^{1/3}: for 2M = t^3, r_c = t and 2M/r_c = t^2, so 4 r_c^2 sqrt(2M/r_c) = 4 t^3 = 8M
    exactly (coefficient of pi), at several t; the M-exponent is 2/3 + (1/2)(1 - 1/3) = 1, while an M-independent
    cutoff gives 1/2. The neglected factor sqrt(1 - r_c/2M) has r_c/2M = (2M)^{-2/3} (exponent -2/3); at t = 5/4
    the full volume 4 r_c^2 sqrt(f) is exactly 3/5 = sqrt(1 - 1/t^2) of 8M.
"""
from fractions import Fraction as F

import GA

S13 = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]
# (M, r, sin theta) with beta = sqrt(2M/r) and sqrt(f) rational: 2M/r = 25/9 (f = 16/9), 2M/r = 25/16 (f = 9/16)
SLICES = [(F(25, 18), F(1), F(3, 5)), (F(25, 32), F(1), F(5, 13)), (F(25, 4), F(9, 2), F(4, 5))]
TS = [F(2), F(5, 4), F(3, 7), F(10)]


def isqrt(n):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def sqrt_q(x):
    """Exact rational square root of x >= 0, or None."""
    a, b = isqrt(x.numerator), isqrt(x.denominator)
    return F(a, b) if a * a == x.numerator and b * b == x.denominator else None


def hbinv(a, beta):
    return GA.add(a, GA.scal(beta * GA.dot(a, E[0], S13), E[1]))


def hbf(a, beta):
    return GA.sub(a, GA.scal(beta * GA.dot(a, E[0], S13), E[1]))


def check_induced_slice_geometry_and_volume():
    ok = True
    for M, r, sn in SLICES:
        beta = sqrt_q(2 * M / r)
        ok = ok and beta is not None and beta > 1
        f = 2 * M / r - 1
        sf = sqrt_q(f)
        ok = ok and sf is not None and f > 0
        ok = ok and all(GA.eq(hbf(hbinv(a, beta), beta), a) for a in E)
        ok = ok and GA.dot(hbinv(E[0], beta), hbinv(E[0], beta), S13) == 1 - beta * beta == -f
        tang = [E[0], GA.scal(r, E[2]), GA.scal(r * sn, E[3])]
        phys = [hbinv(v, beta) for v in tang]
        gram = [[-GA.dot(u, v, S13) for v in phys] for u in phys]
        ok = ok and gram == [[f, 0, 0], [0, r * r, 0], [0, 0, r * r * sn * sn]]
        det = gram[0][0] * gram[1][1] * gram[2][2]
        ok = ok and det == (sf * r * r * sn) ** 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_induced_slice_geometry_and_volume"; return _tp_rv


def check_cutoff_gives_exactly_eight_pi_m():
    ok = True
    for t in TS:
        M = t ** 3 / 2
        rc = t
        ok = ok and rc ** 3 == 2 * M
        root = sqrt_q(2 * M / rc)
        ok = ok and root == t and 4 * rc * rc * root == 8 * M
    # M-scaling, M -> 8M (t -> 2t): the volume scales by 8 (exponent 1), r_c/2M by 1/4 = 8^(-2/3);
    # with an M-independent cutoff r_c = 1, M -> 4M scales 4 r_c^2 sqrt(2M/r_c) by 2 = 4^(1/2)
    vol = lambda tt: 4 * tt * tt * sqrt_q(tt ** 3 / tt)
    ok = ok and vol(2 * TS[1]) == 8 * vol(TS[1])
    ok = ok and ((2 * TS[1]) / (2 * TS[1]) ** 3) / (TS[1] / TS[1] ** 3) == F(1, 4)
    fixed = lambda MM: 4 * sqrt_q(2 * MM)
    ok = ok and fixed(F(8)) == 2 * fixed(F(2))
    t = F(5, 4)
    M, rc = t ** 3 / 2, t
    f = 2 * M / rc - 1
    ok = ok and rc / (2 * M) == 1 / (t * t)
    ok = ok and 4 * rc * rc * sqrt_q(f) == F(3, 5) * 8 * M and sqrt_q(1 - rc / (2 * M)) == F(3, 5)
    _tp_rv = (ok); assert _tp_rv is not False, "check_cutoff_gives_exactly_eight_pi_m"; return _tp_rv
