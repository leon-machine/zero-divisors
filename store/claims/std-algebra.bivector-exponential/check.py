from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


# rational points on the three unit "circles": c^2 - lambda s^2 = 1
POINTS = {-1: (F(3, 5), F(4, 5)), 1: (F(5, 4), F(3, 4)), 0: (F(1), F(7, 2))}
# (signature, a, b) with a, b orthogonal; b null in the last two
PLANES = [
    ((3, 0, 0), [1, 0, 0], [0, 1, 0]),
    ((1, 1, 0), [1, 0], [0, 1]),
    ((2, 1, 0), [0, 1, 0], [0, 0, 1]),
    ((2, 0, 1), [1, 0, 0], [0, 0, 1]),
    ((1, 2, 0), [0, 0, 1], [1, 1, 0]),
]


def check_powers_collapse():
    premise("std-algebra.vector-squares")
    premise("std-algebra.orthogonal-anticommute")
    ok = True
    lams = []
    for (p, q, r), ac, bc in PLANES:
        sq = GA.sig(p, q, r)
        a, b = S.vec(ac), S.vec(bc)
        ok = ok and GA.dot(a, b, sq) == 0
        A = GA.mul(a, b, sq)
        ok = ok and S.grades(A) == [2]
        A2 = GA.mul(A, A, sq)
        lam = A2.get((), F(0))
        ok = ok and GA.eq(A2, GA.sc(lam))
        lams.append(lam)
        P = GA.sc(1)
        for k in range(1, 9):
            P = GA.mul(P, A, sq)
            exp = GA.sc(lam ** (k // 2)) if k % 2 == 0 else GA.scal(lam ** (k // 2), A)
            ok = ok and GA.eq(P, exp)
    ok = ok and lams == [-1, 1, 1, 0, 0]
    # every bivector in dimension 3 squares to a scalar; in dimension 4 not always
    for p, q, r in S.signatures(3)[9:]:
        sq = GA.sig(p, q, r)
        A = S.sample(3, 4, grades_=(2,))
        ok = ok and S.grades(GA.mul(A, A, sq)) in ([0], [])
    sq = GA.sig(4, 0)
    A = GA.add(S.blade(0, 1), S.blade(2, 3))
    ok = ok and S.grades(GA.mul(A, A, sq)) == [0, 4]
    GA.check("A^2 scalar for simple bivectors (and all bivectors in n = 3); powers collapse to lambda^k, lambda^k A", ok)
    return ok


def check_closed_forms_are_rotors():
    premise("std-algebra.involution-properties")
    premise("std-algebra.inverse-of-vector")
    ok = True
    tested = 0
    for (p, q, r), ac, bc in PLANES:
        sq = GA.sig(p, q, r)
        a, b = S.vec(ac), S.vec(bc)
        A = GA.mul(a, b, sq)
        lam = GA.mul(A, A, sq).get((), F(0))
        c, s = POINTS[int(lam)]
        ok = ok and c * c - lam * s * s == 1
        R = GA.add(GA.sc(c), GA.scal(s, A))
        ok = ok and GA.eq(GA.mul(R, GA.reverse(R), sq), GA.sc(1))
        # addition law of the exponential: (c, s)(c, s) = (c^2 + lam s^2, 2 c s)
        R2 = GA.mul(R, R, sq)
        ok = ok and GA.eq(R2, GA.add(GA.sc(c * c + lam * s * s), GA.scal(2 * c * s, A)))
        # a product of two invertible vectors
        eps = GA.dot(a, a, sq)
        w = GA.add(GA.scal(eps * c, a), GA.scal(s, b))
        ok = ok and GA.eq(GA.mul(a, w, sq), R)
        ok = ok and GA.dot(w, w, sq) == eps
        # the action on V preserves Q and maps vectors to vectors
        for i in range(len(sq)):
            y = GA.mul(GA.mul(R, GA.gen(i), sq), GA.reverse(R), sq)
            ok = ok and S.grades(y) == [1] and GA.dot(y, y, sq) == sq[i]
            tested += 1
    ok = ok and tested == 3 + 2 + 3 + 3 + 3
    # the rotation by (3/5, 4/5) in the e0 e1 plane of R^3 sends e0 to (c^2 - s^2) e0 - 2 c s e1
    sq = GA.sig(3, 0)
    R = GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), S.blade(0, 1)))
    y = GA.mul(GA.mul(R, GA.gen(0), sq), GA.reverse(R), sq)
    ok = ok and GA.eq(y, S.vec([F(-7, 25), F(-24, 25), 0]))
    GA.check("cos/cosh/null closed forms: R R~ = 1, R = product of two invertible vectors, R x R~ an isometry", ok)
    return ok
