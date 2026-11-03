"""sheaf.conservation-degeneracy-absolute-form: exact checks of the signature-counting argument.

Exterior models on a transversal: the cometric G is diag(lambda, G1) with lambda > 0 on the physical side,
lambda < 0 on the far side (tameness: the dying eigenvalue changes sign once) and G1 of signature (p-1, q);
the completion is standard, h = G perp K, with the same K on both exteriors.
(1) For every (p, q) with p >= 1, p + q <= 5, and every K of signature (a, b), a + b <= 3: the exterior
    totals (p+a, q+b) and (p-1+a, q+1+b) differ, computed by exact congruence diagonalisation of the
    exterior Gram matrices, and det h has opposite signs (-1)^(q+b) and (-1)^(q+b+1) on the two exteriors.
(2) Hence every continuous family of forms joining the exteriors is degenerate somewhere: for polynomial
    families h(t) = (1-t) A + t B + t(1-t) C (A, B the exteriors, several symmetric C, including dense
    integer ones) det h(t) is a polynomial with det h(0) det h(1) < 0, so it has a root in (0, 1); bisection
    with exact signs locates it in an interval of width 1/64, and h is checked degenerate at the exact root
    when it is rational (C = 0: the root t = 1/2).
(3) The constancy of sig(K) is needed: if K switches from (1, 1) to (2, 0) the totals agree, and the
    rational rotation path h(t) = R(t) D R(t)^T, R(t) the Cayley rotation (cos, sin) = ((1-t^2)/(1+t^2),
    2t/(1+t^2)) in the plane of k and K's negative direction, has det h(t) = det D for every t (a rational-
    function identity) and joins diag(+1, G1, (1, -1)) to diag(-1, G1, (1, 1)).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

C_SEEDS = [None, [[0, 1, 2, 0, 1], [1, 3, 0, 1, 0], [2, 0, -1, 1, 2], [0, 1, 1, 2, 1], [1, 0, 2, 1, -2]],
           [[5, -3, 1, 2, 0], [-3, 2, 4, 0, 1], [1, 4, -6, 3, 2], [2, 0, 3, 1, -1], [0, 1, 2, -1, 4]]]
PATH_CASES = [(1, 3, (1, 1)), (2, 1, (0, 2)), (2, 2, (1, 0))]


def diag(vals):
    n = len(vals)
    return [[F(vals[i]) if i == j else F(0) for j in range(n)] for i in range(n)]


def exterior(p, q, a, b, lam):
    return diag([lam] + [1] * (p - 1) + [-1] * q + [1] * a + [-1] * b)


def det(M):
    n = len(M)
    A = [list(r) for r in M]
    d = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return d


def check_exterior_totals_differ():
    premise("sheaf.tameness")
    count = 0
    for n in range(1, 6):
        for p in range(1, n + 1):
            q = n - p
            for k in range(4):
                for a in range(k + 1):
                    b = k - a
                    phys = GA.congruence_signature(exterior(p, q, a, b, 1))
                    far = GA.congruence_signature(exterior(p, q, a, b, -1))
                    assert phys == (p + a, q + b, 0) and far == (p - 1 + a, q + 1 + b, 0)
                    assert phys != far
                    dp, df = det(exterior(p, q, a, b, 1)), det(exterior(p, q, a, b, -1))
                    assert dp == (-1) ** (q + b) and df == (-1) ** (q + b + 1)
                    count += 1
    assert count == 150


def check_every_joining_path_degenerates():
    premise("sheaf.tameness")
    for (p, q, (a, b)) in PATH_CASES:
        A, B = exterior(p, q, a, b, 1), exterior(p, q, a, b, -1)
        d = len(A)
        for seed in C_SEEDS:
            Cm = [[F(0)] * d for _ in range(d)] if seed is None else \
                [[F(seed[i % 5][j % 5] + seed[j % 5][i % 5]) for j in range(d)] for i in range(d)]
            h = lambda t: [[(1 - t) * A[i][j] + t * B[i][j] + t * (1 - t) * Cm[i][j] for j in range(d)]
                           for i in range(d)]
            lo, hi = F(0), F(1)
            dlo, dhi = det(h(lo)), det(h(hi))
            assert dlo * dhi < 0
            for _ in range(6):
                mid = (lo + hi) / 2
                dm = det(h(mid))
                if dm == 0:
                    lo = hi = mid
                    break
                if (dm > 0) == (dlo > 0):
                    lo, dlo = mid, dm
                else:
                    hi = mid
            assert hi - lo <= F(1, 64)
            if seed is None:
                assert lo == hi == F(1, 2) and GA.congruence_signature(h(lo))[2] == 1


def check_switching_sig_k_avoids_degeneracy():
    p, q = 2, 1
    D = diag([1] + [1] * (p - 1) + [-1] * q + [1, -1])        # physical exterior, K = (1, 1)
    d = len(D)
    i0, i1 = 0, d - 1                                        # k and K's negative direction
    t = GA.RF.var()
    one = GA.RF1
    cs, sn = (one - t * t) / (one + t * t), (GA.RF.const(2) * t) / (one + t * t)
    Rm = [[GA.RF.const(int(i == j)) for j in range(d)] for i in range(d)]
    Rm[i0][i0], Rm[i1][i1], Rm[i0][i1], Rm[i1][i0] = cs, cs, GA.RF.const(0) - sn, sn
    Dr = [[GA.RF.const(x) for x in row] for row in D]
    hRD = [[sum((Rm[i][k] * Dr[k][l] * Rm[j][l] for k in range(d) for l in range(d)), GA.RF0)
            for j in range(d)] for i in range(d)]
    assert GA.rf_mat_det(hRD).eqrf(GA.RF.const(det(D)))
    end = [[x.eval(1) for x in row] for row in hRD]
    assert end == diag([-1] + [1] * (p - 1) + [-1] * q + [1, 1])
    assert GA.congruence_signature(D) == GA.congruence_signature(end) == (p + 1, q + 1, 0)
    for tv in (F(1, 3), F(1, 2), F(5, 7)):
        assert det([[x.eval(tv) for x in row] for row in hRD]) == det(D) != 0
