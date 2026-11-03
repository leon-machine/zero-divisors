"""odd-extensions.imported-representatives-dimension-nearest-four-types: exact checks.

(1) Representatives. Over all signatures with 1 <= p + q <= 10 the rule of the census under P3
    (dimension four for the even residues; for the odd ones dimension three where a signature with
    a single time exists there, else dimension five) gives (1,3) at 6, (3,1) at 2, (2,2) at 0,
    (4,0) and (0,4) at 4, (2,1) at 1, (1,2) at 7, (4,1) at 3, (1,4) at 5; the residues without a
    causal (single-time) representative are exactly 0 and 4, so six admit matter.
(2) Types, from exact Wedderburn invariants computed in GA.py: the centre (central blades), and a
    primitive idempotent f (product of (1 + b)/2 over a maximal commuting set of blades of square +1,
    found greedily) whose corner fAf is shown to be a division algebra: R (dimension 1), or H
    (basis f, x, y, xy with x^2 = -a f, y^2 = -b f, a, b > 0, xy = -yx). Cl(1,3): centre R,
    fAf = H, 16 = 2^2 * 4, so Mat(2, H) with one irreducible module of real dimension 8;
    Cl(3,1): centre R, fAf = R, Mat(4, R), one module of dimension 4. The division algebras differ,
    so by Wedderburn's uniqueness the two are not isomorphic.
(3) The type is a function of the residue: the eight signatures with p + q <= 6 of residues 6 and 2
    ((0,2), (1,3), (2,4), (6,0); (2,0), (3,1), (4,2), (0,6)) are simple, residue 6 has fAf = H
    and every one of residue 2 has fAf = R (simple, centre R).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

NMAX = 10
SIGS = [(p, q) for p in range(NMAX + 1) for q in range(NMAX + 1) if 1 <= p + q <= NMAX]
STATED = {6: [(1, 3)], 2: [(3, 1)], 0: [(2, 2)], 4: [(0, 4), (4, 0)],
          1: [(2, 1)], 7: [(1, 2)], 3: [(4, 1)], 5: [(1, 4)]}


def res(p, q):
    return (p - q) % 8


def causal(p, q):
    return min(p, q) == 1


def representatives(r):
    if r % 2 == 0:
        return sorted(s for s in SIGS if sum(s) == 4 and res(*s) == r)
    three = [s for s in SIGS if sum(s) == 3 and res(*s) == r and causal(*s)]
    if three:
        return sorted(three)
    return sorted(s for s in SIGS if sum(s) == 5 and res(*s) == r and causal(*s))


def blade(b):
    return {b: F(1)}


def rank(xs, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in xs])


def centre_dim(p, q):
    sq = GA.sig(p, q)
    n = p + q
    return sum(1 for b in GA.all_blades(n)
               if all(GA.commutes(blade(b), GA.gen(i), sq) for i in range(n)))


def corner(p, q):
    """(dim fAf, division algebra name) for a greedily built primitive idempotent f"""
    n, sq = p + q, GA.sig(p, q)
    chosen, group = [], {(): F(1)}
    for b in GA.all_blades(n):
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
    f = GA.sc(1)
    for b in chosen:
        f = GA.mul(f, GA.scal(F(1, 2), GA.add(GA.sc(1), blade(b))), sq)
    assert GA.eq(GA.mul(f, f, sq), f)
    elems = [GA.mul(GA.mul(f, blade(b), sq), f, sq) for b in GA.all_blades(n)]
    d = rank(elems, n)
    nz = [x for x in elems if x]

    def neg_square(x):
        s = GA.mul(x, x, sq)
        c = s.get((), F(0)) / f[()]
        return c < 0 and GA.eq(s, GA.scal(c, f))
    if d == 1:
        return d, "R"
    units = [x for x in nz if neg_square(x)]
    if d == 2 and units:
        return d, "C"
    for x in units:
        for y in units:
            xy = GA.mul(x, y, sq)
            if GA.is_zero(GA.add(xy, GA.mul(y, x, sq))) and rank([f, x, y, xy], n) == 4:
                return d, "H"
    return d, "not a division algebra"


def check_representatives_and_sterile():
    premise("dark-matter.towers-are-residues-single-clock-filter")
    reps = {r: representatives(r) for r in range(8)}
    assert reps == STATED
    sterile = sorted(r for r in range(8) if not any(causal(*s) for s in reps[r]))
    assert sterile == [0, 4]
    assert 8 - len(sterile) == 6
    return True


def check_shadow_types():
    premise("dark-matter.type-residue-what-each-tower-can")
    assert centre_dim(1, 3) == 1 and centre_dim(3, 1) == 1
    d13, D13 = corner(1, 3)
    d31, D31 = corner(3, 1)
    assert (d13, D13) == (4, "H") and (d31, D31) == (1, "R")
    m13_sq, m31_sq = 2 ** 4 // d13, 2 ** 4 // d31
    assert m13_sq == 2 ** 2 and m31_sq == 4 ** 2
    assert 2 * d13 == 8 and 4 * d31 == 4            # irreducible module m * dim D
    assert D13 != D31
    return True


def check_type_depends_on_residue_alone():
    premise("dark-matter.type-residue-what-each-tower-can")
    seen = {6: set(), 2: set()}
    count = 0
    for n in range(1, 7):
        for p in range(n + 1):
            q = n - p
            r = res(p, q)
            if r in seen:
                assert centre_dim(p, q) == 1
                seen[r].add(corner(p, q)[1])
                count += 1
    assert seen == {6: {"H"}, 2: {"R"}} and count == 8
    return True
