"""dark-matter.asymmetry-arrow-counted-fifteenth-refutation: exact checks of the computable part.

(i) The flag as particle against antiparticle (premise: imported-derived-generation-flag): on the
three-pair Fock ideal built in GA.py (split form (3,3), w_i = (e_i + e_(3+i))/2, v_i = (e_i - e_(3+i))/2,
f = w_1 w_2 w_3, states v_S f), the flag conjugate R = e_3 e_4 e_5 (the versor negating the pair
partners, an isometry carrying W to W') sends the state with creation set S, characterised as the state
killed by exactly the v_i with i in S, to the state with the complementary set, exchanging Fock grades
k and 3 - k (in particular the singlets 0 and 3); R^2 = 1 and its twisted adjoint action carries
every w_i to v_i.
(ii) The degree count: a theta-term integrates a characteristic class of top degree over the tower;
Chern classes have degree 2k and Pontryagin classes 4k, so the available degrees are the even ones.
On the P3 representatives of all eight residues (dimensions three, four and five, taken from the census
rule) a theta-term exists exactly at the even residues, and that set equals the set where the flag bit
exists (premise: flag-bit-exists-exactly-tower-dimension, the bit at dimension 0 mod 4). The coincidence
is a fact about the P3 window: in dimensions 2 and 6 an even-degree class exists while the bit does not,
which is also checked, so the statement is read at the representatives, as the claim does.
(iii) Confinement: the towers carrying the bit and a single time ((min(p,q) = 1) are r = 6, 2 only.
Not computed: the neutron-dipole bound (it rests on a hadronic matrix element not stated in the claim),
the stance on epsilon, and the democracy premise P4 (a premise, not a computation).
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise

SIGS = [(p, q) for p in range(7) for q in range(7) if 1 <= p + q <= 6]


def p3(r):
    if r % 2 == 0:
        return sorted(s for s in SIGS if sum(s) == 4 and (s[0] - s[1]) % 8 == r)
    three = [s for s in SIGS if sum(s) == 3 and (s[0] - s[1]) % 8 == r]
    if any(min(s) == 1 for s in three):
        return sorted(three)
    return sorted(s for s in SIGS if sum(s) == 5 and (s[0] - s[1]) % 8 == r)


def class_degrees(top):
    chern = {2 * k for k in range(1, top + 1)}
    pontryagin = {4 * k for k in range(1, top + 1)}
    return {d for d in chern | pontryagin if d <= top}


def check_flag_conjugate_is_particle_antiparticle():
    premise("dark-matter.imported-derived-generation-flag")
    sq = GA.sig(3, 3)
    w = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(3 + i))) for i in range(3)]
    v = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(3 + i))) for i in range(3)]
    f = GA.mul(GA.mul(w[0], w[1], sq), w[2], sq)
    R = GA.mul(GA.mul(GA.gen(3), GA.gen(4), sq), GA.gen(5), sq)

    def st(S):
        y = f
        for i in reversed(S):
            y = GA.mul(v[i], y, sq)
        return y

    def index_set(psi):
        return frozenset(i for i in range(3) if GA.is_zero(GA.mul(v[i], psi, sq)))
    ok = GA.eq(GA.mul(R, R, sq), GA.sc(1))
    # the twisted adjoint action x -> -R x R^-1 of the odd versor R carries w_i to v_i
    Rinv = R
    ok = ok and (len(w) == len(v) and all(GA.eq(GA.neg(GA.mul(GA.mul(R, x, sq), Rinv, sq)), y) for x, y in zip(w, v)))
    count = 0
    for k in range(4):
        for S in combinations(range(3), k):
            s = st(S)
            Rs = GA.mul(R, s, sq)
            ok = ok and not GA.is_zero(s) and not GA.is_zero(Rs)
            ok = ok and index_set(s) == frozenset(S)
            ok = ok and index_set(Rs) == frozenset(range(3)) - frozenset(S)
            count += 1
    ok = ok and count == 8
    GA.check("prop:arrow(i): the flag conjugate e3 e4 e5 maps creation set S to its complement (grades k <-> 3 - k) "
             "on all 8 Fock states, R^2 = 1, w_i -> v_i", ok)
    return ok


def check_theta_exists_exactly_where_the_bit_does():
    premise("dark-matter.flag-bit-exists-exactly-tower-dimension")
    reps = {r: p3(r) for r in range(8)}
    dims = {r: {p + q for p, q in reps[r]} for r in range(8)}
    ok = dims == {0: {4}, 1: {3}, 2: {4}, 3: {5}, 4: {4}, 5: {5}, 6: {4}, 7: {3}}
    theta = sorted(r for r in range(8) if all(d in class_degrees(d) for d in dims[r]))
    bit = sorted(r for r in range(8) if all(d % 4 == 0 for d in dims[r]))
    ok = ok and theta == [0, 2, 4, 6] and bit == theta
    ok = ok and all(d % 2 == 0 for d in class_degrees(12)) and 3 not in class_degrees(5) and 5 not in class_degrees(5)
    off_window = {d: (d in class_degrees(d), d % 4 == 0) for d in (2, 6)}
    ok = ok and off_window == {2: (True, False), 6: (True, False)}
    GA.check("prop:arrow(ii): at the P3 representatives a theta-term (even top degree) exists exactly at "
             "r = 0, 2, 4, 6, where the bit does; odd towers none (dimensions 2, 6 differ off the window)", ok)
    return ok


def check_asymmetry_confined_to_this_tower_and_the_mirror():
    premise("dark-matter.flag-bit-exists-exactly-tower-dimension")
    reps = {r: p3(r) for r in range(8)}
    carriers = sorted(r for r in range(8)
                      if all((p + q) % 4 == 0 for p, q in reps[r]) and any(min(p, q) == 1 for p, q in reps[r]))
    ok = carriers == [2, 6] and (1, 3) in reps[6] and (3, 1) in reps[2]
    ok = ok and all((p + q) % 2 == 1 for r in (1, 3, 5, 7) for p, q in reps[r])
    GA.check("prop:arrow(iii): oriented causal towers are r = 6 (1,3) and r = 2 (3,1); odd towers carry none", ok)
    return ok
