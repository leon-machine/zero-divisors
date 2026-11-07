"""synthesis.affine-cell-boost-spreads-without-scrambling: exact checks (Fractions).

One-particle space L^2(R_+, dU) restricted to functions constant on unit affine cells [j, j+1);
such a function is the vector of its cell values, and <f, g> = sum_j f_j g_j. The boost at
rapidity ln m acts as the dilation (D_m f)(U) = m^{-1/2} f(U/m); for m = 4 the factor is 1/2,
so D_4 maps cell-constant functions to cell-constant functions exactly:
(D_4 f)_l = f_{floor(l/4)} / 2. Checked:
  (a) D_4 is isometric, D_4 o D_4 = D_16 (the flow property at rapidities ln 4, ln 16);
  (b) the cell mode chi_j goes to 2^{-n} times the sum of 4^n consecutive cells after n steps:
      support 4^n = e^{lambda}, amplitude e^{-lambda/2}, norm 1;
  (c) every overlap <chi_k, D_4^n chi_j> (the CAR anticommutator {a(D^n chi_j), a*(chi_k)}) is 0 or
      2^{-n}: overlaps with a fixed cell decay as e^{-lambda/2};
  (d) on the log cells [4^i, 4^{i+1}) the same D_4 is a displacement: the normalised indicator of
      one log cell goes to that of the next (no spreading);
  (e) in the affine-cell basis D_4 is not diagonal: it moves weight from cell j to cells 4j..4j+3.
"""
import GA
from fractions import Fraction as F
from tp_premise import premise

L = 1024                       # cells kept; functions supported in [0, L)


def D(f, m=4, amp=F(1, 2)):
    """dilation by m on cell-constant vectors; amp = m^{-1/2} (exact for m = 4, 16)"""
    out = [F(0)] * L
    for l in range(L):
        out[l] = amp * f[l // m]
    return out


def chi(j):
    v = [F(0)] * L
    v[j] = F(1)
    return v


def ip(f, g):
    return sum((x * y for x, y in zip(f, g)), F(0))


def support(f):
    return [i for i, x in enumerate(f) if x != 0]


def check_affine_cells_spread_at_rate_kappa():
    premise("synthesis.phase-flow-is-time-rotor-flow-kms-continuation")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    # (a) isometry on the cells that stay inside the window, and the flow property
    for j in (0, 1, 3, 7):
        f = chi(j)
        assert ip(D(f), D(f)) == 1
        assert D(D(f)) == D(f, 16, F(1, 4))
    g = [F(0)] * L
    g[2], g[5], g[9] = F(3), F(-1, 2), F(2, 7)
    assert ip(D(g), D(g)) == ip(g, g)
    # (b) support and amplitude after n steps, for a cell mode
    for j in (1, 2):
        f = chi(j)
        for n in range(1, 5):
            f = D(f)
            s = support(f)
            assert len(s) == 4 ** n and s == list(range(j * 4 ** n, (j + 1) * 4 ** n))
            assert all(f[i] == F(1, 2 ** n) for i in s)
            assert ip(f, f) == 1
            # (c) overlaps with any fixed cell: 0 or 2^-n
            assert {f[k] for k in range(L)} <= {F(0), F(1, 2 ** n)}
    # cells needed to cover N cells from one: N = 4^n at rapidity n ln 4, i.e. kappa t = ln N
    assert [4 ** n for n in range(1, 5)] == [4, 16, 64, 256]
    GA.check("the rapidity-ln4 boost spreads one affine cell over 4 cells at amplitude 1/2; after n steps "
             "4^n cells at 2^-n, norm 1, every fixed-cell overlap 0 or 2^-n", True)


def check_log_cells_are_displaced_and_generator_hops():
    premise("synthesis.phase-flow-is-time-rotor-flow-kms-continuation")
    premise("angle.imported-theorems-deliver-their-hypotheses")

    def log_cell(i):
        v = [F(0)] * L
        for l in range(4 ** i, 4 ** (i + 1)):
            v[l] = F(1)
        return v
    for i in range(0, 4):
        x, y = log_cell(i), log_cell(i + 1)
        assert ip(y, y) == 4 * ip(x, x)                          # normalisations differ by 2
        assert D(x) == [F(1, 2) * t for t in y]                  # D(1_i) = (1/2) 1_{i+1}: normalised map i -> i+1
        assert ip(D(x), D(x)) == ip(x, x)
    # (e) in affine cells the map is off-diagonal: weight leaves cell j (j >= 1)
    for j in (1, 5, 20):
        f = D(chi(j))
        assert f[j] == 0 and ip(f, chi(4 * j)) == F(1, 2)
    GA.check("on log cells the boost displaces (i -> i+1, no spreading); on affine cells it is off-diagonal "
             "(moves weight from cell j to cells 4j..4j+3)", True)
