"""odd-extensions.imported-frozen-point-degenerate-algebras: exact checks.

The rung as GA's Cl(2,4) (e_0 +1; e_1, e_2, e_3 -1; e_4 +1; e_5 -1), frozen point I = c e_4 + d e_5,
Q(I) = c^2 - d^2 = Lambda/3, Stelle-West vector V = (3/Lambda)(d e_4 + c e_5) (orthogonal to I and to the frame).
(1) Q(I) Q(V) = -1 for the samples with Lambda != 0, either sign.
(2) Stabilisers in so(2,4) = the 15 bivectors: the stabiliser of I (kernel of B -> [B, I]) is 10-dimensional for
    every sample. For Q(I) != 0 the invariant form <B B'>_0 restricted to it is nondegenerate (reductive: so(1,4)
    or so(2,3)). For Q(I) = 0 the restriction has a 4-dimensional radical, spanned by I e_mu (mu = 0..3), which is
    an abelian ideal (the translations of the Poincare-type stabiliser); the stabiliser of the null line [I]
    ([B, I] proportional to I) is 11-dimensional, the parabolic one.
(3) For every (p, q) with p + q <= 4, in Cl(p, q; 1) (GA signature with one generator of square 0) the
    nilpotent generator n satisfies n^2 = 0, n != 0 (a vector-type zero divisor), and n Cl is a two-sided ideal of
    dimension 2^(p+q) with every product of two of its elements zero.
The one-sided completions of the sheaf paper are cited, not recomputed (sheaf.one-sided-completion untouched).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
SAMPLES = [(F(2), F(1)), (F(1), F(2)), (F(3, 2), F(1)), (F(1), F(1)), (F(-2), F(-2))]
BIV = [GA.mul(GA.gen(i), GA.gen(j), SQ) for i, j in combinations(range(6), 2)]


def frozen(c, d):
    return {(4,): c, (5,): d}


def lie(a, b):
    return GA.sub(GA.mul(a, b, SQ), GA.mul(b, a, SQ))


def as_row(x, keys):
    return [x.get(k, F(0)) for k in keys]


def kernel_combos(images, keys):
    cols = [as_row(x, keys) for x in images]
    M = [[cols[j][i] for j in range(len(cols))] for i in range(len(keys))]
    if not M:
        return [[F(1) if i == j else F(0) for i in range(len(images))] for j in range(len(images))]
    return GA.field_kernel(M)


def combo(c, xs):
    return GA.add(*[GA.scal(x, xs[i]) for i, x in enumerate(c) if x])


def rank_mv(xs):
    keys = sorted({b for x in xs for b in x})
    return GA.rank_of_vectors([as_row(x, keys) for x in xs]) if keys else 0


def check_qi_times_qv():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    n = 0
    for c, d in SAMPLES:
        qi = c * c - d * d
        if qi == 0:
            continue
        n += 1
        V = GA.scal(1 / qi, {(4,): d, (5,): c})
        I = frozen(c, d)
        ok = ok and GA.dot(I, V, SQ) == 0 and GA.dot(V, V, SQ) == -1 / qi
        ok = ok and GA.dot(I, I, SQ) * GA.dot(V, V, SQ) == -1
    ok = ok and n == 3
    GA.check("Q(I) Q(V) = -1 for Lambda != 0", ok)
    return ok


def check_stabiliser_reductive_iff_non_null():
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for c, d in SAMPLES:
        I = frozen(c, d)
        imgs = [lie(B, I) for B in BIV]
        keys = [(i,) for i in range(6)]
        ker = kernel_combos(imgs, keys)
        stab = [combo(k, BIV) for k in ker]
        ok = ok and len(stab) == 10
        G = [[GA.mul(x, y, SQ).get((), F(0)) for y in stab] for x in stab]
        rad = GA.field_kernel(G)
        if c * c != d * d:
            ok = ok and rad == []
        else:
            ok = ok and len(rad) == 4
            radel = [combo(r, stab) for r in rad]
            trans = [GA.mul(I, GA.gen(m), SQ) for m in range(4)]
            ok = ok and rank_mv(radel) == 4 and rank_mv(radel + trans) == 4
            ok = ok and all(lie(x, y) == {} for x in trans for y in trans)
            ok = ok and all(rank_mv(trans + [lie(s, t)]) == 4 for s in stab for t in trans)
            # stabiliser of the null line: [B, I] in span{I}
            ext = [as_row(lie(B, I), keys) + [F(0)] for B in BIV] + [as_row(I, keys) + [F(1)]]
            M = [[ext[j][i] for j in range(len(ext))] for i in range(7)]
            line = GA.field_kernel(M[:6])
            ok = ok and len(line) == 11
    GA.check("stabiliser of I: 10-dim, reductive iff Q(I) != 0; at Q(I) = 0 Poincare-type, line stabiliser 11-dim", ok)
    return ok


def check_degenerate_clifford_ideal():
    premise("sheaf.degeneration-sheaf")
    premise("sheaf.resolution-ideal-theoretically")
    ok = True
    cases = 0
    for n in range(0, 5):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p, q, 1)
            nil = GA.gen(n)
            blades = GA.all_blades(n + 1)
            ok = ok and GA.mul(nil, nil, sq) == {} and nil != {}
            ideal = [GA.mul(nil, {b: F(1)}, sq) for b in blades]
            ideal = [x for x in ideal if x]
            ok = ok and rank_mv(ideal) == 2 ** n
            ok = ok and all(GA.mul(x, y, sq) == {} for x in ideal for y in ideal)
            gens = [GA.gen(i) for i in range(n + 1)]
            ok = ok and all(rank_mv(ideal + [GA.mul(g, x, sq), GA.mul(x, g, sq)]) == 2 ** n for x in ideal for g in gens)
            cases += 1
    ok = ok and cases == 15
    GA.check("Cl(p,q;1): nilpotent generator, n Cl a two-sided square-zero ideal of dimension 2^(p+q)", ok)
    return ok
