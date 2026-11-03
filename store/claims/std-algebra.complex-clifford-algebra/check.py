from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise

I_ = GA.QI(0, 1)
ONE = GA.QI(1)
ZERO = GA.QI(0)


def _q(a):
    return a if isinstance(a, GA.QI) else GA.QI(F(a))


def _qscal(c, x):
    c = _q(c)
    return {b: c * v for b, v in x.items() if c * v != 0}


def _qvec(cs):
    return {(i,): _q(c) for i, c in enumerate(cs) if _q(c) != 0}


def _qcoords(x, n):
    return [_q(x.get(b, 0)) for b in GA.all_blades(n)]


def _qrank(xs, n):
    return GA.field_rank([_qcoords(x, n) for x in xs]) if xs else 0


# ---- the Fock operators on Lambda W over Q(i) ------------------------------

def _subsets(k):
    return [frozenset(c) for m in range(k + 1) for c in combinations(range(k), m)]


def _wedge(j, k):
    """Matrix of w_j ^ on Lambda W (basis: subsets in _subsets order)."""
    basis = _subsets(k)
    pos = {s: i for i, s in enumerate(basis)}
    M = [[ZERO] * len(basis) for _ in basis]
    for s in basis:
        if j not in s:
            sign = -1 if sum(1 for t in s if t < j) % 2 else 1
            M[pos[s | {j}]][pos[s]] = _q(sign)
    return M


def _contract(j, k):
    """Matrix of the contraction iota_j (iota_j w_l = delta_jl) on Lambda W."""
    basis = _subsets(k)
    pos = {s: i for i, s in enumerate(basis)}
    M = [[ZERO] * len(basis) for _ in basis]
    for s in basis:
        if j in s:
            sign = -1 if sum(1 for t in s if t < j) % 2 else 1
            M[pos[s - {j}]][pos[s]] = _q(sign)
    return M


def _fock_orthonormal(k):
    """c(e_{2j}) = w_j + v_j, c(e_{2j+1}) = -i (w_j - v_j) for w_j = (e_{2j} + i e_{2j+1})/2,
    v_j = (e_{2j} - i e_{2j+1})/2; with c(w_j) = w_j ^, c(v_j) = iota_j."""
    ms = []
    for j in range(k):
        W, V = _wedge(j, k), _contract(j, k)
        ms.append(S.mat_add(W, V))
        ms.append(S.mat_scal(GA.QI(0, -1), S.mat_add(W, S.mat_scal(-1, V))))
    return ms


def _products(ms):
    d = len(ms[0])
    out = []
    for m in range(len(ms) + 1):
        for idx in combinations(range(len(ms)), m):
            P = S.mat_id(d)
            for i in idx:
                P = S.mat_mul(P, ms[i])
            out.append(P)
    return out


def _flat(M):
    return [a for row in M for a in row]


def _gs_orthogonalise(G):
    """Exact symmetric Gram-Schmidt over Q(i) for a nondegenerate complex symmetric Gram matrix:
    returns (P, D) with the rows of P a basis and P G P^T = diag(D), D_i != 0."""
    n = len(G)
    vecs = [[_q(int(i == j)) for j in range(n)] for i in range(n)]

    def bil(x, y):
        return sum((x[i] * _q(G[i][j]) * y[j] for i in range(n) for j in range(n)), ZERO)

    out = []
    pool = vecs[:]
    while pool:
        pick = next((v for v in pool if bil(v, v)), None)
        if pick is None:
            # all remaining vectors null: some pair has nonzero pairing; use their sum
            a, b = next((a, b) for a in pool for b in pool if a is not b and bil(a, b))
            pick = [x + y for x, y in zip(a, b)]
            pool.remove(a)
        else:
            pool.remove(pick)
        qp = bil(pick, pick)
        out.append(pick)
        pool = [[x - bil(v, pick) / qp * y for x, y in zip(v, pick)] for v in pool]
        pool = [v for v in pool if any(v)]
    D = [bil(v, v) for v in out]
    return out, D


