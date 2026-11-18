"""Heating coefficients across curvature couplings and on the chain's bath: exact checks.

The coefficient of the pair-production theorem's clause (v), summed over a produced light content D with
spin-two sum C_D = n_s + 3 n_w + 12 n_v and trace sum tau_D, from a bath (N_s, N_w, N_v) with trace sum tau_B:
    c / pi^3 = (1/17280) [ (C_D (N_s + 12 N_v) + 5 tau_D tau_B)/225 + 49 C_D N_w/4800 ],  tau = (1 - 6 xi)^2.
pi is never a decimal: 103993/33102 < pi < 355/113 (two convergents of its continued fraction), each used at the end that weakens the statement tested.
Fourth roots are never taken: a margin m = (c*/c)^(1/4) is tested as c* against m^4 c.

(1) Scalars to scalars with two different couplings, directly in the spacetime algebra Cl(1,3): the weight is
    (pi/180)(1 + 5 tau_1 tau_2) (exact integration of a quartic in the cosine through five rational angles).
(2) The Standard Model's content from the Standard Model's bath: 1519247/82944000 at coupling 0, lower by
    16/777600 (5120/4557741 of itself) when either side is conformal; no stated figure moves.
(3) The tilt window on the doublets of bath and copies: ratio between 5.91 and 6.31; four copies cross the
    stored c* = 13.4949 at xi between 1.5239 and 1.5241; at central inputs c* is between 14.44 and 14.45 and
    is not reached. One further real scalar at the window's coupling.
(4) The chain's content between M_I and M_U, (N_s, 48, 21) with N_s = 64, 68, 188: per-vector ratio, the
    margins of the Pati-Salam clause at 22 vectors and at four contents, and for copies of the chain's own
    content the dependence on the scalars' coupling (N_s = 188: below c* only for xi between 0.022 and 0.311).
"""
from fractions import Fraction as F

import GA
from GA import add, dot, gen, scal
from tp_premise import premise

S = GA.sig(1, 3)
E = [gen(i) for i in range(4)]
REC = [E[0]] + [GA.neg(x) for x in E[1:]]

PI_LO, PI_HI = F(103993, 33102), F(355, 113)
SM_BATH = (4, 45, 12)                         # real scalars, chiral fermions, vectors
ODD_TOWER_VECTORS = 22
TILT_LO, TILT_HI = F(1522584375, 10 ** 9), F(1548079215, 10 ** 9)
CHAIN_FERMIONS, CHAIN_VECTORS = 48, 21
CHAIN_SCALARS = {64: (4, 60, 0), 68: (8, 60, 0), 188: (8, 60, 120)}     # bidoublet, (10,1,3), (15,2,2)
CHAIN_B_MINIMAL = {64: 28, 68: 32, 188: 152}                             # stored -36 + N_s
CHAIN_M_I = 19 * 10 ** 9                      # GeV, the chain with the (15,2,2) at two loops (stored)
CHAIN_M_U_LEAST = 11 * 10 ** 15               # GeV, the least of the stored unification scales
CEILING = 6 * 10 ** 14                        # GeV, the ceiling reheating (stored)
ANGLES = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(-7, 25), F(24, 25)), (F(-8, 17), F(15, 17)),
          (F(20, 29), F(21, 29))]
COUPLING_PAIRS = [(F(0), F(0)), (F(0), F(1, 6)), (F(1, 6), F(1, 6)), (F(0), F(153, 100)),
                  (F(153, 100), F(153, 100)), (F(-1, 3), F(2, 7)), (TILT_LO, TILT_HI)]


def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x}


def d(a, b):
    return dot(a, b, S)


def floor(x):
    return x.numerator // x.denominator


def tau(xi):
    return (1 - 6 * xi) ** 2


def coeff(CD, tauD, bath, tauB):
    """c / pi^3 for a produced content (spin-two sum CD, trace sum tauD) from a bath with trace sum tauB."""
    Ns, Nw, Nv = bath
    return (F(CD * (Ns + 12 * Nv) + 5 * tauD * tauB, 225) + F(49 * CD * Nw, 4800)) / 17280


def spin_two_sum(content):
    ns, nw, nv = content
    return ns + 3 * nw + 12 * nv


