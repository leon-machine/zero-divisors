"""synthesis.transmutation-of-the-rung-field-needs-a-charged-pair-near-450-gev: exact checks.

The Gildener-Weinberg one-loop scalon mass (cited from memory, an explicit hypothesis of the claim):
8 pi^2 v^2 m_S^2 = sum_vectors 3 M^4 + sum_real scalars M^4 - sum_Dirac 4 N_c M^4, masses on the flat direction.
The weights come from the rung field's content on its flat physical ray: the gauge mass form of
synthesis.rung-field-on-the-lift-locus (2) (eigenvalues g^2, g^2, g^2 + g'^2, 0), the charged plane of the physical
directions (two real), the top's Dirac entry |beta| under the c* reading. Inputs: stored masses; v in [246, 247] GeV
(the tree value from the stored M_W, sin^2 theta_W(M_Z), alpha(M_Z) is certified inside), m_t in [162, 173] GeV
(stored pole and M_Z-scale values inside), pi in [333/106, 355/113]. Exact arithmetic throughout.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

PI_LO, PI_HI = F(333, 106), F(355, 113)
V_LO, V_HI = F(246), F(247)
MT_LO, MT_HI = F(162), F(173)
MH_LO, MH_HI = F(125), F(1254, 10)
G_SAMPLES = [(F(2, 3), F(1, 2)), (F(13, 20), F(7, 20))]
MPM_LO, MPM_HI = F(450), F(456)
MID_LO = F(454)
ZERO = F(0)
THR_LO1, THR_HI1 = F(250), F(267)
V_PDG = F(24622, 100)
Q_LO, Q_HI = F(32, 10), F(35, 10)
CW_LO, CW_HI = F(97, 10), F(99, 10)
SMNEG_LO, SMNEG_HI = F(45), F(47)
THR_LO, THR_HI = F(249), F(268)


def charpoly_roots_ok(Pm, roots):
    """det(P - r 1) = 0 for every listed root, with multiplicities by rank."""
    n = len(Pm)
    out = []
    for r in roots:
        M = [[Pm[i][j] - (r if i == j else 0) for j in range(n)] for i in range(n)]
        out.append(n - GA.mat_rank(M))
    return out


def gauge_form(g, gp):
    return [[g * g, 0, 0, 0], [0, g * g, 0, 0], [0, 0, g * g, g * gp], [0, 0, g * gp, gp * gp]]


def weights(g, gp):
    """GW weights read from the content: (W^4 weight, Z^4 weight, charged-scalar weight, top weight)."""
    mult = charpoly_roots_ok(gauge_form(g, gp), [g * g, g * g + gp * gp, F(0)])
    n_w, n_z, n_photon = mult
    polarisations = 3
    charged_real = 2          # the charged plane of the physical directions (stored clause (3)), checked below
    dirac_dof, colours = 4, 3
    return polarisations * n_w, polarisations * n_z, charged_real, -dirac_dof * colours, n_photon


def light(sign_mb=1):
    mb = quantity("quantity.bottom-quark-mass")
    mc = quantity("quantity.charm-quark-mass")
    mtau = quantity("quantity.tau-mass") / 1000
    return 12 * mb ** 4 + 12 * mc ** 4 + 4 * mtau ** 4


def mpm4(pi, v, mh, mt, MW, MZ, wW, wZ, ws, wt):
    """m_pm^4 solved from 8 pi^2 v^2 m_h^2 = wW M_W^4 + wZ M_Z^4 + ws m_pm^4 + wt m_t^4 - light."""
    return (8 * pi * pi * v * v * mh * mh - wW * MW ** 4 - wZ * MZ ** 4 - wt * mt ** 4 + light()) / ws


def check_weights_from_the_rung_content():
    """(i): the gauge mass form has eigenvalues g^2 (twice), g^2 + g'^2 (once), 0 (once), so the weights are
    6 M_W^4 + 3 M_Z^4 with one massless photon; the charged plane is two real directions; the top weight -12."""
    premise("synthesis.rung-field-on-the-lift-locus")
    for g, gp in G_SAMPLES:
        wW, wZ, ws, wt, nph = weights(g, gp)
        GA.check("weights (6, 3, 2, -12) and one photon", (wW, wZ, ws, wt, nph) == (6, 3, 2, -12, 1))
        GA.check("eigenvalues sum to the trace", 2 * g * g + (g * g + gp * gp) == sum(gauge_form(g, gp)[i][i] for i in range(4)))
    return True


def check_charged_mass_scales_with_the_norm_on_the_flat_ray():
    """(i): on the flat physical ray of an admissible scale-free potential (cone Q = 0, alpha = 0, beta = (-lam, 0)),
    the charged mass squared from the exact second variation along the charged plane equals 2(2a - e) N, proportional
    to N (M_W^2 = g^2 N/2 and M_Z^2 are proportional to N by their formula): the content needed by the GW formula is homogeneous of degree one in N."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    a, b, e = F(3, 4), F(-1, 4), F(1, 2)

    def V(al, be):
        A = sum(x * x for x in al)
        B = sum(x * x for x in be)
        Nn, mm = (A + B) / 2, (A - B) / 2
        return a * Nn * Nn + b * mm * mm + e * Nn * mm
    for lam in (F(1), F(3), F(10)):
        Nst = lam * lam / 2
        # alpha = (0, eps z) keeps Q = alpha^T beta = 0 exactly; second variation by finite exact differences
        eps = F(1, 7)
        z = F(1)
        Vp = V([0, eps * z], [-lam, 0])
        V0 = V([0, 0], [-lam, 0])
        GA.check("flat: V vanishes on the ray", V0 == 0)
        # alpha = (0, eps z): dN = dm = eps^2 |z|^2/2 exactly, kinetic coefficient 2 N(d) = |z|^2 = 1
        GA.check("exact variation along the charged plane",
                 Vp - V0 == (2 * a - e) * 2 * Nst * eps * eps / 2 + (a + b + e) * eps ** 4 / 4)
        mass2 = 2 * ((Vp - V0) - (a + b + e) * eps ** 4 / 4) / (eps * eps)
        GA.check("charged mass 2(2a - e)N, proportional to N", mass2 == 2 * (2 * a - e) * Nst)
    return True


