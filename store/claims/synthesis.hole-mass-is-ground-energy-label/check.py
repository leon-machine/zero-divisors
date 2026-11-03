"""synthesis.hole-mass-is-ground-energy-label: exact checks.

Finite spectra with integer levels e_i >= 0 (in units of one weight eps) and degeneracies g_i;
u = exp(-beta eps) is a symbol in (0, 1) and every quantity is an exact rational function of u
(GA.RF), so no exponential or logarithm is evaluated.  The theorem's analytic step is the Gibbs
identity S = beta <H'> + ln Z' (H' = H - E_0 >= 0), so that beta <H'> < S exactly when Z' > 1
and the ground energy then exceeds the free energy F = M/2.

(a) Z' > 1 (Bernstein certificate on (0, 1)) for the four listed spectra (one mode, two modes of weights 1
    and 2, a four-level ladder, a degenerate two-level spectrum) and for all 53 spectra with levels 0..3,
    ground at 0 and degeneracies at most 2 that have more than one state; Z' = 1 for the single state;
(b) u d<H'>/du = Var(H') exactly, Var > 0 on (0, 1): <H> falls as beta rises at fixed H;
(c) zero-weight counted sector: Z' = 2^|J|, <H'> = 0, so E_0 = M and Smarr is beta E_0 = 2 S,
    checked as e^{-beta E_0} = (e^{-S})^2 = 4^{-|J|}; positive weights 1, 2 give Z' = (1+u)(1+u^2);
(d) symmetric ordering: n - 1/2 = -(1/2) tanh(x/2) < 0, so beta E <= 0 < s(x) there too.
"""
from fractions import Fraction as Fr
import GA
from GA import RF
from tp_premise import premise

R0, R1 = RF.const(0), RF.const(1)
U = RF.var()


def rf(num, den):
    return RF([Fr(x) for x in num], [Fr(x) for x in den])


def comb(n, k):
    c = Fr(1)
    for i in range(k):
        c = c * (n - i) / (i + 1)
    return c


def poly_positive_open_unit(p):
    p = [Fr(c) for c in p]
    d = len(p) - 1
    if d < 0:
        return False
    b = [sum((comb(k, i) / comb(d, i) * p[i] for i in range(k + 1)), Fr(0)) for k in range(d + 1)]
    return all(x >= 0 for x in b) and any(x > 0 for x in b)


def positive_on_unit_interval(r):
    if not r.num or not r.den:
        return False
    if poly_positive_open_unit(r.num) and poly_positive_open_unit(r.den):
        return True
    return poly_positive_open_unit([-c for c in r.num]) and poly_positive_open_unit([-c for c in r.den])


def upow(k):
    out = R1
    for _ in range(k):
        out = out * U
    return out


def partition(spec):
    Z = R0
    for e, g in spec:
        Z = Z + RF.const(g) * upow(e)
    return Z


def moments(spec):
    Z = partition(spec)
    m1, m2 = R0, R0
    for e, g in spec:
        w = RF.const(g) * upow(e)
        m1 = m1 + RF.const(e) * w
        m2 = m2 + RF.const(e * e) * w
    E = m1 / Z
    return Z, E, m2 / Z - E * E


def fock(weights):
    """spectrum of sum_k w_k N_k on the Fock space of the modes (levels with multiplicity)."""
    levels = {}
    n = len(weights)
    for idx in range(2 ** n):
        e = sum(w for s, w in enumerate(weights) if (idx >> s) & 1)
        levels[e] = levels.get(e, 0) + 1
    return sorted(levels.items())


def check_ground_energy_exceeds_free_energy():
    premise("singularity.kms-uniqueness-factor")
    premise("synthesis.quarter-from-temperature")
    # one fermion mode, two modes of weights 1 and 2, a truncated oscillator, a degenerate ground
    specs = [fock([1]), fock([1, 2]), [(0, 1), (1, 1), (2, 1), (3, 1)], [(0, 2), (1, 3)]]
    expected = [rf([1, 1], [1]), rf([1, 1, 1, 1], [1]), rf([1, 1, 1, 1], [1]), rf([2, 3], [1])]
    for spec, z in zip(specs, expected):
        Z = partition(spec)
        assert (Z - z).is_zero()
        assert positive_on_unit_interval(Z - R1)          # Z' > 1, so beta <H'> < S
    # the single nondegenerate level is the only exception: Z' = 1 and S = 0
    assert (partition([(0, 1)]) - R1).is_zero()
    # every spectrum with levels 0..3 (ground at 0) and degeneracies at most 2, more than one state
    count = 0
    for g0 in (1, 2):
        for g1 in range(3):
            for g2 in range(3):
                for g3 in range(3):
                    spec = [(e, g) for e, g in ((0, g0), (1, g1), (2, g2), (3, g3)) if g]
                    if sum(g for _, g in spec) == 1:
                        assert (partition(spec) - R1).is_zero()
                        continue
                    assert positive_on_unit_interval(partition(spec) - R1)
                    count += 1
    assert count == 53


def check_heat_capacity_sign():
    premise("singularity.kms-uniqueness-factor")
    for spec, var in [(fock([1]), rf([0, 1], [1, 2, 1])),
                      ([(0, 1), (1, 1), (2, 1)], rf([0, 1, 4, 1], [1, 2, 3, 2, 1]))]:
        Z, E, V = moments(spec)
        assert (V - var).is_zero()
        assert (U * E.deriv() - V).is_zero()               # u dE/du = Var
        assert positive_on_unit_interval(V)                # so dE/dbeta = -eps Var < 0


def check_zero_weight_split():
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.boundary-mode-thermal-entropy")
    for J in range(1, 7):
        spec = fock([0] * J)
        Z, E, V = moments(spec)
        assert (Z - RF.const(2 ** J)).is_zero() and E.is_zero() and V.is_zero()
        # e^{-S} = 2^{-J}; Z_total = e^{-beta E_0} Z' = e^{-S} forces e^{-beta E_0} = 4^{-J}
        eS = Fr(1, 2 ** J)
        assert eS / 2 ** J == Fr(1, 4 ** J) == eS * eS
    # positive weights 1, 2: Z' = (1 + u)(1 + u^2) > 1 and <H'> > 0, so M/2 < E_0 < M
    Z, E, V = moments(fock([1, 2]))
    assert (Z - rf([1, 1], [1]) * rf([1, 0, 1], [1])).is_zero()
    assert positive_on_unit_interval(E) and positive_on_unit_interval(Z - R1)


def check_symmetric_ordering():
    premise("synthesis.boundary-mode-thermal-entropy")
    # n = u/(1+u) with u = e^{-x}; tanh(x/2) = (1 - u)/(1 + u)
    n = rf([0, 1], [1, 1])
    half = RF.const(Fr(1, 2))
    tanh_half = rf([1, -1], [1, 1])
    assert (n - half + half * tanh_half).is_zero()
    assert positive_on_unit_interval(half - n)          # beta E = x (n - 1/2) <= 0 < s(x)
    # at zero weight (u = 1) both orderings give zero energy
    assert (n - half).eval(1) == 0 and tanh_half.eval(1) == 0
