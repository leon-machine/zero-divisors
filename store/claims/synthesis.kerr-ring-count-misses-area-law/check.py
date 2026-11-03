"""synthesis.kerr-ring-count-misses-area-law: exact checks.

Kerr in the Kerr-Schild gauge written in oblate coordinates (t, r, u = cos theta, phi), signature (-+++):
  eta = -dt^2 + Sigma/P dr^2 + Sigma/(1 - u^2) du^2 + P (1 - u^2) dphi^2,  P = r^2 + a^2,
  k   = -dt - (Sigma/P) dr + a (1 - u^2) dphi,  g = eta + 2 H k k,  H = M r / Sigma,  Sigma = r^2 + a^2 u^2.
Every entry is a rational function of (M, a, r, u), so all identities are checked in Fractions.
  (1) k is eta-null; det g = -Sigma^2 (the Kerr-Schild determinant); Sigma g^{rr} = r^2 - 2Mr + a^2
      (so r = r_+- are the null hypersurfaces); the horizon cross-section has area density P(r_+) = r_+^2 + a^2.
  (2) on the tube z = r - I a u = rho (c + I s), c^2 + s^2 = 1 (Pythagorean rationals), the Gram
      determinant of (d_t, d_psi, d_phi) equals -rho^4 [1 + (rho^2/a^2)(c^2 - s^2) - (2 M rho/a^2) c^3],
      identically in rho (checked off and on the (C1) locus rho^3 = 2M); also with d_t replaced by
      d_t + Omega d_phi (same determinant).
  (3) circle averages: <x> = 0 and <x^2> = eps^2/2 + 5 del^2/16 for x = eps cos 2psi - del cos^3 psi, by
      exact Fourier averages <cos^n> = binom(n, n/2)/2^n; the polynomial bound 1 + x/2 - x^2/2 <= sqrt(1+x)
      <= 1 + x/2 on |x| <= 1/2 in the squared form.
  (4) regime: under a^2 >= 8 M rho_c the tube lies in |r| <= rho_c < a^2/(2M) <= r_-, the bracket is
      >= 1/2 (timelike tube), and at r = -rho_c, u = 0 the axial Killing field is timelike.
  (5) the count ratio N/(A_+/4) = (pi/2) rho_c^2 (1 - eta)/sqrt(M^2 - a^2) at nu = 1/16 pi and the
      outer modular period, as a rational multiple of pi at exact sample holes; it halves when M grows
      by 8 at fixed a/M (the M^{-1/3} law); Schwarzschild control V' = beta = 8 pi M gives ratio 1.
"""
from fractions import Fraction as F
import GA  # noqa: F401  (house rule; the computation is rational arithmetic on metric components)
from tp_premise import premise


class Det:
    """Deterministic integer sequence (exact integers only) for reproducible rational sample points."""

    def __init__(self, seed):
        self.x = seed

    def nxt(self):
        self.x = (self.x * 1103515245 + 12345) % 2147483648
        return self.x // 65536

    def randint(self, lo, hi):
        return lo + self.nxt() % (hi - lo + 1)


def metric(M, a, r, u):
    S = r * r + a * a * u * u
    P = r * r + a * a
    eta = [[F(0)] * 4 for _ in range(4)]
    eta[0][0] = F(-1)
    eta[1][1] = S / P
    eta[2][2] = S / (1 - u * u)
    eta[3][3] = P * (1 - u * u)
    k = [F(-1), -S / P, F(0), a * (1 - u * u)]
    assert sum(k[i] * k[i] / eta[i][i] for i in range(4)) == 0          # k null for eta
    H = M * r / S
    return [[eta[i][j] + 2 * H * k[i] * k[j] for j in range(4)] for i in range(4)]


def det(m):
    n = len(m)
    m = [row[:] for row in m]
    d = F(1)
    for i in range(n):
        p = next((j for j in range(i, n) if m[j][i] != 0), None)
        if p is None:
            return F(0)
        if p != i:
            m[i], m[p] = m[p], m[i]
            d = -d
        d *= m[i][i]
        for j in range(i + 1, n):
            f = m[j][i] / m[i][i]
            for c in range(i, n):
                m[j][c] -= f * m[i][c]
    return d


def inverse(m):
    n = len(m)
    a = [row[:] + [F(1) if i == j else F(0) for j in range(n)] for i, row in enumerate(m)]
    for i in range(n):
        p = next(j for j in range(i, n) if a[j][i] != 0)
        a[i], a[p] = a[p], a[i]
        piv = a[i][i]
        a[i] = [x / piv for x in a[i]]
        for j in range(n):
            if j != i and a[j][i] != 0:
                f = a[j][i]
                a[j] = [x - f * y for x, y in zip(a[j], a[i])]
    return [row[n:] for row in a]


