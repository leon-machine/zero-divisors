"""synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets: exact checks.

A doublet is an even element phi of Cl(3,0) (basis 1, e23, e31, e12); the weak generators act by left multiplication
by B_a / 2 (B = e23, e31, e12) and hypercharge by right multiplication, phi -> -phi e12 / 2; the real form is
<phi, psi> = <phi~ psi>_0. Two doublets Phi = (phi1, phi2), eight real components. Invariants N_k = <phi_k~ phi_k>_0,
K = <psi>_0^2 + <psi>_{12}^2 and K' = <psi>_{23}^2 + <psi>_{31}^2 with psi = phi1~ phi2.
V = lam (N1 + N2 - w)^2 + mu (N1 - N2)^2 + kap K, a gauge-invariant quartic.
(1) The generators: a representation of su(2) + u(1) by antisymmetric maps, no nonzero joint invariant vector.
(2) Gauge invariance of N, K, K' under rational rotors, and <grad V, X Phi> = 0 at samples.
(3) The degree-two identity Hess V(v)(h, X v) + <grad V(v), X h> = 0, and the obstruction <grad V(v), X h> nonzero
    at a non-stationary vacuum, zero at the stationary vacua used below.
(4) Goldstone rank: 0 at Phi = 0, 3 exactly when Phi != 0 and K' = 0 (the doublets aligned over span{1, e12}),
    4 otherwise, on all 3^8 pairs with entries in {-1, 0, 1}; K + K' = N1 N2.
(5) Two potentials: kap = -1, w = 3/2 has global minima N1 = N2 = 1, K = 1 (aligned, rank 3, value -3/4);
    kap = +1, w = 2 has global minima N1 = N2 = 1, K = 0 (rank 4, value 0); both stationary there.
(6) The lift locus: with the dictionary (z1, z2) -> z1 + e31 z2, z = x + y e12, the complex form is psi's
    span{1, e12} part; on phi2^dagger phi1 = -H^2 the rank is 3 exactly when N1 N2 = H^4 and 4 otherwise.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = GA.sig(3, 0)
ONE = ()
E23, E13, E12 = (1, 2), (0, 2), (0, 1)          # e31 = -e13
BASIS = [GA.sc(1), {E23: F(1)}, {E13: F(-1)}, {E12: F(1)}]   # 1, e23, e31, e12
BIV = [{E23: F(1)}, {E13: F(-1)}, {E12: F(1)}]


def q(c):
    """even element from coordinates on 1, e23, e31, e12"""
    return GA.add(*[GA.scal(F(x), b) for x, b in zip(c, BASIS)])


def coords(x):
    return [x.get(ONE, F(0)), x.get(E23, F(0)), -x.get(E13, F(0)), x.get(E12, F(0))]


def ip(x, y):
    return GA.mul(GA.reverse(x), y, SQ).get(ONE, F(0))


def gen_action(a, phi):
    if a < 3:
        return GA.scal(F(1, 2), GA.mul(BIV[a], phi, SQ))
    return GA.scal(F(-1, 2), GA.mul(phi, BIV[2], SQ))


def act(a, P):
    return (gen_action(a, P[0]), gen_action(a, P[1]))


def vec(P):
    return coords(P[0]) + coords(P[1])


def from_vec(v):
    return (q(v[:4]), q(v[4:]))


def inner(P, R):
    return ip(P[0], R[0]) + ip(P[1], R[1])


def invariants(P):
    N1, N2 = ip(P[0], P[0]), ip(P[1], P[1])
    psi = GA.mul(GA.reverse(P[0]), P[1], SQ)
    c = coords(psi)
    return N1, N2, c[0] ** 2 + c[3] ** 2, c[1] ** 2 + c[2] ** 2


def V(P, lam, mu, kap, w):
    N1, N2, K, _ = invariants(P)
    return lam * (N1 + N2 - w) ** 2 + mu * (N1 - N2) ** 2 + kap * K


def line_coeffs(f, v, h):
    """coefficients of the degree-4 polynomial t -> f(v + t h), exactly, by interpolation at t = 0..4"""
    ts = [F(t) for t in range(5)]
    ys = [f(from_vec([a + t * b for a, b in zip(v, h)])) for t in ts]
    # Newton divided differences, then expand
    n = len(ts)
    coef = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (ts[i] - ts[i - j])
    poly = [F(0)] * n
    for i in range(n - 1, -1, -1):
        # poly = poly * (t - ts[i]) + coef[i]
        new = [F(0)] * n
        for k in range(n - 1):
            new[k + 1] += poly[k]
        for k in range(n):
            new[k] -= ts[i] * poly[k]
        new[0] += coef[i]
        poly = new
    return poly


def d1(f, v, h):
    return line_coeffs(f, v, h)[1]


def hess(f, v, h, k):
    s = [a + b for a, b in zip(h, k)]
    return line_coeffs(f, v, s)[2] - line_coeffs(f, v, h)[2] - line_coeffs(f, v, k)[2]


def unit(i):
    return [F(1) if j == i else F(0) for j in range(8)]


def grad(f, v):
    return [d1(f, v, unit(i)) for i in range(8)]


def rank_at(P):
    return GA.mat_rank([vec(act(a, P)) for a in range(4)])


def pot(lam, mu, kap, w):
    return lambda P: V(P, F(lam), F(mu), F(kap), F(w))


# (1) --------------------------------------------------------------------------------------------

def check_generators_form_the_electroweak_algebra_on_two_doublets():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent")
    ok = True
    samples = [(q([1, 2, -1, 3]), q([0, 1, 1, -2])), (q([F(1, 2), 0, 3, 1]), q([2, -1, 0, F(1, 3)]))]
    for P in samples:
        for a in range(4):
            for b in range(4):
                lhs = [x - y for x, y in zip(vec(act(a, act(b, P))), vec(act(b, act(a, P))))]
                if a < 3 and b < 3 and a != b:
                    c = 3 - a - b
                    sign = F(-1) if (a, b) in ((0, 1), (1, 2), (2, 0)) else F(1)
                    rhs = [sign * x for x in vec(act(c, P))]
                else:
                    rhs = [F(0)] * 8
                ok = ok and lhs == rhs
        for a in range(4):
            for R in samples:
                ok = ok and inner(act(a, P), R) == -inner(P, act(a, R))
    # no nonzero vector of R^8 is fixed by all four generators
    rows = []
    for i in range(8):
        e = from_vec(unit(i))
        rows.append(sum((vec(act(a, e)) for a in range(4)), []))
    ok = ok and GA.mat_rank(rows) == 8
    GA.check("su(2) + u(1) on two doublets in Cl(3,0)^+: a representation by antisymmetric maps, no invariant vector",
             ok)
    return ok


# (2) --------------------------------------------------------------------------------------------

def check_potential_is_gauge_invariant():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    ok = True
    rot = [GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), b)) for b in BIV]
    samples = [(q([1, 2, -1, 3]), q([0, 1, 1, -2])), (q([F(1, 2), 0, 3, 1]), q([2, -1, 0, F(1, 3)]))]
    for P in samples:
        inv = invariants(P)
        ok = ok and inv[2] + inv[3] == inv[0] * inv[1]
        for U in rot:
            L = (GA.mul(U, P[0], SQ), GA.mul(U, P[1], SQ))
            ok = ok and invariants(L) == inv
        Rr = rot[2]
        Rt = (GA.mul(P[0], Rr, SQ), GA.mul(P[1], Rr, SQ))
        ok = ok and invariants(Rt) == inv
        f = pot(1, 2, -3, 5)
        g = grad(f, vec(P))
        for a in range(4):
            ok = ok and sum(x * y for x, y in zip(g, vec(act(a, P)))) == 0
    # K is not invariant under a non-gauge map (left e12 on one doublet only): the test is not vacuous
    P = samples[0]
    U = rot[0]
    ok = ok and invariants((GA.mul(U, P[0], SQ), P[1]))[2] != invariants(P)[2]
    GA.check("N1, N2, K, K' are invariant under rational weak and hypercharge rotors; <grad V, X Phi> = 0", ok)
    return ok


# (3) --------------------------------------------------------------------------------------------

def check_free_brst_symmetry_needs_a_stationary_vacuum():
    premise("synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent")
    premise("synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta")
    ok = True
    f = pot(1, 1, -1, F(3, 2))
    v_off = [F(1), F(0), F(0), F(0), F(0), F(1, 2), F(0), F(0)]    # not stationary
    hs = [unit(i) for i in range(8)] + [[F(1), F(-1), F(2), F(0), F(1), F(0), F(-1), F(3)]]
    obstruction = []
    for v in (v_off, [F(1), F(0), F(0), F(-2), F(1), F(1), F(0), F(0)]):
        g = grad(f, v)
        for a in range(4):
            Xv = vec(act(a, from_vec(v)))
            for h in hs:
                Xh = vec(act(a, from_vec(h)))
                o = sum(x * y for x, y in zip(g, Xh))
                ok = ok and hess(f, v, h, Xv) + o == 0
                if v is v_off:
                    obstruction.append(o)
    ok = ok and any(o != 0 for o in obstruction)
    # pinned values at the non-stationary point: V = 5/8, gradient (2, 0, 0, 0, 0, -2, 0, 0), and the obstruction
    # matrix <grad V, X_a e_i> (rows a, columns i) with eight entries of modulus one
    g = grad(f, v_off)
    ok = ok and f(from_vec(v_off)) == F(5, 8) and g == [F(2), 0, 0, 0, 0, F(-2), 0, 0]
    obs = [[sum(x * y for x, y in zip(g, vec(act(a, from_vec(unit(i)))))) for i in range(8)] for a in range(4)]
    ok = ok and obs == [[0, -1, 0, 0, -1, 0, 0, 0], [0, 0, -1, 0, 0, 0, 0, 1], [0, 0, 0, -1, 0, 0, -1, 0],
                        [0, 0, 0, 1, 0, 0, -1, 0]]
    # at the stationary vacua of check (5) the gradient vanishes, so the obstruction vanishes
    for (lam, mu, kap, w), v in (((1, 1, -1, F(3, 2)), [F(1)] + [F(0)] * 3 + [F(1)] + [F(0)] * 3),
                                 ((1, 1, 1, 2), [F(1)] + [F(0)] * 3 + [F(0), F(1), F(0), F(0)])):
        g = grad(pot(lam, mu, kap, w), v)
        ok = ok and g == [F(0)] * 8
    GA.check("s0 S2 + s1 S1 = 0 on the potential; s1 S1 != 0 off a stationary point, = 0 on it", ok)
    return ok


# (4) --------------------------------------------------------------------------------------------

def check_goldstone_rank_is_three_exactly_on_aligned_doublets():
    premise("synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta")
    ok = True
    counts = {0: 0, 3: 0, 4: 0}
    other = 0
    for c in product((-1, 0, 1), repeat=8):
        P = (q(c[:4]), q(c[4:]))
        r = rank_at(P)
        N1, N2, K, Kp = invariants(P)
        if r in counts:
            counts[r] += 1
        else:
            other += 1
        zero = all(x == 0 for x in c)
        want = 0 if zero else (3 if Kp == 0 else 4)
        ok = ok and r == want and K + Kp == N1 * N2
    ok = ok and other == 0 and counts == {0: 1, 3: 672, 4: 5888}
    # the neutral vacuum of the stored count: both doublets scalar
    ok = ok and rank_at((q([3, 0, 0, 0]), q([5, 0, 0, 0]))) == 3
    GA.check("Goldstone rank 0, 3, 4: rank 3 exactly when the two doublets are aligned (K' = 0)", ok)
    return ok


# (5) --------------------------------------------------------------------------------------------

def check_one_coupling_sign_decides_the_pattern():
    premise("synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta")
    ok = True
    # kap = -1, w = 3/2: V >= f(N1, N2) = (3/4)(S - 2)^2 + (5/4) D^2 - 3/4 with equality iff K' = 0
    fneg = pot(1, 1, 1, F(3, 2))
    for c in ([1, 2, -1, 3, 0, 1, 1, -2], [F(1, 2), 0, 3, 1, 2, -1, 0, F(1, 3)], [1, 0, 0, 0, 0, 1, 0, 0]):
        P = from_vec([F(x) for x in c])
        N1, N2, K, Kp = invariants(P)
        S, D = N1 + N2, N1 - N2
        bound = F(3, 4) * (S - 2) ** 2 + F(5, 4) * D ** 2 - F(3, 4)
        ok = ok and fneg(P) - bound == Kp and fneg(P) >= F(-3, 4)
    vneg = (q([1, 0, 0, 0]), q([1, 0, 0, 0]))
    ok = ok and fneg(vneg) == F(-3, 4) and rank_at(vneg) == 3
    # a charge-breaking configuration with the same norms lies higher
    cb = (q([1, 0, 0, 0]), q([0, 1, 0, 0]))
    ok = ok and fneg(cb) == F(1, 4) and rank_at(cb) == 4
    # kap = +1, w = 2: V >= 0, zero exactly at N1 = N2 = 1, K = 0
    fpos = pot(1, 1, 1, 2)
    ok = ok and fpos(cb) == 0 and rank_at(cb) == 4
    ok = ok and fpos(vneg) == 1
    for c in ([1, 2, -1, 3, 0, 1, 1, -2], [F(1, 2), 0, 3, 1, 2, -1, 0, F(1, 3)], [0, 0, 1, 0, 1, 0, 0, 0]):
        P = from_vec([F(x) for x in c])
        N1, N2, K, Kp = invariants(P)
        ok = ok and fpos(P) == (N1 + N2 - 2) ** 2 + (N1 - N2) ** 2 + K and fpos(P) >= 0
    # the mass matrices: rank 3 with eigen-count (3 massive) and rank 4 (4 massive); physical mode counts
    for P, r, modes in ((vneg, 3, 27 + 5), (cb, 4, 28 + 4)):
        massive = rank_at(P)
        ok = ok and massive == r and 2 * (12 - massive) + 3 * massive + (8 - massive) == modes
    GA.check("kap = -1: global minima aligned (rank 3, V = -3/4); kap = +1: global minima charge-breaking (rank 4)",
             ok)
    return ok


# (6) --------------------------------------------------------------------------------------------

def check_lift_locus_rank_three_exactly_on_the_boundary():
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-on-the-lift-locus")
    ok = True
    I = BIV[2]

    def emb(z1, z2):
        """(z1, z2), z = (x, y) for x + y e12, to z1 + e31 z2"""
        a = GA.add(GA.sc(z1[0]), GA.scal(z1[1], I))
        b = GA.add(GA.sc(z2[0]), GA.scal(z2[1], I))
        return GA.add(a, GA.mul(BIV[1], b, SQ))

    def cmul(z, w):
        return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

    def conj(z):
        return (z[0], -z[1])

    zs = [((F(1), F(2)), (F(-1), F(1, 2))), ((F(0), F(3)), (F(2), F(-1))), ((F(1, 3), F(0)), (F(0), F(0)))]
    for z in zs:
        for w in zs:
            psi = GA.mul(GA.reverse(emb(*z)), emb(*w), SQ)
            herm = (cmul(conj(z[0]), w[0])[0] + cmul(conj(z[1]), w[1])[0],
                    cmul(conj(z[0]), w[0])[1] + cmul(conj(z[1]), w[1])[1])
            ok = ok and (psi.get(ONE, F(0)), psi.get(E12, F(0))) == herm
        # left e12 / 2 acts as diag(e12, -e12) / 2: T3 = sigma_3 / 2 times the unit
        lhs = GA.mul(I, emb(*z), SQ)
        rhs = emb(cmul((F(0), F(1)), z[0]), cmul((F(0), F(-1)), z[1]))
        ok = ok and GA.eq(lhs, rhs)
    # on L: phi2^dagger phi1 = -H^2, H^2 = 1
    H2 = F(1)
    pts = [(q([2, 0, 0, 0]), q([F(-1, 2), 0, 0, 0]), True), (q([1, 0, 0, 0]), q([-1, 3, 0, 0]), False),
           (q([1, 1, 0, 0]), q([F(-1, 2), F(-1, 2), 0, 0]), True), (q([1, 0, 0, 0]), q([-1, 0, 2, 0]), False),
           (q([0, 1, 1, 0]), q([0, F(-1, 2), F(-1, 2), 3]), False)]
    for p1, p2, boundary in pts:
        psi = GA.mul(GA.reverse(p2), p1, SQ)
        on_L = psi.get(ONE, F(0)) == -H2 and psi.get(E12, F(0)) == 0
        N1, N2, K, Kp = invariants((p1, p2))
        ok = ok and on_L and K == H2 * H2 and N1 * N2 >= H2 * H2
        ok = ok and (N1 * N2 == H2 * H2) == boundary
        ok = ok and rank_at((p1, p2)) == (3 if boundary else 4)
    GA.check("lift locus: Goldstone rank 3 exactly on N1 N2 = H^4 (the charge-preserving boundary), 4 inside, never 0",
             ok)
    return ok


if __name__ == "__main__":
    import sys
    r = [check_generators_form_the_electroweak_algebra_on_two_doublets(), check_potential_is_gauge_invariant(),
         check_free_brst_symmetry_needs_a_stationary_vacuum(), check_goldstone_rank_is_three_exactly_on_aligned_doublets(),
         check_one_coupling_sign_decides_the_pattern(), check_lift_locus_rank_three_exactly_on_the_boundary()]
    sys.exit(0 if all(r) else 1)
