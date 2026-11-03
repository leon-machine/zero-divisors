"""three-routes.radical-gauge-closes-solve: exact checks.

Boundary data of exact Schwarzschild (the imported boundary Gram G(0) on the frame (rho, dt_PG, mu1, mu2),
k = rho + m dt_PG) at m = sqrt(2M) = 1, 2, 3, 1/2, 5/3; transversals u with k(u) = 1 (two per m).
Covectors and vectors are coordinate lists, alpha(v) = sum alpha_i v_i, G(alpha, beta) = alpha^T G beta.
(a) The musical map alpha -> G(alpha, .) has kernel exactly R k (computed kernel) and rank 3 = dim ker k,
    with k^T G = 0, so its image is exactly ker k: G vt = v solves for v in a basis of ker k and samples,
    and not for v = u.
(b) The solution is unique modulo R k: vt + t k solves for every t, the solution set is vt + ker G, and
    G(alpha, vt) does not depend on the gauge.
(c) N(t) = G(vt + t k, vt + t k) + 2 (vt + t k)(u) satisfies N(t) - N(0) = 2 t (slope 2 k(u) = 2), so
    exactly one gauge t* = -N(0)/2 meets the normalisation, and no other sampled gauge does.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MASSES = [F(1), F(2), F(3), F(1, 2), F(5, 3)]
T_SAMPLES = [F(1), F(-3), F(1, 2), F(7, 3)]
V_EXTRA = [[F(1), F(2), F(-1), F(3)], [F(0), F(5), F(1, 3), F(-2)]]
# probe covectors for the gauge independence of G(alpha, vt)
PROBES = [[F(1), F(2), F(-1), F(3)], [F(0), F(1, 2), F(4), F(-2)], [F(2), F(0), F(0), F(1)]]


def _dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def _gq(G, a, b):
    return sum((a[i] * G[i][j] * b[j] for i in range(len(a)) for j in range(len(b))), F(0))


def boundary(m):
    G = [[m * m, -m, F(0), F(0)], [-m, F(1), F(0), F(0)], [F(0), F(0), F(-1), F(0)], [F(0), F(0), F(0), F(-1)]]
    k = [F(1), m, F(0), F(0)]
    us = [[F(1), F(0), F(0), F(0)], [1 - m, F(1), F(3), F(-1)]]
    return G, k, us


def solve(M, rhs):
    n, m = len(M), len(M[0])
    A = [list(M[i]) + [rhs[i]] for i in range(n)]
    r, piv_cols = 0, []
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv_cols.append(c)
        r += 1
    if any(A[i][m] != 0 for i in range(r, n)):
        return None
    x = [F(0)] * m
    for i, c in enumerate(piv_cols):
        x[c] = A[i][m]
    return x


def ker_k_vectors(k, u):
    return GA.field_kernel([k]) + [[w[i] - _dot(k, w) * u[i] for i in range(4)] for w in V_EXTRA]


def check_image_is_ker_k():
    premise("three-routes.imported-boundary-gram-ladder")
    ok = True
    cases = 0
    for m in MASSES:
        G, k, us = boundary(m)
        kerG = GA.field_kernel(G)
        ok = ok and len(kerG) == 1 and GA.rank_of_vectors([kerG[0], k]) == 1
        ok = ok and GA.rank_of_vectors(G) == 3
        ok = ok and all(_dot(k, [G[i][j] for i in range(4)]) == 0 for j in range(4))
        for u in us:
            ok = ok and _dot(k, u) == 1 and solve(G, u) is None
            for v in ker_k_vectors(k, u):
                ok = ok and _dot(k, v) == 0 and solve(G, v) is not None
                cases += 1
    _tp_rv = (ok and cases == 5 * 2 * 5); assert _tp_rv is not False, "check_image_is_ker_k"; return _tp_rv


def check_unique_modulo_radical():
    premise("three-routes.imported-boundary-gram-ladder")
    ok = True
    probes = PROBES
    for m in MASSES:
        G, k, us = boundary(m)
        for v in [v for u in us for v in ker_k_vectors(k, u)]:
            vt = solve(G, v)
            for t in T_SAMPLES:
                alt = [vt[i] + t * k[i] for i in range(4)]
                ok = ok and [_dot(G[i], alt) for i in range(4)] == v
                ok = ok and all(_gq(G, a, alt) == _gq(G, a, vt) == _dot(a, v) for a in probes)
            sols = GA.field_kernel(G)                     # the homogeneous solutions
            ok = ok and len(sols) == 1 and GA.rank_of_vectors(sols + [k]) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_unique_modulo_radical"; return _tp_rv


def check_normalisation_fixes_the_gauge():
    premise("three-routes.imported-boundary-gram-ladder")
    ok = True
    for m in MASSES:
        G, k, us = boundary(m)
        for u in us:
            for v in ker_k_vectors(k, u):
                vt = solve(G, v)

                def N(t):
                    x = [vt[i] + t * k[i] for i in range(4)]
                    return _gq(G, x, x) + 2 * _dot(x, u)
                N0 = N(F(0))
                ok = ok and all(N(t) - N0 == 2 * t for t in T_SAMPLES)
                tstar = -N0 / 2
                ok = ok and N(tstar) == 0 and all(N(tstar + d) != 0 for d in T_SAMPLES)
    _tp_rv = (ok); assert _tp_rv is not False, "check_normalisation_fixes_the_gauge"; return _tp_rv
