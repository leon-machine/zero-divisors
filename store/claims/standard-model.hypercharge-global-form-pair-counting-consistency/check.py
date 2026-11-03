"""standard-model.hypercharge-global-form-pair-counting-consistency: exact checks.

Weights come from the hypercharge generator y = (3i I_2, -2i I_3) acting on the component (j, k) of the five-mode
state space (j slot modes, k pair modes occupied) by the sum of its eigenvalues over occupied modes: q(j, k) =
3j - 2k, Y = q/6. Anomaly sums (Fact imported-anomaly-coefficients, left-handed Weyl content, overall index
factors dropped): [SU(3)]^2 U(1) = sum over coloured multiplets of (SU(2) dim) Y, [SU(2)]^2 U(1) = sum over
doublets of (colour dim) Y, gravitational = sum dim Y, cubic = sum dim Y^3.
(1) Q = (1,1) has q = 1 (Y_Q = 1/6), the full doublet (1,3) q = -3, the empty one (1,0) q = +3; their total mode
    numbers 2, 4, 1: the even listing keeps Q and the full doublet. 3 Y_Q + Y_L = 0 for Y_L = -1/2 and 1 for +1/2;
    |Y_L / Y_Q| = 3.
(2) One-handed listing of the single-spinor sector (the (0, k) components, weight -2k equal to the grade-k weight
    of Lambda^k W): grades 0, 2 kept, 1, 3 conjugated: nu^c, u^c, d^c, e^c = 0, -2/3, 1/3, 1.
(3) All four sums vanish on the derived spectrum, with nu^c at 0 or absent. Uniqueness: with Y_Q = 1/6 the
    [SU(2)]^2 condition gives Y_L = -1/2, [SU(3)]^2 gives Y_u + Y_d = -1/3, gravity gives Y_e = 1, and the cubic
    condition with Y_d = -1/3 - Y_u is a polynomial in Y_u equal to a nonzero multiple of (y - 1/3)(y + 2/3)
    (computed as exact polynomials), so {Y_u, Y_d} = {1/3, -2/3}. Necessity: with a free fourth singlet the
    family Y + t(B - L) satisfies all four sums identically in t (cubic in t, zero at five points), with
    nu^c = t != 0; doublets listed in the opposite handedness give sums (-2/3, 0, 0, 4/9); without the lepton
    doublet the sums are (0, 1/2, 1, 1/4).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
XY = [QI(0, 3), QI(0, 3)]
YY = [QI(0, -2), QI(0, -2), QI(0, -2)]
T_SAMPLES = [F(0), F(1), F(-1), F(2), F(5, 7)]


def _q(j, k):
    """Weight of the component (j, k), from the generator's diagonal (all j-, k-subsets give the same sum)."""
    w = sum((XY[i] for i in range(j)), QI(0)) + sum((YY[i] for i in range(k)), QI(0))
    return w.im


def _Y(j, k):
    return F(_q(j, k), 6)


def _sums(YQ, Yu, Yd, YL, Ye, Yn=None):
    """Content Q(2,3), u^c(1,3b), d^c(1,3b), L(2,1) (YL None: absent), e^c(1,1), nu^c(1,1) (None: absent)."""
    su3 = 2 * YQ + Yu + Yd
    su2 = 3 * YQ + (YL if YL is not None else 0)
    grav = 6 * YQ + 3 * Yu + 3 * Yd + (2 * YL if YL is not None else 0) + Ye + (Yn or 0)
    cub = (6 * YQ ** 3 + 3 * Yu ** 3 + 3 * Yd ** 3 + (2 * YL ** 3 if YL is not None else 0) + Ye ** 3
           + (Yn ** 3 if Yn is not None else 0))
    return (su3, su2, grav, cub)


def _spectrum():
    YQ, YL = _Y(1, 1), _Y(1, 3)
    sing = {k: (_Y(0, k) if k % 2 == 0 else -_Y(0, k)) for k in range(4)}
    return YQ, sing[2], sing[1], YL, sing[3], sing[0]


