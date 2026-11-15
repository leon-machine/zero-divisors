"""synthesis.size-of-an-element-of-the-switch-tower: exact checks.

The rung Cl_Q(k,k) is computed with GA.py: generators 0..k-1 are e_1..e_k (square +1) and k..2k-1 are
f_1..f_k (square -1). The size N(a) = dim(a A)/dim A is computed as the rank of the family
{a * blade}, in exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product

import GA

H = F(1, 2)


def rung(k):
    return GA.sig(k, k)


def e_(i, k):
    return GA.gen(i - 1)


def f_(i, k):
    return GA.gen(k + i - 1)


def v_(i, k):
    return GA.scal(H, GA.add(e_(i, k), f_(i, k)))


def w_(i, k):
    return GA.scal(H, GA.sub(e_(i, k), f_(i, k)))


def mul(x, y, k):
    return GA.mul(x, y, rung(k))


def on_(i, k):
    return mul(v_(i, k), w_(i, k), k)


def off_(i, k):
    return mul(w_(i, k), v_(i, k), k)


def size(a, k):
    blades = GA.all_blades(2 * k)
    index = {b: i for i, b in enumerate(blades)}
    rows = []
    for b in blades:
        p = mul(a, {b: F(1)}, k)
        row = [F(0)] * len(blades)
        for bb, c in p.items():
            row[index[bb]] = c
        rows.append(row)
    return F(GA.rank_of_vectors(rows), len(blades))


def lift(a, k):
    """the same element in the next rung (the f generators are re-indexed)."""
    out = {}
    for b, c in a.items():
        out[tuple(sorted(i if i < k else i + 1 for i in b))] = c
    return out


def samples_rung_two():
    k = 2
    return [
        {}, GA.sc(1), e_(1, k), f_(2, k), v_(1, k), w_(2, k), on_(1, k), off_(2, k),
        GA.add(GA.sc(1), e_(1, k)), GA.add(e_(1, k), GA.scal(2, f_(1, k))),
        mul(v_(1, k), v_(2, k), k), GA.add(on_(1, k), on_(2, k)), mul(on_(1, k), off_(2, k), k),
        GA.add(v_(1, k), w_(2, k)),
    ]


S2 = samples_rung_two()
N2 = [size(a, 2) for a in S2]
# hand values: 0; units 1, e_1, f_2; null vectors and single tests 1/2; 1 + e_1 = 2 * idempotent of rank 2;
# e_1 + 2 f_1 has square -3, a unit; v_1 v_2 rank 1; on_1 + on_2 rank 3; on_1 off_2 rank 1;
# v_1 + w_2 is a null vector (v_1 and w_2 anticommute and square to 0), so 1/2
N2_BY_HAND = [F(0), F(1), F(1), F(1), H, H, H, H, H, F(1), F(1, 4), F(3, 4), F(1, 4), H]


def check_size_bounds_and_rank_inequalities_at_rung_two():
    assert N2 == N2_BY_HAND
    for a, na in zip(S2, N2):
        assert 0 <= na <= 1 and (na == 0) == GA.is_zero(a)
        assert size(GA.scal(F(-3, 7), a), 2) == na
    for (a, na), (b, nb) in product(list(zip(S2, N2)), repeat=2):
        assert size(GA.add(a, b), 2) <= na + nb
        nab = size(mul(a, b, 2), 2)
        assert nab <= na and nab <= nb
    return True


def check_frobenius_inequality_on_all_triples():
    idx = range(len(S2))
    prod2 = {(i, j): mul(S2[i], S2[j], 2) for i in idx for j in idx}
    nprod = {key: size(val, 2) for key, val in prod2.items()}
    cache = {}
    for i, j, l in product(idx, repeat=3):
        abc = mul(prod2[(i, j)], S2[l], 2)
        key = tuple(sorted(abc.items()))
        if key not in cache:
            cache[key] = size(abc, 2)
        assert nprod[(i, j)] + nprod[(j, l)] <= N2[j] + cache[key]
    # hand value: a = on_1, b = 1, c = off_1 gives 1/2 + 1/2 <= 1 + 0, with equality
    assert size(on_(1, 2), 2) + size(off_(1, 2), 2) == 1 and GA.is_zero(mul(on_(1, 2), off_(1, 2), 2))
    return True


def check_size_is_the_rank_on_a_minimal_left_ideal():
    """A P with P = off_1 off_2 is a 4-dimensional left ideal on which Cl_Q(2,2) acts faithfully;
    the size of a is the rank of its action there divided by 4."""
    k = 2
    P = mul(off_(1, k), off_(2, k), k)
    blades = GA.all_blades(4)
    index = {b: i for i, b in enumerate(blades)}

    def vec(x):
        row = [F(0)] * len(blades)
        for bb, c in x.items():
            row[index[bb]] = c
        return row
    span = [vec(mul({b: F(1)}, P, k)) for b in blades]
    assert GA.rank_of_vectors(span) == 4
    for a, na in zip(S2, N2):
        image = [vec(mul(a, mul({b: F(1)}, P, k), k)) for b in blades]
        assert F(GA.rank_of_vectors(image), 4) == na
    return True


def check_size_is_unchanged_up_the_tower():
    for a, na in zip(S2, N2):
        assert size(lift(a, 2), 3) == na
    k = 1
    for a, hand in ((v_(1, k), H), (on_(1, k), H), (e_(1, k), F(1)), (GA.add(GA.sc(1), e_(1, k)), H)):
        assert size(a, 1) == hand == size(lift(a, 1), 2)
    return True


def check_sizes_multiply_on_separate_switches():
    k = 3
    first = [on_(1, k), v_(1, k), GA.add(GA.sc(1), e_(1, k)), e_(1, k), GA.add(on_(1, k), GA.scal(2, v_(1, k)))]
    rest_even = [
        on_(2, k), mul(on_(2, k), off_(3, k), k), GA.add(on_(2, k), on_(3, k)),
        mul(v_(2, k), w_(3, k), k), GA.add(GA.sc(1), mul(e_(2, k), f_(3, k), k)), GA.sc(1),
    ]
    for a in first:
        for b in rest_even:
            ab = mul(a, b, k)
            assert GA.eq(ab, mul(b, a, k))
            assert size(ab, k) == size(a, k) * size(b, k)
    # interleaved index sets: a on switch 2, b even on switches 1 and 3
    a = v_(2, k)
    b = mul(on_(1, k), off_(3, k), k)
    assert size(mul(a, b, k), k) == H * F(1, 4) == F(1, 8)
    # an odd element on other switches need not multiply: v_1 v_2 has size 1/4, but e_1 e_2 is a unit
    assert size(mul(e_(1, k), e_(2, k), k), k) == 1
    return True


BOX = (-2, -1, 0, 1, 2)


def check_null_vectors_have_size_one_half():
    k = 2
    nulls = 0
    for a, b, c, d in product(BOX, repeat=4):
        if (a, b, c, d) == (0, 0, 0, 0):
            continue
        n = GA.add(GA.add(GA.scal(a, e_(1, k)), GA.scal(b, e_(2, k))), GA.add(GA.scal(c, f_(1, k)), GA.scal(d, f_(2, k))))
        q = a * a + b * b - c * c - d * d
        assert size(n, k) == (H if q == 0 else F(1))
        nulls += int(q == 0)
    # hand count: a^2 + b^2 takes the values 0, 1, 2, 4, 5, 8 on the box for 1, 4, 4, 4, 8, 4 pairs (a, b),
    # so a^2 + b^2 = c^2 + d^2 has 1 + 16 + 16 + 16 + 64 + 16 = 129 solutions, 128 of them nonzero
    assert nulls == 128
    assert size(on_(1, k), k) == H == size(off_(1, k), k)
    assert GA.eq(mul(mul(e_(1, k), on_(1, k), k), e_(1, k), k), off_(1, k))
    return True


def check_idempotent_rules_that_force_the_size():
    k = 2
    one = GA.sc(1)
    g1 = on_(1, k)
    g2 = mul(off_(1, k), on_(2, k), k)
    p2 = mul(off_(1, k), off_(2, k), k)
    for x in (g1, g2, p2):
        assert GA.eq(mul(x, x, k), x)
    assert GA.is_zero(mul(g1, g2, k)) and GA.is_zero(mul(g2, p2, k)) and GA.is_zero(mul(g1, p2, k))
    assert GA.eq(GA.add(g1, g2, p2), one)
    assert (size(g1, k), size(g2, k), size(p2, k)) == (H, F(1, 4), F(1, 4))
    assert size(GA.add(g1, g2), k) == F(3, 4) and size(GA.sub(one, g1), k) == H
    # conjugation by the unit u = 1 + v_1 (inverse 1 - v_1) does not change the size
    u, ui = GA.add(one, v_(1, k)), GA.sub(one, v_(1, k))
    assert GA.eq(mul(u, ui, k), one)
    for a, na in zip(S2, N2):
        assert size(mul(mul(u, a, k), ui, k), k) == na
    # the four minimal exclusive tests of rung 2 have equal size 1/4 and sum to 1
    quarters = [mul(x, y, k) for x in (on_(1, k), off_(1, k)) for y in (on_(2, k), off_(2, k))]
    total = {}
    for x in quarters:
        assert size(x, k) == F(1, 4)
        total = GA.add(total, x)
    assert GA.eq(total, one)
    return True
