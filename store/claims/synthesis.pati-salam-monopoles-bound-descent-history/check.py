"""synthesis.pati-salam-monopoles-bound-descent-history: exact checks.

pi is bounded by 3 < pi < 22/7. Inputs (exact rationals from decimal strings):
- the stored chain: M_I = 1.95e10 GeV, g_R(M_I) = 0.469, v_R = M_I/g_R (standard-model.what-angle-asks-neutrino-sector);
  the (10,1,3) breaks Pati-Salam directly to the Standard Model at M_I (standard-model.majorana-element);
- the seeding condition c T^4 >= A/2, A^(1/4) = 1.217e12 GeV, c = 0.312 for the four odd towers' vectors
  (synthesis.seeding-remainder-excludes-perturbative-pati-salam);
- T_0 = 2.7255 K (synthesis.imported-planck-2018-lcdm-parameters), k_B = 8.617333262e-5 eV/K,
  hbar c = 1.973269804e-5 eV cm, c = 2.99792458e10 cm/s, g_s(T_0) = 43/11, reduced Planck mass 2.435e18 GeV;
- literature, cited from memory in the proof: the MACRO flux limit F < 1.4e-16 cm^-2 s^-1 sr^-1, the Kibble
  probability p >= 1/10 per Hubble volume, galactic speeds beta >= 7e-4, Preskill's annihilation floor
  n/s ~ 1e-10 (M/1e14 GeV).
"""
from fractions import Fraction as F
import GA
from GA import mul, add, scal, sc, gen, eq
from tp_premise import premise

PI_LO, PI_HI = F(3), F(22, 7)
MP = F("2.435e18")
G_STAR = F("106.75")
P_K = F(1, 10)
FLUX = F("1.4e-16")
BETA = F("7e-4")
C_CM = F("2.99792458e10")
T0_CM = F("2.7255") * F("8.617333262e-5") / F("1.973269804e-5")     # k_B T_0/(hbar c) in cm^-1
GS0 = F(43, 11)
M_I, G_R = F("1.95e10"), F("0.469")
V_R = M_I / G_R
A4 = F("1.217e12")
C_ODD = F("0.312")


def kibble_sq_lo(T):
    """lower bound on (n_M/s)^2 = p^2 (pi^2 g/1440)(T/M_P)^6, with pi > 3: one monopole per Hubble volume
    H^-3 with probability p, H = pi sqrt(g/90) T^2/M_P, s = (2 pi^2/45) g T^3"""
    return P_K ** 2 * PI_LO ** 2 * G_STAR / 1440 * (T / MP) ** 6


def nmax_hi(beta):
    """upper bound on today's n_M/s from the flux limit: n_M <= 4 pi F/(beta c), s_0 = (2 pi^2/45) g_s0 T_0^3"""
    return 4 * PI_HI * FLUX / (beta * C_CM) / ((2 * PI_LO ** 2 / 45) * GS0 * T0_CM ** 3)


def check_kibble_constant():
    premise("standard-model.what-angle-asks-neutrino-sector")
    # (p H^3/s)^2 = p^2 pi^6 (g/90)^3 (T/M_P)^6 / ((2 pi^2/45)^2 g^2) = p^2 pi^2 g (T/M_P)^6 * 45^2/(4 * 90^3)
    GA.check("45^2/(4 * 90^3) = 1/1440", F(45) ** 2 / (4 * F(90) ** 3) == F(1, 1440))
    # store c pi^n as (c, n): pi^6/(pi^2)^2 = pi^2
    GA.check("pi powers: 6 - 2*2 = 2", 6 - 2 * 2 == 2)
    # control: one per Hubble volume at T = M_P (formal) gives (n/s)^2 = p^2 pi^2 g/1440
    GA.check("formal value at T = M_P", kibble_sq_lo(MP) == P_K ** 2 * 9 * G_STAR / 1440)
    return True


