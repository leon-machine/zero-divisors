"""singularity.causal-epoch-computed-exactly: exact checks of the causal-epoch integral.

All identities are exact: rational functions in u (GA.RF), logarithms as exact formal combinations of
ln p (LogVecs) bounded by rigorous rational intervals, Riemann sums in rational arithmetic.
(1) With r = 2M u^2: the rain worldline (unit energy) has |dt/dr| = 1/(|f| sqrt(1 - f)) = sqrt(r/2M) r/(2M - r)
    (sqrt(1 - f) = sqrt(2M/r) = 1/u inside the horizon), and the integrand in u is 4M u^4/(1 - u^2);
    u^4/(1 - u^2) = -u^2 - 1 + 1/(1 - u^2); (-u^3/3 - u)' = -u^2 - 1 and ((1/2) ln((1+u)/(1-u)))' =
    1/(1 - u^2); with eps = 1 - u^2, (1+u)/(1-u) = (1+u)^2/eps, so the closed form is
    2M ln(1/eps) + 4M (ln(1+u) - u - u^3/3).
(2) The closed form 4M[(1/2) ln((1+u0)/(1-u0)) - u0 - u0^3/3] lies inside the exact lower and upper
    Riemann sums (240 subintervals) of the increasing integrand at u0 = 3/5, 4/5, 9/10; the former closed
    form 2M(ln(1/eps) - 1 + eps) lies outside the bracket at u0 = 9/10.
(3) The expansion: 2M eps <= Delta t - 2M(ln(1/eps) - 8/3 + 2 ln 2) <= 4M eps at u = 9/10, 99/100,
    999/1000, so the remainder is O(eps) with positive sign; the coefficient of ln(1/eps) is the residue
    2M of 1/|f| = r/(2M - r) at r = 2M, and for any energy E > 0 the extra factor E/sqrt(E^2 + |f|) is 1 at
    the horizon, so the coefficient does not depend on E.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401 (the claim has no premises)

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
_DEN = 1 << 160


def _atanh_bounds(z, K=30):
    """Rational bounds on atanh z for 0 <= z <= 1/3."""
    zz = z * z
    term, part = z, F(0)
    for k in range(K):
        part += term / (2 * k + 1)
        term *= zz
    tail = term / ((2 * K + 1) * (1 - zz))
    return part, part + tail


def _out(lo, hi):
    return F((lo.numerator * _DEN) // lo.denominator, _DEN), \
        F(-((-hi.numerator * _DEN) // hi.denominator), _DEN)


def ln_bounds(n):
    """Rational (lower, upper) bounds on ln n, n a positive integer."""
    if n in _LNB:
        return _LNB[n]
    if n == 1:
        return F(0), F(0)
    l2lo, l2hi = _atanh_bounds(F(1, 3))
    l2lo, l2hi = 2 * l2lo, 2 * l2hi
    a = n.bit_length() - 1
    x = F(n, 1 << a)
    zlo, zhi = _atanh_bounds((x - 1) / (x + 1))
    res = _out(a * l2lo + 2 * zlo, a * l2hi + 2 * zhi)
    _LNB[n] = res
    return res


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

MASS = F(3, 2)
U_BRACKET = [F(3, 5), F(4, 5), F(9, 10)]
U_EXPAND = [F(9, 10), F(99, 100), F(999, 1000)]
ENERGIES = [F(1), F(2), F(3, 7)]


def check_integrand_partial_fractions_antiderivative():
    u = GA.RF.var()
    one = GA.RF1
    M4 = GA.RF.const(4 * MASS)
    r = GA.RF.const(2 * MASS) * u * u
    f = one - GA.RF.const(2 * MASS) / r
    absf = GA.RF.const(0) - f
    sqrt_one_minus_f = one / u                       # (1/u)^2 = 2M/r = 1 - f
    assert (sqrt_one_minus_f * sqrt_one_minus_f).eqrf(one - f)
    drdu = r.deriv()
    integrand = (one / (absf * sqrt_one_minus_f)) * drdu
    assert integrand.eqrf(M4 * u * u * u * u / (one - u * u))
    stated = u * (r / (GA.RF.const(2 * MASS) - r)) * drdu       # sqrt(r/2M) = u
    assert stated.eqrf(integrand)
    pf = GA.RF.const(0) - u * u - one + one / (one - u * u)
    assert (u * u * u * u / (one - u * u)).eqrf(pf)
    poly = GA.RF.const(0) - u * u * u / GA.RF.const(3) - u
    assert poly.deriv().eqrf(GA.RF.const(0) - u * u - one)
    logd = GA.RF.const(F(1, 2)) * (one / (one + u) + one / (one - u))
    assert logd.eqrf(one / (one - u * u))
    eps = one - u * u
    assert ((one + u) / (one - u)).eqrf((one + u) * (one + u) / eps)


def closed_form(u0):
    """(log part, rational part) of 4M[(1/2) ln((1+u0)/(1-u0)) - u0 - u0^3/3]."""
    return LogVec.ln_rat((1 + u0) / (1 - u0)) * (2 * MASS), 4 * MASS * (-u0 - u0 ** 3 / 3)


def bracket(u0, n=240):
    """Exact lower and upper Riemann sums of the increasing integrand 4M x^4/(1 - x^2) on [0, u0]."""
    h = u0 / n
    vals = [4 * MASS * (h * i) ** 4 / (1 - (h * i) ** 2) for i in range(n + 1)]
    return sum(vals[:-1]) * h, sum(vals[1:]) * h


def check_closed_form_inside_riemann_bracket():
    for u0 in U_BRACKET:
        lower, upper = bracket(u0)
        L = LogVec.ln_rat((1 + u0) / (1 - u0)) * (2 * MASS)
        rat = 4 * MASS * (-u0 - u0 ** 3 / 3)
        lo, hi = logvec_bounds(L)
        assert lower < lo + rat and hi + rat < upper
    u0 = U_BRACKET[-1]
    eps = 1 - u0 * u0
    lower, upper = bracket(u0)
    olo, ohi = logvec_bounds(LogVec.ln_rat(1 / eps) * (2 * MASS))
    old_rat = 2 * MASS * (eps - 1)
    assert olo + old_rat > upper or ohi + old_rat < lower


def check_expansion_remainder_and_energy_independence():
    for u0 in U_EXPAND:
        eps = 1 - u0 * u0
        L, rat = closed_form(u0)
        expansion = LogVec.ln_rat(1 / eps) * (2 * MASS) + LogVec.ln_int(2) * (4 * MASS)
        lo, hi = logvec_bounds(L - expansion)
        offset = rat + 2 * MASS * F(8, 3)              # closed form minus expansion, rational part
        lo, hi = lo + offset, hi + offset
        assert 2 * MASS * eps <= lo and hi <= 4 * MASS * eps
    r = GA.RF.var()
    twoM = GA.RF.const(2 * MASS)
    absf = twoM / r - GA.RF1
    residue = ((twoM - r) / absf)
    assert residue.eqrf(r) and residue.eval(2 * MASS) == 2 * MASS
    for E in ENERGIES:
        factor_sq = E * E / (E * E + absf.eval(2 * MASS))
        assert absf.eval(2 * MASS) == 0 and factor_sq == 1
