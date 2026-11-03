"""neutrino.leptogenesis-suppressed-alignment-reheating-premise-new: exact checks.

Complex matrices are over the Gaussian rationals (GA.QI). A basis is written as the rows of E, and
T = E (Y_D^dag Y_D) E^T is the representation of Y_D^dag Y_D in it (unnormalised rows; vanishing of
entries and the normalisation-invariant ratios do not depend on the normalisation).
Premise (R) is a premise (no computable content); the arithmetic around it is checked.

(1) Alignment: for M_R = alpha 1 + beta J with beta != 0 the M_3-eigenspace is exactly the line of
u' (kernel of dimension 1) and the alpha-eigenspace is u'^perp (dimension 2), so every heavy
eigenbasis contains u'. For Y_D = y J (y complex), Y_D^dag Y_D = 3|y|^2 J, and in every eigenbasis
(u', e_2, e_3) with e_2 = (a, b, -a-b), e_3 = u' x e_2 (five choices) T has all six off-diagonal
entries zero and only T_11 != 0; so every Im[(T_ij)^2], i != j, vanishes and each epsilon_i = 0;
Y_D e_2 = Y_D e_3 = 0 (the pair has no Dirac coupling).
(2) Washout and the pair: K = m_3/m_* is in (43, 48), containing 45, for m_3 = sqrt(dm31) with
dm31 in (2.45, 2.55)e-3 eV^2 and m_* in (1.06, 1.15) meV. With Y_D = J + delta A (two complex
symmetric A), |T_23|^2/(T_22 T_33) is the same at delta = 1e-1, 1e-2, 1e-3 and equals the closed form
|<A e_2, A e_3>|^2/(|A e_2|^2 |A e_3|^2), nonzero (O(1) in delta), while |T_12|^2/T_11^2 divided by
delta^2 stays in a fixed bracket (O(delta^2)).
(3) Phases: with real breaking (Y_D = J + delta A, A real, three A, two delta), T is real and every
Im[(T_1j)^2] vanishes; with a phase, delta e^{i theta}, e^{i theta} = (3+4i)/5, (5+12i)/13,
(8+15i)/17, the interference term Im[(T_13)^2] is nonzero, and it is zero at theta = 0, pi.
Consistency under (R) and (U): M_3 = m_t^2/m_3 is in (5.8, 6.2)e14 GeV and m_b^2/m_3 in
(3.3, 3.7)e11 GeV (m_t in (172.28, 172.86), m_b in (4.13, 4.23) GeV), and the unification scales of
the Standard-Model paper's branches (7e14, 2e16, 3.36e16 GeV) all lie above M_3 at both ends.
"""
from fractions import Fraction as F

import GA
from series import rounds_to
from GA import QI
from tp_premise import premise

YS = (QI(2, 3), QI(-1, 1), QI(5), QI(0, F(1, 7)))
E2S = ((1, -1), (0, 1), (2, 5), (-3, 1), (1, 1))
ALBE = ((F(2), F(1)), (F(-1), F(5, 3)), (F(7, 2), F(-1)))
A_RES = ([[QI(0), QI(1), QI(0)], [QI(1), QI(0), QI(0, 1)], [QI(0), QI(0, 1), QI(1)]],
         [[QI(1), QI(0), QI(2, 2)], [QI(0), QI(3), QI(1)], [QI(2, 2), QI(1), QI(-1)]])
A_REAL = ([[0, 0, 0], [0, 0, 0], [0, 0, 1]], [[1, 2, 0], [-1, 3, 1], [0, 5, -2]],
          [[2, 0, 1], [0, -1, 0], [1, 0, 4]])
PHASES = ((QI(F(3, 5), F(4, 5))), QI(F(5, 13), F(12, 13)), QI(F(8, 17), F(15, 17)))
DM31 = (F(245, 10 ** 5), F(255, 10 ** 5))
MSTAR = (F(106, 10 ** 5), F(115, 10 ** 5))
MT = (F(17228, 100), F(17286, 100))
MB = (F(413, 100), F(423, 100))
MU_BRANCHES = (7 * 10 ** 14, 2 * 10 ** 16, F(336, 100) * 10 ** 16)
DIGITS = 10 ** 14
# the choice e_2 = (1, -1, 0) of the heavy eigenbasis used by the pair and phase checks
E2_CHOICE = (1, -1)
# sample breaking sizes: the resonant pair at three deltas, real breaking at two, the phase case at one
RES_DELTAS = (F(1, 10), F(1, 100), F(1, 1000))
REAL_DELTAS = (F(1, 10), F(-2, 7))
PHASE_DELTA = F(1, 10)
# the direction A = e_3 e_3^T for the phase case
PHASE_A = A_REAL[0]
# tolerance on the O(delta) correction to |T_12|^2/T_11^2 = (leading) delta^2 (1 + O(delta)), a check
# choice: the samples reach about 3.6 delta
R12_TOL = 5


