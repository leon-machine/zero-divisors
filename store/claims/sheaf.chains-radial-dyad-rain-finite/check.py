"""sheaf.chains-radial-dyad-rain-finite: exact checks.

Conventions of the Schwarzschild composite: 2M = m^2, u = sqrt(r), beta = m/u; covectors in the
coordinate coframe (dt, dr) of the radial plane (the angular legs are untouched by the dyad and by
the gauge field). The cometric is the inverse of the Painleve-Gullstrand metric block
[[1 - beta^2, -beta], [-beta, -1]]; k/sqrt(r) = dr + beta dt; the rain frame is V = d_t - beta d_r,
e_r = d_r. All identities are rational-function identities in u (GA.RF), for m = 1 and m = 3.
(1) n_+- = k/sqrt(r) +- dt are G-null; n_+-(V) = +-1 and n_+-(e_r) = 1 at every radius, while the
coordinate legs diverge at the wall (u dr(V) -> -m != 0).
(2) The gauge field's covector action L(dt) = dt, L(dr) = dr - beta dt is fixed internally by
eta(L a, L b) = G(a, b) on all coordinate pairs, and L^-1(dt + dr) = n_+, L^-1(dt - dr) = -n_-.
(3) The same at rational radii in GA: Cl(1,1) with e_0 (dt, square +1) and e_1 (dr, square -1), the
flat dyad e_0 +- e_1 is null, G(a, b) := eta(L a, L b), and L^-1 of the flat dyad is the physical dyad.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

RF, RF0, RF1 = GA.RF, GA.RF0, GA.RF1
U = RF.var()
MASSES = (F(1), F(3))


def c(x):
    return RF.const(x)


def setup(m):
    beta = c(m) / U
    gtt, gtr, grr = RF1 - beta * beta, -beta, c(-1)
    det = gtt * grr - gtr * gtr
    G = [[grr / det, -gtr / det], [-gtr / det, gtt / det]]          # cometric on (dt, dr)
    return beta, G


def gpair(G, a, b):
    return a[0] * G[0][0] * b[0] + a[0] * G[0][1] * b[1] + a[1] * G[1][0] * b[0] + a[1] * G[1][1] * b[1]


def ev(a, X):
    return a[0] * X[0] + a[1] * X[1]


def check_dyad_null_with_constant_rain_components():
    premise("sheaf.rain-duality")
    ok = True
    for m in MASSES:
        beta, G = setup(m)
        ok = ok and G[0][0].eqrf(RF1) and G[0][1].eqrf(-beta) and G[1][1].eqrf(beta * beta - RF1)
        dt, dr = [RF1, RF0], [RF0, RF1]
        kou = [beta, RF1]
        n_p = [kou[0] + dt[0], kou[1] + dt[1]]
        n_m = [kou[0] - dt[0], kou[1] - dt[1]]
        V, er = [RF1, -beta], [RF0, RF1]
        ok = ok and gpair(G, n_p, n_p).is_zero() and gpair(G, n_m, n_m).is_zero()
        ok = ok and gpair(G, kou, kou).eqrf(c(-1)) and gpair(G, dt, dt).eqrf(RF1) and gpair(G, kou, dt).is_zero()
        ok = ok and ev(n_p, V).eqrf(c(1)) and ev(n_m, V).eqrf(c(-1))
        ok = ok and ev(n_p, er).eqrf(c(1)) and ev(n_m, er).eqrf(c(1))
        # the coordinate leg dr has a divergent rain component: u dr(V) = -m
        ok = ok and (U * ev(dr, V)).eqrf(c(-m))
    GA.check("radial dyad: n_+- null, rain components +-1 and 1 at every radius; dr(V) diverges", ok)
    return ok


def check_gauge_field_carries_flat_dyad_to_physical_dyad():
    premise("sheaf.rain-duality")
    ok = True
    for m in MASSES:
        beta, G = setup(m)
        eta = [[c(1), RF0], [RF0, c(-1)]]

        def L(a):
            return [a[0] - beta * a[1], a[1]]

        def Linv(a):
            return [a[0] + beta * a[1], a[1]]
        basis = [[RF1, RF0], [RF0, RF1]]
        ok = ok and all(gpair(eta, L(a), L(b)).eqrf(gpair(G, a, b)) for a in basis for b in basis)
        ok = ok and all((len(Linv(L(a))) == len(a) and all(x.eqrf(y) for x, y in zip(Linv(L(a)), a))) for a in basis)
        n_p = [beta + RF1, RF1]
        n_m = [beta - RF1, RF1]
        img_p, img_m = Linv([RF1, RF1]), Linv([RF1, c(-1)])
        ok = ok and (len(img_p) == len(n_p) and all(x.eqrf(y) for x, y in zip(img_p, n_p)))
        ok = ok and (len(img_m) == len(n_m) and all(x.eqrf(-y) for x, y in zip(img_m, n_m)))
    GA.check("radial dyad: eta(L a, L b) = G(a, b); L^-1(dt + dr) = n_+, L^-1(dt - dr) = -n_-", ok)
    return ok


SQ = [F(1), F(-1)]
RADII_U = (F(1, 3), F(1, 2), F(1), F(2), F(5))


def check_dyad_in_geometric_algebra():
    premise("sheaf.rain-duality")
    ok = True
    e0, e1 = GA.gen(0), GA.gen(1)
    ok = ok and GA.dot(GA.add(e0, e1), GA.add(e0, e1), SQ) == 0 and GA.dot(GA.sub(e0, e1), GA.sub(e0, e1), SQ) == 0
    for m in MASSES:
        for u in RADII_U:
            beta = m / u

            def L(a):
                return GA.add(a, GA.scal(-beta * a.get((1,), F(0)), e0))

            def Linv(a):
                return GA.add(a, GA.scal(beta * a.get((1,), F(0)), e0))

            def G(a, b):
                return GA.dot(L(a), L(b), SQ)
            ok = ok and G(e0, e0) == 1 and G(e0, e1) == -beta and G(e1, e1) == beta * beta - 1
            n_p = GA.add(e1, GA.scal(beta + 1, e0))
            n_m = GA.add(e1, GA.scal(beta - 1, e0))
            ok = ok and G(n_p, n_p) == 0 and G(n_m, n_m) == 0
            ok = ok and GA.eq(Linv(GA.add(e0, e1)), n_p) and GA.eq(Linv(GA.sub(e0, e1)), GA.neg(n_m))
    GA.check("radial dyad in GA: the gauge field maps the flat null dyad onto the physical one", ok)
    return ok
