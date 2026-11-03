"""synthesis.rung-field-on-the-lift-locus: exact checks.

The rung summand is built in GA.py as Cl(2,2): generators 0, 1 (square +1) are e+_4, e+_5 and 2, 3
(square -1) are e-_4, e-_5; v_a = (e-_a + e+_a)/2, w_a = (e+_a - e-_a)/2. A complexified vector
c = sum_a alpha_a v_a + beta_a w_a is stored as a pair (x, y) of real coordinate vectors in the
basis (v4, v5, w4, w5), c = x + i y. The quadratic form Q, its complex-bilinear extension and the
Hermitian norm N(c) = c* . c are computed with GA.dot; the slot mixing acts through the
commutators of the products v_a w_b computed with GA.mul. Everything is exact (Fractions and
Gaussian rationals).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = GA.sig(2, 2)
EV = [GA.gen(i) for i in range(4)]
HALF = F(1, 2)
V = [GA.scal(HALF, GA.add(EV[2], EV[0])), GA.scal(HALF, GA.add(EV[3], EV[1]))]
W = [GA.scal(HALF, GA.sub(EV[0], EV[2])), GA.scal(HALF, GA.sub(EV[1], EV[3]))]
BASIS = V + W
Z4 = [[F(0)] * 4 for _ in range(4)]
ZV = [F(0)] * 4


def coords(x):
    """Coordinates of a real vector in (v4, v5, w4, w5): e+_a = v_a + w_a, e-_a = v_a - w_a."""
    c = [F(0)] * 4
    for blade, val in x.items():
        assert len(blade) == 1
        i = blade[0]
        if i < 2:
            c[i] += val
            c[2 + i] += val
        else:
            c[i - 2] += val
            c[i] -= val
    return c


def vec(c):
    return GA.add(*[GA.scal(c[i], BASIS[i]) for i in range(4)])


def bil(x, y):
    return GA.dot(vec(x), vec(y), SQ)


def theta(x):
    """The frame involution: fixes e+_a, negates e-_a; checked against GA below."""
    return [x[2], x[3], x[0], x[1]]


def ad(B):
    cols = [coords(GA.sub(GA.mul(B, x, SQ), GA.mul(x, B, SQ))) for x in BASIS]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


E = {(a, b): ad(GA.mul(V[a], W[b], SQ)) for a in range(2) for b in range(2)}


def lin(A, B, c=1):
    return [[A[i][j] + c * B[i][j] for j in range(4)] for i in range(4)]


def scm(A, c):
    return [[c * A[i][j] for j in range(4)] for i in range(4)]


def mv(A, x):
    return [sum((A[i][j] * x[j] for j in range(4)), F(0)) for i in range(4)]


# operators (R, I) mean the complex matrix R + i I acting on c = x + i y
T1 = (Z4, scm(lin(E[(0, 1)], E[(1, 0)]), HALF))          # (i/2) sigma_1
T2 = (scm(lin(E[(0, 1)], E[(1, 0)], -1), HALF), Z4)      # (i/2) sigma_2
T3 = (Z4, scm(lin(E[(0, 0)], E[(1, 1)], -1), HALF))      # (i/2) sigma_3
TY = (Z4, scm(lin(E[(0, 0)], E[(1, 1)]), HALF))          # hypercharge, +1/2 on v, -1/2 on w
GENS = [T1, T2, T3, TY]
KB = (lin(E[(0, 0)], E[(1, 1)]), Z4)                     # K = -2i Y, the boost generator


def app(op, c):
    (R, I), (x, y) = op, c
    Rx, Ry, Ix, Iy = mv(R, x), mv(R, y), mv(I, x), mv(I, y)
    return ([Rx[i] - Iy[i] for i in range(4)], [Ry[i] + Ix[i] for i in range(4)])


def Qb(c, d):
    """Complex-bilinear Q(c, d) as (re, im)."""
    (x, y), (u, w) = c, d
    return (bil(x, u) - bil(y, w), bil(x, w) + bil(y, u))


def Q(c):
    return Qb(c, c)


def G(c, d):
    """Real part of the Hermitian product c* . d, c* = theta(conj c)."""
    (x, y), (u, w) = c, d
    return bil(theta(x), u) + bil(theta(y), w)


def N(c):
    return G(c, c)


def m(c):
    """Hypercharge moment map: G(c, K c), K = -2i Y."""
    return G(c, app(KB, c))


def flat(c):
    return c[0] + c[1]


def unflat(u):
    return (list(u[:4]), list(u[4:]))


def clam(lam, h):
    """Rung component of the frozen point's lift in the frame lam: -lam w4 + (h/lam) v4."""
    return ([h / lam, F(0), -lam, F(0)], list(ZV))


