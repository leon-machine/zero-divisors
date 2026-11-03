"""lepton.imported-twistor-state-pair-system-excitations: exact checks.

Model: the Fock model of Cl(2,4)_C on Lambda W (W maximal isotropic, three modes; wedge and contraction
realise the six ambient generators), with Gaussian-rational coefficients.
(1) The six generators satisfy {c(e_a), c(e_b)} = 2 g_ab; the 64 ordered blade products are linearly
    independent, so Cl(V_C) -> End(Lambda W) = M_8(C) is onto and the module is irreducible; vectors are
    odd, so the halves CS = Lambda^even W and CS- = Lambda^odd W (dimension four each) are exchanged.
(2) For seven sample conformal spinors u (including the vacuum, the top-even state and generic
    Gaussian-rational combinations) the annihilator W_u has dimension exactly three, is totally
    isotropic, and the joint kernel of c(W_u) on the module is the line C u: u is the Fock vacuum of
    the three ladder pairs built on W_u.
(3) For each such u and a dual isotropic complement U' of W_u (the annihilator of an odd spinor,
    transversal to W_u), the eight ordered products c(x_I) u over the subsets I of a basis of U' are a
    basis of the module, the even products lying in CS and the odd ones in CS-. Control: with U' = W_u
    itself the map has rank one.
The statement takes U' as the dual complement of W; the map is an isomorphism for a complement of W_u,
which is the form of the cited source (T9 Thm. 5.3(2)) and is the form checked (see the run report).
standard-model.imported-pair-systems-two-chirality-halves restates this content and is not called.
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


def blade_product(idx):
    M = ID8
    for a in idx:
        M = mmul(M, CB[a])
    return M


# sample conformal spinors (coefficients on 1, w0w1, w0w2, w1w2)
U_SAMPLES = [(1, 0, 0, 0), (0, 0, 0, 1), (1, 1, 0, 0), (1, 2, -3, 5), (QI(1, 1), 2, QI(0, -1), 3),
             (0, 1, 1, 1), (2, 0, QI(0, 1), QI(4, -3))]
# odd spinors whose annihilators serve as candidate complements
ODD_SAMPLES = [(0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (1, 1, 1, 1), (1, -2, 3, 1),
               (QI(0, 1), 1, 2, -1)]


def complement_for(Wu):
    for c4 in ODD_SAMPLES:
        Uc = annihilator(from_odd(c4))
        if len(Uc) == 3 and GA.field_rank(Wu + Uc) == 6:
            return Uc
    return None


def excitation_states(u, basis3):
    out = []
    for k in range(4):
        for I in combinations(range(3), k):
            s = u
            for i in reversed(I):
                s = apply(c_of(basis3[i]), s)
            out.append((k, s))
    return out


def check_fock_module_irreducible_with_two_halves():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    ok = True
    for a in range(6):
        for b in range(6):
            ac = madd(mmul(CB[a], CB[b]), mmul(CB[b], CB[a]))
            ok = ok and ac == (mscal(2 * SQ[a], ID8) if a == b else zmat())
    rows = [[x for row in blade_product(idx) for x in row]
            for k in range(7) for idx in combinations(range(6), k)]
    ok = ok and len(rows) == 64 and GA.field_rank(rows) == 64
    ok = ok and len(EVEN) == 4 and len(ODD) == 4
    for a in range(6):
        for r in range(8):
            for c in range(8):
                if CB[a][r][c]:
                    ok = ok and (len(SUBSETS[r]) + len(SUBSETS[c])) % 2 == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_fock_module_irreducible_with_two_halves"; return _tp_rv


def check_each_conformal_spinor_is_a_fock_vacuum():
    premise("correspondence.twistors-are-states-three-ladder-pairs")
    ok = True
    for c4 in U_SAMPLES:
        u = from_even(c4)
        Wu = annihilator(u)
        ok = ok and len(Wu) == 3
        ok = ok and all(ip(x, y) == ZERO for x in Wu for y in Wu)
        jk = joint_kernel(Wu)
        ok = ok and len(jk) == 1 and GA.field_rank(jk + [u]) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_each_conformal_spinor_is_a_fock_vacuum"; return _tp_rv


def check_excitations_from_a_dual_complement_span_the_module():
    premise("correspondence.twistors-are-states-three-ladder-pairs")
    ok = True
    for c4 in U_SAMPLES:
        u = from_even(c4)
        Wu = annihilator(u)
        Uc = complement_for(Wu)
        ok = ok and Uc is not None
        ok = ok and all(ip(x, y) == ZERO for x in Uc for y in Uc)
        pairing = [[ip(x, y) for y in Uc] for x in Wu]
        ok = ok and GA.field_rank(pairing) == 3
        states = excitation_states(u, Uc)
        ok = ok and GA.field_rank([s for _, s in states]) == 8
        for k, s in states:
            wrong = ODD if k % 2 == 0 else EVEN
            ok = ok and all(not s[i] for i in wrong)
        # control: products from W_u itself only reach the line of u
        ok = ok and GA.field_rank([s for _, s in excitation_states(u, Wu) if any(s)]) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_excitations_from_a_dual_complement_span_the_module"; return _tp_rv
