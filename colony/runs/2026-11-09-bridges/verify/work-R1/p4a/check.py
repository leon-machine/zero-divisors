"""synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element: exact checks.

Two order-four elements whose square is a grading occur in the store. (a) The Klein twist
V = (1 + I k)(1 + I)^{-1} of an even involution k (the grading) with the unit I: checked in Cl(4,1), where
e_1 .. e_4 are the Majorana generators of two modes, the pseudoscalar I is central with I^2 = -1, and
k = e_1e_2e_3e_4. (b) The pseudoscalar omega of the ten Majorana generators of the five modes, in Cl(10,0);
elements of the complexified algebra are pairs (A, B) for A + I B with I a commuting unit. Checks:
  (1) V = p_+ - I p_-, V^2 = k, V commutes with every even element, and Ad_V(e_1) = -I e_1 k is not in the span
      of the generators over span{1, I}: the twist assigns no charge to a generator;
  (2) omega^2 = -1, omega anticommutes with the ten generators and commutes with the 45 bivectors; it is the
      product of the five mode rotors exp((pi/2) e_{2j-1}e_{2j}) = e_{2j-1}e_{2j};
  (3) omega = I Gamma with Gamma the product of (1 - 2 n_j): the same unit I on every even state;
  (4) the Majorana element T = v_1 v_2 v_3 v_4 v_5 is of grade five and omega T omega^{-1} = -T;
  (5) signed sums of the multiplet dimensions (6, 3, 3, 2, 1, 1) and (6, 3, 3, 2, 1).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

MODES = 4
GENS = 2 * MODES
SQ10 = GA.sig(GENS, 0)
SIXTEEN = (6, 3, 3, 2, 1, 1)      # (2,3), (1,3bar), (1,3bar), (2,1), (1,1), (1,1): the sixteen of one generation
FIFTEEN = (6, 3, 3, 2, 1)         # without the neutral singlet
MODULUS = 16


def check_klein_twist_is_a_polynomial_in_the_grading():
    premise("synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics")
    sq = GA.sig(4, 1)
    e = [GA.gen(i) for i in range(5)]
    one = GA.sc(F(1))

    def prod(*xs):
        out = one
        for x in xs:
            out = GA.mul(out, x, sq)
        return out

    I = prod(*e)                                                # central pseudoscalar of Cl(4,1)
    k = prod(e[0], e[1], e[2], e[3])                            # the grading of the two-mode algebra
    assert GA.eq(prod(I, I), GA.neg(one)) and GA.eq(prod(k, k), one)
    for g in e:
        assert GA.commutes(I, g, sq)
    for g in e[:4]:
        assert GA.anticommutes(k, g, sq)                        # generators are odd
    half = F(1, 2)
    V = GA.scal(half, prod(GA.add(one, prod(I, k)), GA.sub(one, I)))        # (1 + I k)(1 + I)^{-1}
    Vinv = GA.scal(half, prod(GA.sub(one, prod(I, k)), GA.add(one, I)))
    p_plus = GA.scal(half, GA.add(one, k))
    p_minus = GA.scal(half, GA.sub(one, k))
    assert GA.eq(prod(V, Vinv), one)
    assert GA.eq(V, GA.sub(p_plus, prod(I, p_minus)))           # V = p_+ - I p_-: a polynomial in k
    assert GA.eq(prod(V, V), k)                                 # order four, square the grading
    for a in range(4):
        for b in range(a + 1, 4):
            assert GA.commutes(V, prod(e[a], e[b]), sq)         # commutes with every even element
    ad = prod(V, e[0], Vinv)
    assert GA.eq(ad, GA.neg(prod(I, e[0], k)))                  # Ad_V(e_1) = -I e_1 k
    grades = set(len(b) for b, c in ad.items() if c != 0)
    assert grades == {2}                                        # e_1 e_5 up to sign: not c e_j or c I e_j (grades 1, 4)
    assert GA.eq(prod(V, V, e[0], Vinv, Vinv), GA.neg(e[0]))    # Ad_V^2 is the grading automorphism
    return True


def blade(*idx):
    out = GA.sc(F(1))
    for i in idx:
        out = GA.mul(out, GA.gen(i), SQ10)
    return out


def check_pseudoscalar_of_the_ten_generators():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    omega = blade(*range(GENS))
    one = GA.sc(F(1))
    assert GA.eq(GA.mul(omega, omega, SQ10), GA.neg(one))       # omega^2 = -1
    for p in range(GENS):
        assert GA.anticommutes(omega, GA.gen(p), SQ10)
    count = 0
    for p in range(GENS):
        for q in range(p + 1, GENS):
            assert GA.commutes(omega, blade(p, q), SQ10)
            count += 1
    assert count == 45
    # omega is the product of the five mode rotors: (e_a e_b)^2 = -1, so exp((pi/2) e_a e_b) = e_a e_b
    rot = one
    for j in range(MODES):
        r = blade(2 * j, 2 * j + 1)
        assert GA.eq(GA.mul(r, r, SQ10), GA.neg(one))
        rot = GA.mul(rot, r, SQ10)
    assert GA.eq(rot, omega)
    return True


def cmul(x, y):
    """(A + I B)(C + I D) with I a commuting unit, I^2 = -1."""
    A, B = x
    C, D = y
    return (GA.sub(GA.mul(A, C, SQ10), GA.mul(B, D, SQ10)), GA.add(GA.mul(A, D, SQ10), GA.mul(B, C, SQ10)))


ZERO = GA.sc(F(0))


def mode_ops(j):
    half = F(1, 2)
    a, b = GA.gen(2 * j), GA.gen(2 * j + 1)
    v = (GA.scal(half, a), GA.scal(half, b))                    # v_j = (e_a + I e_b)/2
    vd = (GA.scal(half, a), GA.scal(-half, b))                  # its adjoint (e_a - I e_b)/2
    return v, vd


def check_pseudoscalar_is_the_unit_times_the_chirality():
    premise("standard-model.majorana-element")
    one = (GA.sc(F(1)), ZERO)
    gamma = one
    for j in range(MODES):
        v, vd = mode_ops(j)
        n = cmul(vd, v)                                         # the number operator of mode j
        assert GA.eq(cmul(n, n)[0], n[0]) and GA.eq(cmul(n, n)[1], n[1])      # a projection
        factor = (GA.sub(one[0], GA.scal(F(2), n[0])), GA.neg(GA.scal(F(2), n[1])))
        gamma = cmul(gamma, factor)
    g2 = cmul(gamma, gamma)
    assert GA.eq(g2[0], one[0]) and GA.is_zero(g2[1])           # Gamma^2 = 1
    omega = blade(*range(GENS))
    i_gamma = (GA.neg(gamma[1]), gamma[0])                      # I Gamma
    assert GA.eq(i_gamma[0], omega) and GA.is_zero(i_gamma[1])  # omega = I Gamma: the unit I on every even state
    return True


def check_majorana_element_is_odd_under_the_pseudoscalar():
    premise("standard-model.majorana-element")
    premise("synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5")
    T = (GA.sc(F(1)), ZERO)
    for j in range(MODES):
        T = cmul(T, mode_ops(j)[0])
    omega = blade(*range(GENS))
    omega_inv = GA.neg(omega)
    for part in T:
        assert not GA.is_zero(part)
        assert set(len(b) for b, c in part.items() if c != 0) == {MODES}      # grade five
        conj = GA.mul(GA.mul(omega, part, SQ10), omega_inv, SQ10)
        assert GA.eq(conj, GA.neg(part))                        # omega T omega^{-1} = -T
    # the mode bivectors: [sum_j e_{2j-1}e_{2j}, T] = c I T with c = 2 * MODES up to the sign convention of v_j,
    # so T has charge 2 under each mode rotor, and every difference of two mode bivectors commutes with T
    def comm(X, part):
        return GA.sub(GA.mul(X, part, SQ10), GA.mul(part, X, SQ10))
    mode_biv = [GA.mul(GA.gen(2 * j), GA.gen(2 * j + 1), SQ10) for j in range(MODES)]
    total = GA.add(*mode_biv)
    i_T = (GA.neg(T[1]), T[0])                                   # I T
    c_re, c_im = comm(total, T[0]), comm(total, T[1])
    weight = 2 * MODES
    plus = GA.eq(c_re, GA.scal(F(weight), i_T[0])) and GA.eq(c_im, GA.scal(F(weight), i_T[1]))
    minus = GA.eq(c_re, GA.scal(F(-weight), i_T[0])) and GA.eq(c_im, GA.scal(F(-weight), i_T[1]))
    assert plus or minus
    for j in range(MODES):
        for l in range(j + 1, MODES):
            d = GA.sub(mode_biv[j], mode_biv[l])
            assert GA.is_zero(comm(d, T[0])) and GA.is_zero(comm(d, T[1]))
    return True


def signed_sums(dims):
    out = []
    for mask in range(2 ** len(dims)):
        out.append(sum(d if (mask >> i) & 1 else -d for i, d in enumerate(dims)))
    return out


def check_signed_dimension_sums_for_fifteen_and_sixteen():
    premise("standard-model.majorana-element")
    s16 = signed_sums(SIXTEEN)
    s15 = signed_sums(FIFTEEN)
    assert sum(SIXTEEN) == MODULUS and sum(FIFTEEN) == MODULUS - 1
    assert all(s % 2 == 1 for s in s15)                         # fifteen: every signed sum is odd
    assert sorted(set(s % MODULUS for s in s16 if s % MODULUS == 0)) == [0]
    zero16 = [s for s in s16 if s % MODULUS == 0]
    assert MODULUS in zero16 and -MODULUS in zero16 and 0 in zero16          # uniform, and balanced choices
    # three fifteen-component generations: no choice of signs gives a multiple of 16, or of 2
    vals15 = sorted(set(s15))
    for a in vals15:
        for b in vals15:
            for c in vals15:
                assert (a + b + c) % 2 == 1
    # two generations can cancel (opposite signs), so the obstruction is for odd numbers of generations
    assert any((a + b) % MODULUS == 0 for a in vals15 for b in vals15)
    # with the same uniform choice in each generation: 15 n_g = 0 mod 16 first at n_g = 16
    assert [g for g in range(1, MODULUS + 1) if (15 * g) % MODULUS == 0] == [MODULUS]
    return True
