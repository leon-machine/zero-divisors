"""odd-extensions.four-extensions-oriented-pair: exact checks of the table.

GA.py basis-blade algebra on five generators, the shadow's four first (this world (1,3): squares
+1, -1, -1, -1; the mirror (3,1): -1, +1, +1, +1) and the added generator e_5 last, with square +1
(time, uniform convention) or -1 (space). For each of the four rows the check computes: the
signature (p, q) of the extension; omega^2 and the centrality of omega; for omega^2 = +1 the two
central idempotents and the Wedderburn type of each ideal (the doubled shadow); for
omega^2 = -1 the centre R + R omega (blade-wise, exhaustive), Cl = Cl^0 + omega Cl^0 and the
type Mat_4(C) (an idempotent with complex corner); the type of Cl^0 from its generators
e_mu e_5; the residue p - q mod 8. Types are read off idempotents whose corner is a division
algebra (R, C or H), so Cl(1,3) = Mat_2(H) and Cl(3,1) = Mat_4(R) are recomputed here. Also the
convention-free rule (square -1 doubles, +1 complexifies) and the causal-convention relabelling
of the mirror's extensions as reversals of ours of the same kind.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
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

N = 5
THIS = (1, -1, -1, -1)
MIRROR = (-1, 1, 1, 1)
ROWS = [("this", THIS, -1), ("this", THIS, 1), ("mirror", MIRROR, -1), ("mirror", MIRROR, 1)]


def signature(sq):
    return (sum(1 for s in sq if s > 0), sum(1 for s in sq if s < 0))


def centre_blades(sq):
    return [b for b in GA.all_blades(N) if is_central(blade_el(b), N, sq)]


def row_data(shadow, s5):
    sq = tuple(shadow) + (s5,)
    e = [GA.gen(i) for i in range(N)]
    om = volume(N, sq)
    om2 = scalar_of(GA.mul(om, om, sq))
    even_gens = [GA.mul(e[m], e[4], sq) for m in range(4)]
    return sq, e, om, om2, even_gens


def check_omega_squares_and_residues():
    premise("odd-extensions.volume-element-odd-dimension")
    premise("odd-extensions.imported-representatives-dimension-nearest-four-types")
    got = []
    for _, shadow, s5 in ROWS:
        sq, e, om, om2, _ = row_data(shadow, s5)
        p, q = signature(sq)
        got.append(((p, q), om2, is_central(om, N, sq), (p - q) % 8))
    want = [((1, 4), 1, True, 5), ((2, 3), -1, True, 7), ((3, 2), 1, True, 1), ((4, 1), -1, True, 3)]
    ok = got == want
    GA.check("the four extensions Cl(1,4), Cl(2,3), Cl(3,2), Cl(4,1): omega central, omega^2 = +1, -1, "
             "+1, -1, residues 5, 7, 1, 3", ok)
    return ok


def check_structures():
    premise("odd-extensions.doubling-or-complexification")
    premise("odd-extensions.imported-representatives-dimension-nearest-four-types")
    full = [blade_el(b) for b in GA.all_blades(N)]
    got = []
    for _, shadow, s5 in ROWS:
        sq, e, om, om2, even_gens = row_data(shadow, s5)
        shadow_type = simple_copy_type(e[:4], sq, N)
        even_type = simple_copy_type(even_gens, sq, N)
        if om2 == 1:
            kinds = []
            for sgn in (1, -1):
                pz = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(sgn, om)))
                ideal = [GA.mul(pz, x, sq) for x in full]
                kinds.append((span_rank(ideal, N), GA.eq(GA.mul(pz, pz, sq), pz), is_central(pz, N, sq)))
            # the ideal of each summand is the shadow's type: the even copy times pz is that ideal
            got.append(("doubled", shadow_type, even_type, kinds))
        else:
            ev = [x for x in full if all(len(b) % 2 == 0 for b in x)]
            spans = span_rank(ev + [GA.mul(om, x, sq) for x in ev], N)
            got.append(("complex", shadow_type, even_type, (centre_blades(sq), spans,
                                                            simple_copy_type(e, sq, N))))
    top = (0, 1, 2, 3, 4)
    want = [
        ("doubled", (2, "H"), (2, "H"), [(16, True, True), (16, True, True)]),
        ("complex", (2, "H"), (4, "R"), ([(), top], 32, (4, "C"))),
        ("doubled", (4, "R"), (4, "R"), [(16, True, True), (16, True, True)]),
        ("complex", (4, "R"), (2, "H"), ([(), top], 32, (4, "C"))),
    ]
    ok = got == want
    GA.check("structures: Cl(1,3)+Cl(1,3); Cl(1,3)xC = Mat_4(C) with Cl^0 = Cl(3,1); "
             "Cl(3,1)+Cl(3,1); Cl(3,1)xC = Mat_4(C) with Cl^0 = Cl(1,3)", ok)
    return ok


def check_even_parts_are_the_stated_shadows():
    premise("odd-extensions.doubling-or-complexification")
    got = []
    for _, shadow, s5 in ROWS:
        sq, e, om, om2, even_gens = row_data(shadow, s5)
        sqs = anticommuting_with_squares(even_gens, sq)
        got.append((tuple(sorted(sqs)), span_rank(words(even_gens, sq), N)))
    # Cl^0(1,4) = Cl(1,3), Cl^0(2,3) = Cl(3,1), Cl^0(3,2) = Cl(3,1), Cl^0(4,1) = Cl(1,3)
    want = [((-1, -1, -1, 1), 16), ((-1, 1, 1, 1), 16), ((-1, 1, 1, 1), 16), ((-1, -1, -1, 1), 16)]
    ok = got == want
    GA.check("even subalgebras generated by e_mu e_5 with the stated signatures", ok)
    return ok


def check_convention_free_rule():
    premise("odd-extensions.doubling-or-complexification")
    premise("odd-extensions.volume-element-odd-dimension")
    ok = True
    for _, shadow, s5 in ROWS:
        sq, e, om, om2, _ = row_data(shadow, s5)
        # a generator of square -1 doubles (omega^2 = +1), one of square +1 complexifies
        ok = ok and om2 == -s5
    # causal convention: the mirror's time is its minus sign, so its time and space extensions are
    # Cl(3,2) and Cl(4,1), the reversals of ours of the same kind
    ours = {"space": signature(THIS + (-1,)), "time": signature(THIS + (1,))}
    mirror_causal = {"space": signature(MIRROR + (1,)), "time": signature(MIRROR + (-1,))}
    ok = ok and mirror_causal == {"space": (4, 1), "time": (3, 2)}
    ok = ok and all(mirror_causal[k] == (ours[k][1], ours[k][0]) for k in ours)
    GA.check("square -1 doubles and +1 complexifies in all four; the causal relabelling is reversal", ok)
    return ok
