"""synthesis.holographic-thermal-fluctuations-fall-short-in-the-descent-window: exact checks.

Thermal fluctuations converted at Hubble exit (Nayeri-Brandenberger-Vafa form, imported):
  P_Phi(k) = 8 G^2 k^-4 <delta rho^2>_R at R = 1/k,  <delta rho^2>_R = T^2 C(R) / R^6.
(1) Index: C ~ R^gamma, T ~ R^tau give P_Phi ~ k^(2 - gamma - 2 tau): checked by exponent arithmetic. Area law at fixed
    T: index 0 (scale invariant), 8.4 standard deviations from the measured -0.0351; extensive capacity: -1; the
    modular temperature T ~ 1/R with the area law: +2. The measured value needs gamma + 2 tau = 2.0351.
(2) Amplitude: C = lam A/(4G), A = 4 pi R^2, gives P_Phi = 8 pi lam G T^2 = 8 pi lam (T/M_Pl)^2, independent of k.
    At the window's ceiling T = 7.3e8 GeV, P_Phi < 9.0e-20 lam; the target (4/9) A_s = 9.33e-10 (Phi = (2/3) zeta in
    the radiation era) needs lam > 1.0e10 there, or T between 7.4e13 and 7.5e13 GeV at lam = 1.
(3) The frozen point's Gibbons-Hawking temperature T = H_L/(2 pi), H_L^2 = H0^2 Omega_L: P_Phi = 2 lam H0^2 Omega_L/(pi
    M_Pl^2) < 1e-122 lam.
pi is bracketed by 3.14159 < pi < 3.1416; constants: M_Pl = 1.22089e19 GeV, hbar = 6.58212e-25 GeV s,
1 Mpc = 3.08568e19 km (cited).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

PI_LO, PI_HI = F("3.14159"), F("3.1416")
MPL = F("1.22089e19")
HBAR = F("6.58212e-25")
MPC_KM = F("3.08568e19")
H0_KMS = F("67.36")
OMEGA_M, OMEGA_R = F("0.3153"), F("0.000092")
AS = F("2.100e-9")
NS1, SIG = F("-0.0351"), F("0.0042")
T_CEIL = F("7.3e8")


def index(gamma, tau):
    # P_Phi ~ k^-4 * T^2 C / R^6 at R = 1/k: exponent of k is -4 - 2 tau - gamma + 6
    return -4 - 2 * tau - gamma + 6


def check_index_from_capacity_and_temperature():
    premise("singularity.area-law-test")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    GA.check("area law at fixed T: scale invariant", index(2, 0) == 0)
    GA.check("extensive capacity at fixed T: index -1", index(3, 0) == -1)
    GA.check("area law at the modular temperature T ~ 1/R: index 2", index(2, -1) == 2)
    GA.check("scale invariance is 8.4 sigma from the measured index", F(83, 10) < (0 - NS1) / SIG < F(84, 10))
    need = 2 - NS1
    GA.check("measured index needs gamma + 2 tau = 2.0351", index(need, 0) == NS1 and need == F("2.0351"))
    GA.check("with gamma = 2 the needed tau is 0.01755", index(2, F("0.01755")) == NS1)
    GA.check("pinned exponent table", [index(g, t) for g in (1, 2, 3) for t in (-1, 0, 1)] == [3, 1, -1, 2, 0, -2, 1, -1, -3])
    return True


def amplitude_bounds(T, lam=1):
    """8 pi lam (T/MPL)^2 bracketed by the pi bracket."""
    x = lam * T * T / (MPL * MPL)
    return 8 * PI_LO * x, 8 * PI_HI * x


def check_amplitude_in_window():
    premise("singularity.area-law-test")
    premise("synthesis.untuned-fit-caps-lightest-heavy-neutrino")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    target = F(4, 9) * AS
    lo, hi = amplitude_bounds(T_CEIL)
    GA.check("at the window ceiling P_Phi < 9.0e-20", hi < F("9.0e-20"))
    GA.check("at the window ceiling P_Phi > 8.9e-20", lo > F("8.9e-20"))
    GA.check("short of (4/9) A_s by more than 1.0e10", target / hi > F("1.0e10"))
    GA.check("1 MeV floor is far below", amplitude_bounds(F("1e-3"))[1] < F("1e-42"))
    # temperature that reaches the target at lam = 1: T^2 = target MPL^2 / (8 pi)
    t2_hi = target * MPL * MPL / (8 * PI_LO)
    t2_lo = target * MPL * MPL / (8 * PI_HI)
    GA.check("required temperature above 7.4e13 GeV", t2_lo > F("7.4e13") ** 2)
    GA.check("required temperature below 7.5e13 GeV", t2_hi < F("7.5e13") ** 2)
    GA.check("required temperature above the window ceiling by more than 1e5", t2_lo > (F("1e5") * T_CEIL) ** 2)
    GA.check("pinned target", target == F(14, 15) * F("1e-9"))
    return True


def check_frozen_point_temperature():
    premise("synthesis.frozen-point-geometry-reads-descent-as-vacuum")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    h0 = H0_KMS / MPC_KM * HBAR  # GeV
    GA.check("H0 between 1.436e-42 and 1.438e-42 GeV", F("1.436e-42") < h0 < F("1.438e-42"))
    omega_l = 1 - OMEGA_M - OMEGA_R
    GA.check("Omega_L = 0.684608", omega_l == F("0.684608"))
    # P = 8 pi lam (H_L/(2 pi))^2 / MPL^2 = 2 lam H0^2 Omega_L / (pi MPL^2)
    p_hi = 2 * h0 * h0 * omega_l / (PI_LO * MPL * MPL)
    GA.check("frozen-point temperature gives P_Phi below 1e-122", p_hi < F("1e-122"))
    GA.check("and above 1e-123", 2 * h0 * h0 * omega_l / (PI_HI * MPL * MPL) > F("1e-123"))
    GA.check("short of the target by more than 1e112", F(4, 9) * AS / p_hi > F("1e112"))
    p_lo = 2 * h0 * h0 * omega_l / (PI_HI * MPL * MPL)
    GA.check("pinned: P_Phi between 6.03e-123 and 6.04e-123", F("6.03e-123") < p_lo and p_hi < F("6.04e-123"))
    GA.check("pinned: H0 between 1.4368e-42 and 1.4369e-42 GeV", F("1.4368e-42") < h0 < F("1.4369e-42"))
    GA.check("pinned: the factor 2/pi form equals 8 pi (H/(2 pi))^2", 8 * PI_LO * (1 / (2 * PI_LO)) ** 2 == 2 / PI_LO)
    return True
