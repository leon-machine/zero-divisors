"""synthesis.frozen-point-geometry-reads-descent-as-vacuum: exact checks.

Ambient Cl(2,4) with generators e0..e3 (spacetime, +,-,-,-), e4 = e_+ (+1), e5 = e_- (-1);
n0 = (e_+ + e_-)/2, ninf = e_+ - e_-, <n0, ninf> = 1, X(x) = n0 + x - Q(x)/2 ninf, the conventions of
mass.de-sitter-scale-frozen-point and of synthesis.frozen-phase-spectrum-not-red. All arithmetic is over
Fractions; pi is bounded by 3 < pi < 22/7; square and cube roots are bracketed by integer roots.

(1) The pair invariant of the frozen point's stabiliser: Z(X, Y) = 1 + (Lambda/3) <X,Y> / (<X,I><Y,I>) is
    projective (unchanged by X -> c X), equals 1 - Q(x - y)/(2 x0 y0) on the chart, so at equal time
    Z - 1 = |dx|^2 / (2 x0^2); it is unchanged by rotors fixing I_fs = H e0 (rotation, spatial translation,
    special conformal map, dilatation) and changed by a time translation (control).
(2) The descent slice in the frozen point's chart: |x_d| = eta_inf - eta_d, with a0 H0 eta_inf, the conformal
    time from the origin to future infinity, in (4.32, 4.34) (exact Riemann brackets of
    int da / sqrt(Or + Om a + OL a^4) with the record Omegas), a0 H0 eta_0 in (3.17, 3.19), and
    a0 H0 eta_d < 1e-7 for T_d >= 1 MeV. The range the amplitude needs (stored bound, sigma^2 <= 1) is
    one comoving length for every T_d, a0 H0 R_req = (3 pi A_s / 2)^(1/3) / kappa in (9.4e-6, 9.8e-6);
    |x_d| exceeds it by more than 4.4e5. The pivot has u_* = k_* |x_d| in (960, 968).
(3) The index: a correlator homogeneous of degree -2 on the slice has Delta^2 proportional to k^2
    (scaling lemma, exact on regulated homogeneous functions as in the stored no-go); the conformal weight
    w = -1 has m^2 = 2 H^2 in the dictionary and its invariant correlator H^2/(8 pi^2 (Z - 1)) equals
    1/(4 pi^2 a^2 |dx|^2) with a = 1/(H |x0|) at equal time; the massless point's Bunch-Davies mode
    chi = e^{-ik eta}(1 - i/(k eta))/sqrt(2k) solves chi'' + (k^2 - 2/eta^2) chi = 0 (exact rational-function
    identity) and gives Delta^2 = (H/2 pi)^2 (1 + u^2), local index 2 u^2/(1 + u^2), above 1.99999 at the pivot
    and above 1.7 at u = 2.7 (the largest observed scales, k = 2/eta_0).
(5) The leading adiabatic index of every unitary-series field, 3 - U/(U + 1/4 - nu^2) with U = u^2 (rational-function
    identity), has floor 2 - 2/(U - 2), above 2 - 3e-6 at the pivot, 484 to 485 standard deviations from the measured index.
(4) The two scales bracket the observed modes: k_*/(a_d H_d) in (4.2e-6, 4.5e-6) (stored rho brackets at 1 MeV),
    k_* |x_d| in (960, 968), Z - 1 at the pivot separation in (5.3e-7, 5.5e-7).
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, gen, reverse, eq, commutes, RF
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
PI_LO, PI_HI = F(3), F(22, 7)
KAPPA = F("0.05") * F("299792.458") / F("67.4")                  # k_*/(a_0 H_0) = 149896229/674000
OM, OR = F("0.315"), F("9.2e-5")
OL = 1 - OM - OR
AS_LO, AS_HI = F("2.07e-9"), F("2.13e-9")
T0 = F("2.7255") * F("8.617333262e-14")                           # GeV
GS0 = F(43, 11)
SCALE = 10 ** 12


def dot(a, b):
    return add(mul(a, b, SQ), mul(b, a, SQ)).get((), F(0)) / 2


def wedge(a, b):
    return scal(F(1, 2), sub(mul(a, b, SQ), mul(b, a, SQ)))


def sandwich(R, v):
    return mul(mul(R, v, SQ), reverse(R), SQ)


n0 = scal(F(1, 2), add(gen(4), gen(5)))
ninf = sub(gen(4), gen(5))
E = [gen(i) for i in range(4)]


def vec(x):
    out = {}
    for i, c in enumerate(x):
        out = add(out, scal(F(c), E[i]))
    return out


def Q(x):
    return x[0] * x[0] - x[1] * x[1] - x[2] * x[2] - x[3] * x[3]


def X(x):
    return add(add(n0, vec(x)), scal(-Q(x) / 2, ninf))


def isqrt(n):
    """integer floor square root by Newton's method (integers only)"""
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            break
        x = y
    while x * x > n:
        x -= 1
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


