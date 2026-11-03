"""one-relation.overlap-table-sorted: exact checks of the computable parts (i) and (ii).

(i) One count in two vocabularies. For every base (p,q) with n = p + q <= 3, in Cl(p+1,q+1) (GA.py; the
    adjoined pair e+ of square +1 and e- of square -1 at indices n, n+1) the ladder pair f = (e+ + e-)/2,
    f* = (e+ - e-)/2 gives matrix units E11 = f f*, E22 = f* f, E12 = f, E21 = f* (E11 + E22 = 1,
    E_ij E_kl = delta_jk E_il); E11 commutes with the base generators, so a -> a E11 is a homomorphism,
    injective (rank 2^n), and its image is the whole corner E11 B E11: Cl(p+1,q+1) = Mat_2(Cl(p,q)), one
    matrix doubling per rung; the four blocks E_i1 (A E11) E_1j span all 4 * 2^n dimensions. The adjoined
    pair is one more CAR mode (the capacity increments are checked in the two-capacities claim).
(ii) An identification: in C^6 with the (2,4) form, three pairwise orthogonal null vectors span an
    isotropic U of dimension 3 with U-perp = U (computed over Q(i)), so the maximal isotropic dimension is
    3 = (n + 2)/2 at n = 4 = floor(6/2) = r_C(2,4).
(iii) and the placement of the constants are readings and identifications, not computations.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
BASES = [(p, n - p) for n in range(0, 4) for p in range(n + 1)]


def rank(xs, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in xs])


def check_ladder_pair_doubles_the_algebra():
    premise("one-relation.imported-completion-ladder")
    premise("one-relation.two-presentations")
    ok = len(BASES) == 10
    for p, q in BASES:
        n = p + q
        S = GA.sig(p, q) + (1, -1)
        N = n + 2
        f = GA.scal(F(1, 2), GA.add(GA.gen(n), GA.gen(n + 1)))
        fs = GA.scal(F(1, 2), GA.sub(GA.gen(n), GA.gen(n + 1)))
        E = {(1, 1): GA.mul(f, fs, S), (2, 2): GA.mul(fs, f, S), (1, 2): f, (2, 1): fs}
        ok = ok and GA.eq(GA.add(E[(1, 1)], E[(2, 2)]), GA.sc(1))
        for (i, j) in E:
            for (k, l) in E:
                ok = ok and GA.eq(GA.mul(E[(i, j)], E[(k, l)], S), E[(i, l)] if j == k else {})
        e = E[(1, 1)]
        ok = ok and all(GA.commutes(GA.gen(i), e, S) for i in range(n))
        base = [GA.mul({b: F(1)}, e, S) for b in GA.all_blades(n)]
        corner = [GA.mul(GA.mul(e, {b: F(1)}, S), e, S) for b in GA.all_blades(N)]
        ok = ok and rank(base, N) == 2 ** n == rank(corner, N) and rank(base + corner, N) == 2 ** n
        # the four corners E_i1 B E_1j together span B: the dimension shadow 4 * 2^n, computed
        blocks = [GA.mul(GA.mul(E[(i, 1)], x, S), E[(1, j)], S) for i in (1, 2) for j in (1, 2) for x in base]
        ok = ok and rank(blocks, N) == 4 * 2 ** n
    _tp_rv = (ok); assert _tp_rv is not False, "check_ladder_pair_doubles_the_algebra"; return _tp_rv


def check_pair_count_is_the_complex_capacity():
    premise("standard-model.pair-count-dimension")
    premise("one-relation.two-capacities-three-consequences")
    S = GA.sig(2, 4)
    half = F(1, 2)
    U = []
    for a, b in ((0, 2), (1, 3)):
        v = [QI(0)] * 6
        v[a], v[b] = QI(half), QI(half)
        U.append(v)
    v = [QI(0)] * 6
    v[4], v[5] = QI(half), QI(0, half)
    U.append(v)
    ok = all(sum((u[i] * w[i] * S[i] for i in range(6)), QI(0)) == 0 for u in U for w in U)
    ok = ok and GA.field_rank(U) == 3
    perp = GA.field_kernel([[u[i] * S[i] for i in range(6)] for u in U])
    ok = ok and len(perp) == 3 and GA.field_rank(perp + U) == 3
    ok = ok and len(U) == (4 + 2) // 2 == 6 // 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_pair_count_is_the_complex_capacity"; return _tp_rv
