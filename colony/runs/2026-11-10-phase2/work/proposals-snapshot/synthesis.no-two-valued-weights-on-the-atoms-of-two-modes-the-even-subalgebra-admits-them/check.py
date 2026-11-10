"""synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them: exact checks.

Cl(2,2) of two modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1), p_k = f_k e_k; the dagger sends a
blade to its inverse; v_k = (e_k + f_k)/2, w_k = (e_k - f_k)/2.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
SQ = (1, -1, 1, -1)

BASES = [
    [(0, 0, 0, 1), (0, 0, 1, 0), (1, 1, 0, 0), (1, -1, 0, 0)],
    [(0, 0, 0, 1), (0, 1, 0, 0), (1, 0, 1, 0), (1, 0, -1, 0)],
    [(1, -1, 1, -1), (1, -1, -1, 1), (1, 1, 0, 0), (0, 0, 1, 1)],
    [(1, -1, 1, -1), (1, 1, 1, 1), (1, 0, -1, 0), (0, 1, 0, -1)],
    [(0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 1), (1, 0, 0, -1)],
    [(1, -1, -1, 1), (1, 1, 1, 1), (1, 0, 0, -1), (0, 1, -1, 0)],
    [(1, 1, -1, 1), (1, 1, 1, -1), (1, -1, 0, 0), (0, 0, 1, 1)],
    [(1, 1, -1, 1), (-1, 1, 1, 1), (1, 0, 1, 0), (0, 1, 0, -1)],
    [(1, 1, 1, -1), (-1, 1, 1, 1), (1, 0, 0, 1), (0, 1, -1, 0)],
]


def dsign(b):
    g = len(b)
    s = (-1) ** (g * (g - 1) // 2)
    for i in b:
        s *= SQ[i]
    return s


def dagger(x):
    return {b: c * dsign(b) for b, c in x.items()}


def clean(x):
    return {b: c for b, c in x.items() if c != 0}


def prod(*xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, SQ)
    return clean(r)


def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return clean(r)


def s0(x):
    return x.get((), F(0))


def setup():
    e = [GA.gen(0), GA.gen(2)]
    f = [GA.gen(1), GA.gen(3)]
    p = [prod(f[k], e[k]) for k in range(2)]
    blades = [ONE] + [{tuple(c): F(1)} for r in range(1, 5) for c in combinations(range(4), r)]
    return e, f, p, blades


def check_eighteen_atoms_in_nine_contexts_admit_no_two_valued_weight():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    e, f, p, blades = setup()
    v = [lin((F(1, 2), e[j]), (F(1, 2), f[j])) for j in range(2)]
    w = [lin((F(1, 2), e[j]), (F(-1, 2), f[j])) for j in range(2)]
    assert all(clean(dagger(v[j])) == w[j] for j in range(2))
    p0 = prod(w[0], v[0], w[1], v[1])
    s = [p0, prod(v[0], p0), prod(v[1], p0), prod(v[0], v[1], p0)]
    for i in range(4):
        for j in range(4):
            assert prod(dagger(s[i]), s[j]) == (p0 if i == j else {})
    assert lin(*[(1, prod(s[i], dagger(s[i]))) for i in range(4)]) == ONE
    rays = sorted(set(r for b in BASES for r in b))
    assert len(rays) == 18

    def atom(r):
        y = lin(*[(r[i], s[i]) for i in range(4)])
        return clean(GA.scal(F(1, sum(c * c for c in r)), prod(y, dagger(y))))

    pi = {r: atom(r) for r in rays}
    for r in rays:
        q = pi[r]
        assert prod(q, q) == q and clean(dagger(q)) == q and s0(q) == F(1, 4)
        assert all(prod(q, b, q) == clean(GA.scal(4 * s0(prod(q, b)), q)) for b in blades)
    for b in BASES:
        assert lin(*[(1, pi[r]) for r in b]) == ONE
        assert all(prod(pi[r], pi[t]) == {} for r in b for t in b if r != t)
    assert all(sum(r in b for b in BASES) == 2 for r in rays)
    idx = {r: i for i, r in enumerate(rays)}
    masks = [sum(1 << idx[r] for r in b) for b in BASES]
    count = 0
    for bits in range(1 << 18):
        if all(bin(bits & m).count("1") == 1 for m in masks):
            count += 1
    assert count == 0
    return True


def check_square_of_nine_blades_has_no_multiplicative_sign_assignment():
    premise("tower.commuting-copies")
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    e, f, p, blades = setup()
    x1, z1, x2, z2 = e[0], p[0], prod(e[1], p[0]), p[1]
    sq = [[x1, x2, prod(x1, x2)], [z2, z1, prod(z1, z2)], [prod(x1, z2), prod(z1, x2), None]]
    sq[2][2] = prod(sq[0][2], sq[1][2])
    for row in sq:
        for o in row:
            assert len(o) == 1 and clean(dagger(o)) == o and prod(o, o) == ONE
    for t in range(3):
        row = sq[t]
        col = [sq[0][t], sq[1][t], sq[2][t]]
        assert all(GA.commutes(a, b, SQ) for a in row for b in row)
        assert all(GA.commutes(a, b, SQ) for a in col for b in col)
    rows = [s0(prod(*r)) for r in sq]
    cols = [s0(prod(sq[0][t], sq[1][t], sq[2][t])) for t in range(3)]
    assert all(len(prod(*r)) == 1 for r in sq)
    assert rows == [1, 1, -1] and cols == [1, 1, 1]
    return True


def check_even_subalgebra_of_two_modes_has_a_two_valued_weight():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    e, f, p, blades = setup()
    gam = prod(p[0], p[1])
    qp = lin((F(1, 2), ONE), (F(1, 2), gam))
    s1, s2 = p[0], prod(e[0], f[1])
    for o in (s1, s2):
        assert clean(dagger(o)) == o and prod(o, o) == ONE and len(next(iter(o))) % 2 == 0
    assert GA.anticommutes(s1, s2, SQ) and clean(dagger(prod(s1, s2))) == GA.neg(prod(s1, s2))
    evens = [b for b in blades if len(next(iter(b))) % 2 == 0]
    assert len(evens) == 8 and all(GA.commutes(gam, b, SQ) for b in evens)
    keys = [next(iter(b)) for b in blades]
    corner = [prod(qp, b) for b in evens]
    assert GA.mat_rank([[c.get(k_, F(0)) for k_ in keys] for c in corner]) == 4
    span = [prod(qp, o) for o in (ONE, s1, s2, prod(s1, s2))]
    assert GA.mat_rank([[c.get(k_, F(0)) for k_ in keys] for c in span]) == 4
    assert GA.mat_rank([[c.get(k_, F(0)) for k_ in keys] for c in span + corner]) == 4

    def h(x, z):
        return 1 if (z > 0 or (z == 0 and x > 0)) else 0

    pts = [(F(1, 2), F(0)), (F(0), F(1, 2)), (F(3, 10), F(4, 10)), (F(-3, 10), F(4, 10)), (F(5, 26), F(-12, 26))]
    for x, z in pts:
        c = prod(qp, lin((F(1, 2), ONE), (x, s1), (z, s2)))
        d = prod(qp, lin((F(1, 2), ONE), (-x, s1), (-z, s2)))
        assert prod(c, c) == c and clean(dagger(c)) == c and prod(c, d) == {} and lin((1, c), (1, d)) == qp
        assert h(x, z) + h(-x, -z) == 1
    return True
