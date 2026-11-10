"""synthesis.composition-cycles-counting-needs-addition: exact checks of clauses (i) to (iv).

The group G of signed directions is realised as the signed blades {+e_S, -e_S} of Cl(p,q), the bit c
acting as -1 (clause (v) of synthesis.signed-directions-and-the-integer-clifford-algebra); GA.py
multiplies with Fraction coefficients, so integer inputs stay integral and every product computed here
is a product in the integer algebra A = Z[G]/(c + 1).
(i)   The bit: repeated comparison in F2 gives k mod 2.
(ii)  Every signed blade g of every signature with n <= 4 has g^2 in {+1, -1} and g^4 = 1; the orders are
      tabulated and compared with hand counts; e_i^k = e_i^(k mod 4), = e_i^(k mod 2) when e_i^2 = +1,
      and e_i^5 = e_i.
(iii) k * 1 for the sample of k are pairwise distinct, of grade 0, nonzero for k != 0, and additive and
      multiplicative in k.
(iv)  Every product of signed blades is a signed blade, never k * 1 with |k| >= 2: all words of length up
      to four in Cl(1,1), Cl(0,2) and Cl(2,0), and pseudo-random words of length up to six (a fixed linear
      congruential sequence) in five signatures with n = 4; the numbers of words are compared with counts
      made by hand.
Sample inputs are at module level; the literals inside the functions are expected values.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise

SIGNATURES = [(p, n - p) for n in (1, 2, 3, 4) for p in range(n + 1)]
POWERS = list(range(0, 41))
KS = list(range(-60, 61))
SMALL_KS = list(range(-7, 8))
WORD_SIGS = [(1, 1), (0, 2), (2, 0)]
WORD_LENGTHS = [1, 2, 3, 4]
RAND_SIGS = [(1, 3), (3, 1), (2, 2), (4, 0), (0, 4)]
RAND_WORDS = 600
RAND_MAXLEN = 6
PARITY_SAMPLE = list(range(0, 101))
SUMS_SIG = (1, 3)


def blades(n):
    return [S for k in range(n + 1) for S in combinations(range(n), k)]


def signed_blades(n):
    return [{S: F(s)} for S in blades(n) for s in (1, -1)]


def power(x, k, sq):
    out = GA.sc(1)
    for _ in range(k):
        out = GA.mul(out, x, sq)
    return out


def is_signed_blade(x):
    return len(x) == 1 and list(x.values())[0] in (F(1), F(-1))


def lcg(seed):
    """A fixed linear congruential sequence (exact integers), standing in for a random source."""
    state = seed
    while True:
        state = (6364136223846793005 * state + 1442695040888963407) % (1 << 64)
        yield state >> 33


def check_the_bit_counts_modulo_two():
    for k in PARITY_SAMPLE:
        s = 0
        for _ in range(k):
            s = (s + 1) % 2
        assert s == k % 2
    assert sum(1 for k in PARITY_SAMPLE if k % 2 == 1) == 50
    return True


def check_every_signed_configuration_has_order_dividing_four():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    tally = {}
    for (p, q) in SIGNATURES:
        n = p + q
        sq = GA.sig(p, q)
        orders = {1: 0, 2: 0, 4: 0}
        for g in signed_blades(n):
            g2 = GA.mul(g, g, sq)
            assert g2 in (GA.sc(1), GA.sc(-1))
            assert GA.mul(g2, g2, sq) == GA.sc(1)
            if g == GA.sc(1):
                orders[1] += 1
            elif g2 == GA.sc(1):
                orders[2] += 1
            else:
                orders[4] += 1
        assert sum(orders.values()) == 2 ** (n + 1)
        tally[(p, q)] = orders
    # hand counts. Cl(2,0): +-1, +-e1, +-e2, +-e12 with e12^2 = -1
    assert tally[(2, 0)] == {1: 1, 2: 5, 4: 2}
    # Cl(0,1): +-1, +-e1 with e1^2 = -1, the cyclic group of order 4
    assert tally[(0, 1)] == {1: 1, 2: 1, 4: 2}
    # Cl(1,0): +-1, +-e1 with e1^2 = 1, the Klein four-group
    assert tally[(1, 0)] == {1: 1, 2: 3, 4: 0}
    # Cl(3,0): squares of blades +1, +1, +1, +1, -1, -1, -1, -1 (grades 0, 1 square to +1; 2, 3 to -1)
    assert tally[(3, 0)] == {1: 1, 2: 7, 4: 8}
    assert len(tally) == 14
    return True


def check_powers_of_a_direction_cycle():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    pairs = 0
    for (p, q) in SIGNATURES:
        n = p + q
        sq = GA.sig(p, q)
        for i in range(n):
            e = GA.gen(i)
            plus = GA.mul(e, e, sq) == GA.sc(1)
            for k in POWERS:
                ek = power(e, k, sq)
                assert ek == power(e, k % 4, sq)
                if plus:
                    assert ek == power(e, k % 2, sq)
                pairs += 1
            assert power(e, 5, sq) == e
            assert power(e, 4, sq) == GA.sc(1)
            assert power(e, 2, sq) == GA.sc(1 if i < p else -1)
    # 1 + 2 + 3 + 4 directions in 2 + 3 + 4 + 5 signatures: 1*2 + 2*3 + 3*4 + 4*5 = 40 directions
    assert pairs == 40 * len(POWERS)
    return True


def check_sums_of_the_unit_are_an_injective_copy_of_the_integers():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    sq = GA.sig(*SUMS_SIG)
    one = GA.sc(1)
    seen = {}
    for k in KS:
        x = GA.sc(0)
        for _ in range(abs(k)):
            x = GA.add(x, one if k > 0 else GA.neg(one))
        if k == 0:
            assert GA.is_zero(x)
            continue
        assert list(x.keys()) == [()]
        assert x[()] not in seen
        seen[x[()]] = k
    assert len(seen) == len(KS) - 1
    for a in SMALL_KS:
        for b in SMALL_KS:
            xa, xb = GA.sc(a), GA.sc(b)
            assert GA.eq(GA.add(xa, xb), GA.sc(a + b))
            assert GA.eq(GA.mul(xa, xb, sq), GA.sc(a * b))
    five = GA.add(one, one, one, one, one)
    assert five == GA.sc(5)
    for i in range(sum(SUMS_SIG)):
        e = GA.gen(i)
        e5 = power(e, 5, sq)
        assert e5 == e and e5 != five
    return True


def check_no_product_of_signed_configurations_counts():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    words = 0
    scalars = set()
    for (p, q) in WORD_SIGS:
        n = p + q
        sq = GA.sig(p, q)
        G = signed_blades(n)
        for length in WORD_LENGTHS:
            for word in product(G, repeat=length):
                x = GA.sc(1)
                for g in word:
                    x = GA.mul(x, g, sq)
                assert is_signed_blade(x)
                if list(x.keys()) == [()]:
                    scalars.add(x[()])
                words += 1
    # 8 signed blades for n = 2: 8 + 64 + 512 + 4096 words in each of three signatures
    assert words == 3 * (8 + 64 + 512 + 4096)
    # the only integers that products reach are +1 and -1
    assert scalars == {F(1), F(-1)}
    gen = lcg(20261108)
    rwords = 0
    for (p, q) in RAND_SIGS:
        n = p + q
        sq = GA.sig(p, q)
        G = signed_blades(n)
        for _ in range(RAND_WORDS):
            x = GA.sc(1)
            for _ in range(1 + next(gen) % RAND_MAXLEN):
                x = GA.mul(x, G[next(gen) % len(G)], sq)
            assert is_signed_blade(x)
            rwords += 1
    assert rwords == 5 * RAND_WORDS
    assert len(G) == 32
    return True
