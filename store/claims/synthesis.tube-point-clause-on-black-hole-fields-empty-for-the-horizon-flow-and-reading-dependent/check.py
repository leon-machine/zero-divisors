"""synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent: exact checks.

Model: Cl(2,4) with the labels of synthesis.wick-rotated-boost-selects-observer-tube-point: e1 (square +1, time),
e2, e3, e4 (square -1), e+ (+1), e- (-1); nO = (e+ + e-)/2, ninf = e+ - e-, X(x) = nO + x - Q(x) ninf / 2. The chart
boost is K = e1 e2 with bifurcation plane span(e3, e4); T = span(e3, e4, e+, e-) is the transverse space, of
signature (1,3). A compatible tube point is m = x_perp + I7 rho u, u = cosh(eta) e1 + sinh(eta) e2, with
Re X(m) = nO + x_perp + (|x_perp|^2 + rho^2) ninf / 2 and Im X(m) = rho u; its observer is
x(m) = x_perp + rho (sinh(eta) e1 + cosh(eta) e2). Exact rationals throughout (rational boosts by the
half-rapidity parameter s: cosh = (1 + s^2)/(1 - s^2), sinh = 2s/(1 - s^2)).
Checks:
  (i)   the bivectors commuting with K are K and the six bivectors of T;
  (ii)  the stabiliser in them of a vector I of T with Q(I) > 0 is a compact so(3), and the compatible tube points
        it fixes are exactly x_perp = centre, rho^2 = Q(I)/alpha^2; for Q(I) <= 0 none is fixed;
  (iii) a bivector of T fixes a compatible tube point exactly when it fixes the observer;
  (iv)  the static chart of the wedge: the rotations of I move every point with s > 0 and fix those with s = 0;
  (v)   the static lapse: the stored static connection gives the acceleration f'/(2 sqrt f); Schwarzschild has
        f' > 0; the Schwarzschild-de Sitter sample has one stationary radius, r_0^3 = 3M/Lambda, for both
        horizons, f(r_0) < 1 with (1 - f(r_0))^3 = 9 Lambda M^2, and scales in the ratio kappa_b/kappa_c = 8/5;
  (vii) the twisted gauge: the chart boost conjugated by the rapidity-dependent rotation about J is the boost
        times a rotation about J; J fixes exactly the axis points of each rotation sphere and their tube points,
        at every sigma, with scales rho = 2 sqrt(1 - sigma^2)/(1 -+ sigma); the helical generator's norm;
        in the de Sitter field the bivectors commuting with I_Lambda and K + c J are spanned by K and J;
        a K + B with a != 0 and B a bivector of T fixes no compatible tube point (in the check of (ii)).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import GA as g
import gtg
from tp_premise import premise

WICK = "synthesis.wick-rotated-boost-selects-observer-tube-point"
DESITTER = "synthesis.de-sitter-field-fixes-the-observer-tube-point"
SCHW = "pairing.imported-schwarzschild-connection-curvature"
GTGD = "synthesis.imported-gtg-dictionary"

SQ = (1, -1, -1, -1, 1, -1)


def vec(*c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


E = [vec(*[1 if j == i else 0 for j in range(6)]) for i in range(6)]
e1, e2, e3, e4, ep, em = E
NO = g.scal(F(1, 2), g.add(ep, em))
NINF = g.sub(ep, em)
K = g.mul(e1, e2, SQ)
BL = list(combinations(range(6), 2))
BIV = [g.mul(E[i], E[j], SQ) for i, j in BL]
TRANSVERSE = [g.mul(E[i], E[j], SQ) for i, j in combinations((2, 3, 4, 5), 2)]


def mul(a, b):
    return g.mul(a, b, SQ)


def comm(a, b):
    return g.sub(mul(a, b), mul(b, a))


def ip(a, b):
    return g.dot(a, b, SQ)


def lin(coeffs, basis):
    return g.add(*[g.scal(F(c), b) for c, b in zip(coeffs, basis)])


def cv(x):
    return [x.get((i,), F(0)) for i in range(6)]


def bv(x):
    return [x.get(t, F(0)) for t in BL]


def rank(rows):
    return g.mat_rank(g.frac_matrix(rows)) if rows else 0


def tractor(alpha, c3, c4, beta):
    """I = alpha nO + c3 e3 + c4 e4 + beta ninf, a vector of T with Q(I) = 2 alpha beta - c3^2 - c4^2."""
    return lin((alpha, c3, c4, beta), (NO, e3, e4, NINF))


def stabiliser(I):
    """A basis of the bivectors of T annihilating I (rows of the kernel of B -> [B, I])."""
    rows = [cv(comm(B, I)) for B in TRANSVERSE]
    # kernel of the 6 x 6 map c -> sum c_j [B_j, I]: solve by exact elimination on the transpose
    n = len(TRANSVERSE)
    A = [[rows[j][i] for j in range(n)] for i in range(6)]
    piv, r = [], 0
    A = [list(map(F, row)) for row in A]
    for c in range(n):
        p = next((k for k in range(r, len(A)) if A[k][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for k in range(len(A)):
            if k != r and A[k][c] != 0:
                A[k] = [x - A[k][c] * y for x, y in zip(A[k], A[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    out = []
    for fc in free:
        sol = [F(0)] * n
        sol[fc] = F(1)
        for k, pc in enumerate(piv):
            sol[pc] = -A[k][fc]
        out.append(lin(sol, TRANSVERSE))
    return out


def killing_form(basis):
    """Matrix of tr(ad X ad Y) on the Lie algebra spanned by `basis` (closed under the commutator)."""
    n = len(basis)
    rows = [bv(b) for b in basis]

    def coords(x):
        # solve x = sum c_i basis_i exactly (basis independent)
        M = [[rows[j][i] for j in range(n)] + [bv(x)[i]] for i in range(len(BL))]
        M = [r for r in M if any(r)]
        sol = [F(0)] * n
        r = 0
        pivs = []
        for c in range(n):
            p = next((k for k in range(r, len(M)) if M[k][c] != 0), None)
            assert p is not None
            M[r], M[p] = M[p], M[r]
            M[r] = [x / M[r][c] for x in M[r]]
            for k in range(len(M)):
                if k != r and M[k][c] != 0:
                    M[k] = [a - M[k][c] * b for a, b in zip(M[k], M[r])]
            pivs.append(c)
            r += 1
        assert all(not any(row[:n]) and row[n] == 0 for row in M[r:])     # x lies in the span
        for k, c in enumerate(pivs):
            sol[c] = M[k][n]
        return sol
    ad = [[coords(g.scal(F(1, 2), comm(basis[i], basis[j]))) for j in range(n)] for i in range(n)]
    # ad[i][j] = coordinates of [b_i, b_j]/2 (the bivector commutator product)
    kf = [[sum(ad[i][k][l] * ad[j][l][k] for k in range(n) for l in range(n)) for j in range(n)] for i in range(n)]
    return kf


def negative_definite(m):
    """Leading principal minors alternate in sign, starting negative (3 x 3)."""
    d1 = m[0][0]
    d2 = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    d3 = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
          + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    return d1 < 0 and d2 > 0 and d3 < 0


def boost_pair(s):
    s = F(s)
    ch = (1 + s * s) / (1 - s * s)
    sh = 2 * s / (1 - s * s)
    return lin((ch, sh), (e1, e2)), lin((sh, ch), (e1, e2))


def tube_parts(x3, x4, rho, s):
    u, w = boost_pair(s)
    rho = F(rho)
    xp = vec(0, 0, x3, x4, 0, 0)
    re = g.add(NO, xp, g.scal((F(x3) ** 2 + F(x4) ** 2 + rho * rho) / 2, NINF))
    im = g.scal(rho, u)
    obs = g.add(xp, g.scal(rho, w))
    return re, im, obs


def X_of(x):
    return g.add(NO, x, g.scal(-ip(x, x) / 2, NINF))


def fixes_tube(B, re, im):
    """B (real, in the centraliser of K) fixes the complex null line of X = re + I7 im: [B, X] = c X with c
    complex. For B in T the commutator [B, im] vanishes and [B, re] lies in T, so the condition is [B, re] = 0;
    the general test is kept: both parts of [B, X] in the complex span of X."""
    dre, dim_ = comm(B, re), comm(B, im)
    if g.is_zero(dre) and g.is_zero(dim_):
        return True
    # c = a + I7 b with [B, re] = a re - b im and [B, im] = a im + b re
    basis = [cv(re), cv(im)]
    if rank(basis + [cv(dre)]) > 2 or rank(basis + [cv(dim_)]) > 2:
        return False

    def coords(x):
        rows = [(cv(re)[i], cv(im)[i], cv(x)[i]) for i in range(6)]
        for i in range(6):
            for j in range(i + 1, 6):
                det = rows[i][0] * rows[j][1] - rows[i][1] * rows[j][0]
                if det != 0:
                    return ((rows[i][2] * rows[j][1] - rows[i][1] * rows[j][2]) / det,
                            (rows[i][0] * rows[j][2] - rows[i][2] * rows[j][0]) / det)
        raise ArithmeticError("re and im are dependent")
    a1, b1 = coords(dre)
    a2, b2 = coords(dim_)
    return a1 == b2 and b1 == -a2


TRACTORS = [(F(1, 2), 0, 0, 1), (2, 0, 0, 1), (1, 1, 0, 1), (F(2, 3), F(1, 2), F(-1, 3), 3), (2, 1, -1, F(3, 2)),
            (F(1, 4), 0, 0, F(1, 2))]                       # (alpha, c3, c4, beta), all with Q(I) > 0
NOT_TIMELIKE = [(0, 0, 0, 1), (1, 1, 0, F(1, 2)), (1, 0, 0, -1), (0, 1, 0, 0), (1, 2, 1, 1)]   # Q(I) <= 0
FEET = [(0, 0), (1, 0), (F(1, 2), F(-1, 3)), (F(3, 4), F(-1, 2)), (F(1, 2), F(1, 2)), (2, 0)]
RHOS = [F(1, 3), F(1, 2), F(1), F(3, 2), F(2), F(3), F(4)]
BOOSTS = [0, F(1, 3), F(-1, 2)]
MIXES = [(1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (1, -2, 3, 1, 0, 2), (0, 1, 1, -1, 2, 5), (3, 1, 0, 0, -1, 1)]


def qI(t):
    a, c3, c4, b = map(F, t)
    return 2 * a * b - c3 * c3 - c4 * c4


def check_centraliser_of_the_boost_is_the_boost_and_the_transverse_bivectors():
    """(i): {B : [B, K] = 0} has dimension 7 and is spanned by K and the six bivectors of T."""
    premise(WICK)
    rows = [bv(comm(B, K)) for B in BIV]
    assert len(BIV) - rank(rows) == 7
    assert all(g.is_zero(comm(B, K)) for B in TRANSVERSE + [K])
    assert rank([bv(B) for B in TRANSVERSE + [K]]) == 7
    assert sum(1 for B in BIV if not g.is_zero(comm(B, K))) == 8        # the eight mixed bivectors do not commute
    assert ip(NO, NINF) == 1 and ip(NO, NO) == 0 and ip(NINF, NINF) == 0


def check_stabiliser_of_a_timelike_vector_is_a_compact_so3_with_one_fixed_boost_orbit():
    """(ii): for Q(I) > 0 the stabiliser is three-dimensional with negative definite Killing form, and the
    compatible tube points it fixes are exactly x_perp = (c3, c4)/alpha, rho^2 = Q(I)/alpha^2."""
    premise(WICK)
    premise(DESITTER)
    hits = 0
    for t in TRACTORS:
        a, c3, c4, b = map(F, t)
        assert qI(t) > 0 and a != 0
        I = tractor(*t)
        assert ip(I, I) == qI(t)
        st = stabiliser(I)
        assert len(st) == 3 and all(g.is_zero(comm(B, I)) and g.is_zero(comm(B, K)) for B in st)
        assert negative_definite(killing_form(st))
        foot = (c3 / a, c4 / a)
        rho2 = qI(t) / (a * a)
        for (x3, x4) in sorted(set((F(p), F(q)) for p, q in FEET) | {foot}):
            for rho in RHOS:
                for s in BOOSTS:
                    re, im, _ = tube_parts(x3, x4, rho, s)
                    fixed = all(fixes_tube(B, re, im) for B in st)
                    want = (F(x3), F(x4)) == foot and rho * rho == rho2
                    assert fixed == want
                    hits += fixed
    # the de Sitter tractor of the stored theorem is the case alpha = Lambda/6, beta = 1: rho^2 = 12/Lambda
    for lam in (12, 3, 48, F(4, 3)):
        assert qI((F(lam) / 6, 0, 0, 1)) / (F(lam) / 6) ** 2 == F(12) / lam
    assert hits == 15         # five of the six samples have rho in RHOS (2, 1, 1, 1, 2); three rapidities each
    for t in NOT_TIMELIKE:
        assert qI(t) <= 0
        I = tractor(*t)
        st = stabiliser(I)
        assert len(st) == 3 and not negative_definite(killing_form(st))
        for (x3, x4) in FEET:
            for rho in RHOS:
                re, im, _ = tube_parts(x3, x4, rho, F(1, 3))
                assert not all(fixes_tube(B, re, im) for B in st)


QUARTER_TRACTOR = (F(1, 2), 0, 0, 1)
BOOST_PARTS = (F(1), F(-1, 3), F(5))               # the coefficients a of K in a K + B


def check_tube_point_is_fixed_exactly_when_its_observer_is():
    """(ii): for B in the bivectors of T, [B, X(m)] = [B, Re X(m)] = [B, X(x(m))], because X(x(m)) is Re X(m)
    plus rho w with w in span(e1, e2); so B fixes m iff it fixes x(m)."""
    premise(WICK)
    gens = [lin(c, TRANSVERSE) for c in MIXES] + stabiliser(tractor(*QUARTER_TRACTOR))
    seen_fixed = seen_moved = 0
    for (x3, x4) in FEET:
        for rho in RHOS:
            for s in BOOSTS:
                re, im, obs = tube_parts(x3, x4, rho, s)
                Xo = X_of(obs)
                assert g.is_zero(g.sub(Xo, g.add(re, g.scal(rho, boost_pair(s)[1]))))
                for B in gens:
                    assert g.is_zero(comm(B, im))
                    assert g.is_zero(g.sub(comm(B, Xo), comm(B, re)))
                    a = fixes_tube(B, re, im)
                    b = g.is_zero(comm(B, Xo))
                    assert a == b
                    seen_fixed += a
                    seen_moved += (not a)
                assert not fixes_tube(K, re, im)             # the boost moves every compatible tube point
                turn = g.scal(F(1, 2), comm(im, re))         # im ^ re: [turn, X] = -+ I7 rho^2 X, a complex multiple
                assert fixes_tube(turn, re, im) and not g.is_zero(comm(turn, re))
                for B in gens:                               # a K + B, a != 0, fixes no compatible tube point
                    assert not any(fixes_tube(g.add(g.scal(a, K), B), re, im) for a in BOOST_PARTS)
    assert (seen_fixed, seen_moved) == (51, 957)


SPHERE = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (F(3, 5), F(4, 5), 0), (F(2, 3), F(-1, 3), F(2, 3)),
          (F(2, 7), F(3, 7), F(6, 7))]
RADII = [(0, 1), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(4, 5), F(3, 5))]      # (s, sqrt(1 - s^2)), ell = 1


def check_static_chart_of_the_wedge_and_the_fixed_points_of_its_rotations():
    """(iv), Lambda = 3 (ell = 1): X = I + sqrt(1 - s^2)(sinh e1 + cosh e2) + s n, n a unit vector of
    span(e3, e4, W), is null and lies over the right wedge; K moves it along tau and the rotations of I move it
    exactly when s > 0; s = 0 is the hyperbola Q(x) = -12/Lambda (s is the statement's sigma)."""
    premise(DESITTER)
    I = tractor(F(1, 2), 0, 0, 1)
    W = lin((F(-1, 2), 1), (NO, NINF))
    assert ip(I, I) == 1 and ip(W, W) == -1 and ip(I, W) == 0
    rot = stabiliser(I)
    assert len(rot) == 3
    moved = fixed = 0
    for (s, c) in RADII:
        assert s * s + c * c == 1
        for hs in BOOSTS:
            u, w = boost_pair(hs)
            for (n3, n4, nw) in SPHERE:
                assert F(n3) ** 2 + F(n4) ** 2 + F(nw) ** 2 == 1
                n = lin((n3, n4, nw), (e3, e4, W))
                X = g.add(I, g.scal(c, w), g.scal(s, n))
                assert ip(X, X) == 0
                lam = ip(X, NINF)                        # coefficient of nO
                assert lam > 0
                x = [v / lam for v in cv(X)[:4]]
                assert x[1] > abs(x[0])                  # the right wedge: x2 > |x1|
                assert g.is_zero(g.sub(g.scal(F(1, 2), comm(K, X)), g.scal(-c, u)))   # K . X = -dX/d(eta)
                is_fixed = all(g.is_zero(comm(B, X)) for B in rot)
                assert is_fixed == (s == 0)
                moved += (not is_fixed)
                fixed += is_fixed
                if s == 0:
                    q = x[0] * x[0] - x[1] * x[1] - x[2] * x[2] - x[3] * x[3]
                    assert q == -4 and x[2] == 0 and x[3] == 0             # Q(x) = -12/Lambda, foot at the centre
    assert moved == 54 and fixed == 18


SDS_HORIZONS = (F(1), F(2))                  # r_b, r_c
SDS_LAMBDA, SDS_MASS = F(3, 7), F(3, 7)
SDS_KAPPAS = (F(2, 7), F(5, 28))             # kappa_b, kappa_c
BRACKET = (F(36, 25), F(13, 9))              # r_0 = 3^(1/3) lies strictly between
SDS_F0_BOUNDS = (F(3, 28), F(10, 91))        # 1 - 3M/r at the bracket's ends
SDS_ONE_MINUS_F0_CUBED = F(243, 343)
ACC_POINTS = [(F(3), F(1, 2), F(1, 10)), (F(5), F(2, 3), F(1, 50)), (F(2), F(1, 3), F(1, 5))]   # r0, sqrt f, Lambda
ANGLE = (F(3, 5), F(4, 5))
SCHW_MASSES = (F(1), F(3, 7), F(5, 2))
SCHW_RADII = (F(21, 10), F(3), F(10), F(1000))        # in units of M


def check_static_lapse_candidates_on_schwarzschild_and_schwarzschild_de_sitter():
    """(v) and (vi): the stored static field with lapse f is torsion-free with Ricci map Lambda, and its static
    observer's acceleration has magnitude f'/(2 sqrt f); on Schwarzschild f' > 0 and f < 1; on the
    Schwarzschild-de Sitter sample one stationary radius serves both horizons."""
    premise(SCHW)
    premise(DESITTER)
    premise(GTGD)
    for (r0, w, lam) in ACC_POINTS:
        M = gtg.mass_for_root(r0, w, lam)
        f = gtg.f_static(M, lam)
        fld = gtg.static_field(r0, ANGLE[0], ANGLE[1], f)
        assert fld.torsion_free()
        for i in range(4):
            ric = gtg.ricci(fld.curvature(), GA.gen(i))
            assert {k: gtg._val(v) for k, v in ric.items() if gtg._val(v)} == {(i,): lam}     # calR(a) = Lambda a
        acc = gtg.bdot(fld.om[0], gtg.e(0))          # (v . D) v = Omega(hb(gamma_0)) . gamma_0 for v = gamma_0
        got = {k: gtg._val(v) for k, v in acc.items() if gtg._val(v)}
        fp = 2 * M / (r0 * r0) - 2 * lam * r0 / 3
        assert set(got) == {(1,)} and got[(1,)] ** 2 == fp * fp / (4 * w * w)
    # Schwarzschild: f < 1 and r^2 f' = 2M > 0 at every radius, so sqrt(f)/kappa < 1/kappa = 4M, not attained
    for M in SCHW_MASSES:
        kappa = 1 / (4 * M)
        assert 1 / (kappa * kappa) == 16 * M * M
        for x in SCHW_RADII:
            r = x * M
            f = 1 - 2 * M / r
            assert 0 < f and M / r > 0 and f / (kappa * kappa) < 1 / (kappa * kappa)
            assert (1 - f) * r * r == 2 * M * r      # f' = (1 - f)/r = 2M/r^2
    # Schwarzschild-de Sitter, the stored sample
    rb, rc = SDS_HORIZONS
    lam, M = SDS_LAMBDA, SDS_MASS

    def f(r):
        return 1 - 2 * M / r - lam * r * r / 3

    def r2fp(r):
        return 2 * M - 2 * lam * r ** 3 / 3          # r^2 f'(r), strictly decreasing in r

    assert f(rb) == 0 and f(rc) == 0
    kb = r2fp(rb) / (2 * rb * rb)
    kc = -r2fp(rc) / (2 * rc * rc)
    assert (kb, kc) == SDS_KAPPAS and kb / kc == F(8, 5)
    lo, hi = BRACKET
    assert rb < lo < hi < rc and r2fp(lo) > 0 > r2fp(hi)
    r0_cubed = 3 * M / lam                           # the zero of r^2 f'
    assert lo ** 3 < r0_cubed < hi ** 3 and r0_cubed == 3
    # at r_0: f = 1 - 3M/r_0, so (1 - f(r_0))^3 = 27 M^3 / r_0^3 = 9 Lambda M^2 (below one: two distinct horizons)
    omf = 27 * M ** 3 / r0_cubed
    assert omf == 9 * lam * M * M == SDS_ONE_MINUS_F0_CUBED
    f_lo, f_hi = 1 - 3 * M / lo, 1 - 3 * M / hi
    assert (f_lo, f_hi) == SDS_F0_BOUNDS and (1 - f_lo) ** 3 > omf > (1 - f_hi) ** 3
    assert all(0 < x < F(1, 9) for x in SDS_F0_BOUNDS)        # 0 < f(r_0) < 1: neither normalised norm is one


TWIST_ROTATIONS = ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)))      # (cos, sin) of R_J(-c eta) and of R_J(-c tau)
TWIST_BOOST = F(1, 4)                                              # half-rapidity parameter of the boost by tau
POS = (3, 12, F(4, 3))                                             # values of Lambda for the de Sitter centraliser
TWIST_RATES = (F(1), F(3, 7), F(-2))                               # values of c
HELICAL = [(F(1), F(1), F(3), F(1, 3), F(3, 5)), (F(1, 4), F(2), F(21, 10), F(1, 21), F(5, 13))]   # a, c, r, f, sin


