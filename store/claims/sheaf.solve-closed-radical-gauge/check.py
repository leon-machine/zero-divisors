"""sheaf.solve-closed-radical-gauge: exact checks.

Wall fibres: for every signature (p, q) with p >= 1, p + q <= 5, a cometric of corank one in a general
frame, G = P^T diag(0, +1 x (p-1), -1 x q) P with radical k = P^-1 e_0, plus the Schwarzschild wall Gram
[[m^2, -m, 0, 0], [-m, 1, 0, 0], 0, 0; diag(-1, -1)] with k = rho + m dt at m = 1, 2. Covectors and
vectors are coordinate lists, alpha(v) = sum alpha_i v_i, G(alpha, beta) = alpha^T G beta.
(a) The musical map alpha -> G(alpha, .) has kernel exactly R k (kernel computed) and rank n - 1, and
    k^T G = 0, so its image is exactly ker k: G vt = v is solvable for every v in a basis of ker k and
    for samples, and not solvable for v = u (k(u) = 1).
(b) Solutions are unique modulo R k: the solution set is vt0 + ker G, and G(alpha, vt) does not depend on
    the gauge.
(c) N(t) = G(vt + t k, vt + t k) + 2 (vt + t k)(u) is affine with slope 2 k(u) = 2 (checked at several t),
    so exactly one gauge representative t* = -N(0)/2 meets N = 0; checked for two transversals u.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (self-contained lemma: no premises)

MAXN = 5
T_SAMPLES = [F(1), F(-3), F(1, 2), F(7, 3)]
V_EXTRA = [[F(1), F(2), F(-1), F(3), F(1, 2)], [F(0), F(5), F(1, 3), F(-2), F(4)]]


def _mm(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def _frame(n):
    U = [[F(1) if i == j else (F((i + 2 * j) % 3 - 1) if j > i else F(0)) for j in range(n)] for i in range(n)]
    L = [[F(1) if i == j else (F((2 * i + j) % 3 - 1) if j < i else F(0)) for j in range(n)] for i in range(n)]
    return _mm(U, L)


def _dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def _transversals(k):
    n = len(k)
    out = []
    for w in ([F(i + 2) for i in range(n)], [F((-1) ** i * (i + 1)) for i in range(n)]):
        if _dot(k, w) == 0:
            w[0] += 1
        out.append([x / _dot(k, w) for x in w])
    return out


def wall_fibres():
    out = []
    for n in range(2, MAXN + 1):
        for p in range(1, n + 1):
            q = n - p
            D = [[F(0)] * n for _ in range(n)]
            for i in range(1, n):
                D[i][i] = F(1) if i < p else F(-1)
            P = _frame(n)
            G = _mm([list(r) for r in zip(*P)], _mm(D, P))
            k = GA.field_solve(P, [F(1)] + [F(0)] * (n - 1))
            out.append((G, k))
    for m in (F(1), F(2)):
        G = [[m * m, -m, F(0), F(0)], [-m, F(1), F(0), F(0)], [F(0), F(0), F(-1), F(0)], [F(0), F(0), F(0), F(-1)]]
        out.append((G, [F(1), m, F(0), F(0)]))
    return out


def solve(M, rhs):
    """One exact solution of M x = rhs, or None."""
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


def _gq(G, a, b):
    return sum((a[i] * G[i][j] * b[j] for i in range(len(a)) for j in range(len(b))), F(0))


def _ker_k_vectors(k):
    """A basis of ker k (computed) plus the projections of two sample vectors along a transversal."""
    n = len(k)
    u0 = _transversals(k)[0]
    extra = [[w[i] - _dot(k, w[:n]) * u0[i] for i in range(n)] for w in V_EXTRA]
    return GA.field_kernel([k]) + extra


def check_musical_image_is_ker_k():
    ok = True
    cases = 0
    for G, k in wall_fibres():
        n = len(k)
        kerG = GA.field_kernel(G)
        ok = ok and len(kerG) == 1 and GA.rank_of_vectors([kerG[0], k]) == 1
        ok = ok and GA.rank_of_vectors(G) == n - 1
        ok = ok and all(_dot(k, [G[i][j] for i in range(n)]) == 0 for j in range(n))   # image in ker k
        for v in _ker_k_vectors(k):
            ok = ok and _dot(k, v) == 0 and solve(G, v) is not None
            cases += 1
        for u in _transversals(k):
            ok = ok and solve(G, u) is None                  # k(u) = 1: not in the image
    _tp_rv = (ok and cases == 78); assert _tp_rv is not False, "check_musical_image_is_ker_k"; return _tp_rv


def probe_covectors(n):
    """Three sample covectors a on which G(a, vt) is compared across gauges."""
    return [[F((i * j) % 5 - 2) for i in range(n)] for j in range(1, 4)]


def check_solution_unique_modulo_k():
    ok = True
    differs = False
    for G, k in wall_fibres():
        n = len(k)
        probes = probe_covectors(n)
        for v in _ker_k_vectors(k):
            vt = solve(G, v)
            for t in T_SAMPLES:
                alt = [vt[i] + t * k[i] for i in range(n)]
                ok = ok and all(sum((G[i][j] * alt[j] for j in range(n)), F(0)) == v[i] for i in range(n))
                ok = ok and all(_gq(G, a, alt) == _gq(G, a, vt) == _dot(a, v) for a in probes)
            # every solution differs from vt by a multiple of k: the difference lies in ker G = R k. A second
            # solution from elimination with the columns reversed (a different free variable; the old row
            # reversal returned vt itself, so the difference was always zero)
            other = solve([list(reversed(r)) for r in G], v)[::-1]
            diff = [other[i] - vt[i] for i in range(n)]
            ok = ok and GA.rank_of_vectors([diff, k]) == 1
            differs = differs or any(diff)
    # the comparison is not vacuous: the two solutions differ (for 74 of the 78 v)
    ok = ok and differs
    _tp_rv = (ok); assert _tp_rv is not False, "check_solution_unique_modulo_k"; return _tp_rv


def check_normalisation_one_gauge():
    ok = True
    for G, k in wall_fibres():
        n = len(k)
        for u in _transversals(k):
            for v in _ker_k_vectors(k):
                vt = solve(G, v)

                def N(t):
                    x = [vt[i] + t * k[i] for i in range(n)]
                    return _gq(G, x, x) + 2 * _dot(x, u)
                N0 = N(F(0))
                ok = ok and all(N(t) - N0 == 2 * t for t in T_SAMPLES)
                tstar = -N0 / 2
                ok = ok and N(tstar) == 0
                ok = ok and all(N(tstar + d) != 0 for d in T_SAMPLES)
    _tp_rv = (ok); assert _tp_rv is not False, "check_normalisation_one_gauge"; return _tp_rv
