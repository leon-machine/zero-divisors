"""lepton.imported-duality-pair-system: exact checks.

(1) Characters: for k = 0..3 the U(3) weights of (Lambda^k W)^* (the negatives of those of Lambda^k W) equal
    those of Lambda^(3-k) W (x) det^-1 (shifted by (-1, -1, -1)); for C^2 the weights of (C^2)^* equal those
    of C^2 (x) det^-1. Both modules are irreducible (one highest weight), so the characters decide.
(2) The intertwiners: the wedge pairing E_k : Lambda^k W x Lambda^(3-k) W -> Lambda^3 W (E_k[S, T] the sign
    of e_S ^ e_T against e_123) is nondegenerate and satisfies C_k(B)^T E_k C_(3-k)(B) = det(B) E_k for
    sample rational B (C_k the k-th compound matrix, the action on Lambda^k), which is the isomorphism
    Lambda^(3-k) W (x) det^-1 -> (Lambda^k W)^*; likewise A^T J A = det(A) J with J = [[0, 1], [-1, 0]] for
    C^2. The textbook source (the -external entity) is the same statement; no premise() call.
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

SAMPLE_B = [[[F(1), F(2), F(0)], [F(0), F(1), F(-3)], [F(4), F(0), F(1)]],
            [[F(2), F(-1), F(1, 2)], [F(3), F(0), F(1)], [F(1), F(1), F(1)]]]
SAMPLE_A = [[[F(2), F(1)], [F(-1), F(3)]], [[F(0), F(5)], [F(1, 3), F(2)]]]


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    return sum(((-1) ** c * M[0][c] * det([row[:c] + row[c + 1:] for row in M[1:]]) for c in range(n)), F(0))


def subsets(n, k):
    return list(combinations(range(n), k))


def compound(B, k):
    S = subsets(len(B), k)
    if k == 0:
        return [[F(1)]]
    return [[det([[B[r][c] for c in J] for r in I]) for J in S] for I in S]


def wedge_sign(S, T):
    seq = list(S) + list(T)
    if sorted(seq) != list(range(len(seq))):
        return 0
    inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])
    return (-1) ** inv


def pairing(k, n=3):
    return [[F(wedge_sign(S, T)) for T in subsets(n, n - k)] for S in subsets(n, k)]


def mmul(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def u3_weights(k):
    return Counter(tuple(1 if a in S else 0 for a in range(3)) for S in combinations(range(3), k))


def check_characters_match():
    ok = True
    for k in range(4):
        dual = Counter({tuple(-x for x in w): m for w, m in u3_weights(k).items()})
        twisted = Counter({tuple(x - 1 for x in w): m for w, m in u3_weights(3 - k).items()})
        ok = ok and dual == twisted
        ok = ok and len(decompose(Counter({((0, 0), w): m for w, m in twisted.items()}))) == 1
    c2 = Counter([(1, 0), (0, 1)])
    ok = ok and Counter({(-a, -b): m for (a, b), m in c2.items()}) == Counter({(a - 1, b - 1): m for (a, b), m in c2.items()})
    # control: without the det^-1 twist the characters differ (Lambda^1 W is not its own dual)
    ok = ok and Counter({tuple(-x for x in w): m for w, m in u3_weights(1).items()}) != u3_weights(2)
    GA.check("(Lambda^k W)^* and Lambda^(3-k) W (x) det^-1 have the same character; likewise for C^2", ok)
    return ok


def check_equivariant_pairings():
    ok = True
    for k in range(4):
        E = pairing(k)
        ok = ok and GA.field_rank(E) == len(E) and len(E) == [1, 3, 3, 1][k]
        for B in SAMPLE_B:
            lhs = mmul(mmul(transpose(compound(B, k)), E), compound(B, 3 - k))
            ok = ok and lhs == [[det(B) * x for x in row] for row in E]
    J = [[F(0), F(1)], [F(-1), F(0)]]
    for A in SAMPLE_A:
        ok = ok and mmul(mmul(transpose(A), J), A) == [[det(A) * x for x in row] for row in J]
    ok = ok and det(SAMPLE_B[0]) == -23
    GA.check("the wedge pairings are nondegenerate and equivariant up to det: the stated dualities", ok)
    return ok
