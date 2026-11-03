#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
GA.py: the Transport Papers' shared exact-arithmetic library.

Deposited alongside each paper's verify_TXX.py script.  Everything here is
exact: rational arithmetic (fractions.Fraction) throughout, no floating point
anywhere.  The library contains the machinery common to the series'
verification scripts; each script keeps only its paper-specific checks.

Contents:
  1. Check harness: FAILURES, check(label, ok).
  2. Basis-blade Clifford engine for diagonal signatures (degenerate
     generators permitted): elements are dicts {blade tuple: Fraction};
     blade_mul, mul, add, neg, sub, scal, sc, gen, grade_inv, reverse,
     eq, is_zero, commutes, anticommutes, sig, all_blades, basis_vector_of,
     dot (symmetric scalar product of vectors; aliases dotv, dot_scalar).
  3. Exact linear algebra over the rationals: rank_of_vectors (Gaussian
     elimination), congruence_signature (symmetric congruence
     diagonalisation with zero-diagonal repair), frac_matrix, mat_rank,
     mat_mul, mat_eq.
  4. Exterior-algebra model of the Clifford action for ARBITRARY rational
     Gram matrices (non-diagonal and degenerate included): ext_wedge,
     ext_contract, ext_c, ext_state_eq, ext_sigma_blade.  The symbol map is
     triangular, so the model is faithful.
  5. Exact polynomials and rational functions in one variable: ptrim, padd,
     pneg, pmul, pconst, peval, pderiv, pdivmod, pgcd; class RF (gcd-reduced,
     with arithmetic, deriv, eqrf, eval, is_zero); RF0, RF1; and matrices
     over the rational-function field: rf_mat_det, rf_mat_solve,
     rf_mat_inverse.
  6. Truncated power series over the rationals (added with T7): ps_trunc,
     ps_mul, ps_int, ps_inv, ps_pow_rat (J.C.P. Miller), ps_compose.
  7. Gaussian rationals QI = Q(i) and generic-field linear algebra (added
     with T14): class QI (exact complex rationals with conj), QI_I, qi,
     field_rank (rank of a matrix over any exact field), field_mat_mul,
     field_solve.
