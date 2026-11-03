"""transport.representation-independent-minimality-completion: exact checks.

M_ij = -1/2 Q(p_i - p_j) for the n + 2 points p_0 = 0, p_i = e_i, p_{n+1} = 2 e_1 of Lemma
transport.conformal-gram-matrix.
(1) The chart exists in the model: in Cl(p+1, q+1) the lifts s_i = X(p_i) satisfy
    s_i . s_j = M_ij, M has rank n + 2 and signature (p+1, q+1), and the s_i span the whole
    ambient (rank n + 2): equality case, signature exactly (p+1, q+1). All 20 signatures with
    1 <= n <= 5.
(2) Larger hosts: in V'' = R^(p+1, q+1) + R^(a, b) (non-diagonal extra block) the same s_i give the
    chart; S^perp has signature (a, b) and p'' = (p + 1) + a, q'' = (q + 1) + b (orthogonal
    splitting computed from the Gram matrix of S + S^perp).
(3) Smaller or differently balanced hosts are excluded: a Gram matrix S^T J S of n + 2 vectors in
    a space of signature (p'', q'') has positive index <= p'' and negative index <= q''
    (inertia, tested on sample S); since M has indices (p+1, q+1), every (p'', q'') with
    p'' < p + 1 or q'' < q + 1 and p'' + q'' <= n + 3 admits no chart.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SAMPLE_S = [
    [[1, 0, 2], [0, 1, -1], [3, 1, 0], [1, 1, 1]],
    [[2, -1, 0, 1], [1, 1, 1, 1], [0, 3, -2, 1]],
    [[1, 2], [3, 4], [5, 6], [0, 1], [1, 0]],
]


def _M(p, q):
    n = p + q
    sqV = GA.sig(p, q)
    pts = [[F(0)] * n] + [[F(1) if j == i else F(0) for j in range(n)] for i in range(n)]
    pts.append([F(2) if j == 0 else F(0) for j in range(n)])

    def Q(v):
        return sum(sqV[i] * v[i] * v[i] for i in range(n))

    M = [[-Q([a - b for a, b in zip(x, y)]) / 2 for y in pts] for x in pts]
    return pts, M


def _lift(pt, n, sq):
    ep, em = GA.gen(n), GA.gen(n + 1)
    n0 = GA.scal(F(1, 2), GA.sub(em, ep))
    ninf = GA.add(em, ep)
    x = {(i,): c for i, c in enumerate(pt) if c != 0}
    Qx = GA.mul(x, x, sq).get((), F(0))
    return GA.add(n0, x, GA.scal(Qx / 2, ninf))


def check_chart_in_the_model_equality_case():
    premise("transport.conformal-gram-matrix")
    ok = True
    count = 0
    for n in range(1, 6):
        for p in range(n + 1):
            q = n - p
            pts, M = _M(p, q)
            ok = ok and GA.mat_rank(M) == n + 2 and GA.congruence_signature(M) == (p + 1, q + 1, 0)
            sq = GA.sig(p, q) + (1, -1)
            S = [_lift(pt, n, sq) for pt in pts]
            ok = ok and all(GA.dot(S[i], S[j], sq) == M[i][j] for i in range(n + 2) for j in range(n + 2))
            rows = [[s.get((k,), F(0)) for k in range(n + 2)] for s in S]
            ok = ok and GA.mat_rank(rows) == n + 2
            count += 1
    ok = ok and count == 20
    GA.check("M has signature (p+1,q+1), rank n+2, and is realised by the lifts spanning R^(p+1,q+1)", ok)
    return ok


# Sample extra blocks (Gram matrices of the adjoined summand: definite, indefinite, hyperbolic, rank 3)
# and sample base signatures.
EXTRA_BLOCKS = [[[1]], [[-1]], [[2, 1], [1, -3]], [[0, 1], [1, 0]], [[1, 1, 0], [1, 2, 1], [0, 1, -1]]]
HOST_SIGNATURES = [(1, 1), (1, 3), (3, 1), (2, 0), (0, 2), (2, 2)]


def unit_rows(m):
    """The standard basis of Q^m as rows."""
    return [[F(1) if j == i else F(0) for j in range(m)] for i in range(m)]


def check_larger_hosts_split_off_the_chart():
    premise("transport.conformal-gram-matrix")
    ok = True
    for (p, q) in HOST_SIGNATURES:
        n = p + q
        pts, M = _M(p, q)
        sq = GA.sig(p, q) + (1, -1)
        d = len(sq)
        S = [_lift(pt, n, sq) for pt in pts]
        for X in EXTRA_BLOCKS:
            m = len(X)
            a, b, _ = GA.congruence_signature(X)
            N = d + m
            G = [[F(0)] * N for _ in range(N)]
            for i in range(d):
                G[i][i] = F(sq[i])
            for i in range(m):
                for j in range(m):
                    G[d + i][d + j] = F(X[i][j])
            P, Qn, Z = GA.congruence_signature(G)
            ok = ok and Z == 0 and P == p + 1 + a and Qn == q + 1 + b
            # the chart vectors, embedded, still have Gram M; their complement is the extra block
            emb = [[s.get((k,), F(0)) for k in range(d)] + [F(0)] * m for s in S]
            gram = [[sum(u[i] * G[i][j] * v[j] for i in range(N) for j in range(N)) for v in emb] for u in emb]
            ok = ok and gram == M
            perp = [[F(0)] * d + row for row in unit_rows(m)]
            ok = ok and all(sum(u[i] * G[i][j] * v[j] for i in range(N) for j in range(N)) == 0
                            for u in emb for v in perp)
            # the chart spans the n + 2 ambient directions, so its complement has dimension exactly m
            ok = ok and GA.rank_of_vectors(emb) == n + 2 and GA.rank_of_vectors(perp) == m
    GA.check("in larger hosts the chart splits off: p'' = p+1+a, q'' = q+1+b", ok)
    return ok


def check_smaller_hosts_admit_no_chart():
    premise("transport.conformal-gram-matrix")
    ok = True
    # inertia: positive / negative index of S^T J S bounded by those of J
    for S in SAMPLE_S:
        d = len(S)
        for pp in range(d + 1):
            J = [[F(1 if i < pp else -1) if i == j else F(0) for j in range(d)] for i in range(d)]
            k = len(S[0])
            G = [[sum(F(S[a][u]) * J[a][b] * F(S[b][v]) for a in range(d) for b in range(d))
                  for v in range(k)] for u in range(k)]
            P, N, _ = GA.congruence_signature(G)
            ok = ok and P <= pp and N <= d - pp
    excluded = 0
    for (p, q) in [(1, 1), (1, 3), (3, 1), (2, 1), (0, 3)]:
        n = p + q
        _, M = _M(p, q)
        P, N, _ = GA.congruence_signature(M)
        for pp in range(0, n + 4):
            for qq in range(0, n + 4 - pp):
                if pp < p + 1 or qq < q + 1:
                    ok = ok and (P > pp or N > qq)
                    excluded += 1
    # hosts with p'' + q'' <= n + 3: (n+4)(n+5)/2 pairs, of which 3 are admissible
    # ((p+1, q+1), (p+2, q+1), (p+1, q+2)); excluded 18 for (1,1), 33 for (1,3) and (3,1),
    # 25 for (2,1) and (0,3)
    ok = ok and excluded == 18 + 33 + 33 + 25 + 25
    GA.check("no chart in any host with p'' < p+1 or q'' < q+1 (inertia), 134 hosts excluded", ok)
    return ok
