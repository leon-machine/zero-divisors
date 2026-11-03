"""standard-model.imported-tower-commuting-copies-fock-module: exact checks.

Floors T_k = Cl(p+k, q+k) in GA.py (ground generators first, then plane j as e_j (+1), f_j (-1);
v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2). The Fock module Lambda span(v_1..v_k) is the occupation
basis with v_j by wedge and w_j by contraction (Jordan-Wigner signs). Checked, on the instances
listed:
(1) the CAR as vector identities in T_k, k = 1, 2, 3, over the grounds (1,3), (0,0), (2,1);
(2) the commuting copies, k = 1, 2, over (1,3), (1,1), (0,2): the twisted ground generators
    x omega_1 ... omega_k satisfy the ground relations and commute with the 2k plane generators,
    whose words span 4^k dimensions, and A-words times B-words are 2^(n+2k) distinct blades, so
    multiplication A_k (x) B_k -> T_k is an isomorphism;
(3) the Chevalley (Fock) action, k = 1, 2, 3: the plane generators act with the relations of
    Cl(k,k) and their 4^k words act as a basis of End(Lambda W_k), so the module is irreducible and
    B_k = Mat_{2^k}(R); the vacuum is annihilated by every w_j and cyclic for the v_j; each rung
    adds one qubit, the first k planes acting by one block on both halves of Lambda W_{k+1};
(4) the *-structure on the real form of T_1 over (1,1), (0,2) and T_2 over (0,0): the
    antiautomorphism with x* = x (x^2 = 1), x* = -x (x^2 = -1) is antimultiplicative on all blade
    pairs and involutive, makes every blade unitary, and gives v_j* = w_j. Conjugate-linearity is
    the extension to complex coefficients and is not separately computed.
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
# ---------------------------------------------------------------------------
# The Fock module Lambda W_k in the occupation basis: states are bitmasks 0 .. 2^k - 1, bit j set
# when v_j is present; the wedge monomial basis v_{j1} ^ ... ^ v_{jr} (j1 < ... < jr) is
# orthonormal. v_j acts by wedge (sign (-1)^(occupied modes below j)), w_j by contraction.
# Operators are sparse matrices {(row, col): Fraction}.
# ---------------------------------------------------------------------------


def k_wedge(j, k):
    return {(s | 1 << j, s): F((-1) ** bin(s & ((1 << j) - 1)).count("1"))
            for s in range(2 ** k) if not s >> j & 1}


def k_contract(j, k):
    return {(s & ~(1 << j), s): F((-1) ** bin(s & ((1 << j) - 1)).count("1"))
            for s in range(2 ** k) if s >> j & 1}


def smm(*Ms):
    out = Ms[0]
    for B in Ms[1:]:
        rows = {}
        for (r, c), x in B.items():
            get_or_set(rows, r, []).append((c, x))
        acc = {}
        for (r, t), x in out.items():
            for c, y in rows.get(t, ()):
                acc[(r, c)] = acc.get((r, c), 0) + x * y
        out = {key: v for key, v in acc.items() if v}
    return out


def sadd(*Ms):
    acc = {}
    for M in Ms:
        for key, x in M.items():
            acc[key] = acc.get(key, 0) + x
    return {key: v for key, v in acc.items() if v}


def ssc(c, A):
    return {key: c * x for key, x in A.items() if c * x}


def str_(A):
    return {(c, r): x for (r, c), x in A.items()}


def sident(d):
    return {(s, s): F(1) for s in range(d)}


def plane_images(k):
    """rho(e_j) = wedge + contraction, rho(f_j) = wedge - contraction, in GA generator order."""
    out = []
    for j in range(k):
        a, b = k_wedge(j, k), k_contract(j, k)
        out += [sadd(a, b), sadd(a, ssc(-1, b))]
    return out


def flat(M, d):
    return [M.get((r, c), F(0)) for r in range(d) for c in range(d)]

CAR_GROUNDS = [(1, 3), (0, 0), (2, 1)]
COPY_GROUNDS = [(1, 3), (1, 1), (0, 2)]
STAR_FLOORS = [(1, 1, 1), (0, 2, 1), (0, 0, 2)]


def car_ok(vs, ws, sq):
    ok = True
    for i in range(len(vs)):
        for j in range(len(vs)):
            ok = ok and GA.is_zero(GA.add(GA.mul(vs[i], vs[j], sq), GA.mul(vs[j], vs[i], sq)))
            ok = ok and GA.is_zero(GA.add(GA.mul(ws[i], ws[j], sq), GA.mul(ws[j], ws[i], sq)))
            ac = GA.add(GA.mul(vs[i], ws[j], sq), GA.mul(ws[j], vs[i], sq))
            ok = ok and GA.eq(ac, GA.sc(1) if i == j else {})
    return ok


CAR_RUNGS = (1, 2, 3)


def _acomm(x, y, sq):
    return GA.add(GA.mul(x, y, sq), GA.mul(y, x, sq))


def check_ladder_pairs_satisfy_car():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    ok = True
    for p, q in CAR_GROUNDS:
        for k in CAR_RUNGS:
            sq = floor_sq(p, q, k)
            n = p + q
            # T_k = Cl(p+k, q+k): p + k generators of square +1 and q + k of square -1
            ok = ok and sq.count(1) == p + k and sq.count(-1) == q + k
            vs, ws = zip(*[plane(n, j) for j in range(k)])
            for i in range(k):
                for j in range(k):
                    ok = ok and GA.is_zero(_acomm(vs[i], vs[j], sq)) and GA.is_zero(_acomm(ws[i], ws[j], sq))
                    ok = ok and GA.eq(_acomm(vs[i], ws[j], sq), GA.sc(F(1)) if i == j else {})
                # By hand, with e^2 = 1, f^2 = -1: v w = (e^2 - e f + f e - f^2)/4 = (1 - e f)/2 and
                # w v = (1 + e f)/2, two complementary idempotents.
                ef = GA.mul(GA.gen(n + 2 * i), GA.gen(n + 2 * i + 1), sq)
                ok = ok and GA.eq(GA.mul(vs[i], ws[i], sq), GA.scal(F(1, 2), GA.sub(GA.sc(F(1)), ef)))
                ok = ok and GA.eq(GA.mul(ws[i], vs[i], sq), GA.scal(F(1, 2), GA.add(GA.sc(F(1)), ef)))
    GA.check("v_i v_j + v_j v_i = 0, w_i w_j + w_j w_i = 0, v_i w_j + w_j v_i = delta_ij, k <= 3", ok)
    return ok


def check_commuting_copies():
    premise("tower.commuting-copies")
    ok = True
    for p, q in COPY_GROUNDS:
        n = p + q
        for k in (1, 2):
            sq = floor_sq(p, q, k)
            tw = twisted_ground(n, k, sq)
            pg = [GA.gen(n + i) for i in range(2 * k)]
            ok = ok and anticommuting_with_squares(tw, sq) == [1] * p + [-1] * q
            ok = ok and anticommuting_with_squares(pg, sq) == [1, -1] * k
            ok = ok and all(GA.commutes(x, y, sq) for x in tw for y in pg)
            ok = ok and span_rank(words(pg, sq), n + 2 * k) == 4 ** k
            hit = tensor_blades(tw, pg, sq)
            ok = ok and hit is not None and len(hit) == 2 ** (n + 2 * k)
    GA.check("A_k = Cl(p,q) twisted and B_k = Cl(k,k) commute and multiply onto T_k, k = 1, 2", ok)
    return ok


def check_fock_module_one_qubit_per_rung():
    premise("tower.fock-module-one-qubit-per-rung")
    ok = True
    for k in (1, 2, 3):
        d = 2 ** k
        rho = plane_images(k)
        sqs = [1, -1] * k
        one = sident(d)
        for a in range(2 * k):
            ok = ok and smm(rho[a], rho[a]) == ssc(sqs[a], one)
            for b in range(a + 1, 2 * k):
                ok = ok and not sadd(smm(rho[a], rho[b]), smm(rho[b], rho[a]))
        imgs = []
        for r in range(2 * k + 1):
            for B in combinations(range(2 * k), r):
                imgs.append(flat(smm(*([one] + [rho[i] for i in B])), d))
        ok = ok and len(imgs) == 4 ** k and GA.rank_of_vectors(imgs) == d * d
        # vacuum: killed by every w_j, cyclic for the v_j
        vac = {(0, 0): F(1)}
        ok = ok and all(not smm(k_contract(j, k), vac) for j in range(k))
        states = set()
        for r in range(k + 1):
            for S in combinations(range(k), r):
                x = vac
                for j in reversed(S):
                    x = smm(k_wedge(j, k), x)
                states |= {row for (row, _c) in x}
        ok = ok and states == set(range(d))
        # one qubit per rung: on Lambda W_{k+1} the first k planes act by the same block on both halves
        big = plane_images(k + 1)
        for a in range(2 * k):
            blk0 = {(r, c): x for (r, c), x in big[a].items() if r < d and c < d}
            blk1 = {(r - d, c - d): x for (r, c), x in big[a].items() if r >= d and c >= d}
            cross = [key for key in big[a] if (key[0] < d) != (key[1] < d)]
            ok = ok and blk0 == rho[a] and blk1 == rho[a] and not cross
    GA.check("Lambda W_k irreducible for B_k = Mat_{2^k}(R), vacuum cyclic, one qubit per rung, k <= 3", ok)
    return ok


def star_blade(b, sq):
    """The antiautomorphism with x* = x for x^2 = 1, x* = -x for x^2 = -1, on a blade: the
    reversed product of the starred generators."""
    out = GA.sc(1)
    for i in reversed(b):
        out = GA.mul(out, GA.scal(sq[i], GA.gen(i)), sq)
    return out


def star(x, sq):
    return GA.add(*[GA.scal(c, star_blade(b, sq)) for b, c in x.items()]) if x else {}


def check_star_structure():
    premise("tower.structure-tower-c-norms")
    ok = True
    for p, q, k in STAR_FLOORS:
        n = p + q
        m = n + 2 * k
        sq = floor_sq(p, q, k)
        blades = [blade_el(b) for b in GA.all_blades(m)]
        for b in GA.all_blades(m):
            r = len(b)
            nneg = sum(1 for i in b if sq[i] < 0)
            ok = ok and GA.eq(star_blade(b, sq), blade_el(b, (-1) ** (r * (r - 1) // 2 + nneg)))
        for x in blades:
            ok = ok and GA.eq(star(star(x, sq), sq), x)
            ok = ok and GA.eq(GA.mul(star(x, sq), x, sq), GA.sc(1))
            for y in blades:
                ok = ok and GA.eq(star(GA.mul(x, y, sq), sq), GA.mul(star(y, sq), star(x, sq), sq))
        for j in range(k):
            v, w = plane(n, j)
            ok = ok and GA.eq(star(v, sq), w) and GA.eq(star(w, sq), v)
    GA.check("the explicit *-antiautomorphism (real form, three floors) is antimultiplicative, "
             "involutive, unitary on blades and gives v_j* = w_j", ok)
    return ok
