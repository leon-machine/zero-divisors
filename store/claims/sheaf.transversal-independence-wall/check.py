"""sheaf.transversal-independence-wall: exact checks.

Wall fibres: the Schwarzschild wall Gram [[m^2, -m, 0, 0], [-m, 1, 0, 0], 0, 0; diag(-1, -1)] with
k = rho + m dt at m = 1, 2, and general-frame wall cometrics G = P^T diag(0, +-1, ...) P (radical
k = P^-1 e_0) for (p, q) = (1, 2), (2, 1), (1, 3), (2, 2); transversal u with k(u) = 1; collar constants
(mu, nu) = (-2, 3) and (2, 3). The ambient form h_u on T = T*M + span(n0, ninf): G on covectors,
h(alpha, n0) = nu alpha(u), h(alpha, ninf) = mu alpha(u), h(n0, ninf) = -1, n0^2 = ninf^2 = 0.
For v in a basis of ker k, vt is the normalised solve (G vt = v, G(vt, vt) + 2 vt(u) = 0) and Phi_v is
the identity on T*M with n0 -> n0 + nu vt, ninf -> ninf + mu vt.
(1) Phi_v^T h_u Phi_v = h_(u+v) exactly; (Phi_v - 1)^2 = 0; Phi_v fixes k and every covector; the
    un-normalised representative vt + k breaks the identity (control).
(2) The cocycle: vt + wt (w normalised against u + v) is the representative of v + w normalised against u,
    and Phi^u_v Phi^(u+v)_w = Phi^u_(v+w) as matrices.
(3) Clifford level, in the exterior model of Cl(T, h_u) on all basis states: Phi_v(k*) = k* + vt/2 with
    k* = n0/(2 nu) is null with {k, Phi_v(k*)} = 1 (a ladder partner of the same k, different from k*),
    and Phi_v(sigma) = sigma + vt k for sigma = k* k - k k*, with the images computed by applying Phi_v.
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


def check_phi_is_unipotent_isometry_fixing_cotangent():
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    cases = 0
    for G, k, u in wall_fibres():
        n = len(k)
        for mu, nu in MUNU:
            hu = ambient(G, u, mu, nu)
            for v in GA.field_kernel([k]):
                vt = normalised(G, k, u, v)
                ok = ok and _gq(G, vt, vt) + 2 * _dot(vt, u) == 0
                P = phi(vt, mu, nu)
                huv = ambient(G, [u[i] + v[i] for i in range(n)], mu, nu)
                ok = ok and _mm(_tr(P), _mm(hu, P)) == huv
                N = [[P[i][j] - (1 if i == j else 0) for j in range(n + 2)] for i in range(n + 2)]
                ok = ok and all(x == 0 for row in _mm(N, N) for x in row)
                ok = ok and all(_apply(P, e) == e for e in _eye(n + 2)[:n])     # identity on T*M (k included)
                bad = phi([vt[i] + k[i] for i in range(n)], mu, nu)
                ok = ok and _mm(_tr(bad), _mm(hu, bad)) != huv
                cases += 1
    _tp_rv = (ok and cases == 2 * (3 + 3 + 2 + 2 + 3 + 3)); assert _tp_rv is not False, "check_phi_is_unipotent_isometry_fixing_cotangent"; return _tp_rv


def _compose_pairs(basis):
    """Sample pairs (v, w) in ker k for the cocycle."""
    n = len(basis[0])
    return [(basis[0], basis[-1]), (basis[-1], [basis[0][i] - 2 * basis[-1][i] for i in range(n)])]


# Hand sample: the Schwarzschild wall at m = 1, u = e_0, v = e_2, w = e_3 (both in ker k), (mu, nu) = (-2, 3).
HAND_M = F(1)
HAND_V = [F(0), F(0), F(1), F(0)]
HAND_W = [F(0), F(0), F(0), F(1)]
HAND_MUNU = (F(-2), F(3))


def check_intertwiners_compose():
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    # By hand at the m = 1 wall (G = [[1,-1],[-1,1]] + diag(-1,-1), k = (1,1,0,0)): G x = e_2 gives
    # x = (0,0,-1,0) + t k, and G(x,x) + 2 x(u) = -1 + t = 0 at t = 1/2, so vt = (1/2,1/2,-1,0); against
    # u + v likewise wt = (1/2,1/2,0,-1); v + w against u gives x = (0,0,-1,-1), G(x,x) = -2, t = 1,
    # zt = (1,1,-1,-1) = vt + wt. The composite's n0 and ninf columns are nu zt = (3,3,-3,-3), mu zt = (-2,-2,2,2).
    G, k, u = [f for f in wall_fibres() if f[1][1] == HAND_M][0]
    mu, nu = HAND_MUNU
    vt = normalised(G, k, u, HAND_V)
    wt = normalised(G, k, [u[i] + HAND_V[i] for i in range(4)], HAND_W)
    ok = ok and vt == [F(1, 2), F(1, 2), F(-1), F(0)] and wt == [F(1, 2), F(1, 2), F(0), F(-1)]
    comp = _mm(phi(vt, mu, nu), phi(wt, mu, nu))
    ok = ok and [comp[i][4] for i in range(4)] == [F(3), F(3), F(-3), F(-3)]
    ok = ok and [comp[i][5] for i in range(4)] == [F(-2), F(-2), F(2), F(2)]
    for G, k, u in wall_fibres():
        n = len(k)
        basis = GA.field_kernel([k])
        ok = ok and len(basis) == n - 1          # ker of a nonzero covector: corank one
        pairs = _compose_pairs(basis)
        for mu, nu in MUNU:
            for v, w in pairs:
                uv = [u[i] + v[i] for i in range(n)]
                vt = normalised(G, k, u, v)
                wt = normalised(G, k, uv, w)
                zt = normalised(G, k, u, [v[i] + w[i] for i in range(n)])
                ok = ok and [vt[i] + wt[i] for i in range(n)] == zt
                ok = ok and _mm(phi(vt, mu, nu), phi(wt, mu, nu)) == phi(zt, mu, nu)
                # G(wt, vt) = wt(v), the defining property used in the cocycle
                ok = ok and _gq(G, wt, vt) == _dot(wt, v)
    _tp_rv = (ok); assert _tp_rv is not False, "check_intertwiners_compose"; return _tp_rv


def _st_add(*ds):
    out = {}
    for d in ds:
        for S, c in d.items():
            out[S] = out.get(S, F(0)) + c
    return {S: c for S, c in out.items() if c != 0}


def _st_neg(d):
    return {S: -c for S, c in d.items()}


def check_ladder_partner_and_parity_images():
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    mu, nu = MUNU[0]
    for G, k, u in wall_fibres()[1:3]:            # Schwarzschild m = 2 and the (1, 2) wall
        n = len(k)
        N = n + 2
        hu = ambient(G, u, mu, nu)
        k6 = list(k) + [F(0), F(0)]
        kstar = [F(0)] * n + [F(1) / (2 * nu), F(0)]
        v = GA.field_kernel([k])[0]
        vt = normalised(G, k, u, v)
        vt6 = list(vt) + [F(0), F(0)]
        P = phi(vt, mu, nu)
        ks_img = _apply(P, kstar)
        ok = ok and ks_img == [kstar[i] + vt6[i] / 2 for i in range(N)] and ks_img != kstar
        ok = ok and _apply(P, k6) == k6
        ok = ok and _gq(hu, ks_img, ks_img) == 0 and 2 * _gq(hu, k6, ks_img) == 1

        def act(x, st):
            return GA.ext_c(x, hu, st)
        for S in GA.all_blades(N):
            st = {frozenset(S): F(1)}
            car = _st_add(act(k6, act(ks_img, st)), act(ks_img, act(k6, st)))
            ok = ok and GA.ext_state_eq(car, st)
            sig_old = _st_add(act(kstar, act(k6, st)), _st_neg(act(k6, act(kstar, st))))
            sig_new = _st_add(act(ks_img, act(k6, st)), _st_neg(act(k6, act(ks_img, st))))
            ok = ok and GA.ext_state_eq(sig_new, _st_add(sig_old, act(vt6, act(k6, st))))
    _tp_rv = (ok); assert _tp_rv is not False, "check_ladder_partner_and_parity_images"; return _tp_rv
