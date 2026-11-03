"""odd-extensions.imported-copy-theorem-soldered-residue: exact checks of the algebraic clauses.

(1) Cl^0(2,4) = Cl^0(4,2): with e'_j the generator of Cl(4,2) of opposite square to e_i of Cl(2,4),
    phi(e_I) = (-1)^(|I|/2) e'_I is multiplicative on all 32 x 32 pairs of even blades and
    bijective (rank 32); it preserves grade and commutes with reversion, so it carries the
    products of pairs of vectors (phi(uv) = -u'v') and the spin group of one onto that of the
    other: Spin(2,4) = Spin(4,2).
(2) Both are Mat(4, C): the centre of Cl^0(2,4) is span{1, I6} with I6^2 = -1, and a primitive
    idempotent f (product of (1 + b)/2 over a greedy maximal commuting set of even blades of square
    +1) has corner span{f, I6 f} = C, with 32 = 2 * 4^2; the same holds in Cl^0(4,2).
(3) The residue is soldered: (2,4) and (4,2) have residues 6 and 2, and the Gram forms of their
    generating subspaces have congruence signatures (2,4) and (4,2), so no isomorphism carrying
    vectors to vectors joins Cl(2,4) and Cl(4,2), although their even parts are isomorphic by (1).
Not computable: that the one metric superselects the tower charge, and the invariance of the mass
formula and helicity form beyond their algebraic carrier.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ24, SQ42 = GA.sig(2, 4), GA.sig(4, 2)
IDX = {0: 4, 1: 5, 2: 0, 3: 1, 4: 2, 5: 3}
EVEN = [b for b in GA.all_blades(6) if len(b) % 2 == 0]
# sample vectors u, v of Cl(2,4) for phi(uv) = -u'v'
U_SAMPLE = {(0,): F(1), (2,): F(2), (5,): F(-1)}
V_SAMPLE = {(1,): F(3), (3,): F(1), (4,): F(1, 2)}


def blade(b):
    return {b: F(1)}


def prod(xs, sq):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def rank(xs, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in xs])


def phi_blade(b):
    return GA.scal((-1) ** (len(b) // 2), prod([GA.gen(IDX[i]) for i in b], SQ42))


def phi(x):
    return GA.add(*[GA.scal(c, phi_blade(b)) for b, c in x.items()]) if x else {}


def corner(sq, pool):
    chosen, group = [], {(): F(1)}
    for b in pool:
        x = blade(b)
        if b == () or b in group or GA.mul(x, x, sq) != GA.sc(1):
            continue
        if not all(GA.commutes(x, blade(c), sq) for c in chosen):
            continue
        chosen.append(b)
        new = dict(group)
        for g, s in group.items():
            (gb, gs), = GA.mul({g: s}, x, sq).items()
            new[gb] = gs
        group = new
    f = prod([GA.scal(F(1, 2), GA.add(GA.sc(1), blade(b))) for b in chosen], sq)
    assert GA.eq(GA.mul(f, f, sq), f)
    elems = [GA.mul(GA.mul(f, blade(b), sq), f, sq) for b in pool]
    return rank(elems, 6), f


def check_even_subalgebras_isomorphic():
    premise("dark-matter.mirror-tower-copy-one")
    assert all(SQ42[IDX[i]] == -SQ24[i] for i in range(len(SQ24)))
    assert len(EVEN) == 32
    for b1 in EVEN:
        for b2 in EVEN:
            assert GA.eq(phi(GA.mul(blade(b1), blade(b2), SQ24)), GA.mul(phi_blade(b1), phi_blade(b2), SQ42))
    assert rank([phi_blade(b) for b in EVEN], len(SQ42)) == 32
    for b in EVEN:
        img = phi_blade(b)
        assert all(len(c) == len(b) for c in img)
        assert GA.eq(GA.reverse(img), phi(GA.reverse(blade(b))))
    u, v = U_SAMPLE, V_SAMPLE
    up = {(IDX[i],): c for (i,), c in u.items()}
    vp = {(IDX[i],): c for (i,), c in v.items()}
    assert GA.eq(phi(GA.mul(u, v, SQ24)), GA.scal(-1, GA.mul(up, vp, SQ42)))
    return True


def check_both_are_mat4c():
    premise("dark-matter.mirror-tower-copy-one")
    for sq in (SQ24, SQ42):
        I6 = prod([GA.gen(i) for i in range(6)], sq)
        assert GA.eq(GA.mul(I6, I6, sq), GA.sc(-1))
        centre = [b for b in EVEN if all(GA.commutes(blade(b), blade(c), sq) for c in EVEN)]
        assert centre == [(), (0, 1, 2, 3, 4, 5)]
        d, f = corner(sq, EVEN)
        assert d == 2
        If = GA.mul(I6, f, sq)
        assert rank([f, If], 6) == 2 and GA.eq(GA.mul(If, If, sq), GA.scal(-1, f))
        assert len(EVEN) == d * 4 ** 2
    return True


def check_residue_is_soldered():
    premise("dark-matter.residue-soldered-invariant-not-algebraic-one")
    out = {}
    for p, q in ((2, 4), (4, 2)):
        sq = GA.sig(p, q)
        G = [[GA.dot(GA.gen(i), GA.gen(j), sq) for j in range(6)] for i in range(6)]
        out[(p - q) % 8] = GA.congruence_signature(G)
    assert out == {6: (2, 4, 0), 2: (4, 2, 0)}
    return True
