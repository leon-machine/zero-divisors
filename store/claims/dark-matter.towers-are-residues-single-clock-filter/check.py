"""dark-matter.towers-are-residues-single-clock-filter: exact checks.

Signatures (p,q) with 1 <= p + q <= 10, residue r = p - q mod 8, causal iff min(p,q) = 1.
- Towers: the rung step (p,q) -> (p+1,q+1) keeps r, and with the period steps (p,q) -> (p+8,q),
  (p,q+8) of the imported mod-8 clock the grid 0 <= p, q <= 16 splits into exactly eight classes (union-find), one per
  residue: the eight towers are the eight residues.
- Convention: reversal sends r to -r, keeps causality, swaps 6 and 2; Cl(1,3) and Cl(3,1) are not
  isomorphic: in GA.py the corner f Cl f of a primitive idempotent (greedy Lounesto construction,
  certified by the signature of the regular trace form) is H for (1,3) and R for (3,1).
- (i) the lowest causal signature per residue; the rule t = 1, s = 1..8 hits every residue causally.
- (ii) under P3 (dimension nearest four; odd residues: three if it has a causal member, else five) the
  representatives are as stated, the sterile set is {0, 4}, and it equals the fixed set of r -> -r.
- (iii) sterile sets of the windows [1,5], [3,6], [3,10], [3,5]; with no lower bound the lowest
  signatures of r = 6, 2 are the definite (0,2), (2,0).
P2 (the convention is indexical) is a reading, not a computation: no premise() call for it.
"""
from fractions import Fraction as F
import GA
from pyutil import get_or_set
from tp_premise import premise

NMAX = 10
SIGS = [(p, q) for p in range(NMAX + 1) for q in range(NMAX + 1) if 1 <= p + q <= NMAX]


GRID = 17


def res(p, q):
    return (p - q) % 8


def causal(p, q):
    return min(p, q) == 1


def p3(r):
    if r % 2 == 0:
        return sorted(s for s in SIGS if sum(s) == 4 and res(*s) == r)
    three = [s for s in SIGS if sum(s) == 3 and res(*s) == r]
    if any(causal(*s) for s in three):
        return sorted(three)
    return sorted(s for s in SIGS if sum(s) == 5 and res(*s) == r)


def sterile_in(lo, hi):
    return sorted(r for r in range(8)
                  if not any(causal(*s) for s in SIGS if lo <= sum(s) <= hi and res(*s) == r))


def corner_type(p, q):
    """Division algebra f Cl(p,q) f for a greedy primitive idempotent, via the trace-form signature."""
    n = p + q
    sq = GA.sig(p, q)
    bl = GA.all_blades(n)

    def co(x):
        return [x.get(b, F(0)) for b in bl]

    def dim_left(f):
        return GA.rank_of_vectors([co(GA.mul({b: F(1)}, f, sq)) for b in bl])
    f, dim, chosen = GA.sc(1), 2 ** n, []
    for b in bl:
        if b and GA.mul({b: F(1)}, {b: F(1)}, sq) == {(): F(1)} and \
                all(GA.commutes({b: F(1)}, {c: F(1)}, sq) for c in chosen):
            f2 = GA.mul(f, GA.scal(F(1, 2), GA.add(GA.sc(1), {b: F(1)})), sq)
            d2 = dim_left(f2)
            if 0 < d2 < dim:
                f, dim, chosen = f2, d2, chosen + [b]
    rows, el = [], []
    for b in bl:
        y = GA.mul(GA.mul(f, {b: F(1)}, sq), f, sq)
        if y and GA.rank_of_vectors(rows + [co(y)]) > len(rows):
            rows.append(co(y))
            el.append(y)
    d = len(el)

    def coords(y):
        M = [[rows[i][k] for i in range(d)] + [co(y)[k]] for k in range(len(bl))]
        kv = next(v for v in GA.field_kernel(M) if v[d] != 0)
        return [-kv[i] / kv[d] for i in range(d)]
    # trace of left multiplication by el_i el_j on the corner
    T = []
    for i in range(d):
        row = []
        for j in range(d):
            x = GA.mul(el[i], el[j], sq)
            row.append(sum(coords(GA.mul(x, el[k], sq))[k] for k in range(d)))
        T.append(row)
    return {(1, 0, 0): "R", (1, 1, 0): "C", (1, 3, 0): "H"}.get(tuple(GA.congruence_signature(T))), dim


