"""sheaf.determinant-identity-blow-up-expansion: exact checks of the determinant identity and the
blow-up expansion, as identities of rational functions in the transversal parameter tau (GA.RF).

Collar models in a frame (k, m_1, ..., m_{n-1}) of T*M extended by (n0, ninf): G has k-row
(lambda(tau), b(tau)) with lambda(0) = 0, b(0) = 0 (the radical k at tau = 0), a tau-dependent surviving
block G1, and e = evaluation at u with k(u) = 1 and nonzero tangential parts. The ambient Gram h is G on
T*M, h(n0, ninf) = -1, h(alpha, n0) = nu beta e(alpha), h(alpha, ninf) = mu beta e(alpha). Three models
(n = 4, 4, 3; diagonal and non-diagonal G1, lambda'(0) = 1, 3, -2) and four couplings (mu, nu, beta),
including mu nu < 0.
(1) s = G^{-1}(e, e) is computed by solving G x = e; the Schur complement D - C G^{-1} C^T of the G-block
    equals [[0, -1], [-1, 0]] - beta^2 s [[nu^2, mu nu], [mu nu, mu^2]] entrywise, its determinant is
    -(1 + 2 mu nu beta^2 s), and det h = det G * (-(1 + 2 mu nu beta^2 s)) exactly.
(2) tau s at tau = 0 equals 1/lambda'(0); s - 1/lambda has no pole at tau = 0 (it is O(1)); s > 0 just on
    the side where lambda > 0 and s < 0 on the other (tau = +-1/1000).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401 (the claim has no premises)

R = GA.RF.const
T = GA.RF.var()
Z = GA.RF0


def model(i):
    if i == 0:
        lam = T + R(2) * T * T
        b = [R(3) * T, T * T, Z]
        G1 = [[R(-1), Z, Z], [Z, R(-1), Z], [Z, Z, R(-1) + T]]
        e = [R(1), R(F(1, 2)), Z, Z]
    elif i == 1:
        lam = R(3) * T - T * T
        b = [T, Z, R(2) * T]
        G1 = [[R(-1), R(F(1, 2)), Z], [R(F(1, 2)), R(-2) + T * T, Z], [Z, Z, R(1)]]
        e = [R(1), Z, R(F(1, 3)), R(-1)]
    else:
        lam = R(-2) * T + R(5) * T * T * T
        b = [T * T, R(-1) * T]
        G1 = [[R(-1), T], [T, R(-3)]]
        e = [R(1), R(2), R(F(-1, 2))]
    n = len(e)
    G = [[lam] + b] + [[b[i]] + G1[i] for i in range(n - 1)]
    return G, e, lam


COUPLINGS = [(F(2), F(3), F(1)), (F(2), F(3), F(1, 2)), (F(-1), F(5), F(2, 3)), (F(1, 2), F(-4), F(3))]


def gram_h(G, e, mu, nu, beta):
    n = len(e)
    h = [[Z] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            h[i][j] = G[i][j]
        h[i][n] = h[n][i] = R(nu * beta) * e[i]
        h[i][n + 1] = h[n + 1][i] = R(mu * beta) * e[i]
    h[n][n + 1] = h[n + 1][n] = R(-1)
    return h


def s_of(G, e):
    x = GA.rf_mat_solve(G, e)
    s = Z
    for i in range(len(e)):
        s = s + e[i] * x[i]
    return s, x


def check_schur_complement_and_determinant_identity():
    for i in range(3):
        G, e, lam = model(i)
        n = len(e)
        s, x = s_of(G, e)
        detG = GA.rf_mat_det(G)
        assert not detG.is_zero()
        for (mu, nu, beta) in COUPLINGS:
            h = gram_h(G, e, mu, nu, beta)
            C = [[h[n + a][j] for j in range(n)] for a in range(2)]
            Ginv_Ct = [GA.rf_mat_solve(G, [C[a][j] for j in range(n)]) for a in range(2)]
            schur = [[h[n + a][n + c] - sum((C[a][j] * Ginv_Ct[c][j] for j in range(n)), Z)
                      for c in range(2)] for a in range(2)]
            b2 = R(beta * beta) * s
            want = [[R(0) - b2 * R(nu * nu), R(-1) - b2 * R(mu * nu)],
                    [R(-1) - b2 * R(mu * nu), R(0) - b2 * R(mu * mu)]]
            assert all(schur[a][c].eqrf(want[a][c]) for a in range(2) for c in range(2))
            detS = schur[0][0] * schur[1][1] - schur[0][1] * schur[1][0]
            Fm = GA.RF1 + R(2 * mu * nu * beta * beta) * s
            assert detS.eqrf(R(0) - Fm)
            assert GA.rf_mat_det(h).eqrf(detG * (R(0) - Fm))


# sample points just either side of the radical at tau = 0
SIDE_TAUS = (F(1, 1000), F(-1, 1000))


def sign(x):
    """Sign of a rational: 1, 0 or -1."""
    return (x > 0) - (x < 0)


def check_blow_up_expansion():
    for i, lam_prime0 in enumerate((F(1), F(3), F(-2))):
        G, e, lam = model(i)
        s, x = s_of(G, e)
        assert lam.deriv().eval(0) == lam_prime0
        assert (T * s).eval(0) == 1 / lam_prime0
        rem = s - GA.RF1 / lam
        # s - 1/lambda has no pole at tau = 0: tau (s - 1/lambda) vanishes there (it raises on a double pole
        # and is nonzero on a simple one)
        assert (T * rem).eval(0) == 0
        for tau in SIDE_TAUS:
            assert sign(s.eval(tau)) == sign(lam.eval(tau))
            assert sign(s.eval(tau)) == sign(tau) * sign(lam_prime0)
