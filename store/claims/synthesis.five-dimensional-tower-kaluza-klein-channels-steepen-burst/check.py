"""synthesis.five-dimensional-tower-kaluza-klein-channels-steepen-burst: exact checks.

check_level_sum: the Kaluza-Klein levels of a five-dimensional tower's field on a fifth direction of
  extent L_f have masses k pi/L_f, k >= 0 (natural condition at the ends) or 2 pi |k|/L_f, k in Z
  (circle); in both cases the level count below mu differs from L_f mu/pi by at most one. With
  h = pi M/L_f and a per-level coefficient psi(M mu) of bounded variation, the level sum S(h) obeys
  |h S(h) - int psi| <= h TV(psi): checked exactly on polynomial shapes of compact support (monotone
  and not), with exact expected sums, so the summed coefficient is (L_f/(pi M)) int psi + O(1).
check_mass_time_law: with M^2 |dM/dt| = A + B/M (B the Kaluza-Klein term), the remaining lifetime
  t(M) = int_0^M m^3 dm/(A m + B) lies between M^4/(4(B + A M)) and M^4/(4B) and between
  M^3/(3A) - B M^2/(2A^2) and M^3/(3A): checked through the integrand bounds, exactly, by polynomial
  integration; the pure Kaluza-Klein law M^4 = 4 B tau holds on fourth powers, and no constant D
  makes it a time rescaling of M^3 = 3 Psi_0 tau.
check_tail_steepening: the time-integrated primary tail N(E) = int phi(E M) M^3 dM/(A M + B) for a
  flux shape phi(x) >= 0 supported on [x_lo, x_hi] is bracketed exactly (piecewise bounds on the
  denominator, exact polynomial integrals); E^4 N(E) lies in [C_3/(B + A x_hi/E), C_3/B] and closes on
  C_3/B as E grows, E^3 N(E) closes on C_2/A as E falls (C_k = int phi x^k), and N(2E)/N(E) lies
  near 1/16 above the break and near 1/8 below it; the pure laws hold exactly.
"""
from fractions import Fraction as F
import GA
from GA import pmul
from tp_premise import premise


def pint(p, lo, hi):
    """Exact integral of a polynomial (coefficient list) from lo to hi."""
    tot = F(0)
    for k, c in enumerate(p):
        tot += c * (F(hi) ** (k + 1) - F(lo) ** (k + 1)) / (k + 1)
    return tot


def peval(p, x):
    return sum((c * F(x) ** k for k, c in enumerate(p)), F(0))


# shapes on [0, 1] (zero beyond 1): (polynomial, exact integral, exact total variation on [0, inf))
SHAPES = [
    ([F(1), F(-2), F(1)], F(1, 3), F(1)),                 # (1 - y)^2, monotone, TV = psi(0) = 1
    ([F(0), F(1), F(-1)], F(1, 6), F(1, 2)),              # y (1 - y), rises to 1/4 and falls: TV = 1/2
    ([F(0), F(0), F(1), F(-1)], F(1, 12), F(8, 27)),      # y^2 (1 - y), max 4/27 at 2/3: TV = 8/27
]


def neumann_sum(p, h):
    """sum_{k >= 0} psi(k h) for psi supported on [0, 1]."""
    tot, k = F(0), 0
    while k * h <= 1:
        tot += peval(p, k * h)
        k += 1
    return tot


def circle_sum(p, h):
    """sum_{k in Z} psi(2 |k| h): levels 2 pi |k|/L_f, doubly degenerate above zero."""
    tot, k = peval(p, 0), 1
    while 2 * k * h <= 1:
        tot += 2 * peval(p, 2 * k * h)
        k += 1
    return tot


def check_level_sum():
    premise("dark-tower-matter.five-dimensional-towers")
    premise("dark-matter.sourcing-rule-forced-not-chosen")
    premise("hawking.greybody-inheritance-under-interface-premise")
    for p, integral, tv in SHAPES:
        assert pint(p, 0, 1) == integral
        for N in (7, 10, 33, 64):
            h = F(1, N)
            for S in (neumann_sum(p, h), circle_sum(p, h)):
                assert abs(h * S - integral) <= h * tv
            # level count below mu: N(mu) - L_f mu/pi in [0, 1] (Neumann), (-1, 1] (circle)
            for mu in (F(1, 3), F(5, 7), F(1)):
                nn = sum(1 for k in range(0, 2 * N + 2) if k * h <= mu)
                nc = 1 + 2 * sum(1 for k in range(1, 2 * N + 2) if 2 * k * h <= mu)
                assert 0 <= nn - mu / h <= 1 and -1 < nc - mu / h <= 1
    # exact expected values (mutation sensitivity): (1 - y)^2 at h = 1/10: (N+1)(2N+1)/(6N) = 77/20
    assert neumann_sum(SHAPES[0][0], F(1, 10)) == F(77, 20)
    assert neumann_sum(SHAPES[1][0], F(1, 10)) == F(33, 20)
    assert circle_sum(SHAPES[0][0], F(1, 10)) == F(17, 5)
    # linear growth in L_f/M: halving h doubles the sum up to the variation bound
    s1, s2 = neumann_sum(SHAPES[0][0], F(1, 32)), neumann_sum(SHAPES[0][0], F(1, 64))
    assert abs(s2 - 2 * s1) <= 2 * SHAPES[0][2]
    assert s2 > F(64, 3) and s1 > F(32, 3)
    GA.check("Kaluza-Klein level sum = (L_f/(pi M)) int psi + O(TV): grows linearly in L_f/M", True)
    return True


