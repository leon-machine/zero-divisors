"""synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r: exact checks.

Rigorous rational interval arithmetic (Fractions, outward rounding at 10^-45; no floating point):
pi from Machin's formula, e^{-pi m/200} by interval powers of e^{-pi/200} (Taylor series with an explicit
remainder), ln(1 + u) = 2 artanh(u/(2 + u)) with a geometric remainder, explicit tails.

The array A(r): fermion modes x_k = 2 pi (k + 1/2)/r, k in Z (the antiperiodic circle of r thermal periods),
Gibbs product state; lg = ln(1 + e^{-x}), en = x/(e^x + 1), var = x^2 e^x/(e^x + 1)^2 per mode.
  f(r)      = pi/(12 r) + 2 sum lg          (ln Z, zeta-regularised symmetric ordering)
  e(r)      = 2 sum en                      (beta E above the sea)
  e_sym(r)  = e(r) - pi/(12 r)
  S(r)      = 2 sum (lg + en)
  v(r)      = 2 sum var
Continuum values for a window of r thermal periods: pi r/12 (ln Z and beta E, boost ordering), pi r/6 (entropy,
variance). Dual forms: the sums over A(1/r).
"""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise

DEN = 10 ** 45
TOL = F(1, 10 ** 30)
BASE = 200
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


def array(r):
    """Intervals of (sum lg, sum en, sum var) over the modes x = 2 pi (k + 1/2)/r, k >= 0 (half the array)."""
    r = F(r)
    assert r <= 8        # the tail constant below needs mode spacing 2 pi/r above ln 2
    if r not in _C:
        tot = [[F(0), F(0)], [F(0), F(0)], [F(0), F(0)]]
        k = 0
        while True:
            mm = F(BASE) * (2 * k + 1) / r
            assert mm.denominator == 1
            m = mm.numerator
            if m > 30 * BASE:
                break
            for t, q in zip(tot, mode(m)):
                t[0] += q[0]
                t[1] += q[1]
            k += 1
        pu = pi_bounds()[1]
        xk = pu * m / BASE
        tail = ru(2 * (1 + xk) * (1 + xk) * ipow(m)[1])
        assert tail < F(1, 10 ** 33)
        for t in tot:
            t[1] += tail
        _C[r] = tuple((t[0], t[1]) for t in tot)
    return _C[r]


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


def f_direct(r):
    return iadd(pi_times(F(1) / (12 * F(r))), iscale(2, array(r)[0]))


def f_dual(r):
    return iadd(pi_times(F(r) / 12), iscale(2, array(F(1) / F(r))[0]))


def e_above(r):
    return iscale(2, array(r)[1])


def e_sym(r):
    return isub(e_above(r), pi_times(F(1) / (12 * F(r))))


def entropy(r):
    a = array(r)
    return iscale(2, iadd(a[0], a[1]))


def delta_dual(r):
    """Delta(r) = S(r) - pi r/6 in the dual form 2 sum (lg - en) over A(1/r)."""
    a = array(F(1) / F(r))
    return iscale(2, isub(a[0], a[1]))


def check_self_duality_of_the_partition_function():
    premise("synthesis.imported-theta-function-identities")
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    ok = True
    for r in (2, 4, F(1, 2), F(4, 5)):
        ok = ok and same(f_direct(r), f_dual(r))
    # the fixed point: ln Z = (1/2) ln 2, and it exceeds the continuum's pi/12
    ok = ok and same(f_direct(1), iscale(F(1, 2), ln2_bounds()))
    ok = ok and inside(isub(f_direct(1), pi_times(F(1, 12))), F(8477, 10 ** 5), F(8478, 10 ** 5))
    # control: off the dual pair the values differ (f(2) is not f(4))
    ok = ok and not same(f_direct(2), f_direct(4))
    GA.check("(i) ln Z(r) = ln Z(1/r) at r = 2, 4, 1/2, 4/5 within 10^-30; ln Z(1) = (1/2) ln 2, "
             "0.08477... above pi/12", ok)
    return ok


