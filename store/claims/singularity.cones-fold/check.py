"""singularity.cones-fold: exact checks in Gauge Theory Gravity.

Flat spacetime: Cl(1,3) in GA.py, signature (+,-,-,-), e_t = gamma_0, e_r = gamma_1. PG gauge field
hb = 1 - beta P, P(a) = (a.e_t) e_r, hb^{-1} = 1 + beta P; g(a,a) = Q(hb^{-1}(a)) computed with GA.mul.
(1) For a = e_t + lambda e_r: hb^{-1}(a) = e_t + (lambda + beta) e_r and g(a,a) = 1 - (lambda + beta)^2,
    checked in GA at sample (beta, lambda) and as an identity in lambda (Q(lambda), GA.RF) for each
    sample beta, by matching g at three values of lambda (g is quadratic in lambda);
    1 - (lambda + beta)^2 = -(lambda - (-beta + 1))(lambda - (-beta - 1)) over Q(lambda): a is g-null
    exactly at lambda = -beta +- 1; the g-null vectors are the hb-images of the flat null e_t +- e_r.
(2) At the horizon beta = 1 the null pair is lambda = 0 (hovering) and lambda = -2 (ingoing).
(3) Folding: for beta > 1 the normalised e_t-coefficients 1/(-beta +- 1) are both negative (both
    branches tip inward) and bounded in size by 1/(beta - 1), so both normalised directions
    converge to e_r; g(e_t, e_t), computed in GA and fitted as the quadratic in beta it is, equals
    1 - beta^2 over Q(beta): unbounded below.
(4) The limit direction e_r is the null kernel direction of singularity.degeneration-exactly: P e_r = 0
    and the limit form ghat(a,b) = -(a.e_t)(b.e_t) vanishes on e_r against every frame vector.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
ET, ER = GA.gen(0), GA.gen(1)
BETAS = [F(3, 7), F(1), F(5, 2), F(10)]


def P(a):
    return GA.scal(GA.dot(a, ET, S13), ER)


def hb(a, bt):
    return GA.sub(a, GA.scal(bt, P(a)))


def hb_inv(a, bt):
    return GA.add(a, GA.scal(bt, P(a)))


def g_aa(lam, bt):
    x = hb_inv(GA.add(ET, GA.scal(lam, ER)), bt)
    return GA.mul(x, x, S13).get((), F(0))


def check_null_directions_of_the_physical_cone():
    lv = GA.RF.var()
    for bt in BETAS:
        for lam in (F(-2), F(0), F(1, 2), F(3)):
            x = hb_inv(GA.add(ET, GA.scal(lam, ER)), bt)
            assert GA.eq(x, GA.add(ET, GA.scal(lam + bt, ER)))
        # g is a quadratic in lambda: three values fix it
        q0, q1, qm = g_aa(F(0), bt), g_aa(F(1), bt), g_aa(F(-1), bt)
        a2, a1 = (q1 + qm) / 2 - q0, (q1 - qm) / 2
        poly = GA.RF([q0, a1, a2])
        claimed = GA.RF1 - (lv + GA.RF.const(bt)) * (lv + GA.RF.const(bt))
        assert poly.eqrf(claimed)
        factored = -((lv - GA.RF.const(-bt + 1)) * (lv - GA.RF.const(-bt - 1)))
        assert claimed.eqrf(factored)
        for sgn in (1, -1):
            assert g_aa(-bt + sgn, bt) == 0
            img = hb(GA.add(ET, GA.scal(F(sgn), ER)), bt)
            assert GA.eq(img, GA.add(ET, GA.scal(sgn - bt, ER)))
        assert g_aa(-bt + F(1, 3), bt) != 0
    return True


def check_horizon_null_pair():
    roots = [lam for lam in (F(-3), F(-2), F(-1), F(0), F(1), F(2)) if g_aa(lam, F(1)) == 0]
    assert roots == [-2, 0]
    return True


def check_cones_fold_onto_e_r():
    for bt in (F(2), F(10), F(1000)):
        cs = [1 / (-bt + 1), 1 / (-bt - 1)]
        for cf in cs:
            assert cf < 0
            assert abs(cf) * (bt - 1) <= 1
    # g(e_t, e_t) is quadratic in beta; fitted from GA at beta = 0, 1, -1 it is 1 - beta^2
    def gtt(bt):
        x = hb_inv(ET, bt)
        return GA.mul(x, x, S13).get((), F(0))
    q0, q1, qm = gtt(F(0)), gtt(F(1)), gtt(F(-1))
    fit = GA.RF([q0, (q1 - qm) / 2, (q1 + qm) / 2 - q0])
    bv = GA.RF.var()
    assert fit.eqrf(GA.RF1 - bv * bv)
    assert [gtt(bt) for bt in (F(10), F(100))] == [-99, -9999]
    return True


def check_limit_direction_is_null_kernel_direction():
    premise("singularity.degeneration-exactly")
    assert GA.is_zero(P(ER))
    frame = [GA.gen(i) for i in range(4)]
    assert all(-(GA.dot(ER, ET, S13) * GA.dot(c, ET, S13)) == 0 for c in frame)
    assert -(GA.dot(ET, ET, S13) * GA.dot(ET, ET, S13)) == -1
    return True
