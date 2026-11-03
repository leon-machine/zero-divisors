"""sheaf.degeneration-sheaf: exact checks of the degeneration sheaf's fibres.

(1) Wall fibres, blade-exact (GA, diagonal degenerate signatures): for every (p, q) with p >= 1 and
    n = p + q <= 5 the wall fibre is Cl of (p-1) squares +1, q squares -1 and the radical k (square 0).
    k anticommutes with every other generator and k a = a^ k on every blade; J = A k and k A both have rank
    2^(n-1) and their sum has the same rank (J = Ak = kA); J^2 = 0 on all products of a spanning set; the
    k-deleting projection is multiplicative onto Cl(p-1, q) (structure constants on all blade pairs).
(2) Non-orthogonal fibres (GA exterior model, faithful for any Gram): four degenerate Gram matrices of
    corank one (n = 3, 4) whose radical k is not a basis vector: c(k)^2 = 0, the left ideal A k and the right
    ideal k A (both as spans of products acting on the exterior algebra) have rank 2^(n-1) and coincide, and
    J^2 = 0 (a k b k = 0 for all basis pairs).
(3) Support exactly on the wall: along G(tau) = G0 + tau E_kk (k the radical at tau = 0), A k has rank 2^n
    at tau = 1/3, -2, 5 (k invertible, k^2 = tau) and 2^(n-1) at tau = 0.
(4) Off the wall, the physical case: Cl(1,3) and Cl(0,4) both have centre R (dimension 1), an idempotent
    P with dim A P = 8 and corner P A P of dimension 4 containing i, j with i^2 = j^2 = -P, ij = -ji,
    spanned by P, i, j, ij: so both are Mat_2(H). The wall quotient there is Cl(0, 3).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

GRAMS = [
    [[1, 1, 0], [1, 1, 0], [0, 0, -1]],
    [[2, 1, 1], [1, 0, 1], [1, 1, 0]],
    [[1, 0, 1, 0], [0, -1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 2]],
    [[0, 1, 0, 1], [1, 0, 0, 1], [0, 0, -1, 0], [1, 1, 0, 2]],
]


def blade_el(I):
    return {tuple(I): F(1)}


def check_wall_fibre_ideal_and_quotient():
    premise("sheaf.tameness")
    premise("sheaf.blade-basis-degenerate-forms-included")
    count = 0
    for n in range(1, 6):
        for p in range(1, n + 1):
            q = n - p
            sq = GA.sig(p - 1, q, 1)
            k = GA.gen(n - 1)
            blades = GA.all_blades(n)
            for i in range(n - 1):
                assert GA.anticommutes(k, GA.gen(i), sq)
            for I in blades:
                b = blade_el(I)
                assert GA.eq(GA.mul(k, b, sq), GA.mul(GA.grade_inv(b), k, sq))
            Ak = [GA.mul(blade_el(I), k, sq) for I in blades]
            kA = [GA.mul(k, blade_el(I), sq) for I in blades]
            r1 = GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in Ak])
            r2 = GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in kA])
            r12 = GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in Ak + kA])
            assert r1 == r2 == r12 == 2 ** (n - 1)
            Jb = [GA.mul(blade_el(I), k, sq) for I in GA.all_blades(n - 1)]
            assert all(GA.is_zero(GA.mul(x, y, sq)) for x in Jb for y in Jb)
            sq_quot = GA.sig(p - 1, q)
            for I in GA.all_blades(n - 1):
                for J in GA.all_blades(n - 1):
                    full = GA.mul(blade_el(I), blade_el(J), sq)
                    proj = {bb: c for bb, c in full.items() if (n - 1) not in bb}
                    assert GA.eq(proj, GA.mul(blade_el(I), blade_el(J), sq_quot))
            count += 1
    assert count == 15


def element_state(I, B, n):
    return GA.ext_sigma_blade(list(I), B, n)


def act_blade(I, B, n, state):
    for i in reversed(I):
        state = GA.ext_c([F(int(j == i)) for j in range(n)], B, state)
    return state


def svec(state, keys):
    return [state.get(K, F(0)) for K in keys]


def radical(B):
    n = len(B)
    rows = [[F(B[i][j]) for j in range(n)] for i in range(n)]
    ker = GA.field_kernel(rows)
    assert len(ker) == 1
    return ker[0]


def check_non_orthogonal_wall_fibres():
    premise("sheaf.blade-basis-degenerate-forms-included")
    for B in GRAMS:
        n = len(B)
        k = radical(B)
        assert sum(1 for x in k if x != 0) >= 2
        keys = [frozenset(S) for r in range(n + 1) for S in combinations(range(n), r)]
        blades = GA.all_blades(n)
        one = {frozenset(): F(1)}
        kstate = GA.ext_c(k, B, one)
        assert not GA.ext_c(k, B, kstate)                         # k^2 = 0
        left = [act_blade(I, B, n, kstate) for I in blades]       # a k
        right = [GA.ext_c(k, B, element_state(I, B, n)) for I in blades]   # k a
        rl = GA.rank_of_vectors([svec(x, keys) for x in left])
        rr = GA.rank_of_vectors([svec(x, keys) for x in right])
        rb = GA.rank_of_vectors([svec(x, keys) for x in left + right])
        assert rl == rr == rb == 2 ** (n - 1)
        for I in blades:
            for J in blades:
                # (e_I k)(e_J k) acting on 1: e_I k e_J k 1
                st = act_blade(I, B, n, GA.ext_c(k, B, act_blade(J, B, n, kstate)))
                assert not st


def check_ideal_supported_exactly_on_the_wall():
    for n in (3, 4):
        keys = [frozenset(S) for r in range(n + 1) for S in combinations(range(n), r)]
        blades = GA.all_blades(n)
        for tau in (F(0), F(1, 3), F(-2), F(5)):
            B = [[F(0)] * n for _ in range(n)]
            B[0][0] = tau
            for i in range(1, n):
                B[i][i] = F(1) if i == 1 else F(-1)
            k = [F(1)] + [F(0)] * (n - 1)
            kstate = GA.ext_c(k, B, {frozenset(): F(1)})
            r = GA.rank_of_vectors([svec(act_blade(I, B, n, kstate), keys) for I in blades])
            assert r == (2 ** (n - 1) if tau == 0 else 2 ** n)


def corner_is_quaternions(p, q, P):
    sq = GA.sig(p, q)
    n = p + q
    blades = GA.all_blades(n)
    corner = [GA.mul(GA.mul(P, blade_el(I), sq), P, sq) for I in blades]
    AP = [GA.mul(blade_el(I), P, sq) for I in blades]
    if GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in AP]) != 8:
        return False
    if GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in corner]) != 4:
        return False
    units = [x for x in corner if not GA.is_zero(x) and GA.eq(GA.mul(x, x, sq), GA.scal(-1, P))]
    for i in units:
        for j in units:
            if GA.is_zero(GA.add(GA.mul(i, j, sq), GA.mul(j, i, sq))):
                ij = GA.mul(i, j, sq)
                span = [P, i, j, ij]
                if GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in span]) == 4:
                    return True
    return False


def check_physical_fibres_are_mat2_quaternions():
    premise("sheaf.imported-classification-values")
    half = F(1, 2)
    for (p, q, gen_list) in ((1, 3, [0]), (0, 4, [0, 1, 2])):
        sq = GA.sig(p, q)
        n = p + q
        blades = GA.all_blades(n)
        cen = [I for I in blades if all(GA.commutes(blade_el(I), GA.gen(i), sq) for i in range(n))]
        assert cen == [()]
        g = GA.sc(1)
        for i in gen_list:
            g = GA.mul(g, GA.gen(i), sq)
        assert GA.eq(GA.mul(g, g, sq), GA.sc(1))
        P = GA.scal(half, GA.add(GA.sc(1), g))
        assert GA.eq(GA.mul(P, P, GA.sig(p, q)), P)
        assert corner_is_quaternions(p, q, P)
    # the physical wall quotient (p-1, q) = (0, 3): Cl(0,3) has centre span(1, e0e1e2)
    sq3 = GA.sig(0, 3)
    cen3 = [I for I in GA.all_blades(3) if all(GA.commutes(blade_el(I), GA.gen(i), sq3) for i in range(3))]
    assert cen3 == [(), (0, 1, 2)]
