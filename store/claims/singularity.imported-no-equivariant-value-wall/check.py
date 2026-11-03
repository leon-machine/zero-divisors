"""singularity.imported-no-equivariant-value-wall: exact checks on the Schwarzschild boundary data at two masses
(m = 1, 2; G(0) = [[m^2, -m], [-m, 1]] + diag(-1, -1), k = rho + m dt), collar constants mu, nu = -2, 3, base
transversal u = (1, 0, 0, 0) with k(u) = 1.

h_u is the 6 x 6 ambient form on (rho, dt, mu1, mu2, n0, ninf): G, coupling columns nu u and mu u, and the
hyperbolic block [[0, -1], [-1, 0]]. tilde v solves G tilde v = v (v in ker k) in the radical gauge with
G(tilde v, tilde v) + 2 tilde v(u) = 0; Phi_v is the identity on T*M with Phi_v(n0) = n0 + nu tilde v,
Phi_v(ninf) = ninf + mu tilde v; g_lambda = id + k lambda^T and hat g = g_lambda + id.
(1) For lambda = (-m, 1, 0, 0) and (0, 0, 1, -1): Phi^T h_u Phi = h_(u + lambda) and hat g^T h_u hat g =
h_(u + lambda), so theta = hat g Phi^{-1} satisfies theta^T h_u theta = h_u, theta k = k, theta != id, and theta
preserves T*M, acting there as g_lambda (so it preserves the grading and the degeneration subalgebra).
(2) The contragredient (theta|T*M)^{-T}, computed by exact inversion, is id - lambda k^T; it translates three
candidates by -lambda and fixes none: a natural candidate value would be a fixed point, and there is none.
(3) Fix(theta) (exact kernel of theta - id) has dimension 4 and lies in the h_u-orthogonal of k, whereas the
partner k* = n0/(2 nu) has h_u(k, k*) = 1/2: no theta-fixed ladder partner.
(4) For each of the 26 nonzero v in the {-1, 0, 1}-lattice of ker k, Phi_v(k*) = k* + tilde v/2 is a ladder partner
of k in (T, h_u) (null, h_u(k, .) = 1/2), G tilde v = v recovers v, and the 27 partners are pairwise distinct
(injective in v).
sheaf.no-equivariant-value-wall is this statement itself (imported verbatim), so it gets no premise() call.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

MASSES = (F(1), F(2))
MU, NU = F(-2), F(3)
U0 = [F(1), F(0), F(0), F(0)]


mm = GA.mat_mul


def tr(A):
    return [list(r) for r in zip(*A)]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def data(m):
    G = [[m * m, -m, F(0), F(0)], [-m, F(1), F(0), F(0)], [F(0), F(0), F(-1), F(0)], [F(0), F(0), F(0), F(-1)]]
    return G, [F(1), m, F(0), F(0)]


def build_h(G, u):
    h = [[F(0)] * 6 for _ in range(6)]
    for i in range(4):
        for j in range(4):
            h[i][j] = G[i][j]
        h[i][4] = h[4][i] = NU * u[i]
        h[i][5] = h[5][i] = MU * u[i]
    h[4][5] = h[5][4] = F(-1)
    return h


def quad(G, a, b):
    return sum(a[i] * G[i][j] * b[j] for i in range(len(a)) for j in range(len(a)))


def solve_any(M, rhs):
    """One solution of the singular system M x = rhs (pivot columns, free variables 0)."""
    n = len(M)
    A = [list(M[i]) + [rhs[i]] for i in range(n)]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, n) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    assert all(A[i][n] == 0 for i in range(r, n))
    x = [F(0)] * n
    for i, c in enumerate(piv):
        x[c] = A[i][n]
    return x


def vtilde(G, k, v, u):
    t0 = solve_any(G, v)
    base = quad(G, t0, t0) + 2 * sum(t0[i] * u[i] for i in range(4))
    return [t0[i] - (base / 2) * k[i] for i in range(4)]


def phi(vt):
    P = eye(6)
    for i in range(4):
        P[i][4] = NU * vt[i]
        P[i][5] = MU * vt[i]
    return P


def theta_for(G, k, lam):
    vt = vtilde(G, k, lam, U0)
    P = phi(vt)
    Pinv = [[2 * (F(1) if i == j else F(0)) - P[i][j] for j in range(6)] for i in range(6)]
    ghat = eye(6)
    for i in range(4):
        for j in range(4):
            ghat[i][j] += k[i] * lam[j]
    return P, ghat, mm(ghat, Pinv)


def lambdas(m):
    return [[-m, F(1), F(0), F(0)], [F(0), F(0), F(1), F(-1)]]


def check_theta_is_automorphism_fixing_k():
    premise("sheaf.base-unipotents-wall")
    premise("sheaf.transversal-independence-wall")
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    for m in MASSES:
        G, k = data(m)
        hu = build_h(G, U0)
        k6 = k + [F(0), F(0)]
        for lam in lambdas(m):
            ok = ok and sum(k[i] * lam[i] for i in range(4)) == 0
            huv = build_h(G, [U0[i] + lam[i] for i in range(4)])
            P, ghat, th = theta_for(G, k, lam)
            ok = ok and mm(tr(P), mm(hu, P)) == huv and mm(tr(ghat), mm(hu, ghat)) == huv
            ok = ok and mm(tr(th), mm(hu, th)) == hu and th != eye(6)
            ok = ok and [sum(th[i][j] * k6[j] for j in range(6)) for i in range(6)] == k6
            # theta preserves T*M and acts there as g_lambda = id + k lambda^T
            ok = ok and all(th[i][j] == 0 for i in (4, 5) for j in range(4))
            ok = ok and all(th[i][j] == (1 if i == j else 0) + k[i] * lam[j] for i in range(4) for j in range(4))
    GA.check("theta = hat g Phi^{-1} is an isometry of h_u fixing k, acting on T*M as g_lambda", ok)
    return ok


def check_contragredient_translates_candidates():
    premise("sheaf.base-unipotents-wall")
    ok = True
    for m in MASSES:
        G, k = data(m)
        for lam in lambdas(m):
            th = theta_for(G, k, lam)[2]
            base = [row[:4] for row in th[:4]]
            cols = [GA.field_solve(base, [F(1) if i == c else F(0) for i in range(4)]) for c in range(4)]
            dual = [[cols[i][j] for j in range(4)] for i in range(4)]     # transpose of the inverse
            ok = ok and dual == [[(1 if i == j else 0) - lam[i] * k[j] for j in range(4)] for i in range(4)]
            for c in (U0, [F(1) - m, F(1), F(0), F(0)], [F(1), F(0), F(5), F(-2)]):
                ok = ok and sum(k[i] * c[i] for i in range(4)) == 1
                img = [sum(dual[i][j] * c[j] for j in range(4)) for i in range(4)]
                ok = ok and img == [c[i] - lam[i] for i in range(4)] and img != c
    GA.check("the contragredient is id - lambda (x) k: every candidate moves by -lambda, none is fixed", ok)
    return ok


def check_no_theta_fixed_ladder_partner():
    premise("sheaf.transversal-independence-wall")
    ok = True
    for m in MASSES:
        G, k = data(m)
        hu = build_h(G, U0)
        k6 = k + [F(0), F(0)]
        kstar = [F(0)] * 4 + [1 / (2 * NU), F(0)]
        ok = ok and 2 * quad(hu, k6, kstar) == 1 and quad(hu, kstar, kstar) == 0
        for lam in lambdas(m):
            th = theta_for(G, k, lam)[2]
            fix = GA.field_kernel([[th[i][j] - (1 if i == j else 0) for j in range(6)] for i in range(6)])
            ok = ok and len(fix) == 4 and all(quad(hu, k6, x) == 0 for x in fix)
    GA.check("Fix(theta) is 4-dimensional inside k-perp, while a ladder partner has h(k, x) = 1/2", ok)
    return ok


def check_partners_attached_injectively():
    premise("sheaf.transversal-independence-wall")
    premise("sheaf.solve-closed-radical-gauge")
    ok = True
    for m in MASSES:
        G, k = data(m)
        hu = build_h(G, U0)
        k6 = k + [F(0), F(0)]
        kstar = [F(0)] * 4 + [1 / (2 * NU), F(0)]
        basis = [[-m, F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
        partners = []
        for c in product((-1, 0, 1), repeat=3):
            v = [sum(c[b] * basis[b][i] for b in range(3)) for i in range(4)]
            vt = vtilde(G, k, v, U0)
            ok = ok and [sum(G[i][j] * vt[j] for j in range(4)) for i in range(4)] == v
            ok = ok and quad(G, vt, vt) + 2 * sum(vt[i] * U0[i] for i in range(4)) == 0
            P = phi(vt)
            pk = [sum(P[i][j] * kstar[j] for j in range(6)) for i in range(6)]
            ok = ok and pk == [kstar[i] + (vt + [F(0), F(0)])[i] / 2 for i in range(6)]
            ok = ok and quad(hu, pk, pk) == 0 and 2 * quad(hu, k6, pk) == 1
            partners.append(tuple(pk))
        ok = ok and len(partners) == 27 and len(set(partners)) == 27
    GA.check("Phi_v(k*) = k* + tilde v/2 is a ladder partner of k for every v, injectively in v", ok)
    return ok
