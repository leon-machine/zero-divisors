"""synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two: exact checks.

Cl(p,q) on the blades of the generators (p of square +1 first, then q of square -1), rational coefficients.
The dagger is the linear extension of the inverse of a blade: reverse times the product of the squares.
An observable is x with dagger(x) = x and x x = 1. C = A1 B1 + A1 B2 + A2 B1 - A2 B2 with [Ai, Bj] = 0.

(1) the dagger, the positive form and the identity C^2 = 4 - [A1,A2][B1,B2] on observables that are not blades;
(2) the fourteen excluded signatures: the self-adjoint blades are 1, a central J (odd cases) and an anticommuting
    frame (times J), with independent pairwise products, which is all the proof of clause (ii) uses;
(3) every other signature of four, five or six directions carries a configuration of blades with C^2 = 4 + 4K,
    and the functionals <(1 + K)(1 + rC) x>_0 have value 8r on C and 8 on C^2;
(4) the excluded list is the list of matrix size at most two in the stored classification.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

ONE = GA.sc(F(1))


def dsign(b, sq):
    g = len(b)
    s = (-1) ** (g * (g - 1) // 2)
    for i in b:
        s *= sq[i]
    return s


def dagger(x, sq):
    return {b: c * dsign(b, sq) for b, c in x.items()}


def bl(b):
    return {tuple(b): F(1)}


def prod(sq, *xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return r


def comm(x, y, sq):
    return GA.sub(GA.mul(x, y, sq), GA.mul(y, x, sq))


def chsh(sq, a1, a2, b1, b2):
    return GA.add(prod(sq, a1, b1), prod(sq, a1, b2), prod(sq, a2, b1), GA.neg(prod(sq, a2, b2)))


def s0(x):
    return x.get((), F(0))


def self_adjoint_blades(sq):
    n = len(sq)
    blades = [b for k in range(n + 1) for b in combinations(range(n), k)]
    return [b for b in blades if dsign(b, sq) == 1]


def is_central(b, sq):
    return all(GA.commutes(bl(b), GA.gen(i), sq) for i in range(len(sq)))


def check_dagger_is_blade_inverse_and_the_chsh_square_identity():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    for sq in (GA.sig(3, 1), GA.sig(2, 2), GA.sig(4, 0), GA.sig(1, 3)):
        n = len(sq)
        for k in range(n + 1):
            for b in combinations(range(n), k):
                assert prod(sq, bl(b), dagger(bl(b), sq)) == ONE
    sq = GA.sig(3, 1)
    x = GA.add(GA.scal(F(2), bl((0,))), GA.scal(F(-3), bl((1, 3))), GA.scal(F(5), bl((0, 1, 2, 3))), GA.sc(F(7)))
    assert s0(prod(sq, x, dagger(x, sq))) == 4 + 9 + 25 + 49
    y = GA.add(bl((2,)), GA.scal(F(4), bl((0, 3))))
    assert dagger(prod(sq, x, y), sq) == prod(sq, dagger(y, sq), dagger(x, sq))
    # observables that are not blades, in Cl(3,1): A in the plane of e0, e1; B in the plane of the commuting pair
    a1 = GA.add(GA.scal(F(3, 5), bl((0,))), GA.scal(F(4, 5), bl((1,))))
    a2 = GA.add(GA.scal(F(5, 13), bl((0,))), GA.scal(F(-12, 13), bl((1,))))
    b1 = GA.add(GA.scal(F(8, 17), bl((2, 3))), GA.scal(F(15, 17), bl((0, 1, 3))))
    b2 = GA.add(GA.scal(F(20, 29), bl((2, 3))), GA.scal(F(21, 29), bl((0, 1, 3))))
    for o in (a1, a2, b1, b2):
        assert dagger(o, sq) == o and prod(sq, o, o) == ONE
    for a in (a1, a2):
        for b in (b1, b2):
            assert GA.commutes(a, b, sq)
    c = chsh(sq, a1, a2, b1, b2)
    assert dagger(c, sq) == c
    rhs = GA.sub(GA.sc(F(4)), prod(sq, comm(a1, a2, sq), comm(b1, b2, sq)))
    assert prod(sq, c, c) == rhs
    assert not GA.is_zero(prod(sq, comm(a1, a2, sq), comm(b1, b2, sq)))
    return True


def frame_data(p, q):
    """(has central J, frame size) and the frame test used by the proof of clause (ii)."""
    sq = GA.sig(p, q)
    herm = self_adjoint_blades(sq)
    for b in herm:
        assert prod(sq, bl(b), bl(b)) == ONE
    central = [b for b in herm if b and is_central(b, sq)]
    assert len(central) <= 1
    rest = [b for b in herm if b and b not in central]
    if central:
        jb = central[0]
        assert jb == tuple(range(p + q))
        classes, seen = [], set()
        for b in rest:
            if b in seen:
                continue
            partner = next(iter(prod(sq, bl(jb), bl(b))))
            assert partner in rest
            seen.update((b, partner))
            classes.append(b)
        frame = classes
        modulo = lambda t: frozenset((t, next(iter(prod(sq, bl(jb), bl(t))))))
    else:
        frame = rest
        modulo = lambda t: frozenset((t,))
    ok = True
    products = set()
    reserved = {modulo(())} | {modulo(b) for b in frame}
    for h, k in combinations(frame, 2):
        ok = ok and GA.anticommutes(bl(h), bl(k), sq)
        t = modulo(next(iter(prod(sq, bl(h), bl(k)))))
        ok = ok and t not in reserved and t not in products
        products.add(t)
    return bool(central), len(frame), ok, len(herm)


def check_excluded_signatures_have_only_an_anticommuting_frame_of_observables():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    expected = {
        (1, 0): (True, 0, 2), (0, 1): (False, 0, 1),
        (2, 0): (False, 2, 3), (1, 1): (False, 2, 3), (0, 2): (False, 0, 1),
        (3, 0): (False, 3, 4), (2, 1): (True, 2, 6), (1, 2): (False, 3, 4), (0, 3): (True, 0, 2),
        (4, 0): (False, 5, 6), (1, 3): (False, 5, 6), (0, 4): (False, 5, 6),
        (5, 0): (True, 5, 12), (1, 4): (True, 5, 12),
    }
    assert len(expected) == 14
    for (p, q), (has_j, size, dim) in expected.items():
        got_j, got_size, ok, got_dim = frame_data(p, q)
        assert ok, (p, q)
        assert (got_j, got_size, got_dim) == (has_j, size, dim), (p, q)
    # the frame test fails in the two other signatures of four directions
    assert not frame_data(3, 1)[2] and not frame_data(2, 2)[2]
    assert frame_data(3, 1)[3] == 10 and frame_data(2, 2)[3] == 10
    # the lemma on elements that are not blades, Cl(4,0): unit vectors of the frame e0..e3, I
    sq = GA.sig(4, 0)
    ps = bl((0, 1, 2, 3))
    u = GA.add(GA.scal(F(3, 5), bl((0,))), GA.scal(F(4, 5), ps))
    w = GA.add(GA.scal(F(5, 13), bl((0,))), GA.scal(F(12, 13), bl((2,))))
    for o in (u, w):
        assert dagger(o, sq) == o and prod(sq, o, o) == ONE
    assert not GA.commutes(u, w, sq)
    assert GA.commutes(u, GA.neg(u), sq)
    assert comm(u, w, sq) == GA.scal(F(2), GA.sub(prod(sq, u, w), GA.sc(F(3, 5) * F(5, 13))))
    return True


def check_remaining_signatures_carry_blades_with_chsh_square_four_plus_four_k():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    table = {
        (3, 1): ((0,), (1,), (2, 3), (0, 1, 3)),
        (2, 2): ((0,), (1,), (0, 1, 2), (0, 1, 3)),
        (4, 1): ((0,), (1,), (2, 4), (3, 4)),
        (3, 2): ((0,), (1,), (2, 3), (2, 4)),
        (2, 3): ((0,), (1,), (0, 1, 2), (0, 1, 3)),
        (0, 5): ((0, 1, 2), (0, 1, 3), (2, 3, 4), (0, 2, 3, 4)),
        (6, 0): ((0,), (1,), (2, 3, 4, 5), (0, 1, 2, 3, 4)),
        (5, 1): ((0,), (1,), (2, 5), (3, 5)),
        (4, 2): ((0,), (1,), (2, 4), (2, 5)),
        (3, 3): ((0,), (1,), (2, 3), (2, 4)),
        (2, 4): ((0,), (1,), (0, 1, 2), (0, 1, 3)),
        (1, 5): ((0,), (0, 1), (2, 3, 4, 5), (0, 1, 2, 3, 4)),
        (0, 6): ((0, 1, 2), (0, 1, 3), (0, 4, 5), (1, 4, 5)),
    }
    assert len(table) == 13
    for (p, q), blades in table.items():
        sq = GA.sig(p, q)
        a1, a2, b1, b2 = (bl(b) for b in blades)
        for o in (a1, a2, b1, b2):
            assert dagger(o, sq) == o and prod(sq, o, o) == ONE, (p, q)
        assert GA.anticommutes(a1, a2, sq) and GA.anticommutes(b1, b2, sq), (p, q)
        for a in (a1, a2):
            for b in (b1, b2):
                assert GA.commutes(a, b, sq), (p, q)
        c = chsh(sq, a1, a2, b1, b2)
        k = GA.neg(prod(sq, a1, a2, b1, b2))
        assert len(k) == 1 and () not in k and not is_central(next(iter(k)), sq)
        assert dagger(k, sq) == k and prod(sq, k, k) == ONE and GA.commutes(k, c, sq)
        c2 = prod(sq, c, c)
        assert c2 == GA.add(GA.sc(F(4)), GA.scal(F(4), k)), (p, q)
        assert prod(sq, c2, c) == GA.scal(F(8), c)
        for r in (F(1, 3), F(-7, 20), F(3, 8)):
            assert 8 * r * r <= 2
            rho = prod(sq, GA.add(ONE, k), GA.add(ONE, GA.scal(r, c)))
            assert dagger(rho, sq) == rho
            assert s0(rho) == 1 and s0(prod(sq, rho, c)) == 8 * r and s0(prod(sq, rho, c2)) == 8
            assert (8 * r) ** 2 < 8
            for t in (F(1, 2), F(-3, 4), F(5, 2)):
                x = GA.add(GA.add(ONE, k), GA.scal(t, c), a1)
                assert s0(prod(sq, rho, x, dagger(x, sq))) >= 0
        # outside 8 r^2 <= 1 the functional is not positive
        r = F(3, 8)
        assert 8 * r * r > 1
        rho = prod(sq, GA.add(ONE, k), GA.add(ONE, GA.scal(r, c)))
        x = GA.sub(GA.scal(F(3), ONE), c)
        assert s0(prod(sq, rho, x, dagger(x, sq))) == 9 - 18 + 8
    return True


def check_excluded_list_is_matrix_size_at_most_two_in_the_classification():
    premise("transport.classification-real-clifford-algebras")
    # matrix size k of Cl(p,q) = M_k(D) or M_k(D) + M_k(D), from p - q mod 8 (the stored table)
    def size(p, q):
        n, m = p + q, (p - q) % 8
        drop = {0: 0, 2: 0, 1: 1, 3: 1, 7: 1, 4: 2, 6: 2, 5: 3}[m]
        assert (n - drop) % 2 == 0
        return 2 ** ((n - drop) // 2)
    excluded = {(p, n - p) for n in range(1, 4) for p in range(n + 1)} | {(4, 0), (1, 3), (0, 4), (5, 0), (1, 4)}
    assert len(excluded) == 14
    for n in range(1, 9):
        for p in range(n + 1):
            assert (size(p, n - p) <= 2) == ((p, n - p) in excluded), (p, n - p)
    assert size(3, 1) == 4 and size(1, 3) == 2 and size(3, 0) == 2 and size(2, 2) == 4
    return True
