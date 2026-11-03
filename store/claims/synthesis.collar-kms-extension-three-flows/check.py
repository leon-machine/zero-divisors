"""synthesis.collar-kms-extension-three-flows: exact checks.

Units 2M = 1: A = 1/r - 1, horizon r = 1, kappa = 1/2, tau = (2/3) r^{3/2} S(r) with
S(r) = sum_n binom(2n, n) 4^{-n} * 3/(2n + 3) r^n, the series of tau = int_0^r sqrt(x/(1-x)) dx.
Rates of the t-line holonomy on the slice r: Killing rho(r) = 1/(2 r^2); Hubble-normalised
rho_H(r) = tau |A'| / (2 sqrt A) = (1/3) S(r) (1 - r)^{-1/2}; rapidity 1.
Checks, as exact truncated series: S's first coefficients against the stored collar form; rho_H =
1/3 + 4/15 r + ... against the stored rate; the Killing-KMS state with rapidity period 2 pi on the
horizon slice has rapidity period 2 pi / r^2 and local Hubble-normalised inverse temperature
6 pi (1 - r)^{1/2} / (r^2 S(r)), so r^2 beta_H,loc / (6 pi) = 1 - 4/5 r + ...; the Hubble-KMS state
at 6 pi has rapidity period 2 pi (1 + 4/5 r + ...); the ratio rho_H / rho = tau sqrt(r/(1-r)) is
strictly increasing (its series coefficients are positive and it is a product of increasing
factors). On two slices (4x4 product of matrix factors) the unique KMS state of a product flow is
the product of Gibbs states, and two non-proportional rate profiles have no common KMS state.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

N = 8


def S_series(N):
    # binom(2n, n) 4^{-n} built exactly by the ratio c_n / c_{n-1} = (2n - 1) / (2n)
    out, c = [], F(1)
    for n in range(N + 1):
        if n > 0:
            c = c * F(2 * n - 1, 2 * n)
        out.append(c * F(3, 2 * n + 3))
    return out


def check_collar_rates_and_temperatures():
    premise("singularity.imported-interior-collar-kasner-form")
    premise("singularity.modular-flow-boundary-modes-holonomy-universal")
    S = S_series(N)
    assert S[:3] == [F(1), F(3, 10), F(9, 56)]
    # tau = (2/3) r^{3/2} S: d tau / dr = sqrt(r/(1-r)) = r^{1/2} (1 - r)^{-1/2}
    # derivative of (2/3) r^{3/2} S = r^{1/2} [ S + (2/3) r S' ]
    lhs = [S[n] + F(2, 3) * n * S[n] for n in range(N + 1)]
    one_minus_r = [F(1), F(-1)] + [F(0)] * (N - 1)
    rhs = GA.ps_pow_rat(one_minus_r, F(-1, 2), N)
    assert lhs == rhs
    # Hubble-normalised rate on the slice r
    rhoH = [F(1, 3) * c for c in GA.ps_mul(S, rhs, N)]
    assert rhoH[:2] == [F(1, 3), F(4, 15)]
    # Killing rate from the metric: rho = -A'/2 with A = (1 - r)/r, an identity in Q(r)
    A = GA.RF([F(1), F(-1)], [F(0), F(1)])
    rho = A.deriv() * GA.RF.const(F(-1, 2))
    assert rho.eqrf(GA.RF([F(1, 2)], [F(0), F(0), F(1)]))           # rho = 1/(2 r^2)
    kappa = rho.eval(F(1))
    assert kappa == F(1, 2)                                           # surface gravity, 2M = 1
    beta_over_pi = 2 / kappa                                          # (R) at the horizon slice
    period_over_pi = rho * GA.RF.const(beta_over_pi)                  # rapidity period / pi on slice r
    assert period_over_pi.eqrf(GA.RF([F(2)], [F(0), F(0), F(1)]))    # = 2 / r^2
    for r in [F(1), F(1, 2), F(1, 4), F(1, 8)]:
        assert (period_over_pi.eval(r) == 2) == (r == 1)
        assert period_over_pi.eval(r) >= 2
    # local Hubble-normalised inverse temperature of that state, times r^2 / pi, by two routes:
    # route 1: beta_K * (r^2 rho) / rho_H, from the rate series; route 2: 6 sqrt(1-r)/S
    r2rho = (rho * GA.RF([F(0), F(0), F(1)], [F(1)])).eval(F(7, 3))   # r^2 rho is constant
    assert r2rho == F(1, 2)
    route1 = [beta_over_pi * r2rho * c for c in GA.ps_inv(rhoH, N)]
    sqrt1mr = GA.ps_pow_rat(one_minus_r, F(1, 2), N)
    loc = GA.ps_mul(sqrt1mr, GA.ps_inv(S, N), N)
    route2 = [6 * c for c in loc]
    assert route1 == route2
    assert route1[:2] == [F(6), F(-24, 5)]                            # 6 pi r^-2 (1 - 4r/5 + ...)
    # Hubble-KMS at beta_H = 6 pi: rapidity period / (2 pi) = 3 rho_H = S (1 - r)^{-1/2}
    per = [3 * c for c in rhoH]
    assert per[:2] == [F(1), F(4, 5)]
    # rho_H / rho = tau sqrt(r/(1-r)) = (2/3) r^2 S (1-r)^{-1/2}: positive coefficients
    ratio = [F(2, 3) * c for c in GA.ps_mul(S, rhs, N)]
    assert all(c > 0 for c in ratio)
    assert all(c > 0 for c in S) and all(c > 0 for c in rhs)
    return True


def mm(A, B):
    return [[sum((A[i][l] * B[l][j] for l in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def diag(xs):
    return [[xs[i] if i == j else F(0) for j in range(len(xs))] for i in range(len(xs))]


def check_product_kms_and_no_common_state():
    premise("singularity.kms-uniqueness-factor")
    premise("singularity.imported-general-form")
    # two slices, K_r = N_r - 1/2; product basis |n1 n2>, generator f1 K1 + f2 K2.
    # e^{-beta f_k K_k} on |n> is y_k^{(1 - 2n)} with y_k = e^{beta f_k / 2}; use y rational.
    def gibbs(y1, y2):
        ent = []
        for n1 in (0, 1):
            for n2 in (0, 1):
                ent.append(y1 ** (1 - 2 * n1) * y2 ** (1 - 2 * n2))
        Z = sum(ent)
        return diag([e / Z for e in ent]), diag(ent)
    units = [[[F(int((i, j) == (a, b))) for j in range(4)] for i in range(4)] for a in range(4) for b in range(4)]
    # profile f = (1, 2) at e^{beta/2} = 2: y = (2, 4)
    rho, S = gibbs(F(2), F(4))
    Si = diag([1 / S[i][i] for i in range(4)])
    for A in units:
        for B in units:
            assert tr(mm(rho, mm(A, mm(S, mm(B, Si))))) == tr(mm(rho, mm(B, A)))   # KMS for f at beta
    # product form: rho = rho_1 (x) rho_2
    p1 = [F(2), F(1, 2)]; p2 = [F(4), F(1, 4)]
    Z1, Z2 = sum(p1), sum(p2)
    assert [rho[i][i] for i in range(4)] == [p1[a] / Z1 * p2[b] / Z2 for a in (0, 1) for b in (0, 1)]
    # profile g = (1, 3): a g-KMS state at any beta' is diag(y'^{(1-2n1)} y'^{3(1-2n2)}); equality of
    # population ratios with rho needs y'^2 = 2^2 (slice 1) and y'^6 = 4^2 (slice 2): 4^3 != 16
    r1 = rho[0][0] / rho[2][2]           # slice-1 ratio  = y1^2 = 4
    r2 = rho[0][0] / rho[1][1]           # slice-2 ratio  = y2^2 = 16
    assert r1 == 4 and r2 == 16
    assert r1 ** 3 != r2                 # g-KMS would need r2 = r1^3
    assert r1 ** 2 == r2                 # consistent with f = (1, 2): r2 = r1^2
    return True
