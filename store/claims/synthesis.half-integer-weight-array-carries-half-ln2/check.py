"""synthesis.half-integer-weight-array-carries-half-ln2: exact checks.

Rigorous rational bounds (Fractions with outward rounding; no floating point):
pi from Machin's formula with bracketing alternating partial sums; e^{-pi} from the Taylor
series of e^{pi} with an explicit remainder; ln(1 + u) from bracketing alternating partial
sums; ln 2 = sum 1/(k 2^k) with an explicit tail; the tail of the array sum from
s(x) <= (1 + x) e^{-x}.  The mode entropy is s(x) = ln(1 + e^{-x}) + x e^{-x}/(1 + e^{-x}),
increasing in e^{-x} and in x at fixed e^{-x} for the second term, which is how lower and
upper bounds are assembled.

(i)   the array with weights kappa (k + 1/2) has entropy S_half = 2 sum_{k>=0} s((2k+1) pi)
      with |S_half - ln 2 / 2| < 10^-57 (the bound that holds without the theta identities);
(ii)  the array with weights kappa k has S_0 = ln 2 + 2 sum_{k>=1} s(2 pi k) in
      (0.720396698946605, 0.720396698946606), the value of the store's clause (vi), and
      1/(4 S_0) in (0.3470310, 0.3470311);
(after iii) one Euclidean period is the rotor -1 (R(pi) = B, R(2 pi) = B^2 = -1 in Cl(2,0)), and on a
      four-mode window with weights k + 1/2 the phase of exp(2 pi i K) is (-1)^N on every
      basis state, while for weights k it is 1.
"""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise

PREMISES = (
    "synthesis.boundary-mode-thermal-entropy",
    "synthesis.residue-from-mode-entropy",
    "state-selection.where-fermi-dirac-comes",
    "singularity.bosonisation-bridge-s-wave-sector",
)

DEN = 10 ** 70


def rd(x):
    return series.round_down(x, DEN)


def ru(x):
    return series.round_up(x, DEN)


def arctan_inv(m, N):
    """(lo, hi): the partial sums of arctan(1/m) to N and N + 1 terms."""
    return series.arctan_inv_bracket(m, N + 1)


def pi_bounds():
    a5 = arctan_inv(5, 60)
    a239 = arctan_inv(239, 30)
    return (rd(16 * a5[0] - 4 * a239[1]), ru(16 * a5[1] - 4 * a239[0]))


def exp_bounds(x, N):
    s, term = F(0), F(1)
    for n in range(N):
        s += term
        term = term * x / (n + 1)
    rem = term / (1 - x / (N + 1))
    return (rd(s), ru(s + rem))


def ln1p_bounds(u, N):
    s, p = F(0), F(1)
    for k in range(1, N + 1):
        p = p * u
        s += F((-1) ** (k + 1)) * p / k
    t = s + F((-1) ** (N + 2)) * p * u / (N + 1)
    return (rd(min(s, t)), ru(max(s, t)))


def ln2_bounds(N):
    s = sum(F(1, k * 2 ** k) for k in range(1, N + 1))
    return (rd(s), ru(s + F(1, (N + 1) * 2 ** N)))


def q_bounds():
    pl, pu = pi_bounds()
    el, eu = exp_bounds(pu, 120), exp_bounds(pl, 120)
    return pl, pu, rd(1 / el[1]), ru(1 / eu[0])     # bounds on pi and on e^{-pi}


def array_entropy(ns, with_zero_mode, K):
    """ns(k) = n with x_k = n pi; sum over k in range(K) of 2 s(x_k), plus ln 2 if a zero mode."""
    pl, pu, ql, qu = q_bounds()
    lo, hi = (ln2_bounds(260) if with_zero_mode else (F(0), F(0)))
    for k in range(K):
        n = ns(k)
        ul, uu = rd(ql ** n), ru(qu ** n)
        a, b = ln1p_bounds(ul, 40), ln1p_bounds(uu, 40)
        lo += 2 * (a[0] + rd(n * pl * ul / (1 + ul)))
        hi += 2 * (b[1] + ru(n * pu * uu / (1 + uu)))
    tail = F(0)
    n0 = ns(K)
    for n in range(n0, n0 + 120, 2):
        tail += (1 + n * pu) * qu ** n
    hi += 2 * (ru(tail) + F(1, 10 ** 60))
    return rd(lo), ru(hi)


def check_half_offset_half_bit():
    premise("synthesis.imported-theta-function-identities")
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("singularity.bosonisation-bridge-s-wave-sector")
    lo, hi = array_entropy(lambda k: 2 * k + 1, False, 26)
    l2 = ln2_bounds(260)
    ok = hi - lo < F(1, 10 ** 57)
    ok = ok and lo - l2[1] / 2 > -F(1, 10 ** 57) and hi - l2[0] / 2 < F(1, 10 ** 57)
    # and it is not ln 2: the half offset carries half a bit, the zero offset more than one
    ok = ok and hi < F(7, 20)
    GA.check("(i) weights kappa(k + 1/2): array entropy within 10^-57 of ln2/2", ok)
    return ok


def check_zero_offset_value():
    premise("synthesis.imported-theta-function-identities")
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("synthesis.residue-from-mode-entropy")
    lo, hi = array_entropy(lambda k: 2 * k + 2, True, 26)
    ok = lo > F(720396698946605, 10 ** 15) and hi < F(720396698946606, 10 ** 15)
    ok = ok and 1 / (4 * hi) > F(3470310, 10 ** 7) and 1 / (4 * lo) < F(3470311, 10 ** 7)
    # ratio to the registered density: ln 2 / S_0 in (0.96, 0.97), which holds no p/q, q <= 4
    l2 = ln2_bounds(260)
    rlo, rhi = l2[0] / hi, l2[1] / lo
    ok = ok and rlo > F(96, 100) and rhi < F(97, 100)
    ok = ok and not any(rlo <= F(p, q) <= rhi for q in range(1, 5) for p in range(0, 5))
    GA.check("(ii) weights kappa k: array entropy 0.720396698946605..., arrays per Planck "
             "area 0.3470310...", ok)
    return ok


def check_recurrence_signs():
    premise("synthesis.imported-theta-function-identities")
    premise("state-selection.where-fermi-dirac-comes")
    premise("singularity.bosonisation-bridge-s-wave-sector")
    sq = (1, 1)                                    # Cl(2,0): e1^2 = e2^2 = +1
    B = GA.mul(GA.gen(0), GA.gen(1), sq)           # Euclidean rotation bivector
    ok = GA.eq(GA.mul(B, B, sq), GA.sc(-1))        # R(pi) = B, so R(2 pi) = B^2 = -1
    n = 4
    for idx in range(2 ** n):
        bits = [(idx >> j) & 1 for j in range(n)]
        N = sum(bits)
        twoK_half = sum((2 * j + 1) * b for j, b in enumerate(bits))   # 2 K, weights j + 1/2
        twoK_int = sum(2 * j * b for j, b in enumerate(bits))          # 2 K, weights j
        # exp(2 pi i K) = exp(i pi (2K)): sign (-1)^(2K)
        ok = ok and (twoK_half - N) % 2 == 0 and twoK_int % 2 == 0
    GA.check("(after iii) one Euclidean period is the rotor -1; half-integer weights make the "
             "Killing flow at 2 pi / kappa the parity (-1)^N, integer weights the identity", ok)
    return ok


def run():
    return all([check_half_offset_half_bit(), check_zero_offset_value(), check_recurrence_signs()])


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
