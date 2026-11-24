"""synthesis.additive-weights-on-the-even-projectors-are-linear-from-three-modes-on: exact checks.

Cl(l,l) of l modes: e_j (square +1, index 2j), f_j (square -1, index 2j+1); the dagger sends a blade to its
inverse; s_I = v_I P_0 for subsets I; Gamma = e_1 f_1 ... e_l f_l is the pseudoscalar.  Fraction arithmetic only.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

ONE = GA.sc(F(1))


def prod(sq, *xs):
    out = ONE
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def dagger(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b)
        s = F(-1) ** (g * (g - 1) // 2)
        for k in b:
            s *= sq[k]
        out[b] = s * c
    return out


def dot(a, b):
    return sum(F(x) * F(y) for x, y in zip(a, b))


def modes(count):
    """Signature, P_0, the subsets ordered even ones first, the elements s_I and the pseudoscalar."""
    sq = tuple([1, -1] * count)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(count)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(count)]
    p0 = ONE
    for j in range(count):
        p0 = prod(sq, p0, w[j], v[j])
    subsets = [s for k in range(count + 1) for s in combinations(range(count), k)]
    subsets = [s for s in subsets if len(s) % 2 == 0] + [s for s in subsets if len(s) % 2 == 1]
    s = [prod(sq, *([v[j] for j in sub] + [p0])) for sub in subsets]
    gamma = {tuple(range(2 * count)): F(1)}
    return sq, p0, subsets, s, gamma


def atom(sq, s, r):
    y = GA.add(*[GA.scal(F(c), s[i]) for i, c in enumerate(r) if c != 0])
    return GA.scal(1 / dot(r, r), prod(sq, y, dagger(y, sq)))


def is_even(x):
    return all(len(b) % 2 == 0 for b in x)


def projector(sq, x):
    return GA.eq(prod(sq, x, x), x) and GA.eq(dagger(x, sq), x)


def check_even_subalgebra_of_three_modes_is_the_commutant_of_the_pseudoscalar_and_two_blocks_of_size_four():
    premise("synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four")
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    sq, p0, subsets, s, gamma = modes(3)
    size = len(s)
    assert size == 8 and [len(sub) % 2 for sub in subsets] == [0, 0, 0, 0, 1, 1, 1, 1] and p0[()] == F(1, 8)
    assert GA.eq(prod(sq, gamma, gamma), ONE) and GA.eq(dagger(gamma, sq), gamma)
    factors = [prod(sq, GA.gen(2 * j), GA.gen(2 * j + 1)) for j in range(3)]
    assert GA.eq(prod(sq, *factors), gamma)
    for i in range(size):
        assert GA.eq(prod(sq, gamma, s[i]), GA.scal(1 if i < 4 else -1, s[i]))
    blades = GA.all_blades(6)
    for b in blades:
        x = {b: F(1)}
        if len(b) % 2 == 0:
            assert GA.commutes(gamma, x, sq)
        else:
            assert GA.anticommutes(gamma, x, sq)
    sd = [dagger(x, sq) for x in s]
    for i in range(size):
        for j in range(size):
            assert GA.eq(prod(sq, sd[i], s[j]), p0 if i == j else {})
    rows = []
    for b in blades:
        row = []
        for i in range(size):
            xi = prod(sq, sd[i], {b: F(1)})
            for j in range(size):
                z = prod(sq, xi, s[j])
                c = z.get((), F(0)) / p0[()]
                assert GA.eq(z, GA.scal(c, p0))
                if ((i < 4) != (j < 4)) == (len(b) % 2 == 0):
                    assert c == 0
                row.append(c)
        rows.append(row)
    assert GA.mat_rank(rows) == 64
    assert GA.mat_rank([row for b, row in zip(blades, rows) if len(b) % 2 == 0]) == 32
    for sign in (1, -1):
        half = GA.scal(F(1, 2), GA.add(ONE, GA.scal(sign, gamma)))
        assert projector(sq, half) and is_even(half) and half[()] == F(1, 2)
        block = range(4) if sign == 1 else range(4, 8)
        assert GA.eq(half, GA.add(*[prod(sq, s[i], sd[i]) for i in block]))
    return True


def check_block_atoms_of_three_modes_are_even_projectors_and_a_linear_weight_is_recovered_block_by_block():
    premise("synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four")
    sq, p0, subsets, s, gamma = modes(3)
    plus = [(1, 2, 0, -1, 0, 0, 0, 0), (2, -1, 3, 0, 0, 0, 0, 0)]
    minus = [(0, 0, 0, 0, 1, 1, -2, 3), (0, 0, 0, 0, 5, -1, 2, 0)]
    for r in plus + minus:
        pi = atom(sq, s, r)
        assert projector(sq, pi) and is_even(pi) and pi[()] == F(1, 8)
    assert dot(plus[0], plus[1]) == 0 and dot(minus[0], minus[1]) == 0
    assert GA.is_zero(prod(sq, atom(sq, s, plus[0]), atom(sq, s, plus[1])))
    for a in plus:
        for b in minus:
            assert GA.is_zero(prod(sq, atom(sq, s, a), atom(sq, s, b)))
            assert projector(sq, GA.add(atom(sq, s, a), atom(sq, s, b)))
    mixed = atom(sq, s, (1, 0, 0, 0, 1, 0, 0, 0))
    assert projector(sq, mixed) and not is_even(mixed)
    # a linear map on the even subalgebra: L(x) = 8 <R x>_0 with R = sum rho_IJ s_I s_J^dagger, rho in two blocks
    rho = [[F(0)] * 8 for _ in range(8)]
    for i in range(4):
        for j in range(4):
            rho[i][j] = F((i + 1) * (j + 1), 5) + (2 if i == j else 0)
            rho[4 + i][4 + j] = F(i + j, 3) - (1 if i == j else 0)
    big_r = GA.add(*[GA.scal(rho[i][j], prod(sq, s[i], dagger(s[j], sq)))
                     for i in range(8) for j in range(8) if rho[i][j] != 0])
    assert is_even(big_r)

    def weight(x):
        return 8 * prod(sq, big_r, x).get((), F(0))

    def form(r):
        return sum(rho[i][j] * r[i] * r[j] for i in range(8) for j in range(8)) / dot(r, r)

    for r in plus + minus:
        assert weight(atom(sq, s, r)) == form(r)
    assert weight(atom(sq, s, plus[0])) == F(61, 30) and weight(atom(sq, s, minus[0])) == F(-1, 5)
    half = GA.scal(F(1, 2), GA.add(ONE, gamma))
    assert weight(half) == sum(rho[i][i] for i in range(4)) == 14
    assert weight(ONE) - weight(half) == sum(rho[i][i] for i in range(4, 8)) == 0
    # the twenty values at e_I and e_I + e_J inside the blocks give rho back
    for block in (range(4), range(4, 8)):
        for i in block:
            ei = tuple(1 if k == i else 0 for k in range(8))
            assert weight(atom(sq, s, ei)) == rho[i][i]
            for j in block:
                if j > i:
                    pair = tuple(1 if k in (i, j) else 0 for k in range(8))
                    assert (2 * weight(atom(sq, s, pair)) - rho[i][i] - rho[j][j]) / 2 == rho[i][j]
    # the sign is not implied: this linear weight is negative on an even projector
    assert weight(atom(sq, s, (0, 0, 0, 0, 1, 0, 0, 0))) == -1
    return True


def check_two_modes_have_blocks_of_size_two_and_a_parity_weight_on_a_block_is_additive_and_not_linear():
    premise("synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four")
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    sq, p0, subsets, s, gamma = modes(2)
    assert len(s) == 4 and [len(sub) for sub in subsets] == [0, 2, 1, 1] and p0[()] == F(1, 4)
    half = GA.scal(F(1, 2), GA.add(ONE, gamma))

    def weight(a, b):
        """On the rays of a block: 1, 0 or 1/2 by the parities of the primitive integer vector."""
        assert (a % 2, b % 2) != (0, 0)
        return {(1, 0): F(1), (0, 1): F(0), (1, 1): F(1, 2)}[(a % 2, b % 2)]

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    box = 7
    count = 0
    for a in range(-box, box + 1):
        for b in range(-box, box + 1):
            if gcd(a, b) == 1:
                assert weight(a, b) + weight(-b, a) == 1
                count += 1
    assert count == 144
    for a, b in [(1, 2), (3, 1), (2, 5)]:
        e1 = atom(sq, s, (a, b, 0, 0))
        e2 = atom(sq, s, (-b, a, 0, 0))
        assert projector(sq, e1) and is_even(e1) and GA.is_zero(prod(sq, e1, e2)) and GA.eq(GA.add(e1, e2), half)
    # the only quadratic candidate, fixed by the values at (1,0), (0,1), (1,1), is r_0^2 / r.r
    rho = [[weight(1, 0), (2 * weight(1, 1) - weight(1, 0) - weight(0, 1)) / 2], [F(0), weight(0, 1)]]
    rho[1][0] = rho[0][1]
    assert rho == [[1, 0], [0, 0]]
    assert weight(1, 2) == 1 and (rho[0][0] * 1 + 2 * rho[0][1] * 2 + rho[1][1] * 4) / 5 == F(1, 5)
    return True
