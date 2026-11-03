"""hawking.full-uniqueness-given-dynamics: exact checks on finite windows (the window case of the corollary).

Two fermionic modes, Jordan-Wigner matrices over Q, |S> = prod_{i in S, increasing} a_i^dag |0>. One-particle
dynamics h = U diag(w1, w2) U^T with the rational rotation U = [[3/5, -4/5], [4/5, 3/5]] (h not diagonal in the
mode basis) and Boltzmann factors q_j = e^{-beta w_j}, so e^{-beta h} = U diag(q1, q2) U^T is rational; the
second quantisation G = e^{-beta H} = Gamma(e^{-beta h}) (1 on the vacuum, e^{-beta h} on one particle, the
determinant on two) is built from creation operators. A second, diagonal h is also used.
(1) Among ALL states (all 4 x 4 density matrices rho, 16 unknowns) the KMS condition
    tr(rho A B) = tr(rho B G A G^{-1}) for all matrix units A, B has a one-dimensional solution space, spanned by G.
(2) The normalised solution is the quasi-free state omega_I: its two-point matrix omega(a_i^dag a_j) is the symbol
    A_I = (1 + e^{beta h})^{-1} = U diag(q/(1 + q)) U^T (transposed per the convention <g, A f>), its pairing
    omega(a_i a_j) vanishes, and the four-point function obeys Wick's rule (the determinant of the two-point
    matrix).
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

U = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
DYN = [((F(1, 2), F(1, 3)), U), ((F(1, 5), F(3)), [[F(1), F(0)], [F(0), F(1)]])]
D = 4


mm = GA.mat_mul


def tr(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def madd(a, b, c=1):
    return [[a[i][j] + F(c) * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def ident(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def ann(j):
    """a_j on two Jordan-Wigner modes, dense (LSB bitmask basis)."""
    return fock.to_dense(fock.ann(j, 2), D)


A = [ann(0), ann(1)]
C = [tr(A[0]), tr(A[1])]


def second_quantise(T):
    """Gamma(T): |S> -> prod a^dag(T e_i)|0>, as a matrix."""
    G = [[F(0)] * D for _ in range(D)]
    for s in range(D):
        v = [[F(1)], [F(0)], [F(0)], [F(0)]]
        for i in reversed([i for i in range(2) if (s >> i) & 1]):
            cf = madd([[F(0)] * D for _ in range(D)], C[0], T[0][i])
            cf = madd(cf, C[1], T[1][i])
            v = mm(cf, v)
        for r in range(D):
            G[r][s] = v[r][0]
    return G


def one_particle(qs, rot):
    return mm(mm(rot, [[qs[0], F(0)], [F(0), qs[1]]]), tr(rot))


def kms_states(G, Gi):
    """Kernel of rho -> {tr(rho A B) - tr(rho B G A G^{-1})} over matrix units A, B."""
    units = []
    for a in range(D):
        for b in range(D):
            E = [[F(0)] * D for _ in range(D)]
            E[a][b] = F(1)
            units.append(E)
    rows = []
    for Aa in units:
        sig = mm(mm(G, Aa), Gi)
        for Bb in units:
            X = madd(mm(Aa, Bb), mm(Bb, sig), -1)
            # tr(rho X) = sum_{r,c} rho[r][c] X[c][r]
            rows.append([X[c][r] for r in range(D) for c in range(D)])
    return GA.field_kernel(rows)


def check_kms_state_unique_among_all_states():
    premise("hawking.imported-ideal-fermi-gas-uniqueness")
    ok = True
    for qs, rot in DYN:
        g1 = one_particle(qs, rot)
        g1i = one_particle((1 / qs[0], 1 / qs[1]), rot)
        G, Gi = second_quantise(g1), second_quantise(g1i)
        ok = ok and mm(G, Gi) == ident(D)
        ok = ok and G[0][0] == 1 and G[3][3] == qs[0] * qs[1]
        ker = kms_states(G, Gi)
        ok = ok and len(ker) == 1
        rho = [[ker[0][D * r + c] for c in range(D)] for r in range(D)]
        ok = ok and GA.field_rank([sum(rho, []), sum(G, [])]) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_kms_state_unique_among_all_states"; return _tp_rv


def check_unique_state_is_quasi_free_with_fermi_dirac_symbol():
    premise("hawking.imported-ideal-fermi-gas-uniqueness")
    premise("hawking.imported-quasi-free-states-car-algebra")
    ok = True
    for qs, rot in DYN:
        G = second_quantise(one_particle(qs, rot))
        Z = sum(G[i][i] for i in range(D))
        ok = ok and Z == (1 + qs[0]) * (1 + qs[1])
        rho = [[G[r][c] / Z for c in range(D)] for r in range(D)]

        def om(X):
            return sum(rho[r][c] * X[c][r] for r in range(D) for c in range(D))
        two = [[om(mm(C[i], A[j])) for j in range(2)] for i in range(2)]
        sym = mm(mm(rot, [[qs[0] / (1 + qs[0]), F(0)], [F(0), qs[1] / (1 + qs[1])]]), tr(rot))
        ok = ok and two == tr(sym)
        ok = ok and all(om(mm(A[i], A[j])) == 0 and om(mm(C[i], C[j])) == 0 for i in range(2) for j in range(2))
        four = om(mm(mm(C[0], C[1]), mm(A[1], A[0])))
        ok = ok and four == two[0][0] * two[1][1] - two[0][1] * two[1][0]
    _tp_rv = (ok); assert _tp_rv is not False, "check_unique_state_is_quasi_free_with_fermi_dirac_symbol"; return _tp_rv
