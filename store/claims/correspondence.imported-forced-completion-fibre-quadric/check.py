"""correspondence.imported-forced-completion-fibre-quadric: exact checks for Cl(1,3).

(1) Type-N zero divisor with no element-level resolution: v = e0 + e1 in Cl(1,3) is a nonzero
    null vector, a zero divisor (v v = 0) with no inverse; in Cl(1,3) and in Cl(2,4) every sample
    pseudo-inverse sigma = w0 + alpha + v beta + v w0 delta (v sigma v = v) is moved by the null
    rotation R = 1 + v e2 = u' e2 / Q(e2) (u' = e2 + Q(e2) v), which fixes v: R sigma R^{-1} - sigma + e2
    is killed by v while v e2 != 0, so no equivariant resolution exists (the transvection no-go).
(2) The minimal completion is Cl(1,3) -> Cl(2,4). Minimality, in the sense of transport.minimality (a null-lift
    completion W must make X(x) = f(x) + x null for every x, so Q_W(f(x)) = -Q(x), with f(0) a nonzero null
    vector of W): W = 0 fails since X(e0) = e0 has Q = 1; every one-dimensional W, Gram [g] with g != 0
    (sampled over both signs), fails twice, since f(0) = t e has g t^2 = 0 only at t = 0, and the equations
    g t^2 = -Q(e0) = -1 and g t^2 = -Q(e1) = 1 need t^2 of opposite signs. Hence dim W >= 2; a two-dimensional
    admissible complement is a hyperbolic plane (sample Grams reduce to [[0,1],[1,0]]), so the completion is
    unique up to isomorphism, and the conformal model exported by transport.minimality has signature (2,4).
(3) The resolving assignments lie on the quadric of null rays of R^(2,4): the lifts X(x) of sample
    x in R^(1,3) are null; iota X(x) = e+ X(x) e+ is null and nonzero for every sample, equal to
    -Q(x) X(x/Q(x)) on invertible x and to -(x0 + ninf/2) on null x0 (v, 3v, 0), an ideal point.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def check_type_n_zero_divisor_has_no_element_level_resolution():
    premise("transport.no-go-level-elements")
    ok = True
    for ascent in (False, True):
        sq = GA.sig(1, 3) + ((1, -1) if ascent else ())
        v = GA.add(GA.gen(0), GA.gen(1))
        w0 = GA.scal(F(1, 4), GA.sub(GA.gen(0), GA.gen(1)))
        u = GA.gen(2)
        ok = ok and GA.is_zero(GA.mul(v, v, sq)) and GA.dot(v, w0, sq) == F(1, 2)
        Qu = GA.mul(u, u, sq).get((), F(0))
        ok = ok and Qu == -1
        R = GA.add(GA.sc(1), GA.mul(v, u, sq))
        Rinv = GA.sub(GA.sc(1), GA.mul(v, u, sq))
        ok = ok and GA.eq(GA.mul(R, Rinv, sq), GA.sc(1))
        ok = ok and GA.eq(GA.scal(1 / Qu, GA.mul(GA.add(u, GA.scal(Qu, v)), u, sq)), R)
        ok = ok and GA.eq(GA.mul(GA.mul(R, v, sq), Rinv, sq), v)
        e3 = GA.gen(3)
        extra = GA.gen(4) if ascent else GA.sc(2)
        samples = [({}, {}, {}),
                   (GA.add(GA.sc(1), GA.mul(u, e3, sq)), GA.scal(3, e3), {}),
                   (GA.scal(F(1, 2), extra), GA.sc(-1), GA.add(e3, GA.sc(4))),
                   (GA.mul(e3, extra, sq), {}, GA.scal(5, GA.mul(u, e3, sq)))]
        for alpha, beta, delta in samples:
            sigma = GA.add(w0, alpha, GA.mul(v, beta, sq), GA.mul(GA.mul(v, w0, sq), delta, sq))
            ok = ok and GA.eq(GA.mul(GA.mul(v, sigma, sq), v, sq), v)
            moved = GA.mul(GA.mul(R, sigma, sq), Rinv, sq)
            ok = ok and GA.is_zero(GA.mul(v, GA.add(GA.sub(moved, sigma), u), sq))
            ok = ok and not GA.eq(moved, sigma) and not GA.is_zero(GA.mul(v, u, sq))
    GA.check("type-N divisor e0 + e1 of Cl(1,3): every pseudo-inverse moved by a null rotation fixing it", ok)
    return ok


def check_minimal_completion_is_cl24():
    ex = premise("transport.minimality")
    M = ex["conformal"](1, 3)
    sq = M["sq"]
    ok = True
    basis = [GA.gen(i) for i in range(6)]
    G = [[GA.dot(a, b, sq) for b in basis] for a in basis]
    ok = ok and GA.congruence_signature(G) == (2, 4, 0)
    # no completion below dimension two: W = 0 and every one-dimensional W fail
    e0, e1 = GA.gen(0), GA.gen(1)
    s13 = GA.sig(1, 3)
    Q0, Q1 = GA.mul(e0, e0, s13).get((), F(0)), GA.mul(e1, e1, s13).get((), F(0))
    ok = ok and (Q0, Q1) == (1, -1)                              # X(x) = x is not null at x = e0
    for g in (F(1), F(-1), F(3, 2), F(-5), F(1, 7)):
        need = [-Q0 / g, -Q1 / g]                                # t^2 that g t^2 = -Q(x) requires
        ok = ok and min(need) < 0 and need[0] * need[1] == -1 / (g * g)
        ok = ok and all(g * t * t != 0 for t in (F(1), F(-2), F(1, 3)))   # f(0) = t e is never null for t != 0
    for Gw in ([[1, 2], [2, 3]], [[0, 3], [3, -1]], [[2, 1], [1, -4]]):
        Gw = [[F(x) for x in r] for r in Gw]
        a, b, c = Gw[0][0], Gw[0][1], Gw[1][1]
        # null vector (x, 1) with a x^2 + 2 b x + c = 0 (roots are rational for these samples)
        if a == 0:
            v = [F(1), F(0)]
        else:
            disc = b * b - a * c
            r = next(F(k, 1) for k in range(0, 50) if F(k * k) == disc)
            v = [(-b + r) / a, F(1)]
        Gv = [sum(Gw[i][j] * v[j] for j in range(2)) for i in range(2)]
        k = 0 if Gv[0] != 0 else 1
        w = [F(0), F(0)]
        w[k] = 1 / Gv[k]
        qw = sum(Gw[i][j] * w[i] * w[j] for i in range(2) for j in range(2))
        w = [w[i] - qw / 2 * v[i] for i in range(2)]
        gram = [[sum(Gw[i][j] * x[i] * y[j] for i in range(2) for j in range(2)) for y in (v, w)] for x in (v, w)]
        ok = ok and gram == [[0, 1], [1, 0]] and GA.congruence_signature(Gw) == (1, 1, 0)
    GA.check("no completion of Cl(1,3) below dimension two; the two-dimensional complement is a hyperbolic plane, giving Cl(2,4)", ok)
    return ok


def check_assignments_on_null_quadric_of_r24():
    ex = premise("transport.minimality")
    premise("transport.totality")
    M = ex["conformal"](1, 3)
    sq = M["sq"]
    ok = True
    xs = [[1, 2, -1, 3], [F(1, 2), -3, 2, 1], [2, 0, 1, 1], [0, 0, 1, 0]]
    nulls = [[1, 1, 0, 0], [3, 3, 0, 0], [0, 0, 0, 0], [5, 3, 4, 0]]
    for cs in xs + nulls:
        x = M["vec"](cs)
        Qx = M["Q"](x)
        Xx = M["X"](x)
        I = M["iota"](Xx)
        ok = ok and GA.is_zero(GA.mul(Xx, Xx, sq)) and GA.is_zero(GA.mul(I, I, sq)) and not GA.is_zero(I)
        if cs in nulls:
            ok = ok and Qx == 0 and GA.eq(I, GA.scal(-1, GA.add(x, GA.scal(F(1, 2), M["ninf"]))))
            ok = ok and GA.dot(I, M["ninf"], sq) == 0             # n0-coefficient zero: ideal
        else:
            ok = ok and Qx != 0 and GA.eq(I, GA.scal(-Qx, M["X"](GA.scal(1 / Qx, x))))
    GA.check("lifts and their transported reciprocals lie on the null quadric of R^(2,4); null x0 ideal", ok)
    return ok
