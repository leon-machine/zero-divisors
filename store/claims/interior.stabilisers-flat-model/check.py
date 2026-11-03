"""interior.stabilisers-flat-model: exact checks in Cl(2,4).

V = the vectors of Cl(2,4) (GA.py: generators 0..3 of squares +1, -1, -1, -1 span W = R^{1,3}, then e+ (+1),
e- (-1)); n0 = (e+ + e-)/2, ninf = e+ - e- (null, n0 . ninf = 1). A bivector B acts on V by the commutator
product, which is (a ^ b)(v) = (b.v) a - (a.v) b. Point tractors X(x) = n0 + x - Q(x)/2 ninf.
(1) The stabiliser of the vector ninf, computed as a kernel on the 15 bivectors, has dimension 10 and is
    spanned by Lambda^2 W (6) and ninf ^ W (4); ninf ^ W is an abelian ideal on which Lambda^2 W acts
    (the Poincare algebra); (n0 ^ w)(ninf) = -w.
(2) The stabiliser of the ray (B(ninf) in R ninf) has dimension 11; (ninf ^ n0)(ninf) = ninf; it is a
    maximal subalgebra: adding any one of the four n0 ^ e_i generates all 15 dimensions.
(3) N = ninf ^ w: N^3 = 0, the image of N^2 lies in R ninf, N^2(v) = -(ninf . v) Q(w) ninf on every
    basis vector, so N^2 = 0 exactly for null w (one-step) and N^2 != 0 for non-null w (two-step), on the
    basis and on sample null and non-null w; exp(tN) X(x) = X(x - t w) exactly (the series stops at t^2),
    so the nilradical acts on the point space as the translations, and X(x) is null with
    X(x) . X(y) = -Q(x - y)/2.
"""
from fractions import Fraction as F

import GA

S24 = (1, -1, -1, -1, 1, -1)
N0 = GA.scal(F(1, 2), GA.add(GA.gen(4), GA.gen(5)))
NI = GA.sub(GA.gen(4), GA.gen(5))
BL2 = [b for b in GA.all_blades(6) if len(b) == 2]
VB = [(i,) for i in range(6)]
W = [GA.gen(i) for i in range(4)]


def cm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S24), GA.mul(Y, X, S24)))


def dt(a, b):
    return GA.dot(a, b, S24)


def co(x, basis):
    return [x.get(b, F(0)) for b in basis]


def w4(c):
    return GA.add(*[GA.scal(F(c[i]), W[i]) for i in range(4)])


def point(x):
    xv = w4(x)
    return GA.add(N0, xv, GA.scal(-dt(xv, xv) / 2, NI))


LEVI = [cm(W[i], W[j]) for i in range(4) for j in range(i + 1, 4)]
NIL = [cm(NI, w) for w in W]
SAMPLE_W = [[1, 1, 0, 0], [3, 0, 4, 0], [2, 1, 0, 0], [0, 1, 2, -1], [1, 2, 0, 0]]
# The coordinate basis of W, run through the nilradical identities before the samples.
UNIT_W = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
# Flow parameters t for exp(tN) X(x) = X(x - t w).
SAMPLE_T = (F(3, 2), F(-2, 5))
# The named null and non-null directions e0 + e1 and 2 e0 + e1 (both also in SAMPLE_W).
NULL_W = [1, 1, 0, 0]
NONNULL_W = [2, 1, 0, 0]
SAMPLE_X = [[2, F(1, 3), -1, 4], [F(-1, 2), 5, 0, 1], [F(-7, 3), 0, F(11, 5), F(-1, 2)]]


def span_rank(elems):
    return GA.rank_of_vectors([co(x, BL2) for x in elems])


def generated_dim(gens):
    basis = list(gens)
    while True:
        r = span_rank(basis)
        new = basis + [cm(a, b) for a in basis for b in basis]
        if span_rank(new) == r:
            return r
        # keep an independent spanning set
        keep = []
        for x in new:
            if span_rank(keep + [x]) > len(keep):
                keep.append(x)
        basis = keep


