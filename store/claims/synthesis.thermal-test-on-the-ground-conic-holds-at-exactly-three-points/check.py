"""synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points: certified enclosures.

On the ground conic (delta - 1/2)^2 = (1 - r^2)/12 the thermal test is the vanishing of
    T(delta) = -r^2/24 + sum over a in {k + delta, k + 1 - delta : k >= 0} of a / (exp(2 pi a / r) + 1),
with r^2 = 1 - 12 (delta - 1/2)^2.  The checks enclose T, T' and T'' on intervals of delta with rational
endpoints.  Arithmetic: integers only.  An interval is a pair (lo, hi) of integers standing for
[lo / 2^128, hi / 2^128], every operation rounded outward; a jet is a triple of intervals enclosing a
function and its first two derivatives on an interval of delta.  Scalars only (grade 0).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

BITS = 128
P = 1 << BITS
KTERMS = 8          # the sum is taken over k < KTERMS, the rest bounded


def fl(n, d):
    return n // d


def ce(n, d):
    return -((-n) // d)


def iv(a, b=None):
    a = F(a)
    b = a if b is None else F(b)
    return (fl(a.numerator * P, a.denominator), ce(b.numerator * P, b.denominator))


def iadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def ineg(x):
    return (-x[1], -x[0])


def isub(x, y):
    return (x[0] - y[1], x[1] - y[0])


def imul(x, y):
    c = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return (fl(min(c), P), ce(max(c), P))


def irecip(x):
    if x[0] > 0:
        return (fl(P * P, x[1]), ce(P * P, x[0]))
    if x[1] < 0:
        return ineg(irecip(ineg(x)))
    raise ZeroDivisionError("interval contains zero")


def isqrt_int(n):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def isqrt(x):
    if x[0] <= 0:
        raise ValueError("square root of an interval reaching zero")
    lo = isqrt_int(x[0] * P)
    hi = isqrt_int(x[1] * P)
    if hi * hi < x[1] * P:
        hi += 1
    return (lo, hi)


def iexp(x):
    """exp of an interval.  At an end t: halve until |t| <= 1/2 (rounding the halves outward), sum the series to
    order 30 with interval terms (the remainder, below 2^-140, is covered by widening by one unit), square back."""
    def point(t, up):
        s = 0
        while abs(t) > P // 2:
            t = ce(t, 2) if up else fl(t, 2)
            s += 1
        term = (P, P)
        tot = (P, P)
        tt = (t, t)
        for k in range(1, 31):
            term = imul(term, tt)
            term = (fl(term[0], k), ce(term[1], k))
            tot = iadd(tot, term)
        tot = (tot[0] - 1, tot[1] + 1)
        for _ in range(s):
            tot = imul(tot, tot)
        return tot
    lo = point(x[0], False)[0]
    hi = point(x[1], True)[1]
    return (max(lo, 0), hi)


def pi_interval():
    """pi = 16 atan(1/5) - 4 atan(1/239); the partial sums of each alternating series bracket its value."""
    def bracket(n, terms):
        s = F(0)
        last = []
        for k in range(terms):
            s += F((-1) ** k, (2 * k + 1) * n ** (2 * k + 1))
            last.append(s)
        return (min(last[-2:]), max(last[-2:]))
    a5 = bracket(5, 60)
    a239 = bracket(239, 18)
    return iv(16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])


PI = pi_interval()
ZERO = (0, 0)


def jconst(c):
    return (iv(c), ZERO, ZERO)


def jvar(x):
    return (x, (P, P), ZERO)


def jadd(a, b):
    return tuple(iadd(u, v) for u, v in zip(a, b))


def jsub(a, b):
    return tuple(isub(u, v) for u, v in zip(a, b))


def jscale(c, a):
    c = iv(c)
    return tuple(imul(c, u) for u in a)


def jmul(a, b):
    two = iv(2)
    return (imul(a[0], b[0]),
            iadd(imul(a[1], b[0]), imul(a[0], b[1])),
            iadd(iadd(imul(a[2], b[0]), imul(two, imul(a[1], b[1]))), imul(a[0], b[2])))


def jrecip(g):
    h = irecip(g[0])
    h2 = imul(h, h)
    h3 = imul(h2, h)
    return (h, ineg(imul(g[1], h2)), iadd(ineg(imul(g[2], h2)), imul(iv(2), imul(imul(g[1], g[1]), h3))))


def jsqrt(g):
    s = isqrt(g[0])
    r = irecip(s)
    r3 = imul(imul(r, r), r)
    return (s, imul(iv(F(1, 2)), imul(g[1], r)),
            isub(imul(iv(F(1, 2)), imul(g[2], r)), imul(iv(F(1, 4)), imul(imul(g[1], g[1]), r3))))


def jfermi(g):
    """Jet of s(g), s(x) = 1/(exp(x) + 1): s' = -s(1 - s) and s'' = s(1 - s)(1 - 2s), then the chain rule."""
    e = iexp(g[0])
    s = irecip(iadd(e, (P, P)))
    one = (P, P)
    t = imul(s, isub(one, s))
    s1 = ineg(t)
    s2 = imul(t, isub(one, imul(iv(2), s)))
    return (s, imul(s1, g[1]), iadd(imul(s2, imul(g[1], g[1])), imul(s1, g[2])))


