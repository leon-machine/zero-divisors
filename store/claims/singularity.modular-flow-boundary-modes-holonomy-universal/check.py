"""singularity.modular-flow-boundary-modes-holonomy-universal: exact checks in Gauge Theory Gravity.

Collar, units 2M = 1, synchronous gauge: derived metric d tau^2 - A dt^2 - r^2 dOmega^2, A = 1/r - 1; physical
orthonormal frame e0 = g_tau, e1, e2, e3 (GA, Cl(1,3)); along a t-line the physical vector over d_t is
sqrt(A) e1 and the rotation-gauge field on e1 is -sigma_1 B_1 (GTG sign), B_1 = e0 ^ e1,
sigma_1 = d_tau log sqrt(A) = -A'/(2 sqrt(A)) (free fall from rest at the horizon, dr/dtau = -sqrt(A)).
Rational sample points: A = w^2, r = 1/(1 + w^2).
(i) Omega(d_t) = sqrt(A) (-sigma_1 B_1) = (A'/2) B_1 computed in GA at w = 0 (horizon), 1/2, 1, 3, 7/4; the
    transport d e/dt = -Omega(d_t) x e sends e0 to -rate e1 and e1 to -rate e0, rate = |A'|/2 = 1/(2 r^2), and fixes
    e2, e3 (a boost in B_1). As rational functions: -A'/2 = 1/(2r^2); at r = 1 the rate is 1/2 = kappa
    (units 2M = 1); inside r = 1/2, 1/4, 1/8 give 2, 8, 32 and the KMS period over pi, 2/rate = 4 r^2, shrinks.
    In general units the rate M/r^2 at r = 2M R times 2M is 1/(2 R^2) for M = 1/2, 3/2, 5: M drops out.
(ii) Hubble-normalised: S(r) defined by S + (2/3) r S' = (1 - r)^{-1/2} (so that (2/3) r^{3/2} S(r) =
    int_0^r sqrt(u/(1-u)) du = tau), S = 1 + (3/10) r + (9/56) r^2 + ...; the rate tau |A'|/(2 sqrt A) =
    (1/3) S (1 - r)^{-1/2} = 1/3 + (4/15) r + ...; limit |p_1| = 1/3 and beta_H/pi = 2/(1/3) = 6.
(iii) Sphere rate (2/3) S (1 - r)^{1/2} = 2/3 - (2/15) r + ..., giving 2/(2/3) = 3 (i.e. 3 pi). The limiting
    boosts B_1, B_2, B_3 pairwise fail to commute, (B_1 B_2 - B_2 B_1)/2 = -e1 e2 = -R_12; a Gibbs-type density
    of flow i, ch - sh B_i (ch^2 - sh^2 = 1, sh != 0), lies in no span(1, B_j), j != i, the only place a
    beta' != 0 Gibbs density of flow j can lie, while the trace (density 1) lies in all three.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]


def wedge(a, b):
    return GA.scal(F(1, 2), GA.sub(GA.mul(a, b, S), GA.mul(b, a, S)))


B = [None, wedge(E[0], E[1]), wedge(E[0], E[2]), wedge(E[0], E[3])]


def cx(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def check_t_line_holonomy_rate():
    premise("singularity.imported-interior-collar-kasner-form")
    premise("singularity.plane-rate")
    premise("singularity.modular-structure-completed-pair")
    ok = True
    for w in (F(0), F(1, 2), F(1), F(3), F(7, 4)):
        A = w * w
        r = 1 / (1 + A)
        ok = ok and A == 1 / r - 1
        Ap = -1 / (r * r)
        rate = -Ap / 2
        if w != 0:
            sigma1 = -Ap / (2 * w)
            Om_t = GA.scal(w, GA.scal(-sigma1, B[1]))     # omega(sqrt(A) e1)
            ok = ok and GA.eq(Om_t, GA.scal(Ap / 2, B[1]))
        else:
            Om_t = GA.scal(Ap / 2, B[1])                 # the continuous extension at the horizon
        gen = GA.neg(Om_t)
        ok = ok and GA.eq(cx(gen, E[0]), GA.scal(-rate, E[1]))
        ok = ok and GA.eq(cx(gen, E[1]), GA.scal(-rate, E[0]))
        ok = ok and GA.is_zero(cx(gen, E[2])) and GA.is_zero(cx(gen, E[3]))
        ok = ok and rate == 1 / (2 * r * r)
    rr = GA.RF.var()
    A = GA.RF1 / rr - GA.RF1
    rate = A.deriv() * GA.RF.const(F(-1, 2))
    ok = ok and rate.eqrf(GA.RF1 / (GA.RF.const(2) * rr * rr)) and rate.eval(F(1)) == F(1, 2)
    ok = ok and [rate.eval(F(1, 2)), rate.eval(F(1, 4)), rate.eval(F(1, 8))] == [F(2), F(8), F(32)]
    ok = ok and [2 / rate.eval(x) for x in (F(1), F(1, 2), F(1, 4))] == [4 * x * x for x in (F(1), F(1, 2), F(1, 4))]
    for M in (F(1, 2), F(3, 2), F(5)):
        for R in (F(1), F(1, 3)):
            ok = ok and (M / (2 * M * R) ** 2) * 2 * M == 1 / (2 * R * R)
    _tp_rv = (ok); assert _tp_rv is not False, "check_t_line_holonomy_rate"; return _tp_rv


N = 6


def series():
    one_minus = [F(1), F(-1)]
    inv_sqrt = GA.ps_pow_rat(one_minus, F(-1, 2), N)
    sqrt_1mr = GA.ps_pow_rat(one_minus, F(1, 2), N)
    # S + (2/3) r S' = (1 - r)^{-1/2}: coefficientwise s_k (1 + 2k/3) = c_k
    Sr = [inv_sqrt[k] / (1 + F(2 * k, 3)) for k in range(N + 1)]
    return inv_sqrt, sqrt_1mr, Sr


def check_hubble_normalised_limit_six_pi():
    premise("singularity.imported-interior-collar-kasner-form")
    premise("singularity.r-regularity-fixed-locus")
    inv_sqrt, sqrt_1mr, Sr = series()
    ok = Sr[0] == 1 and Sr[1] == F(3, 10) and Sr[2] == F(9, 56)
    # tau' = r^{1/2} (S + (2/3) r S') must equal r^{1/2} (1 - r)^{-1/2}
    lhs = [Sr[k] + F(2, 3) * k * Sr[k] for k in range(N + 1)]
    ok = ok and lhs == inv_sqrt
    hub1 = [F(1, 3) * c for c in GA.ps_mul(Sr, inv_sqrt, N)]
    ok = ok and hub1[0] == F(1, 3) and hub1[1] == F(4, 15)
    ok = ok and 2 / hub1[0] == 6
    _tp_rv = (ok); assert _tp_rv is not False, "check_hubble_normalised_limit_six_pi"; return _tp_rv


def check_sphere_rate_and_noncommuting_boosts():
    premise("singularity.imported-interior-collar-kasner-form")
    premise("singularity.modular-structure-completed-pair")
    inv_sqrt, sqrt_1mr, Sr = series()
    hub2 = [F(2, 3) * c for c in GA.ps_mul(Sr, sqrt_1mr, N)]
    ok = hub2[0] == F(2, 3) and hub2[1] == F(-2, 15) and 2 / hub2[0] == 3
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            if i < j:
                c = cx(B[i], B[j])
                ok = ok and not GA.is_zero(c)
                ok = ok and GA.eq(c, GA.neg(GA.mul(E[i], E[j], S)))
    blades = GA.all_blades(4)
    for i in (1, 2, 3):
        for ch, sh in ((F(5, 4), F(3, 4)), (F(13, 5), F(-12, 5))):
            rho = GA.sub(GA.sc(ch), GA.scal(sh, B[i]))
            for j in (1, 2, 3):
                vecs = [[x.get(b, F(0)) for b in blades] for x in (GA.sc(1), B[j], rho)]
                ok = ok and (GA.rank_of_vectors(vecs) == 2) == (i == j)
        for j in (1, 2, 3):
            ok = ok and GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in (GA.sc(1), B[j])]) == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_sphere_rate_and_noncommuting_boosts"; return _tp_rv
