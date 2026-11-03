"""standard-model.what-direction-made: exact checks.

Module, pairing, forms, chi, B - L and T_GJ from the EXPORTS of
families.doublet-direction-module-georgi-jarlskog-clebsch; species and the N_W table from (S) and the
composites Proposition.
(1) On the sixteen, N_W is 1 on Q and 3 on L (rung-odd, N_R = 1) and 0, 2 on the rung-even species; B - L takes
    the four values {1, 1/3, -1/3, -1} while (-1)^{N_R} takes two.
(2) Symmetrised forms f(X) of X = w_4, w_4 N_W, w_4 chi, w_4 N_W chi: f(w_4 N_W) = 3/2 f(w_4); f(w_4 chi) = 0;
    f(w_4 N_W chi) couples (L, e^c) with |y_e| = 3/2 and (Q, d^c) with |y_d| = 1/2 and is not a multiple of
    f(w_4); T_GJ = w_4 chi - 2/3 w_4 N_W chi as operators, and f(T_GJ) = -2/3 f(w_4 N_W chi).
The last sentence of the statement (the pair number is outside every object of the mass mechanism derived in
the series) is a survey of the series and is not computed.
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
from tp_premise import premise


def _module():
    return premise("families.doublet-direction-module-georgi-jarlskog-clebsch")["module"]


def check_pair_number_table():
    M = _module()
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.hyp-s-slot-statistics")
    tab = {}
    for s in M["SIXTEEN"]:
        get_or_set(tab, M["species"](s), set()).add((M["nw"](s), M["nr"](s) % 2))
    ok = tab["Q"] == {(1, 1)} and tab["L"] == {(3, 1)}
    ok = ok and {next(iter(tab[x]))[0] for x in ("nuc", "uc", "ec", "dc")} == {0, 2}
    ok = ok and all(next(iter(tab[x]))[1] == 0 for x in ("nuc", "uc", "ec", "dc"))
    bl = {M["BL"][(s, s)] for s in M["SIXTEEN"]}
    parity = {M["CHI"][(s, s)] for s in M["SIXTEEN"]}
    ok = ok and bl == {F(1), F(1, 3), F(-1, 3), F(-1)} and len(parity) == 2
    GA.check("N_W: Q 1, L 3, rung-even 0 and 2; B - L four values, rung parity two", ok)
    return ok


def check_four_operators_forms():
    M = _module()
    premise("standard-model.hyp-s-slot-statistics")
    mm, sym, form, msc, meq = M["mm"], M["sym"], M["form"], M["msc"], M["meq"]
    w4, NW, CHI = M["W"][3], M["NW"], M["CHI"]
    f1 = sym(form(w4))
    f2 = sym(form(mm(w4, NW)))
    f3 = sym(form(mm(w4, CHI)))
    f4 = sym(form(mm(w4, NW, CHI)))
    ok = f1 != {} and meq(f2, msc(F(3, 2), f1)) and f3 == {}
    cl = M["clebsch"](f4)
    ok = ok and set(cl) == {("L", "ec"), ("Q", "dc")}
    ok = ok and {abs(x) for x in cl[("L", "ec")]} == {F(3, 2)} and {abs(x) for x in cl[("Q", "dc")]} == {F(1, 2)}
    ok = ok and M["rank"]([f1, f4]) == 2
    TGJ = M["T_GJ"]()
    ok = ok and meq(TGJ, M["msub"](mm(w4, CHI), msc(F(2, 3), mm(w4, NW, CHI))))
    ok = ok and meq(sym(form(TGJ)), msc(F(-2, 3), f4))
    GA.check("w4, w4 N_W give the 10 (3/2), w4 chi gives zero, w4 N_W chi gives the 126; f(T_GJ) = -2/3 f(w4 N_W chi)", ok)
    return ok
