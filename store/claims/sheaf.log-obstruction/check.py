"""sheaf.log-obstruction: exact checks.

The two formulas are checked without assuming them, from tau^{e(x)} = tau^{e0} exp((e(x) - e0) log tau), the
exponential written out as a truncated power series in x with coefficients polynomial in L = log tau, using only
the constant-exponent rules tau d/dtau tau^{e0} = e0 tau^{e0}, tau d/dtau L = 1, d/dx L = 0:
(1) d/dx tau^{e(x)} = e'(x) L tau^{e(x)} and tau d/dtau tau^{e(x)} = e(x) tau^{e(x)}, coefficient by coefficient
to x-order 7, for three exponent polynomials (linear, quadratic, constant);
(2) the algebra: tau^{e} tau^{f} = tau^{e+f} (exp addition law in the series), so products of monomials are
monomials and the algebra is commutative; tau d/dtau keeps it log-free; d/dx keeps it log-free exactly when
e' = 0 (constant exponent: no log terms at all; nonconstant: the L-coefficient at x = 0 is e'(0));
(3) the algebraic core of the non-membership: tau^{e0} L is a rank-two generalised eigenvector of tau d/dtau
((tau d/dtau - e0) kills it only on the second application), whereas any finite combination of pure powers with
constant coefficients is killed by prod_j (tau d/dtau - c_j); so it is not such a combination.
Not checked: the non-membership with smooth coefficient functions g_j(tau), whose proof is analytic (log tau is
unbounded at tau = 0).
"""
from fractions import Fraction as F
import GA

N = 7          # x-order of the truncation
# exponent polynomials e(x) = e0 + e1 x + e2 x^2 (generic samples)
EXPONENTS = [(F(2, 3), F(1), F(0)), (F(1), F(-1, 2), F(3)), (F(5, 4), F(0), F(0))]


def clean(d):
    return {k: v for k, v in d.items() if v != 0}


def trunc(d, n):
    return clean({k: v for k, v in d.items() if k[0] <= n})


def smul(a, b, n):
    out = {}
    for (i, j), c in a.items():
        for (k, m), d in b.items():
            if i + k <= n:
                out[(i + k, j + m)] = out.get((i + k, j + m), F(0)) + c * d
    return clean(out)


def sadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)


def sscal(c, a):
    return clean({k: c * v for k, v in a.items()})


def series_power(e1, e2, n):
    """tau^{e(x)} / tau^{e0} = exp((e1 x + e2 x^2) L), keys (x-degree, L-degree)."""
    f = clean({(1, 1): e1, (2, 1): e2})
    out = {(0, 0): F(1)}
    term = {(0, 0): F(1)}
    for k in range(1, n + 1):
        term = sscal(F(1, k), smul(term, f, n))
        out = sadd(out, term)
    return out


def d_x(a):
    out = {}
    for (i, j), c in a.items():
        if i > 0:
            out[(i - 1, j)] = out.get((i - 1, j), F(0)) + i * c
    return clean(out)


def tau_d_tau(a, e0):
    out = {}
    for (i, j), c in a.items():
        out[(i, j)] = out.get((i, j), F(0)) + e0 * c
        if j > 0:
            out[(i, j - 1)] = out.get((i, j - 1), F(0)) + j * c
    return clean(out)


def check_chain_rule_formulas():
    ok = True
    for (e0, e1, e2) in EXPONENTS:
        S = series_power(e1, e2, N)
        # e'(x) L and e(x), derived by hand from e = e0 + e1 x + e2 x^2
        eprime_L = clean({(0, 1): e1, (1, 1): 2 * e2})
        e_of_x = clean({(0, 0): e0, (1, 0): e1, (2, 0): e2})
        ok = ok and trunc(d_x(S), N - 1) == trunc(smul(eprime_L, S, N), N - 1)
        ok = ok and tau_d_tau(S, e0) == smul(e_of_x, S, N)
        # the L-coefficient of d/dx tau^e at x = 0 is e'(0) = e1
        ok = ok and d_x(S).get((0, 1), F(0)) == e1
    GA.check("d/dx tau^{e(x)} = e'(x) log(tau) tau^{e(x)} and tau d/dtau tau^{e(x)} = e(x) tau^{e(x)}", ok)
    return ok


MOVING_E1 = F(3, 2)          # a nonconstant linear exponent e = e0 + (3/2) x


def check_algebra_and_stability():
    ok = True
    (a0, a1, a2), (b0, b1, b2) = EXPONENTS[0], EXPONENTS[1]
    Sa = series_power(a1, a2, N)
    Sb = series_power(b1, b2, N)
    Sab = series_power(a1 + b1, a2 + b2, N)
    # tau^e tau^f = tau^{e+f}: the prefactors multiply to tau^{e0+f0}, the series by the addition law
    ok = ok and smul(Sa, Sb, N) == Sab and smul(Sb, Sa, N) == Sab
    # the x^1 L^1 coefficient of tau^e tau^f is e1 + f1, the x^2 L^2 coefficient (e1 + f1)^2 / 2
    ok = ok and Sab[(1, 1)] == a1 + b1 and Sab[(2, 2)] == (a1 + b1) ** 2 / 2
    # tau d/dtau keeps monomials log-free: on f(x) tau^{e(x)} with no log factor beyond the exponential's,
    # the result is e(x) f(x) tau^{e(x)}; its x^0 L^0 coefficient is e0
    for (e0, e1, e2) in EXPONENTS:
        ok = ok and tau_d_tau(series_power(e1, e2, N), e0)[(0, 0)] == e0
    # tangential stability exactly for constant exponents
    const = series_power(F(0), F(0), N)
    ok = ok and const == {(0, 0): F(1)} and d_x(const) == {}
    moving = series_power(MOVING_E1, F(0), N)
    ok = ok and d_x(moving)[(0, 1)] == MOVING_E1 and d_x(moving)[(1, 2)] == MOVING_E1 ** 2
    GA.check("the algebra is commutative and closed, tau d/dtau-stable, tangentially stable iff e' = 0", ok)
    return ok


# sample exponent e0 of the log term tau^{e0} log(tau)
E0_SAMPLE = F(2, 3)
# sample pure-power sum sum_j a_j tau^{c_j}, as {c_j: a_j}
PURE_POWER_COMBO = {F(2, 3): F(5), F(1, 3): F(-2), F(7, 4): F(1)}


def check_log_is_a_jordan_block():
    ok = True
    e0 = E0_SAMPLE
    logterm = {(0, 1): F(1)}                       # tau^{e0} L
    once = sadd(tau_d_tau(logterm, e0), sscal(-e0, logterm))
    twice = sadd(tau_d_tau(once, e0), sscal(-e0, once))
    ok = ok and once == {(0, 0): F(1)} and twice == {}
    # a combination of pure powers tau^{c_j} (constant coefficients) is killed by prod (tau d/dtau - c_j):
    # represent sum a_j tau^{c_j} as {c_j: a_j}; tau d/dtau multiplies the coefficient of tau^c by c
    combo = PURE_POWER_COMBO
    vec = dict(combo)
    for c in combo:
        vec = clean({cc: (cc - c) * a for cc, a in vec.items()})
    ok = ok and vec == {}
    # while a single factor (tau d/dtau - e0) does not kill tau^{e0} L (it leaves tau^{e0})
    ok = ok and once != {}
    GA.check("tau^{e0} log(tau) is a rank-two Jordan vector of tau d/dtau; finite pure-power sums are not", ok)
    return ok