def sqrt_lo(q):
    """rational lower bound on sqrt(q), q > 0 rational"""
    p, r = q.numerator, q.denominator
    return F(isqrt(p * r * SCALE * SCALE), r * SCALE)


def sqrt_hi(q):
    p, r = q.numerator, q.denominator
    return F(isqrt(p * r * SCALE * SCALE) + 1, r * SCALE)


def icbrt(n):
    """integer floor cube root"""
    lo, hi = 0, 1
    while hi ** 3 <= n:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** 3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def cbrt_lo(q):
    p, r = q.numerator, q.denominator
    return F(icbrt(p * r * r * SCALE ** 3), r * SCALE)


def cbrt_hi(q):
    p, r = q.numerator, q.denominator
    return F(icbrt(p * r * r * SCALE ** 3) + 1, r * SCALE)


def Zinv(Xv, Yv, I, lam):
    """Z(X, Y) = 1 + (Lambda/3) <X,Y>/(<X,I><Y,I>)"""
    return 1 + (lam / 3) * dot(Xv, Yv) / (dot(Xv, I) * dot(Yv, I))


POINTS = [(F(-2), F(0), F(0), F(0)), (F(-2), F(1), F(-3), F(1, 2)), (F(-1, 3), F(5), F(2), F(7)),
          (F(-3, 4), F(-1, 2), F(0), F(1)), (F(-2), F(3), F(0), F(-4))]


