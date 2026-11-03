"""sheaf.no-equivariant-value-wall: exact checks.

Wall fibres and collar data as in the transversal-independence check: the Schwarzschild wall Gram at
m = 1, 2 (k = rho + m dt) and general-frame corank-one cometrics for (p, q) = (1, 2), (2, 1), (1, 3),
(2, 2); transversal u with k(u) = 1; (mu, nu) = (-2, 3) and (2, 3); h_u the ambient form. For lambda in
a basis of ker k and one combination: g_lambda(alpha) = alpha + alpha(lambda) k, ghat = g_lambda + id,
Phi_lambda the normalised intertwiner, theta = ghat Phi_lambda^-1 (Phi^-1 = 2 - Phi, unipotent).
(1) ghat^T h_u ghat = h_(u+lambda); theta^T h_u theta = h_u; theta k = k; theta maps T*M to itself and
    restricts there to g_lambda; theta != 1.
(2) The contragredient (theta|T*M)^-T, computed by exact inversion, is 1 - lambda (x) k; it translates every
    sampled candidate (k(u') = 1) by -lambda and fixes none; it is additive in lambda (an action of
    (ker k, +)), and only lambda = 0 fixes a candidate (free).
(3) Fix(theta) (kernel of theta - 1) has dimension n = {a in T*M : a(lambda) = 0} + {b n0 + c ninf :
    b nu + c mu = 0}, as the proof derives, and h_u(k, x) = 0 on all of it: no theta-fixed ladder partner
    (a partner has h_u(k, x) = 1/2).
(4) The partner attached to the candidate u + v, Phi_v(k*) = k* + vt/2, is a ladder partner of k in h_u, and
    v -> vt is injective: vt recovers v through alpha(v) = G(alpha, vt), and distinct v give distinct partners.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(1, 2), (2, 1), (1, 3), (2, 2)]
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


def _frame(n):
    U = [[F(1) if i == j else (F((i + 2 * j) % 3 - 1) if j > i else F(0)) for j in range(n)] for i in range(n)]
    L = [[F(1) if i == j else (F((2 * i + j) % 3 - 1) if j < i else F(0)) for j in range(n)] for i in range(n)]
    return _mm(U, L)


def wall_fibres():
    out = []
    for m in (F(1), F(2)):
        G = [[m * m, -m, F(0), F(0)], [-m, F(1), F(0), F(0)], [F(0), F(0), F(-1), F(0)], [F(0), F(0), F(0), F(-1)]]
        out.append((G, [F(1), m, F(0), F(0)], [F(1), F(0), F(0), F(0)]))
    for (p, q) in SIGS:
        n = p + q
        D = [[F(0)] * n for _ in range(n)]
        for i in range(1, n):
            D[i][i] = F(1) if i < p else F(-1)
        P = _frame(n)
        G = _mm(_tr(P), _mm(D, P))
        k = GA.field_solve(P, [F(1)] + [F(0)] * (n - 1))
        w = [F(i + 2) for i in range(n)]
        out.append((G, k, [x / _dot(k, w) for x in w]))
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
    n = len(k)
    return basis + [[basis[0][i] - 3 * basis[-1][i] for i in range(n)]]


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
    ok = _mm(P, Pinv) == _eye(n2)
    return _mm(ghat(k, lam), Pinv), ok


def check_theta_is_automorphism_fixing_k():
    premise("sheaf.base-unipotents-wall")
    premise("sheaf.transversal-independence-wall")
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    cases = 0
    for G, k, u in wall_fibres():
        n = len(k)
        k6 = list(k) + [F(0), F(0)]
        for mu, nu in MUNU:
            hu = ambient(G, u, mu, nu)
            for lam in lambdas(k):
                hul = ambient(G, [u[i] + lam[i] for i in range(n)], mu, nu)
                Gh = ghat(k, lam)
                ok = ok and _mm(_tr(Gh), _mm(hu, Gh)) == hul
                th, inv_ok = theta(G, k, u, lam, mu, nu)
                ok = ok and inv_ok and _mm(_tr(th), _mm(hu, th)) == hu
                ok = ok and _apply(th, k6) == k6 and th != _eye(n + 2)
                for j in range(n):
                    col = [th[i][j] for i in range(n + 2)]
                    want = [(1 if i == j else 0) + k[i] * lam[j] for i in range(n)] + [0, 0]
                    ok = ok and col == want
                cases += 1
    _tp_rv = (ok and cases == 2 * (4 + 4 + 3 + 3 + 4 + 4)); assert _tp_rv is not False, "check_theta_is_automorphism_fixing_k"; return _tp_rv


def check_dual_action_translates_candidates():
    premise("sheaf.base-unipotents-wall")
    premise("sheaf.transversal-independence-wall")
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    mu, nu = MUNU[0]
    for G, k, u in wall_fibres():
        n = len(k)
        cands = [u, [u[i] + 2 * GA.field_kernel([k])[0][i] for i in range(n)]]
        duals = {}
        for idx, lam in enumerate(lambdas(k)):
            th, _ = theta(G, k, u, lam, mu, nu)
            base = [[th[i][j] for j in range(n)] for i in range(n)]
            inv = [GA.field_solve(base, e) for e in _eye(n)]          # columns of the inverse
            dual = [[inv[i][j] for j in range(n)] for i in range(n)]   # inverse transposed (inv[c] = column c)
            closed = [[(1 if i == j else 0) - lam[i] * k[j] for j in range(n)] for i in range(n)]
            ok = ok and dual == closed
            for c in cands:
                ok = ok and _dot(k, c) == 1
                img = _apply(dual, c)
                ok = ok and img == [c[i] - lam[i] for i in range(n)] and img != c
            duals[idx] = (lam, dual)
        # additivity: dual(lambda) dual(lambda') = dual(lambda + lambda'), and only lambda = 0 fixes u
        (l0, d0), (l1, d1) = duals[0], duals[1]
        th01, _ = theta(G, k, u, [l0[i] + l1[i] for i in range(n)], mu, nu)
        base01 = [[th01[i][j] for j in range(n)] for i in range(n)]
        inv01 = [GA.field_solve(base01, e) for e in _eye(n)]
        ok = ok and _mm(d0, d1) == [[inv01[i][j] for j in range(n)] for i in range(n)]
        zero_fix, _ = theta(G, k, u, [F(0)] * n, mu, nu)
        ok = ok and zero_fix == _eye(n + 2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_dual_action_translates_candidates"; return _tp_rv


def check_no_theta_fixed_ladder_partner():
    premise("sheaf.transversal-independence-wall")
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    for G, k, u in wall_fibres():
        n = len(k)
        k6 = list(k) + [F(0), F(0)]
        for mu, nu in MUNU:
            hu = ambient(G, u, mu, nu)
            for lam in lambdas(k):
                th, _ = theta(G, k, u, lam, mu, nu)
                fix = GA.field_kernel([[th[i][j] - (1 if i == j else 0) for j in range(n + 2)] for i in range(n + 2)])
                ok = ok and len(fix) == n
                ok = ok and all(_gq(hu, k6, x) == 0 for x in fix)
                # the proof's description of the fixed set
                desc = [list(a) + [F(0), F(0)] for a in GA.field_kernel([lam])] + [[F(0)] * n + [mu, -nu]]
                ok = ok and all(_apply(th, x) == x for x in desc)
                ok = ok and GA.rank_of_vectors(desc) == n == GA.rank_of_vectors(desc + fix)
    _tp_rv = (ok); assert _tp_rv is not False, "check_no_theta_fixed_ladder_partner"; return _tp_rv


def check_partners_attached_injectively():
    premise("sheaf.transversal-independence-wall")
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    mu, nu = MUNU[0]
    for G, k, u in wall_fibres():
        n = len(k)
        hu = ambient(G, u, mu, nu)
        k6 = list(k) + [F(0), F(0)]
        kstar = [F(0)] * n + [F(1) / (2 * nu), F(0)]
        partners = []
        vs = lambdas(k) + [[F(0)] * n]
        for v in vs:
            vt = normalised(G, k, u, v)
            ok = ok and [_dot(G[i], vt) for i in range(n)] == list(v)     # vt recovers v
            x = _apply(phi(vt, mu, nu), kstar)
            ok = ok and x == [kstar[i] + (vt[i] / 2 if i < n else 0) for i in range(n + 2)]
            ok = ok and _gq(hu, x, x) == 0 and 2 * _gq(hu, k6, x) == 1
            partners.append(tuple(x))
        ok = ok and len(set(partners)) == len(vs)
    _tp_rv = (ok); assert _tp_rv is not False, "check_partners_attached_injectively"; return _tp_rv
