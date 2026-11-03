"""standard-model.supersymmetric-row-two-loops: exact checks.

Exact part. The two-loop matrices are rebuilt from the component listings by the two formulas of
the imported Fact (generic Weyl/scalar formula below the threshold, superfield formula above) and
compared with the quoted matrices; the generic formula on the supersymmetric components does not
return the supersymmetric matrix (it omits the gaugino-matter Yukawas).

Run. The two-loop equations with the top Yukawa, d g_i^2/dt = g_i^4/(8 pi^2) (b_i + B_ij g_j^2/(16
pi^2) - c_i y_t^2/(16 pi^2)) and the one-loop y_t equation, are integrated by classical RK4 in
fixed-point integer arithmetic (96 fractional bits, no floating point), step 1/8 in t = ln(mu/M_Z),
from the record's central values (alpha_em^-1 = 127.951, sin^2 = 0.23122, alpha_s = 0.1180,
y_t(M_Z) = 0.95), switching to the supersymmetric coefficients at t_I = ln(M_I/M_Z); a_1 = a_2 is
located by bisection and the mismatch a_3 - a_1 there is recorded. A claimed M_I is confirmed by
a sign change of the mismatch between two rational t_I bracketing it; the brackets' GeV values
come from rigorous rational bounds on pi (Machin) and exp (Taylor with remainder), and must round
to the stated figures. M_U and alpha_U^-1 at both ends must round to 1.1 x 10^16 GeV and 25.7.
The shifts (alpha_s +- 0.0009, Yukawa off, y_t = 0.99, sin beta = 0.9, sin^2 + 0.0001) are each
bracketed the same way and their differences from the central bracket must round to the stated
shifts. Control: with the two-loop and Yukawa terms off, the integrator's threshold brackets the
exact one-loop value 2 pi x (1 - f) of the full supersymmetric content to 10^-5 in t, 62.1 GeV.
The integration is a numerical method in exact arithmetic: its truncation error (about 10^-9 in
the mismatch, compared at steps 1/4, 1/8, 1/16 when the check was written) is far below the
mismatch at the brackets (about 5 x 10^-5).
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

# ---------------------------------------------------------------------------
# rigorous rational bounds for pi and exp
# ---------------------------------------------------------------------------


def pi_bounds():
    return series.pi_bracket(40)       # Machin, 40 alternating terms per arctan


def exp_bounds(t):
    """lo <= e^t <= hi, rational, rigorous (series.exp_bounds; the reciprocal for t < 0)."""
    t = F(t)
    if t < 0:
        lo, hi = series.exp_bounds(-t)
        return 1 / hi, 1 / lo
    return series.exp_bounds(t)


PI_LO, PI_HI = pi_bounds()
MZ = F(911876, 10000)


def gev(t_lo, t_hi):
    """Rigorous GeV interval for M_Z e^t, t in [t_lo, t_hi]."""
    return MZ * exp_bounds(t_lo)[0], MZ * exp_bounds(t_hi)[1]


def rounds_to(lo, hi, mant, e):
    """Every value in [lo, hi] rounds to mant x 10^e."""
    u = F(10) ** e
    return (mant - F(1, 2)) * u <= lo and hi < (mant + F(1, 2)) * u


# ---------------------------------------------------------------------------
# component listings and the two-loop formulas
# ---------------------------------------------------------------------------
WEYL, SC = "weyl", "scalar"
H = F(1, 2)
CG = (F(0), F(2), F(3))
GEN = [("Q", WEYL, 2, H, 3, H, F(1, 6), 1), ("L", WEYL, 2, H, 1, 0, F(-1, 2), 1),
       ("u^c", WEYL, 1, 0, 3, H, F(-2, 3), 1), ("d^c", WEYL, 1, 0, 3, H, F(1, 3), 1),
       ("e^c", WEYL, 1, 0, 1, 0, F(1), 1), ("nu^c", WEYL, 1, 0, 1, 0, F(0), 1)]
SM = [(n, k, d2, T2, d3, T3, Y, 3 * m) for (n, k, d2, T2, d3, T3, Y, m) in GEN] + [("H", SC, 2, H, 1, 0, H, 1)]
GAUGINOS = [("gluino", WEYL, 1, 0, 8, F(3), F(0), 1), ("wino", WEYL, 3, F(2), 1, 0, F(0), 1),
            ("bino", WEYL, 1, 0, 1, 0, F(0), 1)]
HIGGSINOS = [("Hu~", WEYL, 2, H, 1, 0, H, 1), ("Hd~", WEYL, 2, H, 1, 0, -H, 1)]
MSSM = (SM + GAUGINOS + HIGGSINOS + [("H2", SC, 2, H, 1, 0, -H, 1)]
        + [(n, SC, d2, T2, d3, T3, Y, 3 * m) for (n, k, d2, T2, d3, T3, Y, m) in GEN])
CHIRAL = ([(n, WEYL, d2, T2, d3, T3, Y, 3 * m) for (n, k, d2, T2, d3, T3, Y, m) in GEN]
          + [("Hu", WEYL, 2, H, 1, 0, H, 1), ("Hd", WEYL, 2, H, 1, 0, -H, 1)])


def casimirs(fd):
    _, kind, d2, T2, d3, T3, Y, m = fd
    return (F(3, 5) * Y * Y, {1: F(0), 2: F(3, 4), 3: F(2)}[d2], {1: F(0), 3: F(4, 3), 8: F(3)}[d3])


def tidx(fd):
    _, kind, d2, T2, d3, T3, Y, m = fd
    return (F(3, 5) * Y * Y * d2 * d3 * m, T2 * d3 * m, T3 * d2 * m)


def b_generic(fields):
    B = [[F(0)] * 3 for _ in range(3)]
    for i in range(3):
        B[i][i] += -F(34, 3) * CG[i] ** 2
        for fd in fields:
            T, C = tidx(fd), casimirs(fd)
            wC, wG = (F(2), F(10, 3)) if fd[1] == WEYL else (F(4), F(2, 3))
            for j in range(3):
                B[i][j] += T[i] * (wC * C[j] + (wG * CG[i] if i == j else 0))
    return B


def b_superfield(chiral):
    B = [[F(0)] * 3 for _ in range(3)]
    for i in range(3):
        B[i][i] += -6 * CG[i] ** 2
        for fd in chiral:
            T, C = tidx(fd), casimirs(fd)
            for j in range(3):
                B[i][j] += 4 * T[i] * C[j] + (2 * CG[i] * T[i] if i == j else 0)
    return B


# ---------------------------------------------------------------------------
# the run, in fixed-point integer arithmetic
# ---------------------------------------------------------------------------
P = 96
ONE = 1 << P


def fx(q):
    q = F(q)
    return (q.numerator << P) // q.denominator


def fmul(a, b):
    return (a * b) >> P


def fdiv(a, b):
    return (a << P) // b


PI = fx((PI_LO + PI_HI) / 2)
KK = fmul(16 * PI, PI)
QUOTED = {False: ((F(199, 50), F(27, 10), F(44, 5)), (F(9, 10), F(35, 6), F(12)), (F(11, 10), F(9, 2), F(-26))),
          True: ((F(199, 25), F(27, 5), F(88, 5)), (F(9, 5), F(25), F(24)), (F(11, 5), F(9), F(14)))}
ONE_LOOP = {False: (F(41, 10), F(-19, 6), F(-7)), True: (F(33, 5), F(1), F(-3))}
CY = {False: (F(17, 10), F(3, 2), F(2)), True: (F(26, 5), F(6), F(4))}
YT = {False: (F(9, 2), F(17, 20), F(9, 4), F(8)), True: (F(6), F(13, 15), F(3), F(16, 3))}
CX = {s: ([fx(v) for v in ONE_LOOP[s]], [[fx(v) for v in r] for r in QUOTED[s]],
          [fx(v) for v in CY[s]], [fx(v) for v in YT[s]]) for s in (False, True)}
CENTRAL = dict(aem_inv=F(127951, 1000), s2=F(23122, 100000), as_inv=F(10000, 1180), yt0=F(95, 100))
STEP = F(1, 8)
T_MAX = fx(45)      # no crossing below 10^21 GeV: no meeting


def deriv(Y, susy, yuk, two):
    G, yt = Y[:3], Y[3]
    b, B, c, ycoef = CX[susy]
    yt2 = fmul(yt, yt)
    out = []
    for i in range(3):
        inner = b[i]
        if two:
            inner += fdiv(sum(fmul(B[i][j], G[j]) for j in range(3)), KK)
            if yuk:
                inner -= fdiv(fmul(c[i], yt2), KK)
        out.append(fdiv(2 * fmul(fmul(G[i], G[i]), inner), KK))
    y0, y1, y2, y3 = ycoef
    out.append(fdiv(fmul(yt, fmul(y0, yt2) - fmul(y1, G[0]) - fmul(y2, G[1]) - fmul(y3, G[2])), KK))
    return out


def rk4(Y, h, *a):
    k1 = deriv(Y, *a)
    k2 = deriv([y + fmul(h, k) // 2 for y, k in zip(Y, k1)], *a)
    k3 = deriv([y + fmul(h, k) // 2 for y, k in zip(Y, k2)], *a)
    k4 = deriv([y + fmul(h, k) for y, k in zip(Y, k3)], *a)
    return [y + fmul(h, p + 2 * q + 2 * r + s) // 6 for y, p, q, r, s in zip(Y, k1, k2, k3, k4)]


def run(tI, aem_inv, s2, as_inv, yt0, yuk=True, two=True, sinb=F(1)):
    """Mismatch a_3 - a_1 at the a_1 = a_2 crossing, the crossing t_c, and a_1 there."""
    aem = 1 / aem_inv
    Y = [fmul(4 * PI, fx(a)) for a in (F(5, 3) * aem / (1 - s2), aem / s2, 1 / as_inv)] + [fx(yt0)]
    n = int(abs(tI) / STEP) + 1
    h = fx(tI / n)
    for _ in range(n):
        Y = rk4(Y, h, False, yuk, two)
    Y[3] = fdiv(Y[3], fx(sinb))
    t, Hx = fx(tI), fx(STEP)

    def d12(Z):
        return fdiv(4 * PI, Z[0]) - fdiv(4 * PI, Z[1])
    while True:
        Z = rk4(Y, Hx, True, yuk, two)
        if d12(Z) <= 0:
            break
        Y, t = Z, t + Hx
        if t > T_MAX or min(Z[:3]) <= 0:
            return None
    lo, hi = 0, Hx
    while hi - lo > ONE >> 36:
        mid = (lo + hi) // 2
        if d12(rk4(Y, mid, True, yuk, two)) > 0:
            lo = mid
        else:
            hi = mid
    Z = rk4(Y, lo, True, yuk, two)
    a = [fdiv(4 * PI, g) for g in Z[:3]]
    return F(a[2] - a[0], ONE), F(t + lo, ONE), F(a[0], ONE)


def bracket(t_lo, t_hi, **kw):
    """Confirms a meeting threshold in [t_lo, t_hi]: (M_I interval, M_U interval, a_U interval)."""
    inp = dict(CENTRAL)
    inp.update(kw)
    r1, r2 = run(t_lo, **inp), run(t_hi, **inp)
    if r1 is None or r2 is None:
        return None
    (m1, tc1, a1), (m2, tc2, a2) = r1, r2
    if not (m1 > 0 > m2):
        return None
    return gev(t_lo, t_hi), gev(min(tc1, tc2), max(tc1, tc2)), (min(a1, a2), max(a1, a2))


# rational threshold brackets t_I = ln(M_I/M_Z) (located by a float scan when the check was written)
T_CENTRAL = (F(32094, 10000), F(32099, 10000))
T_AS_UP = (F(29335, 10000), F(29340, 10000))       # alpha_s = 0.1189
T_AS_DOWN = (F(34898, 10000), F(34903, 10000))     # alpha_s = 0.1171
T_YUK_OFF = (F(33472, 10000), F(33477, 10000))
T_YT99 = (F(31839, 10000), F(31844, 10000))
T_SINB = (F(31393, 10000), F(31398, 10000))
T_S2UP = (F(30840, 10000), F(30845, 10000))


def central():
    return bracket(*T_CENTRAL)


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------


def check_two_loop_matrices_from_the_formulas():
    premise("standard-model.imported-two-loop-gauge-coefficients")
    premise("standard-model.hyp-s-slot-statistics")
    ok = b_generic(SM) == [[F(199, 50), F(27, 10), F(44, 5)], [F(9, 10), F(35, 6), F(12)],
                           [F(11, 10), F(9, 2), F(-26)]]
    ok = ok and b_superfield(CHIRAL) == [[F(199, 25), F(27, 5), F(88, 5)], [F(9, 5), F(25), F(24)],
                                         [F(11, 5), F(9), F(14)]]
    ok = ok and b_generic(MSSM) != b_superfield(CHIRAL)
    # without the lepton doublet the generic matrix is not the Standard Model's
    noL = [fd for fd in SM if fd[0] != "L"]
    ok = ok and b_generic(noL)[1][1] != F(35, 6)
    GA.check("two loops: the SM and MSSM matrices from the component listings; generic != superfield", ok)
    return ok


def check_integrator_against_exact_one_loop():
    premise("standard-model.imported-two-loop-gauge-coefficients")
    # exact one-loop threshold of the full supersymmetric content at T12's inputs
    a_em, s2, a_s = F(128), F(2312, 10000), F(500, 59)
    A = (F(3, 5) * (a_em - s2 * a_em), s2 * a_em, a_s)
    b, d = ONE_LOOP[False], (F(5, 2), F(25, 6), F(4))
    D12, D23 = A[0] - A[1], A[1] - A[2]
    b12, b23, d12, d23 = b[0] - b[1], b[1] - b[2], d[0] - d[1], d[1] - d[2]
    det = b12 * d23 - b23 * d12
    x, y = (D12 * d23 - D23 * d12) / det, (b12 * D23 - b23 * D12) / det
    w = x - y                                  # t_I = 2 pi (x - y) < 0: below M_Z
    ok = w < 0
    t_lo, t_hi = 2 * PI_HI * w - F(1, 10 ** 5), 2 * PI_LO * w + F(1, 10 ** 5)
    kw = dict(aem_inv=a_em, s2=s2, as_inv=a_s, yt0=F(95, 100), yuk=False, two=False)
    r1, r2 = run(t_lo, **kw), run(t_hi, **kw)
    ok = ok and r1 is not None and r2 is not None and r1[0] > 0 > r2[0]
    lo, hi = gev(t_lo, t_hi)
    ok = ok and rounds_to(lo, hi, 621, -1)
    GA.check("two loops (control): one-loop integration brackets the exact threshold 62.1 GeV to 1e-5 in t", ok)
    return ok


def check_central_meeting_point():
    premise("standard-model.imported-two-loop-gauge-coefficients")
    premise("standard-model.hyp-s-slot-statistics")
    r = central()
    ok = r is not None
    if ok:
        (mi_lo, mi_hi), (mu_lo, mu_hi), (au_lo, au_hi) = r
        ok = rounds_to(mi_lo, mi_hi, 23, 2)            # M_I = 2.3 TeV
        ok = ok and rounds_to(mu_lo, mu_hi, 11, 15)    # M_U = 1.1 x 10^16 GeV
        ok = ok and rounds_to(au_lo, au_hi, 257, -1)   # alpha_U^-1 = 25.7
        ok = ok and mi_lo > 1000 and mi_hi < 10000     # low TeV range: admissible at two loops
    GA.check("two loops: the couplings meet exactly at M_I = 2.3 TeV, M_U = 1.1e16 GeV, alpha_U^-1 = 25.7", ok)
    return ok


def check_alpha_s_range():
    premise("standard-model.imported-two-loop-gauge-coefficients")
    premise("standard-model.hyp-s-slot-statistics")
    up = bracket(*T_AS_UP, as_inv=F(10000, 1189))
    down = bracket(*T_AS_DOWN, as_inv=F(10000, 1171))
    ok = up is not None and down is not None
    if ok:
        ok = rounds_to(up[0][0], up[0][1], 17, 2) and rounds_to(down[0][0], down[0][1], 30, 2)
    GA.check("two loops: M_I moves between 1.7 and 3.0 TeV across alpha_s = 0.1180 +- 0.0009", ok)
    return ok


def check_threshold_shifts():
    premise("standard-model.imported-two-loop-gauge-coefficients")
    premise("standard-model.hyp-s-slot-statistics")
    c = central()
    ok = c is not None
    shifts = [(bracket(*T_YUK_OFF, yuk=False), 3, -1),                 # 0.3 TeV, Yukawa off
              (bracket(*T_YT99, yt0=F(99, 100)), 6, -2),               # 0.06 TeV, y_t = 0.99
              (bracket(*T_SINB, sinb=F(9, 10)), 15, -2),               # 0.15 TeV, sin beta = 0.9
              (bracket(*T_S2UP, s2=F(23132, 100000)), 27, -2)]         # 0.27 TeV, sin^2 + 0.0001
    for r, mant, e in shifts:
        ok = ok and r is not None
        if ok:
            # |Delta M_I| in TeV, as an interval
            d1, d2 = abs(c[0][0] - r[0][1]), abs(c[0][1] - r[0][0])
            ok = ok and rounds_to(min(d1, d2) / 1000, max(d1, d2) / 1000, mant, e)
    GA.check("two loops: shifts of M_I by 0.3, 0.06, 0.15 and 0.27 TeV under the four variations", ok)
    return ok


EXPORTS = {"central": central, "gev": gev, "exp_bounds": exp_bounds, "pi_bounds": pi_bounds,
           "rounds_to": rounds_to}
