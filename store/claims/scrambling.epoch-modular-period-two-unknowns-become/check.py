"""scrambling.epoch-modular-period-two-unknowns-become: exact checks.

Exact monomials c 2^a 3^b pi^p M^e L^l (L = ln 2 as a formal symbol). Units G = c = hbar = 1.
(1) The epoch: kappa = 1/(2 r_s) with r_s = 2M is 1/(4M); a clock normalised to unit rapidity
    has conjugation period 2 pi in its Euclidean continuation (on a unit-rapidity block A^2 = 1,
    so (iA)^2 = -1 and exp(theta iA) has period 2 pi; checked on the atom's block, ad of sigma/2
    on the vectors of Cl(1,1) computed in GA.py), and the
    conversion at kappa gives Delta t = beta = 2 pi / kappa = 8 pi M. The e-folding time 1/kappa is
    4M = beta/(2 pi), not a period.
(2) Both directions: the count over the epoch is N = (8 pi M) nu beta (slice volume per unit time
    8 pi M), so N = S_BH = 4 pi M^2 iff nu Delta t = M/2 (Proposition area-law-test) iff
    nu = (M/2)/beta = 1/(16 pi): among sampled densities exactly this one gives S_BH, and
    nu beta = M/2 at it. In the capacity convention (count times ln 2 equals S_BH) the same
    condition gives nu = 1/(16 pi ln 2), the 1-nat value divided by L.
The premise (IC) is assumed, not checked.
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


def check_epoch_is_the_modular_period():
    premise("scrambling.clock-inventory-boundary-modes")
    premise("singularity.euclidean-rotor-where-it-lies")
    r_s = num(2) * M
    kappa = ONE / (num(2) * r_s)
    assert kappa == num(F(1, 4)) / M
    # the atom's unit-rapidity block, computed: ad of sigma/2 = e0 e1 / 2 on the vectors of Cl(1,1)
    S = GA.sig(1, 1)
    half_sigma = {(0, 1): F(1, 2)}
    cols = []
    for a in range(2):
        w = GA.sub(GA.mul(half_sigma, GA.gen(a), S), GA.mul(GA.gen(a), half_sigma, S))
        cols.append([w.get((b,), F(0)) for b in range(2)])
    A = [[cols[j][i] for j in range(2)] for i in range(2)]
    A2 = [[sum(A[i][k] * A[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    assert A2 == [[1, 0], [0, 1]]                  # so (iA)^2 = -A^2 = -1: period 2 pi
    beta = num(2) * PI / kappa
    assert beta == num(8) * PI * M
    efold = ONE / kappa
    assert efold == num(4) * M and beta / efold == num(2) * PI
    return True


def check_density_prediction_both_directions():
    premise("scrambling.area-law-test")
    vol = num(8) * PI * M                          # slice cells per unit Killing time
    beta = num(8) * PI * M
    S_BH = num(4) * PI * M * M
    nu_pred = (Mono(F(1, 2)) * M) / beta
    assert nu_pred == num(F(1, 16)) / PI
    hits = []
    for c in (F(1, 8), F(1, 16), F(1, 32), F(1, 4)):
        nu = num(c) / PI
        if vol * nu * beta == S_BH:
            hits.append(c)
        assert (nu * beta == Mono(F(1, 2)) * M) == (vol * nu * beta == S_BH)
    assert hits == [F(1, 16)]
    # capacity convention: (count) ln 2 = S_BH
    nu_cap = S_BH / (vol * beta * LN2)
    assert nu_cap == num(F(1, 16)) / (PI * LN2) and nu_cap * LN2 == nu_pred
    return True
