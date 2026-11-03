"""synthesis.dimmed-burst-time-rescaled-copy: exact checks.

check_mass_loss_law: a hole of mass M emitting in channels whose flux per unit energy depends on
  M and E only through x = M E (greybody inheritance, T_H = 1/(8 pi M)) loses mass at
  P(M) = M^-2 * int x phi(x) dx: tested with polynomial flux shapes of compact support in x,
  exactly, at several M; adding towers multiplies the constant by rho.
check_time_rescaling: with M_rho(t)^3 = 3 alpha rho t (t the remaining lifetime), for visible
  emission h(E, M) built from powers of M^3 (so that the time integral is exact), the visible count
  in the last tau equals (1/rho) times the undimmed count in the last rho tau; the visible energy
  in the last tau scales as rho^(-2/3) (checked on cubes), the temperature at fixed remaining time
  as rho^(-1/3) (on cubes), and for a primary flux h(M E) of compact support the high-energy tail
  is tau-independent and scales as 1/rho.
check_mirror_floor: with the mirror's emission coefficient equal to ours, g the gravitational and o
  the odd towers' coefficients relative to ours, the dimming ratio against the standard expectation
  (this tower plus gravitons) is D = (2 + g + o)/(1 + g), at least 2 iff o >= g, and 2 - g/(1 + g)
  for o = 0. check_time_rescaling also runs the identity with a graviton term in the baseline.
"""
from fractions import Fraction as F
import GA
from GA import pmul, padd, pconst, peval
from tp_premise import premise


def pint(p, lo, hi):
    """Exact integral of a polynomial (coefficient list) from lo to hi."""
    tot = F(0)
    for k, c in enumerate(p):
        tot += c * (F(hi) ** (k + 1) - F(lo) ** (k + 1)) / (k + 1)
    return tot


def check_mass_loss_law():
    premise("hawking.greybody-inheritance-under-interface-premise")
    premise("dark-matter.parallel-boundary-mode-spaces-one-wall")
    shapes = [[F(0), F(0), F(1), F(-2), F(1)],          # x^2 (1 - x)^2 on [0, 1]
              [F(0), F(3), F(-1, 2)],                     # 3x - x^2/2 on [0, 1]
              [F(0), F(0), F(0), F(1), F(-1)]]            # x^3 (1 - x) on [0, 1]
    for phi in shapes:
        xphi = pmul([F(0), F(1)], phi)
        const = pint(xphi, 0, 1)
        assert const > 0
        for M in (F(1), F(2), F(3, 2), F(5, 7)):
            # P(M) = int_0^{1/M} E phi(M E) dE, substituting the polynomial in E
            phiE = [c * M ** k for k, c in enumerate(phi)]
            P = pint(pmul([F(0), F(1)], phiE), 0, 1 / M)
            assert P * M ** 2 == const
            for rho in (F(2), F(3)):
                assert rho * P * M ** 2 == rho * const
    GA.check("mass loss P(M) = c / M^2 for every flux shape in M E; towers multiply c by rho", True)
    return True


def visible_count(coeffs, E, rho, alpha, tau):
    """int_0^tau h(E, M_rho(t)) dt with h = sum_k coeffs[k](E) M^(3k), M^3 = 3 alpha rho t."""
    tot = F(0)
    for k, ck in enumerate(coeffs):
        tot += ck(E) * (3 * alpha * rho) ** k * F(tau) ** (k + 1) / (k + 1)
    return tot


