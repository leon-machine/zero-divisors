"""standard-model.segre-lemma-automorphisms-preserving-decomposable-tensors: exact checks.

The finite core of the lemma, in exact rational linear algebra.
(1) Infinitesimal form: the linear maps X of C^m (x) C^k whose flow preserves the Segre cone (the
decomposable tensors, cut out by the 2 x 2 minors z_ab z_cd - z_ad z_cb) are those with
D_X(minor) in the span of the minors for every minor. This linear condition is solved exactly for
(m, k) = (2, 2), (2, 3), (3, 2), (2, 4), (3, 3): the solution space has dimension m^2 + k^2 - 1 and
contains every A (x) 1 + 1 (x) B, which span a space of the same dimension, so the identity
component of the stabiliser is {A (x) B}. (The full group statement, including the absence of other
components when m != k, is the lemma's argument and is not reduced to a finite computation.)
(2) The first step of the proof: u (x) v + u' (x) v' has rank 2 when u, u' and v, v' are independent,
and rank at most 1 when they share a factor.
(3) Product form is detected by the realignment R(T) (rank 1 for A (x) B, rank m^2 for the swap): for
m = k the swap preserves decomposable tensors and is not of product form.
(4) Unitary rebalancing: for A = 2 U_1, B = U_2/2 with U_i orthogonal, A (x) B is orthogonal, A^T A = 4,
B^T B = 1/4, and (A/2, 2B) are orthogonal.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise  # noqa: F401  (self-contained classical lemma: no premises)


def stabiliser_dimension(m, k):
    n = m * k
    idx = {(i, j): i * k + j for i in range(m) for j in range(k)}
    minors = [((idx[(a, c)], idx[(b, d)]), (idx[(a, d)], idx[(b, c)]))
              for a, b in combinations(range(m), 2) for c, d in combinations(range(k), 2)]
    nq = len(minors)
    mono = {}
    for p in range(n):
        for q in range(p, n):
            mono[(p, q)] = len(mono)
    ncols = n * n + nq * nq
    rows = []
    for qi, ((A, B), (C, D)) in enumerate(minors):
        eqs = [[F(0)] * ncols for _ in mono]
        # D_X q = z_B (Xz)_A + z_A (Xz)_B - z_D (Xz)_C - z_C (Xz)_D
        for s, (left, mult) in ((1, (A, B)), (1, (B, A)), (-1, (C, D)), (-1, (D, C))):
            for p in range(n):
                key = (min(mult, p), max(mult, p))
                eqs[mono[key]][left * n + p] += s
        # minus sum_q' c_{q,q'} q'
        for qj, ((A2, B2), (C2, D2)) in enumerate(minors):
            col = n * n + qi * nq + qj
            eqs[mono[(min(A2, B2), max(A2, B2))]][col] -= 1
            eqs[mono[(min(C2, D2), max(C2, D2))]][col] += 1
        rows += eqs
    kernel = GA.field_kernel(rows)
    return [vec[:n * n] for vec in kernel]


def kron(A, B):
    return [[A[i // len(B)][j // len(B)] * B[i % len(B)][j % len(B)] for j in range(len(A) * len(B))]
            for i in range(len(A) * len(B))]


def unit(n, a, b):
    return [[F(1) if (i, j) == (a, b) else F(0) for j in range(n)] for i in range(n)]


def product_generators(m, k):
    Im = [[F(int(i == j)) for j in range(m)] for i in range(m)]
    Ik = [[F(int(i == j)) for j in range(k)] for i in range(k)]
    gens = [kron(unit(m, a, b), Ik) for a in range(m) for b in range(m)]
    gens += [kron(Im, unit(k, a, b)) for a in range(k) for b in range(k)]
    return [[x for row in g for x in row] for g in gens]


def realign(T, m, k):
    """R(T)_{(a,a'),(b,b')} = T_{(a,b),(a',b')} for T on C^m (x) C^k."""
    return [[T[a * k + b][a2 * k + b2] for b in range(k) for b2 in range(k)] for a in range(m) for a2 in range(m)]


SHAPES = ((2, 2), (2, 3), (3, 2), (2, 4), (3, 3))


def check_stabiliser_lie_algebra_is_gl_m_plus_gl_k():
    ok = True
    expected = {(2, 2): 7, (2, 3): 12, (3, 2): 12, (2, 4): 19, (3, 3): 17}
    for m, k in SHAPES:
        sol = stabiliser_dimension(m, k)
        dim = GA.mat_rank(sol)
        ok = ok and len(sol) == dim == expected[(m, k)] == m * m + k * k - 1
        # the solutions are exactly the span of A (x) 1 + 1 (x) B
        gens = product_generators(m, k)
        ok = ok and GA.mat_rank(gens) == dim and GA.mat_rank(sol + gens) == dim
    GA.check("Segre: the Lie algebra preserving decomposable tensors is gl(m) + gl(k), dim m^2 + k^2 - 1", ok)
    return ok


def outer(u, v):
    return [[a * b for b in v] for a in u]


def madd(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


U_SAMPLES = ([F(1), F(2)], [F(3), F(-1)], [F(1, 2), F(5)])
V_SAMPLES = ([F(1), F(0), F(2)], [F(0), F(1), F(-3)], [F(2), F(7), F(1)])


def check_sum_of_two_decomposables():
    ok = True
    for u, u2 in combinations(U_SAMPLES, 2):
        for v, v2 in combinations(V_SAMPLES, 2):
            ok = ok and GA.mat_rank(madd(outer(u, v), outer(u2, v2))) == 2
            ok = ok and GA.mat_rank(madd(outer(u, v), outer(u, v2))) == 1
            ok = ok and GA.mat_rank(madd(outer(u, v), outer(u2, v))) == 1
    GA.check("Segre: u(x)v + u'(x)v' has rank 2 iff neither factor is shared", ok)
    return ok


SWAP_U = ([F(1), F(2), F(0)], [F(3), F(-1), F(4)])
SWAP_V = ([F(0), F(1), F(5)], [F(2), F(2), F(-1)])
KA = [[F(1), F(2)], [F(-1), F(3)]]
KB = [[F(2), F(0), F(1)], [F(1), F(1), F(0)], [F(0), F(-2), F(1)]]


def swap_matrix(m):
    return [[F(1) if (i % m, i // m) == (j // m, j % m) else F(0) for j in range(m * m)] for i in range(m * m)]


def check_swap_and_product_form():
    ok = True
    for m in (2, 3):
        swap = swap_matrix(m)
        ok = ok and GA.mat_rank(realign(swap, m, m)) == m * m
        # the swap sends u (x) v to v (x) u: decomposable to decomposable
        for u in SWAP_U:
            for v in SWAP_V:
                t = [x for row in outer(u[:m], v[:m]) for x in row]
                img = [sum(swap[i][j] * t[j] for j in range(m * m)) for i in range(m * m)]
                ok = ok and img == [x for row in outer(v[:m], u[:m]) for x in row]
    ok = ok and GA.mat_rank(realign(swap_matrix(2), 2, 2)) == 4 and GA.mat_rank(realign(swap_matrix(3), 3, 3)) == 9
    ok = ok and GA.mat_rank(realign(kron(KA, KB), 2, 3)) == 1
    GA.check("Segre: product maps have realignment rank 1; the swap (m = k) has rank m^2", ok)
    return ok


def transpose(M):
    return [list(r) for r in zip(*M)]


def check_unitary_rebalancing():
    R1 = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    R2 = [[F(5, 13), F(12, 13), F(0)], [F(-12, 13), F(5, 13), F(0)], [F(0), F(0), F(1)]]
    A = [[2 * x for x in r] for r in R1]
    B = [[x / 2 for x in r] for r in R2]
    T = kron(A, B)
    ok = GA.mat_mul(transpose(T), T) == [[F(int(i == j)) for j in range(6)] for i in range(6)]
    ok = ok and GA.mat_mul(transpose(A), A) == [[F(4) if i == j else F(0) for j in range(2)] for i in range(2)]
    ok = ok and GA.mat_mul(transpose(B), B) == [[F(1, 4) if i == j else F(0) for j in range(3)] for i in range(3)]
    A2 = [[x / 2 for x in r] for r in A]
    B2 = [[2 * x for x in r] for r in B]
    ok = ok and GA.mat_mul(transpose(A2), A2) == [[F(int(i == j)) for j in range(2)] for i in range(2)]
    ok = ok and kron(A2, B2) == T
    GA.check("Segre: a unitary A (x) B rebalances to unitary factors", ok)
    return ok
