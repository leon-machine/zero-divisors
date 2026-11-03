"""families.rigidity-pairing-sector-one-event: exact checks in Q(zeta), zeta^2 + zeta + 1 = 0.

(1) Every antisymmetric family factor is a cross-product matrix: the channel wedges p q^T - q p^T equal
    [q x p]_x for sample p, q, and the antisymmetric 3 x 3 matrices are exactly the 3-dimensional image
    of a -> [a]_x. For five sample complex a (entries in Q(zeta)): G G^dag = |a|^2 1 - conj(a) a^T,
    G G^dag conj(a) = 0, G G^dag w = |a|^2 w on the two vectors w = a x e_1, a x e_2 (a.w = 0), and
    (w_1, w_2, conj(a)) are independent: spectrum {|a|^2, |a|^2, 0}, identically in a.
(2) Takagi: with xi = tau G (x) eps (eps the unitary 2 x 2 symplectic form), xi xi^dag = tau^2 G G^dag (x) 1,
    of rank 4, annihilated by xi xi^dag - sigma^2 with sigma^2 = tau^2 |a|^2: {sigma x4, 0, 0}.
(3) Channels: f_+ x f_- = (zeta^2 - zeta)(1,1,1) and u' x f_+ = (zeta^2 - zeta) f_+ with |zeta^2 - zeta|^2 = 3;
    the normalised channel vectors a_A, a_B are unit and Hermitian-orthogonal, so |a_A + lambda e^{i chi} a_B|^2
    = 1 + lambda^2 for lambda in {0, 3/4, 4/3, 2} and e^{i chi} in {1, zeta, zeta^2}: r = tau sqrt(1 + lambda^2).
(4) Coherent vector and equal gain: with the Gaussian data of the imported squeezed-vacuum Fact
    (N = s^2 conj(Pi), M = -s c xi_hat), Pi = xi_hat xi_hat^dag = R (x) 1 with R = 1 - conj(n) n^T, and
    <Omega_k> = tr(Theta_k M) = 2 s c n_k exactly at the rational hyperbolic points (s, c) = (3/4, 5/4),
    (12/5, 13/5); the channel vector is a_k = (zeta^2 - zeta)(1 + lambda e^{i chi} zeta^k)/3, i.e.
    v_k is proportional to 1 + lambda e^{i chi} zeta^k, and at lambda = 1 (|a| = sqrt 2) this is the displayed
    universal-point formula -i sqrt(2/3) s c (1 + e^{i chi} zeta^k) since -i/sqrt 3 = (zeta^2 - zeta)/3.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# ---- exact helpers: Q(zeta_3), Z[sqrt 2], integer square roots, rational bounds ----
class CY(object):
    """a + b zeta with zeta^2 = -1 - zeta (zeta = e^{2 pi i/3}), exact."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def _c(o):
        return o if isinstance(o, CY) else CY(o)

    def __add__(s, o):
        o = CY._c(o)
        return CY(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __sub__(s, o):
        o = CY._c(o)
        return CY(s.a - o.a, s.b - o.b)

    def __rsub__(s, o):
        return CY._c(o) - s

    def __neg__(s):
        return CY(-s.a, -s.b)

    def __mul__(s, o):
        o = CY._c(o)
        return CY(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a - s.b * o.b)
    __rmul__ = __mul__

    def conj(s):
        return CY(s.a - s.b, -s.b)

    def __truediv__(s, o):
        o = CY._c(o)
        n = o.nsq()
        if n == 0:
            raise ZeroDivisionError
        return s * o.conj() * CY(1 / n)

    def __bool__(s):
        return s.a != 0 or s.b != 0

    def re(s):
        return s.a - s.b / 2

    def nsq(s):
        """|z|^2 = a^2 - ab + b^2 (rational)."""
        return s.a * s.a - s.a * s.b + s.b * s.b

    def __eq__(s, o):
        o = CY._c(o)
        return s.a == o.a and s.b == o.b

    def __ne__(s, o):
        return not s.__eq__(o)

    def __hash__(s):
        return hash((s.a, s.b))


ZETA = CY(0, 1)
Z2 = ZETA * ZETA
ISQ3 = Z2 - ZETA          # zeta^2 - zeta = -i sqrt(3)


class R2(object):
    """p + q sqrt(2), exact."""
    __slots__ = ("p", "q")

    def __init__(self, p=0, q=0):
        self.p, self.q = F(p), F(q)

    @staticmethod
    def _c(o):
        return o if isinstance(o, R2) else R2(o)

    def __add__(s, o):
        o = R2._c(o)
        return R2(s.p + o.p, s.q + o.q)
    __radd__ = __add__

    def __sub__(s, o):
        o = R2._c(o)
        return R2(s.p - o.p, s.q - o.q)

    def __mul__(s, o):
        o = R2._c(o)
        return R2(s.p * o.p + 2 * s.q * o.q, s.p * o.q + s.q * o.p)
    __rmul__ = __mul__

    def __eq__(s, o):
        o = R2._c(o)
        return s.p == o.p and s.q == o.q

    def __ne__(s, o):
        return not s.__eq__(o)

    def sign(s):
        """Exact sign of p + q sqrt 2."""
        if s.q == 0 or s.p == 0 or (s.p > 0) == (s.q > 0):
            v = s.p if s.q == 0 else (s.q if s.p == 0 else s.p)
            return (v > 0) - (v < 0)
        big_p = s.p * s.p > 2 * s.q * s.q
        lead = s.p if big_p else s.q
        return (lead > 0) - (lead < 0)


def isqrt(n):
    """floor(sqrt(n)) for an integer n >= 0 (Newton)."""
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def sqrt_bounds(m, digits=10):
    """Rationals lo <= sqrt(m) <= hi with hi - lo = 10^-digits / den(m)."""
    m = F(m)
    scale = 10 ** digits
    lo_int = isqrt(m.numerator * m.denominator * scale * scale)
    lo, hi = F(lo_int, m.denominator * scale), F(lo_int + 1, m.denominator * scale)
    assert lo * lo <= m <= hi * hi
    return lo, hi


# PDG 2024 charged-lepton masses (MeV) and the tau uncertainty
ME, MU, MT = F(51099895, 10 ** 8), F(1056583755, 10 ** 7), F(177693, 100)
MT_ERR = F(9, 100)
# ---- end of exact helpers ----
# ---- matrices over Q(zeta) and the Gaussian data of the antisymmetric pairing ----
EPS3 = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
EPS2 = [[CY(0), CY(1)], [CY(-1), CY(0)]]
U_ALL = [CY(1), CY(1), CY(1)]
F_PLUS = [CY(1), ZETA, Z2]
F_MINUS = [CY(1), Z2, ZETA]


def cz(n, m):
    return [[CY(0) for _ in range(m)] for _ in range(n)]


def cmm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), CY(0)) for j in range(p)] for i in range(n)]


