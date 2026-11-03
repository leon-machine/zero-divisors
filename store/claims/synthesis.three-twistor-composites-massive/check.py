"""synthesis.three-twistor-composites-massive: exact checks.

Gaussian rationals (pairs of Fractions) stand for the chart's I6-complex components, as in the
check of synthesis.many-twistor-join. Twistor coordinates Z = (omega^1, omega^2, pi^1, pi^2) on
the basis e1..e4; the frozen point is the bivector I = e1^e2 + lam e3^e4, so that
B^{il} = eps(I ^ Z^i ^ Z^l) = <pi^i pi^l> + lam [omega^i omega^l] (the join's convention).
Checked:
  (a) the contraction identity  iota_{zeta} I = -(B^{23} Z^1 + B^{31} Z^2 + B^{12} Z^3), with
      zeta(x) = eps(Z^1 ^ Z^2 ^ Z^3 ^ x) the composite's dual twistor, for random triples and lam;
  (b) det of the 4x4 matrix of I is lam^2 (Pfaffian lam), so iota I is invertible iff lam != 0;
  (c) the radical vector u = -iota_zeta I is B-orthogonal to every constituent;
  (d) for lam != 0 every independent triple (also inside N = 4, 5 composites) has sum |B|^2 > 0,
      and for lam > 0, m^2 = 2 sum |B|^2 + 2 lam C_N > 0 (the join);
  (e) at lam = 0 the three-planes containing the omega-plane have every B zero and m^2 = 0, and
      iota_zeta n_inf = 0 exactly when zeta kills e1 and e2;
  (f) rank two is attained at lam > 0 (T11's plane e1, e4: B = 0, h = 0).
"""
import GA  # noqa: F401  (house rule; the computation below is in Gaussian rationals)
from fractions import Fraction as F
from tp_premise import premise


class _Rng:
    """Deterministic integer generator (Lehmer); no floats and no random module."""

    def __init__(self, seed):
        self.s = seed % 2147483647 or 1

    def _next(self):
        self.s = (self.s * 48271) % 2147483647
        return self.s

    def randint(self, a, b):
        return a + self._next() % (b - a + 1)


