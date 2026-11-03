"""odd-extensions.belongs-tower: exact checks.

Setting of Facts odd-extensions.imported-frozen-point and Theorem odd-extensions.are-ascents-pair-signed
in R^{2,4} (GA.py, squares (+,+,-,-,-,-)): the frozen point I = c e_+ + d e_- with
c^2 - d^2 = Lambda/3 and the Stelle-West vector V = (3/Lambda)(d e_+ + c e_-), sampled at
Lambda > 0 and Lambda < 0. Checked: Q(V) = -3/Lambda, <I,V> = 0; the soldered space {I,V}^perp
(exact kernel) is the Lorentz frame, of signature (1,3) for every Lambda (also at Lambda = 0, where
it is the frame inside the degenerate I^perp), so the residue (Fact
odd-extensions.imported-copy-theorem-soldered-residue: the signature of the soldered space) is 6,
while the abstract algebra Cl(I^perp) has residue 5 or 7; V is orthogonal to the soldered space
and not in it; Cl(I^perp) contains the soldered algebra and lies in the rung Cl(2,4), which
e_I completes (dimension 64). (iii) at Lambda/3 a rational square: the frame plus e_V = V/|V| is an
orthonormal basis of I^perp of Gram diag(1,-1,-1,-1,-1), the isometry onto R^{1,4} sends e_V to
the fifth basis vector and the soldered space onto a four-dimensional subspace of signature
(1,3), not onto a soldered space of signature (1,4). The "no map of soldered data" step is the
proof's definitional argument; what is computed is the mismatch of the soldered signatures.
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

SAMPLES = [(1, 1), (2, F(1, 2)), (5, F(2, 3)), (1, F(-1, 5)), (F(3, 2), -4), (7, F(-1, 7))]
# Lambda = 3 t s with 3 / Lambda a rational square, so |V| is rational
UNIT_SAMPLES = [((1, 1), 1), ((2, 2), F(1, 2)), ((1, F(1, 4)), 2)]


def check_soldered_space_is_the_lorentz_frame():
    premise("odd-extensions.imported-frozen-point")
    premise("odd-extensions.are-ascents-pair-signed")
    ok = True
    frame = [GA.gen(i) for i in FRAME]
    for t, s in SAMPLES:
        I, lam = frozen(t, s)
        V = stelle_west(t, s)
        ok = ok and GA.dot(V, V, SQ6) == -3 / lam and GA.dot(I, V, SQ6) == 0
        ok = ok and GA.dot(I, I, SQ6) * GA.dot(V, V, SQ6) < 0
        sold = perp_basis([I, V])
        ok = ok and len(sold) == 4 and span_rank(sold + frame, 6) == 4
        ok = ok and gram_signature(sold) == (1, 3, 0)
        ok = ok and all(GA.dot(V, x, SQ6) == 0 for x in sold) and span_rank(sold + [V], 6) == 5
        ok = ok and all(GA.anticommutes(V, x, SQ6) for x in frame)
    # Lambda = 0: the frame still has signature (1,3), inside the degenerate I^perp
    I0, lam0 = frozen(2, 0)
    ok = ok and lam0 == 0 and gram_signature(frame) == (1, 3, 0)
    ok = ok and all(GA.dot(I0, x, SQ6) == 0 for x in frame) and gram_signature(perp_basis([I0])) == (1, 3, 1)
    GA.check("the soldered space {I,V}^perp is the Lorentz frame, signature (1,3) for every Lambda", ok)
    return ok


def check_tower_charge_six_not_five_or_seven():
    premise("odd-extensions.imported-copy-theorem-soldered-residue")
    premise("odd-extensions.are-ascents-pair-signed")
    ok = True
    seen = set()
    for t, s in SAMPLES:
        I, lam = frozen(t, s)
        V = stelle_west(t, s)
        sp, sm, sz = gram_signature(perp_basis([I, V]))
        ap, am, az = gram_signature(perp_basis([I]))
        seen.add(((sp - sm) % 8, (ap - am) % 8))
        # Cl(I^perp) = algebra of the frame and V: contains the frame algebra, inside Cl(2,4)
        gens = [GA.gen(i) for i in FRAME] + [V]
        alg = words(gens, SQ6)
        ok = ok and span_rank(alg, 6) == 32
        ok = ok and span_rank(alg + words([GA.gen(i) for i in FRAME], SQ6), 6) == 32
        ok = ok and span_rank(words(gens + [I], SQ6), 6) == 64
    ok = ok and seen == {(6, 5), (6, 7)}
    GA.check("soldered residue 6 on every sample; the abstract algebra's residue is 5 (Lambda > 0) or 7", ok)
    return ok


def check_isometry_carries_e_v_to_a_tangent_direction():
    premise("odd-extensions.imported-frozen-point")
    premise("odd-extensions.imported-copy-theorem-soldered-residue")
    ok = True
    for (t, s), norm in UNIT_SAMPLES:
        I, lam = frozen(t, s)
        V = stelle_west(t, s)
        ok = ok and lam > 0 and -GA.dot(V, V, SQ6) == norm * norm
        eV = GA.scal(1 / F(norm), V)
        basis = [GA.gen(i) for i in FRAME] + [eV]
        gram = [[GA.dot(a, b, SQ6) for b in basis] for a in basis]
        want = [[F(1) if (i == j == 0) else (F(-1) if i == j else F(0)) for j in range(5)] for i in range(5)]
        ok = ok and gram == want
        # the coordinates in this orthonormal basis are the isometry onto R^{1,4}: e_V is the fifth
        # basis vector, a tangent direction of the five-dimensional shadow
        ok = ok and span_rank(basis, 6) == 5 and span_rank(perp_basis([I]) + basis, 6) == 5
        # the soldered space goes to the span of the first four: dimension 4 of 5, signature (1,3),
        # while a residue-5 shadow is soldered along all of R^{1,4}, signature (1,4)
        s4, s5 = gram_signature(basis[:4]), gram_signature(basis)
        ok = ok and s4 == (1, 3, 0) and s5 == (1, 4, 0)
        ok = ok and (s4[0] - s4[1]) % 8 == 6 and (s5[0] - s5[1]) % 8 == 5
    GA.check("I^perp = R^{1,4} by an isometry taking e_V to a fifth tangent direction; soldered (1,3) vs (1,4)", ok)
    return ok
