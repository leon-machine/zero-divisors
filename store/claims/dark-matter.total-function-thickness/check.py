"""dark-matter.total-function-thickness: exact checks.

Numbers of Q(pi) are Laurent polynomials in pi, {k: c} for sum c pi^k (pi transcendental, so
polynomial identities are identities of reals); a thickness c is passed as a monomial, so that
c = pi/2 and c = pi/(2c') are exact. Decimal statements use rational bounds on pi and integer
square roots (no floating point). Observed ratio 0.1200/0.02237 with sigma 0.065.

(0) The family from the densities: rho_5D = m c/(V_4 d^3), rho_3D = m/(c V_2 d^3), rho_us =
    m/(V_3 d^3) give f_3D = 4/(3c), f_5D = 8c/(3 pi), and with the mirror's share 1 and two equal
    shares in each odd pair, T(c) = 1 + 8/(3c) + 16c/(3 pi), at sample c and two unit lengths d.
(i)   T(c) = T(pi/(2c)) as an identity in pi for sample rational c.
(ii)  With A = 8/3, B = 16/(3 pi): (T(c) - 1)^2 - 4AB = (A/c - Bc)^2 (identity), so T >= T* =
      1 + 2 sqrt(AB), with equality iff c^2 = A/B = pi/2; (T* - 1)^2 = 512/(9 pi) = 4 * 128/(9 pi);
      c* in (1.25325, 1.25335), T* in (5.2553, 5.2555), and (obs - T*)/sigma in (1.65, 1.75).
(iii) c = 1 and c = pi/2 both solve B c^2 - (T(1) - 1) c + A = 0 (identity in pi), with product
      A/B = pi/2; T(1) = T(pi/2) in (5.36425, 5.36435).
(iv)  One-sigma windows: the four boundaries are bracketed to round to 0.943, 1.086, 1.447, 1.667
      (T - obs crosses sigma between c - 1/2000 and c + 1/2000 of each endpoint); between the windows
      (c = 1.25) T is below obs - sigma; the two-sigma set is one interval whose ends round to 0.898
      and 1.750, and the floor T* is inside it.
(v)   The three-dimensional fraction 2 f_3D / T = 8/(3c T(c)) is in (0.4965, 0.4975) at c = 1,
      (0.4045, 0.4055) at c*, and (0.3155, 0.3165) at c = pi/2.
"""
from fractions import Fraction as F

import GA
from series import rounds_to
from tp_premise import premise

PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)
OBS = F(1200, 10000) / F(2237, 100000)
SIG = F(65, 1000)
SAMPLE_C = [F(1), F(2), F(1, 2), F(3, 7), F(5)]
UNITS = [F(1), F(49, 50)]
MASS = F(938, 7)


def lp(c, k=0):
    return {k: F(c)} if c != 0 else {}


def ladd(*xs):
    out = {}
    for x in xs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def lmul(*xs):
    out = {0: F(1)}
    for b in xs:
        new = {}
        for k1, c1 in out.items():
            for k2, c2 in b.items():
                new[k1 + k2] = new.get(k1 + k2, F(0)) + c1 * c2
        out = {k: c for k, c in new.items() if c != 0}
    return out


def linv(a):
    assert len(a) == 1
    (k, c), = a.items()
    return {-k: 1 / c}


def bounds(x):
    lo = hi = F(0)
    for k, c in x.items():
        u, v = c * PI_LO ** k, c * PI_HI ** k
        lo += min(u, v)
        hi += max(u, v)
    return lo, hi


def ball(D):
    V = {0: lp(1), 1: lp(2)}
    for n in range(2, D + 1):
        V[n] = lmul(lp(F(2, n), 1), V[n - 2])
    return V[D]


def T(c):
    """the stated closed form, c a monomial"""
    return ladd(lp(1), lmul(lp(F(8, 3)), linv(c)), lmul(lp(F(16, 3), -1), c))


