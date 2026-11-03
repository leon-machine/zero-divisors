"""families.skeleton-rank-one-plus-ordering-shift: exact Wick evaluation in Q(zeta).

Six modes (family i, spinor A); Theta_k = (1/2) E_k (x) eps with (E_k)_ij = eps_kij. Gaussian data of the
rigidity premise and the imported squeezed-vacuum Fact: N = s^2 conj(Pi), M = -s c xi_hat, Pi = R (x) 1,
omega_k = tr(Theta_k M) = 2 s c n_k. At the rational hyperbolic points (s, c) = (3/4, 5/4), (12/5, 13/5)
(c^2 - s^2 = 1, x = s^2), feeding ratios lambda in {0, 3/4, 4/3} (|a| = 1, 5/4, 5/3) and channel phases
e^{i chi} in {1, zeta, zeta^2} (two phases per ratio, each phase used):
(1) the four Wick pieces tr(Th_l Th_k) = delta_kl, tr(Th_k Th_l N^T) + tr(Th_l Th_k N) = s^2 delta_kl
    + s^2 conj(n_k) n_l, 2 tr(Th_k N Th_l N^T) = 2 s^4 conj(n_k) n_l, conj(omega_k) omega_l = 4 s^2 c^2 conj(n_k) n_l,
    and their sum H = c^2 1 + x(5 + 6x) conj(n) n^T (eq. H).
(2) The normal-ordered form (last two pieces) is 2x(2 + 3x) conj(n) n^T: rank one, and it annihilates the
    light plane {w : n^T w = 0} (spanned by n x e_j): the light pair is strictly massless. The ordering term
    (first two pieces) is c^2 1 + x conj(n) n^T and acts on the light plane as c^2.
(3) H conj(n) = (1 + 6x + 6x^2) conj(n), H w = c^2 w on the light plane; the characteristic polynomial of H
    (trace, second invariant, determinant) is the same for every ratio and phase at fixed depth, with trace
    3 + 8x + 6x^2: the spectrum depends on the pairing only through r, and m_e = m_mu identically. The trace and
    heavy-eigenvalue identities hold as rational-function identities in x.
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
    return (len(A) == len(B) and all(len(ra) == len(rb) for ra, rb in zip(A, B)) and all(x == y for ra, rb in zip(A, B) for x, y in zip(ra, rb)))


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

POINTS = [(F(3, 4), F(5, 4)), (F(12, 5), F(13, 5))]
RATIOS = [(F(0), F(1)), (F(3, 4), F(5, 4)), (F(4, 3), F(5, 3))]
PHASES = [CY(1), ZETA, Z2]
TH = theta_ops()


def wick(sv, cv, lam, amod, ph):
    a, n, xi_hat, Pi, N, M = gaussian_data(sv, cv, lam, amod, ph)
    NT = cT(N)
    om = [ctr(cmm(T, M)) for T in TH]
    P = {}
    for k in range(3):
        for l in range(3):
            Tk, Tl = TH[k], TH[l]
            p1 = ctr(cmm(Tl, Tk))
            p2 = ctr(cmm(cmm(Tk, Tl), NT)) + ctr(cmm(cmm(Tl, Tk), N))
            p3 = ctr(cmm(cmm(cmm(Tk, N), Tl), NT)) * 2
            p4 = om[k].conj() * om[l]
            P[(k, l)] = (p1, p2, p3, p4)
    return n, P


def light_plane(n):
    return [cross(n, [CY(1 if i == j else 0) for i in range(3)]) for j in range(2)]


def apply(Mx, w):
    return [sum((Mx[i][j] * w[j] for j in range(3)), CY(0)) for i in range(3)]


def check_wick_pieces_and_closed_form():
    premise("families.imported-squeezed-vacuum-bosonic-pairing")
    premise("families.rigidity-pairing-sector-one-event")
    ok = True
    for sv, cv in POINTS:
        x = sv * sv
        for idx, (lam, amod) in enumerate(RATIOS):
            for ph in (PHASES[idx], PHASES[(idx + 1) % 3]):
                n, P = wick(sv, cv, lam, amod, ph)
                for (k, l), (p1, p2, p3, p4) in P.items():
                    d = CY(1) if k == l else CY(0)
                    nn = n[k].conj() * n[l]
                    ok = ok and p1 == d and p2 == d * x + nn * x
                    ok = ok and p3 == nn * (2 * x * x) and p4 == nn * (4 * x * cv * cv)
                    ok = ok and p1 + p2 + p3 + p4 == d * (cv * cv) + nn * (x * (5 + 6 * x))
    _tp_rv = (ok); assert _tp_rv is not False, "check_wick_pieces_and_closed_form"; return _tp_rv


def check_normal_ordered_rank_one_and_ordering_floor():
    premise("families.imported-squeezed-vacuum-bosonic-pairing")
    premise("families.rigidity-pairing-sector-one-event")
    ok = True
    for sv, cv in POINTS:
        x = sv * sv
        for lam, amod in RATIOS[1:]:
            ph = PHASES[(RATIOS.index((lam, amod))) % 3]
            n, P = wick(sv, cv, lam, amod, ph)
            NO = [[P[(k, l)][2] + P[(k, l)][3] for l in range(3)] for k in range(3)]
            OR = [[P[(k, l)][0] + P[(k, l)][1] for l in range(3)] for k in range(3)]
            nn = [[n[k].conj() * n[l] for l in range(3)] for k in range(3)]
            ok = ok and ceq(NO, cscale(2 * x * (2 + 3 * x), nn)) and GA.field_rank(NO) == 1
            ok = ok and ceq(OR, cadd(cscale(cv * cv, ceye(3)), cscale(x, nn)))
            for w in light_plane(n):
                ok = ok and apply(NO, w) == [CY(0)] * 3
                ok = ok and apply(OR, w) == [wi * (cv * cv) for wi in w]
    _tp_rv = (ok); assert _tp_rv is not False, "check_normal_ordered_rank_one_and_ordering_floor"; return _tp_rv


def check_spectrum_depends_only_on_depth():
    premise("families.rigidity-pairing-sector-one-event")
    ok = True
    for sv, cv in POINTS:
        x = sv * sv
        invs = set()
        for lam, amod in RATIOS:
            a, n, _, _, _, _ = gaussian_data(sv, cv, lam, amod, PHASES[1])
            nn = [[n[k].conj() * n[l] for l in range(3)] for k in range(3)]
            H = cadd(cscale(cv * cv, ceye(3)), cscale(x * (5 + 6 * x), nn))
            nb = [v.conj() for v in n]
            ok = ok and apply(H, nb) == [v * (1 + 6 * x + 6 * x * x) for v in nb]
            ws = light_plane(n)
            ok = ok and all(apply(H, w) == [wi * (cv * cv) for wi in w] for w in ws)
            ok = ok and GA.field_rank([ws[0], ws[1], nb]) == 3
            tr = ctr(H)
            e2 = sum((H[i][i] * H[j][j] - H[i][j] * H[j][i] for i in range(3) for j in range(i + 1, 3)), CY(0))
            det = (H[0][0] * (H[1][1] * H[2][2] - H[1][2] * H[2][1]) - H[0][1] * (H[1][0] * H[2][2] - H[1][2] * H[2][0])
                   + H[0][2] * (H[1][0] * H[2][1] - H[1][1] * H[2][0]))
            ok = ok and tr == CY(3 + 8 * x + 6 * x * x)
            invs.add((tr, e2, det))
        ok = ok and len(invs) == 1
        tr, e2, det = invs.pop()
        c2, h = cv * cv, 1 + 6 * x + 6 * x * x
        ok = ok and e2 == CY(c2 * c2 + 2 * c2 * h) and det == CY(c2 * c2 * h)
    X = GA.RF.var()
    c2 = GA.RF1 + X
    ok = ok and (GA.RF.const(3) * c2 + X * (GA.RF.const(5) + GA.RF.const(6) * X)).eqrf(
        GA.RF.const(3) + GA.RF.const(8) * X + GA.RF.const(6) * X * X)
    ok = ok and (c2 + X * (GA.RF.const(5) + GA.RF.const(6) * X)).eqrf(GA.RF1 + GA.RF.const(6) * X + GA.RF.const(6) * X * X)
    _tp_rv = (ok); assert _tp_rv is not False, "check_spectrum_depends_only_on_depth"; return _tp_rv
