"""tower.algebraic-limit-even-charge: exact checks of the finite core.

The direct limit itself is infinite; what is checked is every finite square that builds it, at
the stages k = 0, 1, 2. Floors T_k = Cl(p+k, q+k) in GA.py (ground generators first, then the
planes e_j (+1), f_j (-1)); A = Cl(p,q). The identification phi_k : T_k -> A (x) Mat_{2^k} is
inverted by the nested Peirce dictionary of Theorem tower.commuting-copies: a matrix with entries
a_{IJ} in A (indices I = (i_k, ..., i_1), i = 1 the occupied and 2 the empty state, so that
E_11 = v w, E_12 = v, E_21 = w, E_22 = w v, the k-th plane outermost) goes to
sum E^k_{i_k 1} ( ... sum alpha_k(a_{IJ}) E^1_{i_1 j_1} ... ) E^k_{1 j_k}, with alpha_k the twisted
embedding (odd ground elements times Omega_k). Checked:
(1) Lemma tower.compatibility-connecting-maps-transported at the stages used: the tower inclusion
    iota_k equals phi_{k+1}^{-1} o Ad(V_k) o theta_k o phi_k on a basis of A (x) Mat_{2^k},
    V_k = diag(u_A (x) 1, 1 (x) Omega_k-bar), for A = Cl(1,1), Cl(2,0) (k = 0, 1, 2) and Cl(1,3)
    (k = 0, 1); and the same corrector fails for the odd-charge ground Cl(1,0).
(2) The theorem's intertwiners: W_0 = 1, W_{k+1} = theta_k(W_k) V_k^{-1}; then
    Ad(W_{k+1}) phi_{k+1} iota_k = theta_k Ad(W_k) phi_k on a basis of T_k: the tower embeddings
    become the block doublings m -> diag(m, m) exactly, stage by stage, so the two direct systems
    are isomorphic (their limit is A (x) Mat_{2^infinity} by definition).
(3) The second description: iota_k is the inclusion of the Clifford algebra of
    R^{p,q} + H_1 + ... + H_k into that of the next space (generators to generators, squares kept),
    and dim T_k = dim A * 4^k.
"""
from fractions import Fraction as F
from itertools import combinations, product

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

EVEN_GROUNDS = [((1, 1), 2), ((2, 0), 2), ((1, 3), 1)]   # (signature, highest k checked)


def ground_basis(n):
    return [blade_el(b) for b in GA.all_blades(n)]


def alpha(a, Om, sq):
    out = {}
    for b, c in a.items():
        piece = {b: c} if len(b) % 2 == 0 else GA.mul({b: c}, Om, sq)
        out = GA.add(out, piece)
    return out


def units_of_plane(n, j, sq):
    v, w = plane(n, j)
    return {(1, 1): GA.mul(v, w, sq), (1, 2): v, (2, 1): w, (2, 2): GA.mul(w, v, sq)}


def phi_inv(M, n, k, sq):
    """M: {(I, J): ground element}, I, J tuples (i_k, ..., i_1); returns the element of T_k."""
    if k == 0:
        return M.get(((), ()), {})
    Om = big_omega(n, k, sq)
    Es = [units_of_plane(n, j, sq) for j in range(k)]

    def level(m, outer_I, outer_J):
        # the block of M with fixed outer indices, expanded over planes m-1, ..., 0
        if m == 0:
            return alpha(M.get((outer_I, outer_J), {}), Om, sq)
        out = {}
        if m == 1:
            for i1 in (1, 2):
                for j1 in (1, 2):
                    a = M.get((outer_I + (i1,), outer_J + (j1,)))
                    if a:
                        out = GA.add(out, GA.mul(alpha(a, Om, sq), Es[0][(i1, j1)], sq))
            return out
        E = Es[m - 1]
        for im in (1, 2):
            for jm in (1, 2):
                inner = level(m - 1, outer_I + (im,), outer_J + (jm,))
                if inner:
                    out = GA.add(out, GA.mul(GA.mul(E[(im, 1)], inner, sq), E[(1, jm)], sq))
        return out

    return level(k, (), ())


def idx(k):
    return list(product((1, 2), repeat=k))


def theta(M):
    out = {}
    for (I, J), a in M.items():
        for o in (1, 2):
            out[((o,) + I, (o,) + J)] = a
    return out


def diag_mul(D, M, sq, left=True):
    """D diagonal {I: element}; returns D M (left) or M D (right)."""
    out = {}
    for (I, J), a in M.items():
        x = GA.mul(D[I], a, sq) if left else GA.mul(a, D[J], sq)
        if not GA.is_zero(x):
            out[(I, J)] = x
    return out


