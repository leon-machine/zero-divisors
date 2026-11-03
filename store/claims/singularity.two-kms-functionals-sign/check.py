"""singularity.two-kms-functionals-sign: exact checks.

The mode factor is Mat_2 acting on the two-state module {|0>, v*|0>} with creation v* = E_10,
annihilation v = E_01, N = v* v = diag(0, 1), K = N, fermion parity Gamma = 1 - 2N, and the analytically
continued flow alpha_{i beta}(a) = e^{-beta omega K} a e^{beta omega K} = Eb a Eb^{-1} with Eb = diag(1, x),
x = e^{-beta omega} in (0, 1). The Boltzmann factor x is treated as an exact rational sample (several
values); every identity is linear in the density matrix, so the claims are checked by computing kernels.
(1) The functionals phi = tr(rho .) obeying the ungraded KMS identity on all 16 pairs of matrix units
    form a computed one-dimensional space spanned by Eb; normalised: Z = 1 + x, occupancy 1/(1/x + 1).
(2) The graded identity (eps_b = -1 on the odd units v, v*) gives a one-dimensional space spanned by
    Gamma Eb; Z_Gamma = 1 - x, "occupancy" -x/(1 - x) < 0, so the normalised functional is not positive.
(3) Z and Z_Gamma are the sums over the two module states |0>, v*|0> (the orbit ends because (v*)^2 = 0)
    of x^N and (-1)^N x^N; the ungraded identity is the one whose order reversal carries no sign.
The uniqueness of (1) is computed here (a kernel), not imported, so singularity.kms-uniqueness-factor is
not called.
"""
from fractions import Fraction as F

import GA

XS = [F(1, 2), F(9, 16), F(1, 7), F(3, 4), F(2, 3)]


mm = GA.mat_mul


def tr(A):
    return A[0][0] + A[1][1]


UNITS = [[[F(1) if (i, j) == (a, b) else F(0) for j in range(2)] for i in range(2)]
         for a in range(2) for b in range(2)]


def diag(a, b):
    return [[F(a), F(0)], [F(0), F(b)]]


def kms_kernel(x, graded):
    """Basis of {rho : tr(rho a b) = eps_b tr(rho b alpha(a)) for all units a, b}."""
    Eb, Ebi = diag(1, x), diag(1, 1 / x)
    Gam = diag(1, -1)
    rows = []
    for A in UNITS:
        aa = mm(mm(Eb, A), Ebi)
        for B in UNITS:
            eps = 1
            if graded and mm(mm(Gam, B), Gam) != B:
                eps = -1
            L, R = mm(A, B), mm(B, aa)
            # tr(rho M) = sum_ij rho_ij M_ji ; unknowns rho_00, rho_01, rho_10, rho_11
            rows.append([L[j][i] - eps * R[j][i] for i in range(2) for j in range(2)])
    return GA.field_kernel(rows)


def proportional(v, w):
    return GA.rank_of_vectors([v, w]) == 1


def check_ungraded_kms_is_unique_gibbs_state():
    for x in XS:
        ker = kms_kernel(x, False)
        assert len(ker) == 1
        assert proportional(ker[0], [F(1), F(0), F(0), x])
        Z = tr(diag(1, x))
        assert Z == 1 + x
        occ = tr(mm(diag(1, x), diag(0, 1))) / Z
        assert occ == 1 / (1 / x + 1) and 0 < occ < F(1, 2)
        # the graded identity is not satisfied by the Gibbs state
        assert len(kms_kernel(x, True)) == 1 and not proportional(kms_kernel(x, True)[0], ker[0])
    return True


def check_graded_kms_is_parity_twisted_not_a_state():
    for x in XS:
        ker = kms_kernel(x, True)
        assert len(ker) == 1
        GEb = mm(diag(1, -1), diag(1, x))
        assert proportional(ker[0], [GEb[0][0], GEb[0][1], GEb[1][0], GEb[1][1]])
        ZG = tr(GEb)
        assert ZG == 1 - x
        occ = tr(mm(GEb, diag(0, 1))) / ZG
        assert occ == -x / (1 - x) and occ < 0
        # not positive: the normalised functional is negative on the projector N
        rho = [[c / ZG for c in row] for row in GEb]
        assert rho[1][1] < 0 and rho[0][0] > 1
    return True


def check_plus_one_is_the_two_state_sum():
    vs = [[F(0), F(0)], [F(1), F(0)]]          # creation v* = E_10
    v = [[F(0), F(1)], [F(0), F(0)]]
    N = mm(vs, v)
    assert N == diag(0, 1) and mm(vs, vs) == diag(0, 0)
    vac = [F(1), F(0)]
    orbit = [vac]
    while True:
        nxt = [sum((vs[i][k] * orbit[-1][k] for k in range(2)), F(0)) for i in range(2)]
        if nxt == [F(0), F(0)]:
            break
        orbit.append(nxt)
    assert len(orbit) == 2
    for x in XS:
        occs = [sum((orbit[s][i] * N[i][i] * orbit[s][i] for i in range(2)), F(0)) for s in range(2)]
        Z = sum((x ** int(o) for o in occs), F(0))
        ZG = sum(((-1) ** int(o) * x ** int(o) for o in occs), F(0))
        assert Z == tr(diag(1, x)) == 1 + x
        assert ZG == 1 - x
        # Fermi-Dirac: 1/n = e^{beta omega} + 1; the twisted one has e^{beta omega} - 1 with a minus
        n = x / Z
        nG = -x / ZG
        assert 1 / n - 1 / x == 1
        assert 1 / nG + 1 / x == 1
    return True
