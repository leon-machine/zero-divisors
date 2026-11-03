"""interior.stabiliser-rotates-parabolic-reductive: exact checks in Cl(2,4).

V = R^(2,4) as the vectors of GA Cl(2,4) (generators 0, 1 square +1, generators 2..5 square -1), with
ninf = (e1 + e5)/2, n0 = e1 - e5 (null, <ninf, n0> = 1) and W = span(e0, e2, e3, e4) = R^(1,3). The
frozen point is I = ninf + (Lambda/6) n0 (Theorem interior.scale-tractor-leaves-cone), for
Lambda in {0, 3, 12, -3, -12}. The structure algebra so(2,4) is the 15 bivectors acting on vectors
by commutators; the invariant form on it is the scalar part <B1 B2>.
(1) Q(I) = Lambda/3. The stabiliser {B : [B, I] = 0} (exact kernel) has dimension 10 in every case;
    for Lambda != 0 it is spanned by the wedges of a basis of I-perp (Lambda^2(I-perp)), and for
    Lambda = 0 by Lambda^2 W + ninf ^ W.
(2) The type. The invariant form on the stabiliser has congruence signature (4, 6, 0) for Lambda > 0,
    so(1,4) (boosts against rotations), and (6, 4, 0) for Lambda < 0, so(2,3): nondegenerate, so the
    stabiliser is reductive with trivial nilradical; I-perp has signature (1,4), resp. (2,3). For
    Lambda = 0 the form is (3, 3, 4): its radical is ninf ^ W, a 4-dimensional abelian ideal acting on V
    by null shears (cube zero, square into R ninf): the Poincare algebra, the parabolic case.
(3) The section and infinity. On the section <X, I> = 1, Q(X) = 0, Y = X - I/Q(I) has
    Q(Y) = -1/Q(I) and tangent space of signature (1,3) (de Sitter, anti-de Sitter); a null X in
    I-perp has X-perp in I-perp of signature (0, 3, 1) for Lambda > 0 (spacelike infinity) and
    (1, 2, 1) for Lambda < 0 (timelike infinity).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = GA.sig(2, 4)
E = [GA.gen(i) for i in range(6)]
GRAM = [[F(SQ[i]) if i == j else F(0) for j in range(6)] for i in range(6)]
NINF = GA.scal(F(1, 2), GA.add(E[1], E[5]))
N0 = GA.sub(E[1], E[5])
WB = [E[0], E[2], E[3], E[4]]
BIV = list(combinations(range(6), 2))
VEC = [(i,) for i in range(6)]
LAMBDAS = (F(0), F(3), F(12), F(-3), F(-12))
NULL_IN_PERP = {F(3): E[0], F(12): GA.scal(F(2), E[0]), F(-3): E[2], F(-12): GA.scal(F(2), E[2])}


def frozen(lam):
    return GA.add(NINF, GA.scal(lam / 6, N0))


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def br(a, b):
    return GA.sub(GA.mul(a, b, SQ), GA.mul(b, a, SQ))


def from_biv(c):
    return {b: v for b, v in zip(BIV, c) if v != 0}


def stabiliser(I):
    cols = [coords(br({b: F(1)}, I), VEC) for b in BIV]
    return [from_biv(v) for v in GA.field_kernel([[cols[j][i] for j in range(15)] for i in range(6)])]


def perp(vectors):
    rows = [[sum((coords(v, VEC)[k] * GRAM[k][j] for k in range(6)), F(0)) for j in range(6)] for v in vectors]
    return [{(i,): c for i, c in enumerate(v) if c != 0} for v in GA.field_kernel(rows)]


def gram_of(vs):
    return [[GA.dot(a, b, SQ) for b in vs] for a in vs]


def form(Bs):
    return [[GA.mul(a, b, SQ).get((), F(0)) for b in Bs] for a in Bs]


def wedge(a, b):
    return GA.scal(F(1, 2), br(a, b))


def check_stabiliser_dimension_and_shape():
    premise("interior.scale-tractor-leaves-cone")
    premise("interior.stabilisers-flat-model")
    premise("interior.non-null-stabilisers-section-they-act")
    ok = True
    ok = ok and GA.dot(NINF, NINF, SQ) == 0 and GA.dot(N0, N0, SQ) == 0 and GA.dot(NINF, N0, SQ) == 1
    ok = ok and GA.congruence_signature(gram_of(WB)) == (1, 3, 0)
    for lam in LAMBDAS:
        I = frozen(lam)
        ok = ok and GA.dot(I, I, SQ) == lam / 3
        S = stabiliser(I)
        ok = ok and len(S) == 10
        if lam != 0:
            P = perp([I])
            span = [wedge(a, b) for a, b in combinations(P, 2)]
        else:
            span = [wedge(a, b) for a, b in combinations(WB, 2)] + [wedge(NINF, w) for w in WB]
        ok = ok and len(span) == 10 and all(GA.is_zero(br(B, I)) for B in span)
        ok = ok and GA.rank_of_vectors([coords(B, BIV) for B in S + span]) == 10
    GA.check("Q(I) = Lambda/3; stabiliser of dimension 10: Lambda^2(I-perp), or Lambda^2 W + ninf ^ W at Lambda = 0", ok)
    return ok


def check_reductive_or_parabolic():
    premise("interior.stabilisers-flat-model")
    premise("interior.non-null-stabilisers-section-they-act")
    ok = True
    for lam in LAMBDAS:
        I = frozen(lam)
        S = stabiliser(I)
        sg = GA.congruence_signature(form(S))
        if lam > 0:
            ok = ok and sg == (4, 6, 0) and GA.congruence_signature(gram_of(perp([I]))) == (1, 4, 0)
        elif lam < 0:
            ok = ok and sg == (6, 4, 0) and GA.congruence_signature(gram_of(perp([I]))) == (2, 3, 0)
        else:
            ok = ok and sg == (3, 3, 4)
            Nil = [wedge(NINF, w) for w in WB]
            ok = ok and all(GA.mul(a, b, SQ).get((), F(0)) == 0 for a in Nil for b in S)
            ok = ok and all(GA.is_zero(br(a, b)) for a in Nil for b in Nil)
            ok = ok and all(GA.rank_of_vectors([coords(br(s, n), BIV) for n in Nil] +
                                               [coords(n, BIV) for n in Nil]) == 4 for s in S)
            for n in Nil:
                for x in E:
                    x1 = GA.scal(F(1, 2), br(x, n))
                    x2 = GA.scal(F(1, 2), br(x1, n))
                    x3 = GA.scal(F(1, 2), br(x2, n))
                    ok = ok and GA.is_zero(x3)
                    ok = ok and GA.rank_of_vectors([coords(x2, VEC), coords(NINF, VEC)]) <= 1
    GA.check("invariant form (4,6) so(1,4) for Lambda > 0, (6,4) so(2,3) for Lambda < 0; (3,3,4) with "
             "nilradical ninf ^ W (abelian ideal, null shears) for Lambda = 0", ok)
    return ok


def check_section_and_polar_infinity():
    premise("interior.non-null-stabilisers-section-they-act")
    ok = True
    for lam in LAMBDAS[1:]:
        I = frozen(lam)
        QI_ = GA.dot(I, I, SQ)
        X = N0
        ok = ok and GA.dot(X, X, SQ) == 0 and GA.dot(X, I, SQ) == 1
        Y = GA.sub(X, GA.scal(1 / QI_, I))
        ok = ok and GA.dot(Y, Y, SQ) == -3 / lam and GA.dot(Y, I, SQ) == 0
        ok = ok and GA.congruence_signature(gram_of(perp([I, Y]))) == (1, 3, 0)
        Xn = GA.sub(GA.add(NINF, NULL_IN_PERP[lam]), GA.scal(lam / 6, N0))
        ok = ok and GA.dot(Xn, Xn, SQ) == 0 and GA.dot(Xn, I, SQ) == 0
        sg = GA.congruence_signature(gram_of(perp([I, Xn])))
        ok = ok and sg == ((0, 3, 1) if lam > 0 else (1, 2, 1))
    GA.check("Y = X - I/Q(I) has Q(Y) = -1/Q(I) with Lorentzian tangent; polar infinity spacelike for "
             "Lambda > 0, timelike for Lambda < 0", ok)
    return ok
