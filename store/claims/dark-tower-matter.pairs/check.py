"""dark-tower-matter.pairs: exact checks, in GA.py (complex coefficients as GA.QI).

For the six causal towers (p,q) = (2,1), (1,2), (1,3), (3,1), (4,1), (1,4) the conformal space is
Vhat = R^(p+1, q+1): (3,2), (2,3), (2,4), (4,2), (5,2), (2,5).
(1) Real Witt index min(p+1, q+1) = 2 in every case: two real ladder pairs w = (e_i + e_j)/2,
    v = (e_i - e_j)/2 (Q(e_i) = +1, Q(e_j) = -1) obey the CAR, and the orthogonal complement of the
    two hyperbolic planes is definite (all remaining squares of one sign), so it has no nonzero real
    null vector: by Witt decomposition the real index is exactly 2, and no unit is needed for the
    two real pairs.
(2) Complex Witt index floor(dim Vhat / 2): over Q(i), two remaining generators of equal square s
    give a third pair w = (e_a + i e_b)/2, v = s (e_a - i e_b)/2; all three pairs obey the CAR in
    dimensions 6 and 7, while in dimension 5 the complement is one vector of nonzero square
    (anisotropic over C). So the index is 2 (dim 5) and 3 (dims 6, 7): the third pair needs a
    complex unit in this tower, the mirror and the five-dimensional towers, and none is needed in
    the three-dimensional towers.
(3) The field and its unit: in the tower corner F = f Cl^0 f, f = (1 + e_t e_a)/2, the field is C
    in this tower (1,3) and the mirror (3,1): F = span{f, u} with u f = f u = u and u^2 = -f, so
    (alpha f + beta u)^2 = -f forces alpha beta = 0 and alpha^2 - beta^2 = -1, i.e. the unit is +-u,
    fixed up to sign (both signs verified). Controls: in the three-dimensional towers F = R f has
    no unit; in the five-dimensional towers F = H and the units form a sphere (three anticommuting
    basis units, and (3 u1 + 4 u2)/5 is a unit different from every +-u_k).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
TOWERS = [(2, 1), (1, 2), (1, 3), (3, 1), (4, 1), (1, 4)]


def car(ws, vs, S):
    one = {(): F(1)}
    for i in range(len(ws)):
        for k in range(len(ws)):
            ac = GA.add(GA.mul(ws[i], vs[k], S), GA.mul(vs[k], ws[i], S))
            if not GA.eq(ac, one if i == k else {}):
                return False
            if not GA.is_zero(GA.add(GA.mul(ws[i], ws[k], S), GA.mul(ws[k], ws[i], S))):
                return False
            if not GA.is_zero(GA.add(GA.mul(vs[i], vs[k], S), GA.mul(vs[k], vs[i], S))):
                return False
    return True


def real_pairs(P, Q):
    S = GA.sig(P, Q)
    pos = [a for a in range(P + Q) if S[a] == 1]
    neg = [a for a in range(P + Q) if S[a] == -1]
    k = min(len(pos), len(neg))
    ws = [GA.scal(F(1, 2), GA.add(GA.gen(pos[i]), GA.gen(neg[i]))) for i in range(k)]
    vs = [GA.scal(F(1, 2), GA.sub(GA.gen(pos[i]), GA.gen(neg[i]))) for i in range(k)]
    rest = pos[k:] + neg[k:]
    return S, ws, vs, rest


def check_real_witt_index():
    premise("dark-tower-matter.constituents-field")
    for (p, q) in TOWERS:
        P, Q = p + 1, q + 1
        S, ws, vs, rest = real_pairs(P, Q)
        assert len(ws) == 2 and min(P, Q) == 2
        assert car(ws, vs, S)
        # the complement of the two hyperbolic planes is definite: anisotropic over R
        gram = [[GA.dot(GA.gen(a), GA.gen(b), S) for b in rest] for a in rest]
        pos, neg, zer = GA.congruence_signature(gram)
        assert zer == 0 and (pos == 0 or neg == 0) and pos + neg == P + Q - 4
    return True


def check_complex_witt_index():
    premise("dark-tower-matter.constituents-field")
    index = {}
    for (p, q) in TOWERS:
        P, Q = p + 1, q + 1
        S, ws, vs, rest = real_pairs(P, Q)
        n = P + Q
        npairs = 2
        if len(rest) >= 2:
            a, b = rest[0], rest[1]
            s = S[a]
            assert S[b] == s
            w = {(a,): QI(F(1, 2)), (b,): QI(0, F(1, 2))}
            v = {(a,): QI(F(s, 2)), (b,): QI(0, F(-s, 2))}
            assert GA.is_zero(GA.mul(w, w, S)) and GA.is_zero(GA.mul(v, v, S))
            assert car(ws + [w], vs + [v], S)
            npairs = 3
            rest = rest[2:]
        # what is left is at most one vector of nonzero square: anisotropic over C
        assert len(rest) <= 1 and all(S[c] != 0 for c in rest)
        assert npairs == n // 2
        index[(P, Q)] = npairs
    assert index == {(3, 2): 2, (2, 3): 2, (2, 4): 3, (4, 2): 3, (5, 2): 3, (2, 5): 3}
    return True


def corner(p, q):
    S = GA.sig(p, q)
    t = 0 if p == 1 else p + q - 1
    a = 1 if p == 1 else 0
    f = GA.add(GA.sc(F(1, 2)), GA.scal(F(1, 2), GA.mul(GA.gen(t), GA.gen(a), S)))
    ev = [b for b in GA.all_blades(p + q) if len(b) % 2 == 0]
    vecs, C = [], []
    for K in ev:
        x = GA.mul(GA.mul(f, {K: F(1)}, S), f, S)
        v = [x.get(b, F(0)) for b in ev]
        if any(v) and GA.rank_of_vectors(vecs + [v]) > len(vecs):
            vecs.append(v)
            C.append(x)
    return S, f, C


def check_unit_fixed_up_to_sign():
    premise("dark-tower-matter.constituents-field")
    for (p, q) in ((1, 3), (3, 1)):
        S, f, C = corner(p, q)
        assert len(C) == 2 and GA.eq(C[0], f)
        u = C[1]
        assert GA.eq(GA.mul(u, f, S), u) and GA.eq(GA.mul(f, u, S), u)
        assert GA.eq(GA.mul(u, u, S), GA.scal(-1, f))
        # (alpha f + beta u)^2 = (alpha^2 - beta^2) f + 2 alpha beta u: read off the products
        for (al, be) in ((F(2), F(3)), (F(1, 2), F(-1)), (F(0), F(5))):
            x = GA.add(GA.scal(al, f), GA.scal(be, u))
            assert GA.eq(GA.mul(x, x, S), GA.add(GA.scal(al * al - be * be, f), GA.scal(2 * al * be, u)))
        for sgn in (1, -1):
            assert GA.eq(GA.mul(GA.scal(sgn, u), GA.scal(sgn, u), S), GA.scal(-1, f))
    for (p, q) in ((2, 1), (1, 2)):
        S, f, C = corner(p, q)
        assert len(C) == 1                                     # F = R f: (alpha f)^2 = alpha^2 f
    for (p, q) in ((4, 1), (1, 4)):
        S, f, C = corner(p, q)
        assert len(C) == 4
        us = C[1:]
        for i, x in enumerate(us):
            assert GA.eq(GA.mul(x, x, S), GA.scal(-1, f))
            for y in us[:i]:
                assert GA.is_zero(GA.add(GA.mul(x, y, S), GA.mul(y, x, S)))
        m = GA.add(GA.scal(F(3, 5), us[0]), GA.scal(F(4, 5), us[1]))
        assert GA.eq(GA.mul(m, m, S), GA.scal(-1, f))
        assert all(not GA.eq(m, GA.scal(s, x)) for x in us for s in (1, -1))
    return True
