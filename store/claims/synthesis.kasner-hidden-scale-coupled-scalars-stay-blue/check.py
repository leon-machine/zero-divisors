"""synthesis.kasner-hidden-scale-coupled-scalars-stay-blue: exact checks.

Diagonal field near a wall, derived metric d tau^2 - sum_j tau^(2 p_j) (dx^j)^2 over three observed directions
and one hidden direction y, with b = tau^(p_h) and sum p = 1. A scalar whose four-dimensional action carries
b^lambda, S = int d tau d^3x sqrt|g_4| b^lambda (-(1/2) g^(mu nu) d phi d phi), has along the principal axis i
phi'' + (alpha/tau) phi' + k^2 tau^(-2 p_i) phi = 0 with alpha = 1 + (lambda - 1) p_h.
(1) Reduction weights (GA, Cl(1,4)): sqrt|g_5| = sqrt|g_4| b, and the y-y entry of the inverse derived metric is
    -1/b^2, so a five-dimensional massless scalar's zero mode has lambda = 1, the Wilson-line component A_y of a
    five-dimensional gauge field lambda = -1, a field confined to the observed directions lambda = 0.
(2) Bessel order: phi = tau^a f(s), a = (1 - alpha)/2, s = k tau^q/q, q = 1 - p_i, turns the equation into
    Bessel's of order nu = |a|/q = |lambda - 1| |p_h|/(2q), checked on formal terms s^n (ln s)^m.
(3) Normalisation: alpha + 2a = 1, so the adiabatic normalisation |N|^2 = pi/(4q) is free of k; superhorizon
    Y_nu ~ s^(-nu) gives n - 1 = 3 - 2 nu for nu > 0.
(4) Equal observed exponents: on the vacuum sphere only p = 0 (Milne) and p = 1/2 ((1/2,1/2,1/2,-1/2)); on the
    stiff disk the segment 0 <= p <= 1/2; there |1 - 3p|/(1 - p) <= 1, so nu <= |lambda - 1|/2.
(5) Every point of the ball (sum p = 1, sum p^2 <= 1 over four directions): a single exponent lies in [-1/2, 1],
    and for |lambda - 1| <= 2 some observed axis has nu <= 1 (sampled on a grid, worst case lambda = -1).
(6) The stored fields have lambda in {0, -1} and the generic bulk entry 1: nu <= 1 and n - 1 >= 1. A red index
    needs |lambda - 1| > 3. The towers' gauge vector zero modes (weight b) have order p/(1 - p) <= 1.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

NS1, SIG = F("-0.0351"), F("0.0042")
SQ5 = (1, -1, -1, -1, -1)          # Cl(1,4): e0 time, e1..e3 observed, e4 the hidden direction


# ---------------- formal terms: dict (e, m) -> c meaning c tau^e (ln tau)^m ----------------
def fadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
        if out[k] == 0:
            del out[k]
    return out


def fscal(c, a):
    return {k: c * v for k, v in a.items() if c * v != 0}


def fshift(a, de):
    return {(e + de, m): c for (e, m), c in a.items()}


def fdtau(a):
    out = {}
    for (e, m), c in a.items():
        if e != 0:
            out = fadd(out, {(e - 1, m): c * e})
        if m > 0:
            out = fadd(out, {(e - 1, m - 1): c * m})
    return out


def s_term(n, m, q):
    """s^n (ln s)^m with k = q, so s = tau^q and ln s = q ln tau"""
    return {(n * q, m): q ** m}


def tau_op(phi, alpha, p, k):
    d1 = fdtau(phi)
    return fadd(fadd(fdtau(d1), fscal(alpha, fshift(d1, -1))), fscal(k * k, fshift(phi, -2 * p)))


def bessel_op_in_tau(n, m, q, p, nu2, a):
    """k^2 tau^(-2p) tau^a (f'' + f'/s + f - nu^2 f/s^2), f = s^n (ln s)^m, k = q"""
    t = {}
    for coef, mm in [(n * n - nu2, m), (2 * n * m, m - 1), (m * (m - 1), m - 2)]:
        if coef != 0 and mm >= 0:
            t = fadd(t, fscal(coef, s_term(n - 2, mm, q)))
    t = fadd(t, s_term(n, m, q))
    return fscal(q * q, fshift(t, a - 2 * p))


def alpha_of(lam, ph):
    return 1 + (lam - 1) * ph


def nu_of(lam, ph, p):
    return abs((lam - 1) * ph) / (2 * (1 - p))


POINTS = {
    "5D isotropic vacuum": (F(1, 2), F(1, 2), F(1, 2), F(-1, 2)),
    "Milne vacuum": (F(0), F(0), F(0), F(1)),
    "stiff, hidden static": (F(1, 3), F(1, 3), F(1, 3), F(0)),
    "stiff, p = 1/4": (F(1, 4), F(1, 4), F(1, 4), F(1, 4)),
    "stiff, p = 5/12": (F(5, 12), F(5, 12), F(5, 12), F(-1, 4)),
    "anisotropic vacuum": (F(2, 3), F(2, 3), F(-1, 3), F(0)),
}


def _frame_volume(ps, tau, dims):
    """GA: product of the orthogonal frame vectors e0 and tau^(p_j) e_j over dims; returns the blade coefficient"""
    v = GA.gen(0)
    for j in dims:
        v = GA.mul(v, GA.scal(tau[j], GA.gen(j + 1)), SQ5)
    return v


def check_reduction_weights():
    premise("synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands")
    premise("dark-tower-matter.five-dimensional-content")
    premise("dark-tower-matter.five-dimensional-towers")
    # sample tau = 2^12, so tau^p is rational for every exponent with denominator dividing 12
    T = 2 ** 12
    for name, ps in POINTS.items():
        GA.check("%s: exponents sum to 1" % name, sum(ps) == 1)
        powv = [F(2) ** int(12 * x) for x in ps]          # tau^(p_j) = 2^(12 p_j)
        v5 = _frame_volume(ps, powv, [0, 1, 2, 3])
        v4 = _frame_volume(ps, powv, [0, 1, 2])
        c5 = list(v5.values())[0]
        c4 = list(v4.values())[0]
        GA.check("%s: sqrt|g_5| = tau^(sum p) = tau" % name, abs(c5) == T)
        GA.check("%s: sqrt|g_5| = sqrt|g_4| b" % name, abs(c5) == abs(c4) * powv[3])
        fy = GA.scal(powv[3], GA.gen(4))
        qy = GA.mul(fy, fy, SQ5)
        GA.check("%s: Q(f_y) = -b^2" % name, GA.eq(qy, GA.sc(-powv[3] ** 2)))
        # weights relative to sqrt|g_4|: bulk scalar b^1, A_y with g^yy = -1/b^2 gives b^(1 - 2) = b^-1, confined b^0
        for lam, w in [(1, abs(c5)), (-1, abs(c5) / powv[3] ** 2), (0, abs(c4))]:
            GA.check("%s: weight b^%d" % (name, lam), w == abs(c4) * powv[3] ** lam)
            # friction exponent alpha = (exponent of tau in weight) = (1 - p_h) + lambda p_h
            GA.check("%s: alpha for lambda = %d" % (name, lam),
                     (1 - ps[3]) + lam * ps[3] == alpha_of(lam, ps[3]))
    return True


FP_COUNT = 350
FP_VALUE = F(44963783, 13824)


def check_bessel_order():
    premise("synthesis.kasner-approach-gives-horizon-exit-and-index-three")
    premise("interior.kasner-form-interior")
    count, finger = 0, F(0)
    for name, ps in POINTS.items():
        ph = ps[3]
        for p in sorted(set(ps[:3])):
            q = 1 - p
            for lam in [-1, 0, 1, 3, 5]:
                al = alpha_of(lam, ph)
                a = (1 - al) / 2
                nu2 = (a / q) ** 2
                GA.check("nu^2 = ((lambda - 1) p_h/(2q))^2 (%s, lambda %d)" % (name, lam),
                         nu2 == nu_of(lam, ph, p) ** 2)
                for n in [F(0), F(1), F(2), F(5, 2), nu_of(lam, ph, p)]:
                    for m in [0, 1]:
                        phi = fshift(s_term(n, m, q), a)
                        lhs = tau_op(phi, al, p, q)
                        rhs = bessel_op_in_tau(n, m, q, p, nu2, a)
                        GA.check("%s p=%s lambda=%d s^%s ln^%d" % (name, p, lam, n, m), lhs == rhs)
                        count += 1
                        finger += sum(c * (e + 2) * (mm + 1) for (e, mm), c in lhs.items())
                # control: the order of the stored claim (0) fails unless (lambda - 1) p_h = 0
                lhs = tau_op(fshift(s_term(F(2), 0, q), a), al, p, q)
                bad = bessel_op_in_tau(F(2), 0, q, p, F(0), a)
                GA.check("control: order 0 holds iff (lambda - 1) p_h = 0 (%s, lambda %d)" % (name, lam),
                         (lhs == bad) == ((lam - 1) * ph == 0))
    GA.check("identity count pinned", count == FP_COUNT)
    GA.check("fingerprint pinned", finger == FP_VALUE)
    return True


def check_normalisation_and_index():
    premise("synthesis.kasner-approach-gives-horizon-exit-and-index-three")
    for name, ps in POINTS.items():
        for lam in [-1, 0, 1]:
            al = alpha_of(lam, ps[3])
            a = (1 - al) / 2
            # tau^alpha (phi phidot* - c.c.) = |N|^2 tau^(alpha + 2a) (ds/dtau) W = |N|^2 tau^(alpha+2a) k tau^(-p) W,
            # W[H1, H2] = -4i/(pi s), s = k tau^q/q: the tau and k powers cancel iff alpha + 2a = 1
            GA.check("%s lambda %d: alpha + 2a = 1, normalisation k-free" % (name, lam), al + 2 * a == 1)
    # superhorizon: Delta^2 ~ k^3 |N|^2 s^(-2 nu), s ~ k: n - 1 = 3 - 2 nu
    for nu in [F(1, 2), F(1), F(3, 2), F(2)]:
        GA.check("k-exponent of k^3 s^(-2nu) is 3 - 2nu (nu = %s)" % nu, 3 + (-2 * nu) * 1 == 3 - 2 * nu)
    # pinned orders and indices at the two isotropic vacuum points for the stored couplings
    for name in ["5D isotropic vacuum", "Milne vacuum"]:
        ps = POINTS[name]
        got = [(lam, nu_of(lam, ps[3], ps[0]), 3 - 2 * nu_of(lam, ps[3], ps[0])) for lam in (-1, 0, 1)]
        GA.check("%s: (lambda, nu, n - 1) pinned" % name,
                 got == [(-1, F(1), F(1)), (0, F(1, 2), F(2)), (1, F(0), F(3))])
    return True


def seg_ratio(p):
    return abs(1 - 3 * p) / (1 - p)


def check_equal_observed_exponents():
    premise("synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue")
    premise("interior.kasner-form-interior")
    # equal observed exponents p, hidden p_h = 1 - 3p; sum of squares 3p^2 + (1 - 3p)^2 = 1 + 12p^2 - 6p
    for p in [F(k, 24) for k in range(-24, 25)]:
        s2 = 3 * p * p + (1 - 3 * p) ** 2
        GA.check("sum of squares identity at p = %s" % p, s2 - 1 == 12 * p * p - 6 * p)
        GA.check("on the circle iff p in {0, 1/2} (p = %s)" % p, (s2 == 1) == (p in (F(0), F(1, 2))))
        GA.check("inside the disk iff 0 <= p <= 1/2 (p = %s)" % p, (s2 <= 1) == (0 <= p <= F(1, 2)))
    # bound |1 - 3p|/(1 - p) <= 1 on [0, 1/2]: 1 - ratio = 2p/(1 - p) for p <= 1/3, (2 - 4p)/(1 - p) for p >= 1/3
    for p in [F(k, 60) for k in range(0, 31)]:
        r = seg_ratio(p)
        GA.check("ratio <= 1 at p = %s" % p, r <= 1)
        GA.check("1 - ratio closed form at p = %s" % p,
                 1 - r == (2 * p / (1 - p) if p <= F(1, 3) else (2 - 4 * p) / (1 - p)))
    GA.check("equality only at the vacuum endpoints",
             [p for p in [F(k, 60) for k in range(0, 31)] if seg_ratio(p) == 1] == [F(0), F(1, 2)])
    GA.check("ratio vanishes at the static hidden point p = 1/3", seg_ratio(F(1, 3)) == 0)
    # a static hidden direction gives order 0 on every axis for every lambda (anisotropic vacuum point and a disk point)
    for ps in [POINTS["anisotropic vacuum"], (F(1, 2), F(1, 2), F(0), F(0))]:
        GA.check("static hidden direction: every lambda gives order 0 on every axis",
                 sum(ps) == 1 and all(nu_of(lam, ps[3], x) == 0 for lam in (-1, 0, 1, 5) for x in ps[:3]))
    # unequal observed exponents with a moving hidden direction: the orders differ between axes (lambda = -1)
    ps3 = (F(5, 12), F(5, 12), F(1, 4), F(-1, 12))
    GA.check("unequal observed exponents, p_h != 0: orders differ between axes (lambda = -1)",
             sum(ps3) == 1 and nu_of(-1, ps3[3], ps3[0]) == F(1, 7) and nu_of(-1, ps3[3], ps3[2]) == F(1, 9))
    return True


FP_BALL = (2347, 1)


def check_every_point_has_a_blue_axis():
    premise("synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue")
    premise("dark-tower-matter.five-dimensional-towers")
    # range of one exponent: p^2 + (1 - p)^2/3 <= 1  <=>  2(2p + 1)(p - 1) <= 0
    for p in [F(k, 24) for k in range(-36, 37)]:
        lhs = 3 * (p * p + (1 - p) ** 2 / 3 - 1)
        GA.check("factorisation at p = %s" % p, lhs == 2 * (2 * p + 1) * (p - 1))
        GA.check("in range iff -1/2 <= p <= 1 (p = %s)" % p, (lhs <= 0) == (F(-1, 2) <= p <= 1))
    # three observed orders above 1 would need 3|p_h| > 2 + p_h
    for ph in [F(k, 24) for k in range(-12, 25)]:
        GA.check("3|p_h| > 2 + p_h impossible on [-1/2, 1] (p_h = %s)" % ph, not (3 * abs(ph) > 2 + ph))
    # grid over the ball, step 1/12 in the observed exponents, lambda = -1 (|lambda - 1| = 2, the extreme)
    npts, worst, worst_pts = 0, F(-1), []
    grid = [F(k, 12) for k in range(-6, 13)]
    for a in grid:
        for b in grid:
            for c in grid:
                ph = 1 - a - b - c
                if a * a + b * b + c * c + ph * ph > 1:
                    continue
                npts += 1
                GA.check("single exponents in [-1/2, 1]", all(F(-1, 2) <= x <= 1 for x in (a, b, c, ph)))
                orders = [nu_of(-1, ph, x) for x in (a, b, c) if x < 1]
                m = min(orders)
                GA.check("some exiting axis has order <= 1", m <= 1)
                if m > worst:
                    worst, worst_pts = m, [(a, b, c, ph)]
                elif m == worst:
                    worst_pts.append((a, b, c, ph))
    GA.check("grid point count and worst least order pinned", (npts, worst) == FP_BALL)
    GA.check("worst case at the 5D isotropic vacuum point", (F(1, 2), F(1, 2), F(1, 2), F(-1, 2)) in worst_pts)
    return True


def check_stored_fields_blue():
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("dark-tower-matter.five-dimensional-content")
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    grid = [F(k, 60) for k in range(0, 31)]
    for lam in [0, 1, -1]:
        nus = [abs(lam - 1) * seg_ratio(p) / 2 for p in grid]
        GA.check("lambda %d: nu <= |lambda - 1|/2 <= 1 on the segment" % lam, max(nus) == F(abs(lam - 1), 2))
        GA.check("lambda %d: n - 1 >= 3 - |lambda - 1| >= 1" % lam, min(3 - 2 * x for x in nus) == 3 - abs(lam - 1))
    gap = 1 - NS1
    GA.check("gap to the measured index at least 1.0351", gap == F("1.0351"))
    GA.check("more than 246 standard deviations", gap / SIG > 246 and gap / SIG < 247)
    # a red index within an epoch needs |lambda - 1| > 3 (control lambda = 5): then the segment covers [-1, 3],
    # and the measured value is reached only by choosing p (one number for one target)
    nus5 = [abs(5 - 1) * seg_ratio(p) / 2 for p in grid]
    GA.check("control lambda = 5: index range on the grid is [-1, 3]",
             min(3 - 2 * x for x in nus5) == -1 and max(3 - 2 * x for x in nus5) == 3)
    GA.check("red needs |lambda - 1| > 3", all((3 - abs(lam - 1) < 0) == (abs(lam - 1) > 3) for lam in range(-6, 9)))
    # the towers' gauge vector zero modes, weight b on a transverse vector: alpha = 1 - 2 p_j, order p/(1 - p)
    for p in grid:
        al = 1 + (1 - 1) * (1 - 3 * p) - 2 * p
        nu_v = abs(1 - al) / (2 * (1 - p))
        GA.check("vector zero mode order p/(1 - p) <= 1 at p = %s" % p, nu_v == p / (1 - p) and nu_v <= 1)
    GA.check("vector control: conformal order 1/2 at the static point",
             abs(1 - (1 - 2 * F(1, 3))) / (2 * (1 - F(1, 3))) == F(1, 2))
    return True