def check_towers_are_the_eight_residues():
    premise("dark-matter.imported-eight-towers-mod-8-clock")
    ok = all(res(p + 1, q + 1) == res(p, q) for p, q in SIGS)
    grid = [(p, q) for p in range(GRID) for q in range(GRID)]
    parent = {s: s for s in grid}

    def find(s):
        while parent[s] != s:
            s = parent[s]
        return s
    for p, q in grid:
        for t in ((p + 1, q + 1), (p + 8, q), (p, q + 8)):
            if t in parent:
                parent[find(t)] = find((p, q))
    classes = {}
    for s in grid:
        get_or_set(classes, find(s), set()).add(res(*s))
    ok = ok and len(classes) == 8 and all(len(v) == 1 for v in classes.values())
    ok = ok and sorted(next(iter(v)) for v in classes.values()) == list(range(8))
    GA.check("prop:residues: the rung step keeps r, and rung plus period steps split the grid into 8 classes, "
             "one per residue", ok)
    return ok


def check_reversal_convention_and_types():
    ok = all(res(q, p) == (-res(p, q)) % 8 and causal(q, p) == causal(p, q) for p, q in SIGS)
    ok = ok and res(1, 3) == 6 and res(3, 1) == 2
    d13, m13 = corner_type(1, 3)
    d31, m31 = corner_type(3, 1)
    # Cl(1,3) = Mat(2,H): module dimension 8; Cl(3,1) = Mat(4,R): module dimension 4
    ok = ok and (d13, m13) == ("H", 8) and (d31, m31) == ("R", 4)
    GA.check("reversal: r -> -r, causality kept, 6 <-> 2; Cl(1,3) has D = H (module 8), Cl(3,1) D = R "
             "(module 4): not isomorphic", ok)
    return ok


def check_census_lowest_causal():
    lowest = {}
    for r in range(8):
        c = sorted((s for s in SIGS if res(*s) == r and causal(*s)), key=lambda s: (sum(s), s))
        lowest[r] = c[0] if c else None
    ok = lowest == {0: (1, 1), 1: (2, 1), 2: (3, 1), 3: (4, 1), 4: (1, 5), 5: (1, 4), 6: (1, 3), 7: (1, 2)}
    ok = ok and res(5, 1) == 4 and causal(5, 1) and sum(lowest[4]) == 6
    ok = ok and sorted(res(1, s) for s in range(1, 9)) == list(range(8)) and all(causal(1, s) for s in range(1, 9))
    GA.check("prop:residues(i): lowest causal signatures (1,1), (2,1), (3,1), (4,1), (1,5)/(5,1), (1,4), "
             "(1,3), (1,2)", ok)
    return ok


def check_sort_under_p3():
    premise("dark-matter.p3-nearest-dimension-representatives")
    reps = {r: p3(r) for r in range(8)}
    ok = (1, 3) in reps[6] and (3, 1) in reps[2] and reps[0] == [(2, 2)] and reps[4] == [(0, 4), (4, 0)]
    ok = ok and (2, 1) in reps[1] and (1, 2) in reps[7] and (4, 1) in reps[3] and (1, 4) in reps[5]
    ok = ok and all(sum(s) == 3 for s in reps[1] + reps[7]) and all(sum(s) == 5 for s in reps[3] + reps[5])
    sterile = sorted(r for r in range(8) if not any(causal(*s) for s in reps[r]))
    fixed = sorted(r for r in range(8) if (-r) % 8 == r)
    ok = ok and sterile == [0, 4] and fixed == [0, 4] and 8 - len(sterile) == 6
    GA.check("prop:residues(ii): P3 representatives as stated; sterile {0, 4} = fixed points of r -> -r; six "
             "admit matter", ok)
    return ok


def check_window_sensitivity():
    ok = sterile_in(1, 5) == [4] and sterile_in(3, 6) == [0] and sterile_in(3, 10) == [] \
        and sterile_in(3, 5) == [0, 4]
    ok = ok and causal(1, 1) and res(1, 1) == 0 and causal(1, 5) and res(1, 5) == 4 and causal(1, 9) \
        and res(1, 9) == 0 and sum((1, 9)) == 10
    lowest_any = {r: min((s for s in SIGS if res(*s) == r), key=lambda s: (sum(s), s)) for r in range(8)}
    ok = ok and lowest_any[6] == (0, 2) and lowest_any[2] == (2, 0)
    GA.check("prop:residues(iii): windows [1,5] -> {4}, [3,6] -> {0}, [3,10] -> {}, [3,5] -> {0,4}; lowest "
             "r = 6, 2 with no lower bound are (0,2), (2,0)", ok)
    return ok
