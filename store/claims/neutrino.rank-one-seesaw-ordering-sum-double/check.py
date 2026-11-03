"""neutrino.rank-one-seesaw-ordering-sum-double: exact checks of clauses (0) to (3) and the
numbers stated inside Premise (H).

Masses in eV. Square roots are bracketed exactly: isqrt is integer Newton iteration, and
sqrt(x) for rational x is bracketed to 1e-14; bounds on sums of roots use those brackets.
Splittings: dm21 in (7.3, 7.7)e-5 eV^2, dm31 in (2.45, 2.55)e-3 eV^2; sin^2 th12 in (0.295, 0.319),
sin^2 th13 in (0.0216, 0.0227).

(0) In the basis (u', (1,-1,0), (1,1,-2)) of both sectors (P6 = diag(P, P)), the 6 x 6 matrix
[[0, d J], [d J, alpha 1 + beta J]] becomes the democratic block [[0, 3d], [3d, M_3]] on
(nu_u', N_u'), the two N_perp with Majorana mass alpha and no Dirac entry, and two massless light
states, for samples including alpha = 0. For alpha != 0, J M_R^-1 J = (3/M_3) J and the light matrix
is (3 d^2/M_3) J, rank one with eigenvalue (3d)^2/M_3 = m_D^2/M_3 on u'. A rank-one m_D gives a
rank-one light matrix for invertible M_R, S3-invariant or not.
(1) Inverted ordering needs m_1/m_2 >= sqrt(1 - dm21/dm31) > 0.98. A rank-one J plus small symmetric
corrections (epsilon = 1/100, four directions) has, by inertia of L - t 1 at t = 1 and t = 2, one
eigenvalue above 2 and two below 1: one heavy, two light, never a degenerate heaviest pair.
(2) The floor sqrt(dm21) + sqrt(dm31) is in (0.0580, 0.0593); the sum is in (0.0591, 0.0604) at
m_1 = 1 meV, above 0.0616 at 3 meV and 0.0736 at 10 meV; at m_1 = 0.1 meV it exceeds the floor by
(0.1005, 0.1010) meV (Premise (H)'s 0.1007); at m_1 = 8.7 meV (order m_2) it exceeds 0.07 eV;
m_2/m_3 is in (0.16, 0.18).
(3) At m_1 = 0, |c13^2 s12^2 m_2 +- s13^2 m_3| is in (3.5, 3.9) meV (phase 0) and (1.3, 1.7) meV
(phase pi), so the hull is (1.3, 3.9) meV; at m_1 = 0.1 meV the m_1 term is below 0.08 meV and each
value moves by less than 0.1 meV; every value is below 10 meV, the lower edge of the
next-generation band, and below the current 28 meV.
"""
from fractions import Fraction as F

import GA
from series import rounds_to
from tp_premise import premise

SAMPLES = ((F(0), F(1), F(3)), (F(2), F(1), F(3)), (F(-1), F(5, 3), F(1, 2)),
           (F(10) ** 6, F(10) ** 5, F(100)))
GENERIC_MR = ([[F(1), F(0), F(0)], [F(0), F(3), F(0)], [F(0), F(0), F(5)]],
              [[F(2), F(1), F(0)], [F(1), F(5), F(1)], [F(0), F(1), F(4)]],
              [[F(7), F(-2), F(1)], [F(-2), F(11), F(0)], [F(1), F(0), F(3)]])
RANK_ONE_MD = [[F(1), F(2), F(-1)], [F(2), F(4), F(-2)], [F(3), F(6), F(-3)]]
CORRECTIONS = ([[F(1), F(0), F(2)], [F(0), F(-1), F(1)], [F(2), F(1), F(3)]],
               [[F(5), F(-3), F(0)], [F(-3), F(2), F(4)], [F(0), F(4), F(-6)]],
               [[F(0), F(1), F(1)], [F(1), F(0), F(1)], [F(1), F(1), F(0)]],
               [[F(-7), F(2), F(3)], [F(2), F(8), F(-1)], [F(3), F(-1), F(1)]])
