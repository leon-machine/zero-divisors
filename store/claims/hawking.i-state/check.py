"""hawking.i-state: exact checks.

Boltzmann factors x_j = e^{-beta omega_j} are rational; the Fermi-Dirac symbol is n_j = x_j/(1 + x_j) =
1/(e^{beta omega_j} + 1).
(1) Existence on windows (Fock space of a three-mode window, Jordan-Wigner matrices): the product state with
    marginals diag(1 - n_j, n_j), built from the symbol, equals the Gibbs matrix e^{-beta H_F}/Z, built from
    the dynamics, entry by entry; it satisfies the KMS identity omega(A alpha_{i beta}(B)) = omega(B A) on all
    4096 matrix-unit pairs; it is quasi-free (Wick: omega(a1* a1 a2* a2) = n1 n2, odd moments vanish); and
    its restriction (partial trace) to the two-mode subwindow is the two-mode FD state, so the window
    states are consistent and define one state on the inductive limit.
(2), (3) Converse on a two-mode window, for three pairs of Boltzmann factors (one with degenerate
    frequencies): the full KMS constraint system for an unknown 4 x 4 density matrix has a one-dimensional
    solution space spanned by the Gibbs matrix; the solution has vanishing pairing omega(a_j* a_k*) = 0 and
    symbol omega(a_j* a_k) = delta_jk n_j.
(2), (3) at the one-particle level, with a non-diagonal h: E = e^{-beta h} = O diag(x) O^T for a rational
    orthogonal O. The KMS identity on (a(g), a*(f)) gives (1 - A) E = A; solved for an unknown 3 x 3 symbol
    A it has the unique solution A = E (1 + E)^{-1}, which satisfies A (1 + E) = E, commutes with h and has
    eigenvalues x_j/(1 + x_j) on the eigenvectors of h. On (a*(g), a*(f)) it gives P E = -P for an unknown
    antisymmetric pairing P, whose only solution is P = 0.
"""
from fractions import Fraction as F
from itertools import product

import GA
import fock
from tp_premise import premise

XS3 = [F(1, 2), F(1, 3), F(1, 5)]
PAIRS = [(F(1, 2), F(1, 3)), (F(2, 7), F(2, 7)), (F(9, 4), F(1, 6))]
O3 = [[F(1, 3), F(2, 3), F(2, 3)], [F(2, 3), F(1, 3), F(-2, 3)], [F(2, 3), F(-2, 3), F(1, 3)]]
XH = [F(1, 4), F(2, 3), F(5, 2)]


mm = GA.mat_mul


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def tp(A):
    return [list(r) for r in zip(*A)]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def cre(j, k):
    """a_j^dagger on k modes, Jordan-Wigner, basis index = bitmask (bit i = mode i)."""
    return fock.to_dense(fock.cre(j, k), 2 ** k)


def boltz(xs, s):
    out = F(1)
    for j, x in enumerate(xs):
        if s >> j & 1:
            out *= x
    return out


def check_window_gibbs_fd_kms_quasifree_consistent():
    premise("hawking.gibbs-states-are-kms-conversely-finite")
    premise("hawking.imported-quasi-free-states-car-algebra")
    premise("hawking.imported-kms-passes-inductive-limits")
    k, N = 3, 8
    Z = sum(boltz(XS3, s) for s in range(N))
    gibbs = [boltz(XS3, s) / Z for s in range(N)]
    nn = [x / (1 + x) for x in XS3]
    fd = []
    for s in range(N):
        w = F(1)
        for j in range(k):
            w *= nn[j] if s >> j & 1 else 1 - nn[j]
        fd.append(w)
    ok = fd == gibbs and Z == F(12, 5)
    # KMS on all matrix-unit pairs E_{s1 t1}, E_{s2 t2}
    for s1, t1, s2, t2 in product(range(N), repeat=4):
        lhs = fd[s1] if (t1 == s2 and t2 == s1) else F(0)          # omega(E_{s1t1} E_{s2t2})
        rhs = (boltz(XS3, s1) / boltz(XS3, t1)) * fd[s2] if (t2 == s1 and s2 == t1) else F(0)
        ok = ok and lhs == rhs
    rho = [[fd[i] if i == j else F(0) for j in range(N)] for i in range(N)]
    a = [cre(j, k) for j in range(k)]
    ad = [tp(x) for x in a]
    num = [mm(a[j], ad[j]) for j in range(k)]
    ok = ok and all(tr(mm(rho, num[j])) == nn[j] for j in range(k))
    ok = ok and tr(mm(rho, mm(num[0], num[1]))) == nn[0] * nn[1]
    ok = ok and tr(mm(rho, mm(num[0], mm(num[1], num[2])))) == nn[0] * nn[1] * nn[2]
    ok = ok and all(tr(mm(rho, a[j])) == 0 for j in range(k))
    ok = ok and tr(mm(rho, mm(a[0], mm(a[1], ad[2])))) == 0
    # partial trace over mode 2 gives the two-mode FD state
    red = [sum(fd[s | (b << 2)] for b in (0, 1)) for s in range(4)]
    want = []
    for s in range(4):
        w = F(1)
        for j in range(2):
            w *= nn[j] if s >> j & 1 else 1 - nn[j]
        want.append(w)
    _tp_rv = (ok and red == want); assert _tp_rv is not False, "check_window_gibbs_fd_kms_quasifree_consistent"; return _tp_rv