def c_star(rem, eta, kappa, vR, pi):
    """The stored threshold of the Pati-Salam clause (i): A / (2 M_3^4), M_3 = 4 pi v_R."""
    MP = F(2435, 1000) * F(10) ** 18
    A = 3 * kappa * MP ** 3 * rem * F(938272, 10 ** 6) * eta
    return A / (2 * (4 * pi * vR) ** 4)


def stored_c_star():
    E10 = F(10)
    return c_star(F(4364, 1000) - F(65, 1000), F(865, 100) / E10 ** 11, F(1453, 10), F(425, 100) * E10 ** 10, PI_HI)


# ---- (1) --------------------------------------------------------------------------------------------------
def scalar_source(p, q, xi):
    k = add(p, q)
    k2 = d(k, k)
    return lambda a: add(scal(-d(a, q), p), scal(-d(a, p), q), scal(d(p, q), a),
                         scal(2 * xi * d(a, k), k), scal(-2 * xi * k2, a))


def bilinear(T1, T2):
    ip = sum(d(T1(E[a]), T2(REC[a])) for a in range(4))
    t1 = sum(d(REC[a], T1(E[a])) for a in range(4))
    t2 = sum(d(REC[a], T2(E[a])) for a in range(4))
    return ip - F(1, 2) * t1 * t2


def quartic_integral(vals):
    n = len(vals)
    M = [[c ** k for k in range(n)] for c, _ in vals]
    rhs = [v for _, v in vals]
    for i in range(n):
        piv = next(r for r in range(i, n) if M[r][i] != 0)
        M[i], M[piv] = M[piv], M[i]
        rhs[i], rhs[piv] = rhs[piv], rhs[i]
        for r in range(n):
            if r != i and M[r][i] != 0:
                f = M[r][i] / M[i][i]
                M[r] = [a - f * b for a, b in zip(M[r], M[i])]
                rhs[r] -= f * rhs[i]
    co = [rhs[i] / M[i][i] for i in range(n)]
    return sum(co[k] * F(2, k + 1) for k in range(0, n, 2))


def check_scalar_channel_weight_at_unequal_couplings():
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    ok = True
    p1, p2 = vec([1, 0, 0, 1]), vec([1, 0, 0, -1])
    s = d(add(p1, p2), add(p1, p2))
    ok = ok and s == 4
    for x1, x2 in COUPLING_PAIRS:
        vals = []
        for c, s_ in ANGLES:
            p3, p4 = vec([1, s_, 0, c]), vec([1, -s_, 0, -c])
            b = bilinear(scalar_source(p1, p2, x1), scalar_source(p3, p4, x2))
            # the stored bracket: spin-two part and trace part
            ok = ok and b == s * s / 4 * (c * c - F(1, 3)) - s * s / 6 * (1 - 6 * x1) * (1 - 6 * x2)
            vals.append((c, b ** 2 / s ** 4))
        W = quartic_integral(vals) * 2 * F(1, 4)        # over pi: azimuth 2 pi, one half per identical pair
        ok = ok and W == (1 + 5 * tau(x1) * tau(x2)) / 180
    ok = ok and tau(F(0)) == 1 and tau(F(1, 6)) == 0
    GA.check("scalars to scalars with couplings xi_1, xi_2: weight (pi/180)(1 + 5 tau_1 tau_2) at seven pairs", ok)
    return ok


