"""standard-model.what-derived-what-not: exact checks of the computable part of (1) and (2).

GA model of the two rungs' hyperbolic planes (the spacetime part plays no role): Cl(2,2) with
e_+ (square +1), e_- (square -1) for the first rung and e_+', e_-' for the second;
n_O = (e_- - e_+)/2, n_inf = e_- + e_+ (null, n_O . n_inf = -1), and likewise primed; the second
rung's mode vectors are v_4 = n_inf'/2, w_4 = -n_O' (v_4 . w_4 = 1/2, i.e. v w + w v = 1).
At several rational Lambda: the frozen point I = n_inf - (Lambda/6) n_O has Q(I) = Lambda/3; its lift
X(I) = n_O' + I + (Lambda/6) n_inf' is null; the rung component is -w_4 + (Lambda/3) v_4, orthogonal to
the first rung, of norm -Lambda/3, with coefficient one on -w_4 for every Lambda (the lift's
normalisation) and the conjugate direction v_4 entering at order Lambda; the reciprocal's lift has rung
component v_4 - (Lambda/3) w_4. The rung directions are the doublet directions: w_4 and v_4 carry
2T_3 = -1, +1 and Y = -1/2, +1/2 (checked on the Fock module's commutators).
The unit conversion of (2): 246 GeV / (1.4 x 10^-42 GeV) lies between 10^44 and 10^45.
Clause (3) is a statement of scope and is not checked.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = [F(1), F(-1), F(1), F(-1)]           # e_+, e_-, e_+', e_-'
EP, EM, EP2, EM2 = (GA.gen(i) for i in range(4))
HALF = F(1, 2)
NO, NINF = GA.scal(HALF, GA.sub(EM, EP)), GA.add(EM, EP)
NO2, NINF2 = GA.scal(HALF, GA.sub(EM2, EP2)), GA.add(EM2, EP2)
V4, W4 = GA.scal(HALF, NINF2), GA.neg(NO2)
LAMBDAS = (F(3), F(-6), F(1, 7), F(-2, 5), F(9, 4))


def Q(x):
    return GA.dot(x, x, SQ)


def check_rung_component_norm_and_normalisation():
    premise("standard-model.transported-frozen-point")
    premise("standard-model.frozen-point-first-rung-component")
    ok = Q(NO) == 0 and Q(NINF) == 0 and GA.dot(NO, NINF, SQ) == -1
    ok = ok and Q(V4) == 0 and Q(W4) == 0 and GA.dot(V4, W4, SQ) == HALF
    ok = ok and GA.eq(GA.add(GA.mul(V4, W4, SQ), GA.mul(W4, V4, SQ)), GA.sc(1))
    for L in LAMBDAS:
        I = GA.sub(NINF, GA.scal(L / 6, NO))
        ok = ok and Q(I) == L / 3
        X = GA.add(NO2, I, GA.scal(L / 6, NINF2))
        ok = ok and Q(X) == 0
        rung = GA.sub(X, I)
        ok = ok and GA.eq(rung, GA.add(GA.neg(W4), GA.scal(L / 3, V4)))
        ok = ok and Q(rung) == -L / 3 and Q(rung) + Q(I) == 0
        ok = ok and all(GA.dot(rung, y, SQ) == 0 for y in (EP, EM))
        # coefficient one on -w_4 whatever Lambda; the admixture of v_4 is Lambda/3
        ok = ok and GA.dot(rung, V4, SQ) == -HALF and GA.dot(rung, W4, SQ) == L / 6
        # the reciprocal's lift, normalised to ground component I
        Xr = GA.add(GA.scal(L / 3, NO2), I, GA.scal(HALF, NINF2))
        ok = ok and Q(Xr) == 0 and GA.eq(GA.sub(Xr, I), GA.sub(V4, GA.scal(L / 3, W4)))
    GA.check("what is derived (2): rung component -w_4 + (Lambda/3) v_4 of norm -Lambda/3, coefficient one", ok)
    return ok


# Fock module of the two rung modes (4, 5) and one pair mode (1), enough for the commutators
STATES = [frozenset(c) for r in range(4) for c in combinations((1, 4, 5), r)]


def act(kind, a, st):
    out = {}
    for S, c in st.items():
        if kind == "v" and a not in S:
            T = S | {a}
        elif kind == "w" and a in S:
            T = S - {a}
        else:
            continue
        sign = -1 if sum(1 for j in S if j < a) % 2 else 1
        out[T] = out.get(T, 0) + sign * c
    return out


def weight(S):
    return F(3 * len(S & {4, 5}) - 2 * len(S & {1}), 6), (4 in S) - (5 in S)


def check_rung_directions_are_doublet_directions():
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    ok = True
    for kind, (y, t) in (("w", (F(-1, 2), -1)), ("v", (F(1, 2), 1))):
        for S in STATES:
            for T, c in act(kind, 4, {S: F(1)}).items():
                ok = ok and weight(T)[0] - weight(S)[0] == y and weight(T)[1] - weight(S)[1] == t
    # the conversion: v / H = 246 GeV / 1.4e-42 GeV is of order 10^44
    ratio = F(246) / (F(14, 10) * F(1, 10 ** 42))
    ok = ok and 10 ** 44 <= ratio < 10 ** 45
    GA.check("what is derived (1), (2): w_4, v_4 carry Y = -1/2, +1/2 (H_d, H_u directions); v/H ~ 10^44", ok)
    return ok
