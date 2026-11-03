"""odd-extensions.imported-towers-clock: exact checks.

Floors Cl(p+1, q+1) in GA.py (ground generators first, then the plane e, f with squares +1, -1).
Checked:
(1) the (1,1) ascent preserves p - q and Cl(p+1, q+1) = Mat_2(Cl(p,q)): the twisted ground
    generators x omega satisfy the ground relations and commute with e and f; the plane algebra has
    the four matrix units v w, v, w, w v (E_{ST} E_{UW} = delta_{TU} E_{SW}, sum E_{SS} = 1); and
    the products of the twisted words with the plane words are 2^(n+2) distinct basis blades, for
    all 10 signatures with p + q <= 3.
(2) the period eight: Cl(8,0) = Cl(0,8) = Mat_16(R) exactly (an idempotent of four commuting
    factors with corner R f and left ideal of dimension 16), and Cl(p+8, q), Cl(p, q+8) are
    Cl(p,q) tensor that factor by the same twist, for (p,q) = (1,0), (0,1).
(3) under the ascent and the shifts by eight, the signatures with p + q <= 14 fall into exactly
    eight classes, one per residue p - q mod 8: the eight parallel towers.
The general statements are the cited theorems; the instances above are their finite core.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
from tp_premise import premise

# ---------------------------------------------------------------------------
# Exact Clifford helpers on top of GA.py (elements are dicts {blade: Fraction}).
# ---------------------------------------------------------------------------


def blade_el(b, c=1):
    return {tuple(b): F(c)} if c else {}


def prod(xs, sq):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def coords(x, n):
    return [x.get(b, F(0)) for b in GA.all_blades(n)]


def span_rank(els, n):
    els = [e for e in els if not GA.is_zero(e)]
    return GA.rank_of_vectors([coords(e, n) for e in els]) if els else 0


def words(gens, sq):
    """The ordered products of all subsets of gens: they span the generated subalgebra
    when the generators pairwise anticommute and square to nonzero scalars."""
    out = []
    for r in range(len(gens) + 1):
        for idx in combinations(range(len(gens)), r):
            out.append(prod([gens[i] for i in idx], sq))
    return out


def scalar_of(x):
    """x as a scalar if it is one, else None."""
    if GA.is_zero(x):
        return F(0)
    if set(x) == {()}:
        return x[()]
    return None


def anticommuting_with_squares(gens, sq):
    """The list of squares if the gens pairwise anticommute and square to scalars, else None."""
    out = []
    for i, g in enumerate(gens):
        s = scalar_of(GA.mul(g, g, sq))
        if s is None:
            return None
        out.append(s)
        for h in gens[i + 1:]:
            if not GA.anticommutes(g, h, sq):
                return None
    return out


def volume(n, sq):
    return prod([GA.gen(i) for i in range(n)], sq)


def is_central(x, n, sq):
    return all(GA.commutes(x, GA.gen(i), sq) for i in range(n))


def corner(f, basis, sq, n):
    """An independent spanning list of f b f, b in basis."""
    out, vecs = [], []
    for b in basis:
        y = GA.mul(GA.mul(f, b, sq), f, sq)
        if GA.is_zero(y):
            continue
        v = coords(y, n)
        if GA.rank_of_vectors(vecs + [v]) > len(vecs):
            vecs.append(v)
            out.append(y)
    return out


def corner_division_type(f, basis, sq, n):
    """'R', 'C' or 'H' when f is an idempotent whose corner f A f is that division algebra
    (exact: R = span{f}; C = f plus an element squaring to -f; H = quaternion units i, j,
    i j with i^2 = j^2 = -f, i j = -j i), else None. A division corner makes f primitive,
    so the letter is the Wedderburn division algebra of the simple algebra A."""
    if not GA.eq(GA.mul(f, f, sq), f):
        return None
    cb = corner(f, basis, sq, n)
    if len(cb) == 1:
        return "R"
    roots = []
    for b in basis:
        y = GA.mul(GA.mul(f, b, sq), f, sq)
        if not GA.is_zero(y) and GA.eq(GA.mul(y, y, sq), GA.neg(f)):
            roots.append(y)
    if len(cb) == 2 and roots:
        return "C"
    if len(cb) == 4:
        for i, a in enumerate(roots):
            for c in roots[i + 1:]:
                if GA.is_zero(GA.add(GA.mul(a, c, sq), GA.mul(c, a, sq))):
                    if span_rank([f, a, c, GA.mul(a, c, sq)], n) == 4:
                        return "H"
    return None


def idempotent_from(us, sq):
    """prod (1 + u)/2 over commuting elements u with u^2 = 1."""
    f = GA.sc(1)
    for u in us:
        f = GA.mul(f, GA.scal(F(1, 2), GA.add(GA.sc(1), u)), sq)
    return f


def simple_copy_type(gens, sq, n):
    """For a simple subalgebra spanned by words(gens): (k, D) with the subalgebra Mat_k(D),
    found from an idempotent f = prod (1 + u)/2 (u words squaring to 1, commuting) whose corner
    is a division algebra; dim = k^2 dim D is asserted. None if no such f is found."""
    basis = words(gens, sq)
    dim = span_rank(basis, n)
    units = [u for u in basis if scalar_of(u) is None and GA.eq(GA.mul(u, u, sq), GA.sc(1))]
    trials = [[]] + [[u] for u in units]
    trials += [[u, v] for i, u in enumerate(units) for v in units[i + 1:] if GA.commutes(u, v, sq)]
    for us in trials:
        f = idempotent_from(us, sq)
        if GA.is_zero(f):
            continue
        d = corner_division_type(f, basis, sq, n)
        if d is None:
            continue
        dd = {"R": 1, "C": 2, "H": 4}[d]
        k = 1
        while k * k * dd < dim:
            k += 1
        assert k * k * dd == dim
        return (k, d)
    return None
# ---------------------------------------------------------------------------
# Floors of the tower in GA.py: T_k over Cl(p,q) has the ground generators 0..n-1 (p squares +1,
# then q squares -1) and plane j (0-based) at n + 2j (e_j, square +1), n + 2j + 1 (f_j, square -1).
# v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2, omega_j = e_j f_j, Omega_k = omega_1 ... omega_k.
# ---------------------------------------------------------------------------


def floor_sq(p, q, k):
    return tuple([1] * p + [-1] * q + [1, -1] * k)


def plane(n, j):
    e, f = GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1)
    return GA.scal(F(1, 2), GA.add(e, f)), GA.scal(F(1, 2), GA.sub(e, f))


def big_omega(n, k, sq):
    return prod([GA.mul(GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1), sq) for j in range(k)], sq)


def twisted_ground(n, k, sq):
    Om = big_omega(n, k, sq)
    return [GA.mul(GA.gen(i), Om, sq) for i in range(n)]


def matrix_units(n, k, sq):
    """E[(S, T)] = v_S f v_T^dagger, S, T subsets of the k planes, f = prod_j w_j v_j the vacuum
    projector and v_T^dagger the reversed product of the w's; the Fock-basis matrix units of B_k."""
    vs, ws = zip(*[plane(n, j) for j in range(k)]) if k else ((), ())
    f = prod([GA.mul(ws[j], vs[j], sq) for j in range(k)], sq)
    subsets = [S for r in range(k + 1) for S in combinations(range(k), r)]
    E = {}
    for S in subsets:
        left = prod([vs[j] for j in S], sq)
        for T in subsets:
            right = prod([ws[j] for j in reversed(T)], sq)
            E[(S, T)] = GA.mul(GA.mul(left, f, sq), right, sq)
    return subsets, E


