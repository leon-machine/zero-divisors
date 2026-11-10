"""synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages: exact checks.

Rigorous rational interval arithmetic (Fractions, outward rounding at 10^-45; no floating point): pi from
Machin's formula, e^{-pi m/600} by interval powers, ln(1 + u) = 2 artanh(u/(2 + u)), explicit tails.

The array A(delta, r): fermion modes x_k = 2 pi (k + delta)/r, k in Z (the circle of r thermal periods with
twist delta; delta = 1/2 antiperiodic, delta = 0 periodic), Gibbs product state; per mode of |x|:
lg = ln(1 + e^{-|x|}), en = |x|/(e^{|x|} + 1), var = x^2 e^{|x|}/(e^{|x|} + 1)^2; a mode with x = 0 carries
ln 2 of entropy. S = sum (lg + en), v = sum var, e = sum en (above the sea).
"""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise

DEN = 10 ** 45
TOL = F(1, 10 ** 30)
BASE = 600
_C = {}


def rd(x):
    return series.round_down(x, DEN)


def ru(x):
    return series.round_up(x, DEN)


def pi_bounds():
    if "pi" not in _C:
        a5 = series.arctan_inv_bracket(5, 36)
        a239 = series.arctan_inv_bracket(239, 12)
        _C["pi"] = (rd(16 * a5[0] - 4 * a239[1]), ru(16 * a5[1] - 4 * a239[0]))
    return _C["pi"]


def base_bounds():
    """Bounds on e^{-pi/BASE}."""
    if "b" not in _C:
        pl, pu = pi_bounds()
        out = []
        for x in (pl / BASE, pu / BASE):
            s, term = F(0), F(1)
            for n in range(26):
                s += term
                term = term * x / (n + 1)
            out.append((s, s + 2 * term))
        _C["b"] = (rd(F(1) / out[1][1]), ru(F(1) / out[0][0]))
    return _C["b"]


def ipow(m):
    """Bounds on e^{-pi m/BASE}, m a nonnegative integer."""
    lo, hi = base_bounds()
    rl, rh = F(1), F(1)
    while m:
        if m & 1:
            rl, rh = rd(rl * lo), ru(rh * hi)
        lo, hi = rd(lo * lo), ru(hi * hi)
        m >>= 1
    return rl, rh


def ln1p_bounds(u):
    z = u / (2 + u)
    s, p = F(0), z
    for j in range(34):
        s += p / (2 * j + 1)
        p = p * z * z
    return rd(2 * s), ru(2 * s + 2 * p / (1 - z * z))


def ln2_bounds():
    if "l2" not in _C:
        _C["l2"] = ln1p_bounds(F(1))
    return _C["l2"]


def mode(m):
    """Intervals (lg, en, var) of the mode x = pi m/BASE."""
    pl, pu = pi_bounds()
    xl, xu = pl * m / BASE, pu * m / BASE
    ul, uu = ipow(m)
    lg = (ln1p_bounds(ul)[0], ln1p_bounds(uu)[1])
    en = (rd(xl * ul / (1 + ul)), ru(xu * uu / (1 + uu)))
    var = (rd(xl * xl * ul / ((1 + ul) * (1 + ul))), ru(xu * xu * uu / ((1 + uu) * (1 + uu))))
    return lg, en, var


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def isub(a, b):
    return (a[0] - b[1], a[1] - b[0])


def iscale(c, a):
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def pi_times(c):
    return iscale(F(c), pi_bounds())


def same(a, b):
    """Two intervals of width below TOL that overlap."""
    return a[1] - a[0] < TOL and b[1] - b[0] < TOL and a[0] <= b[1] and b[0] <= a[1]


def inside(a, lo, hi):
    return lo < a[0] and a[1] < hi




