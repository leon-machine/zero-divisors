"""interior.schwarzschild-de-sitter-weighted-limit: exact checks in Gauge Theory Gravity.

The Schwarzschild-de Sitter interior field on flat spacetime in synchronous gauge (labels (r, t, theta, phi),
2M = 1): hb^{-1}(e_r) = A^{-1/2} gamma0, hb^{-1}(e_t) = sqrt(A) gamma1, hb^{-1}(e_theta) = r gamma2,
hb^{-1}(e_phi) = r sin(theta) gamma3, A = (1 - r + (Lambda/3) r^3)/r; Omega(e_i) = -sigma_i e_0 ^ e_i (+ the
sphere term), the Definition's sign. Sample points are chosen with sqrt(A) rational, which fixes rational
Lambda of both signs.
(1) The field: Omega satisfies the torsion equation (rank 24), the frame is D-parallel along e_0, and the
    store's curvature calR(B) = -R(hb(B)) computed from Omega is exactly -(M/r^3) S(B) + (Lambda/3) B on all six
    frame planes (S(B) = -(B + 3 sigma B sigma)/2, sigma = e_0 e_1): Schwarzschild plus de Sitter.
(2) Relative corrections of order Lambda r^3: A_SdS/A_S - 1 = Lambda r^3/(3(1 - r)) exactly at samples; with
    c = Lambda/3 at two values, tau(rho) agrees with Schwarzschild through rho^8 and first differs at rho^9 by
    -c/9 (relative order r^3 ~ tau^2, linear in Lambda); the rate series agree through rho^5 and first differ at
    rho^6; the printed constants -1/3, -4/15, 2/3, -2/15 are unchanged.
(3) Holonomy: in the conformal model Cl(2,4) (W = span(g0, g2, g3, g4), n0, ninf null with n0 . ninf = 1), the
    limiting values -p_i B_i with p = (-1/3, 2/3, 2/3) generate a 6-dimensional algebra (Lambda^2 W). The scale
    tractor I_g = n0 + (Lambda/6) ninf has I_g^2 = Lambda/3 and is annihilated by every element. Its stabiliser
    has dimension 10 with nondegenerate intrinsic Killing form for Lambda != 0 (reductive, no nilradical) and the
    complement of I_g has signature (1,4) for Lambda > 0 (so(1,4)), (2,3) for Lambda < 0; Lambda^2 W is a proper
    subalgebra. For Lambda = 0 the Killing form is degenerate (control: the parabolic case).
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (jets, multivectors with jet coefficients, Field, torsion, curvature) ----
S13 = gtg.S13
J, gbiv = gtg.J, gtg.biv
# the Schwarzschild(-de Sitter) interior field in synchronous gauge, labels (r, t, theta, phi), 2M = 1:
# interior_field(r0, w, s0, c0) -> (field, Lambda, (r, A, sA, s1, s2, sn, cs))
interior_field = gtg.sync_interior_field
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

# ---- end of series ----
# ---- the conformal model Cl(2,4): W = span(g0, g2, g3, g4) of signature (1,3), hyperbolic plane (g1, g5) ----
S24 = GA.sig(2, 4)
W_IDX = (0, 2, 3, 4)
N0, NINF = gtg.null_pair(S24, 1, 5)                         # null, n0 . ninf = 1


def t_rank(xs):
    return gtg.biv_rank(xs, S24)


def t_wbiv(i, j):
    """The bivector W_i ^ W_j of the mu-slot (i < j indices into W_IDX)."""
    return GA.mul(GA.gen(W_IDX[i]), GA.gen(W_IDX[j]), S24)


def scale_tractor(lam):
    """I_g = (1, 0, Lambda/6) in the splitting: n0 + (Lambda/6) ninf, norm I^2 = Lambda/3 (this layout's orientation;
    not gtg.scale_tractor, which is ninf + (Lambda/6) n0 in the gtg.S24 layout)."""
    return GA.add(N0, GA.scal(F(lam) / 6, NINF))


def annihilates(B, I):
    """B . I = 0 for a bivector B and a vector I."""
    return gtg.annihilates(B, I, S24)


def lie_closure(gens):
    return gtg.lie_closure(gens, S24)


def stabiliser(I):
    """Basis of {X bivector : X . I = 0} (kernel of the linear map on the 15 basis bivectors)."""
    return gtg.stabiliser(I, S24)


def killing_rank(L):
    """Rank of the intrinsic Killing form tr(ad_X ad_Y) of the Lie algebra spanned by the basis L."""
    return gtg.killing_rank(L, S24)
# ---- end of the conformal model ----

SDS = [(F(1, 2), F(3, 2), F(3, 5), F(4, 5)), (F(1, 5), F(5, 2), F(5, 13), F(12, 13)),
       (F(1, 2), F(1, 2), F(4, 5), F(3, 5))]
CS = [F(1), F(-2), F(5, 7)]
A_SAMPLES = [(F(1, 3), F(3)), (F(1, 10), F(-6)), (F(2, 7), F(1, 2))]
P_KASNER = (F(-1, 3), F(2, 3), F(2, 3))


def shape(B):
    sig = GA.mul(GA.gen(0), GA.gen(1), S13)
    return GA.scal(F(-1, 2), GA.add(B, GA.scal(3, GA.mul(GA.mul(sig, B, S13), sig, S13))))


def check_sds_field_is_schwarzschild_plus_de_sitter():
    premise("interior.kasner-form-interior")
    premise("interior.exact-parallelism-convergence-rate")
    ok = True
    lams = set()
    for r0, w, s0, c0 in SDS:
        fld, lam, jets = interior_field(r0, w, s0, c0)
        lams.add(lam > 0)
        ok = ok and lam != 0 and fld.torsion_free() and fld.torsion_rank() == 24
        ok = ok and all(fld.cov_phys([F(1), F(0), F(0), F(0)], {(b,): J(1)}) == {} for b in range(4))
        Rc = fld.curvature()
        M = F(1, 2)
        for (a, b), val in Rc.items():
            B = gbiv(a, b)
            want = GA.add(GA.scal(-M / r0 ** 3, shape(B)), GA.scal(lam / 3, B))
            ok = ok and GA.eq(val, want)
    ok = ok and lams == {True, False}
    _tp_rv = (ok); assert _tp_rv is not False, "check_sds_field_is_schwarzschild_plus_de_sitter"; return _tp_rv


def check_corrections_relative_order_lambda_r3():
    premise("interior.kasner-form-interior")
    premise("interior.exact-parallelism-convergence-rate")
    ok = True
    for r, lam in A_SAMPLES:
        AS, ASdS = (1 - r) / r, (1 - r + lam / 3 * r ** 3) / r
        ok = ok and ASdS / AS - 1 == lam * r ** 3 / (3 * (1 - r))
    t0 = tau_series(0)
    s10, s20 = rate_series(0, t0)
    for c in CS:
        t = tau_series(c)
        ok = ok and all(t[k] == t0[k] for k in range(9)) and t[9] - t0[9] == -c / 9
        s1, s2 = rate_series(c, t)
        ok = ok and all(s1[k] == s10[k] and s2[k] == s20[k] for k in range(6))
        ok = ok and s1[6] != s10[6] and s2[6] != s20[6]
        ok = ok and (s1[0], s1[2], s2[0], s2[2]) == (F(-1, 3), F(-4, 15), F(2, 3), F(-2, 15))
    _tp_rv = (ok); assert _tp_rv is not False, "check_corrections_relative_order_lambda_r3"; return _tp_rv


def check_holonomy_inside_reductive_stabiliser():
    premise("interior.boosts-generate-exactly-levi-factor")
    premise("interior.non-null-stabilisers-section-they-act")
    premise("interior.scale-tractor-leaves-cone")
    premise("interior.weighted-limit-theorem")
    vals = [GA.scal(-p, t_wbiv(0, i + 1)) for i, p in enumerate(P_KASNER)]
    L = lie_closure(vals)
    ok = len(L) == 6
    for lam, sig in ((F(3), (1, 4)), (F(-6), (2, 3)), (F(0), None)):
        I = scale_tractor(lam)
        ok = ok and GA.eq(GA.mul(I, I, S24), GA.sc(lam / 3))
        ok = ok and all(annihilates(x, I) for x in L)
        St = stabiliser(I)
        ok = ok and len(St) == 10 and t_rank(St + L) == 10
        kr = killing_rank(St)
        if sig is None:
            ok = ok and kr < 10
        else:
            ok = ok and kr == 10
            # signature of I_g^perp: the tractor Gram on a basis of the complement
            G = [[GA.dot(GA.gen(i), GA.gen(j), S24) for j in range(6)] for i in range(6)]
            Iv = [I.get((a,), F(0)) for a in range(6)]
            perp = GA.field_kernel([[sum(Iv[i] * G[i][j] for i in range(6)) for j in range(6)]])
            Gp = [[sum(u[i] * G[i][j] * v[j] for i in range(6) for j in range(6)) for v in perp] for u in perp]
            ok = ok and GA.congruence_signature(Gp)[:2] == sig
    _tp_rv = (ok); assert _tp_rv is not False, "check_holonomy_inside_reductive_stabiliser"; return _tp_rv
