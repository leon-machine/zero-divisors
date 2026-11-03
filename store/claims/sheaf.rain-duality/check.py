"""sheaf.rain-duality: exact checks, as rational-function identities in u = sqrt(r) at two masses (2M = m^2,
m = 1, 3), at the equator (sin theta enters mu2 and e_phi reciprocally and cancels in every pairing used).

Coordinates (t, r, theta, phi); PG cometric G; rain frame V = d_t - beta d_r, e_r = d_r, e_theta = d_theta / r,
e_phi = d_phi / r, beta = m/u.
(1) The coframe (dt, k/sqrt r, mu1, mu2), k/sqrt r = dr + beta dt, pairs with (V, e_r, e_theta, e_phi) to the
identity matrix at every radius; in particular (k/sqrt r)(V) = 0 (the rain identity of the premise).
(2) Its G-Gram is exactly diag(1, -1, -1, -1), and G(k/sqrt r, k/sqrt r) = g_k / r = -1.
(3) Membership: for alpha = A du + B dt + C' dtheta + D' sin dphi, the rain components are A/(2u),
B - m A/(2u^2), C'/u^2, D'/u^2 (computed from the coordinate pairings, du = dr/(2u)); for every monomial
coefficient u^j (j = 0..3) in every slot, the components are bounded at u = 0 exactly when the coefficient of alpha
on the W-frame (rho = 2u^2 du, dt, mu1 = u^2 dtheta, mu2 = u^2 sin dphi) is a polynomial, i.e. exactly when
alpha lies in W. The norm identity |alpha|^2 = alpha(V)^2 - sum alpha(e_i)^2 holds for five covectors; the
covector (k/sqrt r - dt)/u has norm identically 0 yet unbounded rain components (a bounded norm does not give
membership); dr(V) = -m/u and dtheta(e_theta) = 1/r diverge.
(4) rho = u (k/sqrt r) - m dt; the W -> W_exc transition has determinant -u; the coefficients of a covector on
the coframe are its rain components (exact solve); the W_exc Gram at the boundary is the nondegenerate Minkowski
form of the exceptional regime.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

U = GA.RF.var()
R = U * U
MASSES = (F(1), F(3))


def C(x):
    return GA.RF.const(F(x))


def setup(m):
    beta = C(m) / U
    Z, O = GA.RF0, GA.RF1
    G = [[O, -beta, Z, Z],
         [-beta, (C(m * m) - R) / R, Z, Z],
         [Z, Z, -(O / (R * R)), Z],
         [Z, Z, Z, -(O / (R * R))]]
    frame = [[O, -beta, Z, Z], [Z, O, Z, Z], [Z, Z, O / R, Z], [Z, Z, Z, O / R]]
    cof = {"dt": [O, Z, Z, Z], "kou": [beta, O, Z, Z], "mu1": [Z, Z, R, Z], "mu2": [Z, Z, Z, R],
           "rho": [Z, U, Z, Z], "dr": [Z, O, Z, Z], "dth": [Z, Z, O, Z]}
    return G, frame, cof


def pair(a, X):
    acc = GA.RF0
    for i in range(4):
        acc = acc + a[i] * X[i]
    return acc


def gform(G, a, b):
    acc = GA.RF0
    for i in range(4):
        for j in range(4):
            if not G[i][j].is_zero():
                acc = acc + a[i] * G[i][j] * b[j]
    return acc


def bounded(f):
    try:
        f.eval(F(0))
        return True
    except ZeroDivisionError:
        return False


def check_dual_coframe_of_rain_frame():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        G, frame, cof = setup(m)
        coframe = [cof["dt"], cof["kou"], cof["mu1"], cof["mu2"]]
        for i in range(4):
            for j in range(4):
                ok = ok and pair(coframe[i], frame[j]).eqrf(GA.RF1 if i == j else GA.RF0)
        # the rain identity: k = u (k/sqrt r) annihilates V at every radius
        ok = ok and (U * pair(cof["kou"], frame[0])).is_zero()
    GA.check("(dt, k/sqrt r, mu1, mu2) is the dual coframe of the rain frame at every radius", ok)
    return ok


def check_minkowski_gram_at_every_radius():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    eta = [1, -1, -1, -1]
    for m in MASSES:
        G, frame, cof = setup(m)
        coframe = [cof["dt"], cof["kou"], cof["mu1"], cof["mu2"]]
        for i in range(4):
            for j in range(4):
                ok = ok and gform(G, coframe[i], coframe[j]).eqrf(C(eta[i]) if i == j else GA.RF0)
        k = [cof["kou"][i] * U for i in range(4)]
        ok = ok and gform(G, k, k).eqrf(-R) and (gform(G, k, k) / R).eqrf(C(-1))
        # the rain frame is G-orthonormal as vectors (covariant PG metric at the equator)
        beta = C(m) / U
        gcov = [[GA.RF1 - beta * beta, -beta, GA.RF0, GA.RF0], [-beta, C(-1), GA.RF0, GA.RF0],
                [GA.RF0, GA.RF0, -(R * R), GA.RF0], [GA.RF0, GA.RF0, GA.RF0, -(R * R)]]
        for i in range(4):
            for j in range(4):
                ok = ok and gform(gcov, frame[i], frame[j]).eqrf(C(eta[i]) if i == j else GA.RF0)
    GA.check("the rain coframe has Gram exactly diag(1,-1,-1,-1) at every radius; g_k / r = -1", ok)
    return ok


def components(m, A, B, Cp, Dp):
    """Rain components of A du + B dt + C' dtheta + D' sin dphi; du = dr/(2u)."""
    G, frame, cof = setup(m)
    alpha = [B, A / (C(2) * U), Cp, Dp]          # coordinate components on (dt, dr, dtheta, sin dphi)
    return [pair(alpha, frame[j]) for j in range(4)], alpha, G, frame


def check_membership_iff_bounded_rain_components():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        # the component formulas, for generic symbolic slots (each coefficient a separate monomial test below)
        A, B, Cp, Dp = C(2) + U, C(-1) + R, C(3) * U, C(5)
        comps, alpha, G, frame = components(m, A, B, Cp, Dp)
        ok = ok and comps[1].eqrf(A / (C(2) * U)) and comps[0].eqrf(B - C(m) * A / (C(2) * R))
        ok = ok and comps[2].eqrf(Cp / R) and comps[3].eqrf(Dp / R)
        # monomial scan: slot s carries u^j, others zero
        for slot in range(4):
            for j in range(4):
                coeffs = [GA.RF0] * 4
                mono = GA.RF1
                for _ in range(j):
                    mono = mono * U
                coeffs[slot] = mono
                comps, _, _, _ = components(m, *coeffs)
                is_bounded = all(bounded(c) for c in comps)
                # W-coefficients: A = 2u^2 a_rho, B = b_dt, C' = u^2 c1, D' = u^2 c2
                wcoef = [coeffs[0] / (C(2) * R), coeffs[1], coeffs[2] / R, coeffs[3] / R]
                in_w = all(len(w.den) == 1 for w in wcoef)
                expected = (j >= 2) if slot != 1 else True
                ok = ok and is_bounded == in_w == expected
        # the norm identity, five covectors
        _, frame, cof = setup(m)
        tests = [cof["rho"], cof["dt"], cof["mu1"], cof["kou"],
                 [cof["rho"][i] + C(2) * cof["dt"][i] + C(3) * cof["mu1"][i] for i in range(4)]]
        for a in tests:
            rhs = pair(a, frame[0]) * pair(a, frame[0])
            for j in (1, 2, 3):
                rhs = rhs - pair(a, frame[j]) * pair(a, frame[j])
            ok = ok and gform(G, a, a).eqrf(rhs)
        # bounded norm without membership: (k/sqrt r - dt)/u is null with components (1/u)(-1, 1, 0, 0)
        nm = [(cof["kou"][i] - cof["dt"][i]) / U for i in range(4)]
        ok = ok and gform(G, nm, nm).is_zero()
        ok = ok and pair(nm, frame[0]).eqrf(C(-1) / U) and pair(nm, frame[1]).eqrf(GA.RF1 / U)
        ok = ok and not bounded(pair(nm, frame[1]))
        # the excluded coordinate forms diverge
        ok = ok and pair(cof["dr"], frame[0]).eqrf(C(-m) / U)
        ok = ok and pair(cof["dth"], frame[2]).eqrf(GA.RF1 / R)
    GA.check("a u-smooth form is in W iff its rain components are bounded; a bounded norm is not enough", ok)
    return ok


def check_exceptional_module_and_transition():
    premise("sheaf.exceptional-algebra-black-hole")
    ok = True
    for m in MASSES:
        G, frame, cof = setup(m)
        ok = ok and all((U * cof["kou"][i] - C(m) * cof["dt"][i]).eqrf(cof["rho"][i]) for i in range(4))
        # transition: W-frame (rho, dt, mu1, mu2) on the W_exc frame (dt, k/sqrt r, mu1, mu2)
        T = [[C(-m), U, GA.RF0, GA.RF0], [GA.RF1, GA.RF0, GA.RF0, GA.RF0],
             [GA.RF0, GA.RF0, GA.RF1, GA.RF0], [GA.RF0, GA.RF0, GA.RF0, GA.RF1]]
        ok = ok and GA.rf_mat_det(T).eqrf(-U)
        # coefficients on the coframe equal rain components: solve coframe^T c = alpha
        coframe = [cof["dt"], cof["kou"], cof["mu1"], cof["mu2"]]
        alpha = [C(2) + U, C(3) / U, R, C(-7)]
        M = [[coframe[j][i] for j in range(4)] for i in range(4)]
        c = GA.rf_mat_solve(M, alpha)
        ok = ok and all(c[j].eqrf(pair(alpha, frame[j])) for j in range(4))
        # the exceptional regime's rescaled frame (rho, k/sqrt r, mu1, mu2) at the boundary: diag(m^2, -1, -1, -1)
        ex = [cof["rho"], cof["kou"], cof["mu1"], cof["mu2"]]
        Gex = [[gform(G, ex[i], ex[j]).eval(F(0)) for j in range(4)] for i in range(4)]
        ok = ok and Gex == [[m * m, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
        ok = ok and GA.congruence_signature(Gex) == (1, 3, 0)
    GA.check("rho = sqrt r (k/sqrt r) - m dt, transition det -sqrt r; coframe coefficients are rain components", ok)
    return ok
