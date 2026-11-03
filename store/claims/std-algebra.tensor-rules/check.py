from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def to_mat(M):
    return S.mat(M)


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def right_matrix(x, sq):
    n = len(sq)
    blades = GA.all_blades(n)
    cols = [S.coords(GA.mul({b: F(1)}, x, sq), n) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


def flat(M):
    return [a for row in M for a in row]


# (V signature, W signature): every case of the three plane rules, a degenerate V included
CASES = [
    ((1, 0, 0), (1, 1)), ((0, 1, 0), (1, 1)), ((1, 1, 0), (1, 1)), ((2, 0, 0), (1, 1)),
    ((1, 0, 0), (2, 0)), ((0, 1, 0), (2, 0)), ((1, 1, 0), (2, 0)), ((0, 2, 0), (2, 0)),
    ((1, 0, 0), (0, 2)), ((0, 1, 0), (0, 2)), ((2, 0, 0), (0, 2)), ((1, 0, 1), (0, 2)),
    ((0, 0, 1), (1, 1)),
]


def qkron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def qid(d):
    return [[F(1) if i == j else F(0) for j in range(d)] for i in range(d)]


def rational_rep(ms, sq, dim):
    """Rational version of stdalg.check_matrix_rep: relations, and the 2^n products span dim."""
    n, d = len(ms), len(ms[0])
    one = qid(d)
    ok = all(GA.mat_mul(ms[i], ms[i]) == [[sq[i] * a for a in r] for r in one] for i in range(n))
    for i in range(n):
        for j in range(i + 1, n):
            a, b = GA.mat_mul(ms[i], ms[j]), GA.mat_mul(ms[j], ms[i])
            ok = ok and all(a[x][y] + b[x][y] == 0 for x in range(d) for y in range(d))
    prods = []
    for k in range(n + 1):
        for idx in combinations(range(n), k):
            P = one
            for i in idx:
                P = GA.mat_mul(P, ms[i])
            prods.append(flat(P))
    return ok and GA.rank_of_vectors(prods) == dim


def check_tensor_rule():
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.blade-basis")
    premise("std-algebra.orthogonal-anticommute")
    premise("primer.sign")
    premise("std-algebra.pseudoscalar-commutation")
    ok = True
    results = []
    for (p, q, r), (a, b) in CASES:
        sqV, sqW = GA.sig(p, q, r), GA.sig(a, b)
        nV, nW = len(sqV), len(sqW)
        om = S.pseudoscalar(nW)
        eps = GA.mul(om, om, sqW).get((), F(0))
        ok = ok and eps == (-1) ** (nW * (nW - 1) // 2) * (-1) ** b
        ok = ok and all(GA.anticommutes(om, GA.gen(j), sqW) for j in range(nW))
        IV = qid(2 ** nV)
        LW = S.left_matrix(om, sqW)
        gens = [qkron(S.left_matrix(GA.gen(i), sqV), LW) for i in range(nV)]
        gens += [qkron(IV, S.left_matrix(GA.gen(j), sqW)) for j in range(nW)]
        target = [eps * s for s in sqV] + list(sqW)
        ok = ok and rational_rep(gens, target, 2 ** (nV + nW))
        results.append((target.count(1), target.count(-1), target.count(0)))
    ok = ok and results == [(2, 1, 0), (1, 2, 0), (2, 2, 0), (3, 1, 0),
                            (2, 1, 0), (3, 0, 0), (3, 1, 0), (4, 0, 0),
                            (0, 3, 0), (1, 2, 0), (0, 4, 0), (0, 3, 1),
                            (1, 1, 1)]
    GA.check("Cl(V perp W, eps Q + Q_W) = Cl(V) (x) Cl(W) for thirteen pairs, degenerate V included", ok)
    return ok
