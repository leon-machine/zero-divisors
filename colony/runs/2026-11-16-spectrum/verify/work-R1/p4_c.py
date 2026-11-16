"""synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta: exact checks.

Physical units at the descent: kappa = k/a_d, X = H_d/kappa = a_d H_d/k, rho the total energy density,
M_H = 4 pi rho/(3 H_d^3) the Hubble mass, x_p the density of quanta at momentum p (0 <= x_p <= g), w_p >= |p| the
one-particle energy, w_max its largest value on the support of x, rho_F = int w x = f rho, and
s = 3 kappa^3 int (w + kappa)^2 x /(2 pi^2 rho^2) the stored shot term for the contrast of the total density.
(1) X_E = (E - E_0)^2 + E(1 - E) <= 1 for projectors E_0 and 0 <= E <= 1 (rational samples, signature computed by
    congruence); hence x_p <= g.  Discrete Pauli count and the energy inequality
    sum (w + kappa)^2 x <= (w_max + kappa)(2 sum w x + kappa g #{|p| < kappa}) on families of rational profiles,
    the extreme ones included; the longitudinal momentum form obeys the same mode-by-mode bound (3/4)(w + kappa)^2 as the
    energy form, being (3/4) p_L^2 + kappa^2/4 with |p_L| <= w.
(2) The ceiling in Hubble masses: (3 kappa^3/(2 pi^2 rho)) (w_max + kappa)(2f + eta) =
    (2 (2f + eta)/pi) X^(-3) (w_max + kappa)/M_H identically (pi carried as a rational symbol), and
    eta = g kappa^4/(6 pi^2 rho) = 4 g G H^2/(9 pi X^4) with H^2 = 8 pi G rho/3.
(3) Thresholds for an amplitude A under the three conversions: (C0) R = delta/4, (C1) R = delta/4 + 2 X u,
    (CA) R = (3/2) X^2 delta, with sd(u) <= (3/4) sqrt(s) in the radiation era.  Solving D^2 = A for the least
    (w_max + kappa)/M_H gives 8 pi A X^3/(2f + eta), 8 pi A X^3/((2f + eta)(1 + 6X)^2), 2 pi A/(9 (2f + eta) X);
    the three are verified by substitution.  Numbers at k = a_0 H_0 with the stored X > 4.96e7 (1 MeV) and
    X > 7.27e22 (1e12 GeV), A = 2.0e-9, f <= 1, eta < 1e-20, 333/106 < pi < 22/7:
    (C0) above 3.0e15 and 9.6e60 Hubble masses; (C1) above 0.034 and 5.0e13 Hubble masses, which with
    (M_H/M)^2 = 1440 (M/T_d)^4/g (M the reduced Planck mass 2.435e18 GeV, g = 10.75 and 106.75) is above 2.3e42
    and 1.1e27 reduced Planck masses; (CA) at the pivot, X > 3.2e20 at 1e12 GeV, A <= 2.2e-9, f = 1: below
    2.5e-30 Hubble masses, while T_d/M_H > 1e-20 there, so thermal quanta meet it with nine orders to spare.
    White contrast reaching 16 A at X has contrast 16 A X^3 at the Hubble scale: above 3.9e15 at 1 MeV.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI_LO, PI_HI = F(333, 106), F(22, 7)
A_LO, A_HI = F(20, 10) / 10 ** 9, F(22, 10) / 10 ** 9
X_1MEV, X_TOP, XPIV_TOP = F(496, 100) * 10 ** 7, F(727, 100) * 10 ** 22, F(32, 10) * 10 ** 20
MRED = F(2435, 1000) * 10 ** 18          # reduced Planck mass, GeV
ETA_MAX = F(1, 10 ** 20)


def _mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]


def _msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def _madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def _eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def _nonneg(M):
    """Positive semidefinite, by the exact signature of the symmetric rational matrix."""
    sig = GA.congruence_signature(GA.frac_matrix(M))
    return sig[1] == 0


def check_pauli_count_and_energy_inequality():
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    ok = True
    # X_E <= 1 and X_E >= 0 on rational samples: E symmetric with 0 <= E <= 1, E_0 a rational projector
    c, s = F(3, 5), F(4, 5)
    rot = [[c, -s, F(0)], [s, c, F(0)], [F(0), F(0), F(1)]]
    rot_t = [[rot[j][i] for j in range(3)] for i in range(3)]
    proj = _mm(_mm(rot, [[F(1), F(0), F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(1)]]), rot_t)
    ok = ok and _mm(proj, proj) == proj
    c2, s2 = F(5, 13), F(12, 13)
    rot2 = [[F(1), F(0), F(0)], [F(0), c2, -s2], [F(0), s2, c2]]
    rot2_t = [[rot2[j][i] for j in range(3)] for i in range(3)]
    for occ in ((F(1, 2), F(1, 3), F(9, 10)), (F(0), F(1), F(1, 7)), (F(1), F(1), F(1)), (F(2, 3), F(2, 3), F(0))):
        E = _mm(_mm(rot2, [[occ[0], F(0), F(0)], [F(0), occ[1], F(0)], [F(0), F(0), occ[2]]]), rot2_t)
        ok = ok and _nonneg(E) and _nonneg(_msub(_eye(3), E))
        for E0 in (proj, _msub(_eye(3), proj), _eye(3), [[F(0)] * 3 for _ in range(3)]):
            D = _msub(E, E0)
            XE = _madd(_mm(D, D), _mm(E, _msub(_eye(3), E)))
            ok = ok and _nonneg(XE) and _nonneg(_msub(_eye(3), XE))
            ok = ok and sum(XE[i][i] for i in range(3)) == \
                sum(_mm(E, _msub(_eye(3), E0))[i][i] + _mm(_msub(_eye(3), E), E0)[i][i] for i in range(3))
    # the bound fails without positivity of 1 - E: an "occupation" 3/2 gives X_E = 3/2 > 1 over the empty reference
    ok = ok and not _nonneg(_msub(_eye(1), [[F(3, 2) ** 2 + F(3, 2) * (1 - F(3, 2))]]))
    # discrete momenta p = (i, j, l) on a cubic grid, massless or massive energies bounded below by |p|:
    # w^2 = p^2 + m^2 is carried through its square; use energies w_p = |p|_1 >= |p| (rational, and >= |p|_2)
    g = 4
    grid = [(i, j, l) for i in range(-3, 4) for j in range(-3, 4) for l in range(-3, 4)]

    def energy(p, m):
        return F(abs(p[0]) + abs(p[1]) + abs(p[2])) + m

    profiles = {
        "soft": lambda p: F(g) if p[0] ** 2 + p[1] ** 2 + p[2] ** 2 <= 2 else F(0),
        "shell": lambda p: F(1, 2) if p[0] ** 2 + p[1] ** 2 + p[2] ** 2 == 9 else F(0),
        "broad": lambda p: F(g, 1 + p[0] ** 2 + p[1] ** 2 + p[2] ** 2),
        "one": lambda p: F(1, 3) if p == (3, 3, 3) else F(0),
        "full": lambda p: F(g),
    }
    for name, prof in profiles.items():
        for m in (F(0), F(1, 2), F(5)):
            for kap in (F(1, 3), F(1), F(5, 2), F(7)):
                xs = [(p, prof(p)) for p in grid if prof(p) != 0]
                ok = ok and all(0 <= x <= g for _, x in xs)
                wmax = max(energy(p, m) for p, _ in xs)
                lhs = sum(((energy(p, m) + kap) ** 2 * x for p, x in xs), F(0))
                rho_f = sum((energy(p, m) * x for p, x in xs), F(0))
                nbar = sum((x for _, x in xs), F(0))
                soft_modes = sum(1 for p in grid if p[0] ** 2 + p[1] ** 2 + p[2] ** 2 < kap ** 2)
                n_soft = sum((x for p, x in xs if energy(p, m) < kap), F(0))
                # Pauli: the quanta with energy below kappa sit in the momentum ball |p| < kappa
                ok = ok and n_soft <= g * soft_modes
                ok = ok and kap * nbar <= kap * g * soft_modes + rho_f
                ok = ok and lhs <= (wmax + kap) * (1 * rho_f + kap * g * soft_modes)
                # energy and longitudinal momentum (first axis) forms, mode by mode, both below (3/4)(w + kappa)^2:
                # (1/2)[(w_(p+k)^2 + w_(p-k)^2)/4 + w_p^2] with w_(p +- k) <= w_p + kappa, and
                # (1/2)[((p_L + kappa)^2 + (p_L - kappa)^2)/4 + p_L^2]
                for p, _ in xs:
                    w = energy(p, m)
                    top = F(3, 4) * (w + kap) ** 2
                    ok = ok and F(1, 2) * (2 * (w + kap) ** 2 / 4 + w ** 2) <= top
                    ok = ok and F(1, 2) * (((p[0] + kap) ** 2 + (p[0] - kap) ** 2) / 4 + F(p[0] ** 2)) <= top
                    ok = ok and F(1, 2) * (((p[0] + kap) ** 2 + (p[0] - kap) ** 2) / 4 + F(p[0] ** 2)) \
                        == F(3, 4) * p[0] ** 2 + kap ** 2 / 4
    # the factor 2 is needed: quanta all at energy w_max = kappa give lhs = 4 kappa^2 nbar = 2 (w_max + kappa) rho_F
    lhs = (F(3) + F(3)) ** 2 * F(1, 3)
    ok = ok and lhs == (F(3) + F(3)) * 2 * (F(3) * F(1, 3)) and lhs > (F(3) + F(3)) * 1 * (F(3) * F(1, 3))
    assert ok


def check_ceiling_of_the_shot_term_in_hubble_masses():
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    ok = True
    for pi in (PI_LO, PI_HI, F(3)):
        for rho, H, X, wmax, f, g in ((F(7), F(2), F(5), F(11), F(1), 4), (F(1, 3), F(9, 4), F(10 ** 6), F(10 ** 9), F(1, 50), 2),
                                      (F(1000), F(1, 7), F(3, 2), F(1, 100), F(1, 2), 16)):
            kap = H / X
            MH = 4 * pi * rho / (3 * H ** 3)
            G = 3 * H ** 2 / (8 * pi * rho)
            eta = g * kap ** 4 / (6 * pi ** 2 * rho)
            ok = ok and eta == 4 * g * G * H ** 2 / (9 * pi * X ** 4)
            ok = ok and MH == 1 / (2 * G * H)
            lhs = 3 * kap ** 3 / (2 * pi ** 2 * rho ** 2) * (wmax + kap) * (2 * f * rho + g * kap ** 4 / (6 * pi ** 2))
            rhs = 2 * (2 * f + eta) / (pi * X ** 3) * (wmax + kap) / MH
            ok = ok and lhs == rhs
    assert ok


def check_thresholds_under_the_three_conversions():
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    ok = True
    # the thresholds solve D^2 = A at the ceiling of the shot term (pi a rational symbol)
    for pi in (PI_LO, PI_HI):
        for A, X, f, eta in ((F(1, 10 ** 9), F(10 ** 4), F(1), F(0)), (F(3, 10 ** 8), F(77), F(1, 9), F(1, 1000))):
            pref = 2 * (2 * f + eta) / (pi * X ** 3)          # s = pref * m, m = (w_max + kappa)/M_H
            m0 = 8 * pi * A * X ** 3 / (2 * f + eta)
            m1 = 8 * pi * A * X ** 3 / ((2 * f + eta) * (1 + 6 * X) ** 2)
            mA = 2 * pi * A / (9 * (2 * f + eta) * X)
            ok = ok and pref * m0 / 16 == A                    # (C0): D^2 = s/16
            ok = ok and pref * m1 * (1 + 6 * X) ** 2 / 16 == A  # (C1): D = sqrt(s)(1/4 + 2 X 3/4)
            ok = ok and F(9, 4) * X ** 4 * pref * mA == A       # (CA): D^2 = (9/4) X^4 s
            ok = ok and F(1, 4) + 2 * X * F(3, 4) == (1 + 6 * X) / 4
    # numbers, f <= 1 so 2f + eta <= 2 + ETA_MAX; lower bounds use pi > 333/106 and A >= 2.0e-9
    den = 2 + ETA_MAX
    c0_lo = lambda X: 8 * PI_LO * A_LO * X ** 3 / den
    c1_lo = lambda X: 8 * PI_LO * A_LO * X ** 3 / (den * (1 + 6 * X) ** 2)
    ok = ok and c0_lo(X_1MEV) > F(30, 10) * 10 ** 15 and c0_lo(X_TOP) > F(96, 10) * 10 ** 60
    ok = ok and c1_lo(X_1MEV) > F(34, 1000) and c1_lo(X_TOP) > F(50, 10) * 10 ** 13
    ok = ok and c0_lo(X_1MEV) < F(31, 10) * 10 ** 15 and c1_lo(X_1MEV) < F(35, 1000)   # the brackets are tight
    # (C1) threshold is increasing in X on a grid between the two ends
    xs = [X_1MEV * 10 ** j for j in range(0, 16)]
    ok = ok and all(c1_lo(xs[j + 1]) > c1_lo(xs[j]) for j in range(len(xs) - 1))
    # Hubble mass in reduced Planck masses: (M_H/M)^2 = 1440 (M/T_d)^4 / g
    mh2_1mev = 1440 * (MRED / F(1, 1000)) ** 4 / F(1075, 100)
    mh2_top = 1440 * (MRED / 10 ** 12) ** 4 / F(10675, 100)
    ok = ok and c1_lo(X_1MEV) ** 2 * mh2_1mev > (F(23, 10) * 10 ** 42) ** 2
    ok = ok and c1_lo(X_TOP) ** 2 * mh2_top > (F(11, 10) * 10 ** 27) ** 2
    ok = ok and mh2_top > (2 * 10 ** 13) ** 2 and mh2_1mev > (6 * 10 ** 43) ** 2
    # (CA) at the pivot, top of the window, f = 1: requirement below 2.5e-30 Hubble masses; T_d/M_H above 1e-20
    ca_hi = 2 * PI_HI * A_HI / (9 * 2 * XPIV_TOP)
    ok = ok and ca_hi < F(25, 10) / 10 ** 30
    t_over_mh_sq = (10 ** 12 / MRED) ** 2 / mh2_top
    ok = ok and t_over_mh_sq > (F(1) / 10 ** 20) ** 2 and t_over_mh_sq > (10 ** 9 * ca_hi) ** 2
    # white contrast reaching 16 A at X is 16 A X^3 at the Hubble scale
    ok = ok and 16 * A_LO * X_1MEV ** 3 > F(39, 10) * 10 ** 15
    assert ok
