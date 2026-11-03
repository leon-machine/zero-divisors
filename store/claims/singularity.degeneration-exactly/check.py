"""singularity.degeneration-exactly: exact checks in Gauge Theory Gravity.

Flat spacetime: Cl(1,3) in GA.py, signature (+,-,-,-), frame e_t, e_r, e_theta, e_phi = gamma_0..gamma_3.
The PG gauge field hb(a) = a - beta (a.e_t) e_r = (1 - beta P)(a), its inverse 1 + beta P, and the
derived metric g(a,b) = hb^{-1}(a) . hb^{-1}(b) (GA.dot). Identities in beta are checked over Q(beta)
(GA.RF), so they hold at every finite beta.
(1) The map: beta^{-1} hb = beta^{-1} - P as matrices over Q(beta); P has rank 1, image R e_r (the
    image of e_t, which spans it), and kernel, computed exactly, equal to e_t-perp =
    span(e_r, e_theta, e_phi) (the kernel of a -> a . e_t).
(2) The metric: for all 16 frame pairs, beta^{-2} g(a,b) = -(a.e_t)(b.e_t) + beta^{-1}[(a.e_t)(b.e_r) +
    (b.e_t)(a.e_r)] + beta^{-2}(a.b) over Q(beta) (g computed in GA at five beta values and matched to
    the polynomial of degree 2 that it is); the limit form ghat(a,b) = -(a.e_t)(b.e_t) has congruence
    signature (0, 1, 3) and radical (kernel of its matrix) equal to ker P = e_t-perp.
(3) e_r lies in the radical and ghat(e_r, e_r) = 0, while g(e_r, e_r) = -1 at every beta (identity).
"""
from fractions import Fraction as F

import GA

S13 = GA.sig(1, 3)
ET, ER = GA.gen(0), GA.gen(1)
FRAME = [GA.gen(i) for i in range(4)]
BETAS = [F(1, 3), F(1), F(5, 2), F(7), F(50)]


def P(a):
    return GA.scal(GA.dot(a, ET, S13), ER)


def col(x):
    return [x.get((i,), F(0)) for i in range(4)]


def interp2(xs, ys, x):
    """Value at x of the polynomial of degree <= len(xs)-1 through (xs, ys) (Lagrange, exact)."""
    tot = F(0)
    for i, xi in enumerate(xs):
        term = ys[i]
        for j, xj in enumerate(xs):
            if j != i:
                term = term * (x - xj) / (xi - xj)
        tot += term
    return tot


def check_rescaled_map_limit_rank_one():
    b = GA.RF.var()
    Pm = [[P(FRAME[j]).get((i,), F(0)) for j in range(4)] for i in range(4)]
    hbm = [[GA.RF.const(F(1 if i == j else 0)) - b * GA.RF.const(Pm[i][j]) for j in range(4)]
           for i in range(4)]
    for i in range(4):
        for j in range(4):
            lhs = hbm[i][j] / b
            rhs = GA.RF.const(F(1 if i == j else 0)) / b - GA.RF.const(Pm[i][j])
            assert lhs.eqrf(rhs)
    assert GA.mat_rank(Pm) == 1
    assert col(P(ET)) == [0, 1, 0, 0]
    ker = GA.field_kernel(Pm)
    perp = GA.field_kernel([[GA.dot(FRAME[j], ET, S13) for j in range(4)]])
    assert len(ker) == 3 and len(perp) == 3
    want = [col(GA.gen(i)) for i in (1, 2, 3)]
    assert GA.rank_of_vectors(ker + want) == 3 and GA.rank_of_vectors(perp + ker) == 3
    return True


def check_rescaled_metric_limit_form():
    xs = [F(1) / bt for bt in BETAS]              # u = beta^{-1}
    for a in FRAME:
        for c in FRAME:
            ys = []
            for bt in BETAS:
                ha, hc = GA.add(a, GA.scal(bt, P(a))), GA.add(c, GA.scal(bt, P(c)))
                ys.append(GA.dot(ha, hc, S13) / (bt * bt))
            at, ct = GA.dot(a, ET, S13), GA.dot(c, ET, S13)
            ar, cr = GA.dot(a, ER, S13), GA.dot(c, ER, S13)
            pred = [-(at * ct) + u * (at * cr + ct * ar) + u * u * GA.dot(a, c, S13) for u in xs]
            assert ys == pred
            # the data lie on one quadratic in u, so the identity holds for every beta
            assert interp2(xs[:3], ys[:3], xs[4]) == ys[4]
            assert interp2(xs[:3], ys[:3], F(0)) == -(at * ct)
    ghat = [[-(GA.dot(a, ET, S13) * GA.dot(c, ET, S13)) for c in FRAME] for a in FRAME]
    assert GA.congruence_signature(ghat) == (0, 1, 3)
    rad = GA.field_kernel(ghat)
    Pm = [[P(FRAME[j]).get((i,), F(0)) for j in range(4)] for i in range(4)]
    assert len(rad) == 3 and GA.rank_of_vectors(rad + GA.field_kernel(Pm)) == 3
    return True


def check_folded_direction_is_null_for_limit_form_only():
    ghat_er = [-(GA.dot(ER, ET, S13) * GA.dot(c, ET, S13)) for c in FRAME]
    assert ghat_er == [0, 0, 0, 0]
    b = GA.RF.var()
    # g(e_r, e_r) over Q(beta): hb^{-1}(e_r) = e_r + beta (e_r . e_t) e_r
    coef = GA.RF1 + b * GA.RF.const(GA.dot(ER, ET, S13))
    g_rr = coef * coef * GA.RF.const(GA.dot(ER, ER, S13))
    assert g_rr.eqrf(GA.RF.const(-1))
    for bt in BETAS:
        h = GA.add(ER, GA.scal(bt, P(ER)))
        assert GA.dot(h, h, S13) == -1
    return True
