"""sheaf.blade-basis-degenerate-forms-included: exact checks.

The algebra Cl(W, B) for an arbitrary rational symmetric Gram matrix B in an arbitrary basis e_1..e_n
(non-orthogonal, degenerate, zero) is modelled faithfully on the exterior algebra (GA section 4):
c(a) = a wedge + contraction with B(a, .), so c(a)^2 = B(a, a) and x -> x.1 is the symbol map.
(1) For Gram matrices of sizes 2, 3, 4 (hyperbolic in a null basis, the zero form, rank-one with no
orthogonal pair, degenerate non-orthogonal, nondegenerate non-orthogonal) the symbols of the 2^n
blades e_I are linearly independent (rank 2^n): the blades are a basis.
(2) The structure constants of e_I e_J in the blade basis (computed by unitriangular back-substitution)
satisfy e_i e_j + e_j e_i = 2 B_ij and e_i^2 = B_ii, are associative on every triple of blades, and
for diagonal B agree with GA.mul.
(3) Polynomial in the entries: along B(t) = B0 + t B1 every structure constant at t = n + 1, 1/2 and
-7/3 equals the Lagrange interpolant of its values at t = 0..n, i.e. it is a polynomial of degree at
most n in t; and the constant of e_2 e_1 at the scalar blade is exactly 2 B_12(t), linear in t.
"""
from fractions import Fraction as F
from itertools import combinations
import GA

GRAMS = [
    [[0, 1], [1, 0]],
    [[0, 0], [0, 0]],
    [[1, 2], [2, 0]],
    [[0, 0, 0], [0, 2, 1], [0, 1, -3]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 1, 0, 2], [1, 0, 3, 0], [0, 3, -1, 1], [2, 0, 1, 0]],
    [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
]
# indices of GRAMS whose blade triples are tested for associativity: every n <= 3 and one 4x4 (time)
ASSOC_GRAMS = [0, 1, 2, 3, 4, 5, 6]
# diagonal forms on which the model's structure constants are compared with GA.mul
DIAGONAL_SIGS = (GA.sig(1, 1, 1), GA.sig(2, 1), GA.sig(0, 2, 2))
# the sample line B(t) = LINE_B0 + t LINE_B1 in 3x3 Gram space
LINE_B0 = [[0, 0, 0], [0, 2, 1], [0, 1, -3]]
LINE_B1 = [[1, 0, 2], [0, 0, 1], [2, 1, 1]]
# interpolation nodes t = 0..n (n + 1 of them: agreement off the nodes means degree <= n)
LINE_NODES = [F(k) for k in range(len(LINE_B0) + 1)]
# off-node sample values of t
LINE_OFF_NODES = (F(len(LINE_B0) + 1), F(1, 2), F(-7, 3))


def blade_el(I):
    """The basis element e_I as a coefficient dict."""
    return {I: F(1)}


def coef(x, K):
    """Coefficient of blade K in x (zero when absent)."""
    return x.get(K, F(0))


def blades(n):
    out = []
    for k in range(n + 1):
        out.extend(combinations(range(n), k))
    return out


def unit(i, n):
    return [F(1) if j == i else F(0) for j in range(n)]


def to_blades(state, B, n):
    """Blade coordinates of the element whose symbol is `state` (sigma(e_K) = e_K + lower degree)."""
    st = dict(state)
    coef = {}
    while st:
        K = max(st, key=lambda S: (len(S), sorted(S)))
        c = st[K]
        Kt = tuple(sorted(K))
        coef[Kt] = coef.get(Kt, F(0)) + c
        sig = GA.ext_sigma_blade(Kt, B, n)
        for S, a in sig.items():
            st[S] = st.get(S, F(0)) - c * a
        st = {S: a for S, a in st.items() if a != 0}
    return {K: c for K, c in coef.items() if c != 0}


def table(B):
    n = len(B)
    Bf = GA.frac_matrix(B)
    T = {}
    for I in blades(n):
        for J in blades(n):
            st = GA.ext_sigma_blade(J, Bf, n)
            for i in reversed(I):
                st = GA.ext_c(unit(i, n), Bf, st)
            T[(I, J)] = to_blades(st, Bf, n)
    return T


