"""synthesis.cumulants-at-fixed-second-moments-keep-the-floor: exact checks (Fractions).

Six bosonic face modes p = (i, A), family i in {0,1,2}, slot A in {0,1};
Theta_k[(i,A),(j,B)] = (1/2) eps_{kij} eps_{AB}, as in the skeleton theorem and the unit-plus-Gram
proposition.  The number Gram is N_kl = <a^dag Theta_k Theta_l a>.
"""
from fractions import Fraction as F
from itertools import product
from tp_premise import premise
from GA import mul, gen, sig, mat_mul

MODES = [(i, A) for i in range(3) for A in range(2)]
CL3 = sig(3, 0)


def eps3(k, i, j):
    """Levi-Civita symbol from the Clifford product in Cl(3,0)."""
    if len({k, i, j}) < 3:
        return 0
    return int(mul(mul(gen(k), gen(i), CL3), gen(j), CL3).get((0, 1, 2), 0))


def eps2(A, B):
    return 0 if A == B else (1 if (A, B) == (0, 1) else -1)


THETA = [[[F(1, 2) * eps3(k, p[0], q[0]) * eps2(p[1], q[1]) for q in MODES] for p in MODES]
         for k in range(3)]


def check_number_gram_is_family_density():
    """Theta_k Theta_l = (1/4)(delta_kl 1 - (e_l e_k^T) x 1_slot) on the six modes, so
    2 N_kl = (1/2)(delta_kl n - rho_lk) with rho_kl = sum_A <a_kA^dag a_lA>; verified as a matrix
    identity and on exact Fock states (real rational superpositions of monomials)."""
    premise("synthesis.face-mass-form-unit-plus-gram")
    for k in range(3):
        for l in range(3):
            TT = mat_mul(THETA[k], THETA[l])
            for a, p in enumerate(MODES):
                for b, q in enumerate(MODES):
                    want = F(1, 4) * ((1 if (k == l and a == b) else 0)
                                      - (1 if (p[0] == l and q[0] == k and p[1] == q[1]) else 0))
                    assert TT[a][b] == want
    # Fock states: monomials m (occupations of the six modes), <m|m'> = delta prod m_p!
    def fact(n):
        out = 1
        for j in range(2, n + 1):
            out *= j
        return out

    def norm(m):
        out = 1
        for x in m:
            out *= fact(x)
        return out

    def ann(p, st):
        out = {}
        for m, c in st.items():
            if m[p]:
                mm = list(m)
                mm[p] -= 1
                mm = tuple(mm)
                out[mm] = out.get(mm, F(0)) + c * m[p]
        return {m: c for m, c in out.items() if c != 0}

    def ip(s, t):
        return sum((c * t[m] * norm(m) for m, c in s.items() if m in t), F(0))

    def lin(terms):
        out = {}
        for c, st in terms:
            for m, v in st.items():
                out[m] = out.get(m, F(0)) + c * v
        return {m: v for m, v in out.items() if v != 0}

    states = [
        {(1, 0, 0, 1, 0, 0): F(1), (0, 0, 2, 0, 0, 1): F(-2, 3), (0, 1, 0, 0, 1, 1): F(5, 4)},
        {(2, 1, 0, 0, 0, 0): F(1), (0, 0, 1, 1, 1, 0): F(3), (1, 0, 0, 0, 0, 2): F(-1, 2),
         (0, 0, 0, 0, 0, 0): F(2)},
        {(0, 3, 0, 0, 1, 0): F(1, 5), (1, 1, 1, 1, 0, 0): F(-1)},
        {(1, 0, 0, 0, 0, 0): F(1), (0, 0, 1, 0, 0, 0): F(2), (0, 0, 0, 0, 1, 1): F(-1),
         (0, 1, 0, 1, 0, 0): F(1, 3)},
    ]
    seen = []
    for psi in states:
        aps = [ann(p, psi) for p in range(6)]
        n = sum((ip(x, x) for x in aps), F(0))
        rho = [[sum((ip(aps[2 * k + A], aps[2 * l + A]) for A in range(2)), F(0)) for l in range(3)]
               for k in range(3)]
        assert sum(rho[k][k] for k in range(3)) == n
        seen.append((n / ip(psi, psi), rho[0][1] / ip(psi, psi)))
        Ta = [[lin([(THETA[k][p][q], aps[q]) for q in range(6) if THETA[k][p][q] != 0])
               for p in range(6)] for k in range(3)]
        for k in range(3):
            for l in range(3):
                N2 = 2 * sum((ip(Ta[k][p], Ta[l][p]) for p in range(6)), F(0))
                assert N2 == F(1, 2) * ((n if k == l else 0) - rho[l][k])
    # the states are pinned: normalised mean numbers and one off-diagonal density entry
    assert seen[0][0] == F(449, 48) / F(497, 144) and seen[1][0] == F(69, 31)
    assert seen[2][0] == 4 and seen[3] == (F(13, 11), F(18, 55))


