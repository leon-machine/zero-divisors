from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def refl(u, x, sq):
    return GA.sub(x, GA.scal(2 * GA.dot(x, u, sq) / GA.dot(u, u, sq), u))


def apply(images, x):
    out = {}
    for b, c in x.items():
        out = GA.add(out, GA.scal(c, images[b[0]]))
    return out


def factor(images, sq):
    """The constructive step of the proof: fix e_0, e_1, ... in turn by one or two reflections.
    Returns the reflecting vectors, applied last-first, with f = s_{u_1} ... s_{u_k}."""
    n = len(sq)
    h = [dict(v) for v in images]
    us = []
    for i in range(n):
        a = GA.gen(i)
        b = h[i]
        if GA.eq(a, b):
            continue
        d = GA.sub(b, a)
        steps = [d] if GA.dot(d, d, sq) != 0 else [GA.add(b, a), a]
        for u in steps:
            h = [refl(u, y, sq) for y in h]
            us.append(u)
    return us, h


# rational isometries: (signature, images of the basis)
ISOMETRIES = [
    ((2, 0, 0), [[F(3, 5), F(4, 5)], [F(-4, 5), F(3, 5)]]),
    ((1, 1, 0), [[F(5, 4), F(3, 4)], [F(3, 4), F(5, 4)]]),
    ((1, 1, 0), [[F(-5, 4), F(3, 4)], [F(-3, 4), F(5, 4)]]),
    ((3, 0, 0), [[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
    ((2, 1, 0), [[F(3, 4), 1, F(3, 4)], [F(-4, 5), F(3, 5), 0], [F(9, 20), F(3, 5), F(5, 4)]]),
    ((1, 2, 0), [[F(5, 3), F(4, 3), 0], [F(4, 3), F(5, 3), 0], [0, 0, -1]]),
]


def check_isometries_factor_into_reflections():
    ok = True
    counts = []
    for (p, q, r), rows in ISOMETRIES:
        sq = GA.sig(p, q, r)
        n = len(sq)
        imgs = [S.vec(row) for row in rows]
        ok = ok and all(GA.dot(imgs[i], imgs[j], sq) == (sq[i] if i == j else 0)
                        for i in range(n) for j in range(n))
        us, h = factor(imgs, sq)
        ok = ok and all(GA.eq(h[i], GA.gen(i)) for i in range(n))
        ok = ok and all(GA.dot(u, u, sq) != 0 for u in us)
        # recompose: s_{u_1} ... s_{u_k} applied to e_i gives f(e_i)
        for i in range(n):
            y = GA.gen(i)
            for u in reversed(us):
                y = refl(u, y, sq)
            ok = ok and GA.eq(y, imgs[i])
        counts.append(len(us))
    ok = ok and counts == [2, 2, 1, 2, 2, 3]
    ok = ok and all(c <= len(rows) for c, (_, rows) in zip(counts, ISOMETRIES))
    GA.check("six rational isometries in signatures (2,0),(1,1),(3,0),(2,1),(1,2) factor into <= n reflections", ok)
    return ok


def check_degenerate_counterexample():
    """On R^{1,0,1}, e_1 -> 2 e_1 is an isometry; every reflection fixes e_1."""
    sq = GA.sig(1, 0, 1)
    ok = GA.dot(GA.scal(2, GA.gen(1)), GA.scal(2, GA.gen(1)), sq) == 0
    ok = ok and GA.dot(GA.gen(0), GA.scal(2, GA.gen(1)), sq) == 0
    fixed = 0
    for c in ([1, 0], [1, 1], [1, -3], [2, 5]):
        u = S.vec(c)
        ok = ok and GA.dot(u, u, sq) != 0
        ok = ok and GA.eq(refl(u, GA.gen(1), sq), GA.gen(1))
        fixed += 1
    ok = ok and fixed == 4
    GA.check("degenerate R^{1,0,1}: reflections fix the radical, so e_1 -> 2 e_1 is not a product of them", ok)
    return ok