"""

from fractions import Fraction
from itertools import combinations

# ---------------------------------------------------------------------------
# 1. check harness
# ---------------------------------------------------------------------------

FAILURES = []


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILURES.append(label)


# ---------------------------------------------------------------------------
# 2. basis-blade Clifford engine (diagonal signatures; degenerate allowed)
# ---------------------------------------------------------------------------

def blade_mul(b1, b2, squares):
    """Product of two basis blades: returns (sign_coefficient, blade)."""
    lst = list(b1) + list(b2)
    coeff = Fraction(1)
    i = 0
    while i < len(lst) - 1:
        if lst[i] < lst[i + 1]:
            i += 1
        elif lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            coeff = -coeff
            if i > 0:
                i -= 1
        else:  # equal: contract e_k e_k = squares[k]
            coeff *= squares[lst[i]]
            del lst[i + 1]
            del lst[i]
            if coeff == 0:
                return Fraction(0), ()
            if i > 0:
                i -= 1
    return coeff, tuple(lst)


def mul(x, y, squares):
    out = {}
    for b1, c1 in x.items():
        for b2, c2 in y.items():
            s, b = blade_mul(b1, b2, squares)
            c = c1 * c2 * s
            if c != 0:
                out[b] = out.get(b, Fraction(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def add(*xs):
    out = {}
    for x in xs:
        for b, c in x.items():
            out[b] = out.get(b, Fraction(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def neg(x):
    return {b: -c for b, c in x.items()}


def sub(x, y):
    return add(x, neg(y))


def scal(c, x):
    c = Fraction(c)
    return {b: c * cc for b, cc in x.items()} if c != 0 else {}


def sc(c):
    c = Fraction(c)
    return {(): c} if c != 0 else {}


def gen(i):
    return {(i,): Fraction(1)}


def grade_inv(x):
    return {b: (c if len(b) % 2 == 0 else -c) for b, c in x.items()}


def reverse(x):
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = Fraction(-1) ** (g * (g - 1) // 2)
        out[b] = sign * c
    return {b: c for b, c in out.items() if c != 0}


def eq(x, y):
    return sub(x, y) == {}


def is_zero(x):
    return x == {}


def commutes(x, y, squares):
    return eq(mul(x, y, squares), mul(y, x, squares))


def anticommutes(x, y, squares):
    return is_zero(add(mul(x, y, squares), mul(y, x, squares)))


def sig(p, q, r=0):
    """Signature tuple: p generators squaring +1, q squaring -1, r squaring 0."""
    return tuple([1] * p + [-1] * q + [0] * r)


def all_blades(n):
    out = []
    for k in range(n + 1):
        out.extend(combinations(range(n), k))
    return out


def basis_vector_of(x, blades):
    return [x.get(b, Fraction(0)) for b in blades]


def dot(x, y, squares):
    """Symmetric scalar product of vectors: scalar part of (xy + yx)/2."""
    z = add(mul(x, y, squares), mul(y, x, squares))
    return z.get((), Fraction(0)) / 2


dotv = dot
dot_scalar = dot


# ---------------------------------------------------------------------------
# 3. exact linear algebra over the rationals
# ---------------------------------------------------------------------------

def rank_of_vectors(vectors):
    """Exact rank by Gaussian elimination over Fraction."""
    m = [list(v) for v in vectors]
    rank, ncols = 0, (len(m[0]) if m else 0)
    row = 0
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
        row += 1
        rank += 1
        if row == len(m):
            break
    return rank


def congruence_signature(M):
    """Exact signature (n_plus, n_minus, n_zero) of a rational symmetric matrix
    by congruence diagonalisation with the standard zero-diagonal repair."""
    n = len(M)
    A = [[Fraction(M[i][j]) for j in range(n)] for i in range(n)]
    pos = neg_ = zer = 0
    r = 0
    while r < n:
        piv = next((i for i in range(r, n) if A[i][i] != 0), None)
        if piv is None:
            found = None
            for i in range(r, n):
                for j in range(i + 1, n):
                    if A[i][j] != 0:
                        found = (i, j)
                        break
                if found:
                    break
            if found is None:
                zer += n - r
                break
            i, j = found
            for k in range(n):
                A[i][k] += A[j][k]
            for k in range(n):
                A[k][i] += A[k][j]
            continue
        if piv != r:
            A[r], A[piv] = A[piv], A[r]
            for k in range(n):
                A[k][r], A[k][piv] = A[k][piv], A[k][r]
        d = A[r][r]
        if d > 0:
            pos += 1
        else:
            neg_ += 1
        for i in range(r + 1, n):
            f = A[i][r] / d
            if f:
                for k in range(n):
                    A[i][k] -= f * A[r][k]
                for k in range(n):
                    A[k][i] -= f * A[k][r]
        r += 1
    return pos, neg_, zer


def frac_matrix(M):
    return [[Fraction(x) for x in row] for row in M]


def mat_rank(M):
    return rank_of_vectors([list(r) for r in M]) if M else 0


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def mat_eq(A, B):
    return len(A) == len(B) and all(A[i] == B[i] for i in range(len(A)))


# ---------------------------------------------------------------------------
# 4. exterior-algebra model of Cl(W, B) for arbitrary rational Gram B
#    states: dict {frozenset: Fraction};  c(alpha) = wedge + contraction
# ---------------------------------------------------------------------------

def ext_wedge(i, state):
    out = {}
    for S, c in state.items():
        if i in S:
            continue
        sign = Fraction(-1) ** len([j for j in S if j < i])
        T = frozenset(S | {i})
        out[T] = out.get(T, Fraction(0)) + sign * c
    return {S: c for S, c in out.items() if c != 0}


def ext_contract(fvals, state):
    out = {}
    for S, c in state.items():
        Ss = sorted(S)
        for pos, j in enumerate(Ss):
            if fvals[j] == 0:
                continue
            sign = Fraction(-1) ** pos
            T = frozenset(S - {j})
            out[T] = out.get(T, Fraction(0)) + sign * fvals[j] * c
    return {S: c for S, c in out.items() if c != 0}


def ext_c(alpha, B, state):
    """Clifford action of the vector alpha (coefficient list) on an exterior state."""
    n = len(alpha)
    out = {}
    for i in range(n):
        if alpha[i] != 0:
            for S, c in ext_wedge(i, state).items():
                out[S] = out.get(S, Fraction(0)) + alpha[i] * c
    fvals = [sum(alpha[i] * Fraction(B[i][j]) for i in range(n)) for j in range(n)]
    for S, c in ext_contract(fvals, state).items():
        out[S] = out.get(S, Fraction(0)) + c
    return {S: c for S, c in out.items() if c != 0}


def ext_state_eq(x, y):
    ks = set(x) | set(y)
    return all(x.get(k, Fraction(0)) == y.get(k, Fraction(0)) for k in ks)


def ext_sigma_blade(I, B, n):
    state = {frozenset(): Fraction(1)}
    for i in reversed(I):
        state = ext_c([Fraction(1) if j == i else Fraction(0) for j in range(n)], B, state)
    return state


# ---------------------------------------------------------------------------
# 5. exact polynomials and rational functions in one variable
# ---------------------------------------------------------------------------

def ptrim(p):
    while p and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else Fraction(0)) + (b[i] if i < len(b) else Fraction(0))
                  for i in range(n)])


def pneg(a):
    return [-x for x in a]


def pmul(a, b):
    if not a or not b:
        return []
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return ptrim(out)


def pconst(c):
    c = Fraction(c)
    return [c] if c != 0 else []


def peval(p, t):
    t = Fraction(t)
    out = Fraction(0)
    for c in reversed(p):
        out = out * t + c
    return out


def pderiv(a):
    return ptrim([Fraction(i) * a[i] for i in range(1, len(a))])


def pdivmod(a, b):
    """Polynomial division over Fraction: returns (quotient, remainder)."""
    a = list(a)
    q = [Fraction(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b) and a:
        f = a[-1] / b[-1]
        d = len(a) - len(b)
        q[d] = f
        for i in range(len(b)):
            a[d + i] -= f * b[i]
        ptrim(a)
    return ptrim(q), ptrim(a)


def pgcd(a, b):
    a, b = ptrim(list(a)), ptrim(list(b))
    while b:
        a, b = b, pdivmod(a, b)[1]
    if a:
        lead = a[-1]
        a = [c / lead for c in a]
    return a


class RF(object):
    """Rational function num/den (polynomial coefficient lists), gcd-reduced."""

    def __init__(self, num, den=None):
        if den is None:
            den = pconst(1)
        if not den:
            raise ZeroDivisionError
        num, den = ptrim(list(num)), ptrim(list(den))
        if not num:
            den = pconst(1)
        else:
            g = pgcd(num, den)
            if len(g) > 1:
                num = pdivmod(num, g)[0]
                den = pdivmod(den, g)[0]
        self.num = num
        self.den = den

    @staticmethod
    def const(c):
        return RF(pconst(c))

    @staticmethod
    def var():
        return RF([Fraction(0), Fraction(1)])

    def __add__(self, o):
        return RF(padd(pmul(self.num, o.den), pmul(o.num, self.den)), pmul(self.den, o.den))

    def __sub__(self, o):
        return RF(padd(pmul(self.num, o.den), pneg(pmul(o.num, self.den))), pmul(self.den, o.den))

    def __mul__(self, o):
        return RF(pmul(self.num, o.num), pmul(self.den, o.den))

    def __truediv__(self, o):
        if not o.num:
            raise ZeroDivisionError
        return RF(pmul(self.num, o.den), pmul(self.den, o.num))

    def __neg__(self):
        return RF(pneg(self.num), self.den)

    def deriv(self):
        return RF(padd(pmul(pderiv(self.num), self.den), pneg(pmul(self.num, pderiv(self.den)))),
                  pmul(self.den, self.den))

    def eqrf(self, o):
        return pmul(self.num, o.den) == pmul(o.num, self.den)

    def is_zero(self):
        return not self.num

    def eval(self, t):
        if not self.num:
            return Fraction(0)
        d = peval(self.den, t)
        if d == 0:
            raise ZeroDivisionError("pole at %s" % t)
        return peval(self.num, t) / d


RF0 = RF.const(0)
RF1 = RF.const(1)


def rf_mat_det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    out = RF0
    for j in range(n):
        if M[0][j].is_zero():
            continue
        minor = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = M[0][j] * rf_mat_det(minor)
        out = out + term if j % 2 == 0 else out - term
    return out


def rf_mat_solve(M, rhs):
    """Solve M x = rhs over the rational-function field (M square, invertible)."""
    n = len(M)
    A = [[M[i][j] for j in range(n)] + [rhs[i]] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if not A[r][col].is_zero())
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r != col and not A[r][col].is_zero():
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [A[i][n] for i in range(n)]


def rf_mat_inverse(M):
    n = len(M)
    cols = []
    for j in range(n):
        e = [RF1 if i == j else RF0 for i in range(n)]
        cols.append(rf_mat_solve(M, e))
    return [[cols[j][i] for j in range(n)] for i in range(n)]


# ---------------------------------------------------------------------------
# 6. truncated power series over the rationals (added with T7; coefficient
#    lists [c0, c1, ...] in a formal variable, all operations exact and
#    truncated to a stated order N, meaning coefficients 0..N are kept)
# ---------------------------------------------------------------------------

def ps_trunc(a, N):
    """Truncate a coefficient list to order N (inclusive)."""
    return list(a[:N + 1]) + [Fraction(0)] * max(0, N + 1 - len(a))


def ps_mul(a, b, N):
    """Product of two truncated series, to order N."""
    out = [Fraction(0)] * (N + 1)
    for i, x in enumerate(a[:N + 1]):
        if x == 0:
            continue
        for j, y in enumerate(b[:N + 1 - i]):
            out[i + j] += x * y
    return out


def ps_int(a):
    """Termwise antiderivative with zero constant term."""
    return [Fraction(0)] + [Fraction(c, 1) / (i + 1) for i, c in enumerate(a)]


def ps_inv(a, N):
    """Multiplicative inverse of a series with a[0] != 0, to order N."""
    a = ps_trunc(a, N)
    if a[0] == 0:
        raise ZeroDivisionError("series has zero constant term")
    b = [Fraction(0)] * (N + 1)
    b[0] = 1 / Fraction(a[0])
    for n in range(1, N + 1):
        b[n] = -b[0] * sum(a[k] * b[n - k] for k in range(1, n + 1))
    return b


def ps_pow_rat(a, alpha, N):
    """a(x)**alpha for a series with a[0] == 1 and rational alpha,
    by the J.C.P. Miller recurrence; exact, to order N."""
    a = ps_trunc(a, N)
    if a[0] != 1:
        raise ValueError("ps_pow_rat needs unit constant term")
    alpha = Fraction(alpha)
    b = [Fraction(0)] * (N + 1)
    b[0] = Fraction(1)
    for n in range(1, N + 1):
        b[n] = sum(((alpha + 1) * Fraction(k, n) - 1) * a[k] * b[n - k]
                   for k in range(1, n + 1))
    return b


def ps_compose(f, g, N):
    """f(g(x)) for truncated series with g[0] == 0, to order N."""
    g = ps_trunc(g, N)
    if g[0] != 0:
        raise ValueError("ps_compose needs g(0) = 0")
    out = [Fraction(0)] * (N + 1)
    out[0] = Fraction(f[0]) if f else Fraction(0)
    gp = [Fraction(1)] + [Fraction(0)] * N  # g**k, running
    for k in range(1, min(len(f), N + 1)):
        gp = ps_mul(gp, g, N)
        if f[k] == 0:
            continue
        for i in range(N + 1):
            out[i] += Fraction(f[k]) * gp[i]
    return out


# ---------------------------------------------------------------------------
# 7. Gaussian rationals QI = Q(i), and generic-field linear algebra (added
#    with T9's verify_T09.py, 2026-08-21; field_kernel added with T9 v1.2;
#    append-only per house rule 12).  QI is an exact field: both
#    components are fractions.Fraction, no floating point.  The field_* helpers
#    work over any exact field whose elements support +, -, *, /, ==, and
#    truthiness (nonzero test), so they serve Fraction and QI alike.
# ---------------------------------------------------------------------------

class QI(object):
    """Gaussian rational re + im*i, exact."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        if isinstance(re, QI):
            self.re, self.im = re.re, re.im
            if im:
                raise ValueError("QI(QI, im) with im != 0")
        else:
            self.re = Fraction(re)
            self.im = Fraction(im)

    @staticmethod
    def _co(x):
        return x if isinstance(x, QI) else QI(x)

    def __add__(self, o):
        o = QI._co(o)
        return QI(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = QI._co(o)
        return QI(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return QI._co(o).__sub__(self)

    def __mul__(self, o):
        o = QI._co(o)
        return QI(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = QI._co(o)
        n = o.re * o.re + o.im * o.im
        if n == 0:
            raise ZeroDivisionError
        return QI((self.re * o.re + self.im * o.im) / n, (self.im * o.re - self.re * o.im) / n)

    def __rtruediv__(self, o):
        return QI._co(o).__truediv__(self)

    def __neg__(self):
        return QI(-self.re, -self.im)

    def __eq__(self, o):
        o = QI._co(o)
        return self.re == o.re and self.im == o.im

    def __ne__(self, o):
        return not self.__eq__(o)

    def __bool__(self):
        return self.re != 0 or self.im != 0

    __nonzero__ = __bool__

    def conj(self):
        return QI(self.re, -self.im)

    def __repr__(self):
        return "QI(%s, %s)" % (self.re, self.im)


QI_I = QI(0, 1)


def qi(re=0, im=0):
    return QI(re, im)


def field_rank(M):
    """Exact rank of a matrix over any exact field (rows of field elements)."""
    m = [list(r) for r in M]
    if not m:
        return 0
    rank, row, ncols = 0, 0, len(m[0])
    for col in range(ncols):
        piv = next((r for r in range(row, len(m)) if m[r][col]), None)
        if piv is None:
            continue
        m[row], m[piv] = m[piv], m[row]
        pv = m[row][col]
        m[row] = [a / pv for a in m[row]]
        for r in range(len(m)):
            if r != row and m[r][col]:
                f = m[r][col]
                m[r] = [a - f * b for a, b in zip(m[r], m[row])]
        row += 1
        rank += 1
        if row == len(m):
            break
    return rank


def field_mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), QI(0)) for j in range(p)]
            for i in range(n)]


def field_solve(M, rhs):
    """Solve M x = rhs over any exact field (M square, invertible)."""
    n = len(M)
    A = [[M[i][j] for j in range(n)] + [rhs[i]] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col])
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r != col and A[r][col]:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [A[i][n] for i in range(n)]


def field_kernel(M):
    """Basis of the kernel of a matrix over any exact field (rows x cols);
    promoted from verify_T09.py (2026-09-01, T9 v1.2), append-only."""
    rows, cols = len(M), len(M[0])
    A = [list(row) for row in M]
    piv_cols = []
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv_cols.append(c)
        r += 1
        if r == rows:
            break
    zero = A[0][0] - A[0][0]
    one = zero + 1
    free = [c for c in range(cols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [zero] * cols
        v[fc] = one
        for i, pc in enumerate(piv_cols):
            v[pc] = -A[i][fc]
        basis.append(v)
    return basis