def minors_nonneg(M):
    """A real symmetric 3 x 3 matrix is positive semidefinite iff all its principal minors are >= 0."""
    d1 = all(M[i][i] >= 0 for i in range(3))
    d2 = all(M[i][i] * M[j][j] - M[i][j] * M[j][i] >= 0 for i in range(3) for j in range(i + 1, 3))
    det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
           + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return d1 and d2 and det >= 0


def check_floor_at_fixed_second_moments():
    """Skeleton pieces: omega omega^dag = 4x(1 + x) P, 2N = x(1 + P), K_Gauss = 2x^2 P, summing with the
    unit to cosh^2 r 1 + x(5 + 6x) P; the number bound 1 + (n - rho_max)/2 equals the floor 1 + x.
    With the second moments held, H = (1 + x) 1 + (5x + 4x^2) P + K with K any Gram matrix, so
    H - (1 + x) 1 is positive semidefinite; then the physical ratios need lambda_tau >= (m_tau/m_e)^2 (1 + x*)."""
    premise("families.skeleton-rank-one-plus-ordering-shift")
    premise("synthesis.face-mass-form-unit-plus-gram")
    premise("families.koide-class-crossing-fit-conclusion")
    for x in (F(1, 3), F(2), F(7693325, 10000)):
        # coefficient of P: x(5 + 6x) = 4x(1 + x) [coherent] + 2x^2 [K] + x [2N]
        assert x * (5 + 6 * x) == 4 * x * (1 + x) + 2 * x * x + x
        # number bound: n = 4x, rho^T = 2x(1 - P) has eigenvalues 2x, 2x, 0
        n, rho_max = 4 * x, 2 * x
        assert 1 + (n - rho_max) / 2 == 1 + x
        # trace identity of the skeleton: tr H = 3 + n + sum_k |Omega_k psi|^2 with the latter 4x + 6x^2
        assert 2 * (1 + x) + (1 + 6 * x + 6 * x * x) == 3 + n + (4 * x + 6 * x * x)
    # H - (1 + x) 1 = (5x + 4x^2) P + K is PSD for rank-one rational P and Gram K = G^T G
    v = [F(1), F(2), F(2)]
    P = [[v[i] * v[j] / 9 for j in range(3)] for i in range(3)]
    Gs = [[[F(1), F(-2), F(0)], [F(3), F(1, 2), F(-1)], [F(0), F(0), F(0)]],
          [[F(2), F(1), F(-2)], [F(0), F(0), F(1, 3)], [F(5), F(-1), F(1)]]]
    x = F(7693325, 10000)
    for G in Gs:
        GT = [list(r) for r in zip(*G)]
        K = mat_mul(GT, G)
        H = [[(1 + x) * (1 if i == j else 0) + (5 * x + 4 * x * x) * P[i][j] + K[i][j] for j in range(3)]
             for i in range(3)]
        D = [[H[i][j] - (1 + x) * (1 if i == j else 0) for j in range(3)] for i in range(3)]
        assert minors_nonneg(D)
    # the numbers: masses in MeV (PDG 2024 as quoted in the store: m_tau = 1776.93 +- 0.09)
    me, mmu = F(51099895, 10 ** 8), F(1056583755, 10 ** 7)
    mtau_lo, mtau_hi = F(177684, 100), F(177702, 100)
    Rte_lo, Rte_hi = (mtau_lo / me) ** 2, (mtau_hi / me) ** 2
    Rme = (mmu / me) ** 2
    assert F(12090, 1000) * 10 ** 6 < Rte_lo < Rte_hi < F(12094, 1000) * 10 ** 6
    assert F(427530, 10) < Rme < F(427532, 10)
    xs_lo, xs_hi = F(7693324, 10000), F(7693326, 10000)               # x* = 769.3325
    need_tau = Rte_lo * (1 + xs_lo)                                     # lambda_tau lower bound
    gauss_tau = 1 + 6 * xs_hi + 6 * xs_hi * xs_hi
    assert need_tau > 9313 * 10 ** 6 and gauss_tau < 3556 * 10 ** 3
    # K_tautau must exceed need_tau - (1 + x) - (5x + 4x^2), about 7,860 times its Gaussian value 2x^2
    K_need = need_tau - (1 + 6 * xs_hi + 4 * xs_hi * xs_hi)
    assert K_need > 7860 * 2 * xs_hi * xs_hi
    # Weyl: lambda_2(K) >= lambda_mu - (1 + 6x + 4x^2) with lambda_mu >= (m_mu/m_e)^2 (1 + x*)
    lam2 = Rme * (1 + xs_lo) - (1 + 6 * xs_hi + 4 * xs_hi * xs_hi)
    assert lam2 > 305 * 10 ** 5


EXPORTS = {}
