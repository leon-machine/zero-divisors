"""scrambling.pair-mode-qubit-one-object: exact checks.

Cl(2,4) in GA.py (generators 0, 1 square +1; 2..5 square -1). Two ladder pairs on orthogonal
hyperbolic planes: v_1 = (e_0 + e_2)/2, w_1 = (e_0 - e_2)/2, v_2 = (e_1 + e_3)/2, w_2 = (e_1 - e_3)/2.
(1) The two pairs satisfy the CAR of two modes, all relations exactly, as vectors of Cl(2,4).
(2) No third pair: the creation span W = span(v_1, v_2) is maximal isotropic, since the form on
    W^perp has signature (0, 2, 2) (W^perp / W negative definite), and an exhaustive search over the
    isotropic vectors of R^(2,4) with coefficients in {-1,0,1} finds no totally isotropic subspace
    of dimension 3: exactly two pairs, the Witt index min(2,4).
(3) One pair is one qubit: on the Fock space of one mode (basis |0>, v|0>), v and w act by the
    matrices E21 and E12, w|0> = 0, and 1, v, w, vw span all of Mat_2 (rank 4); for the two pairs
    the Fock space has dimension 4 = 2^2. Entropy of the maximally mixed state of d = 2^k states,
    with ln 2 carried as a formal unit: -sum (1/d) ln(1/d) = log2(d) ln 2 = k ln 2; for one pair
    k = 1 (ln 2 nats), for the two pairs of Cl(2,4) k = 2: the count of pairs is the count of modes.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise

S24 = GA.sig(2, 4)


def pairs():
    h = F(1, 2)
    v = [GA.scal(h, GA.add(GA.gen(0), GA.gen(2))), GA.scal(h, GA.add(GA.gen(1), GA.gen(3)))]
    w = [GA.scal(h, GA.sub(GA.gen(0), GA.gen(2))), GA.scal(h, GA.sub(GA.gen(1), GA.gen(3)))]
    return v, w


def anti(a, b):
    return GA.add(GA.mul(a, b, S24), GA.mul(b, a, S24))


def check_two_pairs_satisfy_car_in_cl24():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    v, w = pairs()
    for i in range(2):
        for j in range(2):
            assert GA.is_zero(anti(v[i], v[j])) and GA.is_zero(anti(w[i], w[j]))
            assert GA.eq(anti(v[i], w[j]), GA.sc(1) if i == j else {})
    return True


def check_no_third_pair():
    premise("tower.witt-index-quantum-capacity")
    v, _ = pairs()
    rows = [[S24[i] * x.get((i,), F(0)) for i in range(6)] for x in v]
    perp = GA.field_kernel(rows)
    assert len(perp) == 4
    gram = [[sum(S24[i] * a[i] * b[i] for i in range(6)) for b in perp] for a in perp]
    assert GA.congruence_signature(gram) == (0, 2, 2)
    iso = []
    for co in product((-1, 0, 1), repeat=6):
        if any(co) and sum(S24[i] * co[i] * co[i] for i in range(6)) == 0:
            if next(c for c in co if c) > 0:
                iso.append([F(c) for c in co])

    def orth(a, b):
        return sum(S24[i] * a[i] * b[i] for i in range(6)) == 0
    best = 0
    for a, b in combinations(range(len(iso)), 2):
        if orth(iso[a], iso[b]) and GA.rank_of_vectors([iso[a], iso[b]]) == 2:
            best = max(best, 2)
            for c in range(b + 1, len(iso)):
                if orth(iso[a], iso[c]) and orth(iso[b], iso[c]):
                    best = max(best, GA.rank_of_vectors([iso[a], iso[b], iso[c]]))
    assert best == 2
    return True


def check_pair_is_one_qubit():
    premise("tower.fock-module-one-qubit-per-rung")
    # one mode: states |0> = (1, 0), v|0> = (0, 1); v by wedge, w by contraction
    V = [[F(0), F(0)], [F(1), F(0)]]
    W = [[F(0), F(1)], [F(0), F(0)]]
    I2 = [[F(1), F(0)], [F(0), F(1)]]

    def mm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    assert [W[i][0] for i in range(2)] == [0, 0]
    assert [r[0] for r in V] == [0, 1]
    VW, WV = mm(V, W), mm(W, V)
    assert [[VW[i][j] + WV[i][j] for j in range(2)] for i in range(2)] == I2
    assert mm(V, V) == [[0, 0], [0, 0]] and mm(W, W) == [[0, 0], [0, 0]]
    assert GA.rank_of_vectors([sum(M, []) for M in (I2, V, W, VW)]) == 4
    # entropy of the maximally mixed state in units of ln 2: d * (1/d) * log2(d)
    for k, d in ((1, 2), (2, 4)):
        p = F(1, d)
        log2_inv_p = d.bit_length() - 1
        assert 2 ** log2_inv_p == d
        S_over_ln2 = d * p * log2_inv_p
        assert S_over_ln2 == k
    n_pairs = len(pairs()[0])
    assert 2 ** n_pairs == 4
    return True
