"""tower.answers-iteration-question: exact checks of the computable clauses.

Clause 1 (one forced ascent on the physical side, one rung per shadow wall beyond it) is a
statement about the geometry of a tame degeneration (Fact tower.wall-package) with no finite
algebraic core here, and is not checked. Clauses 2 and 3 are checked on the physical tower
Cl(1+k, 3+k) in GA.py (ground generators first, then plane j as e_j (+1), f_j (-1)):
(2) the clock never ticks: the charge (1+k) - (3+k) mod 8 is 6 at every floor; the centre of each
    floor k = 0, 1, 2 is R (blade-wise, exhaustive, valid for diagonal forms), so no floor has a
    central idempotent; and each floor is Mat_{2^(k+1)}(H), read off the idempotent
    f = (1 + e_0)/2 prod_j w_j v_j whose corner f T_k f is a quaternion algebra (a division corner,
    so f is primitive): the same division ring H at every floor, Morita-stationary;
(3) the fermionic ladder: the plane pairs give k CAR modes on floor k (k <= 3), one more per rung,
    and the Fock module of the modes doubles per rung (2^k states).
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


def centre_blades(sq):
    m = len(sq)
    return [b for b in GA.all_blades(m) if all(GA.commutes(blade_el(b), GA.gen(i), sq) for i in range(m))]


def check_clock_never_ticks():
    premise("tower.rigidity-clock-frozen")
    ok = True
    types = []
    for k in (0, 1, 2):
        sq = floor_sq(1, 3, k)
        m = len(sq)
        ok = ok and ((1 + k) - (3 + k)) % 8 == 6
        ok = ok and centre_blades(sq) == [()]
        us = [GA.gen(0)]
        f = idempotent_from(us, sq)
        for j in range(k):
            v, w = plane(4, j)
            f = GA.mul(f, GA.mul(w, v, sq), sq)
        ok = ok and GA.eq(GA.mul(f, f, sq), f)
        basis = [blade_el(b) for b in GA.all_blades(m)]
        types.append((corner_division_type(f, basis, sq, m), f.get((), F(0))))
    # division ring H at every floor; trace of f = 1/(2 * 2^k): rank one of Mat_{2^(k+1)}(H)
    ok = ok and types == [("H", F(1, 2)), ("H", F(1, 4)), ("H", F(1, 8))]
    GA.check("physical tower: charge 6, centre R, Mat_{2^(k+1)}(H) at k = 0, 1, 2", ok)
    return ok


def check_one_qubit_per_rung():
    premise("tower.car-limit-even-charge")
    ok = True
    counts = []
    for k in (1, 2, 3):
        sq = floor_sq(1, 3, k)
        pairs = [plane(4, j) for j in range(k)]
        good = 0
        for i, (vi, wi) in enumerate(pairs):
            row = all(GA.is_zero(GA.add(GA.mul(vi, vj, sq), GA.mul(vj, vi, sq)))
                      and GA.eq(GA.add(GA.mul(vi, wj, sq), GA.mul(wj, vi, sq)), GA.sc(1) if i == j else {})
                      for j, (vj, wj) in enumerate(pairs))
            good += 1 if row else 0
        counts.append(good)
        # the Fock module of the modes: the 2^k wedge monomials of the creation vectors are independent
        vs = [v for v, w in pairs]
        mons = words(vs, sq)
        ok = ok and span_rank(mons, 4 + 2 * k) == 2 ** k
    ok = ok and counts == [1, 2, 3]
    GA.check("one CAR mode per rung and a Fock space doubling per rung on the physical tower", ok)
    return ok