class C:
    """Gaussian rational a + i b."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(s, o):
        o = cc(o); return C(s.re + o.re, s.im + o.im)
    __radd__ = __add__

    def __sub__(s, o):
        o = cc(o); return C(s.re - o.re, s.im - o.im)

    def __neg__(s):
        return C(-s.re, -s.im)

    def __mul__(s, o):
        o = cc(o); return C(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    __rmul__ = __mul__

    def conj(s):
        return C(s.re, -s.im)

    def abs2(s):
        return s.re * s.re + s.im * s.im

    def __eq__(s, o):
        o = cc(o); return s.re == o.re and s.im == o.im


def cc(x):
    return x if isinstance(x, C) else C(x)


def rnd(rng, k=3):
    return C(F(rng.randint(-k, k), rng.randint(1, 3)), F(rng.randint(-k, k), rng.randint(1, 3)))


def det(M):
    if len(M) == 1:
        return M[0][0]
    return sum(((-1) ** c * M[0][c] * det([row[:c] + row[c + 1:] for row in M[1:]])
                for c in range(len(M))), C())


def unit(k):
    return [C(1 if j == k else 0) for j in range(4)]


def vol(a, b, c, d):
    """eps(a ^ b ^ c ^ d) with eps(e1 e2 e3 e4) = 1 (determinant of the four columns)."""
    return det([a, b, c, d])


def I_matrix(lam):
    """I^{ab} for I = e1 ^ e2 + lam e3 ^ e4."""
    M = [[C() for _ in range(4)] for _ in range(4)]
    M[0][1], M[1][0] = C(1), C(-1)
    M[2][3], M[3][2] = C(lam), C(-lam)
    return M


def B(Zi, Zl, lam):
    """B^{il} = eps(I ^ Z^i ^ Z^l) = eps(e1 e2 Zi Zl) + lam eps(e3 e4 Zi Zl)."""
    return vol(unit(0), unit(1), Zi, Zl) + lam * vol(unit(2), unit(3), Zi, Zl)


def br(u, w):
    return u[0] * w[1] - u[1] * w[0]


def herm(Z, W):
    """bar Z . W = conj(pi_Z).omega_W + conj(omega_Z).pi_W."""
    return sum((Z[2 + a].conj() * W[a] + Z[a].conj() * W[2 + a] for a in range(2)), C())


def m2(Zs, lam):
    """The join (synthesis.many-twistor-join (2)): 2 sum |B|^2 + 2 lam C_N."""
    N = len(Zs)
    sB = sum((B(Zs[i], Zs[l], lam).abs2() for i in range(N) for l in range(i + 1, N)), F(0))
    h = [[herm(Zi, Zl) for Zl in Zs] for Zi in Zs]
    tr2 = sum((h[i][l] * h[l][i] for i in range(N) for l in range(N)), C())
    tr1 = sum((h[i][i] for i in range(N)), C())
    cN = tr2 * F(1, 2) - tr1 * tr1 * F(1, 4)
    assert cN.im == 0
    return 2 * sB + 2 * lam * cN.re, sB, h


def contraction(Z1, Z2, Z3, lam):
    """u^b = sum_a zeta_a I^{ab}, zeta_a = eps(Z1 ^ Z2 ^ Z3 ^ e_a)."""
    zeta = [vol(Z1, Z2, Z3, unit(a)) for a in range(4)]
    M = I_matrix(lam)
    return [sum((zeta[a] * M[a][b] for a in range(4)), C()) for b in range(4)], zeta


def _generic_part():
    rng = _Rng(31415926)
    # (b) det I = lam^2: the bivector I_Lambda is nondegenerate exactly when Lambda != 0
    for lam in (F(0), F(1, 6), F(-2, 3), F(5)):
        assert det(I_matrix(lam)) == C(lam * lam)
    # B by the eps route agrees with the bracket formula of the join
    for _ in range(3):
        Z, W = [rnd(rng) for _ in range(4)], [rnd(rng) for _ in range(4)]
        for lam in (F(1, 6), F(-3, 4)):
            assert B(Z, W, lam) == br(Z[2:], W[2:]) + lam * br(Z[:2], W[:2])
    for N in (3, 4, 5):
        for trial in range(3):
            Zs = [[rnd(rng) for _ in range(4)] for _ in range(N)]
            Z1, Z2, Z3 = Zs[0], Zs[1], Zs[2]
            assert not (vol(Z1, Z2, Z3, unit(trial % 4)) == 0 and vol(Z1, Z2, Z3, unit((trial + 1) % 4)) == 0)
            for lam in (F(1, 6), F(1), F(-2, 3), F(0)):
                u, zeta = contraction(Z1, Z2, Z3, lam)
                b23, b31, b12 = B(Z2, Z3, lam), B(Z3, Z1, lam), B(Z1, Z2, lam)
                # (a) the contraction identity
                rhs = [-(b23 * Z1[q] + b31 * Z2[q] + b12 * Z3[q]) for q in range(4)]
                assert u == rhs
                # (c) the radical vector is B-orthogonal to every constituent of the triple
                for Zj in (Z1, Z2, Z3):
                    assert B(u, Zj, lam) == 0
                if lam != 0:
                    # (d) a nonzero face for every independent triple
                    assert b23.abs2() + b31.abs2() + b12.abs2() > 0
                else:
                    # (e) at lam = 0, u vanishes iff zeta kills e1 and e2
                    assert (u == [C()] * 4) == (zeta[0] == 0 and zeta[1] == 0)
            for lam in (F(1, 6), F(3)):
                mm, sB, _ = m2(Zs, lam)
                assert sB > 0 and mm >= 2 * sB and mm > 0
    # (e) lam = 0: three-planes containing the omega-plane, Z^i = (omega^i, c_i pi0)
    for _ in range(3):
        pi0 = [rnd(rng), rnd(rng)]
        Zs = []
        for k in range(3):
            c = rnd(rng)
            Zs.append([rnd(rng), rnd(rng), c * pi0[0], c * pi0[1]])
        mm, sB, _ = m2(Zs, F(0))
        assert sB == 0 and mm == 0
        u, zeta = contraction(Zs[0], Zs[1], Zs[2], F(0))
        assert u == [C()] * 4 and zeta[0] == 0 and zeta[1] == 0
        # the same composite is massive as soon as lam != 0, when it is independent
        if not (zeta[2] == 0 and zeta[3] == 0):
            for lam in (F(1, 6), F(2)):
                mm, sB, _ = m2(Zs, lam)
                assert sB > 0 and mm > 0
    # (f) rank two is attained at lam > 0: Z = a e1 + b e4 (T11's massless plane)
    for lam in (F(1, 6), F(3)):
        Zs = [[C(1), C(), C(), C(1)], [C(2), C(), C(), C(0, 1)], [C(-1), C(), C(), C(2)]]
        mm, sB, h = m2(Zs, lam)
        assert sB == 0 and all(v == 0 for row in h for v in row) and mm == 0
        # these three are dependent: their dual twistor vanishes identically
        assert all(vol(Zs[0], Zs[1], Zs[2], unit(a)) == 0 for a in range(4))
    return True


def _Z(*xs):
    return [cc(x) for x in xs]


def check_three_twistor_composites_massive():
    premise("synthesis.many-twistor-join")
    premise("mass.exact-join")
    premise("mass.de-sitter-scale-frozen-point")
    # worked example, by hand: Z1 = (omega (1,0), pi (0,1)), Z2 = ((0,1),(1,0)), Z3 = ((1,0),(1,0))
    lam = F(1, 6)
    Z1, Z2, Z3 = _Z(1, 0, 0, 1), _Z(0, 1, 1, 0), _Z(1, 0, 1, 0)
    assert B(Z2, Z3, lam) == -lam and B(Z3, Z1, lam) == 1 and B(Z1, Z2, lam) == lam - 1
    u, zeta = contraction(Z1, Z2, Z3, lam)
    assert u == _Z(1, -1, -lam, lam)
    mm, sB, h = m2([Z1, Z2, Z3], lam)
    assert h == [_Z(0, 2, 1), _Z(2, 0, 1), _Z(1, 1, 2)]
    assert sB == F(31, 18) and mm == F(52, 9)
    # Lambda = 0 family W = S_omega + C pi0 with pi0 = (1, 2): massless at lam = 0, massive at lam = 1/6
    Y = [_Z(1, 0, 1, 2), _Z(0, 1, 2, 4), _Z(1, 1, 5, 10)]
    assert m2(Y, F(0))[0] == 0 and m2(Y, F(0))[1] == 0
    assert m2(Y, lam)[1] == 3 * lam * lam and m2(Y, lam)[1] == F(1, 12)
    assert not all(z == 0 for z in contraction(Y[0], Y[1], Y[2], F(0))[1])
    # det I = lam^2
    assert det(I_matrix(F(2, 3))) == C(F(4, 9))
    return _generic_part()
