"""state-selection.where-fermi-dirac-comes: exact checks.

(1) The Euclidean rotor (Proposition state-selection.euclidean-partner-curvature-selected): in Cl(1,3), sigma_r =
    e0 e1, I = e0 e1 e2 e3, J = I sigma_r with J^2 = -1, R(c, s) = c + s J for a rational point (c, s) of the
    unit circle standing for (cos(theta/2), sin(theta/2)). The group law R(c1, s1) R(c2, s2) = R(c1 c2 - s1 s2,
    c1 s2 + s1 c2) holds at sample points; R_pi = R(0, 1) = J, R_2pi = R_pi^2 = -1, R_4pi = +1; conjugation by
    R_pi moves e0 (so the conjugation period is not pi) and conjugation by R_2pi is the identity on every blade.
(2) Even and odd sectors (Theorem singularity.descent-parity-average): on the completed pair in Cl(1,1),
    v = (e0 + e1)/2, v* = (e0 - e1)/2, grading element sigma = e0 e1 (sigma^2 = 1), E(x) = (x + sigma x sigma)/2
    fixes the even blades and kills v, v* (the odd sector, the ladder generators). R_2pi = -1 acts trivially by
    conjugation on every blade. On the ladder generators it acts by the module action, -1 . v = -v; extended
    factorwise to every word x_1 ... x_n in v, v* (n <= 4) it gives (-1)^n x_1 ... x_n, and this equals the
    parity automorphism sigma x sigma on every nonzero word: +1 on the even words, -1 on the odd words, so one
    action separates the two sectors. Odd correlator: for one mode (a, a^dag on C^2, H = w N, thermal state
    rho = diag(1, q)/(1 + q), q = e^{-beta w}) the Euclidean ordered correlator G(tau) = e^{-tau w} Tr(rho a a^dag)
    for 0 < tau < beta and s e^{-tau w} Tr(rho a^dag a) for -beta < tau < 0, with s the grading sign of the
    generator (sigma v sigma = s v, computed: s = -1), has G(tau - beta) / G(tau) = s: antiperiodic, at sample q.
    For the even observable N (s = +1, N commutes with H) the same ratio is +1: periodic.
(3) The statistics: for one fermionic mode (M_2, a a^dag + a^dag a = 1) the KMS identity
    omega(a^dag a) = q omega(a a^dag), q = e^{-beta w}, solved over all 2 x 2 density matrices gives
    n = q/(1 + q) = 1/(e^{beta w} + 1); the commutator case omega(b b^dag) = 1 + omega(b^dag b) solved for n gives
    q/(1 - q) = 1/(e^{beta w} - 1): the sign of the denominator is the sign of the (anti)commutator, at sample q.
Not checked: the Matsubara reading itself, which the claim flags as the standard reading.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
S11 = GA.sig(1, 1)
CIRCLE = [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13)), (F(-8, 17), F(15, 17)), (F(1), F(0))]
QS = [F(1, 2), F(9, 16), F(1, 7)]


def rotor(c, s, J):
    return GA.add(GA.sc(c), GA.scal(s, J))


def check_euclidean_rotor_period():
    premise("state-selection.euclidean-partner-curvature-selected")
    I = GA.mul(GA.mul(GA.gen(0), GA.gen(1), S13), GA.mul(GA.gen(2), GA.gen(3), S13), S13)
    J = GA.mul(I, GA.mul(GA.gen(0), GA.gen(1), S13), S13)
    ok = GA.mul(J, J, S13) == {(): F(-1)}
    for c1, s1 in CIRCLE:
        for c2, s2 in CIRCLE:
            lhs = GA.mul(rotor(c1, s1, J), rotor(c2, s2, J), S13)
            ok = ok and GA.eq(lhs, rotor(c1 * c2 - s1 * s2, c1 * s2 + s1 * c2, J))
    Rpi = rotor(F(0), F(1), J)
    R2pi = GA.mul(Rpi, Rpi, S13)
    ok = ok and GA.eq(Rpi, J) and R2pi == {(): F(-1)} and GA.mul(R2pi, R2pi, S13) == {(): F(1)}
    Rpi_inv = rotor(F(0), F(-1), J)
    ok = ok and not GA.eq(GA.mul(GA.mul(Rpi, GA.gen(2), S13), Rpi_inv, S13), GA.gen(2))
    for b in GA.all_blades(4):
        x = {b: F(1)}
        ok = ok and GA.eq(GA.mul(GA.mul(R2pi, x, S13), R2pi, S13), x)
    _tp_rv = (ok); assert _tp_rv is not False, "check_euclidean_rotor_period"; return _tp_rv


def check_even_sector_periodic_odd_sector_antiperiodic():
    premise("singularity.descent-parity-average")
    e0, e1 = GA.gen(0), GA.gen(1)
    sigma = GA.mul(e0, e1, S11)
    ok = GA.mul(sigma, sigma, S11) == {(): F(1)}
    v = GA.scal(F(1, 2), GA.add(e0, e1))
    vs = GA.scal(F(1, 2), GA.sub(e0, e1))

    def E(x):
        return GA.scal(F(1, 2), GA.add(x, GA.mul(GA.mul(sigma, x, S11), sigma, S11)))

    def alpha(x):
        return GA.mul(GA.mul(sigma, x, S11), sigma, S11)
    even = [GA.sc(1), sigma, GA.mul(vs, v, S11), GA.mul(v, vs, S11)]
    odd = [v, vs, e0, e1]
    ok = ok and all(GA.eq(E(x), x) for x in even) and all(E(x) == {} for x in odd)
    minus = GA.sc(-1)
    ok = ok and all(GA.eq(GA.mul(GA.mul(minus, x, S11), minus, S11), x) for x in even + odd)
    # R_2pi = -1 on the ladder generators, extended factorwise to words: equals alpha, sector by sector
    words = [([], GA.sc(1))]
    n_even = n_odd = 0
    for length in range(1, 5):
        words = [(w + [g], GA.mul(x, g, S11)) for w, x in words for g in (v, vs)]
        for w, x in words:
            if GA.is_zero(x):
                continue
            moved = GA.sc(1)
            for g in w:
                moved = GA.mul(moved, GA.mul(minus, g, S11), S11)
            ok = ok and GA.eq(moved, alpha(x))
            if length % 2 == 0:
                ok = ok and GA.eq(alpha(x), x) and GA.eq(E(x), x)
                n_even += 1
            else:
                ok = ok and GA.eq(alpha(x), GA.neg(x)) and E(x) == {}
                n_odd += 1
    ok = ok and (n_even, n_odd) == (4, 4)
    # grading sign of the ladder generator, then the ordered thermal correlator of one mode
    s = F(-1) if GA.eq(alpha(v), GA.neg(v)) else F(1)
    ok = ok and s == -1 and GA.eq(alpha(vs), GA.scal(s, vs))
    a = [[F(0), F(1)], [F(0), F(0)]]
    ad = [[F(0), F(0)], [F(1), F(0)]]

    def mm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

    def tr(A):
        return A[0][0] + A[1][1]
    N = mm(ad, a)
    for q in QS:
        rho = [[1 / (1 + q), F(0)], [F(0), q / (1 + q)]]
        ok = ok and tr(rho) == 1
        g_gt, g_lt = tr(mm(rho, mm(a, ad))), tr(mm(rho, mm(ad, a)))
        # e^{-(tau - beta) w} = e^{-tau w} / q: G(tau - beta) / G(tau) = s g_lt / (q g_gt)
        ok = ok and s * g_lt / (q * g_gt) == -1
        # even observable N: diagonal, so e^{tau H} N e^{-tau H} = N; its correlator Tr(rho N N) is
        # tau-independent and its ordering sign is the grading sign of the number element v v*
        nn = tr(mm(rho, mm(N, N)))
        s_even = F(1) if GA.eq(alpha(GA.mul(v, vs, S11)), GA.mul(v, vs, S11)) else F(-1)
        ok = ok and N[0][1] == 0 and N[1][0] == 0 and nn == q / (1 + q) and s_even * nn / nn == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_even_sector_periodic_odd_sector_antiperiodic"; return _tp_rv


def check_anticommutator_gives_fermi_dirac():
    ok = True
    for q in QS:
        # density rho = diag(p0, p1) + off-diagonal; KMS with K = N: omega(E_ab E_cd) = (w_a/w_b) omega(E_cd E_ab)
        w = [F(1), q]
        rows = []
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        row = [F(0)] * 4
                        if b == c:
                            row[2 * d + a] += 1
                        if d == a:
                            row[2 * b + c] -= w[a] / w[b]
                        rows.append(row)
        ker = GA.field_kernel(rows)
        ok = ok and len(ker) == 1
        rho = ker[0]
        n = rho[3] / (rho[0] + rho[3])
        ok = ok and n == q / (1 + q) and n == 1 / (1 / q + 1)
        # commutator (Bose) relation: n = q (1 + n)
        nb = q / (1 - q)
        ok = ok and nb == q * (1 + nb) and nb == 1 / (1 / q - 1) and nb != n
    _tp_rv = (ok); assert _tp_rv is not False, "check_anticommutator_gives_fermi_dirac"; return _tp_rv
