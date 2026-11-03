"""standard-model.equal-weight-module: exact checks.

Module, forms, B - L, chi, T_GJ and its up-type twin T^u = v_4 (B - L) chi from the EXPORTS of
families.doublet-direction-module-georgi-jarlskog-clebsch; the pairing matrix from the EXPORTS of
standard-model.invariant-pairing-five-modes (compared with the module's forms before use); the Majorana
element T = v_1 v_2 v_3 v_4 v_5 of standard-model.majorana-element; dagger is the transpose (real matrices).
(0) P = T^T T + T T^T is the projector onto span{|0> = nu^c, |full>} (P^2 = P, rank 2).
(1) The form of v_4 - (v_4 P + P v_4) equals the form of 3/4 (v_4 + T^u); it equals v_4's form on (Q, u^c) and has
    no (L, nu^c) entry; the form of w_4 - (w_4 P + P w_4) equals the form of w_4.
(2) On the sixteen (commutators restricted to columns in the sixteen; on the full module [w_4, P] != 0, so the
    restriction in the statement matters): [v_4, P] = -[T^u, P] != 0, so [a v_4 + a' T^u, P] = (a - a') [v_4, P] vanishes iff a' = a; T^u |nu^c> =
    -v_4 |nu^c> != 0, so a v_4 + a' T^u kills nu^c iff a' = a; [w_4, P] = [T_GJ, P] = 0. The iff is also run
    over a grid of sample (a, a') and (b, b') (module level).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

GRID = [(F(1), F(1)), (F(2), F(-3)), (F(-5, 2), F(-5, 2)), (F(0), F(4)), (F(7), F(0)), (F(1, 3), F(1, 3))]


def _module():
    return premise("families.doublet-direction-module-georgi-jarlskog-clebsch")["module"]


def projector(M):
    premise("standard-model.majorana-element")
    T = M["mm"](*[M["V"][m] for m in range(M["NM"])])
    return T, M["madd"](M["mm"](M["tr"](T), T), M["mm"](T, M["tr"](T)))


def check_projector_onto_nu_c_pair():
    M = _module()
    T, P = projector(M)
    ok = list(T) == [(M["DIM"] - 1, 0)]
    ok = ok and M["meq"](M["mm"](P, P), P) and P == {(0, 0): F(1), (31, 31): F(1)}
    ok = ok and M["species"](0) == "nuc"
    premise("standard-model.hyp-s-slot-statistics")
    GA.check("P = T^T T + T T^T projects onto nu^c and its conjugate", ok)
    return ok


def check_equal_weight_forms():
    M = _module()
    premise("standard-model.hyp-s-slot-statistics")
    pairing = premise("standard-model.invariant-pairing-five-modes")["pairing"]()
    mm, madd, msc, msub, meq, form = M["mm"], M["madd"], M["msc"], M["msub"], M["meq"], M["form"]
    # the pairing premise agrees with the module's form construction
    ok = all(pairing.get((s, M["complement"](s))) == M["bcoef"](s) for s in range(M["DIM"]))
    ok = ok and len(pairing) == M["DIM"]
    _, P = projector(M)
    v4, w4 = M["V"][3], M["W"][3]
    Tu = M["T_GJ_up"]()
    kept = msub(v4, madd(mm(v4, P), mm(P, v4)))
    ok = ok and meq(form(kept), msc(F(3, 4), form(madd(v4, Tu))))
    fk, fv = form(kept), form(v4)
    cl = M["clebsch"](fk)
    ok = ok and set(cl) == {("Q", "uc")}
    ok = ok and all(fk.get(k) == x for k, x in fv.items() if M["clebsch"]({k: x}).keys() == {("Q", "uc")})
    keptw = msub(w4, madd(mm(w4, P), mm(P, w4)))
    ok = ok and meq(form(keptw), form(w4))
    GA.check("v4 off the condensate has the form of 3/4 (v4 + T^u): equal weight, no (L, nu^c); w4 unchanged", ok)
    return ok


def check_commutes_iff_equal_weight():
    M = _module()
    premise("standard-model.hyp-s-slot-statistics")
    madd, msc, mm = M["madd"], M["msc"], M["mm"]
    six = set(M["SIXTEEN"])

    def comm(A, B):
        return {k: x for k, x in M["comm"](A, B).items() if k[1] in six}

    _, P = projector(M)
    v4, w4 = M["V"][3], M["W"][3]
    Tu, Td = M["T_GJ_up"](), M["T_GJ"]()
    cv, ct = comm(v4, P), comm(Tu, P)
    ok = cv != {} and M["meq"](ct, msc(-1, cv))
    vac = {(0, 0): F(1)}
    kv, kt = mm(v4, vac), mm(Tu, vac)
    ok = ok and kv != {} and M["meq"](kt, msc(-1, kv))
    ok = ok and comm(w4, P) == {} and comm(Td, P) == {} and M["comm"](w4, P) != {}
    for a, a2 in GRID:
        X = madd(msc(a, v4), msc(a2, Tu))
        ok = ok and (comm(X, P) == {}) == (a == a2) == (mm(X, vac) == {})
        Y = madd(msc(a, w4), msc(a2, Td))
        ok = ok and comm(Y, P) == {}
    GA.check("a v4 + a' T^u commutes with P iff a' = a iff it kills nu^c; b w4 + b' T_GJ always commutes", ok)
    return ok
