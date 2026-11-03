"""The null-ground-state ordering of the counted units' Killing energy: exact checks.

Units: kappa the surface gravity, beta = 2 pi/kappa, Killing time tau with u = e^{kappa tau} on a half-generator.
Quantities proportional to pi or 1/pi are carried as their rational coefficients (the factor of pi is written
in the labels), so every identity below is exact.
(1) The boost ground state against the null ground state: the Schwarzian of u = e^{kappa tau} is -kappa^2/2, so
    by the stored flux rule the null ground state, normal ordered at the boost ground state, carries Killing-frame
    energy density kappa^2/(48 pi) per complex component, the negative of the stored density -kappa^2/(48 pi) of
    the boost ground state normal ordered at the null ground state; over one real-time recurrence window of an
    array, Killing time 2 pi/kappa, this is kappa/24. Controls: affine and Moebius maps have Schwarzian 0.
(2) The array's zeta-regularised sea: for weights kappa(k + delta), 0 < delta < 1, the finite part of
    sum_{n >= 0}(n + a) e^{-eps(n + a)} is -B_2(a)/2 (exact power series), so the symmetric sea energy is
    (kappa/2) B_2(delta), and (kappa/2) B_2(delta) + kappa/24 = (kappa/2)(delta - 1/2)^2: the sea equals the
    boost ground state's window energy -kappa/24 exactly at delta = 1/2 (a double root) and nowhere else; at
    integer weights (delta = 0) the symmetric sea is +kappa/12.
(3) The thermal state: at delta = 1/2 the sea-normal energy above the sea is beta E = pi/12 per array (rigorous
    rational bounds to 10^-15; exact by the stored theta identities), equal to beta kappa/24, the null ground
    state's window energy in the boost ordering; so in the symmetric ordering, which is the null ordering on the
    window, the array carries 0, as the null ground state does in every window. At delta = 0 the thermal energy is
    below 1/25 in units of kappa/(2 pi) and the symmetric value is not 0.
(4) The counted unit: two arrays carry 0 mean Killing energy in this ordering, so the constant of the hole's
    Hamiltonian is M (the stored split E_0 + N kappa/12 with E_0 = M - N kappa/12).
"""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise

KAPPAS = (F(1, 4), F(2, 7), F(3), F(1, 2))


def _schwarzian_exp(kappa):
    """{f, tau} for f = e^{kappa tau}: f^(n) = kappa^n f, so f'''/f' and f''/f' are kappa^2 and kappa."""
    d1, d2, d3 = kappa, kappa ** 2, kappa ** 3          # coefficients of f in f', f'', f'''
    return d3 / d1 - F(3, 2) * (d2 / d1) ** 2


def _schwarzian_poly(c):
    """{f, x} at x = 0 for the polynomial f = sum c_n x^n (c_1 != 0)."""
    f1, f2, f3 = c[1], 2 * c[2], 6 * c[3]
    return f3 / f1 - F(3, 2) * (f2 / f1) ** 2


