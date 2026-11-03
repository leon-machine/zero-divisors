"""mass.invariant-forms-simple-lie-algebra: exact checks.

The claim: on a finite-dimensional simple Lie algebra over C any two nonzero invariant symmetric
bilinear forms are proportional. Finite core checked here, on explicit simple algebras given by
rational structure constants (the rank of a rational linear system is the same over Q and over C,
so the dimension computed is the complex one):
(1) for sl(2), sl(3), so(5) and so(6) = sl(4) the space of invariant symmetric bilinear forms
    S([x, y], z) + S(y, [x, z]) = 0 is computed as an exact kernel: it is one-dimensional, and the
    Killing form tr(ad x ad y) lies in it and is nondegenerate (Cartan's criterion), so every invariant
    form is a multiple of the Killing form;
(2) controls that are not simple: gl(2) = sl(2) + C and so(4) = sl(2) + sl(2) each carry a
    two-dimensional space of invariant symmetric forms, so simplicity is what the statement needs.
For the larger algebras invariance is imposed under ad of a generating set (the elements x with ad x
skew for S form a Lie subalgebra), and the generating property is checked by closing the set under
brackets to full dimension.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise  # noqa: F401  (the claim cites only textbook results)


def unit(n, i, j):
    M = [[F(0)] * n for _ in range(n)]
    M[i][j] = F(1)
    return M


def madd(A, B, c=F(1)):
    return [[a + c * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), F(0)) for j in range(n)] for i in range(n)]


def br(A, B):
    return madd(mmul(A, B), mmul(B, A), F(-1))


def flat(M):
    return [x for row in M for x in row]


def sl_basis(n):
    out = [unit(n, i, j) for i in range(n) for j in range(n) if i != j]
    out += [madd(unit(n, i, i), unit(n, i + 1, i + 1), F(-1)) for i in range(n - 1)]
    return out


def gl_basis(n):
    return [unit(n, i, j) for i in range(n) for j in range(n)]


def so_basis(n):
    return [madd(unit(n, i, j), unit(n, j, i), F(-1)) for i, j in combinations(range(n), 2)]


class Lie:
    """Structure constants of a matrix Lie algebra in a given basis."""

    def __init__(self, basis):
        self.basis = basis
        self.n = len(basis)
        rows = [flat(b) for b in basis]
        # pivot coordinates: reduce the basis to read coordinates off a set of entries
        self.rows = rows
        self.c = {}
        for i in range(self.n):
            for j in range(self.n):
                self.c[(i, j)] = self.coords(br(basis[i], basis[j]))

    def coords(self, M):
        t = flat(M)
        cols = [list(r) for r in self.rows] + [[-x for x in t]]
        # kernel of the matrix whose columns are the basis vectors and -t
        A = [[cols[k][e] for k in range(len(cols))] for e in range(len(t))]
        ker = GA.field_kernel(A)
        ker = [v for v in ker if v[-1] != 0]
        v = ker[0]
        return [x / v[-1] for x in v[:-1]]

    def ad(self, i):
        """Matrix of ad x_i: column j is the coordinate vector of [x_i, x_j]."""
        return [[self.c[(i, j)][k] for j in range(self.n)] for k in range(self.n)]


def generated_dim(L, gens):
    span = [list(v) for v in gens]
    frontier = list(span)
    while frontier:
        new = []
        for a in frontier:
            for b in gens:
                v = [sum((a[i] * b[j] * L.c[(i, j)][k] for i in range(L.n) for j in range(L.n)
                          if a[i] and b[j]), F(0)) for k in range(L.n)]
                if GA.rank_of_vectors(span + [v]) > GA.rank_of_vectors(span):
                    span.append(v)
                    new.append(v)
        frontier = new
    return GA.rank_of_vectors(span)


def invariant_forms(L, which):
    """Kernel of the invariance equations for symmetric S, unknowns S_ab (a <= b), imposed under ad x_i
    for i in `which`."""
    pairs = [(a, b) for a in range(L.n) for b in range(a, L.n)]
    pos = {p: k for k, p in enumerate(pairs)}

    def var(a, b):
        return pos[(a, b) if a <= b else (b, a)]

    rows = []
    for i in which:
        ad = L.ad(i)
        for j in range(L.n):
            for k in range(j, L.n):
                row = [F(0)] * len(pairs)
                # S([x_i, x_j], x_k) + S(x_j, [x_i, x_k])
                for m in range(L.n):
                    if ad[m][j]:
                        row[var(m, k)] += ad[m][j]
                    if ad[m][k]:
                        row[var(j, m)] += ad[m][k]
                if any(row):
                    rows.append(row)
    ker = GA.field_kernel(rows)
    return pairs, ker


def killing(L):
    ads = [L.ad(i) for i in range(L.n)]
    return [[sum((ads[a][r][s] * ads[b][s][r] for r in range(L.n) for s in range(L.n)), F(0))
             for b in range(L.n)] for a in range(L.n)]


ALGEBRAS = {
    "sl2": Lie(sl_basis(2)),
    "sl3": Lie(sl_basis(3)),
    "so5": Lie(so_basis(5)),
    "so6": Lie(so_basis(6)),
    "gl2": Lie(gl_basis(2)),
    "so4": Lie(so_basis(4)),
}
# generating sets for the larger algebras (indices into the basis)
GENS = {"sl2": None, "sl3": None, "gl2": None, "so4": None, "so5": (0, 4, 7, 9), "so6": (0, 5, 9, 12, 14)}


def form_dim_and_killing(name):
    L = ALGEBRAS[name]
    which = range(L.n) if GENS[name] is None else GENS[name]
    pairs, ker = invariant_forms(L, which)
    K = killing(L)
    kvec = [K[a][b] for a, b in pairs]
    in_span = GA.rank_of_vectors(ker + [kvec]) == len(ker)
    return L, len(ker), K, in_span


def check_simple_algebras_have_one_invariant_form():
    ok = True
    expected_dims = {"sl2": 3, "sl3": 8, "so5": 10, "so6": 15}
    for name, d in expected_dims.items():
        L, nforms, K, in_span = form_dim_and_killing(name)
        ok = ok and L.n == d
        if GENS[name] is not None:
            e = [[F(1) if k == i else F(0) for k in range(L.n)] for i in GENS[name]]
            ok = ok and generated_dim(L, e) == d
        # exactly one invariant symmetric form up to scale, and it is the Killing form
        ok = ok and nforms == 1 and in_span
        # Killing form nondegenerate (Cartan's criterion for a simple algebra)
        ok = ok and GA.mat_rank(K) == d
    # Killing form of sl(2) on (E, F, H): K(E,F) = 4, K(H,H) = 8
    _, _, K2, _ = form_dim_and_killing("sl2")
    ok = ok and K2[0][1] == 4 and K2[2][2] == 8 and K2[0][0] == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_simple_algebras_have_one_invariant_form"; return _tp_rv


def check_non_simple_controls_have_two_forms():
    ok = True
    for name, d in (("gl2", 4), ("so4", 6)):
        L, nforms, K, in_span = form_dim_and_killing(name)
        ok = ok and L.n == d and nforms == 2 and in_span
    # the Killing form of gl(2) is degenerate (the centre is in its radical), so it is not the only one
    _, _, Kgl, _ = form_dim_and_killing("gl2")
    ok = ok and GA.mat_rank(Kgl) == 3
    _tp_rv = (ok); assert _tp_rv is not False, "check_non_simple_controls_have_two_forms"; return _tp_rv
