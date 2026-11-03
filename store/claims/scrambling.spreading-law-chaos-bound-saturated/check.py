"""scrambling.spreading-law-chaos-bound-saturated: exact checks of the computable core.

Checked: the boost flow's exponential action on the ladder operators, the threshold e^{kappa t_*} = N, and
the rate arithmetic. Not checked (no finite exact content): the generic-coupling operator-spreading model
itself and the Maldacena-Shenker-Stanford bound, which enter as the declared rate-model tier.
(1) In the atom Cl(1,1) (GA), sigma = e+ e- squares to 1 and the rotor R(x) = (x + 1/x)/2 + (x - 1/x)/2 sigma
    (x = e^{lambda/2}, lambda = kappa t the rapidity) has inverse (x + 1/x)/2 - (x - 1/x)/2 sigma, scales
    the ladder operators f = (e+ + e-)/2, f* = (e+ - e-)/2 by x^{-2} and x^2, that is e^{-+kappa t}, and obeys
    R(x) R(y) = R(xy) (the flow is a one-parameter group, amplitudes grow as e^{kappa t}). In Cl(2,2) (two
    modes) the common boost R_1(x) R_2(x) scales all four ladder operators with the same factors: one
    rapidity for every mode.
(2) Threshold: an amplitude 1/N carried by the flow reaches 1 exactly when e^{kappa t} = x^2 = N (checked
    at N = 4, 9, 25, 49 with x^2 = N, and strictly below 1 at the previous integer x), so
    t_* = kappa^{-1} ln N; with ln N a formal logarithm (LogVec) and N = S, t_* = 4M ln S.
(3) Rates: kappa = f'(2M)/2 = 1/(4M) from f = 1 - 2M/r (exact rational functions, several M), so
    beta = 2 pi/kappa = 8 pi M, beta/(2 pi) = 1/kappa = 4M, and the expansion rate kappa equals 2 pi T
    with T = 1/beta (pi formal).
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

# --- formal logarithms: a LogVec is a finite rational combination sum_p a_p ln p over primes, so
# entropies of rational spectra are exact LogVecs; inequalities are decided by rigorous rational
# bounds on ln p (ln p = a ln 2 + 2 atanh z, atanh summed with an explicit geometric tail bound) ---

def factorise(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


class LogVec(object):
    def __init__(self, d=None):
        self.d = {p: F(c) for p, c in (d or {}).items() if c != 0}

    @staticmethod
    def ln_int(n):
        return LogVec({p: e for p, e in factorise(n).items()})

    @staticmethod
    def ln_rat(q):
        q = F(q)
        assert q > 0
        return LogVec.ln_int(q.numerator) - LogVec.ln_int(q.denominator)

    def __add__(self, o):
        d = dict(self.d)
        for p, c in o.d.items():
            d[p] = d.get(p, F(0)) + c
        return LogVec(d)

    def __neg__(self):
        return LogVec({p: -c for p, c in self.d.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, c):
        return LogVec({p: v * F(c) for p, v in self.d.items()})

    __rmul__ = __mul__

    def __eq__(self, o):
        return self.d == o.d

    def __ne__(self, o):
        return not self.__eq__(o)


_LNB = {}
def ln_bounds(n):
    """Rational (lower, upper) bounds on ln n, n a positive integer (series.ln_bounds, cached)."""
    if n not in _LNB:
        _LNB[n] = series.ln_bounds(n)
    return _LNB[n]


def logvec_bounds(v):
    lo, hi = F(0), F(0)
    for p, c in v.d.items():
        a, b = ln_bounds(p)
        if c > 0:
            lo += c * a
            hi += c * b
        else:
            lo += c * b
            hi += c * a
    return lo, hi


def logvec_lt(u, v):
    """u < v, decided rigorously; equal vectors give False."""
    if u == v:
        return False
    lo, hi = logvec_bounds(v - u)
    if lo > 0:
        return True
    if hi < 0:
        return False
    raise ValueError("bounds too weak")


def logvec_le(u, v):
    return u == v or logvec_lt(u, v)


def entropy(probs):
    """-sum p ln p of a rational spectrum, as a LogVec (nats)."""
    out = LogVec()
    for p in probs:
        if p != 0:
            assert p > 0
            out = out - LogVec.ln_rat(p) * p
    return out

SQ11 = (1, -1)
SQ22 = (1, 1, -1, -1)
XS = [F(2), F(3, 2), F(5), F(1, 3)]
NS = [4, 9, 25, 49]
MASSES = [F(1), F(3, 2), F(7)]


def rotor(x, plus, minus, sq):
    sig = GA.mul(GA.gen(plus), GA.gen(minus), sq)
    ch, sh = (x + 1 / x) / 2, (x - 1 / x) / 2
    return GA.add(GA.sc(ch), GA.scal(sh, sig)), GA.sub(GA.sc(ch), GA.scal(sh, sig)), sig


def ladders(plus, minus):
    f = GA.scal(F(1, 2), GA.add(GA.gen(plus), GA.gen(minus)))
    fs = GA.scal(F(1, 2), GA.sub(GA.gen(plus), GA.gen(minus)))
    return f, fs


def check_boost_flow_scales_ladders_exponentially():
    premise("scrambling.imported-modes-modular-inventory")
    premise("scrambling.clock-inventory-boundary-modes")
    f, fs = ladders(0, 1)
    for x in XS:
        R, Rinv, sig = rotor(x, 0, 1, SQ11)
        assert GA.eq(GA.mul(sig, sig, SQ11), GA.sc(1))
        assert GA.eq(GA.mul(R, Rinv, SQ11), GA.sc(1))
        assert GA.eq(GA.mul(GA.mul(R, f, SQ11), Rinv, SQ11), GA.scal(1 / (x * x), f))
        assert GA.eq(GA.mul(GA.mul(R, fs, SQ11), Rinv, SQ11), GA.scal(x * x, fs))
        for y in XS:
            Ry = rotor(y, 0, 1, SQ11)[0]
            assert GA.eq(GA.mul(R, Ry, SQ11), rotor(x * y, 0, 1, SQ11)[0])
    # two modes in Cl(2,2): e+_1 = e0, e+_2 = e1, e-_1 = e2, e-_2 = e3; the common boost
    for x in XS[:2]:
        R1, R1i, _ = rotor(x, 0, 2, SQ22)
        R2, R2i, _ = rotor(x, 1, 3, SQ22)
        R, Ri = GA.mul(R1, R2, SQ22), GA.mul(R2i, R1i, SQ22)
        assert GA.eq(GA.mul(R, Ri, SQ22), GA.sc(1))
        for (p, m) in ((0, 2), (1, 3)):
            g, gs = ladders(p, m)
            assert GA.eq(GA.mul(GA.mul(R, g, SQ22), Ri, SQ22), GA.scal(1 / (x * x), g))
            assert GA.eq(GA.mul(GA.mul(R, gs, SQ22), Ri, SQ22), GA.scal(x * x, gs))


iroot = series.isqrt


def check_spreading_threshold_is_log_n():
    premise("scrambling.area-law-test")
    f, fs = ladders(0, 1)
    for N in NS:
        x = F(iroot(N))
        assert x * x == N
        R, Rinv, _ = rotor(x, 0, 1, SQ11)
        grown = GA.mul(GA.mul(R, GA.scal(F(1, N), fs), SQ11), Rinv, SQ11)
        assert GA.eq(grown, fs)                              # amplitude 1/N grown to 1
        Rb, Rbinv, _ = rotor(x - 1, 0, 1, SQ11)
        early = GA.mul(GA.mul(Rb, GA.scal(F(1, N), fs), SQ11), Rbinv, SQ11)
        coef = early[(0,)] * 2
        assert 0 < coef < 1
    for M in MASSES:
        kappa_inv = 4 * M
        for N in NS:
            t_star = LogVec.ln_int(N) * kappa_inv          # kappa t_* = ln N
            assert t_star * (1 / kappa_inv) == LogVec.ln_int(N)
            assert t_star == LogVec.ln_int(iroot(N)) * (8 * M)


def check_rate_is_modular_rate():
    premise("scrambling.mode-count")
    r = GA.RF.var()
    for M in MASSES:
        f = GA.RF1 - GA.RF.const(2 * M) / r
        kappa = f.deriv().eval(2 * M) / 2
        assert kappa == 1 / (4 * M)
        beta_over_pi = 2 / kappa                              # beta = 2 pi / kappa
        assert beta_over_pi == 8 * M
        assert beta_over_pi / 2 == 1 / kappa == 4 * M
        T_times_pi = 1 / beta_over_pi                         # pi T = 1/(beta/pi)
        assert kappa == 2 * T_times_pi
