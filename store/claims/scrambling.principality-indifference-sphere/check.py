"""scrambling.principality-indifference-sphere: exact checks of the mathematical core.

The selection itself rests on the indifference Principle (a premise, not computable). Checked, for
every n = 2..6 and every partition lambda of n, on the sl_2 embedding into Mat_n built as the
direct sum of irreducible blocks (block of size m: h v_k = (m - 1 - 2k) v_k, f v_k = v_(k+1),
e v_k = k(m - k) v_(k-1)), with exact rational matrices:
(1) [e, f] = h, [h, e] = 2e, [h, f] = -2f; the Jordan type of e (ranks of its powers) recovers
    lambda, so the embedding carries exactly the partition data of Fact
    imported-kostant-madore-partition-data (i).
(2) The adjoint decomposition of Mat_n: dim ker ad_e (the number of irreducible summands) is
    sum_ab min(lambda_a, lambda_b), and the number of trivial summands (dim ker ad_e intersect
    ker ad_h, the commutant of the embedded sl_2) is the number of pairs of equal parts. The
    principal embedding (lambda = (n)) is the only one whose summands have distinct ad_h highest
    weights, 0, 2, ..., 2(n - 1) (multiplicity free, 1 + 3 + ... + (2n - 1) = n^2); every other
    partition has a repeated summand.
(3) Fuzzy sphere: the Casimir ef + fe + h^2/2 is a scalar exactly when all parts are equal (value
    (m^2 - 1)/2 for parts m), and the commutant of the embedded sl_2 is one-dimensional exactly for
    lambda = (n): only the principal embedding gives one irreducible round fuzzy sphere,
    sum X_i^2 proportional to 1 with trivial commutant; the other isotypic partitions (k, ..., k)
    give copies of a smaller sphere with a k^2-dimensional commutant (partition data).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def triple(lam):
    n = sum(lam)
    e = [[F(0)] * n for _ in range(n)]
    f = [[F(0)] * n for _ in range(n)]
    h = [[F(0)] * n for _ in range(n)]
    off = 0
    for m in lam:
        for k in range(m):
            h[off + k][off + k] = F(m - 1 - 2 * k)
            if k + 1 < m:
                f[off + k + 1][off + k] = F(1)
            if k > 0:
                e[off + k - 1][off + k] = F(k * (m - k))
        off += m
    return e, f, h


def mm(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n) if A[i][k]), F(0)) for j in range(n)] for i in range(n)]


def sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def scal(c, A):
    return [[c * a for a in r] for r in A]


def comm(A, B):
    return sub(mm(A, B), mm(B, A))


def ad_matrix(X):
    n = len(X)
    cols = []
    for i in range(n):
        for j in range(n):
            U = [[F(1) if (r, c) == (i, j) else F(0) for c in range(n)] for r in range(n)]
            C = comm(X, U)
            cols.append([C[r][c] for r in range(n) for c in range(n)])
    return [[cols[c][r] for c in range(n * n)] for r in range(n * n)]


rank = GA.mat_rank


def check_triples_and_partition_data():
    premise("scrambling.imported-kostant-madore-partition-data")
    premise("scrambling.boundary-mode-space-matrix")
    count = 0
    for n in range(2, 7):
        for lam in partitions(n):
            e, f, h = triple(lam)
            assert comm(e, f) == h
            assert comm(h, e) == scal(2, e) and comm(h, f) == scal(-2, f)
            # Jordan type of e: number of blocks of size >= k is rank(e^(k-1)) - rank(e^k)
            powers, P = [], [[F(int(i == j)) for j in range(n)] for i in range(n)]
            for k in range(n + 1):
                powers.append(rank(P))
                P = mm(P, e)
            ge = [powers[k - 1] - powers[k] for k in range(1, n + 1)]
            recovered = tuple(sorted((k for k in range(1, n + 1) for _ in range(ge[k - 1] - (ge[k] if k < n else 0))), reverse=True))
            assert recovered == lam
            count += 1
    assert count == 28                                       # p(2) + ... + p(6) = 2 + 3 + 5 + 7 + 11
    return True


def check_principal_is_multiplicity_free():
    premise("scrambling.imported-kostant-madore-partition-data")
    for n in range(2, 7):
        principal_like = []
        for lam in partitions(n):
            e, f, h = triple(lam)
            ade, adh = ad_matrix(e), ad_matrix(h)
            ker_e = n * n - rank(ade)
            assert ker_e == sum(min(a, b) for a in lam for b in lam)
            ker_eh = n * n - rank(ade + adh)
            assert ker_eh == sum(1 for a in lam for b in lam if a == b)
            # highest weights: ad_h is diagonal on matrix units and ad_e raises the weight by 2,
            # so ker ad_e splits by weight; the multiplicity of highest weight w is the kernel
            # dimension of ad_e on the weight-w columns
            weights = []
            for w in sorted({adh[c][c] for c in range(n * n)}):
                cols = [c for c in range(n * n) if adh[c][c] == w]
                sub_ = [[ade[r][c] for c in cols] for r in range(n * n)]
                weights.extend([w] * (len(cols) - rank(sub_)))
            assert len(weights) == ker_e
            distinct = len(set(weights)) == len(weights)
            if distinct and ker_e == n:
                principal_like.append(lam)
                assert sorted(weights) == [F(2 * l) for l in range(n)]
                assert sum(2 * l + 1 for l in range(n)) == n * n
        assert principal_like == [(n,)]
    return True


def check_round_irreducible_sphere_only_for_principal():
    premise("scrambling.imported-kostant-madore-partition-data")
    for n in range(2, 7):
        for lam in partitions(n):
            e, f, h = triple(lam)
            C = [[a + b + c for a, b, c in zip(r1, r2, r3)]
                 for r1, r2, r3 in zip(mm(e, f), mm(f, e), scal(F(1, 2), mm(h, h)))]
            is_scalar = all(C[i][j] == (C[0][0] if i == j else 0) for i in range(n) for j in range(n))
            assert is_scalar == (len(set(lam)) == 1)
            if is_scalar:
                assert C[0][0] == F(lam[0] * lam[0] - 1, 2)
            # commutant of the image: matrices commuting with e, f, h
            comm_dim = n * n - rank(ad_matrix(e) + ad_matrix(f) + ad_matrix(h))
            assert comm_dim == sum(1 for a in lam for b in lam if a == b)
            assert (is_scalar and comm_dim == 1) == (lam == (n,))
    return True
