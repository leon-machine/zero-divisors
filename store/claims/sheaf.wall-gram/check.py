"""sheaf.wall-gram: exact checks.

At a wall point of every signature (p, q) with p >= 1 and p + q <= 6 the cometric G is built in a
general (non-orthonormal) frame of covectors, G = P^T diag(0, +1 x (p-1), -1 x q) P, with radical
k = P^-1 e_0 (so G k = 0), and a transversal u with k(u) = 1. The ambient form h on
T = T*M + span(n0, ninf) is that of the collar data at beta = 1: h = G on covectors,
h(alpha, n0) = nu alpha(u), h(alpha, ninf) = mu alpha(u), h(n0, ninf) = -1, n0^2 = ninf^2 = 0.
For each signature and each (mu, nu) in a grid with both signs of mu nu:
(2) the Gram of (k, n0, ninf) read off h is [[0, nu, mu], [nu, 0, -1], [mu, -1, 0]], and its
    determinant (exact elimination) is -2 mu nu, also checked as a polynomial in (mu, nu) on a 4 x 4 grid;
(3) span(k, n0) is a hyperbolic plane, w = k + nu ninf - mu n0 is h-orthogonal to k and n0 with
    h(w, w) = 2 mu nu, and the block signature is (2, 1) for mu nu > 0 and (1, 2) for mu nu < 0;
(1), (4) V1 = {alpha : alpha(u) = 0} (computed as a kernel) is complementary to R k, h-orthogonal to
    the block, carries G|V1 of signature (p - 1, q) (the degeneration-sheaf quotient form), and the full
    h is nondegenerate of signature (p + 1, q + 1) if mu nu > 0 and (p, q + 2) if mu nu < 0.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MAXN = 6
MUNU = [(F(2), F(3)), (F(-1), F(5)), (F(1, 3), F(-2)), (F(-4), F(-1, 2))]
GRID = [F(1), F(-2), F(1, 3), F(5)]


def _mm(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def _tr(A):
    return [list(r) for r in zip(*A)]


def _frame(n):
    """Fixed invertible integer frame change P = U L (unit triangular factors)."""
    U = [[F(1) if i == j else (F((i + 2 * j) % 3 - 1) if j > i else F(0)) for j in range(n)] for i in range(n)]
    L = [[F(1) if i == j else (F((2 * i + j) % 3 - 1) if j < i else F(0)) for j in range(n)] for i in range(n)]
    return _mm(U, L)


def _inv(M):
    n = len(M)
    cols = [GA.field_solve(M, [F(1) if i == c else F(0) for i in range(n)]) for c in range(n)]
    return [[cols[c][r] for c in range(n)] for r in range(n)]


def wall_data(p, q):
    n = p + q
    D = [[F(0)] * n for _ in range(n)]
    for i in range(1, n):
        D[i][i] = F(1) if i < p else F(-1)
    P = _frame(n)
    G = _mm(_tr(P), _mm(D, P))
    k = [row[0] for row in _inv(P)]                       # P k = e_0
    w = [F(i + 2) for i in range(n)]
    kw = sum((a * b for a, b in zip(k, w)), F(0))
    if kw == 0:
        w[0] += 1
        kw = sum((a * b for a, b in zip(k, w)), F(0))
    u = [x / kw for x in w]                                # k(u) = 1
    return G, k, u


def ambient(G, u, mu, nu):
    n = len(G)
    h = [[F(0)] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            h[i][j] = G[i][j]
        h[i][n] = h[n][i] = nu * u[i]
        h[i][n + 1] = h[n + 1][i] = mu * u[i]
    h[n][n + 1] = h[n + 1][n] = F(-1)
    return h


def form(h, x, y):
    return sum((x[i] * h[i][j] * y[j] for i in range(len(x)) for j in range(len(y))), F(0))


def det(M):
    A = [list(r) for r in M]
    n = len(A)
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
            A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return d


def signatures():
    return [(p, q) for n in range(1, MAXN + 1) for p in range(1, n + 1) for q in [n - p]]


def block_vectors(n, k):
    kk = list(k) + [F(0), F(0)]
    n0 = [F(0)] * n + [F(1), F(0)]
    ni = [F(0)] * n + [F(0), F(1)]
    return kk, n0, ni


def check_block_gram_and_determinant():
    ok = True
    count = 0
    for (p, q) in signatures():
        G, k, u = wall_data(p, q)
        n = p + q
        ok = ok and all(sum((G[i][j] * k[j] for j in range(n)), F(0)) == 0 for i in range(n))
        kk, n0, ni = block_vectors(n, k)
        for mu, nu in MUNU:
            h = ambient(G, u, mu, nu)
            blk = [[form(h, a, b) for b in (kk, n0, ni)] for a in (kk, n0, ni)]
            ok = ok and blk == [[0, nu, mu], [nu, 0, -1], [mu, -1, 0]]
            ok = ok and det(blk) == -2 * mu * nu and det(blk) != 0
            count += 1
    # the determinant as a polynomial in (mu, nu): agreement on a 4 x 4 grid fixes a polynomial of
    # degree <= 3 in each variable, which bounds the 3 x 3 determinant
    for mu in GRID:
        for nu in GRID:
            B = [[F(0), nu, mu], [nu, F(0), F(-1)], [mu, F(-1), F(0)]]
            ok = ok and det(B) == -2 * mu * nu
    _tp_rv = (ok and count == 4 * 21); assert _tp_rv is not False, "check_block_gram_and_determinant"; return _tp_rv


def check_hyperbolic_plane_and_orthocomplement():
    ok = True
    for (p, q) in signatures():
        G, k, u = wall_data(p, q)
        n = p + q
        kk, n0, ni = block_vectors(n, k)
        for mu, nu in MUNU:
            h = ambient(G, u, mu, nu)
            plane = [[form(h, a, b) for b in (kk, n0)] for a in (kk, n0)]
            ok = ok and GA.congruence_signature(plane) == (1, 1, 0)
            w = [kk[i] + nu * ni[i] - mu * n0[i] for i in range(n + 2)]
            ok = ok and form(h, w, kk) == 0 and form(h, w, n0) == 0
            ok = ok and form(h, w, w) == 2 * mu * nu
            ok = ok and GA.rank_of_vectors([kk, n0, w]) == 3
            blk = [[form(h, a, b) for b in (kk, n0, ni)] for a in (kk, n0, ni)]
            want = (2, 1, 0) if mu * nu > 0 else (1, 2, 0)
            ok = ok and GA.congruence_signature(blk) == want
    _tp_rv = (ok); assert _tp_rv is not False, "check_hyperbolic_plane_and_orthocomplement"; return _tp_rv


def check_orthogonal_splitting_and_wall_signature():
    premise("sheaf.degeneration-sheaf")      # G|V1 is the induced quotient form, signature (p-1, q)
    ok = True
    for (p, q) in signatures():
        G, k, u = wall_data(p, q)
        n = p + q
        V1 = GA.field_kernel([u])                         # covectors with alpha(u) = 0
        ok = ok and len(V1) == n - 1 and GA.rank_of_vectors(V1 + [k]) == n
        GV1 = [[sum((a[i] * G[i][j] * b[j] for i in range(n) for j in range(n)), F(0)) for b in V1] for a in V1]
        if n > 1:
            ok = ok and GA.congruence_signature(GV1) == (p - 1, q, 0)
        kk, n0, ni = block_vectors(n, k)
        V1e = [list(a) + [F(0), F(0)] for a in V1]
        for mu, nu in MUNU:
            h = ambient(G, u, mu, nu)
            ok = ok and all(form(h, a, b) == 0 for a in V1e for b in (kk, n0, ni))
            ok = ok and GA.rank_of_vectors(V1e + [kk, n0, ni]) == n + 2
            want = (p + 1, q + 1, 0) if mu * nu > 0 else (p, q + 2, 0)
            ok = ok and GA.congruence_signature(h) == want
    _tp_rv = (ok); assert _tp_rv is not False, "check_orthogonal_splitting_and_wall_signature"; return _tp_rv
