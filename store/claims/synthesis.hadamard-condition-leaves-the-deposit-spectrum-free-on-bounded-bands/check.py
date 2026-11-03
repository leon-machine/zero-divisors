"""synthesis.hadamard-condition-leaves-the-deposit-spectrum-free-on-bounded-bands: exact checks.

Conformally coupled scalar (weight w = -1 of the dictionary, m^2 = 2 H^2) on the frozen point's field in its
flat slicing, a = -1/(H eta); chi = a phi. Complex numbers are Gaussian rationals (GA.QI), read as
a + b I4 in the spacetime algebra Cl(1,3) (the series' unit i = I4); e^{-ik eta} is sampled at rational
points of the unit circle and sqrt(2k) is kept rational by taking 2k a rational square.
Homogeneous quasi-free data relative to the conformal vacuum chi_k = e^{-ik eta}/sqrt(2k): occupation
n_k >= 0 and pair term c_k with |c_k|^2 <= n_k (n_k + 1); pure states u = alpha chi + beta chi-bar.

(1) The mode equation: for w = -1 the dictionary's m^2 a^2 cancels a''/a exactly (the massless point
    w = 0 keeps -2/eta^2, the control); I4^2 = -1 and QI multiplication is the span{1, I4} product.
(2) Bogoliubov data alpha = (q + 1/q)/2, beta = +-(q - 1/q)/2 w^2 keep the Wronskian (|alpha|^2 - |beta|^2 = 1)
    and give the slice ratio rho = Delta^2_omega/Delta^2_0 = q^2 (aligned) or 1/q^2 (opposed), for every
    rational q > 0 sampled on a band: every positive square ratio is reached exactly.
(3) The price of a ratio: rho = 1 + 2n + 2 Re(c w) obeys 4 n rho >= (rho - 1)^2 for every admissible (n, c, w),
    with equality for the pure aligned data; so n >= (sqrt rho - 1/sqrt rho)^2/4.
(4) The conformal energy |u'|^2 + k^2 |u|^2 has no cross term: chi'^2 + k^2 chi^2 = 0 exactly, so the energy
    difference has Fourier weight 2 k n_k >= 0 (pure: 2k|beta|^2). Control: the massless point's
    Bunch-Davies mode has chi'^2 + k^2 chi^2 = (k/2)(2/z^2 - 2i/z^3 - 1/z^4) e^{-2iz} != 0.
(5) A band's difference kernel is regular: int_{k1}^{k2} k sin(kr)/(kr) dk = (cos k1 r - cos k2 r)/r^2,
    exact Taylor coefficients in r^2 up to r^24, value (k2^2 - k1^2)/2 at r = 0, no r^-2 term.
(6) The ultraviolet end: for a ratio law rho = k^q on all k >= 1 the lower bound on n_k makes the energy
    moment int k^3 n_k dk grow without bound over shells [b^j, b^(j+1)], b = 2^10000, for
    q = -20351/10000 (the store's target law n_k ~ k^(n_s - 3) at n_s = 0.9649), q = -1, q = 1/2, and for a
    constant occupation (the dilatation-invariant case); a shell-supported occupation gives a finite moment.
(7) The infrared end: int_eps^1 k^(s - 1) dk = (1 - eps^s)/s at eps = 2^(-10000 m) grows without bound for
    s = -351/10000 (the red law) and over dyadic shells for s = 0; for the vacuum's s = 2 it stays below 1/2;
    the blue law rho = 1/k on (0, 1] is realised by pure data with finite moments 1/12 and 1/6.
(6') A constant ratio C != 1 (q = 0) fails the energy moment as well.
"""
from fractions import Fraction as F

import GA
from GA import QI
from tp_premise import premise

S13 = (1, -1, -1, -1)
CIRCLE = [(F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(8, 17), F(-15, 17)), (F(1), F(0)),
          (F(-7, 25), F(-24, 25)), (F(20, 29), F(21, 29))]
QS = [F(1, 3), F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(5), F(41, 7), F(1000)]
TWO_K_ROOTS = [F(1), F(2), F(3, 5), F(7)]          # sqrt(2k): 2k = s^2


def absq(z):
    return z.re * z.re + z.im * z.im


def _one(c):
    return GA.sc(c)


