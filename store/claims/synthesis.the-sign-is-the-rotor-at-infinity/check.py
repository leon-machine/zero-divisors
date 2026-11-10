"""synthesis.the-sign-is-the-rotor-at-infinity: exact checks.

Cl_Q(2,0) with GA.py (Fraction coefficients, blades () and (0, 1)); B = e1 e2, B^2 = -1.
R_t = ((1 - t^2) - 2t B)/(1 + t^2) for rational t, R_inf = -1.
(0) R_t is (1 - tB)(1 + tB)^{-1} computed with the inverse (1 - tB)/(1 + t^2).
(1) R_t ~R_t = 1, and v -> R_t v ~R_t maps integer vectors to rational vectors with the same square.
(2) R_s R_t = R_{s (+) t} on all pairs from a set of rationals with infinity, the cases st = 1 included.
(3) t -> R_t is a bijection onto the rational points of the circle a^2 + b^2 = 1 of height <= 60,
    inverse a + bB -> -b/(1 + a), -1 -> infinity.
(4) R_1 = -B is the half turn, R_1^2 = R_inf = -1, and R_inf acts on vectors as the identity.
(5) Over the rational-function field: a^2 + b^2 = 1, a' = -4t/(1 + t^2)^2 and a'^2 + b'^2 = 4/(1 + t^2)^2;
    the substitution t = 1/u maps 2 dt/(1 + t^2) on [1, inf) to 2 du/(1 + u^2) on (0, 1].
(6) The length 4 * int_0^1 dt/(1 + t^2) lies between rational Riemann bounds (f decreasing, directed
    rounding) of width below 1/1000, overlapping the Machin bounds on pi.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = GA.sig(2, 0)
B = {(0, 1): F(1)}
INF = "inf"


def even(a, b):
    out = {}
    if a != 0:
        out[()] = F(a)
    if b != 0:
        out[(0, 1)] = F(b)
    return out


def R(t):
    if t == INF:
        return GA.sc(-1)
    t = F(t)
    return even((1 - t * t) / (1 + t * t), -2 * t / (1 + t * t))


def oplus(s, t):
    if s == INF and t == INF:
        return F(0)
    if s == INF or t == INF:
        u = t if s == INF else s
        return INF if u == 0 else -1 / F(u)
    s, t = F(s), F(t)
    if s * t == 1:
        return INF
    return (s + t) / (1 - s * t)


GRID17 = [F(k, 17) for k in range(-40, 41)]
GRID23 = [F(k, 23) for k in range(-80, 81)]
GRID7 = [F(k, 7) for k in range(0, 400)]
VEC_RANGE = list(range(-3, 4))
HEIGHT = 60
RADII = list(range(1, HEIGHT + 1))
SAMPLE_VECTORS = [{(0,): F(1)}, {(1,): F(1)}, {(0,): F(3), (1,): F(-4)}]
RIEMANN_N = 4000
ROUND_D = 10 ** 15
ATAN_TERMS_5, ATAN_TERMS_239 = 12, 6


def isqrt(n):
    """Integer square root by Newton's method (exact integers)."""
    if n < 2:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


RATIONALS = [F(0), F(1), F(-1), F(2), F(-2), F(1, 2), F(-1, 2), F(3), F(1, 3), F(-3), F(-1, 3),
             F(2, 3), F(3, 2), F(-2, 3), F(-3, 2), F(5, 7), F(7, 5), F(-7, 5), F(4, 9), F(9, 4),
             F(11, 13)]


