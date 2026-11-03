"""dark-matter.two-families-are-two-chiralities: exact checks.

Split form in dimension 2m (m = 1..4): e_0..e_{m-1} square +1, e_m..e_{2m-1} square -1; null pairs
w_i = (e_i + e_{m+i})/2, v_i = (e_i - e_{m+i})/2 with v_i w_j + w_j v_i = delta_ij; W = span(w),
W' = span(v); f = w_1...w_m; S = Cl f = span{v_S f}; I = e_0 ... e_{2m-1} with I^2 = 1.
(i) The states of S killed by all of W form a line, spanned by f (Fock grade 0); those killed by all
of W' form a line, spanned by the top state v_1...v_m f (Fock grade m); both are I-eigenstates.
(ii) For odd versors (invertible vectors u) the pure spinor of Ad_u(W) is u f (killed by every
Ad_u(w_i), nonzero), with I-eigenvalue opposite to f's; for even versors u2 u1 it is u2 u1 f with
the same eigenvalue as f.
(iii) I^2 = 1, so the chirality takes only the values +-1, and both occur; the swap U_k (w_k replaced
by v_k) is Ad_u(W) for u = w_k - v_k, with pure spinor v_k f of opposite chirality; the Witt pair
W, W' has opposite chiralities iff m is odd.
Odd dimension 2m + 1 (extra generator l of square +1, m = 1..3): omega is central; Ad_l fixes every
w_i and v_i (an odd isometry stabilising W, so the special group already reaches every image of W);
on S = Cl f P, P = (1 + omega)/2, the spin-algebra element l v_1 anticommutes with the Fock parity
Gamma = e_0 ... e_{2m-1} and maps the grade-0 state f P to a nonzero multiple of the grade-1 state
v_1 f P: the spin algebra does not preserve the grade parity of S.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise


# the split dimensions 2m sampled by the versor check
M_RANGE = range(1, 5)


def sample_vectors(m):
    """Three sample vectors of the split form in dimension 2m: e_0, e_0 + 2 e_{2m-1}, 3 e_{m-1} + e_m."""
    n = 2 * m
    return [GA.gen(0), GA.add(GA.gen(0), GA.scal(2, GA.gen(n - 1))),
            GA.add(GA.scal(3, GA.gen(m - 1)), GA.gen(m))]


def fock(m, extra=0):
    sq = tuple([1] * m + [-1] * m + [1] * extra)
    w = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(m + i))) for i in range(m)]
    v = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(m + i))) for i in range(m)]
    f = GA.sc(1)
    for x in w:
        f = GA.mul(f, x, sq)
    I = GA.sc(1)
    for i in range(2 * m):
        I = GA.mul(I, GA.gen(i), sq)
    return sq, w, v, f, I


def prod(xs, sq):
    y = GA.sc(1)
    for x in xs:
        y = GA.mul(y, x, sq)
    return y


def fock_states(m, v, f, sq):
    """v_S f for S subsets of {0..m-1}, ordered by S; Fock grade |S|."""
    out = []
    for k in range(m + 1):
        for S in combinations(range(m), k):
            out.append((S, GA.mul(prod([v[i] for i in S], sq), f, sq)))
    return out


def coords(x, n):
    return [x.get(b, F(0)) for b in GA.all_blades(n)]


def eigen(I, psi, sq):
    for lam in (1, -1):
        if GA.eq(GA.mul(I, psi, sq), GA.scal(lam, psi)):
            return lam
    return None


def annihilated_line(ops, states, sq, n):
    """Kernel of c -> (op sum c_k s_k)_op on the span of the states."""
    rows = []
    for op in ops:
        imgs = [coords(GA.mul(op, s, sq), n) for s in states]
        for r in range(len(imgs[0])):
            rows.append([imgs[k][r] for k in range(len(states))])
    return GA.field_kernel(rows)


def check_pure_spinors_of_witt_pair():
    ok = True
    for m in range(1, 5):
        sq, w, v, f, I = fock(m)
        n = 2 * m
        ok = ok and all(GA.eq(GA.add(GA.mul(v[i], w[j], sq), GA.mul(w[j], v[i], sq)), GA.sc(1 if i == j else 0))
                        for i in range(m) for j in range(m))
        st = fock_states(m, v, f, sq)
        sts = [s for _, s in st]
        allS = [GA.mul({b: F(1)}, f, sq) for b in GA.all_blades(n)]
        ok = ok and GA.rank_of_vectors([coords(s, n) for s in sts]) == 2 ** m
        ok = ok and GA.rank_of_vectors([coords(s, n) for s in sts + allS]) == 2 ** m
        kW = annihilated_line(w, sts, sq, n)
        kWp = annihilated_line(v, sts, sq, n)
        ok = ok and len(kW) == 1 and len(kWp) == 1
        ok = ok and [j for j in range(2 ** m) if kW[0][j] != 0] == [0]
        ok = ok and [j for j in range(2 ** m) if kWp[0][j] != 0] == [2 ** m - 1]
        ok = ok and st[-1][0] == tuple(range(m)) and len(st[-1][0]) == m
        ok = ok and eigen(I, f, sq) is not None and eigen(I, st[-1][1], sq) is not None
    GA.check("in dimension 2m <= 8 the pure spinors of W and W' are f and the top state, unique up to scale", ok)
    return ok


def check_versor_parity_and_chirality():
    premise("primer.twisted-adjoint-action")
    ok = True
    for m in M_RANGE:
        sq, w, v, f, I = fock(m)
        lam = eigen(I, f, sq)
        ok = ok and lam in (1, -1)
        us = sample_vectors(m)
        # by hand: Q(e_0) = 1, Q(e_0 + 2 e_{2m-1}) = 1 - 4 = -3, Q(3 e_{m-1} + e_m) = 9 - 1 = 8: every
        # sample is invertible (this replaces a filter that dropped non-invertible samples silently)
        qs = (1, -3, 8)
        ok = ok and (len(us) == len(qs) and all(GA.eq(GA.mul(u, u, sq), GA.sc(q)) for u, q in zip(us, qs)))
        for u in us:
            Q = GA.mul(u, u, sq)[()]
            uinv = GA.scal(1 / Q, u)
            ok = ok and GA.eq(GA.mul(u, uinv, sq), GA.sc(1))
            psi = GA.mul(u, f, sq)
            U = [GA.neg(GA.mul(GA.mul(u, x, sq), uinv, sq)) for x in w]
            ok = ok and not GA.is_zero(psi) and all(GA.is_zero(GA.mul(x, psi, sq)) for x in U)
            ok = ok and eigen(I, psi, sq) == -lam
        for a in range(len(us)):
            for b in range(len(us)):
                if a != b:
                    g = GA.mul(us[a], us[b], sq)
                    psi = GA.mul(g, f, sq)
                    ok = ok and not GA.is_zero(psi) and eigen(I, psi, sq) == lam
    GA.check("odd versors reverse the chirality of the pure spinor, even versors preserve it", ok)
    return ok


def check_two_families_and_witt_pair_parity():
    premise("dark-matter.flag-insensitive-residue-no-flag-level")
    premise("primer.twisted-adjoint-action")
    ok = True
    opposite = {}
    for m in range(1, 5):
        sq, w, v, f, I = fock(m)
        n = 2 * m
        ok = ok and GA.eq(GA.mul(I, I, sq), GA.sc(1))
        lam = eigen(I, f, sq)
        top = GA.mul(prod(v, sq), f, sq)
        opposite[m] = eigen(I, top, sq) == -lam
        for k in range(m):
            u = GA.sub(w[k], v[k])
            Q = GA.mul(u, u, sq)[()]
            uinv = GA.scal(1 / Q, u)
            ad = [GA.neg(GA.mul(GA.mul(u, x, sq), uinv, sq)) for x in w]
            ok = ok and Q == -1 and GA.eq(ad[k], v[k])
            ok = ok and all(GA.eq(ad[j], w[j]) for j in range(m) if j != k)
            psi = GA.mul(v[k], f, sq)
            ok = ok and GA.eq(GA.mul(u, f, sq), GA.neg(psi))
            ok = ok and all(GA.is_zero(GA.mul(x, psi, sq)) for x in ad) and eigen(I, psi, sq) == -lam
    ok = ok and opposite == {1: True, 2: False, 3: True, 4: False}
    GA.check("two families (chirality +-1); the Witt pair W, W' is split between them iff m is odd", ok)
    return ok


def check_odd_dimension_one_family():
    premise("primer.twisted-adjoint-action")
    ok = True
    for m in range(1, 4):
        sq, w, v, f, Gam = fock(m, 1)
        n = 2 * m + 1
        ell = GA.gen(2 * m)
        om = GA.mul(Gam, ell, sq)
        ok = ok and all(GA.commutes(om, GA.gen(i), sq) for i in range(n))
        ok = ok and GA.eq(GA.mul(om, om, sq), GA.sc(1))
        # the reflection in l fixes W and W' pointwise
        ok = ok and all(GA.eq(GA.neg(GA.mul(GA.mul(ell, x, sq), ell, sq)), x) for x in w + v)
        P = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
        fP = GA.mul(f, P, sq)
        v1fP = GA.mul(v[0], fP, sq)
        B = GA.mul(ell, v[0], sq)
        ok = ok and GA.anticommutes(B, Gam, sq)
        img = GA.mul(B, fP, sq)
        lam = eigen(Gam, fP, sq)
        ok = ok and lam is not None and eigen(Gam, v1fP, sq) == -lam
        ok = ok and (GA.eq(img, v1fP) or GA.eq(img, GA.neg(v1fP))) and not GA.is_zero(img)
        # S = Cl f P has dimension 2^m
        Ss = [GA.mul({b: F(1)}, fP, sq) for b in GA.all_blades(n)]
        ok = ok and GA.rank_of_vectors([coords(s, n) for s in Ss]) == 2 ** m
    GA.check("odd dimension: omega central, l fixes W, and the spin algebra mixes the Fock parity of S", ok)
    return ok
