"""standard-model.frozen-point-first-rung-component: exact checks.

Conventions (root paper): R^{2,4} = R^{1,3} + H_1 with e_+ (+1), spacetime f0 (+1), f1, f2, f3 (-1), e_- (-1)
(GA indices 0, 1..4, 5); nO = (e_- - e_+)/2, nInf = e_- + e_+.
(1) nO and nInf are null with nO . nInf = -1; a vector s nO + t nInf of H_1 has norm -2st (sample (s, t));
    with the scale slot t = 1 and Q(I) = Lambda/3 the nO coefficient is forced to -Lambda/6 (the one solution
    of the linear equation -2s = Lambda/3); I = nInf - (Lambda/6) nO has no spacetime component and
    Q(I) = Lambda/3 for six values of Lambda, and is the null nInf at Lambda = 0.
(2) The complex unit I_4 = f0 f1 f2 f3 squares to -1, commutes with e_+, e_- (so with H_1) and anticommutes
    with the spacetime vectors; H_1 + I_4 H_1 is four-dimensional (H_1 tensor C).
(3) Pair mode: W = span(nInf, f0 + f1, f2 + i f3) is maximal isotropic in V_C and W' = span(nO, f0 - f1,
    f2 - i f3) is an isotropic complement dual to it (pairing matrix diagonal and invertible, W + W' = V_C):
    H_1 tensor C = span(nInf, nO) is one pair mode of W with its dual partner.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = (1, 1, -1, -1, -1, -1)
EP, EM_ = GA.gen(0), GA.gen(5)
NO = GA.scal(F(1, 2), GA.sub(EM_, EP))
NINF = GA.add(EM_, EP)
SPACETIME = [GA.gen(a) for a in (1, 2, 3, 4)]
LAMBDAS = [F(0), F(1), F(-3), F(2, 7), F(6), F(-1, 5)]
ST_SAMPLES = [(F(1), F(1)), (F(2), F(-3)), (F(1, 2), F(5, 4))]
QI = GA.QI


def dot(x, y):
    return GA.dot(x, y, SQ)


def check_frozen_point_is_a_rung_vector():
    premise("standard-model.imported-frozen-point-grip-thirteenth-refutation")
    ok = True
    ok = ok and dot(NO, NO) == 0 and dot(NINF, NINF) == 0 and dot(NO, NINF) == -1
    for s, t in ST_SAMPLES:
        v = GA.add(GA.scal(s, NO), GA.scal(t, NINF))
        ok = ok and dot(v, v) == -2 * s * t
    for L in LAMBDAS:
        # scale slot t = 1 and Q = Lambda/3: the linear equation -2 s = Lambda/3 has the one root s = -Lambda/6
        s = (L / 3) / F(-2)
        ok = ok and s == -L / 6
        I = GA.sub(NINF, GA.scal(L / 6, NO))
        ok = ok and dot(I, I) == L / 3
        ok = ok and all(dot(I, f) == 0 for f in SPACETIME)
        ok = ok and set(I) <= {(0,), (5,)}
        if L == 0:
            ok = ok and GA.eq(I, NINF) and dot(I, I) == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_frozen_point_is_a_rung_vector"; return _tp_rv


def check_rung_plane_is_a_pair_mode():
    premise("standard-model.imported-fock-model-twistor-space")
    ok = True
    I4 = GA.mul(GA.mul(SPACETIME[0], SPACETIME[1], SQ), GA.mul(SPACETIME[2], SPACETIME[3], SQ), SQ)
    ok = ok and GA.eq(GA.mul(I4, I4, SQ), GA.sc(-1))
    ok = ok and GA.commutes(I4, EP, SQ) and GA.commutes(I4, EM_, SQ)
    ok = ok and all(GA.anticommutes(I4, f, SQ) for f in SPACETIME)
    span = [EP, EM_, GA.mul(I4, EP, SQ), GA.mul(I4, EM_, SQ)]
    blades = sorted({b for x in span for b in x})
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in span]) == 4

    def cv(*c):
        return [QI(x) if not isinstance(x, QI) else x for x in c]

    def ipc(u, v):
        return sum((SQ[a] * u[a] * v[a] for a in range(6)), QI(0))
    nInf = cv(1, 0, 0, 0, 0, 1)
    nO = cv(F(-1, 2), 0, 0, 0, 0, F(1, 2))
    W = [nInf, cv(0, 1, 1, 0, 0, 0), cv(0, 0, 0, 1, QI(0, 1), 0)]
    Wd = [nO, cv(0, 1, -1, 0, 0, 0), cv(0, 0, 0, 1, QI(0, -1), 0)]
    ok = ok and all(ipc(x, y) == QI(0) for x in W for y in W)
    ok = ok and all(ipc(x, y) == QI(0) for x in Wd for y in Wd)
    pairing = [[ipc(x, y) for y in Wd] for x in W]
    ok = ok and pairing == [[QI(-1), QI(0), QI(0)], [QI(0), QI(2), QI(0)], [QI(0), QI(0), QI(-2)]]
    ok = ok and GA.field_rank(W + Wd) == 6
    _tp_rv = (ok); assert _tp_rv is not False, "check_rung_plane_is_a_pair_mode"; return _tp_rv
