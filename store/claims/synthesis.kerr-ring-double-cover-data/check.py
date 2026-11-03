"""synthesis.kerr-ring-double-cover-data: exact checks.

Complex rationals are pairs of Fractions; i is identified with the pseudoscalar I as in
interior.complex-scale-inverse-cube-killing-spinor. Oblate data: rho^2 = x^2 + y^2 = (r^2 + a^2)(1 - c^2),
Z = r c, c = cos(theta).
  (1) z^2 = w with z = r - i a c and w = rho^2 + (Z - i a)^2, on fixed (deterministically generated) rational (r, c, a);
      dw = 2a d rho - 2 i a dZ at the ring (rho = a, Z = 0), by exact differentiation of w;
  (2) the Kerr-Schild potential H = M r^3 / (r^4 + a^2 Z^2) equals M Re(1/z); it vanishes on the disc
      (r = 0, c != 0), where z is purely imaginary;
  (3) the involution (r, c) -> (-r, -c) fixes (rho^2, Z), maps z -> -z, H -> -H, scale -> -scale;
  (4) winding numbers, by exact crossing counts on rational closed polygons: the scale -M z^-3 winds
      -3 around z = 0 (double cover); along the image loop downstairs the phase of the scale turns by
      -3 pi, i.e. the scale returns to its negative.
"""
from fractions import Fraction as F
import GA  # noqa: F401  (house rule; the computation is complex-rational arithmetic)
from tp_premise import premise


class Det:
    """Deterministic integer sequence (linear congruential, exact integers only) supplying fixed
    rational test points; replaces pseudo-random sampling so the check is reproducible and exact."""

    def __init__(self, seed):
        self.x = seed

    def _next(self):
        self.x = (self.x * 1103515245 + 12345) % 2147483648
        return self.x // 65536

    def randint(self, lo, hi):
        return lo + self._next() % (hi - lo + 1)

    def choice(self, seq):
        return seq[self._next() % len(seq)]

    def sample(self, seq, k):
        pool = list(seq)
        out = []
        for _ in range(k):
            out.append(pool.pop(self._next() % len(pool)))
        return out


