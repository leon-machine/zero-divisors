"""angle.imported-conformal-model-null-rotations: exact checks (GA blade engine).

(1) Conformal model, for (p, q) in (1,3), (3,1), (2,0), (0,2), (2,2), (1,1): in Cl(p+1, q+1) with e+ (square +1)
    and e- (square -1) appended, nO = (e- - e+)/2 and nInf = e- + e+ are null with nO . nInf = -1;
    X(x) = nO + x + Q(x) nInf / 2 is null and X(x) . X(y) = -Q(x - y)/2 for every pair of sample points x, y
    (Q(x) = x^2).
(2) Null rotations: for a null v with a partner w (v . w != 0) and U = {v, w}^perp, namely
    (v, w, U) = (nInf, nO, base vectors) in Cl(2,4), Cl(3,1) and Cl(2,2), and (e0 + e1, (e0 - e1)/4, span(e2, e3))
    inside Cl(1,3): R_u = 1 + v u is even with R_u reverse(R_u) = 1, fixes v, maps every basis vector to a
    vector, R_u R_u' = R_(u + u') on sample pairs, and u -> v u is injective on U (rank dim U), so u -> R_u
    is an isomorphism of (U, +) onto N_v = {R_u}. Control: u = v (outside U) gives R = 1.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(1, 3), (3, 1), (2, 0), (0, 2), (2, 2), (1, 1)]
COEFFS = [(F(1), F(-2), F(1, 3), F(0)), (F(3, 4), F(0), F(-1), F(5)), (F(-2), F(1, 2), F(2), F(-1, 7))]
UCOEFFS = [(F(1), F(2, 3), F(-1), F(4)), (F(-3), F(1, 5), F(0), F(2))]


def vecs(n, coeffs):
    return [{(i,): c for i, c in enumerate(cs[:n]) if c != 0} for cs in coeffs]


def dot(x, y, sq):
    z = GA.add(GA.mul(x, y, sq), GA.mul(y, x, sq))
    return z.get((), F(0)) * F(1, 2)


def conformal(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    nO = GA.scal(F(1, 2), GA.sub(em, ep))
    nI = GA.add(em, ep)
    return n, sq, nO, nI


def X(x, nO, nI, sq):
    Q = GA.mul(x, x, sq).get((), F(0))
    return GA.add(nO, x, GA.scal(Q * F(1, 2), nI))


def check_conformal_model():
    premise("transport.totality")
    ok = True
    for p, q in SIGS:
        n, sq, nO, nI = conformal(p, q)
        ok = ok and GA.mul(nO, nO, sq) == {} and GA.mul(nI, nI, sq) == {}
        ok = ok and dot(nO, nI, sq) == -1
        pts = vecs(n, COEFFS)
        for x in pts:
            ok = ok and GA.mul(X(x, nO, nI, sq), X(x, nO, nI, sq), sq) == {}
            for y in pts:
                d = GA.sub(x, y)
                Qd = GA.mul(d, d, sq).get((), F(0))
                ok = ok and dot(X(x, nO, nI, sq), X(y, nO, nI, sq), sq) == -Qd * F(1, 2)
    GA.check("conformal model: null pair with nO . nInf = -1, X(x) null, X(x) . X(y) = -Q(x - y)/2", ok)
    return ok


def null_rotation_cases():
    out = []
    for p, q in [(1, 3), (2, 0), (1, 1)]:
        n, sq, nO, nI = conformal(p, q)
        out.append((sq, nI, nO, [GA.gen(i) for i in range(n)], n + 2))
    sq = GA.sig(1, 3)
    v = GA.add(GA.gen(0), GA.gen(1))
    w = GA.scal(F(1, 4), GA.sub(GA.gen(0), GA.gen(1)))
    out.append((sq, v, w, [GA.gen(2), GA.gen(3)], 4))
    return out


def check_null_rotations_isomorphic_to_u():
    premise("transport.group-null-rotations")
    ok = True
    for sq, v, w, Ubasis, m_ in null_rotation_cases():
        ok = ok and GA.mul(v, v, sq) == {} and dot(v, w, sq) != 0
        ok = ok and all(dot(u, v, sq) == 0 and dot(u, w, sq) == 0 for u in Ubasis)
        us = []
        for cs in UCOEFFS:
            u = {}
            for c, b in zip(cs, Ubasis):
                u = GA.add(u, GA.scal(c, b))
            us.append(u)
        for u in us:
            R = GA.add(GA.sc(1), GA.mul(v, u, sq))
            ok = ok and all(len(b) % 2 == 0 for b in R)
            ok = ok and GA.mul(R, GA.reverse(R), sq) == GA.sc(1)
            Rinv = GA.reverse(R)
            ok = ok and GA.mul(GA.mul(R, v, sq), Rinv, sq) == v
            ok = ok and all(all(len(b) == 1 for b in GA.mul(GA.mul(R, GA.gen(i), sq), Rinv, sq)) for i in range(m_))
        for u in us:
            for u2 in us:
                lhs = GA.mul(GA.add(GA.sc(1), GA.mul(v, u, sq)), GA.add(GA.sc(1), GA.mul(v, u2, sq)), sq)
                ok = ok and lhs == GA.add(GA.sc(1), GA.mul(v, GA.add(u, u2), sq))
        rows = [GA.basis_vector_of(GA.mul(v, u, sq), GA.all_blades(m_)) for u in Ubasis]
        ok = ok and GA.rank_of_vectors(rows) == len(Ubasis)
        ok = ok and GA.add(GA.sc(1), GA.mul(v, v, sq)) == GA.sc(1)
    ok = ok and [len(c[3]) for c in null_rotation_cases()] == [4, 2, 2, 2]
    GA.check("R_u = 1 + v u: rotors fixing v, R_u R_u' = R_(u+u'), injective on U", ok)
    return ok
