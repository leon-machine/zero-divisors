"""scrambling.imported-collars-coframe-exceptional-set-helicity: exact checks of the computable part.

Flat background Cl(1,3) (GA.py, (+,-,-,-)), 2M = 1 (r_h = 1). The Schwarzschild interior field comes from the
premise check interior.interior-connection-exactly (EXPORTS; labels (r, t, theta, phi), hb^{-1}(e_t) =
sqrt(A) gamma1, A = (1 - r)/r, hb^{-1}(e_theta) = r gamma2, hb^{-1}(e_phi) = r sin(theta) gamma3; exact
values at rational points). The coframe is the component set theta^a(v) = gamma^a . hb^{-1}(v). Computed:
(1) the weighted coframe: (r^{1/2} sqrt(A))^2 = 1 - r and r^{-1} . r = 1 at every sample, so the weights
    r^{1/2}, r^{-1}, r^{-1} make the coframe (sqrt(A) dt, r dtheta, r sin dphi) tend to (dt, dtheta,
    sin dphi), which is (dt, r_h dtheta, r_h sin dphi) at r_h = 1; the orders of the coframe entries in r
    are (-1/2, 1, 1);
(2) with proper time tau ~ r^{3/2} (the interior series tau = (2/3) r^{3/2}(1 + O(r))) the orders become the
    Kasner exponents (2/3)(-1/2, 1, 1) = (-1/3, 2/3, 2/3);
(3) the homogeneities -2s - 2 of the two helicities: -4 and 0 for the photon (s = +1, -1), -6 and +2 for the
    graviton (s = +2, -2), distinct within each species.
The channel identification J3 is a modelling joint of T7 and is not computable.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13


def m_val(x):
    """Values of a jet multivector. Local (not gtg.m_val) because the fields come from the premise's EXPORTS,
    whose jets may be the premise's own class until that check is migrated."""
    return {b: c.v for b, c in x.items() if c.v != 0}
# ---- end of engine ----


# ---- exact series of the Schwarzschild interior (2M = 1) in u = sqrt(r) ----
NS = 8


def interior_series(N=NS):
    """tau(u) = int_0^r sqrt(s/(1-s)) ds = int 2 v^2 (1 - v^2)^{-1/2} dv; returns (tau, tau sigma_1,
    tau sigma_2, R/u^2, tau/r) as coefficient lists in u, with sigma_1 = -(1/2) r^{-3/2} (1 - r)^{-1/2},
    sigma_2 = r^{-3/2} (1 - r)^{1/2}, R = (3 tau/2)^{2/3}."""
    w = GA.ps_pow_rat([F(1), F(0), F(-1)], F(-1, 2), N)
    tau = GA.ps_int(GA.ps_mul([F(0), F(0), F(2)], w, N))
    t3 = GA.ps_trunc(tau[3:], N)
    ts1 = [-c / 2 for c in GA.ps_mul(w, t3, N)]
    ts2 = GA.ps_mul(GA.ps_pow_rat([F(1), F(0), F(-1)], F(1, 2), N), t3, N)
    Ru2 = GA.ps_pow_rat([F(3, 2) * c for c in t3], F(2, 3), N)
    tau_over_r = [F(0)] + t3[:N]
    return tau, ts1, ts2, Ru2, tau_over_r


SAMPLES = [(F(1, 2), F(3, 5), F(4, 5)), (F(1), F(5, 13), F(12, 13)), (F(3), F(4, 5), F(3, 5))]
SPINS = {"photon": (1, -1), "graviton": (2, -2)}


def check_weighted_coframe_on_the_exceptional_set():
    premise("interior.kasner-form-interior")
    field = premise("interior.interior-connection-exactly")["interior_field"]
    ok = True
    for k, s0, c0 in SAMPLES:
        fld, r0, _ = field(k, s0, c0)
        th = [[GA.dot(GA.scal(F(1) / S13[a], GA.gen(a)), m_val(fld.g[mu]), S13) for mu in range(4)] for a in range(4)]
        sqA, rth, rph = th[1][1], th[2][2], th[3][3]
        ok = ok and sqA * sqA == (1 - r0) / r0 and rth == r0 and rph == r0 * s0
        ok = ok and r0 * sqA * sqA == 1 - r0 and rth / r0 == 1 and rph / r0 == s0
    _tp_rv = (ok); assert _tp_rv is not False, "check_weighted_coframe_on_the_exceptional_set"; return _tp_rv


def check_orders_become_kasner_exponents():
    premise("sheaf.weights-are-forced-are-kasner-exponents")
    tau = interior_series()[0]
    lead = next(i for i, c in enumerate(tau) if c != 0)            # tau ~ u^lead, u = r^{1/2}
    tau_order = F(lead, 2)
    orders = (F(-1, 2), F(1), F(1))
    p = tuple(o / tau_order for o in orders)
    _tp_rv = (tau_order == F(3, 2) and p == (F(-1, 3), F(2, 3), F(2, 3)) and sum(p) == 1); assert _tp_rv is not False, "check_orders_become_kasner_exponents"; return _tp_rv


def check_helicity_homogeneities():
    premise("hawking.homogeneity-ordering-shift")
    h = {name: tuple(-2 * s - 2 for s in ss) for name, ss in SPINS.items()}
    _tp_rv = (h == {"photon": (-4, 0), "graviton": (-6, 2)} and all(a != b for a, b in h.values())); assert _tp_rv is not False, "check_helicity_homogeneities"; return _tp_rv
