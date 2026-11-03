"""transport.where-obstruction-lies-commuting-square: exact checks.

A = Cl(p,q), n = p + q even; A_s = Cl(p,q+1) (new generator of square -1), A_t = Cl(p+1,q) (square +1), the
new generator at index n (GA.py signature tuples). Type C: the volume element is central with square +1.
(a) For every even (p,q) with 0 <= n <= 8: A_s is type C iff p - q = 2 mod 4 and A_t iff p - q = 0 mod 4,
    exactly one of the two; the other has omega central with omega^2 = -1; for n <= 6 its central blades
    are exactly {1, omega} (centre C, a field, so the semisimple algebra is simple).
(b) For the obstructed extension X (n <= 6): eps_+ X has dimension 2^n and a -> eps_+ a is injective on
    Cl^0(X) (n <= 4); Cl^0(X) contains generators of A itself: h_i = e_i nu (spacelike case) or
    h_i = e_i nu omega_A (timelike case, where e_i nu alone has the squares of Cl(q,p)); they are even,
    satisfy the relations of Cl(p,q) and span 2^n dimensions (n <= 4).
(b') The grade involution maps eps_+ X onto eps_- X (n <= 4); after adjoining the repair generator nu
    (either sign) conjugation by nu is the grade involution on X and nu eps_+ nu^-1 = eps_-, with
    eps_+ + nu eps_+ nu^-1 = 1.
(c) Opposite-sign repair (index n+1): the adjoined Gram is diag(+1,-1), signature (1,1); with u the
    adjoined generator of square +1 and w that of square -1, both choices f = (u +- w)/2, f* = (u -+ w)/2
    satisfy f^2 = f*^2 = 0 and f f* + f* f = 1; the Rule 2 matrix units {eps_+, eps_-, eps_+ nu, s eps_- nu} have a corner of dimension
    2^n (n <= 4), P = f f* commutes with A and P B P has dimension 2^n (the Rule 1 amplification); the
    residue of Cl(p+1,q+1) is p - q.
(d) Same-sign repair: Cl(p,q+2) or Cl(p+2,q), residue d -+ 2, adjoined Gram (0,2) or (2,0) (definite: no
    null combination a e + b nu with (a,b) in a rational net), centre R, and the same matrix units.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise

GRID6 = [(p, n - p) for n in range(0, 7, 2) for p in range(n + 1)]
GRID8 = [(p, n - p) for n in range(0, 9, 2) for p in range(n + 1)]
ONE = GA.sc(1)


def vol(n):
    return {tuple(range(n)): F(1)}


def central(x, S):
    return all(GA.commutes(x, GA.gen(i), S) for i in range(len(S)))


def central_blades(S):
    return [b for b in GA.all_blades(len(S)) if central({b: F(1)}, S)]


def is_type_c(S):
    w = vol(len(S))
    return central(w, S) and GA.eq(GA.mul(w, w, S), ONE)


def span_rank(elems, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in elems])


def obstructed(p, q):
    if (p - q) % 4 == 2:
        return GA.sig(p, q) + (-1,), -1
    return GA.sig(p, q) + (1,), 1


def check_exactly_one_extension_obstructed():
    premise("transport.existence-classification-type-c")
    premise("transport.centre")
    premise("transport.sign")
    ok = len(GRID8) == 25
    for (p, q) in GRID8:
        n = p + q
        Ss, St = GA.sig(p, q) + (-1,), GA.sig(p, q) + (1,)
        cs, ct = is_type_c(Ss), is_type_c(St)
        ok = ok and cs == ((p - q) % 4 == 2) and ct == ((p - q) % 4 == 0) and cs != ct
        other = St if cs else Ss
        w = vol(n + 1)
        ok = ok and central(w, other) and GA.eq(GA.mul(w, w, other), GA.sc(-1))
        if n <= 6:
            ok = ok and central_blades(other) == [(), tuple(range(n + 1))]
    _tp_rv = (ok); assert _tp_rv is not False, "check_exactly_one_extension_obstructed"; return _tp_rv


def check_ideals_exchanged_by_grade_involution_inner_after_repair():
    premise("transport.ascent-renders-grade-involution-inner")
    ok = True
    for (p, q) in GRID6:
        n = p + q
        S, s = obstructed(p, q)
        epp = GA.scal(F(1, 2), GA.add(ONE, vol(n + 1)))
        epm = GA.scal(F(1, 2), GA.sub(ONE, vol(n + 1)))
        ok = ok and GA.eq(GA.grade_inv(epp), epm)
        if n <= 4:
            allb = [{b: F(1)} for b in GA.all_blades(n + 1)]
            ok = ok and span_rank([GA.grade_inv(GA.mul(epp, x, S)) for x in allb] +
                                  [GA.mul(epm, x, S) for x in allb], n + 1) == 2 ** n
        # in the repaired algebra (either sign of the repair generator, index n+1) conjugation by it is
        # the grade involution on the extension and exchanges eps_+ and eps_-
        for t in (1, -1):
            S2 = S + (t,)
            nu = GA.gen(n + 1)
            nui = GA.scal(F(t), nu)
            ok = ok and GA.eq(GA.mul(GA.mul(nu, epp, S2), nui, S2), epm)
            for i in range(n + 1):
                ok = ok and GA.eq(GA.mul(GA.mul(nu, GA.gen(i), S2), nui, S2), GA.neg(GA.gen(i)))
            ok = ok and GA.eq(GA.add(epp, GA.mul(GA.mul(nu, epp, S2), nui, S2)), ONE)
    _tp_rv = (ok); assert _tp_rv is not False, "check_ideals_exchanged_by_grade_involution_inner_after_repair"; return _tp_rv


# Size limit for the rank computations in check_ideals_are_copies_of_a.
MAX_N_RANK = 4


def unit_blade(b):
    return {b: F(1)}


def even_units(m):
    """The even basis blades of Cl(m), each with coefficient 1."""
    return [unit_blade(b) for b in GA.all_blades(m) if len(b) % 2 == 0]


def check_ideals_are_copies_of_a():
    premise("transport.corner-even-subalgebra")
    premise("transport.even-subalgebra-one-dimensional-extension")
    premise("transport.classification-real-clifford-algebras")
    ok = True
    timelike = 0
    for (p, q) in GRID6:
        n = p + q
        S, s = obstructed(p, q)
        nu = GA.gen(n)
        epp = GA.scal(F(1, 2), GA.add(ONE, vol(n + 1)))
        ok = ok and GA.eq(GA.mul(epp, epp, S), epp)                          # eps_+ is an idempotent
        if n <= MAX_N_RANK:
            allb = [unit_blade(b) for b in GA.all_blades(len(S))]
            evb = even_units(len(S))
            ok = ok and span_rank([GA.mul(epp, x, S) for x in allb], len(S)) == 2 ** n
            ok = ok and span_rank([GA.mul(epp, x, S) for x in evb], len(S)) == 2 ** n
        wA = vol(n)
        h = []
        for i in range(n):
            x = GA.mul(GA.gen(i), nu, S)
            if s == 1:
                x = GA.mul(x, wA, S)
            h.append(x)
        target = GA.sig(p, q)
        for i in range(n):
            ok = ok and all(len(b) % 2 == 0 for b in h[i])
            ok = ok and GA.eq(GA.mul(h[i], h[i], S), GA.sc(target[i]))
            ok = ok and all(GA.anticommutes(h[i], h[j], S) for j in range(n) if j != i)
        if s == 1 and n:
            # timelike case: e_i nu alone has the squares of Cl(q,p)
            timelike += 1
            for i in range(n):
                xi = GA.mul(GA.gen(i), nu, S)
                ok = ok and GA.eq(GA.mul(xi, xi, S), GA.sc(-target[i]))
        if n <= MAX_N_RANK:
            prods = []
            for sub in GA.all_blades(n):
                x = ONE
                for i in sub:
                    x = GA.mul(x, h[i], S)
                prods.append(x)
            ok = ok and span_rank(prods, len(S)) == 2 ** n
    # by hand: p - q = 0 mod 4 with n = 2, 4, 6 even: (1,1); (0,4), (2,2), (4,0); (1,5), (3,3), (5,1)
    ok = ok and timelike == 7
    _tp_rv = (ok); assert _tp_rv is not False, "check_ideals_are_copies_of_a"; return _tp_rv


def matrix_units_and_corner(S, n, rank_too):
    nu = GA.gen(n)
    s = S[n]
    epp = GA.scal(F(1, 2), GA.add(ONE, vol(n)))
    epm = GA.scal(F(1, 2), GA.sub(ONE, vol(n)))
    E = {(1, 1): epp, (2, 2): epm, (1, 2): GA.mul(epp, nu, S), (2, 1): GA.scal(s, GA.mul(epm, nu, S))}
    ok = GA.eq(GA.add(epp, epm), ONE)
    for i, j, k, m in product((1, 2), repeat=4):
        want = E[(i, m)] if j == k else {}
        ok = ok and GA.eq(GA.mul(E[(i, j)], E[(k, m)], S), want)
    if rank_too:
        allb = [{b: F(1)} for b in GA.all_blades(len(S))]
        ok = ok and span_rank([GA.mul(GA.mul(epp, x, S), epp, S) for x in allb], len(S)) == 2 ** (n - 1)
    return ok


def check_opposite_sign_repair_is_rule_one_ascent():
    premise("transport.rule-1-morita-trivial")
    premise("transport.matrix-units-peirce-isomorphism")
    premise("transport.rule-2-ideal-fusion-sharp-form")
    ok = True
    for (p, q) in GRID6:
        n = p + q
        S1, s = obstructed(p, q)
        S = S1 + (-s,)
        ok = ok and S.count(1) == p + 1 and S.count(-1) == q + 1
        ok = ok and ((p + 1) - (q + 1)) % 8 == (p - q) % 8
        a, b = GA.gen(n), GA.gen(n + 1)
        ok = ok and GA.congruence_signature([[S[n], 0], [0, S[n + 1]]]) == (1, 1, 0)
        u, w = (a, b) if S[n] == 1 else (b, a)
        for sg in (1, -1):
            f = GA.scal(F(1, 2), GA.add(u, GA.scal(sg, w)))
            fs = GA.scal(F(1, 2), GA.sub(u, GA.scal(sg, w)))
            ok = ok and GA.is_zero(GA.mul(f, f, S)) and GA.is_zero(GA.mul(fs, fs, S))
            ok = ok and GA.eq(GA.add(GA.mul(f, fs, S), GA.mul(fs, f, S)), ONE)
        f = GA.scal(F(1, 2), GA.add(u, w))
        fs = GA.scal(F(1, 2), GA.sub(u, w))
        ok = ok and matrix_units_and_corner(S, n + 1, n <= 4)
        P = GA.mul(f, fs, S)
        ok = ok and GA.eq(GA.mul(P, P, S), P)
        ok = ok and all(GA.commutes(P, GA.gen(i), S) for i in range(n))
        if n <= 4:
            allb = [{bb: F(1)} for bb in GA.all_blades(n + 2)]
            ok = ok and span_rank([GA.mul(GA.mul(P, x, S), P, S) for x in allb], n + 2) == 2 ** n
    _tp_rv = (ok); assert _tp_rv is not False, "check_opposite_sign_repair_is_rule_one_ascent"; return _tp_rv


def check_same_sign_repair_definite_two_residues_away():
    premise("transport.rule-2-ideal-fusion-sharp-form")
    ok = True
    for (p, q) in GRID6:
        n = p + q
        d = (p - q) % 8
        S1, s = obstructed(p, q)
        S = S1 + (s,)
        pp = S.count(1)
        qq = len(S) - pp
        ok = ok and (pp, qq) == ((p, q + 2) if s == -1 else (p + 2, q))
        ok = ok and (pp - qq) % 8 == (d + 2 * s) % 8
        gram = GA.congruence_signature([[S[n], 0], [0, S[n + 1]]])
        ok = ok and gram == ((0, 2, 0) if s == -1 else (2, 0, 0))
        for a, b in product(range(-2, 3), repeat=2):
            if a or b:
                x = GA.add(GA.scal(a, GA.gen(n)), GA.scal(b, GA.gen(n + 1)))
                ok = ok and GA.mul(x, x, S).get((), F(0)) == s * (a * a + b * b)
        ok = ok and central_blades(S) == [()]
        ok = ok and matrix_units_and_corner(S, n + 1, n <= 4)
    _tp_rv = (ok); assert _tp_rv is not False, "check_same_sign_repair_definite_two_residues_away"; return _tp_rv