def kms_kernel(xs):
    N = 4
    rows = []
    for s1, t1, s2, t2 in product(range(N), repeat=4):
        c = [F(0)] * 16                      # unknown rho[a][b] at 4 a + b; omega(E_ab) = rho[b][a]
        if t1 == s2:
            c[4 * t2 + s1] += 1
        if t2 == s1:
            c[4 * t1 + s2] -= boltz(xs, s1) / boltz(xs, t1)
        if any(c):
            rows.append(c)
    return GA.field_kernel(rows)


def check_full_kms_forces_gibbs_gauge_invariance_and_fd_symbol():
    premise("hawking.gibbs-states-are-kms-conversely-finite")
    ok = True
    for xs in PAIRS:
        ker = kms_kernel(xs)
        ok = ok and len(ker) == 1
        v = ker[0]
        rho = [[v[4 * a + b] for b in range(4)] for a in range(4)]
        t = tr(rho)
        rho = [[x / t for x in r] for r in rho]
        Z = sum(boltz(xs, s) for s in range(4))
        ok = ok and all(rho[a][b] == (boltz(xs, a) / Z if a == b else 0) for a in range(4) for b in range(4))
        a_ = [cre(j, 2) for j in range(2)]
        ad = [tp(x) for x in a_]
        for j in range(2):
            for kk in range(2):
                ok = ok and tr(mm(rho, mm(a_[j], a_[kk]))) == 0          # pairing omega(a*_j a*_k)
                sym = tr(mm(rho, mm(a_[j], ad[kk])))                     # omega(a*_j a_k)
                ok = ok and sym == (xs[j] / (1 + xs[j]) if j == kk else 0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_full_kms_forces_gibbs_gauge_invariance_and_fd_symbol"; return _tp_rv


def check_one_particle_kms_symbol_and_pairing():
    premise("hawking.imported-quasi-free-states-car-algebra")
    ok = mm(O3, tp(O3)) == eye(3)
    D = [[XH[i] if i == j else F(0) for j in range(3)] for i in range(3)]
    E = mm(mm(O3, D), tp(O3))
    ok = ok and any(E[i][j] != 0 for i in range(3) for j in range(3) if i != j)
    # unknown A (9 entries): (1 - A) E - A = 0, i.e. A (E + 1) = E
    rows, rhs = [], []
    for i in range(3):
        for j in range(3):
            c = [F(0)] * 9
            for t in range(3):
                c[3 * i + t] += E[t][j] + (1 if t == j else 0)
            rows.append(c)
            rhs.append(E[i][j])
    ok = ok and GA.field_rank(rows) == 9
    sol = GA.field_solve(rows, rhs)
    A = [[sol[3 * i + j] for j in range(3)] for i in range(3)]
    I3 = eye(3)
    ok = ok and mm(A, [[E[i][j] + I3[i][j] for j in range(3)] for i in range(3)]) == E
    ok = ok and mm(A, E) == mm(E, A)
    AO = mm(A, O3)
    ok = ok and all(AO[i][j] == O3[i][j] * XH[j] / (1 + XH[j]) for i in range(3) for j in range(3))
    # pairing: unknown antisymmetric P (p01, p02, p12); KMS: P E + P = 0
    def Pm(p):
        return [[F(0), p[0], p[1]], [-p[0], F(0), p[2]], [-p[1], -p[2], F(0)]]
    cols = []
    for u in range(3):
        e = [F(1) if t == u else F(0) for t in range(3)]
        P = Pm(e)
        M = mm(P, E)
        cols.append([M[i][j] + P[i][j] for i in range(3) for j in range(3)])
    sysm = tp(cols)
    ok = ok and GA.field_rank(sysm) == 3 and GA.field_kernel(sysm) == []
    _tp_rv = (ok); assert _tp_rv is not False, "check_one_particle_kms_symbol_and_pairing"; return _tp_rv