def isqrt(n):
    if n < 2:
        return n
    x, y = n, (n + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def sqrt_bounds(q, scale=10 ** 12):
    """rational (lo, hi) with lo <= sqrt(q) <= hi"""
    s = isqrt(q.numerator * scale * scale // q.denominator)
    return F(s, scale), F(s + 1, scale)


def check_family_from_densities():
    premise("dark-matter.r1-equal-mass-per-quantum")
    premise("dark-matter.r2-one-quantum-per-unit-ball")
    premise("dark-matter.projection-every-towers-content-dilutes-ones")
    premise("dark-matter.population-count-one-share-half-percent")
    premise("dark-matter.p2-indifference")
    for c in SAMPLE_C:
        for d in UNITS:
            r5 = lmul(lp(MASS * c / d ** 3), linv(ball(4)))
            r3 = lmul(lp(MASS / (c * d ** 3)), linv(ball(2)))
            ru = lmul(lp(MASS / d ** 3), linv(ball(3)))
            f5, f3 = lmul(r5, linv(ru)), lmul(r3, linv(ru))
            assert f3 == {0: F(4, 3) / c} and f5 == {-1: F(8, 3) * c}
            total = ladd(lp(1), lmul(lp(2), f3), lmul(lp(2), f5))
            assert total == T(lp(c))
            assert total == {0: 1 + F(8, 3) / c, -1: F(16, 3) * c}
    return True


def check_exchange_symmetry():
    for c in SAMPLE_C:
        assert T(lp(c)) == T(lmul(lp(F(1, 2), 1), linv(lp(c))))
    assert T(lp(1)) == T(lp(F(1, 2), 1))
    return True


def check_minimum():
    A, B = lp(F(8, 3)), lp(F(16, 3), -1)
    for c in SAMPLE_C:
        t1 = ladd(T(lp(c)), lp(-1))
        lhs = ladd(lmul(t1, t1), lmul(lp(-4), A, B))
        diff = ladd(lmul(A, linv(lp(c))), lmul(lp(-1), B, lp(c)))
        assert lhs == lmul(diff, diff)
    assert lmul(A, linv(B)) == {1: F(1, 2)}                  # c*^2 = pi/2
    four_ab = lmul(lp(4), A, B)
    assert four_ab == {-1: F(512, 9)} and four_ab == lmul(lp(4), lp(F(128, 9), -1))
    c2_lo, c2_hi = PI_LO / 2, PI_HI / 2
    assert F(125325, 100000) ** 2 < c2_lo and c2_hi < F(125335, 100000) ** 2
    s_lo, _ = sqrt_bounds(F(512, 9) / PI_HI)
    _, s_hi = sqrt_bounds(F(512, 9) / PI_LO)
    t_lo, t_hi = 1 + s_lo, 1 + s_hi
    assert F(52553, 10000) < t_lo and t_hi < F(52555, 10000)
    assert F(165, 100) < (OBS - t_hi) / SIG and (OBS - t_lo) / SIG < F(175, 100)
    return True


def check_two_roots():
    A, B = lp(F(8, 3)), lp(F(16, 3), -1)
    t1m = ladd(T(lp(1)), lp(-1))
    for root in (lp(1), lp(F(1, 2), 1)):
        quad = ladd(lmul(B, root, root), lmul(lp(-1), t1m, root), A)
        assert quad == {}
    assert lmul(A, linv(B)) == lmul(lp(1), lp(F(1, 2), 1))
    lo, hi = bounds(T(lp(1)))
    assert F(536425, 100000) < lo and hi < F(536435, 100000)
    assert T(lp(F(1, 2), 1)) == T(lp(1))
    return True


def sig_dist(c):
    lo, hi = bounds(T(lp(c)))
    return (lo - OBS) / SIG, (hi - OBS) / SIG


def check_windows():
    # each endpoint e: one side of e -/+ 1/2000 is inside k sigma, the other outside
    for e, k, inside_right in ((943, 1, True), (1086, 1, False), (1447, 1, True), (1667, 1, False),
                               (898, 2, True), (1750, 2, False)):
        left, right = F(2 * e - 1, 2000), F(2 * e + 1, 2000)
        l_lo, l_hi = sig_dist(left)
        r_lo, r_hi = sig_dist(right)
        if inside_right:
            assert abs(l_lo) > k and abs(l_hi) > k and abs(r_lo) < k and abs(r_hi) < k
        else:
            assert abs(l_lo) < k and abs(l_hi) < k and abs(r_lo) > k and abs(r_hi) > k
    lo, hi = sig_dist(F(125, 100))
    assert hi < -1
    s_lo, _ = sqrt_bounds(F(512, 9) / PI_HI)
    assert (OBS - (1 + s_lo)) / SIG < 2
    return True


def check_self_interacting_fraction():
    # by hand (decimal evaluation): 8/(3 T(1)) = 0.4971118 and, at c = pi/2, 16/(3 pi T(pi/2)) = 0.3164712,
    # which round to the quoted 0.497 and 0.316
    for c, m7, m3 in ((lp(1), 4971118, 497), (lp(F(1, 2), 1), 3164712, 316)):
        num = bounds(lmul(lp(F(8, 3)), linv(c)))
        den = bounds(T(c))
        for q in (num[0] / den[1], num[1] / den[0]):
            assert rounds_to(q, m7, -7) and rounds_to(q, m3, -3)
    # at c* = sqrt(pi/2): with x = sqrt(2/pi), 8/(3c*) = 8x/3 and T* = 1 + 16x/3
    x_lo, _ = sqrt_bounds(2 / PI_HI)
    _, x_hi = sqrt_bounds(2 / PI_LO)
    f_lo = (8 * x_lo / 3) / (1 + 16 * x_hi / 3)
    f_hi = (8 * x_hi / 3) / (1 + 16 * x_lo / 3)
    # by hand: 0.4048595, the quoted 0.405
    assert all(rounds_to(f, 4048595, -7) and rounds_to(f, 405, -3) for f in (f_lo, f_hi))
    return True
