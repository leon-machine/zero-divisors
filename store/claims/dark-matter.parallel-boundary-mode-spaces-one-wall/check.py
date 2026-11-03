"""dark-matter.parallel-boundary-mode-spaces-one-wall: exact checks of the arithmetic behind (ii)-(iv).

Exact rationals; pi bracketed by Machin's formula. Constants of the record: M_Pl = 1.220890e19 GeV
(non-reduced), m_p = 0.938272 GeV, M_sun = 1.116e57 GeV, 1 g = 5.6096e23 GeV, 1 GeV = 1.16045e13 K;
SI: m_e, e, hbar, c, eps0, G and M_sun = 1.98847e30 kg.
(ii) Information is cheap: S_BH = 4 pi (M/M_Pl)^2 at one solar mass lies in (1.0, 1.1) x 10^77, while a
solar-mass progenitor of M_sun/m_p > 1e57 baryons carries below 1.2 x 10^58 nats even at ten nats per
baryon: the ratio is below 1.2 x 10^-19.
(iii) The Schwinger discharge (premise: the imported discharge fact): E_c = m_e^2 c^3/(e hbar),
Q_c = 4 pi eps0 E_c r_+^2 with r_+ = 2 G M/c^2 lies in (1.28, 1.29) x 10^15 C at one solar mass;
(Q_c/Q_ext)^2 = Q_c^2/(4 pi eps0 G M^2) is proportional to M^2 (exact ratios at 10 and 1e-8 solar masses)
and in ((7.4e-6)^2, (7.6e-6)^2) at one solar mass; it reaches one at M^2 in ((1.3e5)^2, (1.4e5)^2) solar
masses squared, so below about 1.3e5 solar masses discharge returns the charge and above it does not.
(iv) Charge is expensive: T_H = M_Pl^2/(8 pi M) at one solar mass is in (6.0, 6.5) x 10^-8 K (nanokelvin
scale) and m_p/T_H exceeds 1e20; the most baryons a hole can ever emit, M*/m_p with M* = M_Pl^2/(8 pi m_p)
the mass at which T_H = m_p, is below 7 x 10^36 against more than 1e57 swallowed: return fraction below
1e-20.
(i) and (v) (democratic return of energy, no remnant) are premises' content, not computed.
"""
from fractions import Fraction as F
import GA
from series import rounds_to
from tp_premise import premise

# --- exact bracketing helpers (rationals only) ---
def _arctan_inv(k, terms):
    """Partial sums of arctan(1/k) (alternating series): returns (lo, hi)."""
    s, lo, hi = F(0), None, None
    for j in range(terms):
        t = F((-1) ** j, (2 * j + 1) * k ** (2 * j + 1))
        s += t
        if j % 2 == 0:
            hi = s
        else:
            lo = s
    return lo, hi


def pi_bracket(terms=24):
    """Machin: pi = 16 arctan(1/5) - 4 arctan(1/239), with alternating-series brackets."""
    a_lo, a_hi = _arctan_inv(5, terms)
    b_lo, b_hi = _arctan_inv(239, terms)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def iroot_bracket(x, k, denom):
    """(lo, hi), multiples of 1/denom, with lo^k <= x < hi^k (integer bisection)."""
    n = x * denom ** k
    t = n.numerator // n.denominator
    lo, hi = 0, 1
    while hi ** k <= t:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** k <= t:
            lo = mid
        else:
            hi = mid
    return F(lo, denom), F(lo + 1, denom)


