"""lepton.imported-tensor-ledger-contains-no-lepton: exact checks.

The tensor ledger Lambda(C^2 (x) C^3) on the six cells e_i (x) f_a, with the automorphisms acting cell by cell,
as exact U(2) x U(3) characters (weight of a set of cells = its row counts and column counts), decomposed
into irreducibles by peeling highest weights against Schur characters (semistandard tableaux).
(1) Grade by grade the decomposition is (1,1); (2,3); (3,3b) + (1,6); (4,1) + (2,8); (3,3) + (1,6b); (2,3b);
    (1,1), and the abelian weight q = 3|lam| - 2|mu| of every component equals the cell number
    (each cell carries 3 - 2 = 1 under (lambda^3 a, lambda^-2 b)).
(2) No component is (2,1).
(3) The row-filling states wedge_a (v (x) f_a), computed as 3 x 3 minors for exact sample v, are
    homogeneous cubic in v (scaling v by c scales them by c^3), lie in the cell sets with one cell per
    column (SU(3) weight (1,1,1), the determinant), and span a 4-dimensional space whose U(2) weights are
    (3,0), (2,1), (1,2), (0,3): S^3 C^2 (x) Lambda^3 C^3 = (4,1), of weight 3.
The ledger and its action are those of the cited series results (raw representation content; quark-lepton
content, Prop. 5.3(2) for the row-filling states), which the functions call as premises; the decomposition
itself is recomputed.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# Exact characters of U(2) x U(3): a representation is a Counter of weights
# ((a1, a2), (b1, b2, b3)); irreducibles are products of Schur characters,
# computed by enumerating semistandard tableaux. Decomposition peels the
# lexicographically largest weight, which is always a highest weight.
# ---------------------------------------------------------------------------


def ssyt(shape, n):
    """Content vectors of the semistandard tableaux of the given shape with entries 0..n-1."""
    cells = [(r, c) for r, row in enumerate(shape) for c in range(row)]
    out = Counter()

    def fill(i, T):
        if i == len(cells):
            cont = [0] * n
            for v in T.values():
                cont[v] += 1
            out[tuple(cont)] += 1
            return
        r, c = cells[i]
        lo = 0
        if c > 0:
            lo = max(lo, T[(r, c - 1)])
        if r > 0:
            lo = max(lo, T[(r - 1, c)] + 1)
        for v in range(lo, n):
            T[(r, c)] = v
            fill(i + 1, T)
            del T[(r, c)]

    fill(0, {})
    return out


def schur(hw, n):
    """Character of the U(n) irreducible with highest weight hw (entries may be negative)."""
    m = min(hw)
    shape = [h - m for h in hw]
    ch = ssyt([s for s in shape if s > 0], n)
    return Counter({tuple(x + m for x in w): c for w, c in ch.items()})


def irr_char(lam, mu):
    a, b = schur(lam, 2), schur(mu, 3)
    return Counter({(wa, wb): ca * cb for wa, ca in a.items() for wb, cb in b.items()})


def decompose(ch):
    """List of ((lam, mu), multiplicity) for a U(2) x U(3) character."""
    ch = Counter({k: v for k, v in ch.items() if v})
    out = []
    while ch:
        top = max(ch)
        m = ch[top]
        if m < 0:
            return None
        out.append((top, m))
        ch.subtract(Counter({k: m * v for k, v in irr_char(*top).items()}))
        ch = Counter({k: v for k, v in ch.items() if v})
    return out


SU3_NAME = {(0, 0): "1", (1, 0): "3", (0, 1): "3b", (2, 0): "6", (0, 2): "6b", (1, 1): "8",
            (3, 0): "10", (0, 3): "10b"}


def label(lam, mu):
    """(SU(2) dimension, SU(3) name, abelian weight q = 3|lam| - 2|mu|)."""
    return (lam[0] - lam[1] + 1, SU3_NAME[(mu[0] - mu[1], mu[1] - mu[2])], 3 * sum(lam) - 2 * sum(mu))


def cell_ledger(k):
    """Character of Lambda^k(C^2 (x) C^3): cells (i, a), weight = (row counts, column counts)."""
    cells = [(i, a) for i in range(2) for a in range(3)]
    ch = Counter()
    for S in combinations(cells, k):
        u2 = tuple(sum(1 for (i, a) in S if i == r) for r in range(2))
        u3 = tuple(sum(1 for (i, a) in S if a == c) for c in range(3))
        ch[(u2, u3)] += 1
    return ch


def five_mode(j, k):
    """Character of Lambda^j C^2 (x) Lambda^k C^3 (j slots, k pairs)."""
    ch = Counter()
    for S in combinations(range(2), j):
        for T in combinations(range(3), k):
            ch[(tuple(1 if r in S else 0 for r in range(2)), tuple(1 if c in T else 0 for c in range(3)))] += 1
    return ch


CONJ = {"1": "1", "3": "3b", "3b": "3", "6": "6b", "6b": "6", "8": "8"}
NCOL = {"1": 1, "3": 3, "3b": 3, "6": 6, "6b": 6, "8": 8}


def conj(sp):
    d2, col, y = sp
    return (d2, CONJ[col], -y)


def anomaly_sums(species):
    """The four sums of the imported anomaly Fact over left-handed species (d2, colour, Y):
    [SU(3)]^2 U(1) over colour (anti)triplets weighted by SU(2) multiplicity, [SU(2)]^2 U(1) over
    doublets weighted by colour multiplicity, U(1)^3, gravitational."""
    su3 = sum((d2 * y for d2, col, y in species if col in ("3", "3b")), F(0))
    su2 = sum((NCOL[col] * y for d2, col, y in species if d2 == 2), F(0))
    cub = sum((d2 * NCOL[col] * y ** 3 for d2, col, y in species), F(0))
    grav = sum((d2 * NCOL[col] * y for d2, col, y in species), F(0))
    return (su3, su2, cub, grav)


def five_mode_species():
    """(j, k) -> (SU(2) dim, colour, Y) of the five-mode module, read from its characters."""
    out = {}
    for j in range(3):
        for k in range(4):
            dec = decompose(five_mode(j, k))
            (lam, mu), m = dec[0]
            d2, col, q = label(lam, mu)
            out[(j, k)] = (d2, col, F(q, 6)) if len(dec) == 1 and m == 1 else None
    return out


def solve_generation(yQ):
    """Solve the four anomaly conditions for (Y_L, Y_e, s = Y_u + Y_d, p = Y_u Y_d) given Y_Q and the
    content Q (2,3), L (2,1), u^c, d^c (1,3b), e^c (1,1), and nu^c (1,1) at Y = 0 or absent (the two
    give the same equations, nu^c contributing 0 to every sum)."""
    yL = -3 * yQ                                   # [SU(2)]^2 U(1): 3 Y_Q + Y_L = 0
    s = -2 * yQ                                    # [SU(3)]^2 U(1): 2 Y_Q + Y_u + Y_d = 0
    ye = -(6 * yQ + 2 * yL + 3 * s)                # gravitational (the nu^c term is 0 either way)
    rest = 6 * yQ ** 3 + 2 * yL ** 3 + ye ** 3     # U(1)^3: rest + 3 (Y_u^3 + Y_d^3) = 0
    cubes = -rest / 3                              # Y_u^3 + Y_d^3 = s^3 - 3 s p
    p = (s ** 3 - cubes) / (3 * s)
    return yL, ye, s, p

SAMPLE_V = [(F(1), F(0)), (F(0), F(1)), (F(2), F(3)), (F(-1), F(5, 2)), (F(7), F(-2)), (F(1, 3), F(1, 4))]
CELLS = [(i, a) for i in range(2) for a in range(3)]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def row_state(v):
    """Coordinates of wedge_{a=0,1,2} (v (x) f_a) on the basis of 3-cell sets."""
    vecs = []
    for a in range(3):
        vecs.append([v[i] if b == a else F(0) for (i, b) in CELLS])
    out = {}
    for S in combinations(range(6), 3):
        M = [[vecs[r][c] for c in S] for r in range(3)]
        d = det3(M)
        if d:
            out[S] = d
    return out


def check_decomposition_and_weight():
    premise("standard-model.raw-representation-content-state-space")
    want = {0: [(1, "1")], 1: [(2, "3")], 2: [(3, "3b"), (1, "6")], 3: [(4, "1"), (2, "8")],
            4: [(3, "3"), (1, "6b")], 5: [(2, "3b")], 6: [(1, "1")]}
    ok = True
    total = 0
    for k in range(7):
        dec = decompose(cell_ledger(k))
        ok = ok and dec is not None and all(m == 1 for _, m in dec)
        labs = [label(lam, mu) for (lam, mu), m in dec]
        ok = ok and sorted((d, c) for d, c, q in labs) == sorted(want[k])
        ok = ok and all(q == k for d, c, q in labs)
        total += sum(d * NCOL[c] for d, c, q in labs)
    ok = ok and total == 64
    GA.check("the tensor ledger decomposes as stated, graded by cell number = abelian weight", ok)
    return ok


def check_no_lepton_doublet():
    premise("standard-model.raw-representation-content-state-space")
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    comps = []
    for k in range(7):
        comps += [label(lam, mu) for (lam, mu), m in decompose(cell_ledger(k))]
    ok = len(comps) == 10
    ok = ok and not any(d == 2 and c == "1" for d, c, q in comps)
    doublets = sorted(c for d, c, q in comps if d == 2)
    ok = ok and doublets == ["3", "3b", "8"]
    GA.check("no (2,1) occurs in the tensor ledger", ok)
    return ok


def check_row_filling_states_are_the_4_1():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    states = [row_state(v) for v in SAMPLE_V]
    ok = all(states)
    # one cell per column: cell index = 3 i + a, so the columns of S are {c % 3}
    ok = ok and all(sorted(c % 3 for c in S) == [0, 1, 2] for st in states for S in st)
    # cubic: v -> 2 v multiplies every coordinate by 8
    for v, st in zip(SAMPLE_V, states):
        st2 = row_state((2 * v[0], 2 * v[1]))
        ok = ok and st2 == {S: 8 * x for S, x in st.items()}
    keys = sorted({S for st in states for S in st})
    mat = [[st.get(S, F(0)) for S in keys] for st in states]
    ok = ok and GA.field_rank(mat) == 4
    u2w = sorted({(sum(1 for c in S if c < 3), sum(1 for c in S if c >= 3)) for S in keys})
    ok = ok and u2w == [(0, 3), (1, 2), (2, 1), (3, 0)]
    ok = ok and all(len(S) == 3 for S in keys)
    GA.check("the row-filling states span S^3 C^2 (x) Lambda^3 C^3 = (4,1), of weight 3", ok)
    return ok
