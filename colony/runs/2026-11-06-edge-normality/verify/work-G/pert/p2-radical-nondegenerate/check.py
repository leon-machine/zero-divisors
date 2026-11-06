"""synthesis.hyperbolic-plane-integral-orders-and-partner-inverse: exact checks.

Cl(1,1) with e_+ = gen 0 (square +1), e_- = gen 1 (square -1); Witt pair a = (e_+ + e_-)/2,
a' = (e_+ - e_-)/2. Z-spans are handled through exact coordinates in the basis
(1, a, a', a a') of the Witt order. Everything is exact (Fractions in GA.py).
(1) The Witt order: a^2 = a'^2 = 0, a a' + a' a = 1; the Z-span of 1, a, a', a a' is closed
    under products with integer structure constants, and x -> [[<x,aa'>, <x,a>], [<x,a'>, <x,a'a>]]
    is multiplicative on it (a ring isomorphism onto 2 x 2 integer matrices), with integral
    orthogonal idempotents a a', a' a summing to 1.
(2) The orthogonal order: the Z-span of 1, e_+, e_-, e_+ e_- is closed, lies in the Witt order with
    index 4 (change-of-basis determinant), contains twice the Witt order, and contains no
    idempotent but 0 and 1 (every element has integer scalar part, while an idempotent of Cl(1,1)
    other than 0, 1 has scalar part 1/2; brute force over a box as a control); the lattices
    Z a + Z a' (polar form of Q unimodular, Q(x a + y a') = x y) and Z e_+ + Z e_- (B unimodular,
    Q odd).
(3) The partner as generalised inverse: n m n = n, m n m = m for Witt pairs in Cl(1,1), Cl(2,2),
    Cl(1,3) (real null pairs), self-adjointness of n m, m n for the adjoint exchanging a and a'.
(4) The derivative: m (f(x + n) - f(x)) = f'(x) m n for f = 2x^3 + 5x and for
    g = (x^3 + 3x)/(x^2 + 1) at several rational x.
(5) A radical vector rho of Cl(p,q,r) has rho x rho = 0 for every blade x: no generalised inverse;
    the embedding rho -> a of Cl(0,0,1) in Cl(1,1) respects the relation.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

S11 = GA.sig(1, 1)
ONE = GA.sc(1)
EP, EM = GA.gen(0), GA.gen(1)
A = GA.scal(F(1, 2), GA.add(EP, EM))
AP = GA.scal(F(1, 2), GA.sub(EP, EM))


def m11(x, y):
    return GA.mul(x, y, S11)


AAP = m11(A, AP)
APA = m11(AP, A)
WBASIS = [ONE, A, AP, AAP]
BLADES = [(), (0,), (1,), (0, 1)]


def coords(x, basis):
    """Exact coordinates of x in a basis of Cl(1,1) (4 x 4 solve)."""
    M = [[b.get(bl, F(0)) for b in basis] for bl in BLADES]
    rhs = [x.get(bl, F(0)) for bl in BLADES]
    return GA.field_solve(M, rhs)


def to_matrix(x):
    """[[alpha, beta], [gamma, delta]] for x = alpha a a' + beta a + gamma a' + delta a' a."""
    c1, ca, cap, caap = coords(x, WBASIS)       # x = c1 + ca a + cap a' + caap a a'
    # 1 = a a' + a' a
    return [[c1 + caap, ca], [cap, c1]]


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def is_int(v):
    return all(F(c).denominator == 1 for c in v)


def det(M):
    n = len(M)
    M = [list(r) for r in M]
    d = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [M[r][k] - f * M[c][k] for k in range(n)]
    return d


