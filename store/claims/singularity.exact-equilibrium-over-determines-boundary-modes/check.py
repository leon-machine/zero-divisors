"""singularity.exact-equilibrium-over-determines-boundary-modes: exact checks.

Entropies are computed exactly: for rational p, log p = sum_primes e_p log(prime), and the logs of primes are
linearly independent over Q, so S(rho) = -sum p log p is an exact vector of rational coefficients on the
primes, and equal entropies are equal vectors.
(1) The exact geometric modular state rho = e^{-beta K_geo}/Z, built from the spectrum of
    K_geo = sum_k omega_k N_k (three modes, weights (1, 2, 3) at y = e^{-beta} = 2/3, and (1, 1/2, 2) at
    y = 4/9 so that y^(1/2) = 2/3), equals the product of the single-mode Gibbs states e^{-beta omega_k N_k}/Z_k
    entrywise.
(2) For these states: the total correlation C(rho) = sum_k S(rho_k) - S(rho) is exactly 0; rho is a fixed
    point of the number-basis pinching E_N, so the deficit D(rho || E_N rho) = S(E_N rho) - S(rho) is exactly 0
    (the premise's identity), and D = C(rho) - C(E_N rho) holds with both sides 0.
(3) The deviation carries the correlations: the pure even state c|00> + s|11> (c = 3/5, s = 4/5) has the same
    Gibbs marginals as the product state at x = s^2/c^2 = 16/9 but is not that product; its total correlation
    is 2 S(m) != 0, its deficit is S(E_N rho) = S(m) != 0, and D = C(rho) - C(E_N rho) exactly.
"""
import GA
from fractions import Fraction as F
from itertools import product

from tp_premise import premise


def factor(n):
    out, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def logvec(p):
    """log p for rational p > 0 as {prime: integer exponent}."""
    v = {}
    for pr, e in factor(p.numerator).items():
        v[pr] = v.get(pr, 0) + e
    for pr, e in factor(p.denominator).items():
        v[pr] = v.get(pr, 0) - e
    return v


def entropy(probs):
    out = {}
    for p in probs:
        if p == 0:
            continue
        for pr, e in logvec(p).items():
            out[pr] = out.get(pr, F(0)) - p * e
    return {k: c for k, c in out.items() if c != 0}


def vadd(*terms):
    out = {}
    for sgn, v in terms:
        for k, c in v.items():
            out[k] = out.get(k, F(0)) + sgn * c
    return {k: c for k, c in out.items() if c != 0}


SPECS = [((1, 2, 3), F(2, 3), {1: F(2, 3), 2: F(4, 9), 3: F(8, 27)}),
         ((1, F(1, 2), 2), F(4, 9), {1: F(4, 9), F(1, 2): F(2, 3), 2: F(16, 81)})]


def geo_state(weights, ypow):
    states = list(product((0, 1), repeat=len(weights)))
    wts = []
    for s in states:
        w = F(1)
        for om, n in zip(weights, s):
            if n:
                w *= ypow[om]
        wts.append(w)
    Z = sum(wts)
    return states, [w / Z for w in wts]


def check_geometric_state_is_product():
    premise("singularity.kms-uniqueness-factor")
    ok = True
    for weights, y, ypow in SPECS:
        states, p = geo_state(weights, ypow)
        for om in weights:
            fo = F(om)
            ok = ok and ypow[om] ** fo.denominator == y ** fo.numerator      # ypow[om] = y^om
        for s, ps in zip(states, p):
            prod_ = F(1)
            for om, n in zip(weights, s):
                x = ypow[om]
                prod_ *= (x if n else 1) / (1 + x)
            ok = ok and ps == prod_
    _tp_rv = (ok); assert _tp_rv is not False, "check_geometric_state_is_product"; return _tp_rv


def marg(states, p, k):
    p1 = sum(ps for s, ps in zip(states, p) if s[k])
    return [1 - p1, p1]


def check_zero_correlation_and_zero_deficit():
    premise("singularity.deficit-theorem-cost-descent-exactly")
    premise("singularity.deficit-carried-quanta-correlations")
    ok = True
    for weights, y, ypow in SPECS:
        states, p = geo_state(weights, ypow)
        S = entropy(p)
        Sk = [entropy(marg(states, p, k)) for k in range(len(weights))]
        C = vadd(*[(1, v) for v in Sk], (-1, S))
        ok = ok and C == {} and S != {}
        # the state is diagonal in the joint number basis: E_N rho = rho, so S(E_N rho) = S(rho)
        D = vadd((1, entropy(p)), (-1, S))
        CE = vadd(*[(1, v) for v in Sk], (-1, entropy(p)))
        ok = ok and D == {} and D == vadd((1, C), (-1, CE))
    _tp_rv = (ok); assert _tp_rv is not False, "check_zero_correlation_and_zero_deficit"; return _tp_rv


def check_correlated_state_carries_the_deficit():
    premise("singularity.deficit-theorem-cost-descent-exactly")
    premise("singularity.deficit-carried-quanta-correlations")
    c, s = F(3, 5), F(4, 5)
    # rho = |psi><psi|, psi = c|00> + s|11>: pure, S(rho) = 0; marginals diag(c^2, s^2) each
    m = [c * c, s * s]
    x = m[1] / m[0]
    ok = x == F(16, 9) and m == [1 / (1 + x), x / (1 + x)]
    S_rho = {}
    Sm = entropy(m)
    EN = [c * c, F(0), F(0), s * s]                    # pinching keeps the diagonal of |psi><psi|
    S_EN = entropy(EN)
    prod_state = [m[0] * m[0], m[0] * m[1], m[1] * m[0], m[1] * m[1]]
    ok = ok and EN != prod_state
    C_rho = vadd((2, Sm), (-1, S_rho))
    C_EN = vadd((2, Sm), (-1, S_EN))
    D = vadd((1, S_EN), (-1, S_rho))
    ok = ok and C_rho == vadd((2, Sm)) and C_rho != {} and D == Sm and D != {}
    ok = ok and D == vadd((1, C_rho), (-1, C_EN))
    _tp_rv = (ok); assert _tp_rv is not False, "check_correlated_state_carries_the_deficit"; return _tp_rv