def corrector(n, k, sq):
    """V_k = diag(u_A (x) 1, 1 (x) Omega_k-bar) and its inverse, as diagonals over (i_{k+1}, I)."""
    uA = prod([GA.gen(i) for i in range(n)], sq)
    u2 = scalar_of(GA.mul(uA, uA, sq))
    V, Vi = {}, {}
    for I in idx(k + 1):
        if I[0] == 1:
            V[I], Vi[I] = uA, GA.scal(1 / u2, uA)
        else:
            s = 1
            for i in I[1:]:
                s = -s if i == 1 else s
            V[I], Vi[I] = GA.sc(s), GA.sc(s)
    return V, Vi


def basis_matrices(n, k):
    out = []
    for a in ground_basis(n):
        for I in idx(k):
            for J in idx(k):
                out.append({(I, J): a})
    return out


def transported_ok(p, q, k):
    n = p + q
    sq = floor_sq(p, q, k + 1)
    V, Vi = corrector(n, k, sq)
    ok = True
    for M in basis_matrices(n, k):
        lhs = phi_inv(M, n, k, sq)
        rhs = phi_inv(diag_mul(Vi, diag_mul(V, theta(M), sq), sq, left=False), n, k + 1, sq)
        ok = ok and GA.eq(lhs, rhs)
    return ok


def check_transported_connecting_map_is_corrected_doubling():
    premise("tower.commuting-copies")
    premise("tower.compatibility-connecting-maps-transported")
    ok = True
    for (p, q), kmax in EVEN_GROUNDS:
        for k in range(kmax + 1):
            ok = ok and transported_ok(p, q, k)
    # control: odd charge, the ground volume is central and the corrector does not work
    ok = ok and not transported_ok(1, 0, 0) and not transported_ok(1, 0, 1)
    GA.check("iota_k = phi_{k+1}^{-1} Ad(V_k) theta_k phi_k for even charge (k <= 2); fails for Cl(1,0)", ok)
    return ok


def check_intertwiners_make_the_embeddings_block_doublings():
    premise("tower.commuting-copies")
    premise("tower.compatibility-connecting-maps-transported")
    ok = True
    for (p, q), kmax in EVEN_GROUNDS:
        n = p + q
        W = {(): GA.sc(1)}
        Wi = {(): GA.sc(1)}
        for k in range(kmax + 1):
            sq = floor_sq(p, q, k + 1)
            V, Vi = corrector(n, k, sq)
            W1 = {I: GA.mul(W[I[1:]], Vi[I], sq) for I in idx(k + 1)}       # theta(W_k) V_k^{-1}
            W1i = {I: GA.mul(V[I], Wi[I[1:]], sq) for I in idx(k + 1)}
            ok = ok and all(GA.eq(GA.mul(W1[I], W1i[I], sq), GA.sc(1)) for I in idx(k + 1))
            for M in basis_matrices(n, k):
                # t = Lambda_k^{-1}(M) = phi_k^{-1}(W_k^{-1} M W_k); want Lambda_{k+1}(t) = theta(M)
                t = phi_inv(diag_mul(Wi, diag_mul(W, M, sq, left=False), sq), n, k, sq)
                s = phi_inv(diag_mul(W1i, diag_mul(W1, theta(M), sq, left=False), sq), n, k + 1, sq)
                ok = ok and GA.eq(s, t) and not GA.is_zero(t)
            W, Wi = W1, W1i
    GA.check("with W_{k+1} = theta(W_k) V_k^{-1} the tower embeddings are the block doublings, k <= 2", ok)
    return ok


def check_limit_is_clifford_algebra_of_the_union():
    premise("tower.commuting-copies")
    ok = True
    for (p, q), kmax in EVEN_GROUNDS:
        n = p + q
        for k in range(kmax + 1):
            sq_k, sq_k1 = floor_sq(p, q, k), floor_sq(p, q, k + 1)
            ok = ok and sq_k1[:len(sq_k)] == sq_k and sq_k1[len(sq_k):] == (1, -1)
            # products of the generators of T_k are the same in T_{k+1}: iota_k is the inclusion
            gens = [GA.gen(i) for i in range(n + 2 * k)]
            ok = ok and all(GA.eq(GA.mul(a, b, sq_k), GA.mul(a, b, sq_k1)) for a in gens for b in gens)
            ok = ok and len(GA.all_blades(n + 2 * k)) == len(ground_basis(n)) * 4 ** k
    GA.check("iota_k is the inclusion of Clifford algebras of the nested quadratic spaces", ok)
    return ok
