from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def wedge(i, st):
    return GA.ext_wedge(i, st)


def contract(i, st, k):
    return GA.ext_contract([F(1) if j == i else F(0) for j in range(k)], st)


def keys(k):
    return [frozenset(I) for m in range(k + 1) for I in combinations(range(k), m)]


def op_matrix(fn, k):
    ks = keys(k)
    cols = []
    for K in ks:
        out = fn({K: F(1)})
        cols.append([out.get(L, F(0)) for L in ks])
    return [[cols[j][i] for j in range(len(ks))] for i in range(len(ks))]


def gen_matrices(k):
    """c(e_i) = contract_i + wedge_i (Q = +1) and c(e_(k+i)) = contract_i - wedge_i (Q = -1):
    e_i = v_i + w_i, e_(k+i) = v_i - w_i with v_i acting by contraction, w_i by wedge."""
    ms = []
    for i in range(k):
        ms.append(op_matrix(lambda st, i=i: GA.add(contract(i, st, k), wedge(i, st)), k))
    for i in range(k):
        ms.append(op_matrix(lambda st, i=i: GA.sub(contract(i, st, k), wedge(i, st)), k))
    return ms


def witt_pair(i, k):
    """v_i = (e_i + e_(k+i))/2, w_i = (e_i - e_(k+i))/2 in Cl(k, k)."""
    half = F(1, 2)
    v = {(i,): half, (k + i,): half}
    w = {(i,): half, (k + i,): -half}
    return v, w

KS = [1, 2, 3]


def check_wedge_and_contraction_give_the_whole_matrix_algebra():
    premise("std-algebra.witt-basis-car")
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.blade-basis")
    ok = True
    dims = []
    for k in KS:
        ms = [S.mat(M) for M in gen_matrices(k)]
        ok = ok and S.check_matrix_rep(ms, GA.sig(k, k), 4 ** k)
        dims.append(len(ms[0]))
    ok = ok and dims == [2, 4, 8]
    GA.check("wedge and contraction satisfy the Clifford relations of Cl(k,k) and span End(Lambda W), k = 1, 2, 3", ok)
    return ok


def check_fock_space_is_the_left_ideal_of_the_vacuum():
    premise("std-algebra.witt-basis-car")
    premise("std-algebra.blade-basis")
    ok = True
    ranks = []
    intertwined = 0
    for k in KS:
        sq = GA.sig(k, k)
        n = 2 * k
        pairs = [witt_pair(i, k) for i in range(k)]
        f = GA.sc(1)
        for v, w in pairs:
            f = GA.mul(f, GA.mul(v, w, sq), sq)
        ok = ok and GA.eq(GA.mul(f, f, sq), f)
        ok = ok and all(GA.mul(v, f, sq) == {} for v, w in pairs)
        ranks.append(S.span_rank([GA.mul({b: F(1)}, f, sq) for b in GA.all_blades(n)], n))
        # the basis w_I f, indexed like the exterior basis e_I
        ks = keys(k)
        basis = {}
        for K in ks:
            x = GA.sc(1)
            for i in sorted(K):
                x = GA.mul(x, pairs[i][1], sq)
            basis[K] = GA.mul(x, f, sq)
        ok = ok and S.span_rank(list(basis.values()), n) == 2 ** k
        ms = gen_matrices(k)
        for a in range(n):
            M = ms[a]
            for col, K in enumerate(ks):
                lhs = GA.mul(GA.gen(a), basis[K], sq)
                rhs = GA.add(*[GA.scal(M[row][col], basis[L]) for row, L in enumerate(ks)])
                ok = ok and GA.eq(lhs, rhs)
                intertwined += 1
    ok = ok and ranks == [2, 4, 8]
    ok = ok and intertwined == 2 * 2 + 4 * 4 + 6 * 8
    GA.check("f = prod v_i w_i is an idempotent killed by every v_i; Cl f has dimension 2^k and w_I f -> e_I intertwines", ok)
    return ok