def thermal_jet(x):
    """Enclosures of T, T', T'' on the interval x of delta."""
    d = jvar(x)
    u = jsub(d, jconst(F(1, 2)))
    r2 = jsub(jconst(1), jscale(12, jmul(u, u)))
    lam = jmul(jscale(2, (PI, ZERO, ZERO)), jrecip(jsqrt(r2)))
    tot = jscale(F(-1, 24), r2)
    for k in range(KTERMS):
        for a in (jadd(jconst(k), d), jsub(jconst(k + 1), d)):
            tot = jadd(tot, jmul(a, jfermi(jmul(lam, a))))
    # the terms with k >= KTERMS: each, and each of its first two derivatives, is at most
    # 11 M^2 a^3 exp(-lam a) in size with M = max(1, lam, |lam'|, |lam''|); their sum is below
    # (223/10) M^2 (KTERMS + 1)^3 exp(-lam KTERMS)   (the proof, step 2)
    big = max(P, lam[0][1], abs(lam[1][0]), abs(lam[1][1]), abs(lam[2][0]), abs(lam[2][1]))
    rho = irecip(iexp((lam[0][0] * KTERMS, lam[0][0] * KTERMS)))
    bound = imul(imul(iv(F(223, 10) * (KTERMS + 1) ** 3), imul((big, big), (big, big))), (0, rho[1]))[1]
    return tuple(iadd(c, (-bound, bound)) for c in tot)


def sign_on(lo, hi, want, count, depth=0):
    """True if T has the sign `want` on all of [lo, hi]: mean-value form T(mid) + T'([lo, hi]) [-h, h],
    bisecting when it does not decide."""
    count[0] += 1
    mid = (lo + hi) / 2
    h = (hi - lo) / 2
    enc = iadd(thermal_jet(iv(mid))[0], imul(thermal_jet(iv(lo, hi))[1], iv(-h, h)))
    if (want < 0 and enc[1] < 0) or (want > 0 and enc[0] > 0):
        return True
    if depth > 24:
        return False
    return sign_on(lo, mid, want, count, depth + 1) and sign_on(mid, hi, want, count, depth + 1)


def derivative_sign_on(lo, hi, order, want, pieces):
    ok = True
    for i in range(pieces):
        a = lo + (hi - lo) * i / pieces
        b = lo + (hi - lo) * (i + 1) / pieces
        j = thermal_jet(iv(a, b))[order]
        ok = ok and (j[1] < 0 if want < 0 else j[0] > 0)
    return ok


# the cuts of the proof, as fractions of delta
D_A = F(429, 2000)
Q_LO, Q_HI = F(246, 1000), F(254, 1000)
T_LO, T_HI = F(3233, 10000), F(3433, 10000)
H_LO = F(46, 100)


