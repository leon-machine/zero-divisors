"""one-relation.imported-flag-arrow-superselection: exact checks of the finite content (GA blade engine).

Most of this Fact is premises and a declared stance (CPT covariance, Hypothesis (S), the flag as a datum,
the inherited asymmetry, the superselection of tower charge), which are not computable. Its finite core,
the Witt flag on the three-pair structure and its single orientation bit, is checked on the split real form
Cl(3,3) with pairs e_(2k) (square +1), e_(2k+1) (square -1), v_k = (e_(2k) + e_(2k+1))/2,
w_k = (e_(2k) - e_(2k+1))/2:
(1) v_k, w_k are null with v_k w_k + w_k v_k = 1 and different pairs anticommute; the 8 choices of half of each
    pair give the products psi = u_1 u_2 u_3 (u_k in {v_k, w_k}), each nonzero and annihilated (on the left)
    by its own three null vectors.
(2) The volume element omega (omega^2 = 1) acts on each psi by a sign; the 8 choices split 4 / 4, and the
    sign is (-1)^(number of w's) times that of v1v2v3: one bit, the family (orientation) of the flag.
(3) The flag conjugate v_k <-> w_k for all three pairs (the reflections e_(2k+1) -> -e_(2k+1), an isometry)
    is multiplicative on all blade pairs, exchanges v1v2v3 and w1w2w3 and reverses the bit (three swaps);
    swapping the halves of any two pairs keeps it. The bit is a Z_2 orientation, not a frame vector.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = (1, -1, 1, -1, 1, -1)
OMEGA = {tuple(range(6)): F(1)}


def pair(k):
    a, b = GA.gen(2 * k), GA.gen(2 * k + 1)
    return GA.scal(F(1, 2), GA.add(a, b)), GA.scal(F(1, 2), GA.sub(a, b))


def conjugate(x, ks=(0, 1, 2)):
    flips = {2 * k + 1 for k in ks}
    return {b: c * (-1) ** sum(1 for i in b if i in flips) for b, c in x.items()}


def psi_of(choice):
    out = GA.sc(1)
    for k, c in enumerate(choice):
        out = GA.mul(out, pair(k)[c], SQ)
    return out


def bit(psi):
    w = GA.mul(OMEGA, psi, SQ)
    if w == psi:
        return 1
    if w == GA.neg(psi):
        return -1
    return 0


def check_witt_flags_of_three_pairs():
    premise("dark-matter.orientation-arrow-seventeenth-refutation")
    ok = True
    for k in range(3):
        v, w = pair(k)
        ok = ok and GA.mul(v, v, SQ) == {} and GA.mul(w, w, SQ) == {}
        ok = ok and GA.add(GA.mul(v, w, SQ), GA.mul(w, v, SQ)) == GA.sc(1)
        for j in range(3):
            if j != k:
                ok = ok and all(GA.anticommutes(x, y, SQ) for x in pair(k) for y in pair(j))
    choices = list(product((0, 1), repeat=3))
    ok = ok and len(choices) == 8
    for ch in choices:
        psi = psi_of(ch)
        ok = ok and psi != {}
        ok = ok and all(GA.mul(pair(k)[ch[k]], psi, SQ) == {} for k in range(3))
    GA.check("three null pairs; the 8 half-choices give nonzero pure products killed by their own halves", ok)
    return ok


def check_single_orientation_bit():
    premise("dark-matter.orientation-arrow-seventeenth-refutation")
    ok = True
    ok = ok and GA.mul(OMEGA, OMEGA, SQ) == GA.sc(1)
    bits = {ch: bit(psi_of(ch)) for ch in product((0, 1), repeat=3)}
    ok = ok and sorted(bits.values()) == [-1] * 4 + [1] * 4
    base = bits[(0, 0, 0)]
    ok = ok and all(b == base * (-1) ** sum(ch) for ch, b in bits.items())
    GA.check("the volume element splits the 8 flags 4/4: one orientation bit, (-1)^(number of w's)", ok)
    return ok


def check_conjugate_reverses_bit():
    premise("dark-matter.orientation-arrow-seventeenth-refutation")
    ok = True
    for a in GA.all_blades(6):
        for b in GA.all_blades(6):
            x, y = {a: F(1)}, {b: F(1)}
            ok = ok and conjugate(GA.mul(x, y, SQ)) == GA.mul(conjugate(x), conjugate(y), SQ)
    v123, w123 = psi_of((0, 0, 0)), psi_of((1, 1, 1))
    ok = ok and conjugate(v123) == w123 and conjugate(w123) == v123
    ok = ok and bit(conjugate(v123)) == -bit(v123)
    for ch in product((0, 1), repeat=3):
        psi = psi_of(ch)
        ok = ok and bit(conjugate(psi)) == -bit(psi)
        ok = ok and all(bit(conjugate(psi, ks)) == bit(psi) for ks in ((0, 1), (0, 2), (1, 2)))
    GA.check("the flag conjugate exchanges v1v2v3 and w1w2w3 and reverses the bit; two swaps keep it", ok)
    return ok
