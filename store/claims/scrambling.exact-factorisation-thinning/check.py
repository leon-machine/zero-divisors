"""scrambling.exact-factorisation-thinning: exact checks.

Exact monomials c 2^a 3^b pi^p M^e (2 and 3 folded out of c). Units G = c = hbar = 1, r_h = 2M,
A = 4 pi r_h^2, S_BH = A/4, kappa = 1/(2 r_h), beta = 2 pi/kappa.
(i)   The slice count per unit Killing time, 4 pi r_c^2 sqrt(2M/r_c) at the curvature cutoff
      r_c = (2M)^(1/3) (computed), is 8 pi M = 4 pi r_h = A/r_h. The leading-order qualifier: the
      neglected factor is sqrt(1 - r_c/2M), and r_c/2M = (2M)^(-2/3) has negative M-exponent.
(ii)  Per modular period N_slice = 64 pi^2 M^2 and N_slice/S_BH = 16 pi.
(iii) 16 pi = (beta/r_h)(A/S_BH) = 4 pi x 4; beta/r_h = 2 pi/(kappa r_h) = 4 pi has M-exponent 0
      (universal for Schwarzschild), and A/S_BH = 4.
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


def geometry():
    r_h = num(2) * M
    A = num(4) * PI * r_h * r_h
    S_BH = A / num(4)
    kappa = ONE / (num(2) * r_h)
    beta = num(2) * PI / kappa
    r_c = (TWO * M).pow(F(1, 3))
    vol = num(4) * PI * r_c * r_c * (TWO * M / r_c).pow(F(1, 2))
    return r_h, A, S_BH, kappa, beta, r_c, vol


def check_slice_count_per_unit_time():
    premise("scrambling.slice-volume-exactly-per-unit-killing")
    r_h, A, S_BH, kappa, beta, r_c, vol = geometry()
    assert vol == num(8) * PI * M
    assert vol == num(4) * PI * r_h and vol == A / r_h
    ratio = r_c / (num(2) * M)
    assert ratio == (TWO * M).pow(F(-2, 3)) and ratio.x["M"] < 0
    return True


def check_slice_count_per_period():
    premise("scrambling.slice-volume-exactly-per-unit-killing")
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    r_h, A, S_BH, kappa, beta, r_c, vol = geometry()
    assert beta == num(8) * PI * M
    N_slice = vol * beta
    assert N_slice == num(64) * PI * PI * M * M
    assert N_slice / S_BH == num(16) * PI
    return True


def check_factorisation():
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    r_h, A, S_BH, kappa, beta, r_c, vol = geometry()
    f1, f2 = beta / r_h, A / S_BH
    assert f1 == num(4) * PI and f1.x["M"] == 0
    assert num(2) * PI / (kappa * r_h) == num(4) * PI
    assert f2 == num(4)
    assert f1 * f2 == num(16) * PI == (vol * beta) / S_BH
    return True
