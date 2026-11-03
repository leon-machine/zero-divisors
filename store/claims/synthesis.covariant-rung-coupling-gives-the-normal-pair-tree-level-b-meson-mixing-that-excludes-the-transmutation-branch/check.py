"""The normal pair of the covariant rung coupling against neutral-meson mixing: exact checks.

Setting: the linear rung field at its vacuum alpha = 0, beta = (-lam, 0), lam = v, with the covariant coupling
Y c + Ytilde c* (M_d = beta Y + conj(alpha) Ytilde, M_u = alpha Y + conj(beta) Ytilde on the rung-4 components),
Y, Ytilde complex symmetric (the rung 10). The normal pair is the neutral alpha_4 direction (eight real components,
kinetic coefficient one, so alpha_4 = sqrt2 phi with phi canonical complex). In the down-quark mass basis its
coupling is -kappa phibar dbar_L A d_R + h.c. with kappa = sqrt2 / v and A = V^dag Mhat_u V^* (V the left mixing
U_u^dag U_d), so |A_jk| = |sum_i V_ij V_ik m_i| with CKM magnitudes and free relative phases.
Integrating out H and A (masses m_H, m_A; a = 1/m_H^2, b = 1/m_A^2) gives
L_eff = J^dag J (a + b)/2 + (J^2 + J^dag^2)(a - b)/4, J = kappa dbar_L A d_R.
Inputs (imported, ranges conservative): CKM magnitudes, running quark masses at the scalar mass, meson masses,
decay constants, bag parameters, measured mass differences. Exact rationals only.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

QI = GA.QI

# ---------------------------------------------------------------- imported inputs (rational intervals)
CKM = {  # (low, high) of |V_ij|, rows u c t, columns d s b
    ("u", "d"): (F(97), F(100)), ("u", "s"): (F(222, 1000), F(227, 1000)), ("u", "b"): (F(0), F(45, 10000)),
    ("c", "d"): (F(215, 1000), F(227, 1000)), ("c", "s"): (F(96, 100), F(99, 100)), ("c", "b"): (F(390, 10000), F(425, 10000)),
    ("t", "d"): (F(78, 10000), F(92, 10000)), ("t", "s"): (F(376, 10000), F(425, 10000)), ("t", "b"): (F(99, 100), F(1)),
}
CKM[("u", "d")] = (F(97, 100), F(1))
MQ = {"u": (F(0), F(2, 1000)), "c": (F(50, 100), F(70, 100)), "t": (F(140), F(172))}   # GeV, running at 100 to 600 GeV
MESON = {  # mass, f low, B4 low, B2 high, (m_q1 + m_q2) high at the hadronic scale, Delta M (GeV)
    "Bs": (F(536692, 100000), F(228, 1000), F(85, 100), F(95, 100), F(430, 100), F(17765, 1000) * F(6582119569, 10 ** 22)),
    "Bd": (F(527966, 100000), F(187, 1000), F(85, 100), F(95, 100), F(430, 100), F(5069, 10000) * F(6582119569, 10 ** 22)),
    "K": (F(497611, 1000000), F(1554, 10000), F(70, 100), F(95, 100), F(10, 100), F(3484, 1000) * F(1, 10 ** 15)),
}
M_UP = F(542)   # stored upper bound on m_H, m_A under (GW) and (D)


def cm(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), QI(0)) for j in range(n)] for i in range(n)]


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A))]


def tr_(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A))]


def cconj(A):
    return [[x.conj() for x in r] for r in A]


def inv3(A):
    n = 3
    M = [list(r) + [QI(1) if i == j else QI(0) for j in range(n)] for i, r in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != QI(0))
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != QI(0):
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [r[n:] for r in M]


def cayley(K):
    """Exact unitary (1 - K)(1 + K)^-1 from an anti-Hermitian Gaussian-rational K."""
    one = [[QI(1) if i == j else QI(0) for j in range(3)] for i in range(3)]
    P = [[one[i][j] - K[i][j] for j in range(3)] for i in range(3)]
    Mn = [[one[i][j] + K[i][j] for j in range(3)] for i in range(3)]
    return cm(P, inv3(Mn))


def antiherm(entries):
    (a, b, c, d, e, f, g, h, i) = entries
    K = [[QI(0, a), QI(b, c), QI(d, e)], [QI(-b, c), QI(0, f), QI(g, h)], [QI(-d, e), QI(-g, h), QI(0, i)]]
    return K


KU = (F(1, 3), F(1, 5), F(-1, 7), F(1, 9), F(2, 11), F(-1, 4), F(1, 6), F(1, 8), F(1, 10))
KD = (F(-1, 5), F(1, 7), F(1, 3), F(-1, 11), F(1, 4), F(1, 9), F(-1, 6), F(1, 12), F(-1, 2))
DU = (F(1, 500), F(13, 10), F(173))
DD = (F(1, 200), F(1, 10), F(21, 5))
LAM = F(246)
JTEST = [(QI(F(3, 2), F(-2, 5)), F(1, 7), F(1, 3)), (QI(F(-1, 3), F(4)), F(2), F(2)), (QI(F(5), F(1, 2)), F(1, 11), F(3, 4))]


def diag3(d):
    return [[QI(d[i]) if i == j else QI(0) for j in range(3)] for i in range(3)]


def check_normal_pair_couples_down_quarks_through_the_up_mass_matrix():
    """At alpha = 0 the coefficient of conj(alpha_4) in M_d is Ytilde = -M_u/lam; with symmetric Y, Ytilde and
    Takagi forms M_q = U_q Mhat_q U_q^T, in the down mass basis it is -V^dag Mhat_u V^* / lam (V = U_u^dag U_d),
    symmetric and not diagonal; the up quarks see -V Mhat_d V^T / lam."""
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.imported-takagi-factorisation")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    Uu = cayley(antiherm(KU))
    Ud = cayley(antiherm(KD))
    one = [[QI(1) if i == j else QI(0) for j in range(3)] for i in range(3)]
    GA.check("the Cayley transforms are unitary", cm(Uu, dag(Uu)) == one and cm(Ud, dag(Ud)) == one)
    Du = diag3(DU)
    Dd = diag3(DD)
    Mu = cm(cm(Uu, Du), tr_(Uu))
    Md = cm(cm(Ud, Dd), tr_(Ud))
    lam = LAM
    Y = [[-x / QI(lam) for x in r] for r in Md]       # M_d = beta Y at beta = -lam
    Yt = [[-x / QI(lam) for x in r] for r in Mu]      # M_u = conj(beta) Ytilde
    GA.check("Y and Ytilde are complex symmetric (the rung 10)", Y == tr_(Y) and Yt == tr_(Yt))
    # mass matrices from the stored formulas at alpha = 0, beta = -lam, and the alpha_4 coefficients
    beta = QI(-lam)
    GA.check("stored formulas reproduce the mass matrices at the vacuum",
             [[beta * x for x in r] for r in Y] == Md and [[beta.conj() * x for x in r] for r in Yt] == Mu)
    V = cm(dag(Uu), Ud)
    Ad = cm(cm(dag(Ud), Yt), cconj(Ud))     # coefficient of conj(alpha_4) in M_d, down mass basis
    want = cm(cm(dag(V), Du), cconj(V))
    GA.check("down-sector normal-pair coupling = -V^dag Mhat_u V^* / lam", Ad == [[-x / QI(lam) for x in r] for r in want])
    GA.check("it is symmetric and has nonzero off-diagonal entries", Ad == tr_(Ad) and all(Ad[i][j] != QI(0) for i in range(3) for j in range(3) if i != j))
    Au = cm(cm(dag(Uu), Y), cconj(Uu))      # coefficient of alpha_4 in M_u, up mass basis
    wantu = cm(cm(V, Dd), tr_(V))
    GA.check("up-sector normal-pair coupling = -V Mhat_d V^T / lam", Au == [[-x / QI(lam) for x in r] for r in wantu])


def check_integrating_out_the_normal_pair():
    """With phi = (H + iA)/sqrt2, sources K_H = (J + J^dag)/sqrt2, K_A = i(J^dag - J)/sqrt2:
    K_H^2/(2 m_H^2) + K_A^2/(2 m_A^2) = J^dag J (a + b)/2 + (J^2 + J^dag^2)(a - b)/4 (commuting test values)."""
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    ok = True
    for J, a, b in JTEST:
        Jd = J.conj()
        KH2 = (J + Jd) * (J + Jd) / 2
        KA2 = QI(0, 1) * (Jd - J) * QI(0, 1) * (Jd - J) / 2
        lhs = KH2 * QI(a / 2) + KA2 * QI(b / 2)
        rhs = Jd * J * QI((a + b) / 2) + (J * J + Jd * Jd) * QI((a - b) / 4)
        ok = ok and lhs == rhs
    GA.check("tree-level exchange of the normal pair: LR operator weight (a + b)/2, LL and RR weight (a - b)/4", ok)


def lower_abs_entry(j, k, dominant):
    """Lower bound on |sum_i V_ij V_ik m_i| over the ranges and all relative phases: the dominant term minus the rest."""
    lo = MQ[dominant][0] * CKM[(dominant, j)][0] * CKM[(dominant, k)][0]
    for i in ("u", "c", "t"):
        if i != dominant:
            lo -= MQ[i][1] * CKM[(i, j)][1] * CKM[(i, k)][1]
    return lo


def m12_lower(Aabs, meson, split_any):
    """Lower bound on |M12| (GeV) from the normal pair with both masses at most M_UP (vacuum insertion, eta = 1).
    E4 = (R/4 + 1/24) m f^2 B4, E2 = (5/24) R m f^2 B2; degenerate: kappa^2 |A|^2 E4 / M^2;
    any split: kappa^2 |A|^2 (E4 - E2) / M^2, valid when E4 > E2."""
    m, flo, b4, b2, mq, dm = MESON[meson]
    R = (m / mq) ** 2
    E4 = (R / 4 + F(1, 24)) * m * flo * flo * b4
    E2 = F(5, 24) * R * m * flo * flo * b2
    v = quantity("quantity.fermi-scale") + F(1)        # v <= 247.22 GeV, conservative
    kap2 = 2 / (v * v)
    E = (E4 - E2) if split_any else E4
    return kap2 * Aabs * Aabs * E / (M_UP * M_UP), E4, E2


def check_flavour_changing_entries_are_bounded_below():
    """|A_sb| >= m_t|V_ts||V_tb| - m_c|V_cs||V_cb| - m_u|V_us||V_ub| > 5.18 GeV; |A_db| > 1.07 GeV;
    |A_sd| >= m_c|V_cs||V_cd| - m_t|V_ts||V_td| - m_u|V_us||V_ud| > 0.035 GeV (over all phases and the ranges)."""
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.imported-b-meson-mixing-inputs-vacuum-insertion-lattice-and-tree-level-quark-mixing")
    sb = lower_abs_entry("s", "b", "t")
    db = lower_abs_entry("d", "b", "t")
    sd = lower_abs_entry("s", "d", "c")
    GA.check("|A_sb| bound = 5181905457/10^9 > 5.18 GeV", sb == F(5181905457, 10 ** 9) and 100 * sb > 518)
    GA.check("|A_db| bound = 4297271/4000000 > 1.07 GeV", db == F(4297271, 4000000) and 100 * db > 107)
    GA.check("|A_sd| bound = 17747/500000 > 0.035 GeV", sd == F(17747, 500000) and 1000 * sd > 35)
    GA.check("the triangle bound is tight against the top term alone for sb (control: without the charm term it is larger)",
             MQ["t"][0] * CKM[("t", "s")][0] * CKM[("t", "b")][0] > sb)


SPLITS = [(F(1), F(1)), (F(1), F(1, 2)), (F(1), F(1, 10)), (F(3, 4), F(1, 5)), (F(1, 2), F(1, 2))]   # (a, b) in units of 1/M_UP^2


def split_bound(a, b, E4, E2):
    return (a + b) / 2 * E4 - abs(a - b) / 2 * E2


def check_tree_level_mixing_exceeds_the_measured_mass_differences():
    """For both normal-pair masses at most 542 GeV: the lower bound on |M12| is smallest at m_H = m_A = 542 GeV
    (for a >= b it is a(E4 - E2)/2 + b(E4 + E2)/2, increasing in a and b when E4 > E2), where it exceeds
    Delta M / 2 by more than 52 (Bs) and 50 (Bd); for the kaon (E4 < E2) only the degenerate case, more than 4."""
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.imported-b-meson-mixing-inputs-vacuum-insertion-lattice-and-tree-level-quark-mixing")
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    sb = lower_abs_entry("s", "b", "t")
    db = lower_abs_entry("d", "b", "t")
    sd = lower_abs_entry("s", "d", "c")
    out = {}
    for meson, A in (("Bs", sb), ("Bd", db), ("K", sd)):
        dm = MESON[meson][5]
        deg, E4, E2 = m12_lower(A, meson, False)
        out[meson] = (deg / (dm / 2), E4, E2)
    for meson in ("Bs", "Bd"):
        E4, E2 = out[meson][1], out[meson][2]
        GA.check(meson + ": E4 > E2, and the split bound at a, b >= 1 (units 1/542^2) is at least its value at a = b = 1",
                 E4 > E2 and all(split_bound(a, b, E4, E2) >= split_bound(F(1), F(1), E4, E2)
                                 for a, b in [(x + 1, y + 1) for x, y in SPLITS])
                 and split_bound(F(1), F(1), E4, E2) == E4)
        GA.check(meson + ": for a >= b the bound is a(E4 - E2)/2 + b(E4 + E2)/2",
                 all(split_bound(a, b, E4, E2) == a * (E4 - E2) / 2 + b * (E4 + E2) / 2 for a, b in SPLITS if a >= b))
    GA.check("Bs: excess > 52 for every split with both masses at most 542 GeV", out["Bs"][0] > 52)
    GA.check("Bd: excess > 50 for every split with both masses at most 542 GeV", out["Bd"][0] > 50)
    GA.check("K: degenerate excess > 4; for the kaon E4 < E2 (a split can cancel)", out["K"][0] > 4 and not out["K"][1] > out["K"][2])
    deg, _, _ = m12_lower(db, "Bd", False)
    GA.check("control: rescaled to 3 TeV the Bd lower bound falls below 2 Delta M_d / 2", deg * M_UP ** 2 / F(3000) ** 2 < 2 * MESON["Bd"][5] / 2)


if __name__ == "__main__":
    for fn in [check_normal_pair_couples_down_quarks_through_the_up_mass_matrix, check_integrating_out_the_normal_pair,
               check_flavour_changing_entries_are_bounded_below, check_tree_level_mixing_exceeds_the_measured_mass_differences]:
        fn()
    print("FAILURES:", GA.FAILURES)