def check_conformal_mode_equation_and_complex_unit():
    premise("standard-model.imported-frozen-point-dictionary")
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    # i = I4 in Cl(1,3): I4^2 = -1 and (a + b I4)(c + d I4) matches the QI product
    E = [GA.gen(i) for i in range(4)]
    I4 = GA.mul(GA.mul(E[0], E[1], S13), GA.mul(E[2], E[3], S13), S13)
    assert GA.eq(GA.mul(I4, I4, S13), _one(-1))
    for (c1, s1) in CIRCLE[:3]:
        for (c2, s2) in CIRCLE[3:]:
            z1, z2 = QI(c1, s1), QI(c2, s2)
            lhs = GA.mul(GA.add(_one(c1), GA.scal(s1, I4)), GA.add(_one(c2), GA.scal(s2, I4)), S13)
            p = z1 * z2
            assert GA.eq(lhs, GA.add(_one(p.re), GA.scal(p.im, I4)))
    # chi'' + (k^2 + m^2 a^2 - a''/a) chi = 0 with a = -1/(H eta): a''/a = 2/eta^2;
    # dictionary m^2 = -w (w + 3) H^2: w = -1 gives m^2 a^2 = 2/eta^2, so the potential cancels exactly
    for H in (F(1), F(3, 7), F(5)):
        for eta in (F(-1), F(-2, 9), F(-13, 4)):
            a = -1 / (H * eta)
            app_over_a = F(2) / eta ** 2                    # (-1/(H eta))'' / a
            for w, expect_zero in ((-1, True), (0, False)):
                m2 = -w * (w + 3) * H * H
                pot = m2 * a * a - app_over_a
                assert (pot == 0) == expect_zero
                if w == 0:
                    assert pot == -F(2) / eta ** 2
    # chi = w/sqrt(2k) with w = e^{-ik eta}: chi'' = -k^2 chi
    for s in TWO_K_ROOTS:
        k = s * s / 2
        for (c, sn) in CIRCLE:
            chi = QI(c, sn) / s
            chi1 = QI(0, -k) * chi
            chi2 = QI(0, -k) * chi1
            assert chi2 + k * k * chi == QI(0)
    return True


def bogo(q, aligned, w):
    C = (q + 1 / q) / 2
    S = (q - 1 / q) / 2
    alpha = QI(C)
    beta = (QI(S) if aligned else QI(-S)) * w * w
    return alpha, beta


def check_every_positive_ratio_is_reached_on_a_band():
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    premise("synthesis.imported-de-sitter-invariant-hadamard-state-unique")
    for s in TWO_K_ROOTS:
        k = s * s / 2
        for (c, sn) in CIRCLE:
            w = QI(c, sn)                                   # e^{-ik eta_d}
            chi = w / s
            chib = w.conj() / s
            chi1 = QI(0, -k) * chi
            chib1 = QI(0, k) * chib
            W0 = chi * chib1 - chi1 * chib                  # Wronskian of the vacuum mode: i
            assert W0 == QI(0, 1)
            for q in QS:
                for aligned in (True, False):
                    alpha, beta = bogo(q, aligned, w)
                    assert absq(alpha) - absq(beta) == 1
                    u = alpha * chi + beta * chib
                    ub = alpha.conj() * chib + beta.conj() * chi
                    u1 = alpha * chi1 + beta * chib1
                    ub1 = alpha.conj() * chib1 + beta.conj() * chi1
                    assert u * ub1 - u1 * ub == QI(0, 1)    # the commutator is untouched
                    rho = absq(u) / absq(chi)                # Delta^2_omega / Delta^2_0 on the slice
                    assert rho == (q * q if aligned else 1 / (q * q))
                    assert absq(beta) == ((q - 1 / q) / 2) ** 2
    return True


def check_price_of_a_ratio():
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    samples = 0
    for n in (F(0), F(1, 10), F(1, 2), F(3), F(250)):
        bound = n * (n + 1)
        for cr in (F(0), F(1, 7), F(-2, 3), F(5, 2), F(-17)):
            for ci in (F(0), F(1, 3), F(-9, 4), F(11)):
                c = QI(cr, ci)
                if absq(c) > bound:
                    continue
                for (x, y) in CIRCLE:
                    rho = 1 + 2 * n + 2 * (c * QI(x, y)).re
                    assert rho >= 0
                    assert 4 * n * rho >= (rho - 1) ** 2
                    samples += 1
    assert samples > 100
    # equality for pure aligned data: n = S^2, c = S C (real), w = 1
    for q in QS:
        C, S = (q + 1 / q) / 2, (q - 1 / q) / 2
        n = S * S
        assert absq(QI(S * C)) == n * (n + 1)
        for sign in (1, -1):
            rho = 1 + 2 * n + 2 * sign * S * C
            assert rho == (q * q if sign == 1 else 1 / (q * q))
            assert 4 * n * rho == (rho - 1) ** 2
    return True


