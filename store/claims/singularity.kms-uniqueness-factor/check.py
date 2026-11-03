"""singularity.kms-uniqueness-factor: exact checks on matrix factors Mat_n, n = 2, 3, 4.

A flow alpha_t = Ad(e^{itK}) is given by a Hermitian K = U diag(k_a) U^T with integer spectrum
(degenerate spectra included) and a rational orthogonal U (non-diagonal K included). For beta != 0
put q = e^{-beta} (a positive rational, both signs of beta: q = 2/3 and 3/2); then e^{-beta K} =
U diag(q^{k_a}) U^T and e^{beta K} = U diag(q^{-k_a}) U^T are exact.
(1) The KMS identity tr(rho a b) = tr(rho b e^{-beta K} a e^{beta K}) for all pairs of matrix units
a, b is solved as a linear system in the n^2 entries of rho: its solution space is exactly
one-dimensional and spanned by e^{-beta K}, so rho = e^{-beta K}/tr e^{-beta K} is the only KMS state
(if and only if).
(2) The KMS states of one flow form a line parametrised by beta: for non-scalar K, different beta give
different states (here q = 2/3, 3/2, 1/5), while the tracial state (beta = 0) is not KMS at
beta != 0 (control).
"""
from fractions import Fraction as F

import GA

R3 = [[F(1, 3), F(2, 3), F(2, 3)], [F(2, 3), F(1, 3), F(-2, 3)], [F(2, 3), F(-2, 3), F(1, 3)]]
R2 = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
FLOWS = [
    (2, [0, 1], None), (2, [0, 1], R2), (3, [0, 1, 1], None), (3, [0, 1, 3], R3),
    (3, [2, 0, 0], R3), (4, [0, 0, 1, 2], None),
]
QS = [F(2, 3), F(3, 2)]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


mm = GA.mat_mul


def tp(A):
    return [list(r) for r in zip(*A)]


def expK(n, spec, U, q):
    """e^{-beta K} with q = e^{-beta}: U diag(q^{k}) U^T."""
    U = U or eye(n)
    D = [[q ** spec[i] if i == j else F(0) for j in range(n)] for i in range(n)]
    return mm(mm(U, D), tp(U))


def kms_rows(n, E, Ei):
    """Rows of the linear system tr(rho a b) - tr(rho b E a Ei) = 0 in the unknowns rho[r][c]."""
    rows = []
    units = [(i, j) for i in range(n) for j in range(n)]
    for (i, j) in units:
        for (k, l) in units:
            # tr(rho E_ij E_kl) = delta_jk rho[l][i]
            row = [F(0)] * (n * n)
            if j == k:
                row[l * n + i] += 1
            # b E a Ei with a = E_ij, b = E_kl: (E_kl E E_ij Ei) = E[l][i] * E_k(row j of Ei)
            # tr(rho E_kl E E_ij Ei) = E[l][i] * sum_c Ei[j][c] rho[c][k]
            for c in range(n):
                row[c * n + k] -= E[l][i] * Ei[j][c]
            rows.append(row)
    return rows


def check_kms_iff_gibbs():
    cases = 0
    for n, spec, U in FLOWS:
        for q in QS:
            E = expK(n, spec, U, q)
            Ei = expK(n, spec, U, 1 / q)
            assert mm(E, Ei) == eye(n)
            ker = GA.field_kernel(kms_rows(n, E, Ei))
            assert len(ker) == 1, (n, spec, len(ker))
            flatE = [E[r][c] for r in range(n) for c in range(n)]
            assert GA.field_rank([ker[0], flatE]) == 1
            # normalised: the Gibbs state, with trace 1
            Z = sum((E[i][i] for i in range(n)), F(0))
            rho = [[E[r][c] / Z for c in range(n)] for r in range(n)]
            assert sum((rho[i][i] for i in range(n)), F(0)) == 1
            assert all(sum(r) == 0 for r in mm(kms_rows(n, E, Ei), [[x] for x in flatE]))
            cases += 1
    assert cases == 12, cases


def check_kms_states_form_a_line_in_beta():
    for n, spec, U in FLOWS:
        states = []
        for q in (F(2, 3), F(3, 2), F(1, 5)):
            E = expK(n, spec, U, q)
            Z = sum((E[i][i] for i in range(n)), F(0))
            states.append([[E[r][c] / Z for c in range(n)] for r in range(n)])
        assert states[0] != states[1] and states[1] != states[2] and states[0] != states[2]
        # control: the tracial state id/n is not KMS at beta != 0
        E = expK(n, spec, U, F(2, 3))
        Ei = expK(n, spec, U, F(3, 2))
        tracial = [F(1, n) if r == c else F(0) for r in range(n) for c in range(n)]
        res = mm(kms_rows(n, E, Ei), [[x] for x in tracial])
        assert any(r[0] != 0 for r in res)
    # a scalar K (all eigenvalues equal) has the tracial state at every beta: the line degenerates
    E = expK(3, [1, 1, 1], R3, F(2, 3))
    Ei = expK(3, [1, 1, 1], R3, F(3, 2))
    assert GA.field_kernel(kms_rows(3, E, Ei)) == [[F(1), F(0), F(0), F(0), F(1), F(0), F(0), F(0), F(1)]]
