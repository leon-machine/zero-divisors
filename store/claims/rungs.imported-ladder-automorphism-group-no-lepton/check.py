"""rungs.imported-ladder-automorphism-group-no-lepton: exact checks.

(1) Mixings of n conformal spinors (n = 2, 3): Z_i in C^4 = (omega_i, pi_i), the momentum
    P = sum_i pi_i pi_i^dagger (a Hermitian 2 x 2 matrix) and the helicity form sum_i h(Z_i, Z_i) with
    h(Z, Z') = Z^dagger H Z', H = [[0, 1], [1, 0]] in 2 x 2 blocks (signature (2,2)), over Q(i) (GA.QI).
    U (x) 1 preserves both at every sample configuration for sample unitary U (permutations, rational
    rotations, complex unitaries), and for sample non-unitary U (diagonal stretch, shear, a complex
    orthogonal matrix with U^T U = 1) some sample configuration is not preserved: the mixing group is cut
    out by U^dagger U = 1, which is why the two sums (sesquilinear in Z) single out U(n).
(2) The Lie algebra of the automorphisms of C^m (x) C^n is the image of (X, Y) -> X (x) 1 + 1 (x) Y,
    of dimension m^2 + n^2 - 1 with kernel spanned by (1, -1): 12 for C^2 (x) C^3 (s(u(2) + u(3)), the
    quotient by K) and 17 for C^3 (x) C^3 (su(3) + su(3) + u(1)). Group level: (lambda 1) (x) (lambda^-1 1) = 1
    for sample lambda; det(lambda A) det(lambda^-1 B) = lambda^-1 det A det B for sample A, B, lambda, so each
    K-coset meets det A det B = 1 exactly once (at lambda = det A det B).
(3) The tensor ledger Lambda(C^2 (x) C^3), as exact U(2) x U(3) characters peeled into irreducibles,
    contains no (2,1).
Premise calls name the entities whose objects each function instantiates: the momentum and helicity forms
(internal-symmetry-ladder), the automorphisms A (x) B and their quotient (gauge algebra, global form), the
tensor ledger with its cell-by-cell action (quark-lepton content); the conclusions are recomputed.
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

QI = GA.QI
I = GA.QI_I
UNITARY = [
    [[QI(0), QI(1)], [QI(1), QI(0)]],
    [[QI(F(3, 5)), QI(F(-4, 5))], [QI(F(4, 5)), QI(F(3, 5))]],
    [[QI(F(1, 2), F(1, 2)), QI(F(1, 2), F(-1, 2))], [QI(F(1, 2), F(-1, 2)), QI(F(1, 2), F(1, 2))]],
    [[QI(0, 1), QI(0), QI(0)], [QI(0), QI(0), QI(1)], [QI(0), QI(1), QI(0)]],
    [[QI(F(3, 5)), QI(0), QI(F(4, 5))], [QI(0), QI(0, 1), QI(0)], [QI(F(-4, 5)), QI(0), QI(F(3, 5))]],
]
NONUNITARY = [
    [[QI(2), QI(0)], [QI(0), QI(1)]],
    [[QI(1), QI(1)], [QI(0), QI(1)]],
    [[QI(F(5, 4)), QI(0, F(3, 4))], [QI(0, F(-3, 4)), QI(F(5, 4))]],
]
CONFIGS = [
    [[QI(1), QI(0, 2), QI(-1), QI(3)], [QI(2, -1), QI(0), QI(1, 1), QI(F(1, 2))], [QI(0), QI(1), QI(0, -1), QI(2)]],
    [[QI(1), QI(0), QI(0), QI(0)], [QI(0), QI(0), QI(1), QI(0)], [QI(0), QI(1), QI(0), QI(1)]],
    [[QI(0), QI(0), QI(1), QI(1)], [QI(0), QI(0), QI(1), QI(-1)], [QI(1), QI(0), QI(0), QI(0)]],
]
SAMPLE_A = [[F(2), F(1)], [F(-1), F(3)]]
SAMPLE_B = [[F(1), F(2), F(0)], [F(0), F(1), F(-3)], [F(4), F(0), F(1)]]


def herm_h(Z, W):
    """h(Z, W) = conj(omega_Z) . pi_W + conj(pi_Z) . omega_W."""
    return sum((Z[a].conj() * W[a + 2] + Z[a + 2].conj() * W[a] for a in range(2)), QI(0))


def momentum(conf):
    return [[sum((Z[2 + r] * Z[2 + c].conj() for Z in conf), QI(0)) for c in range(2)] for r in range(2)]


def helicity(conf):
    return sum((herm_h(Z, Z) for Z in conf), QI(0))


def mix(U, conf):
    n = len(U)
    return [[sum((U[i][j] * conf[j][a] for j in range(n)), QI(0)) for a in range(4)] for i in range(n)]


def preserved(U, conf):
    new = mix(U, conf)
    return momentum(new) == momentum(conf) and helicity(new) == helicity(conf)


def is_unitary(U):
    n = len(U)
    return all(sum((U[k][i].conj() * U[k][j] for k in range(n)), QI(0)) == (1 if i == j else 0)
               for i in range(n) for j in range(n))


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A)) for l in range(len(B))]
            for i in range(len(A)) for k in range(len(B))]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def unit(n, i, j):
    return [[F(1) if (r, c) == (i, j) else F(0) for c in range(n)] for r in range(n)]


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    return sum(((-1) ** c * M[0][c] * det([row[:c] + row[c + 1:] for row in M[1:]]) for c in range(n)), F(0))


def check_mixings_preserving_momentum_and_helicity_are_unitary():
    premise("standard-model.internal-symmetry-ladder")
    ok = all(is_unitary(U) for U in UNITARY) and not any(is_unitary(U) for U in NONUNITARY)
    for U in UNITARY:
        n = len(U)
        ok = ok and all(preserved(U, conf[:n]) for conf in CONFIGS)
    for U in NONUNITARY:
        n = len(U)
        ok = ok and not all(preserved(U, conf[:n]) for conf in CONFIGS)
    # the complex orthogonal sample has U^T U = 1 but is not unitary
    C = NONUNITARY[2]
    ok = ok and all(sum((C[k][i] * C[k][j] for k in range(2)), QI(0)) == (1 if i == j else 0)
                    for i in range(2) for j in range(2))
    # helicity form has signature (2,2) on C^4: h(e0 + e2) = 2, h(e0 - e2) = -2
    e = [[QI(1), QI(0), QI(1), QI(0)], [QI(1), QI(0), QI(-1), QI(0)]]
    ok = ok and herm_h(e[0], e[0]) == 2 and herm_h(e[1], e[1]) == -2
    GA.check("mixings preserving momentum and helicity at every configuration are the unitary ones", ok)
    return ok


def check_automorphism_algebras_and_cosets():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("standard-model.global-form-quotient-determined")
    dims = {}
    for m, n in ((2, 3), (3, 3)):
        imgs = []
        for i in range(m):
            for j in range(m):
                imgs.append(kron(unit(m, i, j), eye(n)))
        for i in range(n):
            for j in range(n):
                imgs.append(kron(eye(m), unit(n, i, j)))
        dims[(m, n)] = GA.field_rank([[x for row in M for x in row] for M in imgs])
    ok = dims == {(2, 3): 12, (3, 3): 17}
    # kernel of (X, Y) -> X (x) 1 + 1 (x) Y: one line in each case, spanned by (1, -1)
    ok = ok and (2 * 2 + 3 * 3) - dims[(2, 3)] == 1 and (3 * 3 + 3 * 3) - dims[(3, 3)] == 1
    for lam in (F(2), F(-3, 7), F(5, 2)):
        ok = ok and kron([[lam, F(0)], [F(0), lam]], [[1 / lam if i == j else F(0) for j in range(3)]
                                                      for i in range(3)]) == eye(6)
        A2 = [[lam * x for x in row] for row in SAMPLE_A]
        B2 = [[x / lam for x in row] for row in SAMPLE_B]
        ok = ok and det(A2) * det(B2) == det(SAMPLE_A) * det(SAMPLE_B) / lam
    d = det(SAMPLE_A) * det(SAMPLE_B)
    ok = ok and d == -161
    A3 = [[d * x for x in row] for row in SAMPLE_A]
    B3 = [[x / d for x in row] for row in SAMPLE_B]
    ok = ok and det(A3) * det(B3) == 1
    GA.check("automorphism algebras of dimension 12 and 17; each K-coset meets det A det B = 1 once", ok)
    return ok


def check_tensor_ledger_has_no_lepton_doublet():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    comps = []
    for k in range(7):
        dec = decompose(cell_ledger(k))
        comps += [label(lam, mu) for (lam, mu), m in dec]
    ok = len(comps) == 10 and not any(d == 2 and c == "1" for d, c, q in comps)
    ok = ok and sum(d * NCOL[c] for d, c, q in comps) == 64
    # control: the five-mode module of Hypothesis (S) does contain a (2,1), at (j, k) = (1, 3)
    ok = ok and label(*decompose(five_mode(1, 3))[0][0])[:2] == (2, "1")
    GA.check("the tensor ledger contains no (2,1)", ok)
    return ok