def check_witt_order_is_the_integer_matrices():
    premise("std-algebra.witt-basis-car")
    premise("std-algebra.cl11-matrix")
    assert GA.is_zero(m11(A, A)) and GA.is_zero(m11(AP, AP))
    assert GA.eq(GA.add(AAP, APA), ONE)
    for x in WBASIS:
        for y in WBASIS:
            assert is_int(coords(m11(x, y), WBASIS))
            assert matmul(to_matrix(x), to_matrix(y)) == to_matrix(m11(x, y))
    assert to_matrix(A) == [[0, 1], [0, 0]] and to_matrix(AP) == [[0, 0], [1, 0]]
    assert to_matrix(AAP) == [[1, 0], [0, 0]] and to_matrix(APA) == [[0, 0], [0, 1]]
    assert GA.eq(m11(AAP, AAP), AAP) and GA.eq(m11(APA, APA), APA)
    assert GA.is_zero(m11(AAP, APA)) and GA.is_zero(m11(APA, AAP))
    return True


def check_orthogonal_order_has_index_four_and_no_idempotents():
    premise("one-relation.two-presentations")
    obasis = [ONE, EP, EM, m11(EP, EM)]
    for x in obasis:
        for y in obasis:
            assert is_int(coords(m11(x, y), obasis))
    change = [coords(x, WBASIS) for x in obasis]
    assert all(is_int(r) for r in change)
    assert abs(det(change)) == 4
    for w in WBASIS:
        assert is_int(coords(GA.scal(2, w), obasis))
    assert not is_int(coords(A, obasis))
    # idempotents of Cl(1,1) other than 0, 1 have scalar part 1/2: x^2 - x for x = s + rest
    for s, b, c, d in product(range(-3, 4), repeat=4):
        x = GA.add(GA.sc(s), GA.scal(b, EP), GA.scal(c, EM), GA.scal(d, obasis[3]))
        idem = GA.eq(m11(x, x), x)
        assert idem == (GA.is_zero(x) or GA.eq(x, ONE))
    found = 0
    for s, b, c, d in product(range(-1, 2), repeat=4):
        x = GA.add(GA.scal(s, ONE), GA.scal(b, A), GA.scal(c, AP), GA.scal(d, AAP))
        if GA.eq(m11(x, x), x) and not GA.is_zero(x) and not GA.eq(x, ONE):
            found += 1
            assert x.get((), F(0)) == F(1, 2)
    assert found == 10
    # the lattices: Q(x a + y a') = x y (polar form of Q unimodular), Q(x e+ + y e-) = x^2 - y^2
    for x, y in product(range(-2, 3), repeat=2):
        v = GA.add(GA.scal(x, A), GA.scal(y, AP))
        assert m11(v, v) == GA.sc(x * y)
        w = GA.add(GA.scal(x, EP), GA.scal(y, EM))
        assert m11(w, w) == GA.sc(x * x - y * y)
    return True


def witt_pairs():
    out = [(S11, A, AP)]
    for p, q in ((2, 2), (1, 3)):
        S = GA.sig(p, q)
        # the real null pair on the plane of generators 0 (square +1) and p (square -1)
        n = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(p)))
        m = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(p)))
        out.append((S, n, m))
    return out


def adjoint(x):
    """Reversion composed with e_- -> -e_-: exchanges a and a'."""
    flip = {b: (c if (1 not in b) else -c) for b, c in x.items()}
    return GA.reverse(flip)


def check_partner_is_a_generalised_inverse():
    premise("std-algebra.witt-basis-car")
    premise("transport.regularity-localises-zero-divisors-idempotents")
    count = 0
    for S, n, m in witt_pairs():
        assert GA.is_zero(GA.mul(n, n, S)) and GA.is_zero(GA.mul(m, m, S))
        assert GA.eq(GA.add(GA.mul(n, m, S), GA.mul(m, n, S)), GA.sc(1))
        assert GA.eq(GA.mul(GA.mul(n, m, S), n, S), n)
        assert GA.eq(GA.mul(GA.mul(m, n, S), m, S), m)
        P = GA.mul(m, n, S)
        assert GA.eq(GA.mul(P, P, S), P)
        count += 1
    assert count == 3
    assert GA.eq(adjoint(A), AP) and GA.eq(adjoint(AP), A)
    for x in WBASIS:
        for y in WBASIS:
            assert GA.eq(adjoint(m11(x, y)), m11(adjoint(y), adjoint(x)))
    assert GA.eq(adjoint(AAP), AAP) and GA.eq(adjoint(APA), APA)
    return True


