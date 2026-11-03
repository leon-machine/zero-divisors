"""hawking.imported-modular-descent-premises-geometric-normalisation: exact checks of the finite content.

One mode, H = sigma/2 = N - 1/2 on span{|0>, |1>}; the KMS condition at inverse temperature beta is written
with the Boltzmann symbol q = e^(-beta) (rapidity units): alpha_(i beta)(E_ij) = q^(h_i - h_j) E_ij, and
rho is KMS iff Tr(rho A B) = Tr(rho B alpha_(i beta)(A)) for all matrix units A, B.
(1) For q in {9/16, 16/9, 1/3, 5} the KMS solution space in Mat_2 is the line of diag(1, q): the Gibbs
    (Fermi-Dirac) form diag(1, q)/(1 + q), the same form for every q.
(2) A pure, boost-invariant entangling state of the pair, c|00> + s|11> (cs != 0, Schmidt rank 2), is
    annihilated by the boost generator H_1 - H_2 (opposite weights on the two sides) and descends to
    diag(c^2, s^2), which is KMS at q = (s/c)^2: 9/16 (beta > 0) at (4/5, 3/5) and 16/9 (beta < 0) at
    (3/5, 4/5), so the hypotheses leave beta free, its sign included.
(3) Normalisation: kappa = f'(r_h)/2 = 1/(4M) for f = 1 - 2M/r (exact rational functions, three M); one
    rapidity period 2 pi is the Schwarzschild time 2 pi / kappa = 8 pi M (coefficient of pi: 8M), and
    T_H = kappa / (2 pi) = 1/(8 pi M) (coefficient of 1/pi: 1/(8M)); a mode of Schwarzschild frequency omega
    has rapidity frequency omega / kappa = 4 M omega, so beta = 2 pi gives the exponent 2 pi * 4 M omega
    = omega / T_H, and the reduced density matrix is diag(1, e^(-omega/T_H))/Z.
Not computed: positivity and the premises (P), (R) themselves, and the shape-operator reading of the boost
plane (S(sigma) = -2 sigma), which needs the curvature data of singularity.matching-steps-4b-4c-join-equation.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QS = [F(9, 16), F(16, 9), F(1, 3), F(5)]
MASSES = [F(1), F(1, 2), F(5, 3)]
H = [F(-1, 2), F(1, 2)]          # weights of N - 1/2 on |0>, |1>


def kms_space(q):
    """Kernel of the KMS conditions on rho = [[r00, r01], [r10, r11]] (unknowns in that order)."""
    def unit(i, j):
        return [[F(1) if (a, b) == (i, j) else F(0) for b in range(2)] for a in range(2)]

    def mm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

    def tr_coeffs(X):
        # Tr(rho X) = sum_ij rho_ij X_ji, coefficients on (r00, r01, r10, r11)
        return [X[0][0], X[1][0], X[0][1], X[1][1]]
    rows = []
    for i in range(2):
        for j in range(2):
            A = unit(i, j)
            alphaA = [[A[a][b] * q ** int(H[a] - H[b]) for b in range(2)] for a in range(2)]
            for k in range(2):
                for l in range(2):
                    B = unit(k, l)
                    lhs = tr_coeffs(mm(A, B))
                    rhs = tr_coeffs(mm(B, alphaA))
                    rows.append([x - y for x, y in zip(lhs, rhs)])
    return GA.field_kernel(rows)


def check_kms_states_are_gibbs_lines():
    premise("hawking.modular-structure-completed-pair")
    premise("singularity.modular-descent")
    premise("singularity.descended-form-state-independent")
    ok = True
    for q in QS:
        ker = kms_space(q)
        ok = ok and len(ker) == 1
        v = ker[0]
        ok = ok and v[1] == 0 and v[2] == 0 and v[0] != 0 and v[3] / v[0] == q
    GA.check("the KMS states of one mode at Boltzmann symbol q are the line diag(1, q)", ok)
    return ok


def check_descended_state_kms_at_free_beta():
    premise("singularity.modular-descent")
    premise("singularity.rate-rigidity-temperature-not-algebra-intrinsic")
    ok = True
    found = []
    for c, s in ((F(4, 5), F(3, 5)), (F(3, 5), F(4, 5))):
        # boost invariance: H_1 - H_2 (opposite weights on the two sides) annihilates c|00> + s|11>
        amps = {(0, 0): c, (1, 1): s}
        ok = ok and all((H[a] - H[b]) * x == 0 for (a, b), x in amps.items()) and c * s != 0
        ok = ok and (H[0] - H[1]) != 0                    # the odd components |01>, |10> would move
        red = [c * c, s * s]
        q = red[1] / red[0]
        ker = kms_space(q)
        ok = ok and len(ker) == 1 and ker[0][3] / ker[0][0] == red[1] / red[0]
        found.append(q)
    ok = ok and found == [F(9, 16), F(16, 9)] and (found[0] < 1) and (found[1] > 1)
    GA.check("descended marginals are KMS at q = (s/c)^2: 9/16 and 16/9, so beta is free in sign and size", ok)
    return ok


def check_geometric_normalisation():
    premise("singularity.computed")
    premise("singularity.euclidean-section-period")
    premise("singularity.r-regularity-fixed-locus")
    premise("singularity.rate-discharge-hypothesis-iii")
    ok = True
    for M in MASSES:
        fr = GA.RF([-2 * M, F(1)], [F(0), F(1)])
        kappa = fr.deriv().eval(2 * M) * F(1, 2)
        ok = ok and kappa == F(1) / (4 * M)
        period_pi = F(2) / kappa                              # Schwarzschild period / pi
        ok = ok and period_pi == 8 * M
        TH_inv_pi = kappa / 2                              # T_H * pi
        ok = ok and TH_inv_pi == F(1) / (8 * M)
        omega = F(3, 7)
        exponent_pi = 2 * (omega / kappa)                  # beta_rapidity * rapidity frequency / pi
        ok = ok and exponent_pi == omega / TH_inv_pi
    GA.check("kappa = 1/4M, period 8 pi M, T_H = 1/(8 pi M); beta = 2 pi in rapidity is omega/T_H per mode", ok)
    return ok
