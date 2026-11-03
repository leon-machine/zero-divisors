"""synthesis.adiabatic-deposit-modulation-is-a-time-shift: exact checks.

Separate-universe reading of a classical modulation of the descent's deposit. Local data on a slice of uniform
time at the deposit: the visible bath's temperature T_d, the deposited charge density n_Q (common to the towers
and the same in the mirror, by the charge reading), and the mirror's deposit per unit charge epsilon (energy
epsilon T_d per unit charge, thermalised in the mirror). Modulation vector v = (d ln T_d, d ln n_Q, d ln eps).
Conserved curvature perturbations (sectors decoupled after the deposit):
  zeta_gamma = d ln T_d,  zeta_Q = (1/3) d ln n_Q,  zeta_m = (1/4) d ln rho_m with rho_m = eps T_d n_Q.
Entropy perturbations against the photons: S_Q = 3(zeta_Q - zeta_gamma), S_m = 3(zeta_m - zeta_gamma).
(1) The map v -> (S_Q, S_m) has rank 2 and kernel spanned by (1, 3, 0): the time shift.
(2) Consistency with the stored deposit law xi^4 = (4/3) Y_B eps: d ln xi^4 = (4/3) S_m, d ln Y_B = S_Q.
(3) Single-parameter modulations: T_d at fixed n_Q gives S_Q = -3 zeta, S_m = -(9/4) zeta; eps alone gives
    zeta_gamma = zeta_Q = 0 and S_m = (3/4) d ln eps; n_Q alone gives zeta_gamma = 0, S_Q = d ln n_Q.
(4) Large-scale estimate for (3a): matter carrying the deposited charge is at least baryons plus the mirror's
    baryons, f_Q >= 2 Omega_b/Omega_m; the Sachs-Wolfe combination zeta + 2 S_eff with S_eff = f_Q S_Q has a
    non-adiabatic part 6 f_Q zeta >= 1.88 zeta, so the non-adiabatic share of the large-scale temperature
    variance is at least 0.27 in magnitude for either sign convention, against Planck's 0.013.
(5) Mirror radiation share at the deposit (g' = g): xi^4/(1 + xi^4) < 0.0388 under the N_eff cap xi < 0.448.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

THIRD, QUARTER = F(1, 3), F(1, 4)
OMB_H2, OMC_H2 = F("0.02237"), F("0.1200")      # Planck 2018 TT,TE,EE+lowE+lensing (cited, see proof)
PLANCK_NONAD = F("0.013")                        # CDM non-adiabatic share of the temperature variance, 95% CL


def zetas(v):
    dT, dn, de = v
    zg = dT
    zq = THIRD * dn
    zm = QUARTER * (de + dn + dT)
    return zg, zq, zm


def entropies(v):
    zg, zq, zm = zetas(v)
    return 3 * (zq - zg), 3 * (zm - zg)


def matrix():
    cols = [entropies(e) for e in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
    return [[F(cols[j][i]) for j in range(3)] for i in range(2)]


def check_entropy_map_and_kernel():
    premise("synthesis.mirror-temperature-measures-deposit-under-r")
    premise("dark-matter.stored-asymmetry-charge-not-number")
    M = matrix()
    GA.check("S_Q row is (-3, 1, 0)", M[0] == [F(-3), F(1), F(0)])
    GA.check("S_m row is (-9/4, 3/4, 3/4)", M[1] == [F(-9, 4), F(3, 4), F(3, 4)])
    GA.check("rank 2", GA.mat_rank(M) == 2)
    ker = GA.field_kernel(M)
    GA.check("kernel is one-dimensional", len(ker) == 1)
    k = ker[0]
    scale = k[0]
    GA.check("kernel spanned by (1, 3, 0)", scale != 0 and [x / scale for x in k] == [F(1), F(3), F(0)])
    GA.check("time shift is adiabatic", entropies((F(1), F(3), F(0))) == (0, 0))
    # along the time shift every zeta is equal: zeta_gamma = zeta_Q = zeta_m = d ln T_d
    GA.check("time shift: all zetas equal", len(set(zetas((F(1), F(3), F(0))))) == 1)
    # control: any other direction in a small grid is non-adiabatic
    bad = 0
    for a in range(-2, 3):
        for b in range(-6, 7):
            for c in range(-2, 3):
                if entropies((F(a), F(b), F(c))) == (0, 0):
                    GA.check("adiabatic grid point lies on the time shift", (b, c) == (3 * a, 0))
                else:
                    bad += 1
    GA.check("grid count of non-adiabatic directions pinned", bad == 320)
    return True


def check_deposit_law_consistency():
    premise("synthesis.mirror-temperature-measures-deposit-under-r")
    # xi^4 = rho_m/rho_gamma (equal g) ~ eps T n_Q / T^4 = eps n_Q T^-3; Y_B ~ n_Q/T^3
    vals = []
    for v in [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1)), (F(2), F(-1), F(5))]:
        dT, dn, de = v
        dxi4 = de + dn - 3 * dT
        dY = dn - 3 * dT
        SQ, Sm = entropies(v)
        GA.check("d ln xi^4 = (4/3) S_m at %s" % (v,), dxi4 == F(4, 3) * Sm)
        GA.check("d ln Y_B = S_Q at %s" % (v,), dY == SQ)
        GA.check("xi^4 = (4/3) Y_B eps differentiated: d ln xi^4 = d ln Y_B + d ln eps", dxi4 == dY + de)
        vals.append((dxi4, dY, Sm))
    GA.check("values pinned", vals == [(-3, -3, F(-9, 4)), (1, 1, F(3, 4)), (1, 0, F(3, 4)), (-2, -7, F(-3, 2))])
    return True


def check_single_modulations():
    premise("dark-matter.stored-asymmetry-charge-not-number")
    premise("synthesis.mirror-temperature-measures-deposit-under-r")
    # (a) temperature at fixed charge
    zg, zq, zm = zetas((F(1), F(0), F(0)))
    SQ, Sm = entropies((F(1), F(0), F(0)))
    GA.check("(a) S_Q = -3 zeta_gamma", SQ == -3 * zg)
    GA.check("(a) S_m = -(9/4) zeta_gamma", Sm == F(-9, 4) * zg)
    # (b) epsilon alone: photons and charge carriers carry no curvature perturbation of their own
    zg, zq, zm = zetas((F(0), F(0), F(1)))
    SQ, Sm = entropies((F(0), F(0), F(1)))
    GA.check("(b) zeta_gamma = zeta_Q = 0", zg == 0 and zq == 0)
    GA.check("(b) S_m = 3/4 d ln eps", Sm == F(3, 4))
    # (c) charge alone
    zg, zq, zm = zetas((F(0), F(1), F(0)))
    SQ, Sm = entropies((F(0), F(1), F(0)))
    GA.check("(c) zeta_gamma = 0, S_Q = d ln n_Q", zg == 0 and SQ == 1)
    return True


def check_sachs_wolfe_share():
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("dark-matter.stored-asymmetry-charge-not-number")
    fQ = 2 * OMB_H2 / (OMB_H2 + OMC_H2)
    GA.check("f_Q >= 2 Omega_b/Omega_m is between 0.31 and 0.32", F("0.31") < fQ < F("0.32"))
    r = 6 * fQ                                  # |2 S_eff|/|zeta| with S_eff = f_Q S_Q, S_Q = -3 zeta
    GA.check("non-adiabatic amplitude ratio above 1.88", r > F("1.88"))
    # non-adiabatic share of the variance for a fully correlated mode: 1 - 1/(1 + s r)^2, s = +1 or -1
    for s in (1, -1):
        share = 1 - 1 / (1 + s * r) ** 2
        GA.check("share magnitude above 0.27 (sign %d)" % s, abs(share) > F("0.27"))
        GA.check("share magnitude above 20 times the Planck bound (sign %d)" % s, abs(share) > 20 * PLANCK_NONAD)
    GA.check("ratio pinned", r == F(26844, 14237))
    return True


def check_mirror_radiation_share():
    premise("synthesis.mirror-temperature-measures-deposit-under-r")
    xi = F("0.448")
    share = xi ** 4 / (1 + xi ** 4)
    GA.check("mirror share at the N_eff cap below 0.0388", share < F("0.0388") and share > F("0.0387"))
    # at the helium edge xi = 2e-2 the share is below 1.7e-7
    xh = F(2, 100)
    GA.check("helium mirror share below 1.7e-7", xh ** 4 / (1 + xh ** 4) < F("1.7e-7"))
    return True
