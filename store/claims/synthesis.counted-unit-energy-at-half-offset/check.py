"""synthesis.counted-unit-energy-at-half-offset: exact checks.

Rigorous rational bounds (Fractions with outward rounding; no floating point), as in the
stored check of synthesis.half-integer-weight-array-carries-half-ln2: pi from Machin's formula,
e^{-pi} from the Taylor series of e^{pi} with an explicit remainder, ln(1 + u) and ln 2 from
bracketing series, tails from x e^{-x} bounds.

(i)   one array, weights kappa(k + 1/2), at y = 2 pi: beta E (measured from the sea) is within
      10^-55 of pi/12, while the zero offset gives beta E in (0.02351, 0.02352): offset-specific;
(ii)  the sea's zeta-regularised energy: the finite part of sum_{n>=0} (n + 1/2) e^{-eps(n + 1/2)}
      is 1/24 = -B_2(1/2)/2 (exact power series), so the sea carries -kappa/24 per array and the
      symmetric (modular) normalisation gives the array beta E = 0 and ln Z = (1/2) ln 2;
(iii) the counted unit (two arrays) against the hole: beta E = pi/6, E/(TS) = pi/(6 ln 2) in
      (0.75539, 0.75540), and under the area law E/M = pi/(12 ln 2) in (0.37769, 0.37770), so the
      Gibbs label is E0/M in (0.62230, 0.62231), inside (1/2, 1];
(iv)  the unit's heat capacity beta^2 Var(E) is in (1.5964, 1.5965), against 0 for a zero-weight
      mode: the two realisations of ln 2 differ at second order;
"""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise

DEN = 10 ** 70


def rd(x):
    return series.round_down(x, DEN)


def ru(x):
    return series.round_up(x, DEN)


def pi_bounds():
    a5 = series.arctan_inv_bracket(5, 61)
    a239 = series.arctan_inv_bracket(239, 31)
    return (rd(16 * a5[0] - 4 * a239[1]), ru(16 * a5[1] - 4 * a239[0]))


def exp_bounds(x, N):
    s, term = F(0), F(1)
    for n in range(N):
        s += term
        term = term * x / (n + 1)
    rem = term / (1 - x / (N + 1))
    return (rd(s), ru(s + rem))


def ln1p_bounds(u, N):
    s, p = F(0), F(1)
    for k in range(1, N + 1):
        p = p * u
        s += F((-1) ** (k + 1)) * p / k
    t = s + F((-1) ** (N + 2)) * p * u / (N + 1)
    return (rd(min(s, t)), ru(max(s, t)))


def ln2_bounds(N):
    s = sum(F(1, k * 2 ** k) for k in range(1, N + 1))
    return (rd(s), ru(s + F(1, (N + 1) * 2 ** N)))


_Q = []


def q_bounds():
    if not _Q:
        pl, pu = pi_bounds()
        el, eu = exp_bounds(pu, 120), exp_bounds(pl, 120)
        _Q.extend([pl, pu, rd(1 / el[1]), ru(1 / eu[0])])   # pi and e^{-pi}
    return tuple(_Q)


