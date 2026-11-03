"""synthesis.exceptional-boundary-measure-c1-c2-one-calibration: exact checks.

Schwarzschild interior, units G = c = 1 kept general in M: write 2M = a^2, r = s^2, x = r/2M = s^2/a^2.
Synchronous form ds^2 = dtau^2 - A dt^2 - r^2 dOmega^2, A = 2M/r - 1, tau(r) = int_0^r A^(-1/2).
All series are power series in x with Fraction coefficients, truncated at order NS.

(1) tau = (2 s^3 / 3a) T(x), T_k = 3 c_k/(2k+3), c_k = binom(2k,k)/4^k; A (dtau/dr)^2 = 1 exactly
    (tau is the unit-speed, Killing-invariant defining function of E = {tau = 0}); the scale factors
    sqrt(A) ~ tau^(-1/3), r ~ tau^(2/3): Kasner exponents with p1+p2+p3 = 1 = p1^2+p2^2+p3^2.
(2) slice volume per unit Killing time vol = 4 pi a s^3 (1-x)^(1/2) (checked against the GA volume
    trivector of the frame at rational points); vol/tau = 6 pi a^2 (1-x)^(1/2)/T(x) -> 6 pi a^2 = 12 pi M:
    the weighted limit mu_E is finite and nonzero because the exponents sum to one.
(3) curvature eigenvalue (2M/r^3) tau^2 = (4/9) T^2 -> 4/9: the eigenvalue threshold lambda is the
    proper time tau_c = (2/3) lambda^(-1/2) at leading order, so nu' = nu tau_c = (2/3) kappa_s with
    kappa_s = nu lambda^(-1/2).
(4) at tau_c = (2/3) T(x_c) (exactly the slice 2M/r^3 = 1) vol = 8 pi M (1-x_c)^(1/2), the store's count
    volume; at a general eigenvalue threshold K the leading count is 12 pi M nu tau_c = 8 pi M nu K^(-1/2).
(5) calibration: N ln2 = S_BH over the modular epoch 8 pi M  <=>  nu' ln2 = 1/(24 pi), equivalently
    kappa_s ln2 = 1/(16 pi).
"""
from fractions import Fraction as F
from GA import mul as gmul, gen, scal, reverse, add, sub
from tp_premise import premise

NS = 9


def binom(n, k):
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


def s_sqrt1m(n=NS):                       # (1 - x)^(1/2)
    out, c = [], F(1)
    for k in range(n):
        out.append(c)
        c = c * (F(1, 2) - k) / (k + 1) * (-1)
    return out


def s_isqrt1m(n=NS):                      # (1 - x)^(-1/2)
    return [F(binom(2 * k, k), 4 ** k) for k in range(n)]


def s_mul(p, q):
    out = [F(0)] * NS
    for i, u in enumerate(p):
        for j, v in enumerate(q):
            if i + j < NS:
                out[i + j] += u * v
    return out


def s_inv(p):
    out = [F(0)] * NS
    out[0] = 1 / p[0]
    for n in range(1, NS):
        out[n] = -sum(p[k] * out[n - k] for k in range(1, n + 1)) / p[0]
    return out


def tau_T():                               # tau = (2 s^3/(3 a)) T(x)
    return [3 * c / (2 * k + 3) for k, c in enumerate(s_isqrt1m())]


SQ = (1, -1, -1, -1)


def check_kasner_defining_function():
    premise("interior.kasner-form-interior")
    premise("singularity.imported-interior-collar-kasner-form")
    T = tau_T()
    assert T[0] == 1 and T[1] == F(3, 10)                 # tau = (2/3) r^(3/2) (1 + 3r/10 + ...), 2M = 1
    # unit speed: with r = s^2, dtau/ds = 2 s^2 (a^2 - s^2)^(-1/2), so in units a = 1 the s-series of
    # dtau/ds / (2 s^2) must be (1 - x)^(-1/2); from tau = (2/3) s^3 T(x), x = s^2:
    # dtau/ds = 2 s^2 sum_k T_k (2k+3)/3 x^k
    d = [T[k] * (2 * k + 3) / 3 for k in range(NS)]
    assert d == s_isqrt1m()
    # A (dtau/dr)^2 = 1: dtau/dr = (1/2s) dtau/ds = s (a^2 - s^2)^(-1/2), A = (a^2 - s^2)/s^2
    for a, s in [(F(5), F(3)), (F(13), F(5)), (F(5, 2), F(3, 2))]:
        A = (a * a - s * s) / (s * s)
        dtdr_sq = s * s / (a * a - s * s)
        assert A * dtdr_sq == 1
    # any F(r) with A F'^2 = 1 has F' = +- A^(-1/2); F(0) = 0 then forces F = +- tau: no free constant.
    # Kasner exponents: sqrt(A) ~ a/s and tau ~ 2 s^3/(3a), so sqrt(A) ~ tau^(-1/3), r = s^2 ~ tau^(2/3)
    p = [F(-1, 3), F(2, 3), F(2, 3)]
    assert 3 * p[0] == -1 and 3 * p[1] == 2               # powers of s: -1 = 3 p1, 2 = 3 p2
    assert sum(p) == 1 and sum(q * q for q in p) == 1
    return True


