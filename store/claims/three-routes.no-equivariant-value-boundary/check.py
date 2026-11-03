"""three-routes.no-equivariant-value-boundary: exact checks.

Boundary data of exact Schwarzschild at m = sqrt(2M) = 1, 2, 3, 1/2 (boundary Gram G(0) on the frame
(rho, dt_PG, mu1, mu2), k = rho + m dt_PG), two transversals u each, (mu, nu) = (-2, 3) and (2, 3); h_u the
ambient form of the imported collar data. For lambda in a basis of ker k and one combination:
g_lambda(alpha) = alpha + alpha(lambda) k on W, ghat = g_lambda + id, Phi_lambda the normalised intertwiner of
the change-of-transversal theorem, theta = ghat Phi_lambda^-1 with Phi^-1 = 2 - Phi.
(1) ghat is an isometry (T, h_(u+lambda)) -> (T, h_u); theta^T h_u theta = h_u; theta restricts to g_lambda
    on W (columns of theta on W computed); theta k = k; theta != 1.
(2) The dual action on candidate values, (theta|W)^-T computed by exact inversion, is 1 - lambda (x) k: every
    sampled candidate u' (k(u') = 1) goes to u' - lambda, none is fixed for lambda != 0, the action is additive
    in lambda, and theta at lambda = 0 is the identity: a free translation action of (ker k, +), so a natural
    candidate assignment (a common fixed point) does not exist.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MASSES = [F(1), F(2), F(3), F(1, 2)]
MUNU = [(F(-2), F(3)), (F(2), F(3))]


def _mm(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def _tr(A):
    return [list(r) for r in zip(*A)]


def _eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def _dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def _gq(G, a, b):
    return sum((a[i] * G[i][j] * b[j] for i in range(len(a)) for j in range(len(b))), F(0))


def boundary_fibres():
    """Schwarzschild boundary data G(0) on the frame (rho, dt_PG, mu1, mu2), k = rho + m dt_PG, with two
    transversals u (k(u) = 1) for each m = sqrt(2M)."""
    out = []
    for m in MASSES:
        G = [[m * m, -m, F(0), F(0)], [-m, F(1), F(0), F(0)], [F(0), F(0), F(-1), F(0)], [F(0), F(0), F(0), F(-1)]]
        k = [F(1), m, F(0), F(0)]
        for u in ([F(1), F(0), F(0), F(0)], [1 - m, F(1), F(3), F(-1)]):
            out.append((G, k, u))
    return out


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


def normalised(G, k, u, v):
    vt0 = solve(G, v)
    t = -(_gq(G, vt0, vt0) + 2 * _dot(vt0, u)) / 2
    return [vt0[i] + t * k[i] for i in range(len(k))]


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


def phi(vt, mu, nu):
    n = len(vt)
    P = _eye(n + 2)
    for i in range(n):
        P[i][n] = nu * vt[i]
        P[i][n + 1] = mu * vt[i]
    return P


def _apply(M, x):
    return [_dot(row, x) for row in M]




def lambdas(k):
    basis = GA.field_kernel([k])
    return basis + [[basis[0][i] - 3 * basis[-1][i] for i in range(len(k))]]


def ghat(k, lam):
    n = len(k)
    M = _eye(n + 2)
    for i in range(n):
        for j in range(n):
            M[i][j] += k[i] * lam[j]
    return M


def theta(G, k, u, lam, mu, nu):
    P = phi(normalised(G, k, u, lam), mu, nu)
    n2 = len(P)
    Pinv = [[2 * (1 if i == j else 0) - P[i][j] for j in range(n2)] for i in range(n2)]
    return _mm(ghat(k, lam), Pinv)


def dual_on_w(th, n):
    base = [[th[i][j] for j in range(n)] for i in range(n)]
    inv = [GA.field_solve(base, e) for e in _eye(n)]        # inv[c] = column c of the inverse
    return [[inv[i][j] for j in range(n)] for i in range(n)]   # its transpose


def check_theta_is_automorphism_of_completed_structure():
    premise("three-routes.base-unipotents-their-action-candidates")
    premise("three-routes.change-transversal-canonical-isomorphism-completions")
    premise("three-routes.imported-collar-data-coupling")
    ok = True
    cases = 0
    for G, k, u in boundary_fibres():
        n = len(k)
        k6 = list(k) + [F(0), F(0)]
        for mu, nu in MUNU:
            hu = ambient(G, u, mu, nu)
            for lam in lambdas(k):
                hul = ambient(G, [u[i] + lam[i] for i in range(n)], mu, nu)
                Gh = ghat(k, lam)
                ok = ok and _mm(_tr(Gh), _mm(hu, Gh)) == hul
                th = theta(G, k, u, lam, mu, nu)
                ok = ok and _mm(_tr(th), _mm(hu, th)) == hu
                ok = ok and _apply(th, k6) == k6 and th != _eye(n + 2)
                for j in range(n):
                    col = [th[i][j] for i in range(n + 2)]
                    ok = ok and col == [(1 if i == j else 0) + k[i] * lam[j] for i in range(n)] + [0, 0]
                cases += 1
    _tp_rv = (ok and cases == 4 * 2 * 2 * 4); assert _tp_rv is not False, "check_theta_is_automorphism_of_completed_structure"; return _tp_rv


def check_dual_action_is_free_translation():
    premise("three-routes.base-unipotents-their-action-candidates")
    premise("three-routes.change-transversal-canonical-isomorphism-completions")
    ok = True
    mu, nu = MUNU[0]
    for G, k, u in boundary_fibres():
        n = len(k)
        basis = GA.field_kernel([k])
        cands = [u, [u[i] + 2 * basis[0][i] - basis[1][i] for i in range(n)]]
        ds = []
        for lam in lambdas(k):
            d = dual_on_w(theta(G, k, u, lam, mu, nu), n)
            ok = ok and d == [[(1 if i == j else 0) - lam[i] * k[j] for j in range(n)] for i in range(n)]
            for c in cands:
                img = _apply(d, c)
                ok = ok and _dot(k, c) == 1 and img == [c[i] - lam[i] for i in range(n)] and img != c
            ds.append((lam, d))
        (l0, d0), (l1, d1) = ds[0], ds[1]
        d01 = dual_on_w(theta(G, k, u, [l0[i] + l1[i] for i in range(n)], mu, nu), n)
        ok = ok and _mm(d0, d1) == d01
        ok = ok and theta(G, k, u, [F(0)] * n, mu, nu) == _eye(n + 2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_dual_action_is_free_translation"; return _tp_rv
