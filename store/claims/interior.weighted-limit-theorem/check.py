"""interior.weighted-limit-theorem: exact checks in Gauge Theory Gravity (the Schwarzschild member, and the
values-level algebra for every admissible field).

The Schwarzschild interior field (labels (r, t, theta, phi), 2M = 1): hb^{-1}(e_r) = A^{-1/2} gamma0,
hb^{-1}(e_t) = sqrt(A) gamma1, hb^{-1}(e_theta) = r gamma2, hb^{-1}(e_phi) = r sin(theta) gamma3, A = 1/r - 1, and
Omega(e_i) = -sigma_i B_i (B_i = e_0 ^ e_i) plus (cot(theta)/r) R_23 on e_3: the Definition's sign, in which the
Kasner Cartan forms assemble to minus the weighted boosts. The tractor side uses the conformal model Cl(2,4)
(W = span(g0, g2, g3, g4), n0 = (g1 + g5)/2, ninf = g1 - g5).
(1) The field's Omega is the torsion-free one (rank 24) and has exactly the boost entries -sigma_i on B_i and the
    rotation entry cot(theta)/r on R_23. Hubble normalised: tau sigma_i - p_i starts at rho^2 (O(tau^{2/3})),
    the rotation coefficient tau cot(theta)/r at rho^1 (O(tau^{1/3})).
(2), (3) The limiting values are -p_i B_i with p = (-1/3, 2/3, 2/3) the computed rate limits; the scale tractor
    I_g = n0 + (Lambda/6) ninf (Lambda = 0 and Lambda = 3, -6) is annihilated by every B_i (W is orthogonal to
    I_g), so the constant section is parallel for the limiting connection.
(4) The values generate exactly Lambda^2 W: dimension 6, spanning the six W-bivectors, with no component on any
    blade containing g1 or g5 (no n ^ W, n0 ^ W or ninf ^ n0 part); each p_i != 0. For Lambda = 0 the stabiliser
    of the null I_g is Lambda^2 W + (I_g ^ W) (dimension 10), I_g ^ W is an abelian ideal (the nilradical) and
    Lambda^2 W a complement: the Levi factor. For Lambda != 0 the stabiliser (dimension 10) has nondegenerate
    Killing form and contains Lambda^2 W properly.
(5) Transport level along the abelian directions: Omega(e_1) and Omega(e_2) are single fixed bivectors times
    scalars (so the transports along t- and theta-lines commute), while on the phi-lines B_3 and R_23 do not
    commute. Along the tau-geodesics the scale-factor ratios to the Kasner model, sqrt(1 - r) S^{1/3} and
    S^{-2/3}, differ from 1 at order rho^2 (O(tau^{2/3})).
"""
from fractions import Fraction as F

import GA
import gtg
import series
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13
m_val = gtg.m_val
gbiv = gtg.biv                          # gamma_a gamma_b


def torsion_rank(fld):
    """Rank of the algebraic torsion map Omega -> (Omega_mu . g_nu - Omega_nu . g_mu) at the point (24 = injective:
    the torsion equation then fixes Omega uniquely)."""
    return fld.torsion_rank()


# ---- the Schwarzschild(-de Sitter) interior field in synchronous gauge, labels (r, t, theta, phi), 2M = 1 ----
def interior_field(r0, w, s0, c0):
    """hb^{-1}(e_r) = gamma0/sqrt(A), hb^{-1}(e_t) = sqrt(A) gamma1, hb^{-1}(e_theta) = r gamma2,
    hb^{-1}(e_phi) = r sin(theta) gamma3, A = (1 - r + (Lambda/3) r^3)/r with Lambda fixed by sqrt(A(r0)) = w;
    Omega(e_i) = -sigma_i e_0 ^ e_i, plus (cot(theta)/r) e_2 ^ e_3 on e_3 (gtg.sync_interior_field).
    Returns (field, Lambda, (r, A, sA, s1, s2, sn, cs))."""
    return gtg.sync_interior_field(r0, w, s0, c0)
# ---- end of engine ----
# ---- exact series of the (Schwarzschild-de Sitter) interior in rho = sqrt(r), 2M = 1 ----
NS = 12


def tau_series(c, N=NS):
    """tau(rho) = int_0^r A^{-1/2} du, A = (1 - u + c u^3)/u (c = Lambda/3), as a series in rho = sqrt(r):
    d tau = 2 rho^2 (1 - rho^2 + c rho^6)^{-1/2} d rho."""
    fac = [F(1), F(0), F(-1), F(0), F(0), F(0), F(c)]
    half = GA.ps_pow_rat(fac, F(-1, 2), N)
    return GA.ps_int(GA.ps_mul([F(0), F(0), F(2)], half, N))[:N + 1]


