"""hawking.i-state-continuum: exact checks of the window case (finite spectral windows of a pure-point h).

Windows of two and three fermionic modes, Jordan-Wigner matrices over Q. The one-particle dynamics is
h = U diag(w) U^T for rational orthogonal U, with rational Boltzmann factors q_j = e^{-beta w_j}, so
e^{-beta h} = U diag(q) U^T and e^{beta h} = U diag(1/q) U^T are exact.
(1) The quasi-free state with symbol A_I = (1 + e^{beta h})^{-1}, built from the symbol alone as the density
    det(1 - A) Gamma(A (1 - A)^{-1}) (Fact hawking.imported-quasi-free-states-car-algebra), equals the Gibbs
    state Gamma(e^{-beta h})/Z of the dynamics and satisfies the KMS identity
    tr(rho X Y) = tr(rho Y G X G^{-1}) on all pairs of matrix units (two- and three-mode windows); 0 <= A_I <= 1.
(2) Pairing: G a(f) G^{-1} = a(e^{beta h} f) as an operator identity, and the KMS identity for a quasi-free state's
    pairing P(f, g) = omega(a(f) a(g)) (antisymmetric) reads P(f, g) = -P(e^{beta h} f, g); its solution space is
    zero (the pairing vanishes).
(3) Symbol derivation: the two-point KMS identity <g, A (1 + e^{-beta h}) f> = <g, e^{-beta h} f> for all basis
    f, g, with A an unknown matrix (n^2 unknowns), has the unique solution A = A_I, on two- and three-mode windows.
Not checked: the continuum statements themselves (the core, unbounded h, the upgrade of Fact
hawking.imported-quasi-free-kms-reduces-two) and the closing uniqueness sentence, which rests on Fact
hawking.imported-ideal-fermi-gas-uniqueness (checked on windows in hawking.full-uniqueness-given-dynamics).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock
from tp_premise import premise

U2 = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
# rational orthogonal 3 x 3 (Pythagorean quadruple 1, 2, 2, 3)
U3 = [[F(1, 3), F(2, 3), F(2, 3)], [F(2, 3), F(1, 3), F(-2, 3)], [F(2, 3), F(-2, 3), F(1, 3)]]
WINDOWS = [((F(1, 2), F(1, 3)), U2), ((F(1, 4), F(2), F(1, 3)), U3)]


mm = GA.mat_mul


def tr(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def madd(a, b, c=1):
    return [[a[i][j] + F(c) * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def ident(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def diag(v):
    return [[v[i] if i == j else F(0) for j in range(len(v))] for i in range(len(v))]


def ann(n, j):
    """a_j on n Jordan-Wigner modes, dense (LSB bitmask basis)."""
    return fock.to_dense(fock.ann(j, n), 1 << n)


def gamma(n, T):
    d = 1 << n
    Cs = [tr(ann(n, j)) for j in range(n)]
    G = [[F(0)] * d for _ in range(d)]
    for s in range(d):
        v = [[F(1)]] + [[F(0)] for _ in range(d - 1)]
        for i in reversed([i for i in range(n) if (s >> i) & 1]):
            cf = [[F(0)] * d for _ in range(d)]
            for j in range(n):
                cf = madd(cf, Cs[j], T[j][i])
            v = mm(cf, v)
        for r in range(d):
            G[r][s] = v[r][0]
    return G


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    return sum((-1) ** j * M[0][j] * det([row[:j] + row[j + 1:] for row in M[1:]]) for j in range(n))


def inverse(M):
    n = len(M)
    cols = [GA.field_solve([row[:] for row in M], [F(1) if i == j else F(0) for i in range(n)]) for j in range(n)]
    return tr(cols)


def check_fermi_dirac_quasi_free_state_is_kms():
    premise("hawking.imported-quasi-free-states-car-algebra")
    premise("hawking.i-state")
    ok = True
    for qs, U in WINDOWS:
        n = len(qs)
        d = 1 << n
        g = mm(mm(U, diag(list(qs))), tr(U))
        gi = mm(mm(U, diag([1 / q for q in qs])), tr(U))
        AI = inverse(madd(ident(n), gi))                    # (1 + e^{beta h})^{-1}
        ok = ok and AI == mm(mm(U, diag([q / (1 + q) for q in qs])), tr(U))
        ok = ok and all(0 < q / (1 + q) < 1 for q in qs)
        Ohm = mm(AI, inverse(madd(ident(n), AI, -1)))       # A (1 - A)^{-1}
        rho = [[det(madd(ident(n), AI, -1)) * x for x in row] for row in gamma(n, Ohm)]
        G = gamma(n, g)
        Z = sum(G[i][i] for i in range(d))
        ok = ok and rho == [[x / Z for x in row] for row in G]
        ok = ok and sum(rho[i][i] for i in range(d)) == 1
        Gi = gamma(n, gi)
        # KMS on matrix units: tr(rho E_ab E_cd) = tr(rho E_cd G E_ab G^{-1})
        for a in range(d):
            for b in range(d):
                col_a = [G[r][a] for r in range(d)]
                row_b = Gi[b]
                for c in range(d):
                    for e in range(d):
                        lhs = rho[e][a] if b == c else F(0)
                        # tr(rho E_cd G E_ab G^{-1}) = sum_r rho[r][c] (G E_ab G^{-1})[e][r]
                        rhs = sum(rho[r][c] * G[e][a] * row_b[r] for r in range(d))
                        ok = ok and lhs == rhs
                        if not ok:
                            _tp_rv = (False); assert _tp_rv is not False, "check_fermi_dirac_quasi_free_state_is_kms"; return _tp_rv
                del col_a
    _tp_rv = (ok); assert _tp_rv is not False, "check_fermi_dirac_quasi_free_state_is_kms"; return _tp_rv


def check_pairing_of_kms_state_vanishes():
    premise("hawking.i-state")
    ok = True
    for qs, U in WINDOWS:
        n = len(qs)
        gi = mm(mm(U, diag([1 / q for q in qs])), tr(U))      # e^{beta h}
        G = gamma(n, mm(mm(U, diag(list(qs))), tr(U)))
        Gi = gamma(n, gi)
        As = [ann(n, j) for j in range(n)]
        for j in range(n):
            lhs = mm(mm(G, As[j]), Gi)
            rhs = [[F(0)] * (1 << n) for _ in range(1 << n)]
            for k in range(n):
                rhs = madd(rhs, As[k], gi[k][j])
            ok = ok and lhs == rhs
        # unknown antisymmetric pairing P_{ij} = omega(a_i a_j), i < j
        pairs = list(combinations(range(n), 2))

        def P_coeff(i, j):
            row = [F(0)] * len(pairs)
            if i < j:
                row[pairs.index((i, j))] = F(1)
            elif i > j:
                row[pairs.index((j, i))] = F(-1)
            return row
        rows = []
        for i in range(n):
            for j in range(n):
                # P(e_i, e_j) + P(e^{beta h} e_i, e_j) = 0
                row = P_coeff(i, j)
                for k in range(n):
                    row = [x + gi[k][i] * y for x, y in zip(row, P_coeff(k, j))]
                rows.append(row)
        ok = ok and GA.field_rank(rows) == len(pairs) and len(pairs) == n * (n - 1) // 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_pairing_of_kms_state_vanishes"; return _tp_rv


def check_two_point_kms_forces_the_fermi_dirac_symbol():
    premise("hawking.i-state")
    ok = True
    for qs, U in WINDOWS:
        n = len(qs)
        g = mm(mm(U, diag(list(qs))), tr(U))
        M = madd(ident(n), g)
        # unknown A (n^2 entries, row-major): (A M)_{ij} = g_{ij}
        rows, rhs = [], []
        for i in range(n):
            for j in range(n):
                row = [F(0)] * (n * n)
                for k in range(n):
                    row[n * i + k] += M[k][j]
                rows.append(row)
                rhs.append(g[i][j])
        ok = ok and GA.field_rank(rows) == n * n
        sol = GA.field_solve(rows, rhs)
        A = [sol[n * i:n * i + n] for i in range(n)]
        ok = ok and A == mm(mm(U, diag([q / (1 + q) for q in qs])), tr(U))
    _tp_rv = (ok); assert _tp_rv is not False, "check_two_point_kms_forces_the_fermi_dirac_symbol"; return _tp_rv