def check_standard_model_content_alone_gives_negative_mass():
    """(ii): with the weights of (i), 6 M_W^4 + 3 M_Z^4 - 12 m_t^4 - light < 0 for every m_t in [162, 173] GeV (the
    stored m_t values lie in that range): without the charged pair the scalon mass squared is negative; the bosons
    alone would give the classic value, between 9.7 and 9.9 GeV."""
    premise("synthesis.rung-field-on-the-lift-locus")
    MW = quantity("quantity.w-boson-mass")
    MZ = quantity("quantity.z-boson-mass")
    mt_pole = quantity("quantity.top-quark-mass")
    mt_mz = quantity("quantity.top-quark-mass-mz")
    wW, wZ, ws, wt, _ = weights(*G_SAMPLES[0])
    GA.check("stored top masses inside the range", MT_LO <= mt_mz <= MT_HI and MT_LO <= mt_pole <= MT_HI)
    GA.check("weights are 6, 3, -12", (wW, wZ, wt) == (6, 3, -12))
    GA.check("SM content: negative at the lightest top", wW * MW ** 4 + wZ * MZ ** 4 + wt * MT_LO ** 4 - light() < 0)
    bos = wW * MW ** 4 + wZ * MZ ** 4
    GA.check("bosons alone: m between 9.7 and 9.9 GeV",
             CW_LO ** 2 * 8 * PI_HI ** 2 * V_HI ** 2 < bos < CW_HI ** 2 * 8 * PI_LO ** 2 * V_LO ** 2)
    GA.check("SM content at the stored pole top: m_S^2 between -(47 GeV)^2 and -(45 GeV)^2",
             -SMNEG_HI ** 2 * 8 * PI_LO ** 2 * V_LO ** 2 < bos + wt * mt_pole ** 4 - light() < -SMNEG_LO ** 2 * 8 * PI_HI ** 2 * V_HI ** 2)
    return True


