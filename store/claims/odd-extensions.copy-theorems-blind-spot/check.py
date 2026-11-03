"""odd-extensions.copy-theorems-blind-spot: exact checks in GA.py.

Cl(2,4) has generators e1, e2 of square +1 (time) and e3..e6 of square -1 (space), held in GA.py
as indices 0..5. Wedderburn types are computed exactly: a primitive idempotent f is a product of
(1 + b)/2 over a greedily built maximal commuting set of blades of square +1 (inside the algebra
in question), and the corner fAf is shown to be a division algebra (R: dimension 1; C: basis f, x
with x^2 = -a f, a > 0; H: basis f, x, y, xy with x^2 = -a f, y^2 = -b f, xy = -yx).

(1) Cl^0(2,4) = Cl(2,3) = Cl(4,1): e_i e6 (i = 1..5) and e_i e1 (i = 2..6) satisfy the relations of
    Cl(2,3) and Cl(4,1) and their products span all 32 dimensions of Cl^0(2,4). I6 = e1..e6 is even,
    I6^2 = -1, and the centre of Cl^0(2,4) is span{1, I6}; the corner of a primitive idempotent of
    Cl^0(2,4) is span{f, I6 f} = C, and 32 = 2 * 4^2: Mat(4, C), with I6 its complex unit.
(2) Both oriented shadows sit inside Cl^0(2,4): e_i e6 (i = 2..5) generate a Cl(1,3) and e_i e1
    (i = 2..5) a Cl(3,1) (relations and 16-dimensional span).
(3) The rungs do not identify: Cl(2,4) has corner H (Mat(4, H)) and Cl(4,2) has corner R
    (Mat(8, R)), both simple with centre R, so they are not isomorphic.
(4) The odd extensions do not identify: the centres of Cl(2,3) and Cl(4,1) are spanned by 1 and
    omega with omega^2 = -1 (C, a field), those of Cl(3,2) and Cl(1,4) by 1 and omega with
    omega^2 = +1 (R + R: (1 + omega)/2 is a nontrivial central idempotent); so Cl(2,3) != Cl(3,2)
    and Cl(1,4) != Cl(4,1). Their even subalgebras do identify (phi(e_I) = (-1)^(|I|/2) e'_I is
    multiplicative on all even blade pairs of Cl(2,3) -> Cl(3,2) and of Cl(1,4) -> Cl(4,1)), so the
    distinction needs an odd element: the centre's omega is the bare new generator times the
    shadow's pseudoscalar.
Not computable: that no derived quantity of the series uses the bare fifth generator (imported).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ24 = GA.sig(2, 4)


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


def relations(gens, sq, target):
    for g, t in zip(gens, target):
        if not GA.eq(GA.mul(g, g, sq), GA.sc(t)):
            return False
    return all(GA.anticommutes(a, b, sq) for a, b in combinations(gens, 2))


def words(gens, sq):
    out = []
    for k in range(len(gens) + 1):
        for S in combinations(gens, k):
            out.append(prod(S, sq))
    return out


def corner(n, sq, pool):
    """corner dimension and name for a greedy primitive idempotent built from blades in pool"""
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
    d = rank(elems, n)

    def neg_square(x):
        s = GA.mul(x, x, sq)
        c = s.get((), F(0)) / f[()]
        return c < 0 and GA.eq(s, GA.scal(c, f))
    units = [x for x in elems if x and neg_square(x)]
    if d == 1:
        return d, "R", f
    if d == 2 and units:
        return d, "C", f
    for x in units:
        for y in units:
            xy = GA.mul(x, y, sq)
            if GA.is_zero(GA.add(xy, GA.mul(y, x, sq))) and rank([f, x, y, xy], n) == 4:
                return d, "H", f
    return d, "?", f


def check_even_subalgebra_is_mat4c():
    premise("odd-extensions.twistor-algebra")
    sq = SQ24
    e = [GA.gen(i) for i in range(6)]
    via6 = [GA.mul(e[i], e[5], sq) for i in range(5)]
    via1 = [GA.mul(e[i], e[0], sq) for i in range(1, 6)]
    assert relations(via6, sq, [1, 1, -1, -1, -1])
    assert relations(via1, sq, [-1, 1, 1, 1, 1])
    assert rank(words(via6, sq), 6) == 32 and rank(words(via1, sq), 6) == 32
    I6 = prod(e, sq)
    assert GA.eq(GA.mul(I6, I6, sq), GA.sc(-1))
    even = [b for b in GA.all_blades(6) if len(b) % 2 == 0]
    assert len(even) == 32
    centre = [b for b in even if all(GA.commutes(blade(b), blade(c), sq) for c in even)]
    assert centre == [(), (0, 1, 2, 3, 4, 5)]
    d, name, f = corner(6, sq, even)
    assert (d, name) == (2, "C")
    assert rank([f, GA.mul(I6, f, sq)], 6) == 2
    assert 32 == d * 4 ** 2
    return True


def check_both_shadows_inside():
    premise("odd-extensions.twistor-algebra")
    sq = SQ24
    e = [GA.gen(i) for i in range(6)]
    s13 = [GA.mul(e[i], e[5], sq) for i in range(1, 5)]
    s31 = [GA.mul(e[i], e[0], sq) for i in range(1, 5)]
    assert relations(s13, sq, [1, -1, -1, -1])
    assert relations(s31, sq, [-1, 1, 1, 1])
    assert rank(words(s13, sq), 6) == 16 and rank(words(s31, sq), 6) == 16
    return True


def check_rungs_not_isomorphic():
    premise("odd-extensions.imported-towers-clock")
    premise("odd-extensions.imported-representatives-dimension-nearest-four-types")
    out = {}
    for p, q in ((2, 4), (4, 2)):
        sq = GA.sig(p, q)
        allb = GA.all_blades(6)
        centre = [b for b in allb if all(GA.commutes(blade(b), GA.gen(i), sq) for i in range(6))]
        assert centre == [()]
        d, name, f = corner(6, sq, allb)
        out[(p, q)] = (d, name)
    assert out == {(2, 4): (4, "H"), (4, 2): (1, "R")}
    assert 2 ** 6 == out[(2, 4)][0] * 4 ** 2 and 2 ** 6 == out[(4, 2)][0] * 8 ** 2
    return True


IDX = {(2, 3): {0: 3, 1: 4, 2: 0, 3: 1, 4: 2}, (1, 4): {0: 4, 1: 0, 2: 1, 3: 2, 4: 3}}


def check_odd_extensions_differ():
    premise("odd-extensions.twistor-algebra")
    omega2 = {}
    for p, q in ((2, 3), (4, 1), (3, 2), (1, 4)):
        sq = GA.sig(p, q)
        allb = GA.all_blades(5)
        centre = [b for b in allb if all(GA.commutes(blade(b), GA.gen(i), sq) for i in range(5))]
        assert centre == [(), (0, 1, 2, 3, 4)]
        w = blade((0, 1, 2, 3, 4))
        omega2[(p, q)] = GA.mul(w, w, sq)[()]
        ep = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
        assert GA.eq(GA.mul(ep, ep, sq), ep) == (omega2[(p, q)] == 1)
    assert omega2 == {(2, 3): -1, (4, 1): -1, (3, 2): 1, (1, 4): 1}
    # the even subalgebras of the reversed pairs do identify
    for (p, q), idx in IDX.items():
        sq, sqr = GA.sig(p, q), GA.sig(q, p)
        assert all(sqr[idx[i]] == -sq[i] for i in range(5))
        even = [b for b in GA.all_blades(5) if len(b) % 2 == 0]

        def phi_b(b):
            x = prod([GA.gen(idx[i]) for i in b], sqr)
            return GA.scal((-1) ** (len(b) // 2), x)

        def phi(x):
            return GA.add(*[GA.scal(c, phi_b(b)) for b, c in x.items()]) if x else {}
        for b1 in even:
            for b2 in even:
                assert GA.eq(phi(GA.mul(blade(b1), blade(b2), sq)), GA.mul(phi_b(b1), phi_b(b2), sqr))
        assert rank([phi_b(b) for b in even], 5) == 16
    return True
