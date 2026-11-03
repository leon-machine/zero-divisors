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


def annihilator(psi, k):
    """Basis of {x = sum a_i v_i + b_i w_i : x psi = 0}, coordinates (a_0..a_(k-1), b_0..b_(k-1))."""
    ks = keys(k)
    cols = []
    for i in range(k):
        out = contract(i, psi, k)
        cols.append([out.get(K, F(0)) for K in ks])
    for i in range(k):
        out = wedge(i, psi)
        cols.append([out.get(K, F(0)) for K in ks])
    M = [[cols[j][r] for j in range(2 * k)] for r in range(len(ks))]
    return S.nullspace(M)


def polar(x, y, k):
    """B(x, y) for x = (a, b): B(v_i, w_j) = delta_ij / 2, null otherwise."""
    return sum(x[i] * y[k + i] + x[k + i] * y[i] for i in range(k)) / 2


def spinor(k, seed, parity):
    out = {}
    for j, K in enumerate(keys(k)):
        if len(K) % 2 != parity:
            continue
        c = (5 * seed + 2 * j + j * j) % 5 - 2
        if c:
            out[K] = F(c)
    return out


def thouless(Z, k):
    """exp(sum_(i<j) Z_ij w_i ^ w_j) applied to 1, the series terminating."""
    def quad(st):
        out = {}
        for i in range(k):
            for j in range(i + 1, k):
                if Z[i][j]:
                    out = GA.add(out, GA.scal(Z[i][j], wedge(i, wedge(j, st))))
        return out
    term = {frozenset(): F(1)}
    total = dict(term)
    m = 1
    while term:
        term = {K: c / m for K, c in quad(term).items()}
        total = GA.add(total, term)
        m += 1
    return total


SAMPLES = [(2, 1), (2, 2), (3, 1), (3, 2), (3, 3)]
ZS = [[[0, 2, -1], [-2, 0, 3], [1, -3, 0]],
      [[0, 1, 0, 2], [-1, 0, 1, 0], [0, -1, 0, 1], [-2, 0, -1, 0]]]


def check_annihilators_null_and_purity_in_low_dimension():
    ok = True
    dims = []
    for k, seed in SAMPLES:
        for parity in (0, 1):
            psi = spinor(k, seed, parity)
            ok = ok and psi != {}
            N = annihilator(psi, k)
            ok = ok and all(polar(x, y, k) == 0 for x in N for y in N)
            dims.append(len(N))
    ok = ok and dims == [2] * 4 + [3] * 6
    # k = 4: 1 + w_1 w_2 w_3 w_4 is annihilated by no vector
    psi = {frozenset(): F(1), frozenset(range(4)): F(1)}
    ok = ok and len(annihilator(psi, 4)) == 0
    # a mixed-parity spinor in k = 2 is not pure
    ok = ok and len(annihilator({frozenset(): F(1), frozenset([0]): F(1)}, 2)) < 2
    GA.check("annihilators are totally null; definite-parity spinors are pure for k = 2, 3; 1 + w1w2w3w4 is not", ok)
    return ok


def check_thouless_form_is_pure():
    ok = True
    dims = []
    for Z in ZS:
        k = len(Z)
        Zf = [[F(a) for a in row] for row in Z]
        psi = thouless(Zf, k)
        N = annihilator(psi, k)
        dims.append(len(N))
        for i in range(k):
            x = [F(1) if j == i else F(0) for j in range(k)] + [-Zf[i][j] for j in range(k)]
            image = GA.add(contract(i, psi, k), *[GA.scal(-Zf[i][j], wedge(j, psi)) for j in range(k)])
            ok = ok and image == {}
            ok = ok and GA.rank_of_vectors(N + [x]) == len(N)
    ok = ok and dims == [3, 4]
    GA.check("the Thouless spinors exp(Z_ij w_i w_j) are pure with annihilator v_i - Z_ij w_j (k = 3, 4)", ok)
    return ok