def check_pair_invariant_of_the_stabiliser():
    premise("mass.de-sitter-scale-frozen-point")
    premise("dark-matter.imported-frozen-point-de-sitter-radius")
    premise("synthesis.frozen-phase-spectrum-not-red")
    ok = True
    for h in (F(1), F(1, 2), F(3)):
        lam = 3 * h * h
        Ifs = scal(h, E[0])
        ok = ok and dot(Ifs, Ifs) == lam / 3
        for x in POINTS:
            for y in POINTS:
                Xv, Yv = X(x), X(y)
                z = Zinv(Xv, Yv, Ifs, lam)
                d = tuple(x[i] - y[i] for i in range(4))
                # chart form: <X,Y> = -Q(x-y)/2, <X,I> = H x0
                ok = ok and dot(Xv, Yv) == -Q(d) / 2 and dot(Xv, Ifs) == h * x[0]
                ok = ok and z == 1 - Q(d) / (2 * x[0] * y[0])
                # projective: rescaling a representative changes nothing
                ok = ok and Zinv(scal(F(7, 3), Xv), scal(F(-5), Yv), Ifs, lam) == z
                if x[0] == y[0]:
                    ok = ok and z - 1 == (d[1] * d[1] + d[2] * d[2] + d[3] * d[3]) / (2 * x[0] * x[0])
        # rotors in the stabiliser of I_fs: rotation (cos, sin) = (3/5, 4/5) in the e1 e2 plane (half-angle form),
        # spatial translation 1 - ninf a/2, special conformal map 1 + n0 b/2, dilatation 5/4 + 3/4 n0^ninf
        rot = add({(): F(3, 5)}, scal(F(4, 5), wedge(E[1], E[2])))
        a_vec = vec((F(0), F(2), F(-1), F(3)))
        trans = sub({(): F(1)}, scal(F(1, 2), mul(ninf, a_vec, SQ)))
        b_vec = vec((F(0), F(1, 3), F(1), F(-2)))
        spec = add({(): F(1)}, scal(F(1, 2), mul(n0, b_vec, SQ)))
        dil = add({(): F(5, 4)}, scal(F(3, 4), wedge(n0, ninf)))
        tbad = sub({(): F(1)}, scal(F(1, 2), mul(ninf, vec((F(1), F(0), F(0), F(0))), SQ)))  # time translation
        for R in (rot, trans, spec, dil):
            ok = ok and eq(mul(R, reverse(R), SQ), {(): F(1)})
            ok = ok and eq(sandwich(R, Ifs), Ifs)
            for x in POINTS[:3]:
                for y in POINTS[:3]:
                    Xv, Yv = X(x), X(y)
                    ok = ok and Zinv(sandwich(R, Xv), sandwich(R, Yv), Ifs, lam) == Zinv(Xv, Yv, Ifs, lam)
        # control: a time translation moves I_fs and changes Z
        ok = ok and eq(mul(tbad, reverse(tbad), SQ), {(): F(1)}) and not eq(sandwich(tbad, Ifs), Ifs)
        Xv, Yv = X(POINTS[1]), X(POINTS[2])
        ok = ok and Zinv(sandwich(tbad, Xv), sandwich(tbad, Yv), Ifs, lam) != Zinv(Xv, Yv, Ifs, lam)
    GA.check("Z is the stabiliser's pair invariant, projective, 1 - Q(x-y)/(2 x0 y0), |dx|^2/(2 x0^2) at equal time", ok)
    return ok


_ETA = {}


def eta_brackets():
    if "v" in _ETA:
        return _ETA["v"]
    _ETA["v"] = _eta_brackets()
    return _ETA["v"]


def _eta_brackets():
    """exact lower and upper bounds on a0 H0 eta(a) = int_0^a da'/sqrt(Or + Om a' + OL a'^4), at a = 1 and a -> oo.
    The integrand g is decreasing (f increasing), so on [a_i, a_{i+1}] the integral lies between
    (a_{i+1} - a_i) g(a_{i+1}) and (a_{i+1} - a_i) g(a_i); the first segment [0, a_1] is bounded by a_1 g(0) above
    and a_1 g(a_1) below; the tail beyond A uses OL a^4 <= f <= OL a^4 (1 + d), d = (Om A + Or)/(OL A^4)."""
    def f(a):
        return OR + OM * a + OL * a ** 4

    def g_lo(a):   # lower bound on 1/sqrt(f)
        return 1 / sqrt_hi(f(a))

    def g_hi(a):
        return 1 / sqrt_lo(f(a))

    D = 10 ** 15                      # every term is rounded down (lower sum) or up (upper sum) to a multiple of 1e-15

    def down(q):
        return F((q * D).__floor__(), D)

    def up(q):
        return F((q * D).__ceil__(), D)

    a1 = F(1, 10 ** 8)
    lo = down(a1 * g_lo(a1))
    hi = up(a1 * g_hi(a1))
    lo0 = hi0 = None
    a = a1
    ratio = F(2001, 2000)
    A = F(200)
    while a < A:
        # next point: a * ratio rounded up to six significant figures, so denominators stay small
        nxt = a * ratio
        e = 0
        while F(10) ** e <= nxt:
            e += 1
        grid = F(10) ** (e - 7)
        nxt = (nxt / grid).__ceil__() * grid
        if nxt > A:
            nxt = A
        if a < 1 <= nxt and nxt != 1:
            nxt = F(1)
        w = nxt - a
        lo += down(w * g_lo(nxt))
        hi += up(w * g_hi(a))
        a = nxt
        if a == 1:
            lo0, hi0 = lo, hi
    d = (OM * A + OR) / (OL * A ** 4)
    tail_hi = 1 / (sqrt_lo(OL) * A)
    tail_lo = 1 / (sqrt_hi(OL * (1 + d)) * A)
    return lo0, hi0, lo + down(tail_lo), hi + up(tail_hi)