def array_sums(ns, K):
    """Bounds on beta E = 2 sum x n(x), S = 2 sum s(x), C = 2 sum x^2 n(1-n), x = ns(k) pi."""
    pl, pu, ql, qu = q_bounds()
    E, S, C = [F(0), F(0)], [F(0), F(0)], [F(0), F(0)]
    for k in range(K):
        n = ns(k)
        ul, uu = rd(ql ** n), ru(qu ** n)
        el, eu = rd(n * pl * ul / (1 + ul)), ru(n * pu * uu / (1 + uu))
        a, b = ln1p_bounds(ul, 40), ln1p_bounds(uu, 40)
        E[0] += 2 * el
        E[1] += 2 * eu
        S[0] += 2 * (a[0] + el)
        S[1] += 2 * (b[1] + eu)
        C[0] += 2 * rd((n * pl) ** 2 * ul / (1 + ul) ** 2)
        C[1] += 2 * ru((n * pu) ** 2 * uu / (1 + uu) ** 2)
    tail_e, tail_c, n0 = F(0), F(0), ns(K)
    for n in range(n0, n0 + 120, 2):
        tail_e += (1 + n * pu) * qu ** n
        tail_c += (n * pu) ** 2 * qu ** n
    pad = F(1, 10 ** 60)
    E[1] += 2 * (ru(tail_e) + pad)
    S[1] += 2 * (ru(tail_e) + pad)
    C[1] += 2 * (ru(tail_c) + pad)
    return [rd(E[0]), ru(E[1])], [rd(S[0]), ru(S[1])], [rd(C[0]), ru(C[1])]


_H = {}


def half():
    if "h" not in _H:
        _H["h"] = array_sums(lambda k: 2 * k + 1, 26)
    return _H["h"]


def check_array_thermal_energy():
    premise("synthesis.imported-theta-function-identities")
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    pl, pu = q_bounds()[:2]
    E, S, _ = half()
    ok = E[1] - E[0] < F(1, 10 ** 56)
    ok = ok and E[0] - pu / 12 > -F(1, 10 ** 55) and E[1] - pl / 12 < F(1, 10 ** 55)
    l2 = ln2_bounds(260)
    ok = ok and S[0] - l2[1] / 2 > -F(1, 10 ** 55) and S[1] - l2[0] / 2 < F(1, 10 ** 55)
    # control: the zero offset (no zero-mode energy) is not pi/12
    E0 = array_sums(lambda k: 2 * k + 2, 26)[0]
    ok = ok and E0[0] > F(2351, 10 ** 5) and E0[1] < F(2352, 10 ** 5)
    GA.check("(i) half offset at y = 2 pi: beta E per array within 10^-55 of pi/12 "
             "(zero offset: 0.02351...)", ok)
    return ok


def bernoulli(M):
    """B_0..B_M exactly, from sum_{k=0}^{m} C(m+1, k) B_k = 0."""
    B = [F(1)]
    for m in range(1, M + 1):
        B.append(-sum(series.pbinomial(m + 1, k) * B[k] for k in range(m)) / (m + 1))
    return B


def check_sea_energy_zeta():
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    premise("synthesis.hole-mass-is-ground-energy-label")
    N = 12
    # g(eps) = 2 sinh(eps/2)/eps as a power series; sum_n e^{-eps(n+1/2)} = 1/(2 sinh(eps/2))
    g = [F(0)] * N
    fact = 1
    for j in range(N):
        fact *= (j + 1)
        if j % 2 == 0:
            g[j] = F(1, fact * 2 ** j)
    h = series.ps_inv(g, N)             # 1/(2 sinh(eps/2)) = h(eps)/eps
    # every coefficient: eps h(eps) = sum_n B_{2n}(1/2) eps^{2n}/(2n)!, B_{2n}(1/2) = (2^{1-2n} - 1) B_{2n}
    B = bernoulli(N)
    ok = True
    fj = 1
    for j in range(N):
        if j > 0:
            fj *= j
        want = (F(2) ** (1 - j) - 1) * B[j] / fj if j % 2 == 0 else F(0)
        ok = ok and h[j] == want
    # -d/deps (h/eps) = h0/eps^2 - sum_{j>=2} (j - 1) h_j eps^{j-2}; finite part is -h_2
    finite = -h[2]
    ok = ok and h[0] == 1 and finite == F(1, 24)
    # Bernoulli polynomial: zeta(-1, a) = -B_2(a)/2 with B_2(a) = a^2 - a + 1/6
    a = F(1, 2)
    ok = ok and B[2] == F(1, 6) and -(a * a - a + B[2]) / 2 == finite
    # control: integer weights (a = 1, sum n) give -1/12, not 1/24
    a = F(1)
    ok = ok and -(a * a - a + B[2]) / 2 == F(-1, 12)
    # symmetric ordering: per array beta E_sym = beta E - 2 pi * (1/24); per unit ln Z = ln 2
    pl, pu = q_bounds()[:2]
    E, S, _ = half()
    esym = (E[0] - 2 * pu * finite, E[1] - 2 * pl * finite)
    ok = ok and abs(esym[0]) < F(1, 10 ** 55) and abs(esym[1]) < F(1, 10 ** 55)
    lnz = (S[0] - esym[1], S[1] - esym[0])
    l2 = ln2_bounds(260)
    ok = ok and 2 * lnz[0] - l2[1] > -F(1, 10 ** 54) and 2 * lnz[1] - l2[0] < F(1, 10 ** 54)
    GA.check("(ii) sea energy -kappa zeta(-1,1/2) = -kappa/24 per array (exact Laurent series "
             "against Bernoulli numbers); symmetric normalisation: beta E = 0, ln Z per unit = ln 2", ok)
    return ok


