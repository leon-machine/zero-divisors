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


def check_contraction_derivation_and_expansion():
    premise("std-algebra.product-decomposition")
    premise("std-algebra.exterior-isomorphism")
    premise("std-algebra.involution-properties")
    ok = True
    tested = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        a = smpv(n, 2)
        X, Y = smp(n, 3), smp(n, 6)
        Xh = GA.grade_inv(X)
        lhs = S.lc(a, GA.mul(X, Y, sq), sq)
        rhs = GA.add(GA.mul(S.lc(a, X, sq), Y, sq), GA.mul(Xh, S.lc(a, Y, sq), sq))
        ok = ok and GA.eq(lhs, rhs)
        lhs = S.lc(a, S.outer(X, Y, sq), sq)
        rhs = GA.add(S.outer(S.lc(a, X, sq), Y, sq), S.outer(Xh, S.lc(a, Y, sq), sq))
        ok = ok and GA.eq(lhs, rhs)
        ok = ok and S.lc(a, S.lc(a, X, sq), sq) == {}
        tested += 1
    # the expansion for three vectors in a degenerate signature
    sq = GA.sig(2, 1, 1)
    a = smpv(4, 1)
    bs = [smpv(4, s) for s in (2, 3, 5)]
    lhs = S.lc(a, S.outer(S.outer(bs[0], bs[1], sq), bs[2], sq), sq)
    rhs = GA.add(GA.scal(GA.dot(a, bs[0], sq), S.outer(bs[1], bs[2], sq)),
                 GA.scal(-GA.dot(a, bs[1], sq), S.outer(bs[0], bs[2], sq)),
                 GA.scal(GA.dot(a, bs[2], sq), S.outer(bs[0], bs[1], sq)))
    ok = ok and GA.eq(lhs, rhs)
    ok = ok and [GA.dot(a, b, sq) for b in bs] == [2, 3, -2]
    # control: without the grade involution the outer-product rule fails
    sq = GA.sig(3, 0)
    a, X, Y = smpv(3, 2), smp(3, 3), smp(3, 6)
    bad = GA.add(S.outer(S.lc(a, X, sq), Y, sq), S.outer(X, S.lc(a, Y, sq), sq))
    ok = ok and not GA.eq(S.lc(a, S.outer(X, Y, sq), sq), bad)
    ok = ok and tested == 34
    GA.check("a lc is a graded derivation of both products, squares to 0, and expands a blade", ok)
    return ok
