"""dark-tower-matter.imported-our-towers-chain: exact checks of the computable parts of the chain.

Complex numbers are Gaussian rationals (GA.QI).
(1) Momenta: for two-component spinors pi, p_AA' = sum pi_A conj(pi)_A'. One constituent: det p = 0
    (null). Two: p^2 = eps^AB eps^A'B' p_AA' p_BB' (contracted explicitly) equals 2 det p and
    2 |<pi1 pi2>|^2 with <pi1 pi2> = pi1_0 pi2_1 - pi1_1 pi2_0; aligned spinors give p^2 = 0.
(2) Three ladder pairs: in Cl(2,4) (e0, e1 of square +1, e2..e5 of square -1) with complex
    coefficients, v_1 = (e0 + e2)/2, w_1 = (e0 - e2)/2, v_2 = (e1 + e3)/2, w_2 = (e1 - e3)/2,
    v_3 = (i e4 + e5)/2, w_3 = (i e4 - e5)/2 satisfy the canonical anticommutation relations
    v_i v_j + v_j v_i = 0, w_i w_j + w_j w_i = 0, v_i w_j + w_j v_i = delta_ij; span{v_i} is totally
    isotropic of dimension 3 = (n + 2)/2 at n = 4, the maximum in V_C of dimension 6 (W in W-perp
    forces dim W <= 3); the Fock space has 2^3 = 8 states, 4 of each parity.
(3) Mixings: on n = 2 and n = 3 constituents, Z^i -> U^i_j Z^j preserves the total momentum
    Pi Pi^dagger and the helicity form sum |Z^i|^2 for unitary U (exact Cayley transforms
    (1 - A)(1 + A)^-1 of anti-Hermitian A, with det U not 1) and fails for non-unitary controls.
(4) Content: the single-spinor grades k = 0..3 carry Lambda^k C^3 with weight q = -2k (Y = q/6);
    listing the even grades and conjugating the odd ones gives (1)_0, (3bar)_1/3, (3bar)_-2/3,
    (1)_1; with Q = (2,3)_1/6 (weight 1) and L = (2,1)_-1/2 (weight -3) all four anomaly sums
    vanish ([SU(3)]^2 U(1), [SU(2)]^2 U(1), U(1)^3, gravitational), every field and the Higgs
    doublet (2,1)_1/2 and its colour partner (1,3)_-1/3 lie on the Z_6 lattice
    (t/3 + delta/2 + Y integral), and the image of u(2) + u(3) acting on C^2 (x) C^3 has real
    dimension 12 = 3 + 8 + 1 (a one-dimensional kernel).
Not computed: the derivations themselves (twistor correspondence, Hypothesis (S)), which the
chain's premises carry.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

QI = GA.QI
SPINORS = [[QI(1, 2), QI(-3, 1)], [QI(2, 0), QI(F(1, 2), -1)], [QI(0, 1), QI(5, 3)]]
ALIGN = QI(F(2, 3), -1)
ANTI_HERM = [
    [[QI(0, 1), QI(2, 1)], [QI(-2, 1), QI(0, -3)]],
    [[QI(0, 2), QI(1, 0), QI(0, 1)], [QI(-1, 0), QI(0, -1), QI(3, 2)], [QI(0, 1), QI(-3, 2), QI(0, 1)]],
]
NON_UNITARY = [
    [[QI(1), QI(1)], [QI(0), QI(1)]],
    [[QI(2), QI(0), QI(0)], [QI(0), QI(1), QI(0)], [QI(0), QI(0), QI(1)]],
]


def outer_sum(spinors):
    return [[sum((s[a] * s[b].conj() for s in spinors), QI(0)) for b in range(2)] for a in range(2)]


def det2(p):
    return p[0][0] * p[1][1] - p[0][1] * p[1][0]


EPS = [[0, 1], [-1, 0]]


def p_squared(p):
    tot = QI(0)
    for A in range(2):
        for B in range(2):
            for A2 in range(2):
                for B2 in range(2):
                    tot = tot + EPS[A][B] * EPS[A2][B2] * p[A][A2] * p[B][B2]
    return tot


def check_one_and_two_constituents():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    for s in SPINORS:
        assert det2(outer_sum([s])) == 0 and p_squared(outer_sum([s])) == 0
    for s1, s2 in combinations(SPINORS, 2):
        p = outer_sum([s1, s2])
        br = s1[0] * s2[1] - s1[1] * s2[0]
        m2 = p_squared(p)
        assert m2 == 2 * det2(p) and m2 == 2 * br * br.conj() and m2 != 0
        aligned = outer_sum([s1, [ALIGN * x for x in s1]])
        assert p_squared(aligned) == 0
    return True


SQ = GA.sig(2, 4)


def cvec(terms):
    return {(i,): c for i, c in terms}


def cmul(x, y):
    out = {}
    for b1, c1 in x.items():
        for b2, c2 in y.items():
            s, b = GA.blade_mul(b1, b2, SQ)
            c = c1 * c2 * s
            out[b] = out.get(b, QI(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def cadd(x, y):
    out = dict(x)
    for b, c in y.items():
        out[b] = out.get(b, QI(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def check_three_ladder_pairs():
    premise("standard-model.pair-count-dimension")
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    h = QI(F(1, 2))
    v = [cvec([(0, h), (2, h)]), cvec([(1, h), (3, h)]), cvec([(4, QI(0, F(1, 2))), (5, h)])]
    w = [cvec([(0, h), (2, -h)]), cvec([(1, h), (3, -h)]), cvec([(4, QI(0, F(1, 2))), (5, -h)])]
    for i in range(3):
        for j in range(3):
            assert cadd(cmul(v[i], v[j]), cmul(v[j], v[i])) == {}
            assert cadd(cmul(w[i], w[j]), cmul(w[j], w[i])) == {}
            vw = cadd(cmul(v[i], w[j]), cmul(w[j], v[i]))
            assert vw == ({(): QI(1)} if i == j else {})
    n = 4
    assert (n + 2) // 2 == len(v) and 2 * len(v) == 6
    states = [S for k in range(4) for S in combinations(range(3), k)]
    assert len(states) == 8 and sum(1 for S in states if len(S) % 2 == 0) == 4
    return True


def det(M):
    if len(M) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return sum((M[0][j] * det([row[:j] + row[j + 1:] for row in M[1:]]) * (1 if j % 2 == 0 else -1)
                for j in range(len(M))), QI(0))


def mat_mul(A, B):
    return GA.field_mat_mul(A, B)


def dagger(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def inverse(M):
    n = len(M)
    cols = [GA.field_solve(M, [QI(1) if i == j else QI(0) for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def cayley(A):
    n = len(A)
    I = [[QI(1) if i == j else QI(0) for j in range(n)] for i in range(n)]
    minus = [[I[i][j] - A[i][j] for j in range(n)] for i in range(n)]
    plus = [[I[i][j] + A[i][j] for j in range(n)] for i in range(n)]
    return mat_mul(minus, inverse(plus))


def invariants(U, spinors):
    n = len(spinors)
    Pi = [[spinors[i][a] for i in range(n)] for a in range(2)]          # 2 x n
    PiU = mat_mul(Pi, [[U[j][i] for j in range(n)] for i in range(n)])  # columns mixed by U
    return mat_mul(Pi, dagger(Pi)), mat_mul(PiU, dagger(PiU))


def check_mixings_are_unitary():
    premise("standard-model.internal-symmetry-ladder")
    for A, B in zip(ANTI_HERM, NON_UNITARY):
        n = len(A)
        assert dagger(A) == [[-x for x in row] for row in A]
        U = cayley(A)
        I = [[QI(1) if i == j else QI(0) for j in range(n)] for i in range(n)]
        assert mat_mul(dagger(U), U) == I
        assert det(U) != QI(1)
        conf = SPINORS[:n]
        before, after = invariants(U, conf)
        assert before == after
        helicity = sum((x * x.conj() for s in conf for x in s), QI(0))
        mixed = [[sum((U[i][j] * conf[j][a] for j in range(n)), QI(0)) for a in range(2)] for i in range(n)]
        assert sum((x * x.conj() for s in mixed for x in s), QI(0)) == helicity
        before, after = invariants(B, conf)
        assert before != after
    return True


def check_content_anomalies_and_lattice():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    premise("standard-model.global-form-quotient-determined")
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    # (name, weak dimension, colour: 0 singlet, 1 triplet, 2 antitriplet, hypercharge)
    singlets = []
    for k in range(4):
        dim = len(list(combinations(range(3), k)))
        colour = {1: 0, 3: 1 if k == 1 else 2}[dim]
        Y = F(-2 * k, 6)
        if k % 2 == 1:                       # conjugate the odd grades
            Y, colour = -Y, {0: 0, 1: 2, 2: 1}[colour]
        singlets.append((1, colour, Y))
    assert [s[2] for s in singlets] == [0, F(1, 3), F(-2, 3), 1]
    fields = [(2, 1, F(1, 6)), (2, 0, F(-3, 6))] + singlets
    ncol = {0: 1, 1: 3, 2: 3}
    su3 = sum(d * Y for d, c, Y in fields if c)
    su2 = sum(ncol[c] * Y for d, c, Y in fields if d == 2)
    cubic = sum(d * ncol[c] * Y ** 3 for d, c, Y in fields)
    grav = sum(d * ncol[c] * Y for d, c, Y in fields)
    assert su3 == 0 and su2 == 0 and cubic == 0 and grav == 0
    for d, c, Y in fields + [(2, 0, F(1, 2)), (1, 1, F(-1, 3))]:
        assert (F(c, 3) + F(d - 1, 2) + Y).denominator == 1
    # the automorphism algebra of C^2 (x) C^3: image of u(2) + u(3) under (X, Y) -> X(x)1 + 1(x)Y
    basis = [(X, None) for X in u_basis(2)] + [(None, Y) for Y in u_basis(3)]
    rows = []
    for X, Y in basis:
        X = X or [[QI(0)] * 2 for _ in range(2)]
        Y = Y or [[QI(0)] * 3 for _ in range(3)]
        M = [[(X[a][b] if c == d else QI(0)) + (Y[c][d] if a == b else QI(0))
              for b in range(2) for d in range(3)] for a in range(2) for c in range(3)]
        rows.append([z for row in M for x in row for z in (x.re, x.im)])
    assert len(basis) == 13 and GA.rank_of_vectors(rows) == 12
    return True


def u_basis(n):
    out = []
    for a in range(n):
        for b in range(n):
            M = [[QI(0)] * n for _ in range(n)]
            if a == b:
                M[a][a] = QI(0, 1)
            elif a < b:
                M[a][b], M[b][a] = QI(1), QI(-1)
            else:
                M[a][b], M[b][a] = QI(0, 1), QI(0, 1)
            out.append(M)
    return out