def check_counted_unit_against_mass():
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.quarter-from-temperature")
    premise("synthesis.hole-mass-is-ground-energy-label")
    pl, pu = q_bounds()[:2]
    l2 = ln2_bounds(260)
    E, _, _ = half()
    eu = (2 * E[0], 2 * E[1])                      # beta E per counted unit
    ok = eu[0] - pu / 6 > -F(1, 10 ** 54) and eu[1] - pl / 6 < F(1, 10 ** 54)
    r = (eu[0] / l2[1], eu[1] / l2[0])             # E/(TS), unit entropy ln 2
    ok = ok and r[0] > F(75539, 10 ** 5) and r[1] < F(75540, 10 ** 5) and r[1] < 1
    # area law along the family, sampled at M = 1, 3/2, 7 (exact rationals; pi, ln 2 bounded)
    for M in (F(1), F(3, 2), F(7)):
        # N = A/(4 ln 2) units, A = 16 pi M^2; E_unit = (beta E_unit) T with T = 1/(8 pi M)
        Nl, Nh = 16 * pl * M * M / (4 * l2[1]), 16 * pu * M * M / (4 * l2[0])
        e_unit = (eu[0] / (8 * pu * M), eu[1] / (8 * pl * M))
        Ec = (Nl * e_unit[0] / M, Nh * e_unit[1] / M)
        ok = ok and Ec[0] > F(37769, 10 ** 5) and Ec[1] < F(37770, 10 ** 5)
        E0 = (1 - Ec[1], 1 - Ec[0])
        ok = ok and E0[0] > F(62230, 10 ** 5) and E0[1] < F(62231, 10 ** 5)
        ok = ok and F(1, 2) < E0[0] and E0[1] <= 1
        # TS = M/2: the unit energy sits below TS
        ok = ok and Ec[1] < F(1, 2)
    GA.check("(iii) counted unit: beta E = pi/6, E/TS = pi/(6 ln 2) = 0.75539...; area law: "
             "E/M = 0.37769..., label E0/M = 0.62230...", ok)
    return ok


def check_heat_capacity_distinguishes():
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    _, _, C = half()
    cu = (2 * C[0], 2 * C[1])
    ok = cu[0] > F(15964, 10 ** 4) and cu[1] < F(15965, 10 ** 4)
    # zero-weight mode: x = 0, variance x^2 n (1 - n) = 0 exactly, and Z = 2, S = ln 2, E = 0
    x = F(0)
    ok = ok and x * x * F(1, 2) * F(1, 2) == 0
    GA.check("(iv) heat capacity of one counted unit 1.5964..., of one zero-weight mode 0", ok)
    return ok


def run():
    return all([check_array_thermal_energy(), check_sea_energy_zeta(),
                check_counted_unit_against_mass(), check_heat_capacity_distinguishes()])


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
