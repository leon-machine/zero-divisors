"""standard-model.chain: exact checks of parts (1) to (3); part (4) is at record level.

Coefficients from component listings: a field is (representation per factor, multiplicity), SU(N)
representations '1', 'N', 'Nb', 'adj', 'sym' with (dimension, index T, Casimir C) = (1, 0, 0), (N, 1/2,
(N^2 - 1)/2N), (N^2 - 1, N, N), (N(N+1)/2, (N+2)/2, (N-1)(N+2)/N), and U(1) entries Y with T = C = (3/5) Y^2.
b_i = -(11/3) C(G_i) + (2/3) sum_Weyl T_i + (1/3) sum_scalars T_i (T_i weighted by the other dimensions), and
the two-loop matrix by the generic formula of the two-loop Fact.
(1) Standard Model listing (three generations, one Higgs doublet): b = (41/10, -19/6, -7) and the Fact's
    two-loop matrix (a test of the routine). Pati-Salam (4, 2L, 2R), three generations (4,2,1) + (4b,1,2),
    the complex (10,1,3) and the bidoublet (1,2,2): b = (-23/3, -19/6, 7/2) real, (-23/3, -3, 11/3) complex,
    (-7/3, 2, 26/3) complex with the (15,2,2), and the stated two-loop matrix in the last case.
(2) One loop with the matching a_1 = (3/5) a_2R + (2/5) a_4, a_2 = a_2L, a_3 = a_4 at M_I and the inputs of
    the spectrum run: a_i(M_Z) = a_U + b_i^SM x + b_i^eff y solved exactly (Cramer) and substituted back:
    the stated x, y; a_U = alpha_U^-1 = 46.12, 45.69, 37.11 to two places; and, with certified bounds
    (pi from Machin's formula with alternating-series bounds, exp from Taylor polynomials with remainder
    bounds, all rational) and M_Z = 91.1876 GeV (the record's value, an input not stored as an entity),
    M_I = M_Z e^(2 pi x) and M_U = M_Z e^(2 pi (x + y)) round to the stated two significant figures.
(3) The real-bidoublet chain as a one-threshold shift: Delta = b^eff - b^SM = (-76/15, 0, -2/3), equal to the
    extra gauge bosons (-154/15, 0, -11/3) plus the (10,1,3) (26/5, 0, 3) (fermions and the bidoublet's
    light doublet cancel against the Standard Model's); f = y/(x + y) = 5610391/17511460 = 0.320, equal to
    the theorem's (R b_23 - b_12)/(Delta_12 - R Delta_23); and (1 + R) Delta_2 > Delta_1 + R Delta_3.
(4) is a numerical two-loop integration at record level and is not tested here.
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

H = F(1, 2)
SM_GROUPS = [("U1",), ("SU", 2), ("SU", 3)]
PS_GROUPS = [("SU", 4), ("SU", 2), ("SU", 2)]
GEN = [((F(1, 6), "N", "N"), 1), ((F(-1, 2), "N", "1"), 1), ((F(-2, 3), "1", "Nb"), 1),
       ((F(1, 3), "1", "Nb"), 1), ((F(1), "1", "1"), 1), ((F(0), "1", "1"), 1)]
SM_WEYL = [(r, 3 * m) for r, m in GEN]
SM_SCALAR = [((H, "N", "1"), 1)]
PS_WEYL = [(("N", "N", "1"), 3), (("Nb", "1", "N"), 3)]
CHAINS = {
    "real": [(("1", "N", "N"), H), (("sym", "1", "adj"), 1)],
    "complex": [(("1", "N", "N"), 1), (("sym", "1", "adj"), 1)],
    "complex15": [(("1", "N", "N"), 1), (("sym", "1", "adj"), 1), (("adj", "N", "N"), 1)],
}
INPUTS = (F(128), F(2312, 10000), F(500, 59))
MZ = F(911876, 10000)


def su_rep(N, name):
    if name == "1":
        return (1, F(0), F(0))
    if name in ("N", "Nb"):
        return (N, H, F(N * N - 1, 2 * N))
    if name == "adj":
        return (N * N - 1, F(N), F(N))
    return (N * (N + 1) // 2, F(N + 2, 2), F((N - 1) * (N + 2), N))


def data(groups, rep):
    dims, T, C = [], [], []
    for g, r in zip(groups, rep):
        if g[0] == "U1":
            dims.append(1)
            T.append(F(3, 5) * r * r)
            C.append(F(3, 5) * r * r)
        else:
            d, t, c = su_rep(g[1], r)
            dims.append(d)
            T.append(t)
            C.append(c)
    return dims, T, C


def weighted_T(groups, rep, i):
    dims, T, C = data(groups, rep)
    w = T[i]
    for k, d in enumerate(dims):
        if k != i:
            w *= d
    return w


def coeffs(groups, weyl, scal):
    n = len(groups)
    CG = [F(0) if g[0] == "U1" else F(g[1]) for g in groups]
    b, B = [], [[F(0)] * n for _ in range(n)]
    for i in range(n):
        tw = sum((m * weighted_T(groups, r, i) for r, m in weyl), F(0))
        ts = sum((m * weighted_T(groups, r, i) for r, m in scal), F(0))
        b.append(-F(11, 3) * CG[i] + F(2, 3) * tw + F(1, 3) * ts)
        for j in range(n):
            s = F(0)
            if i == j:
                s += -F(34, 3) * CG[i] ** 2 + F(10, 3) * CG[i] * tw + F(2, 3) * CG[i] * ts
            s += sum((2 * m * weighted_T(groups, r, i) * data(groups, r)[2][j] for r, m in weyl), F(0))
            s += sum((4 * m * weighted_T(groups, r, i) * data(groups, r)[2][j] for r, m in scal), F(0))
            B[i][j] = s
    return b, B


def record():
    A, s2, a3 = INPUTS
    a2 = s2 * A
    return (F(3, 5) * (A - a2), a2, a3)


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def solve_chain(bPS, bSM):
    beff = [F(3, 5) * bPS[2] + F(2, 5) * bPS[0], bPS[1], bPS[0]]
    a = record()
    M = [[F(1), bSM[i], beff[i]] for i in range(3)]
    d = det3(M)
    sol = []
    for k in range(3):
        Mk = [[a[i] if j == k else M[i][j] for j in range(3)] for i in range(3)]
        sol.append(det3(Mk) / d)
    aU, x, y = sol
    back = all(aU + bSM[i] * x + beff[i] * y == a[i] for i in range(3))
    return aU, x, y, beff, back


# certified rational bounds -------------------------------------------------------------------------

def gev_bounds(x):
    """Certified bounds on M_Z e^(2 pi x), x >= 0 (series.pi_bounds, series.exp_bounds)."""
    p_lo, p_hi = series.pi_bounds()
    return MZ * series.exp_bounds(2 * p_lo * x)[0], MZ * series.exp_bounds(2 * p_hi * x)[1]


def rounds_to(lo, hi, mant, exp10):
    """[lo, hi] lies inside the rounding interval of mant x 10^exp10 (mant with one decimal)."""
    c = F(mant, 10) * F(10) ** exp10
    half = F(1, 20) * F(10) ** exp10
    return c - half <= lo and hi < c + half


# checks ---------------------------------------------------------------------------------------------

def check_one_and_two_loop_coefficients():
    premise("standard-model.imported-coefficient-sum-indices")
    premise("standard-model.imported-two-loop-gauge-coefficients")
    premise("standard-model.imported-pati-salam-representation-theory-survival")
    premise("standard-model.majorana-element")
    premise("standard-model.left-right-parity-what-breaks-it")
    premise("standard-model.hyp-s-slot-statistics")
    bSM, BSM = coeffs(SM_GROUPS, SM_WEYL, SM_SCALAR)
    ok = bSM == [F(41, 10), F(-19, 6), F(-7)]
    ok = ok and BSM == [[F(199, 50), F(27, 10), F(44, 5)], [F(9, 10), F(35, 6), F(12)], [F(11, 10), F(9, 2), F(-26)]]
    co = {k: coeffs(PS_GROUPS, PS_WEYL, v) for k, v in CHAINS.items()}
    ok = ok and co["real"][0] == [F(-23, 3), F(-19, 6), F(7, 2)]
    ok = ok and co["complex"][0] == [F(-23, 3), F(-3), F(11, 3)]
    ok = ok and co["complex15"][0] == [F(-7, 3), F(2), F(26, 3)]
    ok = ok and co["complex15"][1] == [[F(2435, 6), F(105, 2), F(249, 2)], [F(525, 2), F(73), F(48)],
                                        [F(1245, 2), F(48), F(779, 3)]]
    GA.check("one- and two-loop coefficients of the three Pati-Salam chains", ok)
    return ok


def check_one_loop_chain_solutions():
    premise("standard-model.matching-traces")
    premise("standard-model.spectrum-run")
    premise("standard-model.imported-coefficient-sum-indices")
    bSM, _ = coeffs(SM_GROUPS, SM_WEYL, SM_SCALAR)
    want = {"real": (F(11901069, 3355625), F(5610391, 3355625), F(4612, 100), (43, 11), (16, 16)),
            "complex": (F(25548992, 7116875), F(11220782, 7116875), F(4569, 100), (57, 11), (11, 16)),
            "complex15": (F(22055284, 6305625), F(11220782, 6305625), F(3711, 100), (32, 11), (23, 16))}
    ok = True
    for k, (x0, y0, aU0, mi, mu) in want.items():
        bPS = coeffs(PS_GROUPS, PS_WEYL, CHAINS[k])[0]
        aU, x, y, beff, back = solve_chain(bPS, bSM)
        ok = ok and back and x == x0 and y == y0 and abs(aU - aU0) < F(1, 200)
        ok = ok and x > 0 and y > 0 and aU > 0
        lo, hi = gev_bounds(x)
        ok = ok and rounds_to(lo, hi, mi[0], mi[1])
        lo, hi = gev_bounds(x + y)
        ok = ok and rounds_to(lo, hi, mu[0], mu[1])
    GA.check("the one-loop chains meet at the stated exact x, y, alpha_U^-1, M_I and M_U", ok)
    return ok


def check_real_chain_as_one_threshold_shift():
    premise("standard-model.one-threshold-exact-criterion")
    premise("standard-model.direction-demanded-content-doublet-heavy")
    premise("standard-model.imported-coefficient-sum-indices")
    bSM, _ = coeffs(SM_GROUPS, SM_WEYL, SM_SCALAR)
    bPS = coeffs(PS_GROUPS, PS_WEYL, CHAINS["real"])[0]
    aU, x, y, beff, back = solve_chain(bPS, bSM)
    D = [beff[i] - bSM[i] for i in range(3)]
    ok = back and D == [F(-76, 15), F(0), F(-2, 3)]
    # gauge bosons: Pati-Salam adjoints projected minus the Standard Model's
    gPS = [-F(11, 3) * 4, -F(11, 3) * 2, -F(11, 3) * 2]
    gSM = [F(0), -F(11, 3) * 2, -F(11, 3) * 3]
    gauge = [F(3, 5) * gPS[2] + F(2, 5) * gPS[0] - gSM[0], gPS[1] - gSM[1], gPS[0] - gSM[2]]
    with_t = coeffs(PS_GROUPS, [], [(("sym", "1", "adj"), 1)])[0]
    bare = coeffs(PS_GROUPS, [], [])[0]
    t = [with_t[i] - bare[i] for i in range(3)]
    ok = ok and bare == gPS
    trip = [F(3, 5) * t[2] + F(2, 5) * t[0], t[1], t[0]]
    ok = ok and gauge == [F(-154, 15), F(0), F(-11, 3)] and trip == [F(26, 5), F(0), F(3)]
    ok = ok and [gauge[i] + trip[i] for i in range(3)] == D
    a1, a2, a3 = record()
    R = (a1 - a2) / (a2 - a3)
    b12, b23 = bSM[0] - bSM[1], bSM[1] - bSM[2]
    f = y / (x + y)
    ok = ok and f == F(5610391, 17511460) and abs(f - F(32, 100)) < F(1, 200)
    ok = ok and f == (R * b23 - b12) / ((D[0] - D[1]) - R * (D[1] - D[2]))
    ok = ok and (1 + R) * D[1] > D[0] + R * D[2] and min(D) < 0
    GA.check("the real-bidoublet chain is the one-threshold shift (-76/15, 0, -2/3) at f = 0.320", ok)
    return ok
