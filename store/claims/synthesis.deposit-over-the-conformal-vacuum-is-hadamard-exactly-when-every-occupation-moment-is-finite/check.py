"""A homogeneous deposit over the conformal vacuum of a Weyl-flat descended field: exact checks.

Spacetime algebra Cl(1,3), e0^2 = +1, e1^2 = e2^2 = e3^2 = -1; the unit imaginary is I4 = e0 e1 e2 e3
(I4^2 = -1). Massless Dirac field in the conformal picture (comoving momenta p, energy |p|).

(1) The massless shell projectors (matrix reading of left multiplication): for a unit spatial vector n
    (n^2 = -1), Lambda_pm(n) = (1 pm n e0)/2 are idempotent, complementary, mutually annihilating,
    Dirac-self-adjoint (e0 reverse(L) e0 = L), with scalar part 1/2; Lambda_+ = p e0/(2 p0) for the null
    p = p0 (e0 + n). So the deposit's remainder kernel is a superposition of plane waves with bounded
    projector weights: |R| <= (2 pi)^-3 M_0 a^-3 (bounded remainder from M_0 alone).
(2) Coincidence data have one sign: for z = c + s I4 with c^2 + s^2 = 1 (the phase of a plane wave at a
    step), z z^-1 = 1 with z^-1 = c - s I4, and (z + z^-1 - 2)^m = (-1)^m ((c - 1)^2 + s^2)^m; and in the
    frequency omega of the remainder along a timelike line (particles at omega = |p| with weight +n_+,
    antiparticles at omega = -|p| with weight -n_-, the sign of the b b^dag reordering), omega^(2m+1)
    times the weight is |p|^(2m+1) n_pm >= 0 for both: the odd time derivatives at coincidence are positive
    superpositions, so their finiteness forces the moments (Bochner and the moment lemma, proof).
(3) The thermal (Fermi-Dirac) profile: with y = e^-x in (0, 1], n_FD = y/(1 + y) <= y = e^-x, and
    int_0^inf x^k e^-x dx = k! (antiderivative -e^-x P_k, P_k = sum_j k!/j! x^j, checked as the polynomial
    identity P_k - P_k' = x^k); so per helicity and species M_k <= 4 pi (k + 2)! T^(k+3), finite for all k.
(4) The power-tail profile n = (1 + p/T)^-6: with q = p/(1 + p) the radial moments are
    int_0^1 q^(2+k) (1 - q)^(2-k) dq: 1/30, 1/20, 1/5 for k = 0, 1, 2 (exact polynomial integrals), so the
    number, the mean energy 3T/2 and the energy spread c = M_2 M_0 / M_1^2 = 8/3 are finite (the stored
    shot term is finite), while for k = 3 the dyadic pieces [1 - 2^(1-j), 1 - 2^-j] each contribute at
    least (1 - 2^(1-j))^5 / 2, so the partial integrals grow without bound: M_3 (and every higher moment)
    is infinite. The profile is a valid occupation (between 0 and 1).
(The conformal-covariance lemma and the homogeneity of the flat massless kernel are checked in the result
filed alongside on Weyl-flat fields; clause (v)'s bound is proof-only.)
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1)
E = [GA.gen(i) for i in range(4)]
I4 = GA.mul(GA.mul(E[0], E[1], S), GA.mul(E[2], E[3], S), S)
ONE = GA.sc(1)
# Pythagorean unit spatial directions (n1, n2, n3) with n1^2 + n2^2 + n3^2 = 1
DIRS = [(F(3, 13), F(4, 13), F(12, 13)), (F(1, 3), F(2, 3), F(2, 3)), (F(2, 7), F(-3, 7), F(6, 7)),
        (F(0), F(0), F(1)), (F(-4, 9), F(4, 9), F(7, 9))]


P0S = (F(1), F(5, 2), F(7))
PHASES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]
MS = list(range(1, 6))
PABS = (F(1, 3), F(2), F(9))
OCCS = ((F(1, 2), F(1, 5)), (F(1, 3), F(1)), (F(1), F(3, 4)))
YS = (F(1), F(1, 2), F(1, 7), F(3, 100), F(1, 10 ** 6))
KS = list(range(0, 16))
TAIL_PS = (F(0), F(1, 3), F(2), F(50))
PIECES = list(range(1, 41))


def mul(*xs):
    out = ONE
    for x in xs:
        out = GA.mul(out, x, S)
    return out


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def scalar_part(x):
    return x.get((), F(0))


def check_massless_shell_projectors():
    premise("field-theory.second-quantisation")
    premise("synthesis.imported-microlocal-hadamard-condition")
    ok = True
    for n1, n2, n3 in DIRS:
        ok &= n1 * n1 + n2 * n2 + n3 * n3 == 1
        n = vec((0, n1, n2, n3))
        ne0 = mul(n, E[0])
        ok &= GA.eq(mul(ne0, ne0), ONE)
        Lp = GA.scal(F(1, 2), GA.add(ONE, ne0))
        Lm = GA.scal(F(1, 2), GA.sub(ONE, ne0))
        ok &= GA.eq(mul(Lp, Lp), Lp) and GA.eq(mul(Lm, Lm), Lm)
        ok &= GA.eq(GA.add(Lp, Lm), ONE) and GA.is_zero(mul(Lp, Lm))
        for L in (Lp, Lm):
            ok &= GA.eq(mul(E[0], GA.reverse(L), E[0]), L)
            ok &= scalar_part(L) == F(1, 2)
        for p0 in P0S:
            p = GA.add(GA.scal(p0, E[0]), GA.scal(p0, n))
            ok &= GA.dot(p, p, S) == 0
            ok &= GA.eq(GA.scal(1 / (2 * p0), mul(p, E[0])), Lp)
            ok &= GA.is_zero(mul(p, Lp))
    GA.check("massless shell projectors (1 pm n e0)/2: idempotent, complementary, Dirac-self-adjoint, "
             "scalar part 1/2, Lambda_+ = p e0/(2 p0) on the null shell, p Lambda_+ = 0", ok)
    return ok


def check_coincidence_differences_have_one_sign():
    premise("synthesis.imported-microlocal-hadamard-condition")
    ok = GA.eq(mul(I4, I4), GA.scal(-1, ONE))
    for a, b, c in PHASES:
        cs, sn = F(a, c), F(b, c)
        z = GA.add(GA.scal(cs, ONE), GA.scal(sn, I4))
        zi = GA.sub(GA.scal(cs, ONE), GA.scal(sn, I4))
        ok &= GA.eq(mul(z, zi), ONE)
        d = GA.sub(GA.add(z, zi), GA.scal(2, ONE))
        mag = (cs - 1) ** 2 + sn ** 2
        ok &= mag > 0
        acc = ONE
        for m in MS:
            acc = mul(acc, d)
            ok &= GA.eq(acc, GA.scal((-1) ** m * mag ** m, ONE))
    for m in MS:
        for pabs in PABS:
            for npl, nmi in OCCS:
                part = pabs ** (2 * m + 1) * npl               # omega = +|p|, weight +n_+
                anti = (-pabs) ** (2 * m + 1) * (-nmi)         # omega = -|p|, weight -n_-
                ok &= part > 0 and anti > 0 and part + anti == pabs ** (2 * m + 1) * (npl + nmi)
                even = (-pabs) ** (2 * m) * (-nmi)
                ok &= even < 0 < pabs ** (2 * m) * npl         # even orders mix the signs
    GA.check("(z + 1/z - 2)^m = (-1)^m |z - 1|^(2m) for unit z = c + s I4, and odd powers of the frequency "
             "give particles and antiparticles the same sign: coincidence data are positive superpositions", ok)
    return ok


def poly_factorial_antiderivative(k):
    """P_k(x) = sum_{j<=k} k!/j! x^j as a coefficient list (index = power)."""
    fact = [1]
    for j in range(1, k + 1):
        fact.append(fact[-1] * j)
    return [F(fact[k], fact[j]) for j in range(k + 1)]


def check_thermal_profile_has_every_moment():
    premise("hawking.i-state")
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    ok = True
    for y in YS:
        ok &= y / (1 + y) < y                     # n_FD = y/(1 + y) below y = e^-x
    facts = []
    for k in KS:
        P = poly_factorial_antiderivative(k)
        facts.append(P[0])
        # (d/dx)(-e^-x P) = e^-x (P - P'): need P - P' = x^k
        diff = GA.padd(P, GA.pneg(GA.pderiv(P)))
        ok &= GA.ptrim(diff) == GA.ptrim([F(0)] * k + [F(1)])
    # int_0^inf x^k e^-x dx = k!; the moment of order k is bounded by 16 pi (k + 2)! T^(k+3)
    ok &= facts[:8] == [1, 1, 2, 6, 24, 120, 720, 5040]
    ok &= [16 * facts[k + 2] for k in range(4)] == [32, 96, 384, 1920]
    GA.check("Fermi-Dirac profile below e^-x; int x^k e^-x = k! exactly (polynomial identity P - P' = x^k), "
             "so every moment of the thermal deposit is finite", ok)
    return ok


def pint01(poly):
    return sum((c / (j + 1) for j, c in enumerate(poly)), F(0))


def binom_poly(a, b):
    """q^a (1 - q)^b for integers a, b >= 0 as a coefficient list."""
    p = [F(0)] * a + [F(1)]
    for _ in range(b):
        p = GA.pmul(p, [F(1), F(-1)])
    return p


def check_power_tail_profile_has_finite_shot_term_but_not_every_moment():
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    premise("synthesis.imported-microlocal-hadamard-condition")
    ok = True
    expo = 6
    M = [pint01(binom_poly(2 + k, expo - 4 - k)) for k in range(3)]
    ok &= M == [F(1, 30), F(1, 20), F(1, 5)]
    mean_energy = M[1] / M[0]
    c_spread = M[2] * M[0] / (M[1] * M[1])
    ok &= mean_energy == F(3, 2) and c_spread == F(8, 3)
    # occupation between 0 and 1 at sample momenta
    for p in TAIL_PS:
        occ = 1 / (1 + p) ** expo
        ok &= 0 < occ <= 1
    # k = 3: integrand q^5 (1 - q)^-1; dyadic piece [1 - 2^(1-j), 1 - 2^-j] has length 2^-j, there
    # 1/(1 - q) >= 2^(j-1) and q^5 >= (1 - 2^(1-j))^5, so it contributes at least (1 - 2^(1-j))^5 / 2
    partial = F(0)
    for j in PIECES:
        lo = 1 - F(1, 2 ** (j - 1))
        piece = lo ** (2 + 3) * F(2 ** (j - 1)) * F(1, 2 ** j)
        partial += piece
        if j >= 3:
            ok &= piece >= F(1, 10)
    ok &= partial > 3
    GA.check("power-tail profile (1 + p/T)^-6: number, mean energy 3T/2 and spread 8/3 finite (stored shot term "
             "finite), third and higher moments infinite (dyadic lower bounds)", ok)
    return ok


if __name__ == "__main__":
    for fn in (check_massless_shell_projectors, check_coincidence_differences_have_one_sign,
               check_thermal_profile_has_every_moment,
               check_power_tail_profile_has_finite_shot_term_but_not_every_moment):
        fn()
    print("FAILURES:", GA.FAILURES)
