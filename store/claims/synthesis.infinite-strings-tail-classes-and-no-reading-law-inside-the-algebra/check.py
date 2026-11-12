"""synthesis.infinite-strings-tail-classes-and-no-reading-law-inside-the-algebra: exact checks.

Finite floors only. Clifford side: Cl_Q(n,n), generators e_1, f_1, e_2, f_2, ... (squares +1, -1),
v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2, on_j = v_j w_j, off_j = w_j v_j, the adjoint of (P).
Fock side (lib/fock.py, LSB bitmask basis): v_j the creation, w_j the annihilation on rung j.
"""
from fractions import Fraction as F
from itertools import combinations, product
import GA
import fock
from GA import add, sub, scal, mul, gen, sc
from tp_premise import premise


# ---------------------------------------------------------------- Clifford side
def sq(n):
    return tuple([1, -1] * n)


def e(j):
    return gen(2 * j)


def f(j):
    return gen(2 * j + 1)


def v(j):
    return scal(F(1, 2), add(e(j), f(j)))


def w(j):
    return scal(F(1, 2), sub(e(j), f(j)))


def blades(idx):
    return [{tuple(c): F(1)} for r in range(len(idx) + 1) for c in combinations(idx, r)]


def dagger(x):
    out = {}
    for b, c in x.items():
        g = len(b)
        out[b] = c * F(-1) ** (g * (g - 1) // 2) * F(-1) ** sum(1 for i in b if i % 2 == 1)
    return out


def flip(x, which):
    return {b: c * F(-1) ** sum(1 for i in b if i in which) for b, c in x.items()}


def s0(x):
    return x.get((), F(0))


def is_even(x):
    return all(len(k) % 2 == 0 for k in x)


def string_proj(s, S):
    P = sc(1)
    for j, bit in enumerate(s):
        P = mul(P, mul(v(j), w(j), S) if bit else mul(w(j), v(j), S), S)
    return P


# ---------------------------------------------------------------- Fock side
def vadd(*vs):
    out = {}
    for x in vs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def vsc(c, x):
    return {k: F(c) * cc for k, cc in x.items()} if c != 0 else {}


def ip(x, y):
    return sum(c * y.get(k, F(0)) for k, c in x.items())


def cre(k, x):
    return fock.cre_on(k, x)


def ann(k, x):
    return fock.ann_on(k, x)


def num(k, x):
    return cre(k, ann(k, x))


OPS = (lambda k, x: x, cre, ann, num)


def apply_word(word, rungs, x):
    for op, k in zip(word, rungs):
        x = OPS[op](k, x)
        if not x:
            break
    return x


def hop_rotor(a, b, c, s, x):
    """(1 - Pi) + c Pi + s (v_a w_b - v_b w_a) on the rungs a, b; Pi the one-quantum test of the two rungs."""
    na, nb = num(a, x), num(b, x)
    Pi = vadd(na, nb, vsc(-2, num(a, nb)))
    h = vadd(cre(a, ann(b, x)), vsc(-1, cre(b, ann(a, x))))
    return vadd(x, vsc(-1, Pi), vsc(c, Pi), vsc(s, h))


def controlled(a, b, c, s, x):
    """off_0 + on_0 R_(a,b)."""
    on = num(0, x)
    return vadd(x, vsc(-1, on), hop_rotor(a, b, c, s, on))


def check_strings_under_finite_changes_and_under_all_sign_changes():
    premise("synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    n = 3
    S = sq(n)
    strings = list(product((0, 1), repeat=n))
    P = {s: string_proj(s, S) for s in strings}
    ok = True
    for j in range(n):
        ej = e(j)
        ok = ok and mul(ej, ej, S) == sc(1) and dagger(ej) == ej and not is_even(ej)
        for s in strings:
            t = tuple(b ^ (1 if i == j else 0) for i, b in enumerate(s))
            # conjugation by the odd unitary e_j changes the value of rung j and no other (group G2)
            ok = ok and mul(mul(ej, P[s], S), ej, S) == P[t]
            # so does the sign change of f_j (groups G1 and G3)
            ok = ok and flip(P[s], {2 * j + 1}) == P[t]
    # an element of the floor of the first two rungs, even or odd, commutes with the tests of rung 3:
    # conjugation by it cannot change the value of a rung outside its floor
    on3 = mul(v(2), w(2), S)
    for b in blades(range(4)):
        ok = ok and mul(b, on3, S) == mul(on3, b, S)
    # the sign change of all f_j at once maps every string to its complement (an element of G3 that
    # on the infinite tower changes infinitely many rungs)
    allf = {2 * j + 1 for j in range(n)}
    ok = ok and all(flip(P[s], allf) == P[tuple(1 - b for b in s)] for s in strings)
    ok = ok and all(dagger(flip(b, allf)) == flip(dagger(b), allf) for b in blades(range(2 * n)))
    GA.check("finite changes of a string are conjugations by e_j or sign changes of f_j; none reaches beyond its floor", ok)
    return ok


def check_no_element_connects_strings_that_differ_beyond_its_support():
    premise("tower.fock-module-one-qubit-per-rung")
    m = 4
    ok = True
    zero_cases, nonzero_inside = 0, 0
    states = list(range(2 ** m))
    for word in product(range(4), repeat=2):                 # a full basis of the algebra on rungs 0, 1
        for s in states:
            xs = apply_word(word, [0, 1], {s: F(1)})
            for t in states:
                val = xs.get(t, F(0))                         # <t| x |s>
                if (s ^ t) & 0b1100:                          # the strings differ on rung 2 or 3
                    ok = ok and val == 0
                    zero_cases += 1
                elif val != 0:
                    nonzero_inside += 1
    ok = ok and zero_cases == 16 * 16 * 12 and nonzero_inside == NONZERO_INSIDE
    GA.check("no element on rungs 0, 1 has a nonzero value between strings that differ on rung 2 or 3", ok)
    return ok


NONZERO_INSIDE = 100     # per rung the basis 1, v, w, v w has 2 + 1 + 1 + 1 = 5 nonzero entries; 5 * 5 * 4 states of rungs 2, 3


def check_even_atoms_other_than_strings_also_average_to_the_symmetric_state():
    premise("synthesis.premise-positivity-of-values")
    premise("synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight")
    S = sq(2)
    one = sc(1)
    P0 = string_proj((0, 0), S)
    ys = [add(P0, mul(mul(v(0), v(1), S), P0, S)), sub(P0, mul(mul(v(0), v(1), S), P0, S)),
          mul(add(v(0), v(1)), P0, S), mul(sub(v(0), v(1)), P0, S)]
    atoms = [scal(F(1, 2), mul(y, dagger(y), S)) for y in ys]
    ok = True
    for i, A in enumerate(atoms):
        ok = ok and mul(A, A, S) == A and dagger(A) == A and is_even(A) and s0(A) == F(1, 4)
        for j, B in enumerate(atoms):
            if i != j:
                ok = ok and mul(A, B, S) == {}
    ok = ok and add(*atoms) == one
    # their uniform average has density 1/4: the symmetric state, the same as the average of the four strings
    strings = [string_proj(s, S) for s in product((0, 1), repeat=2)]
    ok = ok and scal(F(1, 4), add(*atoms)) == scal(F(1, 4), add(*strings)) == scal(F(1, 4), one)
    # none of the four is a string state: each gives two strings the weight 1/2
    for A in atoms:
        wts = sorted(s0(mul(A, Ps, S)) / s0(A) for Ps in strings)
        ok = ok and wts == [F(0), F(0), F(1, 2), F(1, 2)]
    # the multi-mode descent sends each to an equal mixture of two strings
    for A in atoms:
        EA = add(*[mul(mul(Ps, A, S), Ps, S) for Ps in strings])
        parts = [Ps for Ps in strings if s0(mul(A, Ps, S)) != 0]
        ok = ok and len(parts) == 2 and EA == scal(F(1, 2), add(*parts))
    GA.check("four even atoms that are not strings are orthogonal, sum to 1 and average to the symmetric state", ok)
    return ok


UNIT_VECTORS = ((F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)), (F(4, 5), F(3, 5)), (F(5, 13), F(12, 13)),
                (F(-3, 5), F(4, 5)), (F(8, 17), F(15, 17)))


def check_weight_after_a_coupling_is_a_quadratic_form_and_is_not_two_valued():
    premise("synthesis.premise-positivity-of-values")
    ok = True
    c, s = F(3, 5), F(4, 5)
    couplings = {
        "controlled rotor of the fresh pair": lambda x: controlled(2, 3, c, s, x),
        "controlled exchange of the fresh pair": lambda x: controlled(2, 3, F(0), F(1), x),
        "rotor between system rung 1 and fresh rung 2": lambda x: hop_rotor(1, 2, c, s, x),
        "both in turn": lambda x: hop_rotor(1, 2, c, s, controlled(2, 3, c, s, x)),
    }
    tests = {"on_0": lambda x: num(0, x), "on_1": lambda x: num(1, x), "on_2": lambda x: num(2, x),
             "on_0 on_3": lambda x: num(0, num(3, x)), "off_1 on_2": lambda x: vadd(num(2, x), vsc(-1, num(1, num(2, x))))}
    forms = 0
    constant = 0
    for data in range(4):                                     # the four strings of the fresh pair (rungs 2, 3)
        base = {data << 2: F(1)}
        phi = [cre(0, base), cre(1, base)]                    # system quantum on rung 0, on rung 1
        for U in couplings.values():
            out = [U(p) for p in phi]
            ok = ok and ip(out[0], out[0]) == 1 and ip(out[1], out[1]) == 1 and ip(out[0], out[1]) == 0
            for E in tests.values():
                M = [[ip(out[i], E(out[j])) for j in range(2)] for i in range(2)]
                ok = ok and M[0][1] == M[1][0]
                forms += 1
                q = [a * a * M[0][0] + 2 * a * b * M[0][1] + b * b * M[1][1] for a, b in UNIT_VECTORS]
                # the weight of the test for the input a phi_0 + b phi_1 is this quadratic form
                for (a, b), qv in zip(UNIT_VECTORS, q):
                    psi = vadd(vsc(a, phi[0]), vsc(b, phi[1]))
                    ok = ok and ip(U(psi), E(U(psi))) == qv and 0 <= qv <= 1
                is_const = M[0][1] == 0 and M[0][0] == M[1][1]
                two_valued_points = sum(1 for qv in q if qv in (F(0), F(1)))
                # a form that is not a multiple of the unit form is 0 or 1 at no more than four directions
                ok = ok and (is_const or two_valued_points <= 4)
                # and if it is 0 or 1 at all seven directions it is constant
                ok = ok and (two_valued_points < 7 or is_const)
                constant += 1 if is_const else 0
    ok = ok and forms == 80 and constant == CONSTANT_FORMS
    # the seven directions are pairwise different points of the projective line
    for (a1, b1), (a2, b2) in combinations(UNIT_VECTORS, 2):
        ok = ok and a1 * b2 - a2 * b1 != 0
    ok = ok and all(a * a + b * b == 1 for a, b in UNIT_VECTORS)
    GA.check("for 4 data strings, 4 couplings, 5 tests: the weight is a quadratic form, two-valued only when constant", ok)
    return ok


CONSTANT_FORMS = 13      # of the 80 forms, those that are a multiple of the unit form (recorded from the computation)


def check_reading_until_decided_gives_the_prescribed_weight():
    premise("synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws")
    p = F(9, 25)
    digits = []
    x = p
    for _ in range(20):
        x = 2 * x
        d = 1 if x >= 1 else 0
        digits.append(d)
        x -= d
    ok = x == p                                              # the binary expansion of 9/25 has period 20
    one_period = sum(F(d, 2 ** (k + 1)) for k, d in enumerate(digits))
    ok = ok and one_period / (1 - F(1, 2 ** 20)) == p        # sum over all k of d_k 2^-k
    # rule: read unbiased values b_1, b_2, ...; stop at the first k with b_k != d_k; outcome a if b_k < d_k.
    # exact enumeration of all prefixes of length 12
    n = 12
    won = undecided = 0
    reads_total = 0
    for bits in product((0, 1), repeat=n):
        k = next((i for i in range(n) if bits[i] != digits[i]), None)
        if k is None:
            undecided += 1
            reads_total += n
        else:
            reads_total += k + 1
            if bits[k] < digits[k]:
                won += 1
    ok = ok and undecided == 1
    ok = ok and F(won, 2 ** n) == sum(F(d, 2 ** (k + 1)) for k, d in enumerate(digits[:n]))
    ok = ok and F(won, 2 ** n) <= p <= F(won + undecided, 2 ** n)
    # mean number of reads, truncated at n: 2 - 2^(1-n); the limit is 2
    ok = ok and F(reads_total, 2 ** n) == 2 - F(2, 2 ** n)
    # a fixed number n of reads gives only weights with denominator 2^n; 9/25 is not one of them
    ok = ok and all((p * 2 ** k).denominator != 1 for k in range(1, 41))
    GA.check("reading unbiased values until decided gives exactly 9/25, mean 2 reads; no bounded number of reads does", ok)
    return ok