def gram(g, vs):
    return [[sum(v[i] * g[i][j] * w[j] for i in range(4) for j in range(4)) for w in vs] for v in vs]


def pyth(m, n):
    return (F(m * m - n * n, m * m + n * n), F(2 * m * n, m * m + n * n))


def bracket(M, a, rho, c, s):
    return 1 + rho * rho / (a * a) * (c * c - s * s) - 2 * M * rho / (a * a) * c ** 3


def binom(n, k):
    out = 1
    for j in range(k):
        out = out * (n - j) // (j + 1)
    return out


def avg_cos_pow(n):
    return F(binom(n, n // 2), 2 ** n) if n % 2 == 0 else F(0)


def pmul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0)) for i in range(n)]


def avg(p):
    return sum(cf * avg_cos_pow(k) for k, cf in enumerate(p))


def check_kerr_schild_data():
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    rng = Det(11)
    for _ in range(12):
        M = F(rng.randint(1, 9), rng.randint(1, 3))
        a = F(rng.randint(1, 9), rng.randint(1, 4))
        r = F(rng.randint(-15, 15), rng.randint(1, 5))
        u = F(rng.randint(-6, 6), 7)
        if r == 0 and u == 0:
            continue
        g = metric(M, a, r, u)
        S = r * r + a * a * u * u
        assert det(g) == -S * S                                    # Kerr-Schild: det g = det eta
        gi = inverse(g)
        assert S * gi[1][1] == r * r - 2 * M * r + a * a           # Sigma g^{rr} = Delta
    # worked hole M = 5, a = 3: r_+ = 9, r_- = 1, P(r_+) = 90 = 2 M r_+
    M, a = F(5), F(3)
    for rp in (F(9), F(1)):
        assert rp * rp - 2 * M * rp + a * a == 0
    for u in (F(0), F(1, 2), F(-3, 4), F(2, 9)):
        g = metric(M, a, F(9), u)
        assert g[2][3] == 0 and g[2][2] * g[3][3] == (F(81) + 9) ** 2   # area density r_+^2 + a^2
    return True


def check_tube_determinant():
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    premise("interior.complex-scale-inverse-cube-killing-spinor")
    premise("synthesis.kerr-ring-double-cover-data")
    holes = [(F(500), F(300), F(10)), (F(4000), F(2400), F(20)), (F(7, 2), F(3), F(1, 2)),
             (F(5), F(4), F(1)), (F(32), F(32), F(4))]
    for (M, a, rho) in holes:
        for (m, n) in [(2, 1), (3, 2), (1, 3), (5, 1), (-2, 3), (4, -7)]:
            for sgn in (1, -1):
                c, s = pyth(m, n)
                c = sgn * c
                r, u = rho * c, -rho * s / a                     # z = r - I a u = rho (c + I s)
                assert r * r + a * a * u * u == rho * rho
                g = metric(M, a, r, u)
                Tt = [F(1), F(0), F(0), F(0)]
                Tp = [F(0), -rho * s, -rho * c / a, F(0)]       # d/dpsi of (r, u)
                Tf = [F(0), F(0), F(0), F(1)]
                d = det(gram(g, [Tt, Tp, Tf]))
                assert d == -rho ** 4 * bracket(M, a, rho, c, s)
                Om = F(1, 13)
                assert det(gram(g, [[F(1), F(0), F(0), Om], Tp, Tf])) == d   # any flow d_t + Omega d_phi
    # the (C1) locus rho^3 = 2M is among the samples
    assert F(10) ** 3 == 2 * F(500) and F(20) ** 3 == 2 * F(4000) and F(4) ** 3 == 2 * F(32)
    return True


