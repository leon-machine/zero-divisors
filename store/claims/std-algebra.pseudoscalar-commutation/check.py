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


def check_pseudoscalar_commutation():
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.grade-decomposition")
    premise("primer.sign")
    ok = True
    tested = 0
    nilpotent = 0
    for p, q, r in S.signatures(5):
        sq = GA.sig(p, q, r)
        n = len(sq)
        I = S.pseudoscalar(n)
        X = smp(n, n + p)
        for k in range(n + 1):
            Xk = S.grade(X, k)
            ok = ok and GA.eq(GA.mul(I, Xk, sq), GA.scal((-1) ** (k * (n - 1)), GA.mul(Xk, I, sq)))
        ok = ok and GA.eq(GA.mul(I, X, sq), GA.mul(X if n % 2 else GA.grade_inv(X), I, sq))
        prodQ = F(1)
        for s in sq:
            prodQ *= s
        ok = ok and GA.eq(GA.mul(I, GA.reverse(I), sq), GA.sc(prodQ))
        I2 = GA.mul(I, I, sq)
        if r == 0:
            ok = ok and GA.eq(I2, GA.sc((-1) ** (n * (n - 1) // 2) * (-1) ** q))
        else:
            ok = ok and I2 == {}
            nilpotent += 1
        tested += 1
    ok = ok and tested == 3 + 6 + 10 + 15 + 21
    ok = ok and nilpotent == 1 + 3 + 6 + 10 + 15
    GA.check("I X_k = (-1)^(k(n-1)) X_k I; I I~ = prod Q(e_i); I^2 = 0 iff degenerate (n <= 5)", ok)
    return ok
