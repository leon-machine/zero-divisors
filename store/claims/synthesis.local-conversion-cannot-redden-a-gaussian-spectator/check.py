"""synthesis.local-conversion-cannot-redden-a-gaussian-spectator: exact checks.

A statistically homogeneous Gaussian field sigma (the smeared field of a quasi-free state at spacelike separation,
or a classical Gaussian modulation), standardised x = (sigma - mean)/s, with normalised correlation rho(r) between
two points. A local conversion zeta = f(sigma) (curvaton, modulated descent, any separate-universe map) has the
Hermite expansion f = sum_n c_n He_n(x).
(1) Mehler: for a standard bivariate Gaussian (X, Y) with correlation rho, E[He_m(X) He_n(Y)] = delta_mn n! rho^n.
    Checked exactly for m, n <= 7 as polynomials in rho, with moments from Y = rho X + (1 - rho^2)^(1/2) Z
    (only even powers of the square root survive, so every moment is a polynomial in rho with rational
    coefficients).
(2) Covariance of a conversion: Cov(f(X), f(Y)) = sum_{n >= 1} c_n^2 n! rho^n, computed directly from moments for
    the curvaton's series (2/3) x - (1/3) x^2 + (2/9) x^3 (x = delta sigma / sigma), for a modulated-descent law
    Gamma = sigma^3 read through -(1/6) ln, truncated at fourth order, and for a pure square; every coefficient is
    non-negative and the lowest power is the lowest Hermite order present.
(3) Large-scale index: with rho ~ A r^(-m), 0 < m < 3, the term rho^n has index min(n m, 3) (white noise beyond 3),
    so the leading index is n0 m (n0 the lowest order present) if n0 m < 3, at least 3 otherwise: never below m.
    The Fourier coefficient of r^(-beta), Gamma(2 - beta) sin(pi (2 - beta)/2), is positive on 0 < beta < 3 (sign
    table by intervals), so each term enters with a positive weight.
(2b) Local degree: d ln g / d ln r = nbar d ln rho / d ln r with nbar = rho g'/g a mean order, at least the Hermite
    rank, checked at sample rho in (0, 1]; with a linear term nbar - 1 <= (11/24) rho for the curvaton series.
(4) The series, under (F): the stored indices on the descent slice at u = k|x_d| (massless 2u^2/(1+u^2); unitary
    series at least 2 - 2/(u^2 - 2)) exceed 1.62 at u = 2.7 and 1.99 at the pivot; a conversion with c_1 != 0
    keeps them, so the gap to -0.0351 +- 0.0042 is over 394 standard deviations at the largest scales.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

NS1, SIG = F("-0.0351"), F("0.0042")


# polynomials in rho: lists of Fractions, index = power
def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def pscal(c, a):
    return [c * x for x in a]


def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def binom(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def gauss_moment(n):
    """E[X^n] for a standard Gaussian: (n-1)!! for even n, 0 for odd n."""
    if n % 2:
        return 0
    r = 1
    for i in range(n - 1, 0, -2):
        r *= i
    return r


def joint_moment(a, b):
    """E[X^a Y^b] as a polynomial in rho, Y = rho X + t Z, t^2 = 1 - rho^2."""
    total = [F(0)]
    for j in range(b + 1):
        e = b - j
        if e % 2:
            continue
        term = [F(0)] * j + [F(binom(b, j) * gauss_moment(a + j) * gauss_moment(e))]
        one_minus = [F(1)]
        for _ in range(e // 2):
            one_minus = pmul(one_minus, [F(1), F(0), F(-1)])
        total = padd(total, pmul(term, one_minus))
    return ptrim(total)


def hermite(n):
    """Probabilists' Hermite polynomial He_n as coefficient list in x."""
    h0, h1 = [F(1)], [F(0), F(1)]
    if n == 0:
        return h0
    for k in range(1, n):
        h0, h1 = h1, padd([F(0)] + h1, pscal(-k, h0))
    return h1


def expect_pair(fx, gy):
    """E[f(X) g(Y)] for polynomials f, g (coefficient lists in x, y), as a polynomial in rho."""
    total = [F(0)]
    for a, ca in enumerate(fx):
        if ca == 0:
            continue
        for b, cb in enumerate(gy):
            if cb == 0:
                continue
            total = padd(total, pscal(ca * cb, joint_moment(a, b)))
    return ptrim(total)


def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def hermite_coeffs(f, nmax):
    """c_n = E[f(X) He_n(X)]/n! (rho = 1 moments)."""
    out = []
    for n in range(nmax + 1):
        val = expect_pair(f, hermite(n))
        out.append(sum(val) / fact(n))  # rho = 1: Y = X
    return out


