"""synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane: exact checks.

The bit is modelled by 2 x 2 matrices in the basis (s_off, s_on); integer entries stay integral,
so the identities checked hold over Z and, by reduction, over every commutative ring. Targets of
the universal property are switches in Clifford algebras computed with GA.py and conjugates of the
model under GL_2(Z).
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


def check_set_and_clear_are_a_switch_with_tests():
    assert mm(V, V) == Z2 and mm(W, W) == Z2
    assert ma(VW, WV) == I2
    assert mm(VW, VW) == VW and mm(WV, WV) == WV and mm(VW, WV) == Z2 and mm(WV, VW) == Z2
    assert VW == M(0, 0, 0, 1) and WV == M(1, 0, 0, 0)      # is-on, is-off
    return True


def _det4(rows):
    m = [list(r) for r in rows]
    d = F(1)
    for c in range(4):
        p = next((r for r in range(c, 4) if m[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            m[c], m[p] = m[p], m[c]
            d = -d
        d *= m[c][c]
        for r in range(c + 1, 4):
            f = m[r][c] / m[c][c]
            m[r] = [a - f * b for a, b in zip(m[r], m[c])]
    return d


def check_basis_of_the_endomorphisms_over_the_integers():
    assert (WV, W, V, VW) == (M(1, 0, 0, 0), M(0, 1, 0, 0), M(0, 0, 1, 0), M(0, 0, 0, 1))
    assert abs(_det4([flat(I2), flat(V), flat(W), flat(VW)])) == 1
    return True


BOX = list(range(-4, 5))


def check_square_is_the_hyperbolic_form():
    for a, b in product(BOX, repeat=2):
        x = ma(ms(a, V), ms(b, W))
        assert mm(x, x) == ms(a * b, I2)
    x = ma(ms(3, V), ms(5, W))          # hand value: (3v + 5w)^2 = 15
    assert mm(x, x) == ms(15, I2)
    x = ma(ms(-2, V), ms(7, W))         # hand value: (-2v + 7w)^2 = -14
    assert mm(x, x) == ms(-14, I2)
    return True


def _table_ok(one, a, b, mul_, lin_eq):
    src = [I2, V, W, VW]
    tgt = [one, a, b, mul_(a, b)]

    def coords(X):   # X = p*1 + r*v + q*w + (s - p)*vw for X = [[p, q], [r, s]]
        return [X[0][0], X[1][0], X[0][1], X[1][1] - X[0][0]]
    return all(lin_eq(mul_(tgt[i], tgt[j]), coords(mm(src[i], src[j])), tgt) for i in range(4) for j in range(4))


def check_universal_property_on_target_switches():
    h = F(1, 2)

    def ga_target(sq, a, b):
        mul_ = lambda x, y: GA.mul(x, y, sq)
        assert GA.is_zero(mul_(a, a)) and GA.is_zero(mul_(b, b)) and GA.eq(GA.add(mul_(a, b), mul_(b, a)), GA.sc(1))

        def lin_eq(lhs, c, tgt):
            rhs = {}
            for ci, t in zip(c, tgt):
                rhs = GA.add(rhs, GA.scal(ci, t))
            return GA.eq(lhs, rhs)
        return _table_ok(GA.sc(1), a, b, mul_, lin_eq)
    s11, s22 = GA.sig(1, 1), GA.sig(2, 2)
    assert ga_target(s11, GA.scal(h, GA.add(GA.gen(0), GA.gen(1))), GA.scal(h, GA.sub(GA.gen(0), GA.gen(1))))
    a22, b22 = GA.scal(h, GA.add(GA.gen(0), GA.gen(2))), GA.scal(h, GA.sub(GA.gen(0), GA.gen(2)))
    assert ga_target(s22, a22, b22)
    # a switch that is not a pair of vectors: conjugate by the unit 1 + n, n nilpotent
    n_ = GA.mul(GA.scal(h, GA.add(GA.gen(1), GA.gen(3))), GA.gen(0), s22)
    u, ui = GA.add(GA.sc(1), n_), GA.sub(GA.sc(1), n_)
    assert GA.eq(GA.mul(u, ui, s22), GA.sc(1))
    conj = lambda x: GA.mul(GA.mul(u, x, s22), ui, s22)
    assert ga_target(s22, conj(a22), conj(b22))
    # integer switches: GL_2(Z)-conjugates of (v, w)
    count = 0
    for p, q, r, s in product(range(-2, 3), repeat=4):
        g = M(p, q, r, s)
        if abs(det(g)) != 1:
            continue
        gi = inv(g)
        a, b = mm(mm(g, V), gi), mm(mm(g, W), gi)

        def lin_eq(lhs, c, tgt):
            rhs = Z2
            for ci, t in zip(c, tgt):
                rhs = ma(rhs, ms(ci, t))
            return lhs == rhs
        assert _table_ok(I2, a, b, mm, lin_eq)
        count += 1
    assert count == 104      # the unimodular integer matrices with entries in [-2, 2]
    return True


def check_orthonormal_pair_from_the_switch():
    ep, em = ma(V, W), ma(V, ms(-1, W))
    assert mm(ep, ep) == I2 and mm(em, em) == ms(-1, I2)
    assert mm(ep, em) == ms(-1, mm(em, ep)) == ma(WV, ms(-1, VW))
    assert ep == M(0, 1, 1, 0) and mm(ep, em) == M(1, 0, 0, -1)
    return True
