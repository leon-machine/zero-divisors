"""sheaf.boundary-units-invert: exact checks of the algebraic core.

Elements of the variable-order algebra are modelled by finite exponent families without logarithms,
{exponent (Fraction): coefficient}, multiplied by adding exponents and truncated at a level N
(terms of exponent >= N dropped). Sample a = 3 tau^(1/2) - 2 tau^(3/4) + tau^(5/3) - 4 tau^(7/2), every
exponent >= delta = 1/2; level N = 4.
(1) Admissibility: every exponent of a^k is >= k delta (the minimum is exactly k/2 here), so only
k <= N/delta = 8 contribute below level N; (-a)^k truncated is empty for k = 9, 10, 11.
(2) The Neumann sum b = sum_(k <= 8) (-a)^k satisfies (1 + a) b = 1 modulo tau^N.
(3) General case: c = 2 + tau + 3 tau^2 (smooth, positive near E) and c + a are inverted modulo tau^N
by c^-1 (1 + a/c)^-1, with (c + a) times the result = 1 modulo tau^N.
(4) Convergence where |a| <= 1/2: at tau = 2^-12, 3^-12, 5^-12 (rational fractional powers), a(tau)
is evaluated exactly, |a| <= 1/2, and the partial sums S_K obey the geometric identity
S_K - 1/(1 + a) = -(-a)^(K+1)/(1 + a), so |S_K - 1/(1 + a)| <= 2 |a|^(K+1).
Local uniform convergence on a compact is analysis and is represented by the sampled bound only.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (self-contained lemma: no premises)

A = {F(1, 2): F(3), F(3, 4): F(-2), F(5, 3): F(1), F(7, 2): F(-4)}
LEVEL = F(4)
C_SMOOTH = {F(0): F(2), F(1): F(1), F(2): F(3)}


def mul(x, y, level=LEVEL):
    out = {}
    for e1, c1 in x.items():
        for e2, c2 in y.items():
            e = e1 + e2
            if e < level:
                out[e] = out.get(e, F(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def add(*xs):
    out = {}
    for x in xs:
        for e, c in x.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def scal(s, x):
    return {e: s * c for e, c in x.items()}


def power(x, k, level=LEVEL):
    out = {F(0): F(1)}
    for _ in range(k):
        out = mul(out, x, level)
    return out


def neumann(x, kmax, level=LEVEL):
    return add(*[power(scal(-1, x), k, level) for k in range(kmax + 1)])


def inverse_smooth(cc, level=LEVEL):
    """1/c for c = c_0 + c_1 tau + ... with c_0 > 0, as a truncated power series."""
    c0 = cc[F(0)]
    rest = scal(1 / c0, {e: v for e, v in cc.items() if e != 0})
    return scal(1 / c0, neumann(rest, int(level) + 1, level))


def check_admissible_neumann_inverse():
    ok = True
    delta = min(A)
    ok = ok and delta == F(1, 2)
    for k in range(1, 12):
        big = power(A, k, F(100))
        ok = ok and min(big) == k * delta
        if k * delta >= LEVEL:
            ok = ok and power(A, k) == {}
    b = neumann(A, 8)
    lhs = mul(add({F(0): F(1)}, A), b)
    ok = ok and lhs == {F(0): F(1)}
    # stopping at k = 6 leaves the remainder -(-a)^7, whose lowest exponent 7/2 lies below the level
    short = mul(add({F(0): F(1)}, A), neumann(A, 6))
    ok = ok and short != {F(0): F(1)} and min(e for e in short if e != 0) == F(7, 2)
    GA.check("units: a = O(tau^delta) gives an admissible Neumann series with (1 + a) b = 1 mod tau^N", ok)
    return ok


def check_smooth_positive_plus_small_is_invertible():
    ok = True
    ci = inverse_smooth(C_SMOOTH)
    ok = ok and mul(C_SMOOTH, ci) == {F(0): F(1)} and ci[F(0)] == F(1, 2)
    a_over_c = mul(A, ci)
    inv = mul(ci, neumann(a_over_c, 8))
    ok = ok and mul(add(C_SMOOTH, A), inv) == {F(0): F(1)}
    ok = ok and min(a_over_c) == F(1, 2)
    GA.check("units: c + a is invertible for c smooth positive and a of positive order", ok)
    return ok


TAUS_BASE = (2, 3, 5)


def evaluate(x, base):
    """x at tau = base^-12 (all exponents are multiples of 1/12)."""
    tot = F(0)
    for e, c in x.items():
        k = e * 12
        tot += c * F(1, base) ** int(k)
    return tot


def check_geometric_convergence_where_a_is_small():
    ok = True
    for base in TAUS_BASE:
        av = evaluate(A, base)
        ok = ok and abs(av) <= F(1, 2)
        exact = 1 / (1 + av)
        s = F(0)
        for K in range(11):
            s += (-av) ** K
            ok = ok and s - exact == -((-av) ** (K + 1)) / (1 + av)
            ok = ok and abs(s - exact) <= 2 * abs(av) ** (K + 1)
    # tau = 2^-12: a = 3/64 - 2/512 + 1/2^20 - 4/2^42
    ok = ok and evaluate(A, 2) == F(3, 64) - F(2, 512) + F(1, 2 ** 20) - F(4, 2 ** 42)
    GA.check("units: the Neumann partial sums converge geometrically where |a| <= 1/2", ok)
    return ok