def check_hypercharge_is_a_circle_in_pati_salam():
    premise("standard-model.majorana-element")
    premise("standard-model.imported-pati-salam-representation-theory-survival")
    # Y = T3R + (B-L)/2 on (4,2,1) + (4bar,1,2): (B-L)/2 = diag(1/6,1/6,1/6,-1/2) on the 4 is traceless,
    # T3R = +-1/2 is traceless on the doublet, so Y lies in the semisimple algebra su(4)+su(2)_R and generates a
    # circle in the simply connected G; it commutes with su(3)+su(2)_L, so H contains a central U(1) and
    # pi_2(G/H) = pi_1(H) contains Z.
    bl = [F(1, 6)] * 3 + [F(-1, 2)]
    GA.check("(B-L)/2 traceless on the 4", sum(bl) == 0)
    GA.check("T3R traceless on the doublet", F(1, 2) + F(-1, 2) == 0)
    # Standard Model hypercharges (Q = T3L + Y): left (4,2,1) gives Y = (B-L)/2: Q_L 1/6 and L -1/2;
    # right (4bar,1,2) gives u^c, d^c, e^c, nu^c: Y = -(B-L)/2 -+ 1/2 ... listed as charges of the conjugates
    yl = sorted(set(bl))
    GA.check("left-handed hypercharges 1/6 (quarks), -1/2 (leptons)", yl == [F(-1, 2), F(1, 6)])
    right = sorted({-b + t for b in set(bl) for t in (F(1, 2), F(-1, 2))})
    GA.check("conjugate right-handed hypercharges -2/3, 1/3, 0, 1",
             right == [F(-2, 3), F(0), F(1, 3), F(1)])
    # the circle closes: exp(2 pi i t Y) = 1 on the 16 first at t = 6 (lcm of denominators)
    allq = set(bl) | set(right)
    GA.check("period 6 on the 16", all((6 * q).denominator == 1 for q in allq)
             and not all((3 * q).denominator == 1 for q in allq))
    # GA form: a unit imaginary for the phase, the spatial bivector e1e2 of Cl(2,4), squares to -1
    SQ = (1, -1, -1, -1, 1, -1)
    i12 = mul(gen(1), gen(2), SQ)
    GA.check("phase unit squares to -1", eq(mul(i12, i12, SQ), sc(-1)))
    return True


