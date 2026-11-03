"""odd-extensions.two-readings-which-which: exact checks of the computable part.

In R^{2,4} (GA.py, squares (+,+,-,-,-,-)) with the frozen point I = c e_+ + d e_-,
c^2 - d^2 = Lambda/3 > 0, and the Stelle-West vector V = (3/Lambda)(d e_+ + c e_-), as in
Proposition odd-extensions.belongs-tower. Checked: (a) one algebra, two solderings: Cl(I^perp) has
signature (1,4) (the five-dimensional shadow's algebra) and is soldered along the Lorentz frame
{I,V}^perp, signature (1,3), so the series' residue (the soldered signature) is 6, while the
soldering along all five directions gives residue 5; (b) V lies on the de Sitter hyperboloid
{X in I^perp : Q(X) = -3/Lambda} and is its normal: the tangent space there, the kernel of
<V, .> inside I^perp, is the Lorentz frame, so V is not a tangent (spacetime) direction; (c) its
norm is fixed, Lambda Q(V) = -3 on every sample, i.e. Q(V) = -l^2 with l^2 = 3/Lambda (l itself
is irrational in general; the identity is checked on its square). The size L of a fifth tangent
direction of a populated five-dimensional tower is a datum the series does not fix and has no
computable content here.
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

SAMPLES = [(1, 1), (2, F(1, 2)), (5, F(2, 3)), (F(1, 3), F(1, 7)), (4, 9)]


def tangent_space_at(V, I):
    """Vectors of I^perp orthogonal to V: the tangent space of the hyperboloid Q = Q(V) at V."""
    return perp_basis([I, V])


def check_one_algebra_two_solderings():
    premise("odd-extensions.belongs-tower")
    ok = True
    for t, s in SAMPLES:
        I, lam = frozen(t, s)
        V = stelle_west(t, s)
        whole = perp_basis([I])
        sold = perp_basis([I, V])
        a, b = gram_signature(whole), gram_signature(sold)
        ok = ok and lam > 0 and a == (1, 4, 0) and b == (1, 3, 0)
        ok = ok and (b[0] - b[1]) % 8 == 6 and (a[0] - a[1]) % 8 == 5
    GA.check("Cl(I^perp) = Cl(1,4) soldered along (1,3): residue 6, not the residue 5 of the full soldering", ok)
    return ok


def check_stelle_west_vector_is_the_normal_of_fixed_norm():
    premise("odd-extensions.belongs-tower")
    ok = True
    frame = [GA.gen(i) for i in FRAME]
    for t, s in SAMPLES:
        I, lam = frozen(t, s)
        V = stelle_west(t, s)
        ok = ok and lam * GA.dot(V, V, SQ6) == -3
        ok = ok and GA.dot(I, V, SQ6) == 0
        T = tangent_space_at(V, I)
        ok = ok and len(T) == 4 and span_rank(T + frame, 6) == 4
        ok = ok and span_rank(T + [V], 6) == 5
        # a curve X(u) = V + u x - (u^2 Q(x)/(2 Q(V))) V + O(u^3) on the hyperboloid has velocity x in T
        for x in frame:
            ok = ok and GA.dot(V, x, SQ6) == 0
    GA.check("V is the normal of the de Sitter hyperboloid, with Lambda Q(V) = -3 (l^2 = 3/Lambda)", ok)
    return ok
