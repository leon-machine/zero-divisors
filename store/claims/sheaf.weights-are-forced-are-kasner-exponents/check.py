"""sheaf.weights-are-forced-are-kasner-exponents: exact checks in Gauge Theory Gravity.

The Schwarzschild interior gravitational field (2M = 1, 0 < r < 1) in the static (Schwarzschild-coordinate)
gauge on flat Cl(1,3) (GA.py, (+,-,-,-)) with labels (r, t, theta, phi): hb^{-1}(e_r) = gamma0/sqrt(-f),
hb^{-1}(e_t) = sqrt(-f) gamma1, hb^{-1}(e_theta) = r gamma2, hb^{-1}(e_phi) = r sin(theta) gamma3,
f = 1 - 1/r, at rational points with sqrt(-f), sin, cos rational. The derived cometric on the coordinate
coframe is G(e^mu, e^nu) = g^mu . g^nu with the reciprocal physical frame g^mu = hb^T(e^mu). Computed:
(1) G = diag((1 - r)/r, -r/(1 - r), -1/r^2, -1/(r^2 sin^2)) at every sample; hence r G_rr = 1 - r,
    G_tt/r = -1/(1 - r), r^2 G_thth = -1: the entries have exact orders (-1, +1, -2) at r = 0 with
    nonzero leading coefficients (1, -1, -1);
(2) the rescaled entries r^{2 a_i} G_ii have orders 2 a_i + (-1, 1, -2); over the half-integer grid
    a_i in {-2, ..., 2} (729 triples) the continuous extensions with a corank-one limit whose dying entry is
    the Killing-time entry at first order are exactly (1/2, 0, 1); the nondegenerate ones exactly
    (1/2, -1/2, 1); with the radial entry dying at first order instead, exactly (1, -1/2, 1); the orders are
    affine in a with invertible linear part, so each profile has one solution in all of Q^3;
(3) in proper time tau ~ r^{3/2} (the radial weight 1/2 makes r^{1/2} dr = d((2/3) r^{3/2})) the exceptional
    weights (-1/2, 1, 1) on (dt, dtheta, dphi) are the Kasner exponents (2/3)(-1/2, 1, 1) =
    (-1/3, 2/3, 2/3), with sum p = sum p^2 = 1.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
KS = [F(1, 2), F(1), F(2), F(1, 3)]                    # sqrt(-f) = 1/k at r = k^2/(1 + k^2)
ANG = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]
HALF = [F(k, 2) for k in range(-4, 5)]
ORDERS = (-1, 1, -2)


def cometric(k, s0):
    r = k * k / (1 + k * k)
    smf = 1 / k                                         # sqrt(-f) = sqrt((1 - r)/r)
    diag = [1 / smf, smf, r, r * s0]                    # hb^{-1}(e_mu) = diag[mu] gamma_mu
    g_up = [GA.scal(F(1) / (diag[m] * S13[m]), GA.gen(m)) for m in range(4)]
    g_dn = [GA.scal(diag[m], GA.gen(m)) for m in range(4)]
    ok = all(GA.dot(g_dn[m], g_up[n], S13) == (1 if m == n else 0) for m in range(4) for n in range(4))
    return r, [[GA.dot(g_up[m], g_up[n], S13) for n in range(4)] for m in range(4)], ok


def check_cometric_and_its_orders():
    ok = True
    for k in KS:
        for s0, c0 in ANG:
            r, G, dual = cometric(k, s0)
            ok = ok and dual
            want = [(1 - r) / r, -r / (1 - r), -1 / (r * r), -1 / (r * r * s0 * s0)]
            ok = ok and all(G[m][n] == (want[m] if m == n else 0) for m in range(4) for n in range(4))
            ok = ok and r * G[0][0] == 1 - r and G[1][1] / r == -1 / (1 - r) and r * r * G[2][2] == -1
    _tp_rv = (ok); assert _tp_rv is not False, "check_cometric_and_its_orders"; return _tp_rv


def profile(a):
    """Orders of the rescaled (r, t, theta) entries."""
    return tuple(2 * ai + e for ai, e in zip(a, ORDERS))


def check_weights_forced_per_profile():
    premise("sheaf.exceptional-algebra-black-hole")
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    sols = {"dying_t": [], "nondeg": [], "dying_r": []}
    for ar in HALF:
        for at in HALF:
            for ath in HALF:
                o = profile((ar, at, ath))
                if o == (0, 1, 0):
                    sols["dying_t"].append((ar, at, ath))
                if o == (0, 0, 0):
                    sols["nondeg"].append((ar, at, ath))
                if o == (1, 0, 0):
                    sols["dying_r"].append((ar, at, ath))
    ok = sols == {"dying_t": [(F(1, 2), 0, 1)], "nondeg": [(F(1, 2), F(-1, 2), 1)], "dying_r": [(1, F(-1, 2), 1)]}
    lin = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
    _tp_rv = (ok and GA.mat_rank(lin) == 3); assert _tp_rv is not False, "check_weights_forced_per_profile"; return _tp_rv


def check_exceptional_weights_are_kasner_exponents():
    premise("sheaf.kasner-data-interior")
    a_r, weights = F(1, 2), (F(-1, 2), F(1), F(1))
    tau_exponent = a_r + 1                              # r^{1/2} dr = d((2/3) r^{3/2})
    p = tuple(w / tau_exponent for w in weights)
    _tp_rv = (tau_exponent == F(3, 2) and p == (F(-1, 3), F(2, 3), F(2, 3)) and sum(p) == 1 and sum(x * x for x in p) == 1); assert _tp_rv is not False, "check_exceptional_weights_are_kasner_exponents"; return _tp_rv
