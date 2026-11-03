"""standard-model.neutrino-dirac-matrix-charged-fermions: exact checks on complex rational matrices.

The Clebsch structure of the imported Fact: two 10s (Y1, Y2 symmetric), one 126 (f symmetric), one
120 (h antisymmetric), complex vevs (Gaussian rationals, GA.QI), 3 x 3 family matrices:
  M_u = sum v_u^a Y_a + w_u f + c_u h,   M_nu = sum v_u^a Y_a - 3 w_u f + c_nu h,
  M_d = sum v_d^a Y_a + w_d f + c_d h,   M_e  = sum v_d^a Y_a - 3 w_d f + c_e h.
(1) No 120: M_d - M_e = 4 w_d f and M_u - M_nu = 4 w_u f (the 10s cancel; the 126 leaves 1 - (-3) = 4).
(2) Premise (EW): the data are built with 4 w_u f_33 = m_t and (M_nu)_33 = 0 (one entry of Y1 solved
    for), so (M_u)_33 = m_t; then M_nu = M_u - m_t fhat with fhat = (M_d - M_e)/(M_d - M_e)_33, and the
    Majorana matrix M_R = v_R f is v_R f_33 fhat (fixed up to its scale). A second parameter set with
    the same M_u, M_d, M_e (rescaled 126 couplings f -> f/2, w -> 2w, and the 10s split as Y1' = Y1 + Y2)
    gives the same M_nu: the neutrino Dirac matrix is fixed by the charged fermions.
(3) With a 120: the differences become 4 w_d f + (c_d - c_e) h and 4 w_u f + (c_u - c_nu) h, and
    changing c_nu alone leaves M_u, M_d, M_e unchanged while M_nu moves: M_nu is no longer fixed.
"""
from fractions import Fraction as F

import GA
from GA import QI
from tp_premise import premise


def q(a, b=0):
    return QI(F(a), F(b))


Y1 = [[q(1, 1), q(2), q(0, -1)], [q(2), q(3, -2), q(1)], [q(0, -1), q(1), q(5)]]
Y2 = [[q(F(1, 2)), q(0, 1), q(-1)], [q(0, 1), q(2, 2), q(0)], [q(-1), q(0), q(F(1, 3), 1)]]
FM = [[q(1), q(F(1, 4), -1), q(2)], [q(F(1, 4), -1), q(-3), q(0, 2)], [q(2), q(0, 2), q(7, 1)]]
HM = [[q(0), q(1, 1), q(-2)], [q(-1, -1), q(0), q(3, F(1, 2))], [q(2), q(-3, F(-1, 2)), q(0)]]
VU = (q(2, -1), q(F(1, 3), 4))
VD = (q(-1, F(1, 2)), q(3))
WD = q(F(2, 5), -1)
CS = {"u": q(1, -2), "nu": q(F(-1, 3)), "d": q(0, 5), "e": q(2, 2)}
MT = q(F(17257, 100))
VR = q(F(4154, 1) * 10 ** 7)


def lin(*terms):
    out = [[q(0)] * 3 for _ in range(3)]
    for c, M in terms:
        out = [[out[i][j] + c * M[i][j] for j in range(3)] for i in range(3)]
    return out


def masses(Y, vu, vd, f, wu, wd, h, cs):
    Mu = lin((vu[0], Y[0]), (vu[1], Y[1]), (wu, f), (cs["u"], h))
    Mnu = lin((vu[0], Y[0]), (vu[1], Y[1]), (q(-3) * wu, f), (cs["nu"], h))
    Md = lin((vd[0], Y[0]), (vd[1], Y[1]), (wd, f), (cs["d"], h))
    Me = lin((vd[0], Y[0]), (vd[1], Y[1]), (q(-3) * wd, f), (cs["e"], h))
    return Mu, Mnu, Md, Me


def ew_data():
    """Data with 4 w_u f33 = m_t and (M_nu)33 = 0, solving for (Y1)33 (no 120)."""
    wu = MT / (q(4) * FM[2][2])
    y1 = [row[:] for row in Y1]
    y1[2][2] = (q(3) * wu * FM[2][2] - VU[1] * Y2[2][2]) / VU[0]
    return y1, wu


def check_differences_without_120():
    premise("standard-model.imported-clebsch-structure-seesaw")
    ok = True
    zero = {k: q(0) for k in CS}
    wu = q(F(-3, 2), 1)
    Mu, Mnu, Md, Me = masses((Y1, Y2), VU, VD, FM, wu, WD, HM, zero)
    ok = ok and lin((q(1), Md), (q(-1), Me)) == lin((q(4) * WD, FM))
    ok = ok and lin((q(1), Mu), (q(-1), Mnu)) == lin((q(4) * wu, FM))
    GA.check("no 120: M_d - M_e = 4 w_d f and M_u - M_nu = 4 w_u f", ok)
    return ok


def check_neutrino_matrix_fixed_under_ew():
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.premise-ew-equal-weight")
    ok = True
    zero = {k: q(0) for k in CS}
    y1, wu = ew_data()
    Mu, Mnu, Md, Me = masses((y1, Y2), VU, VD, FM, wu, WD, HM, zero)
    ok = ok and q(4) * wu * FM[2][2] == MT and Mnu[2][2] == q(0) and Mu[2][2] == MT
    diff = lin((q(1), Md), (q(-1), Me))
    fhat = [[x / diff[2][2] for x in row] for row in diff]
    ok = ok and Mnu == lin((q(1), Mu), (-MT, fhat))
    MR = [[VR * x for x in row] for row in FM]
    ok = ok and MR == [[VR * FM[2][2] * x for x in row] for row in fhat]
    # a second parameter set with the same charged matrices
    f2 = [[x / q(2) for x in row] for row in FM]
    y1b = lin((q(1), y1), (q(1), Y2))                      # 10s split differently: Y1' = Y1 + Y2
    vub = (VU[0], VU[1] - VU[0])
    vdb = (VD[0], VD[1] - VD[0])
    Mu2, Mnu2, Md2, Me2 = masses((y1b, Y2), vub, vdb, f2, q(2) * wu, q(2) * WD, HM, zero)
    ok = ok and (Mu2, Md2, Me2) == (Mu, Md, Me) and Mnu2 == Mnu
    GA.check("(EW): M_nu = M_u - m_t fhat, M_R proportional to fhat, the same M_nu from a second parameter set", ok)
    return ok


def check_120_unfixes_neutrino_matrix():
    premise("standard-model.imported-clebsch-structure-seesaw")
    ok = True
    wu = q(F(-3, 2), 1)
    Mu, Mnu, Md, Me = masses((Y1, Y2), VU, VD, FM, wu, WD, HM, CS)
    ok = ok and lin((q(1), Md), (q(-1), Me)) == lin((q(4) * WD, FM), (CS["d"] - CS["e"], HM))
    ok = ok and lin((q(1), Mu), (q(-1), Mnu)) == lin((q(4) * wu, FM), (CS["u"] - CS["nu"], HM))
    cs2 = dict(CS)
    cs2["nu"] = CS["nu"] + q(1)
    Mu2, Mnu2, Md2, Me2 = masses((Y1, Y2), VU, VD, FM, wu, WD, HM, cs2)
    ok = ok and (Mu2, Md2, Me2) == (Mu, Md, Me) and Mnu2 != Mnu
    ok = ok and lin((q(1), Mnu2), (q(-1), Mnu)) == HM
    GA.check("with a 120 the differences gain (c_d - c_e) h, (c_u - c_nu) h, and M_nu is no longer fixed", ok)
    return ok