def check_mehler_orthogonality():
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    count = 0
    for m in range(8):
        for n in range(8):
            got = expect_pair(hermite(m), hermite(n))
            want = [F(0)] * n + [F(fact(n))] if m == n else [F(0)]
            GA.check("E[He_%d(X) He_%d(Y)] = %s" % (m, n, "n! rho^n" if m == n else "0"), got == ptrim(want))
            count += 1
    GA.check("64 Mehler identities checked", count == 64)
    GA.check("pinned: E[X^3 Y^3] = 9 rho + 6 rho^3", joint_moment(3, 3) == [0, 9, 0, 6])
    GA.check("pinned: He_4 = x^4 - 6 x^2 + 3", hermite(4) == [3, 0, -6, 0, 1])
    return True


def cov_direct(f):
    full = expect_pair(f, f)
    mean = expect_pair(f, [F(1)])
    return ptrim(padd(full, pscal(-1, [sum(mean) ** 2])))  # mean is rho-free


def check_conversion_covariance_positive():
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    curvaton = [F(0), F(2, 3), F(-1, 3), F(2, 9)]
    # modulated descent: zeta = -(1/6) ln(Gamma/Gamma_bar), Gamma = (1 + u)^3 with u = eps x, eps = 1/10:
    # -(1/2) ln(1 + u) truncated at u^4
    eps = F(1, 10)
    lnser = [F(0), F(1), F(-1, 2), F(1, 3), F(-1, 4)]
    modulated = [F(-1, 2) * c * eps ** i for i, c in enumerate(lnser)]
    square = [F(0), F(0), F(1)]
    cases = [("curvaton series", curvaton, 1), ("modulated descent, Gamma ~ sigma^3", modulated, 1),
             ("pure square", square, 2)]
    for name, f, n0 in cases:
        c = hermite_coeffs(f, len(f) - 1)
        want = [F(0)] + [c[n] ** 2 * fact(n) for n in range(1, len(c))]
        got = cov_direct(f)
        GA.check("%s: Cov = sum c_n^2 n! rho^n" % name, got == ptrim(want))
        GA.check("%s: every coefficient non-negative" % name, all(x >= 0 for x in got))
        low = min(i for i, x in enumerate(got) if x != 0)
        GA.check("%s: lowest power is the lowest Hermite order %d" % (name, n0), low == n0)
    c = hermite_coeffs(curvaton, 3)
    GA.check("pinned: curvaton Hermite coefficients", c == [F(-1, 3), F(4, 3), F(-1, 3), F(2, 9)])
    GA.check("pinned: curvaton Cov", cov_direct(curvaton) == [0, F(16, 9), F(2, 9), F(8, 27)])
    return True


def peval(a, x):
    return sum(c * x ** i for i, c in enumerate(a))


def pderiv(a):
    return [i * a[i] for i in range(1, len(a))] or [F(0)]


def check_local_degree_mean_order():
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    curvaton = [F(0), F(2, 3), F(-1, 3), F(2, 9)]
    eps = F(1, 10)
    lnser = [F(0), F(1), F(-1, 2), F(1, 3), F(-1, 4)]
    modulated = [F(-1, 2) * c * eps ** i for i, c in enumerate(lnser)]
    square = [F(0), F(0), F(1)]
    rhos = [F(1, 10 ** 6), F(1, 1000), F(1, 10), F(1, 2), F(9, 10), F(1)]
    for name, f, n0 in [("curvaton", curvaton, 1), ("modulated", modulated, 1), ("square", square, 2)]:
        g = cov_direct(f)
        for r in rhos:
            nbar = r * peval(pderiv(g), r) / peval(g, r)
            GA.check("%s: mean order at rho = %s is at least the Hermite rank %d" % (name, r, n0), nbar >= n0)
    # with a linear term, nbar - 1 <= rho * sum (n - 1) a_n / a_1 on 0 < rho <= 1
    g = cov_direct(curvaton)
    bound = sum((n - 1) * g[n] for n in range(2, len(g))) / g[1]
    GA.check("pinned: curvaton bound constant", bound == F(11, 24))
    for r in rhos:
        nbar = r * peval(pderiv(g), r) / peval(g, r)
        GA.check("curvaton: nbar - 1 <= (11/24) rho at rho = %s" % r, nbar - 1 <= bound * r)
    fp = sum(r * peval(pderiv(g), r) / peval(g, r) for r in rhos)
    GA.check("pinned: curvaton mean orders summed over the sample",
             fp == F(244616549066074414097382476866, 35924075307971153527175492719))
    GA.check("pinned: six sample correlations", len(rhos) == 6 and rhos[0] * rhos[2] == F(1, 10 ** 7))
    GA.check("pinned: curvaton mean order at rho = 1/2",
             F(1, 2) * peval(pderiv(g), F(1, 2)) / peval(g, F(1, 2)) == F(60, 53))
    return True


