"""lepton.imported-automorphism-group-section-hypercharge-generator: exact checks.

(1) K and the section: (X, Y) -> X (x) 1 + 1 (x) Y on gl(2) + gl(3) has rank 12, kernel the line of (1, -1)
    (Lie algebra of K); (lambda 1_2) (x) (lambda^-1 1_3) = 1_6 for sample lambda; for sample A, B and
    lambda, det(lambda A) det(lambda^-1 B) = lambda^-1 det A det B, so the coset of (A, B) meets
    det A det B = 1 exactly at lambda = det A det B.
(2) Z_6: (a, b, lambda) -> (lambda^3 a, lambda^-2 b) has kernel {lambda : lambda^6 = 1}: among the N-th roots
    of unity lambda = zeta^k (N = 6, 12, 30, 42), lambda^-3 1_2 lies in SU(2) and lambda^2 1_3 in SU(3)
    (determinant exponents -6k and 6k divisible by N) for exactly 6 values of k; and k -> (3k mod 2,
    -2k mod 3), the images in the centres Z_2 x Z_3, is a bijection on Z_6.
(3) The centre of the Lie algebra: the elements of gl(2) + gl(3) commuting with all of it form
    span{(1, 0), (0, 1)} (exact kernel); with the trace condition tr X + tr Y = 0 of S(U(2) x U(3)) the
    centre is the line of (3, -2), so y = (3i 1_2, -2i 1_3) up to scale.
(4) y acts on the cells of C^2 (x) C^3 as i (3 - 2) = i, on Lambda^k of the ledger as i k and on the
    five-mode component (j, k) as i (3j - 2k), the abelian weight q; Y = q/6 gives 1/6 on the quark doublet.
The last sentence of the statement (irreducibles determined by SU(2) content, SU(3) content and weight)
is representation theory of a product group and is not tested.
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


SAMPLE_A = [[F(2), F(1)], [F(-1), F(3)]]
SAMPLE_B = [[F(1), F(2), F(0)], [F(0), F(1), F(-3)], [F(4), F(0), F(1)]]
LAMBDAS = (F(2), F(-3, 7), F(5, 2))


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


def basis23():
    return [("X", i, j) for i in range(2) for j in range(2)] + [("Y", i, j) for i in range(3) for j in range(3)]


def as_pair(coeffs):
    X = [[F(0)] * 2 for _ in range(2)]
    Y = [[F(0)] * 3 for _ in range(3)]
    for (t, i, j), c in zip(basis23(), coeffs):
        (X if t == "X" else Y)[i][j] += c
    return X, Y


def check_kernel_and_section():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("standard-model.global-form-quotient-determined")
    imgs = []
    for t, i, j in basis23():
        M = kron(unit(2, i, j), eye(3)) if t == "X" else kron(eye(2), unit(3, i, j))
        imgs.append([x for row in M for x in row])
    ok = GA.field_rank(imgs) == 12
    ker = GA.field_kernel([list(col) for col in zip(*imgs)])
    ok = ok and len(ker) == 1
    X, Y = as_pair(ker[0])
    c = X[0][0]
    ok = ok and c != 0 and X == [[c, 0], [0, c]] and Y == [[-c if a == b else 0 for b in range(3)] for a in range(3)]
    for lam in LAMBDAS:
        ok = ok and kron([[lam, F(0)], [F(0), lam]], [[1 / lam if a == b else F(0) for b in range(3)]
                                                      for a in range(3)]) == eye(6)
        A2 = [[lam * x for x in row] for row in SAMPLE_A]
        B2 = [[x / lam for x in row] for row in SAMPLE_B]
        ok = ok and det(A2) * det(B2) == det(SAMPLE_A) * det(SAMPLE_B) / lam
    d = det(SAMPLE_A) * det(SAMPLE_B)
    ok = ok and d == -161
    ok = ok and det([[d * x for x in row] for row in SAMPLE_A]) * det([[x / d for x in row] for row in SAMPLE_B]) == 1
    GA.check("K = {(lambda, lambda^-1)} is the kernel; each coset meets det A det B = 1 once", ok)
    return ok


def check_z6_quotient():
    premise("standard-model.global-form-quotient-determined")
    ok = True
    for N in (6, 12, 30, 42):
        ks = [k for k in range(N) if (-3 * 2 * k) % N == 0 and (2 * 3 * k) % N == 0]
        ok = ok and len(ks) == 6
    images = {((3 * k) % 2, (-2 * k) % 3) for k in range(6)}
    ok = ok and len(images) == 6
    GA.check("the kernel of SU(2) x SU(3) x U(1) -> S(U(2) x U(3)) is Z_6", ok)
    return ok


def check_centre_is_hypercharge_line():
    premise("standard-model.global-form-quotient-determined")
    B = basis23()
    rows = []
    # unknown Z = sum z_t b_t; [Z, b_s] = 0 for every basis element b_s, componentwise in gl(2) + gl(3)
    def comm_coeffs(s, t):
        Xs, Ys = as_pair([F(1) if u == s else F(0) for u in range(len(B))])
        Xt, Yt = as_pair([F(1) if u == t else F(0) for u in range(len(B))])
        cx = [[sum(Xt[i][k] * Xs[k][j] - Xs[i][k] * Xt[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        cy = [[sum(Yt[i][k] * Ys[k][j] - Ys[i][k] * Yt[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return [x for row in cx for x in row] + [x for row in cy for x in row]
    cols = {t: [comm_coeffs(s, t) for s in range(len(B))] for t in range(len(B))}
    for s in range(len(B)):
        for comp in range(13):
            rows.append([cols[t][s][comp] for t in range(len(B))])
    centre = GA.field_kernel(rows)
    ok = len(centre) == 2
    traces = [as_pair(z) for z in centre]
    ok = ok and all(X[0][1] == X[1][0] == 0 and X[0][0] == X[1][1] for X, Y in traces)
    # trace condition 2 a + 3 b = 0 on (a 1_2, b 1_3): kernel of [2, 3]
    line = GA.field_kernel([[F(2), F(3)]])
    ok = ok and len(line) == 1 and line[0][0] * (-2) == line[0][1] * 3
    GA.check("the centre of s(u(2) + u(3)) is the line of y = (3i, -2i)", ok)
    return ok


def check_y_acts_by_the_abelian_weight():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    ok = True
    for k in range(7):
        for (lam, mu), m in decompose(cell_ledger(k)):
            ok = ok and label(lam, mu)[2] == k
    for j in range(3):
        for k in range(4):
            for (lam, mu), m in decompose(five_mode(j, k)):
                ok = ok and label(lam, mu)[2] == 3 * j - 2 * k
    q = label(*decompose(cell_ledger(1))[0][0])[2]
    ok = ok and F(q, 6) == F(1, 6) and label(*decompose(cell_ledger(1))[0][0])[:2] == (2, "3")
    GA.check("y acts as i q, q the abelian weight; Y = q/6 = 1/6 on the quark doublet", ok)
    return ok
