"""synthesis.supersymmetric-splits-two-loops: exact checks.

Everything here is exact (Fractions). The record-level numbers of clauses (iii) to (v) come from a
numerical integration of the two-loop equations; they are stated in the proof text as computed
numerically and reproducible, and are not part of this check.

check_coefficients: the generic two-loop matrix of Fact standard-model.imported-two-loop-gauge-coefficients
  rebuilt from component listings (Standard Model and minimal supersymmetric matrices reproduced), the
  calibration of the Yukawa trace term (top coefficients; generic formula plus gaugino-matter Yukawas
  equals the superfield matrix), the gaugino-Higgs-higgsino coefficients, the middle-regime matrices of
  the four splits, and the exact one-loop lines (endpoints of (d), misses of (a) to (c), common diagonal).
check_decision: clause (ii). With M_I = M_I' every split runs exactly the coefficients of the one-threshold
  supersymmetric row in every regime, so the stored row's admissible point is a point of every split;
  it lies in the triangle and meets the proton condition (exact rational comparison of the stated values).
"""
import GA
from GA import mat_eq
from tp_premise import premise
from fractions import Fraction as F

CG = (F(0), F(2), F(3))          # C(G) for U(1), SU(2), SU(3)
DG = (1, 3, 8)                    # dimensions of the gauge groups
SU3 = {1: (1, F(0), F(0)), 3: (3, F(1, 2), F(4, 3)), 8: (8, F(3), F(3))}
SU2 = {1: (1, F(0), F(0)), 2: (2, F(1, 2), F(3, 4)), 3: (3, F(2), F(2))}


def field(r3, r2, Y, mult=1):
    d3, t3, c3 = SU3[r3]
    d2, t2, c2 = SU2[r2]
    Y = F(Y)
    dim = d3 * d2
    T = (F(3, 5) * Y * Y * dim * mult, t2 * d3 * mult, t3 * d2 * mult)   # weighted indices
    C = (F(3, 5) * Y * Y, c2, c3)                                        # Casimirs
    return {"T": T, "C": C, "dim": dim * mult}


def gen_fields():
    return [field(3, 2, F(1, 6)), field(3, 1, F(-2, 3)), field(3, 1, F(1, 3)),
            field(1, 2, F(-1, 2)), field(1, 1, F(1))]


SMF = [f for _ in range(3) for f in gen_fields()]       # SM Weyl fermions, 3 generations
H = field(1, 2, F(1, 2))                                 # one complex Higgs doublet
GLUINO, WINO, BINO = field(8, 1, 0), field(1, 3, 0), field(1, 1, 0)
HIGGSINOS = [field(1, 2, F(1, 2)), field(1, 2, F(-1, 2))]
H2 = field(1, 2, F(1, 2))                                # second complex doublet
SFERMIONS = SMF                                          # scalar copies of the SM fermions


def b_gen(weyl, scal):
    return tuple(-F(11, 3) * CG[i] + F(2, 3) * sum(f["T"][i] for f in weyl)
                 + F(1, 3) * sum(s["T"][i] for s in scal) for i in range(3))


