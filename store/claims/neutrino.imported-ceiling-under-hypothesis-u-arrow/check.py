"""neutrino.imported-ceiling-under-hypothesis-u-arrow: exact checks of the valuation of the rung scale.

Inputs are exact rationals (GeV): the record's quark masses m_b = 4.18 in (4.13, 4.23) and
m_t = 172.57 in (172.28, 172.86) (PDG 2024), and m_3 = 0.050 eV in (49.4, 50.5) meV.
(1) The seesaw inversion: m_3 = m_D^2/M_R iff M_R = m_D^2/m_3 (at sample values), and the scalar
    seesaw it stands for: the light root of lambda^2 - M_R lambda - m_D^2 (the mass matrix
    [[0, m_D], [m_D, M_R]]) lies within 2 m_D^4/M_R^3 of -m_D^2/M_R (sign change of the
    characteristic polynomial), for m_D << M_R.
(2) The two ends under Hypothesis (U), m_D = m_b and m_D = m_t: at the central values
    m_b^2/m_3 rounds to 3.5e11 GeV (two figures) and m_t^2/m_3 to 6e14 GeV (one figure); over the whole
    input box the ends stay in (3.3, 3.7)e11 and (5.8, 6.1)e14 GeV; the ends differ by
    (m_t/m_b)^2, which rounds to 1.7e3 at the central values and lies in (1.6, 1.8)e3 over the box.
Not checked: the qualitative clauses (the asymmetry as inherited data, the orientation as the only
CP-violating mechanism supplied, the flag covariance of the nu_R identification, the reheating), which
are stances and imports with no finite numerical core here.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

EV = F(1, 10 ** 9)                       # 1 eV in GeV
MB = (F(413, 100), F(418, 100), F(423, 100))
MT = (F(17228, 100), F(17257, 100), F(17286, 100))
M3 = (F(494, 10) * EV / 1000, F(50, 1000) * EV, F(505, 10) * EV / 1000)
SEESAW_SAMPLES = ((F(4), F(10) ** 6), (F(17257, 100), F(6) * F(10) ** 14), (F(1, 3), F(7) * F(10) ** 9))


def sig_round(x, s):
    """(mantissa integer, exponent) with x = mantissa 10^(exponent - s + 1) rounded half up."""
    e = 0
    while F(10) ** (e + 1) <= x:
        e += 1
    while F(10) ** e > x:
        e -= 1
    m = x / F(10) ** (e - s + 1)
    return (m * 2 + 1) // 2, e


def check_seesaw_inversion_and_light_root():
    premise("dark-matter.ceiling-valued-inherited-success")
    ok = True
    for mD, MR in SEESAW_SAMPLES:
        m3 = mD * mD / MR
        ok = ok and mD * mD / m3 == MR
        # characteristic polynomial of [[0, m_D], [m_D, M_R]]: lambda^2 - M_R lambda - m_D^2
        tr, det = 0 + MR, 0 * MR - mD * mD
        ok = ok and (tr, det) == (MR, -mD * mD)
        f = lambda lam: lam * lam - tr * lam + det          # noqa: E731
        lam0 = -mD * mD / MR
        ok = ok and f(lam0) == mD ** 4 / MR ** 2
        step = -f(lam0) / (2 * lam0 - tr)                    # one Newton step from -m_D^2/M_R
        ok = ok and step == mD ** 4 / (MR ** 3 + 2 * mD ** 2 * MR)
        lo, hi = lam0 - 2 * mD ** 4 / MR ** 3, lam0 + 2 * mD ** 4 / MR ** 3
        ok = ok and f(lo) > 0 and f(hi) < 0 and hi < 0
    GA.check("M_R = m_D^2/m_3 inverts the seesaw; the light root is -m_D^2/M_R + m_D^4/M_R^3 + ...", ok)
    return ok


def check_two_ends_of_the_range():
    premise("dark-matter.ceiling-valued-inherited-success")
    premise("dark-matter.hyp-u-equal-rank-one-eigenvalues")
    ok = True
    low = MB[1] ** 2 / M3[1]
    high = MT[1] ** 2 / M3[1]
    ok = ok and sig_round(low, 2) == (35, 11) and sig_round(high, 1) == (6, 14)
    ok = ok and sig_round((MT[1] / MB[1]) ** 2, 2) == (17, 3)
    lows = [b * b / m for b in (MB[0], MB[2]) for m in (M3[0], M3[2])]
    highs = [t * t / m for t in (MT[0], MT[2]) for m in (M3[0], M3[2])]
    ratios = [(t / b) ** 2 for t in (MT[0], MT[2]) for b in (MB[0], MB[2])]
    ok = ok and all(F(33, 10) * 10 ** 11 < x < F(37, 10) * 10 ** 11 for x in lows)
    ok = ok and all(F(58, 10) * 10 ** 14 < x < F(61, 10) * 10 ** 14 for x in highs)
    ok = ok and all(F(16, 10) * 10 ** 3 < x < F(18, 10) * 10 ** 3 for x in ratios)
    ok = ok and low < high
    GA.check("m_b^2/m_3 = 3.5e11 GeV and m_t^2/m_3 = 6e14 GeV at the record, ends ratio (m_t/m_b)^2 = 1.7e3", ok)
    return ok
