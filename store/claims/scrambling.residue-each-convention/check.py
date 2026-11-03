"""scrambling.residue-each-convention: exact checks.

Exact monomials c 2^a 3^b pi^p M^e L^l with L = ln 2 a formal symbol. Units G = c = hbar = 1,
A = 4 pi (2M)^2 = 16 pi M^2, S_BH = A/4, N_epoch = kappa_c x A x 1.
(i)   1-nat convention: N_epoch = S_BH gives kappa_c = S_BH/A = 1/4.
(ii)  Capacity convention: N_epoch L = S_BH gives kappa_c = (1/4) L^-1, i.e. A/N_epoch = 4 L Planck
      areas per mode per period.
(iii) The two residues differ by exactly the factor L; the 16 pi thinning N_slice/S_BH of the 1-nat
      convention becomes N_slice/(S_BH/L) = 16 pi L. A two-dimensional state space holds at most
      ln 2 nats: the maximally mixed state's entropy -sum p ln p at p = (1/2, 1/2) is L (formal), and
      ln 2 < 1 because e > 1 + 1 + 1/2 > 2 (positive series, exact partial sum); so the 1-nat
      convention credits a mode with more than it holds.
(iv)  The lift's homogeneities -2s - 2 at s = +-1, +-2 are -4, 0, -6, +2, pairwise distinct (no
      channel holds both helicities); with one helicity per mode the capacity per mode is L and
      kappa_c = (1/4) L^-1, whereas 2L per mode would give (1/8) L^-1. That one mode registers one
      helicity is the lift's modelling joint J3 and is not checked.
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


def horizon():
    A = num(4) * PI * (num(2) * M) * (num(2) * M)
    return A, A / num(4)


def check_residues_in_both_conventions():
    premise("scrambling.integer-holographic-form-identification")
    A, S_BH = horizon()
    assert A == num(16) * PI * M * M and S_BH == num(4) * PI * M * M
    kappa_nat = S_BH / A
    assert kappa_nat == num(F(1, 4))
    N_cap = S_BH / LN2
    kappa_cap = N_cap / A
    assert kappa_cap == num(F(1, 4)) / LN2
    assert A / N_cap == num(4) * LN2
    return True


def check_conventions_differ_by_ln2():
    premise("singularity.area-law-test")
    A, S_BH = horizon()
    kappa_nat, kappa_cap = S_BH / A, (S_BH / LN2) / A
    assert kappa_nat / kappa_cap == LN2
    N_slice = num(64) * PI * PI * M * M
    assert N_slice / S_BH == num(16) * PI
    assert N_slice / (S_BH / LN2) == num(16) * PI * LN2
    # entropy of the maximally mixed qubit state, in units of L: sum p log_2(1/p) at p = (1/2, 1/2)
    probs = [F(1, 2), F(1, 2)]
    s_coeff = sum(p * Mono(1 / p).x["2"] for p in probs)
    assert all(Mono(1 / p) == TWO.pow(Mono(1 / p).x["2"]) for p in probs)
    assert s_coeff == 1
    # ln 2 < 1 iff e > 2: the partial sum of sum 1/k! over k = 0, 1, 2 already exceeds 2
    fact, partial = 1, F(0)
    for k in range(3):
        fact = fact * k if k else 1
        partial += F(1, fact)
    assert partial == F(5, 2) and partial > 2
    return True


def check_one_helicity_per_mode():
    premise("scrambling.imported-collars-coframe-exceptional-set-helicity")
    hom = {s: -2 * s - 2 for s in (-2, -1, 1, 2)}
    assert hom == {-2: 2, -1: 0, 1: -4, 2: -6}
    assert len(set(hom.values())) == 4
    A, S_BH = horizon()
    for per_mode, expect in ((ONE, F(1, 4)), (num(2), F(1, 8))):
        kappa = S_BH / (A * per_mode * LN2)
        assert kappa == num(expect) / LN2
    return True
