"""scrambling.area-law-test: exact checks.

Dimensional quantities are exact monomials c 2^a 3^b pi^p M^e (rational c, rational exponents;
factors of 2 and 3 folded into the exponents so equal quantities have equal representations).
Units G = c = hbar = 1.
(1) The count and the area law: the slice volume per unit Killing time is computed from the
    curvature cutoff, 4 pi r_c^2 sqrt(2M/r_c) with r_c = (2M)^(1/3), giving 8 pi M (Theorem
    mode-count); with nu Delta t = xi M the count N = 8 pi M nu Delta t equals S_BH = 4 pi M^2
    (with A = 4 pi (2M)^2, S_BH = A/4 derived) exactly at xi = 1/2 and at no other sampled xi:
    N / S_BH = 2 xi.
(2) The causal epoch's scale (Fact causal-epoch-computed-exactly): Delta t(eps) =
    2M(ln(1/eps) - 8/3 + 2 ln 2) at eps = 2^-k is 2M((k + 2) ln 2 - 8/3), linear in M; with ln 2
    bracketed exactly by its series sum_j 1/(j 2^j) and the tail bound, it is positive and below
    2M ln(1/eps) for k = 2..12: of order M up to a logarithm.
(3) Lifetime counting: Delta t ~ M^3 gives N ~ M^4; the interior volume with dV/dv ~ M^2 over the
    lifetime gives V ~ M^5; both are linear in the time span, with different mass exponents.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# ---- exact monomials c * 2^a * 3^b * pi^p * M^e * L^l (L = ln 2 as a formal symbol) --------
class Mono(object):
    __slots__ = ("c", "x")
    KEYS = ("2", "3", "pi", "M", "L")

    def __init__(self, c=1, **ex):
        c = F(c)
        x = {k: F(ex.get(k, 0)) for k in Mono.KEYS}
        if c != 0:
            num, den = c.numerator, c.denominator
            for pr, key in ((2, "2"), (3, "3")):
                while num % pr == 0:
                    num //= pr
                    x[key] += 1
                while den % pr == 0:
                    den //= pr
                    x[key] -= 1
            c = F(num, den)
        self.c, self.x = c, x

    def __mul__(self, o):
        return Mono(self.c * o.c, **{k: self.x[k] + o.x[k] for k in Mono.KEYS})

    def __truediv__(self, o):
        return Mono(self.c / o.c, **{k: self.x[k] - o.x[k] for k in Mono.KEYS})

    def pow(self, q):
        q = F(q)
        assert self.c in (1, -1) and (self.c == 1 or q.denominator == 1)
        return Mono(self.c ** q.numerator if self.c == -1 else 1, **{k: self.x[k] * q for k in Mono.KEYS})

    def __eq__(self, o):
        return self.c == o.c and self.x == o.x

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash((self.c, tuple(self.x[k] for k in Mono.KEYS)))

    def __repr__(self):
        return "%s*%s" % (self.c, self.x)

    def is_rational(self):
        return all(self.x[k] == 0 for k in ("pi", "M", "L")) and \
            self.x["2"].denominator == 1 and self.x["3"].denominator == 1


def num(c):
    return Mono(c)


ONE = Mono(1)
TWO = Mono(**{"2": 1})
THREE = Mono(**{"3": 1})
PI = Mono(pi=1)
M = Mono(M=1)
LN2 = Mono(L=1)

XI_SAMPLES = [F(1, 4), F(1, 3), F(1, 2), F(1), F(3, 2), F(2)]


def anchors():
    r_c = (TWO * M).pow(F(1, 3))
    vol = num(4) * PI * r_c * r_c * (TWO * M / r_c).pow(F(1, 2))
    r_s = TWO * M
    A = num(4) * PI * r_s * r_s
    return vol, A / num(4)


def ln2_bounds(n=40):
    s = sum(F(1, j * 2 ** j) for j in range(1, n + 1))
    return s, s + F(1, (n + 1) * 2 ** n)


def check_area_law_iff_half_mass():
    premise("scrambling.mode-count")
    vol, S_BH = anchors()
    assert vol == num(8) * PI * M
    assert S_BH == num(4) * PI * M * M
    hits = []
    for xi in XI_SAMPLES:
        N = vol * Mono(xi) * M                    # nu Delta t = xi M
        assert N / S_BH == num(2 * xi)
        if N == S_BH:
            hits.append(xi)
    assert hits == [F(1, 2)]
    return True


# Sample exponents k for eps = 2^-k, and the precision demanded of the exact ln 2 bracket and of the
# resulting Delta t bracket (any small width serves).
EPS_EXPONENTS = range(2, 13)
LN2_WIDTH = F(1, 10 ** 12)
DT_WIDTH = F(1, 10 ** 10)


def check_causal_epoch_order_m():
    premise("singularity.causal-epoch-computed-exactly")
    lo, hi = ln2_bounds()
    assert lo < hi and hi - lo < LN2_WIDTH
    # by hand from the Fact: 2 ln(1/eps) - Delta t / M = 2 (8/3 - 2 ln 2) = 16/3 - 4 ln 2, the same for
    # every eps, and positive (ln 2 < 4/3), so Delta t < 2 M ln(1/eps) at every eps
    c_lo, c_hi = F(16, 3) - 4 * hi, F(16, 3) - 4 * lo
    assert c_lo > 0
    for k in EPS_EXPONENTS:
        # Delta t / M = 2 (ln(1/eps) - 8/3 + 2 ln 2) at eps = 2^-k, ln(1/eps) = k ln 2
        dt_lo = 2 * ((k + 2) * lo - F(8, 3))
        dt_hi = 2 * ((k + 2) * hi - F(8, 3))
        assert dt_lo == 2 * k * lo - c_hi and dt_hi == 2 * k * hi - c_lo
        assert dt_lo > 0
        assert dt_hi < 2 * k * lo                 # below 2 M ln(1/eps)
        assert dt_hi - dt_lo < DT_WIDTH
    return True


def check_lifetime_scaling():
    premise("scrambling.mode-count")
    vol, S_BH = anchors()
    N_life = vol * M.pow(3)                       # nu of order one, Delta t ~ M^3
    assert N_life.x["M"] == 4
    V_life = M.pow(2) * M.pow(3)                  # dV/dv ~ M^2 over a lifetime ~ M^3
    assert V_life.x["M"] == 5
    # both linear in the span: doubling the span doubles each
    assert vol * (num(2) * M.pow(3)) == num(2) * N_life
    assert M.pow(2) * (num(2) * M.pow(3)) == num(2) * V_life
    return True
