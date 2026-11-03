"""synthesis.collar-temperature-fixed-locally-by-r-loc: exact checks.

(1) Frame Cl(1,3) at a collar point (Q(e0) = 1 along d_tau, e1 the t-direction, e2, e3 the sphere): B1 = e0 e1 is a
unit boost (B1^2 = 1); its timelike plane has the null generators e0 +- e1, dilated with weights -+1 by (1/2) ad_B1,
and its edge plane (e2, e3) is fixed; the same for the sphere boost B2 = e0 e2 with generators e0 +- e2.
(2) Rates (units 2M = 1): the Killing rapidity rate rho(r) = 1/(2 r^2) and the Hubble rate
rho_H = (1/3) S(r) (1 - r)^{-1/2} with S(r) = sum_k binom(2k,k) 4^{-k} 3/(2k+3) r^k: exact power series give
rho_H = 1/3 + (4/15) r + ..., so beta_H/(6 pi) = 1 - (4/5) r + c_2 r^2 + ... ; in Killing time beta = 4 pi r^2.
At the cutoff of a hole with 2M = 1000, r_c = (2M)^{-2/3} = 1/100.
(3) The Killing-extension state of the slice-product reading has rapidity period 2 pi / r^2, which equals 2 pi only at
r = 1: (R_loc) fails on every slice inside (checked at r = 1/2, 1/10, 1/100).
(4) KMS for a flow and its inverse on a matrix factor forces the generator to be scalar (two radial sheets on one
completed pair), and e^{-pi B1}, e^{-pi B2} are not proportional (frame atom carrying both B1 and B2): 1, B1, B2 are
independent, and e^{-pi B} = cosh(pi) - sinh(pi) B for B^2 = 1.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

S13 = GA.sig(1, 3)


def half_ad(B, v):
    return GA.scal(F(1, 2), GA.sub(GA.mul(B, v, S13), GA.mul(v, B, S13)))


def blade(i, j):
    return GA.mul(GA.gen(i), GA.gen(j), S13)


def check_radial_and_sphere_local_horizons():
    premise("synthesis.collar-isotropy-selects-t-boost")
    ok = True
    for j in (1, 2, 3):
        B = blade(0, j)
        ok = ok and GA.eq(GA.mul(B, B, S13), GA.sc(1))
        lp = GA.add(GA.gen(0), GA.gen(j))
        lm = GA.sub(GA.gen(0), GA.gen(j))
        ok = ok and GA.dot(lp, lp, S13) == 0 and GA.dot(lm, lm, S13) == 0
        ok = ok and GA.eq(half_ad(B, lp), GA.neg(lp)) and GA.eq(half_ad(B, lm), lm)
        others = [k for k in (1, 2, 3) if k != j]
        ok = ok and all(GA.is_zero(half_ad(B, GA.gen(k))) for k in others)
    GA.check("B1 (and B2) are unit boosts of local horizons at a collar point, edges fixed", ok)
    return ok


def binom(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def series_S(N):
    return [F(binom(2 * k, k), 4 ** k) * F(3, 2 * k + 3) for k in range(N)]


def series_inv_sqrt_one_minus(N):
    return [F(binom(2 * k, k), 4 ** k) for k in range(N)]


def check_hubble_and_killing_periods_of_r_loc_state():
    premise("singularity.modular-flow-boundary-modes-holonomy-universal")
    premise("synthesis.collar-kms-extension-completion-locus")
    N = 6
    S = series_S(N)
    rhoH = [F(1, 3) * c for c in GA.ps_mul(S, series_inv_sqrt_one_minus(N), N)]
    ok = rhoH[0] == F(1, 3) and rhoH[1] == F(4, 15)
    # beta_H / (6 pi) = (1/3) / rho_H
    inv = GA.ps_inv(rhoH, N)
    ratio = [F(1, 3) * c for c in inv]
    ok = ok and ratio[0] == 1 and ratio[1] == F(-4, 5)
    # cross-check S against the integral tau = int_0^r sqrt(x/(1-x)) dx = (2/3) r^{3/2} S(r):
    # d/dr [r^{3/2} S] = (3/2) r^{1/2} (1 - r)^{-1/2}  <=>  sum_k (k + 3/2) s_k r^k = (3/2) sum_k b_k r^k
    b = series_inv_sqrt_one_minus(N)
    ok = ok and all((k + F(3, 2)) * S[k] == F(3, 2) * b[k] for k in range(N))
    # Killing time: rho = 1/(2 r^2), period 2 pi / rho = 4 pi r^2; horizon r = 1 gives 4 pi = 2 pi / kappa, kappa = 1/2
    for r in (F(1), F(1, 2), F(1, 100)):
        rho = 1 / (2 * r * r)
        ok = ok and 2 / rho == 4 * r * r   # (2 pi / rho) / pi
    ok = ok and 1 / (2 * F(1) ** 2) == F(1, 2)
    # cutoff of a hole with 2M = 1000: r_c^3 = (2M)^{-2}
    rc = F(1, 100)
    ok = ok and rc ** 3 == F(1, 1000 ** 2)
    lead = 1 + ratio[1] * rc
    ok = ok and lead == F(124, 125)
    GA.check("(R_loc) state: beta_H = 6 pi (1 - 4r/5 + ...), Killing beta = 4 pi r^2", ok)
    return ok


def check_killing_extension_violates_r_loc():
    premise("synthesis.collar-kms-extension-three-flows")
    ok = True
    for r in (F(1, 2), F(1, 10), F(1, 100)):
        period_over_2pi = 1 / (r * r)        # rapidity period 2 pi / r^2 of the Killing-extended state
        ok = ok and period_over_2pi != 1 and period_over_2pi > 1
    ok = ok and 1 / (F(1) * F(1)) == 1       # equal at the horizon only
    ok = ok and 1 / (F(1, 2) ** 2) == 4
    # (R) on one mode set under (A): Killing beta = 4 pi (units 2M = 1) run at rapidity rate rho(r_c) = 1/(2 r_c^2)
    # gives rapidity period 4 pi rho(r_c) = 2 pi / r_c^2; at 2M = 1000, r_c = 1/100: 2 pi * 10^4, not 2 pi
    rc = F(1, 100)
    rho_c = 1 / (2 * rc * rc)
    ok = ok and 4 * rho_c / 2 == 10 ** 4 and 4 * rho_c / 2 == 1 / (rc * rc)
    GA.check("the Killing-extended state has rapidity period 2 pi / r^2, not 2 pi, inside the horizon", ok)
    return ok


def check_shared_atoms_carry_no_temperature():
    premise("singularity.kms-uniqueness-factor")
    # (a) one completed pair read by both radial sheets: Gibbs densities diag(1, q) and diag(1, 1/q) at weight w
    q = F(1, 5)                    # stands for e^{-2 pi w}
    rho1 = (F(1) / (1 + q), q / (1 + q))
    rho2 = (F(1) / (1 + 1 / q), (1 / q) / (1 + 1 / q))
    ok = rho1 != rho2 and rho1[1] == F(1, 6) and rho2[1] == F(5, 6)
    # (b) the frame atom: a + b B1 proportional to a + b B2 with b != 0 is impossible, since 1, B1, B2 are independent
    B1, B2 = blade(0, 1), blade(0, 2)
    blades = GA.all_blades(4)
    rows = [GA.basis_vector_of(x, blades) for x in (GA.sc(1), B1, B2)]
    ok = ok and GA.field_rank(rows) == 3
    ok = ok and GA.eq(GA.mul(B1, B1, S13), GA.sc(1)) and GA.eq(GA.mul(B2, B2, S13), GA.sc(1))
    ok = ok and not GA.commutes(B1, B2, S13)
    GA.check("one pair for two sheets, or one frame atom for two planes, has no common period-2 pi state", ok)
    return ok
