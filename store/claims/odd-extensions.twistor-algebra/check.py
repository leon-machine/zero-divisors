"""odd-extensions.twistor-algebra: exact checks.

Conventions: Cl(2,4) with e1, e2 (+1) and e3, ..., e6 (-1) (GA indices 0..5); e6 spacelike, e1 timelike.
(i) The five bivectors e_i e6 (i = 1..5) square to (+,+,-,-,-) and anticommute pairwise (a Cl(2,3)); the five
    e_i e1 (i = 2..6) square to (-,+,+,+,+) (a Cl(4,1)); each set generates all 32 even blades (Cl^0(2,4)).
    omega_6 is even, omega_6^2 = -1, commutes with all 32 even blades and anticommutes with the six vectors;
    the centre of Cl^0(2,4) (kernel of the commutators with a generating set) is span(1, omega_6).
    Cl^0(2,4) = Mat(4, C): the four idempotents f = (1 +- e1e3)/2 (1 +- e2e4)/2 are orthogonal and sum to 1,
    every f_i Cl^0 f_j has real dimension 2 (16 x 2 = 32), and f Cl^0 f = span(f, f omega_6) with
    (f omega_6)^2 = -f: matrix units over C with omega_6 as the complex unit.
(ii) e_i e6 (i = 2..5) square to (1,-1,-1,-1) and generate a 16-dimensional Cl(1,3); e_i e1 (i = 2..5)
    square to (-1,1,1,1) and generate a 16-dimensional Cl(3,1).
(iii) In the Fock model of Cl(2,4)_C (same signature), the even blades preserve CS and restricted to CS span
    all of End(CS) (complex dimension 16): CS is the irreducible module of Cl^0(2,4) = Mat(4,C), and omega_6
    acts on CS as a square root of -1 times the identity. The bivectors (spin generators) are even.
    The rest of (iii) (the inputs of the copy theorem) is a reading with no separate finite content.
(iv) Centre dimension 2 for every odd signature with n <= 5 and 1 for every even one with n <= 6 (central
    blades); omega^2 = -1 in Cl(2,3), Cl(4,1) and +1 in Cl(3,2), Cl(1,4); (1 + omega)/2 is a nontrivial
    central idempotent in the latter, while in the former (a + b omega)(a - b omega) = a^2 + b^2 for sample
    (a, b), so the centre is a field (C); the centres are not isomorphic, hence neither are the algebras.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

from itertools import combinations
# ---------------------------------------------------------------------------
# Fock model of Cl(2,4)_C on Lambda W, W = span(w_0, w_1, w_2), exact over Q(i).
# Ambient orthonormal basis of R^{2,4}: index 0 e_plus (+1), 1 g0 (+1), 2 e_minus (-1),
# 3 g1, 4 g2, 5 g3 (-1).  Witt pairs: (e_plus, e_minus) -> mode 0, (g0, g1) -> mode 1,
# (g2, g3) complexified -> mode 2; c(w_i) = wedge, c(w'_i) = contraction, <w_i, w'_j> = delta_ij / 2.
# ---------------------------------------------------------------------------
QI = GA.QI
ZERO, ONE, IU = QI(0), QI(1), QI(0, 1)
SQ = (1, 1, -1, -1, -1, -1)
SUBSETS = [frozenset(s) for k in range(4) for s in combinations(range(3), k)]
IDX = {S: i for i, S in enumerate(SUBSETS)}
EVEN = [IDX[S] for S in SUBSETS if len(S) % 2 == 0]
ODD = [IDX[S] for S in SUBSETS if len(S) % 2 == 1]
FULL = frozenset(range(3))


def zmat(n=8):
    return [[ZERO] * n for _ in range(n)]


def wedge_mat(i):
    M = zmat()
    for S in SUBSETS:
        if i not in S:
            M[IDX[S | {i}]][IDX[S]] = QI((-1) ** len([j for j in S if j < i]))
    return M


def contract_mat(i):
    M = zmat()
    for S in SUBSETS:
        if i in S:
            M[IDX[S - {i}]][IDX[S]] = QI((-1) ** sorted(S).index(i))
    return M


def madd(*Ms):
    n = len(Ms[0])
    return [[sum((M[r][c] for M in Ms), ZERO) for c in range(len(Ms[0][0]))] for r in range(n)]


def mscal(c, M):
    c = QI(c) if not isinstance(c, QI) else c
    return [[c * v for v in row] for row in M]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B)) if A[i][k] and B[k][j]), ZERO)
             for j in range(len(B[0]))] for i in range(len(A))]


def mzero(M):
    return all(not v for row in M for v in row)


def apply(M, u):
    return [sum((M[r][c] * u[c] for c in range(len(u)) if M[r][c] and u[c]), ZERO) for r in range(len(M))]


CW = [wedge_mat(i) for i in range(3)]
CWP = [contract_mat(i) for i in range(3)]
CB = [madd(CW[0], CWP[0]), madd(CW[1], CWP[1]), madd(CW[0], mscal(-1, CWP[0])),
      madd(CW[1], mscal(-1, CWP[1])), madd(CW[2], mscal(-1, CWP[2])), mscal(QI(0, -1), madd(CW[2], CWP[2]))]
ID8 = [[ONE if r == c else ZERO for c in range(8)] for r in range(8)]


def c_of(v):
    """Operator of the ambient vector with coordinates v (six QI) in the orthonormal basis."""
    M = zmat()
    for a in range(6):
        if v[a]:
            M = madd(M, mscal(v[a], CB[a]))
    return M


def ip(u, v):
    return sum((SQ[a] * u[a] * v[a] for a in range(6)), ZERO)


def qv(*xs):
    return [x if isinstance(x, QI) else QI(x) for x in xs]


def annihilator(u):
    """Basis of W_u = {v in C^6 : c(v) u = 0}."""
    cols = [apply(CB[a], u) for a in range(6)]
    return GA.field_kernel([[cols[a][r] for a in range(6)] for r in range(8)])


def joint_kernel(vecs):
    rows = []
    for v in vecs:
        rows += c_of(v)
    return GA.field_kernel(rows)


def from_even(c4):
    out = [ZERO] * 8
    for k, col in enumerate(EVEN):
        out[col] = c4[k] if isinstance(c4[k], QI) else QI(c4[k])
    return out


def from_odd(c4):
    out = [ZERO] * 8
    for k, col in enumerate(ODD):
        out[col] = c4[k] if isinstance(c4[k], QI) else QI(c4[k])
    return out


def eps_sign(S):
    seq = sorted(S) + sorted(FULL - S)
    return (-1) ** sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[a] > seq[b])


# the top-degree pairing on Lambda W, twisted by the reversal sign on the first argument
BCOEF = {S: (-1) ** (len(S) * (len(S) - 1) // 2) * eps_sign(S) for S in SUBSETS}


def bpair(p, q):
    return sum((BCOEF[S] * p[IDX[S]] * q[IDX[FULL - S]] for S in SUBSETS), ZERO)


GAMMA = [[(ONE if len(SUBSETS[r]) % 2 == 0 else -ONE) if r == c else ZERO for c in range(8)] for r in range(8)]
E8 = [[ONE if i == j else ZERO for i in range(8)] for j in range(8)]
ECS = [from_even([1 if k == i else 0 for k in range(4)]) for i in range(4)]


def conj(u):
    return [x.conj() for x in u]


def restrict_cs(M):
    """Columns of M on the even half (an 8 x 4 matrix)."""
    return [[row[c] for c in EVEN] for row in M]


def cs_kernel(v):
    """Kernel of c(v) on the conformal spinor half, as 8-vectors."""
    return [from_even(k) for k in GA.field_kernel(restrict_cs(c_of(v)))]


def skew_form(v):
    """M_v(Z1, Z2) = B(Z1, c(v) Z2) on the conformal spinor half: the bivector of v in Lambda^2 CS*."""
    C = c_of(v)
    return [[bpair(ECS[i], apply(C, ECS[j])) for j in range(4)] for i in range(4)]


def pfaff4(M):
    return M[0][1] * M[2][3] - M[0][2] * M[1][3] + M[0][3] * M[1][2]


# Witt data of the conformal model: n0 = (e_plus + e_minus)/2, ninf = e_plus - e_minus, <n0, ninf> = 1
N0 = qv(F(1, 2), 0, F(1, 2), 0, 0, 0)
NINF = qv(1, 0, -1, 0, 0, 0)


def point(x):
    """X(x) = n0 + x - (1/2) Q(x) ninf for x = (t, x1, x2, x3) (rational or Gaussian rational)."""
    xv = qv(0, x[0], 0, x[1], x[2], x[3])
    Q = ip(xv, xv)
    return [N0[a] + xv[a] - QI(F(1, 2)) * Q * NINF[a] for a in range(6)], Q

SQ6 = (1, 1, -1, -1, -1, -1)
EVEN_BLADES = [b for b in GA.all_blades(6) if len(b) % 2 == 0]
OMEGA6 = {(0, 1, 2, 3, 4, 5): F(1)}
AB_SAMPLES = [(F(1), F(1)), (F(2), F(-3)), (F(1, 2), F(5, 7))]


def m6(x, y):
    return GA.mul(x, y, SQ6)


def bl(*idx):
    x = GA.sc(1)
    for i in idx:
        x = m6(x, GA.gen(i))
    return x


def generated_dim(gens, sq, blades):
    span = [GA.sc(1)]
    frontier = [GA.sc(1)]
    rows = [GA.basis_vector_of(GA.sc(1), blades)]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = GA.mul(x, g, sq)
                r = GA.basis_vector_of(y, blades)
                if GA.rank_of_vectors(rows + [r]) > len(rows):
                    rows.append(r)
                    new.append(y)
        frontier = new
    return len(rows)


def relations(gens, sq, squares):
    ok = (len(gens) == len(squares) and all(GA.eq(GA.mul(g, g, sq), GA.sc(s)) for g, s in zip(gens, squares)))
    ok = ok and all(GA.anticommutes(gens[i], gens[j], sq) for i in range(len(gens)) for j in range(i + 1, len(gens)))
    return ok


def check_even_subalgebra_is_cl23_cl41_and_mat4c():
    premise("odd-extensions.doubling-or-complexification")
    premise("odd-extensions.four-extensions-oriented-pair")
    ok = True
    allb = GA.all_blades(6)
    space = [m6(GA.gen(i), GA.gen(5)) for i in range(5)]
    time = [m6(GA.gen(i), GA.gen(0)) for i in range(1, 6)]
    ok = ok and relations(space, SQ6, (1, 1, -1, -1, -1)) and relations(time, SQ6, (-1, 1, 1, 1, 1))
    ok = ok and generated_dim(space, SQ6, allb) == 32 and generated_dim(time, SQ6, allb) == 32
    ok = ok and all(len(b) % 2 == 0 for g in space + time for b in g)
    # omega_6
    ok = ok and GA.eq(m6(OMEGA6, OMEGA6), GA.sc(-1))
    ok = ok and all(GA.commutes(OMEGA6, {b: F(1)}, SQ6) for b in EVEN_BLADES)
    ok = ok and all(GA.anticommutes(OMEGA6, GA.gen(i), SQ6) for i in range(6))
    # centre of Cl^0 by kernel: x in Cl^0 with [x, e_i e_(i+1)] = 0 for i = 0..4 (these generate Cl^0)
    gens = [bl(i, i + 1) for i in range(5)]
    rows = []
    for g in gens:
        comms = [GA.sub(m6({b: F(1)}, g), m6(g, {b: F(1)})) for b in EVEN_BLADES]
        for target in EVEN_BLADES:
            rows.append([c.get(target, F(0)) for c in comms])
    ker = GA.field_kernel([[F(x) for x in r] for r in rows])
    ok = ok and len(ker) == 2
    centre_rows = [[F(1) if b == () else F(0) for b in EVEN_BLADES],
                   [F(1) if b == (0, 1, 2, 3, 4, 5) else F(0) for b in EVEN_BLADES]]
    ok = ok and GA.rank_of_vectors(ker + centre_rows) == 2
    # Mat(4, C): four orthogonal idempotents with two-dimensional corners
    p, q = bl(0, 2), bl(1, 3)
    fs = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            fs.append(m6(GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(s1, p))),
                         GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(s2, q)))))
    ok = ok and GA.eq(GA.add(*fs), GA.sc(1))
    ok = ok and all(GA.eq(m6(fs[i], fs[j]), fs[i] if i == j else {}) for i in range(4) for j in range(4))
    total = 0
    for i in range(4):
        for j in range(4):
            d = GA.rank_of_vectors([GA.basis_vector_of(m6(m6(fs[i], {b: F(1)}), fs[j]), EVEN_BLADES)
                                    for b in EVEN_BLADES])
            ok = ok and d == 2
            total += d
    ok = ok and total == 32
    for f in fs:
        fo = m6(f, OMEGA6)
        ok = ok and GA.eq(m6(fo, fo), GA.neg(f))
    _tp_rv = (ok); assert _tp_rv is not False, "check_even_subalgebra_is_cl23_cl41_and_mat4c"; return _tp_rv


def check_both_oriented_shadows_inside_even_subalgebra():
    ok = True
    allb = GA.all_blades(6)
    this_world = [m6(GA.gen(i), GA.gen(5)) for i in range(1, 5)]
    mirror = [m6(GA.gen(i), GA.gen(0)) for i in range(1, 5)]
    ok = ok and relations(this_world, SQ6, (1, -1, -1, -1)) and relations(mirror, SQ6, (-1, 1, 1, 1))
    ok = ok and generated_dim(this_world, SQ6, allb) == 16 and generated_dim(mirror, SQ6, allb) == 16
    _tp_rv = (ok); assert _tp_rv is not False, "check_both_oriented_shadows_inside_even_subalgebra"; return _tp_rv


def check_conformal_spinors_are_the_module_of_the_even_subalgebra():
    premise("odd-extensions.imported-conformal-completion")
    ok = True
    reps = []
    for b in EVEN_BLADES:
        M = ID8
        for a in b:
            M = mmul(M, CB[a])
        ok = ok and all(not M[r][c] for r in ODD for c in EVEN)
        reps.append([M[r][c] for r in EVEN for c in EVEN])
    ok = ok and len(reps) == 32 and GA.field_rank(reps) == 16
    Om = ID8
    for a in range(6):
        Om = mmul(Om, CB[a])
    lam = Om[EVEN[0]][EVEN[0]]
    ok = ok and lam * lam == QI(-1)
    ok = ok and all(Om[r][c] == (lam if r == c else ZERO) for r in EVEN for c in EVEN)
    _tp_rv = (ok); assert _tp_rv is not False, "check_conformal_spinors_are_the_module_of_the_even_subalgebra"; return _tp_rv


def check_signature_reversal_changes_the_centre():
    premise("odd-extensions.four-extensions-oriented-pair")
    ok = True
    # central blades: dimension 2 for odd n <= 5, 1 for even n <= 6
    for n in range(1, 7):
        for p in range(n + 1):
            sq = GA.sig(p, n - p)
            central = [b for b in GA.all_blades(n)
                       if all(GA.commutes({b: F(1)}, GA.gen(i), sq) for i in range(n))]
            ok = ok and len(central) == (2 if n % 2 == 1 else 1)
    expect = {(2, 3): -1, (4, 1): -1, (3, 2): 1, (1, 4): 1}
    for (p, q), s in expect.items():
        sq = GA.sig(p, q)
        om = {tuple(range(5)): F(1)}
        ok = ok and GA.eq(GA.mul(om, om, sq), GA.sc(s))
        if s == 1:
            e = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
            ok = ok and GA.eq(GA.mul(e, e, sq), e) and not GA.eq(e, GA.sc(1)) and not GA.is_zero(e)
        else:
            for a, b in AB_SAMPLES:
                x = GA.add(GA.sc(a), GA.scal(b, om))
                xb = GA.sub(GA.sc(a), GA.scal(b, om))
                ok = ok and GA.eq(GA.mul(x, xb, sq), GA.sc(a * a + b * b))
    _tp_rv = (ok); assert _tp_rv is not False, "check_signature_reversal_changes_the_centre"; return _tp_rv