def check_mass_time_law():
    premise("hawking.greybody-inheritance-under-interface-premise")
    premise("dark-matter.parallel-boundary-mode-spaces-one-wall")
    premise("dark-tower-matter.five-dimensional-towers")
    for A, B in ((F(1), F(1)), (F(3, 2), F(1, 5)), (F(2, 7), F(9))):
        for M in (F(1, 10), F(1), F(4)):
            lo = M ** 4 / (4 * (B + A * M))
            hi = M ** 4 / (4 * B)
            # integrand bounds m^3/(B + A M) <= m^3/(A m + B) <= m^3/B on [0, M], at sample points
            for j in range(0, 11):
                m = M * F(j, 10)
                f = m ** 3 / (A * m + B)
                assert m ** 3 / (B + A * M) <= f <= m ** 3 / B
                # large-mass bounds m^2/A - B m/A^2 <= f <= m^2/A
                assert m ** 2 / A - B * m / A ** 2 <= f <= m ** 2 / A
            # integrating the bounding polynomials gives the stated brackets exactly
            assert pint([F(0), F(0), F(0), 1 / (B + A * M)], 0, M) == lo
            assert pint([F(0), F(0), F(0), 1 / B], 0, M) == hi
            assert pint([F(0), -B / A ** 2, 1 / A], 0, M) == M ** 3 / (3 * A) - B * M ** 2 / (2 * A ** 2)
            assert lo < hi
            # 4 B t / M^4 lies in [B/(B + A M), 1]: tends to 1 as M -> 0
            assert 4 * B * lo / M ** 4 == B / (B + A * M)
    # the squeeze tightens as M falls
    A, B = F(1), F(1)
    gaps = [1 - B / (B + A * M) for M in (F(1), F(1, 10), F(1, 100))]
    assert gaps == [F(1, 2), F(1, 11), F(1, 101)]
    # pure Kaluza-Klein law: M^4 = 4 B tau, on fourth powers (B = 1/4: M^4 = tau)
    B = F(1, 4)
    Ds = []
    for tau, M in ((F(1), F(1)), (F(16), F(2)), (F(81), F(3))):
        assert M ** 4 == 4 * B * tau
        # d(M^4)/dtau = 4 B: M^3 dM/dtau = B, with dM/dtau = 1/(4 M^3) here
        assert M ** 3 * (1 / (4 * M ** 3)) == B
        # the constant D needed for M_B(tau) = M_Psi0(D tau), M_Psi0(s)^3 = 3 Psi0 s, Psi0 = 1
        Ds.append(M ** 3 / (3 * tau))
    assert Ds == [F(1, 3), F(1, 6), F(1, 9)]
    assert len(set(Ds)) == 3
    GA.check("mass-time law: M^4/(4(B+AM)) <= t(M) <= M^4/(4B); pure Kaluza-Klein M^4 = 4 B tau, "
             "not a time rescaling of M^3 = 3 Psi_0 tau", True)
    return True


def mixed_tail_bracket(phi, xlo, xhi, A, B, E, K=8):
    """Exact lower and upper bounds on N(E) = int phi(E M) M^3/(A M + B) dM over the support
    xlo/E <= M <= xhi/E (phi >= 0 there), from K subintervals on which the denominator is bounded
    by its end values; each piece is an exact polynomial integral."""
    phiE = [c * E ** k for k, c in enumerate(phi)]
    integrand = pmul(phiE, [F(0), F(0), F(0), F(1)])
    lo_sum, hi_sum = F(0), F(0)
    for i in range(K):
        a = xlo / E + (xhi - xlo) / E * F(i, K)
        b = xlo / E + (xhi - xlo) / E * F(i + 1, K)
        piece = pint(integrand, a, b)
        assert piece >= 0
        lo_sum += piece / (A * b + B)
        hi_sum += piece / (A * a + B)
    return lo_sum, hi_sum


