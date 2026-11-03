"""standard-model.raw-representation-content-state-space: exact checks.

(1) Cauchy decomposition by degree d (the abelian charge, the pair number): Lambda^d(C^2 (x) C^3) is the sum over
    partitions lam of d in the 2 x 3 box of S_lam(C^2) (x) S_lam'(C^3). Dimensions by the hook-content formula;
    the SU(2) irrep is labelled by its dimension, the SU(3) irrep by the conjugate partition reduced modulo full
    columns (1 = (), 3 = (1), 3bar = (1,1), 6 = (2), 6bar = (2,2), 8 = (2,1)). The resulting table must be
    (1,1) | (2,3) | (3,3bar) + (1,6) | (4,1) + (2,8) | (3,3) + (1,6bar) | (2,3bar) | (1,1), with graded dimensions
    1, 6, 15, 20, 15, 6, 1 (total 64).
(2) The decomposition is confirmed independently by characters: e_d of the six products a_i b_j equals
    sum_lam s_lam(a) s_lam'(b) (Schur polynomials by Jacobi-Trudi from complete symmetric functions) for every
    d = 0..6 at three rational points.
(3) Single-spinor sector Lambda^d C^3: S_(1^d) with d = 0..3 gives 1, 3, 3bar, 1.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement

import GA
from tp_premise import premise

POINTS = [((F(2), F(3)), (F(1), F(5), F(7))), ((F(1, 2), F(-3)), (F(2), F(-1), F(1, 3))),
          ((F(-2, 5), F(4)), (F(3), F(1, 7), F(-6)))]
SU3_NAME = {(): "1", (1,): "3", (1, 1): "3b", (2,): "6", (2, 2): "6b", (2, 1): "8"}


def _conj(lam):
    lam = [x for x in lam if x > 0]
    return [sum(1 for x in lam if x > j) for j in range(lam[0])] if lam else []


def _hook_dim(lam, n):
    lam = [x for x in lam if x > 0]
    if not lam:
        return 1
    cj = _conj(lam)
    num, den = 1, 1
    for i, row in enumerate(lam):
        for j in range(row):
            num *= n + j - i
            den *= (row - j) + (cj[j] - i) - 1
    return num // den


def _su3_label(lam):
    """Reduce a partition with at most 3 rows modulo full columns (det = 1 on SU(3))."""
    lam = [x for x in lam if x > 0] + [0] * 3
    lam = lam[:3]
    red = tuple(x - lam[2] for x in lam[:2] if x - lam[2] > 0)
    return SU3_NAME[red]


def _box(d):
    return [(a, d - a) for a in range(4) if 0 <= d - a <= a]


def _esym(vals, k):
    tot = F(0)
    for c in combinations(range(len(vals)), k):
        p = F(1)
        for i in c:
            p *= vals[i]
        tot += p
    return tot


def _hsym(vals, k):
    if k < 0:
        return F(0)
    tot = F(0)
    for c in combinations_with_replacement(range(len(vals)), k):
        p = F(1)
        for i in c:
            p *= vals[i]
        tot += p
    return tot


def _schur(lam, vals):
    """Jacobi-Trudi: det(h_{lam_i - i + j})."""
    lam = [x for x in lam if x > 0]
    n = len(lam)
    if n == 0:
        return F(1)
    M = [[_hsym(vals, lam[i] - i + j) for j in range(n)] for i in range(n)]
    return _det(M)


def _det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    return sum(((-1) ** j * M[0][j] * _det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(n)), F(0))


def check_cauchy_table_by_degree():
    premise("standard-model.imported-cauchy-decomposition-exterior-power")
    expected = [[(1, "1")], [(2, "3")], [(3, "3b"), (1, "6")], [(4, "1"), (2, "8")], [(3, "3"), (1, "6b")],
                [(2, "3b")], [(1, "1")]]
    ok = True
    dims = []
    for d in range(7):
        got = []
        tot = 0
        for lam in _box(d):
            d2 = _hook_dim(list(lam), 2)
            lc = _conj(list(lam))
            d3 = _hook_dim(lc, 3)
            if d2 == 0 or d3 == 0:
                continue
            got.append((d2, _su3_label(lc)))
            tot += d2 * d3
        dims.append(tot)
        ok = ok and sorted(got) == sorted(expected[d])
    binom = [1, 6, 15, 20, 15, 6, 1]
    ok = ok and dims == binom and sum(dims) == 64
    GA.check("Lambda^d(C^2 x C^3) by degree: (1,1), (2,3), (3,3b)+(1,6), (4,1)+(2,8), (3,3)+(1,6b), (2,3b), (1,1)", ok)
    return ok


def check_cauchy_characters():
    premise("standard-model.imported-cauchy-decomposition-exterior-power")
    ok = True
    for a, b in POINTS:
        prods = [x * y for x in a for y in b]
        for d in range(7):
            rhs = sum((_schur(list(lam), list(a)) * _schur(_conj(list(lam)), list(b)) for lam in _box(d)), F(0))
            ok = ok and _esym(prods, d) == rhs
    # the dimension specialisation a = (1, 1), b = (1, 1, 1) gives the binomials
    ones2, ones3 = [F(1)] * 2, [F(1)] * 3
    ok = ok and [sum((_schur(list(l), ones2) * _schur(_conj(list(l)), ones3) for l in _box(d)), F(0))
                 for d in range(7)] == [1, 6, 15, 20, 15, 6, 1]
    GA.check("e_d(a_i b_j) = sum_lam s_lam(a) s_lam'(b) for d = 0..6 at three rational points", ok)
    return ok


def check_single_spinor_sector():
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    labels = [_su3_label([1] * d) for d in range(4)]
    dims = [_hook_dim([1] * d, 3) for d in range(4)]
    ok = labels == ["1", "3", "3b", "1"] and dims == [1, 3, 3, 1]
    GA.check("Lambda^d C^3 = 1, 3, 3bar, 1 for d = 0..3", ok)
    return ok
