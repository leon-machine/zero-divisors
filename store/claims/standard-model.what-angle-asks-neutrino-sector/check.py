"""standard-model.what-angle-asks-neutrino-sector: exact checks of the arithmetic at record level.

The record values (two-loop run of the chain with the (15,2,2), printed by the legacy T12 script at
four figures): M_I = 1.948e10 GeV, g_R(M_I) = 0.4690, m_3 = 0.0502 eV; the statement's m_3 = 0.050 eV is
also used. All arithmetic is exact on these rationals.
(1) The triplet vev: v_R = M_I/g_R rounds to 4.154e10 GeV (four figures, the record's printout) and
    to 4.2e10 (two figures, the display), while M_I and g_R round to the displayed 1.9e10 and 0.47.
(2) The seesaw along the heavy direction, with the Majorana mass M_R = f_J v_R of the imported
    Clebsch structure: m_3 = m_D^2/M_R iff m_D = sqrt(m_3 f_J v_R), checked as m_D^2 = m_3 f_J v_R at
    three couplings f_J; the coefficient m_D/sqrt(f_J) = sqrt(m_3 v_R), rounded exactly (integer square
    roots), is 1.44 GeV for both m_3 = 0.0502 and 0.050 eV (1.444 and 1.441 to three decimals).
Not checked: the two-loop running that produces M_I and g_R (floating-point, record level).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

EV = F(1, 10 ** 9)                    # 1 eV in GeV
MI = F(1948) * F(10) ** 7             # 1.948e10 GeV
GR = F(4690, 10000)
M3_RECORD = F(502, 10000) * EV
M3_STATED = F(50, 1000) * EV
FJ = (F(1), F(1, 4), F(9, 7))


def sig_round(x, s):
    e = 0
    while F(10) ** (e + 1) <= x:
        e += 1
    while F(10) ** e > x:
        e -= 1
    m = x / F(10) ** (e - s + 1)
    return (m * 2 + 1) // 2, e


def isqrt(n):
    """Integer square root (floor) by Newton's method on integers."""
    if n < 2:
        return n
    x = n
    y = (x + n // x) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def round_sqrt(x):
    """sqrt(x) rounded half up to an integer, for rational x >= 0: floor((sqrt(4x) + 1)/2)."""
    return (isqrt((4 * x).numerator // (4 * x).denominator) + 1) // 2


def check_triplet_vev():
    premise("standard-model.chain")
    ok = True
    vR = MI / GR
    ok = ok and sig_round(vR, 4) == (4154, 10) and sig_round(vR, 2) == (42, 10)
    ok = ok and sig_round(MI, 2) == (19, 10) and sig_round(GR, 2) == (47, -1)
    GA.check("v_R = M_I/g_R = 4.154e10 GeV at the record, displayed 4.2e10", ok)
    return ok


def check_effective_dirac_mass():
    premise("standard-model.chain")
    premise("standard-model.imported-clebsch-structure-seesaw")
    ok = True
    vR = MI / GR
    for m3 in (M3_RECORD, M3_STATED):
        for f in FJ:
            MR = f * vR
            mD2 = m3 * f * vR
            ok = ok and mD2 / MR == m3
        ok = ok and round_sqrt(m3 * vR * 10 ** 4) == 144
    ok = ok and round_sqrt(M3_RECORD * vR * 10 ** 6) == 1444
    ok = ok and round_sqrt(M3_STATED * vR * 10 ** 6) == 1441
    GA.check("m_D = sqrt(m_3 f_J v_R) = 1.44 sqrt(f_J) GeV on the seesaw M_R = f_J v_R", ok)
    return ok
