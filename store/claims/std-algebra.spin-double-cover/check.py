from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def ad(g, x, sq, ginv):
    return GA.mul(GA.mul(GA.grade_inv(g), x, sq), ginv, sq)


UNIT = {  # unit vectors in R^{p,q}, rational
    (3, 0): [[1, 0, 0], [F(3, 5), F(4, 5), 0], [0, F(5, 13), F(12, 13)], [F(2, 3), F(1, 3), F(2, 3)]],
    (1, 2): [[1, 0, 0], [F(5, 4), F(3, 4), 0], [0, 1, 0], [F(5, 3), F(4, 3), 0], [0, F(3, 5), F(4, 5)]],
    (2, 2): [[1, 0, 0, 0], [0, 0, 1, 0], [F(5, 4), 0, F(3, 4), 0], [0, F(13, 12), 0, F(5, 12)], [1, 1, 1, 0]],
}


def check_spin_homomorphism_and_kernel():
    premise("primer.twisted-adjoint-action")
    premise("primer.centre")
    premise("std-algebra.reflection")
    premise("std-algebra.inverse-of-vector")
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.z2-grading")
    ok = True
    pairs = 0
    dets = []
    for (p, q), cs in UNIT.items():
        sq = GA.sig(p, q)
        n = len(sq)
        us = [S.vec(c) for c in cs]
        ok = ok and all(GA.dot(u, u, sq) in (1, -1) for u in us)
        for k in (2, 3):
            for idx in combinations(range(len(us)), k):
                g = GA.sc(1)
                norm = F(1)
                for i in idx:
                    g = GA.mul(g, us[i], sq)
                    norm *= GA.dot(us[i], us[i], sq)
                ok = ok and GA.eq(GA.mul(g, GA.reverse(g), sq), GA.sc(norm))
                ginv = GA.scal(1 / norm, GA.reverse(g))
                imgs = [ad(g, GA.gen(i), sq, ginv) for i in range(n)]
                ok = ok and all(S.grades(y) == [1] for y in imgs)
                ok = ok and all(GA.dot(imgs[i], imgs[j], sq) == (sq[i] if i == j else 0)
                                for i in range(n) for j in range(n))
                M = [[GA.RF.const(imgs[j].get((i,), F(0))) for j in range(n)] for i in range(n)]
                d = GA.rf_mat_det(M).eval(F(0))
                ok = ok and d == (-1) ** k
                dets.append(d)
                # -g gives the same isometry
                mg = GA.neg(g)
                ok = ok and all(GA.eq(ad(mg, GA.gen(i), sq, GA.neg(ginv)), imgs[i]) for i in range(n))
                if k == 2 and norm == 1:
                    ok = ok and all(GA.eq(GA.mul(GA.mul(g, GA.gen(i), sq), GA.reverse(g), sq), imgs[i])
                                    for i in range(n))
                pairs += 1
    ok = ok and pairs == 6 + 4 + 10 + 10 + 10 + 10
    ok = ok and dets.count(1) == 26 and dets.count(-1) == 24
    GA.check("Ad is a homomorphism into O(p,q) with det (-1)^k; g and -g act alike; rotors act by R x R~", ok)
    return ok


def check_kernel_is_plus_minus_one():
    """Even and odd elements acting trivially by Ad on V: solved as a linear system."""
    premise("primer.centre")
    ok = True
    sizes = []
    for p, q in ((2, 0), (1, 1), (3, 0), (1, 2), (2, 2), (1, 3)):
        sq = GA.sig(p, q)
        n = len(sq)
        blades = GA.all_blades(n)
        for parity in (0, 1):
            bl = [b for b in blades if len(b) % 2 == parity]
            sign = 1 if parity == 0 else -1
            rows = []
            for i in range(n):
                cols = [S.coords(GA.sub(GA.mul({b: F(1)}, GA.gen(i), sq),
                                        GA.scal(sign, GA.mul(GA.gen(i), {b: F(1)}, sq))), n) for b in bl]
                for k in range(len(blades)):
                    rows.append([cols[j][k] for j in range(len(bl))])
            ns = S.nullspace(rows)
            sizes.append(len(ns))
            if parity == 0:
                ok = ok and len(ns) == 1 and all(v[j] == 0 for v in ns for j in range(1, len(bl)))
    ok = ok and sizes == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    # controls, degenerate: in R^{1,0,1} the null e_1 anticommutes with every vector (odd solution);
    # in R^{0,0,2} the even 1 + e_0 e_1 is invertible, with inverse 1 - e_0 e_1, and commutes with V
    sq = GA.sig(1, 0, 1)
    e1 = GA.gen(1)
    ok = ok and GA.anticommutes(e1, e1, sq) and GA.anticommutes(e1, GA.gen(0), sq)
    sq = GA.sig(0, 0, 2)
    g = GA.add(GA.sc(1), S.blade(0, 1))
    ok = ok and GA.eq(GA.mul(g, GA.sub(GA.sc(2), g), sq), GA.sc(1))
    ok = ok and all(GA.commutes(g, GA.gen(i), sq) for i in range(2))
    GA.check("nondegenerate: only scalars (even) and nothing (odd) satisfy Ad_g = 1 on V", ok)
    return ok