def ctr(A):
    return sum((A[i][i] for i in range(len(A))), CY(0))


def cT(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def cconj(A):
    return [[x.conj() for x in row] for row in A]


def cdag(A):
    return cconj(cT(A))


def cscale(c, A):
    return [[x * c for x in row] for row in A]


def cadd(A, B):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def ceq(A, B):
    return (len(A) == len(B) and all(len(ra) == len(rb) for ra, rb in zip(A, B))
            and all(x == y for ra, rb in zip(A, B) for x, y in zip(ra, rb)))


def ceye(n):
    return [[CY(1) if i == j else CY(0) for j in range(n)] for i in range(n)]


def kron(A, B):
    n, m = len(A), len(B)
    out = cz(n * m, n * m)
    for i in range(n):
        for j in range(n):
            for a in range(m):
                for b in range(m):
                    out[m * i + a][m * j + b] = A[i][j] * B[a][b]
    return out


def cross_mat(a):
    return [[CY(0), -a[2], a[1]], [a[2], CY(0), -a[0]], [-a[1], a[0], CY(0)]]


def cross(p, q):
    return [p[1] * q[2] - p[2] * q[1], p[2] * q[0] - p[0] * q[2], p[0] * q[1] - p[1] * q[0]]


def hdot(p, q):
    return sum((x.conj() * y for x, y in zip(p, q)), CY(0))


def theta_ops():
    out = []
    for k in range(3):
        Ek = [[CY(EPS3.get((k, i, j), 0)) for j in range(3)] for i in range(3)]
        out.append(cscale(F(1, 2), kron(Ek, EPS2)))
    return out


A_CH = [x * F(1, 3) for x in cross(F_PLUS, F_MINUS)]      # a_A = (zeta^2 - zeta)(1,1,1)/3
B_CH = [x * F(1, 3) for x in cross(U_ALL, F_PLUS)]        # a_B = (zeta^2 - zeta) f_+/3


def gaussian_data(sv, cv, lam, amod, phase):
    """Channel vector a = a_A + lam phase a_B (|a| = amod rational), unit ray n, xi_hat = (G x eps)/|a|,
    N = s^2 conj(xi_hat xi_hat^dag), M = -s c xi_hat (the squeezed-vacuum data of the imported Fact)."""
    a = [x + y * phase * lam for x, y in zip(A_CH, B_CH)]
    n = [x * (1 / amod) for x in a]
    xi_hat = cscale(1 / amod, kron(cross_mat(a), EPS2))
    Pi = cmm(xi_hat, cdag(xi_hat))
    N = cscale(sv * sv, cconj(Pi))
    M = cscale(-sv * cv, xi_hat)
    return a, n, xi_hat, Pi, N, M
# ---- end of the pairing block ----

AS = [[CY(1), CY(2, 1), CY(0, -1)], [CY(F(1, 2)), CY(3), CY(1, 1)], [CY(0, 2), CY(-1, 1), CY(F(2, 3), 0)],
      [CY(1), CY(1), CY(1)], [CY(1), ZETA, Z2]]
PQ = [([CY(1), CY(0, 1), CY(2)], [CY(-1), CY(3), CY(1, 1)]), ([CY(2), CY(0), CY(1)], [CY(0), CY(1), CY(5)])]
POINTS = [(F(3, 4), F(5, 4)), (F(12, 5), F(13, 5))]
RATIOS = [(F(0), F(1)), (F(3, 4), F(5, 4)), (F(4, 3), F(5, 3))]
TAUS = [F(1), F(2, 3)]
TAKAGI_AS = AS[:3]                    # sample vectors a for the Takagi check


def check_cross_product_factor_and_gram_spectrum():
    ok = True
    for p, q in PQ:
        W = [[p[i] * q[j] - q[i] * p[j] for j in range(3)] for i in range(3)]
        ok = ok and ceq(W, cross_mat(cross(q, p)))
    imgs = [[x for row in cross_mat([CY(1 if k == j else 0) for j in range(3)]) for x in row] for k in range(3)]
    ok = ok and GA.field_rank([[x.a for x in r] + [x.b for x in r] for r in imgs]) == 3
    for a in AS:
        G = cross_mat(a)
        GGd = cmm(G, cdag(G))
        a2 = hdot(a, a)
        want = [[(a2 if i == j else CY(0)) - a[i].conj() * a[j] for j in range(3)] for i in range(3)]
        ok = ok and ceq(GGd, want)
        abar = [x.conj() for x in a]
        ok = ok and all(sum((GGd[i][j] * abar[j] for j in range(3)), CY(0)) == CY(0) for i in range(3))
        ws = [cross(a, [CY(1), CY(0), CY(0)]), cross(a, [CY(0), CY(1), CY(0)])]
        for w in ws:
            ok = ok and sum((a[i] * w[i] for i in range(3)), CY(0)) == CY(0)
            ok = ok and all(sum((GGd[i][j] * w[j] for j in range(3)), CY(0)) == a2 * w[i] for i in range(3))
        rows = [ws[0], ws[1], abar]
        # independence over Q(zeta) = Q(i sqrt 3): determinant nonzero
        det = (rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
               - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
               + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0]))
        ok = ok and det != CY(0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_cross_product_factor_and_gram_spectrum"; return _tp_rv


def check_takagi_fourfold():
    premise("families.imported-squeezed-vacuum-bosonic-pairing")
    ok = ceq(cmm(EPS2, cdag(EPS2)), ceye(len(EPS2)))
    for a in TAKAGI_AS:
        G = cross_mat(a)
        a2 = hdot(a, a)
        for tau in TAUS:
            xi = cscale(tau, kron(G, EPS2))
            X = cmm(xi, cdag(xi))
            ok = ok and ceq(X, kron(cscale(tau * tau, cmm(G, cdag(G))), ceye(2)))
            sig2 = a2 * (tau * tau)
            Y = cadd(X, cscale(-sig2, ceye(len(X))))
            ok = ok and ceq(cmm(X, Y), cz(len(X), len(X)))
            ok = ok and GA.field_rank(X) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_takagi_fourfold"; return _tp_rv


def check_channel_vectors():
    cAB, cB = cross(F_PLUS, F_MINUS), cross(U_ALL, F_PLUS)
    ok = cAB == [ISQ3 * x for x in U_ALL] and cB == [ISQ3 * x for x in F_PLUS]
    ok = ok and ISQ3.conj() * ISQ3 == CY(3)
    ok = ok and hdot(A_CH, B_CH) == CY(0) and hdot(A_CH, A_CH) == CY(1) and hdot(B_CH, B_CH) == CY(1)
    for lam in (F(0), F(3, 4), F(4, 3), F(2)):
        for ph in (CY(1), ZETA, Z2):
            a = [x + y * ph * lam for x, y in zip(A_CH, B_CH)]
            ok = ok and hdot(a, a) == CY(1 + lam * lam)
    _tp_rv = (ok); assert _tp_rv is not False, "check_channel_vectors"; return _tp_rv


def check_coherent_vector_and_universal_point():
    premise("families.imported-squeezed-vacuum-bosonic-pairing")
    TH = theta_ops()
    ok = True
    for sv, cv in POINTS:
        ok = ok and cv * cv - sv * sv == 1
        for lam, amod in RATIOS:
            for ph in (CY(1), ZETA, Z2):
                a, n, xi_hat, Pi, N, M = gaussian_data(sv, cv, lam, amod, ph)
                ok = ok and hdot(a, a) == CY(amod * amod)
                R3 = [[(CY(1) if i == j else CY(0)) - n[i].conj() * n[j] for j in range(3)] for i in range(3)]
                ok = ok and ceq(Pi, kron(R3, ceye(2)))
                om = [ctr(cmm(T, M)) for T in TH]
                ok = ok and all(om[k] == n[k] * (2 * sv * cv) for k in range(3))
                zk = [CY(1), ZETA, Z2]
                ok = ok and all(a[k] == ISQ3 * (CY(1) + ph * zk[k] * lam) * F(1, 3) for k in range(3))
    _tp_rv = (ok); assert _tp_rv is not False, "check_coherent_vector_and_universal_point"; return _tp_rv
