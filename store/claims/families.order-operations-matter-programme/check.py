"""families.order-operations-matter-programme: exact checks of the computable core.

Module, forms, B - L, chi, T_GJ and the Cl(5,5) model from the EXPORTS of
families.doublet-direction-module-georgi-jarlskog-clebsch; the space of symmetric doublet forms from the EXPORTS
of standard-model.space-symmetric-doublet-mass-forms-two; species from (S). The ordering of the programme and
the reading of the capstone's table are argument, not computed.
(1) Family breaking first fails: a 10 vev tensored with a generic family matrix F gives M_e and M_d with equal
    singular invariants (m_mu = m_s, m_e = m_d), for two sample F.
(2) The factor is available only in the T_GJ direction: the symmetric doublet forms span two dimensions,
    spanned by the 10 form (ratio 1) and the T_GJ form (ratio 3). A two-term coupling alpha w_4 + beta T_GJ
    tensored with F gives M_e M_e^T = r^2 M_d M_d^T with r = (alpha - beta)/(alpha + beta/3) for every F: the one
    coefficient ratio fixes m_mu/m_s and m_e/m_d jointly.
(3) The second source: the one-sided weighting w_4 (B - L) has an antisymmetric form, so with a diagonal family
    matrix its combined form has zero symmetric part (no one-family mass), while with an antisymmetric family
    matrix the combined form is symmetric and nonzero only between families.
(4) Both sources carry the pair-number current: every GA blade of T_GJ and of w_4 (B - L) contains exactly one
    pair-mode bivector e_{2i} e_{2i+1}, and w_4 (B - L) = -2/3 w_4 sum_i v_i ^ w_i.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

FAMS = [[[F(2), F(1, 3), F(-1)], [F(0), F(5, 7), F(4)], [F(-1), F(3), F(1, 2)]],
        [[F(3), F(-1), F(2)], [F(1, 2), F(0), F(1)], [F(-4), F(2, 3), F(5)]]]
COEFFS = [(F(1), F(1, 2)), (F(-2), F(5)), (F(3, 4), F(-1, 3))]
DIAG = [[F(1), F(0), F(0)], [F(0), F(4), F(0)], [F(0), F(0), F(-2)]]
ANTI = [[F(0), F(1), F(-2)], [F(-1), F(0), F(3)], [F(2), F(-3), F(0)]]


def _module():
    return premise("families.doublet-direction-module-georgi-jarlskog-clebsch")["module"]


def gram(A):
    return [[sum(A[i][k] * A[j][k] for k in range(3)) for j in range(3)] for i in range(3)]


def sc(c, A):
    return [[c * x for x in r] for r in A]


def combined(f, A):
    return {((s, i), (t, j)): x * A[i][j] for (s, t), x in f.items() for i in range(3) for j in range(3) if A[i][j]}


def check_family_breaking_first_fails():
    M = _module()
    premise("families.imported-tree-relations-family-no-go")
    premise("standard-model.hyp-s-slot-statistics")
    cl = M["clebsch"](M["form"](M["W"][3]))
    ok = len(cl[("L", "ec")]) >= 1 and {abs(x) for x in cl[("L", "ec")] | cl[("Q", "dc")]} == {1}
    for Fm in FAMS:
        ok = ok and all(gram(sc(ye, Fm)) == gram(sc(yd, Fm)) for ye in cl[("L", "ec")] for yd in cl[("Q", "dc")])
    GA.check("family matrix acting on a 10 vev: M_e M_e^T = M_d M_d^T", ok)
    return ok


def check_two_term_structure_fixes_both_ratios():
    M = _module()
    premise("standard-model.space-symmetric-doublet-mass-forms-two")
    premise("standard-model.hyp-s-slot-statistics")
    _, _, forms = premise("standard-model.space-symmetric-doublet-mass-forms-two")["doublet_forms"](M)
    f10 = M["form"](M["W"][3])
    fGJ = M["form"](M["T_GJ"]())
    ok = M["rank"](forms) == 2 and M["rank"](forms + [M["sym"](f10), M["sym"](fGJ)]) == 2
    lep = [k for k in f10 if {M["species"](k[0]), M["species"](k[1])} == {"L", "ec"}]
    qrk = [k for k in f10 if {M["species"](k[0]), M["species"](k[1])} == {"Q", "dc"}]
    for al, be in COEFFS:
        comb = M["madd"](M["msc"](al, f10), M["msc"](be, fGJ))
        e = {comb[k] / f10[k] for k in lep}
        d = {comb[k] / f10[k] for k in qrk}
        ok = ok and e == {al - be} and d == {al + be / 3}
        r = (al - be) / (al + be / 3)
        for Fm in FAMS:
            ok = ok and gram(sc(al - be, Fm)) == [[r * r * x for x in row] for row in gram(sc(al + be / 3, Fm))]
    GA.check("alpha w4 + beta T_GJ: y_e/y_d = (alpha - beta)/(alpha + beta/3), the same ratio in every family", ok)
    return ok


def check_one_sided_source_between_families():
    M = _module()
    premise("families.imported-grade-three-direction-between-families")
    premise("standard-model.hyp-s-slot-statistics")
    f = M["form"](M["mm"](M["W"][3], M["BL"]))
    ok = f != {} and M["meq"](f, M["msc"](-1, M["ftr"](f)))
    D = combined(f, DIAG)
    ok = ok and D != {} and all(D.get((b, a)) == -x for (a, b), x in D.items())
    A = combined(f, ANTI)
    ok = ok and all(A.get((b, a)) == x for (a, b), x in A.items()) and all(a[1] != b[1] for (a, b) in A)
    ok = ok and len({(a[1], b[1]) for (a, b) in A}) == 6
    GA.check("one-sided weighting: no one-family mass, symmetric entries only between families", ok)
    return ok


def check_both_sources_carry_pair_number():
    M = _module()
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    pairs = [(2 * i, 2 * i + 1) for i in M["PAIRS"]]
    one_sided = M["gmul"](M["gw"](3), M["ga_BL"]())
    pairbiv = GA.add(*[M["gwedge2"](M["gv"](i), M["gw"](i)) for i in M["PAIRS"]])
    ok = GA.eq(one_sided, GA.scal(F(-2, 3), M["gmul"](M["gw"](3), pairbiv)))
    for x in (M["ga_TGJ"](), one_sided):
        ok = ok and x != {} and all(sum(1 for p in pairs if set(p) <= set(bl)) == 1 for bl in x)
    GA.check("T_GJ and w4 (B-L) both carry the pair-sector u(1) generator sum v_i^w_i", ok)
    return ok
