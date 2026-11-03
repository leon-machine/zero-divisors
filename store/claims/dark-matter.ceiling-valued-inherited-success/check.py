"""dark-matter.ceiling-valued-inherited-success: exact checks of the valuation under Hypothesis (U).

Computable part: the leading-order rank-one eigenvalue of a sector (the families alignment), the
seesaw inversion M_R = m_D^2/m_3 and the two ends of the range with their ratio. The statements about
running from the ceiling (an order of magnitude) and about the bottom-tau ratio are imported or
deferred in the statement itself and are not checked.

(1) A democratic rank-one mass form y J (the alignment's texture) has the single nonzero eigenvalue
3y (on u'), the other two zero; under (U) that eigenvalue is m_D, read as m_t or m_b. The seesaw
m_3 = m_D^2/M_R is inverted exactly, M_R = m_D^2/m_3, and recovers m_3.
(2) With m_t in (172, 174) GeV, m_b in (4.15, 4.21) GeV and m_3 in (0.045, 0.055) eV, exact rational
division gives m_t^2/m_3 in (5e14, 7e14) GeV and m_b^2/m_3 in (3e11, 4e11) GeV; at the central values
173, 4.18 GeV and 0.05 eV they are in (5.95, 6.05)e14 (the quoted 6e14) and (3.45, 3.55)e11 (the quoted
3.5e11).
(3) The ratio of the ends is (m_t/m_b)^2 exactly, whatever m_3, in (1600, 1800) on the brackets and
(1650, 1750) at the central values (the quoted 1.7e3); the lower end (bottom reading) is below the
upper (top reading).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MT = (F(172), F(174))
MB = (F(415, 100), F(421, 100))
M3_EV = (F(45, 1000), F(55, 1000))
CENTRAL = (F(173), F(418, 100), F(5, 100))
YUKAWAS = (F(1), F(7, 3), F(-2, 5))
M3_SAMPLES = (F(5, 100), F(1, 3), F(9))
GEV = 10 ** 9
# the statement's quoted windows (GeV, then dimensionless): brackets of the two ends, the windows
# around the quoted central values 6e14 and 3.5e11, and the ratio's bracket and central window
TOP_BRACKET = (5 * 10 ** 14, 7 * 10 ** 14)
BOT_BRACKET = (3 * 10 ** 11, 4 * 10 ** 11)
TOP_CENTRAL_WINDOW = (F(595, 100) * 10 ** 14, F(605, 100) * 10 ** 14)
BOT_CENTRAL_WINDOW = (F(345, 100) * 10 ** 11, F(355, 100) * 10 ** 11)
RATIO_BRACKET = (1600, 1800)
RATIO_CENTRAL_WINDOW = (1650, 1750)


def jmat():
    return [[F(1)] * 3 for _ in range(3)]


def check_rank_one_eigenvalue_and_seesaw_inversion():
    premise("families.alignment-computed-thirteenth-refutation-democracy-one")
    premise("dark-matter.hyp-u-equal-rank-one-eigenvalues")
    ok = True
    for y in YUKAWAS:
        M = [[y * x for x in row] for row in jmat()]
        ok = ok and GA.mat_mul(M, [[F(1)]] * 3) == [[3 * y]] * 3
        ok = ok and GA.mat_mul(M, [[F(1)], [F(-1)], [F(0)]]) == [[F(0)]] * 3
        ok = ok and GA.mat_mul(M, [[F(1)], [F(1)], [F(-2)]]) == [[F(0)]] * 3
        ok = ok and GA.mat_rank(M) == 1
        mD = 3 * y
        for m3 in M3_SAMPLES:
            MR = mD * mD / m3
            ok = ok and mD * mD / MR == m3
    GA.check("rank-one form y J has the one eigenvalue 3y; M_R = m_D^2/m_3 inverts the seesaw", ok)
    return ok


def check_two_ends_of_the_range():
    premise("dark-matter.hyp-u-equal-rank-one-eigenvalues")
    m3_lo, m3_hi = M3_EV
    m3 = (m3_lo / GEV, m3_hi / GEV)
    top = (MT[0] ** 2 / m3[1], MT[1] ** 2 / m3[0])
    bot = (MB[0] ** 2 / m3[1], MB[1] ** 2 / m3[0])
    # exact ends of the brackets, by hand: 172^2 = 29584, 174^2 = 30276, 4.15^2 = 17.2225,
    # 4.21^2 = 17.7241, over 5.5e-11 and 4.5e-11 GeV
    ok = top == (F(29584, 55) * 10 ** 12, F(30276, 45) * 10 ** 12)
    ok = ok and bot == (F(172225, 55) * 10 ** 8, F(177241, 45) * 10 ** 8)
    ok = ok and TOP_BRACKET[0] < top[0] and top[1] < TOP_BRACKET[1]
    ok = ok and BOT_BRACKET[0] < bot[0] and bot[1] < BOT_BRACKET[1]
    mt, mb, m3c = CENTRAL
    m3c = m3c / GEV
    ok = ok and TOP_CENTRAL_WINDOW[0] < mt ** 2 / m3c < TOP_CENTRAL_WINDOW[1]
    ok = ok and BOT_CENTRAL_WINDOW[0] < mb ** 2 / m3c < BOT_CENTRAL_WINDOW[1]
    # exact central values, by hand: 173^2 = 29929 and 4.18^2 = 17.4724, over 5e-11 GeV
    ok = ok and mt ** 2 / m3c == 598580 * 10 ** 9 and mb ** 2 / m3c == 349448 * 10 ** 6
    GA.check("m_t^2/m_3 in (5e14, 7e14) GeV (central 6e14), m_b^2/m_3 in (3e11, 4e11) GeV (central 3.5e11)", ok)
    return ok


def check_ratio_of_the_ends():
    premise("dark-matter.hyp-u-equal-rank-one-eigenvalues")
    ok = True
    mt, mb, _ = CENTRAL
    for m3 in M3_SAMPLES:
        ok = ok and (mt ** 2 / m3) / (mb ** 2 / m3) == (mt / mb) ** 2 and mb ** 2 / m3 < mt ** 2 / m3
    lo, hi = (MT[0] / MB[1]) ** 2, (MT[1] / MB[0]) ** 2
    # exact ends of the bracket, by hand: 172^2/4.21^2 and 174^2/4.15^2
    ok = ok and lo == F(295840000, 177241) and hi == F(302760000, 172225)
    ok = ok and RATIO_BRACKET[0] < lo and hi < RATIO_BRACKET[1]
    ok = ok and RATIO_CENTRAL_WINDOW[0] < (mt / mb) ** 2 < RATIO_CENTRAL_WINDOW[1]
    ok = ok and (mt / mb) ** 2 == F(299290000, 174724)
    GA.check("the ends differ by (m_t/m_b)^2 in (1600, 1800), central 1.7e3", ok)
    return ok