def half(d, r):
    """Intervals of (sum lg, sum en, sum var) over the modes x = 2 pi (k + d)/r, k >= 0, d > 0."""
    d, r = F(d), F(r)
    assert r <= 8        # the tail constant below needs mode spacing 2 pi/r above ln 2
    key = (d, r)
    if key not in _C:
        tot = [[F(0), F(0)], [F(0), F(0)], [F(0), F(0)]]
        k = 0
        while True:
            mm = 2 * BASE * (k + d) / r
            assert mm.denominator == 1
            m = mm.numerator
            if m > 30 * BASE:
                break
            for t, q in zip(tot, mode(m)):
                t[0] += q[0]
                t[1] += q[1]
            k += 1
        xk = pi_bounds()[1] * m / BASE
        tail = ru(2 * (1 + xk) * (1 + xk) * ipow(m)[1])
        assert tail < F(1, 10 ** 33)
        for t in tot:
            t[1] += tail
        _C[key] = tuple((t[0], t[1]) for t in tot)
    return _C[key]


def twisted(d, r):
    """(entropy, energy above the sea, variance) of the array of twist d on r thermal periods."""
    d = F(d)
    if d == 0:
        h = half(1, r)
        lg, en, var = (iscale(2, q) for q in h)
        return iadd(iadd(lg, en), ln2_bounds()), en, var
    a, b = half(d, r), half(1 - d, r)
    lg, en, var = (iadd(p, q) for p, q in zip(a, b))
    return iadd(lg, en), en, var


def bern2(a):
    return a * a - a + F(1, 6)


SPLITS = ((F(7, 3), 2, F(1, 3)), (F(-7, 3), -3, F(2, 3)), (F(1, 2), 0, F(1, 2)), (F(-1, 2), -1, F(1, 2)),
          (F(22, 7), 3, F(1, 7)), (F(-5), -5, F(0)))
LADDERS = tuple((M, r) for M in (1, 2, 3, 5) for r in (F(1), F(3, 2)))
RANGE = 6
SQ = GA.sig(1, 3)


def check_frequencies_split_into_twisted_ladders():
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("hawking.i-state-continuum")
    ok = True
    # every frequency w (in units of kappa/r) is k + delta with one k in Z and one delta in [0, 1)
    for w, k_want, d_want in SPLITS:
        k = w.numerator // w.denominator
        ok = ok and k == k_want and w - k == d_want and 0 <= d_want < 1
    # finite form: the antiperiodic ladder of M r periods is the union of the M ladders of r periods with
    # twists (2 j + 1)/(2 M), exactly, as sets of frequencies
    for M, r in LADDERS:
        big = sorted((k + F(1, 2)) / (M * r) for k in range(-RANGE * M, RANGE * M))
        small = sorted((k + F(2 * j + 1, 2 * M)) / r for j in range(M) for k in range(-RANGE, RANGE))
        ok = ok and big == small and len(set(big)) == 2 * RANGE * M
    # the one-window flow on the fibre of twist j/4 is the j-th power of J = e_2 e_3: -1 on twist 1/2,
    # and the two twists 1/4, 3/4 of the two-period window are the square roots J, -J of -1
    J = GA.mul(GA.gen(2), GA.gen(3), SQ)
    J2 = GA.mul(J, J, SQ)
    J3 = GA.mul(J2, J, SQ)
    ok = ok and GA.eq(J2, GA.sc(-1)) and GA.eq(J3, GA.neg(J)) and GA.eq(GA.mul(J3, J3, SQ), GA.sc(-1))
    ok = ok and GA.eq(GA.mul(J2, J2, SQ), GA.sc(1)) and not GA.eq(J, GA.sc(-1))
    GA.check("(i), (iii) frequencies split uniquely as k + delta; antiperiodic ladder of M r periods = M twisted "
             "ladders of r periods (M = 1, 2, 3, 5); one-window flow J^j on twist j/4", ok)
    return ok


def check_long_window_is_a_product_of_twisted_arrays():
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    premise("synthesis.boundary-mode-thermal-entropy")
    # two periods: twists 1/4 and 3/4 (equal by particle-hole symmetry); three periods: 1/6, 1/2, 5/6
    two, quarter = twisted(F(1, 2), 2), twisted(F(1, 4), 1)
    three, sixth, mid = twisted(F(1, 2), 3), twisted(F(1, 6), 1), twisted(F(1, 2), 1)
    ok = True
    for i in range(3):
        ok = ok and same(two[i], iscale(2, quarter[i]))
        ok = ok and same(three[i], iadd(mid[i], iscale(2, sixth[i])))
    ok = ok and same(mid[0], iscale(F(1, 2), ln2_bounds()))
    ok = ok and inside(quarter[0], F(51375, 10 ** 5), F(51376, 10 ** 5))
    ok = ok and inside(sixth[0], F(6114, 10 ** 4), F(6115, 10 ** 4))
    GA.check("(iii) S, e and v of the antiperiodic array on 2 (3) periods are the sums over the twists "
             "1/4, 3/4 (1/6, 1/2, 5/6) on one period, within 10^-30; S_{1/4}(1) = 0.51375...", ok)
    return ok