def check_measure_limit():
    premise("interior.kasner-form-interior")
    premise("scrambling.slice-volume-exactly-per-unit-killing")
    # GA: the frame trivector (sqrt(A) e1) ^ (r e2) ^ (r e3) has squared magnitude A r^4 at rational points
    # with A a rational square; vol per steradian = sqrt(A) r^2 = s^3 sqrt(a^2 - s^2) (here a s^3 (1-x)^(1/2))
    for a, s, rootA in [(F(5), F(3), F(4, 3)), (F(13), F(5), F(12, 5)), (F(5, 2), F(3, 2), F(4, 3))]:
        A = (a * a - s * s) / (s * s)
        assert rootA * rootA == A
        r = s * s
        B = gmul(gmul(scal(rootA, gen(1)), scal(r, gen(2)), SQ), scal(r, gen(3)), SQ)
        mag2 = gmul(B, reverse(B), SQ).get((), F(0))
        assert mag2 == -A * r ** 4                       # e1 e2 e3 (e1 e2 e3)~ = e1^2 e2^2 e3^2 = -1
        assert rootA * r * r == s ** 3 * (rootA * s) and (rootA * s) ** 2 == a * a - s * s
    # vol / tau = 4 pi a s^3 (1-x)^(1/2) / (2 s^3 T/(3a)) = 6 pi a^2 (1-x)^(1/2)/T
    ratio = s_mul(s_sqrt1m(), s_inv(tau_T()))
    assert ratio[0] == 1                                  # mu_E = 6 pi a^2 = 12 pi M per unit t
    assert ratio[1] == F(-4, 5)
    # exponent bookkeeping: vol ~ tau^(p1+p2+p3); dividing by tau^w is finite and nonzero iff w = 1
    p = [F(-1, 3), F(2, 3), F(2, 3)]
    for w in [F(0), F(2, 3), F(1), F(3, 2)]:
        e = sum(p) - w
        assert (e == 0) == (w == 1)
    return True


def check_threshold_to_proper_time():
    premise("interior.imported-schwarzschild-curvature-spectrum")
    T = tau_T()
    T2 = s_mul(T, T)
    # (2M/r^3) tau^2 = (a^2/s^6)(4 s^6/(9 a^2)) T^2 = (4/9) T^2
    eig = [F(4, 9) * c for c in T2]
    assert eig[0] == F(4, 9) and eig[1] == F(4, 15) and eig[2] == F(32, 175)
    # eigenvalue threshold 2M/r^3 = lam  <=>  tau_c^2 = (4/9)/lam at leading order, so
    # nu' = nu tau_c = (2/3) nu lam^(-1/2) = (2/3) kappa_s: check (nu tau_c)^2 = (4/9) (nu lam^(-1/2))^2
    for lam, tc in [(F(1), F(2, 3)), (F(4), F(1, 3)), (F(1, 9), F(2))]:
        assert tc * tc * lam == F(4, 9)
        nu = F(5, 7)
        assert (nu * tc) ** 2 == F(4, 9) * nu * nu / lam
    return True


def check_store_count_recovered():
    premise("singularity.stretched-singularity-count")
    T = tau_T()
    ratio = s_mul(s_sqrt1m(), s_inv(T))
    # at the (C1) slice tau_c = (2/3) T(x_c): vol = 6 pi a^2 tau_c ratio = 4 pi a^2 T ratio = 8 pi M (1-x)^(1/2)
    vol_over_8piM = s_mul([F(2, 3) * F(3, 2) * c for c in T], ratio)
    assert vol_over_8piM == s_sqrt1m()
    # leading count at threshold K: 12 pi M nu tau_c with tau_c^2 = 4/(9K): (12 tau_c)^2 = 64/K
    for K in (F(1), F(4), F(1, 16)):
        tc2 = F(4, 9) / K
        assert 144 * tc2 * K == 64
    # so the count sees nu and the threshold only through nu' = nu tau_c (at leading order); the first
    # correction differs between the two descriptions: (1-x)^(1/2) = 1 - x/2 at the (C1) slice
    assert s_sqrt1m()[1] == F(-1, 2) and ratio[1] == F(-4, 5)
    return True


def check_calibration():
    premise("singularity.area-law-test")
    premise("singularity.modular-descent")
    # pi-power bookkeeping: a quantity c pi^k is stored as (c, k)
    def pm(u, v):
        return (u[0] * v[0], u[1] + v[1])
    mu_rate = (F(12), 1)                                  # 12 pi M per unit Killing time (coefficient of M)
    epoch = (F(8), 1)                                     # modular period 8 pi M
    muE = pm(mu_rate, epoch)                              # 96 pi^2 M^2
    assert muE == (F(96), 2)
    SBH = (F(4), 1)                                       # 4 pi M^2
    nup = (SBH[0] / muE[0], SBH[1] - muE[1])              # nu' ln2 = S_BH / mu_E
    assert nup == (F(1, 24), -1)
    kappa_s = (nup[0] * F(3, 2), nup[1])                  # nu' = (2/3) kappa_s
    assert kappa_s == (F(1, 16), -1)                      # kappa_s ln2 = 1/(16 pi)
    # the same from the slice count: 8 pi kappa_s M over 8 pi M equals 4 pi M^2 / ln2
    assert pm((F(8), 1), pm(kappa_s, epoch)) == SBH
    return True