def boost_vector(X, hs):
    """The chart boost of half-rapidity parameter hs applied to a vector."""
    ch = (1 + hs * hs) / (1 - hs * hs)
    sh = 2 * hs / (1 - hs * hs)
    v = cv(X)
    v[0], v[1] = ch * v[0] + sh * v[1], sh * v[0] + ch * v[1]
    return vec(*v)


def rotate_about_w(X, cs, sn):
    """The rotation of the (e3, e4) plane, R_J for J = e3 e4, by the angle with cosine cs and sine sn."""
    v = cv(X)
    v[2], v[3] = cs * v[2] - sn * v[3], sn * v[2] + cs * v[3]
    return vec(*v)


def check_twisted_gauge_selects_the_observers_on_the_rotation_axis():
    """(vii), Lambda = 3, J = e3 e4 with axis +-W: psi^{-1} B_tau psi is the boost times a rotation about J;
    J commutes with K and I; it fixes X(eta, sigma, n) exactly when sigma = 0 or n = +-W, and the compatible
    tube points of the axis observers, whose foot is the centre and whose scale is 2 sqrt(1 - sigma^2)/(1 -+ sigma);
    the full so(3) fixes none of them; the helical generator is spacelike near the horizon off the axis."""
    premise(WICK)
    premise(DESITTER)
    premise(SCHW)
    I = tractor(*QUARTER_TRACTOR)
    W = lin((F(-1, 2), 1), (NO, NINF))
    J = mul(e3, e4)
    rot = stabiliser(I)
    assert g.is_zero(comm(J, I)) and g.is_zero(comm(J, K)) and g.is_zero(comm(J, W))
    assert rank([bv(B) for B in rot] + [bv(J)]) == 3                 # J lies in so(3)_I
    (c1, s1), (c2, s2) = TWIST_ROTATIONS
    assert c1 * c1 + s1 * s1 == 1 and c2 * c2 + s2 * s2 == 1
    c12, s12 = c1 * c2 - s1 * s2, c1 * s2 + s1 * c2                  # the rotation at eta + tau
    conj = on_axis = off_axis = 0
    scales = set()
    for (s, c) in RADII:
        for hs in BOOSTS:
            u, w = boost_pair(hs)
            for (n3, n4, nw) in SPHERE:
                X = g.add(I, g.scal(c, w), g.scal(s, lin((n3, n4, nw), (e3, e4, W))))
                # psi at eta rotates by R1, the boost acts, psi^{-1} at eta + tau rotates back by R1 R2
                left = rotate_about_w(boost_vector(rotate_about_w(X, c1, s1), TWIST_BOOST), c12, -s12)
                right = rotate_about_w(boost_vector(X, TWIST_BOOST), c2, -s2)
                assert g.is_zero(g.sub(left, right)) and ip(left, left) == 0
                conj += 1
                fixed_by_j = g.is_zero(comm(J, X))
                assert fixed_by_j == (s == 0 or (n3 == 0 and n4 == 0))
                on_axis += (fixed_by_j and s != 0)
                off_axis += (not fixed_by_j)
            if s == 0:
                continue
            for sign in (1, -1):
                X = g.add(I, g.scal(c, w), g.scal(sign * s, W))
                assert ip(X, X) == 0 and g.is_zero(comm(J, X)) and not all(g.is_zero(comm(B, X)) for B in rot)
                rho = 2 * c / (1 - sign * s)
                re, im, obs = tube_parts(0, 0, rho, hs)
                assert g.is_zero(g.sub(g.scal(1 / ip(X, NINF), X), X_of(obs)))      # the observer of that tube point
                assert fixes_tube(J, re, im) and not all(fixes_tube(B, re, im) for B in rot)
                scales.add(rho)
    assert (conj, on_axis, off_axis) == (72, 9, 45)
    assert sorted(scales) == [F(2, 3), F(1), F(4, 3), F(3), F(4), F(6)]
    # de Sitter: among the ten bivectors commuting with I_Lambda, those commuting with K + c J are K and J only
    for lam in POS:
        I_lam = tractor(F(lam) / 6, 0, 0, 1)
        assert len(BIV) - rank([cv(comm(B, I_lam)) for B in BIV]) == 10
        for c in TWIST_RATES:
            KJ = g.add(K, g.scal(c, J))
            assert g.is_zero(comm(KJ, I_lam))
            assert len(BIV) - rank([cv(comm(B, I_lam)) + bv(comm(B, KJ)) for B in BIV]) == 2
    # the symmetry K generates in the twisted gauge, a d_t + c d_phi, has squared norm a^2 f - c^2 r^2 sin^2
    for (a, c, r, f, sn) in HELICAL:
        assert f == 1 - 2 / r and 0 < f and a * a * f - c * c * r * r * sn * sn < 0      # M = 1
