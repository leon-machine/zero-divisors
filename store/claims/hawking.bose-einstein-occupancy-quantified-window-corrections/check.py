"""hawking.bose-einstein-occupancy-quantified-window-corrections: exact checks.

I-state occupancies on the linear s-wave ladder: n_k = 1/(x^{-k} + 1), x = e^{-beta eps} in (0, 1), taken
at exact rational samples x and also as rational functions (GA.RF).
(1) Detailed balance n_k - n_{k+m} = (x^{-m} - 1) n_{k+m} (1 - n_k): as a rational-function identity in
    a = x^{-k} for fixed b = x^{-m}, as one in b for fixed a, and exactly at every k in [-12, 12], m <= 5.
(2) The bilateral sum: summing (1) over a window telescopes exactly,
    sum_{k=-K}^{K-m} (n_k - n_{k+m}) = sum_{k=-K}^{-K+m-1} n_k - sum_{k=K-m+1}^{K} n_k,
    whose deficit from m is sum (1 - n_k) over the bottom m plus sum n_k over the top m, each term below
    x^{K-m+1}: so sum_k (n_k - n_{k+m}) = m = <[a_m, a_m^dagger]>_I and, dividing by x^{-m} - 1,
    sum_k n_{k+m}(1 - n_k) = m/(x^{-m} - 1); the unit-normalised occupancy is 1/(e^{beta eps m} - 1),
    which obeys Bose-Einstein detailed balance nbar/(1 + nbar) = x^m. The Wick formula
    <a_m^dagger a_m> = sum n_{k+m}(1 - n_k) is checked against the density-matrix expectation in the
    product state on an 8-mode window.
(3) Window tails: for the window [-K, K] the bilateral value exceeds the window sum (k in [-K, K-m]) by a
    positive amount at most 2m x^{K-m}/(1 - x), at exact samples.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

XS = [F(1, 2), F(1, 3), F(2, 3), F(3, 4)]
BS = [F(2), F(3), F(8), F(5, 2)]
AS = [F(1, 3), F(1), F(7), F(9, 4)]
# Sample ladder steps m = 1..5 and rungs k in [-12, 12] for detailed balance at exact x.
BALANCE_MS = range(1, 6)
BALANCE_KS = range(-12, 13)


def occ(k, x):
    return 1 / (x ** (-k) + 1)


def check_detailed_balance_identity():
    a = GA.RF.var()
    one = GA.RF1
    for b in BS:
        B = GA.RF.const(b)
        nk, nkm = one / (a + one), one / (a * B + one)
        assert (nk - nkm).eqrf((B - one) * nkm * (one - nk))
        wrong = (B + one) * nkm * (one - nk)
        assert not (nk - nkm).eqrf(wrong)
    bvar = GA.RF.var()
    for av in AS:
        A = GA.RF.const(av)
        nk, nkm = one / (A + one), one / (A * bvar + one)
        assert (nk - nkm).eqrf((bvar - one) * nkm * (one - nk))
    for x in XS:
        for m in BALANCE_MS:
            for k in BALANCE_KS:
                assert occ(k, x) - occ(k + m, x) == (x ** (-m) - 1) * occ(k + m, x) * (1 - occ(k, x))
    return True


def check_bilateral_sum_is_planck_factor():
    premise("hawking.i-state")
    for x in XS:
        for m in range(1, 5):
            for K in (10, 20):
                tele = sum((occ(k, x) - occ(k + m, x) for k in range(-K, K - m + 1)), F(0))
                bottom = sum((occ(k, x) for k in range(-K, -K + m)), F(0))
                top = sum((occ(k, x) for k in range(K - m + 1, K + 1)), F(0))
                assert tele == bottom - top
                deficit = m - tele
                assert deficit == sum((1 - occ(k, x) for k in range(-K, -K + m)), F(0)) + top
                assert 0 < deficit <= 2 * m * x ** (K - m + 1)
                window = sum((occ(k + m, x) * (1 - occ(k, x)) for k in range(-K, K - m + 1)), F(0))
                assert window * (x ** (-m) - 1) == tele
            planck = m / (x ** (-m) - 1)
            nbar = planck / m
            assert nbar == 1 / ((1 / x) ** m - 1)
            assert nbar / (1 + nbar) == x ** m
    return True


def bilin(a, b, vec):
    """psi_a^dag psi_b on a sparse state vector (LSB bitmask basis, Jordan-Wigner signs)."""
    return fock.cre_on(a, fock.ann_on(b, vec))


def check_wick_formula_on_window():
    premise("hawking.i-state")
    NW, sea = 8, 4
    for x in (F(1, 2), F(2, 3)):
        n = [occ(k - sea, x) for k in range(NW)]
        for m in (1, 2, 3):
            expct = F(0)
            for s in range(1 << NW):
                w = F(1)
                for k in range(NW):
                    w *= n[k] if (s >> k) & 1 else 1 - n[k]
                img = {}
                for k in range(NW - m):              # a_m = sum psi_k^dag psi_{k+m}
                    for t, c in bilin(k, k + m, {s: F(1)}).items():
                        for kk in range(NW - m):     # a_m^dag = sum psi_{k+m}^dag psi_k
                            for t2, c2 in bilin(kk + m, kk, {t: c}).items():
                                img[t2] = img.get(t2, F(0)) + c2
                expct += w * img.get(s, F(0))
            wick = sum((n[k + m] * (1 - n[k]) for k in range(NW - m)), F(0))
            assert expct == wick
    return True


def check_window_tail_bound():
    premise("hawking.i-state")
    for x in XS:
        for m in range(1, 4):
            planck = m / (x ** (-m) - 1)
            for K in (12, 18, 25):
                S = sum((occ(k + m, x) * (1 - occ(k, x)) for k in range(-K, K - m + 1)), F(0))
                gap = planck - S
                assert gap > 0
                assert gap <= 2 * m * x ** (K - m) / (1 - x)
    return True
