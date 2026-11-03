"""sheaf.collision-census: exact checks.

On the Kasner constraint variety p1 + p2 + p3 = 1, p1^2 + p2^2 + p3^2 = 1:
(i) a repeated exponent: setting the pair (i, j) equal to s (all three pairs) reduces the second constraint to
the polynomial 6s^2 - 4s = 2s(3s - 2), so s = 0 or s = 2/3, the triples (0,0,1) and (2/3,2/3,-1/3) up to
permutation; both satisfy the constraints.
(ii) a vanishing exponent: setting p_i = 0 (all three slots) reduces the constraints to 2t(t - 1) = 0 for a
remaining exponent t, so the triple is (0,0,1) up to permutation: zeros come in pairs.
(iii) scan of the rational parametrisation p(u) = (-u, 1+u, u(1+u))/(1+u+u^2), which covers every rational point
of the variety: the constraints hold as rational-function identities; over all u = a/b with |a| <= 7, 1 <= b <= 7
a repeated exponent occurs exactly at u in {0, -1} (Taub) and {1, -2, -1/2} (Schwarzschild), and a zero exponent
exactly at u in {0, -1}, with the census triples there.
No premises: the lemma is self-contained algebra.
"""
from fractions import Fraction as F
import GA

# generic scan range for (iii): every u = a/b with |a| <= 7, 1 <= b <= 7
SCAN = sorted({F(a, b) for a in range(-7, 8) for b in range(1, 8)})


def poly(*c):
    return GA.ptrim([F(x) for x in c])


def kasner(u):
    D = 1 + u + u * u
    return (-u / D, (1 + u) / D, u * (1 + u) / D)


def sorted_triple(t):
    return tuple(sorted(t))


def check_repeated_exponent_census():
    ok = True
    s = poly(0, 1)
    one = poly(1)
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        # p_i = p_j = s, the remaining exponent is 1 - 2s by the linear constraint
        trip = [None, None, None]
        trip[i] = s
        trip[j] = s
        rest = 3 - i - j
        trip[rest] = GA.padd(one, GA.pneg(GA.pmul(poly(2), s)))
        quad = poly(-1)
        for t in trip:
            quad = GA.padd(quad, GA.pmul(t, t))
        # the reduced constraint, and its factorisation 2s(3s - 2)
        ok = ok and quad == poly(0, -4, 6)
        ok = ok and GA.pmul(poly(0, 2), poly(-2, 3)) == quad
        ok = ok and GA.peval(quad, F(0)) == 0 and GA.peval(quad, F(2, 3)) == 0
        ok = ok and GA.peval(quad, F(1, 3)) != 0
    # the two census triples satisfy both constraints
    for trip in ((F(0), F(0), F(1)), (F(-1, 3), F(2, 3), F(2, 3))):
        ok = ok and sum(trip) == 1 and sum(t * t for t in trip) == 1
    GA.check("repeated exponent: 6s^2 - 4s = 2s(3s - 2) for every pair, so s = 0 or 2/3", ok)
    return ok


def check_zero_exponent_forces_a_second_zero():
    ok = True
    t = poly(0, 1)
    one = poly(1)
    for i in range(3):
        # p_i = 0, the other two are t and 1 - t
        other = GA.padd(one, GA.pneg(t))
        gap = GA.padd(GA.padd(GA.pmul(t, t), GA.pmul(other, other)), poly(-1))
        ok = ok and gap == GA.pmul(poly(0, 2), poly(-1, 1))      # 2t(t - 1)
        roots = [r for r in (F(0), F(1), F(1, 2), F(-1)) if GA.peval(gap, r) == 0]
        ok = ok and roots == [F(0), F(1)]
        for r in roots:
            trip = [F(0)] * 3
            js = [j for j in range(3) if j != i]
            trip[js[0]] = r
            trip[js[1]] = 1 - r
            ok = ok and sorted_triple(trip) == (F(0), F(0), F(1))
    GA.check("a zero exponent forces a second zero: 2t(t - 1) = 0, triple (0,0,1) up to permutation", ok)
    return ok


def check_scan_of_rational_parametrisation():
    ok = True
    u = GA.RF.var()
    D = GA.RF1 + u + u * u
    p = (-u / D, (GA.RF1 + u) / D, u * (GA.RF1 + u) / D)
    ok = ok and (p[0] + p[1] + p[2]).eqrf(GA.RF1)
    ok = ok and (p[0] * p[0] + p[1] * p[1] + p[2] * p[2]).eqrf(GA.RF1)
    repeated, zero = set(), set()
    for x in SCAN:
        trip = kasner(x)
        if trip[0] == trip[1] or trip[0] == trip[2] or trip[1] == trip[2]:
            repeated.add(x)
            ok = ok and sorted_triple(trip) in ((F(0), F(0), F(1)), (F(-1, 3), F(2, 3), F(2, 3)))
        if 0 in trip:
            zero.add(x)
            ok = ok and sorted_triple(trip) == (F(0), F(0), F(1))
    ok = ok and repeated == {F(0), F(-1), F(1), F(-2), F(-1, 2)}
    ok = ok and zero == {F(0), F(-1)}
    GA.check("rational points: repeated exponents only at the Taub and Schwarzschild orbits, zeros only in pairs", ok)
    return ok
