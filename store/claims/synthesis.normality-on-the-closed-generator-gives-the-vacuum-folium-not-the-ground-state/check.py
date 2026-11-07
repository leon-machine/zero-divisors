"""Local normality on the closed generator: exact checks.

(1) The attachment closes a null line into a circle. In Cl(2,4) (squares e0 +1, e1..e3 -1, nu +1, e_- -1,
    n_inf = nu + e_-, n_o = (nu - e_-)/2, point X(s) = n_o + s n on the null line of n = e0 + e1) the
    translation rotor 1 + (t/2) n n_inf sends s to s + t, the special conformal rotor 1 + (c/2) m n_o
    (m = e0 - e1) sends s to s/(1 - 2c s), the dilation rotor cosh + sinh nu e_- sends s to s/r^2, all
    projectively; the composite J = T(-1) K(-1/2) T(-1) sends X(s) to a multiple of X(-1/s) and n_o (s = 0)
    to a multiple of n, the point at infinity of the line. The null vacuum kernel with spinor weight,
    (cu + d)^-1 (cv + d)^-1 / (g(u) - g(v)), equals 1/(u - v) for each of these Moebius maps g.
(2) Three arcs cover every pair: with E1 = {|u| > L}, E2, E3 small disjoint intervals inside [-L, L], each
    pair of points of the line avoids some E_k, and each A_k = complement of E_k is an interval of the
    closed generator (A1 bounded; A2, A3 through the point at infinity).
(3) Affine-KMS states fail on one far end. x/sinh x = 1 - x^2/6 + 7x^4/360 - ... (exact series inversion),
    so the KMS kernel differs from the vacuum by a nonzero translation-invariant kernel; for such a kernel
    the integral of |R(u - v)|^2 over n consecutive diagonal unit squares is n times one square's value.
(4) The slope-jump reparametrisation f: f' = 1 - (3/4) S((u + 1)/2) on [-1, 1], S the quintic smoothstep;
    f(-1) = -1, f(1) = 1/4, f' in [1/4, 1], f'' and f''' vanish at both ends, f = u on u <= -1 and u/4 on
    u >= 1. Its vacuum kernel equals the null vacuum's on (1, inf)^2 and on (-inf, -1)^2.
(5) Its cross block on (1, inf) x (-inf, -1) differs from the vacuum's by (u + 2v)/((u - 4v)(u - v)) (times
    i/2 pi), homogeneous of degree -1; on [5, 6] x [-2, -1] the modulus is >= 1/112, and the dilates by 2^k
    are disjoint with equal integrals, so the difference is not square integrable. Slope 9 gives
    (2u + 6v)/((u - 9v)(u - v)); slopes 4 and 9 differ from each other by a nonzero degree -1 kernel.
(6) The affine group is implementable on it: conjugating a translation by b gives U + b near -inf and
    U + b/4 near +inf, whose cross-block change -d/((U - V)(U - V + d)) is degree -2 with
    int_{U, W > L} (U + W)^-4 = 1/(24 L^2) finite; conjugating the dilation gives the same dilation at both
    ends, whose far blocks are unchanged exactly.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

S6 = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
NINF = GA.add(E[4], E[5])
NO = GA.scal(F(1, 2), GA.sub(E[4], E[5]))
NN = GA.add(E[0], E[1])
MM = GA.sub(E[0], E[1])

LINE_S = (F(2), F(-3, 5), F(7, 3), F(1, 4))
TRANS_T = (F(3), F(-1, 2))
SCT_C = (F(1), F(-1, 3))
DIL_R = (F(3, 2), F(2, 5))
KER_PTS = [(F(1, 3), F(-2)), (F(5, 2), F(7, 4)), (F(-3), F(1, 7))]
MOEBIUS = [(F(1), F(3), F(0), F(1)), (F(1), F(0), F(-2), F(1)), (F(3, 2), F(0), F(0), F(2, 3)),
           (F(0), F(-1), F(1), F(0)), (F(2), F(1), F(3), F(2))]

ARC_L = F(10)
ARC_E2 = (F(-3), F(-2))
ARC_E3 = (F(4), F(5))
ARC_WITNESS = [(F(-1000), F(1000)), (F(-5, 2), F(9, 2)), (F(-5, 2), F(1000)), (F(9, 2), F(-1000)), (F(0), F(7))]
ARC_PTS = [F(k, 2) for k in range(-60, 61, 3)] + [F(-1000), F(1000), F(37, 3), F(-9, 2), F(-5, 2), F(9, 2)]

SERIES_N = 8
DIAG_KERNELS = [[F(0), F(1)], [F(0), F(-1, 6), F(0), F(7, 360)]]
DIAG_N = 5
DIAG_L = (F(0), F(3), F(17, 2))

SLOPE = F(1, 4)
F_AT = (F(-1), F(1, 4))
FAR_PTS = [F(1), F(3, 2), F(4), F(13), F(250)]
CROSS_PTS = [(F(1), F(-1)), (F(3), F(-1)), (F(7, 2), F(-5)), (F(40), F(-3, 2))]
RECT = (F(5), F(6), F(-2), F(-1))
RECT_BOUND = F(1, 112)
SHELLS = 40
MU_PAIR = ((F(4), F(2)), (F(9), F(3)))
HOM_S = (F(2), F(1, 3), F(5))
TRANS_B = (F(1), F(-3, 2), F(2))
IMPL_LEFT = (F(-50), F(-7, 2), F(-3))
IMPL_RIGHT = (F(9), F(300), F(13, 2))
FAR_L = (F(1), F(5, 2), F(10))
DIL_LAM = (F(2), F(1, 3))


def _m(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, S6)
    return out


def _sand(R, X):
    return _m(R, X, GA.reverse(R))


def _point(s):
    return GA.add(NO, GA.scal(s, NN))


def _prop(Y, s):
    """Y is a nonzero multiple of the point X(s)."""
    lam = Y.get((4,), F(0)) - Y.get((5,), F(0))     # coefficient of n_o
    return lam != 0 and GA.eq(Y, GA.scal(lam, _point(s)))


def _trans(t):
    return GA.add(GA.sc(1), GA.scal(t / 2, _m(NN, NINF)))


def _sct(c):
    return GA.add(GA.sc(1), GA.scal(c / 2, _m(MM, NO)))


def _dil(r):
    return GA.add(GA.sc((r + 1 / r) / 2), GA.scal((r - 1 / r) / 2, _m(E[4], E[5])))


def _w0(u, v):
    return 1 / (u - v)


def check_the_attachment_closes_each_null_line_into_a_circle():
    premise("synthesis.attachment-conformal-energy-is-generated-by-z")
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    GA.check("n_inf, n_o null with n_inf . n_o = 1",
             _m(NINF, NINF) == {} and _m(NO, NO) == {} and GA.eq(GA.add(_m(NINF, NO), _m(NO, NINF)), GA.sc(2)))
    for s in LINE_S:
        GA.check("X(s) is null", _m(_point(s), _point(s)) == {})
        for t in TRANS_T:
            GA.check("translation: s -> s + t", _prop(_sand(_trans(t), _point(s)), s + t))
        for c in SCT_C:
            GA.check("special conformal: s -> s/(1 - 2cs)", _prop(_sand(_sct(c), _point(s)), s / (1 - 2 * c * s)))
        for r in DIL_R:
            GA.check("dilation: s -> s/r^2", _prop(_sand(_dil(r), _point(s)), s / (r * r)))
        J = _m(_trans(F(-1)), _sct(F(-1, 2)), _trans(F(-1)))
        GA.check("J: s -> -1/s", _prop(_sand(J, _point(s)), -1 / s))
    J = _m(_trans(F(-1)), _sct(F(-1, 2)), _trans(F(-1)))
    Y = _sand(J, NO)
    lam = Y.get((0,), F(0))
    GA.check("J sends s = 0 to the point at infinity n of the line", lam != 0 and GA.eq(Y, GA.scal(lam, NN)))
    for (a, b, c, d) in MOEBIUS:
        GA.check("SL(2) element", a * d - b * c == 1)
        for (u, v) in KER_PTS:
            gu, gv = (a * u + b) / (c * u + d), (a * v + b) / (c * v + d)
            GA.check("vacuum kernel invariant with spinor weight",
                     _w0(gu, gv) / ((c * u + d) * (c * v + d)) == _w0(u, v))


def _in(x, iv):
    return iv[0] < x < iv[1]


def check_three_arcs_cover_every_pair_of_points():
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    E1 = lambda x: x < -ARC_L or x > ARC_L
    E2 = lambda x: _in(x, ARC_E2)
    E3 = lambda x: _in(x, ARC_E3)
    GA.check("E2, E3 disjoint and inside [-L, L]",
             ARC_E2[1] < ARC_E3[0] and -ARC_L < ARC_E2[0] and ARC_E3[1] < ARC_L)
    excl = (E1, E2, E3)
    for x in ARC_PTS:
        GA.check("each point lies in at most one excluded set", sum(1 for e in excl if e(x)) in (0, 1))
        for y in ARC_PTS:
            GA.check("each pair lies in a common arc A_k", any(not e(x) and not e(y) for e in excl))

    def arcs(x, y):
        return tuple(k + 1 for k, e in enumerate(excl) if not e(x) and not e(y))
    # the two far ends are joined only through the arcs A2, A3, which pass through infinity
    expected = ((2, 3), (1,), (3,), (2,), (1, 2, 3))
    GA.check("witness pairs: common arcs as tabulated",
             tuple(arcs(x, y) for (x, y) in ARC_WITNESS) == expected)


def check_affine_kms_states_fail_on_a_single_far_end():
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    # sinh(x)/x = sum x^{2k}/(2k+1)!
    fact = [F(1)]
    for k in range(1, 2 * SERIES_N + 2):
        fact.append(fact[-1] * k)
    sinhx_x = [F(0)] * (SERIES_N + 1)
    for k in range(0, SERIES_N + 1, 2):
        sinhx_x[k] = F(1) / fact[k + 1]
    inv = GA.ps_inv(sinhx_x, SERIES_N)
    GA.check("x/sinh x = 1 - x^2/6 + 7x^4/360 + ...",
             inv[0] == 1 and inv[1] == 0 and inv[2] == F(-1, 6) and inv[3] == 0 and inv[4] == F(7, 360))
    GA.check("the KMS remainder (x/sinh x - 1)/x is nonzero (leading -x/6)", inv[2] != 0)
    # translation-invariant kernel R(u - v): diagonal unit squares contribute equally, and a far end
    # [L, L + n]^2 carries at least n times that
    for poly in DIAG_KERNELS:
        sq = GA.pmul(poly, poly)
        biv = _shift_kernel(sq)
        vals = [_int_rect(biv, L, L + 1, L, L + 1) for L in DIAG_L]
        GA.check("each diagonal unit square has the same positive integral", len(set(vals)) == 1 and vals[0] > 0)
        for L in DIAG_L:
            GA.check("far end [L, L + n]^2 carries >= n squares",
                     _int_rect(biv, L, L + DIAG_N, L, L + DIAG_N) >= DIAG_N * vals[0])


def _binom(n, k):
    out = F(1)
    for i in range(k):
        out = out * (n - i) / (i + 1)
    return out


def _shift_kernel(p):
    """sum_k a_k (u - v)^k as a bivariate polynomial {(i, j): c} for u^i v^j."""
    out = {}
    for k, a in enumerate(p):
        if a == 0:
            continue
        for j in range(k + 1):
            c = a * _binom(k, j) * (-1) ** j
            out[k - j, j] = out.get((k - j, j), F(0)) + c
    return {key: v for key, v in out.items() if v != 0}


def _int_rect(p, x0, x1, y0, y1):
    tot = F(0)
    for (i, j), a in p.items():
        tot += a * (x1 ** (i + 1) - x0 ** (i + 1)) / (i + 1) * (y1 ** (j + 1) - y0 ** (j + 1)) / (j + 1)
    return tot


def _S(t):
    return 6 * t ** 5 - 15 * t ** 4 + 10 * t ** 3


def _fprime_poly():
    # f'(u) = 1 - (3/4) S((u + 1)/2) as a polynomial in u
    t = [F(1, 2), F(1, 2)]
    t3 = GA.pmul(GA.pmul(t, t), t)
    t4 = GA.pmul(t3, t)
    t5 = GA.pmul(t4, t)
    S = GA.padd(GA.padd([6 * c for c in t5], [-15 * c for c in t4]), [10 * c for c in t3])
    return GA.padd([F(1)], [F(-3, 4) * c for c in S])


def _f(u):
    if u <= -1:
        return u
    if u >= 1:
        return SLOPE * u
    fp = _fprime_poly()
    anti = GA.ps_int(fp)
    return F(-1) + GA.peval(anti, u) - GA.peval(anti, F(-1))


def _fp(u):
    if u <= -1:
        return F(1)
    if u >= 1:
        return SLOPE
    return GA.peval(_fprime_poly(), u)


def check_the_slope_jump_vacuum_is_the_null_vacuum_on_each_far_end():
    premise("synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation")
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    fp = _fprime_poly()
    anti = GA.ps_int(fp)
    GA.check("f(1) - f(-1) = 5/4: f(-1) = -1 joins f(1) = 1/4",
             GA.peval(anti, F(1)) - GA.peval(anti, F(-1)) == F_AT[1] - F_AT[0])
    GA.check("f'(-1) = 1, f'(1) = 1/4", GA.peval(fp, F(-1)) == 1 and GA.peval(fp, F(1)) == SLOPE)
    d1 = GA.pderiv(fp)
    d2 = GA.pderiv(d1)
    GA.check("f'' and f''' vanish at both ends (C^3 joins)",
             all(GA.peval(d, x) == 0 for d in (d1, d2) for x in (F(-1), F(1))))
    # S' = 30 t^2 (1 - t)^2 >= 0, so f' decreases from 1 to 1/4: f' in [1/4, 1] > 0
    grid = [F(k, 16) for k in range(-16, 17)]
    GA.check("f' decreasing on [-1, 1] (S' >= 0)", all(GA.peval(d1, x) <= 0 for x in grid))
    GA.check("f' >= 1/4 > 0 on the grid", all(GA.peval(fp, x) >= SLOPE for x in grid))
    for u in FAR_PTS:
        for v in FAR_PTS:
            if u == v:
                continue
            Wr = _fp(u) * SLOPE / (_fp(v) * (_f(u) - _f(v)))    # sqrt(f'(u) f'(v)) = 1/4 on u, v >= 1
            GA.check("right far end: vacuum of f = null vacuum", Wr == _w0(u, v))
            Wl = F(1) / (_f(-u) - _f(-v))                      # sqrt(f' f') = 1 on u, v <= -1
            GA.check("left far end: vacuum of f = null vacuum", Wl == _w0(-u, -v))


def _cross(u, v, mu, rt):
    return rt / (u - mu * v) - 1 / (u - v)


def check_the_slope_jump_vacuum_is_globally_disjoint_from_the_null_vacuum():
    premise("synthesis.imported-powers-stormer-takesaki-disjointness")
    premise("synthesis.local-normality-at-the-edge-gives-the-null-ground-state")
    for (u, v) in CROSS_PTS:
        # sqrt(f'(u) f'(v)) = 1/2 on the cross block, f(u) - f(v) = u/4 - v
        Wf = F(1, 2) / (_f(u) - _f(v))
        GA.check("cross block: W_f - W_0 = (u + 2v)/((u - 4v)(u - v))",
                 Wf - _w0(u, v) == (u + 2 * v) / ((u - 4 * v) * (u - v)))
        for (mu, rt) in MU_PAIR:
            GA.check("slope mu: sqrt(mu)/(u - mu v) form", rt * rt == mu)
            for s in HOM_S:
                GA.check("homogeneous of degree -1", _cross(s * u, s * v, mu, rt) == _cross(u, v, mu, rt) / s)
        (m1, r1), (m2, r2) = MU_PAIR
        GA.check("slope 9: (2u + 6v)/((u - 9v)(u - v))",
                 _cross(u, v, m2, r2) == (2 * u + 6 * v) / ((u - 9 * v) * (u - v)))
        D12 = r1 / (u - m1 * v) - r2 / (u - m2 * v)
        GA.check("slopes 4 and 9 differ by -(u + 6v)/((u - 4v)(u - 9v))",
                 D12 == -(u + 6 * v) / ((u - 4 * v) * (u - 9 * v)))
    u0, u1, v0, v1 = RECT
    GA.check("rectangle inside the cross block", u0 >= 1 and v1 <= -1)
    num_min = u0 + 2 * v0                    # u + 2v increasing in u and v
    den1_max = u1 - 4 * v0
    den2_max = u1 - v0
    GA.check("on the rectangle |u + 2v| >= 1, u - 4v <= 14, u - v <= 8",
             num_min == 1 and den1_max == 14 and den2_max == 8 and num_min > 0 and u0 - 4 * v1 > 0)
    GA.check("modulus bound 1/112", num_min / (den1_max * den2_max) == RECT_BOUND)
    lowers = []
    for k in range(SHELLS):
        q = F(2) ** k
        a0, a1, b0, b1 = q * u0, q * u1, q * v0, q * v1
        if k:
            GA.check("dilated rectangles disjoint", a0 > q / 2 * u1)
        # lower bound of |W_f - W_0| on the dilate, times its area
        lowers.append(((a0 + 2 * b0) / ((a1 - 4 * b0) * (a1 - b0))) ** 2 * (a1 - a0) * (b1 - b0))
    GA.check("each dilate carries the same lower bound (degree -1 kernel)", len(set(lowers)) == 1 and lowers[0] > 0)
    GA.check("the sum over the dilates is SHELLS times it", sum(lowers) == SHELLS * lowers[0])


def _finv_far(U):
    """inverse of f on its far pieces"""
    return U if U <= F_AT[0] else U / SLOPE


def check_the_affine_group_is_implementable_on_the_slope_jump_vacuum():
    premise("synthesis.imported-powers-stormer-takesaki-disjointness")
    premise("synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation")
    for b in TRANS_B:
        for U in IMPL_LEFT:
            GA.check("h = f tau_b f^-1 is U + b near -inf", _f(_finv_far(U - abs(b)) + b) == U - abs(b) + b)
        for U in IMPL_RIGHT:
            GA.check("and U + b/4 near +inf", _f(_finv_far(U + abs(b)) + b) == U + abs(b) + b / 4)
        d = b / 4 - b
        for (U, V) in CROSS_PTS:
            GA.check("cross-block change is degree -2: -d/((U - V)(U - V + d))",
                     _w0(U + b / 4, V + b) - _w0(U, V) == -d / ((U - V) * (U - V + d)))
    for L in FAR_L:
        # G(x) = x^-2 / 6: G'' = (-2)(-3)/6 x^-4 = x^-4, so the quadrant integral is G(2L)
        GA.check("int_{U, W > L} (U + W)^-4 = 1/(24 L^2), finite",
                 F(-2) * F(-3) / 6 == 1 and F(1, 6) / (2 * L) ** 2 == F(1, 24) / L ** 2)
    for lam in DIL_LAM:
        for U in IMPL_LEFT + IMPL_RIGHT:
            GA.check("conjugated dilation is U -> lam U near both ends", _f(_finv_far(U) * lam) == lam * U)
        for (U, V) in CROSS_PTS:
            GA.check("far blocks unchanged by a common dilation", lam * _w0(lam * U, lam * V) == _w0(U, V))
