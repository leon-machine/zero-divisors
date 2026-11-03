# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""stdalg.py: helpers for the checks of the algebra core (subject standard-algebra).

Everything is exact (fractions.Fraction, and GA.QI for the complex unit); no floating
point. Multivectors are GA's dicts {blade tuple: Fraction} over a diagonal signature
`sq` (GA.sig(p, q, r)); degenerate generators are allowed.

Contents:
  signatures(nmax, degenerate)   every (p, q, r) with 1 <= p+q+r <= nmax
  vec(cs), blade(*idx), grade(x, k), grades(x), pseudoscalar(n)
  outer(a, b, sq), lc(a, b, sq)  outer product and left contraction, by grade projection
  conj(x)                        Clifford conjugation (reversion composed with grade involution)
  sample(n, seed, grades=None)   a deterministic multivector with small integer coefficients
  sample_vec(n, seed)
  coords(x, n), span_rank(xs, n) coordinates in the blade basis, rank of a list of elements
  nullspace(M)                   exact basis of the kernel of a rational matrix
  centre_basis(sq)               basis of the centre, solved as a linear system
  left_matrix(x, sq)             matrix of left multiplication by x in the blade basis
  mat_* over GA.QI               mat_id, mat_mul, mat_add, mat_scal, mat_eq, real_span_rank
  check_matrix_rep(ms, sq, dim)  generator images satisfy the Clifford relations and their
                                 products span a real algebra of dimension dim
"""
from fractions import Fraction as F
from itertools import combinations

import GA


def signatures(nmax, degenerate=True):
    out = []
    for n in range(1, nmax + 1):
        for r in range(0, (n if degenerate else 0) + 1):
            for q in range(0, n - r + 1):
                out.append((n - r - q, q, r))
    return out


def vec(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c != 0}


def blade(*idx):
    return {tuple(idx): F(1)}


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def grades(x):
    return sorted({len(b) for b in x})


def pseudoscalar(n):
    return {tuple(range(n)): F(1)}


def outer(a, b, sq):
    out = {}
    for r in grades(a):
        for s in grades(b):
            out = GA.add(out, grade(GA.mul(grade(a, r), grade(b, s), sq), r + s))
    return out


def lc(a, b, sq):
    """Left contraction: <a>_r lc <b>_s = <a_r b_s>_{s-r} when s >= r, else 0."""
    out = {}
    for r in grades(a):
        for s in grades(b):
            if s >= r:
                out = GA.add(out, grade(GA.mul(grade(a, r), grade(b, s), sq), s - r))
    return out


def conj(x):
    return GA.grade_inv(GA.reverse(x))


def sample(n, seed, grades_=None):
    """Deterministic element: coefficient ((seed^2 + 3 seed j + 2 j^2 + j) mod 7) - 3 on the j-th
    blade. Different seeds give different elements, and sample_vec(n, 1..n) are linearly
    independent for n <= 5 (pinned in tests/test_lib_stdalg.py)."""
    out = {}
    for j, b in enumerate(GA.all_blades(n)):
        if grades_ is not None and len(b) not in grades_:
            continue
        c = (seed * seed + 3 * seed * j + 2 * j * j + j) % 7 - 3
        if c:
            out[b] = F(c)
    return out


def sample_vec(n, seed):
    return sample(n, seed, grades_=(1,))


def coords(x, n):
    return [x.get(b, F(0)) for b in GA.all_blades(n)]


def span_rank(xs, n):
    return GA.rank_of_vectors([coords(x, n) for x in xs]) if xs else 0


def nullspace(M):
    """Basis of {x : M x = 0} for a rational matrix M (list of rows)."""
    if not M:
        return []
    ncols = len(M[0])
    m = [[F(a) for a in row] for row in M]
    pivots, row = [], 0
    for col in range(ncols):
        piv = next((r for r in range(row, len(m)) if m[r][col] != 0), None)
        if piv is None:
            continue
        m[row], m[piv] = m[piv], m[row]
        pv = m[row][col]
        m[row] = [a / pv for a in m[row]]
        for r in range(len(m)):
            if r != row and m[r][col] != 0:
                f = m[r][col]
                m[r] = [a - f * b for a, b in zip(m[r], m[row])]
        pivots.append(col)
        row += 1
        if row == len(m):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fcol in free:
        v = [F(0)] * ncols
        v[fcol] = F(1)
        for i, pc in enumerate(pivots):
            v[pc] = -m[i][fcol]
        basis.append(v)
    return basis


def centre_basis(sq):
    """Basis of the centre of the algebra with signature sq: x with e_i x = x e_i for all i."""
    n = len(sq)
    blades = GA.all_blades(n)
    rows = []
    for i in range(n):
        cols = [coords(GA.sub(GA.mul(GA.gen(i), {b: F(1)}, sq), GA.mul({b: F(1)}, GA.gen(i), sq)), n)
                for b in blades]
        for k in range(len(blades)):
            rows.append([cols[j][k] for j in range(len(blades))])
    return [{b: c for b, c in zip(blades, v) if c != 0} for v in nullspace(rows)]


def left_matrix(x, sq):
    n = len(sq)
    blades = GA.all_blades(n)
    cols = [coords(GA.mul(x, {b: F(1)}, sq), n) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


# ---- matrices over GA.QI (Gaussian rationals) -------------------------------

def _qi(a):
    return a if isinstance(a, GA.QI) else GA.QI(F(a))


def mat(rows):
    return [[_qi(a) for a in row] for row in rows]


def mat_id(d):
    return [[_qi(1 if i == j else 0) for j in range(d)] for i in range(d)]


def mat_mul(A, B):
    return GA.field_mat_mul(A, B)


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_scal(c, A):
    c = _qi(c)
    return [[c * a for a in row] for row in A]


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def _re_im(a):
    a = _qi(a)
    return a.re, a.im


def real_span_rank(Ms):
    """Rank over R of a list of complex matrices, each read as a real vector (re, im parts)."""
    rows = []
    for M in Ms:
        row = []
        for r in M:
            for a in r:
                re, im = _re_im(a)
                row += [re, im]
        rows.append(row)
    return GA.rank_of_vectors(rows)


def check_matrix_rep(ms, sq, dim):
    """ms[i] squares to sq[i] times the identity, distinct images anticommute, and the
    2^n ordered products of the images span a real space of dimension dim."""
    n = len(ms)
    d = len(ms[0])
    one = mat_id(d)
    ok = all(mat_eq(mat_mul(ms[i], ms[i]), mat_scal(sq[i], one)) for i in range(n))
    zero = mat_scal(0, one)
    for i in range(n):
        for j in range(i + 1, n):
            ok = ok and mat_eq(mat_add(mat_mul(ms[i], ms[j]), mat_mul(ms[j], ms[i])), zero)
    prods = []
    for k in range(n + 1):
        for idx in combinations(range(n), k):
            P = one
            for i in idx:
                P = mat_mul(P, ms[i])
            prods.append(P)
    return ok and real_span_rank(prods) == dim
