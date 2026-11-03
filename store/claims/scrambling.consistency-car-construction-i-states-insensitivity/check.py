"""scrambling.consistency-car-construction-i-states-insensitivity: exact checks.

(i) (assembly level, its computable core) With m-independent frequencies the one-particle Hamiltonian
    h = sum_l omega_l 1_(2l+1) commutes with the su(2) generators J_z, J_+, J_- of the spin-l blocks
    (l = 1/2, 1, 3/2, rational matrices with [J_+, J_-] = 2 J_z), so the modular flow is a scalar on each
    multiplet; control: an m-dependent h fails to commute.
(ii) On the full Fock space of 4 modes (Jordan-Wigner), E_ij = psi_i^dagger psi_j satisfy
    [E_ij, E_kl] = delta_jk E_il - delta_li E_kj on every basis state, commute with the number operator
    (gauge invariant), preserve the one-particle subspace and act there as the matrix units e_ij; their
    one-particle restrictions span Mat_4 (rank 16).
(iii) Three modes, h with a degenerate two-dimensional multiplet, h = O diag(w1, w1, w2) O^T (O rational
    orthogonal); the I-state symbol Lambda = g(h) = O diag(n1, n1, n2) O^T, n = x/(1 + x). The quasi-free
    density rho = Gamma(Lambda (1 - Lambda)^{-1}) / Z (Gamma = second quantisation, Z = det(1 - Lambda)^{-1})
    has two-point function tr(rho a_i^dagger a_j) = Lambda_ji. For unitaries U over Q(i) with U h U* = h
    (an SU(2) element and a phase on the multiplet, conjugated by O): U Lambda U* = Lambda, and
    Gamma(U) rho Gamma(U)* = rho entrywise on the 8-dimensional Fock space. Control: with
    non-degenerate occupancies the same SU(2) element moves the state.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

QI = GA.QI
ZERO, ONE = QI(0), QI(1)


def q(x):
    return x if isinstance(x, QI) else QI(x)


mm = GA.field_mat_mul


def dag(A):
    return [[q(A[j][i]).conj() for j in range(len(A))] for i in range(len(A[0]))]


def qmat(A):
    return [[q(x) for x in r] for r in A]


def meq(A, B):
    return (len(A) == len(B) and all(len(ra) == len(rb) for ra, rb in zip(A, B)) and all(q(a) == q(b) for ra, rb in zip(A, B) for a, b in zip(ra, rb)))


def sub(A, B):
    return [[q(a) - q(b) for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


# ---- (i) spin blocks ----
def spin_block(two_l):
    dim = two_l + 1
    ms = [F(two_l, 2) - k for k in range(dim)]                     # m = l, l-1, ..., -l
    Jz = [[ms[i] if i == j else F(0) for j in range(dim)] for i in range(dim)]
    Jp = [[F(0)] * dim for _ in range(dim)]
    l = F(two_l, 2)
    for k in range(1, dim):
        m = ms[k]
        Jp[k - 1][k] = l * (l + 1) - m * (m + 1)                     # the squared ladder coefficient
    return Jz, Jp


def blockdiag(blocks):
    n = sum(len(b) for b in blocks)
    M = [[F(0)] * n for _ in range(n)]
    o = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                M[o + i][o + j] = b[i][j]
        o += len(b)
    return M


rmm = GA.mat_mul


def check_multiplet_scalar_flow_commutes_with_su2():
    ok = True
    blocks = [spin_block(t) for t in (1, 2, 3)]
    # rational form of the spin-l rep: J+ with unit entries, J- carrying the squared coefficients
    Jz = blockdiag([b[0] for b in blocks])
    Jp2 = blockdiag([b[1] for b in blocks])
    n = len(Jz)
    Jp = [[F(1) if Jp2[i][j] != 0 else F(0) for j in range(n)] for i in range(n)]
    Jm = [[Jp2[j][i] for j in range(n)] for i in range(n)]               # J- carries the squared coefficient
    comm = [[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(rmm(Jp, Jm), rmm(Jm, Jp))]
    ok = ok and comm == [[2 * x for x in r] for r in Jz] and n == 9
    omegas = [F(3), F(5, 2), F(7, 3)]
    h = blockdiag([[[omegas[k] if i == j else F(0) for j in range(t + 1)] for i in range(t + 1)]
                   for k, t in enumerate((1, 2, 3))])
    for J in (Jz, Jp, Jm):
        ok = ok and rmm(h, J) == rmm(J, h)
    hbad = [[h[i][j] + (F(i, 7) if i == j else 0) for j in range(n)] for i in range(n)]
    ok = ok and rmm(hbad, Jp) != rmm(Jp, hbad)
    _tp_rv = (ok); assert _tp_rv is not False, "check_multiplet_scalar_flow_commutes_with_su2"; return _tp_rv


# ---- (ii) bilinears on Fock space ----
def pdp(a, b, sv):
    """psi_a^dagger psi_b on a state vector (bitmask basis, Jordan-Wigner)."""
    return fock.cre_on(a, fock.ann_on(b, sv))


def lin(*terms):
    return fock.vadd(*[fock.vsc(sgn, d) for sgn, d in terms])


def check_bilinears_gl_n_and_matrix_units():
    premise("scrambling.boundary-mode-space-matrix")
    NM = 4
    ok = True
    for i in range(NM):
        for j in range(NM):
            for k in range(NM):
                for l in range(NM):
                    for s in range(2 ** NM):
                        sv = {s: F(1)}
                        lhs = lin((1, pdp(i, j, pdp(k, l, sv))), (-1, pdp(k, l, pdp(i, j, sv))))
                        rhs = lin(*([(1, pdp(i, l, sv))] if j == k else []), *([(-1, pdp(k, j, sv))] if l == i else []))
                        ok = ok and lhs == rhs
    rows = []
    for i in range(NM):
        for j in range(NM):
            for s in range(2 ** NM):
                img = pdp(i, j, {s: F(1)})
                ok = ok and all(bin(t).count("1") == bin(s).count("1") for t in img)
            M = [[pdp(i, j, {1 << c: F(1)}).get(1 << r, F(0)) for c in range(NM)] for r in range(NM)]
            ok = ok and all(M[r][c] == (1 if (r, c) == (i, j) else 0) for r in range(NM) for c in range(NM))
            rows.append([x for r in M for x in r])
    _tp_rv = (ok and GA.rank_of_vectors(rows) == 16); assert _tp_rv is not False, "check_bilinears_gl_n_and_matrix_units"; return _tp_rv


# ---- (iii) quasi-free I-state invariance ----
O3 = [[F(1, 3), F(2, 3), F(2, 3)], [F(2, 3), F(1, 3), F(-2, 3)], [F(2, 3), F(-2, 3), F(1, 3)]]


def gamma2(T):
    """Second quantisation of a 3 x 3 matrix T on the 8-dim Fock space (JW basis, bitmask)."""
    G = [[ZERO] * 8 for _ in range(8)]
    for s in range(8):
        modes = [m for m in range(3) if s >> m & 1]
        # |s> = a+_{m1} a+_{m2} ... |0> (m1 < m2 < ...): apply the highest first
        terms = {0: ONE}
        for m in reversed(modes):
            new = {}
            for st, cc in terms.items():
                for tgt in range(3):
                    if q(T[tgt][m]) == ZERO or st >> tgt & 1:
                        continue
                    sg = -1 if bin(st & ((1 << tgt) - 1)).count("1") % 2 else 1
                    new[st | 1 << tgt] = new.get(st | 1 << tgt, ZERO) + q(T[tgt][m]) * cc * sg
            terms = new
        for t, c in terms.items():
            G[t][s] = G[t][s] + c
    return G


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def state_for(ns):
    D = [[ns[i] if i == j else F(0) for j in range(3)] for i in range(3)]
    Lam = rmm(rmm(O3, D), [list(r) for r in zip(*O3)])
    T = rmm(rmm(O3, [[ns[i] / (1 - ns[i]) if i == j else F(0) for j in range(3)] for i in range(3)]),
            [list(r) for r in zip(*O3)])
    I3 = [[F(1) if i == j else F(0) for j in range(3)] for i in range(3)]
    Zinv = det3([[I3[i][j] - Lam[i][j] for j in range(3)] for i in range(3)])
    rho = [[x * Zinv for x in r] for r in gamma2(qmat(T))]
    return Lam, rho


def check_quasi_free_symbol_g_of_h_invariant():
    premise("hawking.imported-quasi-free-states-car-algebra")
    ok = True
    x1, x2 = F(1, 3), F(3, 5)
    ns = [x1 / (1 + x1), x1 / (1 + x1), x2 / (1 + x2)]
    Lam, rho = state_for(ns)
    # trace one and two-point function
    ok = ok and sum((rho[i][i] for i in range(8)), ZERO) == ONE
    a = [[[ONE if (t == s | 1 << j and not s >> j & 1) else ZERO for s in range(8)] for t in range(8)]
         for j in range(3)]
    for j in range(3):
        for s in range(8):
            if not s >> j & 1:
                sg = -1 if bin(s & ((1 << j) - 1)).count("1") % 2 else 1
                a[j][s | 1 << j][s] = QI(sg)
    for i in range(3):
        for j in range(3):
            two = mm(rho, mm(a[i], dag(a[j])))
            ok = ok and sum((two[t][t] for t in range(8)), ZERO) == q(Lam[j][i])
    # unitaries commuting with h: SU(2) on the multiplet, and a phase on it, conjugated by O
    su2 = [[QI(F(3, 5)), QI(0, F(-4, 5)), ZERO], [QI(0, F(-4, 5)), QI(F(3, 5)), ZERO], [ZERO, ZERO, ONE]]
    phase = [[QI(F(5, 13), F(12, 13)), ZERO, ZERO], [ZERO, QI(F(5, 13), F(12, 13)), ZERO],
             [ZERO, ZERO, QI(F(3, 5), F(4, 5))]]
    Oq = qmat(O3)
    OqT = qmat([list(r) for r in zip(*O3)])
    hdiag = [[QI(F(2)) if i == j and i < 2 else (QI(F(7)) if i == j else ZERO) for j in range(3)] for i in range(3)]
    h = mm(mm(Oq, hdiag), OqT)
    for Ub in (su2, phase):
        U = mm(mm(Oq, Ub), OqT)
        ok = ok and meq(mm(U, dag(U)), qmat([[1 if i == j else 0 for j in range(3)] for i in range(3)]))
        ok = ok and meq(mm(mm(U, h), dag(U)), h)
        ok = ok and meq(mm(mm(U, qmat(Lam)), dag(U)), Lam)
        GU = gamma2(U)
        ok = ok and meq(mm(mm(GU, rho), dag(GU)), rho)
    # control: unequal occupancies on the multiplet are moved by the SU(2) element
    Lam2, rho2 = state_for([F(1, 4), F(1, 2), F(1, 3)])
    U = mm(mm(Oq, su2), OqT)
    GU = gamma2(U)
    ok = ok and not meq(mm(mm(GU, rho2), dag(GU)), rho2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_quasi_free_symbol_g_of_h_invariant"; return _tp_rv
