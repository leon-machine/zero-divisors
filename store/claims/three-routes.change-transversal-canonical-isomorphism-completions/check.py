"""three-routes.change-transversal-canonical-isomorphism-completions: exact checks.

Boundary data of exact Schwarzschild (the imported boundary Gram G(0) on the frame (rho, dt_PG, mu1, mu2),
k = rho + m dt_PG) at m = sqrt(2M) = 1, 2, 3, 1/2, each with two transversals u (k(u) = 1); collar constants
(mu, nu) = (-2, 3) and (2, 3). h_u is the ambient form of the imported collar data at beta = 1: G on W,
h(alpha, n0) = nu alpha(u), h(alpha, ninf) = mu alpha(u), h(n0, ninf) = -1, n0^2 = ninf^2 = 0. For v in a
basis of ker k and one combination, vt is the normalised solve and Phi_v = 1 on W, n0 -> n0 + nu vt,
ninf -> ninf + mu vt.
(1) Phi_v^T h_u Phi_v = h_(u+v) exactly; Phi_v is the identity on W (so fixes k); (Phi_v - 1)^2 = 0 and
    Phi_v^-1 = 2 - Phi_v; the un-normalised representative vt + k breaks the identity (control).
(2) Canonicity: every particular solution vt0 + t k of the solve normalises to the same vt, so Phi_v is
    choice-free.
(3) Ladder to ladder, in the exterior model of the Clifford algebras on all 64 basis states: (k, n0/(2 nu))
    is a CAR pair of Cl(T, h_(u+v)), and its image (Phi k, Phi n0/(2 nu)) is a CAR pair of Cl(T, h_u) for the
    same k ({x, y} = 1, x^2 = y^2 = 0), distinct from the h_u-ladder (k, n0/(2 nu)).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MASSES = [F(1), F(2), F(3), F(1, 2)]
MUNU = [(F(-2), F(3)), (F(2), F(3))]
T_SAMPLES = [F(1), F(-2), F(5, 3)]


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




def vs_of(k):
    basis = GA.field_kernel([k])
    return basis + [[basis[0][i] + 2 * basis[1][i] - basis[2][i] for i in range(len(k))]]


def check_intertwiner_on_boundary_data():
    premise("three-routes.imported-collar-data-coupling")
    premise("three-routes.radical-gauge-closes-solve")
    ok = True
    cases = 0
    for G, k, u in boundary_fibres():
        n = len(k)
        k6 = list(k) + [F(0), F(0)]
        for mu, nu in MUNU:
            hu = ambient(G, u, mu, nu)
            for v in vs_of(k):
                vt = normalised(G, k, u, v)
                P = phi(vt, mu, nu)
                huv = ambient(G, [u[i] + v[i] for i in range(n)], mu, nu)
                ok = ok and _mm(_tr(P), _mm(hu, P)) == huv
                ok = ok and all(_apply(P, e) == e for e in _eye(n + 2)[:n]) and _apply(P, k6) == k6
                Nm = [[P[i][j] - (1 if i == j else 0) for j in range(n + 2)] for i in range(n + 2)]
                ok = ok and all(x == 0 for row in _mm(Nm, Nm) for x in row)
                Pinv = [[2 * (1 if i == j else 0) - P[i][j] for j in range(n + 2)] for i in range(n + 2)]
                ok = ok and _mm(P, Pinv) == _eye(n + 2)
                bad = phi([vt[i] + k[i] for i in range(n)], mu, nu)
                ok = ok and _mm(_tr(bad), _mm(hu, bad)) != huv
                cases += 1
    _tp_rv = (ok and cases == 4 * 2 * 2 * 4); assert _tp_rv is not False, "check_intertwiner_on_boundary_data"; return _tp_rv


def check_normalised_representative_is_choice_free():
    premise("three-routes.radical-gauge-closes-solve")
    ok = True
    for G, k, u in boundary_fibres():
        n = len(k)
        for v in vs_of(k):
            vt = normalised(G, k, u, v)
            vt0 = solve(G, v)
            for t in T_SAMPLES:
                alt = [vt0[i] + t * k[i] for i in range(n)]
                s = -(_gq(G, alt, alt) + 2 * _dot(alt, u)) / 2
                ok = ok and [alt[i] + s * k[i] for i in range(n)] == vt
    _tp_rv = (ok); assert _tp_rv is not False, "check_normalised_representative_is_choice_free"; return _tp_rv


def _st_add(*ds):
    out = {}
    for d in ds:
        for S, c in d.items():
            out[S] = out.get(S, F(0)) + c
    return {S: c for S, c in out.items() if c != 0}


def _is_car(h, x, y):
    ok = True
    for S in GA.all_blades(len(h)):
        st = {frozenset(S): F(1)}
        anti = _st_add(GA.ext_c(x, h, GA.ext_c(y, h, st)), GA.ext_c(y, h, GA.ext_c(x, h, st)))
        ok = ok and GA.ext_state_eq(anti, st)
        ok = ok and GA.ext_c(x, h, GA.ext_c(x, h, st)) == {} and GA.ext_c(y, h, GA.ext_c(y, h, st)) == {}
    return ok


def check_ladder_carried_to_ladder():
    premise("three-routes.imported-collar-data-coupling")
    premise("three-routes.radical-gauge-closes-solve")
    ok = True
    for (G, k, u), (mu, nu) in ((boundary_fibres()[2], MUNU[0]), (boundary_fibres()[5], MUNU[1])):
        n = len(k)
        v = vs_of(k)[0]
        vt = normalised(G, k, u, v)
        P = phi(vt, mu, nu)
        hu = ambient(G, u, mu, nu)
        huv = ambient(G, [u[i] + v[i] for i in range(n)], mu, nu)
        k6 = list(k) + [F(0), F(0)]
        kstar = [F(0)] * n + [F(1) / (2 * nu), F(0)]
        ok = ok and _is_car(huv, k6, kstar)
        img_k, img_ks = _apply(P, k6), _apply(P, kstar)
        ok = ok and img_k == k6 and img_ks != kstar
        ok = ok and _is_car(hu, img_k, img_ks)
    _tp_rv = (ok); assert _tp_rv is not False, "check_ladder_carried_to_ladder"; return _tp_rv
