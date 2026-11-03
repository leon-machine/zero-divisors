"""three-routes.imported-boundary-gram-ladder: exact checks on Schwarzschild data, 2M = m^2 with m = 1, 2 rational,
as rational-function identities in u = sqrt(r).

(1) The Gram of W on (rho, dt_PG, mu1, mu2), derived from the inverse PG metric block, is
[[m^2 - r, -m], [-m, 1]] + diag(-1, -1); det G = -r; at the boundary it is the stated G(0), symmetric of rank 3,
with radical exactly the line of k = rho + m dt_PG and G(k, k) = 0 there, while G(k, k) = -r off the boundary.
(2) The completed form h (normalised transversal dt/m, so k(u) = 1; coupling mu nu < 0): det h = det G (-F) with
F = 1 + 2 mu nu s for three couplings; inside the horizon s < 0 so F >= 1; the global coupling mu nu = -m^2/2 has
det h = m^2 at every radius and signature (2,4) at E and at interior, horizon and exterior radii.
(3) The ladder pair at E: k* = n0/(2 nu) satisfies c(k)c(k*) + c(k*)c(k) = 1 and c(k)^2 = c(k*)^2 = 0 on all
64 states of the exterior model of (T, h|E); off E (u = 1/2, 1) c(k)^2 = h(k, k) = -r != 0, so k is not null
and no ladder pair for k exists there.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

U = GA.RF.var()
R = U * U
MASSES = (F(1), F(2))
COUPLINGS = ((1, -1), (1, F(-1, 2)), (2, F(-1, 4)))          # (nu, mu), mu nu < 0
INSIDE = (F(1, 10), F(1, 3), F(1, 2), F(9, 10))             # u / m inside the horizon
RADII = (F(0), F(1, 4), F(1, 2), F(1), F(2))                 # u / m: boundary, interior, horizon, exterior


def C(x):
    return GA.RF.const(F(x))


def gram(m):
    beta = C(m) / U
    g_tt, g_tr, g_rr = GA.RF1 - beta * beta, -beta, C(-1)
    det = g_tt * g_rr - g_tr * g_tr
    Ctt, Ctr, Crr = g_rr / det, -g_tr / det, g_tt / det
    Z = GA.RF0
    return [[R * Crr, U * Ctr, Z, Z], [U * Ctr, Ctt, Z, Z], [Z, Z, C(-1), Z], [Z, Z, Z, C(-1)]]


def hmat(G, m, nu, mu):
    Z = GA.RF0
    cn, cm = C(F(nu) / m), C(F(mu) / m)
    return [[G[0][0], G[0][1], Z, Z, Z, Z],
            [G[1][0], G[1][1], Z, Z, cn, cm],
            [Z, Z, G[2][2], Z, Z, Z],
            [Z, Z, Z, G[3][3], Z, Z],
            [Z, cn, Z, Z, Z, C(-1)],
            [Z, cm, Z, Z, C(-1), Z]]


def at(M, u0):
    return [[e.eval(u0) for e in row] for row in M]


def check_boundary_gram_and_radical():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        G = gram(m)
        ok = ok and GA.rf_mat_det(G).eqrf(-R)
        G0 = at(G, F(0))
        ok = ok and G0 == [[m * m, -m, 0, 0], [-m, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
        ok = ok and all(G0[i][j] == G0[j][i] for i in range(4) for j in range(4))
        ok = ok and GA.mat_rank(G0) == 3
        ker = GA.field_kernel([[F(x) for x in row] for row in G0])
        ok = ok and len(ker) == 1 and ker[0][1] == m * ker[0][0] and ker[0][2] == 0 and ker[0][3] == 0
        k = [GA.RF1, C(m), GA.RF0, GA.RF0]
        gk = GA.RF0
        for i in range(4):
            for j in range(4):
                gk = gk + k[i] * G[i][j] * k[j]
        ok = ok and gk.eqrf(-R) and gk.eval(F(0)) == 0
    GA.check("G(0) is the stated corank-one matrix with radical R k, k = rho + m dt; det G = -r, G(k,k) = -r", ok)
    return ok


def check_completed_form_nondegenerate_on_physical_closure():
    premise("sheaf.one-sided-completion-singularity")
    ok = True
    for m in MASSES:
        G = gram(m)
        detG = GA.rf_mat_det(G)
        x = GA.rf_mat_solve(G, [GA.RF0, GA.RF1, GA.RF0, GA.RF0])
        s = C(F(1) / (m * m)) * x[1]                      # s = G^{-1}(e, e), e = (0, 1/m, 0, 0)
        ok = ok and s.eqrf((R - C(m * m)) / (C(m * m) * R))
        for nu, mu in COUPLINGS:
            Fn = GA.RF1 + C(2 * nu * mu) * s
            ok = ok and GA.rf_mat_det(hmat(G, m, nu, mu)).eqrf(detG * (-Fn))
            for u0 in (m * f for f in INSIDE):
                ok = ok and s.eval(u0) < 0 and Fn.eval(u0) >= 1
        hg = hmat(G, m, 1, -m * m / 2)
        ok = ok and GA.rf_mat_det(hg).eqrf(C(m * m))
        for u0 in (m * f for f in RADII):
            ok = ok and GA.congruence_signature(at(hg, u0)) == (2, 4, 0)
    GA.check("h is nondegenerate of signature (2,4) on the physical closure, E included", ok)
    return ok


def ext_add(*ds):
    tot = {}
    for d in ds:
        for S, c in d.items():
            tot[S] = tot.get(S, F(0)) + c
    return {S: c for S, c in tot.items() if c != 0}


def check_ladder_pair_exactly_over_boundary():
    premise("sheaf.one-sided-completion-singularity")
    ok = True
    for m in MASSES:
        G = gram(m)
        nu, mu = F(1), F(-1)
        k = [F(1), m, F(0), F(0), F(0), F(0)]
        ks = [F(0)] * 4 + [1 / (2 * nu), F(0)]
        h0 = at(hmat(G, m, nu, mu), F(0))
        for S in GA.all_blades(6):
            st = {frozenset(S): F(1)}
            car = ext_add(GA.ext_c(k, h0, GA.ext_c(ks, h0, st)), GA.ext_c(ks, h0, GA.ext_c(k, h0, st)))
            ok = ok and GA.ext_state_eq(car, st)
            ok = ok and GA.ext_c(k, h0, GA.ext_c(k, h0, st)) == {}
            ok = ok and GA.ext_c(ks, h0, GA.ext_c(ks, h0, st)) == {}
        for u0 in (F(1, 2), F(1)):
            hu = at(hmat(G, m, nu, mu), u0)
            vac = {frozenset(): F(1)}
            ok = ok and GA.ext_c(k, hu, GA.ext_c(k, hu, vac)) == {frozenset(): -u0 * u0}
    GA.check("k* = n0/(2 nu) is a ladder partner of k on E (64 states); off E k^2 = -r, no ladder pair", ok)
    return ok
