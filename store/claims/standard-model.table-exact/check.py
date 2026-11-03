"""standard-model.table-exact: exact checks.

Each row's Dl is rebuilt from a component listing by the imported coefficient formula (Weyl 2/3,
complex scalar 1/3, T_1 = (3/5) Y^2 per component) and compared with the table; r_Dl, f, a_U and the
admissibility verdict come from the one-threshold solver (exported by that claim's check) at the
inputs of the spectrum-run proposition (alpha_em^-1 = 128, sin^2 = 0.2312, alpha_s = 0.118). The
printed decimals are compared by rounding exact rationals. GeV values (M_I = 62 GeV for the full
content; thresholds 8e6, 7e8, 1.5e9 GeV; meeting scales 1.5 to 2.5 x 10^14 GeV) are enclosed by
rigorous rational bounds on pi and exp. Cross-checks: the desert and supersymmetric sin^2 of the
spectrum-run proposition, and the full content's admissibility switching exactly at the record value
sin^2 = 6539/28320. Clause (e) uses the proton condition exported by that claim's check.
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

# --------------------------------------------------------------------------- pi, exp bounds


PI_LO, PI_HI = series.pi_bracket(40)   # Machin, 40 alternating terms per arctan


def exp_bounds(t):
    """lo <= e^t <= hi, rational, rigorous (series.exp_bounds; the reciprocal for t < 0)."""
    t = F(t)
    if t < 0:
        lo, hi = series.exp_bounds(-t)
        return 1 / hi, 1 / lo
    return series.exp_bounds(t)


MZ = F(911876, 10000)


def gev(x):
    """GeV interval of M_Z e^(2 pi x)."""
    lo, hi = sorted((2 * PI_LO * x, 2 * PI_HI * x))
    return MZ * exp_bounds(lo)[0], MZ * exp_bounds(hi)[1]


def rounds_to(lo, hi, mant, e):
    u = F(10) ** e
    return (mant - F(1, 2)) * u <= lo and hi < (mant + F(1, 2)) * u


# --------------------------------------------------------------------------- listings
WEYL, SC = "weyl", "scalar"
H = F(1, 2)
GEN = [("Q", WEYL, 2, H, 3, H, F(1, 6), 1), ("L", WEYL, 2, H, 1, 0, F(-1, 2), 1),
       ("u^c", WEYL, 1, 0, 3, H, F(-2, 3), 1), ("d^c", WEYL, 1, 0, 3, H, F(1, 3), 1),
       ("e^c", WEYL, 1, 0, 1, 0, F(1), 1), ("nu^c", WEYL, 1, 0, 1, 0, F(0), 1)]
GLUINO, WINO, BINO = [("gluino", WEYL, 1, 0, 8, F(3), F(0), 1)], [("wino", WEYL, 3, F(2), 1, 0, F(0), 1)], \
    [("bino", WEYL, 1, 0, 1, 0, F(0), 1)]
HIGGSINOS = [("Hu~", WEYL, 2, H, 1, 0, H, 1), ("Hd~", WEYL, 2, H, 1, 0, -H, 1)]
HIGGS2 = [("H2", SC, 2, H, 1, 0, -H, 1)]
SFERMIONS = [(n, SC, d2, T2, d3, T3, Y, 3 * m) for (n, k, d2, T2, d3, T3, Y, m) in GEN]
FIVEBAR = [("Hd", SC, 2, H, 1, 0, -H, 1), ("T", SC, 1, 0, 3, H, F(1, 3), 1)]
GAUG = GLUINO + WINO + BINO
ROWS = [FIVEBAR, GLUINO, GAUG, HIGGSINOS, HIGGS2, GAUG + HIGGSINOS, GAUG + HIGGSINOS + HIGGS2,
        GAUG + HIGGSINOS + HIGGS2 + SFERMIONS, WINO, WINO + BINO + HIGGSINOS,
        WINO + BINO + HIGGSINOS + HIGGS2 + SFERMIONS]


def delta_b(fields):
    tot = [F(0)] * 3
    for _, kind, d2, T2, d3, T3, Y, m in fields:
        w = F(2, 3) if kind == WEYL else F(1, 3)
        for i, t in enumerate((F(3, 5) * Y * Y * d2 * d3, T2 * d3, T3 * d2)):
            tot[i] += w * t * m
    return tuple(tot)


def record(aem_inv, s2, as_inv):
    a2 = s2 * aem_inv
    return (F(3, 5) * (aem_inv - a2), a2, as_inv)


A_T12 = record(F(128), F(2312, 10000), F(500, 59))
B_SM = (F(41, 10), F(-19, 6), F(-7))


def r_D(d):
    return (B_SM[0] - B_SM[1] + d[0] - d[1]) / (B_SM[1] - B_SM[2] + d[1] - d[2])


def verdict(s):
    """'none', 'worsens', 'short' or 'admissible' from (x, y, a_U, f)."""
    if s is None:
        return "none"
    x, y, aU, f = s
    if f < 0:
        return "worsens"
    if f > 1:
        return "short"
    return "admissible" if x > 0 and aU > 0 else "inadmissible"


# --------------------------------------------------------------------------- checks


def check_table_rows():
    premise("standard-model.imported-coefficient-sum-indices")
    premise("standard-model.complete-multiplets-shift-all-three-coefficients")
    premise("standard-model.spectrum-run")
    solve = premise("standard-model.one-threshold-exact-criterion")["solve"]
    table = [((F(1, 6), F(1, 6), F(1, 6)), None, None, "none"),
             ((F(0), F(0), F(2)), F(218, 55), (-69, -2), "worsens"),
             ((F(0), F(4, 3), F(2)), F(178, 95), (476, -2), "short"),
             ((F(2, 5), F(2, 3), F(0)), F(14, 9), (161, -2), "short"),
             ((F(1, 10), F(1, 6), F(0)), F(9, 5), (642, -2), "short"),
             ((F(2, 5), F(2), F(2)), F(34, 23), (120, -2), "short"),
             ((F(1, 2), F(13, 6), F(2)), F(7, 5), (10116, -4), "short"),
             ((F(5, 2), F(25, 6), F(4)), F(7, 5), (10116, -4), "short"),
             ((F(0), F(4, 3), F(0)), F(178, 155), (60, -2), "admissible"),
             ((F(2, 5), F(2), F(0)), F(34, 35), (44, -2), "admissible"),
             ((F(5, 2), F(25, 6), F(2)), F(14, 15), (41, -2), "admissible")]
    ok = len(ROWS) == len(table) == 11
    for fields, (d, rd, fr, concl) in zip(ROWS, table):
        dd = delta_b(fields)
        ok = ok and dd == d
        s = solve(A_T12, B_SM, dd)
        ok = ok and verdict(s) == concl
        if rd is None:
            ok = ok and dd[0] == dd[1] == dd[2] and r_D(dd) == r_D((F(0),) * 3)
        else:
            ok = ok and r_D(dd) == rd and rounds_to(s[3], s[3], *fr)
    # three gauginos: short with a_U < 0
    ok = ok and solve(A_T12, B_SM, delta_b(GAUG))[2] < 0
    GA.check("table: every row's Dl from its listing, r_Dl, f and conclusion", ok)
    return ok


def check_full_supersymmetric_content():
    premise("standard-model.imported-coefficient-sum-indices")
    premise("standard-model.complete-multiplets-shift-all-three-coefficients")
    premise("standard-model.spectrum-run")
    solve = premise("standard-model.one-threshold-exact-criterion")["solve"]
    full = delta_b(ROWS[7])
    b_full = tuple(B_SM[i] + full[i] for i in range(3))
    ok = b_full == (F(33, 5), F(1), F(-3)) and r_D(full) == (F(33, 5) - 1) / (1 + 3)
    R = (A_T12[0] - A_T12[1]) / (A_T12[1] - A_T12[2])
    ok = ok and rounds_to(F(7, 5) - R, F(7, 5) - R, 55, -4)
    x, y, aU, f = solve(A_T12, B_SM, full)
    lo, hi = gev(x - y)
    ok = ok and rounds_to(lo, hi, 62, 0) and hi < MZ                 # M_I = 62 GeV, below M_Z
    ok = ok and rounds_to(f - 1, f - 1, 12, -3)                      # inadmissible by 1.2 percent in f
    # adding or removing the sfermions (complete multiplets) changes only a_U
    s2 = solve(A_T12, B_SM, delta_b(ROWS[6]))
    ok = ok and s2[0] == x and s2[1] == y and s2[3] == f and s2[2] != aU
    ok = ok and s2[2] - aU == 2 * y                                  # sfermions (c = 2) lower a_U by 2y
    GA.check("table (c): full content r_Dl = 7/5, gap 0.0055, f = 1.0116, M_I = 62 GeV; sfermions inert", ok)
    return ok


def check_three_admissible_rows():
    premise("standard-model.imported-coefficient-sum-indices")
    premise("standard-model.spectrum-run")
    solve = premise("standard-model.one-threshold-exact-criterion")["solve"]
    adm = [i for i, fields in enumerate(ROWS[1:], 1) if verdict(solve(A_T12, B_SM, delta_b(fields))) == "admissible"]
    ok = adm == [8, 9, 10]
    ok = ok and all(not any(fd[0] == "gluino" for fd in ROWS[i]) for i in adm)
    ok = ok and all(any(fd[0] == "gluino" for fd in ROWS[i]) for i in (1, 2, 5, 6, 7))
    stated_MI = {8: (8, 6), 9: (7, 8), 10: (15, 8)}
    mus = []
    for i in adm:
        x, y, aU, f = solve(A_T12, B_SM, delta_b(ROWS[i]))
        lo, hi = gev(x - y)
        ok = ok and rounds_to(lo, hi, *stated_MI[i])
        mus.append(gev(x))
    ok = ok and rounds_to(min(m[0] for m in mus), min(m[1] for m in mus), 15, 13)
    ok = ok and rounds_to(max(m[0] for m in mus), max(m[1] for m in mus), 25, 13)
    GA.check("table (d): exactly three admissible rows, no gluino; thresholds 8e6, 7e8, 1.5e9 GeV", ok)
    return ok


def check_spectrum_run_cross_checks():
    premise("standard-model.spectrum-run")
    solve = premise("standard-model.one-threshold-exact-criterion")["solve"]

    def predict(bs, A=A_T12):
        aem_inv = F(5, 3) * A[0] + A[1]
        x = (aem_inv - F(8, 3) * A[2]) / (F(5, 3) * (bs[0] - bs[2]) + (bs[1] - bs[2]))
        return (A[2] + (bs[1] - bs[2]) * x) / aem_inv
    ok = predict(B_SM) == F(78761, 379488) and predict((F(33, 5), F(1), F(-3))) == F(6539, 28320)
    full = (F(5, 2), F(25, 6), F(4))
    s_star = F(6539, 28320)
    for s2, expect in ((s_star, "admissible"), (s_star - F(1, 10 ** 6), "admissible"),
                       (s_star + F(1, 10 ** 6), "short")):
        ok = ok and verdict(solve(record(F(128), s2, F(500, 59)), B_SM, full)) == expect
    ok = ok and solve(record(F(128), s_star, F(500, 59)), B_SM, full)[3] == 1
    GA.check("table: the spectrum-run sin^2 values, and the full content admissible iff sin^2 <= 6539/28320", ok)
    return ok


def check_admissible_rows_fail_proton_condition():
    premise("standard-model.imported-coefficient-sum-indices")
    solve = premise("standard-model.one-threshold-exact-criterion")["solve"]
    cond = premise("standard-model.proton-condition-candidates")["condition"]
    ok = True
    n = 0
    for fields in ROWS[8:]:
        x, y, aU, f = solve(A_T12, B_SM, delta_b(fields))
        ok = ok and cond(gev(x)[1], aU) < 0
        n += 1
    ok = ok and n == 3
    GA.check("table (e): none of the three admissible rows meets the proton condition", ok)
    return ok
