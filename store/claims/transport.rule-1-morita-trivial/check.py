"""transport.rule-1-morita-trivial: exact checks.

For every signature (p,q) with n = p + q <= 4 (15 cases): A = Cl(p,q) on e_0..e_{n-1}, B = Cl(p+1,q+1)
with e+ = e_n (square +1), e- = e_{n+1} (square -1), f = (e+ + e-)/2, f* = (e+ - e-)/2.
(1) f^2 = f*^2 = 0, ff* + f*f = 1; E11 = ff*, E22 = f*f, E12 = f, E21 = f* satisfy E11 + E22 = 1 and all
    16 relations E_ij E_kl = delta_jk E_il. ff* commutes with A; the corner E11 B E11 has dimension 2^n and
    equals A ff* (the union has the same rank); a -> a ff* is injective on A and multiplicative on all
    pairs of blades of A (n <= 3) and on samples (n = 4).
(2) The Peirce map b -> (E_1i b E_j1) is injective on B, rank 4 * 2^n = dim B, so B = Mat_2(A); on every
    blade a of A it is the twisted diagonal diag(a ff*, a^ ff*) (a^ the grade involution), off-diagonal
    entries zero; with the untwisted a in the (2,2) slot it fails for odd blades (control).
(3) Morita invariants: the number of central blades of B equals that of A, the presence of a central
    non-scalar blade of square +1 (splitness, the type-C diagnosis) agrees, and (p+1) - (q+1) = p - q.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(p, n - p) for n in range(0, 5) for p in range(0, n + 1)]


def setup(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    f = GA.scal(F(1, 2), GA.add(ep, em))
    fs = GA.scal(F(1, 2), GA.sub(ep, em))
    return n, sq, f, fs


def rank(elems, m):
    bl = GA.all_blades(m)
    rows = [GA.basis_vector_of(x, bl) for x in elems]
    return GA.rank_of_vectors(rows) if rows else 0


def central_blades(sq, m):
    return [b for b in GA.all_blades(m)
            if all(GA.commutes(GA.gen(i), {b: F(1)}, sq) for i in range(m))]


def check_ladder_pair_matrix_units_and_corner():
    premise("transport.matrix-units-peirce-isomorphism")
    ok = True
    for (p, q) in SIGS:
        n, sq, f, fs = setup(p, q)
        m = n + 2
        ffs, fsf = GA.mul(f, fs, sq), GA.mul(fs, f, sq)
        ok = ok and GA.is_zero(GA.mul(f, f, sq)) and GA.is_zero(GA.mul(fs, fs, sq))
        ok = ok and GA.eq(GA.add(ffs, fsf), GA.sc(1))
        E = {(1, 1): ffs, (2, 2): fsf, (1, 2): f, (2, 1): fs}
        for (i, j), Eij in E.items():
            for (k, l), Ekl in E.items():
                ok = ok and GA.eq(GA.mul(Eij, Ekl, sq), E[(i, l)] if j == k else {})
        base = GA.all_blades(n)
        ok = ok and all(GA.commutes(ffs, GA.gen(i), sq) for i in range(n))
        corner = [GA.mul(GA.mul(ffs, {b: F(1)}, sq), ffs, sq) for b in GA.all_blades(m)]
        aff = [GA.mul({b: F(1)}, ffs, sq) for b in base]
        ok = ok and rank(corner, m) == 2 ** n and rank(aff, m) == 2 ** n
        ok = ok and rank(corner + aff, m) == 2 ** n
        pairs = [(a, b) for a in base for b in base] if n <= 3 else [(base[i], base[(7 * i + 3) % len(base)])
                                                                    for i in range(len(base))]
        for a, b in pairs:
            ea, eb = {a: F(1)}, {b: F(1)}
            lhs = GA.mul(GA.mul(ea, ffs, sq), GA.mul(eb, ffs, sq), sq)
            ok = ok and GA.eq(lhs, GA.mul(GA.mul(ea, eb, sq), ffs, sq))
    _tp_rv = (ok); assert _tp_rv is not False, "check_ladder_pair_matrix_units_and_corner"; return _tp_rv


def check_twisted_diagonal_and_mat2():
    premise("transport.matrix-units-peirce-isomorphism")
    ok = True
    for (p, q) in SIGS:
        n, sq, f, fs = setup(p, q)
        m = n + 2
        ffs, fsf = GA.mul(f, fs, sq), GA.mul(fs, f, sq)
        E = {(1, 1): ffs, (2, 2): fsf, (1, 2): f, (2, 1): fs}

        def phi(x):
            return {(i, j): GA.mul(GA.mul(E[(1, i)], x, sq), E[(j, 1)], sq) for i in (1, 2) for j in (1, 2)}

        allb = GA.all_blades(m)
        imgs = []
        for b in allb:
            P = phi({b: F(1)})
            imgs.append([c for ij in sorted(P) for c in GA.basis_vector_of(P[ij], allb)])
        ok = ok and GA.rank_of_vectors(imgs) == 4 * 2 ** n == 2 ** m
        odd_seen = False
        for b in GA.all_blades(n):
            a = {b: F(1)}
            P = phi(a)
            ok = ok and GA.eq(P[(1, 1)], GA.mul(a, ffs, sq))
            ok = ok and GA.eq(P[(2, 2)], GA.mul(GA.grade_inv(a), ffs, sq))
            ok = ok and GA.is_zero(P[(1, 2)]) and GA.is_zero(P[(2, 1)])
            if len(b) % 2 == 1:
                odd_seen = True
                ok = ok and not GA.eq(P[(2, 2)], GA.mul(a, ffs, sq))
        ok = ok and (odd_seen or n == 0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_twisted_diagonal_and_mat2"; return _tp_rv


def check_morita_invariants_preserved():
    ok = True
    for (p, q) in SIGS:
        n, sq, f, fs = setup(p, q)
        sqA = GA.sig(p, q)
        cA, cB = central_blades(sqA, n), central_blades(sq, n + 2)
        ok = ok and len(cA) == len(cB)
        splitA = any(b and GA.eq(GA.mul({b: F(1)}, {b: F(1)}, sqA), GA.sc(1)) for b in cA)
        splitB = any(b and GA.eq(GA.mul({b: F(1)}, {b: F(1)}, sq), GA.sc(1)) for b in cB)
        ok = ok and splitA == splitB
        ok = ok and splitA == (n % 2 == 1 and (p - q) % 4 == 1)
        ok = ok and ((p + 1) - (q + 1)) % 8 == (p - q) % 8
    _tp_rv = (ok); assert _tp_rv is not False, "check_morita_invariants_preserved"; return _tp_rv
