"""scrambling.exactness-excludes-cutoff-dependence: exact checks.

Exact monomials c 2^a 3^b pi^p M^e (rational exponents; 2 and 3 folded out of c). Units
G = c = hbar = 1.
(1) The scheme constants are obtained by solving the three cutoff conditions of Lemma
    scheme-robustness-cutoff (2M/r^3 = 1, 48 M^2/r^6 = 1, (2/3) r^(3/2) (2M)^(-1/2) = 1) and
    dividing by M^(1/3): c_0 = 2^(1/3), 2^(2/3) 3^(1/6), 2^(-1/3) 3^(2/3). For every rational
    a = k/d != 0 with 1 <= d <= 12, |k| <= 24, the three c_0^a are pairwise different, so a count
    c pi^p M^m r_c^a takes three different values and cannot equal S_BH in all schemes.
(2) Rationality: 48^(a/6) = 2^(2a/3) 3^(a/6) is rational exactly when a is in 6Z, over the same
    grid of a; at a = 3/2 it is 2 3^(1/4).
(3) The two cutoff-free scales: r_h = 2M carries 4 pi r_h^2 = A = 4 S_BH Planck cells (residue
    1/4), r_* = r_h/2 = M carries 4 pi M^2 = S_BH cells (residue 1); both are fixed multiples of M
    (M-exponent of r/M is 0) and both cell counts are free of any scheme constant.
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

A_GRID = [F(k, d) for d in range(1, 13) for k in range(-24, 25) if k != 0]


def scheme_constants():
    r_curv = (TWO * M).pow(F(1, 3))
    r_kret = (num(16) * THREE * M * M).pow(F(1, 6))
    r_prop = (THREE / TWO).pow(F(2, 3)) * (TWO * M).pow(F(1, 3))
    return r_curv, r_kret, r_prop


def check_scheme_constants_differ():
    premise("scrambling.scheme-robustness-cutoff")
    r_curv, r_kret, r_prop = scheme_constants()
    assert num(2) * M / r_curv.pow(3) == ONE
    assert num(48) * M * M / r_kret.pow(6) == ONE
    assert num(2) / num(3) * r_prop.pow(F(3, 2)) * (num(2) * M).pow(F(-1, 2)) == ONE
    m13 = M.pow(F(1, 3))
    c = [r / m13 for r in (r_curv, r_kret, r_prop)]
    assert c[0] == Mono(**{"2": F(1, 3)})
    assert c[1] == Mono(**{"2": F(2, 3), "3": F(1, 6)})
    assert c[2] == Mono(**{"2": F(-1, 3), "3": F(2, 3)})
    count = 0
    for a in A_GRID:
        vals = [x.pow(a) for x in c]
        assert vals[0] != vals[1] and vals[0] != vals[2] and vals[1] != vals[2]
        # a count carrying r_c^a with any coefficient differs between schemes
        counts = [num(F(3, 7)) * PI * M * M * (r.pow(a)) for r in (r_curv, r_kret, r_prop)]
        assert len(set(counts)) == 3
        count += 1
    assert count == len(A_GRID)
    return True


def check_kretschmann_rationality():
    premise("scrambling.scheme-robustness-cutoff")
    c_k = (num(16) * THREE).pow(F(1, 6))            # 48^(1/6)
    for a in A_GRID + [F(0)]:
        val = c_k.pow(a)
        assert val.is_rational() == (a.denominator == 1 and a.numerator % 6 == 0)
    assert c_k.pow(F(3, 2)) == num(2) * THREE.pow(F(1, 4))
    return True


def check_two_cutoff_free_scales():
    premise("scrambling.residue-each-convention")
    r_h = num(2) * M
    A = num(4) * PI * r_h * r_h
    S_BH = A / num(4)
    r_star = r_h / num(2)
    assert r_star == M
    cells_h = num(4) * PI * r_h * r_h
    cells_s = num(4) * PI * r_star * r_star
    assert cells_h == A and cells_h / S_BH == num(4) and S_BH / cells_h == num(F(1, 4))
    assert cells_s == S_BH and S_BH / cells_s == ONE
    for r in (r_h, r_star):
        assert (r / M).x["M"] == 0 and (r / M).is_rational()
    return True
