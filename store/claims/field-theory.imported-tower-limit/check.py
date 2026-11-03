"""field-theory.imported-tower-limit: exact checks of the CAR from the adjoined planes, rung by rung.

Each adjoined hyperbolic plane j is spanned by a generator e+ (square +1) and e- (square -1), with
v_j = (e+ + e-)/2 and w_j = (e+ - e-)/2.
(1) The planes generate the CAR: on the ground Cl(1,3) with n = 1, 2, 3 planes adjoined
    (Cl(1+n, 3+n)), Q(v_j) = Q(w_j) = 0, {v_j, w_k} = delta_jk, {v_j, v_k} = {w_j, w_k} = 0, and the
    v_j, w_j anticommute with the ground generators.
(2) The finite rungs of the limit are the CAR algebras of n modes: the 4^n ordered monomials in the
    v_j, w_j are independent (n = 1, 2, 3), so the planes generate an algebra of dimension 4^n. In
    Cl(n, n) for n = 1, 2: P = prod_j v_j w_j is a nonzero idempotent with v_j P = 0, the states w_S P
    span a Fock space of dimension 2^n, the matrices of w_j are the transposes of those of v_j
    (w_j = v_j^* for the Fock inner product), they satisfy the CAR as matrices, and the 4^n monomials
    act with rank 4^n = dim Mat_(2^n): the rung algebra is the full matrix algebra Mat_(2^n), the
    CAR algebra of n modes. Rung n sits unitally in rung n + 1 (n = 1, 2): the inclusion of generators
    (the same blades) is multiplicative on every pair of the 4^n monomials (their product computed in rung n
    equals the product computed in rung n + 1), sends 1 to 1, keeps the 4^n monomials independent, and the
    new plane's v_{n+1}, w_{n+1} anticommute with the old generators.
Not checked: the C*-completion and uniqueness of the UHF limit (analytic).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

HALF = F(1, 2)
GROUND = (1, -1, -1, -1)              # the ground Cl(1,3)
RUNGS = (1, 2, 3)
FOCK_RUNGS = (1, 2)


def setup(ground, n):
    sq = tuple(ground) + (1, -1) * n
    g0 = len(ground)
    v = [GA.scal(HALF, GA.add(GA.gen(g0 + 2 * j), GA.gen(g0 + 2 * j + 1))) for j in range(n)]
    w = [GA.scal(HALF, GA.sub(GA.gen(g0 + 2 * j), GA.gen(g0 + 2 * j + 1))) for j in range(n)]
    return sq, v, w


def anti(x, y, sq):
    return GA.add(GA.mul(x, y, sq), GA.mul(y, x, sq))


def prod(xs, sq):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def subsets(n):
    return [S for k in range(n + 1) for S in combinations(range(n), k)]


def monomials(v, w, sq):
    n = len(v)
    return [prod([v[j] for j in S] + [w[k] for k in T], sq) for S in subsets(n) for T in subsets(n)]


def check_planes_generate_car():
    premise("tower.car-limit-even-charge")
    ok = True
    for n in RUNGS:
        sq, v, w = setup(GROUND, n)
        for j in range(n):
            ok = ok and GA.dot(v[j], v[j], sq) == 0 and GA.dot(w[j], w[j], sq) == 0
            ok = ok and GA.is_zero(GA.mul(v[j], v[j], sq)) and GA.is_zero(GA.mul(w[j], w[j], sq))
            for k in range(n):
                ok = ok and GA.eq(anti(v[j], w[k], sq), GA.sc(1 if j == k else 0))
                ok = ok and GA.is_zero(anti(v[j], v[k], sq)) and GA.is_zero(anti(w[j], w[k], sq))
            ok = ok and all(GA.anticommutes(x, GA.gen(i), sq) for x in (v[j], w[j]) for i in range(4))
    GA.check("adjoined planes: null v_j, w_j with {v_j, w_k} = delta_jk, anticommuting with the ground", ok)
    return ok


def coords(basis, y, blades):
    rows = [[b.get(bl, F(0)) for b in basis] + [-y.get(bl, F(0))] for bl in blades]
    ker = GA.field_kernel(rows)
    assert len(ker) == 1 and ker[0][-1] != 0
    return [c / ker[0][-1] for c in ker[0][:-1]]


def check_rungs_are_full_matrix_algebras():
    premise("tower.car-limit-even-charge")
    ok = True
    for n in RUNGS:
        sq, v, w = setup(GROUND, n)
        mons = monomials(v, w, sq)
        blades = GA.all_blades(len(sq))
        ok = ok and len(mons) == 4 ** n
        ok = ok and GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in mons]) == 4 ** n
    for n in FOCK_RUNGS:
        sq, v, w = setup((), n)
        blades = GA.all_blades(len(sq))
        P = prod([GA.mul(v[j], w[j], sq) for j in range(n)], sq)
        ok = ok and not GA.is_zero(P) and GA.eq(GA.mul(P, P, sq), P)
        ok = ok and all(GA.is_zero(GA.mul(v[j], P, sq)) for j in range(n))
        fock = [prod([w[k] for k in S] + [P], sq) for S in subsets(n)]
        d = 2 ** n
        ok = ok and len(fock) == d
        ok = ok and GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in fock]) == d

        def mat(x):
            cols = [coords(fock, GA.mul(x, s, sq), blades) for s in fock]
            return [[cols[j][i] for j in range(d)] for i in range(d)]

        V = [mat(x) for x in v]
        W = [mat(x) for x in w]
        ident = [[F(int(i == j)) for j in range(d)] for i in range(d)]
        for j in range(n):
            ok = ok and W[j] == [list(c) for c in zip(*V[j])]
            for k in range(n):
                car = [[a + b for a, b in zip(r1, r2)] for r1, r2 in
                       zip(GA.mat_mul(V[j], W[k]), GA.mat_mul(W[k], V[j]))]
                ok = ok and car == (ident if j == k else [[F(0)] * d for _ in range(d)])
        images = [[e for row in mat(x) for e in row] for x in monomials(v, w, sq)]
        ok = ok and GA.rank_of_vectors(images) == d * d
    for n in FOCK_RUNGS:
        sq, v, w = setup(GROUND, n)
        sq1, v1, w1 = setup(GROUND, n + 1)
        ok = ok and v1[:n] == v and w1[:n] == w and sq1[:len(sq)] == sq
        mons, mons1 = monomials(v, w, sq), monomials(v1[:n], w1[:n], sq1)
        ok = ok and mons == mons1 and mons[0] == GA.sc(1)
        ok = ok and all(GA.eq(GA.mul(x, y, sq), GA.mul(x, y, sq1)) for x in mons for y in mons)
        blades1 = GA.all_blades(len(sq1))
        ok = ok and GA.rank_of_vectors([GA.basis_vector_of(x, blades1) for x in mons1]) == 4 ** n
        ok = ok and all(GA.anticommutes(x, y, sq1) for x in (v1[n], w1[n]) for y in v + w)
    GA.check("rung n: 4^n independent monomials; Fock space of dimension 2^n, w_j = v_j^T, image = Mat_(2^n); "
             "rung n sits unitally in rung n + 1", ok)
    return ok
