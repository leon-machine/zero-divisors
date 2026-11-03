"""synthesis.colour-light-content-proton-ceiling: exact checks.

Everything is exact (Fractions). The one transcendental step, M_13 = M_Z exp(2 pi t_13), is bounded
above and below in rationals: pi < 22/7 and pi > 223/71, M_Z in (91.18, 91.19) GeV, and exp bounded by
a Taylor majorant / minorant applied to x/2^s and squared s times.

test_ceiling: the record values and t_13, a_3 + 7 t_13; the bounds 2.4e14 < M_13 < 2.5e14 GeV; the proton
  figure below 1/10 against 5.2 sqrt(15) > 20; the miss factors (above 200, lifetime above 1.2e5);
  clause (i) on multi-threshold spectra (exact crossing); clause (iii) for the three admissible rows;
  the closing remark rebuilt from the index formula (colour singlets, triplet threshold Y^2 = 5/18,
  Q and d^c triplets, gluino Delta = (0, 0, 2)).
"""
import GA
import series
from tp_premise import premise
from fractions import Fraction as F

B = (F(41, 10), F(-19, 6), F(-7))        # Standard Model coefficients below every threshold


def record():
    a2 = F(2312, 10000) * 128
    a1 = F(3, 5) * (128 - a2)
    a3 = F(500, 59)
    return a1, a2, a3


def run(a, t, thresholds, i):
    """a_i(t) = a_i - b_i t - sum_k Dl_i^(k) (t - t_k)_+"""
    v = a[i] - B[i] * t
    for tk, D in thresholds:
        if t > tk:
            v -= D[i] * (t - tk)
    return v


def crossing13(a, thresholds):
    """exact zero of d(t) = a_1(t) - a_3(t), piecewise linear and strictly decreasing"""
    knots = sorted({F(0)} | {tk for tk, _ in thresholds})
    knots.append(knots[-1] + 1000)
    for lo, hi in zip(knots, knots[1:]):
        dlo = run(a, lo, thresholds, 0) - run(a, lo, thresholds, 2)
        dhi = run(a, hi, thresholds, 0) - run(a, hi, thresholds, 2)
        assert dhi < dlo                                    # strictly decreasing piece
        if dlo >= 0 >= dhi:
            return lo + dlo * (hi - lo) / (dlo - dhi)
    raise AssertionError("no crossing")


exp_bounds = series.exp_bounds          # rational lo <= exp(x) <= hi for 0 <= x
roundup = series.round_up               # smallest multiple of 1/den >= x
rounddown = series.round_down           # largest multiple of 1/den <= x


def triplet_delta(d, Y, kappa):
    """colour triplet in an SU(2) rep of dimension d: indices T1 = 3/5 Y^2 * 3d, T3 = d/2"""
    T1 = F(3, 5) * Y * Y * 3 * d
    T2 = 3 * F(d * (d * d - 1), 12)                        # three colours times the SU(2) index
    T3 = F(d, 2)
    return (kappa * T1, kappa * T2, kappa * T3)


