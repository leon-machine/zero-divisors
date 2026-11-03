"""synthesis.sudden-descent-feature-not-tilt: exact checks.

Massless scalar in the frozen phase's flat slicing, chi = a phi, a = -1/(H eta), in the variable
z = k eta < 0: chi'' + (1 - 2/z^2) chi = 0. Expressions are stored as E^s * sum_n c_n z^(-n) with
E = e^(-iz), s in {+1, -1}, c_n Gaussian rationals (GA.QI); d/dz acts exactly.

(1) u = E (1 - i/z) solves the mode equation; the Wronskian u ubar' - u' ubar is 2i.
(2) Initial data chi = 1, chi' = -i at z_d (instantaneous vacuum, units sqrt(2k) = 1):
    alpha = E_d^(-1) A(z_d), beta = -E_d B(z_d) with A = 1 + i/z - 1/(2 z^2), B = 1/(2 z^2);
    |alpha|^2 - |beta|^2 = 1 identically.
(3) F(x) = |alpha - beta|^2 at x = -z_d equals
    1 + 1/(2x^4) + x^(-2) [ (1 - 1/(2x^2)) cos 2x - x^(-1) sin 2x ],
    checked as an identity in independent (x, cos 2x, sin 2x) on rational points of the circle.
(4) Small x: x^4 F(x) = (4/9) x^6 + O(x^8) (exact Taylor coefficients), so F ~ (4/9) x^2: blue.
(5) Large x: (|A| - B)^2 <= F <= (|A| + B)^2 with |A|^2 = 1 + 1/(4x^4); for 7-e-fold windows in
    [3, oo) the ratio F(x1)/F(x2) stays below exp(7 (1 - n_s)) at the weakest 2-sigma tilt.
(6) Every window: exact enclosures of F on (0, 1] (Taylor with tail bound), [1, 3] (grid of cells
    with Taylor-enclosed cos, sin and |G'| <= 6) and [3, oo) (envelope) exclude the drop for all x1 > 0.
"""
from fractions import Fraction as F
from GA import QI
from tp_premise import premise

I = QI(0, 1)


def lp(d):
    return {n: c for n, c in d.items() if c != QI(0)}


def deriv(expr):
    s, co = expr
    out = {}
    for n, c in co.items():
        out[n] = out.get(n, QI(0)) + c * QI(0, -s)      # d/dz E^s = -i s E^s
        if n:
            out[n + 1] = out.get(n + 1, QI(0)) + c * (-n)  # d/dz z^-n = -n z^-(n+1)
    return (s, lp(out))