def check_rational_rotors_are_rotors():
    premise("synthesis.division-gives-the-rationals")
    tested = 0
    for t in RATIONALS + GRID17:
        one_plus = GA.add(GA.sc(1), GA.scal(t, B))
        inv = GA.scal(1 / (1 + t * t), GA.sub(GA.sc(1), GA.scal(t, B)))
        assert GA.mul(one_plus, inv, SQ) == GA.sc(1) and GA.mul(inv, one_plus, SQ) == GA.sc(1)
        Rt = GA.mul(GA.sub(GA.sc(1), GA.scal(t, B)), inv, SQ)
        assert GA.eq(Rt, R(t))
        assert GA.mul(Rt, GA.reverse(Rt), SQ) == GA.sc(1)
        tested += 1
        for x in VEC_RANGE:
            for y in VEC_RANGE:
                v = {k: F(c) for k, c in (((0,), x), ((1,), y)) if c != 0}
                w = GA.mul(GA.mul(Rt, v, SQ), GA.reverse(Rt), SQ)
                assert all(len(k) == 1 for k in w)
                assert GA.mul(w, w, SQ) == GA.mul(v, v, SQ)
    assert R(F(0)) == GA.sc(1)
    assert GA.eq(R(F(1)), {(0, 1): F(-1)})
    assert GA.eq(R(F(2)), {(): F(-3, 5), (0, 1): F(-4, 5)})
    assert tested == len(RATIONALS) + len(GRID17)
    return True


def check_composition_is_tangent_addition_with_infinity():
    premise("synthesis.division-gives-the-rationals")
    pts = RATIONALS + [INF]
    count = 0
    special = 0
    for s in pts:
        for t in pts:
            lhs = GA.mul(R(s), R(t), SQ)
            assert GA.eq(lhs, R(oplus(s, t))), (s, t)
            if s != INF and t != INF and s * t == 1:
                special += 1
            count += 1
    assert count == len(pts) ** 2
    # pairs with st = 1 in RATIONALS: (1,1), (-1,-1), (2,1/2), (-2,-1/2), (3,1/3), (-3,-1/3), (2/3,3/2),
    # (-2/3,-3/2), (5/7,7/5), (4/9,9/4), each unordered pair of distinct entries counted twice: 2 + 8 * 2
    assert special == 18
    # hand values: two half turns are the sign; 1/2 (+) 1/3 = 1; inf (+) 2 = -1/2
    assert oplus(F(1), F(1)) == INF and oplus(F(1, 2), F(1, 3)) == F(1) and oplus(INF, F(2)) == F(-1, 2)
    return True


def check_bijection_onto_the_rational_rotor_circle():
    premise("synthesis.division-gives-the-rationals")
    points = set()
    for r in RADII:
        for m in range(0, r + 1):
            n2 = r * r - m * m
            n = isqrt(n2)
            if n * n == n2:
                for sa in (1, -1):
                    for sb in (1, -1):
                        points.add((F(sa * m, r), F(sb * n, r)))
    assert (F(-1), F(0)) in points and (F(1), F(0)) in points
    # primitive triples with hypotenuse <= 60: (3,4,5) (5,12,13) (8,15,17) (7,24,25) (20,21,29) (12,35,37)
    # (9,40,41) (28,45,53), eight points each with signs and the swap, and the four points on the axes
    assert len(points) == 4 + 8 * 8
    images = set()
    for (a, b) in points:
        assert a * a + b * b == 1
        if a == -1:
            t = INF
        else:
            t = -b / (1 + a)
        assert GA.eq(R(t), even(a, b))
        images.add(t)
    assert len(images) == len(points)   # injective on these points
    # and every t in a grid maps into the circle and back
    # (3/5, 4/5) has t = -1/2 and (0, -1) has t = 1
    assert -F(4, 5) / (1 + F(3, 5)) == F(-1, 2) and -F(-1) / (1 + F(0)) == F(1)
    for t in GRID23:
        Rt = R(t)
        a, b = Rt.get((), F(0)), Rt.get((0, 1), F(0))
        assert a * a + b * b == 1 and a != -1 and -b / (1 + a) == t
    return True


