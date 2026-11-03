"""standard-model.grade-three-georgi-jarlskog-direction: exact checks.

Module, pairing, species and the Cl(5,5) model come from the EXPORTS of
families.doublet-direction-module-georgi-jarlskog-clebsch (which defines B - L, chi and T_GJ).
(1) w_4 (B - L) and v_4 (B - L) are pure grade three in GA's Cl(5,5) (no grade 1, no grade 5), and their
    matrix images are the module operators w_4 (1 - 2/3 N_W), v_4 (1 - 2/3 N_W). That grade three is the 120
    is the imported spinor-bilinear Fact, not recomputed.
(2) Their mass forms on the sixteen are nonzero and antisymmetric; they couple exactly (L, e^c), (Q, d^c),
    respectively (L, nu^c), (Q, u^c), each pair with a single entry magnitude, lepton : quark = 3.
(3) With a sample antisymmetric 3 x 3 family matrix A (module level), the combined form
    Y((s, f), (t, g)) = Y(s, t) A[f][g] on 16 x 3 is symmetric, zero on every family-diagonal block f = g and
    nonzero off it; control: a symmetric family matrix gives a combined form that is not symmetric.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

FAM_A = [[F(0), F(2), F(-5, 3)], [F(-2), F(0), F(7)], [F(5, 3), F(-7), F(0)]]
FAM_S = [[F(1), F(2), F(-5, 3)], [F(2), F(4), F(7)], [F(-5, 3), F(7), F(3, 2)]]


def _module():
    return premise("families.doublet-direction-module-georgi-jarlskog-clebsch")["module"]



def combined(M, f, A):
    return {((s, i), (t, j)): x * A[i][j] for (s, t), x in f.items() for i in range(3) for j in range(3) if A[i][j]}


def check_one_sided_weightings_grade_three():
    M = _module()
    premise("standard-model.imported-spinor-bilinears")
    ok = True
    for gx, X in ((M["gw"](3), M["W"][3]), (M["gv"](3), M["V"][3])):
        t = M["gmul"](gx, M["ga_BL"]())
        ok = ok and M["grades"](t) == [3] and M["gpart"](t, 1) == {} and M["gpart"](t, 5) == {}
        ok = ok and M["meq"](M["to_mat"](t), M["mm"](X, M["BL"]))
    GA.check("w4 (B-L) and v4 (B-L) are pure grade three", ok)
    return ok


def check_forms_antisymmetric_ratio_three():
    M = _module()
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for X, lep, qrk in ((M["W"][3], ("L", "ec"), ("Q", "dc")), (M["V"][3], ("L", "nuc"), ("Q", "uc"))):
        f = M["form"](M["mm"](X, M["BL"]))
        cl = M["clebsch"](f)
        ok = ok and f != {} and M["meq"](f, M["msc"](-1, M["ftr"](f)))
        ok = ok and set(cl) == {lep, qrk}
        ml, mq = {abs(x) for x in cl[lep]}, {abs(x) for x in cl[qrk]}
        ok = ok and len(ml) == 1 and len(mq) == 1 and ml.pop() == 3 * mq.pop()
    GA.check("one-sided weightings: antisymmetric forms on (L,e^c),(Q,d^c) / (L,nu^c),(Q,u^c), moduli ratio 3", ok)
    return ok


def check_antisymmetric_family_matrix_off_diagonal():
    M = _module()
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for X in (M["W"][3], M["V"][3]):
        f = M["form"](M["mm"](X, M["BL"]))
        Y = combined(M, f, FAM_A)
        ok = ok and Y != {} and all(Y.get((b, a)) == x for (a, b), x in Y.items())
        ok = ok and all(a[1] != b[1] for (a, b) in Y)
        ok = ok and {(a[1], b[1]) for (a, b) in Y} == {(i, j) for i in range(3) for j in range(3) if i != j}
        Z = combined(M, f, FAM_S)
        ok = ok and any(Z.get((b, a)) != x for (a, b), x in Z.items())
    GA.check("with an antisymmetric family matrix the form is symmetric and vanishes on the family diagonal", ok)
    return ok