def dclam(lam, h):
    return ([-h / (lam * lam), F(0), F(-1), F(0)], list(ZV))


def stab_dim(c):
    return 4 - GA.rank_of_vectors([flat(app(T, c)) for T in GENS])


def cmplx(z):
    return GA.qi(z[0], z[1])


def from_complex(al, be):
    """c with complex coefficients alpha (on v4, v5), beta (on w4, w5)."""
    x = [al[0].re, al[1].re, be[0].re, be[1].re]
    y = [al[0].im, al[1].im, be[0].im, be[1].im]
    return (x, y)


def to_complex(c):
    x, y = c
    return [GA.qi(x[i], y[i]) for i in range(4)]


def u2_act(A, c):
    """The group element A in U(2): alpha -> A alpha, beta -> conj(A) beta."""
    z = to_complex(c)
    al, be = z[:2], z[2:]
    Ab = [[A[i][j].conj() for j in range(2)] for i in range(2)]
    na = [A[i][0] * al[0] + A[i][1] * al[1] for i in range(2)]
    nb = [Ab[i][0] * be[0] + Ab[i][1] * be[1] for i in range(2)]
    return from_complex(na, nb)


LAMS = [F(1, 5), F(1, 3), F(1), F(2), F(7)]
LAMBDAS = [F(1), F(3, 2), F(1, 7)]


def check_setting():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    # v, w are a CAR pair per rung; theta is the frame involution; Q(a v + b w) = a b
    for a in range(2):
        for b in range(2):
            ac = GA.add(GA.mul(V[a], W[b], SQ), GA.mul(W[b], V[a], SQ))
            assert GA.eq(ac, GA.sc(F(1) if a == b else F(0)))
    for i in range(4):
        e = coords(EV[i])
        assert theta(e) == [(1 if i < 2 else -1) * u for u in e]
    assert Q(([F(2), F(0), F(3), F(0)], list(ZV))) == (F(6), F(0))
    # the slot generators act by X on v-coefficients and by -X^T on w-coefficients
    for a in range(2):
        for b in range(2):
            want = [[F(0)] * 4 for _ in range(4)]
            want[a][b] = F(1)
            want[2 + b][2 + a] = F(-1)
            assert E[(a, b)] == want
    # hypercharge weights +1/2 on v, -1/2 on w (as i Y on the coordinates)
    assert TY[1] == [[HALF, 0, 0, 0], [0, HALF, 0, 0], [0, 0, -HALF, 0], [0, 0, 0, -HALF]]
    # every generator preserves the complex-bilinear Q and the Hermitian N
    c = ([F(1), F(2), F(-3), F(5)], [F(4), F(-1), F(2), F(1)])
    d = ([F(2), F(-1), F(1), F(3)], [F(0), F(1), F(-2), F(1)])
    for T in GENS:
        a1, a2 = Qb(app(T, c), d), Qb(c, app(T, d))
        assert (a1[0] + a2[0], a1[1] + a2[1]) == (0, 0)
        assert G(app(T, c), c) == 0
    # N(c) = (|alpha|^2 + |beta|^2)/2
    x, y = c
    assert N(c) == HALF * sum((x[i] * x[i] + y[i] * y[i] for i in range(4)), F(0))
    return True


