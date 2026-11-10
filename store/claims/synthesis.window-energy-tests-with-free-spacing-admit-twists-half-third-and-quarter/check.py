"""The two window energy tests with the array's spacing left free: exact checks.

An array of window ratio r and twist delta has weights (kappa/r)(k + delta), k in Z, 0 < delta < 1; beta = 2 pi/kappa.
In units of kappa, with the symmetric (zeta-regularised) ordering:
  sea energy                      B_2(delta)/(2 r),            B_2(a) = a^2 - a + 1/6,
  continuum boost ground state    -r/24 over the window of r thermal periods (null ordering),
  thermal excitation energy       (1/r) sum_w w/(e^{2 pi w/r} + 1), w over k + delta and k + 1 - delta, k >= 0.
Ground test:  B_2(delta)/(2 r) + r/24 = 0.      Thermal test:  t(r, delta) := B_2(delta)/2 + sum_w w/(e^{2 pi w/r} + 1) = 0.
(1) the ground test is the conic (delta - 1/2)^2 = (1 - r^2)/12 (exact polynomial identity);
(2) the thermal test holds at (r^2, delta) = (1, 1/2), (1/4, 1/4), (2/3, 1/3) (rigorous rational enclosures of width
    below 10^-12; exact equality is the proof's eta-quotient argument) and fails at controls;
(3) entropies at the three points: (1/2) ln 2, (1/4) ln 2 and a value in (0.29379, 0.29380), that is 0.3598 per
    thermal period at twist 1/3 against (1/2) ln 2 < 0.3466 and pi/6 > 0.5235;
(4) with the parity clause (every beta omega an odd multiple of pi): r = 1/m, delta = (j + 1/2)/m, the ground test is
    m^2 - 3 n^2 = 1 with n = 2j + 1 - m, and the thermal test fails for every such m >= 7 (bound checked to m = 400).
"""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise

DEN = 10 ** 40
_PI = []


def _pi():
    if not _PI:
        lo, hi = series.pi_bracket(40)
        _PI.extend([lo, hi])
    return tuple(_PI)


def _B2(a):
    return a * a - a + F(1, 6)


def _scale(r2):
    """Rational bounds on 2 pi / r for r^2 = r2 (so 2 pi / r = 2 pi sqrt(1/r2))."""
    pl, pu = _pi()
    inv = 1 / F(r2)
    n, d = inv.numerator, inv.denominator
    if series.isqrt(n) ** 2 == n and series.isqrt(d) ** 2 == d:
        s_lo = s_hi = F(series.isqrt(n), series.isqrt(d))
    else:
        s_lo, s_hi = series.sqrt_bounds(inv, 30)
    return 2 * pl * s_lo, 2 * pu * s_hi


def _ws(delta, K):
    out = []
    for k in range(K):
        out.append(k + delta)
        out.append(k + 1 - delta)
    return out


def _thermal_sum(r2, delta, K=14):
    """Rigorous bounds on sum_w w/(e^{c w} + 1), c = 2 pi/r, over w = k + delta, k + 1 - delta, k >= 0."""
    cl, cu = _scale(r2)
    lo, hi = F(0), F(0)
    for w in _ws(delta, K):
        el = series.exp_bounds(cl * w)[0]
        eu = series.exp_bounds(cu * w)[1]
        lo += series.round_down(w / (eu + 1), DEN)
        hi += series.round_up(w / (el + 1), DEN)
    # tail: w >= K, w/(e^{c w} + 1) < w e^{-c w}; two towers, each below a geometric series of ratio 1/2
    eK = series.exp_bounds(cl * K)[0]
    hi += 2 * 2 * (K + 1) / eK
    return lo, hi


def _entropy(r2, delta, K=14):
    """Rigorous bounds on sum_w s(c w), s(x) = ln(1 + e^{-x}) + x/(e^{x} + 1), c = 2 pi/r."""
    cl, cu = _scale(r2)
    lo, hi = F(0), F(0)
    for w in _ws(delta, K):
        el = series.exp_bounds(cl * w)[0]
        eu = series.exp_bounds(cu * w)[1]
        # ln(1 + 1/e): e in [el, eu]
        a_lo = series.log_bounds(series.round_down(1 + 1 / eu, DEN))[0]
        a_hi = series.log_bounds(series.round_up(1 + 1 / el, DEN))[1]
        # x/(e^x + 1) is decreasing for x >= 2 (all arguments here exceed 2 pi/5 ... use both ends)
        cands = [cl * w / (el + 1), cl * w / (eu + 1), cu * w / (el + 1), cu * w / (eu + 1)]
        lo += series.round_down(a_lo + min(cands), DEN)
        hi += series.round_up(a_hi + max(cands), DEN)
    eK = series.exp_bounds(cl * K)[0]
    hi += 2 * 2 * (cu * (K + 1) + 1) / eK          # s(x) < (x + 1) e^{-x}
    return lo, hi


POINTS = ((F(1), F(1, 2)), (F(1, 4), F(1, 4)), (F(2, 3), F(1, 3)))


