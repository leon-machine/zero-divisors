"""standard-model.space-symmetric-doublet-mass-forms-two: exact checks.

Module, pairing, forms, T_GJ from the EXPORTS of families.doublet-direction-module-georgi-jarlskog-clebsch;
species from Hypothesis (S).
(1) All 512 odd normal-ordered monomials v_S w_T in the ten mode operators are enumerated; those that are
    ad-eigenvectors with hypercharge -1/2 and T_3 = -1/2 are kept; the su(3)-invariant part of their span is
    computed as an exact kernel (dimension 8); the symmetrised forms Y_T on the sixteen of a basis of it span
    exactly 2 dimensions, contain the forms of w_4 and of T_GJ, and couple no species pair other than
    (L, e^c), (Q, d^c). The 10 form has |y_e / y_d| = 1, the T_GJ form 3.
(2) The ratio is free: on every coupled entry the T_GJ form is the 10 form times -1 (lepton pair) or +1/3
    (quark pair), so alpha Y_{w_4} + beta Y_{T_GJ} has y_e / y_d = (alpha - beta) / (alpha + beta / 3); for
    sample target ratios r (module level, including 0 and negative values) the solved (alpha, beta) gives r
    entry by entry, and f_10 + f_GJ kills (L, e^c) while keeping (Q, d^c).
EXPORTS["doublet_forms"](module) returns (odd monomials, invariant doublet operators, their symmetric forms).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

TARGETS = [F(0), F(2), F(-5), F(7, 4), F(1, 3)]


def _module():
    return premise("families.doublet-direction-module-georgi-jarlskog-clebsch")["module"]


def monomials(M, parity):
    out = []
    subsets = [S for k in range(6) for S in combinations(range(5), k)]
    for S in subsets:
        for T in subsets:
            if (len(S) + len(T)) % 2 == parity:
                ops = [M["V"][m] for m in S] + [M["W"][m] for m in T]
                X = M["mm"](M["ONE"], *ops)
                if X:
                    out.append(X)
    return out


def doublet_forms(M):
    mons = monomials(M, 1)
    sel = [X for X in mons if M["op_weight"](M["HYP"], X) == F(-1, 2) and M["op_weight"](M["T3"], X) == F(-1, 2)]
    imgs = []
    for X in sel:
        out = {}
        for gi, g in enumerate(M["SU3"]):
            for k, x in M["comm"](g, X).items():
                out[(gi,) + k] = x
        imgs.append(out)
    _, ker = M["kernel"](imgs)
    inv = [M["madd"](*[M["msc"](x, sel[i]) for i, x in c.items()]) for c in ker]
    return mons, inv, [M["sym"](M["form"](X)) for X in inv]


EXPORTS = {"doublet_forms": doublet_forms}


def check_two_dimensional_space():
    M = _module()
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    premise("standard-model.hyp-s-slot-statistics")
    mons, inv, forms = doublet_forms(M)
    rank = M["rank"]
    ok = len(mons) == 512 and len(inv) == 8
    f10 = M["sym"](M["form"](M["W"][3]))
    fGJ = M["sym"](M["form"](M["T_GJ"]()))
    ok = ok and rank(forms) == 2 and rank(forms + [f10, fGJ]) == 2 and rank([f10, fGJ]) == 2
    pairs = {tuple(sorted((M["species"](s), M["species"](t)))) for f in forms for (s, t) in f}
    ok = ok and pairs == {("L", "ec"), ("Q", "dc")}
    for f, r in ((f10, 1), (fGJ, 3)):
        cl = M["clebsch"](f)
        ye, yd = {abs(x) for x in cl[("L", "ec")]}, {abs(x) for x in cl[("Q", "dc")]}
        ok = ok and len(ye) == 1 and len(yd) == 1 and ye.pop() == r * yd.pop()
    GA.check("symmetric odd colour-singlet doublet forms span exactly two dimensions: the 10 and T_GJ", ok)
    return ok


def check_ratio_is_free():
    M = _module()
    premise("standard-model.hyp-s-slot-statistics")
    f10 = M["form"](M["W"][3])
    fGJ = M["form"](M["T_GJ"]())
    lep = [k for k in f10 if {M["species"](k[0]), M["species"](k[1])} == {"L", "ec"}]
    qrk = [k for k in f10 if {M["species"](k[0]), M["species"](k[1])} == {"Q", "dc"}]
    ok = set(fGJ) == set(f10) and len(lep) == 2 and len(qrk) == 6
    ok = ok and all(fGJ[k] == -f10[k] for k in lep) and all(fGJ[k] == F(1, 3) * f10[k] for k in qrk)
    s = M["madd"](f10, fGJ)
    ok = ok and all(k not in s for k in lep) and all(s[k] == F(4, 3) * f10[k] for k in qrk)
    for r in TARGETS:
        beta = F(1)
        alpha = (1 + r / 3) / (1 - r)
        comb = M["madd"](M["msc"](alpha, f10), M["msc"](beta, fGJ))
        e = {comb.get(k, 0) / f10[k] for k in lep}
        d = {comb.get(k, 0) / f10[k] for k in qrk}
        ok = ok and len(e) == 1 and len(d) == 1 and e.pop() == r * d.pop()
    GA.check("alpha Y_10 + beta Y_GJ reaches every sampled ratio y_e/y_d; Y_10 + Y_GJ kills (L, e^c)", ok)
    return ok
