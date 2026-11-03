"""odd-extensions.line-tame-wall: exact checks.

GA model of the rung R^(2,4): Cl(2,4) with e_1 (square +1) and e_2, e_3, e_4 (square -1) the Lorentz
frame, and e_+ (square +1), e_- (square -1) spanning the hyperbolic plane with the canonical null
frame I_0 = e_+ + e_-, phi = (e_+ - e_-)/2 (null, <I_0, phi> = 1). For a gauge a (nonzero rational)
and b = Lambda/(6a): I_Lambda = a I_0 + b phi (so 2ab = Lambda/3, Q(I_Lambda) = Lambda/3) and
w_Lambda = a I_0 - b phi. Samples: seven values of Lambda (zero included) and four gauges, plus the
smooth gauges a(Lambda) = 1 + Lambda and 2 - Lambda^2 evaluated on the same points.
(i) The Gram of (e_1, ..., e_4, w_Lambda) is diag(1, -1, -1, -1, -Lambda/3) in every gauge, and
w_Lambda, I_Lambda are orthogonal; the family is degenerate exactly at Lambda = 0 (rank 4 of 5 there,
5 elsewhere), with radical spanned by w_0 = a(0) I_0; the dying eigenvalue -Lambda/3 has difference
quotient -1/3 at six nonzero Lambda and, as a rational function of Lambda, derivative -1/3.
(ii) The signature is (2,3) for Lambda < 0 and (1,4) for Lambda > 0.
(iii) The gauge a = b needs a^2 = Lambda/6: it exists for Lambda = 6 s^2 (a = s) and for no Lambda < 0,
and a(Lambda) = sqrt(Lambda/6) has difference quotients a/Lambda = n/6 at Lambda = 6/n^2, unbounded:
not smooth at the wall. The scalar invariants are gauge independent, while the radical vector
w_0 = a(0) I_0 depends on the normalisation a(0).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = [F(1), F(-1), F(-1), F(-1), F(1), F(-1)]      # e_1, e_2, e_3, e_4, e_+, e_-
E = [GA.gen(i) for i in range(6)]
I0 = GA.add(E[4], E[5])
PHI = GA.scal(F(1, 2), GA.sub(E[4], E[5]))
LAMBDAS = (F(-6), F(-1), F(-1, 4), F(0), F(1, 5), F(3), F(12))
GAUGES = (F(1), F(-2), F(3, 7), F(5))


def frozen(L, a):
    b = L / (6 * a)
    return GA.add(GA.scal(a, I0), GA.scal(b, PHI)), GA.sub(GA.scal(a, I0), GA.scal(b, PHI))


def gram(vs):
    return [[GA.dot(x, y, SQ) for y in vs] for x in vs]


def check_gram_and_tameness():
    premise("odd-extensions.transport-constrains-frozen-point-only-through")
    premise("odd-extensions.imported-tame-walls-exceptional-algebra-residue")
    ok = GA.dot(I0, I0, SQ) == 0 and GA.dot(PHI, PHI, SQ) == 0 and GA.dot(I0, PHI, SQ) == 1
    gauges = [(L, a) for L in LAMBDAS for a in GAUGES] + [(L, 1 + L) for L in LAMBDAS if L != -1] + \
        [(L, 2 - L * L) for L in LAMBDAS]
    for L, a in gauges:
        I, w = frozen(L, a)
        ok = ok and GA.dot(I, I, SQ) == L / 3
        G = gram(E[:4] + [w])
        ok = ok and G == [[(SQ[i] if i < 4 else -L / 3) if i == j else F(0) for j in range(5)] for i in range(5)]
        ok = ok and GA.dot(w, I, SQ) == 0 and all(GA.dot(I, e, SQ) == 0 for e in E[:4])
        ok = ok and GA.mat_rank(G) == (4 if L == 0 else 5)
        if L == 0:
            # the radical is the line of w_0 = a(0) I_0
            ok = ok and GA.eq(w, GA.scal(a, I0)) and all(GA.dot(w, x, SQ) == 0 for x in E[:4] + [w])
        else:
            ok = ok and (GA.dot(w, w, SQ) - 0) / L == F(-1, 3)
    # the dying eigenvalue as a rational function of Lambda in the gauge a = 1: derivative -1/3
    t = GA.RF.var()
    dying = GA.RF.const(-2) * GA.RF.const(1) * (t / GA.RF.const(6))
    ok = ok and dying.deriv().eqrf(GA.RF.const(F(-1, 3))) and dying.eval(F(0)) == 0
    GA.check("line wall (i): Gram diag(1,-1,-1,-1,-Lambda/3), degenerate only at 0, radical w_0, slope -1/3", ok)
    return ok


def check_signatures_on_the_two_sides():
    premise("odd-extensions.four-extensions-oriented-pair")
    ok = True
    for L in LAMBDAS:
        for a in GAUGES:
            sig = GA.congruence_signature(gram(E[:4] + [frozen(L, a)[1]]))
            if L < 0:
                ok = ok and sig == (2, 3, 0)
            elif L > 0:
                ok = ok and sig == (1, 4, 0)
            else:
                ok = ok and sig == (1, 3, 1)
    GA.check("line wall (ii): signature (2,3) for Lambda < 0 and (1,4) for Lambda > 0", ok)
    return ok


SQUARES = (1, 2, 3, 4, 6)


def check_symmetric_gauge_not_smooth():
    premise("odd-extensions.transport-constrains-frozen-point-only-through")
    ok = True
    quot = []
    for n in SQUARES:
        L = F(6, n * n)
        s = F(1, n)
        I, w = frozen(L, s)
        ok = ok and GA.eq(I, GA.scal(s, GA.add(I0, PHI)))          # a = b = s
        quot.append(s / L)
    ok = ok and quot == [F(n, 6) for n in SQUARES]
    ok = ok and all(quot[i] < quot[i + 1] for i in range(len(SQUARES) - 1))
    # for Lambda < 0, a = b would need 2 a^2 = Lambda/3 < 0
    ok = ok and all(2 * a * a >= 0 > L / 3 for L in LAMBDAS if L < 0 for a in GAUGES)
    # invariants agree across gauges, the radical vector does not
    sigs = {GA.congruence_signature(gram(E[:4] + [frozen(F(-1), a)[1]])) for a in GAUGES}
    ok = ok and sigs == {(2, 3, 0)}
    w1, w2 = frozen(F(0), F(1))[1], frozen(F(0), F(5))[1]
    ok = ok and GA.eq(w2, GA.scal(5, w1)) and not GA.eq(w1, w2)
    GA.check("line wall (iii): the gauge a = b is not smooth and fails for Lambda < 0; invariants gauge free", ok)
    return ok
