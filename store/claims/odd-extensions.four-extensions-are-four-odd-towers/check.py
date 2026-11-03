"""odd-extensions.four-extensions-are-four-odd-towers: exact checks.

(1) Residues and roles: the four extensions (1,4), (2,3), (3,2), (4,1) have residues 5, 7, 1, 3;
    (1,4) and (4,1) are the representatives of Fact
    odd-extensions.imported-representatives-dimension-nearest-four-types at r = 5 and r = 3; (2,3)
    and (3,2) are the conformal ambients (t+1, s+1) of (1,2) and (2,1), residues 7 and 1.
(2) The conformal step is one rung of the tower: in Cl(2,3) and Cl(3,2) (GA.py, the shadow's
    generators first, then e (+1), f (-1)), the twisted generators x e f satisfy the relations of
    Cl(1,2), resp. Cl(2,1), commute with e and f, the plane has the matrix units v w, v, w, w v,
    and the products of the two sets of words are the 32 distinct blades: Cl(t+1, s+1) =
    Mat_2(Cl(t,s)), residue unchanged.
(3) The frozen point's algebra: in R^{2,4} with I = c e_+ + d e_-, c^2 - d^2 = Lambda/3, the
    complement I^perp (exact kernel) has signature (1,4) for Lambda > 0 (the five-dimensional
    shadow's quadratic space) and (2,3) for Lambda < 0 (the three-dimensional ambient's), while
    its soldered part, the Lorentz frame, has signature (1,3), residue 6, in both: equal as
    algebras, not as soldered objects (Proposition odd-extensions.belongs-tower).
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
# ---------------------------------------------------------------------------
# The tractor space R^{2,4} in GA.py: index 0 the Lorentz time (+1), 1 = e_+ (+1),
# 2, 3, 4 the Lorentz space (-1), 5 = e_- (-1). The Lorentz frame is 0, 2, 3, 4.
# The frozen point I = c e_+ + d e_- with c^2 - d^2 = Lambda/3, written c = (t+s)/2,
# d = (t-s)/2 so that Lambda = 3 t s; the Stelle-West vector V = (3/Lambda)(d e_+ + c e_-).
# ---------------------------------------------------------------------------
SQ6 = (1, 1, -1, -1, -1, -1)
FRAME = (0, 2, 3, 4)
EP, EM = 1, 5


def vec6(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c}


def frozen(t, s):
    t, s = F(t), F(s)
    c, d = (t + s) / 2, (t - s) / 2
    return GA.add(GA.scal(c, GA.gen(EP)), GA.scal(d, GA.gen(EM))), 3 * t * s


def stelle_west(t, s):
    t, s = F(t), F(s)
    c, d = (t + s) / 2, (t - s) / 2
    lam = 3 * t * s
    return GA.scal(3 / lam, GA.add(GA.scal(d, GA.gen(EP)), GA.scal(c, GA.gen(EM))))


def vcoords(x):
    return [x.get((i,), F(0)) for i in range(6)]


def perp_basis(vs):
    """A basis of the orthogonal complement in R^{2,4} of the vectors vs (exact kernel)."""
    rows = [[F(SQ6[i]) * vcoords(v)[i] for i in range(6)] for v in vs]
    return [vec6(k) for k in GA.field_kernel(rows)]


def gram_signature(vs):
    return GA.congruence_signature([[GA.dot(a, b, SQ6) for b in vs] for a in vs])

FOUR = [(1, 4), (2, 3), (3, 2), (4, 1)]
THREE_DIM = [(1, 2), (2, 1)]
SAMPLES = [(1, 1), (5, F(2, 3)), (1, F(-1, 5)), (F(3, 2), -4)]


def residue(s):
    return (s[0] - s[1]) % 8


def check_residues_and_roles():
    premise("odd-extensions.four-extensions-oriented-pair")
    premise("odd-extensions.imported-representatives-dimension-nearest-four-types")
    premise("odd-extensions.imported-conformal-completion")
    ok = [residue(s) for s in FOUR] == [5, 7, 1, 3]
    # the representatives table of the Fact at the dimension nearest four
    table = {6: [(1, 3)], 2: [(3, 1)], 0: [(2, 2)], 4: [(0, 4), (4, 0)], 1: [(2, 1)], 7: [(1, 2)],
             3: [(4, 1)], 5: [(1, 4)]}
    ok = ok and all(residue(s) == r for r, ss in table.items() for s in ss)
    ok = ok and FOUR[0] in table[residue(FOUR[0])] and FOUR[3] in table[residue(FOUR[3])]
    amb = [(t + 1, s + 1) for t, s in THREE_DIM]
    ok = ok and amb == [(2, 3), (3, 2)]
    ok = ok and [residue(s) for s in THREE_DIM] == [7, 1] == [residue(s) for s in amb]
    ok = ok and [sum(s) for s in THREE_DIM] == [3, 3] and [sum(s) for s in (FOUR[0], FOUR[3])] == [5, 5]
    GA.check("residues 5, 7, 1, 3: (1,4), (4,1) represent r = 5, 3; (2,3), (3,2) are ambients of (1,2), (2,1)", ok)
    return ok


def check_conformal_step_is_one_rung():
    premise("odd-extensions.imported-towers-clock")
    premise("odd-extensions.imported-conformal-completion")
    ok = True
    for t, s in THREE_DIM:
        n = t + s
        sq = floor_sq(t, s, 1)
        tw = twisted_ground(n, 1, sq)
        ok = ok and anticommuting_with_squares(tw, sq) == [1] * t + [-1] * s
        ok = ok and all(GA.commutes(x, GA.gen(n + i), sq) for x in tw for i in range(2))
        subsets, E = matrix_units(n, 1, sq)
        ok = ok and matrix_units_ok(subsets, E, sq)
        hit = tensor_blades(tw, [GA.gen(n), GA.gen(n + 1)], sq)
        ok = ok and hit is not None and len(hit) == 32
        ok = ok and (sum(1 for x in sq if x > 0), sum(1 for x in sq if x < 0)) == (t + 1, s + 1)
    GA.check("Cl(2,3) = Mat_2(Cl(1,2)) and Cl(3,2) = Mat_2(Cl(2,1)) by the commuting copies", ok)
    return ok


def check_frozen_point_algebra_coincides_as_algebra_only():
    premise("odd-extensions.translation-bivectors-frozen-point")
    premise("odd-extensions.belongs-tower")
    seen = set()
    ok = True
    frame = [GA.gen(i) for i in FRAME]
    for t, s in SAMPLES:
        I, lam = frozen(t, s)
        a = gram_signature(perp_basis([I]))
        b = gram_signature(frame)
        ok = ok and all(GA.dot(I, x, SQ6) == 0 for x in frame)
        seen.add((lam > 0, a[:2], residue(a[:2]), residue(b[:2])))
    ok = ok and seen == {(True, (1, 4), 5, 6), (False, (2, 3), 7, 6)}
    GA.check("Cl(I^perp) has the quadratic space (1,4) for Lambda > 0 and (2,3) for Lambda < 0; soldered "
             "residue 6", ok)
    return ok
