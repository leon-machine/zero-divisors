"""scrambling.per-slice-verification-two-failed-aggregations: exact checks.

Exact monomials c 2^a 3^b pi^p M^e (rational exponents). Units G = c = hbar = l_P = 1.
(1) The slice-cell count at the curvature cutoff r_c = (2M)^(1/3) (solved from 2M/r^3 = 1):
    n^2 = 4 pi r_c^2 = 4 pi (2M)^(2/3), M-exponent 2/3; it carries the factor 2^(2/3), so it is not
    a rational multiple of a power of pi: only the scaling is fixed exactly.
(2) Operator-cell aggregation (nu = 1): V/S_BH = 16 pi with V = (8 pi M) beta, beta = 8 pi M.
(3) Fundamental-per-slice aggregation: spheres per unit Killing time = slice volume / n^2
    = (2M)^(1/3); with n = (n^2)^(1/2) of M-exponent 1/3 and Delta t = beta, the count has
    M-exponent 1/3 + 1/3 + 1 = 5/3, not 2.
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


def slice_data():
    r_c = (TWO * M).pow(F(1, 3))
    vol = num(4) * PI * r_c * r_c * (TWO * M / r_c).pow(F(1, 2))
    n_sq = num(4) * PI * r_c * r_c
    beta = num(8) * PI * M
    S_BH = num(4) * PI * M * M
    return r_c, vol, n_sq, beta, S_BH


def check_slice_check_scaling():
    premise("scrambling.slice-volume-exactly-per-unit-killing")
    r_c, vol, n_sq, beta, S_BH = slice_data()
    assert num(2) * M / r_c.pow(3) == ONE
    assert n_sq == num(4) * PI * TWO.pow(F(2, 3)) * M.pow(F(2, 3))
    assert n_sq.x["M"] == F(2, 3)
    assert n_sq.x["2"].denominator != 1               # not rational times a power of pi
    return True


def check_operator_cell_aggregation_overshoot():
    premise("scrambling.integer-holographic-form-identification")
    r_c, vol, n_sq, beta, S_BH = slice_data()
    V = vol * beta
    assert V / S_BH == num(16) * PI
    return True


def check_fundamental_aggregation_breaks_scaling():
    premise("scrambling.slice-volume-exactly-per-unit-killing")
    r_c, vol, n_sq, beta, S_BH = slice_data()
    spheres_per_t = vol / n_sq
    assert spheres_per_t == (TWO * M).pow(F(1, 3))
    n = n_sq.pow(F(1, 2)) if n_sq.c == 1 else None
    assert n is not None and n.x["M"] == F(1, 3)
    N_fund = n * spheres_per_t * beta
    assert N_fund.x["M"] == F(5, 3)
    assert N_fund.x["M"] != S_BH.x["M"]
    return True