def check_time_rescaling():
    premise("hawking.greybody-inheritance-under-interface-premise")
    premise("dark-matter.parallel-boundary-mode-spaces-one-wall")
    coeffs = [lambda E: E * E, lambda E: -3 * E, lambda E: F(2, 5) + E ** 3]
    for rho in (F(2), F(3), F(7, 2)):
        for alpha in (F(1), F(5, 3)):
            for tau in (F(1), F(2, 7)):
                for E in (F(1), F(4, 3)):
                    lhs = visible_count(coeffs, E, rho, alpha, tau)
                    rhs = visible_count(coeffs, E, F(1), alpha, rho * tau) / rho
                    assert lhs == rhs
                    assert visible_count(coeffs, E, rho, alpha, tau) != visible_count(coeffs, E, F(1), alpha, tau) / rho
    # baseline with gravitons: rho_0 = 1 + g; N_rho(E; tau) = (rho_0/rho) N_rho0(E; (rho/rho_0) tau)
    for rho0, rho in ((F(101, 100), F(2)), (F(21, 20), F(5, 2))):
        for alpha in (F(1), F(5, 3)):
            for tau in (F(1), F(2, 7)):
                for E in (F(1), F(4, 3)):
                    lhs = visible_count(coeffs, E, rho, alpha, tau)
                    rhs = visible_count(coeffs, E, rho0, alpha, rho / rho0 * tau) * rho0 / rho
                    assert lhs == rhs
    assert visible_count(coeffs, F(1), F(2), F(1), F(1)) == \
        visible_count(coeffs, F(1), F(101, 100), F(1), F(200, 101)) * F(101, 200)
    for rho, alpha, tau, E, val, naive in ((F(2), F(1), F(1), F(1), F(44, 5), F(7, 20)),
                                           (F(3), F(5, 3), F(2, 7), F(4, 3), F(8968, 3087), F(6392, 83349))):
        assert visible_count(coeffs, E, rho, alpha, tau) == val
        assert visible_count(coeffs, E, F(1), alpha, rho * tau) / rho == val
        assert visible_count(coeffs, E, F(1), alpha, tau) / rho == naive
    for rho in (F(8), F(27), F(2)):
        for alpha in (F(1), F(1, 3)):
            tau = F(5)
            M1cube = 3 * alpha * tau
            Mrcube = 3 * alpha * rho * tau
            # visible energy in the last tau is M(tau)/rho; its ratio to the undimmed value, cubed
            ratio_cubed = (Mrcube / rho ** 3) / M1cube
            assert ratio_cubed == 1 / rho ** 2
            # temperature is proportional to 1/M: ratio cubed
            assert M1cube / Mrcube == 1 / rho
    # tail of a primary flux h(M E) supported on M E <= 1: N(E; tau) = (1/(alpha E^3)) int_0^{E M(tau)} h(x) x^2 dx
    h = [F(1), F(-1)]                                     # h(x) = 1 - x on [0, 1]
    full = pint(pmul(h, [F(0), F(0), F(1)]), 0, 1)
    assert full == F(1, 12)
    def tail_count(E, alpha, rho, Mtop):
        """(1/(alpha rho)) int_0^{Mtop} h(E M) M^2 dM, h supported on E M <= 1."""
        top = min(Mtop, 1 / E)
        hE = [c * E ** k for k, c in enumerate(h)]
        return pint(pmul(hE, [F(0), F(0), F(1)]), 0, top) / (alpha * rho)
    for alpha in (F(1), F(2)):
        for E in (F(3), F(5, 2)):
            for rho in (F(1), F(2), F(5)):
                vals = {tail_count(E, alpha, rho, M) for M in (F(1), F(2), F(7, 3))}
                assert vals == {full / (alpha * rho * E ** 3)}
            assert tail_count(E, alpha, F(1), F(1, 2) / E) < full / (alpha * E ** 3)
    GA.check("time rescaling: N_rho(E; tau) = N_1(E; rho tau)/rho; window energy rho^(-2/3); "
             "temperature rho^(-1/3); primary tail 1/rho", True)
    return True


def check_mirror_floor():
    premise("dark-matter.mirror-tower-copy-one")
    premise("dark-matter.parallel-boundary-mode-spaces-one-wall")
    # g = Psi_grav/Psi_vis, o = Psi_odd/Psi_vis: dimming ratio against the standard-model
    # expectation (gravitons included) is rho/rho_0 = (2 + g + o)/(1 + g)
    table = [(F(0), F(0), F(2)), (F(1, 100), F(0), F(201, 101)), (F(1, 100), F(1, 100), F(2)),
             (F(1, 50), F(1, 2), F(42, 17))]
    for g, o, rx in table:
        ratio = (2 + g + o) / (1 + g)
        assert ratio == rx
        assert (ratio >= 2) == (o >= g)
        assert ratio == 2 + (o - g) / (1 + g)
    # with o = 0 the floor is 2 - g/(1 + g)
    for g in (F(1, 100), F(3, 200)):
        assert (2 + g) / (1 + g) == 2 - g / (1 + g) and (2 + g) / (1 + g) < 2
    GA.check("mirror floor relative to the graviton baseline: (2 + g + o)/(1 + g), >= 2 iff o >= g", True)
    return True