def check_ground_test_is_a_conic():
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")
    # B_2(delta)/(2r) + r/24 = ((delta - 1/2)^2 - (1 - r^2)/12)/(2r): polynomial identity, degree 2 in delta and
    # 1 in r^2 after clearing 2r; a 4 x 3 grid exceeds the degrees
    for delta in (F(1, 7), F(2, 5), F(1, 2), F(5, 6)):
        for r2 in (F(1, 9), F(3, 4), F(5, 2)):
            lhs = _B2(delta) + r2 / 12                      # 2r x (ground test)
            rhs = (delta - F(1, 2)) ** 2 - (1 - r2) / 12
            GA.check("ground test is the conic", lhs == rhs)
    for r2, delta in POINTS:
        GA.check("the three points lie on the conic", _B2(delta) + r2 / 12 == 0)
        GA.check("and their mirror twists", _B2(1 - delta) + r2 / 12 == 0)
    GA.check("stored case: B_2(1/2) = -1/12", _B2(F(1, 2)) == F(-1, 12))
    GA.check("B_2(1/4) = -1/48", _B2(F(1, 4)) == F(-1, 48))
    GA.check("B_2(1/3) = -1/18", _B2(F(1, 3)) == F(-1, 18))
    # off the conic: the window of one thermal period admits only the half twist (stored clause (ii))
    for delta in (F(1, 3), F(1, 4), F(2, 5)):
        GA.check("r = 1 excludes other twists", _B2(delta) + F(1, 12) != 0)
    GA.check("twist 1/6 lies on no real window", (F(1, 6) - F(1, 2)) ** 2 > F(1, 12))
    # no r > 1: (delta - 1/2)^2 >= 0 forces r^2 <= 1
    GA.check("no window longer than one thermal period", (1 - F(9, 4)) / 12 < 0)
    # particle-hole symmetric single arrays have twist 1/2 (twist 0 is excluded: B_2(0) = 1/6 > 0 meets no window)
    for r2, delta in POINTS:
        GA.check("only the half twist is its own mirror", (delta == 1 - delta) == (r2 == 1))
    GA.check("zero twist lies on no window", _B2(F(0)) + F(1, 12) > 0 and _B2(F(0)) > 0)
    return True


def _on_conic(delta):
    """r^2 of the conic point with twist delta."""
    return 1 - 12 * (delta - F(1, 2)) ** 2


TOL = F(1, 10 ** 12)
# controls (r^2, delta, sign of the thermal test value): two on the conic, three off it
CONTROLS = ((_on_conic(F(2, 5)), F(2, 5), -1), (_on_conic(F(3, 10)), F(3, 10), 1), (F(2, 3), F(1, 4), 1),
            (F(1, 4), F(1, 2), -1), (F(4), F(1, 2), 1))


def check_thermal_test_holds_at_three_points():
    premise("synthesis.imported-theta-function-identities")
    premise("synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r")                 # twist 1/2: r = 1 only
    premise("synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages")   # twist 1/4: the halves
    # excitation sums at the three points: 1/24 (the cited base's identity at r = 1), 1/96, 1/36
    targets = (F(1, 24), F(1, 96), F(1, 36))
    for (r2, delta), target in zip(POINTS, targets):
        lo, hi = _thermal_sum(r2, delta)
        GA.check("excitation sum enclosed", lo <= target <= hi and hi - lo < TOL)
        GA.check("it is minus half of B_2: the thermal test value is 0", target == -_B2(delta) / 2)
        GA.check("it is r^2/24: the excitation energy is kappa r/24", target == r2 / 24)
    for r2, delta, sign in CONTROLS:
        lo, hi = _thermal_sum(r2, delta)
        t_lo, t_hi = _B2(delta) / 2 + lo, _B2(delta) / 2 + hi
        GA.check("control: thermal test fails with the stated sign", (t_lo > 0) if sign > 0 else (t_hi < 0))
    return True


def check_entropies_at_the_three_points():
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    l2lo, l2hi = series.ln_bounds(2)
    pl, pu = _pi()
    tol = F(1, 10 ** 12)
    lo, hi = _entropy(F(1), F(1, 2))
    GA.check("half twist: (1/2) ln 2", lo <= l2lo / 2 and l2hi / 2 <= hi and hi - lo < tol)
    lo4, hi4 = _entropy(F(1, 4), F(1, 4))
    GA.check("quarter twist: (1/4) ln 2", lo4 <= l2lo / 4 and l2hi / 4 <= hi4 and hi4 - lo4 < tol)
    GA.check("quarter twist per thermal period: (1/2) ln 2", 2 * lo4 <= l2lo / 2 and l2hi / 2 <= 2 * hi4)
    lo3, hi3 = _entropy(F(2, 3), F(1, 3))
    GA.check("third twist: entropy in (0.29379, 0.29380)", F(29379, 100000) < lo3 and hi3 < F(29380, 100000))
    # per thermal period: S / r, r = sqrt(2/3), so (S/r)^2 = 3 S^2 / 2
    GA.check("third twist per thermal period above 0.3598", 3 * lo3 ** 2 / 2 > F(3598, 10000) ** 2)
    GA.check("third twist per thermal period below 0.3599", 3 * hi3 ** 2 / 2 < F(3599, 10000) ** 2)
    GA.check("it exceeds (1/2) ln 2", 3 * lo3 ** 2 / 2 > (l2hi / 2) ** 2)
    GA.check("and is below the continuum rate pi/6", 3 * hi3 ** 2 / 2 < (pl / 6) ** 2)
    GA.check("(1/2) ln 2 < 0.3466 and pi/6 > 0.5235", l2hi / 2 < F(3466, 10000) and pl / 6 > F(5235, 10000))
    # arrays per ln 2 at the third twist: not 2 and not an integer
    GA.check("ln 2 over the third-twist entropy lies in (2.35, 2.36)", F(235, 100) * hi3 < l2lo and l2hi < F(236, 100) * lo3)
    return True