def test_ceiling():
    premise("standard-model.imported-one-loop-running-trace-ratio")
    premise("standard-model.spectrum-run")
    premise("standard-model.one-threshold-exact-criterion")
    premise("standard-model.table-exact")
    premise("standard-model.imported-proton-condition")
    premise("standard-model.imported-coefficient-sum-indices")
    a = record()
    a1, a2, a3 = a
    assert a2 == F(18496, 625) and a1 == F(184512, 3125)
    t13 = (a1 - a3) / (B[0] - B[2])
    assert t13 == F(18647416, 4093125)
    ceil = a3 + 7 * t13
    assert ceil == F(165219412, 4093125)
    assert abs(ceil - F(404, 10)) < F(5, 100)                  # 40.4 to the stated precision
    GA.check("t_13 = 18647416/4093125 and a_3 + 7 t_13 = 165219412/4093125 = 40.37", True)

    # M_13 = M_Z exp(2 pi t_13): rigorous rational bounds
    _, hi = exp_bounds(roundup(2 * F(22, 7) * t13, 10 ** 6))
    lo, _ = exp_bounds(rounddown(2 * F(223, 71) * t13, 10 ** 6))
    M13_hi = F(9119, 100) * hi
    M13_lo = F(9118, 100) * lo
    assert M13_hi < F(25, 10) * 10 ** 14
    assert M13_lo > F(24, 10) * 10 ** 14
    GA.check("2.4e14 < M_13 < 2.5e14 GeV", True)

    # (ii): the proton figure at the bound, and the misses
    P_hi = ceil / 45 * (M13_hi / 10 ** 15) ** 2
    assert P_hi < ceil / 45 / 16 < F(57, 1000) < F(1, 10)
    assert F(52, 10) ** 2 * 15 == F(4056, 10) and F(4056, 10) > 400   # 5.2 sqrt(15) > 20
    assert 20 / F(1, 10) == 200                                       # figure misses by more than 200
    assert (20 / F(57, 1000)) ** 2 > F(12, 10) * 10 ** 5             # lifetime misses by more than 1.2e5
    P_lo = ceil / 45 * (M13_lo / 10 ** 15) ** 2
    assert 10 ** 5 < F(4056, 10) / P_hi ** 2 and F(4056, 10) / P_lo ** 2 < 2 * 10 ** 5   # about 1e5
    GA.check("proton figure at the ceiling below 1/10 against 5.2 sqrt 15 > 20; misses above 200 and 1e5", True)

    # (i) on multi-threshold spectra with Dl_1 >= Dl_3 >= 0
    spectra = [
        [],
        [(F(1), (F(0), F(4, 3), F(0)))],                                    # wino: attains both bounds
        [(F(2), (F(2, 5), F(2), F(0)))],
        [(F(1, 2), (F(5, 2), F(25, 6), F(2)))],
        [(F(1), (F(1), F(1), F(1))), (F(3), (F(0), F(4, 3), F(0)))],          # complete multiplet + wino
        [(F(1), (F(3), F(0), F(1))), (F(2), (F(1, 2), F(2), F(1, 2))), (F(4), (F(6), F(1), F(0)))],
        [(F(0), (F(2), F(2), F(1))), (F(5), (F(7), F(0), F(7)))],             # second one above the crossing
    ]
    for th in spectra:
        assert all(D[0] >= D[2] >= 0 and tk >= 0 for tk, D in th)
        ts = crossing13(a, th)
        assert ts <= t13
        assert run(a, ts, th, 2) <= ceil
        below = [D for tk, D in th if tk < t13]
        assert (ts == t13) == all(D[0] == D[2] for D in below)
        if all(D[0] == 0 and D[2] == 0 for D in below):
            assert ts == t13 and run(a, ts, th, 2) == ceil
    # a gluino breaks the bound: the crossing moves above t_13
    assert crossing13(a, [(F(1), (F(0), F(0), F(2)))]) > t13
    GA.check("(i): crossing at or below t_13, a_3 there at most a_3 + 7 t_13, equality exactly as stated", True)

    # (iii) the three admissible rows
    for D in [(F(0), F(4, 3), F(0)), (F(2, 5), F(2), F(0)), (F(5, 2), F(25, 6), F(2))]:
        assert D[0] >= D[2] >= 0
    GA.check("(iii): the three admissible rows satisfy Dl_1 >= Dl_3 >= 0", True)

    # closing remark from the index formula
    for d in (1, 2, 3):
        for kappa in (F(2, 3), F(1, 3)):
            for Y in (F(0), F(1, 6), F(1, 3), F(1, 2), F(2, 3), F(1), F(-2, 3)):
                D = triplet_delta(d, Y, kappa)
                assert D[2] > 0
                assert (D[0] >= D[2]) == (18 * Y * Y >= 5)
                assert D[0] - D[2] == kappa * d * (F(9, 5) * Y * Y - F(1, 2))
    assert 18 * F(1, 6) ** 2 < 5 and 18 * F(1, 3) ** 2 < 5 and 18 * F(2, 3) ** 2 >= 5
    gluino = (F(0), F(0), F(2, 3) * 3)                             # Weyl adjoint of SU(3), T_3 = 3
    assert gluino == (0, 0, 2) and gluino[0] - gluino[2] == -2
    singlet = (F(2, 3) * F(3, 5) * F(1, 4) * 2, F(2, 3) * F(1, 2), F(0))   # a lepton-like doublet
    assert singlet[0] >= singlet[2] == 0
    GA.check("closing remark: singlets satisfy the hypothesis, triplets iff Y^2 >= 5/18, Q, d^c, gluino do not",
             True)
    return True