def B_gen(weyl, scal):
    B = [[F(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            v = F(0)
            if i == j:
                v += -F(34, 3) * CG[i] ** 2 + F(10, 3) * CG[i] * sum(f["T"][i] for f in weyl) \
                     + F(2, 3) * CG[i] * sum(s["T"][i] for s in scal)
            v += 2 * sum(f["T"][i] * f["C"][j] for f in weyl) + 4 * sum(s["T"][i] * s["C"][j] for s in scal)
            B[i][j] = v
    return B


def B_susy(chiral):
    b = tuple(-3 * CG[i] + sum(p["T"][i] for p in chiral) for i in range(3))
    B = [[(-6 * CG[i] ** 2 + 2 * CG[i] * sum(p["T"][i] for p in chiral) if i == j else F(0))
          + 4 * sum(p["T"][i] * p["C"][j] for p in chiral) for j in range(3)] for i in range(3)]
    return b, B


# ---------- Yukawa traces from explicit components -----------------------------------------
# A Yukawa monomial c * phi * psi_A * psi_B (phi a complex scalar component or its conjugate)
# contributes |c|^2 to (Y Y+)_{AA} and to (Y Y+)_{BB} after summing the two real components of
# phi (each carries |c|^2/2).  Fermion components carry Casimirs (C1, C2, C3).

def yuk_trace(monomials, cas):
    """monomials: list of (|c|^2 as Fraction-valued dict over coupling symbols, A, B).
    cas: dict component -> (C1,C2,C3). Returns per group i a dict symbol -> coefficient."""
    out = [dict(), dict(), dict()]
    for c2, A, B in monomials:
        for comp in (A, B):
            for i in range(3):
                for sym, v in c2.items():
                    out[i][sym] = out[i].get(sym, F(0)) + cas[comp][i] * v
    return [{s: v / DG[i] for s, v in out[i].items()} for i in range(3)]


def pauli():
    # entries as (re, im) Fractions; we need |entry|^2 only
    s1 = [[0, 1], [1, 0]]
    s2 = [[0, 1], [1, 0]]          # |(-i, i)| pattern has the same moduli as s1
    s3 = [[1, 0], [0, 1]]          # |diag(1,-1)|
    return [s1, s2, s3]


def top_yukawa_monomials():
    """y_t Q_{alpha i} eps^{ij} H_j u^c_alpha. Components: Q(alpha,i), U(alpha)."""
    mons, cas = [], {}
    for a in range(3):
        cas[("U", a)] = (F(3, 5) * F(4, 9), F(0), F(4, 3))
        for i in range(2):
            cas[("Q", a, i)] = (F(3, 5) * F(1, 36), F(3, 4), F(4, 3))
            mons.append(({"yt2": F(1)}, ("Q", a, i), ("U", a)))   # eps has unit moduli
    return mons, cas


def gaugino_higgs_monomials(with_gluino=False):
    """Giudice-Romanino split-SUSY couplings:
       -(H^+/sqrt2)(gu sigma^a W^a + gpu B) Hu - (H^T i s2/sqrt2)(-gd sigma^a W^a + gpd B) Hd + h.c.
    |coefficient|^2 = g^2 |sigma^a_kl|^2 / 2 per scalar component; two real components per
    complex component give back |.|^2 * 1 -> we record (g^2/2)*2/2 ... done explicitly:
    each complex scalar component contributes |c|^2 (c = g sigma/sqrt2), i.e. g^2|sigma|^2/2."""
    mons, cas = [], {}
    for a in range(3):
        cas[("W", a)] = (F(0), F(2), F(0))
    cas[("B",)] = (F(0), F(0), F(0))
    for hs in ("Hu", "Hd"):
        for l in range(2):
            cas[(hs, l)] = (F(3, 5) * F(1, 4), F(3, 4), F(0))
    P = pauli()
    for hs, gw, gb in (("Hu", "gu2", "gpu2"), ("Hd", "gd2", "gpd2")):
        for l in range(2):
            for k in range(2):          # scalar component H_k (or eps-rotated: same moduli)
                for a in range(3):
                    m = P[a][k][l]
                    if m:
                        mons.append(({gw: F(1, 2)}, ("W", a), (hs, l)))
                if k == l:
                    mons.append(({gb: F(1, 2)}, ("B",), (hs, l)))
    if with_gluino:
        for a in range(8):
            cas[("G", a)] = (F(0), F(0), F(3))      # gluino has no Higgs-higgsino coupling
    return mons, cas


def gaugino_matter_Y4(chiral):
    """Y4_ij from sqrt2 g_j phi^* T^a psi lambda^a, computed by the trace identity
    sum_m |T^a_mn|^2 = (T^a T^a)_nn: psi_n gets 2 g_j^2 C_j(R), lambda_j^a gets 2 g_j^2 T_j(R)/d(G_j)*..."""
    Y = [[F(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            v = F(0)
            for p in chiral:
                v += 2 * p["dim"] * p["C"][i] * p["C"][j] / DG[i]       # matter fermions
                if i == j:
                    v += 2 * CG[i] * p["T"][i]                          # gauginos (C(G_i) * 2 g^2 T_i d(G)/d(G))
            Y[i][j] = v
    return Y


def mat(Ms):
    return [[F(x) for x in r] for r in Ms]


B_SM_STORE = mat([[F(199, 50), F(27, 10), F(44, 5)], [F(9, 10), F(35, 6), 12], [F(11, 10), F(9, 2), -26]])
B_MSSM_STORE = mat([[F(199, 25), F(27, 5), F(88, 5)], [F(9, 5), 25, 24], [F(11, 5), 9, 14]])


def checks():
    # 1. SM
    assert b_gen(SMF, [H]) == (F(41, 10), F(-19, 6), F(-7))
    assert B_gen(SMF, [H]) == B_SM_STORE
    # 2. top Yukawa calibration
    mons, cas = top_yukawa_monomials()
    yt = yuk_trace(mons, cas)
    assert [d["yt2"] for d in yt] == [F(17, 10), F(3, 2), F(2)]
    # 3. MSSM: superfield formula = store; generic + gaugino-matter Yukawas = superfield
    chiral = SMF + [field(1, 2, F(1, 2)), field(1, 2, F(-1, 2))]
    bS, BS = B_susy(chiral)
    assert bS == (F(33, 5), F(1), F(-3)) and BS == B_MSSM_STORE
    weyl = SMF + HIGGSINOS + [GLUINO, WINO, BINO]
    scal = SFERMIONS + [H, H2]
    assert b_gen(weyl, scal) == bS
    Bg = B_gen(weyl, scal)
    Y4 = gaugino_matter_Y4(chiral)
    assert [[Bg[i][j] - Y4[i][j] for j in range(3)] for i in range(3)] == BS
    assert Bg != BS            # the generic formula alone does not return the SUSY matrix
    # 4. gaugino-Higgs-higgsino Yukawa coefficients (split SUSY), from components
    mons, cas = gaugino_higgs_monomials()
    d = yuk_trace(mons, cas)
    dW = tuple(d[i].get("gu2", F(0)) for i in range(3))
    dWd = tuple(d[i].get("gd2", F(0)) for i in range(3))
    dB = tuple(d[i].get("gpu2", F(0)) for i in range(3))
    assert dW == dWd == (F(9, 20), F(11, 4), F(0))
    assert dB == (F(3, 20), F(1, 4), F(0))
    return dW, dB


SPLITS = {
    # name: (light Weyl, light scalars, heavy Weyl, heavy scalars, gaugino-Higgs Yukawas below heavy)
    "a": ([GLUINO, WINO, BINO] + HIGGSINOS, [], [], SFERMIONS + [H2], True),
    "b": (HIGGSINOS, [], [GLUINO, WINO, BINO], SFERMIONS + [H2], False),
    "c": (HIGGSINOS, [H2], [GLUINO, WINO, BINO], SFERMIONS, False),
    "d": ([WINO, BINO] + HIGGSINOS, [], [GLUINO], SFERMIONS + [H2], True),
}


def regimes(split, dW, dB, ytilde_scale=F(1)):
    """(b, B, c) for: below M_I (SM), between (SM + light), above M_I' (MSSM).
    Gaugino Yukawas in the middle regime are absorbed into B by gu^2+gd^2 = g2^2 and
    gpu^2+gpd^2 = (3/5) g1^2 (tree matching, tracking approximation; scaled by ytilde_scale)."""
    lw, ls, hw, hs, gy = SPLITS[split]
    bSM, BSM = b_gen(SMF, [H]), B_gen(SMF, [H])
    bM, BM = b_gen(SMF + lw, [H] + ls), B_gen(SMF + lw, [H] + ls)
    if gy:
        for i in range(3):
            BM[i][1] -= ytilde_scale * dW[i]
            BM[i][0] -= ytilde_scale * F(3, 5) * dB[i]
    chiral = SMF + HIGGSINOS[:1] + HIGGSINOS[1:]
    bS, BS = B_susy(SMF + [field(1, 2, F(1, 2)), field(1, 2, F(-1, 2))])
    cSM = (F(17, 10), F(3, 2), F(2))
    cS = (F(26, 5), F(6), F(4))
    return [(bSM, BSM, cSM), (bM, BM, cSM), (bS, BS, cS)]






DW, DB = (F(9, 20), F(11, 4), F(0)), (F(3, 20), F(1, 4), F(0))
FULL = (F(5, 2), F(25, 6), F(4))
LIGHT = {"a": (F(2, 5), F(2), F(2)), "b": (F(2, 5), F(2, 3), F(0)),
         "c": (F(1, 2), F(5, 6), F(0)), "d": (F(2, 5), F(2), F(0))}


def one_loop_line(Dl, Dh, R, b):
    b12, b23 = b[0] - b[1], b[1] - b[2]
    A = (Dl[0] - Dl[1]) - R * (Dl[1] - Dl[2])
    Bc = (Dh[0] - Dh[1]) - R * (Dh[1] - Dh[2])
    return A, Bc, R * b23 - b12


def check_coefficients():
    premise("standard-model.imported-two-loop-gauge-coefficients")
    premise("standard-model.imported-coefficient-sum-indices")
    premise("standard-model.table-exact")
    premise("standard-model.four-supersymmetric-splits")
    premise("standard-model.two-threshold-criterion")
    premise("standard-model.spectrum-run")
    dW, dB = checks()                     # SM, MSSM, top calibration, generic + Y4 = superfield
    assert (dW, dB) == (DW, DB)
    expect_mid = {
        "a": (F(9, 2), F(-7, 6), F(-5)), "b": (F(9, 2), F(-5, 2), F(-7)),
        "c": (F(23, 5), F(-7, 3), F(-7)), "d": (F(9, 2), F(-7, 6), F(-7))}
    expect_B = {   # generic formula, gaugino Yukawas off (the Fact's formula as quoted)
        "a": [[F(104, 25), F(18, 5), F(44, 5)], [F(6, 5), F(106, 3), F(12)], [F(11, 10), F(9, 2), F(22)]],
        "b": [[F(104, 25), F(18, 5), F(44, 5)], [F(6, 5), F(14), F(12)], [F(11, 10), F(9, 2), F(-26)]],
        "c": [[F(217, 50), F(9, 2), F(44, 5)], [F(3, 2), F(97, 6), F(12)], [F(11, 10), F(9, 2), F(-26)]],
        "d": [[F(104, 25), F(18, 5), F(44, 5)], [F(6, 5), F(106, 3), F(12)], [F(11, 10), F(9, 2), F(-26)]]}
    bSM = (F(41, 10), F(-19, 6), F(-7))
    for s in "abcd":
        R0 = regimes(s, DW, DB, F(0))
        assert R0[0][0] == bSM and R0[0][1] == B_SM_STORE
        assert R0[1][0] == expect_mid[s] and R0[1][1] == expect_B[s]
        assert R0[2][0] == (F(33, 5), F(1), F(-3)) and R0[2][1] == B_MSSM_STORE
        dl = tuple(R0[1][0][i] - bSM[i] for i in range(3))
        dh = tuple(R0[2][0][i] - R0[1][0][i] for i in range(3))
        assert dl == LIGHT[s] and tuple(dl[i] + dh[i] for i in range(3)) == FULL
        R1 = regimes(s, DW, DB, F(1))
        if s in "ad":                       # gaugino Yukawas: B_i2 -= dW_i, B_i1 -= (3/5) dB_i
            assert all(R1[1][1][i][1] == R0[1][1][i][1] - DW[i] for i in range(3))
            assert all(R1[1][1][i][0] == R0[1][1][i][0] - F(3, 5) * DB[i] for i in range(3))
        else:
            assert R1[1][1] == R0[1][1]
    # one loop at the inputs of spectrum-run: exact endpoints and the common diagonal point
    aem, s2, als = F(128), F(2312, 10000), F(118, 1000)
    a2 = s2 * aem
    a1 = F(3, 5) * (aem - a2)
    a3 = 1 / als
    R = (a1 - a2) / (a2 - a3)
    diag = None
    for s in "abcd":
        Dl = LIGHT[s]
        Dh = tuple(FULL[i] - Dl[i] for i in range(3))
        A, Bc, C = one_loop_line(Dl, Dh, R, bSM)
        fd = C / (A + Bc)                   # f = f': the full content at one threshold
        diag = fd if diag is None else diag
        assert fd == diag
        fp_at_f1 = (C - A) / Bc
        f_at_fp0 = C / A
        inside = (0 <= fp_at_f1 <= 1) or (0 <= f_at_fp0 <= 1)
        assert inside == (s == "d")         # (a)-(c) miss, (d) admissible
        if s == "d":
            assert abs(fp_at_f1 - F(99115, 100000)) < F(1, 100000)
            assert abs(f_at_fp0 - F(4377, 10000)) < F(1, 10000)
    assert diag > 1 and abs(diag - F(10116, 10000)) < F(1, 10000)
    b12, b23 = bSM[0] - bSM[1], bSM[1] - bSM[2]
    assert diag == (R * b23 - b12) / ((FULL[0] - FULL[1]) - R * (FULL[1] - FULL[2]))
    return True


def check_decision():
    premise("standard-model.supersymmetric-row-two-loops")
    premise("standard-model.imported-proton-condition")
    premise("standard-model.proton-condition-candidates")
    premise("standard-model.two-threshold-criterion")
    premise("standard-model.imported-two-loop-gauge-coefficients")
    premise("standard-model.four-supersymmetric-splits")
    premise("standard-model.imported-coefficient-sum-indices")   # the one-loop coefficients of the listings
    premise("standard-model.table-exact")                         # the component listings and f = 1.0116
    premise("standard-model.spectrum-run")                        # the inputs used in (4)
    # (1) at M_I = M_I' the middle regime has zero length: below the common threshold every split runs
    #     the Standard Model (b, B, c), above it the minimal supersymmetric (b, B, c); these are the two
    #     regimes of the stored one-threshold row, whatever the light set and whether or not the
    #     gaugino Yukawas are included in the middle regime.
    row_below = (b_gen(SMF, [H]), B_gen(SMF, [H]), (F(17, 10), F(3, 2), F(2)))
    row_above = (B_susy(SMF + HIGGSINOS)[0], B_susy(SMF + HIGGSINOS)[1], (F(26, 5), F(6), F(4)))
    assert row_below[0] == (F(41, 10), F(-19, 6), F(-7)) and mat_eq(row_below[1], B_SM_STORE)
    assert row_above[0] == (F(33, 5), F(1), F(-3)) and mat_eq(row_above[1], B_MSSM_STORE)
    for s in "abcd":
        for yt in (F(0), F(1)):
            R = regimes(s, DW, DB, yt)
            assert R[0][0] == row_below[0] and mat_eq(R[0][1], row_below[1]) and R[0][2] == row_below[2]
            assert R[2][0] == row_above[0] and mat_eq(R[2][1], row_above[1]) and R[2][2] == row_above[2]
            # and the middle regime differs from both, so f != f' is a genuinely different run
            assert R[1][0] != row_below[0] and R[1][0] != row_above[0]
    # (2) the stored row's point: M_Z < M_I = 2300 GeV < M_U = 1.1e16 GeV, so
    #     f = ln(M_U/M_I)/ln(M_U/M_Z) lies strictly between 0 and 1 for every split (logs monotone).
    MZ = F(911876, 10000)
    MI = F(2300)
    MU = 11 * F(10) ** 15
    aU = F(257, 10)
    assert MZ < MI < MU
    # (3) the proton condition at the row's point, Fact imported-proton-condition:
    #     (aU/45)(MU/1e15)^2 > 5.2 sqrt(15); both sides positive, so compare squares exactly.
    lhs = aU / 45 * (MU / F(10) ** 15) ** 2
    assert lhs > 0 and lhs ** 2 > F(52, 10) ** 2 * 15
    # the same comparison fails at the one-loop row candidates' scale (M_U = 1.6e14), as a control
    low = aU / 45 * (F(16, 100)) ** 2
    assert low ** 2 < F(52, 10) ** 2 * 15
    # (4) at one loop the common diagonal point is f = 1.0116... > 1 (check_coefficients computes it
    #     exactly), so at one loop the same spectrum is outside the triangle: the decision changes
    #     between one and two loops only through the row's two-loop threshold.
    aem, s2, als = F(128), F(2312, 10000), F(118, 1000)
    a2 = s2 * aem
    a1 = F(3, 5) * (aem - a2)
    a3 = 1 / als
    Rr = (a1 - a2) / (a2 - a3)
    b = row_below[0]
    fd = (Rr * (b[1] - b[2]) - (b[0] - b[1])) / ((FULL[0] - FULL[1]) - Rr * (FULL[1] - FULL[2]))
    assert fd > 1
    return True
