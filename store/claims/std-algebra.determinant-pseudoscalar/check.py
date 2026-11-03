from fractions import Fraction as F
from itertools import combinations, permutations

import GA
import stdalg as S
from tp_premise import premise


def smp(n, seed, grades=None):
    """Deterministic sample element; coefficients ((3 seed + 1)(j + 1) + seed j^2) mod 7 - 3."""
    out = {}
    for j, b in enumerate(GA.all_blades(n)):
        if grades is not None and len(b) not in grades:
            continue
        c = ((3 * seed + 1) * (j + 1) + seed * j * j) % 7 - 3
        if c:
            out[b] = F(c)
    return out


def smpv(n, seed):
    return smp(n, seed, grades=(1,))


MATS = [
    [[2, 1, 0], [0, 1, 3], [1, 0, 1]],
    [[1, 2, 3], [0, 1, 4], [5, 6, 0]],
    [[1, 1, 0, 2], [0, 1, 1, 0], [3, 0, 1, 1], [0, 2, 0, 1]],
    [[1, 2, 0, 0], [2, 4, 0, 0], [0, 0, 1, 1], [0, 0, 1, 2]],
]


def leibniz_det(M):
    k = len(M)
    tot = F(0)
    for perm in permutations(range(k)):
        sign = 1
        for i in range(k):
            for j in range(i + 1, k):
                if perm[i] > perm[j]:
                    sign = -sign
        t = F(sign)
        for j in range(k):
            t *= M[perm[j]][j]
        tot += t
    return tot


def outermorphism(M, sq):
    n = len(M)
    imgs = [{(i,): F(M[i][j]) for i in range(n) if M[i][j] != 0} for j in range(n)]

    def fbar(x):
        out = {}
        for b, c in x.items():
            y = GA.sc(1)
            for i in b:
                y = S.outer(y, imgs[i], sq)
            out = GA.add(out, GA.scal(c, y))
        return out
    return fbar


def check_determinant_on_pseudoscalar():
    premise("std-algebra.exterior-isomorphism")
    premise("std-algebra.grade-decomposition")
    premise("std-algebra.functoriality")
    ok = True
    dets = []
    for M in MATS:
        n = len(M)
        d = leibniz_det(M)
        dets.append(d)
        for sq in (GA.sig(n, 0), GA.sig(1, n - 1), GA.sig(n - 1, 0, 1)):
            fbar = outermorphism(M, sq)
            I = S.pseudoscalar(n)
            ok = ok and GA.eq(fbar(I), GA.scal(d, I))
            # f-bar respects the outer product on sampled elements
            x, y = smp(n, 1), smp(n, 2)
            ok = ok and GA.eq(fbar(S.outer(x, y, sq)), S.outer(fbar(x), fbar(y), sq))
    ok = ok and dets == [5, 1, -6, 0]
    # multiplicativity: det(fg) = det f det g
    A, Bm = MATS[0], MATS[1]
    AB = [[sum(A[i][k] * Bm[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    ok = ok and leibniz_det(AB) == 5
    # for an isometry (a rational boost of R^{2,1}) the outermorphism is the algebra homomorphism
    sq = GA.sig(2, 1)
    Bt = [[F(5, 4), 0, F(3, 4)], [0, 1, 0], [F(3, 4), 0, F(5, 4)]]
    fbar = outermorphism(Bt, sq)
    bl = [{b: F(1)} for b in GA.all_blades(3)]
    ok = ok and all(GA.eq(fbar(GA.mul(x, y, sq)), GA.mul(fbar(x), fbar(y), sq)) for x in bl for y in bl)
    ok = ok and leibniz_det(Bt) == 1
    # control: for a non-isometry the outermorphism does not respect the geometric product
    fbar = outermorphism(MATS[0], GA.sig(3, 0))
    e0 = GA.gen(0)
    ok = ok and not GA.eq(fbar(GA.mul(e0, e0, GA.sig(3, 0))), GA.mul(fbar(e0), fbar(e0), GA.sig(3, 0)))
    GA.check("f-bar(I) = det(f) I in three signatures each; f-bar respects ^; isometry case is Cl(f)", ok)
    return ok
