"""dark-tower-matter.imported-towers-their-types: exact checks of the computable clauses.

(1) The residue p - q mod 8 is constant along (1,1) ascents: adjoining k null pairs (Gram blocks
    [[0,1],[1,0]]) to diag(+1 x p, -1 x q) gives congruence signature (p + k, q + k), for every
    (p,q) with p + q <= 6 and k = 1, 2, 3.
(2) Under the P3 rule (dimension four for even residues; for odd ones dimension three where a
    single-time signature exists there, else the single-time signatures of dimension five) the
    representatives over all signatures with 1 <= p + q <= 10 are exactly the stated ones; the
    residues with no single-time representative are 0 and 4 (sterile).
(3) The odd residues carry no orientation bit: the bit exists exactly at tower dimension 0 mod 4
    (the flag-bit theorem); every signature of an odd residue has odd dimension (checked for all
    p + q <= 10), and there the volume element is central (blade-wise, for every odd-residue
    signature with p + q <= 7), while the even-residue representatives all sit at dimension 4.
Not computable here: exact superselection (the towers interact only through the one metric).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

NMAX = 10
SIGS = [(p, q) for p in range(NMAX + 1) for q in range(NMAX + 1) if 1 <= p + q <= NMAX]
STATED = {6: [(1, 3)], 2: [(3, 1)], 0: [(2, 2)], 4: [(0, 4), (4, 0)],
          1: [(2, 1)], 7: [(1, 2)], 3: [(4, 1)], 5: [(1, 4)]}


def res(p, q):
    return (p - q) % 8


def causal(p, q):
    return min(p, q) == 1


def representatives(r):
    if r % 2 == 0:
        return sorted(s for s in SIGS if sum(s) == 4 and res(*s) == r)
    three = [s for s in SIGS if sum(s) == 3 and res(*s) == r and causal(*s)]
    if three:
        return sorted(three)
    return sorted(s for s in SIGS if sum(s) == 5 and res(*s) == r and causal(*s))


def ascend(p, q, k):
    n = p + q
    G = [[F(0)] * (n + 2 * k) for _ in range(n + 2 * k)]
    for i in range(n):
        G[i][i] = F(1 if i < p else -1)
    for j in range(k):
        a, b = n + 2 * j, n + 2 * j + 1
        G[a][b] = G[b][a] = F(1)
    return GA.congruence_signature(G)


def check_residue_constant_along_ascents():
    premise("tower.rigidity-clock-frozen")
    premise("dark-matter.towers-are-residues-single-clock-filter")
    count = 0
    for n in range(0, 7):
        for p in range(n + 1):
            q = n - p
            for k in (1, 2, 3):
                s = ascend(p, q, k)
                assert s == (p + k, q + k, 0) and res(s[0], s[1]) == res(p, q)
                count += 1
    assert count == 84
    return True


def check_representatives_under_p3():
    premise("dark-matter.p3-nearest-dimension-representatives")
    premise("dark-matter.towers-are-residues-single-clock-filter")
    reps = {r: representatives(r) for r in range(8)}
    assert reps == STATED
    sterile = sorted(r for r in range(8) if not any(causal(*s) for s in reps[r]))
    assert sterile == [0, 4]
    return True


def check_odd_residues_carry_no_bit():
    premise("dark-matter.flag-bit-exists-exactly-tower-dimension")
    premise("dark-matter.p3-nearest-dimension-representatives")
    assert all((p + q) % 2 == 1 for p, q in SIGS if res(p, q) % 2 == 1)
    central = 0
    for n in range(1, 8, 2):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p, q)
            w = {tuple(range(n)): F(1)}
            assert all(GA.commutes(w, GA.gen(i), sq) for i in range(n))
            central += 1
    assert central == 20
    bit = {r: all(sum(s) % 4 == 0 for s in representatives(r)) for r in range(8)}
    assert sorted(r for r in bit if bit[r]) == [0, 2, 4, 6]
    return True