def check_conformal_energy_has_no_cross_term():
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    pairs = ((QI(F(5, 4)), QI(F(3, 4)), F(9, 16)),
             (QI(F(13, 12)), QI(F(1, 4), F(1, 3)), F(25, 144)),
             (QI(F(5, 13), F(12, 13)) * QI(F(13, 12)), QI(F(-5, 12)), F(25, 144)))
    for alpha, beta, b2 in pairs:
        assert absq(beta) == b2 and absq(alpha) - absq(beta) == 1
    for s in TWO_K_ROOTS:
        k = s * s / 2
        for (c, sn) in CIRCLE:
            w = QI(c, sn)
            chi = w / s
            chi1 = QI(0, -k) * chi
            assert chi1 * chi1 + k * k * chi * chi == QI(0)
            assert absq(chi1) + k * k * absq(chi) == k
            for alpha, beta, b2 in pairs:
                u = alpha * chi + beta * chi.conj()
                u1 = alpha * chi1 + beta * chi1.conj()
                E = absq(u1) + k * k * absq(u)
                assert E - k == 2 * k * b2                   # Fourier weight of the energy difference: 2 k n
    # control: the massless point's Bunch-Davies mode e^{-iz}(1 - i/z)/sqrt(2k), z = k eta, 2k = 1
    k = F(1, 2)
    vals = []
    for z in (F(-1), F(-3, 2), F(-7)):
        g = QI(1, -1 / z)                                    # chi = E g, E = e^{-iz}
        dg = QI(0, -1) * g + QI(0, 1 / (z * z))              # d/dz (E g) = E (-i g + g')
        vals.append((k * k) * (dg * dg + g * g))             # (chi'^2 + k^2 chi^2)/E^2, chi' = k d/dz
    assert vals[0] == QI(F(1, 4), F(1, 2))                  # (1/4)(2/z^2 - 1/z^4 - 2i/z^3) at z = -1
    assert vals[1] == QI(F(2, 9) - F(1, 4) * F(16, 81), F(4, 27))
    assert vals[2] == QI(F(1, 4) * (F(2, 49) - F(1, 2401)), F(1, 4) * F(2, 343))
    return True


def check_band_difference_kernel_is_regular():
    premise("synthesis.imported-microlocal-hadamard-condition")
    fact = [F(1)]
    for n in range(1, 40):
        fact.append(fact[-1] * n)
    for (k1, k2) in ((F(1), F(2)), (F(1, 3), F(7, 2)), (F(5), F(6))):
        # termwise: int_{k1}^{k2} k * sum_m (-1)^m (k r)^(2m)/(2m+1)! dk
        termwise = [(-1) ** m * (k2 ** (2 * m + 2) - k1 ** (2 * m + 2)) / ((2 * m + 2) * fact[2 * m + 1])
                    for m in range(12)]
        # closed form (cos k1 r - cos k2 r)/r^2: coefficient of r^(2m) from the r^(2m+2) terms of the cosines
        closed = [(-1) ** (m + 1) * (k1 ** (2 * m + 2) - k2 ** (2 * m + 2)) / fact[2 * m + 2] for m in range(12)]
        assert termwise == closed
        assert closed[0] == (k2 * k2 - k1 * k1) / 2 and closed[0] > 0
    # near r = 0 the band kernel stays at its value (k2^2 - k1^2)/2, while the vacuum's equal-time kernel
    # 1/(4 pi^2 a^2 r^2) (times 4 pi^2 a^2) grows as r^-2: alternating series with decreasing terms at r <= 1/10
    k1, k2 = F(1), F(2)
    c = [(-1) ** (m + 1) * (k1 ** (2 * m + 2) - k2 ** (2 * m + 2)) / fact[2 * m + 2] for m in range(12)]
    for r in (F(1, 10), F(1, 100), F(1, 1000)):
        part = sum(c[m] * r ** (2 * m) for m in range(12))
        assert abs(part - c[0]) <= abs(c[1]) * r * r
        assert 1 / (r * r) > 50 * part
    return True