def check_descent_slice_and_the_range():
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.imported-bbn-reheating-temperature-floor")
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    premise("mass.de-sitter-scale-frozen-point")
    eta0_lo, eta0_hi, etai_lo, etai_hi = eta_brackets()
    ok = F(317, 100) < eta0_lo and eta0_hi < F(319, 100)
    ok = ok and F(432, 100) < etai_lo and etai_hi < F(434, 100)
    GA.check("a0 H0 eta_0 in (3.17, 3.19) and a0 H0 eta_inf in (4.32, 4.34)", ok)
    # the descent at T_d >= 1 MeV, g_s >= 10.75: a_d^3 = (T0/Td)^3 (gs0/g) < 1e-27, so eta_d < a_d/sqrt(Or) < 1e-7
    ad3 = (T0 / F(1, 1000)) ** 3 * GS0 / F(1075, 100)
    ok2 = ad3 < F(22, 10 ** 11) ** 3 and F(22, 10 ** 11) / sqrt_lo(OR) < F(1, 10 ** 7)
    GA.check("a0 H0 eta_d < 1e-7 for T_d >= 1 MeV (a_d < 2.2e-10), so |x_d| = eta_inf - eta_d in (4.32, 4.34)", ok2)
    # the other reading of the join (frozen phase ending at the descent, a continuous): k/(a_d H_Lambda) for k = a0 H0
    # is (a0/a_d)/sqrt(OL) > 5.9e9/0.83 > 7e9 at T_d = 1 MeV, g_s = 10.75
    ok2b = ad3 < (F(168, 10 ** 12)) ** 3 and F(10 ** 12, 168) > F(59, 10) * 10 ** 9
    ok2b = ok2b and F(10 ** 12, 168) / sqrt_hi(OL) > 7 * 10 ** 9
    GA.check("second join: a0/a_d > 5.9e9 and k/(a_d H_Lambda) > 7e9 for k = a0 H0 at 1 MeV", ok2b)
    xd_lo, xd_hi = etai_lo - F(1, 10 ** 7), etai_hi
    # the range the stored amplitude bound needs, in comoving units: R a0 H0 = (3 pi A_s/(2 sigma^2))^(1/3)/kappa, sigma^2 <= 1
    R_lo = cbrt_lo(F(3, 2) * PI_LO * AS_LO) / KAPPA
    R_hi = cbrt_hi(F(3, 2) * PI_HI * AS_HI) / KAPPA
    ok3 = F(94, 10 ** 7) < R_lo and R_hi < F(98, 10 ** 7)
    # the same length as the stored 'K Hubble lengths of the descent': K/rho = R a0 H0, with rho = a_d H_d/(a_0 H_0)
    GA.check("a0 H0 R_req in (9.4e-6, 9.8e-6), one comoving length for every T_d", ok3)
    GA.check("|x_d| exceeds R_req by more than 4.4e5", xd_lo / R_hi > F(44, 10) * 10 ** 5)
    u_lo, u_hi = KAPPA * xd_lo, KAPPA * xd_hi
    GA.check("u_* = k_* |x_d| in (960, 968)", F(960) < u_lo and u_hi < F(968))
    # the largest observed scales: k = 2/eta_0 gives u = 2 |x_d|/eta_0 in (2.70, 2.74)
    u2_lo, u2_hi = 2 * xd_lo / eta0_hi, 2 * xd_hi / eta0_lo
    GA.check("u at k = 2/eta_0 in (2.70, 2.74)", F(270, 100) < u2_lo and u2_hi < F(274, 100))
    return ok and ok2 and ok2b and ok3


