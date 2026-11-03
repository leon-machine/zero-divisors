"""standard-model.under-s-state-space-complete-multiplets: exact checks.

The state space Lambda(C^2 + C^3) is built as the 32 occupation states of five modes, slots 0, 1 and
pairs 2, 3, 4 (j = occupied slots, k = occupied pairs). On a state the Cartan generators act by
eigenvalues: weak T_3 = (n_0 - n_1)/2, colour H = (n_2 - n_3)/2 (a normalised su(3) Cartan,
tr H^2 = 1/2 on the triplet), hypercharge Y = (3j - 2k)/6 (the weight 3j - 2k of the premise).
Indices are traces of squares over the states, T_1 = (3/5) sum Y^2, T_2 = sum T_3^2, T_3 = sum H^2,
and the Weyl shift is Dl = (2/3) T. This computes (1) the 16 + 16 split by total parity, (2) the
hypercharge multisets of the halves, (3) the equal shifts 4/3 of each half and their inertness
(through the one-threshold solver), (4) all 64 sub-multisets of the six components of the even half:
exactly the eight unions of 10 = {Q, u^c, e^c}, 5bar = {L, d^c}, 1 = {nu^c} shift equally.
The final reading sentences (slot-heavy) are interpretation and are not checked.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

MODES = range(5)
SLOTS, PAIRS = (0, 1), (2, 3, 4)
STATES = [frozenset(c) for r in range(6) for c in combinations(MODES, r)]


def jk(S):
    return sum(1 for m in S if m in SLOTS), sum(1 for m in S if m in PAIRS)


def charges(S):
    j, k = jk(S)
    t3 = F((0 in S) - (1 in S), 2)
    h = F((2 in S) - (3 in S), 2)
    return F(3 * j - 2 * k, 6), t3, h


def shift(states):
    """Weyl one-loop shift Dl = (2/3)(T_1, T_2, T_3) from traces over the states."""
    T1 = F(3, 5) * sum(charges(S)[0] ** 2 for S in states)
    T2 = sum(charges(S)[1] ** 2 for S in states)
    T3 = sum(charges(S)[2] ** 2 for S in states)
    return tuple(F(2, 3) * t for t in (T1, T2, T3))


EVEN = [S for S in STATES if len(S) % 2 == 0]
ODD = [S for S in STATES if len(S) % 2 == 1]
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}
COMPONENTS = {name: [S for S in EVEN if jk(S) == key] for key, name in NAMES.items()}


def check_halves_have_sixteen_states():
    premise("standard-model.hyp-s-slot-statistics")
    ok = len(STATES) == 32 and len(EVEN) == 16 and len(ODD) == 16
    ok = ok and sorted(len(v) for v in COMPONENTS.values()) == [1, 1, 2, 3, 3, 6]
    GA.check("state space: 32 states, even half 16, odd half 16", ok)
    return ok


def check_hypercharge_multisets():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.under-s-composites-state-space-spinor")
    gen = sorted([F(1, 6)] * 6 + [F(-1, 2)] * 2 + [F(-2, 3)] * 3 + [F(1, 3)] * 3 + [F(1), F(0)])
    even = sorted(charges(S)[0] for S in EVEN)
    odd = sorted(charges(S)[0] for S in ODD)
    ok = even == gen and odd == sorted(-y for y in gen)
    GA.check("state space: even half has the generation's hypercharges, odd half their negatives", ok)
    return ok


def check_each_half_shifts_equally_and_is_inert():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.complete-multiplets-shift-all-three-coefficients")
    solve = premise("standard-model.one-threshold-exact-criterion")["solve"]
    ok = shift(EVEN) == (F(4, 3),) * 3 and shift(ODD) == (F(4, 3),) * 3
    # 4/3 = (2/3) x 2, the index of the 16 being 2
    ok = ok and shift(EVEN)[0] == F(2, 3) * 2
    # inert: adding a half (or the whole state space) at a common threshold moves no f, x, y
    A = (F(6), F(3), F(1))
    b, d = (F(2), F(1), F(0)), (F(1), F(0), F(0))
    base = solve(A, b, d)
    for extra in (shift(EVEN), shift(STATES)):
        s = solve(A, b, tuple(d[i] + extra[i] for i in range(3)))
        ok = ok and s[0] == base[0] and s[1] == base[1] and s[3] == base[3]
    ok = ok and shift(STATES) == (F(8, 3),) * 3
    GA.check("state space: each half shifts b_1, b_2, b_3 by 4/3 and is inert", ok)
    return ok


def check_exactly_eight_inert_splits():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.under-s-composites-state-space-spinor")
    names = sorted(COMPONENTS)
    inert = []
    count = 0
    for r in range(7):
        for sub in combinations(names, r):
            count += 1
            dd = shift([S for n in sub for S in COMPONENTS[n]])
            if dd[0] == dd[1] == dd[2]:
                inert.append(sorted(sub))
    pieces = [["Q", "e^c", "u^c"], ["L", "d^c"], ["nu^c"]]
    unions = [sorted(sum((pieces[i] for i in range(3) if mask >> i & 1), [])) for mask in range(8)]
    ok = count == 64 and sorted(inert) == sorted(unions) and len(inert) == 8
    # the pieces' own shifts: 10 by 1, 5bar by 1/3 (Weyl), singlet by 0
    ok = ok and shift(COMPONENTS["Q"] + COMPONENTS["u^c"] + COMPONENTS["e^c"]) == (F(1),) * 3
    ok = ok and shift(COMPONENTS["L"] + COMPONENTS["d^c"]) == (F(1, 3),) * 3
    GA.check("state space: of the 64 sub-multisets exactly the 8 unions of 10, 5bar, 1 are inert", ok)
    return ok