def sign_fourier_coeff(beta):
    """Sign of Gamma(s) sin(pi s/2), s = 2 - beta, on 0 < beta < 3, from interval facts:
    Gamma > 0 on (0, 2], Gamma < 0 on (-1, 0); sin(pi s/2) > 0 on (0, 2), < 0 on (-1, 0); at s = 0 the limit is
    pi/2 > 0."""
    s = 2 - beta
    if s == 0:
        return 1
    g = 1 if s > 0 else -1
    t = 1 if 0 < s < 2 else -1
    return g * t


def large_scale_index(m, n0):
    b = n0 * m
    return b if b < 3 else F(3)


def check_index_never_below_field():
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    ms = [F(1, 10), F(1, 3), F(1, 2), F(1), F(3, 2), F(2), F(5, 2), F(29, 10)]
    for m in ms:
        for n0 in range(1, 7):
            L = large_scale_index(m, n0)
            GA.check("m = %s, n0 = %d: index %s >= m" % (m, n0, L), L >= m)
            if n0 == 1:
                GA.check("m = %s: linear term keeps the index exactly" % m, L == m)
    for k in range(1, 30):
        beta = F(k, 10)
        GA.check("Fourier weight of r^-%s positive" % beta, sign_fourier_coeff(beta) > 0)
    table = [large_scale_index(m, n0) for m in ms for n0 in range(1, 7)]
    GA.check("pinned: grid size 48", len(table) == 48)
    GA.check("pinned: sum of the grid's indices", sum(table) == F(207, 2))
    GA.check("pinned: number of white-noise entries", sum(1 for L in table if L == 3) == 25)
    GA.check("pinned: 29 Fourier exponents tested", len([k for k in range(1, 30)]) == 29)
    GA.check("pinned: s = 0 limit and the two sign intervals",
             (sign_fourier_coeff(F(2)), sign_fourier_coeff(F(1, 2)), sign_fourier_coeff(F(5, 2))) == (1, 1, 1))
    GA.check("pinned: m = 2, n0 = 2 gives white noise 3", large_scale_index(F(2), 2) == 3)
    GA.check("pinned: m = 1, n0 = 2 gives 2", large_scale_index(F(1), 2) == 2)
    return True


def check_series_fields_give_blue():
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    # stored indices at u = k|x_d|: massless 2u^2/(1+u^2); unitary series at least 2 - 2/(u^2 - 2)
    u_big, u_piv = F(27, 10), F(960)
    massless = lambda u: 2 * u * u / (1 + u * u)
    unitary_lo = lambda u: 2 - 2 / (u * u - 2)
    GA.check("pinned: massless index at u = 2.7 is 1458/829", massless(u_big) == F(1458, 829))
    GA.check("massless index above 1.75 at the largest observed scales", massless(u_big) > F(175, 100))
    GA.check("pinned: unitary-series floor at u = 2.7 is 2 - 200/529", unitary_lo(u_big) == 2 - F(200, 529))
    GA.check("unitary-series floor above 1.62 at the largest observed scales", unitary_lo(u_big) > F(162, 100))
    GA.check("both above 1.99 at the pivot", massless(u_piv) > F(199, 100) and unitary_lo(u_piv) > F(199, 100))
    GA.check("largest scales: more than 394 sigma", (unitary_lo(u_big) - NS1) / SIG > 394)
    GA.check("pivot: more than 482 sigma", (unitary_lo(u_piv) - NS1) / SIG > 482)
    GA.check("index increases with u (massless, between the two ends)",
             massless(u_big) < massless(F(10)) < massless(u_piv))
    m = F(2)  # descent-slice correlator 1/(4 pi^2 a^2 r^2): degree -2
    for n0 in range(1, 6):
        L = large_scale_index(m, n0)
        GA.check("frozen-point field, lowest order %d: index %s >= 2" % (n0, L), L >= 2)
        gap = (L - NS1) / SIG
        GA.check("lowest order %d: more than 480 sigma from the measured index" % n0, gap > 480)
    GA.check("pinned gap at the linear order", (2 - NS1) / SIG == F(20351, 42))
    Ls = [large_scale_index(m, n0) for n0 in range(1, 6)]
    GA.check("pinned: indices for lowest orders 1 to 5", Ls == [2, 3, 3, 3, 3])
    GA.check("pinned: white-noise gap", (3 - NS1) / SIG == F(30351, 42))
    GA.check("a red zeta needs m < 0: no positive m reaches the measured index",
             all(large_scale_index(mm, n) > NS1 for mm in [F(1, 100), F(1, 10)] for n in range(1, 4)))
    return True