def rate_series(c, tau, N=NS):
    """(tau sigma_1, tau sigma_2) as series in rho, sigma_1 = d_tau log sqrt(A) = A'/(2 sqrt A),
    sigma_2 = d_tau log r = sqrt(A)/r."""
    fac = [F(1), F(0), F(-1), F(0), F(0), F(0), F(c)]
    inv_sqrt = GA.ps_pow_rat(fac, F(-1, 2), N)
    t3 = GA.ps_trunc([tau[3 + k] for k in range(N - 2)], N)
    ts1 = GA.ps_mul(GA.ps_mul(t3, [F(-1, 2), F(0), F(0), F(0), F(0), F(0), F(c)], N), inv_sqrt, N)
    ts2 = GA.ps_mul(t3, GA.ps_pow_rat(fac, F(1, 2), N), N)
    return ts1, ts2


def r_of_R(tau, N=NS):
    """R = (3 tau/2)^{2/3} as a series in rho (R = rho^2 (1 + ...))."""
    U = [tau[3 + k] * F(3, 2) for k in range(N - 2)]
    return GA.ps_trunc([F(0), F(0)] + GA.ps_pow_rat(GA.ps_trunc(U, N), F(2, 3), N), N)


def peel_in_R(ts, Rser, N=NS):
    """(c0, c1, residual) with ts = c0 + c1 R + c2 R^2 + residual, by exact division against R(rho)."""
    Rsq = GA.ps_mul(Rser, Rser, N)
    c0 = ts[0]
    r1 = [ts[k] - (c0 if k == 0 else F(0)) for k in range(N + 1)]
    c1 = r1[2] / Rser[2]
    r2 = [r1[k] - c1 * Rser[k] for k in range(N + 1)]
    c2 = r2[4] / Rsq[4]
    r3 = [r2[k] - c2 * Rsq[k] for k in range(N + 1)]
    return c0, c1, r3


lead = series.ps_valuation                # index of the first nonzero coefficient
# ---- end of series ----
# ---- the conformal model Cl(2,4): W = span(g0, g2, g3, g4) of signature (1,3), hyperbolic plane (g1, g5) ----
S24 = GA.sig(2, 4)
W_IDX = (0, 2, 3, 4)
N0, NINF = gtg.null_pair(S24, 1, 5)                         # (g1 + g5)/2 and g1 - g5: null, n0 . ninf = 1


def t_comm(x, y):
    return gtg.comm(x, y, S24)


def t_rank(xs):
    return gtg.biv_rank(xs, S24)


def t_wbiv(i, j):
    """The bivector W_i ^ W_j of the mu-slot (i < j indices into W_IDX)."""
    return GA.mul(GA.gen(W_IDX[i]), GA.gen(W_IDX[j]), S24)


def scale_tractor(lam):
    """I_g = (1, 0, Lambda/6) in the splitting: n0 + (Lambda/6) ninf, norm I^2 = Lambda/3 (this layout)."""
    return GA.add(N0, GA.scal(F(lam) / 6, NINF))


def annihilates(B, I):
    """B . I = 0 for a bivector B and a vector I."""
    return gtg.annihilates(B, I, S24)


def lie_closure(gens):
    return gtg.lie_closure(gens, S24)


def stabiliser(I):
    """Basis of {X bivector : X . I = 0}."""
    return gtg.stabiliser(I, S24)


def killing_rank(L):
    """Rank of the intrinsic Killing form tr(ad_X ad_Y) of the Lie algebra spanned by the basis L."""
    return gtg.killing_rank(L, S24)
# ---- end of the conformal model ----

SAMPLES = [(F(1, 2), F(1), F(3, 5), F(4, 5)), (F(1, 5), F(2), F(5, 13), F(12, 13)),
           (F(4, 5), F(1, 2), F(4, 5), F(3, 5))]


def check_connection_shape_and_rates():
    premise("interior.interior-connection-exactly")
    premise("interior.exact-parallelism-convergence-rate")
    ok = True
    for r0, w, s0, c0 in SAMPLES:
        fld, lam, (r, A, sA, s1, s2, sn, cs) = interior_field(r0, w, s0, c0)
        ok = ok and fld.torsion_free() and torsion_rank(fld) == 24
        ok = ok and m_val(fld.om[1]) == {(0, 1): -s1.v} and m_val(fld.om[2]) == {(0, 2): -s2.v}
        ok = ok and m_val(fld.om[3]) == {(0, 3): -s2.v, (2, 3): c0 / (s0 * r0)} and m_val(fld.om[0]) == {}
    tau = tau_series(0)
    lt = lead(tau)
    ts1, ts2 = rate_series(0, tau)
    for ser in (ts1, ts2):
        d = [ser[k] - (ser[0] if k == 0 else 0) for k in range(len(ser))]
        ok = ok and F(lead(d), lt) == F(2, 3)
    rot = [F(0)] + [F(3, 2) * tau[3 + k] for k in range(NS - 2)]
    ok = ok and F(lead(rot), lt) == F(1, 3)
    _tp_rv = (ok); assert _tp_rv is not False, "check_connection_shape_and_rates"; return _tp_rv