def lmul(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            out[a + b] = out.get(a + b, QI(0)) + x * y
    return lp(out)


def ladd(p, q, cq=QI(1)):
    out = dict(p)
    for n, c in q.items():
        out[n] = out.get(n, QI(0)) + cq * c
    return lp(out)


def conj_expr(expr):
    s, co = expr
    return (-s, {n: c.conj() for n, c in co.items()})


def leval(co, z):
    return sum((c * (F(1) / z ** n) for n, c in co.items()), QI(0))


U = (1, {0: QI(1), 1: QI(0, -1)})
UB = conj_expr(U)


def check_mode_function_and_wronskian():
    premise("synthesis.frozen-phase-spectrum-not-red")
    premise("mass.de-sitter-scale-frozen-point")
    u1 = deriv(U)
    u2 = deriv(u1)
    # u'' + (1 - 2 z^-2) u = 0
    lhs = ladd(ladd(u2[1], U[1]), lmul({2: QI(-2)}, U[1]))
    assert u2[0] == U[0] and lhs == {}
    # Wronskian: E^1 * E^-1 = 1
    ub1 = deriv(UB)
    W = ladd(lmul(U[1], ub1[1]), lmul(u1[1], UB[1]), QI(-1))
    assert W == {0: QI(0, 2)}
    return True


def check_bogoliubov_normalisation():
    premise("synthesis.frozen-phase-spectrum-not-red")
    u1, ub1 = deriv(U), deriv(UB)
    # alpha = (f ubar' - f' ubar)/W, f = 1, f' = -i ; beta = (u f' - u' f)/W
    W = QI(0, 2)
    Acoef = {n: c / W for n, c in ladd(ub1[1], UB[1], QI(0, 1)).items()}     # times E^-1
    Bcoef = {n: c / W for n, c in ladd(lmul({0: QI(0, -1)}, U[1]), u1[1], QI(-1)).items()}  # times E
    assert Acoef == {0: QI(1), 1: QI(0, 1), 2: QI(F(-1, 2))}
    assert Bcoef == {2: QI(F(-1, 2))}
    # |alpha|^2 - |beta|^2 = 1 for real z: the E factors have modulus one and cancel
    A2 = lmul(Acoef, {n: c.conj() for n, c in Acoef.items()})
    B2 = lmul(Bcoef, {n: c.conj() for n, c in Bcoef.items()})
    assert ladd(A2, B2, QI(-1)) == {0: QI(1)}
    return True


def check_closed_form():
    premise("synthesis.frozen-phase-spectrum-not-red")
    circle = [(F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(8, 17), F(-15, 17)), (F(1), F(0)),
              (F(-7, 25), F(-24, 25))]
    for x in (F(1, 3), F(1), F(5, 2), F(7), F(40)):
        z = -x
        A = QI(1) + QI(0, 1) / z - QI(1) / (2 * z * z)
        B = F(1) / (2 * z * z)
        for C, S in circle:
            assert C * C + S * S == 1
            w = QI(C, S)                                   # e^{-2 i z_d} = e^{2ix}
            val = A + w * B                                # alpha - beta up to a unit factor
            Fdirect = (val * val.conj()).re
            Fclosed = 1 + F(1) / (2 * x ** 4) + (F(1) / x ** 2) * ((1 - F(1) / (2 * x * x)) * C - S / x)
            assert Fdirect == Fclosed
    return True


def check_small_x_blue():
    premise("synthesis.frozen-phase-spectrum-not-red")
    # Taylor series of x^4 F(x) = x^4 + 1/2 + (x^2 - 1/2) cos 2x - x sin 2x to order x^10
    N = 12
    fact = [F(1)]
    for n in range(1, N + 2):
        fact.append(fact[-1] * n)
    cos2 = [F(0)] * (N + 1)
    sin2 = [F(0)] * (N + 1)
    for n in range(N + 1):
        if n % 2 == 0:
            cos2[n] = F((-1) ** (n // 2) * 2 ** n) / fact[n]
        else:
            sin2[n] = F((-1) ** ((n - 1) // 2) * 2 ** n) / fact[n]
    ser = [F(0)] * (N + 1)
    ser[0] += F(1, 2)
    ser[4] += 1
    for n in range(N + 1):
        if n + 2 <= N:
            ser[n + 2] += cos2[n]
        ser[n] += -F(1, 2) * cos2[n]
        if n + 1 <= N:
            ser[n + 1] += -sin2[n]
    assert all(c == 0 for c in ser[:6])
    assert ser[6] == F(4, 9)                       # F(x) = (4/9) x^2 + O(x^4)
    assert ser[7] == 0 and ser[8] == F(-1, 15) and ser[10] == F(8, 1575)   # n_s - 1 -> +2 as x -> 0
    return True


def check_large_x_windows_not_red():
    premise("synthesis.frozen-phase-spectrum-not-red")
    # e^7 > 1096 from a partial sum of the exponential series (a lower bound)
    term = F(1)
    e7 = F(1)
    for n in range(1, 40):
        term = term * 7 / n
        e7 += term
    assert e7 > 1096
    # weakest red tilt in the 2-sigma band: 1 - n_s >= 0.0351 - 2 * 0.0042 = 0.0267
    d = F(351, 10000) - 2 * F(42, 10000)
    assert d == F(267, 10000)
    drop = 7 * d                                   # required ln F(x1) - ln F(x2)
    ebound = 1 + drop + drop * drop / 2            # <= e^drop
    # for x >= 3: F(x1) <= (1 + 1/(8 x1^4) + 1/(2 x1^2))^2 (sqrt(1+t) <= 1 + t/2), decreasing in x1;
    # F(x2) >= (1 - 1/(2 x2^2))^2 with x2 >= 1096 x1 >= 3288
    x1 = F(3)
    up = (1 + F(1) / (8 * x1 ** 4) + F(1) / (2 * x1 ** 2)) ** 2
    x2 = 1096 * x1
    lo = (1 - F(1) / (2 * x2 ** 2)) ** 2
    assert up / lo < ebound
    # and the bound is not slack at the cut: at x1 = 2 it would fail, so the cut matters
    x1b = F(2)
    upb = (1 + F(1) / (8 * x1b ** 4) + F(1) / (2 * x1b ** 2)) ** 2
    assert upb / lo > ebound
    # sanity of the envelope: |A|^2 = 1 + 1/(4 x^4) exactly
    for x in (F(3), F(10)):
        A = QI(1) - QI(0, 1) / x - QI(1) / (2 * x * x)
        assert (A * A.conj()).re == 1 + F(1) / (4 * x ** 4)
    return True


def _cos_sin_enclosure(y, N):
    """Rational enclosures of cos y and sin y for rational 0 <= y <= 8 from Taylor partial sums
    up to degree N, with the Lagrange bound |y|^(N+1)/(N+1)! on the remainder."""
    c, s, term = F(0), F(0), F(1)
    for n in range(0, N + 1):
        if n:
            term = term * y / n
        if n % 4 == 0:
            c += term
        elif n % 4 == 1:
            s += term
        elif n % 4 == 2:
            c -= term
        else:
            s -= term
    rem = term * y / (N + 1)
    return (c - rem, c + rem), (s - rem, s + rem)


# Inputs of (iv): windows of EFOLDS e-folds, the weakest 2-sigma red tilt 1 - n_s = 0.0267.
EFOLDS, TILT_2SIGMA = 7, F(267, 10000)
# Precision parameters of the enclosures (larger values also work): terms of the e^7 series, Taylor
# order on (0, 1], grid step and cell count on [1, 3], degree of the cos/sin enclosures.
E7_TERMS, TAYLOR_N = 40, 30
GRID_H, GRID_CELLS, TRIG_N = F(1, 100), 200, 40
# Points where F is enclosed independently (closed form with cos/sin enclosures) to test soundness.
SMALL_POINTS = [F(1, 2), F(1)]


def _F_point(x):
    """Enclosure (lo, hi) of F(x) = 1 + 1/(2x^4) + x^-2 [(1 - 1/(2x^2)) cos 2x - x^-1 sin 2x] at a
    rational 0 < x <= 4, from the closed form (3) and Taylor enclosures of cos 2x and sin 2x."""
    (clo, chi), (slo, shi) = _cos_sin_enclosure(2 * x, TRIG_N)
    coef = 1 - 1 / (2 * x * x)
    c_lo, c_hi = (coef * clo, coef * chi) if coef >= 0 else (coef * chi, coef * clo)
    base = 1 + 1 / (2 * x ** 4)
    return base + (c_lo - shi / x) / (x * x), base + (c_hi - slo / x) / (x * x)


def check_every_window_not_red():
    premise("synthesis.frozen-phase-spectrum-not-red")
    # required factor: F(x1)/F(x2) >= e^(7 * 0.0267) >= 1 + y + y^2/2 for a constant index in the
    # 2-sigma band, x2 = e^7 x1 >= 1096 x1. Show F(x1)/F(x2) < 1 + y + y^2/2 for every x1 > 0.
    y = EFOLDS * TILT_2SIGMA
    need = 1 + y + y * y / 2
    assert need == F(240873161, 200000000)          # by hand: 1 + 0.1869 + 0.1869^2/2 = 1.204365805
    term, e7 = F(1), F(1)
    for n in range(1, E7_TERMS):
        term = term * EFOLDS / n
        e7 += term
    ratio = int(e7)
    assert ratio == 1096                                                # e^7 = 1096.63: x2 > 1096 x1
    # (a) x in (0, 1]: F(x) = sum_{n >= 6} s_n x^(n-4), s_n the Taylor coefficients of x^4 F;
    # |s_n| <= 3 * 2^n/(n-2)!, so F(x) <= S x^2 and F(x) >= (4/9 - T) x^2 with S, T exact bounds
    N = TAYLOR_N
    fact = [F(1)]
    for n in range(1, N + 3):
        fact.append(fact[-1] * n)
    ser = [F(0)] * (N + 3)
    ser[0] += F(1, 2)
    ser[4] += 1
    for n in range(N + 1):
        cn = F((-1) ** (n // 2) * 2 ** n) / fact[n] if n % 2 == 0 else F(0)
        sn = F((-1) ** ((n - 1) // 2) * 2 ** n) / fact[n] if n % 2 == 1 else F(0)
        ser[n + 2] += cn
        ser[n] += -F(1, 2) * cn
        ser[n + 1] += -sn
    assert all(v == 0 for v in ser[:6]) and ser[6] == F(4, 9)
    # the coefficient bound, on the computed range; beyond N the ratio of bounds is 2/(n-1) <= 1/15,
    # so the tail is at most the first omitted bound times 15/14
    assert all(abs(ser[n]) <= 3 * F(2 ** n) / fact[n - 2] for n in range(6, N + 1))
    tail = 3 * F(2 ** (N + 1)) / fact[N - 1] * F(15, 14)
    S = sum((abs(v) for v in ser[6:N + 1]), F(0)) + tail
    T = sum((abs(v) for v in ser[7:N + 1]), F(0)) + tail
    assert S < F(53, 100) and F(4, 9) - T > F(37, 100)
    # soundness: the bounds bracket independent enclosures of F at sample points of (0, 1]
    for x in SMALL_POINTS:
        f_lo, f_hi = _F_point(x)
        assert (F(4, 9) - T) * x * x <= f_lo and f_hi <= S * x * x
    # (b) x in [1, 3]: grid x0 = 1 + j/100, G = (1 - 1/(2x^2)) cos 2x - sin(2x)/x, |G'| <= 6 there,
    # F = 1 + 1/(2x^4) + G/x^2; enclose F on each cell [x0, x0 + h]
    h = GRID_H
    assert 1 + GRID_CELLS * h == 3                                      # the cells cover [1, 3]
    Fmax, Fmin = F(0), F(10)
    for j in range(GRID_CELLS):
        x0 = 1 + j * h
        (clo, chi), (slo, shi) = _cos_sin_enclosure(2 * x0, TRIG_N)
        coef = 1 - 1 / (2 * x0 * x0)
        g_hi = coef * chi - slo / x0 + 6 * h
        g_lo = coef * clo - shi / x0 - 6 * h
        up = 1 + 1 / (2 * x0 ** 4) + (g_hi / (x0 * x0) if g_hi >= 0 else g_hi / ((x0 + h) ** 2))
        lo = 1 + 1 / (2 * (x0 + h) ** 4) + (g_lo / (x0 * x0) if g_lo < 0 else g_lo / ((x0 + h) ** 2))
        # soundness: the cell enclosure contains the independent enclosures of F at both cell ends
        for xe in (x0, x0 + h):
            f_lo, f_hi = _F_point(xe)
            assert lo <= f_lo and f_hi <= up
        Fmax, Fmin = max(Fmax, up), min(Fmin, lo)
    assert Fmax < F(116, 100) and Fmin > F(30, 100)
    # (c) x >= 3: (1 - 1/(2x^2))^2 <= F <= (1 + 1/(8x^4) + 1/(2x^2))^2
    hi3 = (1 + F(1, 8 * 81) + F(1, 18)) ** 2
    lo3 = (1 - F(1, 18)) ** 2
    f_lo, f_hi = _F_point(F(3))
    assert lo3 <= f_lo and f_hi <= hi3                                   # the envelope at x = 3
    lo_far = (1 - F(1, 2 * ratio ** 2)) ** 2                            # x2 >= 1096
    # windows: x1 >= 1 (x2 >= 1096): F(x1) <= max(Fmax, hi3)
    assert max(Fmax, hi3) / lo_far < need
    # x1 in (0, 1] with x2 >= 3: F(x1) <= S
    assert S / lo3 < need
    # x1 in (0, 1] with x2 in [1, 3]: x1 <= 3/1096, F(x1) <= S x1^2, F(x2) >= Fmin
    assert S * F(3, ratio) ** 2 / Fmin < need
    # x1, x2 both in (0, 1]: F(x1)/F(x2) <= S x1^2 / ((4/9 - T) x2^2) <= S / ((4/9 - T) 1096^2)
    assert S / ((F(4, 9) - T) * ratio ** 2) < need
    # the margin is real: a much weaker required tilt would not be excluded at the maximum
    assert Fmax / lo_far > 1 + F(1, 10)
    return True
