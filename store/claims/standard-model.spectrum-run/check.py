"""standard-model.spectrum-run: exact checks.

One-loop running a_i(M_Z) = a_U + b_i t, t = L/2pi, with the matching alpha_em^-1 = (5/3) a_1 + a_2 and
alpha_s^-1 = a_3 (Fact imported-one-loop-running-trace-ratio (a)); sin^2 theta_W = a_2 / alpha_em^-1.
(1) The four linear equations in (a_1, a_2, a_U, t) are solved exactly (GA.field_solve) and agree with the closed
    form t = (alpha_em^-1 - (8/3) alpha_s^-1)/((5/3)(b1 - b3) + (b2 - b3)), a_2 = a_3 + (b2 - b3) t, at several
    input sets. At alpha_em^-1 = 128, alpha_s^-1 = 500/59: SM coefficients give t = 18656/3953 and
    sin^2 = 78761/379488; supersymmetric ones give t = 4664/885 and 6539/28320; both t > 0 and t_SUSY > t_SM.
(2) Without the Higgs doublet (its one-loop indices (1/3)(3/5 * 2 * 1/4, 1/2, 0) = (1/10, 1/6, 0) removed),
    sin^2 = 3457/16992. A complete generation adds the same amount (4/3) to each b_i (its index sums are 2, 2, 2,
    from sum Y^2 = 10/3 and the doublet and triplet counts), so sin^2 is the same for 0..5 generations.
(3) With all three couplings from the record (a_2 = 0.2312 * 128), the pairwise meetings t_ij = (a_i - a_j)/(b_i - b_j)
    are pairwise distinct for the SM coefficients.
(4) Scales, by rigorous rational bounds (pi from Machin's series with alternating remainders, exp from its Taylor
    series with remainder and repeated squaring, outward rounding): M_U = M_Z exp(2 pi t), M_Z = 91.1876 GeV. SM:
    M_U in (6.5, 7.5) x 10^14; SUSY: (1.5, 2.5) x 10^16 (it is 2.19 x 10^16, the stated 2 x 10^16 to one figure); the SUSY pairwise meetings at the record lie in
    (1.95, 2.05), (2.15, 2.25), (2.25, 2.35) x 10^16, the largest over the smallest below 1.2. The alpha_s spread
    (0.1180 +- 0.0009) moves the SM prediction by a half-width in (0.00026, 0.00028), and the miss
    0.2312 - 78761/379488 is between 85 and 95 half-widths ("about ninety").
EXPORTS: pi_bounds, exp_bounds, gev_bounds, record, solve_one_loop, MZ for the splits check.
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

B_SM = (F(41, 10), F(-19, 6), F(-7))
B_SUSY = (F(33, 5), F(1), F(-3))
AEM, AS = F(128), F(500, 59)
S2_REC = F(2312, 10000)
MZ = F(911876, 10000)
INPUTS = [(F(128), F(500, 59)), (F(127), F(9)), (F(130), F(25, 3))]
B_TESTS = [B_SM, B_SUSY, (F(1), F(2), F(-5))]


def solve_one_loop(b, aem=AEM, a3=AS):
    """Unknowns (a1, a2, aU, t): (5/3) a1 + a2 = aem; a1 - aU - b1 t = 0; a2 - aU - b2 t = 0; aU + b3 t = a3."""
    M = [[F(5, 3), F(1), F(0), F(0)], [F(1), F(0), F(-1), -b[0]], [F(0), F(1), F(-1), -b[1]], [F(0), F(0), F(1), b[2]]]
    a1, a2, aU, t = GA.field_solve(M, [aem, F(0), F(0), a3])
    return a2 / aem, t


def record(s2=S2_REC, aem=AEM, a3=AS):
    a2 = s2 * aem
    return (F(3, 5) * (aem - a2), a2, a3)


pi_bounds = series.pi_bounds          # Machin, n alternating atan terms
exp_bounds = series.exp_bounds        # halving and squaring, outward rounding to 2^-80


def gev_bounds(t, pib=None):
    """Bounds on M_Z exp(2 pi t) for t >= 0."""
    plo, phi = pib or pi_bounds()
    return MZ * exp_bounds(2 * plo * t)[0], MZ * exp_bounds(2 * phi * t)[1]


def check_closed_form_and_values():
    premise("standard-model.imported-one-loop-running-trace-ratio")
    premise("standard-model.weak-angle-over-derived-generation")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for aem, a3 in INPUTS:
        for b in B_TESTS:
            s2, t = solve_one_loop(b, aem, a3)
            tc = (aem - F(8, 3) * a3) / (F(5, 3) * (b[0] - b[2]) + (b[1] - b[2]))
            ok = ok and t == tc and s2 == (a3 + (b[1] - b[2]) * tc) / aem
    s_sm, t_sm = solve_one_loop(B_SM)
    s_su, t_su = solve_one_loop(B_SUSY)
    ok = ok and (s_sm, t_sm) == (F(78761, 379488), F(18656, 3953))
    ok = ok and (s_su, t_su) == (F(6539, 28320), F(4664, 885))
    ok = ok and t_sm > 0 and t_su > t_sm and s_sm < S2_REC and abs(s_su - S2_REC) < F(1, 1000)
    GA.check("SM: t = 18656/3953, sin^2 = 78761/379488; SUSY: t = 4664/885, sin^2 = 6539/28320", ok)
    return ok


def check_higgs_and_generations():
    premise("standard-model.imported-one-loop-running-trace-ratio")
    premise("standard-model.weak-angle-over-derived-generation")
    higgs = (F(1, 3) * F(3, 5) * 2 * F(1, 4), F(1, 3) * F(1, 2), F(0))
    nohiggs = tuple(b - h for b, h in zip(B_SM, higgs))
    ok = higgs == (F(1, 10), F(1, 6), F(0)) and solve_one_loop(nohiggs)[0] == F(3457, 16992)
    # one generation's index sums: T1 = 3/5 sum Y^2 = 3/5 * 10/3; T2 = 1/2 per doublet state-colour; T3 = 1/2 per triplet
    gen = [(2, 3, F(1, 6)), (2, 1, F(-1, 2)), (1, 3, F(-2, 3)), (1, 3, F(1, 3)), (1, 1, F(1)), (1, 1, F(0))]
    T1 = F(3, 5) * sum(d2 * d3 * y * y for d2, d3, y in gen)
    T2 = sum(F(1, 2) * d3 for d2, d3, y in gen if d2 == 2)
    T3 = sum(F(1, 2) * d2 for d2, d3, y in gen if d3 == 3)
    ok = ok and (T1, T2, T3) == (2, 2, 2)
    shift = F(2, 3) * T1
    base = tuple(b - 3 * shift for b in B_SM)
    vals = {solve_one_loop(tuple(x + ng * shift for x in base))[0] for ng in range(6)}
    ok = ok and shift == F(4, 3) and vals == {F(78761, 379488)}
    GA.check("no Higgs: sin^2 = 3457/16992; complete generations are inert (each adds 4/3 to every b_i)", ok)
    return ok


def check_no_common_meeting():
    premise("standard-model.imported-one-loop-running-trace-ratio")
    a = record()
    t = {(i, j): (a[i] - a[j]) / (B_SM[i] - B_SM[j]) for i in range(3) for j in range(i + 1, 3)}
    ok = len(set(t.values())) == 3 and all(v > 0 for v in t.values())
    GA.check("SM pairwise meetings at the record are three distinct scales", ok)
    return ok


def check_scales_and_spread():
    premise("standard-model.imported-one-loop-running-trace-ratio")
    pib = pi_bounds()
    ok = F(314159265, 10 ** 8) < pib[0] < pib[1] < F(314159266, 10 ** 8)
    lo, hi = gev_bounds(solve_one_loop(B_SM)[1], pib)
    ok = ok and F(65, 10) * 10 ** 14 < lo and hi < F(75, 10) * 10 ** 14
    lo, hi = gev_bounds(solve_one_loop(B_SUSY)[1], pib)
    ok = ok and F(15, 10) * 10 ** 16 < lo and hi < F(25, 10) * 10 ** 16
    a = record()
    pairs = [(0, 1), (0, 2), (1, 2)]
    windows = [(F(195, 100), F(205, 100)), (F(215, 100), F(225, 100)), (F(225, 100), F(235, 100))]
    meet = sorted(gev_bounds((a[i] - a[j]) / (B_SUSY[i] - B_SUSY[j]), pib) for i, j in pairs)
    for (lo, hi), (wl, wh) in zip(meet, windows):
        ok = ok and wl * 10 ** 16 < lo and hi < wh * 10 ** 16
    ok = ok and meet[-1][1] / meet[0][0] < F(12, 10)
    s_hi = solve_one_loop(B_SM, AEM, 1 / F(1171, 10000))[0]
    s_lo = solve_one_loop(B_SM, AEM, 1 / F(1189, 10000))[0]
    half = abs(s_hi - s_lo) / 2
    miss = S2_REC - solve_one_loop(B_SM)[0]
    ok = ok and F(26, 100000) < half < F(28, 100000) and 85 < miss / half < 95
    GA.check("M_U ~ 7e14 (SM), 2.0e16 (SUSY); SUSY meetings 2.0, 2.2, 2.3 e16; miss ~ 90 alpha_s half-widths", ok)
    return ok


EXPORTS = {"pi_bounds": pi_bounds, "exp_bounds": exp_bounds, "gev_bounds": gev_bounds, "record": record,
           "solve_one_loop": solve_one_loop, "MZ": MZ}