def check_causal_minimum_exceeds_flux_limit():
    premise("standard-model.what-angle-asks-neutrino-sector")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    # every integer literal below sits in an exact equality or an integer floor pin, so changing any one fails
    GA.check("v_R = M_I/g_R = 19500000000000/469 GeV exactly", V_R == F(19500000000000, 469))
    GA.check("s_0 prefactor at pi = 3: (2 * 3^2/45) g_s0 = 86/55", (2 * PI_LO * PI_LO / 45) * GS0 == F(86, 55))
    s0_lo = (2 * PI_LO * PI_LO / 45) * GS0 * T0_CM * T0_CM * T0_CM
    s0_hi = (2 * PI_HI * PI_HI / 45) * GS0 * T0_CM * T0_CM * T0_CM
    GA.check("s_0 brackets: floor 2636 (pi = 3) and 2893 (pi = 22/7), 2891 cm^-3 at pi",
             s0_lo // 1 == 2636 and s0_hi // 1 == 2893)
    k2 = kibble_sq_lo(V_R)
    nm = nmax_hi(BETA)
    GA.check("causal minimum at T = v_R: (n_M/s)^2 floor-pinned, 1.65e-49 (n_M/s = 4.07e-25)",
             (k2 * 10 ** 51) // 1 == 165)
    GA.check("flux maximum at beta = 7e-4: n_M/s floor-pinned at 3.18e-26", (nm * 10 ** 28) // 1 == 318)
    # excess: (minimum/maximum)^2 = 163.41..., so the minimum exceeds the maximum by 12.78 with adverse pi
    GA.check("excess squared pinned: 100 k2/nm^2 has floor 16341", (100 * k2 / (nm * nm)) // 1 == 16341)
    # threshold: the minimum scales as T^3, so (T_*/v_R)^6 = nm^2/k2; with adverse pi brackets 6.119e-3
    # (T_* = 0.428 v_R) and with reversed brackets 4.217e-3 (T_* = 0.402 v_R): T_* lies in (0.3, 0.48) v_R
    nmax_lo = 4 * PI_LO * FLUX / (BETA * C_CM) / s0_hi
    k2_hi = k2 * (PI_HI / PI_LO) * (PI_HI / PI_LO)
    GA.check("threshold sixth power pinned on both sides",
             (10 ** 6 * nm * nm / k2) // 1 == 6119 and (10 ** 6 * nmax_lo * nmax_lo / k2_hi) // 1 == 4217)
    t48, t30 = F("0.48"), F("0.3")
    sixth = lambda x: x * x * x * x * x * x
    GA.check("so 0.3 v_R < T_* < 0.48 v_R",
             sixth(t30) < nmax_lo * nmax_lo / k2_hi and nm * nm / k2 < sixth(t48))
    # speed: the minimum exceeds the maximum for beta > beta_*, beta_*^2 = (nm beta)^2/k2 = 2.998e-9
    GA.check("beta_*^2 pinned at 2.998e-9 (beta_* = 5.5e-5 < 1e-4)",
             (10 ** 12 * (nm * BETA) * (nm * BETA) / k2) // 1 == 2998)
    return True


def check_annihilation_cannot_lower_it():
    premise("standard-model.what-angle-asks-neutrino-sector")
    # monopole mass ~ 4 pi v_R/g_R > 1e12 GeV; Preskill's floor 1e-10 (M/1e14) lies far above the causal minimum,
    # so annihilation (which acts only above its floor) cannot bring n_M/s below min(initial, floor)
    MM = 4 * PI_LO * V_R / G_R
    GA.check("M_M at pi = 3: 4 * 3 * v_R/g_R has floor 1063e9 GeV", MM // 10 ** 9 == 1063)
    floor = F("1e-10") * MM / F("1e14")
    GA.check("Preskill floor pinned at 1.063e-12", (floor * 10 ** 15) // 1 == 1063)
    GA.check("floor^2/minimum^2 has floor 68440e20: the floor is 2.6e12 times the causal minimum",
             (floor * floor / kibble_sq_lo(V_R)) // 10 ** 20 == 68440)
    # overclosure is not the constraint: Omega h^2 < 0.12 allows n/s < 0.12 * 1.0537e-5/(M * 2891)
    clos = F("0.12") * F("1.0537e-5") / (F("1.1e12") * 2891)
    GA.check("closure maximum pinned at 3.976e-22 (s_0 = 2891, M_M = 1.1e12 GeV)", (clos * 10 ** 25) // 1 == 3976)
    GA.check("closure maximum squared exceeds the causal minimum squared", clos * clos > kibble_sq_lo(V_R))
    return True


def check_seeding_needs_cold_transition():
    premise("synthesis.seeding-remainder-excludes-perturbative-pati-salam")
    # seeding: T_desc^4 >= A/(2c) with c = 0.312: T_desc > 1.36e12 GeV
    t4 = A4 ** 4 / (2 * C_ODD)
    GA.check("T_seed > 1.36e12 GeV", t4 > F("1.36e12") ** 4 and t4 < F("1.38e12") ** 4)
    GA.check("T_seed > 32 v_R: the bath restores Pati-Salam unless non-restoration", t4 > (32 * V_R) ** 4)
    # the transition then happens in the descended phase; with the flux limit it needs T_c < 0.48 v_R < 2.0e10 GeV
    GA.check("0.48 v_R < 2.0e10 GeV", F("0.48") * V_R < F("2.0e10"))
    # seeding below the transition, T_desc < 2.0e10, would need c > A/(2 T^4)
    c_needed = A4 ** 4 / (2 * F("2.0e10") ** 4)
    GA.check("seeding at T_desc < 2e10 needs c > 6.8e6 (about 3e9 vectors at 2.3e-3 each)",
             c_needed > F("6.8e6") and c_needed / F("2.3e-3") > F("2.9e9"))
    # aligned-deposit clause: a deposit below T_c whose orientation is uncorrelated beyond its Hubble length
    # gives the same minimum at T_desc, excluded for T_desc > 0.48 v_R
    GA.check("deposit clause threshold is the same function", kibble_sq_lo(F("0.48") * V_R) > nmax_hi(BETA) ** 2)
    return True
