"""dark-tower-matter.r1-has-no-mechanism-odd-towers: exact check of the computable core.

Assembly level; the absence of a mass mechanism is a reading of the cited results. Checked:
(1) The share without a mechanism: with the unit-ball shares 1 (mirror), 4/3 per three-dimensional
    tower, 8/(3 pi) per five-dimensional tower (two of each) and our tower excluded from the dark
    total, the three- and five-dimensional towers carry (8 pi + 16)/(11 pi + 16) of the dark matter
    (formed from the shares and checked against this closed form at rational sample values of pi).
    The form is decreasing in pi (derivative numerator 8*16 - 16*11 < 0), so pi in (333/106, 355/113) puts it in
    (0.8133, 0.8137): about 81 percent. The individual shares 18.6, 24.9, 15.8 percent are
    bracketed the same way.
(2) The viable-phase bound: (m/e^2)^2 <= 2e-16 (the K4 survival bound) gives m/e^2 <= sqrt(2) 1e-8,
    which lies in (1.41e-8, 1.42e-8): the stated m/e^2 <~ 1.4e-8 (a rounding of sqrt(2) 1e-8, not a
    strict bound below 1.4e-8). Its reciprocal e^2/m >= 1/1.42e-8 exceeds 7e7, the survival-sheets
    threshold.
(3) No dimensional transmutation in three dimensions: with [A] = (d - 2)/2 and the covariant
    derivative d + eA, [e^2] = 4 - d is 1 in d = 3 (dimensionful, so masses are not fixed by a
    running scale), 0 in d = 4 (transmutation possible), -1 in d = 5 (infrared free).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI_LO, PI_HI = F(333, 106), F(355, 113)
PI_SAMPLES = [F(3), F(22, 7), F(7, 2)]


def shares(pi):
    mirror, d3, d5 = F(1), F(4, 3), F(8, 3) / pi
    total = mirror + 2 * d3 + 2 * d5
    return mirror / total, d3 / total, d5 / total, total


def check_share_without_mechanism():
    premise("dark-tower-matter.imported-unit-ball-rule")
    premise("dark-tower-matter.five-dimensional-towers")
    for pi in PI_SAMPLES:
        m, d3, d5, total = shares(pi)
        assert total == (11 * pi + 16) / (3 * pi)
        assert 2 * d3 + 2 * d5 == (8 * pi + 16) / (11 * pi + 16)
    # (8 pi + 16)/(11 pi + 16) is decreasing in pi (checked along the samples and the bounds)
    vals = [(8 * pi + 16) / (11 * pi + 16) for pi in sorted(PI_SAMPLES + [PI_LO, PI_HI])]
    assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
    lo = (8 * PI_HI + 16) / (11 * PI_HI + 16)
    hi = (8 * PI_LO + 16) / (11 * PI_LO + 16)
    assert F(8133, 10000) < lo < hi < F(8137, 10000)
    assert F(805, 1000) <= lo and hi < F(815, 1000)           # about 81 percent
    # the individual shares (each monotone in pi): bracket by the pi bounds
    a, b = shares(PI_LO), shares(PI_HI)
    for i, pct in ((0, 186), (1, 249), (2, 158)):
        x, y = min(a[i], b[i]), max(a[i], b[i])
        assert F(pct * 10 - 5, 10000) <= x and y < F(pct * 10 + 5, 10000)
    return True


def check_viable_phase_bound():
    premise("dark-tower-matter.survival-sheets")
    pbound = F(2, 10 ** 16)
    lo, hi = F(141, 10 ** 10), F(142, 10 ** 10)
    assert lo ** 2 < pbound < hi ** 2
    assert F(135, 10 ** 10) <= lo and hi < F(145, 10 ** 10)    # rounds to 1.4e-8
    assert 1 / hi > 7 * 10 ** 7                                 # e^2/m > 7e7 (survival-sheets)
    return True


def check_coupling_dimension():
    premise("dark-tower-matter.gauge-algebras")
    dims = {}
    for d in (3, 4, 5):
        a_dim = F(d - 2, 2)
        e_dim = 1 - a_dim
        dims[d] = 2 * e_dim
    assert dims == {3: 1, 4: 0, 5: -1}
    return True