# ---- (2) --------------------------------------------------------------------------------------------------
def check_stored_readings_move_no_stated_figure():
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    premise("synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt")
    ok = True
    CSM = spin_two_sum(SM_BATH)
    ok = ok and CSM == 283
    # the composite coefficient is the sum of the theorem's coefficients over the produced species
    per = (4 * coeff(1, 1, SM_BATH, 4) + 45 * coeff(3, 0, SM_BATH, 4) + 12 * coeff(12, 0, SM_BATH, 4))
    stored = coeff(CSM, 4, SM_BATH, 4)
    ok = ok and per == stored == F(1519247, 82944000)
    ok = ok and coeff(1, 1, SM_BATH, 4) == F(5789, 82944000) and coeff(12, 0, SM_BATH, 4) == F(16087, 20736000)
    # conformal on either side or both: one value, lower by 16/777600
    conf = [coeff(CSM, 0, SM_BATH, 4), coeff(CSM, 4, SM_BATH, 0), coeff(CSM, 0, SM_BATH, 0)]
    ok = ok and len(set(conf)) == 1 and stored - conf[0] == F(16, 777600)
    ok = ok and (stored - conf[0]) / stored == F(5120, 4557741)
    # stated figures: c in (0.5672, 0.5673) against (0.5679, 0.5680); both round to 0.57, both below 1
    ok = ok and F(5679, 10 ** 4) < stored * PI_LO ** 3 < stored * PI_HI ** 3 < F(568, 10 ** 3)
    ok = ok and F(5672, 10 ** 4) < conf[0] * PI_LO ** 3 < conf[0] * PI_HI ** 3 < F(5673, 10 ** 4)
    # the floor goes as c^(1/4): the ratio of fourth powers is within 0.12 percent, so the floor within 0.03 percent
    ok = ok and F(9997, 10 ** 4) ** 4 < conf[0] / stored < 1
    # the Pati-Salam margins 2.2 and 1.5 and the count 23: unchanged
    cs = stored_c_star()
    ok = ok and floor(cs * 10 ** 4) == 134949
    for val in (stored, conf[0]):
        ok = ok and cs > F(156, 100) ** 4 * 4 * val * PI_HI ** 3
        ok = ok and floor(cs / (val * PI_HI ** 3)) == floor(cs / (val * PI_LO ** 3)) == 23
    # a produced vector or fermion does not see any coupling
    for tB in (0, 4, 4 * tau(TILT_HI)):
        ok = ok and coeff(12, 0, SM_BATH, tB) == F(16087, 20736000) and coeff(3, 0, SM_BATH, tB) == F(16087, 82944000)
    # one produced real scalar: conformal is lower by 4/777600 (7.4 percent)
    ok = ok and coeff(1, 1, SM_BATH, 4) - coeff(1, 0, SM_BATH, 4) == F(4, 777600)
    ok = ok and F(926, 1000) < coeff(1, 0, SM_BATH, 4) / coeff(1, 1, SM_BATH, 4) < F(927, 1000)
    GA.check("Standard-Model content from its own bath: 1519247 pi^3/82944000 at coupling 0, lower by "
             "5120/4557741 of itself at the conformal value; margins 1.5 and the count 23 unchanged", ok)
    return ok


# ---- (3) --------------------------------------------------------------------------------------------------
def check_tilt_window_on_the_doublets_uses_up_the_margin():
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    premise("synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point")
    premise("synthesis.seeding-remainder-excludes-perturbative-pati-salam")
    ok = True
    CSM = spin_two_sum(SM_BATH)
    stored = coeff(CSM, 4, SM_BATH, 4)
    tl, th = tau(TILT_LO), tau(TILT_HI)
    ok = ok and F(6618, 100) < tl < F(6619, 100) and F(6869, 100) < th < F(6870, 100)
    lo, hi = coeff(CSM, 4 * tl, SM_BATH, 4 * tl), coeff(CSM, 4 * th, SM_BATH, 4 * th)
    ok = ok and F(591, 100) < lo / stored < F(592, 100) and F(630, 100) < hi / stored < F(631, 100)
    ok = ok and F(3362, 1000) < lo * PI_LO ** 3 < lo * PI_HI ** 3 < F(3363, 1000)
    ok = ok and F(3578, 1000) < hi * PI_LO ** 3 < hi * PI_HI ** 3 < F(3579, 1000)
    # four copies against the stored c* (inputs at the weakening ends): below at the lower end, above at the upper
    cs = stored_c_star()
    ok = ok and floor(cs * 10 ** 4) == 134949
    ok = ok and 4 * lo * PI_HI ** 3 < cs < 4 * hi * PI_LO ** 3
    ok = ok and F(13448, 1000) < 4 * lo * PI_LO ** 3 and 4 * hi * PI_HI ** 3 < F(14314, 1000)
    # the crossing lies between xi = 1.5239 and 1.5241
    xa, xb = F(15239, 10 ** 4), F(15241, 10 ** 4)
    ok = ok and TILT_LO < xa < xb < TILT_HI
    ok = ok and 4 * coeff(CSM, 4 * tau(xa), SM_BATH, 4 * tau(xa)) * PI_HI ** 3 < cs
    ok = ok and 4 * coeff(CSM, 4 * tau(xb), SM_BATH, 4 * tau(xb)) * PI_LO ** 3 > cs
    # the stored margin 1.5 is gone on both sides: (c*/c)^(1/4) between 0.98 and 1.01
    ok = ok and F(98, 100) ** 4 * 4 * hi * PI_HI ** 3 < cs < F(101, 100) ** 4 * 4 * lo * PI_LO ** 3
    # at central inputs (remainder 4.364, 8.7e-11, 145.26, v_R = 4.2e10) c* is in (14.44, 14.45): not reached
    E10 = F(10)
    for pi in (PI_LO, PI_HI):
        cc = c_star(F(4364, 1000), F(87, 10) / E10 ** 11, F(14526, 100), F(42, 10) * E10 ** 10, pi)
        ok = ok and F(1444, 100) < cc < F(1445, 100)
        ok = ok and 4 * hi * PI_HI ** 3 < cc < F(102, 100) ** 4 * 4 * lo * PI_LO ** 3
    # the tilt coupling on the bath's doublets only (copies at 0): ratio between 1.07 and 1.08
    for t in (tl, th):
        ok = ok and F(107, 100) < coeff(CSM, 4, SM_BATH, 4 * t) / stored < F(108, 100)
    # one further real scalar at the window's coupling: in the bath only, in bath and copy, alone as a relic
    bath5 = (5, 45, 12)
    for t in (tl, th):
        ok = ok and F(102, 100) < coeff(CSM, 4, bath5, 4 + t) / stored < F(103, 100)
        ok = ok and F(135, 100) < coeff(CSM + 1, 4 + t, bath5, 4 + t) / stored < F(138, 100)
        alone = coeff(1, t, SM_BATH, 4)
        ok = ok and F(58, 10) < alone / coeff(1, 1, SM_BATH, 4) < F(60, 10)
        ok = ok and 2 * alone > coeff(12, 0, SM_BATH, 4) > alone           # between half a vector and one
    GA.check("tilt window on the doublets of bath and copies: ratio 5.91 to 6.31; four copies cross the stored "
             "c* = 13.4949 at xi in (1.5239, 1.5241); central c* in (14.44, 14.45) is not reached", ok)
    return ok