def check_vector_stabiliser_is_poincare():
    cols = [co(cm({b: F(1)}, NI), VB) for b in BL2]
    ker = GA.field_kernel([list(r) for r in zip(*cols)])
    ok = len(ker) == 10
    stab = [{BL2[i]: k[i] for i in range(15) if k[i]} for k in ker]
    ok = ok and all(GA.is_zero(cm(B, NI)) for B in LEVI + NIL)
    ok = ok and span_rank(LEVI) == 6 and span_rank(NIL) == 4
    ok = ok and span_rank(LEVI + NIL) == 10 and span_rank(LEVI + NIL + stab) == 10
    ok = ok and all(GA.is_zero(cm(a, b)) for a in NIL for b in NIL)
    ok = ok and all(span_rank(NIL + [cm(L, N)]) == 4 for L in LEVI for N in NIL)
    ok = ok and all(span_rank(LEVI + [cm(a, b)]) == 6 for a in LEVI for b in LEVI)
    ok = ok and all(GA.eq(cm(cm(N0, w), NI), GA.neg(w)) for w in W)
    _tp_rv = (ok); assert _tp_rv is not False, "check_vector_stabiliser_is_poincare"; return _tp_rv


def check_ray_stabiliser_is_maximal_parabolic():
    keep = [i for i in range(6) if i not in (4, 5)]
    # B(ninf) in R ninf: the components of B(ninf) along W and along n0 vanish
    cols = []
    for b in BL2:
        y = cm({b: F(1)}, NI)
        cols.append([y.get((i,), F(0)) for i in keep] + [dt(y, NI)])
    ker = GA.field_kernel([list(r) for r in zip(*cols)])
    ok = len(ker) == 11
    grading = cm(NI, N0)
    ok = ok and GA.eq(cm(grading, NI), NI)
    par = LEVI + NIL + [grading]
    ok = ok and span_rank(par) == 11 and generated_dim(par) == 11
    for w in W:
        ok = ok and generated_dim(par + [cm(N0, w)]) == 15
    _tp_rv = (ok); assert _tp_rv is not False, "check_ray_stabiliser_is_maximal_parabolic"; return _tp_rv


def check_nilradical_null_shears_and_translations():
    ok = True
    basis = [GA.gen(i) for i in range(len(S24))]
    for wc in UNIT_W + SAMPLE_W:
        w = w4(wc)
        Nw = cm(NI, w)
        q = dt(w, w)
        N1 = lambda v: cm(Nw, v)
        for v in basis:
            n2 = N1(N1(v))
            ok = ok and GA.eq(n2, GA.scal(-dt(NI, v) * q, NI))
            ok = ok and GA.is_zero(N1(n2))
        two_step = any(not GA.is_zero(N1(N1(v))) for v in basis)
        one_nonzero = any(not GA.is_zero(N1(v)) for v in basis)
        ok = ok and one_nonzero and two_step == (q != 0)
        for t in SAMPLE_T:
            for x in SAMPLE_X:
                X = point(x)
                eX = GA.add(X, GA.scal(t, N1(X)), GA.scal(t * t / 2, N1(N1(X))))
                xs = [F(x[i]) - t * wc[i] for i in range(4)]
                ok = ok and GA.eq(eX, point(xs))
    for xa in SAMPLE_X:
        for xb in SAMPLE_X:
            d = w4([F(xa[i]) - F(xb[i]) for i in range(4)])
            ok = ok and dt(point(xa), point(xa)) == 0 and dt(point(xa), point(xb)) == -dt(d, d) / 2
    # null w = e0 + e1 is one-step; w = 2 e0 + e1 has Q = 4 - 1 = 3 (by hand)
    wn, wq = w4(NULL_W), w4(NONNULL_W)
    ok = ok and dt(wn, wn) == 0 and dt(wq, wq) == 3
    _tp_rv = (ok); assert _tp_rv is not False, "check_nilradical_null_shears_and_translations"; return _tp_rv
