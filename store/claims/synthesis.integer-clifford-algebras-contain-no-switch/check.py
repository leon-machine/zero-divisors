"""synthesis.integer-clifford-algebras-contain-no-switch: exact checks.

Cl_Z(p,q) is computed with GA.py (Fraction coefficients; integer inputs stay integral). The
idempotent and switch searches are over boxes of integer coefficients and support the proof; the
mod-2 identities of the proof are checked exhaustively for n <= 3.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA


def M(a, b, c, d):
    return ((F(a), F(b)), (F(c), F(d)))


def mm(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)) for i in range(n))


def ma(A, B):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(A, B))


def ms(c, A):
    return tuple(tuple(F(c) * x for x in r) for r in A)


def flat(A):
    return [x for r in A for x in r]


I2, Z2 = M(1, 0, 0, 1), M(0, 0, 0, 0)
# states: s_off = (1,0)^T, s_on = (0,1)^T
V = M(0, 0, 1, 0)      # set:   off -> on, on -> 0
W = M(0, 1, 0, 0)      # clear: on -> off, off -> 0
VW, WV = mm(V, W), mm(W, V)


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv(A):
    d = det(A)
    return ms(1 / d, ((A[1][1], -A[0][1]), (-A[1][0], A[0][0])))


def is_scalar(A):
    return A[0][1] == 0 and A[1][0] == 0 and A[0][0] == A[1][1]


def box_elements(n, lo, hi):
    blades = GA.all_blades(n)
    for cs in product(range(lo, hi + 1), repeat=len(blades)):
        yield {b: F(c) for b, c in zip(blades, cs) if c}


DIMS = (1, 2, 3)
IDEMPOTENT_BOXES = ((1, -4, 4), (2, -2, 2), (3, -1, 1))        # (n, least coefficient, greatest)
PLANES = (GA.sig(1, 1), GA.sig(2, 0), GA.sig(0, 2))
NIL_BOX = (-3, 3)
MIXED = ((1, 1), (2, 1), (1, 2), (2, 2), (3, 1), (1, 3))


def signatures(n):
    return [GA.sig(p, n - p) for p in range(n + 1)]


def check_reduction_mod_two_is_the_commutative_group_algebra():
    pairs = 0
    for n in DIMS:
        blades = GA.all_blades(n)
        for sq in signatures(n):
            for b1 in blades:
                for b2 in blades:
                    s1, r1 = GA.blade_mul(b1, b2, sq)
                    s2, r2 = GA.blade_mul(b2, b1, sq)
                    assert r1 == r2 == tuple(sorted(set(b1) ^ set(b2)))
                    assert s1 * s1 == 1 and s2 * s2 == 1
                    pairs += 1
    # hand count: (n + 1) signatures times 4^n pairs of blades: 2*4 + 3*16 + 4*64
    assert pairs == 312
    return True


def check_square_is_the_coefficient_sum_mod_two():
    total = 0
    for n in (1, 2, 3):
        blades = GA.all_blades(n)
        for coeffs in product((0, 1), repeat=len(blades)):
            acc = {}
            for i, ci in enumerate(coeffs):
                for j, cj in enumerate(coeffs):
                    if ci and cj:
                        r = tuple(sorted(set(blades[i]) ^ set(blades[j])))
                        acc[r] = (acc.get(r, 0) + 1) % 2
            assert {k: x for k, x in acc.items() if x} == ({(): 1} if sum(coeffs) % 2 else {})
            total += 1
    assert total == 2 ** 2 + 2 ** 4 + 2 ** 8
    return True


def check_no_integral_idempotents_on_boxes():
    searched = 0
    for n, lo, hi in IDEMPOTENT_BOXES:
        for sq in signatures(n):
            found = []
            for x in box_elements(n, lo, hi):
                searched += 1
                if GA.eq(GA.mul(x, x, sq), x):
                    found.append(x)
            assert len(found) == 2 and {} in found and any(GA.eq(x, GA.sc(1)) for x in found)
    # hand count: 2 * 9^2 + 3 * 5^4 + 4 * 3^8 elements
    assert searched == 162 + 1875 + 26244
    return True


def nilpotents(sq):
    return [x for x in box_elements(2, NIL_BOX[0], NIL_BOX[1]) if x and GA.is_zero(GA.mul(x, x, sq))]


def check_no_integral_switch_on_boxes():
    counts = []
    for sq in PLANES:
        nil = nilpotents(sq)
        counts.append(len(nil))
        scalars = set()
        for a in nil:
            for b in nil:
                anti = GA.add(GA.mul(a, b, sq), GA.mul(b, a, sq))
                assert all(c % 2 == 0 for c in anti.values())      # anticommutators are even
                if set(anti) <= {()}:
                    scalars.add(anti.get((), F(0)))
        assert 1 not in scalars
        if nil:
            assert 2 in scalars or -2 in scalars                   # the least nonzero value is attained
    assert counts == [24, 24, 0]      # Cl(1,1), Cl(2,0); the quaternions Cl(0,2) have none
    return True


def check_half_vectors_are_a_switch():
    h = F(1, 2)
    for p, q in MIXED:
        sq = GA.sig(p, q)
        a = GA.scal(h, GA.add(GA.gen(0), GA.gen(p)))
        b = GA.scal(h, GA.sub(GA.gen(0), GA.gen(p)))
        assert GA.is_zero(GA.mul(a, a, sq)) and GA.is_zero(GA.mul(b, b, sq))
        assert GA.eq(GA.add(GA.mul(a, b, sq), GA.mul(b, a, sq)), GA.sc(1))
    return True


def check_orthonormal_order_has_index_four_in_the_switch_order():
    ep, em = ma(V, W), ma(V, ms(-1, W))
    images = (I2, ep, em, mm(ep, em))
    blades = GA.all_blades(2)
    s11 = GA.sig(1, 1)

    def image(x):
        X = Z2
        for b, r in zip(blades, images):
            X = ma(X, ms(x.get(b, 0), r))
        return X
    # determinant of the coordinate map: index 4
    rows = [flat(r) for r in images]
    m = [list(r) for r in rows]
    d = F(1)
    for c in range(4):
        p = next(r for r in range(c, 4) if m[r][c] != 0)
        if p != c:
            m[c], m[p] = m[p], m[c]
            d = -d
        d *= m[c][c]
        for r in range(c + 1, 4):
            f = m[r][c] / m[c][c]
            m[r] = [a - f * b for a, b in zip(m[r], m[c])]
    assert abs(d) == 4
    samples = [{b: F(c) for b, c in zip(blades, cs) if c} for cs in ((1, 2, -1, 0), (0, 1, 1, 1), (3, 0, -2, 1))]
    for x in box_elements(2, -2, 2):
        X = image(x)
        assert (X[0][0] - X[1][1]) % 2 == 0 and (X[0][1] - X[1][0]) % 2 == 0
        for y in samples:
            assert image(GA.mul(x, y, s11)) == mm(X, image(y))
    for a, b, c, dd in product(range(-2, 3), repeat=4):          # every matrix of the parity lattice is hit
        if (a - dd) % 2 == 0 and (b - c) % 2 == 0:
            x = {(): F(a + dd, 2), (0,): F(b + c, 2), (1,): F(c - b, 2), (0, 1): F(a - dd, 2)}
            assert all(t.denominator == 1 for t in x.values())
            assert image(x) == M(a, b, c, dd)
    return True
