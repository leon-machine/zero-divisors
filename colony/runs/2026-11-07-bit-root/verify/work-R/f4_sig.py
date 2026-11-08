"""synthesis.frobenius-and-universality-in-clifford-algebras: exact checks.

All algebra is done with GA.py over Fractions; polynomials with coefficients in Cl(0,1) are lists of
GA elements (index = degree).
(1) Real polynomials in Cl(0,1): square roots in Cl(0,1) by the explicit formula (exact on squares of
    rational elements); the Cauchy bound M = 1 + sum |c_i| brackets a sign change of odd-degree
    polynomials; the Laplace step: for p = (X^2 + 1)(X^2 + 4), whose roots e, -e, 2e, -2e lie in
    Cl(0,1), the polynomial prod_{i<j} (X - (r_i + r_j + t r_i r_j)) has real coefficients for several
    t, equal for t = 0 to the hand value X^6 + 10X^4 + 9X^2.
(2) The pure part: in Cl(0,1) and Cl(0,2) an element x = a + v squares to a real number exactly when
    a = 0 or v = 0, and x^2 - 2a x + (a^2 - v^2) = 0 with v^2 = -(sum of squares).
(3) The bivector argument: in Cl(0,k), k = 2, 3, 4, u = e1e2 has u^2 = -1, anticommutes with e1 and e2,
    commutes with e_j (j >= 3), and (u e_j)^2 = +1, so (1 - u e_j)(1 + u e_j) = 0; e1, e2, e1e2 satisfy
    the relations of three anticommuting vectors of square -1 (the quotient of Cl(0,3) by e3 = e1e2 is
    Cl(0,2)); e1e2 leaves span{1, e1, e2}; dimensions 1, 2, 4 of the three division algebras.
(4) Universality: the elements E_{I,J} = w_I f v_J^rev of Cl(k,k), f = v1 w1 ... vk wk, are matrix units
    (k = 1, 2, 3); the regular representations of the dual numbers, the split-complex numbers, the
    upper triangular 2 x 2 matrices, R[x]/(x^3) and the quaternions Cl(0,2) map through them to
    injective homomorphisms into Cl(k,k) with an idempotent image of the unit.
(5) The number systems inside: Cl(1,0) splits by (1 +- e1)/2; a null vector of Cl(1,1) spans the dual
    numbers; Cl(0,1) and Cl(0,2) have x xbar = sum of squares.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise

S01 = GA.sig(0, 1)
E = GA.gen(0)


# ---- polynomials over Cl(0,1) -------------------------------------------------------------

def c(a, b=0):
    return GA.add(GA.sc(a), GA.scal(b, E))


def pmul(P, Q):
    out = [{} for _ in range(len(P) + len(Q) - 1)]
    for i, x in enumerate(P):
        for j, y in enumerate(Q):
            out[i + j] = GA.add(out[i + j], GA.mul(x, y, S01))
    return out


def linear(root):
    return [GA.neg(root), GA.sc(1)]


def isqrt_frac(x):
    x = F(x)
    assert x >= 0
    def isq(m):
        lo, hi = 0, m + 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if mid * mid <= m:
                lo = mid
            else:
                hi = mid
        return lo
    n, d = isq(x.numerator), isq(x.denominator)
    assert n * n == x.numerator and d * d == x.denominator
    return F(n, d)


SQRT_INPUTS = ((3, 4), (F(1, 2), -2), (-5, 1), (0, 3), (2, 0), (F(-7, 3), F(5, 6)))
ODD_POLYS = ((-3, 1, 0, 1), (5, -2, 7, -1, 0, 1), (0, 0, -9, 1))
LAPLACE_ROOTS = ((0, 1), (0, -1), (0, 2), (0, -2))
LAPLACE_T = (0, 1, 2, -3, F(1, 2))


def check_real_polynomials_have_roots_in_the_plane_algebra():
    premise("std-algebra.complex-numbers")
    # square roots in Cl(0,1): z = a + b e, r = sqrt(a^2 + b^2), X = sqrt((r + a)/2), Y = sgn(b) sqrt((r - a)/2)
    found = []
    for x0, y0 in SQRT_INPUTS:
        z = GA.mul(c(x0, y0), c(x0, y0), S01)
        a, b = z.get((), F(0)), z.get((0,), F(0))
        r = isqrt_frac(a * a + b * b)
        X = isqrt_frac((r + a) / 2)
        Y = isqrt_frac((r - a) / 2) * (1 if b >= 0 else -1)
        w = c(X, Y)
        assert GA.mul(w, w, S01) == z
        found.append((X, Y))
    # the formula returns the root with nonnegative real part (hand values)
    assert found == [(3, 4), (F(1, 2), -2), (5, -1), (0, 3), (2, 0), (F(7, 3), F(-5, 6))]
    assert GA.mul(c(3, 4), c(3, 4), S01) == c(-7, 24)
    # odd degree: p(-M) < 0 < p(M) with M = 1 + sum |c_i| (monic)
    Ms = []
    for coeffs in ODD_POLYS:
        M = 1 + sum(abs(x) for x in coeffs[:-1])
        val = lambda t: sum(F(cf) * F(t) ** i for i, cf in enumerate(coeffs))
        assert val(M) > 0 and val(-M) < 0
        Ms.append(M)
    assert Ms == [5, 16, 10]
    # the Laplace step on p = (X^2 + 1)(X^2 + 4)
    roots = [c(x, y) for x, y in LAPLACE_ROOTS]
    p = [GA.sc(1)]
    for r in roots:
        p = pmul(p, linear(r))
    assert p == [GA.sc(4), {}, GA.sc(5), {}, GA.sc(1)]
    for t in LAPLACE_T:
        g = [GA.sc(1)]
        for i, j in combinations(range(len(roots)), 2):
            s = GA.add(roots[i], roots[j], GA.scal(t, GA.mul(roots[i], roots[j], S01)))
            g = pmul(g, linear(s))
        assert len(g) == 7
        assert all((0,) not in coef for coef in g)
        if t == 0:
            assert g == [{}, {}, GA.sc(9), {}, GA.sc(10), {}, GA.sc(1)]
        if t == 1:
            # values r_i + r_j + r_i r_j: 1, -2 + 3e, 2 - e, 2 + e, -2 - 3e, 4; the constant term is
            # their product (six factors): 1 * 4 * (4 + 9) * (4 + 1)
            assert g[0] == GA.sc(4 * (4 + 9) * (4 + 1))
    return True


def check_pure_part_and_minimal_polynomial():
    premise("std-algebra.quaternions")
    for k in (1, 2):
        sq = GA.sig(0, k)
        bl = GA.all_blades(k)
        for cs in product((-2, 0, 1, 3), repeat=2 ** k):
            x = {S: F(v) for S, v in zip(bl, cs) if v != 0}
            a = F(cs[0])
            v = GA.sub(x, GA.sc(a))
            x2 = GA.mul(x, x, sq)
            v2 = GA.mul(v, v, sq)
            assert v2 == GA.sc(-sum(t * t for t in cs[1:]))
            real_square = all(len(b) == 0 for b in x2)
            assert real_square == (a == 0 or not v)
            lhs = GA.add(x2, GA.scal(-2 * a, x), GA.sc(a * a - v2.get((), F(0))))
            assert lhs == {}
    return True


def check_the_bivector_bounds_the_dimension():
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.blade-basis")
    premise("transport.exceptional-division-algebras")
    for k in (2, 3, 4):
        sq = GA.sig(0, k)
        e = [GA.gen(i) for i in range(k)]
        u = GA.mul(e[0], e[1], sq)
        assert GA.mul(u, u, sq) == GA.sc(-1)
        assert GA.anticommutes(u, e[0], sq) and GA.anticommutes(u, e[1], sq)
        for j in range(2, k):
            assert GA.commutes(u, e[j], sq)
            w = GA.mul(u, e[j], sq)
            assert GA.mul(w, w, sq) == GA.sc(1)
            assert GA.mul(GA.sub(GA.sc(1), w), GA.add(GA.sc(1), w), sq) == {}
    # in Cl(0,2): e1, e2, e1e2 satisfy the relations of Cl(0,3) generators (e3 -> e1e2)
    sq = GA.sig(1, 1)
    g = [GA.gen(0), GA.gen(1), GA.mul(GA.gen(0), GA.gen(1), sq)]
    for i in range(3):
        assert GA.mul(g[i], g[i], sq) == GA.sc(-1)
        for j in range(i + 1, 3):
            assert GA.anticommutes(g[i], g[j], sq)
    # e1e2 is not in span{1, e1, e2}: a three-dimensional R + V is not closed
    assert set(GA.mul(GA.gen(0), GA.gen(1), sq)) == {(0, 1)}
    # dimensions of the division algebras: 2^0, 2^1, 2^2 blades
    assert [len(GA.all_blades(k)) for k in (0, 1, 2)] == [1, 2, 4]
    return True


# ---- matrix units of Cl(k,k) and the regular representation ---------------------------------

def witt(k):
    sq = GA.sig(k, k)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(k + i))) for i in range(k)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(k + i))) for i in range(k)]
    return sq, v, w


def prod_(xs, sq):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def matrix_units(k):
    sq, v, w = witt(k)
    f = prod_([GA.mul(v[i], w[i], sq) for i in range(k)], sq)
    subsets = [S for m in range(k + 1) for S in combinations(range(k), m)]
    Eu = {}
    for I in subsets:
        for J in subsets:
            Eu[I, J] = prod_([w[i] for i in I] + [f] + [v[j] for j in reversed(J)], sq)
    return sq, subsets, Eu


def regular_rep(struct, d):
    """struct[i][j] = coefficient list of b_i b_j; L(b_i)_{s t} = coefficient of b_s in b_i b_t."""
    return [[[struct[i][t][s] for t in range(d)] for s in range(d)] for i in range(d)]


def mat_prod(A, B):
    n = len(A)
    return [[sum(A[i][l] * B[l][j] for l in range(n)) for j in range(n)] for i in range(n)]


def algebras():
    out = {}
    # dual numbers span{1, x}, x^2 = 0
    out["dual"] = [[[1, 0], [0, 1]], [[0, 1], [0, 0]]]
    # split-complex span{1, j}, j^2 = 1
    out["split"] = [[[1, 0], [0, 1]], [[0, 1], [1, 0]]]
    # R[x]/(x^3): basis 1, x, x^2
    out["truncated"] = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                        [[0, 1, 0], [0, 0, 1], [0, 0, 0]],
                        [[0, 0, 1], [0, 0, 0], [0, 0, 0]]]
    # upper triangular 2 x 2: basis E11, E12, E22 (unit E11 + E22 is not a basis element)
    out["triangular"] = [[[1, 0, 0], [0, 1, 0], [0, 0, 0]],
                         [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
                         [[0, 0, 0], [0, 0, 0], [0, 0, 1]]]
    # quaternions Cl(0,2) from GA: basis 1, e1, e2, e12
    sq = GA.sig(0, 2)
    bl = GA.all_blades(2)
    out["quaternions"] = [[GA.basis_vector_of(GA.mul({a: F(1)}, {b: F(1)}, sq), bl) for b in bl]
                          for a in bl]
    return out


def check_every_algebra_embeds_in_some_cl_kk():
    premise("std-algebra.witt-basis-car")
    premise("std-algebra.fock-representation")
    premise("std-algebra.matrix-units")
    unit_counts = {}
    for k in (1, 2, 3):
        sq, subsets, Eu = matrix_units(k)
        total = {}
        for (I, J), x in Eu.items():
            if I == J:
                total = GA.add(total, x)
        assert total == GA.sc(1)
        if k <= 2:
            for (I, J), x in Eu.items():
                for (K, L), y in Eu.items():
                    want = Eu[I, L] if J == K else {}
                    assert GA.eq(GA.mul(x, y, sq), want)
        unit_counts[k] = len(Eu)
    assert unit_counts == {1: 4, 2: 16, 3: 64}
    dims = {}
    for name, struct in algebras().items():
        d = len(struct)
        k = 1 if d <= 2 else 2
        sq, subsets, Eu = matrix_units(k)
        idx = subsets[:d]
        L = regular_rep(struct, d)
        def phi(M):
            out = {}
            for s in range(d):
                for t in range(d):
                    if M[s][t] != 0:
                        out = GA.add(out, GA.scal(M[s][t], Eu[idx[s], idx[t]]))
            return out
        imgs = [phi(L[i]) for i in range(d)]
        # homomorphism on basis pairs: phi(b_i b_j) = phi(b_i) phi(b_j)
        for i in range(d):
            for j in range(d):
                Lij = [[sum(F(struct[i][j][m]) * L[m][s][t] for m in range(d)) for t in range(d)]
                       for s in range(d)]
                assert Lij == mat_prod(L[i], L[j])
                assert GA.eq(phi(Lij), GA.mul(imgs[i], imgs[j], sq))
        # injective
        big = GA.all_blades(2 * k)
        assert GA.rank_of_vectors([GA.basis_vector_of(x, big) for x in imgs]) == d
        # the image of the unit is the corner idempotent
        one = [[1 if s == t else 0 for t in range(d)] for s in range(d)]
        Eidem = phi(one)
        assert GA.eq(GA.mul(Eidem, Eidem, sq), Eidem)
        for x in imgs:
            assert GA.eq(GA.mul(Eidem, x, sq), x) and GA.eq(GA.mul(x, Eidem, sq), x)
        dims[name] = d
    assert dims == {"dual": 2, "split": 2, "truncated": 3, "triangular": 3, "quaternions": 4}
    return True


def check_the_number_systems_inside():
    premise("std-algebra.complex-numbers")
    premise("std-algebra.quaternions")
    # split-complex: Cl(1,0) = R eps+ + R eps-
    sq = GA.sig(1, 0)
    ep = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.gen(0)))
    em = GA.scal(F(1, 2), GA.sub(GA.sc(1), GA.gen(0)))
    assert GA.mul(ep, ep, sq) == ep and GA.mul(em, em, sq) == em
    assert GA.mul(ep, em, sq) == {} and GA.add(ep, em) == GA.sc(1)
    # dual numbers: a null vector of Cl(1,1)
    sq = GA.sig(1, 1)
    n = GA.add(GA.gen(0), GA.gen(1))
    assert GA.mul(n, n, sq) == {}
    for a, b, c2, d in ((2, 3, -1, 5), (F(1, 2), 0, 4, -7)):
        x = GA.add(GA.sc(a), GA.scal(b, n))
        y = GA.add(GA.sc(c2), GA.scal(d, n))
        assert GA.mul(x, y, sq) == GA.add(GA.sc(a * c2), GA.scal(a * d + b * c2, n))
    # Cl(0,1), Cl(0,2): x xbar = sum of squares
    for k in (1, 2):
        sq = GA.sig(0, k)
        bl = GA.all_blades(k)
        for cs in product((-1, 2, 3), repeat=2 ** k):
            x = {S: F(v) for S, v in zip(bl, cs)}
            xbar = GA.grade_inv(GA.reverse(x))
            assert GA.mul(x, xbar, sq) == GA.sc(sum(v * v for v in cs))
    return True
