"""synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes: exact checks.

Cl(2,2) of two modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1); the dagger sends a blade to its
inverse.  Settings: A_1 = e_1, A_2 = f_1 e_1, B'_1 = e_2 f_1 e_1, B'_2 = f_2 e_2.  Fraction arithmetic only.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
SQ = (1, -1, 1, -1)


def prod(*xs):
    out = ONE
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def dagger(x):
    out = {}
    for b, c in x.items():
        g = len(b)
        s = F(-1) ** (g * (g - 1) // 2)
        for k in b:
            s *= SQ[k]
        out[b] = s * c
    return out


def s0(x):
    return x.get((), F(0))


def setting():
    e1, f1, e2, f2 = [GA.gen(i) for i in range(4)]
    a = [e1, prod(f1, e1)]
    b = [prod(e2, f1, e1), prod(f2, e2)]
    t = {(i, j): prod(a[i], b[j]) for i in range(2) for j in range(2)}
    c = GA.add(t[0, 0], t[0, 1], t[1, 0], GA.neg(t[1, 1]))
    return a, b, t, c, prod(e1, f2)


def projector(x):
    return GA.eq(prod(x, x), x) and GA.eq(dagger(x), x)


def atom(r):
    v = [GA.scal(F(1, 2), GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(2)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(2)]
    p0 = prod(w[0], v[0], w[1], v[1])
    s = [p0, prod(v[0], p0), prod(v[1], p0), prod(v[0], v[1], p0)]
    y = GA.add(*[GA.scal(F(r[i]), s[i]) for i in range(4) if r[i] != 0])
    return GA.scal(1 / sum(F(x) * F(x) for x in r), prod(y, dagger(y)))


def check_chsh_element_is_a_combination_of_four_rational_projectors_in_two_commuting_pairs():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    a, b, t, c, k = setting()
    for x in a + b + list(t.values()):
        assert GA.eq(dagger(x), x) and GA.eq(prod(x, x), ONE)
    assert all(GA.commutes(x, y, SQ) for x in a for y in b)
    e = {key: GA.scal(F(1, 2), GA.add(ONE, x)) for key, x in t.items()}
    assert all(projector(x) and s0(x) == F(1, 2) for x in e.values())
    combo = GA.sub(GA.scal(2, GA.add(e[0, 0], e[0, 1], e[1, 0], GA.neg(e[1, 1]))), GA.scal(2, ONE))
    assert GA.eq(c, combo)
    commuting = [(x, y) for x, y in combinations(sorted(t), 2) if GA.commutes(t[x], t[y], SQ)]
    anti = [(x, y) for x, y in combinations(sorted(t), 2) if GA.anticommutes(t[x], t[y], SQ)]
    assert commuting == [((0, 0), (1, 1)), ((0, 1), (1, 0))] and len(anti) == 4
    d1 = GA.sub(t[0, 0], t[1, 1])
    d2 = GA.add(t[0, 1], t[1, 0])
    assert GA.eq(GA.add(d1, d2), c) and not GA.commutes(d1, d2, SQ)
    for d in (d1, d2):
        assert GA.eq(prod(d, d, d), GA.scal(4, d)) and GA.eq(prod(d, d), GA.add(GA.scal(2, ONE), GA.scal(2, k)))
    return True


def check_chsh_element_has_no_decomposition_into_commuting_rational_projectors():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    a, b, t, c, k = setting()
    c2 = prod(c, c)
    assert GA.eq(dagger(k), k) and GA.eq(prod(k, k), ONE)
    assert GA.eq(c2, GA.add(GA.scal(4, ONE), GA.scal(4, k)))
    assert GA.eq(prod(c2, c), GA.scal(8, c)) and not GA.is_zero(c) and not GA.eq(c2, GA.scal(8, ONE))
    # x^2 - 8 has no rational root: 8 q^2 = p^2 has no solution in the box, and 8 lies strictly between 2^2 and 3^2
    assert not any(8 * q * q == p * p for q in range(1, 60) for p in range(1, 180)) and 2 * 2 < 8 < 3 * 3
    kernel = GA.sub(ONE, GA.scal(F(1, 8), c2))
    assert projector(kernel) and s0(kernel) == F(1, 2) and GA.is_zero(prod(c, kernel))
    return True


def check_sum_of_correlators_is_the_linear_value_bounded_for_states_and_four_for_the_box():
    premise("synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear")
    a, b, t, c, k = setting()
    e = {key: GA.scal(F(1, 2), GA.add(ONE, x)) for key, x in t.items()}

    def correlators(weight):
        return [weight(e[key]) - weight(GA.sub(ONE, e[key])) for key in sorted(e)]

    def chsh(weight):
        kap = correlators(weight)
        return kap[0] + kap[1] + kap[2] - kap[3]

    # states: the atoms' functionals x -> 4 <Pi_r x>_0
    best = F(0)
    for r in product(range(-3, 4), repeat=4):
        if not any(r):
            continue
        pi = atom(r)

        def weight(x, pi=pi):
            return 4 * s0(prod(pi, x))

        s = chsh(weight)
        assert s == weight(c) and s * s < 8
        assert s * s <= weight(prod(c, c)) == 4 + 4 * weight(k) <= 8
        best = max(best, s)
    assert best == F(14, 5)
    pi = atom((-1, 2, -2, -1))
    assert projector(pi) and correlators(lambda x: 4 * s0(prod(pi, x))) == [F(3, 5), F(4, 5), F(4, 5), F(-3, 5)]

    # the functional of value 4: additive, non-negative on the sixteen joint outcomes of the four settings
    def box(x):
        return s0(prod(GA.add(ONE, c), x))

    assert box(ONE) == 1 and correlators(box) == [1, 1, 1, -1] and chsh(box) == 4
    table = []
    for i, j in product(range(2), repeat=2):
        for sa, sb in product((1, -1), repeat=2):
            joint = prod(GA.scal(F(1, 2), GA.add(ONE, GA.scal(sa, a[i]))), GA.scal(F(1, 2), GA.add(ONE, GA.scal(sb, b[j]))))
            assert projector(joint)
            table.append(box(joint))
    assert len(table) == 16 and sorted(set(table)) == [0, F(1, 2)]
    assert box(atom((1, 0, 0, 1))) == F(-1, 4) and projector(atom((1, 0, 0, 1)))
    return True
