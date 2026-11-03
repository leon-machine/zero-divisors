"""scrambling.uniqueness-internal-scaling: exact checks of the scaling test.

Dimensional quantities are exact monomials c * 2^a * 3^b * pi^p * M^e with rational c and rational
exponents (factors 2 and 3 folded into the exponents, so equal quantities have equal representations);
every scaling statement is an identity of exponents. Units G = c = hbar = 1.
(1) The framework's cutoff: 2M/r^3 = 1 gives r_c = (2M)^{1/3}, and the slice volume per unit Killing time
    4 pi r_c^2 sqrt(2M/r_c) is exactly 8 pi M (p = 1). The Kretschmann cutoff 48 M^2/r^6 = 1 and the
    unit-proper-time cutoff give radii 2^{2/3} 3^{1/6} M^{1/3} and 3^{2/3} 2^{-1/3} M^{1/3}: the same
    M-exponent 1/3 and the same p = 1, with order-one coefficients.
(2) Alternatives: the sphere-only count 4 pi r_c^2 has exponent 2/3 and the fixed-radius volume
    4 pi r_0^2 sqrt(2M/r_0) has exponent 1/2, so with Delta t of order M they give M^{5/3} and M^{3/2};
    the area law M^2 then needs q = 4/3 and q = 3/2, outside the admissible set {1, 3} (a logarithmic
    dressing multiplies by ln M and changes no exponent). Over all computed schemes, p = 1 is the only
    exponent with 2 - p admissible, and it needs q = 1, an order-M timescale.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


class Mono(object):
    __slots__ = ("c", "a", "b", "p", "e")

    def __init__(self, c=1, a=0, b=0, p=0, e=0):
        c, a, b = F(c), F(a), F(b)
        if c != 0:
            n, d = c.numerator, c.denominator
            while n % 2 == 0:
                n //= 2
                a += 1
            while d % 2 == 0:
                d //= 2
                a -= 1
            while n % 3 == 0:
                n //= 3
                b += 1
            while d % 3 == 0:
                d //= 3
                b -= 1
            c = F(n, d)
        self.c, self.a, self.b, self.p, self.e = c, a, b, F(p), F(e)

    def __mul__(self, o):
        return Mono(self.c * o.c, self.a + o.a, self.b + o.b, self.p + o.p, self.e + o.e)

    def __truediv__(self, o):
        return Mono(self.c / o.c, self.a - o.a, self.b - o.b, self.p - o.p, self.e - o.e)

    def pow(self, q):
        q = F(q)
        assert self.c == 1
        return Mono(1, self.a * q, self.b * q, self.p * q, self.e * q)

    def __eq__(self, o):
        return (self.c, self.a, self.b, self.p, self.e) == (o.c, o.a, o.b, o.p, o.e)


M = Mono(e=1)
PI = Mono(p=1)
TWO = Mono(a=1)
THREE = Mono(b=1)
R0 = Mono(1, -2, 2)                        # a mass-independent cutoff radius, 9/4
ADMISSIBLE = (F(1), F(3))                  # Delta t ~ M (crossing, epoch, modular) and ~ M^3 (lifetime)


def num(x):
    return Mono(c=x)


def slice_volume(r):
    return num(4) * PI * r * r * (TWO * M / r).pow(F(1, 2))


def check_internal_cutoff_gives_linear_volume():
    premise("scrambling.slice-volume-exactly-per-unit-killing")
    r_c = (TWO * M).pow(F(1, 3))
    assert r_c * r_c * r_c == TWO * M
    assert slice_volume(r_c) == num(8) * PI * M
    r_k = (TWO.pow(4) * THREE * M * M).pow(F(1, 6))
    assert r_k == Mono(1, F(2, 3), F(1, 6), 0, F(1, 3))
    assert (r_k * r_k * r_k) * (r_k * r_k * r_k) == num(48) * M * M
    r_t = (THREE / TWO).pow(F(2, 3)) * (TWO * M).pow(F(1, 3))
    assert r_t == Mono(1, F(-1, 3), F(2, 3), 0, F(1, 3))
    # (2/3) r^{3/2} (2M)^{-1/2} = 1 at r_t
    assert num(F(2, 3)) * r_t.pow(F(3, 2)) * (TWO * M).pow(F(-1, 2)) == num(1)
    for r in (r_c, r_k, r_t):
        assert r.e == F(1, 3) and slice_volume(r).e == 1


def check_alternatives_fail_and_p_one_is_unique():
    r_c = (TWO * M).pow(F(1, 3))
    sphere = num(4) * PI * r_c * r_c
    fixed = slice_volume(R0)
    internal = slice_volume(r_c)
    assert sphere.e == F(2, 3) and fixed.e == F(1, 2) and internal.e == 1
    order_M = M
    assert (sphere * order_M).e == F(5, 3) and (fixed * order_M).e == F(3, 2)
    assert (internal * order_M).e == 2
    needed = {s: F(2) - v.e for s, v in (("sphere", sphere), ("fixed", fixed), ("internal", internal))}
    assert needed == {"sphere": F(4, 3), "fixed": F(3, 2), "internal": F(1)}
    working = [s for s, q in needed.items() if q in ADMISSIBLE]
    assert working == ["internal"] and needed["internal"] == ADMISSIBLE[0]
    lifetime_p = F(2) - ADMISSIBLE[1]
    assert lifetime_p == -1 and lifetime_p not in [v.e for v in (sphere, fixed, internal)]
