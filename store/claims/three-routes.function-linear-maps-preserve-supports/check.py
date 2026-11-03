"""three-routes.function-linear-maps-preserve-supports: exact checks of the finite (algebraic) core.

The lemma's analytic part (bump functions on Sigma = R x S^2 with support near supp(s)) has no finite
content; what is checked is the algebraic step it rests on, Ds = D(fs) = f Ds for f = 1 on supp(s), on
finite point sets, where the indicator of a set is the bump function. Model: N points (N = 2, 3, 4), a free
module of rank r (r = 1, 2) over the functions on the points; sections are vectors in Q^(N r), a function f
acts as diag(f(x)) (x) 1_r.
(1) The C(U)-linear maps (those commuting with every multiplication operator, computed as the kernel of
    D -> [D, M_f] for the point indicators, which span all functions) form a space of dimension N r^2: the
    block-diagonal maps, i.e. bundle maps.
(2) For every basis map D of that space, a general combination, and every section supported on each subset S
    of the points: Ds = f Ds with f the indicator of S, hence supp(Ds) is contained in supp(s).
(3) Control: a map with a cross component (a hop between two points) is not function-linear and moves support.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise  # noqa: F401  (self-contained lemma: no premises)

CASES = [(2, 1), (3, 1), (4, 1), (2, 2), (3, 2)]


def _mult(N, r, f):
    """The multiplication operator of the function f (a list of N values)."""
    d = N * r
    return [[f[i // r] if i == j else F(0) for j in range(d)] for i in range(d)]


def _mv(M, v):
    return [sum((a * b for a, b in zip(row, v)), F(0)) for row in M]


def _mm(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def _support(N, r, s):
    return frozenset(x for x in range(N) if any(s[x * r + a] != 0 for a in range(r)))


def function_linear_maps(N, r):
    d = N * r
    rows = []
    for x in range(N):
        chi = _mult(N, r, [F(1) if y == x else F(0) for y in range(N)])
        # [D, chi]_(ij) = sum_t D_it chi_tj - chi_it D_tj, linear in the d^2 unknowns D_ab (index a d + b)
        for i in range(d):
            for j in range(d):
                row = [F(0)] * (d * d)
                row[i * d + j] += chi[j][j] - chi[i][i]
                rows.append(row)
    basis = GA.field_kernel(rows)
    return [[[v[i * d + j] for j in range(d)] for i in range(d)] for v in basis]


def check_function_linear_maps_are_bundle_maps():
    ok = True
    for N, r in CASES:
        Ds = function_linear_maps(N, r)
        ok = ok and len(Ds) == N * r * r
        for D in Ds:
            ok = ok and all(D[i][j] == 0 for i in range(N * r) for j in range(N * r) if i // r != j // r)
            f = [F(t * t - 2) for t in range(N)]
            ok = ok and _mm(D, _mult(N, r, f)) == _mm(_mult(N, r, f), D)
    _tp_rv = (ok); assert _tp_rv is not False, "check_function_linear_maps_are_bundle_maps"; return _tp_rv


def check_supports_are_preserved():
    ok = True
    tested = 0
    for N, r in CASES:
        Ds = function_linear_maps(N, r)
        general = [[sum((F(c + 1) * D[i][j] for c, D in enumerate(Ds)), F(0)) for j in range(N * r)]
                   for i in range(N * r)]
        for D in Ds + [general]:
            for size in range(N + 1):
                for S in combinations(range(N), size):
                    s = [F(x + a + 1) if x in S else F(0) for x in range(N) for a in range(r)]
                    f = _mult(N, r, [F(1) if x in S else F(0) for x in range(N)])
                    ok = ok and _mv(f, s) == s and _mv(D, s) == _mv(f, _mv(D, s))
                    ok = ok and _support(N, r, _mv(D, s)) <= _support(N, r, s) == frozenset(S)
                    tested += 1
    _tp_rv = (ok and tested == 264); assert _tp_rv is not False, "check_supports_are_preserved"; return _tp_rv


def check_hopping_is_not_function_linear():
    ok = True
    for N, r in CASES:
        d = N * r
        for i in range(d):
            for j in range(d):
                E = [[F(1) if (a, b) == (i, j) else F(0) for b in range(d)] for a in range(d)]
                linear = all(_mm(E, _mult(N, r, [F(1) if y == x else F(0) for y in range(N)]))
                             == _mm(_mult(N, r, [F(1) if y == x else F(0) for y in range(N)]), E) for x in range(N))
                ok = ok and linear == (i // r == j // r)
                s = [F(1) if t == j else F(0) for t in range(d)]
                moved = not (_support(N, r, _mv(E, s)) <= _support(N, r, s))
                ok = ok and moved == (i // r != j // r)
    _tp_rv = (ok); assert _tp_rv is not False, "check_hopping_is_not_function_linear"; return _tp_rv
