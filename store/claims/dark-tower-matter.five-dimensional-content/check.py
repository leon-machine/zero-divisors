"""dark-tower-matter.five-dimensional-content: exact checks.

The state space Lambda(C^1 + C^3) is enumerated as the subsets of four modes (the slot and three pairs):
a state is (s, P) with s in {0, 1} the slot occupation and P a subset of the pairs, k = |P|.
- 16 = 2^4 states; Y = s - k/3; the complement (s, P) -> (1 - s, complement of P) negates Y and sends
  k to 3 - k, which conjugates the colour representation (Lambda^k C^3: 1, 3, 3bar, 1 for k = 0..3, the
  triality k mod 3 negated); so the 16 states are eight species-states and their conjugates, grouped by
  (|Y|, colour dimension) into exactly four vector-like Dirac species U (3, 2/3), D (3, -1/3), E (1, -1),
  N (1, 0) with the stated states (s, k), and the neutral N is the empty state and the full row (1, 3).
- The charges are those of one generation without the weak doublet: u_R 2/3, d_R -1/3, e_R -1, nu_R 0.
- The centre lambda 1_3 of U(3), acting through the section B -> ((det B)^-1, B), multiplies the slot by
  det^-1 = lambda^-3 and each occupied pair by lambda: the exponent on (s, k) is k - 3s = -3Y for all 16,
  so 3Y is an integer with 3Y + k = 3s = 0 mod 3: the U(3) lattice, satisfied by every state.
Premises: the three-dimensional content (the slot-pair construction), the gauge algebra u(3) (the
group acting) and Hypothesis (S) (the state space is the exterior algebra of slot plus pairs).
EXPORTS["species"]() gives {name: (colour dimension, Y, [(s, k), ...])}.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from pyutil import get_or_set
from tp_premise import premise

COLOUR_DIM = {0: 1, 1: 3, 2: 3, 3: 1}


def states():
    out = []
    for s in (0, 1):
        for k in range(4):
            for P in combinations(range(3), k):
                out.append((s, P))
    return out


def Y(s, k):
    return F(s) - F(k, 3)


def species():
    """Group the 16 states by (|Y|, colour dimension); the listed species-state is the colour triplet
    (k = 1) for coloured species and the s = 0 state for singlets (the table's convention)."""
    groups = {}
    for s, P in states():
        k = len(P)
        get_or_set(groups, (abs(Y(s, k)), COLOUR_DIM[k]), set()).add((s, k))
    named = {}
    for (aY, cdim), sk in groups.items():
        rep = next(t for t in sorted(sk) if (t[1] == 1 if cdim == 3 else t[0] == 0))
        name = {(3, F(2, 3)): "U", (3, F(-1, 3)): "D", (1, F(-1)): "E", (1, F(0)): "N"}[(cdim, Y(*rep))]
        named[name] = (cdim, Y(*rep), sorted(sk))
    return named


def check_sixteen_states_four_species():
    premise("dark-tower-matter.hypothesis-s-slot-statistics")
    premise("dark-tower-matter.three-dimensional-content")
    st = states()
    ok = len(st) == 16
    pairs = set()
    for s, P in st:
        k = len(P)
        Pc = tuple(i for i in range(3) if i not in P)
        ok = ok and Y(1 - s, 3 - k) == -Y(s, k) and COLOUR_DIM[3 - k] == COLOUR_DIM[k]
        ok = ok and (-(3 - k)) % 3 == k % 3 and (1 - s, Pc) in st
        pairs.add(frozenset([(s, P), (1 - s, Pc)]))
    ok = ok and len(pairs) == 8
    sp = species()
    want = {"U": (3, F(2, 3), [(0, 2), (1, 1)]), "D": (3, F(-1, 3), [(0, 1), (1, 2)]),
            "E": (1, F(-1), [(0, 3), (1, 0)]), "N": (1, F(0), [(0, 0), (1, 3)])}
    ok = ok and sp == want
    mult = sum(COLOUR_DIM[k] for sp_ in sp.values() for s, k in sp_[2])
    ok = ok and mult == 16
    sm = {"U": F(2, 3), "D": F(-1, 3), "E": F(-1), "N": F(0)}
    ok = ok and all(sp[nm][1] == sm[nm] for nm in sm)
    GA.check("prop:content5: 16 states, complement negates Y and conjugates colour; species U (3, 2/3), D (3, -1/3), "
             "E (1, -1), N (1, 0), the charges of a generation without the doublet", ok)
    return ok


def check_centre_acts_by_minus_three_y():
    premise("dark-tower-matter.gauge-algebras")
    ok = True
    for s, P in states():
        k = len(P)
        exponent = -3 * s + k * 1
        ok = ok and exponent == -3 * Y(s, k) and (3 * Y(s, k)).denominator == 1
        ok = ok and (3 * Y(s, k) + k) % 3 == 0 and 3 * Y(s, k) + k == 3 * s
    GA.check("prop:content5: the centre of U(3) acts by lambda^(k - 3s) = lambda^(-3Y); 3Y + k = 0 mod 3 on all states",
             ok)
    return ok


EXPORTS = {"species": species}
