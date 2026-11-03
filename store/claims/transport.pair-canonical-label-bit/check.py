"""transport.pair-canonical-label-bit: exact checks.

(1) The pair and the involution: for sample idempotents e not in {0, 1} (conjugated blade
    idempotents, so not blades themselves) in Cl(1,1), Cl(2,2), Cl(1,3), Cl(3,1): u = 2e - 1 has
    u^2 = 1, e = (1 + u)/2 and 1 - e = (1 - u)/2 are its spectral projections (u e = e,
    u(1 - e) = -(1 - e), e(1 - e) = 0), and exchanging e with 1 - e is u -> -u.
(2) Type P label (Theorem transport.classification-idempotent-orbits(2)): the conjugator space
    {g : g e = (1 - e) g} is computed as an exact kernel. For balanced e (dim eA = dim (1 - e)A) it
    contains an invertible element (left multiplication of full rank), so the labelling is inner;
    for unbalanced e the right-ideal dimensions differ (4 against 12 in Cl(2,2) and Cl(3,1)) and a
    generic element of the conjugator space is singular, so rank order fixes the label.
(3) Type C label (Proposition transport.ascent-renders-grade-involution-inner): in the split
    signatures (1,0), (2,1), (0,3), (3,2) the central eps_+- are fixed by every inner automorphism, the
    grade involution swaps them, and no element anticommutes with all generators (exact kernel {0}),
    so the swap is outer; after the ascent by one generator e_new of either sign, e_new eps_+ e_new^-1
    = eps_- and the swap is inner.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def el(*terms):
    out = {}
    for c, b in terms:
        out = GA.add(out, {tuple(b): F(c)})
    return out


# (p, q, blade idempotent factors, conjugating element g, balanced?)
IDEMS = [
    (1, 1, [[0]], el((2, []), (1, [1])), True),
    (2, 2, [[0, 2]], el((3, []), (1, [1]), (1, [0, 1])), True),
    (1, 3, [[0]], el((2, []), (1, [0, 1])), True),
    (2, 2, [[0], [1, 3]], el((2, []), (1, [2])), False),
    (3, 1, [[0], [1, 3]], el((3, []), (1, [2]), (1, [0, 1])), False),
]


def build(p, q, factors, g):
    sq = GA.sig(p, q)
    e = GA.sc(1)
    for b in factors:
        e = GA.mul(e, GA.scal(F(1, 2), GA.add(GA.sc(1), {tuple(b): F(1)})), sq)
    n = p + q
    blades = GA.all_blades(n)
    gi = inverse(g, sq, blades)
    return sq, blades, GA.mul(GA.mul(g, e, sq), gi, sq)


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def lmat(x, sq, blades):
    cols = [coords(GA.mul(x, {b: F(1)}, sq), blades) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


def inverse(x, sq, blades):
    sol = GA.field_solve(lmat(x, sq, blades), coords(GA.sc(1), blades))
    return {b: c for b, c in zip(blades, sol) if c != 0}


def right_ideal_dim(e, sq, blades):
    return GA.field_rank([coords(GA.mul(e, {b: F(1)}, sq), blades) for b in blades])


def check_pair_and_involution_determine_each_other():
    ok = True
    for p, q, factors, g, bal in IDEMS:
        sq, blades, e = build(p, q, factors, g)
        one = GA.sc(1)
        ok = ok and GA.eq(GA.mul(e, e, sq), e) and not GA.is_zero(e) and not GA.eq(e, one)
        ok = ok and len(e) > 1 + len(factors)            # a genuine conjugate, not a blade idempotent
        u = GA.sub(GA.scal(2, e), one)
        f = GA.sub(one, e)
        ok = ok and GA.eq(GA.mul(u, u, sq), one)
        ok = ok and GA.eq(GA.scal(F(1, 2), GA.add(one, u)), e) and GA.eq(GA.scal(F(1, 2), GA.sub(one, u)), f)
        ok = ok and GA.eq(GA.mul(u, e, sq), e) and GA.eq(GA.mul(u, f, sq), GA.neg(f))
        ok = ok and GA.is_zero(GA.mul(e, f, sq))
        ok = ok and GA.eq(GA.sub(GA.scal(2, f), one), GA.neg(u))
    GA.check("u = 2e - 1 is an involution with spectral projections e, 1 - e; relabelling is u -> -u", ok)
    return ok


def check_type_p_label_inner_iff_balanced():
    premise("transport.classification-idempotent-orbits")
    ok = True
    dims = []
    for p, q, factors, g, bal in IDEMS:
        sq, blades, e = build(p, q, factors, g)
        f = GA.sub(GA.sc(1), e)
        de, df = right_ideal_dim(e, sq, blades), right_ideal_dim(f, sq, blades)
        dims.append((de, df))
        cols = []
        for b in blades:
            x = {b: F(1)}
            cols.append(coords(GA.sub(GA.mul(x, e, sq), GA.mul(f, x, sq)), blades))
        M = [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]
        ker = GA.field_kernel(M)
        generic = {}
        for t, kv in enumerate(ker):
            generic = GA.add(generic, GA.scal(t + 1, {b: c for b, c in zip(blades, kv) if c != 0}))
        full = GA.field_rank(lmat(generic, sq, blades)) == len(blades)
        ok = ok and full == bal and (de == df) == bal
        if full:
            gi = inverse(generic, sq, blades)
            ok = ok and GA.eq(GA.mul(GA.mul(generic, e, sq), gi, sq), f)
    ok = ok and dims == [(2, 2), (8, 8), (8, 8), (4, 12), (4, 12)]
    GA.check("e ~ 1 - e by an inner automorphism exactly for the balanced idempotents", ok)
    return ok


def check_type_c_label_outer_until_ascent():
    premise("transport.ascent-renders-grade-involution-inner")
    ok = True
    for p, q in ((1, 0), (2, 1), (0, 3), (3, 2)):
        n = p + q
        sq = GA.sig(p, q)
        blades = GA.all_blades(n)
        w = {tuple(range(n)): F(1)}
        ep = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
        em = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
        ok = ok and all(GA.commutes(GA.gen(i), ep, sq) for i in range(n))
        ok = ok and GA.eq(GA.grade_inv(ep), em)
        # no g anticommutes with every generator: the grade involution is not inner
        rows = []
        for b in blades:
            x = {b: F(1)}
            col = []
            for i in range(n):
                col += coords(GA.add(GA.mul(x, GA.gen(i), sq), GA.mul(GA.gen(i), x, sq)), blades)
            rows.append(col)
        M = [[rows[j][i] for j in range(len(blades))] for i in range(len(rows[0]))]
        ok = ok and GA.field_rank(M) == len(blades)
        for s in (1, -1):
            sq2 = sq + (s,)
            en = GA.gen(n)
            en_inv = GA.scal(F(s), en)
            ok = ok and GA.eq(GA.mul(en, en_inv, sq2), GA.sc(1))
            ok = ok and GA.eq(GA.mul(GA.mul(en, ep, sq2), en_inv, sq2), em)
    GA.check("eps_+- are swapped only by the outer grade involution; after the ascent e_new swaps them inner", ok)
    return ok