def check_orientation_fixed_by_anomaly():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.imported-anomaly-coefficients")
    YQ, Yfull, Yempty = _Y(1, 1), _Y(1, 3), _Y(1, 0)
    ok = (YQ, Yfull, Yempty) == (F(1, 6), F(-1, 2), F(1, 2))
    ok = ok and [(1 + 1) % 2, (1 + 3) % 2, (1 + 0) % 2] == [0, 0, 1]
    ok = ok and 3 * YQ + Yfull == 0 and 3 * YQ + Yempty == 1
    ok = ok and abs(Yfull / YQ) == 3 and _q(0, 3) - _q(0, 0) == -6
    GA.check("Y_Q = 1/6, Y_L = -1/2 (even listing); 3 Y_Q + Y_L = 0, and 1 for the empty doublet", ok)
    return ok


def check_one_handed_singlet_spectrum():
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    premise("standard-model.chirality-two-halves-spinor-module-conjugation")
    YQ, Yu, Yd, YL, Ye, Yn = _spectrum()
    ok = (Yn, Yu, Yd, Ye) == (F(0), F(-2, 3), F(1, 3), F(1))
    # grade-k weight of Lambda^k W (C^3 eigenvalues alone) equals the (0, k) component weight -2k
    ok = ok and all(_q(0, k) == -2 * k for k in range(4))
    GA.check("one-handed listing: nu^c, u^c, d^c, e^c = 0, -2/3, 1/3, 1", ok)
    return ok


def check_anomaly_free_and_unique():
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    premise("standard-model.hyp-s-slot-statistics")
    YQ, Yu, Yd, YL, Ye, Yn = _spectrum()
    ok = _sums(YQ, Yu, Yd, YL, Ye, Yn) == (0, 0, 0, 0) and _sums(YQ, Yu, Yd, YL, Ye, None) == (0, 0, 0, 0)
    q = F(1, 6)
    YL_f = -3 * q
    s = -2 * q
    Ye_f = -(6 * q + 2 * YL_f + 3 * s)
    # cubic with y = Y_u, Y_d = s - y:  6q^3 + 3y^3 + 3(s - y)^3 + 2 YL^3 + Ye^3
    y = [F(0), F(1)]
    sy = [s, F(-1)]
    cube = lambda p: GA.pmul(GA.pmul(p, p), p)
    P = GA.padd(GA.padd(GA.pmul([F(3)], cube(y)), GA.pmul([F(3)], cube(sy))),
                GA.pconst(6 * q ** 3 + 2 * YL_f ** 3 + Ye_f ** 3))
    roots = GA.pmul([F(-1, 3), F(1)], [F(2, 3), F(1)])
    quo, rem = GA.pdivmod(P, roots)
    ok = ok and (YL_f, s, Ye_f) == (F(-1, 2), F(-1, 3), F(1)) and len(P) == 3 and rem == [] and len(quo) == 1
    ok = ok and {Yu, Yd} == {F(1, 3), F(-2, 3)} and GA.peval(P, Yu) == 0 and GA.peval(P, Yd) == 0
    GA.check("all four sums vanish; given the content they force Y_L = -1/2, Y_e = 1, {Y_u, Y_d} = {1/3, -2/3}", ok)
    return ok


def check_hypotheses_necessary():
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.hyp-s-slot-statistics")
    YQ, Yu, Yd, YL, Ye, Yn = _spectrum()
    BL = (F(1, 3), F(-1, 3), F(-1, 3), F(-1), F(1), F(1))
    SM = (YQ, Yu, Yd, YL, Ye, Yn)
    ok = True
    for t in T_SAMPLES:
        Yt = tuple(a + t * b for a, b in zip(SM, BL))
        ok = ok and _sums(*Yt) == (0, 0, 0, 0) and (t == 0 or Yt[5] != 0)
        if Yt[0] != 0:
            Ys = tuple(YQ / Yt[0] * x for x in Yt)
            ok = ok and _sums(*Ys) == (0, 0, 0, 0)
    ok = ok and _sums(F(1, 6), F(-1, 6), F(-1, 6), F(-1, 2), F(1, 2), F(1, 2)) == (0, 0, 0, 0)
    ok = ok and _sums(-YQ, Yu, Yd, -YL, Ye, Yn) == (F(-2, 3), 0, 0, F(4, 9))
    ok = ok and _sums(YQ, Yu, Yd, None, Ye, Yn) == (0, F(1, 2), 1, F(1, 4))
    GA.check("free fourth singlet: a one-parameter family; flipped doublets: (-2/3, 0, 0, 4/9); no L: (0, 1/2, 1, 1/4)",
             ok)
    return ok
