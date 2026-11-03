"""standard-model.weak-angle-over-derived-generation: exact checks.

States are enumerated one by one: a multiplet (SU(2) dim, colour dim, Y) contributes, for each colour index and
each eigenvalue T3 of the SU(2) Cartan generator (sigma_3/2 on a doublet, 0 on a singlet), one state of charge
Q = T3 + Y. The hypercharges are computed from the generator y = (3i I_2, -2i I_3) acting on the component (j, k)
by 3j - 2k (one-handed listing: Q (1,1), L (1,3), singlets (0,k) conjugated for odd k).
(1) Over one derived generation: sum T3^2 = 2, sum Y^2 = 10/3, sum T3 Y = 0, sum Q^2 = 16/3, ratio 3/8.
(2) Without the lepton doublet: 3/2, 17/6, 13/3, ratio 9/26; the lepton contributes exactly 1/2 to each sum.
(3) Over the fibre C^2 (x) C^3 alone the ratio is 9/10, over the two doublets alone 3/4.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
XY = [QI(0, 3), QI(0, 3)]
YY = [QI(0, -2), QI(0, -2), QI(0, -2)]
SIGMA3_HALF = [F(1, 2), F(-1, 2)]


def _Y(j, k):
    return F((sum((XY[i] for i in range(j)), QI(0)) + sum((YY[i] for i in range(k)), QI(0))).im, 6)


def _generation():
    """(name, SU(2) dim, colour dim, Y) for the derived generation in the one-handed listing."""
    sing = lambda k: _Y(0, k) if k % 2 == 0 else -_Y(0, k)
    return [("Q", 2, 3, _Y(1, 1)), ("L", 2, 1, _Y(1, 3)), ("uc", 1, 3, sing(2)), ("dc", 1, 3, sing(1)),
            ("ec", 1, 1, sing(3)), ("nuc", 1, 1, sing(0))]


def _sums(content):
    t3 = y2 = cr = q2 = F(0)
    for (_, d2, d3, Y) in content:
        eig = SIGMA3_HALF if d2 == 2 else [F(0)]
        for _c in range(d3):
            for T in eig:
                t3 += T * T
                y2 += Y * Y
                cr += T * Y
                q2 += (T + Y) * (T + Y)
    return t3, y2, cr, q2


def check_three_eighths_over_generation():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    premise("standard-model.hyp-s-slot-statistics")
    t3, y2, cr, q2 = _sums(_generation())
    ok = (t3, y2, cr, q2) == (2, F(10, 3), 0, F(16, 3)) and t3 / q2 == F(3, 8) and t3 / (t3 + y2) == F(3, 8)
    GA.check("one generation: sum T3^2 = 2, sum Y^2 = 10/3, ratio 3/8", ok)
    return ok


def check_without_lepton_doublet():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    gen = _generation()
    t3, y2, cr, q2 = _sums([f for f in gen if f[0] != "L"])
    T3, Y2, CR, Q2 = _sums(gen)
    ok = (t3, y2, q2) == (F(3, 2), F(17, 6), F(13, 3)) and t3 / q2 == F(9, 26)
    ok = ok and T3 - t3 == F(1, 2) and Y2 - y2 == F(1, 2)
    GA.check("without L: 3/2, 17/6, 13/3, ratio 9/26; L adds 1/2 to each sum", ok)
    return ok


def check_fibre_and_doublets():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    premise("standard-model.hyp-s-slot-statistics")
    gen = _generation()
    t3f, y2f, crf, q2f = _sums([f for f in gen if f[0] == "Q"])
    t3d, y2d, crd, q2d = _sums([f for f in gen if f[0] in ("Q", "L")])
    ok = t3f / q2f == F(9, 10) and t3d / q2d == F(3, 4) and crf == 0 and crd == 0
    GA.check("fibre alone 9/10, two doublets alone 3/4", ok)
    return ok