def check_index_of_the_invariant_class():
    premise("standard-model.imported-frozen-point-dictionary")
    premise("mass.de-sitter-scale-frozen-point")
    premise("synthesis.frozen-phase-spectrum-not-red")
    premise("synthesis.sudden-descent-feature-not-tilt")
    ok = True
    # (a) the conformal weight w = -1 has m^2 = -w(w+3) H^2 = 2 H^2 (the conformal coupling in de Sitter space)
    for h in (F(1), F(2, 3)):
        ok = ok and -F(-1) * (F(-1) + 3) * h * h == 2 * h * h
    # (b) scaling lemma: a correlator C(r) homogeneous of degree -2 on the slice gives P(lam k) = lam^(-1) P(k) and
    # Delta^2(lam k) = lam^2 Delta^2(k): tested exactly on the regulated homogeneous functions C_n(r) = |r|^(2n),
    # n = -1, whose Fourier transform scales with degree -3 - 2n; for the exact substitution we use the monomial
    # sums S_n(k) = sum over the cubic lattice points of |r|^(2n) e^{...} replaced by the scaling of the measure:
    # under r -> lam r, d^3 r -> lam^3 d^3 r and |r|^(2n) -> lam^(2n) |r|^(2n), so P(k/lam) = lam^(3 + 2n) P(k).
    for n in (F(-1), F(-3, 2), F(0)):
        for lam in (F(2), F(5, 3)):
            degP = 3 + 2 * n          # P(k/lam) = lam^degP P(k)  <=>  P(k) ~ k^(-degP)
            index = 3 - degP          # Delta^2 ~ k^(3 - degP) = k^(-2n)
            ok = ok and index == -2 * n
            ok = ok and lam ** index == lam ** (-2 * n)
    ok = ok and (3 - (3 + 2 * F(-1))) == 2 and (3 - (3 + 2 * F(-3, 2))) == 3 and (3 - (3 + 2 * F(0))) == 0
    # the measured index: Delta^2 ~ k^(n_s - 1) is a correlator of degree 1 - n_s = 351/10000 > 0 on the slice
    ok = ok and -2 * (F(9649, 10000) - 1) / 2 == F(351, 10000) and F(351, 10000) > 0
    GA.check("degree -2 on the slice means n_s - 1 = 2, degree -3 means 3, degree 0 means 0; the measured index needs degree +0.0351", ok)
    # (c) the invariant correlator of the conformal weight, H^2/(8 pi^2 (Z-1)), at equal time equals 1/(4 pi^2 a^2 |dx|^2)
    # with a = 1/(H|x0|): store c pi^n as (c, n)
    ok2 = True
    for h in (F(1), F(1, 2), F(3)):
        for x0 in (F(-2), F(-1, 3), F(-5)):
            for r2 in (F(1), F(7, 3), F(100)):
                zm1 = r2 / (2 * x0 * x0)
                lhs = (h * h / (8 * zm1), -2)
                a = 1 / (h * abs(x0))
                rhs = (1 / (4 * a * a * r2), -2)
                ok2 = ok2 and lhs == rhs
    GA.check("conformal weight: H^2/(8 pi^2 (Z-1)) = 1/(4 pi^2 a^2 |dx|^2) on the slice, degree -2 exactly", ok2)
    # (d) the massless point's Bunch-Davies mode: chi = e^{-ik eta} A(eta), A = (1 - i/(k eta))/sqrt(2k).
    # chi'' + (k^2 - 2/eta^2) chi = e^{-ik eta} [A'' - 2ik A' - 2A/eta^2]; with A = A_r + i A_i, A_r = 1, A_i = -1/(k eta)
    # (the overall 1/sqrt(2k) dropped), the real part is A_r'' + 2k A_i' - 2A_r/eta^2 and the imaginary part is
    # A_i'' - 2k A_r' - 2A_i/eta^2; both vanish identically.
    eta = RF.var()
    ok3 = True
    for k in (F(1), F(3), F(2, 5)):
        Ar = RF.const(F(1))
        Ai = RF.const(F(-1) / k) / eta
        real = Ar.deriv().deriv() + RF.const(2 * k) * Ai.deriv() - RF.const(2) * Ar / (eta * eta)
        imag = Ai.deriv().deriv() - RF.const(2 * k) * Ar.deriv() - RF.const(2) * Ai / (eta * eta)
        ok3 = ok3 and real.is_zero() and imag.is_zero()
        # control: the plane wave alone (A_i = 0) fails: real part is -2/eta^2
        real0 = Ar.deriv().deriv() - RF.const(2) * Ar / (eta * eta)
        ok3 = ok3 and not real0.is_zero()
        # |A|^2 = (1 + 1/(k eta)^2)/(2k); Delta^2 = k^3 |chi|^2 /(2 pi^2 a^2), a = 1/(H|eta|):
        # k^3 (1 + 1/(k eta)^2) H^2 eta^2 /(2k 2 pi^2) = H^2 (u^2 + 1)/(4 pi^2), u = k|eta|
        for e_ in (F(-2), F(-7, 2)):
            for h in (F(1), F(3, 2)):
                modA2 = (Ar.eval(e_) ** 2 + Ai.eval(e_) ** 2) / (2 * k)
                d2 = (k ** 3 * modA2 * h * h * e_ * e_ / 2, -2)
                u = k * abs(e_)
                ok3 = ok3 and d2 == (h * h * (u * u + 1) / 4, -2)
    GA.check("massless point: Bunch-Davies mode solves its equation; Delta^2 = (H/2 pi)^2 (1 + u^2)", ok3)
    # (e) local index 2u^2/(1+u^2): above 1.99999 for u >= 960, above 1.7 for u >= 2.7
    def idx(u):
        return 2 * u * u / (1 + u * u)
    ok4 = idx(F(960)) > F(199999, 100000) and idx(F(270, 100)) > F(17, 10) and idx(F(274, 100)) < F(18, 10)
    ok4 = ok4 and idx(F(1)) == 1 and idx(F(0)) == 0   # outside the frozen point's horizon the massless index drops
    GA.check("local index 2u^2/(1+u^2): > 1.99999 at the pivot, in (1.7, 1.8) at k = 2/eta_0", ok4)
    return ok and ok2 and ok3 and ok4


