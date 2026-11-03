"""standard-model.four-supersymmetric-splits: exact checks.

Species content with one-loop indices (Weyl fermions weight 2/3, complex scalars 1/3; T1 = (3/5) Y^2 per state,
T2 = 1/2 per doublet and 2 for the wino triplet, T3 = 1/2 per triplet and 3 for the gluino), rebuilt so that the
gauge part (0, -22/3, -11) plus three generations and the Higgs doublet give the SM (41/10, -19/6, -7) and the full
supersymmetric content (33/5, 1, -3), the inputs of standard-model.spectrum-run.
Record inputs a = (3/5 (128 - a_2), a_2 = 0.2312 * 128, 500/59), R = (a1 - a2)/(a2 - a3). For a light set D at
M_I and a heavy set D' at M_I' the two-threshold criterion gives the line f (D12 - R D23) + f' (D'12 - R D'23) =
R b23 - b12 inside 0 <= f' <= f <= 1 with a positive meeting scale.
(1) On the line r(f, f') = R exactly (six f per family), off it (f' shifted by +-1/4) not.
(2) Families (a) gauginos + higgsinos light, (b) higgsinos light, (c) both doublets light: the line misses the
    triangle; (d) wino, bino, higgsinos light: a segment with exact endpoints f' = 0, f in (0.437, 0.438), and
    f = 1, f' in (0.990, 0.992).
(3) Scales at the endpoints (rigorous exp and pi bounds from the spectrum-run check's EXPORTS): at (1, f') M_U in
    (1.95, 2.05) x 10^16 and the heavy partners at M_I'/M_Z in (1.33, 1.35), the light ones at M_Z; at (f, 0) the
    electroweak-inos at M_I in (6.5, 7.5) x 10^8 and M_U = M_I' in (1.55, 1.65) x 10^14.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

H = F(1, 2)
# (name, weyl?, SU(2) dim, T2, SU(3) dim, T3, Y, multiplicity)
GEN = [("Q", 1, 2, H, 3, H, F(1, 6), 1), ("L", 1, 2, H, 1, 0, F(-1, 2), 1), ("uc", 1, 1, 0, 3, H, F(-2, 3), 1),
       ("dc", 1, 1, 0, 3, H, F(1, 3), 1), ("ec", 1, 1, 0, 1, 0, F(1), 1), ("nuc", 1, 1, 0, 1, 0, F(0), 1)]
HIGGS = [("H", 0, 2, H, 1, 0, H, 1)]
GAUGINOS = [("gluino", 1, 1, 0, 8, F(3), F(0), 1), ("wino", 1, 3, F(2), 1, 0, F(0), 1), ("bino", 1, 1, 0, 1, 0, F(0), 1)]
HIGGSINOS = [("Hu", 1, 2, H, 1, 0, H, 1), ("Hd", 1, 2, H, 1, 0, -H, 1)]
HIGGS2 = [("H2", 0, 2, H, 1, 0, -H, 1)]
SM = [f[:7] + (3,) for f in GEN] + HIGGS
SFERMIONS = [(f[0], 0) + f[2:7] + (3,) for f in GEN]
F_SAMPLES = [F(0), F(1, 3), F(1, 2), F(1), F(3, 2), F(-1)]


def _delta(fields):
    tot = [F(0)] * 3
    for (_, weyl, d2, T2, d3, T3, Y, m) in fields:
        w = F(2, 3) if weyl else F(1, 3)
        for i, t in enumerate((F(3, 5) * Y * Y * d2 * d3, T2 * d3, T3 * d2)):
            tot[i] += w * t * m
    return tuple(tot)


def _b(fields):
    d = _delta(fields)
    return tuple(g + x for g, x in zip((F(0), F(-22, 3), F(-11)), d))


def _setup(rec):
    a1, a2, a3 = rec()
    bs = _b(SM)
    return (a1, a2, a3), (a1 - a2) / (a2 - a3), bs[0] - bs[1], bs[1] - bs[2]


def _families():
    return [(_delta(GAUGINOS + HIGGSINOS), _delta(SFERMIONS + HIGGS2)),
            (_delta(HIGGSINOS), _delta(GAUGINOS + SFERMIONS + HIGGS2)),
            (_delta(HIGGSINOS + HIGGS2), _delta(GAUGINOS + SFERMIONS)),
            (_delta(GAUGINOS[1:] + HIGGSINOS), _delta(GAUGINOS[:1] + SFERMIONS + HIGGS2))]


def _line(d, dp, R, b12, b23):
    return (d[0] - d[1]) - R * (d[1] - d[2]), (dp[0] - dp[1]) - R * (dp[1] - dp[2]), R * b23 - b12


def _segment(d, dp, a, R, b12, b23):
    P, Q, C = _line(d, dp, R, b12, b23)
    pts = []
    if P != 0 and 0 <= C / P <= 1:
        pts.append((C / P, F(0)))
    if Q != 0 and 0 <= (C - P) / Q <= 1:
        pts.append((F(1), (C - P) / Q))
    if P + Q != 0 and 0 <= C / (P + Q) <= 1:
        pts.append((C / (P + Q), C / (P + Q)))
    pts = sorted(set(pts))
    return [(f, fp) for (f, fp) in pts if (a[0] - a[1]) / (b12 + f * (d[0] - d[1]) + fp * (dp[0] - dp[1])) > 0]


def check_coefficients_and_level_line():
    run = premise("standard-model.spectrum-run")
    premise("standard-model.two-threshold-criterion")
    ok = _b(SM) == (F(41, 10), F(-19, 6), F(-7))
    ok = ok and _b(SM + GAUGINOS + HIGGSINOS + HIGGS2 + SFERMIONS) == (F(33, 5), F(1), F(-3))
    a, R, b12, b23 = _setup(run["record"])

    def r2(d, dp, f, fp):
        return (b12 + f * (d[0] - d[1]) + fp * (dp[0] - dp[1])) / (b23 + f * (d[1] - d[2]) + fp * (dp[1] - dp[2]))
    n_on = n_off = 0
    for d, dp in _families():
        P, Q, C = _line(d, dp, R, b12, b23)
        for f in F_SAMPLES:
            fp = (C - P * f) / Q
            if b23 + f * (d[1] - d[2]) + fp * (dp[1] - dp[2]) != 0:
                ok = ok and r2(d, dp, f, fp) == R
                n_on += 1
            for sh in (F(1, 4), F(-1, 4)):
                if b23 + f * (d[1] - d[2]) + (fp + sh) * (dp[1] - dp[2]) != 0:
                    ok = ok and r2(d, dp, f, fp + sh) != R
                    n_off += 1
    ok = ok and n_on == 24 and n_off == 48
    GA.check("b(SM) = (41/10, -19/6, -7), b(MSSM) = (33/5, 1, -3); r(f, f') = R exactly on the line", ok)
    return ok


def check_three_splits_miss_one_has_segment():
    run = premise("standard-model.spectrum-run")
    premise("standard-model.two-threshold-criterion")
    a, R, b12, b23 = _setup(run["record"])
    segs = [_segment(d, dp, a, R, b12, b23) for d, dp in _families()]
    ok = [len(s) for s in segs] == [0, 0, 0, 2]
    (fa, fpa), (fb, fpb) = segs[3]
    ok = ok and fpa == 0 and F(437, 1000) < fa < F(438, 1000) and fb == 1 and F(990, 1000) < fpb < F(992, 1000)
    GA.check("splits (a), (b), (c) miss the triangle; (d) has the segment (0.438, 0) to (1, 0.991)", ok)
    return ok


def check_scales_at_the_endpoints():
    run = premise("standard-model.spectrum-run")
    premise("standard-model.two-threshold-criterion")
    a, R, b12, b23 = _setup(run["record"])
    d, dp = _families()[3]
    (fa, fpa), (fb, fpb) = _segment(d, dp, a, R, b12, b23)
    pib = run["pi_bounds"]()
    gev = lambda t: run["gev_bounds"](t, pib)
    x = lambda f, fp: (a[0] - a[1]) / (b12 + f * (d[0] - d[1]) + fp * (dp[0] - dp[1]))
    MZ = run["MZ"]
    ok = True
    xb = x(fb, fpb)
    lo, hi = gev(xb)
    ok = ok and F(195, 100) * 10 ** 16 < lo and hi < F(205, 100) * 10 ** 16
    lo, hi = gev(xb * (1 - fpb))
    ok = ok and F(133, 100) < lo / MZ and hi / MZ < F(135, 100) and xb * (1 - fb) == 0
    xa = x(fa, fpa)
    lo, hi = gev(xa * (1 - fa))
    ok = ok and F(65, 10) * 10 ** 8 < lo and hi < F(75, 10) * 10 ** 8
    lo, hi = gev(xa)
    ok = ok and F(155, 100) * 10 ** 14 < lo and hi < F(165, 100) * 10 ** 14 and xa * (1 - fpa) == xa
    GA.check("(d) endpoints: M_U = 2.0e16 with partners within 1.34 M_Z; electroweak-inos at 7e8, M_U = 1.6e14", ok)
    return ok
