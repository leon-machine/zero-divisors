"""scrambling.candidate-principles-their-yields: exact checks.

Exact monomials c 2^a 3^b pi^p M^e (rational exponents, 2 and 3 folded out of c). Units G = c =
hbar = 1, r_h = 2M, A = 4 pi r_h^2, S_BH = A/4, kappa = 1/(2 r_h), beta = 2 pi/kappa.
(P1) The slice count per modular period N_slice = (slice volume per unit t) x beta, with the
     volume 4 pi r_c^2 sqrt(2M/r_c) at the curvature cutoff, is 64 pi^2 M^2 = 16 pi S_BH. The three
     schemes' constants are obtained by solving each cutoff condition (2M/r^3 = 1,
     48 M^2/r^6 = 1, (2/3) r^(3/2) (2M)^(-1/2) = 1) and substituting back; the volume is
     4 pi sqrt(2M) r_c^(3/2), so the count scales as c_0^(3/2): proper-time / curvature = 3/2
     exactly (rational), Kretschmann / curvature = 2^(1/2) 3^(1/4) = 12^(1/4) (irrational:
     non-integral prime exponents).
(P3) The horizon-normalised coframe weights of Fact imported-collars: in units 2M = 1,
     (r^(1/2) sqrt(A))^2 = r (1/r - 1) = 1 - r as a polynomial identity (GA.RF), equal to 1 at the
     exceptional set r = 0, and r^-1 . r = 1; the sphere of radius r_h carries A Planck cells, so
     one per period gives A = 4 S_BH, with no cutoff constant (no 2^(1/3) or 3^(1/6) in it).
(P2) Fundamentals per sphere aggregated over the epoch scale as M^(5/3) (from the slice volume and
     n^2 = 4 pi r_c^2), not M^2: the M-scaling breaks.
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


def schwarzschild():
    r_h = num(2) * M
    A = num(4) * PI * r_h * r_h
    S_BH = A / num(4)
    kappa = ONE / (num(2) * r_h)
    beta = num(2) * PI / kappa
    return r_h, A, S_BH, beta


def slice_volume(r):
    return num(4) * PI * r * r * (TWO * M / r).pow(F(1, 2))


def scheme_radii():
    r_curv = (TWO * M).pow(F(1, 3))
    r_kret = (num(16) * THREE * M * M).pow(F(1, 6))
    r_prop = (THREE / TWO).pow(F(2, 3)) * (TWO * M).pow(F(1, 3))
    return r_curv, r_kret, r_prop


def check_p1_slice_count_scheme_bound():
    premise("scrambling.exact-factorisation-thinning")
    premise("scrambling.scheme-robustness-cutoff")
    r_h, A, S_BH, beta = schwarzschild()
    r_curv, r_kret, r_prop = scheme_radii()
    # each radius solves its cutoff condition
    assert num(2) * M / (r_curv * r_curv * r_curv) == ONE
    assert num(48) * M * M / (r_kret.pow(6)) == ONE
    assert num(2) / num(3) * r_prop.pow(F(3, 2)) * (num(2) * M).pow(F(-1, 2)) == ONE
    N_slice = slice_volume(r_curv) * beta
    assert N_slice == num(64) * PI * PI * M * M
    assert N_slice / S_BH == num(16) * PI
    # the volume is 4 pi sqrt(2M) r^(3/2), so the count scales as c_0^(3/2)
    for r in (r_curv, r_kret, r_prop):
        assert slice_volume(r) == num(4) * PI * (TWO * M).pow(F(1, 2)) * r.pow(F(3, 2))
    prop_ratio = slice_volume(r_prop) / slice_volume(r_curv)
    kret_ratio = slice_volume(r_kret) / slice_volume(r_curv)
    assert prop_ratio == num(F(3, 2)) and prop_ratio.is_rational()
    assert kret_ratio == Mono(**{"2": F(1, 2), "3": F(1, 4)})
    assert kret_ratio.pow(4) == num(12)
    assert not kret_ratio.is_rational()
    return True


def check_p3_horizon_normalised_count():
    premise("scrambling.imported-collars-coframe-exceptional-set-helicity")
    r = GA.RF.var()
    one = GA.RF.const(1)
    # (r^(1/2) sqrt(A))^2 = r A with A = 1/r - 1 (units 2M = 1)
    sq = r * (one / r - one)
    assert sq.eqrf(one - r)
    assert sq.eval(F(0)) == 1 and sq.eval(F(1, 2)) == F(1, 2) and sq.eval(F(1)) == 0
    assert (one / r * r).eqrf(one)
    r_h, A, S_BH, beta = schwarzschild()
    cells = num(4) * PI * r_h * r_h                 # Planck cells on the sphere of radius r_h
    assert cells == A and cells / S_BH == num(4)
    assert cells.x["2"].denominator == 1 and cells.x["3"].denominator == 1
    return True


def check_p2_breaks_scaling():
    premise("scrambling.per-slice-verification-two-failed-aggregations")
    r_h, A, S_BH, beta = schwarzschild()
    r_curv = scheme_radii()[0]
    n_sq = num(4) * PI * r_curv * r_curv
    spheres_per_t = slice_volume(r_curv) / n_sq
    N_fund = n_sq.pow(F(1, 2)) * spheres_per_t * beta
    assert N_fund.x["M"] == F(5, 3)
    assert N_fund.x["M"] != S_BH.x["M"]
    return True