def check_enclosures_contain_zero_at_the_three_stored_points_and_exclude_it_at_controls():
    premise("synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter")
    ok = True
    width = iv(F(1, 10 ** 12))[1]
    for d in (F(1, 4), F(1, 3), F(1, 2)):
        t = thermal_jet(iv(d))[0]
        ok = ok and t[0] <= 0 <= t[1] and t[1] - t[0] < width
    # the conic: r^2 = 1/4, 2/3, 1 at the three twists
    ok = ok and [1 - 12 * (d - F(1, 2)) ** 2 for d in (F(1, 4), F(1, 3), F(1, 2))] == [F(1, 4), F(2, 3), F(1)]
    # controls: T is negative at 0.23 and 0.40 and positive at 0.29, by more than 10^-4
    margin = iv(F(1, 10 ** 4))[1]
    ok = ok and thermal_jet(iv(F(23, 100)))[0][1] < -margin
    ok = ok and thermal_jet(iv(F(40, 100)))[0][1] < -margin
    ok = ok and thermal_jet(iv(F(29, 100)))[0][0] > margin
    # the slope at 1/4 is positive, at 1/3 negative, and T'(1/2) is enclosed by an interval around zero
    ok = ok and thermal_jet(iv(F(1, 4)))[1][0] > 0 and thermal_jet(iv(F(1, 3)))[1][1] < 0
    s = thermal_jet(iv(F(1, 2)))[1]
    ok = ok and s[0] <= 0 <= s[1] and s[1] - s[0] < width
    GA.check("T is enclosed within 10^-12 of zero at twists 1/4, 1/3, 1/2 and away from zero at three controls", ok)
    return ok


def check_no_zero_for_windows_shorter_than_three_twentieths_of_a_period():
    ok = True
    # at delta = D_A the conic has r^2 = 1 - 12 (1/2 - D_A)^2 below (3/20)^2, and r increases with delta
    r2 = 1 - 12 * (F(1, 2) - D_A) ** 2
    ok = ok and 0 < r2 <= F(3, 20) ** 2
    # every a is at least 1/5, since delta > 1/2 - 1/sqrt(12) > 1/5:  (1/2 - 1/5)^2 = 9/100 > 1/12
    ok = ok and (F(1, 2) - F(1, 5)) ** 2 > F(1, 12)
    # the sum is below (41/100) exp(-2 pi/(5 r)); r^2 exp(2 pi/(5 r)) decreases for r < pi/5 and at r = 3/20 it
    # exceeds (9/400) e^8 > (9/400) (2718/1000)^8 > 24 * 41/100
    e_low = sum(F(1, f) for f in (1, 1, 2, 6, 24, 120, 720))
    ok = ok and e_low > F(2718, 1000)
    ok = ok and F(9, 400) * F(2718, 1000) ** 8 > 24 * F(41, 100)
    # 2 pi/(5 * 3/20) >= 8 needs pi >= 3; and 3/20 < pi/5
    ok = ok and PI[0] >= iv(3)[1] and iv(F(3, 20))[1] < imul(PI, iv(F(1, 5)))[0]
    # the bracket of pi has width below 10^-30 and contains 3.14159265358979 to that many digits
    ok = ok and PI[1] - PI[0] < iv(F(1, 10 ** 30))[1]
    ok = ok and iv(F(314159265358979, 10 ** 14))[1] < PI[0] and PI[1] < iv(F(314159265358980, 10 ** 14))[0]
    GA.check("for r <= 3/20 the thermal sum is below r^2/24: the arithmetic of the bound, and the cut at 429/2000", ok)
    return ok


def check_sign_of_the_thermal_test_on_the_three_open_stretches():
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")
    ok = True
    used = [0]
    ok = ok and sign_on(D_A, Q_LO, -1, used)
    ok = ok and sign_on(Q_HI, T_LO, 1, used)
    ok = ok and sign_on(T_HI, H_LO, -1, used)
    ok = ok and 0 < used[0] < 400
    # the stretches and the neighbourhoods tile [429/2000, 1/2]
    ok = ok and D_A < Q_LO < F(1, 4) < Q_HI < T_LO < F(1, 3) < T_HI < H_LO < F(1, 2)
    GA.check("T < 0 on [0.2145, 0.246], T > 0 on [0.254, 0.3233], T < 0 on [0.3433, 0.46]", ok)
    return ok


def check_monotone_near_one_quarter_and_one_third_and_concave_near_one_half():
    premise("synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter")
    ok = True
    ok = ok and derivative_sign_on(Q_LO, Q_HI, 1, 1, 16)
    ok = ok and derivative_sign_on(T_LO, T_HI, 1, -1, 20)
    ok = ok and derivative_sign_on(H_LO, F(1, 2), 2, -1, 40)
    # the signs are not vacuous: the opposite claims fail
    ok = ok and not derivative_sign_on(Q_LO, Q_HI, 1, -1, 16)
    ok = ok and not derivative_sign_on(H_LO, F(1, 2), 2, 1, 40)
    GA.check("T' > 0 on [0.246, 0.254], T' < 0 on [0.3233, 0.3433], T'' < 0 on [0.46, 0.5]", ok)
    return ok