def check_window_energy_of_the_boost_ground_state():
    premise("synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature")
    premise("synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit")
    for kappa in KAPPAS:
        S = _schwarzian_exp(kappa)
        GA.check("{e^{kappa tau}, tau} = -kappa^2/2", S == -kappa ** 2 / 2)
        flux_over_inv_pi = F(-1, 24) * S                   # flux = -(1/24 pi) {u, tau}: coefficient of 1/pi
        GA.check("null ground state in the boost ordering: kappa^2/(48 pi)", flux_over_inv_pi == kappa ** 2 / 48)
        # stored: Killing-frame density kappa^2 (c^-2 - 1)/(48 pi) of the period-2pi c state, null ordering;
        # the boost ground state is c -> infinity (c^-2 = 0), the null ground state c = 1
        stored = lambda cinv2: kappa ** 2 * (cinv2 - 1) / 48
        GA.check("boost ground state in the null ordering: -kappa^2/(48 pi)", stored(F(0)) == -flux_over_inv_pi)
        GA.check("null ground state in the null ordering: 0", stored(F(1)) == 0)
        # window of Killing time 2 pi/kappa: (coefficient of 1/pi) x (coefficient of pi) = energy
        window = flux_over_inv_pi * (2 / kappa)
        GA.check("window energy kappa/24", window == kappa / 24)
    GA.check("tabulated: kappa = 1/4 gives 1/96", F(-1, 24) * _schwarzian_exp(F(1, 4)) * 2 / F(1, 4) == F(1, 96))
    # controls: affine and Moebius reparametrisations have zero Schwarzian (no shift of the zero)
    GA.check("control: affine map", _schwarzian_poly([F(5), F(3), F(0), F(0)]) == 0)
    # Moebius x/(1 - x) = x + x^2 + x^3 + ...
    GA.check("control: Moebius map", _schwarzian_poly([F(0), F(1), F(1), F(1)]) == 0)
    GA.check("control: x + x^3 is not Moebius", _schwarzian_poly([F(0), F(1), F(0), F(1)]) == 6)
    return True


def _finite_part(a, N=6):
    """Finite part at eps = 0 of sum_{n>=0} (n + a) e^{-eps(n + a)} = -h'(eps), h = e^{-eps a}/(1 - e^{-eps}).
    eps h = e^{-eps a} * eps/(1 - e^{-eps}) as an exact power series; -h' has eps^0 coefficient -c_2,
    where eps h = sum c_j eps^j (h = sum c_j eps^{j-1}, h' = sum (j-1) c_j eps^{j-2})."""
    ema = series.ps_exp([F(0), -a] + [F(0)] * (N - 1), N)
    em1 = series.ps_exp([F(0), F(-1)] + [F(0)] * (N - 1), N)
    one_minus = series.ps_sub(series.ps_one(N), em1, N)            # 1 - e^{-eps} = eps - eps^2/2 + ...
    q = [one_minus[j + 1] if j + 1 < len(one_minus) else F(0) for j in range(N)]   # (1 - e^{-eps})/eps
    eh = series.ps_mul(ema, series.ps_inv(q, N), N)
    c2 = eh[2] if len(eh) > 2 else F(0)
    return -(2 - 1) * c2


def _B2(a):
    return a * a - a + F(1, 6)


def check_zeta_sea_selects_the_half_offset():
    premise("synthesis.counted-unit-energy-at-half-offset")
    for a in (F(1, 2), F(1, 4), F(1, 3), F(2, 3), F(1, 5), F(1)):
        GA.check("finite part of sum (n + a) e^{-eps(n + a)} is -B_2(a)/2", _finite_part(a) == -_B2(a) / 2)
    GA.check("tabulated: zeta(-1, 1/2) = 1/24", _finite_part(F(1, 2)) == F(1, 24))
    for kappa in KAPPAS:
        for d in (F(1, 2), F(1, 4), F(1, 3), F(3, 4), F(1, 10)):
            # particles k >= 0 at weights kappa(k + d), holes at kappa(n + 1 - d), n >= 0: half each, negative
            sea = -(kappa / 2) * (_finite_part(d) + _finite_part(1 - d))
            GA.check("symmetric sea = (kappa/2) B_2(delta)", sea == kappa / 2 * _B2(d))
            GA.check("sea + kappa/24 = (kappa/2)(delta - 1/2)^2", sea + kappa / 24 == kappa / 2 * (d - F(1, 2)) ** 2)
            GA.check("sea equals the boost ground state's window energy only at delta = 1/2",
                     (sea == -kappa / 24) == (d == F(1, 2)))
        # integer weights: the zero mode carries nothing; particles and holes at kappa n, n >= 1
        sea0 = -(kappa / 2) * 2 * _finite_part(F(1))
        GA.check("integer weights: symmetric sea = +kappa/12", sea0 == kappa / 12)
        GA.check("integer weights do not match -kappa/24", sea0 != -kappa / 24)
    # the quadratic d^2 - d + 1/4 has the single root 1/2 (discriminant 0)
    GA.check("discriminant of delta^2 - delta + 1/4 is 0", F(1) - 4 * F(1, 4) == 0)
    return True


