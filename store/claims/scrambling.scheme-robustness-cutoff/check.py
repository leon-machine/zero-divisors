"""scrambling.scheme-robustness-cutoff: exact checks.

Planck units (l_P = 1). Quantities of the form +- prod_p p^(a_p) * M^e with rational exponents are
exact monomials (class Mono: prime exponents and the M exponent as Fractions), so real roots such as
48^(1/6) are handled exactly.
(1) The three cutoffs, each solved and substituted back: r_1 = 2^(1/3) M^(1/3) gives 2M/r^3 = 1;
    r_2 = 48^(1/6) M^(1/3) gives 48 M^2/r^6 = 1; r_3 = (3/2)^(2/3) 2^(1/3) M^(1/3) gives
    tau(r) = (2/3) r^(3/2) (2M)^(-1/2) = 1. All three are c_0 M^(1/3) with the same exponent 1/3.
(2) The proper time: from the premise's interior integral tau(r) = int_0^r A(u)^(-1/2) du with
    A = 2M/u - 1, A(u)^(-1) = u/(2M - u) (checked at sample points) and the binomial series of
    (1 - x)^(-1/2) (GA.ps_pow_rat), integrated term by term: tau = (2/3) r^(3/2) (2M)^(-1/2) (1 + (3/10)
    (r/2M) + ...), the premise's expansion in units 2M = 1; its leading term is the one used in (1).
(3) Order one: c_0^6 = 4, 48 and 81/4 exactly, and the constants lie in (1.255, 1.265),
    (1.905, 1.915), (1.645, 1.655) (compared through sixth powers), all in (1, 2).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def factor(n):
    out, d = {}, 2
    while n > 1:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    return out


class Mono(object):
    def __init__(self, q=1, mexp=0, exps=None):
        q = F(q)
        assert q > 0
        e = dict(exps or {})
        for p, k in factor(q.numerator).items():
            e[p] = e.get(p, F(0)) + k
        for p, k in factor(q.denominator).items():
            e[p] = e.get(p, F(0)) - k
        self.e = {p: F(k) for p, k in e.items() if k != 0}
        self.m = F(mexp)

    def __mul__(self, o):
        e = dict(self.e)
        for p, k in o.e.items():
            e[p] = e.get(p, F(0)) + k
        return Mono(1, self.m + o.m, e)

    def pw(self, a):
        a = F(a)
        return Mono(1, self.m * a, {p: k * a for p, k in self.e.items()})

    def __eq__(self, o):
        return self.e == o.e and self.m == o.m

    def rational(self):
        if self.m != 0 or any(k.denominator != 1 for k in self.e.values()):
            return None
        out = F(1)
        for p, k in self.e.items():
            out *= F(p) ** int(k)
        return out


M = Mono(1, 1)
ONE = Mono(1)


def check_three_cutoffs_solve_exactly():
    r1 = (Mono(2) * M).pw(F(1, 3))
    assert Mono(2) * M * r1.pw(-3) == ONE
    r2 = Mono(48).pw(F(1, 6)) * M.pw(F(1, 3))
    assert Mono(48) * M.pw(2) * r2.pw(-6) == ONE
    r3 = Mono(F(3, 2)).pw(F(2, 3)) * Mono(2).pw(F(1, 3)) * M.pw(F(1, 3))
    tau = Mono(F(2, 3)) * r3.pw(F(3, 2)) * (Mono(2) * M).pw(F(-1, 2))
    assert tau == ONE
    for r in (r1, r2, r3):
        assert r.m == F(1, 3)
    # the stated constants
    assert r1 == Mono(2).pw(F(1, 3)) * M.pw(F(1, 3))
    assert r3 == (Mono(F(3, 2)) * Mono(F(3, 2)) * Mono(2)).pw(F(1, 3)) * M.pw(F(1, 3))
    return True


def check_proper_time_leading_term():
    premise("interior.kasner-form-interior")
    for twoM in (F(1), F(3), F(5, 2)):
        for u in (F(1, 7), F(1, 2), twoM / 3):
            A = twoM / u - 1
            assert 1 / A == u / (twoM - u)
    # (1 - x)^(-1/2) = sum c_j x^j; tau = (2M)^(-1/2) sum_j c_j (2M)^(-j) r^(j + 3/2) / (j + 3/2)
    c = GA.ps_pow_rat([F(1), F(-1)], F(-1, 2), 4)
    assert c[:3] == [F(1), F(1, 2), F(3, 8)]
    coeffs = [c[j] / (j + F(3, 2)) for j in range(3)]
    assert coeffs[0] == F(2, 3)
    assert coeffs[1] / coeffs[0] == F(3, 10)
    return True


def check_constants_order_one():
    sixth = [Mono(2).pw(F(1, 3)), Mono(48).pw(F(1, 6)),
             Mono(F(3, 2)).pw(F(2, 3)) * Mono(2).pw(F(1, 3))]
    vals = [x.pw(6).rational() for x in sixth]
    assert vals == [F(4), F(48), F(81, 4)]
    bounds = [(F(1255, 1000), F(1265, 1000)), (F(1905, 1000), F(1915, 1000)),
              (F(1645, 1000), F(1655, 1000))]
    for v, (lo, hi) in zip(vals, bounds):
        assert lo ** 6 < v < hi ** 6
        assert 1 < v < 2 ** 6
    return True
