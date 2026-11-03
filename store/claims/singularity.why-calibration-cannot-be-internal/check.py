"""singularity.why-calibration-cannot-be-internal: exact checks in Gauge Theory Gravity (GA, Cl(1,3)).

Local background frame: e_t = gen 0, e_r = gen 1, e_theta = gen 2, e_phi = gen 3 (unit background vectors).
Stored PG field: hb(a) = a - beta (a . e_t) e_r, hb^{-1}(a) = a + beta (a . e_t) e_r, adjoint
hb^T(a) = a - beta (a . e_r) e_t, beta = sqrt(2M/r); GTG-sign connection on the radial plane
Omega(e_t) = (M/r^2) sigma_r, Omega(e_r) = (beta/(2r)) sigma_r, sigma_r = e_r e_t. Rational samples:
beta, M rational, r = 2M/beta^2.
(1) The connection rate on the singular side: the sigma_r coefficient of Omega(e_r) squares to M/(2 r^3) at
    every sample (beta = 2, 3, 5, 7/2, 10 inside the horizon), it grows strictly as r decreases, and the
    rational function M/(2 r^3) has a pole at r = 0: no finite period there. The horizon rate is finite:
    (K . D)K = kappa K at beta = 1 with kappa = 1/(4M) (K = hb^{-1}(e_t), static), for four masses.
(2) The cross-section Sigma = {t = t0, r = 2M}: the physical angular vectors over r e_theta, r sin(theta)
    e_phi have Gram diag(r^2, r^2 sin^2) -> area 4 pi r^2 = 16 pi M^2 (area/pi = 16 M^2). K is null there,
    orthogonal (flat product) to the physical vectors over the tangent directions e_t, e_theta, e_phi of
    {r = 2M}, and parallel to the physical normal hb^T(nabla r) = hb^T(-e_r) = -K; the flow of K is
    hb(K) = e_t, translation in t, carrying Sigma_{t0} to Sigma_{t0 + s}.
(3) At the horizon the gauge field is invertible and unimodular: P^2 = 0, hb hb^{-1} = 1 on the frame and the
    outermorphism sends I to I (det hb = 1), at the horizon and at the inner samples; the derived metric
    Gram G_mn = hb^{-1}(e_m) . hb^{-1}(e_n) is nondegenerate there (congruence signature (1,3,0)), so division
    does not fail; the static-gauge Gram diag(f, -1/f, ...) is the one that degenerates (f = 0).
(4) The period fixed by (R): 2 pi/kappa = 8 pi M (p/pi = 8M).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = GA.sig(1, 3)
ET, ER, ETH, EPH = (GA.gen(i) for i in range(4))
SIG = GA.mul(ER, ET, S)
I4 = {(0, 1, 2, 3): F(1)}
FRAME = [ET, ER, ETH, EPH]
MASSES = [F(1), F(1, 2), F(3), F(7, 4)]


def dot(a, b):
    return GA.dot(a, b, S)


def hb(a, beta):
    return GA.sub(a, GA.scal(beta * dot(a, ET), ER))


def hbinv(a, beta):
    return GA.add(a, GA.scal(beta * dot(a, ET), ER))


def hbT(a, beta):
    return GA.sub(a, GA.scal(beta * dot(a, ER), ET))


def comm(A, B):
    return GA.scal(F(1, 2), GA.sub(GA.mul(A, B, S), GA.mul(B, A, S)))


def wedge_all(vs):
    out = GA.sc(1)
    for v in vs:
        out = GA.mul(out, v, S)
    return {b: c for b, c in out.items() if len(b) == len(vs)}


def check_only_finite_rate_is_the_horizon_rate():
    premise("singularity.connection-bivector-computed")
    premise("singularity.solution-where-divergence-lies")
    ok = True
    for M in MASSES:
        prev = None
        for beta in (F(2), F(3), F(7, 2), F(5), F(10)):
            r = 2 * M / (beta * beta)
            coef = (beta / (2 * r))
            Om_r = GA.scal(coef, SIG)
            c = -Om_r.get((0, 1), F(0))                 # sigma_r = -e0 e1
            ok = ok and c * c == M / (2 * r ** 3)
            if prev is not None:
                ok = ok and c > prev                    # r decreases as beta increases
            prev = c
        rate_sq = GA.RF.const(M / 2) / (GA.RF.var() * GA.RF.var() * GA.RF.var())
        pole = False
        try:
            rate_sq.eval(F(0))
        except ZeroDivisionError:
            pole = True
        ok = ok and pole
        K = hbinv(ET, F(1))
        KDK = comm(GA.scal(M / (2 * M) ** 2, SIG), K)
        ok = ok and GA.eq(hb(K, F(1)), ET) and GA.eq(KDK, GA.scal(1 / (4 * M), K))
    _tp_rv = (ok); assert _tp_rv is not False, "check_only_finite_rate_is_the_horizon_rate"; return _tp_rv


def check_cross_section_area_null_normal_killing():
    ok = True
    for M in MASSES:
        r = 2 * M
        beta = F(1)
        ok = ok and beta * beta == 2 * M / r
        for s in (F(3, 5), F(1), F(12, 13)):
            ang = [hbinv(GA.scal(r, ETH), beta), hbinv(GA.scal(r * s, EPH), beta)]
            G = [[-dot(a, b) for b in ang] for a in ang]      # spacelike: area form from -Q
            ok = ok and G == [[r * r, 0], [0, r * r * s * s]]
        ok = ok and 4 * r * r == 16 * M * M                  # area/pi = 4 r^2
        K = hbinv(ET, beta)
        ok = ok and dot(K, K) == 0
        for tangent in (ET, ETH, EPH):
            ok = ok and dot(K, hbinv(tangent, beta)) == 0
        normal = hbT(GA.neg(ER), beta)                       # physical gradient of r (nabla r = -e_r)
        ok = ok and GA.eq(normal, GA.neg(K))
        ok = ok and GA.eq(hb(K, beta), ET)                   # flow of K = translation in t
    _tp_rv = (ok); assert _tp_rv is not False, "check_cross_section_area_null_normal_killing"; return _tp_rv


def check_invertible_unimodular_nondegenerate_at_horizon():
    premise("singularity.unipotent-ray")
    premise("transport.transport-algorithm")
    ok = True
    for M in MASSES:
        for beta in (F(1), F(2), F(1, 2)):
            r = 2 * M / (beta * beta)
            # P(a) = (a . e_t) e_r is nilpotent: P(P(a)) = 0 on the frame
            ok = ok and all(GA.is_zero(GA.scal(dot(GA.scal(dot(a, ET), ER), ET), ER)) for a in FRAME)
            ok = ok and r > 0
            ok = ok and all(GA.eq(hb(hbinv(a, beta), beta), a) for a in FRAME)
            ok = ok and GA.eq(wedge_all([hb(a, beta) for a in FRAME]), I4)
            phys = [hbinv(a, beta) for a in FRAME]
            G = [[dot(a, b) for b in phys] for a in phys]
            ok = ok and GA.congruence_signature(G) == (1, 3, 0)
            f = 1 - beta * beta
            static = [[f, 0], [0, -1 / f]] if f != 0 else None
            ok = ok and ((static is None) == (beta == 1))
            if beta == 1:
                ok = ok and G[0][0] == 0 and G[0][1] == -1      # PG: dt^2 - (dr + dt)^2 at the horizon
    _tp_rv = (ok); assert _tp_rv is not False, "check_invertible_unimodular_nondegenerate_at_horizon"; return _tp_rv


def check_period_is_eight_pi_m():
    premise("singularity.euclidean-section-period")
    ok = True
    for M in MASSES:
        kappa = 1 / (4 * M)
        p_over_pi = 2 / kappa
        ok = ok and p_over_pi == 8 * M and kappa * p_over_pi == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_period_is_eight_pi_m"; return _tp_rv