def isqrt(n):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def sqrt_lo(x):
    x = F(x)
    return F(isqrt(x.numerator * x.denominator * DIGITS * DIGITS), x.denominator * DIGITS)


def sqrt_hi(x):
    return sqrt_lo(x) + F(1, F(x).denominator * DIGITS)


def qmat(rows):
    return [[x if isinstance(x, QI) else QI(x) for x in row] for row in rows]


# the democratic matrix J (the unbroken Dirac texture), over the Gaussian rationals
J_DEM = qmat([[1, 1, 1]] * 3)

def qmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def qdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def qtr(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def basis(a, b):
    e2 = [F(a), F(b), F(-a - b)]
    u = [F(1)] * 3
    e3 = [u[1] * e2[2] - u[2] * e2[1], u[2] * e2[0] - u[0] * e2[2], u[0] * e2[1] - u[1] * e2[0]]
    return qmat([u, e2, e3])


def rep(Y, E):
    return qmul(qmul(E, qmul(qdag(Y), Y)), qtr(E))


def abs2(z):
    return (z * z.conj()).re


def check_alignment_kills_decay_asymmetries():
    premise("neutrino.imported-indifference-faces-democratic-alignment-rank")
    premise("neutrino.invariant-symmetric-matrices")
    ok = True
    for al, be in ALBE:
        MR = [[al * int(i == j) + be for j in range(3)] for i in range(3)]
        k3 = GA.field_kernel([[MR[i][j] - (al + 3 * be) * int(i == j) for j in range(3)] for i in range(3)])
        ka = GA.field_kernel([[MR[i][j] - al * int(i == j) for j in range(3)] for i in range(3)])
        ok = ok and len(k3) == 1 and k3[0][0] == k3[0][1] == k3[0][2] != 0
        ok = ok and len(ka) == 2 and all(sum(v) == 0 for v in ka)
    for y in YS:
        Y = [[y] * 3 for _ in range(3)]
        YdY = qmul(qdag(Y), Y)
        ok = ok and all(YdY[i][j] == 3 * abs2(y) for i in range(3) for j in range(3))
        for a, b in E2S:
            E = basis(a, b)
            ok = ok and all(sum((E[i][k] * E[j][k] for k in range(3)), QI(0)) == 0
                            for i in range(3) for j in range(3) if i != j)
            T = rep(Y, E)
            off = [T[i][j] for i in range(3) for j in range(3) if i != j]
            ok = ok and len(off) == 6 and all(z == 0 for z in off)
            ok = ok and T[1][1] == 0 and T[2][2] == 0 and T[0][0] == 27 * abs2(y)
            ok = ok and all((T[i][j] * T[i][j]).im == 0 for i in range(3) for j in range(3) if i != j)
            YE = qmul(Y, qtr(E))
            ok = ok and all(YE[i][j] == 0 for i in range(3) for j in (1, 2))
    GA.check("Y_D = y J: in every heavy eigenbasis Y_D^dag Y_D has no off-diagonal entry; N_perp uncoupled", ok)
    return ok


def check_washout_strength_and_resonant_pair():
    premise("neutrino.rank-one-seesaw-ordering-sum-double")
    m3 = (sqrt_lo(DM31[0]), sqrt_hi(DM31[1]))
    K = (m3[0] / MSTAR[1], m3[1] / MSTAR[0])
    # by hand: sqrt(2.45e-3)/1.15e-3 = 43.04128 and sqrt(2.55e-3)/1.06e-3 = 47.639174, so K is in the
    # quoted (43, 48) and contains 45
    ok = rounds_to(K[0], 4304128, -5) and rounds_to(K[1], 476391742, -7) and K[0] < 45 < K[1]
    E = basis(*E2_CHOICE)
    J = J_DEM
    closed_vals = []
    # by hand, with u' = (1, 1, 1): T_11 = |3 u'|^2 = 27 and T_12 = 3 delta <u', A e_2> + O(delta^2), so
    # |T_12|^2/T_11^2 = delta^2 |<u', A e_2>|^2/81 (1 + O(delta)); <u', A e_2> = -i and -1 + 2i for the
    # two samples, giving 1/81 and 5/81
    for A, lead12 in zip(A_RES, (F(1, 81), F(5, 81))):
        e2 = [QI(x) for x in (1, -1, 0)]
        e3 = [QI(x) for x in (1, 1, -2)]
        Ae2 = [sum((A[i][k] * e2[k] for k in range(3)), QI(0)) for i in range(3)]
        Ae3 = [sum((A[i][k] * e3[k] for k in range(3)), QI(0)) for i in range(3)]
        inner = sum((Ae2[i].conj() * Ae3[i] for i in range(3)), QI(0))
        closed = abs2(inner) / (sum(abs2(z) for z in Ae2) * sum(abs2(z) for z in Ae3))
        r23s = []
        for delta in RES_DELTAS:
            Y = [[J[i][j] + QI(delta) * A[i][j] for j in range(3)] for i in range(3)]
            T = rep(Y, E)
            r23s.append(abs2(T[1][2]) / (T[1][1].re * T[2][2].re))
            r12 = abs2(T[0][1]) / (T[0][0].re ** 2) / (delta * delta)
            ok = ok and abs(r12 / lead12 - 1) < R12_TOL * delta
        ok = ok and r23s == [closed] * len(RES_DELTAS)
        closed_vals.append(closed)
    # by hand: A e_2 = (-1, 1, -i), A e_3 = (1, 1 - 2i, -2 + i): |<,>|^2 = |-1 - 4i|^2 = 17 over 3 x 11;
    # A e_2 = (1, -3, 1 + 2i), A e_3 = (-3 - 4i, 1, 5 + 2i): |3 - 12i|^2 = 153 over 15 x 55 = 51/275.
    # Both nonzero and distinct
    ok = ok and closed_vals == [F(17, 33), F(51, 275)]
    GA.check("K in (43, 48); the pair's |T23|^2/(T22 T33) is delta-independent, |T12|^2/T11^2 ~ delta^2", ok)
    return ok


def check_real_breaking_kills_interference():
    premise("neutrino.real-breaking-assumption")
    ok = True
    E = basis(*E2_CHOICE)
    J = J_DEM
    for A in A_REAL:
        Aq = qmat(A)
        for delta in REAL_DELTAS:
            Y = [[J[i][j] + QI(delta) * Aq[i][j] for j in range(3)] for i in range(3)]
            T = rep(Y, E)
            # T real, so every Im[(T_1j)^2] vanishes
            ok = ok and all(T[i][j].im == 0 for i in range(3) for j in range(3))
    Ae3 = qmat(PHASE_A)
    # e^{i theta} at theta = 0, pi and at the three Pythagorean phases, all of modulus one
    cases = ((QI(1), False), (QI(-1), False)) + tuple((p, True) for p in PHASES)
    ok = ok and all(abs2(ph) == 1 for ph, _ in cases)
    for ph, nonzero in cases:
        dq = QI(PHASE_DELTA) * ph
        Y = [[J[i][j] + dq * Ae3[i][j] for j in range(3)] for i in range(3)]
        T = rep(Y, E)
        ok = ok and (((T[0][2] * T[0][2]).im != 0) == nonzero)
    GA.check("real breaking: Im[(T_1j)^2] = 0; a phase (3+4i)/5, (5+12i)/13, (8+15i)/17 makes it nonzero", ok)
    return ok


def check_unification_above_heavy_scale():
    premise("dark-matter.hyp-u-equal-rank-one-eigenvalues")
    premise("neutrino.imported-ceiling-under-hypothesis-u-arrow")
    GeV = 10 ** 9
    m3 = (sqrt_lo(DM31[0]) / GeV, sqrt_hi(DM31[1]) / GeV)
    top = (MT[0] ** 2 / m3[1], MT[1] ** 2 / m3[0])
    bot = (MB[0] ** 2 / m3[1], MB[1] ** 2 / m3[0])
    ok = F(58, 10) * 10 ** 14 < top[0] and top[1] < F(62, 10) * 10 ** 14
    ok = ok and F(33, 10) * 10 ** 11 < bot[0] and bot[1] < F(37, 10) * 10 ** 11
    ok = ok and all(MU > top[1] and MU > bot[1] for MU in MU_BRANCHES)
    ok = ok and F(1159, 1000) < MU_BRANCHES[0] / top[1] and MU_BRANCHES[0] / top[0] < F(1192, 1000)
    GA.check("M_3 in (5.8, 6.2)e14 or (3.3, 3.7)e11 GeV under (U); every branch's M_U lies above it", ok)
    return ok