def mixed_tail_bracket_low(phi, xlo, xhi, A, B, E):
    """Bounds on the same N(E) from M^3/(A M + B) = (M^2/A)/(1 + B/(A M)), the last factor lying
    between its values at the ends of the support; the M^2 integral is computed exactly."""
    phiE = [c * E ** k for k, c in enumerate(phi)]
    J = pint(pmul(phiE, [F(0), F(0), F(1)]), xlo / E, xhi / E) / A
    assert J >= 0
    return J / (1 + B * E / (A * xlo)), J / (1 + B * E / (A * xhi))


def check_tail_steepening():
    premise("hawking.greybody-inheritance-under-interface-premise")
    premise("dark-matter.parallel-boundary-mode-spaces-one-wall")
    premise("synthesis.dimmed-burst-time-rescaled-copy")
    # phi(x) = (x - 1/2)(1 - x) on [1/2, 1], nonnegative there
    phi = [F(-1, 2), F(3, 2), F(-1)]
    xlo, xhi = F(1, 2), F(1)
    for j in range(0, 11):
        assert peval(phi, xlo + (xhi - xlo) * F(j, 10)) >= 0
    C2 = pint(pmul(phi, [F(0), F(0), F(1)]), xlo, xhi)
    C3 = pint(pmul(phi, [F(0), F(0), F(0), F(1)]), xlo, xhi)
    assert C2 == F(23, 1920) and C3 == F(3, 320)
    A, B = F(1), F(1)
    # mixed law A M + B: E^4 N(E) computed (bracketed exactly) and squeezed onto C3/B at high energy
    prev = None
    for E in (F(100), F(1000), F(10000)):
        lo, hi = mixed_tail_bracket(phi, xlo, xhi, A, B, E)
        lo4, hi4 = E ** 4 * lo, E ** 4 * hi
        assert C3 / (B + A * xhi / E) <= lo4 <= hi4 <= C3 / B
        if prev is not None:
            assert C3 / B - lo4 < prev / 9
        prev = C3 / B - lo4
    lo, hi = mixed_tail_bracket(phi, xlo, xhi, A, B, F(10000))
    assert C3 / B - F(10000) ** 4 * lo < C3 / 9000
    assert not (F(10000) ** 4 * lo <= C2 / B <= F(10000) ** 4 * hi)
    # ... and E^3 N(E) squeezed onto C2/A at low energy
    for E in (F(1, 100), F(1, 1000)):
        lo, hi = mixed_tail_bracket_low(phi, xlo, xhi, A, B, E)
        plo, phi_ = mixed_tail_bracket(phi, xlo, xhi, A, B, E)
        assert max(lo, plo) <= min(hi, phi_)            # the two computed brackets of N(E) overlap
        lo3, hi3 = E ** 3 * lo, E ** 3 * hi
        assert lo3 <= hi3 <= C2 / A
    lo, hi = mixed_tail_bracket_low(phi, xlo, xhi, A, B, F(1, 1000))
    assert C2 / A - F(1, 1000) ** 3 * lo < C2 / 400
    assert not (F(1, 1000) ** 3 * lo <= C3 / A <= F(1, 1000) ** 3 * hi)
    # local spectral index: N(2E)/N(E) near 1/16 above the break, near 1/8 below it
    lo1, hi1 = mixed_tail_bracket(phi, xlo, xhi, A, B, F(1000))
    lo2, hi2 = mixed_tail_bracket(phi, xlo, xhi, A, B, F(2000))
    assert F(1, 17) < lo2 / hi1 <= hi2 / lo1 < F(1, 15)
    lo1, hi1 = mixed_tail_bracket_low(phi, xlo, xhi, A, B, F(1, 2000))
    lo2, hi2 = mixed_tail_bracket_low(phi, xlo, xhi, A, B, F(1, 1000))
    assert F(1, 9) < lo2 / hi1 <= hi2 / lo1 < F(1, 7)
    # B = 0 (no Kaluza-Klein term): E^3 N(E) = C2/A exactly
    for E in (F(2), F(7, 3)):
        phiE = [c * E ** k for k, c in enumerate(phi)]
        N = pint(pmul(phiE, [F(0), F(0), F(1)]), xlo / E, xhi / E) / A
        assert E ** 3 * N == C2 / A
    # pure Kaluza-Klein (A = 0): E^4 N(E) = C3/B exactly: index -4
    for E in (F(2), F(7, 3)):
        phiE = [c * E ** k for k, c in enumerate(phi)]
        N = pint(pmul(phiE, [F(0), F(0), F(0), F(1)]), xlo / E, xhi / E) / B
        assert E ** 4 * N == C3 / B
        assert E ** 3 * N != C3 / B
    GA.check("primary tail of the mixed law: E^-3 below the break, E^-4 above it (computed brackets)", True)
    return True
