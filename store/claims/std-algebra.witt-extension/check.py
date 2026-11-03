from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


# (signature, orthogonal non-null basis of U, images) for the reflection construction
CASES = [
    ((2, 1), [[1, 0, 0]], [[F(5, 4), 0, F(3, 4)]]),
    ((2, 1), [[1, 0, 0]], [[1, 1, 1]]),
    ((2, 2), [[1, 0, 0, 0], [0, 0, 1, 0]], [[0, 1, 0, 0], [0, 0, 0, 1]]),
    ((1, 3), [[0, 1, 0, 0], [1, 0, 0, 0]], [[1, 1, 1, 0], [2, 1, 1, 1]]),
]


def Bq(sq, x, y):
    return sum(F(sq[k]) * x[k] * y[k] for k in range(len(sq)))


def reflect(sq, a, x):
    c = 2 * Bq(sq, x, a) / Bq(sq, a, a)
    return [xi - c * ai for xi, ai in zip(x, a)]


def witt_by_reflections(sq, xs, ys):
    """Reflections whose product maps xs[i] to ys[i]; returns the list of reflection vectors."""
    refl = []

    def apply(x):
        for a in refl:
            x = reflect(sq, a, x)
        return x

    branches = []
    for x, y in zip(xs, ys):
        xp = apply(x)
        d = [a - b for a, b in zip(xp, y)]
        if all(a == 0 for a in d):
            branches.append(0)
            continue
        if Bq(sq, d, d) != 0:
            refl.append(d)
            branches.append(1)
        else:
            s = [a + b for a, b in zip(xp, y)]
            refl.append(s)
            refl.append(y)
            branches.append(2)
    return refl, apply, branches


def check_extension_by_reflections():
    ok = True
    allbr = []
    for (p, q), xs, ys in CASES:
        sq = GA.sig(p, q)
        n = len(sq)
        xs = [[F(a) for a in x] for x in xs]
        ys = [[F(a) for a in y] for y in ys]
        # f is an isometry of U: same Gram matrix
        ok = ok and all(Bq(sq, xs[i], xs[j]) == Bq(sq, ys[i], ys[j]) for i in range(len(xs)) for j in range(len(xs)))
        refl, apply, br = witt_by_reflections(sq, xs, ys)
        allbr += br
        ok = ok and all(apply(x) == y for x, y in zip(xs, ys))
        E = [[F(1) if k == j else F(0) for k in range(n)] for j in range(n)]
        im = [apply(e) for e in E]
        ok = ok and all(Bq(sq, im[i], im[j]) == sq[i] * (1 if i == j else 0) for i in range(n) for j in range(n))
    ok = ok and allbr == [1, 2, 1, 1, 2, 1]
    GA.check("isometries of nondegenerate subspaces extend by products of reflections (both branches)", ok)
    return ok


def check_null_line_extends_and_radical_obstructs():
    """A null line of R^{2,1} mapped to another null line extends (through hyperbolic pairs and the
    complements); in a degenerate space a radical vector cannot be moved off the radical."""
    sq = GA.sig(2, 1)
    u, u2 = [F(1), F(0), F(1)], [F(0), F(1), F(1)]
    # hyperbolic partners in the planes span(e0, e2) and span(e1, e2), and unit complements
    w, w2 = [F(1, 2), F(0), F(-1, 2)], [F(0), F(1, 2), F(-1, 2)]
    c, c2 = [F(0), F(1), F(0)], [F(1), F(0), F(0)]
    ok = Bq(sq, u, u) == 0 and Bq(sq, u2, u2) == 0
    ok = ok and Bq(sq, u, w) == Bq(sq, u2, w2) == 1 and Bq(sq, w, w) == Bq(sq, w2, w2) == 0
    ok = ok and Bq(sq, c, c) == Bq(sq, c2, c2) == 1
    ok = ok and all(Bq(sq, c, z) == 0 for z in (u, w)) and all(Bq(sq, c2, z) == 0 for z in (u2, w2))
    # sigma maps the basis (u, w, c) to (u2, w2, c2); it preserves all inner products of the bases
    src, dst = [u, w, c], [u2, w2, c2]
    ok = ok and all(Bq(sq, src[i], src[j]) == Bq(sq, dst[i], dst[j]) for i in range(3) for j in range(3))
    ok = ok and GA.rank_of_vectors(src) == 3 and GA.rank_of_vectors(dst) == 3
    # degenerate R^{1,1,1}: the radical vector e2 and the null vector e0 + e1 have the same form,
    # but e0 + e1 is not in the radical, so no isometry of V maps e2 to it
    sqd = GA.sig(1, 1, 1)
    r_, v = [F(0), F(0), F(1)], [F(1), F(1), F(0)]
    E = [[F(1) if k == j else F(0) for k in range(3)] for j in range(3)]
    ok = ok and Bq(sqd, r_, r_) == Bq(sqd, v, v) == 0
    ok = ok and all(Bq(sqd, r_, e) == 0 for e in E)
    ok = ok and [Bq(sqd, v, e) for e in E] == [1, -1, 0]
    GA.check("a null line extends to an isometry of R^{2,1}; the radical blocks extension in R^{1,1,1}", ok)
    return ok
