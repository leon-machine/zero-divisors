"""synthesis.no-spin-independent-curvature-level-set-carries-the-count-to-slow-kerr: exact checks.

Kerr in the Kerr-Schild gauge in oblate coordinates (t, r, u = cos theta, phi), signature (-+++), as in the
stored ring count:
  eta = -dt^2 + Sigma/P dr^2 + Sigma/(1 - u^2) du^2 + P (1 - u^2) dphi^2,  P = r^2 + a^2,
  k   = -dt - (Sigma/P) dr + a (1 - u^2) dphi,  g = eta + 2 H k k,  H = M r / Sigma,  Sigma = r^2 + a^2 u^2.
Level set |z| = rho of the curvature scale on the sheet r > 0, in the regime a <= 4 rho/5, rho <= M/3:
  r = R(u), R^2 = rho^2 - a^2 u^2.  Sample points have R = rho c, a u = rho s with (c, s) Pythagorean, so
  every quantity is rational.
  (1) Gram determinant of (d_t, d_u + R' d_r, d_phi) equals rho^2 B(u),
      B = R (2M - R) - a^2 - (1 - u^2) a^4 u^2 / R^2, also for the flow d_t + Omega d_phi.
  (2) regime: r_- <= a^2/M < 3 rho/5 <= R <= rho < M, and (1 - delta) R (2M - rho) <= B <= R (2M - rho) with
      delta = (5/2) a^2/(rho (2M - rho)); B > 0 (spacelike).
  (3) the elementary bounds behind G(eps) = (1/2) int_{-1}^{1} (1 - eps u^2)^{1/4} du:
      (1 - x/4)^4 - (1 - x) = x^2 (3/8 - x/16 + x^2/256), int (1 - eps u^2/4) = 2 - eps/6,
      int (1 - eps u^2) = 2 - 2 eps/3.
  (4) the count ratio: Schwarzschild V'_0 = 4 pi rho^{3/2} sqrt(2M - rho), equal to 8 pi M sqrt(1 - rho/2M) on
      rho^3 = 2M; N/(A_+/4) = 2 nu V'/sqrt(M^2 - a^2); (1 - eps/12)^2 < 1 - a^2/M^2 in the regime.
"""
from fractions import Fraction as F
import GA  # noqa: F401  (house rule; the computation is rational arithmetic on metric components)
from tp_premise import premise


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


def gram(g, vs):
    return [[sum(v[i] * g[i][j] * w[j] for i in range(4) for j in range(4)) for w in vs] for v in vs]


def pyth(m, n):
    return (F(m * m - n * n, m * m + n * n), F(2 * m * n, m * m + n * n))


def bracket(M, a, rho, R, u):
    return R * (2 * M - R) - a * a - (1 - u * u) * a ** 4 * u * u / (R * R)


HOLES = [(F(32), F(2), F(4)), (F(500), F(4), F(10)), (F(27, 2), F(2), F(3)), (F(50), F(3), F(5)),
         (F(32), F(2048, 1025), F(4))]
ANGLES = [(7, 1), (9, 1), (12, 1), (8, -1), (15, -2)]


def pmul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def check_level_set_determinant():
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    premise("interior.complex-scale-inverse-cube-killing-spinor")
    premise("synthesis.kerr-ring-count-misses-area-law")
    seen = 0
    for (M, a, rho) in HOLES:
        for (m, n) in ANGLES:
            c, s = pyth(m, n)
            R, u = rho * c, rho * s / a
            assert R * R + a * a * u * u == rho * rho and -1 < u < 1
            g = metric(M, a, R, u)
            Rp = -a * a * u / R                                   # dR/du on the level set
            Tt = [F(1), F(0), F(0), F(0)]
            Tu = [F(0), Rp, F(1), F(0)]
            Tf = [F(0), F(0), F(0), F(1)]
            d = det(gram(g, [Tt, Tu, Tf]))
            assert d == rho * rho * bracket(M, a, rho, R, u)
            # the stored tube determinant in the angle psi (R = rho cos psi, a u = rho sin psi), times (du/dpsi)^2
            stored = -rho ** 4 * (1 + rho * rho / (a * a) * (c * c - s * s) - 2 * M * rho / (a * a) * c ** 3)
            assert d * (rho * c / a) ** 2 == stored
            assert det(gram(g, [[F(1), F(0), F(0), F(1, 13)], Tu, Tf])) == d    # any flow d_t + Omega d_phi
            seen += 1
    assert seen == 25
    # one value written out: M = 32, a = 2, rho = 4, (c, s) = (24/25, 7/25): R = 96/25, u = 14/25
    M, a, rho = HOLES[0]
    R, u = F(96, 25), F(14, 25)
    assert bracket(M, a, rho, R, u) == F(272137, 1200)
    return True