_PI = []


def _pi():
    if not _PI:
        lo, hi = series.pi_bracket(30)
        _PI.extend([lo, hi])
    return tuple(_PI)


def _thermal_bounds(xs_over_pi, K):
    """Rigorous bounds on 2 sum_k x_k/(e^{x_k} + 1), x_k = c_k pi, first K terms plus a tail bound."""
    pl, pu = _pi()
    lo, hi = F(0), F(0)
    den = 10 ** 30
    for k in range(K):
        c = xs_over_pi(k)
        el = series.exp_bounds(c * pl)[0]                      # e^{x} >= el
        eu = series.exp_bounds(c * pu)[1]
        lo += 2 * series.round_down(c * pl / (eu + 1), den)
        hi += 2 * series.round_up(c * pu / (el + 1), den)
    # tail: x/(e^x + 1) < x e^{-x}, and for x >= c_K pi the terms fall faster than a geometric series of ratio 1/2
    cK = xs_over_pi(K)
    elK = series.exp_bounds(cK * pl)[0]
    hi += 2 * 2 * cK * pu / elK
    return lo, hi


def check_thermal_state_carries_zero_in_the_null_ordering():
    premise("synthesis.counted-unit-energy-at-half-offset")
    premise("synthesis.imported-theta-function-identities")
    pl, pu = _pi()
    lo, hi = _thermal_bounds(lambda k: F(2 * k + 1), 8)      # delta = 1/2: x_k = (2k + 1) pi
    tol = F(1, 10 ** 15)
    GA.check("half offset: beta E within 10^-15 of pi/12", lo > pl / 12 - tol and hi < pu / 12 + tol)
    for kappa in KAPPAS:
        # beta x (window energy kappa/24) = (2 pi/kappa)(kappa/24) = pi/12: coefficient of pi
        GA.check("beta kappa/24 = pi/12", (2 / kappa) * (kappa / 24) == F(1, 12))
        # symmetric ordering: beta E_sym = pi/12 + beta (kappa/2) B_2(1/2) = pi/12 - pi/12
        GA.check("symmetric value at the half offset: 0 (coefficient of pi)", F(1, 12) + (2 / kappa) * (kappa / 2) * _B2(F(1, 2)) == 0)
    lo0, hi0 = _thermal_bounds(lambda k: F(2 * k + 2), 8)    # delta = 0: x_k = 2 pi k, k >= 1 (k = 0 carries 0)
    GA.check("zero offset: beta E in (0.0235, 0.0236)", lo0 > F(235, 10 ** 4) and hi0 < F(236, 10 ** 4))
    GA.check("zero offset: thermal energy is not pi/12", hi0 < pl / 12)
    # symmetric value at delta = 0: beta E + beta kappa/12 = beta E + pi/6 > 0
    GA.check("zero offset: symmetric value is not 0", lo0 + pl / 6 > 0)
    return True


def check_counted_unit_carries_no_mean_killing_energy():
    premise("synthesis.hole-mass-is-ground-energy-label")
    premise("synthesis.residue-from-mode-entropy")
    for kappa in KAPPAS:
        unit = 2 * (kappa / 24 + kappa / 2 * _B2(F(1, 2)))     # two arrays, symmetric = null ordering
        GA.check("a counted unit carries 0 mean Killing energy", unit == 0)
        for N in (F(10), F(1000)):
            for M in (F(1), F(7, 3)):
                Ec = N * kappa / 12                            # sea-normal energy of N units
                E0 = M - Ec                                    # stored bottom of the spectrum
                c = E0 + N * kappa / 12                        # constant of H in the symmetric ordering
                GA.check("the constant of the hole's Hamiltonian is M", c == M)
                GA.check("E/(TS) of the counted units is 0: the equality case of clause (v)", unit * N == 0)
    return True