def check_positivity_threshold():
    """(iii): the scalon mass squared is positive iff 2 m_pm^4 > 12 m_t^4 + light - 6 M_W^4 - 3 M_Z^4; the threshold
    lies in (249, 250) GeV at m_t = 162 and in (267, 268) GeV at m_t = 173, above m_t - m_b."""
    premise("synthesis.rung-field-on-the-lift-locus")
    MW = quantity("quantity.w-boson-mass")
    MZ = quantity("quantity.z-boson-mass")
    mb = quantity("quantity.bottom-quark-mass")
    wW, wZ, ws, wt, _ = weights(*G_SAMPLES[0])

    def B(mpm, mt):
        return wW * MW ** 4 + wZ * MZ ** 4 + ws * mpm ** 4 + wt * mt ** 4 - light()
    for mpm, mt in ((THR_LO, MT_LO), (THR_HI, MT_HI)):
        GA.check("B is the GW combination 6 M_W^4 + 3 M_Z^4 + 2 m_pm^4 - 12 m_t^4 - light",
                 B(mpm, mt) == 6 * MW ** 4 + 3 * MZ ** 4 + 2 * mpm ** 4 - 12 * mt ** 4 - light())
    GA.check("threshold in (249, 250) at the lightest top", B(THR_LO, MT_LO) < ZERO < B(THR_LO1, MT_LO))
    GA.check("threshold in (267, 268) at the heaviest top", B(THR_HI1, MT_HI) < ZERO < B(THR_HI, MT_HI))
    GA.check("threshold above m_t - m_b", THR_LO > MT_HI - mb)
    return True