def check_charge_preserving_locus():
    premise("standard-model.transported-frozen-point")
    premise("synthesis.rung-unit-is-frame-boost")
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    for Lam in LAMBDAS:
        h = Lam / 3
        for lam in LAMS:
            c = clam(lam, h)
            assert Q(c) == (-h, 0)
            assert stab_dim(c) == 1
            # the unbroken generator is Y - T3
            ker = GA.field_kernel([[GA.qi(flat(app(T, c))[k]) for T in GENS] for k in range(8)])
            assert len(ker) == 1
            s = [z.re for z in ker[0]]
            assert s[0] == 0 and s[1] == 0 and s[2] == -s[3] and s[3] != 0
        # misaligned points of L: trivial stabiliser
        for al, be in [((F(1), F(1)), (-h, F(0))), ((F(2), F(3)), (F(1), -(h + 2) / 3))]:
            c = ([al[0], al[1], be[0], be[1]], list(ZV))
            assert Q(c) == (-h, 0)
            assert stab_dim(c) == 0
        # aligned points beta = -(h/|alpha|^2) conj(alpha) are U(2)-images of c_lam, lam = h/|alpha|
        for r in [F(1, 2), F(3), F(5, 4)]:
            for (p, q) in [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]:
                u = [GA.qi(p, 0), GA.qi(0, q)]
                al = [r * u[0], r * u[1]]
                be = [GA.qi(-h / r) * u[0].conj(), GA.qi(-h / r) * u[1].conj()]
                c = from_complex(al, be)
                assert Q(c) == (-h, 0)
                assert stab_dim(c) == 1
                A = [[u[0].conj(), u[1].conj()], [-u[1], u[0]]]
                AhA = [[sum((A[k][i].conj() * A[k][j] for k in range(2)), GA.qi(0)) for j in range(2)]
                       for i in range(2)]
                assert AhA == [[GA.qi(1), GA.qi(0)], [GA.qi(0), GA.qi(1)]]
                assert u2_act(A, c) == clam(h / r, h)
                # lam = |beta| is the invariant, and |alpha||beta| = h
                assert N(([F(0)] * 2 + c[0][2:], [F(0)] * 2 + c[1][2:])) == HALF * (h / r) ** 2
    return True


def check_two_readings_of_gauge_masses():
    premise("standard-model.transported-frozen-point")
    premise("synthesis.rung-unit-is-frame-boost")
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    P0 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    g, gp = F(1), F(1, 2)
    cpl = [g, g, g, gp]
    h = F(1, 3)
    seenN = set()
    for lam in LAMS:
        c = clam(lam, h)
        MH = [[G(app(A, c), app(B, c)) for B in GENS] for A in GENS]
        MQ = [[Qb(app(A, c), app(B, c)) for B in GENS] for A in GENS]
        assert MH == [[N(c) / 4 * P0[i][j] for j in range(4)] for i in range(4)]
        assert MQ == [[(Q(c)[0] / 4 * P0[i][j], F(0)) for j in range(4)] for i in range(4)]
        seenN.add(N(c))
        # with couplings: eigenvalues 0, g^2, g^2, g^2 + g'^2 (times N/4): characteristic polynomial
        P = [[cpl[i] * cpl[j] * P0[i][j] for j in range(4)] for i in range(4)]
        for t in [F(0), F(1, 3), F(2), F(-1), F(5, 2)]:
            M = [[P[i][j] - (t if i == j else 0) for j in range(4)] for i in range(4)]
            assert _det(M) == t * (t - g * g) ** 2 * (t - g * g - gp * gp)
    assert len(seenN) == 4          # N depends on lam (lam and h/lam give the same N)
    return True


def _det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    return sum(((-1) ** j * M[0][j] * _det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(n)), F(0))


