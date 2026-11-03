"""standard-model.fits-record-level: exact checks of the mass content of the four stored fits (the
couplings of legacy verify_T12.py, obs:anglefits), with exact rational arithmetic in place of the legacy
floating-point SVD.

The stored couplings are decimal strings read as exact Fractions; complex entries are GA.QI. For each row:
Y_33 = 3 w_u f_33 (Premise (EW), held exact), M_u = Y + w_u f + c_u H, M_nu = Y - 3 w_u f + c_nu H,
M_d = Z + w_d f + c_d H, M_e = Z - 3 w_d f + c_e H (the Clebsch structure), and the light neutrino matrix
M_light = M_nu (v_R f)^-1 M_nu^T with v_R = 1.95e10/0.469 GeV (the seesaw at the v_R of the neutrino-sector
proposition). Masses are the singular values: the roots of the characteristic cubic of M M^dagger, which is
real; a sign change of the cubic at the squared ends of an interval puts a root in it, and three disjoint
intervals with sign changes locate all three roots (bisection narrows them where a ratio is needed).
  (1) The nine charged-fermion masses lie within 1% (up, charged lepton) and 2% (down) of the record values
      at M_I (the legacy tolerances), in every row.
  (2) m_3 within 1% of 5.02e-11 GeV and m_3/m_2 within 1% of 5.83 in every row; m_1 and the largest |M_nu|
      entry agree with the table to its printed digits (0.03, 0.1, 4.9, 1.7 meV; 0.04, 2.9, 4.0, 2.2 GeV);
      the first row's m_1 is below 0.1 meV; (M_nu)_33 = 0 exactly under (EW).
Not tested (recorded only by the legacy floating-point CONTROL lines): the CKM moduli and phase, the three
lepton mixing angles, and the tuning measure Delta. Hypothesis (S) supplies the lepton doublet whose
Dirac matrix M_nu enters (2), so (2) calls its premise.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

FITS = {
    'natural': {
        'Y': [[('0.00044030999999999996', '8.558e-05'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.24034995', '-0.00696217'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('69.3375', '0.0')]],
        'Z': [[('0.00075216', '-0.00054827'), ('0.00253266', '-0.00586652'), ('0.00265671', '-0.00918216')],
              [('0.00253266', '-0.00586652'), ('-0.0008808', '-0.04857195'), ('-0.29373987', '-0.00537998')],
              [('0.00265671', '-0.00918216'), ('-0.29373987', '-0.00537998'), ('-0.03473334', '0.50947232')]],
        'f': [[('2.159909099841564e-06', '-8.815156696286951e-07'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0007895328365602121', '7.171374093969165e-05'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('0.23807000367250775', '0.0')]],
        'H': [[('0.0', '0.0'), ('0.02177590845600245', '0.0009747223764485373'), ('0.00822980338529986', '-0.05458645619613881')],
              [('-0.02177590845600245', '-0.0009747223764485373'), ('0.0', '0.0'), ('-0.9982371706480334', '0.0')],
              [('-0.00822980338529986', '0.05458645619613881'), ('0.9982371706480334', '0.0'), ('0.0', '0.0')]],
        'wu': ('97.08278927820685', '0.0'),
        'wd': ('0.008947149859879542', '3.115949788115471'),
        'cu': ('0.0', '0.0'),
        'cn': ('-0.03465126', '-0.01185399'),
        'cd': ('-0.24735128', '-0.00300884'),
        'ce': ('-0.00955048', '-0.00124468'),
    },
    'gj126_two10': {
        'Y': [[('0.000653983551094825', '0.0008460701866779715'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('-0.32692023733842507', '0.45020175112285876'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('69.3375', '0.0')]],
        'Z': [[('-0.0027436561059755804', '-0.003365125720341077'), ('0.0049076222711831674', '-0.004726335959628511'), ('-0.003207953313353855', '-0.0016826581891301023')],
              [('0.0049076222711831674', '-0.004726335959628511'), ('0.0', '0.0'), ('0.06520378954772495', '-0.092692036899521')],
              [('-0.003207953313353855', '-0.0016826581891301023'), ('0.06520378954772495', '-0.092692036899521'), ('-0.5824819611272574', '0.06172057857070413')]],
        'f': [[('-6.109819775706838e-07', '-0.0001297670403905826'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0987620468877402', '-0.06905023926118693'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('3.5449077018109154', '0.0')]],
        'H': [[('0.0', '0.0'), ('0.08557073397893822', '0.05442657738299888'), ('0.015877954334293523', '0.027791050323897205')],
              [('-0.08557073397893822', '-0.05442657738299888'), ('0.0', '0.0'), ('0.9943293947423716', '0.0')],
              [('-0.015877954334293523', '-0.027791050323897205'), ('-0.9943293947423716', '0.0'), ('0.0', '0.0')]],
        'wu': ('6.519915874873973', '0.0'),
        'wd': ('-0.21612336005639018', '-0.01412337148205993'),
        'cu': ('0.0', '0.0'),
        'cn': ('0.9167958271897713', '-0.14187472874203033'),
        'cd': ('-0.006490610063581949', '0.09665319646658238'),
        'ce': ('0.18966815537826093', '-0.1208754419902196'),
    },
    'gj126_one10': {
        'Y': [[('0.002659817694930318', '0.0013348'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.9694610208902068', '0.68751179'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('69.33380733332764', '0.0')]],
        'Z': [[('1.1477396090192475e-05', '2.607330196234614e-05'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.002957085559958288', '0.010986007544488929'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('0.511454696555758', '0.42298822508879863')]],
        'f': [[('-0.0003841618032288598', '-0.00020473659254241508'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('-0.10021688863310176', '-0.10545311748377019'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('3.5448924836224682', '0.0')]],
        'H': [[('0.0', '0.0'), ('-0.07667673984276244', '0.062465370504992956'), ('-0.009418130015656171', '-0.0541530995543228')],
              [('0.07667673984276244', '-0.062465370504992956'), ('0.0', '0.0'), ('-0.9935781276227991', '0.0')],
              [('0.009418130015656171', '0.0541530995543228'), ('0.9935781276227991', '0.0'), ('0.0', '0.0')]],
        'wu': ('6.519596635972491', '0.0'),
        'wd': ('0.06251862880519644', '0.204598763981685'),
        'cu': ('-0.14361513', '0.02808065'),
        'cn': ('-2.13103665', '0.63952452'),
        'cd': ('0.03865532', '0.04586222'),
        'ce': ('0.06209646', '0.06630892'),
    },
    'shared_no120': {
        'Y': [[('0.001443564705269343', '0.0006321252819870818'), ('-0.012927810350428328', '0.021763542653096046'), ('0.00786511830511321', '-0.017583889139157937')],
              [('-0.012927810350428332', '0.021763542653096043'), ('-0.25406839648292606', '-0.25204028344307117'), ('0.3941847166536046', '0.14632241507355737')],
              [('0.007865118305113215', '-0.017583889139157947'), ('0.39418471665360466', '0.14632241507355745'), ('69.3375', '0.0')]],
        'Z': [[('-0.0010803809256332174', '4.35032194065487e-05'), ('0.0028630494351771533', '-0.005477306433422383'), ('0.0021456799207014154', '0.005169686922661418')],
              [('0.0028630494351771538', '-0.005477306433422383'), ('-0.0013870412824325464', '0.04368818155292397'), ('0.03197087910883101', '-0.06189021687439567')],
              [('0.0021456799207014163', '0.005169686922661419'), ('0.031970879108831014', '-0.06189021687439568'), ('-0.38452195300565983', '-0.437313333439209')]],
        'f': [[('-0.00012171281146283579', '-9.695207556045759e-05'), ('0.0019828000582194833', '-0.0033379785493365703'), ('-0.0012063107835399904', '0.002696925114444623')],
              [('0.0019828000582194838', '-0.0033379785493365694'), ('0.08758748922675343', '0.038656622826155465'), ('-0.06045799388634301', '-0.022442168105989604')],
              [('-0.0012063107835399913', '0.002696925114444624'), ('-0.060457993886343014', '-0.02244216810598962'), ('3.544874584587284', '0.0')]],
        'H': [[('0.0', '0.0'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('0.0', '0.0')],
              [('0.0', '0.0'), ('0.0', '0.0'), ('0.0', '0.0')]],
        'wu': ('6.519976785777007', '0.0'),
        'wd': ('-0.1478086471861219', '-0.16301013935319839'),
        'cu': ('0.0', '0.0'),
        'cn': ('0.0', '0.0'),
        'cd': ('0.0', '0.0'),
        'ce': ('0.0', '0.0'),
    },
}

ROWS = ["natural", "gj126_two10", "gj126_one10", "shared_no120"]
Q0 = GA.qi(0)
VR = F("1.95e10") / F("0.469")


def cq(pair):
    return GA.qi(F(pair[0]), F(pair[1]))


def mat(row, key):
    return [[cq(FITS[row][key][i][j]) for j in range(3)] for i in range(3)]


def lin(*terms):
    return [[sum((c * M[i][j] for c, M in terms), Q0) for j in range(3)] for i in range(3)]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), Q0) for j in range(3)] for i in range(3)]


def dag(A):
    return [[A[j][i].conj() for j in range(3)] for i in range(3)]


def transpose(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def inverse(M):
    cols = [GA.field_solve([r[:] for r in M], [GA.qi(1) if i == c else Q0 for i in range(3)]) for c in range(3)]
    return [[cols[j][i] for j in range(3)] for i in range(3)]


def matrices(row):
    Y, Z, f, H = mat(row, "Y"), mat(row, "Z"), mat(row, "f"), mat(row, "H")
    c = {k: cq(FITS[row][k]) for k in ("wu", "wd", "cu", "cn", "cd", "ce")}
    Y[2][2] = GA.qi(3) * c["wu"] * f[2][2]
    Mu = lin((GA.qi(1), Y), (c["wu"], f), (c["cu"], H))
    Mn = lin((GA.qi(1), Y), (GA.qi(-3) * c["wu"], f), (c["cn"], H))
    Md = lin((GA.qi(1), Z), (c["wd"], f), (c["cd"], H))
    Me = lin((GA.qi(1), Z), (GA.qi(-3) * c["wd"], f), (c["ce"], H))
    return Mu, Mn, Md, Me, f


def charpoly(M):
    """(a, b, c) with det(lam - M M^dag) = lam^3 - a lam^2 + b lam - c (all real)."""
    K = mmul(M, dag(M))
    a = K[0][0] + K[1][1] + K[2][2]
    b = (K[0][0] * K[1][1] - K[0][1] * K[1][0]) + (K[0][0] * K[2][2] - K[0][2] * K[2][0]) \
        + (K[1][1] * K[2][2] - K[1][2] * K[2][1])
    c = K[0][0] * (K[1][1] * K[2][2] - K[1][2] * K[2][1]) - K[0][1] * (K[1][0] * K[2][2] - K[1][2] * K[2][0]) \
        + K[0][2] * (K[1][0] * K[2][1] - K[1][1] * K[2][0])
    assert a.im == 0 and b.im == 0 and c.im == 0
    return a.re, b.re, c.re


def pval(p, lam):
    a, b, c = p
    return ((lam - a) * lam + b) * lam - c


def root_in(p, lo, hi):
    """A root of the cubic in [lo^2, hi^2] (masses lo, hi) by a sign change."""
    return pval(p, lo * lo) * pval(p, hi * hi) < 0


def narrow(p, lo, hi, rel):
    """Bisect a sign-change bracket [lo^2, hi^2] (in lambda) until hi/lo < 1 + rel; returns (lo^2, hi^2)."""
    a, b = lo * lo, hi * hi
    fa = pval(p, a)
    while b > a * (1 + rel):
        m = (a + b) / 2
        fm = pval(p, m)
        if (fm < 0) == (fa < 0):
            a, fa = m, fm
        else:
            b = m
    return a, b


def light(row):
    Mu, Mn, Md, Me, f = matrices(row)
    fi = inverse(f)
    return mmul(mmul(Mn, [[x / GA.qi(VR) for x in r] for r in fi]), transpose(Mn)), Mn


# record values at M_I (GeV) and the legacy relative tolerances (not fixed by the statement)
CHARGED_TARGETS = {"u": ([F("0.00065"), F("0.3170"), F("92.45")], F(1, 100)),
                   "d": ([F("0.00130"), F("0.0261"), F("1.3651")], F(2, 100)),
                   "e": ([F("0.000502"), F("0.1037"), F("1.764")], F(1, 100))}
M3_REC, RATIO_REC, TOL_NU = F("5.02e-11"), F("5.83"), F(1, 100)     # m_3 (GeV), m_3/m_2, legacy tolerance
NARROW_REL = F(1, 10 ** 5)        # bisection width for the m_3/m_2 brackets (a numerical choice)
# the table's m_1 (meV) and largest |M_nu| entry (GeV) by row, with the half-unit of the printed digit
M1_TABLE = [F("0.03"), F("0.1"), F("4.9"), F("1.7")]
M1_HALF = [F("0.005"), F("0.05"), F("0.05"), F("0.05")]
DIRAC_TABLE = [F("0.04"), F("2.9"), F("4.0"), F("2.2")]
DIRAC_HALF = [F("0.005"), F("0.05"), F("0.05"), F("0.05")]


def check_charged_fermion_masses():
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.premise-ew-equal-weight")
    ok = True
    for row in ROWS:
        Mu, Mn, Md, Me, f = matrices(row)
        for key, M in (("u", Mu), ("d", Md), ("e", Me)):
            p = charpoly(M)
            ms, tol = CHARGED_TARGETS[key]
            bands = [(m * (1 - tol), m * (1 + tol)) for m in ms]
            ok = ok and all(root_in(p, lo, hi) for lo, hi in bands)
            # the three bands are disjoint and ordered, so the three sign changes are three distinct roots
            ends = [x for b in bands for x in b]
            ok = ok and ends == sorted(ends) and len(set(ends)) == len(ends)
    GA.check("nine charged-fermion masses reproduced in all four rows", ok)
    assert ok


def check_neutrino_masses_and_dirac_entries():
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.what-angle-asks-neutrino-sector")
    premise("standard-model.premise-ew-equal-weight")
    premise("standard-model.hyp-s-slot-statistics")
    meV = F(1, 10 ** 12)
    m3, ratio, tol = M3_REC, RATIO_REC, TOL_NU
    lo3, hi3 = m3 * (1 - tol), m3 * (1 + tol)
    rlo, rhi = ratio * (1 - tol), ratio * (1 + tol)
    ok = True
    for r, row in enumerate(ROWS):
        ML, Mn = light(row)
        ok = ok and Mn[2][2] == Q0
        p = charpoly(ML)
        lo1, hi1 = (M1_TABLE[r] - M1_HALF[r]) * meV, (M1_TABLE[r] + M1_HALF[r]) * meV
        ok = ok and root_in(p, lo1, hi1)
        ok = ok and root_in(p, lo3, hi3)
        lo2, hi2 = lo3 / rhi, hi3 / rlo
        ok = ok and hi1 < lo2 and hi2 < lo3 and root_in(p, lo2, hi2)
        a3, b3 = narrow(p, lo3, hi3, NARROW_REL)
        a2, b2 = narrow(p, lo2, hi2, NARROW_REL)
        ok = ok and b3 / a2 <= rhi ** 2 and a3 / b2 >= rlo ** 2
        big = max(x.re * x.re + x.im * x.im for rr in Mn for x in rr)
        ok = ok and (DIRAC_TABLE[r] - DIRAC_HALF[r]) ** 2 <= big <= (DIRAC_TABLE[r] + DIRAC_HALF[r]) ** 2
    first = ROWS.index("natural")
    ok = ok and M1_TABLE[first] + M1_HALF[first] < F("0.1")
    GA.check("m_3, m_3/m_2, m_1 and the largest Dirac entry as tabulated", ok)
    assert ok