def check_energy_matches_only_at_the_fixed_point():
    premise("synthesis.counted-unit-energy-at-half-offset")
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")
    zero = (F(0), F(0))
    # r = 1: the symmetric-ordered energy vanishes; equivalently sum (2n - 1)/(e^{(2n-1) pi} + 1) = 1/24
    ok = same(e_sym(1), zero)
    ok = ok and same(e_above(1), pi_times(F(1, 12)))
    # oddness under r -> 1/r, and values off the fixed point
    for r in (2, 4):
        ok = ok and same(iadd(e_sym(r), e_sym(F(1) / r)), zero)
    ok = ok and inside(e_sym(2), F(50017, 10 ** 5), F(50018, 10 ** 5))
    # D(r) = e(r) - pi r/12: the above-sea energy against the continuum's
    d2 = isub(e_above(2), pi_times(F(2, 12)))
    dh = isub(e_above(F(1, 2)), pi_times(F(1, 24)))
    d4 = isub(e_above(4), pi_times(F(4, 12)))
    ok = ok and inside(d2, F(1074, 10 ** 4), F(1076, 10 ** 4))
    ok = ok and inside(dh, F(-1076, 10 ** 4), F(-1074, 10 ** 4))
    ok = ok and inside(d4, F(653, 10 ** 4), F(654, 10 ** 4)) and same(iadd(d2, dh), zero)
    # the sea against the boost ground state: -pi/(12 r) against -pi r/12, equal only at r = 1
    for r in (F(1, 2), 1, 2, 4):
        ok = ok and ((F(1) / F(r) == F(r)) == (F(r) == 1))
    # the one-window Killing flow of the array at r = 1 is the half turn in the plane of J = e_2 e_3
    sq = GA.sig(1, 3)
    J = GA.mul(GA.gen(2), GA.gen(3), sq)
    ok = ok and GA.eq(GA.mul(J, J, sq), GA.sc(-1))
    GA.check("(ii) e_sym(1) = 0 and e(1) = pi/12 within 10^-30; e_sym odd under r -> 1/r; "
             "e(r) - pi r/12 = 0.1075, 0.0653, -0.1075 at r = 2, 4, 1/2", ok)
    return ok


def check_entropy_difference_as_a_function_of_window_length():
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    # Delta(1) = (1/2) ln 2 - pi/6
    want = isub(iscale(F(1, 2), ln2_bounds()), pi_times(F(1, 6)))
    ok = same(delta_dual(1), want) and inside(want, F(-17703, 10 ** 5), F(-17702, 10 ** 5))
    ok = ok and inside(delta_dual(2), F(-19693, 10 ** 6), F(-19692, 10 ** 6))
    ok = ok and inside(delta_dual(4), F(-8068, 10 ** 8), F(-8067, 10 ** 8))
    ok = ok and inside(delta_dual(8), F(-588, 10 ** 12), F(-586, 10 ** 12))
    # direct against dual form of the entropy
    for r in (2, 4):
        ok = ok and same(entropy(r), iadd(pi_times(F(r, 6)), delta_dual(r)))
    # short windows, from the direct form: Delta < 0 there too
    dh = isub(entropy(F(1, 2)), pi_times(F(1, 12)))
    dq = isub(entropy(F(1, 4)), pi_times(F(1, 24)))
    ok = ok and inside(dh, F(-23465, 10 ** 5), F(-23464, 10 ** 5))
    ok = ok and inside(dq, F(-13081, 10 ** 5), F(-13080, 10 ** 5))
    # remainder bound: |Delta(r) + 2 (pi r - 1) e^{-pi r}| <= 3 pi r e^{-2 pi r} for r = 1, 2, 4
    pl, pu = pi_bounds()
    for r in (1, 2, 4):
        ul, uu = ipow(BASE * r)
        lead = (-2 * (pu * r - 1) * uu, -2 * (pl * r - 1) * ul)
        rem = isub(delta_dual(r), lead)
        ok = ok and max(abs(rem[0]), abs(rem[1])) <= 3 * pl * r * ul * ul
    GA.check("(iii) Delta(1) = (1/2) ln 2 - pi/6 = -0.17702..., Delta(2) = -0.019692..., "
             "Delta(4) = -8.067e-5, Delta(8) = -5.87e-10, Delta(1/2) = -0.23464, Delta(1/4) = -0.13080; "
             "remainder bound at r = 1, 2, 4", ok)
    return ok