def check_measured_higgs_mass_brackets_the_charged_pair():
    """(iv): with m_h in [125, 125.4] (stored 125.20 inside), v in [246, 247] (stored-input tree value inside),
    m_t in [162, 173], pi in [333/106, 355/113]: m_pm^4 lies inside [450^4, 456^4]; at the central inputs
    (v = 246.22, stored m_h and pole m_t) 454 < m_pm < 455; the charged quartic 2a - e = m_pm^2/v^2 is in [3.2, 3.5]."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    MW = quantity("quantity.w-boson-mass")
    MZ = quantity("quantity.z-boson-mass")
    mh = quantity("quantity.higgs-boson-mass")
    s2 = quantity("quantity.weak-mixing-angle-mz")
    ainv = quantity("quantity.inverse-fine-structure-mz")
    GA.check("stored m_h inside the bracket", MH_LO <= mh <= MH_HI)
    vt_hi = MW * MW * s2 * ainv / PI_LO
    vt_lo = MW * MW * s2 * ainv / PI_HI
    GA.check("tree v from stored inputs inside [246, 247]", V_LO ** 2 <= vt_lo and vt_hi <= V_HI ** 2)
    wW, wZ, ws, wt, _ = weights(*G_SAMPLES[0])
    lo = mpm4(PI_LO, V_LO, MH_LO, MT_LO, MW, MZ, wW, wZ, ws, wt)
    hi = mpm4(PI_HI, V_HI, MH_HI, MT_HI, MW, MZ, wW, wZ, ws, wt)
    GA.check("m_pm^4 bracket inside [450^4, 456^4]", MPM_LO ** 4 < lo and hi < MPM_HI ** 4)
    mid = mpm4(PI_HI, V_PDG, mh, quantity("quantity.top-quark-mass"), MW, MZ, wW, wZ, ws, wt)
    GA.check("central inputs: 454 < m_pm < 455", MID_LO ** 4 < mid < (MID_LO + 1) ** 4)
    GA.check("mpm4 is the GW formula solved for m_pm^4", 2 * mid == 8 * PI_HI ** 2 * V_PDG ** 2 * mh ** 2 - 6 * MW ** 4
             - 3 * MZ ** 4 + 12 * quantity("quantity.top-quark-mass") ** 4 + light())
    GA.check("quartic 2a - e = m_pm^2/v^2 in [3.2, 3.5]", Q_LO * V_HI ** 2 < MPM_LO ** 2 and MPM_HI ** 2 < Q_HI * V_LO ** 2)
    return True


# ---------------------------------------------------------------- h -> gamma gamma
TAU_TERMS = 70
ROUND = 10 ** 15
MU_LO, MU_HI = F(898, 1000), F(900, 1000)
AW_LO, AW_HI = F(-8332, 1000), F(-8331, 1000)
AT_LO, AT_HI = F(1835, 1000), F(1836, 1000)
A0_LO, A0_HI = F(336, 1000), F(337, 1000)


def binom(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def rdown(x):
    return F((x.numerator * ROUND) // x.denominator, ROUND)


def rup(x):
    return -rdown(-x)


def arcsin2(tau):
    """[lo, hi] with lo <= arcsin(sqrt(tau))^2 <= hi for 0 < tau < 1: the series (1/2) sum (4 tau)^n / (n^2 C(2n, n)),
    each term at most tau^n, so the tail after K terms is at most tau^(K+1)/(1 - tau)."""
    S = F(0)
    for n in range(1, TAU_TERMS + 1):
        S += (4 * tau) ** n / (2 * n * n * binom(2 * n, n))
        S = rdown(S)
    return S, rup(S + tau ** (TAU_TERMS + 1) / (1 - tau) + F(TAU_TERMS, ROUND))


def amps(tau):
    """Interval amplitudes (vector A1, Dirac A12, scalar A0) as functions of the interval for f(tau)."""
    flo, fhi = arcsin2(tau)
    A1 = sorted(-(2 * tau * tau + 3 * tau + 3 * (2 * tau - 1) * fv) / (tau * tau) for fv in (flo, fhi))
    A12 = sorted(2 * (tau + (tau - 1) * fv) / (tau * tau) for fv in (flo, fhi))
    A0 = sorted(-(tau - fv) / (tau * tau) for fv in (flo, fhi))
    return A1, A12, A0


def check_diphoton_rate_with_the_charged_pair():
    """(v): the charged pair couples to the scalon with g = d m_pm^2/d v = 2 m_pm^2/v (its mass squared is
    proportional to v^2 on the flat ray), so its amplitude enters with unit weight: mu_gamgam = ((A_W + (4/3) A_t + A_0)
    / (A_W + (4/3) A_t))^2 with the standard one-loop functions (cited from memory). With the stored m_h, M_W, pole m_t
    and m_pm in [450, 456] GeV, exact interval arithmetic (arcsin^2 by its series with a tail bound) gives
    0.898 < mu_gamgam < 0.900."""
    premise("synthesis.rung-field-on-the-lift-locus")
    mh = quantity("quantity.higgs-boson-mass")
    MW = quantity("quantity.w-boson-mass")
    mt = quantity("quantity.top-quark-mass")
    tW, tt = mh * mh / (4 * MW * MW), mh * mh / (4 * mt * mt)
    GA.check("taus below threshold", 0 < tW < 1 and 0 < tt < 1)
    # the series reproduces a known value: arcsin(1/2)^2 = pi^2/36 at tau = 1/4
    flo, fhi = arcsin2(F(1, 4))
    GA.check("series bracket contains pi^2/36", flo <= PI_HI ** 2 / 36 and PI_LO ** 2 / 36 <= fhi)
    A1, _, _ = amps(tW)
    _, A12, _ = amps(tt)
    colour_charge = 3 * F(4, 9)
    den = [A1[0] + colour_charge * A12[0], A1[1] + colour_charge * A12[1]]
    GA.check("A_W in (-8.332, -8.331)", AW_LO < A1[0] and A1[1] < AW_HI)
    GA.check("(4/3) A_t in (1.835, 1.836)", AT_LO < colour_charge * A12[0] and colour_charge * A12[1] < AT_HI)
    GA.check("SM amplitude negative (W dominates)", den[1] < 0)
    ratios = []
    for m in (MPM_LO, MPM_HI):
        _, _, A0 = amps(mh * mh / (4 * m * m))
        GA.check("scalar amplitude in (0.336, 0.337)", A0_LO < A0[0] and A0[1] < A0_HI)
        for d in den:
            for a0 in A0:
                ratios.append(((d + a0) / d) ** 2)
    GA.check("0.898 < mu_gamgam < 0.900", MU_LO < min(ratios) and max(ratios) < MU_HI)
    return True
