"""sheaf.basic-properties-operational-characterisation: exact checks of the algebraic core.

Schwarzschild composite with 2M = m^2, u = sqrt(r) (r = u^2), beta = m/u; coordinates (t, r, theta,
phi) at the equator (sin theta = 1 enters mu_2 and e_phi reciprocally and cancels). The frame of W is
rho = u dr, dt, mu_1 = r dtheta, mu_2 = r dphi. Rational-function identities in u (GA.RF), m = 1, 2.
(1) Local freeness and rank: the frame's coefficient matrix in the coordinate coframe has
determinant u^5 (nonzero for r > 0), so W is free of rank 4 and equals the cotangent module away
from E; the frame has bounded G-norms G(rho, rho) = m^2 - r, G(dt, dt) = 1, G(mu_i, mu_i) = -1 with the
cometric computed from the Painleve-Gullstrand metric.
(2) Rain characterisation, algebraic part: the frame's rain-frame components are bounded (u^2 times
each tends to 0 at u = 0), the excluded forms dr and dtheta have divergent components; for
alpha = A du + B dt + C dtheta + D dphi the components are alpha(e_r) = A/(2u),
alpha(V) = B - m A/(2u^2), alpha(e_theta) = C/u^2, and with A = u^2 a, C = u^2 c, D = u^2 d one has
alpha = (a/2) rho + B dt + c mu_1 + d mu_2 identically (the Taylor-division step, for sample polynomial
coefficients). The analytic Taylor division itself is not reduced to a computation.
(3) rho is not smooth at order one: in u, rho = 2 u^2 du has polynomial coefficients, while the
coefficient r^(1/2) of rho = r^(1/2) dr has unbounded difference quotients at r = 1/n^2 (six n). No
polynomial p(r) satisfies p^2 = r: the r^0 and r^1 coefficients of p^2 are a0^2 and 2 a0 a1 (computed on
a grid of 215 nonzero quadratics p, none of which squares to r, each p^2 of even r-valuation), and a0^2 = 0
forces the r^1 coefficient to 0, not 1. beta u = m shows the half-integer growth of beta. That order two is
minimal is read from order one failing for this generator; that no other order-one frame is smooth is
argued in the paper, not computed.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

RF, RF0, RF1 = GA.RF, GA.RF0, GA.RF1
U = RF.var()
R = U * U


def c(x):
    return RF.const(x)


MASSES = (F(1), F(2))


def frame_rows():
    # rows: rho, dt, mu1, mu2 in the coordinate coframe (dt, dr, dtheta, dphi)
    return [[RF0, U, RF0, RF0], [RF1, RF0, RF0, RF0], [RF0, RF0, R, RF0], [RF0, RF0, RF0, R]]


def cometric(m):
    beta = c(m) / U
    return beta, [[RF1, -beta, RF0, RF0], [-beta, beta * beta - RF1, RF0, RF0],
                  [RF0, RF0, -(RF1 / (R * R)), RF0], [RF0, RF0, RF0, -(RF1 / (R * R))]]


def gform(G, a, b):
    tot = RF0
    for i in range(4):
        for j in range(4):
            tot = tot + a[i] * G[i][j] * b[j]
    return tot


def check_free_of_rank_four_with_bounded_norms():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    det = GA.rf_mat_det(frame_rows())
    ok = ok and (det.eqrf(U * R * R) or det.eqrf(-(U * R * R)))
    ok = ok and det.eval(F(1, 3)) != 0 and det.eval(F(0)) == 0
    for m in MASSES:
        beta, G = cometric(m)
        # cometric = inverse of the PG metric block [[1 - beta^2, -beta], [-beta, -1]]
        gt = [[RF1 - beta * beta, -beta], [-beta, c(-1)]]
        prod = [[gt[i][0] * G[0][j] + gt[i][1] * G[1][j] for j in range(2)] for i in range(2)]
        ok = ok and prod[0][0].eqrf(RF1) and prod[1][1].eqrf(RF1) and prod[0][1].is_zero() and prod[1][0].is_zero()
        rho, dt, mu1, mu2 = frame_rows()
        ok = ok and gform(G, rho, rho).eqrf(c(m * m) - R) and gform(G, dt, dt).eqrf(RF1)
        ok = ok and gform(G, mu1, mu1).eqrf(c(-1)) and gform(G, mu2, mu2).eqrf(c(-1))
        ok = ok and gform(G, rho, dt).eqrf(c(-m))
    GA.check("W: free of rank four (determinant u^5), all of T*M off E, frame norms bounded", ok)
    return ok


def check_rain_characterisation_algebra():
    premise("sheaf.rain-duality")
    ok = True
    for m in MASSES:
        beta = c(m) / U
        V, er, eth, eph = [RF1, -beta, RF0, RF0], [RF0, RF1, RF0, RF0], [RF0, RF0, RF1 / R, RF0], [RF0, RF0, RF0, RF1 / R]
        frame = [V, er, eth, eph]

        def ev(a, X):
            tot = RF0
            for i in range(4):
                tot = tot + a[i] * X[i]
            return tot
        rho, dt, mu1, mu2 = frame_rows()
        table = {(0, 0): c(-m), (0, 1): U, (1, 0): RF1, (2, 2): RF1, (3, 3): RF1}
        for i, a in enumerate((rho, dt, mu1, mu2)):
            for j, X in enumerate(frame):
                val = ev(a, X)
                ok = ok and val.eqrf(table.get((i, j), RF0))
        ok = ok and (U * ev([RF0, RF1, RF0, RF0], V)).eval(F(0)) == -m          # dr(V) ~ -m/u
        ok = ok and (R * ev([RF0, RF0, RF1, RF0], eth)).eval(F(0)) == 1           # dtheta(e_theta) ~ 1/r
        # general alpha = A du + B dt + C dtheta + D dphi, du = dr/(2u)
        A, B, C, D = c(F(3)) + U, c(F(-1)) + R, c(F(2)) - U, U * c(F(5))
        alpha = [B, A / (c(2) * U), C, D]
        ok = ok and ev(alpha, er).eqrf(A / (c(2) * U))
        ok = ok and ev(alpha, V).eqrf(B - c(m) * A / (c(2) * R))
        ok = ok and ev(alpha, eth).eqrf(C / R)
        # Taylor division: A = u^2 a, C = u^2 cc, D = u^2 d gives alpha = (a/2) rho + B dt + cc mu1 + d mu2
        a, cc, d = c(F(2)) + U, c(F(-3)) + U * U, c(F(1, 2))
        alpha2 = [B, R * a / (c(2) * U), R * cc, R * d]
        combo = [B, (a / c(2)) * U, cc * R, d * R]
        ok = ok and (len(alpha2) == len(combo) and all(x.eqrf(y) for x, y in zip(alpha2, combo)))
    GA.check("W: bounded rain components of the frame, divergent coordinate forms, component formulas", ok)
    return ok


NS = (1, 2, 3, 5, 8, 13)


def check_rho_not_smooth_at_order_one():
    ok = True
    # in u: rho = u dr = u (2u du) = 2 u^2 du, a polynomial coefficient vanishing to order two
    rho_du = U * (c(2) * U)
    ok = ok and rho_du.eqrf(c(2) * R) and rho_du.den == [F(1)] and rho_du.num == [F(0), F(0), F(2)]
    # in r: the coefficient r^(1/2) of rho = r^(1/2) dr has difference quotients r^(1/2)/r = n at r = 1/n^2,
    # unbounded, so it is not differentiable at r = 0; the u-coefficient 2u^2 has quotient 2u -> 0
    quot = []
    for n in NS:
        r, sqrt_r = F(1, n * n), F(1, n)
        ok = ok and sqrt_r * sqrt_r == r
        quot.append(sqrt_r / r)
        ok = ok and rho_du.eval(F(1, n)) / F(1, n) == F(2, n)
    ok = ok and quot == [F(n) for n in NS] and all(quot[i] < quot[i + 1] for i in range(len(NS) - 1))
    # beta = m/u: beta u = m, so beta grows like r^(-1/2) (half-integer order)
    for m in MASSES:
        ok = ok and ((c(m) / U) * U).eqrf(c(m)) and (c(m) / U).den == [F(0), F(1)]
    # no polynomial square root of r: low coefficients of p^2 and the parity of its r-valuation
    vals = (F(-2), F(-1), F(0), F(1, 2), F(1), F(3))
    count = 0
    for a0 in vals:
        for a1 in vals:
            for a2 in vals:
                pp = GA.ptrim([a0, a1, a2])
                if not pp:
                    continue
                sq = GA.pmul(pp, pp) + [F(0), F(0)]
                ok = ok and sq[0] == a0 * a0 and sq[1] == 2 * a0 * a1
                ok = ok and GA.ptrim(sq[:]) != [F(0), F(1)]
                ok = ok and next(i for i, x in enumerate(sq) if x != 0) % 2 == 0
                ok = ok and (a0 != 0 or sq[1] == 0)
                count += 1
    ok = ok and count == 215
    GA.check("W: rho = 2u^2 du smooth in u; r^(1/2) not smooth in r, no polynomial square root of r", ok)
    return ok