def check_orthogonal_basis_and_witt_basis():
    """A nondegenerate complex symmetric form has an orthogonal basis with nonzero squares
    (exact Gram-Schmidt over Q(i)); from an orthonormal basis, w_j = (e_2j + i e_2j+1)/2 and
    v_j = (e_2j - i e_2j+1)/2 form a Witt basis with v_i w_j + w_j v_i = delta_ij."""
    premise("std-algebra.polarisation")
    premise("std-algebra.witt-basis-car")
    ok = True
    grams = [
        [[0, 1], [1, 0]],
        [[0, I_, 0], [I_, 0, 1], [0, 1, 1]],
        [[1, I_, 0, 0], [I_, 1, 0, 0], [0, 0, 0, 2], [0, 0, 2, I_]],
        [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]],
    ]
    for G in grams:
        n = len(G)
        P, D = _gs_orthogonalise(G)
        ok = ok and len(P) == n and all(D)
        ok = ok and GA.field_rank(P) == n
        for a in range(n):
            for b in range(a + 1, n):
                val = sum((P[a][i] * _q(G[i][j]) * P[b][j] for i in range(n) for j in range(n)), ZERO)
                ok = ok and val == ZERO
    # any totally null W of dimension k has a totally null dual W': v_j = x_j - sum_l B(x_j, x_l) w_l
    def dotc(x, y):
        return sum((a * b for a, b in zip(x, y)), ZERO)

    u1, u2 = [ONE, I_, ZERO, ZERO], [ZERO, ZERO, ONE, I_]
    for W in ([[a + 2 * b for a, b in zip(u1, u2)], [a - I_ * b for a, b in zip(u1, u2)]],
              [[ONE, I_, ZERO, ZERO], [ZERO, ZERO, ONE, GA.QI(0, -1)]]):
        k, n = len(W), 4
        ok = ok and all(dotc(a, b) == ZERO for a in W for b in W)
        cols = next(c for c in combinations(range(n), k)
                    if GA.field_rank([[w[t] for t in c] for w in W]) == k)
        xs = []
        for j in range(k):
            sol = GA.field_solve([[w[t] for t in cols] for w in W],
                                 [GA.QI(F(1, 2)) if i == j else ZERO for i in range(k)])
            x = [ZERO] * n
            for t, val in zip(cols, sol):
                x[t] = val
            xs.append(x)
        vs = []
        for j in range(k):
            v = xs[j][:]
            for l in range(k):
                c = dotc(xs[j], xs[l])
                v = [a - c * b for a, b in zip(v, W[l])]
            vs.append(v)
        for i in range(k):
            for j in range(k):
                ok = ok and dotc(vs[i], W[j]) == (GA.QI(F(1, 2)) if i == j else ZERO)
                ok = ok and dotc(vs[i], vs[j]) == ZERO
        ok = ok and GA.field_rank(W + vs) == n
    # Witt basis in Cl(C^{2k}) with orthonormal generators, k = 1, 2, 3
    for k in (1, 2, 3):
        sq = tuple([1] * (2 * k))
        n = 2 * k
        ws, vs = [], []
        for j in range(k):
            c = [ZERO] * n
            c[2 * j], c[2 * j + 1] = GA.QI(F(1, 2)), GA.QI(0, F(1, 2))
            ws.append(_qvec(c))
            d = [ZERO] * n
            d[2 * j], d[2 * j + 1] = GA.QI(F(1, 2)), GA.QI(0, F(-1, 2))
            vs.append(_qvec(d))
        for i in range(k):
            for j in range(k):
                ok = ok and GA.is_zero(GA.add(GA.mul(ws[i], ws[j], sq), GA.mul(ws[j], ws[i], sq)))
                ok = ok and GA.is_zero(GA.add(GA.mul(vs[i], vs[j], sq), GA.mul(vs[j], vs[i], sq)))
                car = GA.add(GA.mul(vs[i], ws[j], sq), GA.mul(ws[j], vs[i], sq))
                ok = ok and GA.eq(car, {(): ONE} if i == j else {})
    GA.check("complex forms: exact orthogonal bases over Q(i); Witt basis of C^2k gives the CAR", ok)
    return ok