# ---- (4) --------------------------------------------------------------------------------------------------
def check_chain_bath_lowers_the_margins_and_its_scalars_decide_the_copies():
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    premise("synthesis.seeding-remainder-excludes-perturbative-pati-salam")
    premise("synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off")
    premise("standard-model.chain")
    ok = True
    cs = stored_c_star()
    CSM = spin_two_sum(SM_BATH)
    rv0 = coeff(12, 0, SM_BATH, 0)
    # the temperatures concerned lie between M_I and M_U: the clause's largest M_3 = 4 pi v_R, and the ceiling
    M3_cap = 4 * PI_HI * F(425, 100) * F(10) ** 10
    ok = ok and floor(M3_cap / 10 ** 9) == 534 and CHAIN_M_I < M3_cap < CEILING < CHAIN_M_U_LEAST
    ok = ok and floor(M3_cap / CHAIN_M_I) == 28
    expect = {64: dict(ratio=(1695, 1696), vec=(897, 898), mvec=(196, 197), msm=(136, 137), own0=(118, 119), ownc=(121, 122)),
              68: dict(ratio=(1711, 1712), vec=(905, 906), mvec=(196, 197), msm=(136, 137), own0=(117, 118), ownc=(120, 121)),
              188: dict(ratio=(2189, 2190), vec=(1158, 1159), mvec=(184, 185), msm=(127, 128), own0=(95, 97), ownc=(107, 108))}
    for Ns, parts in CHAIN_SCALARS.items():
        ok = ok and sum(parts) == Ns and -36 + Ns == CHAIN_B_MINIMAL[Ns]
        bath = (Ns, CHAIN_FERMIONS, CHAIN_VECTORS)
        ex = expect[Ns]
        rv = coeff(12, 0, bath, Ns)
        ok = ok and rv == coeff(12, 0, bath, 0)                            # no coupling enters
        ok = ok and F(ex['ratio'][0], 1000) < rv / rv0 < F(ex['ratio'][1], 1000)
        c22_lo, c22_hi = ODD_TOWER_VECTORS * rv * PI_LO ** 3, ODD_TOWER_VECTORS * rv * PI_HI ** 3
        ok = ok and F(ex['vec'][0], 1000) < c22_lo < c22_hi < F(ex['vec'][1], 1000)
        # margin at the 22 vectors, in fourth powers: between the two ends, and below the stored 2.2
        ok = ok and F(ex['mvec'][0], 100) ** 4 * c22_hi < cs < F(ex['mvec'][1], 100) ** 4 * c22_lo
        ok = ok and cs < F(22, 10) ** 4 * c22_lo
        # four Standard-Model contents (their scalars at 0) from this bath, its scalars at 0: below the stored 1.5
        sm = 4 * coeff(CSM, 4, bath, Ns)
        ok = ok and F(ex['msm'][0], 100) ** 4 * sm * PI_HI ** 3 < cs < F(ex['msm'][1], 100) ** 4 * sm * PI_LO ** 3
        ok = ok and cs < F(15, 10) ** 4 * sm * PI_LO ** 3
        # four copies of the chain's own content: all scalars at 0, and all conformal
        C = Ns + 3 * CHAIN_FERMIONS + 12 * CHAIN_VECTORS
        own0, ownc = 4 * coeff(C, Ns, bath, Ns), 4 * coeff(C, 0, bath, 0)
        ok = ok and F(ex['own0'][0], 100) ** 4 * own0 * PI_HI ** 3 < cs < F(ex['own0'][1], 100) ** 4 * own0 * PI_LO ** 3
        ok = ok and F(ex['ownc'][0], 100) ** 4 * ownc * PI_HI ** 3 < cs < F(ex['ownc'][1], 100) ** 4 * ownc * PI_LO ** 3
    # N_s = 188: the copies exceed c* at coupling 0 and stay below it at the conformal value
    Ns = 188
    bath = (Ns, CHAIN_FERMIONS, CHAIN_VECTORS)
    C = Ns + 3 * CHAIN_FERMIONS + 12 * CHAIN_VECTORS
    ok = ok and C == 584

    def four(xi, pi):
        t = Ns * tau(xi)
        return 4 * coeff(C, t, bath, t) * pi ** 3
    ok = ok and four(F(0), PI_LO) > cs > four(F(1, 6), PI_HI)
    ok = ok and F(1588, 100) < four(F(0), PI_LO) < four(F(0), PI_HI) < F(1589, 100)
    ok = ok and F(1025, 100) < four(F(1, 6), PI_LO) < four(F(1, 6), PI_HI) < F(1026, 100)
    # the threshold c* counted in species at this bath: 256 vectors, 10 Standard-Model contents, and of the
    # chain's own content 3 copies at coupling 0 or 5 at the conformal value (four exceed it, or do not)
    rv = coeff(12, 0, bath, 0)
    ok = ok and floor(cs / (rv * PI_HI ** 3)) == floor(cs / (rv * PI_LO ** 3)) == 256
    sm1 = coeff(CSM, 4, bath, Ns)
    ok = ok and floor(cs / (sm1 * PI_HI ** 3)) == floor(cs / (sm1 * PI_LO ** 3)) == 10
    ok = ok and floor(4 * cs / four(F(0), PI_HI)) == floor(4 * cs / four(F(0), PI_LO)) == 3
    ok = ok and floor(4 * cs / four(F(1, 6), PI_HI)) == floor(4 * cs / four(F(1, 6), PI_LO)) == 5
    # below c* for xi in [0.022, 0.311], above it at 0.021 and at 0.313
    ok = ok and four(F(22, 1000), PI_HI) < cs and four(F(311, 1000), PI_HI) < cs
    ok = ok and four(F(21, 1000), PI_LO) > cs and four(F(313, 1000), PI_LO) > cs
    # N_s = 64 and 68: the copies stay below c* at coupling 0, and reach it only beyond xi = 0.46
    for Ns2 in (64, 68):
        b2 = (Ns2, CHAIN_FERMIONS, CHAIN_VECTORS)
        C2 = Ns2 + 3 * CHAIN_FERMIONS + 12 * CHAIN_VECTORS
        t = Ns2 * tau(F(46, 100))
        ok = ok and 4 * coeff(C2, t, b2, t) * PI_HI ** 3 < cs
        t = Ns2 * tau(F(48, 100))
        ok = ok and 4 * coeff(C2, t, b2, t) * PI_LO ** 3 > cs
    GA.check("chain bath (N_s, 48, 21), N_s = 64, 68, 188: per-vector ratio 1.70, 1.71, 2.19; margins at 22 "
             "vectors 1.96, 1.96, 1.84 and at four Standard-Model contents 1.36, 1.36, 1.27; four copies of "
             "the chain's content with N_s = 188 are below c* only for xi between 0.022 and 0.311", ok)
    return ok
