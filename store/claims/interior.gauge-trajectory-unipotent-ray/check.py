"""interior.gauge-trajectory-unipotent-ray: exact checks in Gauge Theory Gravity.

Flat spacetime: Cl(1,3) in GA.py, signature (+,-,-,-), frame e_t, e_r, e_theta, e_phi = gamma_0..gamma_3.
P(a) = (a.e_t) e_r; the PG gauge field hb = 1 - beta P with beta = sqrt(2M/r); derived metric
g(a,b) = hb^{-1}(a) . hb^{-1}(b) (GA.dot). Matrices over Q(s) (GA.RF) for identities in a parameter.
(1) P^2 = 0, and (1 + sP)(1 + s'P) = 1 + (s + s')P over Q(s) for several s' (and with 1 + 0P = 1 the
    identity): a one-parameter group. The history is the ray s = -beta(r): at r = 2M/beta^2 for
    beta = 10, 2, 1, 1/2, 1/10 (M = 3/2) r increases while s = -beta increases towards 0, and s <= 0
    throughout (s^2 r = 2M, so s -> -infinity as r -> 0).
(2) hb^{-1} = 1 + beta P over Q(beta), the horizon beta = 1 included (det hb = 1).
(3) The metric is the PG line element: g(e_t,e_t) = 1 - beta^2, g(e_t,e_r) = -beta, g(e_r,e_r) = -1,
    g(e_theta,e_theta) = g(e_phi,e_phi) = -1, all other pairs 0: computed in GA at five beta values and
    matched to the quadratic polynomials in beta (each entry is a polynomial of degree <= 2 in beta).
(4) Division fails nowhere at r > 0 (det hb = 1); the null directions e_t + lambda e_r of g are
    lambda = -beta +- 1, whose normalised directions converge to e_r, which lies in the kernel of the
    rescaled limit -P (singularity.degeneration-exactly).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
ET, ER = GA.gen(0), GA.gen(1)
FRAME = [GA.gen(i) for i in range(4)]
BETAS = [F(0), F(1, 3), F(1), F(5, 2), F(4)]
# Second group parameters s' in (1 + sP)(1 + s'P) = 1 + (s + s')P (s' = 0 is the identity).
SHIFTS = (F(-2), F(0), F(1, 3), F(7))
# Sample mass and beta values along the history ray r = 2M/beta^2, listed with r increasing.
M_RAY = F(3, 2)
BETAS_RAY = (F(10), F(2), F(1), F(1, 2), F(1, 10))


def P(a):
    return GA.scal(GA.dot(a, ET, S13), ER)


def pmat():
    return [[GA.RF.const(P(FRAME[j]).get((i,), F(0))) for j in range(4)] for i in range(4)]


def unit(c=GA.RF1):
    return [[c if i == j else GA.RF0 for j in range(4)] for i in range(4)]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), GA.RF0) for j in range(4)] for i in range(4)]


def plus(A, B, c):
    return [[A[i][j] + c * B[i][j] for j in range(4)] for i in range(4)]


def same(A, B):
    return all(A[i][j].eqrf(B[i][j]) for i in range(4) for j in range(4))


def lagrange(xs, ys, x):
    tot = F(0)
    for i, xi in enumerate(xs):
        t = ys[i]
        for j, xj in enumerate(xs):
            if j != i:
                t = t * (x - xj) / (xi - xj)
        tot += t
    return tot


def check_unipotent_group_and_history_ray():
    s = GA.RF.var()
    Pm = pmat()
    assert all(x.is_zero() for row in mm(Pm, Pm) for x in row)
    for sp in SHIFTS:
        lhs = mm(plus(unit(), Pm, s), plus(unit(), Pm, GA.RF.const(sp)))
        rhs = plus(unit(), Pm, s + GA.RF.const(sp))
        assert same(lhs, rhs)
    M = M_RAY
    prev = None
    for bt in BETAS_RAY:       # r increasing
        r = 2 * M / (bt * bt)
        sv = -bt
        assert sv == -abs(sv)                                   # s <= 0
        assert sv * sv * r == 2 * M                             # s^2 r = 2M, by hand from beta^2 = 2M/r
        assert (sv >= -1) == (r >= 2 * M)                       # |s| <= 1 exactly on and outside the horizon r = 2M
        if prev is not None:
            prev_r, prev_s = prev
            assert r > prev_r and sv > prev_s
        prev = (r, sv)
    return True


def check_closed_form_inverse():
    b = GA.RF.var()
    Pm = pmat()
    H, Hi = plus(unit(), Pm, -b), plus(unit(), Pm, b)
    assert same(mm(H, Hi), unit()) and same(mm(Hi, H), unit())
    assert GA.rf_mat_det(H).eqrf(GA.RF1)
    # By hand: P(e_t) = (e_t . e_t) e_r = e_r and P kills e_r, e_theta, e_phi, so hb = 1 - beta P differs from
    # the identity in exactly one entry, row e_r column e_t, equal to -beta (and +beta in hb^{-1}); trace 4.
    I4 = unit()
    off = [(i, j) for i in range(4) for j in range(4) if not (H[i][j] - I4[i][j]).is_zero()]
    assert off == [(1, 0)]
    assert H[1][0].eqrf(-b) and Hi[1][0].eqrf(b)
    assert sum((H[i][i] for i in range(4)), GA.RF0).eqrf(GA.RF.const(F(4)))
    # the horizon beta = 1: hb(e_t) = e_t - e_r, hb^{-1}(e_t) = e_t + e_r, det 1
    one = [[GA.RF.const(x.eval(F(1))) for x in row] for row in H]
    assert one[1][0].eqrf(GA.RF.const(F(-1))) and one[0][0].eqrf(GA.RF1)
    assert GA.rf_mat_det(one).eqrf(GA.RF1)
    return True


def check_metric_is_painleve_gullstrand():
    gs = {}
    for bt in BETAS:
        hi = [GA.add(a, GA.scal(bt, P(a))) for a in FRAME]
        gs[bt] = [[GA.dot(hi[i], hi[j], S13) for j in range(4)] for i in range(4)]
    want = {(0, 0): lambda x: 1 - x * x, (0, 1): lambda x: -x, (1, 1): lambda x: F(-1),
            (2, 2): lambda x: F(-1), (3, 3): lambda x: F(-1)}
    for i in range(4):
        for j in range(4):
            ys = [gs[bt][i][j] for bt in BETAS]
            f = want.get((min(i, j), max(i, j)), lambda x: F(0))
            assert ys == [f(bt) for bt in BETAS]
            assert lagrange(BETAS[:3], ys[:3], BETAS[4]) == ys[4]
    return True


def check_folding_onto_kernel_direction():
    premise("singularity.degeneration-exactly")
    for bt in (F(1), F(3), F(20)):
        for sgn in (1, -1):
            lam = -bt + sgn
            x = GA.add(GA.add(ET, GA.scal(lam, ER)), GA.scal(bt, P(GA.add(ET, GA.scal(lam, ER)))))
            assert GA.mul(x, x, S13).get((), F(0)) == 0
            if bt > 1:
                cf = 1 / lam
                assert cf < 0 and abs(cf) * (bt - 1) <= 1
    assert GA.is_zero(P(ER))
    return True