def check_averages_and_bound():
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("synthesis.kerr-ring-double-cover-data")
    assert [avg_cos_pow(n) for n in range(7)] == [1, 0, F(1, 2), 0, F(3, 8), 0, F(5, 16)]
    for (eps, de) in [(F(1, 900), F(1, 9)), (F(1, 64), F(1, 4)), (F(2, 5), F(3, 7))]:
        x = [-eps, F(0), 2 * eps, -de]                            # eps cos 2psi - del cos^3 psi
        assert avg(x) == 0
        assert avg(pmul(x, x)) == eps * eps / 2 + 5 * de * de / 16
    # bounds in squared form, as polynomials in x: (1 + x/2)^2 - (1 + x) = x^2/4;
    # (1 + x) - (1 + q)^2 = x^2 - q^2 with q = x/2 - x^2/2, and q^2 = x^2 (1 - x)^2 / 4
    up = padd(pmul([F(1), F(1, 2)], [F(1), F(1, 2)]), [F(-1), F(-1)])
    assert up == [0, 0, F(1, 4)]
    q = [F(0), F(1, 2), F(-1, 2)]
    lo = padd([F(1), F(1)], [-c for c in pmul(padd([F(1)], q), padd([F(1)], q))])
    assert lo == padd(pmul([0, 0, 1], [1]), [-c for c in pmul(q, q)])
    assert pmul(q, q) == pmul([0, 0, F(1, 4)], pmul([1, -1], [1, -1]))
    # one sheet (cos psi > 0): int cos^3 = [sin - sin^3/3] from -1 to 1 (in sin) = 4/3; int cos 2psi = [sin 2psi/2] = 0
    anti = lambda sn: sn - sn ** 3 / 3
    assert anti(F(1)) - anti(F(-1)) == F(4, 3)
    # so on that sheet int (1 + x/2) = pi - (2/3) del: the del-correction coefficient is -(1/2)(4/3)
    assert -F(1, 2) * (anti(F(1)) - anti(F(-1))) == F(-2, 3)
    for k in range(-50, 51):                                     # |x| <= 1/2: (1-x)^2 <= 4 and 1 + q > 0
        x0 = F(k, 100)
        assert (1 - x0) ** 2 <= 4 and 1 + x0 / 2 - x0 * x0 / 2 > 0
    return True


def check_regime_and_ctc():
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    premise("interior.complex-scale-inverse-cube-killing-spinor")
    for (M, a, rho, sq) in [(F(500), F(300), F(10), F(400)), (F(4000), F(2400), F(20), F(3200)),
                            (F(32), F(32), F(4), F(0)), (F(32000), F(19200), F(40), F(25600))]:
        assert rho ** 3 == 2 * M and sq * sq == M * M - a * a and sq >= 0
        assert a * a >= 8 * M * rho                               # hypothesis a >= 2 rho_c^2
        rm = M - sq
        assert rho < a * a / (2 * M) <= rm                         # tube beyond the inner horizon
        eps, de = rho * rho / (a * a), 2 * M * rho / (a * a)
        assert de <= F(1, 4) and eps <= F(1, 64) and eps + de <= F(1, 2)
        for (m, n) in [(2, 1), (1, 2), (3, 4), (1, 0), (0, 1)]:
            for sgn in (1, -1):
                c, s = pyth(m, n)
                c = sgn * c
                assert bracket(M, a, rho, c, s) >= F(1, 2)         # Lorentzian tube
        g = metric(M, a, -rho, F(0))
        assert g[3][3] == rho * rho + a * a * (1 - rho * rho) and g[3][3] < 0   # closed timelike phi-orbit
    return True


def check_count_ratio():
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("singularity.stretched-singularity-count")
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    premise("synthesis.kerr-ring-double-cover-data")
    # Schwarzschild control: V' = 8 pi M = beta, nu = 1/16 pi: N/(A/4) = nu V' beta / (4 pi M^2) = 1
    for M in (F(4), F(500)):
        piV, pibeta = 8 * M, 8 * M                               # coefficients of pi
        assert F(1, 16) * piV * pibeta / (4 * M * M) == 1         # nu = 1/(16 pi): pi^2/pi/pi cancels
    # Kerr: N/(A_+/4) = 2 nu V' / sqrt(M^2 - a^2) with V' = 4 pi^2 rho^2 (1 - eta), nu = 1/(16 pi):
    # coefficient of pi is rho^2 (1 - eta) / (2 sqrt(M^2 - a^2))
    ratios = []
    for (M, a, rho, sq) in [(F(500), F(300), F(10), F(400)), (F(4000), F(2400), F(20), F(3200)),
                            (F(32000), F(19200), F(40), F(25600))]:
        rp = M + sq
        A4 = 2 * M * rp                                           # A_+/4 / pi = (r_+^2 + a^2)
        assert rp * rp + a * a == A4
        tau_over_pi = 4 * rp / sq                                 # beta_+ = 4 pi r_+ M/sqrt(M^2-a^2) = tau M
        lead = F(1, 16) * 4 * rho * rho * (tau_over_pi * M) / A4   # nu V' beta/(A/4): pi^(-1+2+1-1) = pi
        assert lead == rho * rho / (2 * sq)
        eps, de = rho * rho / (a * a), 2 * M * rho / (a * a)
        etamax = eps * eps / 4 + 5 * de * de / 32
        ratios.append((lead * (1 - etamax), lead))
    assert ratios[0][1] == F(1, 8) and ratios[1][1] == F(1, 16) and ratios[2][1] == F(1, 32)
    for j in range(2):
        assert ratios[j + 1][1] * 2 == ratios[j][1]                # M -> 8M halves the ratio: M^{-1/3}
    return True
