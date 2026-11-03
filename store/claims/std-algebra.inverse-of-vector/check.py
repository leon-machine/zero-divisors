from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


VECS = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [2, -1, 0, 1], [0, 0, 1, 1], [1, 0, 0, 1]]
VERSOR = [[1, 2, 0, 0], [1, 0, 2, 0], [0, 1, 0, 2]]


def check_invertible_iff_nonnull():
    premise("std-algebra.vector-squares")
    premise("std-algebra.blade-basis")
    ok = True
    inv = null = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        dim = 2 ** n
        for c in VECS:
            v = S.vec(c[:n])
            if not v:
                continue
            Qv = GA.dot(v, v, sq)
            full = GA.mat_rank(S.left_matrix(v, sq)) == dim
            ok = ok and full == (Qv != 0)
            if Qv != 0:
                w = GA.scal(1 / Qv, v)
                ok = ok and GA.eq(GA.mul(v, w, sq), GA.sc(1)) and GA.eq(GA.mul(w, v, sq), GA.sc(1))
                inv += 1
            else:
                ok = ok and GA.is_zero(GA.mul(v, v, sq))
                null += 1
    ok = ok and (inv, null) == (168, 58)
    GA.check("v invertible iff Q(v) != 0 (left multiplication has full rank); null v squares to 0", ok)
    return ok


def check_versor_norm():
    premise("std-algebra.involution-properties")
    ok = True
    norms = []
    for p, q, r in ((2, 2, 0), (1, 2, 1), (3, 1, 0)):
        sq = GA.sig(p, q, r)
        us = [S.vec(c) for c in VERSOR]
        qs = [GA.dot(u, u, sq) for u in us]
        ok = ok and all(x != 0 for x in qs)
        g = GA.mul(GA.mul(us[0], us[1], sq), us[2], sq)
        prod = qs[0] * qs[1] * qs[2]
        ok = ok and GA.eq(GA.mul(g, GA.reverse(g), sq), GA.sc(prod))
        ok = ok and GA.eq(GA.mul(GA.reverse(g), g, sq), GA.sc(prod))
        norms.append(prod)
    ok = ok and norms == [45, -9, -75]
    GA.check("g g~ = g~ g = product of Q(u_i) for a three-vector versor", ok)
    return ok