def poly_at(coeffs, x, n, S):
    """f(x + n) for f = sum coeffs[k] t^k, x a scalar, n in the algebra."""
    base = GA.add(GA.sc(x), n) if x != 0 else dict(n)
    out, pw = {}, ONE
    for c in coeffs:
        out = GA.add(out, GA.scal(c, pw))
        pw = GA.mul(pw, base, S)
    return out


def peval(coeffs, x):
    return sum(F(c) * F(x) ** k for k, c in enumerate(coeffs))


def pder(coeffs):
    return [k * c for k, c in enumerate(coeffs)][1:]


def check_derivative_through_the_partner():
    premise("std-algebra.witt-basis-car")
    f = [0, 5, 0, 2]                    # 2 x^3 + 5 x
    P = m11(AP, A)
    # (x, f(x), f'(x)) stated by hand: f' = 6 x^2 + 5
    for x, fx, dfx in ((0, 0, 5), (1, 7, 11), (-2, -26, 29), (5, 275, 155), (F(3, 7), F(789, 343), F(299, 49))):
        x = F(x)
        assert peval(f, x) == fx and peval(pder(f), x) == dfx
        fxn = poly_at(f, x, A, S11)
        assert GA.eq(fxn, GA.add(GA.sc(fx), GA.scal(dfx, A)))
        dq = m11(AP, GA.sub(fxn, GA.sc(fx)))
        assert GA.eq(dq, GA.scal(dfx, P))
        if x.denominator == 1:
            assert is_int(coords(fxn, WBASIS)) and is_int(coords(dq, WBASIS))
    num, den = [0, 3, 0, 1], [1, 0, 1]   # (x^3 + 3x) / (x^2 + 1)
    # (x, g(x), g'(x)) stated by hand: g' = (x^4 + 3) / (x^2 + 1)^2
    for x, gx, dgx in ((0, 0, 3), (2, F(14, 5), F(19, 25)), (F(-1, 3), F(-14, 15), F(61, 25))):
        x = F(x)
        h = poly_at(den, x, A, S11)
        hx, dhx = peval(den, x), peval(pder(den), x)
        hinv = GA.sub(GA.sc(1 / hx), GA.scal(dhx / (hx * hx), A))
        assert GA.eq(m11(h, hinv), ONE)
        g = m11(poly_at(num, x, A, S11), hinv)
        assert GA.eq(g, GA.add(GA.sc(gx), GA.scal(dgx, A)))
        assert GA.eq(m11(AP, GA.sub(g, GA.sc(gx))), GA.scal(dgx, P))
    return True


def check_radical_vector_has_no_generalised_inverse():
    premise("std-algebra.radical-ideal-and-quotient")
    premise("conformal.minimal-nondegenerate-completion")
    count = 0
    for p, q, r in ((0, 0, 1), (1, 1, 1), (1, 2, 1), (0, 0, 2), (1, 3, 1)):
        S = GA.sig(p, q + r)
        nn = p + q + r
        for k in range(p + q, nn):
            rho = GA.gen(k)
            for bl in GA.all_blades(nn):
                assert GA.is_zero(GA.mul(GA.mul(rho, {bl: F(1)}, S), rho, S))
            count += 1
    assert count == 6
    # rho -> a respects rho^2 = 0, and the image has the partner a'
    D = GA.sig(0, 0, 1)
    rho = GA.gen(0)
    assert GA.is_zero(GA.mul(rho, rho, D)) and GA.is_zero(m11(A, A))
    assert GA.eq(m11(m11(A, AP), A), A)
    return True