def matrix_units_ok(subsets, E, sq):
    one = GA.add(*[E[(S, S)] for S in subsets])
    if not GA.eq(one, GA.sc(1)):
        return False
    for (S, T), x in E.items():
        for (U, W), y in E.items():
            want = E[(S, W)] if T == U else {}
            if not GA.eq(GA.mul(x, y, sq), want):
                return False
    return True


def tensor_blades(gens_a, gens_b, sq):
    """Products of the ordered words of gens_a with those of gens_b, when every one is a single
    basis blade: the set of blades hit (None if some product is not a single blade)."""
    seen = set()
    for a in words(gens_a, sq):
        for b in words(gens_b, sq):
            x = GA.mul(a, b, sq)
            if len(x) != 1:
                return None
            seen.add(next(iter(x)))
    return seen

ASCENT_K1 = [(p, q) for p in range(4) for q in range(4) if p + q <= 3]
SHIFT_BASES = [(1, 0), (0, 1)]
FOUR_BLADES = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 4, 5), (0, 2, 4, 6)]


def ascent_ok(p, q, k):
    n = p + q
    sq = floor_sq(p, q, k)
    tw = twisted_ground(n, k, sq)
    ok = anticommuting_with_squares(tw, sq) == [1] * p + [-1] * q
    ok = ok and all(GA.commutes(x, GA.gen(n + i), sq) for x in tw for i in range(2 * k))
    subsets, E = matrix_units(n, k, sq)
    ok = ok and len(E) == 4 ** k and matrix_units_ok(subsets, E, sq)
    plane_gens = [GA.gen(n + i) for i in range(2 * k)]
    hit = tensor_blades(tw, plane_gens, sq)
    ok = ok and hit is not None and len(hit) == 2 ** (n + 2 * k)
    ok = ok and ((p + k) - (q + k)) % 8 == (p - q) % 8
    return ok


