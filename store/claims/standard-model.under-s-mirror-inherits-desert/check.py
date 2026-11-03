"""standard-model.under-s-mirror-inherits-desert: exact checks from the species content.

Content per generation (left-handed Weyl, (SU(3) dim, SU(2) dim, Y) with Q = T3 + Y): Q (3,2,1/6),
u^c (3b,1,-2/3), d^c (3b,1,1/3), e^c (1,1,1), nu^c (1,1,0), and under (S) the lepton doublet
L (1,2,-1/2); three generations and one Higgs doublet (1,2,1/2), a complex scalar.
b_i = -11/3 C2(G_i) + 2/3 sum_Weyl T_i + 1/3 sum_scalars T_i, T_1 = 3/5 sum Y^2 (Fact
standard-model.imported-coefficient-sum-indices).
(1) Under (S): (b1, b2, b3) = (41/10, -19/6, -7) and r0 = (b1 - b2)/(b2 - b3) = 218/115. Without the
    lepton doublet: (7/2, -25/6, -7), ratio 46/17; the three lepton doublets contribute 3/5 to b1,
    1 to b2, 0 to b3.
(2) Trace normalisations: over the content without L, k = sum Y^2 / sum T3^2 = 17/9 and
    sum T3^2 / sum Q^2 = 9/26; with L, k = 5/3 (the 3/5 of Fact (a)) and 3/8. In the normalisation
    a1 = alpha_Y^{-1}/k with k = 17/9 the abelian coefficient is 105/34 and the ratio 740/289.
(3) Without L the [SU(2)]^2 U(1)_Y sum is 1/2 per generation (3 x 1/6); with L it is 0.
(4) The mirror's equations are this tower's: the mirror listing (the copy) gives the same b, and
    for sample boundary values the pairwise crossing points t_ij = (a_i - a_j)/(b_i - b_j) agree
    (meeting exactly when (a1 - a2)/(a2 - a3) = r0; four samples miss, two built to meet). Adding the
    other tower's fields as singlets of this tower's groups (index zero) leaves b unchanged, in
    each direction: the resolution is duplicated, never shared.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

GEN = [("Q", 3, 2, F(1, 6)), ("uc", 3, 1, F(-2, 3)), ("dc", 3, 1, F(1, 3)),
       ("ec", 1, 1, F(1)), ("nuc", 1, 1, F(0))]
LEPTON = ("L", 1, 2, F(-1, 2))
HIGGS = ("H", 1, 2, F(1, 2))
BOUNDARY = [(F(59), F(30), F(8)), (F(61), F(29), F(9)), (F(1), F(2), F(3)), (F(10), F(5), F(4))]


def _content(with_L, gens=3):
    one = GEN + ([LEPTON] if with_L else [])
    return one * gens


def _T(field, group):
    name, c, w, y = field
    if group == 1:
        return F(3, 5) * c * w * y * y
    if group == 2:
        return F(1, 2) * c if w == 2 else F(0)
    return F(1, 2) * w if c == 3 else F(0)


def _b(weyl, scalars):
    C2 = {1: 0, 2: 2, 3: 3}
    return tuple(-F(11, 3) * C2[g] + F(2, 3) * sum(_T(f, g) for f in weyl)
                 + F(1, 3) * sum(_T(f, g) for f in scalars) for g in (1, 2, 3))


def _ratio(b):
    return (b[0] - b[1]) / (b[1] - b[2])


def check_coefficients_with_and_without_lepton_doublet():
    premise("standard-model.imported-coefficient-sum-indices")
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    bS = _b(_content(True), [HIGGS])
    b0 = _b(_content(False), [HIGGS])
    ok = ok and bS == (F(41, 10), F(-19, 6), F(-7)) and _ratio(bS) == F(218, 115)
    ok = ok and b0 == (F(7, 2), F(-25, 6), F(-7)) and _ratio(b0) == F(46, 17)
    ok = ok and tuple(x - y for x, y in zip(bS, b0)) == (F(3, 5), F(1), F(0))
    GA.check("b = (41/10, -19/6, -7), r0 = 218/115 under (S); (7/2, -25/6, -7), 46/17 without L", ok)
    return ok


def check_trace_normalisations():
    premise("standard-model.imported-one-loop-running-trace-ratio")
    premise("standard-model.weak-angle-over-derived-generation")
    premise("standard-model.imported-coefficient-sum-indices")
    ok = True

    def sums(fields):
        sy = sum(c * w * y * y for _, c, w, y in fields)
        st = sum(c * F(1, 2) for _, c, w, y in fields if w == 2)       # T3^2 = 1/4 on 2 states
        sq = F(0)
        for _, c, w, y in fields:
            if w == 2:
                sq += c * ((F(1, 2) + y) ** 2 + (-F(1, 2) + y) ** 2)
            else:
                sq += c * y * y
        return sy, st, sq

    sy, st, sq = sums(GEN)
    ok = ok and sy / st == F(17, 9) and st / sq == F(9, 26)
    syL, stL, sqL = sums(GEN + [LEPTON])
    ok = ok and syL / stL == F(5, 3) and stL / sqL == F(3, 8)
    b0 = _b(_content(False), [HIGGS])
    bY = b0[0] * F(5, 3)                       # coefficient of alpha_Y^{-1}
    k = sy / st
    b1k = bY / k
    ok = ok and b1k == F(105, 34) and _ratio((b1k, b0[1], b0[2])) == F(740, 289)
    GA.check("k = 17/9 and 9/26 without L, 5/3 and 3/8 with L; abelian 105/34, ratio 740/289", ok)
    return ok


def check_anomaly_without_lepton_doublet():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    ok = True
    a0 = sum(c * y for _, c, w, y in GEN if w == 2)
    aL = sum(c * y for _, c, w, y in GEN + [LEPTON] if w == 2)
    ok = ok and a0 == F(1, 2) and aL == 0
    GA.check("[SU(2)]^2 U(1)_Y: 1/2 per generation without L, 0 with it", ok)
    return ok


def check_mirror_same_equations_no_sharing():
    premise("standard-model.imported-sectors-superselection-mirror-copy")
    premise("standard-model.no-tower-but-one-contributes-towers")
    premise("standard-model.imported-one-loop-running-trace-ratio")
    ok = True
    ours = _content(True)
    mirror = [(name + "'", c, w, y) for name, c, w, y in ours]      # the copy
    b_ours = _b(ours, [HIGGS])
    b_mirror = _b(mirror, [(HIGGS[0] + "'",) + HIGGS[1:]])
    ok = ok and b_mirror == b_ours
    meets = 0
    for a in BOUNDARY:
        for b in (b_ours, b_mirror):
            t12 = (a[0] - a[1]) / (b[0] - b[1])
            t23 = (a[1] - a[2]) / (b[1] - b[2])
            meet = t12 == t23
            ok = ok and meet == ((a[0] - a[1]) / (a[1] - a[2]) == F(218, 115))
            meets += 1 if meet else 0
    # none of the four BOUNDARY samples has ratio 218/115; two meeting samples are built here
    for a2, a3 in ((F(30), F(15)), (F(7), F(-108))):
        a1 = a2 + F(218, 115) * (a2 - a3)
        for b in (b_ours, b_mirror):
            ok = ok and (a1 - a2) / (b[0] - b[1]) == (a2 - a3) / (b[1] - b[2])
            meets += 1
    ok = ok and meets == 4
    # other towers' fields are singlets of this tower's groups: index zero, b unchanged
    singlets = [(name, 1, 1, F(0)) for name, c, w, y in mirror]
    ok = ok and _b(ours + singlets, [HIGGS]) == b_ours
    ok = ok and _b(mirror + [(name, 1, 1, F(0)) for name, c, w, y in ours], [HIGGS]) == b_mirror
    GA.check("mirror listing gives the same b and the same (non-)meeting; no cross-tower contribution", ok)
    return ok