def check_fock_model_is_the_whole_matrix_algebra():
    """n = 2k, k = 1, 2, 3: the Fock operators of an orthonormal basis square to 1, anticommute,
    and their 4^k ordered products are C-linearly independent in End(Lambda W): Cl_2k(C) = M_2^k(C)."""
    premise("std-algebra.fock-representation")
    premise("std-algebra.blade-basis")
    ok = True
    ranks = []
    for k in (1, 2, 3):
        ms = _fock_orthonormal(k)
        d = 2 ** k
        one = S.mat_id(d)
        zero = S.mat_scal(0, one)
        for i in range(2 * k):
            ok = ok and S.mat_eq(S.mat_mul(ms[i], ms[i]), one)
            for j in range(i + 1, 2 * k):
                ok = ok and S.mat_eq(S.mat_add(S.mat_mul(ms[i], ms[j]), S.mat_mul(ms[j], ms[i])), zero)
        prods = _products(ms)
        ranks.append(GA.field_rank([_flat(P) for P in prods]))
        # vectors act oddly: they swap Lambda^even and Lambda^odd, so the even products are
        # block diagonal and span End(even) + End(odd) (dimension 2 * 4^(k-1))
        basis = _subsets(k)
        par = [len(s) % 2 for s in basis]
        evens = [P for m, P in zip([len(c) for c in _idx_sets(2 * k)], prods) if m % 2 == 0]
        for P in evens:
            ok = ok and all(P[a][b] == ZERO for a in range(d) for b in range(d) if par[a] != par[b])
        ok = ok and GA.field_rank([_flat(P) for P in evens]) == 2 * 4 ** (k - 1)
    ok = ok and ranks == [4, 16, 64]
    GA.check("Fock model over C: 4^k independent products, Cl_2k(C) = End(Lambda W); even part = "
             "End(even) + End(odd), k = 1, 2, 3", ok)
    return ok


def _idx_sets(n):
    return [c for m in range(n + 1) for c in combinations(range(n), m)]


def check_vacuum_idempotent_and_minimal_left_ideal():
    """In Cl(C^2k) itself (k = 1, 2, 3): f = v_1 w_1 ... v_k w_k is idempotent, v_i f = 0, and the
    left ideal Cl f has complex dimension 2^k with basis w_I f."""
    premise("std-algebra.fock-representation")
    premise("std-algebra.witt-basis-car")
    ok = True
    for k in (1, 2, 3):
        n = 2 * k
        sq = tuple([1] * n)
        ws, vs = [], []
        for j in range(k):
            c = [ZERO] * n
            c[2 * j], c[2 * j + 1] = GA.QI(F(1, 2)), GA.QI(0, F(1, 2))
            ws.append(_qvec(c))
            d = [ZERO] * n
            d[2 * j], d[2 * j + 1] = GA.QI(F(1, 2)), GA.QI(0, F(-1, 2))
            vs.append(_qvec(d))
        f = {(): ONE}
        for j in range(k):
            f = GA.mul(f, GA.mul(vs[j], ws[j], sq), sq)
        ok = ok and GA.eq(GA.mul(f, f, sq), f)
        ok = ok and all(GA.is_zero(GA.mul(v, f, sq)) for v in vs)
        left = [GA.mul({b: ONE}, f, sq) for b in GA.all_blades(n)]
        ok = ok and _qrank(left, n) == 2 ** k
        occ = []
        for I in _idx_sets(k):
            x = {(): ONE}
            for j in I:
                x = GA.mul(x, ws[j], sq)
            occ.append(GA.mul(x, f, sq))
        ok = ok and _qrank(occ, n) == 2 ** k
        ok = ok and _qrank(occ + left, n) == 2 ** k
    GA.check("vacuum idempotent f: f^2 = f, v_i f = 0, Cl f of dimension 2^k with basis w_I f", ok)
    return ok