def cm(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cinv(a):
    n = a[0] * a[0] + a[1] * a[1]
    return (a[0] / n, -a[1] / n)


def cneg(a):
    return (-a[0], -a[1])


def scale(M, z):
    zi = cinv(z)
    return cneg((M * cm(cm(zi, zi), zi)[0], M * cm(cm(zi, zi), zi)[1]))


def winding(vals):
    """Winding number of a closed polygon of nonzero complex rationals about 0, by signed crossings of
    the positive real axis; requires consecutive points within a quarter turn (checked exactly)."""
    w = 0
    n = len(vals)
    for j in range(n):
        p, q = vals[j], vals[(j + 1) % n]
        assert p[0] * q[0] + p[1] * q[1] > 0          # angle between consecutive points < pi/2
        if p[1] < 0 <= q[1] and (p[0] > 0 or q[0] > 0):
            # crossing upward; check it crosses the positive axis: x at y = 0
            t = -p[1] / (q[1] - p[1])
            if p[0] + t * (q[0] - p[0]) > 0:
                w += 1
        elif q[1] < 0 <= p[1] and (p[0] > 0 or q[0] > 0):
            t = -p[1] / (q[1] - p[1])
            if p[0] + t * (q[0] - p[0]) > 0:
                w -= 1
    return w


def square(R, m):
    pts = []
    for k in range(m):
        pts.append((R, -R + 2 * R * F(k, m)))
    for k in range(m):
        pts.append((R - 2 * R * F(k, m), R))
    for k in range(m):
        pts.append((-R, R - 2 * R * F(k, m)))
    for k in range(m):
        pts.append((-R + 2 * R * F(k, m), -R))
    return pts


def check_double_cover_identities():
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    premise("interior.complex-factorisation-location-ring")
    premise("interior.complex-scale-inverse-cube-killing-spinor")
    premise("interior.imported-kerr-curvature")
    premise("interior.unipotency-across-kerr-family")
    # worked example: a = 2, r = 1, cos(theta) = 1/2, M = 3: rho^2 = 15/4, Z = 1/2, z = 1 - 2i(1/2) = 1 - i,
    # w = 15/4 + 1/4 - 4 - 2i = -2i = z^2; H = 3/(1 + 1) = 3/2 = 3 Re(1/(1 - i)); scale = -3 z^-3 = (3 - 3i)/4.
    a0, r0, c0, M0 = F(2), F(1), F(1, 2), F(3)
    rho20 = (r0 * r0 + a0 * a0) * (1 - c0 * c0)
    assert rho20 == F(15, 4)
    z0 = (r0, -a0 * c0)
    assert z0 == (F(1), F(-1))
    assert cm(z0, z0) == (rho20 + (r0 * c0) ** 2 - a0 * a0, -2 * a0 * r0 * c0) == (F(0), F(-2))
    assert M0 * r0 ** 3 / (r0 ** 4 + a0 * a0 * (r0 * c0) ** 2) == F(3, 2) == M0 * cinv(z0)[0]
    assert scale(M0, z0) == (F(3, 4), F(-3, 4))
    # in the unipotent Kerr-Schild gauge g = eta - 2 H k k the deviation from eta at this point has
    # coefficient -2H = -3; under the deck map H changes sign (checked on the samples below).
    assert -2 * (M0 * cinv(z0)[0]) == -3
    rng = Det(3)
    for _ in range(200):
        a = F(rng.randint(1, 9), rng.randint(1, 4))
        r = F(rng.randint(-20, 20), rng.randint(1, 7))
        c = F(rng.randint(-6, 6), 7)
        M = F(rng.randint(1, 9), rng.randint(1, 3))
        rho2 = (r * r + a * a) * (1 - c * c)
        Z = r * c
        z = (r, -a * c)
        w = (rho2 + Z * Z - a * a, -2 * a * Z)               # rho^2 + (Z - i a)^2
        assert cm(z, z) == w
        if r != 0 or c != 0:
            H = M * r ** 3 / (r ** 4 + a * a * Z * Z) if r != 0 else F(0)
            assert H == M * cinv(z)[0]                        # H = M Re(1/z)
            if r == 0:
                assert z[0] == 0 and H == 0                   # disc: z imaginary, H = 0
            # the involution
            z2 = (-r, -a * (-c))
            assert z2 == cneg(z)
            assert (r * r + a * a) * (1 - c * c) == ((-r) ** 2 + a * a) * (1 - (-c) ** 2) and (-r) * (-c) == Z
            assert M * cinv(z2)[0] == -M * cinv(z)[0]
            assert scale(M, z2) == cneg(scale(M, z))
    # dw at the ring, by differentiating w(rho, Z) = rho^2 + (Z - i a)^2 (not by hard-coding): w is
    # quadratic, so the symmetric difference quotient is the exact partial derivative.
    def w_of(rho, Z, a):
        return (rho * rho + Z * Z - a * a, -2 * a * Z)
    for a in (F(1), F(3, 2), F(7)):
        assert w_of(a, F(0), a) == (0, 0)                              # w vanishes on the ring
        for hh in (F(1), F(1, 3)):
            pr = [(x - y) / (2 * hh) for x, y in zip(w_of(a + hh, F(0), a), w_of(a - hh, F(0), a))]
            pz = [(x - y) / (2 * hh) for x, y in zip(w_of(a, hh, a), w_of(a, -hh, a))]
            assert tuple(pr) == (2 * a, 0) and tuple(pz) == (0, -2 * a)  # dw = 2a d rho - 2 i a dZ
            # real and imaginary parts independent: dw has rank two (a complex normal coordinate)
            assert pr[0] * pz[1] - pr[1] * pz[0] != 0
        # off the ring w does not vanish: zero set is {rho = a, Z = 0} on a rational sample
        for rho, Z in ((a / 2, F(0)), (a, F(1, 5)), (2 * a, F(-1, 3))):
            assert w_of(rho, Z, a) != (0, 0)
    return True


def check_windings():
    premise("interior.complex-scale-inverse-cube-killing-spinor")
    premise("interior.complex-factorisation-location-ring")
    premise("interior.imported-kerr-curvature")
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    M = F(2)
    loop = square(F(1, 3), 40)                             # a loop around z = 0 on the double cover
    assert winding(loop) == 1
    assert winding([scale(M, z) for z in loop]) == -3      # three full duality cycles, reversed
    def cpow(z, k):
        out = (F(1), F(0))
        base = z if k > 0 else cinv(z)
        for _ in range(abs(k)):
            out = cm(out, base)
        return out
    for k in (-3, -2, -1, 1, 2, 3):
        assert winding([cpow(z, k) for z in loop]) == k
    assert scale(M, loop[0]) == (-M * cpow(loop[0], -3)[0], -M * cpow(loop[0], -3)[1])
    # downstairs: one turn of w = z^2 is half a turn of z, from z0 to -z0 (the other branch)
    half = [p for p in loop if p[1] > 0 or (p[1] == 0 and p[0] > 0)]
    start = half[0]
    # the scale at the two ends of the half loop: z -> -z sends scale -> -scale (phase change by an odd
    # multiple of pi); its winding over the closed double loop is -3, so the half loop carries -3/2 turns
    assert scale(M, cneg(start)) == cneg(scale(M, start))
    w_loop = [cm(z, z) for z in loop]
    assert winding(w_loop) == 2                            # the double-cover loop covers the ring loop twice
    return True
