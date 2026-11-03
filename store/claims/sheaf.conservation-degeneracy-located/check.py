"""sheaf.conservation-degeneracy-located: exact checks of the shadow wall.

Exact collar model on a transversal: G = diag(tau, G1) with G1 = diag of signature (p-1, q) (the
surviving block), e = (1, 0, ..., 0) (k(u) = 1), so s = G^{-1}(e, e) = 1/tau; ambient h on
(k, m, n0, ninf) with h(n0, ninf) = -1, h(k, n0) = nu beta, h(k, ninf) = mu beta. Physical side tau > 0
(dying eigenvalue positive). Signatures (p, q) = (1, 3), (2, 1), (2, 2), (3, 1); couplings with
mu nu > 0 and mu nu < 0; signatures by exact congruence diagonalisation (GA.congruence_signature).
(1) det h(tau), as a rational function, is det G * (-F) with F = 1 + 2 mu nu beta^2 s; off the wall its zero
    set is the zero of F, the single point tau' = -2 mu nu beta^2, simple ((det h)'(tau') != 0), with h of
    corank exactly one there.
(2) mu nu > 0: tau' < 0 (far side); h has signature (p+1, q+1) on the wall, on the physical side and on the
    far side between the wall and tau' (where the Schur block S has signature (2, 0)), and (p, q+2) beyond
    tau' (S of signature (1, 1)).
(3) mu nu < 0: h on the wall has signature (p, q+2) = ((p-1)+1, (q+1)+1), the ascent of the far side's
    (p-1, q+1); the shadow wall tau' > 0 lies on the physical side. In the Schwarzschild orientation (dying
    eigenvalue -r, manifold r > 0) the zero of F sits at r = 2 mu nu beta^2 < 0, outside the manifold.
(4) For neither sign is the signature the same at the two exteriors of a transversal (tau = +-1000).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(1, 3), (2, 1), (2, 2), (3, 1)]
COUPLINGS = [(F(2), F(3), F(1)), (F(1, 2), F(1, 3), F(2)), (F(-2), F(3), F(1)), (F(3), F(-1, 4), F(1, 2))]


def gram(p, q, mu, nu, beta, tau):
    n = p + q
    d = n + 2
    M = [[F(0)] * d for _ in range(d)]
    M[0][0] = F(tau)
    surv = [1] * (p - 1) + [-1] * q
    for a, v in enumerate(surv):
        M[1 + a][1 + a] = F(v)
    M[0][n] = M[n][0] = nu * beta
    M[0][n + 1] = M[n + 1][0] = mu * beta
    M[n][n + 1] = M[n + 1][n] = F(-1)
    return M


def det_rf(p, q, mu, nu, beta):
    t = GA.RF.var()
    M0 = gram(p, q, mu, nu, beta, 0)
    H = [[GA.RF.const(x) for x in row] for row in M0]
    H[0][0] = t
    return GA.rf_mat_det(H), t


def check_degeneracy_locus_is_the_zero_of_F():
    premise("sheaf.determinant-identity-blow-up-expansion")
    for (p, q) in SIGS:
        for (mu, nu, beta) in COUPLINGS:
            deth, t = det_rf(p, q, mu, nu, beta)
            detG = t * GA.RF.const((-1) ** q)
            s = GA.RF1 / t
            Fm = GA.RF1 + GA.RF.const(2 * mu * nu * beta * beta) * s
            assert deth.eqrf(detG * (GA.RF.const(0) - Fm))
            tau_p = -2 * mu * nu * beta * beta
            assert Fm.eval(tau_p) == 0 and deth.eval(tau_p) == 0
            assert len(deth.num) == 2 and len(deth.den) == 1         # linear: one zero only
            assert deth.deriv().eval(tau_p) != 0
            Mz = gram(p, q, mu, nu, beta, tau_p)
            assert GA.congruence_signature(Mz)[2] == 1


def schur_sig(mu, nu, beta, tau):
    b2s = beta * beta / tau
    S = [[-b2s * nu * nu, F(-1) - b2s * mu * nu], [F(-1) - b2s * mu * nu, -b2s * mu * mu]]
    return GA.congruence_signature(S)


def check_signatures_mu_nu_positive():
    premise("sheaf.wall-gram")
    for (p, q) in SIGS:
        for (mu, nu, beta) in COUPLINGS:
            if mu * nu < 0:
                continue
            tau_p = -2 * mu * nu * beta * beta
            assert tau_p < 0
            sig = lambda tau: GA.congruence_signature(gram(p, q, mu, nu, beta, tau))
            assert sig(0) == (p + 1, q + 1, 0)
            for tau in (F(5), F(1, 7), tau_p / 2, tau_p * F(99, 100)):
                assert sig(tau) == (p + 1, q + 1, 0)
            for tau in (tau_p / 2, tau_p * F(99, 100)):
                assert schur_sig(mu, nu, beta, tau) == (2, 0, 0)
            for tau in (tau_p * F(101, 100), tau_p * 2, F(-1000)):
                assert sig(tau) == (p, q + 2, 0) and schur_sig(mu, nu, beta, tau) == (1, 1, 0)


def check_signatures_mu_nu_negative_and_schwarzschild():
    premise("sheaf.wall-gram")
    for (p, q) in SIGS:
        for (mu, nu, beta) in COUPLINGS:
            if mu * nu > 0:
                continue
            tau_p = -2 * mu * nu * beta * beta
            assert tau_p > 0
            sig = lambda tau: GA.congruence_signature(gram(p, q, mu, nu, beta, tau))
            assert sig(0) == (p, q + 2, 0) == ((p - 1) + 1, (q + 1) + 1, 0)
            assert sig(tau_p / 2) == (p, q + 2, 0) and sig(F(-3)) == (p, q + 2, 0)
            assert sig(tau_p * 2) == (p + 1, q + 1, 0)
            # Schwarzschild orientation: lambda = -r, so F = 1 + 2 mu nu beta^2 / (-r) vanishes at r < 0
            r_zero = 2 * mu * nu * beta * beta
            assert r_zero < 0 and 1 + 2 * mu * nu * beta * beta / (-r_zero) == 0


def check_no_two_sided_constant_signature():
    for (p, q) in SIGS:
        for (mu, nu, beta) in COUPLINGS:
            far = GA.congruence_signature(gram(p, q, mu, nu, beta, F(-1000)))
            phys = GA.congruence_signature(gram(p, q, mu, nu, beta, F(1000)))
            assert far != phys and phys == (p + 1, q + 1, 0) and far == (p, q + 2, 0)