def check_parity_clause_leaves_the_half_array_and_its_two_halves():
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")   # the ground test (sea energy, window value)
    premise("synthesis.q-splits-maximum-entropy-affine-weights")            # slope y = beta c = 2 pi/r: here y = 2 pi m
    # parity clause: 2 pi (k + delta)/r an odd multiple of pi for every k: 1/r = m an integer, delta = (j + 1/2)/m
    sols = []
    for m in range(1, 401):
        for j in range(m):
            delta = F(2 * j + 1, 2 * m)
            on_conic = _B2(delta) + F(1, 12 * m * m) == 0
            n = 2 * j + 1 - m
            GA.check("conic is the Pell equation m^2 - 3 n^2 = 1", on_conic == (m * m - 3 * n * n == 1))
            if on_conic:
                sols.append((m, j))
    GA.check("solutions up to m = 400", sorted(set(m for m, _ in sols)) == [1, 2, 7, 26, 97, 362])
    GA.check("m = 1: the half twist", [j for m, j in sols if m == 1] == [0])
    GA.check("m = 2: twists 1/4 and 3/4", [j for m, j in sols if m == 2] == [0, 1])
    # thermal test fails for m >= 7: sum_w w/(e^{2 pi m w} + 1) < 3 e^{-2 pi m/5} < 1/(24 m^2), every w > 1/5
    pl, pu = _pi()
    for m, j in sols:
        if m < 7:
            continue
        delta = F(2 * j + 1, 2 * m)
        GA.check("twist and mirror exceed 1/5", min(delta, 1 - delta) > F(1, 5))
        e = series.exp_bounds(2 * pl * m / 5)[0]
        GA.check("3 e^{-2 pi m/5} < 1/(24 m^2)", F(3) / e < F(1, 24 * m * m))
    # the bound's monotonicity step: m^2 e^{-2 pi m/5} decreases for m >= 2, since (1 + 1/m)^2 < e^{2 pi/5} there
    GA.check("(3/2)^2 < e^{2 pi/5}", F(9, 4) < series.exp_bounds(2 * pl / 5)[0])
    # direct enclosure at m = 7 (twist 3/14): the thermal test value is negative
    lo, hi = _thermal_sum(F(1, 49), F(3, 14))
    GA.check("m = 7: thermal test value is negative", _B2(F(3, 14)) / 2 + hi < 0)
    # the surviving half-array is half of the stored array: odd multiples of pi split 1, 5, 9, ... and 3, 7, 11, ...
    part = sorted([4 * k + 1 for k in range(6)] + [4 * k + 3 for k in range(6)])
    GA.check("the two half-arrays partition the half-twist weights", part == [2 * k + 1 for k in range(12)])
    return True


def check_odd_resonance_at_twist_one_third():
    """Remark 2: the stored evenness criterion (no vanishing signed sum of an odd number of weights)."""
    premise("synthesis.univalence-from-even-stationary-dynamics")
    w = lambda k, delta: k + delta
    third = F(1, 3)
    GA.check("twist 1/3: weights of k = 0, 1, -2 sum to zero", w(0, third) + w(1, third) + w(-2, third) == 0)
    GA.check("they are 1/3, 4/3, -5/3", (w(0, third), w(1, third), w(-2, third)) == (F(1, 3), F(4, 3), F(-5, 3)))
    # twists 1/2 and 1/4: every weight is an odd multiple of delta, so no signed sum of three vanishes (sampled range)
    for delta in (F(1, 2), F(1, 4)):
        ws = [w(k, delta) / delta for k in range(-6, 6)]
        GA.check("weights are odd multiples of the twist", all(x.denominator == 1 and x.numerator % 2 == 1 for x in ws))
        ok = True
        for a in ws:
            for b in ws:
                for c in ws:
                    for sb in (1, -1):
                        for sc in (1, -1):
                            if a + sb * b + sc * c == 0:
                                ok = False
        GA.check("no signed sum of three weights vanishes", ok)
    return True
