"""rule2.rule-2-kaluza-klein-algebra: exact checks in GA.

A5 = Cl(1,4): e0 (+1), e1, e2, e3, e4 (-1); gamma = e0 e1 e2 e3; omega = e0 e1 e2 e3 e4.
(i)   omega = gamma e4 is central with omega^2 = +1, eps_pm are orthogonal idempotents summing to 1, and the
      ideals eps_pm A5 have dimension 16 each (16 + 16 = 32).
(ii)  a -> eps_pm a is multiplicative on all blade pairs of Cl(1,3), injective (rank 16) and onto the ideal;
      eps_+ e4 = -eps_+ gamma, eps_- e4 = +eps_- gamma; omega acts as +1 on eps_+ A5 and -1 on eps_- A5, so
      the two representations are inequivalent; Cl(1,3) = Mat_2(H): the idempotent (1 + e0)/2 has a
      4-dimensional corner spanned by the corner idempotent and three elements i, j, k with
      i^2 = j^2 = -1 (in the corner), ij = k.
(iii) the reflection R (e4 -> -e4) equals grade involution after Ad_{e4} on all 32 blades, sends omega to
      -omega and exchanges eps_pm (so it moves the centre and is not inner).
(iv)  Cl(2,4) (nu^2 = +1) and Cl(1,5) (nu^2 = -1), nu = e5: {eps_+, eps_-, eps_+ nu, s eps_- nu} are 2 x 2
      matrix units, the corner eps_+ B eps_+ has dimension 16 = dim Cl(1,3), and the centre is R
      (central blades computed).
(v)   in both: Ad_nu is the grade involution and Ad_{nu e4} is R on all 32 blades of A5;
      (nu e4)^2 = +1 in Cl(2,4) and -1 in Cl(1,5).
(vi)  in Cl(2,4): (nu, e4) has Gram signature (1,1), f = (nu + e4)/2 and f* = (nu - e4)/2 are null with
      f f* + f* f = 1, P = f f* commutes with Cl(1,3) and P B P has dimension 16 (Rule 1, Mat_2(Cl(1,3)));
      in Cl(1,5) the adjoined plane is negative definite; residues 6 -> 5 -> 6 and 6 -> 5 -> 4 from the
      signature counts.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ONE = GA.sc(1)
SA = GA.sig(1, 4)
OMEGA = {(0, 1, 2, 3, 4): F(1)}
GAMMA = {(0, 1, 2, 3): F(1)}
E4 = GA.gen(4)
EPP = GA.scal(F(1, 2), GA.add(ONE, OMEGA))
EPM = GA.scal(F(1, 2), GA.sub(ONE, OMEGA))
B13 = [b for b in GA.all_blades(5) if 4 not in b]
B5 = GA.all_blades(5)


def bl(b):
    return {b: F(1)}


def span_rank(elems, n):
    blades = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in elems])


def reflect_e4(x):
    return {b: (-c if 4 in b else c) for b, c in x.items()}


def residue(S):
    return (sum(1 for s in S if s == 1) - sum(1 for s in S if s == -1)) % 8


def check_type_c_and_ideals():
    premise("rule2.imported-classification-centre-type-c")
    ok = GA.eq(GA.mul(GAMMA, E4, SA), OMEGA)
    ok = ok and all(GA.commutes(OMEGA, GA.gen(i), SA) for i in range(5))
    ok = ok and GA.eq(GA.mul(OMEGA, OMEGA, SA), ONE)
    ok = ok and GA.eq(GA.mul(EPP, EPP, SA), EPP) and GA.eq(GA.mul(EPM, EPM, SA), EPM)
    ok = ok and GA.is_zero(GA.mul(EPP, EPM, SA)) and GA.eq(GA.add(EPP, EPM), ONE)
    ip = [GA.mul(EPP, bl(b), SA) for b in B5]
    im = [GA.mul(EPM, bl(b), SA) for b in B5]
    ok = ok and span_rank(ip, 5) == 16 and span_rank(im, 5) == 16 and span_rank(ip + im, 5) == 32
    _tp_rv = (ok); assert _tp_rv is not False, "check_type_c_and_ideals"; return _tp_rv


def check_ideals_are_spacetime_algebra_two_dirac_reps():
    premise("rule2.even-subalgebra-one-dimensional-extension")
    premise("rule2.imported-gamma-matrices-odd-dimension")
    ok = True
    for eps in (EPP, EPM):
        img = [GA.mul(eps, bl(b), SA) for b in B13]
        ok = ok and span_rank(img, 5) == 16
        ok = ok and span_rank([GA.mul(eps, bl(b), SA) for b in B5], 5) == 16
        for a in B13:
            for b in B13:
                lhs = GA.mul(GA.mul(eps, bl(a), SA), GA.mul(eps, bl(b), SA), SA)
                ok = ok and GA.eq(lhs, GA.mul(eps, GA.mul(bl(a), bl(b), SA), SA))
    ok = ok and GA.eq(GA.mul(EPP, E4, SA), GA.neg(GA.mul(EPP, GAMMA, SA)))
    ok = ok and GA.eq(GA.mul(EPM, E4, SA), GA.mul(EPM, GAMMA, SA))
    ok = ok and GA.eq(GA.mul(OMEGA, EPP, SA), EPP) and GA.eq(GA.mul(OMEGA, EPM, SA), GA.neg(EPM))
    # Cl(1,3) = Mat_2(H): corner of (1 + e0)/2 is a quaternion algebra
    S13 = GA.sig(1, 3)
    e = GA.scal(F(1, 2), GA.add(ONE, GA.gen(0)))
    corner = [GA.mul(GA.mul(e, bl(b), S13), e, S13) for b in GA.all_blades(4)]
    ok = ok and span_rank(corner, 4) == 4
    qi, qj = GA.mul(e, bl((2, 3)), S13), GA.mul(e, bl((1, 3)), S13)
    qk = GA.mul(qi, qj, S13)
    for x in (qi, qj, qk):
        ok = ok and GA.eq(GA.mul(x, x, S13), GA.neg(e))
        ok = ok and GA.eq(GA.mul(GA.mul(e, x, S13), e, S13), x)
    ok = ok and span_rank([e, qi, qj, qk], 4) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_ideals_are_spacetime_algebra_two_dirac_reps"; return _tp_rv


def check_fifth_parity_is_outer():
    premise("rule2.imported-classification-centre-type-c")
    e4inv = GA.neg(E4)
    ok = GA.eq(GA.mul(E4, e4inv, SA), ONE)
    for b in B5:
        ok = ok and GA.eq(reflect_e4(bl(b)), GA.grade_inv(GA.mul(GA.mul(E4, bl(b), SA), e4inv, SA)))
    ok = ok and GA.eq(reflect_e4(OMEGA), GA.neg(OMEGA))
    ok = ok and GA.eq(reflect_e4(EPP), EPM) and GA.eq(reflect_e4(EPM), EPP)
    # any inner automorphism fixes the central omega; R does not
    ok = ok and not GA.eq(reflect_e4(OMEGA), OMEGA)
    # R negates exactly the 16 of the 32 basis blades that contain e4
    ok = ok and len(B5) == 32 and sum(1 for b in B5 if GA.eq(reflect_e4(bl(b)), GA.neg(bl(b)))) == 16
    _tp_rv = (ok); assert _tp_rv is not False, "check_fifth_parity_is_outer"; return _tp_rv


def repair(s):
    S = SA + (s,)
    nu = GA.gen(5)
    return S, nu, GA.scal(s, nu)


def check_two_repairs_matrix_units_centre_r():
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    ok = True
    for s in (1, -1):
        S, nu, nuinv = repair(s)
        E = {(1, 1): EPP, (2, 2): EPM, (1, 2): GA.mul(EPP, nu, S), (2, 1): GA.scal(s, GA.mul(EPM, nu, S))}
        for i in (1, 2):
            for j in (1, 2):
                for k in (1, 2):
                    for m in (1, 2):
                        ok = ok and GA.eq(GA.mul(E[(i, j)], E[(k, m)], S), E[(i, m)] if j == k else {})
        allb = [bl(b) for b in GA.all_blades(6)]
        ok = ok and span_rank([GA.mul(GA.mul(EPP, x, S), EPP, S) for x in allb], 6) == 16
        cb = [b for b in GA.all_blades(6) if all(GA.commutes(bl(b), GA.gen(i), S) for i in range(6))]
        ok = ok and cb == [()]
        ok = ok and not GA.commutes(EPP, nu, S)
    _tp_rv = (ok); assert _tp_rv is not False, "check_two_repairs_matrix_units_centre_r"; return _tp_rv


def check_parity_becomes_inner_boost_or_rotation():
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    ok = True
    sq = {}
    for s in (1, -1):
        S, nu, nuinv = repair(s)
        u = GA.mul(nu, E4, S)
        u2 = GA.mul(u, u, S)
        sq[s] = u2
        uinv = GA.scal(u2[()], u)
        ok = ok and GA.eq(GA.mul(u, uinv, S), ONE)
        for b in B5:
            ok = ok and GA.eq(GA.mul(GA.mul(nu, bl(b), S), nuinv, S), GA.grade_inv(bl(b)))
            ok = ok and GA.eq(GA.mul(GA.mul(u, bl(b), S), uinv, S), reflect_e4(bl(b)))
    _tp_rv = (ok and GA.eq(sq[1], ONE) and GA.eq(sq[-1], GA.sc(-1))); assert _tp_rv is not False, "check_parity_becomes_inner_boost_or_rotation"; return _tp_rv


def check_cl24_is_rule_one_ascent_of_spacetime():
    premise("rule2.imported-completion-spacetime-algebra-spinors")
    premise("rule2.where-obstruction-sits-commuting-square")
    S, nu, _ = repair(1)
    ok = GA.congruence_signature([[S[5], 0], [0, S[4]]]) == (1, 1, 0)
    f = GA.scal(F(1, 2), GA.add(nu, E4))
    fs = GA.scal(F(1, 2), GA.sub(nu, E4))
    ok = ok and GA.is_zero(GA.mul(f, f, S)) and GA.is_zero(GA.mul(fs, fs, S))
    ok = ok and GA.eq(GA.add(GA.mul(f, fs, S), GA.mul(fs, f, S)), ONE)
    P = GA.mul(f, fs, S)
    ok = ok and GA.eq(GA.mul(P, P, S), P) and all(GA.commutes(P, GA.gen(i), S) for i in range(4))
    allb = [bl(b) for b in GA.all_blades(6)]
    ok = ok and span_rank([GA.mul(GA.mul(P, x, S), P, S) for x in allb], 6) == 16
    S15, _, _ = repair(-1)
    ok = ok and GA.congruence_signature([[S15[4], 0], [0, S15[5]]]) == (0, 2, 0)
    ok = ok and [residue(GA.sig(1, 3)), residue(SA), residue(S), residue(S15)] == [6, 5, 6, 4]
    _tp_rv = (ok); assert _tp_rv is not False, "check_cl24_is_rule_one_ascent_of_spacetime"; return _tp_rv