def check_energy_variance_against_the_continuum():
    premise("synthesis.counted-unit-energy-at-half-offset")
    premise("synthesis.q-splits-maximum-entropy-affine-weights")
    v1 = iscale(2, array(1)[2])
    ok = inside(v1, F(79821, 10 ** 5), F(79822, 10 ** 5))
    ok = ok and inside(isub(v1, pi_times(F(1, 6))), F(2746, 10 ** 4), F(2747, 10 ** 4))
    # dual form: v(r) = pi r/6 + 2 sum (var - 2 en) over A(1/r)
    for r in (1, 2):
        a = array(F(1) / F(r))
        dual = iadd(pi_times(F(r, 6)), iscale(2, isub(a[2], iscale(2, a[1]))))
        ok = ok and same(iscale(2, array(r)[2]), dual)
    ok = ok and inside(isub(iscale(2, array(2)[2]), pi_times(F(2, 6))), F(1000, 10 ** 4), F(1002, 10 ** 4))
    # short windows: the difference is negative at r = 1/2 and positive at r = 5/8, so it vanishes between
    vh = isub(iscale(2, array(F(1, 2))[2]), pi_times(F(1, 12)))
    v58 = isub(iscale(2, array(F(5, 8))[2]), pi_times(F(5, 48)))
    ok = ok and inside(vh, F(-1150, 10 ** 4), F(-1148, 10 ** 4)) and v58[0] > 0
    GA.check("(iv) beta^2 Var(E) per array at r = 1 in (0.79821, 0.79822), 0.2746 above pi/6; "
             "dual form at r = 1, 2; 0.100 above pi/3 at r = 2", ok)
    return ok


def check_residue_if_the_continuum_value_were_counted():
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping")
    premise("synthesis.de-sitter-mode-count")
    pl, pu = pi_bounds()
    l2 = ln2_bounds()
    # residue = 1/(4 <s>) per counted unit; a unit of two arrays carries ln 2, of two components pi/3
    reg = (F(1) / (4 * l2[1]), F(1) / (4 * l2[0]))
    alt = (F(3) / (4 * pu), F(3) / (4 * pl))
    ok = inside(reg, F(36067, 10 ** 5), F(36068, 10 ** 5))
    ok = ok and inside(alt, F(23873, 10 ** 5), F(23874, 10 ** 5))
    # per component: 3/(2 pi) against 1/(2 ln 2); ratio 3 ln 2/pi; components per ln 2: 6 ln 2/pi
    ok = ok and inside((2 * alt[0], 2 * alt[1]), F(47746, 10 ** 5), F(47747, 10 ** 5))
    ok = ok and inside((2 * reg[0], 2 * reg[1]), F(72134, 10 ** 5), F(72135, 10 ** 5))
    ratio = (3 * l2[0] / pu, 3 * l2[1] / pl)
    ok = ok and inside(ratio, F(66190, 10 ** 5), F(66191, 10 ** 5))
    ubar = (2 * ratio[0], 2 * ratio[1])
    ok = ok and 1 < ubar[0] and ubar[1] < 2 and inside(ubar, F(13238, 10 ** 4), F(13239, 10 ** 4))
    # arrays of window r per Planck area per modular period, r/(4 S(r)): 1/(2 ln 2) at r = 1, 0.4866 at r = 2
    s2 = entropy(2)
    ok = ok and inside((F(2) / (4 * s2[1]), F(2) / (4 * s2[0])), F(4866, 10 ** 4), F(4867, 10 ** 4))
    # the cosmological count 4 pi kappa_c N^2 would have the coefficient 3 in place of pi/ln 2
    ok = ok and 4 * F(3, 4) == 3 and inside((pl / l2[1], pu / l2[0]), F(45323, 10 ** 4), F(45324, 10 ** 4))
    GA.check("(v) 1/(4 ln 2) = 0.36067, 3/(4 pi) = 0.23873 per unit of two; 3/(2 pi) per component; "
             "6 ln 2/pi = 1.3238 components per ln 2; r/(4 S(r)) = 0.4866 at r = 2", ok)
    return ok
