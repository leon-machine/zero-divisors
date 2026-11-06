"""Referee P, own routes.
(1) Exact: the swapped-band form of P1 (vi)(c) recomputed in position space, not momentum space.
    form(x) = -2 i eta <x, T rho_0 x> with eta = -1, T = T0 + D, D(u, v) = -(i/pi)(1 - cos 2s)/s, s = u - v.
    For x = e^{-l u}: vacuum part (1/pi)(1/l); D part -(2/pi) int_0^inf e^{-l s}(1 - cos 2s) ds = -(2/pi)(1/l - l/(l^2+4)).
(2) Exploration only (floats): the translation-KMS Loewner function is digamma(beta a/2pi + 1/2) up to constants."""
from fractions import Fraction as F
def laplace_one_minus_cos(l, b):      # int_0^inf e^{-l s}(1 - cos b s) ds
    return 1 / l - l / (l * l + b * b)
for l in (F(1), F(4), F(3, 2)):
    vac = 1 / l
    band = vac - 2 * laplace_one_minus_cos(l, 2)
    mom = F(-1) / l + 2 * l / (l * l + 4)
    print("lambda", l, ": position-space form * pi =", band, "; P1 momentum-space value =", mom, "; agree:", band == mom)
try:
    import mpmath as mp
    mp.mp.dps = 30
    for beta in (2 * mp.pi, mp.mpf(3)):
        def H(a):
            f = lambda p: mp.tanh(beta * p / 2) * (p / (a * a + p * p) - p / (1 + p * p))
            return -mp.quad(f, [0, 1, 10, mp.inf])
        for a in (mp.mpf('0.5'), mp.mpf(2), mp.mpf(7)):
            lhs = H(a) - H(1)
            rhs = mp.digamma(beta * a / (2 * mp.pi) + mp.mpf(1) / 2) - mp.digamma(beta / (2 * mp.pi) + mp.mpf(1) / 2)
            print("beta", mp.nstr(beta, 6), "a", a, "H(a)-H(1) =", mp.nstr(lhs, 15), " psi diff =", mp.nstr(rhs, 15))
except ImportError:
    print("mpmath not available")