def check_regime_and_bracket_bounds():
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    for (M, a, rho) in HOLES:
        assert 5 * a <= 4 * rho and 3 * rho <= M                  # the regime
        assert a * a / M < F(3, 5) * rho                          # r_- = a^2/r_+ <= a^2/M, since r_+ >= M
        delta = F(1, 1) * a * a / (rho * (2 * M - rho))
        for (m, n) in ANGLES:
            c, s = pyth(m, n)
            R, u = rho * c, rho * s / a
            assert F(3, 5) * rho <= R <= rho < M                  # R^2 >= rho^2 - a^2 >= (9/25) rho^2
            B = bracket(M, a, rho, R, u)
            top = R * (2 * M - rho)
            assert 0 < (1 - delta) * top <= B <= top
            assert R * (rho - R) <= a * a * u * u                 # the step R (2M - R) - a^2 <= R (2M - rho)
    # the horizon radii of one exact hole: r_+ = 65536/1025, t = a/r_+ = 1/32, M = r_+ (1 + t^2)/2 = 32
    rp, t = F(65536, 1025), F(1, 32)
    M, a = rp * (1 + t * t) / 2, t * rp
    assert (M, a) == (F(32), F(2048, 1025))
    rm = t * t * rp
    assert rp * rp - 2 * M * rp + a * a == 0 and rm * rm - 2 * M * rm + a * a == 0
    assert rm == F(64, 1025) and rm < F(3, 5) * 4 and 4 < rp
    # the worst cases of the regime, as exact numbers: at a = 4 rho/5, rho = M/3
    # a^2 + a^4/(4 R^2) <= a^2 (1 + (16/25)/(4 * 9/25)) = (13/9) a^2 and 1/(3/5) * 13/9 = 65/27 <= 5/2
    assert 1 + F(16, 25) / (4 * F(9, 25)) == F(13, 9) and F(13, 9) / F(3, 5) == F(65, 27) and F(65, 27) <= F(5, 2)
    return True


def check_quarter_power_bounds():
    premise("interior.complex-scale-inverse-cube-killing-spinor")
    # (1 - x/4)^4 - (1 - x) = (3/8) x^2 - (1/16) x^3 + (1/256) x^4, nonnegative on [0, 1]
    p = [F(1), F(-1, 4)]
    p4 = pmul(pmul(p, p), pmul(p, p))
    diff = [p4[0] - 1, p4[1] + 1] + p4[2:]
    assert diff == [0, 0, F(3, 8), F(-1, 16), F(1, 256)]
    assert F(3, 8) - F(1, 16) > 0                                # so the difference is >= 0 for 0 <= x <= 1
    # integrals over [-1, 1] by antiderivatives: int (1 - eps u^2/4) = 2 - eps/6, int (1 - eps u^2) = 2 - 2 eps/3
    for eps in (F(1, 4), F(16, 25), F(4, 1025)):
        up = lambda w: w - eps * w ** 3 / 12
        lo = lambda w: w - eps * w ** 3 / 3
        assert (up(F(1)) - up(F(-1))) / 2 == 1 - eps / 12
        assert (lo(F(1)) - lo(F(-1))) / 2 == 1 - eps / 3
    return True


def check_count_ratio():
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("singularity.stretched-singularity-count")
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    # Schwarzschild: (V'_0/4 pi)^2 = rho^3 (2M - rho); on rho^3 = 2M this is (2M)^2 (1 - rho/2M)
    for (M, rho) in [(F(32), F(4)), (F(500), F(10)), (F(27, 2), F(3))]:
        assert rho ** 3 == 2 * M
        assert rho ** 3 * (2 * M - rho) == (2 * M) ** 2 * (1 - rho / (2 * M))
    # N/(A_+/4) = nu V' (2 pi/kappa_+)/(A_+/4) = 2 nu V'/sq, with kappa_+ = sq/(2 M r_+), A_+/4 = 2 pi M r_+
    rp, t = F(65536, 1025), F(1, 32)
    M, a = rp * (1 + t * t) / 2, t * rp
    sq = rp * (1 - t * t) / 2
    assert sq * sq == M * M - a * a
    kappa = sq / (2 * M * rp)
    assert kappa == (rp - t * t * rp) / (2 * (rp * rp + a * a))
    assert (2 / kappa) / (2 * M * rp) == 2 / sq                  # coefficient of nu V' (pi cancels)
    # the ratio bound (1 - eps/12)/sqrt(1 - a^2/M^2) < 1, squared, at the sample holes
    for (M, a, rho) in HOLES:
        eps = a * a / (rho * rho)
        assert eps <= F(16, 25)
        assert (1 - eps / 12) ** 2 < 1 - a * a / (M * M)
        # and in general: (1 - eps/12)^2 <= 1 - eps (1/6 - 1/225), while a^2/M^2 <= eps/9
        assert (1 - eps / 12) ** 2 <= 1 - eps * (F(1, 6) - F(1, 225))
        assert a * a / (M * M) <= eps / 9
    assert F(16, 25) / 144 == F(1, 225) and F(1, 9) < F(1, 6) - F(1, 225)
    # at the (C1) locus of M = 500 with a = 4: the count gives at most 1 - 1/75, the area law needs more than 1 - 1/15625
    M, a, rho = HOLES[1]
    assert 1 - (a * a / (rho * rho)) / 12 == F(74, 75)
    assert 1 - a * a / (M * M) == F(15624, 15625)
    return True
