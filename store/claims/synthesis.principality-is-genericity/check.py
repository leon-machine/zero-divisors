"""synthesis.principality-is-genericity: exact checks.

For every partition lambda of n (n up to 6) build the standard sl2 triple (e, h, f) in gl_n
block by block, verify the sl2 relations, and compute by exact rank:
  - the centraliser of e (so the conjugation orbit of e has dimension n^2 - dim centraliser),
  - the commutant of the triple (the symmetries left once the embedding is fixed).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

NMAX = 6


def partitions(n, top=None):
    top = n if top is None else top
    if n == 0:
        yield ()
        return
    for k in range(min(n, top), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def transpose_partition(lam):
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0])) if lam else ()


def triple(lam):
    n = sum(lam)
    e = [[F(0)] * n for _ in range(n)]
    f = [[F(0)] * n for _ in range(n)]
    h = [[F(0)] * n for _ in range(n)]
    off = 0
    for d in lam:
        for i in range(d):
            h[off + i][off + i] = F(d - 1 - 2 * i)
            if i + 1 < d:
                e[off + i][off + i + 1] = F(1)
                f[off + i + 1][off + i] = F((i + 1) * (d - 1 - i))
        off += d
    return e, h, f


def br(A, B):
    AB, BA = GA.mat_mul(A, B), GA.mat_mul(B, A)
    return [[AB[i][j] - BA[i][j] for j in range(len(A))] for i in range(len(A))]


def scal(c, A):
    return [[c * x for x in row] for row in A]


def nullity_of_ad(mats, n):
    """dim {X in gl_n : [X, M] = 0 for all M in mats}."""
    rows = []
    for M in mats:
        for p in range(n):
            for q in range(n):
                row = [F(0)] * (n * n)
                # [X, M]_{pq} = sum_k X_{pk} M_{kq} - M_{pk} X_{kq}
                for k in range(n):
                    row[p * n + k] += M[k][q]
                    row[k * n + q] -= M[p][k]
                rows.append(row)
    return n * n - GA.rank_of_vectors(rows)


def check_principal_is_the_unique_full_dimensional_orbit():
    """dim orbit(e_lambda) = n^2 - sum (lambda^T_i)^2, which equals n^2 - n (the dimension of the
    nilpotent cone) exactly for lambda = (n); the zero orbit (1^n) is the only conjugation-fixed one."""
    premise("scrambling.imported-kostant-madore-partition-data")
    premise("scrambling.boundary-mode-space-matrix")
    for n in range(2, NMAX + 1):
        top = []
        fixed = []
        for lam in partitions(n):
            e, h, f = triple(lam)
            assert br(h, e) == scal(F(2), e) and br(h, f) == scal(F(-2), f) and br(e, f) == h
            cent = nullity_of_ad([e], n)
            assert cent == sum(c * c for c in transpose_partition(lam))
            orbit = n * n - cent
            assert orbit <= n * n - n
            if orbit == n * n - n:
                top.append(lam)
            if orbit == 0:
                fixed.append(lam)
        assert top == [(n,)]
        assert fixed == [tuple([1] * n)]
    return True


def check_indistinguishable_blocks_are_the_rectangular_types():
    """The commutant of the sl2 image has dimension sum over sizes d of m_d^2 (m_d = multiplicity).
    Its blocks of one size are permuted by GL(m_d); blocks of different sizes are told apart by
    their size. So no block is distinguished exactly for rectangular lambda = (k^m), k | n: for n
    prime only (n) and the zero map (1^n); for composite n also every (k^m), 1 < k < n."""
    premise("scrambling.imported-kostant-madore-partition-data")
    premise("scrambling.boundary-mode-space-matrix")
    for n in range(2, NMAX + 1):
        rect = []
        for lam in partitions(n):
            e, h, f = triple(lam)
            comm = nullity_of_ad([e, f], n)
            mult = {}
            for d in lam:
                mult[d] = mult.get(d, 0) + 1
            assert comm == sum(m * m for m in mult.values())
            if len(mult) == 1:
                rect.append(lam)
        divisors = [k for k in range(n, 0, -1) if n % k == 0]
        assert rect == [tuple([k] * (n // k)) for k in divisors]
        assert (len(rect) == 2) == all(n % k for k in range(2, n))      # n prime
    # n = 4: (2,2) has a GL(2) commutant moving its two blocks into each other
    e, h, f = triple((2, 2))
    assert nullity_of_ad([e, f], 4) == 4
    return True
