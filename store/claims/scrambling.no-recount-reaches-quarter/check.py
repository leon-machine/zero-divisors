"""scrambling.no-recount-reaches-quarter: exact checks.

Exact monomials c 2^a 3^b pi^p M^e L^l, L = ln 2 a formal symbol. Units G = c = hbar = 1,
A = 16 pi M^2, S_BH = A/4.
(1) Closure: for every counting rule built from a rational number of modes per cell (8 values), a
    cell area q pi^k in Planck units (q over 6 rationals, k = -2..3) and a rational number of ticks
    per period (5 values), 1440 rules, the residue kappa_c = N_epoch/A with
    N_epoch = modes x (A/cell) x ticks is dimensionless, L-free, with integer pi-exponent and
    rational coefficient: kappa_c = q' pi^k'.
(2) Targets: none of these residues equals the capacity target (1/4) L^-1 as a formal expression
    (the L-exponent is 0 for every rule and -1 for the target); the 1-nat target 1/4 is reached
    (one quarter mode per horizon cell, once per period). That no rational q pi^k equals 1/(4 ln 2)
    numerically needs the transcendence of ln 2 (k = 0, an import) or the algebraic independence of
    pi and ln 2 (k != 0, conjectural); neither is certified here.
(3) The natural rules: P1 (one fermion per slice cell, N = 16 pi S_BH) has kappa_c = 4 pi and P3
    (A per period) has kappa_c = 1; neither is 1/4.
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

MODES = [F(1), F(1, 2), F(3), F(1, 4), F(2, 3), F(5), F(1, 7), F(9, 4)]
CELL_Q = [F(1), F(4), F(1, 2), F(3), F(2, 9), F(7)]
CELL_K = [-2, -1, 0, 1, 2, 3]
TICKS = [F(1), F(2), F(1, 2), F(3, 7), F(5, 3)]


def horizon():
    A = num(16) * PI * M * M
    return A, A / num(4)


def residues():
    A, S_BH = horizon()
    out = []
    for m in MODES:
        for q in CELL_Q:
            for k in CELL_K:
                cell = num(q) * PI.pow(k)
                for t in TICKS:
                    N_epoch = num(m) * (A / cell) * num(t)
                    out.append(N_epoch / A)
    return out


def check_residue_closure():
    premise("scrambling.candidate-principles-their-yields")
    rs = residues()
    assert len(rs) == 1440
    for r in rs:
        assert r.x["M"] == 0 and r.x["L"] == 0
        assert r.x["pi"].denominator == 1
        assert r.x["2"].denominator == 1 and r.x["3"].denominator == 1
    assert {int(r.x["pi"]) for r in rs} == {2, 1, 0, -1, -2, -3}
    return True


def check_targets():
    premise("scrambling.residue-each-convention")
    A, S_BH = horizon()
    target_cap = (S_BH / LN2) / A
    target_nat = S_BH / A
    assert target_cap == num(F(1, 4)) / LN2 and target_cap.x["L"] == -1
    assert target_nat == num(F(1, 4))
    rs = residues()
    assert all(r != target_cap for r in rs)
    assert sum(1 for r in rs if r == target_nat) >= 1
    return True


def check_natural_rules():
    premise("scrambling.candidate-principles-their-yields")
    A, S_BH = horizon()
    P1 = num(16) * PI * S_BH
    P3 = A
    # exact yields 4 pi and 1, neither of which is the quarter
    assert P1 / A == num(4) * PI and P3 / A == ONE
    return True
