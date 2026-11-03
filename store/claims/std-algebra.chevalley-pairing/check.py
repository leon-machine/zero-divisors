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

KS = [1, 2, 3, 4]


def sign_reversal(m):
    return (-1) ** (m * (m - 1) // 2)


def wedge_states(x, y):
    out = {}
    for S_, a in x.items():
        for T, b in y.items():
            if S_ & T:
                continue
            sgn = (-1) ** sum(1 for s in S_ for t in T if s > t)
            K = S_ | T
            out[K] = out.get(K, F(0)) + sgn * a * b
    return {K: c for K, c in out.items() if c != 0}


def beta(x, y, k):
    tx = {S_: sign_reversal(len(S_)) * c for S_, c in x.items()}
    return wedge_states(tx, y).get(frozenset(range(k)), F(0))


def apply(M, st, k):
    ks = keys(k)
    vec = [st.get(K, F(0)) for K in ks]
    out = [sum(M[r][c] * vec[c] for c in range(len(ks))) for r in range(len(ks))]
    return {K: v for K, v in zip(ks, out) if v != 0}


def check_pairing_nondegenerate_symmetry_and_self_adjoint_vectors():
    premise("std-algebra.fock-representation")
    premise("std-algebra.involution-properties")
    ok = True
    ranks, signs = [], []
    for k in KS:
        ks = keys(k)
        basis = [{K: F(1)} for K in ks]
        G = [[beta(x, y, k) for y in basis] for x in basis]
        ranks.append(GA.mat_rank(G))
        sym = [G[i][j] == G[j][i] for i in range(len(ks)) for j in range(len(ks))]
        anti = [G[i][j] == -G[j][i] for i in range(len(ks)) for j in range(len(ks))]
        signs.append(1 if all(sym) else (-1 if all(anti) else 0))
        for i, K in enumerate(ks):
            for j, L in enumerate(ks):
                if G[i][j] != 0:
                    ok = ok and len(K) + len(L) == k
        for M in gen_matrices(k):
            for x in basis:
                for y in basis:
                    ok = ok and beta(apply(M, x, k), y, k) == beta(x, apply(M, y, k), k)
    ok = ok and ranks == [2, 4, 8, 16]
    ok = ok and signs == [1, -1, -1, 1]
    GA.check("beta nondegenerate, pairs degree m with k - m, symmetry (-1)^(k(k-1)/2), every generator self-adjoint (k <= 4)", ok)
    return ok


def check_elements_with_unit_norm_preserve_the_pairing():
    premise("std-algebra.fock-representation")
    ok = True
    tested = 0
    for k in KS[1:]:
        ms = gen_matrices(k)
        n = len(ms[0])
        # R = 5/4 + 3/4 e_0 e_k (a boost in the plane of e_0, e_k): reverse(R) R = 1
        E0k = GA.mat_mul(ms[0], ms[k])
        R = [[F(5, 4) * (1 if r == c else 0) + F(3, 4) * E0k[r][c] for c in range(n)] for r in range(n)]
        Rt = [[F(5, 4) * (1 if r == c else 0) - F(3, 4) * E0k[r][c] for c in range(n)] for r in range(n)]
        ident = [[F(1) if r == c else F(0) for c in range(n)] for r in range(n)]
        ok = ok and GA.mat_mul(Rt, R) == ident
        basis = [{K: F(1)} for K in keys(k)]
        for x in basis:
            for y in basis:
                ok = ok and beta(apply(R, x, k), apply(R, y, k), k) == beta(x, y, k)
                tested += 1
        # control: R itself is not self-adjoint
        ok = ok and any(beta(apply(R, x, k), y, k) != beta(x, apply(R, y, k), k) for x in basis for y in basis)
    ok = ok and tested == 16 + 64 + 256
    GA.check("an element with reverse(R) R = 1 preserves beta (k = 2, 3, 4)", ok)
    return ok
