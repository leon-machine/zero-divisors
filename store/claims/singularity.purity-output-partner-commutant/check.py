"""singularity.purity-output-partner-commutant: exact checks over Q(i).

The mode factor Mat_2, a faithful state rho = diag(lambda_0^2, lambda_1^2) (rational lambda_i > 0),
its GNS space C^2 (x) C^2 (|ij> at 2i + j), Omega = sum_i lambda_i |ii>, pi(a) = a (x) 1.
(1) Omega reproduces rho (<Omega, (a (x) 1) Omega> = tr(rho a) on all matrix units) and is cyclic and
separating (orbits of Mat_2 (x) 1 and of 1 (x) Mat_2 have rank 4).
(2) The commutant of pi(A) in Mat_4, computed as a kernel (16 complex unknowns, over Q(i)), is
4-dimensional and equals 1 (x) Mat_2; and J pi(a) J = 1 (x) conj(a) for the antilinear swap J
(the modular conjugation of the premise), on complex a.
(3) Purifications differ by a unitary on the purifying factor: for Psi = (1 (x) W) Omega with W a
rational rotation and a Q(i) unitary, the marginal is rho, and W is recovered from Psi alone as
W_ji = Psi_ij/lambda_i and is unitary; conversely a vector whose recovered matrix is not unitary
has a different marginal (control).
(4) Gibbs case: rho = diag(1, x)/(1 + x) with x = e^{-omega/T} gives Omega = cos|00> + sin|11> with
tan^2 theta = x (x = 9/16, 16/9, 25/144): the thermofield double of the Schmidt-forcing lemma.
"""
from fractions import Fraction as F

import GA
from GA import QI
from tp_premise import premise

LAMBDAS = [(F(3, 5), F(4, 5)), (F(12, 13), F(5, 13)), (F(8, 17), F(15, 17))]
W_ROT = [[QI(F(3, 5)), QI(F(-4, 5))], [QI(F(4, 5)), QI(F(3, 5))]]
W_CPX = [[QI(F(3, 5)), QI(0, F(4, 5))], [QI(0, F(4, 5)), QI(F(3, 5))]]
A_CPX = [[QI(1, 2), QI(-3, 1)], [QI(0, 5), QI(2, -7)]]


mm = GA.field_mat_mul


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    return [[A[i // 2][j // 2] * B[i % 2][j % 2] for j in range(4)] for i in range(4)]


def eye2():
    return [[QI(1), QI(0)], [QI(0), QI(1)]]


def unit(a, b):
    M = [[QI(0), QI(0)], [QI(0), QI(0)]]
    M[a][b] = QI(1)
    return M


def mv(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v))), QI(0)) for i in range(len(A))]


def omega(lam):
    return [QI(lam[0]), QI(0), QI(0), QI(lam[1])]


def marginal1(psi):
    """Partial trace over the second factor of |psi><psi|."""
    return [[sum((psi[2 * i + k] * psi[2 * j + k].conj() for k in range(2)), QI(0)) for j in range(2)]
            for i in range(2)]


def check_gns_vector_cyclic_separating():
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    for lam in LAMBDAS:
        assert lam[0] ** 2 + lam[1] ** 2 == 1
        Om = omega(lam)
        rho = [lam[0] ** 2, lam[1] ** 2]
        for a in range(2):
            for b in range(2):
                v = mv(kron(unit(a, b), eye2()), Om)
                val = sum((Om[i].conj() * v[i] for i in range(4)), QI(0))
                assert val == (QI(rho[a]) if a == b else QI(0))
        left = [mv(kron(unit(a, b), eye2()), Om) for a in range(2) for b in range(2)]
        right = [mv(kron(eye2(), unit(a, b)), Om) for a in range(2) for b in range(2)]
        assert GA.field_rank(left) == 4 and GA.field_rank(right) == 4


def check_commutant_is_partner_copy_and_J_conjugate():
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    # unknown C (4 x 4 complex): C (E_ab (x) 1) - (E_ab (x) 1) C = 0; real equations over Q(i)
    rows = []
    for a in range(2):
        for b in range(2):
            G = kron(unit(a, b), eye2())
            for i in range(4):
                for j in range(4):
                    r = [QI(0)] * 16
                    for k in range(4):
                        r[4 * i + k] = r[4 * i + k] + G[k][j]
                        r[4 * k + j] = r[4 * k + j] - G[i][k]
                    rows.append(r)
    ker = GA.field_kernel(rows)
    assert len(ker) == 4
    partner = [[x for row in kron(eye2(), unit(a, b)) for x in row] for a in range(2) for b in range(2)]
    assert GA.field_rank(ker + partner) == 4
    # J = antilinear swap: J (a (x) 1) J v = swap(conj((a (x) 1) conj(swap v))) = (1 (x) conj(a)) v
    swap = lambda v: [v[0], v[2], v[1], v[3]]
    conjv = lambda v: [x.conj() for x in v]
    for a in (A_CPX, unit(0, 1)):
        for v in ([QI(1, 1), QI(2), QI(0, -1), QI(3, 2)], [QI(0), QI(1), QI(5, 5), QI(-2)]):
            Jv = swap(conjv(v))
            lhs = swap(conjv(mv(kron(a, eye2()), Jv)))
            abar = [[x.conj() for x in r] for r in a]
            assert lhs == mv(kron(eye2(), abar), v)


def check_purifications_differ_by_partner_unitary():
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    for lam in LAMBDAS:
        Om = omega(lam)
        rho = marginal1(Om)
        assert rho == [[QI(lam[0] ** 2), QI(0)], [QI(0), QI(lam[1] ** 2)]]
        for W in (W_ROT, W_CPX):
            assert mm(W, dag(W)) == [[QI(1), QI(0)], [QI(0), QI(1)]]
            Psi = mv(kron(eye2(), W), Om)
            assert marginal1(Psi) == rho and Psi != Om
            Wrec = [[Psi[2 * i + j] / lam[i] for i in range(2)] for j in range(2)]
            assert Wrec == W
        # control: Psi = (3/5, 0, 0, 4/5)-type vector with the weights swapped is not of this form
        bad = [QI(lam[1]), QI(0), QI(0), QI(lam[0])]
        Wb = [[bad[2 * i + j] / lam[i] for i in range(2)] for j in range(2)]
        assert mm(Wb, dag(Wb)) != [[QI(1), QI(0)], [QI(0), QI(1)]] and marginal1(bad) != rho


def check_gibbs_gives_thermofield_double():
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    for x, (c, s) in ((F(9, 16), (F(4, 5), F(3, 5))), (F(16, 9), (F(3, 5), F(4, 5))),
                      (F(25, 144), (F(12, 13), F(5, 13)))):
        rho = [1 / (1 + x), x / (1 + x)]
        assert rho == [c * c, s * s] and c * c + s * s == 1
        assert (s / c) ** 2 == x
        Om = omega((c, s))
        assert marginal1(Om) == [[QI(rho[0]), QI(0)], [QI(0), QI(rho[1])]]
        assert Om[1] == 0 and Om[2] == 0 and c * s != 0