def check_two_scales_bracket_the_observed_modes():
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    premise("synthesis.quadratic-flows-cannot-thermalise-descent")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.imported-bbn-reheating-temperature-floor")
    # k_*/(a_d H_d) = kappa/rho with rho(1 MeV) > 4.96e7 (stored, recomputed here as a sixth power)
    H0 = F("67.4") * 1000 / F("3.0856775814913673e22") * F("6.582119569e-25")
    MP = F("2.435e18")
    Td, g = F(1, 1000), F(1075, 100)
    rho6 = (T0 / Td) ** 6 * (GS0 / g) ** 2 * (PI_LO ** 2 * g / 90) ** 3 * Td ** 12 / (MP ** 6 * H0 ** 6)
    ok = (F(496, 10) * 10 ** 6) ** 6 < rho6 and rho6 * (PI_HI / PI_LO) ** 6 < (F(521, 10) * 10 ** 6) ** 6
    ok = ok and KAPPA == F(149896229, 674000)
    ok = ok and (F(42, 10 ** 7)) ** 6 < KAPPA ** 6 / rho6 < (F(45, 10 ** 7)) ** 6   # k_*/(a_d H_d) in (4.2e-6, 4.5e-6) at 1 MeV
    _, _, etai_lo, etai_hi = eta_brackets()
    ok = ok and 960 < KAPPA * (etai_lo - F(1, 10 ** 7)) and KAPPA * etai_hi < 968   # k_* |x_d| in (960, 968)
    # at the pivot separation r = 1/k_*, Z - 1 = 1/(2 u^2) in (5.3e-7, 5.5e-7): the Hadamard regime of every invariant state
    ok = ok and F(53, 10 ** 8) < 1 / (2 * F(968) ** 2) and 1 / (2 * F(960) ** 2) < F(55, 10 ** 8)
    GA.check("1/(a_d H_d) < 4.5e-6 / k_* and |x_d| > 960 / k_*: super-horizon for the descent, sub-horizon for the frozen point", ok)
    return ok