def check_odd_dimension_splits():
    """n = 2k + 1 (k = 0, 1, 2): omega_C = i^{n(n-1)/2} e_1...e_n is central with omega_C^2 = 1;
    P+- = (1 +- omega_C)/2 split Cl = Cl P+ + Cl P-, each of dimension 4^k, and e_j -> i e_j e_n
    (j < n) generates Cl^+ as a copy of Cl_2k(C)."""
    premise("std-algebra.complexification")
    premise("std-algebra.even-subalgebra-isomorphism")
    premise("primer.centre")
    premise("primer.sign")
    ok = True
    for k in (0, 1, 2):
        n = 2 * k + 1
        sq = tuple([1] * n)
        m = n * (n - 1) // 2
        ph = ONE
        for _ in range(m):
            ph = ph * I_
        om = {tuple(range(n)): ph}
        ok = ok and GA.eq(GA.mul(om, om, sq), {(): ONE})
        ok = ok and all(GA.eq(GA.mul(om, {(j,): ONE}, sq), GA.mul({(j,): ONE}, om, sq)) for j in range(n))
        Pp = GA.add({(): GA.QI(F(1, 2))}, _qscal(GA.QI(F(1, 2)), om))
        Pm = GA.add({(): GA.QI(F(1, 2))}, _qscal(GA.QI(F(-1, 2)), om))
        ok = ok and GA.eq(GA.mul(Pp, Pp, sq), Pp) and GA.is_zero(GA.mul(Pp, Pm, sq))
        bl = GA.all_blades(n)
        ok = ok and _qrank([GA.mul({b: ONE}, Pp, sq) for b in bl], n) == 4 ** k
        ok = ok and _qrank([GA.mul({b: ONE}, Pm, sq) for b in bl], n) == 4 ** k
        evens = [{b: ONE} for b in bl if len(b) % 2 == 0]
        ok = ok and _qrank([GA.mul(x, Pp, sq) for x in evens], n) == 4 ** k
        # generators of Cl^+ as an algebra with an orthonormal basis of C^{n-1}
        gs = [_qscal(I_, GA.mul({(j,): ONE}, {(n - 1,): ONE}, sq)) for j in range(n - 1)]
        for a in range(len(gs)):
            ok = ok and GA.eq(GA.mul(gs[a], gs[a], sq), {(): ONE})
            for b in range(a + 1, len(gs)):
                ok = ok and GA.is_zero(GA.add(GA.mul(gs[a], gs[b], sq), GA.mul(gs[b], gs[a], sq)))
        prods = []
        for c in _idx_sets(n - 1):
            x = {(): ONE}
            for j in c:
                x = GA.mul(x, gs[j], sq)
            prods.append(x)
        ok = ok and _qrank(prods, n) == 2 ** (n - 1)
    GA.check("odd n: normalised omega_C central, omega_C^2 = 1, Cl = Cl P+ + Cl P- with Cl^+ = Cl_{n-1}(C)", ok)
    return ok


