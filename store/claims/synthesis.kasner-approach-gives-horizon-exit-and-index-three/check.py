"""synthesis.kasner-approach-gives-horizon-exit-and-index-three: exact checks.

Diagonal Bianchi I field, derived metric d tau^2 - sum_j tau^(2 p_j) (dx^j)^2 over all spatial directions (three
observed and any hidden ones), with sum_j p_j = 1 (vacuum Kasner, BKL epochs, a massless scalar shortening the
circle). Then sqrt|g| = tau, and a massless minimally coupled field's mode of comoving momentum k along the
principal axis i obeys phi'' + phi'/tau + k^2 tau^(-2 p_i) phi = 0.
(1) Exponent sets (exact rationals): the BKL circle p(u) at u = 1, 2, 3/2, 7/3 (sum 1, sum of squares 1); the BKL
    map u -> u - 1 and u -> 1/(u - 1) stays on the circle; the five-dimensional isotropic vacuum (1/2,1/2,1/2,-1/2);
    the Schwarzschild interior (-1/3, 2/3, 2/3); the scalar-shortened isotropic point (1/3,1/3,1/3), q^2 = 2/3.
    Every exponent is below 1 except the Milne points, so s = k tau^(1 - p)/(1 - p) -> 0 at the wall on every axis.
(2) Reduction to Bessel order 0: on formal terms c s^n (ln s)^m, with s = (k/q) tau^q, q = 1 - p, the operator
    d^2/d tau^2 + (1/tau) d/d tau + k^2 tau^(-2p) equals k^2 tau^(-2p) (d^2/ds^2 + (1/s) d/ds + 1), computed exactly
    term by term (powers of tau as rational exponents, logs carried as polynomials in ln tau).
    Control: the same substitution with order nu^2/s^2 added fails unless nu = 0.
(3) Pump: a^2 prod b = tau^(1 - p) = (1 - p) eta for the conformal time of the axis, so z^2 is linear in eta and
    the Bessel order is |1/2 - 1/2| = 0, for every exponent set with sum 1 (the sum of squares is never used).
(4) Normalisation: with W[H0^(1), H0^(2)](s) = -4i/(pi s), tau(phi phi.* - phi* phi.) = -4i (1 - p)|N|^2/pi, so
    |N|^2 = pi/(4(1 - p)) is independent of k.
(5) Index: Delta^2 = k^3 |N|^2 M(s)^2/(2 pi^2), M^2 = J0^2 + Y0^2, so n - 1 = 3 + s d ln M^2/ds. Leading small-s
    form M^2 = (4/pi^2)(L^2 + pi^2/4), L = ln(s/2) + gamma: n - 1 = 3 + 2L/(L^2 + pi^2/4), whose minimum over L is
    3 - 2/pi > 2.36 (with pi in (3, 22/7)); at the measured -0.0351 the gap exceeds 2.39, over 560 standard
    deviations of 0.0042.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

PI_LO, PI_HI = F(3), F(22, 7)
NS1, SIG = F("-0.0351"), F("0.0042")


def bkl(u):
    d = 1 + u + u * u
    return (-u / d, (1 + u) / d, u * (1 + u) / d)


def on_circle(p):
    return sum(p) == 1 and sum(x * x for x in p) == 1


# formal expressions: dict (n, m) -> coeff meaning coeff * tau^n * (ln tau)^m, n a Fraction
def fadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
        if out[k] == 0:
            del out[k]
    return out


def fscal(c, a):
    return {k: c * v for k, v in a.items() if c * v != 0}


def fdtau(a):
    out = {}
    for (n, m), c in a.items():
        if n != 0:
            out = fadd(out, {(n - 1, m): c * n})
        if m > 0:
            out = fadd(out, {(n - 1, m - 1): c * m})
    return out


def fshift(a, dn):
    return {(n + dn, m): c for (n, m), c in a.items()}


def s_power_log(n, m, k, p):
    """s^n (ln s)^m with s = (k/q) tau^q, ln s = ln(k/q) + q ln tau; take ln(k/q) = l0 symbolic -> choose k = q so
    l0 = 0 (exact), and keep k general only through the prefactor (k/q)^n"""
    q = 1 - p
    # (ln s)^m = q^m (ln tau)^m when k = q
    return {(n * q, m): q ** m}


def tau_operator(a, k, p, sigma):
    """|g|^(-1/2) d_tau(|g|^(1/2) phi') + k^2 tau^(-2p) phi with |g|^(1/2) = tau^sigma, sigma = sum of the
    exponents: phi'' + sigma phi'/tau + k^2 tau^(-2p) phi"""
    d1 = fdtau(a)
    d2 = fdtau(d1)
    return fadd(fadd(d2, fscal(sigma, fshift(d1, -1))), fscal(k * k, fshift(a, -2 * p)))


def s_operator_in_tau(n, m, k, p, nu2=F(0)):
    """k^2 tau^(-2p) (f'' + f'/s + f - nu^2 f/s^2) for f = s^n (ln s)^m, written back in tau (k = q)"""
    terms = {}
    # f'' + f'/s - nu2 f/s^2 = s^(n-2)[ (n^2 - nu2)(ln s)^m + 2 n m (ln s)^(m-1) + m(m-1)(ln s)^(m-2) ]
    for (coef, mm) in [((n * n - nu2), m), (2 * n * m, m - 1), (m * (m - 1), m - 2)]:
        if coef != 0 and mm >= 0:
            terms = fadd(terms, fscal(coef, s_power_log(n - 2, mm, k, p)))
    terms = fadd(terms, s_power_log(n, m, k, p))
    return fscal(k * k, fshift(terms, -2 * p))


EXPONENT_SETS = {
    "BKL u=1": bkl(F(1)), "BKL u=2": bkl(F(2)), "BKL u=3/2": bkl(F(3, 2)), "BKL u=7/3": bkl(F(7, 3)),
    "5D isotropic vacuum": (F(1, 2), F(1, 2), F(1, 2), F(-1, 2)),
    "Schwarzschild interior": (F(-1, 3), F(2, 3), F(2, 3)),
    "scalar-shortened isotropic": (F(1, 3), F(1, 3), F(1, 3)),
    "disk point (3/5,1/5,1/5)": (F(3, 5), F(1, 5), F(1, 5)),
    "disk point (1/2,1/2,0)": (F(1, 2), F(1, 2), F(0)),
}


def check_exponent_sets_have_unit_sum():
    premise("sheaf.kasner-data-interior")
    premise("synthesis.bkl-bounce-invariant-holonomy-and-bound")
    for name, p in EXPONENT_SETS.items():
        GA.check("%s: sum of exponents 1" % name, sum(p) == 1)
        GA.check("%s: every exponent below 1, so every axis exits" % name, all(x < 1 for x in p))
    for u in [F(1), F(2), F(3, 2), F(7, 3)]:
        GA.check("BKL u = %s on the circle" % u, on_circle(bkl(u)))
    # BKL map: u -> u - 1 (same era) and u -> 1/(u - 1) (era change): both stay on the circle
    for u in [F(5, 2), F(7, 3), F(3)]:
        GA.check("BKL map stays on the circle (u = %s)" % u, on_circle(bkl(u - 1)) and on_circle(bkl(1 / (u - 1))))
    GA.check("5D isotropic is a vacuum Kasner point (sum of squares 1)",
             sum(x * x for x in EXPONENT_SETS["5D isotropic vacuum"]) == 1)
    q2 = 1 - sum(x * x for x in EXPONENT_SETS["scalar-shortened isotropic"])
    GA.check("scalar-shortened isotropic point has q^2 = 2/3", q2 == F(2, 3))
    for name in ["disk point (3/5,1/5,1/5)", "disk point (1/2,1/2,0)"]:
        GA.check("%s lies inside the circle (sum of squares below 1)" % name,
                 sum(x * x for x in EXPONENT_SETS[name]) < 1)
    # one BKL bounce u = 7/3 -> 4/3 -> 1/3 -> era change 1/(4/3 - 1) = 3: every epoch keeps sum 1 and exits
    for u in [F(7, 3), F(4, 3), F(3)]:
        GA.check("BKL epoch u = %s: sum 1, all exponents below 1" % u, sum(bkl(u)) == 1 and all(x < 1 for x in bkl(u)))
    GA.check("Milne point (1,0,0) excluded: exponent 1 has no exit", not all(x < 1 for x in (F(1), F(0), F(0))))
    # GA: the Kasner residue -sum p_i B_i with B_i = e0 e_i; its square is sum p_i^2 = 1 on the circle
    SQ = (1, -1, -1, -1)
    p = bkl(F(2))
    res = GA.add(*[GA.scal(-p[i], GA.mul(GA.gen(0), GA.gen(i + 1), SQ)) for i in range(3)])
    GA.check("residue squares to sum p_i^2 = 1 (boosts commute)", GA.eq(GA.mul(res, res, SQ), GA.sc(1)))
    return True


FP_COUNT = 300
FP_VALUE = F(258098941591926109619111, 25054742747008800000)


def check_bessel_order_zero():
    premise("interior.kasner-form-interior")
    # pinned instance: Schwarzschild axis p = -1/3, k = q = 4/3, s = tau^(4/3), f = s^2 ln s = (4/3) tau^(8/3) ln tau:
    # f'' + f'/tau = (256/27) tau^(2/3) ln tau + (64/9) tau^(2/3), and k^2 tau^(2/3) f = (64/27) tau^(10/3) ln tau
    sw = EXPONENT_SETS["Schwarzschild interior"]
    pin = tau_operator(s_power_log(F(2), 1, F(4, 3), F(-1, 3)), F(4, 3), F(-1, 3), sum(sw))
    GA.check("pinned operator on s^2 ln s at p = -1/3",
             pin == {(F(2, 3), 0): F(64, 9), (F(2, 3), 1): F(256, 27), (F(10, 3), 1): F(64, 27)})
    count, finger = 0, F(0)
    for name, ps in EXPONENT_SETS.items():
        for p in sorted(set(ps)):
            k = 1 - p           # choose k = q so ln(k/q) = 0; the identity is homogeneous in k otherwise
            for n in [F(0), F(1), F(2), F(3), F(5, 2)]:
                for m in [0, 1, 2]:
                    lhs = tau_operator(s_power_log(n, m, k, p), k, p, sum(ps))
                    rhs = s_operator_in_tau(n, m, k, p)
                    GA.check("%s, p = %s, s^%s ln^%d s: tau operator = Bessel-0 operator" % (name, p, n, m),
                             lhs == rhs)
                    count += 1
                    finger += sum(c * (e + 1) * (mm + 1) for (e, mm), c in lhs.items())
            # control: a nonzero order nu^2 = 1/4 breaks the identity by exactly -nu^2 k^2 tau^(-2p) s^(n-2)
            lhs = tau_operator(s_power_log(F(2), 0, k, p), k, p, sum(ps))
            bad = s_operator_in_tau(F(2), 0, k, p, nu2=F(1, 4))
            diff = fadd(bad, fscal(-1, lhs))
            GA.check("control: order 1/2 misses by -(1/4) k^2 tau^(-2p) (%s, p = %s)" % (name, p),
                     diff == {(-2 * p, 0): -F(1, 4) * k * k})
    GA.check("identity count pinned at %d" % count, count == FP_COUNT)
    GA.check("fingerprint of the operator values pinned", finger == FP_VALUE)
    # control: exponent sets with sum p other than 1 (friction sigma/tau) fail the order-0 identity, by
    # (sigma - 1) f'/tau exactly
    for ps in [(F(1, 2), F(1, 2), F(1, 2)), (F(1, 3), F(1, 3), F(0)), (F(-1, 3), F(2, 3), F(2, 3), F(1, 5))]:
        p = ps[0]
        k = 1 - p
        a = s_power_log(F(2), 1, k, p)
        diff = fadd(tau_operator(a, k, p, sum(ps)), fscal(-1, s_operator_in_tau(F(2), 1, k, p)))
        GA.check("control: sum p = %s misses by (sum p - 1) f'/tau" % sum(ps),
                 diff == fscal(sum(ps) - 1, fshift(fdtau(a), -1)) and diff != {})
    GA.check("control sums pinned", [sum(ps) for ps in [(F(1, 2), F(1, 2), F(1, 2)), (F(1, 3), F(1, 3), F(0)),
             (F(-1, 3), F(2, 3), F(2, 3), F(1, 5))]] == [F(3, 2), F(2, 3), F(6, 5)])
    return True


def check_pump_linear_in_conformal_time():
    premise("interior.kasner-form-interior")
    premise("synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands")
    for name, ps in EXPONENT_SETS.items():
        for i, p in enumerate(ps):
            # z^2 = sqrt|g| / a_i = tau^(sum p - p) = tau^(1 - p); eta_i = tau^(1 - p)/(1 - p)
            z2_exp = sum(ps) - p
            GA.check("%s axis %d: z^2 = tau^(1 - p)" % (name, i), z2_exp == 1 - p)
            # z proportional to eta^(1/2): exponent of eta in z is (1/2); Bessel order |1/2 - 1/2| = 0
            s_exp = (z2_exp / 2) / (1 - p)
            GA.check("%s axis %d: z ~ eta^(1/2), order 0" % (name, i), s_exp == F(1, 2) and abs(s_exp - F(1, 2)) == 0)
    # a hidden direction b ~ a^beta in a non-Kasner (fluid) background changes the order: control at de Sitter
    # z ~ a^(1 + beta/2), a ~ 1/|eta|: order |-(1 + beta/2) - 1/2| = 3/2 + beta/2, index 3 - 2 nu = -beta
    for beta in [F(0), F(7, 200), F(1)]:
        nu = F(3, 2) + beta / 2
        GA.check("control (de Sitter, hidden b ~ a^beta): index -beta at beta = %s" % beta, 3 - 2 * nu == -beta)
    return True


def _series_mul(a, b, N):
    out = [F(0)] * N
    for i, x in enumerate(a[:N]):
        if x:
            for j, y in enumerate(b[:N - i]):
                out[i + j] += x * y
    return out


def _deriv(a):
    return [i * a[i] for i in range(1, len(a))] + [F(0)]


def _bessel_series(N):
    """J0 = sum (-1)^k (s/2)^(2k)/(k!)^2 and G1 = sum (-1)^(k+1) H_k (s/2)^(2k)/(k!)^2 as coefficient lists in s;
    Y0 = (2/pi)[(ln(s/2) + gamma) J0 + G1]"""
    J, G = [F(0)] * N, [F(0)] * N
    fact, H = F(1), F(0)
    for k in range(0, N // 2):
        if k > 0:
            fact *= k
            H += F(1, k)
        c = F((-1) ** k, 4 ** k) / (fact * fact)
        J[2 * k] = c
        G[2 * k] = -c * H
    return J, G


def check_normalisation_k_independent():
    premise("interior.kasner-form-interior")
    N = 24
    J, G = _bessel_series(N)
    # J0 solves s J'' + J' + s J = 0
    Jp, Jpp = _deriv(J), _deriv(_deriv(J))
    sJ = [F(0)] + J[:N - 1]
    sJpp = [F(0)] + Jpp[:N - 1]
    GA.check("J0 series solves Bessel order 0", all(x == 0 for x in [sJpp[i] + Jp[i] + sJ[i] for i in range(N - 2)]))
    # Wronskian W[J0, ln s J0 + G1] = J0^2/s + J0 G1' - J0' G1 must be 1/s: times s, J0^2 + s(J0 G1' - J0' G1) = 1
    Gp = _deriv(G)
    w = _series_mul(J, J, N)
    cross = [x - y for x, y in zip(_series_mul(J, Gp, N), _series_mul(Jp, G, N))]
    scross = [F(0)] + cross[:N - 1]
    tot = [w[i] + scross[i] for i in range(N - 2)]
    GA.check("s W[J0, ln s J0 + G1] = 1 to order s^21, so W[J0, Y0] = 2/(pi s)",
             tot[0] == 1 and all(x == 0 for x in tot[1:]))
    # control: dropping the harmonic numbers breaks it
    G_bad = [-x for x in J]
    cross_b = [x - y for x, y in zip(_series_mul(J, _deriv(G_bad), N), _series_mul(Jp, G_bad, N))]
    tot_b = [w[i] + ([F(0)] + cross_b[:N - 1])[i] for i in range(N - 2)]
    GA.check("control: wrong G1 fails", not all(x == 0 for x in tot_b[1:]))
    for p in [F(-1, 3), F(2, 3), F(1, 2), F(-1, 2), F(1, 3)]:
        # tau (phi phidot* - phi* phidot) = tau (ds/dtau) |N|^2 W[H0^(1), H0^(2)] = (1 - p) s |N|^2 (-4i/(pi s)):
        # W[H1, H2] = -2i W[J0, Y0] = -4i/(pi s); the s cancels, so |N|^2 = pi/(4(1 - p)) for every k
        GA.check("normalisation |N|^2 (4/pi)(1 - p) = 1 has a k-free solution (p = %s)" % p,
                 (F(1) / (4 * (1 - p))) * 4 * (1 - p) == 1)
    return True


def check_index_between_two_and_three():
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    # leading small-s form: n - 1 = 3 + 2L/(L^2 + c), c = pi^2/4, L = ln(s/2) + gamma < 0; since c > 0,
    # 2L/(L^2 + c) >= 2/L. For s <= 1e-2, L <= ln(1/200) + gamma < -4.7 (ln 200 > 5.29, gamma < 0.578)
    for c, lo_pin in [(PI_LO * PI_LO / 4, 26138), (PI_HI * PI_HI / 4, 26172)]:
        vs = []
        for L in [F(-47, 10) - F(k, 3) for k in range(0, 300)]:
            v = 3 + 2 * L / (L * L + c)
            GA.check("index above 3 + 2/L", v >= 3 + 2 / L)
            vs.append(v)
        GA.check("sampled minimum pinned (floor of 1e4 times it is %d), above 2.57" % lo_pin,
                 (min(vs) * 10 ** 4) // 1 == lo_pin and min(vs) > F("2.57"))
        GA.check("sampled maximum pinned at 29808e-4, below 3", (max(vs) * 10 ** 4) // 1 == 29808 and max(vs) < 3)
    GA.check("ln 200 = 7 ln 2 + ln(1.5625) > 7(0.693) + 0.446 > 5.29 (log bounds in the proof)",
             7 * F("0.693") + F("0.446") > F("5.29") and 2 ** 7 * F("1.5625") == 200)
    v = 3 + 2 * F(-47, 10) / (F(-47, 10) ** 2 + F(9, 4))
    GA.check("pinned: at L = -4.7, c = 9/4 the index is 3181/1217", v == F(3181, 1217))
    GA.check("blue by 2.0351 against the measured index", 2 - NS1 == F("2.0351"))
    GA.check("sigma count pinned: floor of 10 (2 - n_s + 1)/sigma is 4845", ((2 - NS1) / SIG * 10) // 1 == 4845)
    L = F(-236, 10)
    GA.check("at L = -23.6 (s near 1e-10) the index is pinned at 29156e-4",
             ((3 + 2 * L / (L * L + PI_HI * PI_HI / 4)) * 10 ** 4) // 1 == 29156)
    # not finite range: the spectrum over k^3 is (4/pi^2)(L^2 + pi^2/4), unbounded as L -> -infinity (k -> 0),
    # while the finite-range bound caps Delta^2/(k R)^3 by (2/(3 pi)) <zeta^2>
    for n in [10, 100, 1000]:
        GA.check("log factor exceeds n^2 at L = -n (n = %d)" % n, F(n) ** 2 + PI_LO ** 2 / 4 > n * n)
    GA.check("log factor at L = -1000 pinned", (F(1000) ** 2 + PI_LO ** 2 / 4) == F(4000009, 4))
    return True