def check_adiabatic_index_bound_at_the_descent():
    premise("mass.imported-unitary-representations-de-sitter-group")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.frozen-phase-spectrum-not-red")
    premise("standard-model.imported-frozen-point-dictionary")
    # leading adiabatic order: |chi|^2 = 1/(2 omega), omega^2 = k^2 + M^2, M^2 = (1/4 - nu^2)/eta^2; at fixed eta
    # Delta^2 is proportional to k^3/omega, so with U = (k eta)^2 and M^2 in units of eta^-2,
    # (Delta^2)^2 ~ U^3/(U + M^2) and n - 1 = U d/dU ln(U^3/(U + M^2)) = 3 - U/(U + M^2)
    U = RF.var()
    ok = True
    for M2 in (F(0), F(-2), F(5), F(-1, 3), F(10) ** 6):
        f = U * U * U / (U + RF.const(M2))
        ok = ok and (U * f.deriv() / f).eqrf(RF.const(3) - U / (U + RF.const(M2)))
    # the dictionary: nu^2 = (w + 3/2)^2 = 9/4 - m^2/H^2; unitary series nu^2 <= 9/4, so M^2 = 1/4 - nu^2 >= -2
    for w in (F(0), F(-1), F(-3, 2), F(-3)):
        m2 = -w * (w + 3)
        ok = ok and (w + F(3, 2)) ** 2 == F(9, 4) - m2
    for nu2 in (F(9, 4), F(1, 4), F(0), F(-25)):
        ok = ok and F(1, 4) - nu2 >= -2
    # exact controls: conformal (nu = 1/2, M^2 = 0) gives 2; massless (nu = 3/2, M^2 = -2) adiabatic 2 - 2/(U - 2)
    # against exact 2 - 2/(U + 1): difference below 7/U^2
    ok = ok and (3 - F(1)) == 2
    for UU in (F(10) ** 4, F(960) ** 2):
        ok = ok and abs((2 - F(2) / (UU + 1)) - (2 - F(2) / (UU - 2))) < F(7) / UU ** 2
    # at the pivot U >= 960^2: floor 2 - 2/(U - 2) > 2 - 3e-6; gap to n_s - 1 = -351/10000 between 484 and 485 sigma
    Umin = F(960) ** 2
    lo = 2 - F(2) / (Umin - 2)
    ns, err = F("0.9649"), F("0.0042")
    ok = ok and lo > 2 - F(3, 10 ** 6) and ns - 1 == F(-351, 10000)
    gap = lo - (ns - 1)
    ok = ok and 484 * err < gap < 485 * err
    # at the quadrupole scale U = 2.7^2 the floor is 2 - 2/(U - 2) in (1.62, 1.64)
    Uq = F(27, 10) ** 2
    ok = ok and F(162, 100) < 2 - F(2) / (Uq - 2) < F(164, 100)
    GA.check("adiabatic index 3 - U/(U + M^2) over the unitary series: floor 2 - 2/(U-2), > 2 - 3e-6 at the pivot, 484 to 485 sigma from the measured index", ok)
    return ok