def check_twist_averages_reach_the_continuum_values():
    premise("synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r")
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")
    pl, pu = pi_bounds()
    ok = True
    # the M-point twist average at r = 1 is S_{1/2}(M)/M; its distance from pi/6 falls as Delta(M)/M
    prev = None
    for M, lo, hi in ((1, F(-17703, 10 ** 5), F(-17702, 10 ** 5)), (2, F(-9847, 10 ** 6), F(-9846, 10 ** 6)),
                      (4, F(-2017, 10 ** 8), F(-2016, 10 ** 8)), (8, F(-74, 10 ** 12), F(-73, 10 ** 12))):
        t = twisted(F(1, 2), M)
        gap = isub(iscale(F(1, M), t[0]), pi_times(F(1, 6)))
        ok = ok and inside(gap, lo, hi) and (prev is None or gap[0] > prev)
        prev = gap[1]
        # energy above the sea and variance: averages against pi/12 and pi/6
        if M == 8:
            ok = ok and inside(isub(iscale(F(1, M), t[1]), pi_times(F(1, 12))), F(40, 10 ** 4), F(41, 10 ** 4))
            ok = ok and abs(isub(iscale(F(1, M), t[2]), pi_times(F(1, 6)))[0]) < F(1, 10 ** 8)
    # the zeta-regularised symmetric sea, (pi/r) B_2(delta): its twist sum is the sea of the long window,
    # sum_j B_2((2 j + 1)/(2 M)) = B_2(1/2)/M, and the integral of B_2 over the twist is 0
    for M in (1, 2, 3, 4, 8):
        ok = ok and sum(bern2(F(2 * j + 1, 2 * M)) for j in range(M)) == bern2(F(1, 2)) / M
    for M, dlt in ((2, F(1, 3)), (3, F(1, 4)), (5, F(2, 7))):
        ok = ok and sum(bern2((j + dlt) / M) for j in range(M)) == bern2(dlt) / M
    ok = ok and bern2(F(1, 2)) == F(-1, 12) and F(1, 3) - F(1, 2) + F(1, 6) == 0
    GA.check("(iv) M-point twist averages of the entropy at r = 1 are pi/6 - 0.177, - 0.0098, - 2.0e-5, "
             "- 7.3e-11 (M = 1, 2, 4, 8); sea: sum of B_2 over the twists is B_2(1/2)/M, integral 0", ok)
    return ok


def check_entropy_across_the_twist_circle():
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.q-splits-maximum-entropy-affine-weights")
    p6 = pi_times(F(1, 6))
    s0, s24, s25, s50 = (twisted(d, 1)[0] for d in (0, F(6, 25), F(1, 4), F(1, 2)))
    ok = inside(s0, F(72039, 10 ** 5), F(72040, 10 ** 5))
    # the two particle-hole symmetric twists are on opposite sides of pi/6, which is crossed in (6/25, 1/4)
    ok = ok and s50[1] < s25[0] and s25[1] < p6[0] and p6[1] < s24[0] and s24[1] < s0[0]
    ok = ok and inside(isub(s24, p6), F(18, 10 ** 4), F(19, 10 ** 4))
    ok = ok and inside(isub(s0, p6), F(1967, 10 ** 4), F(1968, 10 ** 4))
    ok = ok and inside(isub(s50, p6), F(-1771, 10 ** 4), F(-1770, 10 ** 4))
    GA.check("(v) at r = 1: S_{1/2} = 0.3466 < S_{1/4} = 0.5138 < pi/6 = 0.5236 < S_{6/25} < S_0 = 0.7204", ok)
    return ok
