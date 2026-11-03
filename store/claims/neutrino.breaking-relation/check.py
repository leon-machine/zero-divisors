"""neutrino.breaking-relation: exact checks (rational 3 x 3 matrices).

M_R = alpha Pi + M_3 J/3, Pi = 1 - J/3, and M_R^-1 = Pi/alpha + J/(3 M_3) is taken from
neutrino.invariant-symmetric-matrices (and confirmed here against Gaussian elimination).
m_D = d (J + delta A), q = (J + delta A) u'.

(1) The exact identity m_D M_R^-1 m_D^T = (d^2 delta^2/alpha) A Pi A^T + (d^2/(3 M_3)) q q^T, with
q = 3u' + delta A u', for three directions A (e_3 e_3^T and two general real matrices), three
(alpha, M_3, d) and four values of delta: both sides are quadratic in delta, so four values fix the
identity in delta. J X J = (sum of entries of X) J for four X, and so a Majorana breaking alone
(m_D = d J, any invertible symmetric M_R, S3-invariant or not) leaves the light matrix rank <= 1.
(2) The reference direction A = e_3 e_3^T: ||Pi A Pi|| = 2/3 (the largest eigenvalue of
Pi A Pi A^T Pi is 4/9 = (2/3)^2), lambda_A = 4/9, lambda'_A = 0, while A Pi A^T = (2/3) e_3 e_3^T has
eigenvalue 2/3, the factor 2/3 between them exactly; delta^2 lambda_A is invariant under
(A, delta) -> (cA, delta/c).
(3) Leading order for a generic direction: with c_1, c_2, c_3 the characteristic coefficients of the
light matrix L (trace, sum of principal 2-minors, determinant), the two light masses have sum
c_2/c_1 and product c_3/c_1 up to the heavy-state correction; against (d^2 delta^2/alpha) times the
trace and the 2-minor sum of the compression Pi A Pi A^T Pi, both ratios lie within 2 delta of 1 at
delta = 10^-2, 10^-3, 10^-4: the light masses are (d^2 delta^2/alpha) times the compression's
eigenvalues at leading order.
(4) The instances: at A = e_3 e_3^T, L has rank two (m_1 = 0), so r = m_2/m_3 solves
r/(1 + r)^2 = c_2/c_1^2, increasing in r on (0, 1); hence r in (0.168, 0.172) at delta = 0.286,
M_3/alpha = 66, against the leading-order delta^2 lambda_A M_3/(9 alpha) in (0.26, 0.275), more than
1.5 times the exact value; at delta = 0.006, M_3/alpha = 1284 the exact ratio is within 4 percent of
the formula and between 0.64 and 0.69 of the A Pi A^T one.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

AS = (
    [[F(0), F(0), F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(1)]],
    [[F(1), F(2), F(0)], [F(-1), F(3), F(1, 2)], [F(0), F(5), F(-2)]],
    [[F(2), F(-1), F(3)], [F(0), F(1, 3), F(1)], [F(4), F(0), F(-1)]],
)
PARAMS = ((F(2), F(5), F(3)), (F(1, 7), F(16), F(1, 2)), (F(10) ** 3, F(10) ** 6, F(100)))
DELTAS = (F(1, 10), F(3, 4), F(-2), F(6, 100))
XS = (
    [[F(1), F(2), F(-3)], [F(5), F(0), F(1, 2)], [F(-1), F(7), F(4)]],
    [[F(2), F(1), F(0)], [F(1), F(5), F(1)], [F(0), F(1), F(4)]],
    [[F(7), F(-2), F(1)], [F(-2), F(11), F(0)], [F(1), F(0), F(3)]],
    [[F(1), F(0), F(0)], [F(0), F(3), F(0)], [F(0), F(0), F(5)]],
)
GEN_A = AS[1]
E3 = AS[0]
U = [F(1), F(1), F(1)]
# leading-order check: one sample (alpha, M_3), three small deltas, and the tolerance on the O(delta)
# remainder (a check choice; the samples reach about 1.03 delta)
LEAD_ALPHA, LEAD_M3 = F(1), F(2)
LEAD_DELTAS = tuple(F(1, 10 ** k) for k in (2, 3, 4))
LEAD_TOL = 2
# the remark's instances (delta, M_3/alpha), at alpha = 1; the ratio m_2/m_3 does not depend on d
INSTANCE_1 = (F(286, 1000), F(66))
INSTANCE_3 = (F(6, 1000), F(1284))
INST_ALPHA, INST_D = F(1), F(1)


def ident():
    return [[F(int(i == j)) for j in range(3)] for i in range(3)]


def jmat():
    return [[F(1)] * 3 for _ in range(3)]


def lin(a, A, b, B):
    return [[a * A[i][j] + b * B[i][j] for j in range(3)] for i in range(3)]


def tr(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def mv(A, x):
    return [sum((A[i][k] * x[k] for k in range(3)), F(0)) for i in range(3)]


def mm(*Ms):
    out = Ms[0]
    for M in Ms[1:]:
        out = GA.mat_mul(out, M)
    return out


def pi():
    return lin(F(1), ident(), F(-1, 3), jmat())


def mr_inv(alpha, M3):
    return lin(1 / alpha, pi(), 1 / (3 * M3), jmat())


def light(alpha, M3, d, delta, A):
    D = lin(d, jmat(), d * delta, A)
    return mm(D, mr_inv(alpha, M3), tr(D))


def coeffs(L):
    c1 = L[0][0] + L[1][1] + L[2][2]
    c2 = sum(L[i][i] * L[j][j] - L[i][j] * L[j][i] for i in range(3) for j in range(i + 1, 3))
    c3 = (L[0][0] * (L[1][1] * L[2][2] - L[1][2] * L[2][1])
          - L[0][1] * (L[1][0] * L[2][2] - L[1][2] * L[2][0])
          + L[0][2] * (L[1][0] * L[2][1] - L[1][1] * L[2][0]))
    return c1, c2, c3


def compression(A):
    P = pi()
    return mm(P, A, P, tr(A), P)


def f_ratio(r):
    return r / ((1 + r) * (1 + r))


def ratio_rounds_to(L, m, e, scale=1):
    """L has rank two and r = m_2/m_3, the root in (0, 1) of r/(1 + r)^2 = c_2/c_1^2, satisfies
    r/scale rounds to m x 10^e (f_ratio is increasing on (0, 1))."""
    u = F(10) ** e
    return ratio_bracket_ok(L, scale * (m * u - u / 2), scale * (m * u + u / 2))


def check_exact_identity_and_majorana_only_breaking():
    premise("neutrino.invariant-symmetric-matrices")
    ok = True
    J = jmat()
    for alpha, M3, d in PARAMS:
        MR = lin(alpha, pi(), M3 / 3, J)
        cols = [GA.field_solve(MR, [F(int(i == c)) for i in range(3)]) for c in range(3)]
        ok = ok and [[cols[c][r] for c in range(3)] for r in range(3)] == mr_inv(alpha, M3)
        for A in AS:
            for delta in DELTAS:
                lhs = light(alpha, M3, d, delta, A)
                q = mv(lin(F(1), J, delta, A), U)
                ok = ok and q == [3 + delta * x for x in mv(A, U)]
                APA = mm(A, pi(), tr(A))
                rhs = [[d * d * delta * delta / alpha * APA[i][j] + d * d / (3 * M3) * q[i] * q[j]
                        for j in range(3)] for i in range(3)]
                ok = ok and lhs == rhs
    for X in XS:
        s = sum(sum(r) for r in X)
        ok = ok and mm(J, X, J) == lin(s, J, F(0), J)
        Xinv = [[c for c in row] for row in X]
        cols = [GA.field_solve(Xinv, [F(int(i == c)) for i in range(3)]) for c in range(3)]
        inv = [[cols[c][r] for c in range(3)] for r in range(3)]
        Lmaj = mm(lin(F(3), J, F(0), J), inv, lin(F(3), J, F(0), J))
        ok = ok and GA.mat_rank(Lmaj) <= 1
    GA.check("m_D M_R^-1 m_D^T = (d^2 delta^2/alpha) A Pi A^T + (d^2/3M_3) q q^T; Majorana-only breaking is rank one", ok)
    return ok


def check_reference_direction_scale():
    ok = True
    C = compression(E3)
    c1, c2, c3 = coeffs(C)
    # eigenvalues of C: 4/9, 0, 0 (rank one, trace 4/9)
    ok = ok and c1 == F(4, 9) and c2 == 0 and c3 == 0 and GA.mat_rank(C) == 1
    PAP = mm(pi(), E3, pi())
    ok = ok and mm(PAP, tr(PAP)) == C
    APA = mm(E3, pi(), tr(E3))
    ok = ok and APA == lin(F(2, 3), E3, F(0), E3)
    ok = ok and APA[2][2] * F(2, 3) == c1 and mv(APA, U) != [F(0)] * 3
    for c in (F(2), F(-3), F(1, 5)):
        cC = coeffs(compression(lin(c, E3, F(0), E3)))[0]
        delta = F(3, 10)
        ok = ok and (delta / c) ** 2 * cC == delta ** 2 * c1
    GA.check("A = e_3 e_3^T: ||Pi A Pi|| = 2/3, lambda_A = 4/9, lambda'_A = 0, A Pi A^T eigenvalue 2/3", ok)
    return ok


def check_leading_order_compression_eigenvalues():
    premise("neutrino.invariant-symmetric-matrices")
    ok = True
    alpha, M3 = LEAD_ALPHA, LEAD_M3
    # by hand: B = Pi A Pi has zero row and column sums; 18 B = [[17, -25, 8], [-16, -4, 20],
    # [-1, 29, -28]] for GEN_A and 27 B = [[-11, -32, 43], [-41, 28, 13], [52, 4, -56]] for AS[2].
    # tr(B B^T) = |B|^2 = 3276/324 = 91/9 and 11484/729 = 1276/81; every 2 x 2 minor of 18 B is
    # +-468 and of 27 B is +-1620, so by Cauchy-Binet e_2 = 9 x 468^2/18^4 = 169/9 and 9 x 1620^2/27^4
    # = 400/9; det = 0 (rank two)
    for A, t_hand, e2_hand in ((GEN_A, F(91, 9), F(169, 9)), (AS[2], F(1276, 81), F(400, 9))):
        C = compression(A)
        t, e2, e3 = coeffs(C)
        ok = ok and (t, e2, e3) == (t_hand, e2_hand, 0)
        for delta in LEAD_DELTAS:
            c1, c2, c3 = coeffs(light(alpha, M3, F(1), delta, A))
            r_sum = (c2 / c1) / (delta * delta / alpha * t)
            r_prod = (c3 / c1) / ((delta * delta / alpha) ** 2 * e2)
            ok = ok and abs(r_sum - 1) < LEAD_TOL * delta and abs(r_prod - 1) < LEAD_TOL * delta
    GA.check("light masses = (d^2 delta^2/alpha) x eigenvalues of Pi A Pi A^T Pi at leading order", ok)
    return ok


def ratio_bracket_ok(L, lo, hi):
    c1, c2, c3 = coeffs(L)
    return c3 == 0 and f_ratio(lo) < c2 / (c1 * c1) < f_ratio(hi)


def check_instances_diagonalised_exactly():
    premise("neutrino.invariant-symmetric-matrices")
    ok = True
    lam = F(4, 9)
    d1, R1 = INSTANCE_1
    L1 = light(INST_ALPHA, R1, INST_D, d1, E3)
    # by hand (decimal root of r/(1 + r)^2 = c_2/c_1^2): r = 0.1695723, in the quoted (0.168, 0.172)
    ok = ok and ratio_rounds_to(L1, 1695723, -7)
    lead1 = d1 * d1 * lam / 9 * R1
    # by hand: 0.286^2 x (4/9) x 66/9 = 0.081796 x 264/81 = 21.594144/81 = 0.26659, the quoted 0.267
    ok = ok and lead1 == F(21594144, 81 * 10 ** 6)
    # the formula exceeds the exact ratio by more than a half: r/lead = 0.63606845, a factor 1.5722
    ok = ok and ratio_rounds_to(L1, 63606845, -8, lead1)
    d3, R3 = INSTANCE_3
    L3 = light(INST_ALPHA, R3, INST_D, d3, E3)
    lead3 = d3 * d3 * lam / 9 * R3
    # within 4 percent of the formula: r/lead = 0.995055
    ok = ok and ratio_rounds_to(L3, 995055, -6, lead3)
    wrong3 = d3 * d3 * F(2, 3) / 9 * R3
    # between 0.64 and 0.69 of the A Pi A^T one: r/wrong = 0.663370
    ok = ok and ratio_rounds_to(L3, 663370, -6, wrong3)
    GA.check("m_2/m_3 in (0.168, 0.172) at delta = 0.286, 66 (formula 0.267); within 4% at 0.006, 1284", ok)
    return ok