def _top_pairing(k):
    """beta(x, y) = top(tau(x) ^ y) on Lambda W, Gram matrix on the subset basis."""
    basis = _subsets(k)

    def wedge_sign(a, b):
        # sign of e_a ^ e_b relative to e_{a u b} (a, b disjoint, both increasing)
        inv = sum(1 for x in a for y in b if x > y)
        return -1 if inv % 2 else 1

    full = frozenset(range(k))
    G = []
    for s in basis:
        row = []
        m = len(s)
        tau = -1 if (m * (m - 1) // 2) % 2 else 1
        for t in basis:
            if s & t or (s | t) != full:
                row.append(ZERO)
            else:
                row.append(_q(tau * wedge_sign(sorted(s), sorted(t))))
        G.append(row)
    return G


def _transpose(M):
    return [list(r) for r in zip(*M)]


def check_complex_chevalley_pairing():
    """k = 1, 2, 3: beta(x, y) = top(tau x ^ y) is nondegenerate, pairs degree m with k - m, has
    symmetry (-1)^{k(k-1)/2}, every complex vector is self-adjoint (c(u)^T G = G c(u)), so every
    complex bivector is skew; for k = 3 it is antisymmetric and pairs even with odd."""
    premise("std-algebra.chevalley-pairing")
    premise("std-algebra.involution-properties")
    ok = True
    for k in (1, 2, 3):
        G = _top_pairing(k)
        d = 2 ** k
        basis = _subsets(k)
        ok = ok and GA.field_rank(G) == d
        sgn = -1 if (k * (k - 1) // 2) % 2 else 1
        ok = ok and S.mat_eq(_transpose(G), S.mat_scal(sgn, G))
        ok = ok and all(G[a][b] == ZERO for a in range(d) for b in range(d)
                        if len(basis[a]) + len(basis[b]) != k)
        ms = []
        for j in range(k):
            ms.append(_wedge(j, k))
            ms.append(_contract(j, k))
        # a complex vector u = sum a_j w_j + b_j v_j with Gaussian coefficients
        coeffs = [GA.QI(1, 2), GA.QI(0, -1), GA.QI(3), GA.QI(-1, 1), GA.QI(2, -3), GA.QI(0, 1)]
        U = S.mat_scal(0, S.mat_id(d))
        for c, Mj in zip(coeffs, ms):
            U = S.mat_add(U, S.mat_scal(c, Mj))
        for Mj in ms + [U]:
            ok = ok and S.mat_eq(S.mat_mul(_transpose(Mj), G), S.mat_mul(G, Mj))
        U2 = ms[0] if k == 1 else S.mat_add(ms[1], S.mat_scal(GA.QI(1, 1), ms[2]))
        # Clifford relations of these complex vectors: U^2 = Q(u) = sum a_j b_j, {U, U2} = 2B(u, u2)
        qu = {1: GA.QI(2, -1), 2: GA.QI(-1, 2), 3: GA.QI(2, 4)}[k]
        ok = ok and qu == sum((coeffs[2 * j] * coeffs[2 * j + 1] for j in range(k)), ZERO)
        ok = ok and S.mat_eq(S.mat_mul(U, U), S.mat_scal(qu, S.mat_id(d)))
        b2 = GA.QI(0, -1) if k == 1 else GA.QI(-1, 2)
        ok = ok and S.mat_eq(S.mat_add(S.mat_mul(U, U2), S.mat_mul(U2, U)), S.mat_scal(b2, S.mat_id(d)))
        Bv = S.mat_add(S.mat_mul(U, U2), S.mat_scal(-1, S.mat_mul(U2, U)))
        ok = ok and S.mat_eq(S.mat_add(S.mat_mul(_transpose(Bv), G), S.mat_mul(G, Bv)),
                             S.mat_scal(0, S.mat_id(d)))
        if k == 3:
            ok = ok and sgn == -1
            ok = ok and all(G[a][b] == ZERO for a in range(d) for b in range(d)
                            if len(basis[a]) % 2 == len(basis[b]) % 2)
    GA.check("C-bilinear Chevalley pairing: nondegenerate, degree m with k - m, symmetry "
             "(-1)^{k(k-1)/2}, complex vectors self-adjoint, bivectors skew; k = 3 antisymmetric", ok)
    return ok


def check_ascended_witt_basis():
    """The isotropic pair of the complexified Cl(2,4) used in the series (w_3 = b_3 + i b_4):
    a Witt basis after scaling, so the Fock model above applies to Cl(2,4)_C."""
    premise("std-algebra.complexification")
    premise("std-algebra.witt-basis-car")
    ok = True
    sq = GA.sig(2, 4)
    # a1, a2 square +1; b1..b4 square -1 (generators 0, 1 and 2..5)
    w = [_qvec([1, 0, 1, 0, 0, 0]), _qvec([0, 1, 0, 1, 0, 0]), _qvec([0, 0, 0, 0, 1, I_])]
    wp = [_qvec([F(1, 2), 0, F(-1, 2), 0, 0, 0]), _qvec([0, F(1, 2), 0, F(-1, 2), 0, 0]),
          _qvec([0, 0, 0, 0, F(-1, 2), GA.QI(0, F(1, 2))])]
    for i in range(3):
        for j in range(3):
            ok = ok and GA.is_zero(GA.add(GA.mul(w[i], w[j], sq), GA.mul(w[j], w[i], sq)))
            ok = ok and GA.is_zero(GA.add(GA.mul(wp[i], wp[j], sq), GA.mul(wp[j], wp[i], sq)))
            # w_i w'_j + w'_j w_i = 2 <w_i, w'_j> = 2 delta_ij: (w'_j / 2, w_i) is a Witt basis
            ok = ok and GA.eq(GA.add(GA.mul(w[i], wp[j], sq), GA.mul(wp[j], w[i], sq)),
                              {(): GA.QI(2)} if i == j else {})
    allv = w + wp
    ok = ok and GA.field_rank([[x.get((t,), ZERO) for t in range(6)] for x in allv]) == 6
    GA.check("the series' isotropic pair of Cl(2,4)_C is a Witt basis up to the factor 2", ok)
    return ok


def _qext_c(alpha, G, state):
    """Clifford action c(v) = v ^ + iota_{B(v, .)} on Lambda C^n, Gram G over Q(i)."""
    n = len(alpha)
    out = {}
    for i in range(n):
        if alpha[i]:
            for S_, c in state.items():
                if i in S_:
                    continue
                sign = -1 if sum(1 for j in S_ if j < i) % 2 else 1
                T = frozenset(S_ | {i})
                out[T] = out.get(T, ZERO) + alpha[i] * c * sign
    fv = [sum((alpha[i] * _q(G[i][j]) for i in range(n)), ZERO) for j in range(n)]
    for S_, c in state.items():
        for pos, j in enumerate(sorted(S_)):
            if fv[j]:
                T = frozenset(S_ - {j})
                out[T] = out.get(T, ZERO) + fv[j] * c * (-1 if pos % 2 else 1)
    return {k: v for k, v in out.items() if v}


def check_blade_basis_for_a_degenerate_complex_form():
    """Gram [[1, i, 0], [i, -1, 0], [0, 0, 0]] over Q(i) (rank 1, radical of dimension 2): the
    symbols of the 8 increasing products are triangular (leading coefficient 1) and independent,
    and c(v)^2 = Q(v) on a complex vector."""
    premise("std-algebra.blade-basis")
    premise("std-algebra.existence-uniqueness")
    ok = True
    G = [[ONE, I_, ZERO], [I_, GA.QI(-1), ZERO], [ZERO, ZERO, ZERO]]
    n = 3
    ok = ok and GA.field_rank(G) == 1
    keys = [frozenset(c) for m in range(n + 1) for c in combinations(range(n), m)]
    rows = []
    for m in range(n + 1):
        for c in combinations(range(n), m):
            st = {frozenset(): ONE}
            for i in reversed(c):
                st = _qext_c([ONE if j == i else ZERO for j in range(n)], G, st)
            ok = ok and st.get(frozenset(c), ZERO) == ONE and all(len(K) <= m for K in st)
            rows.append([st.get(K, ZERO) for K in keys])
    ok = ok and GA.field_rank(rows) == 8
    v = [GA.QI(2, 1), GA.QI(0, 3), GA.QI(-1)]
    qv = sum((v[i] * G[i][j] * v[j] for i in range(n) for j in range(n)), ZERO)
    ok = ok and qv == GA.QI(0, -2)
    st = {frozenset([0]): GA.QI(5), frozenset([1, 2]): GA.QI(1, -1)}
    ok = ok and _qext_c(v, G, _qext_c(v, G, st)) == {k: qv * c for k, c in st.items()}
    GA.check("degenerate complex form: 2^n increasing products independent, c(v)^2 = Q(v)", ok)
    return ok
