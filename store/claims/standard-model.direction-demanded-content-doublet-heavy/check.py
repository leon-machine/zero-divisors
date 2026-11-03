"""standard-model.direction-demanded-content-doublet-heavy: exact checks.

Inputs of the spectrum run: alpha_em^-1 = 128, sin^2 theta_W = 0.2312, alpha_s = 0.118 (a_3 = 500/59),
a_2 = sin^2 alpha_em^-1, a_1 = (3/5)(alpha_em^-1 - a_2); b = (41/10, -19/6, -7). R = (a_1 - a_2)/(a_2 - a_3),
r_0 = (b_1 - b_2)/(b_2 - b_3); the threshold fraction of the one-threshold theorem,
f = (R b_23 - b_12)/(Delta_12 - R Delta_23), and r_Delta = (b_12 + Delta_12)/(b_23 + Delta_23).
(1) a_2 = 18496/625, a_1 = 184512/3125, R = 1357472/973455 (1.3945 to four places), r_0 = 218/115 (1.8957),
    R < r_0.
(2) On a grid of 7^3 rational shifts Delta (each entry in {-2, -2/3, 0, 1/6, 1, 4/3, 7/2}) with nonzero
    denominator: f > 0 exactly when (1 + R) Delta_2 > Delta_1 + R Delta_3; and among those with f > 0 and
    b_23 + Delta_23 > 0, f <= 1 exactly when r_Delta <= R; both outcomes of each test occur on the grid.
    The numerator of f is b_23 (R - r_0) < 0, with b_12 = 109/15 and b_23 = 23/6.
(3) Content with Delta_2 = 0, Delta_3 > 0 and Delta_1 >= 0 has f < 0 (sample Delta_1, Delta_3): the gluino
    (0, 0, 2) gives f = -0.69 (two places) and r_Delta = 218/55. Control: without Delta_1 >= 0 the sign
    can flip, (-2, 0, 1/6) has f > 0.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

GRID = [F(-2), F(-2, 3), F(0), F(1, 6), F(1), F(4, 3), F(7, 2)]
B_SM = (F(41, 10), F(-19, 6), F(-7))     # one-loop coefficients b = (b_1, b_2, b_3), input of the run


def record():
    A, s2, a3 = F(128), F(2312, 10000), F(500, 59)
    a2 = s2 * A
    return (F(3, 5) * (A - a2), a2, a3)


def check_record_ratio_below_r0():
    premise("standard-model.spectrum-run")
    a1, a2, a3 = record()
    b = (F(41, 10), F(-19, 6), F(-7))
    R = (a1 - a2) / (a2 - a3)
    r0 = (b[0] - b[1]) / (b[1] - b[2])
    ok = a2 == F(18496, 625) and a1 == F(184512, 3125) and a3 == F(500, 59)
    ok = ok and R == F(1357472, 973455) and abs(R - F(13945, 10000)) < F(1, 20000)
    ok = ok and r0 == F(218, 115) and abs(r0 - F(18957, 10000)) < F(1, 20000) and R < r0
    GA.check("R = 1357472/973455 < r_0 = 218/115 at the record", ok)
    return ok


def check_direction_criterion():
    premise("standard-model.one-threshold-exact-criterion")
    premise("standard-model.spectrum-run")
    a1, a2, a3 = record()
    b1, b2, b3 = B_SM
    b12, b23 = b1 - b2, b2 - b3
    ok = b12 == F(109, 15) and b23 == F(23, 6)          # by hand: 41/10 + 19/6 = 109/15, 7 - 19/6 = 23/6
    R = (a1 - a2) / (a2 - a3)
    ok = ok and R * b23 - b12 < 0                      # the numerator b_23 (R - r_0) of f is negative
    signs, splits = set(), set()                        # outcomes seen: both sides of each criterion occur
    for d1 in GRID:
        for d2 in GRID:
            for d3 in GRID:
                den = (d1 - d2) - R * (d2 - d3)
                if den == 0:
                    continue
                f = (R * b23 - b12) / den
                pos = f > 0
                ok = ok and (pos == ((1 + R) * d2 > d1 + R * d3))
                signs.add(pos)
                if pos and b23 + (d2 - d3) > 0:
                    rD = (b12 + d1 - d2) / (b23 + d2 - d3)
                    within = f <= 1
                    ok = ok and (within == (rD <= R))
                    splits.add(within)
    ok = ok and signs == {True, False} and splits == {True, False}
    GA.check("f > 0 iff (1 + R) D2 > D1 + R D3; then f <= 1 iff r_Delta <= R", ok)
    return ok


def check_gluino_worsens():
    premise("standard-model.one-threshold-exact-criterion")
    premise("standard-model.spectrum-run")
    a1, a2, a3 = record()
    b = (F(41, 10), F(-19, 6), F(-7))
    b12, b23 = b[0] - b[1], b[1] - b[2]
    R = (a1 - a2) / (a2 - a3)
    ok = True
    for d1 in (F(0), F(1, 10), F(2)):
        for d3 in (F(1, 2), F(2), F(5)):
            f = (R * b23 - b12) / ((d1 - 0) - R * (0 - d3))
            ok = ok and f < 0
    # scope control: with Delta_1 < -R Delta_3 the sign flips, e.g. (-2, 0, 1/6) has f > 0
    ok = ok and (R * b23 - b12) / (F(-2) - R * (0 - F(1, 6))) > 0 and F(-2) + R * F(1, 6) < 0
    fg = (R * b23 - b12) / (0 - R * (0 - 2))
    ok = ok and abs(fg - F(-69, 100)) < F(1, 200)
    ok = ok and (b12 + 0) / (b23 + 0 - 2) == F(218, 55)
    GA.check("a gluino (0, 0, 2) has f < 0 and r_Delta = 218/55: it worsens the miss", ok)
    return ok