DM21 = (F(73, 10 ** 6), F(77, 10 ** 6))
DM31 = (F(245, 10 ** 5), F(255, 10 ** 5))
S12 = (F(295, 1000), F(319, 1000))
S13 = (F(216, 10 ** 4), F(227, 10 ** 4))
DIGITS = 10 ** 14
# literature sensitivities (eV): the lower edge of the next-generation band and the current limit
NEXT_GEN_EDGE = F(10, 1000)
CURRENT_LIMIT = F(28, 1000)


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


def ident(n=3):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def jmat():
    return [[F(1)] * 3 for _ in range(3)]


def lin(a, A, b, B):
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A))] for i in range(len(A))]


def inverse(M):
    n = len(M)
    cols = [GA.field_solve([r[:] for r in M], [F(int(i == c)) for i in range(n)]) for c in range(n)]
    return [[cols[c][r] for c in range(n)] for r in range(n)]


def tr(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def check_democratic_block_decomposition():
    premise("neutrino.imported-indifference-faces-democratic-alignment-rank")
    premise("neutrino.invariant-symmetric-matrices")
    premise("neutrino.seesaw-what-gauge-invariance-proves-what")
    premise("neutrino.m-framework-realises-majorana-term-scale")
    ok = True
    P = [[F(1), F(1), F(1)], [F(1), F(-1), F(1)], [F(1), F(0), F(-2)]]      # columns u', e2, e3
    Z = [[F(0)] * 3 for _ in range(3)]
    P6 = [P[i] + Z[i] for i in range(3)] + [Z[i] + P[i] for i in range(3)]
    P6inv = inverse(P6)
    J = jmat()
    for al, be, d in SAMPLES:
        M3 = al + 3 * be
        MR = lin(al, ident(), be, J)
        big = [Z[i] + [d * x for x in J[i]] for i in range(3)] + [[d * x for x in J[i]] + MR[i] for i in range(3)]
        red = GA.mat_mul(GA.mat_mul(P6inv, big), P6)
        want = [[F(0)] * 6 for _ in range(6)]
        want[0][3] = want[3][0] = 3 * d
        want[3][3], want[4][4], want[5][5] = M3, al, al
        ok = ok and red == want
        if al != 0:
            MRinv = inverse(MR)
            ok = ok and GA.mat_mul(GA.mat_mul(J, MRinv), J) == lin(3 / M3, J, F(0), J)
            light = GA.mat_mul(GA.mat_mul(lin(d, J, F(0), J), MRinv), lin(d, J, F(0), J))
            ok = ok and light == lin(3 * d * d / M3, J, F(0), J) and GA.mat_rank(light) == 1
            ok = ok and GA.mat_mul(light, [[F(1)]] * 3) == [[(3 * d) ** 2 / M3]] * 3
    ok = ok and GA.mat_rank(RANK_ONE_MD) == 1
    for MR in GENERIC_MR:
        lt = GA.mat_mul(GA.mat_mul(RANK_ONE_MD, inverse(MR)), tr(RANK_ONE_MD))
        ok = ok and GA.mat_rank(lt) == 1
    GA.check("democratic block [[0, 3d], [3d, M_3]] splits off; light matrix (3d^2/M_3) J, rank one", ok)
    return ok


def check_normal_ordering():
    ok = 1 - DM21[1] / DM31[0] > F(98, 100) ** 2
    J = jmat()
    eps = F(1, 100)
    for E in CORRECTIONS:
        L = lin(F(1), J, eps, E)
        above_1 = GA.congruence_signature(lin(F(1), L, F(-1), ident()))
        above_2 = GA.congruence_signature(lin(F(1), L, F(-2), ident()))
        ok = ok and above_1[0] == 1 and above_1[1] == 2 and above_2[0] == 1
    GA.check("inverted ordering needs m_1/m_2 > 0.98; rank one plus small corrections gives one heavy, two light", ok)
    return ok


def sum_bracket(m1):
    lo = m1 + sqrt_lo(m1 * m1 + DM21[0]) + sqrt_lo(m1 * m1 + DM31[0])
    hi = m1 + sqrt_hi(m1 * m1 + DM21[1]) + sqrt_hi(m1 * m1 + DM31[1])
    return lo, hi


def check_sum_and_floor():
    premise("neutrino.h-second-stage-hierarchical")
    floor = sum_bracket(F(0))
    ok = F(580, 10 ** 4) < floor[0] and floor[1] < F(593, 10 ** 4)
    s1 = sum_bracket(F(1, 1000))
    ok = ok and F(591, 10 ** 4) < s1[0] and s1[1] < F(604, 10 ** 4)
    ok = ok and sum_bracket(F(3, 1000))[0] > F(616, 10 ** 4)
    ok = ok and sum_bracket(F(10, 1000))[0] > F(736, 10 ** 4)
    s01 = sum_bracket(F(1, 10 ** 4))
    ok = ok and F(1005, 10 ** 7) < s01[0] - floor[0] < F(1010, 10 ** 7)
    ok = ok and F(1005, 10 ** 7) < s01[1] - floor[1] < F(1010, 10 ** 7)
    ok = ok and sum_bracket(F(87, 10 ** 4))[0] > F(7, 100)
    ok = ok and F(16, 100) < sqrt_lo(DM21[0] / DM31[1]) and sqrt_hi(DM21[1] / DM31[0]) < F(18, 100)
    GA.check("floor (0.0580, 0.0593) eV; sum 0.0591-0.0604 at 1 meV; residue 0.1007 meV at 0.1 meV", ok)
    return ok


def mbb_terms(m1):
    m2 = (sqrt_lo(m1 * m1 + DM21[0]), sqrt_hi(m1 * m1 + DM21[1]))
    m3 = (sqrt_lo(m1 * m1 + DM31[0]), sqrt_hi(m1 * m1 + DM31[1]))
    c13 = (1 - S13[1], 1 - S13[0])
    c12 = (1 - S12[1], 1 - S12[0])
    t1 = (c12[0] * c13[0] * m1, c12[1] * c13[1] * m1)
    t2 = (c13[0] * S12[0] * m2[0], c13[1] * S12[1] * m2[1])
    t3 = (S13[0] * m3[0], S13[1] * m3[1])
    return t1, t2, t3


def check_double_beta_values():
    premise("neutrino.h-second-stage-hierarchical")
    premise("neutrino.m-framework-realises-majorana-term-scale")
    t1, t2, t3 = mbb_terms(F(0))
    plus = (t2[0] + t3[0], t2[1] + t3[1])
    minus = (t2[0] - t3[1], t2[1] - t3[0])
    ok = t1 == (0, 0)
    # by hand (decimal evaluation at the range ends, eV): phase 0 gives (3.532412, 3.885044) meV, in the
    # quoted (3.5, 3.9); phase pi gives (1.316972, 1.669605) meV, in the quoted (1.3, 1.7)
    ok = ok and rounds_to(plus[0], 3532412, -9) and rounds_to(plus[1], 38850444, -10)
    ok = ok and rounds_to(minus[0], 1316972, -9) and rounds_to(minus[1], 1669605, -9)
    u1, u2, u3 = mbb_terms(F(1, 10 ** 4))
    # m_1 = 0.1 meV: the m_1 term is c12^2 c13^2 m_1 = (0.681 x 0.9773, 0.705 x 0.9784) x 1e-4 eV, below
    # the quoted 0.08 meV, and each value moves by 0.06672502 to 0.06915728 meV, below the quoted 0.1 meV
    ok = ok and u1 == (F(6655413, 10 ** 11), F(689772, 10 ** 10))
    ok = ok and rounds_to(u1[1] + (u2[1] - t2[1]) + (u3[1] - t3[1]), 6915728, -11)
    ok = ok and rounds_to(u1[0] + (u2[0] - t2[0]) + (u3[0] - t3[0]), 6672502, -11)
    ok = ok and plus[1] < NEXT_GEN_EDGE and plus[1] < CURRENT_LIMIT
    GA.check("m_bb in (3.5, 3.9) or (1.3, 1.7) meV at m_1 = 0; moves < 0.1 meV at m_1 = 0.1 meV", ok)
    return ok
