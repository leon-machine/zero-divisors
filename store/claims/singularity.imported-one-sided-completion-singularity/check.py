"""singularity.imported-one-sided-completion-singularity: exact checks on the Schwarzschild completion.

Data: the Gram G of W on (rho, dt_PG, mu1, mu2) from Fact sheaf.schwarzschild-degeneration-boundary-tame,
as rational functions of u = sqrt r (2M = m^2, horizon at u = m), for m = 1, 2. The coupling of the
collar construction (T4 Def. 4.1) with transversal u = dt/m (so k(u) = 1 for k = rho + m dt_PG) and a
bump b in [0, 1], b = 1 on E and b = 0 outside the horizon: on (rho, dt_PG, mu1, mu2, n0, ninf)
    h = [[G, K], [K^T, H]],  K = b (nu/m, mu/m) in the dt_PG row,  H = [[0, -1], [-1, 0]].
(1) h restricted to T*M is G identically, and on the plane it is H (the plane is hyperbolic).
(2) det h = r + 2 mu nu b^2 (r - m^2)/m^2 as a rational-function identity in u, for four bump values
    and three couplings with mu nu < 0. Inside the horizon (r < m^2) both terms are >= 0 and r > 0,
    outside b = 0 and det h = r, and on E det h = -2 mu nu > 0: det h never vanishes on the closure, so
    no shadow wall forms; the signature is (2,4) on a grid of radii and bump values, E included.
(3) The ladder pair: at E, k* = n0/(2 nu) satisfies c(k)c(k*) + c(k*)c(k) = 1 and c(k)^2 = c(k*)^2 = 0
    on all 64 states of the exterior model of h(0) (GA.ext_c); off E, c(k)^2 = h(k, k) = -r != 0, so
    the pair exists exactly over E.
(4) The orientability clause: k = dPhi with Phi = m t + (2/3) r^(3/2), i.e. k(d_t) = m and
    k(d_r) = dPhi/dr = sqrt r, nowhere zero, and k(d_t - beta d_r) = 0 with beta = m/sqrt r.
Not checked: the identification Cl(2,4) = Mat_4(H) (a classification fact checked elsewhere).
No premise() call on sheaf.one-sided-completion-singularity: this claim is its verbatim import.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

U = GA.RF.var()
R = U * U
MASSES = (F(1), F(2))
COUPLINGS = ((F(1), F(-1)), (F(1), F(-1, 2)), (F(2), F(-3)))       # (nu, mu)
BUMPS = (F(0), F(1, 3), F(3, 4), F(1))
RADII = (F(1, 5), F(1, 2), F(9, 10))                                # u/m inside the horizon
OUTSIDE = (F(1), F(3, 2), F(4))                                     # u/m at and beyond the horizon


def C(x):
    return GA.RF.const(F(x))


def gram(m):
    Z = GA.RF0
    return [[C(m * m) - R, C(-m), Z, Z], [C(-m), GA.RF1, Z, Z], [Z, Z, C(-1), Z], [Z, Z, Z, C(-1)]]


def hmat(m, nu, mu, b):
    G = gram(m)
    Z = GA.RF0
    cn, cm = C(b * nu / m), C(b * mu / m)
    return [[G[0][0], G[0][1], Z, Z, Z, Z],
            [G[1][0], G[1][1], Z, Z, cn, cm],
            [Z, Z, G[2][2], Z, Z, Z],
            [Z, Z, Z, G[3][3], Z, Z],
            [Z, cn, Z, Z, Z, C(-1)],
            [Z, cm, Z, Z, C(-1), Z]]


def at(M, u0):
    return [[e.eval(u0) for e in row] for row in M]


def check_completed_form_nondegenerate_no_shadow_wall():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        G = gram(m)
        for nu, mu in COUPLINGS:
            for b in BUMPS:
                h = hmat(m, nu, mu, b)
                ok = ok and all(h[i][j].eqrf(G[i][j]) for i in range(4) for j in range(4))
                ok = ok and at([row[4:] for row in h[4:]], F(0)) == [[0, -1], [-1, 0]]
                d = GA.rf_mat_det(h)
                ok = ok and d.eqrf(R + C(2 * mu * nu * b * b / (m * m)) * (R - C(m * m)))
                for f in RADII:
                    ok = ok and d.eval(m * f) > 0
                    ok = ok and GA.congruence_signature(at(h, m * f)) == (2, 4, 0)
            h1 = hmat(m, nu, mu, F(1))
            ok = ok and GA.rf_mat_det(h1).eval(F(0)) == -2 * mu * nu
            ok = ok and GA.congruence_signature(at(h1, F(0))) == (2, 4, 0)
        h0 = hmat(m, F(1), F(-1), F(0))
        ok = ok and GA.rf_mat_det(h0).eqrf(R)
        for f in OUTSIDE:
            ok = ok and GA.congruence_signature(at(h0, m * f)) == (2, 4, 0)
    GA.check("h restricts to G, det h = r + 2 mu nu b^2 (r - m^2)/m^2 > 0 on the closure, signature (2,4): "
             "no shadow wall", ok)
    return ok


def ext_add(*ds):
    tot = {}
    for d in ds:
        for S, c in d.items():
            tot[S] = tot.get(S, F(0)) + c
    return {S: c for S, c in tot.items() if c != 0}


def check_ladder_pair_exactly_over_boundary():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        for nu, mu in COUPLINGS[:2]:
            k = [F(1), m, F(0), F(0), F(0), F(0)]
            ks = [F(0)] * 4 + [1 / (2 * nu), F(0)]
            h0 = at(hmat(m, nu, mu, F(1)), F(0))
            for S in GA.all_blades(6):
                st = {frozenset(S): F(1)}
                car = ext_add(GA.ext_c(k, h0, GA.ext_c(ks, h0, st)), GA.ext_c(ks, h0, GA.ext_c(k, h0, st)))
                ok = ok and GA.ext_state_eq(car, st)
                ok = ok and GA.ext_c(k, h0, GA.ext_c(k, h0, st)) == {}
                ok = ok and GA.ext_c(ks, h0, GA.ext_c(ks, h0, st)) == {}
            for f in RADII:
                u0 = m * f
                hu = at(hmat(m, nu, mu, F(1)), u0)
                vac = {frozenset(): F(1)}
                ok = ok and GA.ext_c(k, hu, GA.ext_c(k, hu, vac)) == {frozenset(): -u0 * u0}
    GA.check("k* = n0/(2 nu) is a ladder partner of k on E (64 states); off E c(k)^2 = -r", ok)
    return ok


def check_dying_line_trivialised_by_rain_potential():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        phi_r = (C(F(2, 3)) * R * U).deriv() / R.deriv()       # dPhi/dr for Phi = (2/3) r^(3/2), via u
        ok = ok and phi_r.eqrf(U)
        beta = C(m) / U
        ok = ok and (C(m) - beta * phi_r).is_zero()
        ok = ok and all(phi_r.eval(m * f) == m * f for f in RADII + OUTSIDE)
    GA.check("k = dPhi: k(d_t) = m, k(d_r) = sqrt r, k(d_t - beta d_r) = 0: L is trivial, w1(L) = 0", ok)
    return ok