def shell_lower_bound(q_num, q_den, j, b_exp=10000, const=None):
    """Lower bound of int_{b^j}^{b^(j+1)} k^3 n_k dk, b = 2^b_exp, n_k >= (rho + 1/rho - 2)/4, rho = k^q."""
    lo = 2 ** (b_exp * j)
    hi = 2 ** (b_exp * (j + 1))
    if const is not None:
        nmin = const
    else:
        # q = q_num/q_den with b_exp divisible by q_den: rho at the shell ends is an exact power of 2
        assert b_exp % q_den == 0
        e_lo = q_num * (b_exp // q_den) * j
        e_hi = q_num * (b_exp // q_den) * (j + 1)
        cand = []
        for e in (e_lo, e_hi):
            rho = F(2) ** e
            cand.append((rho + 1 / rho - 2) / 4)
        nmin = min(cand)                                    # rho + 1/rho is monotone on each side of 1
    return (hi - lo) * F(lo) ** 3 * nmin


def check_power_laws_fail_the_energy_moment():
    premise("synthesis.imported-microlocal-hadamard-condition")
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    for (qn, qd) in ((-20351, 10000), (-1, 1), (1, 2)):
        prev = None
        for j in (1, 2, 3):
            lb = shell_lower_bound(qn, qd, j)
            assert lb > 1
            if prev is not None:
                assert lb > prev
            prev = lb
    # constant occupation (the dilatation-invariant case): grows too
    prev = None
    for j in (1, 2, 3):
        lb = shell_lower_bound(0, 1, j, b_exp=4, const=F(1, 1000))
        if prev is not None:
            assert lb > 15 * prev
        prev = lb
    # a constant ratio C != 1 at q = 0: n >= (C + 1/C - 2)/4 > 0, so the moment grows like a constant occupation
    for C in (F(2), F(1, 3)):
        nmin = (C + 1 / C - 2) / 4
        assert nmin > 0
        prev = None
        for j in (1, 2, 3):
            lb = shell_lower_bound(0, 1, j, b_exp=4, const=nmin)
            if prev is not None:
                assert lb > 15 * prev
            prev = lb
    assert (F(1) + 1 / F(1) - 2) / 4 == 0                  # C = 1, q = 0 is the reference itself
    # a shell-supported occupation n = 1 on [1, 2]: finite moment (2^4 - 1)/4
    assert (F(2) ** 4 - 1) / 4 == F(15, 4)
    return True


def check_red_law_has_no_infrared_end():
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    s = F(-351, 10000)
    prev = F(0)
    for m in (1, 2, 3, 4):
        eps_pow_s = F(2) ** (351 * m)                      # eps^s with eps = 2^(-10000 m)
        val = (1 - eps_pow_s) / s
        assert val > prev and val > 10000 * m
        prev = val
    # s = 0 (scale invariance): each dyadic shell [2^-(j+1), 2^-j] contributes at least 1/2
    total = F(0)
    for j in range(40):
        lo, hi = F(1, 2 ** (j + 1)), F(1, 2 ** j)
        total += (hi - lo) / hi
    assert total == 20
    # a blue law reaching k = 0 is allowed: rho = 1/k on (0, 1] (slice index 2), pure states of (i) with
    # n = (1 - k)^2/(4k), |c| = (1 - k^2)/(4k): |c|^2 = n (n + 1) and rho = 1 + 2n + 2|c| (aligned phase, rho >= 1);
    # int_0^1 k n dk = 1/12 and int_0^1 k |c| dk = 1/6 (polynomial integrands), int_0^1 Delta^2 dk/k ~ int_0^1 dk
    for k in (F(1, 7), F(1, 3), F(1, 2), F(4, 5), F(1)):
        n = (1 - k) ** 2 / (4 * k)
        cabs = (1 - k * k) / (4 * k)
        assert cabs * cabs == n * (n + 1)
        assert 1 + 2 * n + 2 * cabs == 1 / k and 1 + 2 * n - 2 * cabs == k
    def integ(coeffs):                                    # int_0^1 sum c_m k^m dk
        return sum((F(c) / (m + 1) for m, c in enumerate(coeffs)), F(0))
    assert integ([F(1, 4), F(-1, 2), F(1, 4)]) == F(1, 12)   # k n = (1 - 2k + k^2)/4
    assert integ([F(1, 4), F(0), F(-1, 4)]) == F(1, 6)          # k |c| = (1 - k^2)/4
    assert integ([F(1)]) == 1                                  # Delta^2/k ~ (k / k) = 1: finite variance
    # the vacuum's s = 2: int_eps^1 k dk = (1 - eps^2)/2 < 1/2
    for m in (1, 2, 3):
        eps = F(1, 2 ** (10000 * m))
        assert (1 - eps * eps) / 2 < F(1, 2)
    return True