def tmul(x, y, T):
    out = {}
    for I, a in x.items():
        for J, b in y.items():
            for K, c in T[(I, J)].items():
                out[K] = out.get(K, F(0)) + a * b * c
    return {K: c for K, c in out.items() if c != 0}


def check_blades_are_a_basis():
    ok = True
    for B in GRAMS:
        n = len(B)
        Bf = GA.frac_matrix(B)
        bl = blades(n)
        vecs = []
        for I in bl:
            st = GA.ext_sigma_blade(I, Bf, n)
            vecs.append([st.get(frozenset(J), F(0)) for J in bl])
        ok = ok and GA.rank_of_vectors(vecs) == 2 ** n
        # the model is a Clifford action: c(a)^2 = B(a, a) on every basis state, a = (1, 2, -1, 3)[:n]
        a = [F(x) for x in (1, 2, -1, 3)[:n]]
        Baa = sum(a[i] * Bf[i][j] * a[j] for i in range(n) for j in range(n))
        for J in bl:
            st = {frozenset(J): F(1)}
            want = {frozenset(J): Baa} if Baa != 0 else {}
            ok = ok and GA.ext_state_eq(GA.ext_c(a, Bf, GA.ext_c(a, Bf, st)), want)
    GA.check("the 2^n blades of any basis are a basis of Cl(W, B), degenerate and non-orthogonal B", ok)
    return ok


def check_structure_constants():
    ok = True
    for idx, B in enumerate(GRAMS):
        n = len(B)
        T = table(B)
        for i in range(n):
            for j in range(n):
                s = GA.add(T[((i,), (j,))], T[((j,), (i,))])
                ok = ok and GA.eq(s, GA.sc(2 * B[i][j]))
        if idx in ASSOC_GRAMS:
            bl = blades(n)
            for I in bl:
                for J in bl:
                    for K in bl:
                        x, y, z = blade_el(I), blade_el(J), blade_el(K)
                        ok = ok and GA.eq(tmul(tmul(x, y, T), z, T), tmul(x, tmul(y, z, T), T))
    # diagonal B: the model's structure constants are GA.mul's
    for sq in DIAGONAL_SIGS:
        n = len(sq)
        B = [[sq[i] if i == j else 0 for j in range(n)] for i in range(n)]
        T = table(B)
        ok = ok and all(GA.eq(T[(I, J)], GA.mul({I: F(1)}, {J: F(1)}, sq))
                        for I in blades(n) for J in blades(n))
    GA.check("structure constants: e_i e_j + e_j e_i = 2 B_ij, associative, equal to GA.mul when diagonal", ok)
    return ok


def lagrange(xs, ys, t):
    tot = F(0)
    for k, (xk, yk) in enumerate(zip(xs, ys)):
        term = yk
        for m, xm in enumerate(xs):
            if m != k:
                term = term * (t - xm) / (xk - xm)
        tot += term
    return tot


def check_structure_constants_polynomial():
    ok = True
    B0, B1 = LINE_B0, LINE_B1
    n = len(B0)

    def B_at(t):
        return [[F(B0[i][j]) + t * B1[i][j] for j in range(n)] for i in range(n)]

    pts = LINE_NODES
    tabs = [table(B_at(t)) for t in pts]
    for t in LINE_OFF_NODES:
        Tt = table(B_at(t))
        for key in Tt:
            Ks = set(Tt[key])
            for tb in tabs:
                Ks |= set(tb[key])
            for K in Ks:
                val = lagrange(pts, [coef(tb[key], K) for tb in tabs], t)
                ok = ok and val == coef(Tt[key], K)
        # rewriting rule e_i e_j = 2 B_ij(t) - e_j e_i (i > j): scalar constant 2 B_ij(t), linear in t,
        # and coefficient -1 on the blade e_j e_i
        for i in range(n):
            for j in range(i):
                ok = ok and coef(Tt[((i,), (j,))], ()) == 2 * (B0[i][j] + t * B1[i][j])
                ok = ok and coef(Tt[((i,), (j,))], (j, i)) == -1
    GA.check("structure constants are polynomial (degree <= n) in the Gram entries along a line", ok)
    return ok
