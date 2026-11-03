"""rule2.rule-2-plane: exact checks in GA.

A3 = Cl(2,1): e_x = e0 (+1), e_y = e1 (+1), e_t = e2 (-1); omega = e_x e_y e_t.
(i)   omega is central with omega^2 = +1; eps_pm orthogonal idempotents summing to 1; each ideal eps_pm A3 has
      dimension 4 and a -> eps_pm a is multiplicative and injective on Cl^0(2,1); Cl^0(2,1) = Cl(2,0) = Mat_2(R)
      (e_x e_t and e_y e_t square to +1 and anticommute; (1 + e_x e_t)/2 is a non-central idempotent of
      Cl^0 with a 1-dimensional corner there); eps_+ e_t = -eps_+ e_x e_y and eps_- e_t = +eps_- e_x e_y;
      the reflection e_x -> -e_x equals grade involution after Ad_{e_x} on all blades, negates omega and
      exchanges eps_pm (outer: it moves the centre).
(ii)  Cl(3,1) (nu^2 = +1) and Cl(2,2) (nu^2 = -1), nu = e3: 2 x 2 matrix units from eps_pm and nu, corner
      eps_+ B eps_+ of dimension 4 (= Mat_2(R), so B = Mat_4(R)), centre R; Ad_nu is the grade involution
      and Ad_{nu e_x} the planar reflection on A3; (nu e_x)^2 = -1 in Cl(3,1), +1 in Cl(2,2); in Cl(3,1) the
      pair (nu, e_t) is a hyperbolic plane with a ladder pair whose projector commutes with Cl(2,0) and has
      corner dimension 4 (Rule 1 ascent of Cl(2,0)); residues 2 -> 1 -> 2 and 2 -> 1 -> 0.
(iii) Cl(1,2): omega central with omega^2 = -1, centre span(1, omega) (no central idempotent: no real
      splitting); (1 + e0)/2 is a non-central idempotent with corner of real dimension 2 (= C), so
      Cl(1,2) = Mat_2(C); over C, (1 +- i omega)/2 are orthogonal idempotents summing to 1 (computed with
      complex coefficients as pairs of real multivectors).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ONE = GA.sc(1)
SA = GA.sig(2, 1)
OMEGA = {(0, 1, 2): F(1)}
EX, EY, ET = GA.gen(0), GA.gen(1), GA.gen(2)
EXY = {(0, 1): F(1)}
EPP = GA.scal(F(1, 2), GA.add(ONE, OMEGA))
EPM = GA.scal(F(1, 2), GA.sub(ONE, OMEGA))
B3 = GA.all_blades(3)
EVEN3 = [b for b in B3 if len(b) % 2 == 0]


def bl(b):
    return {b: F(1)}


def span_rank(elems, n):
    blades = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in elems])


def reflect_x(x):
    return {b: (-c if 0 in b else c) for b, c in x.items()}


def residue(S):
    return (sum(1 for s in S if s == 1) - sum(1 for s in S if s == -1)) % 8


def check_planar_split_and_outer_reflection():
    premise("rule2.imported-classification-centre-type-c")
    premise("rule2.even-subalgebra-one-dimensional-extension")
    ok = all(GA.commutes(OMEGA, GA.gen(i), SA) for i in range(3)) and GA.eq(GA.mul(OMEGA, OMEGA, SA), ONE)
    ok = ok and GA.eq(GA.mul(EPP, EPP, SA), EPP) and GA.is_zero(GA.mul(EPP, EPM, SA))
    ok = ok and GA.eq(GA.add(EPP, EPM), ONE)
    for eps in (EPP, EPM):
        ok = ok and span_rank([GA.mul(eps, bl(b), SA) for b in B3], 3) == 4
        ok = ok and span_rank([GA.mul(eps, bl(b), SA) for b in EVEN3], 3) == 4
        for a in EVEN3:
            for b in EVEN3:
                ok = ok and GA.eq(GA.mul(GA.mul(eps, bl(a), SA), GA.mul(eps, bl(b), SA), SA),
                                  GA.mul(eps, GA.mul(bl(a), bl(b), SA), SA))
    g1, g2 = GA.mul(EX, ET, SA), GA.mul(EY, ET, SA)
    ok = ok and GA.eq(GA.mul(g1, g1, SA), ONE) and GA.eq(GA.mul(g2, g2, SA), ONE)
    ok = ok and GA.anticommutes(g1, g2, SA)
    idem = GA.scal(F(1, 2), GA.add(ONE, g1))
    ok = ok and GA.eq(GA.mul(idem, idem, SA), idem) and not GA.commutes(idem, g2, SA)
    ok = ok and span_rank([GA.mul(GA.mul(idem, bl(b), SA), idem, SA) for b in EVEN3], 3) == 1
    ok = ok and GA.eq(GA.mul(EPP, ET, SA), GA.neg(GA.mul(EPP, EXY, SA)))
    ok = ok and GA.eq(GA.mul(EPM, ET, SA), GA.mul(EPM, EXY, SA))
    exinv = EX                                    # e_x^2 = +1
    for b in B3:
        ok = ok and GA.eq(reflect_x(bl(b)), GA.grade_inv(GA.mul(GA.mul(EX, bl(b), SA), exinv, SA)))
    ok = ok and GA.eq(reflect_x(OMEGA), GA.neg(OMEGA)) and GA.eq(reflect_x(EPP), EPM)
    _tp_rv = (ok); assert _tp_rv is not False, "check_planar_split_and_outer_reflection"; return _tp_rv


def check_two_repairs_mat4r_inner_parity():
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    premise("rule2.where-obstruction-sits-commuting-square")
    ok = True
    sq = {}
    for s in (1, -1):
        S = SA + (s,)
        nu = GA.gen(3)
        nuinv = GA.scal(s, nu)
        E = {(1, 1): EPP, (2, 2): EPM, (1, 2): GA.mul(EPP, nu, S), (2, 1): GA.scal(s, GA.mul(EPM, nu, S))}
        for i in (1, 2):
            for j in (1, 2):
                for k in (1, 2):
                    for m in (1, 2):
                        ok = ok and GA.eq(GA.mul(E[(i, j)], E[(k, m)], S), E[(i, m)] if j == k else {})
        allb = [bl(b) for b in GA.all_blades(4)]
        ok = ok and span_rank([GA.mul(GA.mul(EPP, x, S), EPP, S) for x in allb], 4) == 4
        cb = [b for b in GA.all_blades(4) if all(GA.commutes(bl(b), GA.gen(i), S) for i in range(4))]
        ok = ok and cb == [()]
        u = GA.mul(nu, EX, S)
        u2 = GA.mul(u, u, S)
        sq[s] = u2
        uinv = GA.scal(u2[()], u)
        for b in B3:
            ok = ok and GA.eq(GA.mul(GA.mul(nu, bl(b), S), nuinv, S), GA.grade_inv(bl(b)))
            ok = ok and GA.eq(GA.mul(GA.mul(u, bl(b), S), uinv, S), reflect_x(bl(b)))
    ok = ok and GA.eq(sq[1], GA.sc(-1)) and GA.eq(sq[-1], ONE)
    # Cl(3,1) as the Rule 1 ascent of Cl(2,0): (nu, e_t) hyperbolic
    S = SA + (1,)
    nu = GA.gen(3)
    ok = ok and GA.congruence_signature([[S[3], 0], [0, S[2]]]) == (1, 1, 0)
    f = GA.scal(F(1, 2), GA.add(nu, ET))
    fs = GA.scal(F(1, 2), GA.sub(nu, ET))
    ok = ok and GA.is_zero(GA.mul(f, f, S)) and GA.is_zero(GA.mul(fs, fs, S))
    ok = ok and GA.eq(GA.add(GA.mul(f, fs, S), GA.mul(fs, f, S)), ONE)
    P = GA.mul(f, fs, S)
    ok = ok and GA.commutes(P, EX, S) and GA.commutes(P, EY, S)
    allb = [bl(b) for b in GA.all_blades(4)]
    ok = ok and span_rank([GA.mul(GA.mul(P, x, S), P, S) for x in allb], 4) == 4
    ok = ok and [residue(GA.sig(2, 0)), residue(SA), residue(SA + (1,)), residue(SA + (-1,))] == [2, 1, 2, 0]
    _tp_rv = (ok); assert _tp_rv is not False, "check_two_repairs_mat4r_inner_parity"; return _tp_rv


def cmul(x, y, S):
    """(a + i b)(c + i d) for pairs of real multivectors."""
    a, b = x
    c, d = y
    return (GA.sub(GA.mul(a, c, S), GA.mul(b, d, S)), GA.add(GA.mul(a, d, S), GA.mul(b, c, S)))


def check_time_positive_form_complex_type():
    premise("rule2.imported-classification-centre-type-c")
    S = GA.sig(1, 2)
    w = OMEGA
    ok = all(GA.commutes(w, GA.gen(i), S) for i in range(3)) and GA.eq(GA.mul(w, w, S), GA.sc(-1))
    cb = [b for b in B3 if all(GA.commutes(bl(b), GA.gen(i), S) for i in range(3))]
    ok = ok and cb == [(), (0, 1, 2)]
    e = GA.scal(F(1, 2), GA.add(ONE, GA.gen(0)))
    ok = ok and GA.eq(GA.mul(e, e, S), e) and not GA.commutes(e, GA.gen(1), S)
    ok = ok and span_rank([GA.mul(GA.mul(e, bl(b), S), e, S) for b in B3], 3) == 2
    half = F(1, 2)
    ep = (GA.sc(half), GA.scal(half, w))
    em = (GA.sc(half), GA.scal(-half, w))
    pp, pm = cmul(ep, ep, S), cmul(ep, em, S)
    ok = ok and GA.eq(pp[0], ep[0]) and GA.eq(pp[1], ep[1])
    ok = ok and GA.is_zero(pm[0]) and GA.is_zero(pm[1])
    ok = ok and GA.eq(GA.add(ep[0], em[0]), ONE) and GA.is_zero(GA.add(ep[1], em[1]))
    _tp_rv = (ok); assert _tp_rv is not False, "check_time_positive_form_complex_type"; return _tp_rv
