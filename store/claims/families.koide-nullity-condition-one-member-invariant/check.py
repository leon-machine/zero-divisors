"""families.koide-nullity-condition-one-member-invariant: exact checks.

Face space R^3 with the permutation action of S3; u = (1,1,1)/sqrt 3, s = v.u, d = v - s u, so
s^2 = (sum v)^2/3 and |d|^2 = |v|^2 - s^2.
(1) Decomposition: the fixed space of S3 is one-dimensional (span (1,1,1)); the commutant of the
    permutation representation (matrices commuting with all six permutation matrices) is two-dimensional,
    so the representation is singlet + an irreducible doublet, inequivalent.
(2) The S3-invariant symmetric bilinear forms are exactly two-dimensional (kernel of the invariance
    constraints), spanned by the singlet projector J/3 (giving s^2) and the doublet projector 1 - J/3
    (giving |d|^2): q_{alpha,beta} = alpha s^2 - beta |d|^2. For alpha, beta > 0 the signature is (1,2) with the
    democratic direction timelike (q(1,1,1) = 3 alpha > 0); for beta < 0 (alpha > 0) it is Euclidean (3,0).
(3) The chain Q = 2/3 <=> cos^2 theta = 1/2 <=> s^2 = |d|^2 <=> q(v) = 0 for q = s^2 - |d|^2, with
    Q_v = |v|^2/(3 s^2) and cos^2 theta = s^2/|v|^2, on sample vectors (both sides of the condition) and
    exactly at a point of the cone in Z[sqrt 2].
(4) On the lepton vector v_k = sqrt(m_k): q(v) = 2 s^2 - |v|^2 lies in [0.00615, 0.00625) (prints as 0.0062),
    |v|^2 = sum m_k = 1883.09937445 (1883), and q/|v|^2 lies in [2.5, 3.5) x 10^-6 (three parts in 10^6).
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

PERMS = [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0), (2, 0, 1)]
SAMPLE_V = [[F(1), F(2), F(3)], [F(3), F(-1), F(5, 2)], [F(1), F(1), F(1)], [F(7), F(0), F(-2)],
            [F(4), F(1), F(1)]]
AB = [(F(1), F(1)), (F(2), F(5, 3)), (F(1, 2), F(4))]


def pmat(p):
    return [[F(1) if p[i] == j else F(0) for j in range(3)] for i in range(3)]


def basis9():
    out = []
    for a in range(3):
        for b in range(3):
            X = [[F(0)] * 3 for _ in range(3)]
            X[a][b] = F(1)
            out.append(X)
    return out


def check_singlet_doublet_decomposition():
    # fixed vectors: kernel of (P - 1) stacked over the generators
    rows = []
    for p in PERMS:
        P = pmat(p)
        rows += [[P[i][j] - (1 if i == j else 0) for j in range(3)] for i in range(3)]
    fixed = GA.field_kernel(rows)
    ok = len(fixed) == 1 and fixed[0][0] == fixed[0][1] == fixed[0][2] != 0
    # commutant: X with P X = X P for all P
    cols = []
    for X in basis9():
        col = []
        for p in PERMS:
            P = pmat(p)
            D = [[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(GA.mat_mul(P, X), GA.mat_mul(X, P))]
            col += [x for r in D for x in r]
        cols.append(col)
    ok = ok and 9 - GA.rank_of_vectors(cols) == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_singlet_doublet_decomposition"; return _tp_rv


def check_invariant_forms_two_parameter_family():
    rows = []
    sym = []
    for a in range(3):
        for b in range(a, 3):
            X = [[F(0)] * 3 for _ in range(3)]
            X[a][b] = X[b][a] = F(1)
            sym.append(X)
    cols = []
    for X in sym:
        col = []
        for p in PERMS:
            P = pmat(p)
            Pt = [list(r) for r in zip(*P)]
            D = GA.mat_mul(GA.mat_mul(P, X), Pt)
            col += [D[i][j] - X[i][j] for i in range(3) for j in range(3)]
        cols.append(col)
    dim = 6 - GA.rank_of_vectors(cols)
    ok = dim == 2
    Js = [[F(1, 3)] * 3 for _ in range(3)]                      # singlet projector
    Dp = [[(1 if i == j else 0) - F(1, 3) for j in range(3)] for i in range(3)]
    for alpha, beta in AB:
        Q = [[alpha * Js[i][j] - beta * Dp[i][j] for j in range(3)] for i in range(3)]
        for p in PERMS:
            P = pmat(p)
            Pt = [list(r) for r in zip(*P)]
            ok = ok and GA.mat_mul(GA.mat_mul(P, Q), Pt) == Q
        ok = ok and GA.congruence_signature(Q) == (1, 2, 0)
        ok = ok and sum(Q[i][j] for i in range(3) for j in range(3)) == 3 * alpha
        for v in SAMPLE_V:
            qv = sum(v[i] * Q[i][j] * v[j] for i in range(3) for j in range(3))
            s2 = sum(v) ** 2 / 3
            ok = ok and qv == alpha * s2 - beta * (sum(x * x for x in v) - s2)
        Qe = [[alpha * Js[i][j] + beta * Dp[i][j] for j in range(3)] for i in range(3)]
        ok = ok and GA.congruence_signature(Qe) == (3, 0, 0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_invariant_forms_two_parameter_family"; return _tp_rv


def check_nullity_chain():
    ok = True
    for v in SAMPLE_V:
        nv = sum(x * x for x in v)
        s2 = sum(v) ** 2 / 3
        d2 = nv - s2
        Qv = nv / (3 * s2)
        cos2 = s2 / nv
        ok = ok and Qv == 1 / (3 * cos2)
        ok = ok and (Qv == F(2, 3)) == (cos2 == F(1, 2)) == (s2 == d2) == (s2 - d2 == 0)
    w = [R2(2, 2), R2(2, -1), R2(2, -1)]
    tot = w[0] + w[1] + w[2]
    nw = w[0] * w[0] + w[1] * w[1] + w[2] * w[2]
    ok = ok and tot * tot * R2(2) == nw * R2(3)                  # 2 s^2 = |v|^2 exactly, q = 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_nullity_chain"; return _tp_rv


def check_lepton_vector_null_to_three_parts_per_million():
    bs = [sqrt_bounds(m) for m in (ME, MU, MT)]
    S_lo, S_hi = sum(b[0] for b in bs), sum(b[1] for b in bs)
    nv = ME + MU + MT
    q_lo, q_hi = 2 * S_lo * S_lo / 3 - nv, 2 * S_hi * S_hi / 3 - nv
    ok = F(615, 10 ** 5) <= q_lo and q_hi < F(625, 10 ** 5)
    ok = ok and nv == F(188309937445, 10 ** 8)
    ok = ok and F(25, 10 ** 7) <= q_lo / nv and q_hi / nv < F(35, 10 ** 7)
    _tp_rv = (ok); assert _tp_rv is not False, "check_lepton_vector_null_to_three_parts_per_million"; return _tp_rv