def exp_bracket(x, terms=40):
    """(lo, hi) with lo <= e^x <= hi for rational x, by the Taylor series with remainder."""
    if x < 0:
        lo, hi = exp_bracket(-x, terms)
        return 1 / hi, 1 / lo
    s, t = F(1), F(1)
    for j in range(1, terms + 1):
        t = t * x / j
        s += t
    bound = 3 ** (x.numerator // x.denominator + 1)
    return s, s + t * x / (terms + 1) * bound


PI_LO, PI_HI = pi_bracket()


MPL = F(1220890, 10 ** 6) * 10 ** 19
MP = F(938272, 10 ** 6)
MSUN = F(1116, 1000) * 10 ** 57
K_PER_GEV = F(116045, 10 ** 5) * 10 ** 13
M_E = F(91093837, 10 ** 8) * F(1, 10 ** 30)
E_CH = F(1602176634, 10 ** 9) * F(1, 10 ** 19)
HBAR = F(1054571817, 10 ** 9) * F(1, 10 ** 34)
C_L = F(299792458)
EPS0 = F(88541878128, 10 ** 10) * F(1, 10 ** 12)
G_N = F(667430, 10 ** 5) * F(1, 10 ** 11)
MSUN_KG = F(198847, 10 ** 5) * 10 ** 30


def q_c(m_solar, pi_):
    e_c = M_E ** 2 * C_L ** 3 / (E_CH * HBAR)
    r_plus = 2 * G_N * m_solar * MSUN_KG / C_L ** 2
    return 4 * pi_ * EPS0 * e_c * r_plus ** 2


def ratio2(m_solar, pi_):
    return q_c(m_solar, pi_) ** 2 / (4 * pi_ * EPS0 * G_N * (m_solar * MSUN_KG) ** 2)


def check_information_is_cheap():
    s_lo, s_hi = 4 * PI_LO * (MSUN / MPL) ** 2, 4 * PI_HI * (MSUN / MPL) ** 2
    n_sw = MSUN / MP
    s_star = 10 * n_sw
    ok = F(10) ** 77 < s_lo and s_hi < F(11, 10) * 10 ** 77
    ok = ok and n_sw > F(10) ** 57 and s_star < F(12, 10) * 10 ** 58 and s_star / s_lo < F(12, 10) * F(1, 10 ** 19)
    GA.check("prop:infall(ii): S_BH(solar) in (1.0, 1.1)e77 against at most 1.2e58 for the progenitor", ok)
    return ok


def check_schwinger_discharge_and_crossover():
    premise("dark-matter.imported-schwinger-discharge-charged-hole")
    ok = F(128, 100) * 10 ** 15 < q_c(1, PI_LO) and q_c(1, PI_HI) < F(129, 100) * 10 ** 15
    ok = ok and F(74, 10 ** 7) ** 2 < ratio2(1, PI_LO) and ratio2(1, PI_HI) < F(76, 10 ** 7) ** 2
    ok = ok and ratio2(10, PI_LO) / ratio2(1, PI_LO) == 100
    ok = ok and ratio2(F(1, 10 ** 8), PI_HI) / ratio2(1, PI_HI) == F(1, 10 ** 16)
    mx2_lo, mx2_hi = 1 / ratio2(1, PI_HI), 1 / ratio2(1, PI_LO)
    ok = ok and (F(13, 10) * 10 ** 5) ** 2 < mx2_lo and mx2_hi < (F(14, 10) * 10 ** 5) ** 2
    ok = ok and ratio2(F(12, 10) * 10 ** 5, PI_HI) < 1 < ratio2(F(15, 10) * 10 ** 5, PI_LO)
    GA.check("prop:infall(iii): Q_c(solar) in (1.28, 1.29)e15 C, 7.5e-6 of extremal, proportional to M, extremal at "
             "(1.3, 1.4)e5 solar masses", ok)
    return ok


def check_charge_is_expensive():
    premise("dark-matter.p5-boundary-modes-hold-entropy-not")
    premise("hawking.greybody-inheritance-under-interface-premise")
    th_lo, th_hi = MPL ** 2 / (8 * PI_HI * MSUN), MPL ** 2 / (8 * PI_LO * MSUN)
    # by hand: (1.22089e19)^2/(8 pi 1.116e57) GeV x 1.16045e13 K/GeV = 6.16702e-8 K, in the quoted
    # (6.0, 6.5)e-8 K; m_p/T_H = 0.938272/5.31440e-21 = 1.765549e20, above the quoted 1e20
    ok = all(rounds_to(t * K_PER_GEV, 616702, -13) for t in (th_lo, th_hi))
    ok = ok and all(rounds_to(MP / t, 1765549, 14) for t in (th_lo, th_hi))
    mstar_hi = MPL ** 2 / (8 * PI_LO * MP)
    nmax = mstar_hi / MP
    # by hand: M_Pl^2/(8 pi m_p^2) = 6.736832e36 baryons (below the quoted 7e36), over
    # M_sun/m_p = 1.18943e57: return fraction 5.663961e-21 (below the quoted 1e-20)
    ok = ok and rounds_to(nmax, 6736832, 30) and rounds_to(nmax / (MSUN / MP), 5663961, -27)
    GA.check("prop:infall(iv): T_H(solar) in (6.0, 6.5)e-8 K, m_p/T_H > 1e20; return fraction below 1e-20", ok)
    return ok
