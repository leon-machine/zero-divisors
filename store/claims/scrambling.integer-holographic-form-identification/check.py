"""scrambling.integer-holographic-form-identification: exact checks.

Exact monomials c 2^a 3^b pi^p M^e (2 and 3 folded out of c). Units G = c = hbar = l_P = 1.
(1) The slice volume per unit Killing time, computed at the curvature cutoff r_c = (2M)^(1/3), is
    8 pi M (Theorem mode-count) and beta = 2 pi/kappa with kappa = 1/(4M) is 8 pi M (Theorem
    epoch-modular-period), so V = (8 pi M) beta = 64 pi^2 M^2 = beta^2.
(2) N_epoch = nu V equals S_BH = A/4 = 4 pi M^2 (A = 4 pi (2M)^2) exactly at nu = 1/(16 pi):
    the solution S_BH/V is unique, and among sampled nu = c/pi only c = 1/16 gives S_BH; per
    horizon area, S_BH/A = 1/4 (one fermion per four Planck cells).
(3) The naive reading nu = 1 overshoots by V/S_BH = 16 pi = A/M^2.
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


def epoch_volume():
    r_c = (TWO * M).pow(F(1, 3))
    vol = num(4) * PI * r_c * r_c * (TWO * M / r_c).pow(F(1, 2))
    kappa = ONE / (num(4) * M)
    beta = num(2) * PI / kappa
    A = num(4) * PI * (num(2) * M) * (num(2) * M)
    return vol, beta, A, A / num(4)


def check_epoch_volume_is_beta_squared():
    premise("scrambling.mode-count")
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    vol, beta, A, S_BH = epoch_volume()
    assert vol == num(8) * PI * M and beta == num(8) * PI * M
    V = vol * beta
    assert V == num(64) * PI * PI * M * M
    assert V == beta * beta
    return True


def check_density_iff_integer_count():
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    vol, beta, A, S_BH = epoch_volume()
    V = vol * beta
    assert S_BH / V == num(F(1, 16)) / PI
    hits = [c for c in (F(1, 4), F(1, 8), F(1, 16), F(1, 32), F(1)) if (num(c) / PI) * V == S_BH]
    assert hits == [F(1, 16)]
    assert S_BH == num(4) * PI * M * M and S_BH / A == num(F(1, 4))
    return True


def check_naive_overshoot_is_area_coefficient():
    premise("scrambling.mode-count")
    vol, beta, A, S_BH = epoch_volume()
    V = vol * beta
    assert V / S_BH == num(16) * PI
    assert V / S_BH == A / (M * M)
    return True
