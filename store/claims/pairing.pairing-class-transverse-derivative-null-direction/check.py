"""pairing.pairing-class-transverse-derivative-null-direction: exact checks.

Cl(1,3) in GA.py, eta = diag(1, -1, -1, -1), l = e0 + e1, m = e2 + i e3; complex quantities as Gaussian rationals
(GA.QI); pv(B) = <B . l, m>, B . v = [B, v]/2 (Proposition pairing.stabiliser-parabolic-algebra-null-direction).
A connection is given by matrices w(X)^a_b with nabla_X e_b = w^a_b e_a, and
Omega(X) = sum_{a<b} w^{ab} e_a e_b, w^{ab} = w^a_c eta^{cb}.
(1) Omega reproduces nabla: [Omega(X), e_b]/2 = nabla_X e_b for every b, for the static Schwarzschild frame at
    M = 1/2 (F = sqrt f rational, r = 1/(1 - F^2), f' = 1/r^2, cot(theta) = 3/4 sampled; nabla_{e0} e0 =
    f'/(2F) e1, nabla_{e2} e1 = (F/r) e2, nabla_{e3} e2 = (cot/r) e3, ...) and for random metric-compatible
    rational connection matrices; the frame connections are metric compatible.
(2) The identity pv(Omega(X)) = <nabla_X l, m> for X = e0, e1, e2, e3 and complex combinations, with nabla_X l
    computed from the matrices; Schwarzschild values 0, 0, -F/r, -i F/r.
(3) Rescaling by lambda = F/(1 + F): with the derivative term (e1 lambda) l, e1 lambda = M/(r^2 (1 + F)^2)
    (nonzero), <nabla_X(lambda l), m> = lambda <nabla_X l, m> and pv relative to lambda l is lambda pv, every X.
(4) Real directions: on a grid of real X (Schwarzschild frames) and for four random metric-compatible
    connections (two with vanishing class), pv(Omega(X)) = 0 exactly when nabla_X l is a multiple of l; for the complex direction m, nabla_m l = (F/r) m has pv = 0 but is not a
    multiple of l (the stated failure).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
S13 = GA.sig(1, 3)
ETA = [1, -1, -1, -1]
FS = [F(1, 2), F(3, 5), F(1, 3)]
COT = F(3, 4)
GRID = [(1, 0, 0, 0), (0, 1, 0, 0), (2, -3, 0, 0), (0, 0, 1, 0), (1, 1, 0, 2), (0, 0, 3, -1), (5, 0, -1, 0)]
RANDOM_W = [[(0, 1, 2), (0, 3, -1), (1, 2, 3), (2, 3, 1)], [(0, 1, -2), (1, 3, 5), (0, 2, 1)]]
L_VEC = GA.add(GA.gen(0), GA.gen(1))


def frame_connection(Fv):
    """w[X][a][b]: nabla_{e_X} e_b = sum_a w[X][a][b] e_a, static Schwarzschild frame at M = 1/2."""
    r = 1 / (1 - Fv * Fv)
    acc = (1 / (r * r)) / (2 * Fv)
    k = Fv / r
    c = COT / r
    w = [[[F(0)] * 4 for _ in range(4)] for _ in range(4)]
    w[0][1][0] = acc
    w[0][0][1] = acc
    w[2][2][1] = k
    w[2][1][2] = -k
    w[3][3][1] = k
    w[3][1][3] = -k
    w[3][3][2] = c
    w[3][2][3] = -c
    return w, r


def random_connection(spec):
    """Metric-compatible: w^{ab} antisymmetric, from (a, b, value) with a < b; w^a_b = w^{ac} eta_cb."""
    up = [[F(0)] * 4 for _ in range(4)]
    for a, b, v in spec:
        up[a][b] = F(v)
        up[b][a] = -F(v)
    return [[up[a][b] * ETA[b] for b in range(4)] for a in range(4)]


def omega_bivector(wX):
    out = {}
    for a in range(4):
        for b in range(a + 1, 4):
            wab = wX[a][b] * ETA[b]          # w^{ab} = w^a_b eta^{bb}
            if wab:
                out = GA.add(out, GA.scal(wab, GA.mul(GA.gen(a), GA.gen(b), S13)))
    return out


def nabla_vec(wX, comps):
    return {(a,): sum(wX[a][b] * comps[b] for b in range(4)) for a in range(4)
            if sum(wX[a][b] * comps[b] for b in range(4)) != 0}


def dot_m(v):
    return QI(GA.dot(v, GA.gen(2), S13), GA.dot(v, GA.gen(3), S13))


def pv(B):
    Bl = GA.scal(F(1, 2), GA.sub(GA.mul(B, L_VEC, S13), GA.mul(L_VEC, B, S13)))
    return dot_m(Bl)


def compatible(wX):
    return all(wX[a][b] * ETA[a] + wX[b][a] * ETA[b] == 0 for a in range(4) for b in range(4))


def check_omega_reproduces_the_connection():
    ok = True
    conns = [frame_connection(Fv)[0][X] for Fv in FS for X in range(4)] + [random_connection(s) for s in RANDOM_W]
    for wX in conns:
        ok = ok and compatible(wX)
        Om = omega_bivector(wX)
        for b in range(4):
            e = GA.gen(b)
            half = GA.scal(F(1, 2), GA.sub(GA.mul(Om, e, S13), GA.mul(e, Om, S13)))
            ok = ok and GA.eq(half, nabla_vec(wX, [F(1) if i == b else F(0) for i in range(4)]))
    _tp_rv = (ok and len(conns) == 14); assert _tp_rv is not False, "check_omega_reproduces_the_connection"; return _tp_rv


def check_pairing_class_is_transverse_derivative():
    premise("pairing.stabiliser-parabolic-algebra-null-direction")
    ok = True
    for Fv in FS:
        w, r = frame_connection(Fv)
        expected = [QI(0), QI(0), QI(-Fv / r), QI(0, -Fv / r)]
        for X in range(4):
            Om = omega_bivector(w[X])
            dl = nabla_vec(w[X], [F(1), F(1), F(0), F(0)])
            ok = ok and pv(Om) == dot_m(dl) == expected[X]
        # complex direction X = e2 + i e3 by linearity: pv = -F/r + i(-i F/r) = 0
        ok = ok and expected[2] + QI(0, 1) * expected[3] == 0
    for spec in RANDOM_W:
        wX = random_connection(spec)
        ok = ok and pv(omega_bivector(wX)) == dot_m(nabla_vec(wX, [F(1), F(1), F(0), F(0)]))
    _tp_rv = (ok); assert _tp_rv is not False, "check_pairing_class_is_transverse_derivative"; return _tp_rv


def check_class_scales_with_the_null_direction():
    premise("pairing.stabiliser-parabolic-algebra-null-direction")
    ok = True
    M = F(1, 2)
    for Fv in FS:
        w, r = frame_connection(Fv)
        lam = Fv / (1 + Fv)
        dlam = [F(0), M / (r * r * (1 + Fv) ** 2), F(0), F(0)]       # e_X(lambda)
        # e1(lambda) = F (dlambda/dF)(dF/dr) with dF/dr = M/(r^2 F), written in F: (1 - F^2)^2 / (2 (1 + F)^2)
        ok = ok and dlam[1] == F(1, 2) * (1 - Fv * Fv) ** 2 / (1 + Fv) ** 2
        for X in range(4):
            Om = omega_bivector(w[X])
            dl = nabla_vec(w[X], [F(1), F(1), F(0), F(0)])
            dlam_l = GA.add(GA.scal(lam, dl), GA.scal(dlam[X], L_VEC))
            ok = ok and dot_m(dlam_l) == QI(lam) * dot_m(dl)
            Bl = GA.scal(F(1, 2), GA.sub(GA.mul(Om, GA.scal(lam, L_VEC), S13), GA.mul(GA.scal(lam, L_VEC), Om, S13)))
            ok = ok and dot_m(Bl) == QI(lam) * pv(Om)
        ok = ok and dlam[1] != 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_class_scales_with_the_null_direction"; return _tp_rv


def check_real_directions_parallel_exactly_when_class_vanishes():
    premise("pairing.stabiliser-parabolic-algebra-null-direction")
    ok = True
    zeros = 0
    for Fv in FS:
        w, r = frame_connection(Fv)
        for xs in GRID:
            wX = [[sum(F(xs[X]) * w[X][a][b] for X in range(4)) for b in range(4)] for a in range(4)]
            dl = nabla_vec(wX, [F(1), F(1), F(0), F(0)])
            vanish = pv(omega_bivector(wX)) == 0
            prop = GA.rank_of_vectors([[dl.get((a,), F(0)) for a in range(4)], [F(1), F(1), F(0), F(0)]]) <= 1
            ok = ok and vanish == prop
            zeros += vanish
        # complex direction m: nabla_m l = (F/r)(e2 + i e3) = (F/r) m, class 0, not a multiple of l
        re = nabla_vec(w[2], [F(1), F(1), F(0), F(0)])
        im = nabla_vec(w[3], [F(1), F(1), F(0), F(0)])
        ok = ok and GA.eq(re, GA.scal(Fv / r, GA.gen(2))) and GA.eq(im, GA.scal(Fv / r, GA.gen(3)))
        ok = ok and dot_m(re) + QI(0, 1) * dot_m(im) == 0 and re != {}
    # random metric-compatible connections, two with a nonzero class and two (the second with cancelling
    # w^{02} = w^{12}) with nabla l a nonzero multiple of l
    rzeros = 0
    for spec in RANDOM_W + [[(0, 1, 3), (2, 3, -2)], [(0, 1, -1), (0, 2, 1), (1, 2, 1), (2, 3, 4)]]:
        wX = random_connection(spec)
        dl = nabla_vec(wX, [F(1), F(1), F(0), F(0)])
        vanish = pv(omega_bivector(wX)) == 0
        prop = GA.rank_of_vectors([[dl.get((a,), F(0)) for a in range(4)], [F(1), F(1), F(0), F(0)]]) <= 1
        ok = ok and vanish == prop and dl != {}
        rzeros += vanish
    _tp_rv = (ok and zeros == 9 and rzeros == 2); assert _tp_rv is not False, "check_real_directions_parallel_exactly_when_class_vanishes"; return _tp_rv
