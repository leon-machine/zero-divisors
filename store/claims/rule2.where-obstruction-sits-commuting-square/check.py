"""rule2.where-obstruction-sits-commuting-square: exact checks.

A = Cl(p,q), n = p + q even; A_s = Cl(p,q+1) (nu^2 = -1), A_t = Cl(p+1,q) (nu^2 = +1), the new generator at
index n. Type C means: volume element central with square +1 (computed in GA).
(a) For every even (p,q) with 0 <= n <= 6: A_s is type C iff p - q = 2 mod 4 and A_t iff p - q = 0 mod 4,
    exactly one of the two; the other has omega central with omega^2 = -1 and centre span(1, omega)
    (central blades computed), a field C, so it is simple.
(b) For the obstructed extension X (n <= 6): eps_+ X has dimension 2^n and a -> eps_+ a is injective on the
    even subalgebra; and Cl^0(X) contains generators h_i of A itself: h_i = e_i nu (spacelike case) or
    h_i = e_i nu omega_A (timelike case, where e_i nu alone gives Cl(q,p)), which are even, satisfy the
    relations of Cl(p,q) and generate a subalgebra of dimension 2^n (n <= 4 for the spanning rank).
(c) Opposite-sign repair (index n+1): the adjoined pair has Gram signature (1,1); f = (u + w)/2,
    f* = (u - w)/2 (u the generator of square +1, w of square -1) are null with f f* + f* f = 1;
    {eps_+, eps_-, eps_+ nu, s eps_- nu} (s = nu^2) are 2 x 2 matrix units with corner eps_+ B eps_+ of
    dimension 2^n; P = f f* commutes with A and P B P has dimension 2^n (the Rule 1 amplification);
    the residue of Cl(p+1,q+1) is d. Corner ranks for n <= 4.
(d) Same-sign repair Cl(p,q+2) / Cl(p+2,q): adjoined Gram definite ((2,0) or (0,2)), residue d -+ 2,
    trivial centre, and the same matrix units with a corner of dimension 2^n, so it is Mat_2(A) too.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

GRID = [(p, n - p) for n in range(0, 7, 2) for p in range(n + 1)]
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
    """(signature of the obstructed extension, nu^2) predicted by the residue."""
    if (p - q) % 4 == 2:
        return GA.sig(p, q) + (-1,), -1
    return GA.sig(p, q) + (1,), 1


def check_exactly_one_extension_obstructed():
    premise("rule2.imported-classification-centre-type-c")
    ok = len(GRID) == 16
    for (p, q) in GRID:
        n = p + q
        Ss, St = GA.sig(p, q) + (-1,), GA.sig(p, q) + (1,)
        cs, ct = is_type_c(Ss), is_type_c(St)
        ok = ok and cs == ((p - q) % 4 == 2) and ct == ((p - q) % 4 == 0) and cs != ct
        other = St if cs else Ss
        w = vol(n + 1)
        ok = ok and central(w, other) and GA.eq(GA.mul(w, w, other), GA.sc(-1))
        ok = ok and central_blades(other) == [(), tuple(range(n + 1))]
    _tp_rv = (ok); assert _tp_rv is not False, "check_exactly_one_extension_obstructed"; return _tp_rv


# Largest n = p + q at which the spanning ranks (2^(n+1) blades) are computed; above it only relations.
RANK_MAX_N = 4


def unit_blades(m):
    """Every basis blade of Cl on m generators, with coefficient 1."""
    return [{b: F(1)} for b in GA.all_blades(m)]


def is_even(x):
    return all(len(b) % 2 == 0 for b in x)


def check_ideals_are_copies_of_a():
    premise("rule2.even-subalgebra-one-dimensional-extension")
    ok = True
    for (p, q) in GRID:
        n = p + q
        S, s = obstructed(p, q)
        nu = GA.gen(n)
        epp = GA.scal(F(1, 2), GA.add(ONE, vol(n + 1)))
        ok = ok and GA.eq(GA.mul(epp, epp, S), epp)            # eps_+ is an idempotent
        if n <= RANK_MAX_N:
            allb = unit_blades(len(S))
            evb = [x for x in allb if is_even(x)]
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
            ok = ok and is_even(h[i])
            ok = ok and GA.eq(GA.mul(h[i], h[i], S), GA.sc(target[i]))
        for i, j in combinations(range(n), 2):
            ok = ok and GA.anticommutes(h[i], h[j], S)
        # (e_i nu)^2 = -e_i^2 nu^2 = -s e_i^2: the bare e_i nu give Cl(p,q) when s = -1 and Cl(q,p) when
        # s = +1 (squares flipped), which is why the timelike case needs omega_A
        for i in range(n):
            x = GA.mul(GA.gen(i), nu, S)
            ok = ok and GA.eq(GA.mul(x, x, S), GA.sc(-s * target[i]))
        if n <= RANK_MAX_N:
            prods = [ONE]                                       # products over all subsets of the h_i
            for hi in h:
                prods = prods + [GA.mul(x, hi, S) for x in prods]
            ok = ok and span_rank(prods, len(S)) == 2 ** n
    _tp_rv = (ok); assert _tp_rv is not False, "check_ideals_are_copies_of_a"; return _tp_rv


def matrix_units_and_corner(S, n, rank_too):
    nu = GA.gen(n)
    s = S[n]
    epp = GA.scal(F(1, 2), GA.add(ONE, vol(n)))
    epm = GA.scal(F(1, 2), GA.sub(ONE, vol(n)))
    E = {(1, 1): epp, (2, 2): epm, (1, 2): GA.mul(epp, nu, S), (2, 1): GA.scal(s, GA.mul(epm, nu, S))}
    ok = GA.eq(GA.add(epp, epm), ONE)
    for i in (1, 2):
        for j in (1, 2):
            for k in (1, 2):
                for m in (1, 2):
                    want = E[(i, m)] if j == k else {}
                    ok = ok and GA.eq(GA.mul(E[(i, j)], E[(k, m)], S), want)
    if rank_too:
        allb = [{b: F(1)} for b in GA.all_blades(len(S))]
        ok = ok and span_rank([GA.mul(GA.mul(epp, x, S), epp, S) for x in allb], len(S)) == 2 ** (n - 1)
    return ok


def check_opposite_sign_repair_is_rule_one_ascent():
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    premise("transport.rule-1-morita-trivial")
    ok = True
    for (p, q) in GRID:
        n = p + q
        S1, s = obstructed(p, q)
        S = S1 + (-s,)                               # repair nu of the opposite sign, index n + 1
        ok = ok and sum(1 for x in S if x == 1) == p + 1 and sum(1 for x in S if x == -1) == q + 1
        ok = ok and ((p + 1) - (q + 1)) % 8 == (p - q) % 8
        a, b = GA.gen(n), GA.gen(n + 1)
        ok = ok and GA.congruence_signature([[S[n], 0], [0, S[n + 1]]]) == (1, 1, 0)
        u, w = (a, b) if S[n] == 1 else (b, a)
        f = GA.scal(F(1, 2), GA.add(u, w))
        fs = GA.scal(F(1, 2), GA.sub(u, w))
        ok = ok and GA.is_zero(GA.mul(f, f, S)) and GA.is_zero(GA.mul(fs, fs, S))
        ok = ok and GA.eq(GA.add(GA.mul(f, fs, S), GA.mul(fs, f, S)), ONE)
        # Rule 2 matrix units: base is the obstructed extension (n+1 gens), nu the repair
        ok = ok and matrix_units_and_corner(S, n + 1, n <= 4)
        P = GA.mul(f, fs, S)
        ok = ok and GA.eq(GA.mul(P, P, S), P)
        ok = ok and all(GA.commutes(P, GA.gen(i), S) for i in range(n))
        if n <= 4:
            allb = [{bb: F(1)} for bb in GA.all_blades(n + 2)]
            ok = ok and span_rank([GA.mul(GA.mul(P, x, S), P, S) for x in allb], n + 2) == 2 ** n
    _tp_rv = (ok); assert _tp_rv is not False, "check_opposite_sign_repair_is_rule_one_ascent"; return _tp_rv


def check_same_sign_repair_definite_two_residues_away():
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    ok = True
    for (p, q) in GRID:
        n = p + q
        d = (p - q) % 8
        S1, s = obstructed(p, q)
        S = S1 + (s,)
        pp = sum(1 for x in S if x == 1)
        qq = len(S) - pp
        ok = ok and (pp, qq) == ((p, q + 2) if s == -1 else (p + 2, q))
        ok = ok and (pp - qq) % 8 == (d - 2 * (1 if s == -1 else -1)) % 8
        gram = GA.congruence_signature([[S[n], 0], [0, S[n + 1]]])
        ok = ok and gram == ((0, 2, 0) if s == -1 else (2, 0, 0))
        ok = ok and central_blades(S) == [()]
        ok = ok and matrix_units_and_corner(S, n + 1, n <= 4)
    _tp_rv = (ok); assert _tp_rv is not False, "check_same_sign_repair_definite_two_residues_away"; return _tp_rv
