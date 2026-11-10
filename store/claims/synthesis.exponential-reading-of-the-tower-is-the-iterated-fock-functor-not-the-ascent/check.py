"""synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent: exact checks.

B_k = Cl(k,k) in GA.py with generators e_0..e_{k-1} (square +1) and f_0..f_{k-1} (square -1), ladder
pairs v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2 (the stored convention e_j = v_j + w_j, f_j = v_j - w_j),
vacuum idempotent P = prod_j w_j v_j, Fock module the left ideal B_k P. Everything is exact.
(i)   dim B_3 P = 8 by rank; the level above with pairs indexed by the 8 states is Cl(8,8): its 8 pairs
      satisfy the CAR as vectors, its vacuum idempotent has scalar part 1/256 (normalised trace of a rank-one
      idempotent of Mat_256), and on the exterior algebra of 8 letters the contractions have a one-dimensional
      common kernel and the creation monomials reach 256 states. Iterating k -> 2^k from 3: 3, 8, 256, 2^256.
(ii)  One ascent from three pairs is Cl(4,4): 4 pairs, module of dimension 16; 2^k = k + 1 only at k = 0, 1.
(iii) A CAR family of non-vector elements (the ladder pairs conjugated by the unit 1 + v_0 e_1 f_1, not a versor) has
      linearly independent ordered monomials: 16 in B_2, 64 in B_3, so three pairs exhaust B_3 and the
      dimension bound 4^m <= 4^j leaves no room for a fourth, nor for eight. On Cl(2,0) (Witt index 0) the
      non-vector pair (e_1 + e_1 e_2)/2, (e_1 - e_1 e_2)/2 is a CAR pair: the bound is not the Witt index there.
(iv)  The second-quantised lift L(X) = sum X_TS V_T W_S of the level's ladder operators into the level above
      (k = 2 in Cl(4,4), k = 3 in Cl(8,8)) is a Lie homomorphism on the pair (v_0, w_0) and is not a CAR
      family: L(v_0)^2 != 0, {L(v_0), L(w_0)} != 1, {L(v_0), L(v_1)} != 0.
(v)   Arithmetic on the quoted bracket 2^407 < |J| < 2^408 for the horizon count: strictly between the levels
      2^256 and 2^(2^256) of (i) (compared on exponents); the bracket is not recomputed.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

BASE = 3
SEARCH_LIMIT = 65       # exponents searched for 2^k = k + 1 (all k in the proof)
SEARCH_STEP = 2
HALF = F(1, 2)


def pairs(k):
    sq = GA.sig(k, k)
    v = [GA.scal(HALF, GA.add(GA.gen(j), GA.gen(k + j))) for j in range(k)]
    w = [GA.scal(HALF, GA.sub(GA.gen(j), GA.gen(k + j))) for j in range(k)]
    return sq, v, w


def acomm(x, y, sq):
    return GA.add(GA.mul(x, y, sq), GA.mul(y, x, sq))


def is_car(sq, a, b):
    m = len(a)
    for i in range(m):
        for j in range(m):
            if not GA.is_zero(acomm(a[i], a[j], sq)) or not GA.is_zero(acomm(b[i], b[j], sq)):
                return False
            if not GA.eq(acomm(a[i], b[j], sq), GA.sc(int(i == j))):
                return False
    return True


def vacuum(sq, v, w):
    P = GA.sc(1)
    for j in range(len(v)):
        P = GA.mul(P, GA.mul(w[j], v[j], sq), sq)
    return P


def ideal_dim(k):
    sq, v, w = pairs(k)
    P = vacuum(sq, v, w)
    assert GA.eq(GA.mul(P, P, sq), P)
    blades = GA.all_blades(k + k)
    return GA.rank_of_vectors([GA.basis_vector_of(GA.mul({b: F(1)}, P, sq), blades) for b in blades])


def subsets(k):
    return [frozenset(c) for r in range(k + 1) for c in combinations(range(k), r)]


def wedge(j, S):
    if j in S:
        return None
    return frozenset(S | {j}), (-1) ** len([i for i in S if i < j])


def contract(j, S):
    if j not in S:
        return None
    return frozenset(S - {j}), (-1) ** len([i for i in S if i < j])


def check_three_pairs_have_eight_states_and_the_level_above_has_eight_pairs_and_256_states():
    premise("tower.fock-module-one-qubit-per-rung")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    sq, v, w = pairs(BASE)
    assert is_car(sq, v, w)
    d = ideal_dim(BASE)
    assert d == 8                                          # the 8 objects of the base level: its Fock states
    states = subsets(BASE)
    assert len(states) == d
    sq2, V, W = pairs(d)                                   # the level above: one null pair per state
    assert len(sq2) == 16 and is_car(sq2, V, W)
    P = vacuum(sq2, V, W)
    assert P.get((), F(0)) == F(1, 256) and len(P) == 256  # normalised trace of a rank-one idempotent of Mat_256
    assert GA.eq(GA.mul(P, GA.mul(W[0], V[0], sq2), sq2), P)
    assert 4 ** d * P.get((), F(0)) == 256                 # dim of the left ideal = dim(algebra) x normalised trace
    up = subsets(d)
    assert len(up) == 256
    kernel = [S for S in up if all(contract(j, S) is None for j in range(d))]
    assert kernel == [frozenset()]                         # Fock criterion: the vacuum line only
    reached = {frozenset()}
    for j in range(d):
        reached |= {wedge(j, S)[0] for S in list(reached) if wedge(j, S) is not None}
    assert len(reached) == 256
    counts = [BASE]
    for _ in range(3):
        counts.append(2 ** counts[-1])
    assert counts[:3] == [3, 8, 256] and counts[3] == 2 ** 256 and counts[3].bit_length() == 257
    return True


def capacities(p, q):
    """(real capacity, twice the complex capacity) of signature (p, q) with p + q even: (min(p, q), p + q)."""
    assert (p + q) % SEARCH_STEP == 0
    return min(p, q), p + q


def check_one_ascent_from_three_pairs_gives_four_pairs_and_sixteen_states():
    premise("tower.witt-index-quantum-capacity")
    premise("one-relation.two-capacities-three-consequences")
    premise("tower.fock-module-one-qubit-per-rung")
    # stored capacities of the complex base (2,4) and of its next floor (3,5): real 2 then 3, complex 3 then 4
    assert capacities(2, 4) == (2, BASE + BASE)
    assert capacities(3, 5) == (3, 8)
    sq, v, w = pairs(BASE + 1)                             # one ascent from three real pairs
    n = len(v)
    assert is_car(sq, v, w) and n == 4
    assert ideal_dim(n) == 16                              # module of the next floor: 16 states, computed as a rank
    assert [k for k in range(SEARCH_LIMIT) if 2 ** k == k + 1] == [0, 1]
    return True


def check_non_vector_car_families_fill_the_level_and_a_non_split_floor_exceeds_its_witt_index():
    premise("tower.commuting-copies")
    premise("std-algebra.existence-uniqueness")
    premise("tower.matrix-amplification-structural-properties")
    for k, full in ((2, 16), (3, 64)):
        sq, v, w = pairs(k)
        n = GA.mul(GA.mul(v[0], GA.gen(1), sq), GA.gen(k + 1), sq)   # nilpotent trivector v_0 e_1 f_1
        assert GA.is_zero(GA.mul(n, n, sq))
        u, ui = GA.add(GA.sc(1), n), GA.sub(GA.sc(1), n)
        assert GA.eq(GA.mul(u, ui, sq), GA.sc(1))
        a = [GA.mul(GA.mul(u, x, sq), ui, sq) for x in v]
        b = [GA.mul(GA.mul(u, x, sq), ui, sq) for x in w]
        assert is_car(sq, a, b)
        assert any(len(blade) != 1 for x in a + b for blade in x)   # not vectors
        gens = a + b
        blades = GA.all_blades(k + k)
        mons = []
        for S in blades:
            m = GA.sc(1)
            for i in S:
                m = GA.mul(m, gens[i], sq)
            mons.append(GA.basis_vector_of(m, blades))
        assert GA.rank_of_vectors(mons) == full == 4 ** k == len(blades)
    assert max(m for m in range(20) if 4 ** m <= 4 ** BASE) == 3     # no fourth pair inside B_3
    assert min(j for j in range(20) if 4 ** (2 ** BASE) <= 4 ** j) == 8   # eight pairs need the floor 8
    # a floor that is not split: Cl(2,0), Witt index 0, holds a CAR pair of non-vector elements
    sq20 = GA.sig(2, 0)
    e1, e12 = GA.gen(0), GA.mul(GA.gen(0), GA.gen(1), sq20)
    a20 = GA.scal(HALF, GA.add(e1, e12))
    b20 = GA.scal(HALF, GA.sub(e1, e12))
    assert is_car(sq20, [a20], [b20]) and min(2, 0) == 0
    assert not is_car(sq20, [e1], [e12])
    return True


def check_the_lift_of_the_ladder_to_the_level_above_is_lie_and_not_car():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("field-theory.second-quantisation")
    terms = {2: 16, 3: 96}
    for k in (2, 3):
        st = subsets(k)
        ix = {S: i for i, S in enumerate(st)}
        sq, V, W = pairs(len(st))

        def lift(op, j):
            out = {}
            for S in st:
                r = op(j, S)
                if r is not None:
                    out = GA.add(out, GA.scal(r[1], GA.mul(V[ix[r[0]]], W[ix[S]], sq)))
            return out

        a0, b0, a1 = lift(wedge, 0), lift(contract, 0), lift(wedge, 1)
        comm = GA.sub(GA.mul(a0, b0, sq), GA.mul(b0, a0, sq))
        target = {}
        for S in st:                                       # [v_0, w_0] is +1 on states containing 0, -1 otherwise
            target = GA.add(target, GA.scal(1 if 0 in S else -1, GA.mul(V[ix[S]], W[ix[S]], sq)))
        assert GA.eq(comm, target)
        sqr = GA.mul(a0, a0, sq)
        assert len(sqr) == terms[k] and not GA.is_zero(sqr)
        assert not GA.eq(acomm(a0, b0, sq), GA.sc(1))
        assert not GA.is_zero(acomm(a0, a1, sq))
    return True


def check_the_quoted_horizon_bracket_lies_between_the_third_and_fourth_levels():
    """Arithmetic on the quoted bracket 2^407 < |J| < 2^408 (not recomputed here). No power above 2^256 is formed:
    2^408 < 2^(2^256) is checked on the exponents."""
    premise("standard-model.trichotomy-what-kind-number")
    premise("synthesis.de-sitter-mode-count")
    premise("synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping")
    lo, hi = 407, 408
    counts = [BASE]
    for _ in range(3):
        counts.append(2 ** counts[-1])
    assert [c <= lo for c in counts] == [True, True, True, False]
    assert hi - counts[2] == 152 and hi < counts[3]
    return True