def check_rung_unit_is_the_neutral_mode():
    premise("synthesis.rung-unit-transverse-to-norm")
    premise("standard-model.transported-frozen-point")
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    for Lam in LAMBDAS:
        h = Lam / 3
        for lam in LAMS:
            c = clam(lam, h)
            unit = [[F(1) if k == j else F(0) for k in range(8)] for j in range(8)]
            rows = [[Qb(c, unflat(e))[part] for e in unit] for part in range(2)]
            orb = [flat(app(T, c)) for T in GENS]
            assert GA.rank_of_vectors(rows) == 2                 # T_c L has real dimension 6
            assert GA.rank_of_vectors(orb) == 3                  # gauge orbit of dimension 3
            rows += [[G(unflat(o), unflat(e)) for e in unit] for o in orb]
            nb = [[z.re for z in v] for v in GA.field_kernel([[GA.qi(x) for x in r] for r in rows])]
            assert len(nb) == 3                                  # physical normal space
            dc = dclam(lam, h)
            assert Qb(c, dc) == (0, 0)
            assert all(G(unflat(o), dc) == 0 for o in orb)
            assert GA.rank_of_vectors(nb + [flat(dc)]) == 3      # dc/dlam lies in it
            S = (Z4, lin(TY[1], T3[1], -1))                      # unbroken Y - T3
            assert app(S, dc) == (list(ZV), list(ZV))            # rung unit neutral
            rows2 = rows + [[G(dc, unflat(e)) for e in unit]]
            ch = [[z.re for z in v] for v in GA.field_kernel([[GA.qi(x) for x in r] for r in rows2])]
            assert len(ch) == 2                                  # the charged plane
            for v in ch:
                sv = app(S, unflat(v))
                assert GA.rank_of_vectors(ch + [flat(sv)]) == 2  # S preserves it
                assert app(S, sv) == scal_vec(-1, unflat(v))     # with charge one
            # kinetic coefficients of eta = log(lam/H): Q(dc/deta) = h, N(dc/deta) = N(c)
            de = (scal_list(lam, dc[0]), scal_list(lam, dc[1]))
            assert Q(de) == (h, 0)
            assert N(de) == N(c)
    return True


def scal_list(s, x):
    return [s * u for u in x]


def scal_vec(s, c):
    return (scal_list(s, c[0]), scal_list(s, c[1]))


def check_rung_unit_is_imaginary_hypercharge():
    premise("synthesis.rung-unit-transverse-to-norm")
    premise("synthesis.rung-unit-is-frame-boost")
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    h = F(1, 3)
    # K = -2i Y: i * (i/2) J = -(1/2) J, so -2i Y has real part J and no imaginary part
    assert KB[0] == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
    assert TY[1] == scm(KB[0], HALF)
    for lam in LAMS:
        c = clam(lam, h)
        for s in [F(1, 3), F(2), F(5, 7)]:
            Bs = ([[s, 0, 0, 0], [0, s, 0, 0], [0, 0, F(1) / s, 0], [0, 0, 0, F(1) / s]], Z4)
            bc = app(Bs, c)
            assert bc == clam(lam / s, h)                        # the boost moves along the family
            assert Q(bc) == Q(c)
            assert N(bc) == HALF * (s * s * (h / lam) ** 2 + (lam / s) ** 2)
            assert m(bc) == HALF * (s * s * (h / lam) ** 2 - (lam / s) ** 2)
        # Kempf-Ness: N(c_lam) - h = (1/2)(lam - h/lam)^2 >= 0, zero iff m = 0 iff lam^2 = h
        assert N(c) - h == HALF * (lam - h / lam) ** 2
        assert m(c) == HALF * ((h / lam) ** 2 - lam * lam)
        assert (m(c) == 0) == (lam * lam == h)
        assert N(c) * N(c) == Q(c)[0] ** 2 + m(c) ** 2
    # strict monotonicity of m along the family
    ms = [m(clam(lam, h)) for lam in sorted(LAMS)]
    assert all(ms[i] > ms[i + 1] for i in range(len(ms) - 1))
    # balanced frame: lam^2 = h with h = 1/4 (rational H = 1/2)
    hb = F(1, 4)
    assert m(clam(F(1, 2), hb)) == 0 and N(clam(F(1, 2), hb)) == hb
    return True