def check_ascent_is_matrix_amplification_one_step():
    premise("tower.commuting-copies")
    ok = all(ascent_ok(p, q, 1) for p, q in ASCENT_K1) and len(ASCENT_K1) == 10
    GA.check("Cl(p+1,q+1) = Mat_2(Cl(p,q)) with p - q fixed, all p + q <= 3", ok)
    return ok


def mat16_ok(sq8):
    """Cl(8,0) or Cl(0,8) (sq8 the squares of its 8 generators, placed first) is Mat_16(R)."""
    e = [GA.gen(i) for i in range(8)]
    us = [prod([e[i] for i in b], sq8) for b in FOUR_BLADES]
    ok = all(GA.eq(GA.mul(u, u, sq8), GA.sc(1)) for u in us)
    ok = ok and all(GA.commutes(u, w, sq8) for u in us for w in us)
    f = idempotent_from(us, sq8)
    ok = ok and GA.eq(GA.mul(f, f, sq8), f) and f.get((), F(0)) == F(1, 16)
    # corner f A f = R f: a blade anticommuting with some u_i has f b f = 0, since
    # (1 + u) b (1 + u) = b (1 - u)(1 + u) = 0; a blade commuting with all u_i has f b f = b f,
    # which must be a multiple of f
    for b in GA.all_blades(8):
        x = blade_el(b)
        if all(GA.commutes(x, u, sq8) for u in us):
            y = GA.mul(x, f, sq8)
            lam = y.get((), F(0)) / f[()]
            ok = ok and GA.eq(y, GA.scal(lam, f)) and lam in (1, -1)
        else:
            ok = ok and any(GA.anticommutes(x, u, sq8) for u in us)
    ok = ok and span_rank([GA.mul(blade_el(b), f, sq8) for b in GA.all_blades(8)], 8) == 16
    return ok


def check_period_eight():
    premise("tower.rigidity-clock-frozen")
    ok = mat16_ok((1,) * 8) and mat16_ok((-1,) * 8)
    for p, q in SHIFT_BASES:
        n = p + q
        for s8 in (1, -1):
            sq = tuple([s8] * 8 + [1] * p + [-1] * q)
            Om = prod([GA.gen(i) for i in range(8)], sq)
            ok = ok and GA.eq(GA.mul(Om, Om, sq), GA.sc(1))
            tw = [GA.mul(GA.gen(8 + i), Om, sq) for i in range(n)]
            ok = ok and anticommuting_with_squares(tw, sq) == [1] * p + [-1] * q
            ok = ok and all(GA.commutes(x, GA.gen(i), sq) for x in tw for i in range(8))
            hit = tensor_blades(tw, [GA.gen(i) for i in range(8)], sq)
            ok = ok and hit is not None and len(hit) == 2 ** (n + 8)
    GA.check("Cl(8,0) = Cl(0,8) = Mat_16(R) and Cl(p+8,q), Cl(p,q+8) = Mat_16(Cl(p,q))", ok)
    return ok


def check_eight_towers():
    premise("tower.rigidity-clock-frozen")
    premise("tower.commuting-copies")
    premise("dark-matter.imported-eight-towers-mod-8-clock")
    sigs = [(p, q) for p in range(15) for q in range(15) if p + q <= 14]
    parent = {s: s for s in sigs}

    def find(s):
        while parent[s] != s:
            s = parent[s]
        return s

    def join(a, b):
        if a in parent and b in parent:
            parent[find(a)] = find(b)

    for p, q in sigs:
        join((p, q), (p + 1, q + 1))
        join((p, q), (p + 8, q))
        join((p, q), (p, q + 8))
    classes = {}
    for s in sigs:
        get_or_set(classes, find(s), set()).add((s[0] - s[1]) % 8)
    ok = len(classes) == 8 and all(len(r) == 1 for r in classes.values())
    ok = ok and sorted(next(iter(r)) for r in classes.values()) == list(range(8))
    GA.check("ascent and period eight sort the signatures into eight towers, one per residue", ok)
    return ok
