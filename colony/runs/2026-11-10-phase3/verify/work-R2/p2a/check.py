"""Exact checks: the momentum of Premise H1 is the only spin-covariant quadratic vector on the spinor ideal.

Setting (T14c, Definition of ideals, fields and momentum): a causal tower V = R^(p,q), min(p,q) = 1, e_t the
basis vector of the minority sign, f = (1 + e_t e_a)/2 for a space direction e_a, the spinor ideal
S = Cl^0(V) f, and the momentum j(psi) = <psi e_t rev(psi)>_1. Everything is built in GA.py over Fractions.

The spin algebra is the space of bivectors B; it acts on S by left multiplication, psi -> B psi, and on V by
the commutator, v -> B v - v B. A quadratic map S -> V is the diagonal of a symmetric real bilinear map
beta : S x S -> V; it is spin-covariant when
    beta(B psi, phi) + beta(psi, B phi) = B beta(psi, phi) - beta(psi, phi) B
for every basis bivector B and every pair of basis elements psi, phi of S. This is a homogeneous linear
system with rational coefficients in the coordinates of beta, so its rank over Q is its rank over R, and the
dimension of the solution space is computed exactly. The same system with values in the scalars (right-hand
side zero) counts the invariant quadratic scalars.

Symbolic identities use spinors with polynomial coordinates (a small polynomial ring over Q as GA
coefficients), so they hold for every psi in S.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


class Poly(object):
    """Polynomials over Q in several variables: {exponent tuple: Fraction}."""
    __slots__ = ('t', 'n')

    def __init__(self, t=None, n=0):
        self.t = {k: v for k, v in (t or {}).items() if v != 0}
        self.n = n

    @staticmethod
    def var(i, n):
        return Poly({tuple(int(k == i) for k in range(n)): F(1)}, n)

    def _co(self, o):
        if isinstance(o, Poly):
            return o
        o = F(o)
        return Poly({(0,) * self.n: o}, self.n)

    def __add__(self, o):
        o = self._co(o)
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, 0) + v
        return Poly(r, max(self.n, o.n))

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()}, self.n)

    def __sub__(self, o):
        return self + (-self._co(o))

    def __rsub__(self, o):
        return self._co(o) + (-self)

    def __mul__(self, o):
        if not isinstance(o, Poly):
            o = F(o)
            return Poly({k: v * o for k, v in self.t.items()}, self.n)
        r = {}
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                r[k] = r.get(k, 0) + v1 * v2
        return Poly(r, self.n)

    __rmul__ = __mul__

    def __eq__(self, o):
        return (self - self._co(o)).t == {}

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return id(self)


def mv_eq(x, y):
    return all((x.get(k, 0) - y.get(k, 0)) == 0 for k in set(x) | set(y))


def tower(p, q):
    """The causal tower R^(p,q): e_t is the generator of the minority sign, e_a a space direction."""
    assert min(p, q) == 1
    sq = GA.sig(p, q)
    n = p + q
    t = 0 if p == 1 else p
    a = 1 if t == 0 else 0
    assert sq[t] * sq[a] == -1
    blades = GA.all_blades(n)
    et = GA.gen(t)
    f = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(et, GA.gen(a), sq)))
    assert GA.eq(GA.mul(f, f, sq), f)
    basis, vecs = [], []
    for b in blades:
        if len(b) % 2 == 0:
            x = GA.mul({b: F(1)}, f, sq)
            v = [x.get(c, F(0)) for c in blades]
            if GA.rank_of_vectors(vecs + [v]) > len(vecs):
                vecs.append(v)
                basis.append(x)
    return dict(p=p, q=q, n=n, sq=sq, t=t, et=et, f=f, blades=blades, basis=basis, vecs=vecs,
                I={tuple(range(n)): F(1)})


def coords(x, T):
    """Coordinates of x in the basis of S (exact elimination); raises if x is not in S."""
    cols, blades = T['vecs'], T['blades']
    m = len(cols)
    A = [[cols[c][i] for c in range(m)] + [x.get(blades[i], F(0))] for i in range(len(blades))]
    r, piv = 0, []
    for c in range(m):
        pr = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        A[r] = [v / A[r][c] for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                A[i] = [u - A[i][c] * v for u, v in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    assert r == m and all(A[i][m] == 0 for i in range(r, len(A)))
    out = [F(0)] * m
    for i, c in enumerate(piv):
        out[c] = A[i][m]
    return out


def j_bilinear(T, x, y):
    """The symmetric bilinear map whose diagonal is j: the vector part of (x e_t rev(y) + y e_t rev(x))/2."""
    sq, et = T['sq'], T['et']
    z = GA.add(GA.mul(GA.mul(x, et, sq), GA.reverse(y), sq), GA.mul(GA.mul(y, et, sq), GA.reverse(x), sq))
    return [F(1, 2) * z.get((k,), F(0)) for k in range(T['n'])]


def covariance_system(T, copies, vector_valued):
    """Rows of the covariance equations for symmetric bilinear maps on (copies of S), with values in V
    (vector_valued) or in the scalars. Returns (rows, number of unknowns, index function)."""
    sq, n, basis = T['sq'], T['n'], T['basis']
    d1 = len(basis)
    d = d1 * copies
    bivectors = [{b: F(1)} for b in T['blades'] if len(b) == 2]
    left = []
    for B in bivectors:
        one = [coords(GA.mul(B, e, sq), T) for e in basis]
        cols = []
        for c in range(copies):
            for i in range(d1):
                col = [F(0)] * d
                for l in range(d1):
                    col[c * d1 + l] = one[i][l]
                cols.append(col)
        left.append(cols)
    ad = []
    for B in bivectors:
        cols = []
        for m in range(n):
            c = GA.sub(GA.mul(GA.gen(m), B, sq), GA.mul(B, GA.gen(m), sq))
            assert all(len(b) == 1 for b in c)
            cols.append([c.get((k,), F(0)) for k in range(n)])
        ad.append(cols)
    pairs = [(i, k) for i in range(d) for k in range(i, d)]
    index = {pr: x for x, pr in enumerate(pairs)}
    width = n if vector_valued else 1

    def P(i, k):
        return index[(i, k) if i <= k else (k, i)]

    rows = []
    for bi in range(len(bivectors)):
        for (i, k) in pairs:
            for comp in range(width):
                row = [F(0)] * (len(pairs) * width)
                for l in range(d):
                    if left[bi][i][l] != 0:
                        row[P(l, k) * width + comp] += left[bi][i][l]
                    if left[bi][k][l] != 0:
                        row[P(i, l) * width + comp] += left[bi][k][l]
                if vector_valued:
                    for m in range(n):
                        if ad[bi][m][comp] != 0:
                            row[P(i, k) * width + m] -= ad[bi][m][comp]
                if any(row):
                    rows.append(row)
    return rows, len(pairs) * width, pairs


def solution_dimension(rows, unknowns):
    return unknowns - (GA.mat_rank(rows) if rows else 0)


def satisfies(rows, x):
    return all(sum((r[i] * x[i] for i in range(len(x)) if r[i] != 0), F(0)) == 0 for r in rows)


def symbolic_spinor(T, offset=0, nvars=None):
    d = len(T['basis'])
    nvars = nvars or d
    out = {}
    for i, b in enumerate(T['basis']):
        a = Poly.var(offset + i, nvars)
        for k, v in b.items():
            out[k] = out.get(k, F(0)) + a * v
    return {k: v for k, v in out.items() if v != 0}


def bilinear_y(T, psi):
    sq = T['sq']
    return GA.mul(GA.mul(psi, T['et'], sq), GA.reverse(psi), sq)


def check_one_spin_covariant_quadratic_vector_in_each_causal_tower():
    """In the six causal towers of dimension 3, 4 and 5 the spinor ideal has real dimension 2, 4, 8 and the
    spin-covariant symmetric bilinear maps S x S -> V form a space of dimension exactly 1, which the
    polarisation of j spans (j is covariant and not zero)."""
    premise("dark-tower-matter.constituents-field")
    for (p, q, dim_s, dim_maps) in [(2, 1, 2, 1), (1, 2, 2, 1), (1, 3, 4, 1), (3, 1, 4, 1), (4, 1, 8, 1),
                                    (1, 4, 8, 1)]:
        T = tower(p, q)
        assert len(T['basis']) == dim_s
        rows, unknowns, pairs = covariance_system(T, 1, True)
        assert unknowns == dim_s * (dim_s + 1) * (p + q) // 2
        assert solution_dimension(rows, unknowns) == dim_maps
        jvec = []
        for (i, k) in pairs:
            jvec.extend(j_bilinear(T, T['basis'][i], T['basis'][k]))
        assert any(c != 0 for c in jvec)
        assert satisfies(rows, jvec)
    GA.check("one spin-covariant quadratic vector on S in each causal tower, spanned by j", True)


def check_vector_projection_is_vacuous_in_three_and_four_dimensions_and_not_in_five():
    """psi e_t rev(psi) for symbolic psi in S: grade 1 only in dimensions 3 and 4, grades 1 and 5 in
    dimension 5 (the grade-5 coefficient is not the zero polynomial)."""
    premise("dark-tower-matter.constituents-field")
    for (p, q, top) in [(2, 1, 1), (1, 2, 1), (1, 3, 1), (3, 1, 1), (4, 1, 5), (1, 4, 5)]:
        T = tower(p, q)
        y = bilinear_y(T, symbolic_spinor(T))
        grades = sorted({len(b) for b, c in y.items() if c != 0})
        assert grades == sorted({1, top})
        assert any(c != 0 for b, c in y.items() if len(b) == 1)
    GA.check("the projection in j is vacuous in dimensions 3 and 4; in dimension 5 it drops a central part", True)


def check_five_dimensional_mass_is_the_square_of_the_dropped_central_part():
    """Dimension 5, symbolic psi: psi e_t rev(psi) = j + s I with I the central pseudoscalar;
    (j + s I)^2 = 2 s I (j + s I); m^2(j) = Q(e_t) Q(j) = s^2; and 2 s^2 = <x x^dag>_0 for
    x = rev(psi) psi, the stored single-constituent law. Q(e_t) I^2 = 1 in both towers."""
    premise("dark-tower-matter.where-mass-begins")
    for (p, q) in [(4, 1), (1, 4)]:
        T = tower(p, q)
        sq, et, I, n = T['sq'], T['et'], T['I'], T['n']
        assert n == 5
        Qt = sq[T['t']]
        assert Qt * GA.mul(I, I, sq)[()] == 1
        for g in range(n):
            assert GA.commutes(I, GA.gen(g), sq)
        psi = symbolic_spinor(T)
        y = bilinear_y(T, psi)
        s = y[tuple(range(n))]
        jv = {b: c for b, c in y.items() if len(b) == 1}
        assert s != 0
        lhs = GA.mul(y, y, sq)
        rhs = GA.mul({tuple(range(n)): 2 * s}, y, sq)
        assert mv_eq(lhs, rhs)
        Qj = GA.mul(jv, jv, sq)
        assert set(Qj) <= {()}
        assert Qt * Qj[()] == s * s
        x = GA.mul(GA.reverse(psi), psi, sq)
        xdag = GA.mul(GA.mul(et, GA.reverse(x), sq), GA.scal(F(1, Qt), et), sq)
        assert GA.mul(x, xdag, sq)[()] == 2 * s * s
    GA.check("in dimension 5 the mass of one constituent is the square of the central part j drops", True)


def check_invariant_quadratic_scalars_none_in_three_and_four_dimensions_one_in_five():
    """Spin-invariant symmetric bilinear forms S x S -> R: none in dimensions 3 and 4, a line in dimension 5,
    spanned by the polarisation of s (checked through the covariance equations on rational spinors)."""
    premise("dark-tower-matter.where-mass-begins")
    for (p, q, dim_forms) in [(2, 1, 0), (1, 2, 0), (1, 3, 0), (3, 1, 0), (4, 1, 1), (1, 4, 1)]:
        T = tower(p, q)
        rows, unknowns, pairs = covariance_system(T, 1, False)
        assert solution_dimension(rows, unknowns) == dim_forms
        if dim_forms:
            sq, et, top = T['sq'], T['et'], tuple(range(T['n']))
            svec = []
            for (i, k) in pairs:
                x, w = T['basis'][i], T['basis'][k]
                z = GA.add(GA.mul(GA.mul(x, et, sq), GA.reverse(w), sq),
                           GA.mul(GA.mul(w, et, sq), GA.reverse(x), sq))
                svec.append(F(1, 2) * z.get(top, F(0)))
            assert any(c != 0 for c in svec)
            assert satisfies(rows, svec)
    GA.check("invariant quadratic scalars on S: none in dimensions 3 and 4, the line of s in dimension 5", True)


def check_two_constituents_admit_cross_terms_so_additivity_is_not_forced():
    """On S + S (two constituents) the spin-covariant quadratic vectors form a space of dimension 3 in the
    three-dimensional towers and 4 in the four-dimensional ones, larger than the 2 spanned by the two single
    momenta; the sum j(psi_1) + j(psi_2) is one point of it."""
    premise("dark-tower-matter.where-mass-begins")
    for (p, q, dim_maps) in [(2, 1, 3), (1, 2, 3), (1, 3, 4), (3, 1, 4)]:
        T = tower(p, q)
        d1 = len(T['basis'])
        rows, unknowns, pairs = covariance_system(T, 2, True)
        assert solution_dimension(rows, unknowns) == dim_maps
        assert dim_maps > 2
        total = []
        for (i, k) in pairs:
            if i // d1 == k // d1:
                total.extend(j_bilinear(T, T['basis'][i % d1], T['basis'][k % d1]))
            else:
                total.extend([F(0)] * T['n'])
        assert any(c != 0 for c in total)
        assert satisfies(rows, total)
    GA.check("two constituents: cross terms are covariant too; the total momentum is one choice among them", True)