def check_product_law_and_mirror():
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.transported-frozen-point")
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    def star(c):
        return (theta(c[0]), scal_list(-1, theta(c[1])))
    # c* = theta(conj c) on a complex vector, pinned by hand: alpha = (1 + 2i, i), beta = (3, -i)
    cz = from_complex([GA.qi(1, 2), GA.qi(0, 1)], [GA.qi(3), GA.qi(0, -1)])
    assert star(cz) == from_complex([GA.qi(3), GA.qi(0, 1)], [GA.qi(1, -2), GA.qi(0, -1)])
    hs = []
    for Lam in LAMBDAS:
        h = Lam / 3
        hs.append(h)
        for lam in LAMS:
            c = clam(lam, h)
            a, b = c[0][0], c[0][2]                              # c = a v4 + b w4
            assert c == ([h / lam, F(0), -lam, F(0)], [F(0), F(0), F(0), F(0)])
            assert a * b == -h and abs(a) * abs(b) == h          # up x down tree entries
            assert abs(b) / abs(a) == lam * lam / h
            # read through c*: up-type entries from c* = conj(b) v4 + conj(a) w4, down-type from c
            cst = star(c)
            a_up = cst[0][0]
            assert cst[1] == list(ZV) and abs(a_up) == abs(b) == lam
            assert abs(a_up) * abs(b) == lam * lam == N(c) - m(c)
            assert abs(a_up) * abs(b) != h or lam * lam == h       # the product law fails off balance
            assert a_up == -lam and cst[0] == [-lam, F(0), h / lam, F(0)]
            # the conjugation c* = theta(conj c) maps c_lam to -c_{h/lam}
            cs = star(c)
            assert cs == scal_vec(-1, clam(h / lam, h))
            assert Q(cs) == Q(c) and N(cs) == N(c) and m(cs) == -m(c)
    assert hs == [F(1, 3), F(1, 2), F(1, 21)]
    # pinned by hand at Lambda = 1, lam = 2: a = 1/6, b = -2; through c* the up entry is 2
    c2 = clam(F(2), F(1, 3))
    assert c2 == ([F(1, 6), F(0), F(-2), F(0)], list(ZV))
    assert (N(c2), m(c2)) == (F(145, 72), F(-143, 72)) and N(c2) - m(c2) == 4
    # aligned vectors off L (beta = kappa conj(alpha), kappa complex): N^2 = |Q|^2 + m^2
    # pinned by hand: |alpha|^2 = 6, |kappa|^2 = 10 and 17, so |beta|^2 = 60 and 102; Q = kappa |alpha|^2
    pins = [(F(33), (F(18), F(-6)), F(-27)), (F(54), (F(-6), F(24)), F(-48))]
    for (al, kap), pin in zip([((GA.qi(1, 2), GA.qi(0, 1)), GA.qi(3, -1)), ((GA.qi(2), GA.qi(1, -1)), GA.qi(-1, 4))],
                              pins):
        be = [kap * al[0].conj(), kap * al[1].conj()]
        c = from_complex(list(al), be)
        assert (N(c), Q(c), m(c)) == pin
        q = cmplx(Q(c))
        assert N(c) * N(c) == (q * q.conj()).re + m(c) ** 2
        assert stab_dim(c) == 1
    # misaligned: N^2 > |Q|^2 + m^2
    c = from_complex([GA.qi(1), GA.qi(1)], [GA.qi(1), GA.qi(0)])
    assert (N(c), Q(c), m(c)) == (F(3, 2), (F(1), F(0)), F(1, 2))
    q = cmplx(Q(c))
    assert N(c) * N(c) - (q * q.conj()).re - m(c) ** 2 == 1     # = |alpha|^2|beta|^2 - |Q|^2 = 2 - 1
    assert stab_dim(c) == 0
    return True