def check_limiting_values_annihilate_scale_tractor():
    premise("interior.kasner-form-interior")
    premise("interior.covariant-form-vacuum-equations")
    premise("interior.scale-tractor-leaves-cone")
    premise("interior.metric-parallelism-trace-schouten-condition")
    ts1, ts2 = rate_series(0, tau_series(0))
    p = (ts1[0], ts2[0], ts2[0])
    ok = p == (F(-1, 3), F(2, 3), F(2, 3))
    vals = [GA.scal(-p[i], t_wbiv(0, i + 1)) for i in range(3)]
    for lam in (F(0), F(3), F(-6)):
        I = scale_tractor(lam)
        ok = ok and GA.eq(GA.mul(I, I, S24), GA.sc(lam / 3))
        ok = ok and all(annihilates(v, I) for v in vals)
        ok = ok and all(GA.dot(GA.gen(W_IDX[k]), I, S24) == 0 for k in range(4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_limiting_values_annihilate_scale_tractor"; return _tp_rv


def check_holonomy_algebra_is_levi_factor():
    premise("interior.boosts-generate-exactly-levi-factor")
    premise("interior.stabilisers-flat-model")
    premise("interior.non-null-stabilisers-section-they-act")
    p = (F(-1, 3), F(2, 3), F(2, 3))
    ok = all(x != 0 for x in p)
    vals = [GA.scal(-p[i], t_wbiv(0, i + 1)) for i in range(3)]
    L = lie_closure(vals)
    LW = [t_wbiv(i, j) for i in range(4) for j in range(i + 1, 4)]
    ok = ok and len(L) == 6 and t_rank(L + LW) == 6
    ok = ok and all(1 not in bl and 5 not in bl for x in L for bl in x)
    # Lambda = 0: stabiliser = Lambda^2 W + I ^ W, I ^ W an abelian ideal
    I = scale_tractor(0)
    St = stabiliser(I)
    IW = [GA.scal(F(1, 2), GA.sub(GA.mul(I, GA.gen(W_IDX[k]), S24), GA.mul(GA.gen(W_IDX[k]), I, S24)))
          for k in range(4)]
    ok = ok and len(St) == 10 and t_rank(St + L + IW) == 10 and t_rank(L + IW) == 10 and t_rank(IW) == 4
    ok = ok and all(GA.is_zero(t_comm(a, b)) for a in IW for b in IW)
    ok = ok and all(t_rank(IW + [t_comm(x, a)]) == 4 for x in St for a in IW)
    ok = ok and killing_rank(St) == 6
    for lam in (F(3), F(-6)):
        St2 = stabiliser(scale_tractor(lam))
        ok = ok and len(St2) == 10 and t_rank(St2 + L) == 10 and killing_rank(St2) == 10
    _tp_rv = (ok); assert _tp_rv is not False, "check_holonomy_algebra_is_levi_factor"; return _tp_rv


def check_transport_along_abelian_directions():
    premise("interior.interior-connection-exactly")
    premise("interior.kasner-form-interior")
    fld, lam, jets = interior_field(*SAMPLES[0])
    om = [m_val(fld.om[c]) for c in range(4)]
    ok = len(om[1]) == 1 and len(om[2]) == 1 and len(om[3]) == 2
    B3, R23 = gbiv(0, 3), gbiv(2, 3)
    ok = ok and not GA.commutes(B3, R23, S13)
    tau = tau_series(0)
    S = GA.ps_trunc([F(3, 2) * tau[3 + k] for k in range(NS - 2)], NS)
    for ser in (GA.ps_mul(GA.ps_pow_rat([F(1), F(0), F(-1)], F(1, 2), NS), GA.ps_pow_rat(S, F(1, 3), NS), NS),
                GA.ps_pow_rat(S, F(-2, 3), NS)):
        d = [ser[k] - (1 if k == 0 else 0) for k in range(len(ser))]
        ok = ok and lead(d) == 2 and F(lead(d), lead(tau)) == F(2, 3)
    _tp_rv = (ok); assert _tp_rv is not False, "check_transport_along_abelian_directions"; return _tp_rv
