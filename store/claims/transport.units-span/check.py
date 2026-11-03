"""transport.units-span: exact checks.

Finite-dimensional unital algebras given by a basis and left-multiplication matrices: real Clifford
algebras (GA.py, n <= 4) and two non-Clifford algebras, the upper-triangular 3 x 3 matrices (dimension 6)
and the dual numbers Q[x]/(x^2), plus Mat_2 as 2 x 2 matrices.
(1) For each sample a (zero, nilpotents, null vectors, zero divisors, invertible elements), the reals
    lambda in {0, ..., dim A + 1} with L_a - lambda singular are found by exact rank; there are at most
    dim A of them (the degree bound), so some nonzero lambda in that range leaves a - lambda invertible;
    a - lambda is then two-sided invertible (x solved from (a - lambda) x = 1 also satisfies
    x (a - lambda) = 1) and a = (a - lambda) + lambda 1 is a sum of two units.
(2) The singular sets on hand samples are the eigenvalues of L_a: {0} for a null vector or a
    nilpotent, {0, 2} for 1 + e with e^2 = 1, {3} for 3, {0, 1} for a non-central idempotent of
    the triangular matrices, {2} for 2 - 3x in the dual numbers.
"""
from fractions import Fraction as F

import GA


def cl_algebra(p, q):
    S = GA.sig(p, q)
    bl = GA.all_blades(p + q)

    def to_vec(x):
        return [x.get(b, F(0)) for b in bl]

    def mul(x, y):
        X = {b: c for b, c in zip(bl, x) if c}
        Y = {b: c for b, c in zip(bl, y) if c}
        return to_vec(GA.mul(X, Y, S))
    return len(bl), mul, to_vec(GA.sc(1)), to_vec


def mat_algebra(n, positions):
    """Matrices supported on the given (i, j) positions (a subalgebra containing the identity)."""
    def to_mat(x):
        M = [[F(0)] * n for _ in range(n)]
        for (i, j), c in zip(positions, x):
            M[i][j] = c
        return M

    def mul(x, y):
        P = GA.mat_mul(to_mat(x), to_mat(y))
        return [P[i][j] for (i, j) in positions]
    one = [F(1) if i == j else F(0) for (i, j) in positions]
    return len(positions), mul, one


def dual_numbers():
    def mul(x, y):
        return [x[0] * y[0], x[0] * y[1] + x[1] * y[0]]
    return 2, mul, [F(1), F(0)]


def left(a, dim, mul):
    E = [[F(1) if k == j else F(0) for k in range(dim)] for j in range(dim)]
    cols = [mul(a, e) for e in E]
    return [[cols[j][i] for j in range(dim)] for i in range(dim)]


def singular_lambdas(a, dim, mul, one):
    out = []
    for lam in range(dim + 2):
        b = [x - lam * y for x, y in zip(a, one)]
        if GA.field_rank(left(b, dim, mul)) < dim:
            out.append(lam)
    return out


def two_sided_inverse(b, dim, mul, one):
    Lb = left(b, dim, mul)
    if GA.field_rank(Lb) < dim:
        return None
    x = GA.field_solve(Lb, list(one))
    return x if mul(x, b) == list(one) and mul(b, x) == list(one) else None


TRI = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
FULL2 = [(0, 0), (0, 1), (1, 0), (1, 1)]


def samples():
    out = []
    for p, q in ((1, 1), (2, 0), (0, 2), (1, 2), (1, 3), (2, 2)):
        dim, mul, one, tv = cl_algebra(p, q)
        n = p + q
        els = [tv({}), tv(GA.add(GA.gen(0), GA.gen(n - 1))), tv(GA.add(GA.sc(1), GA.gen(0))),
               tv(GA.add(GA.sc(2), GA.mul(GA.gen(0), GA.gen(1), GA.sig(p, q)))), tv(GA.sc(3))]
        out.append(((p, q), dim, mul, one, els))
    dim, mul, one = mat_algebra(3, TRI)
    out.append(("tri", dim, mul, one, [[F(0), F(1), F(0), F(0), F(0), F(0)], [F(1), F(0), F(0), F(0), F(0), F(0)],
                                       [F(2), F(5), F(-1), F(2), F(0), F(7)]]))
    dim, mul, one = mat_algebra(2, FULL2)
    out.append(("mat2", dim, mul, one, [[F(0), F(1), F(0), F(0)], [F(1), F(2), F(2), F(4)]]))
    dim, mul, one = dual_numbers()
    out.append(("dual", dim, mul, one, [[F(0), F(1)], [F(5), F(-3)]]))
    return out


def check_every_element_is_a_sum_of_two_units():
    ok = True
    count = 0
    for name, dim, mul, one, els in samples():
        for a in els:
            bad = singular_lambdas(a, dim, mul, one)
            ok = ok and len(bad) <= dim
            lam = next(l for l in range(1, dim + 2) if l not in bad)
            b = [x - lam * y for x, y in zip(a, one)]
            x = two_sided_inverse(b, dim, mul, one)
            ok = ok and x is not None and two_sided_inverse([lam * y for y in one], dim, mul, one) is not None
            ok = ok and [u + lam * y for u, y in zip(b, one)] == list(a)
            count += 1
    ok = ok and count == 37
    _tp_rv = (ok); assert _tp_rv is not False, "check_every_element_is_a_sum_of_two_units"; return _tp_rv


def check_singular_sets_are_the_eigenvalues():
    ok = True
    dim, mul, one, tv = cl_algebra(1, 1)
    ok = ok and singular_lambdas(tv(GA.add(GA.gen(0), GA.gen(1))), dim, mul, one) == [0]
    ok = ok and singular_lambdas(tv(GA.add(GA.sc(1), GA.gen(0))), dim, mul, one) == [0, 2]
    ok = ok and singular_lambdas(tv(GA.sc(3)), dim, mul, one) == [3]
    dim, mul, one = mat_algebra(3, TRI)
    ok = ok and singular_lambdas([F(1), F(0), F(0), F(0), F(0), F(0)], dim, mul, one) == [0, 1]
    ok = ok and singular_lambdas([F(0), F(1), F(0), F(0), F(0), F(0)], dim, mul, one) == [0]
    dim, mul, one = dual_numbers()
    ok = ok and singular_lambdas([F(2), F(-3)], dim, mul, one) == [2]
    _tp_rv = (ok); assert _tp_rv is not False, "check_singular_sets_are_the_eigenvalues"; return _tp_rv
