"""transport.one-generator-minimal-minimal-completions-classified: exact checks.

A = Cl(p,q) with p - q = 1 mod 4, for every such signature with n = p + q <= 5 ((1,0), (2,1), (0,3),
(3,2), (1,4), (5,0)); omega = e_0...e_{n-1}; the adjoined generator is nu = e_n with Q(nu) = gamma.
(1) No ascent: omega is central with omega^2 = 1 and omega is not a scalar, so eps_+- = (1 +- omega)/2
    are central idempotents, nonzero and different from 1: A is not simple. The central blades of A
    are exactly {1, omega}.
(2) gamma = 0: J = A nu has dimension 2^n, is a two-sided ideal of B_0 (products of every blade of
    B_0 with every blade of J land in J), J^2 = 0, and dropping the nu-part, B_0 -> A, is
    multiplicative on all blade pairs and onto A with kernel J: B_0 / J = A.
(3) gamma = +-1: the centre of B (computed blade-wise) is R, the corner eps_+ B eps_+ has dimension
    2^(n-1) = dim Cl^0(p,q), and dim B = 4 * 2^(n-1), so B = Mat_2(Cl^0(p,q)) (fusion premise).
    The two ascents are isomorphic as algebras: e_i -> e_i, nu -> omega nu satisfies the relations of
    the other ascent and the images span (rank 2^(n+1)). They are not isometric: the extended Gram
    matrices have congruence signatures (p+1,q) and (p,q+1).
(4) dim V' = n + 2: for 6 rational Gram matrices of V' (degenerate and non-orthogonal ones included),
    the Clifford algebra has dimension 2^(n+2) (exterior model, blades independent), so every ascent
    by two or more directions has dimension at least 2^(n+2) > 2^(n+1).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(1, 0), (2, 1), (0, 3), (3, 2), (1, 4), (5, 0)]
# Gram matrices of two adjoined directions (with V = R^(1,0) or R^(2,1) on the diagonal)
EXT_GRAMS = [
    [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[1, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[1, 0, 2], [0, 1, 0], [2, 0, -3]],
    [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    [[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, -1, 0, 1], [1, 0, 0, 2, 3], [0, 0, 1, 3, 0]],
    [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, -1]],
]


def rank(elems, m):
    bl = GA.all_blades(m)
    rows = [GA.basis_vector_of(x, bl) for x in elems]
    return GA.rank_of_vectors(rows) if rows else 0


def central_blades(sq, m):
    out = []
    for b in GA.all_blades(m):
        e = {b: F(1)}
        if all(GA.commutes(GA.gen(i), e, sq) for i in range(m)):
            out.append(b)
    return out


def check_no_ascent_not_simple():
    premise("transport.existence-classification-type-c")
    ok = True
    for (p, q) in SIGS:
        n = p + q
        sq = GA.sig(p, q)
        omega = {tuple(range(n)): F(1)}
        ok = ok and GA.eq(GA.mul(omega, omega, sq), GA.sc(1))
        ok = ok and central_blades(sq, n) == [(), tuple(range(n))]
        ep = GA.scal(F(1, 2), GA.add(GA.sc(1), omega))
        ok = ok and GA.eq(GA.mul(ep, ep, sq), ep) and not GA.is_zero(ep) and not GA.eq(ep, GA.sc(1))
        # eps_+ A is a proper ideal: dimension 2^(n-1)
        ok = ok and rank([GA.mul(ep, {b: F(1)}, sq) for b in GA.all_blades(n)], n) == 2 ** (n - 1)
    _tp_rv = (ok); assert _tp_rv is not False, "check_no_ascent_not_simple"; return _tp_rv


def check_null_generator_thickens():
    premise("transport.decomposition-commutation")
    ok = True
    for (p, q) in SIGS:
        n = p + q
        sq = GA.sig(p, q) + (0,)
        m = n + 1
        base = GA.all_blades(n)
        nu = GA.gen(n)
        J = [GA.mul({b: F(1)}, nu, sq) for b in base]
        ok = ok and rank(J, m) == 2 ** n
        in_J = lambda x: all(n in bl for bl in x)
        allb = GA.all_blades(m)
        for b in allb:
            for j in J:
                ok = ok and in_J(GA.mul({b: F(1)}, j, sq)) and in_J(GA.mul(j, {b: F(1)}, sq))
        ok = ok and all(GA.is_zero(GA.mul(x, y, sq)) for x in J for y in J)
        proj = lambda x: {bl: c for bl, c in x.items() if n not in bl}
        for b1 in allb:
            for b2 in allb:
                lhs = proj(GA.mul({b1: F(1)}, {b2: F(1)}, sq))
                rhs = GA.mul(proj({b1: F(1)}), proj({b2: F(1)}), sq)
                ok = ok and GA.eq(lhs, rhs)
        ok = ok and 2 ** m - rank(J, m) == 2 ** n
    _tp_rv = (ok); assert _tp_rv is not False, "check_null_generator_thickens"; return _tp_rv


# Sample signs of nu^2 for the one-generator ascent.
NU_SQUARES = (1, -1)


def unit_blade(b):
    return {b: F(1)}


def word(gens, idx, sq):
    """The product gens[i1] gens[i2] ... over the index tuple idx (1 for the empty tuple)."""
    x = GA.sc(1)
    for i in idx:
        x = GA.mul(x, gens[i], sq)
    return x


def check_nondegenerate_ascents_simple_isomorphic_not_isometric():
    premise("transport.rule-2-ideal-fusion-sharp-form")
    ok = True
    for (p, q) in SIGS:
        n = p + q
        m = n + 1
        omega = {tuple(range(n)): F(1)}
        sigs = {}
        for g in NU_SQUARES:
            sq = GA.sig(p, q) + (g,)
            ok = ok and central_blades(sq, m) == [()]
            ep = GA.scal(F(1, 2), GA.add(GA.sc(1), omega))
            ok = ok and GA.eq(GA.mul(ep, ep, sq), ep)                     # eps_+ is an idempotent
            corner = [GA.mul(GA.mul(ep, unit_blade(b), sq), ep, sq) for b in GA.all_blades(m)]
            ok = ok and rank(corner, m) == 2 ** (n - 1) and 4 * 2 ** (n - 1) == 2 ** m
            # nu -> omega nu realises the other ascent inside this one
            gens = [GA.gen(i) for i in range(n)] + [GA.mul(omega, GA.gen(n), sq)]
            other = GA.sig(p, q) + (-g,)
            for i in range(m):
                ok = ok and GA.eq(GA.mul(gens[i], gens[i], sq), GA.sc(other[i]))
                ok = ok and all(GA.anticommutes(gens[i], gens[j], sq) for j in range(m) if j != i)
            prods = [word(gens, bl, sq) for bl in GA.all_blades(m)]
            ok = ok and rank(prods, m) == 2 ** m
            G = [[GA.dot(GA.gen(i), GA.gen(j), sq) for j in range(m)] for i in range(m)]
            sigs[g] = GA.congruence_signature(G)[:2]
        # not isometric: the extended forms have different signatures
        ok = ok and sigs[1] == (p + 1, q) and sigs[-1] == (p, q + 1)
    _tp_rv = (ok); assert _tp_rv is not False, "check_nondegenerate_ascents_simple_isomorphic_not_isometric"; return _tp_rv


def check_two_directions_double_again():
    ok = True
    for G in EXT_GRAMS:
        k = len(G)
        B = [[F(x) for x in row] for row in G]
        states = [GA.ext_sigma_blade(list(I), B, k) for I in GA.all_blades(k)]
        keys = sorted({S for st in states for S in st}, key=lambda s: (len(s), sorted(s)))
        rows = [[st.get(S, F(0)) for S in keys] for st in states]
        n = k - 2
        ok = ok and GA.rank_of_vectors(rows) == 2 ** (n + 2) and 2 ** (n + 2) > 2 ** (n + 1)
    _tp_rv = (ok); assert _tp_rv is not False, "check_two_directions_double_again"; return _tp_rv
