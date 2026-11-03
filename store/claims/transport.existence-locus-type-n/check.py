"""transport.existence-locus-type-n: exact checks.

Cl(p,q) in GA.py, Q(v) = v^2 for vectors. For every (p,q) with 1 <= n = p + q <= 5:
(1) Definite (pq = 0): Q(v) = +-(sum of squares) as a quadratic form (the Gram matrix is +-identity, so
    Q is anisotropic), and no nonzero vector of a rational net with entries in {-2..2} is null.
(2) Mixed (pq != 0): e_1 + e_n (first plus and last minus generator) is null; further null vectors are
    built rationally ((1 - t^2) e_1 + 2t e_2 + (1 + t^2) e_n when p >= 2, and 5 e_1 + 3 e_{p+1} + 4 e_{p+2}
    when q >= 2), 28 in all; at each the gradient 2 B v of Q is nonzero (rank 1), so the null set is a
    cone of dimension n - 1 there.
(3) Every sampled null v is a two-sided zero divisor (v v = 0, v != 0); left multiplication by v has rank
    exactly 2^(n-1) < 2^n, so v has no inverse in Cl(p,q); and in the extensions Cl(p+1,q) and
    Cl(p,q+1) the equations v x = 1 and x v = 1 have no solution (inconsistent linear systems).
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

GRID = [(p, n - p) for n in range(1, 6) for p in range(n + 1)]


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), GA.gen(i)) for i in range(len(c))])


def nulls(p, q):
    """Rational null vectors of R^{p,q}: (1 - t^2) e_i + 2t e_j + (1 + t^2) e_k with Q(e_i) = Q(e_j) = 1,
    Q(e_k) = -1, and e_0 + e_n-1, plus a mixed one when p, q >= 2."""
    n = p + q
    out = [vec([1] + [0] * (n - 2) + [1])]
    if p >= 2:
        for t in (F(1, 2), F(2, 3)):
            c = [0] * n
            c[0], c[1], c[n - 1] = 1 - t * t, 2 * t, 1 + t * t
            out.append(vec(c))
    if q >= 2:
        c = [0] * n
        c[0], c[p], c[p + 1] = 5, 3, 4
        out.append(vec(c))
    return out


def left_rank(v, S):
    n = len(S)
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[GA.mul(v, {b: F(1)}, S).get(c, F(0)) for c in bl] for b in bl])


def solvable(v, S, left):
    """Is v x = 1 (left) or x v = 1 consistent in Cl(S)? (rank of system vs augmented)."""
    n = len(S)
    bl = GA.all_blades(n)
    cols = []
    for b in bl:
        y = GA.mul(v, {b: F(1)}, S) if left else GA.mul({b: F(1)}, v, S)
        cols.append([y.get(c, F(0)) for c in bl])
    A = [list(r) for r in zip(*cols)]
    rhs = [F(1) if c == () else F(0) for c in bl]
    return GA.rank_of_vectors(A) == GA.rank_of_vectors([A[i] + [rhs[i]] for i in range(len(A))])


def check_definite_forms_have_no_null_vectors():
    ok = True
    for p, q in GRID:
        if p and q:
            continue
        S = GA.sig(p, q)
        n = p + q
        gram = [[GA.dot(GA.gen(i), GA.gen(j), S) for j in range(n)] for i in range(n)]
        sgn = 1 if q == 0 else -1
        ok = ok and gram == [[F(sgn) if i == j else F(0) for j in range(n)] for i in range(n)]
        for c in product(range(-2, 3), repeat=min(n, 3)):
            if any(c):
                v = vec(list(c) + [0] * (n - len(c)))
                ok = ok and GA.mul(v, v, S)[()] == sgn * sum(x * x for x in c) != 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_definite_forms_have_no_null_vectors"; return _tp_rv


def check_mixed_forms_have_a_null_cone_of_dimension_n_minus_one():
    ok = True
    count = 0
    for p, q in GRID:
        if not (p and q):
            continue
        S = GA.sig(p, q)
        n = p + q
        for v in nulls(p, q):
            ok = ok and GA.is_zero(GA.mul(v, v, S)) and not GA.is_zero(v)
            grad = [2 * GA.dot(v, GA.gen(i), S) for i in range(n)]
            ok = ok and GA.rank_of_vectors([grad]) == 1
            count += 1
    ok = ok and count == 28
    _tp_rv = (ok); assert _tp_rv is not False, "check_mixed_forms_have_a_null_cone_of_dimension_n_minus_one"; return _tp_rv


# Sample settings: mixed signatures up to n = 4, each also extended by one generator of square +1 or -1;
# control algebra Cl(1,1), whose generators are invertible vectors.
MAX_N_NULL = 4
EXTENSIONS = ((), (1,), (-1,))
CONTROL_SQ = GA.sig(1, 1)


def check_null_vectors_are_non_invertible_zero_divisors():
    premise("transport.noinverse")
    ok = True
    for p, q in GRID:
        if not (p and q) or p + q > MAX_N_NULL:
            continue
        S = GA.sig(p, q)
        n = p + q
        for v in nulls(p, q):
            ok = ok and GA.is_zero(GA.mul(v, v, S))
            ok = ok and left_rank(v, S) == 2 ** (n - 1)
            for ext in EXTENSIONS:
                S2 = S + ext
                ok = ok and not solvable(v, S2, True) and not solvable(v, S2, False)
    # control: invertible vectors (the generators of Cl(1,1), squares +1 and -1) are solvable on both sides
    ok = ok and all(solvable(GA.gen(i), CONTROL_SQ, side) for i in range(len(CONTROL_SQ)) for side in (True, False))
    _tp_rv = (ok); assert _tp_rv is not False, "check_null_vectors_are_non_invertible_zero_divisors"; return _tp_rv
