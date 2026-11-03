"""standard-model.no-go-frozen-point-lifts-do: exact checks.

Module, pairing, forms and T_GJ come from the EXPORTS of families.doublet-direction-module-georgi-jarlskog-clebsch.
I = a v_1 + b w_1 (code mode 0), c_4 = -w_4 + lambda v_4, c_5 = -w_5, as 32 x 32 operators, at four sample
(a, b, lambda) including lambda = 0 and b = 0 (module level).
(1) I^2 = ab, c_4^2 = -lambda, c_5^2 = 0, pairwise anticommuting; the unital algebra they generate, computed
    as the closure of span{1} under right multiplication by the generators, has dimension 8 and is spanned by
    the eight listed products; its odd part (products changing the occupation parity) is
    span{I, c_4, c_5, I c_4 c_5}, of dimension 4.
(2) At the generic sample: c_4 and c_5 commute with all of su(3), I and I c_4 c_5 do not (v_1 w_2 fails); the
    su(3)-invariant part of the odd span, computed as a kernel, is 2-dimensional and equals span{c_4, c_5},
    inside the span of the ten mode operators (grade one, the 10); the colour-singlet part of the whole
    algebra is 4-dimensional; c_5 has hypercharge -1/2 and c_4 none (lambda != 0). T_GJ is not in the algebra,
    its mass form is not in the span of the invariant part's forms (which lie in the span of the forms of the
    four rung mode vectors, the 10), and sum_i v_i ^ w_i is not in the algebra.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SAMPLES = [(F(2), F(3), F(1, 7)), (F(1), F(-1), F(0)), (F(5), F(0), F(-2)), (F(-3), F(4, 3), F(5, 2))]
GENERIC = SAMPLES[0]


def _module():
    return premise("families.doublet-direction-module-georgi-jarlskog-clebsch")["module"]


def gens(M, a, b, lam):
    I = M["madd"](M["msc"](a, M["V"][0]), M["msc"](b, M["W"][0]))
    c4 = M["madd"](M["msc"](-1, M["W"][3]), M["msc"](lam, M["V"][3]))
    c5 = M["msc"](-1, M["W"][4])
    return I, c4, c5


def closure(M, gs):
    basis = [M["ONE"]]
    grown = True
    while grown:
        grown = False
        for X in list(basis):
            for g in gs:
                Y = M["mm"](X, g)
                if M["rank"](basis + [Y]) > len(basis):
                    basis.append(Y)
                    grown = True
    return basis


def odd(M, X):
    return all((M["ntot"](r) + M["ntot"](c)) % 2 == 1 for (r, c) in X)


def check_algebra_is_eight_dimensional():
    M = _module()
    premise("standard-model.transported-frozen-point")
    ok = True
    mm, ONE, msc = M["mm"], M["ONE"], M["msc"]
    for a, b, lam in SAMPLES:
        I, c4, c5 = gens(M, a, b, lam)
        ok = ok and M["meq"](mm(I, I), msc(a * b, ONE)) and M["meq"](mm(c4, c4), msc(-lam, ONE))
        ok = ok and mm(c5, c5) == {}
        ok = ok and all(M["acomm"](x, y) == {} for x, y in ((I, c4), (I, c5), (c4, c5)))
        alg = closure(M, [I, c4, c5])
        listed = [ONE, I, c4, c5, mm(I, c4), mm(I, c5), mm(c4, c5), mm(I, c4, c5)]
        ok = ok and len(alg) == 8 and M["rank"](listed) == 8 and M["rank"](alg + listed) == 8
        odds = [X for X in listed if odd(M, X)]
        ok = ok and len(odds) == 4 and M["rank"](odds) == 4
        ok = ok and M["rank"](odds + [I, c4, c5, mm(I, c4, c5)]) == 4
    GA.check("I, c4, c5 generate an 8-dimensional algebra; odd part span{I, c4, c5, I c4 c5}", ok)
    return ok


def check_no_colour_singlet_doublet_beyond_ten():
    M = _module()
    premise("standard-model.transported-frozen-point")
    mm, comm, rank, kernel = M["mm"], M["comm"], M["rank"], M["kernel"]
    I, c4, c5 = gens(M, *GENERIC)
    SU3 = M["SU3"]

    def colour_image(X):
        out = {}
        for gi, g in enumerate(SU3):
            for k, x in comm(g, X).items():
                out[(gi,) + k] = x
        return out

    def combo(c, ops):
        return M["madd"](*[M["msc"](x, ops[i]) for i, x in c.items()])

    oddspan = [I, c4, c5, mm(I, c4, c5)]
    ok = all(comm(g, c4) == {} and comm(g, c5) == {} for g in SU3)
    v1w2 = mm(M["V"][0], M["W"][1])
    ok = ok and comm(v1w2, I) != {} and comm(v1w2, oddspan[3]) != {}
    _, ker = kernel([colour_image(X) for X in oddspan])
    inv = [combo(c, oddspan) for c in ker]
    ok = ok and len(inv) == 2 and rank(inv + [c4, c5]) == 2 and rank(inv + M["V"] + M["W"]) == 10
    listed = [M["ONE"], I, c4, c5, mm(I, c4), mm(I, c5), mm(c4, c5), mm(I, c4, c5)]
    _, ker_all = kernel([colour_image(X) for X in listed])
    ok = ok and len(ker_all) == 4
    ok = ok and M["op_weight"](M["HYP"], c5) == F(-1, 2) and M["op_weight"](M["HYP"], c4) is None
    TGJ = M["T_GJ"]()
    ok = ok and rank(listed + [TGJ]) == 9
    forms = [M["sym"](M["form"](X)) for X in inv]
    fGJ = M["sym"](M["form"](TGJ))
    ten = [M["sym"](M["form"](X)) for X in (M["V"][3], M["V"][4], M["W"][3], M["W"][4])]
    ok = ok and rank(forms) == 2 and rank(forms + ten) == rank(ten) == 4
    ok = ok and rank(forms + [fGJ]) == 3 and rank(ten + [fGJ]) == 5
    pairbiv = M["to_mat"](GA.add(*[M["gwedge2"](M["gv"](i), M["gw"](i)) for i in M["PAIRS"]]))
    ok = ok and rank(listed + [pairbiv]) == 9
    GA.check("colour-singlet odd part is span{c4, c5} (the 10); T_GJ and sum v_i^w_i are outside the algebra", ok)
    return ok