def check_the_full_turn_is_the_sign_and_fixes_vectors():
    premise("synthesis.division-gives-the-rationals")
    R1 = R(F(1))
    assert GA.eq(R1, GA.neg(B))
    for v in SAMPLE_VECTORS:
        assert GA.eq(GA.mul(GA.mul(R1, v, SQ), GA.reverse(R1), SQ), GA.neg(v))     # half turn
        Rinf = R(INF)
        assert GA.eq(GA.mul(GA.mul(Rinf, v, SQ), GA.reverse(Rinf), SQ), v)          # full turn
    assert GA.eq(GA.mul(R1, R1, SQ), GA.sc(-1))                                     # two half turns
    assert oplus(F(1), F(1)) == INF
    return True


def check_speed_and_half_circle():
    t = GA.RF.var()
    one = GA.RF.const(1)
    den = one + t * t
    a = (one - t * t) / den
    b = (GA.RF.const(-2) * t) / den
    assert (a * a + b * b).eqrf(one)
    da, db = a.deriv(), b.deriv()
    assert da.eqrf((GA.RF.const(-4) * t) / (den * den))
    assert db.eqrf((GA.RF.const(-2) * (one - t * t)) / (den * den))
    assert (da * da + db * db).eqrf(GA.RF.const(4) / (den * den))
    # on t >= 0: b <= 0 and a strictly decreasing (sampled exactly)
    prev = None
    for tv in GRID7:
        assert (b.eval(tv) < 0) == (tv > 0)
        av = a.eval(tv)
        if prev is not None:
            assert av < prev
        prev = av
    # t = 1/u: f(1/u) * (1/u^2) = f(u) for f = 2/(1 + t^2)
    u = GA.RF.var()
    f_of_inv = GA.RF.const(2) / (one + one / (u * u))
    assert (f_of_inv * (one / (u * u))).eqrf(GA.RF.const(2) / (one + u * u))
    return True


def _floor_q(x, D):
    return F((x.numerator * D) // x.denominator, D)


def _ceil_q(x, D):
    return F(-((-x.numerator * D) // x.denominator), D)


def check_length_brackets_pi():
    # length = int_0^inf 2/(1+t^2) = 4 int_0^1 1/(1+t^2) (substitution of check 5); f decreasing on [0, 1]
    N, D = RIEMANN_N, ROUND_D
    lo = F(0)
    hi = F(0)
    for k in range(N):
        left = F(1) / (1 + F(k, N) ** 2)
        right = F(1) / (1 + F(k + 1, N) ** 2)
        lo += _floor_q(right / N, D)
        hi += _ceil_q(left / N, D)
    Llo, Lhi = 4 * lo, 4 * hi
    assert Lhi - Llo < F(1, 1000)

    # Machin: pi = 16 atan(1/5) - 4 atan(1/239); alternating series bracket atan(x) for 0 < x < 1
    def atan_bounds(x, terms):
        s, out = F(0), []
        for k in range(terms):
            s += (-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
            out.append(s)
        return min(out[-2:]), max(out[-2:])
    a5 = atan_bounds(F(1, 5), ATAN_TERMS_5)
    a239 = atan_bounds(F(1, 239), ATAN_TERMS_239)
    pi_lo = 16 * a5[0] - 4 * a239[1]
    pi_hi = 16 * a5[1] - 4 * a239[0]
    # the brackets are the last terms of the alternating series: x^(2k+1)/(2k+1) for k = terms - 1
    assert a5[1] - a5[0] == F(1, 5) ** 23 / 23
    assert a239[1] - a239[0] == F(1, 239) ** 11 / 11
    # the width of the bracket on pi: 16 / (23 * 5^23) + 4 / (11 * 239^11), about 5.84e-17
    assert pi_hi - pi_lo == 16 * F(1, 5) ** 23 / 23 + 4 * F(1, 239) ** 11 / 11
    assert Llo <= pi_hi and pi_lo <= Lhi
    assert F(3141, 1000) < Llo and Lhi < F(3143, 1000)
    return True
