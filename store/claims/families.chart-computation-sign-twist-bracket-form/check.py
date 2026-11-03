"""families.chart-computation-sign-twist-bracket-form: exact checks.

Cyclotomic arithmetic: Q(zeta), zeta^2 + zeta + 1 = 0 (class CY); Gaussian rationals for the spinor
arrays; rational interval arithmetic on the PDG 2024 lepton masses; sin/cos by alternating-series bounds.
(1) Sign twist: for two 3 x 2 arrays W (rows: the three omega-spinors), relabelling the rows by any of the
    six permutations pi gives Omega'_k = sgn(pi) Omega_{pi(k)} (Omega_k the minor of rows k+1, k+2): the
    twisted permutation representation. Its character sgn(pi) fix(pi) has multiplicities 0 (trivial),
    1 (sign) and 1 (two-dimensional): 3 x sgn = sgn + 2. The democratic vector spans the sign summand.
(2) Bracket form: C(Omega) = sum Omega_k^2 equals det(W^T W) (Cauchy-Binet) on the arrays, is invariant
    under the twisted action, and on real v equals s^2 + |d|^2 = |v|^2 (the member alpha = 1, beta = -1).
    The S3-invariant symmetric tensors are two-dimensional (delta and J). C(v_lepton) = sum m_k =
    1883.09937445 MeV, not zero. On the doublet: C(f_+-) = 0, C(f_+, f_-) = 3, C(a f_+ + b f_-) = 6ab on a
    grid of (a, b), so the null vectors are exactly the two Fourier lines; Gamma f_+ is real only for Gamma = 0.
(3) Fourier coordinates: Gamma -> (Re(Gamma zeta^k))_k is R-linear of rank 2 into the plane sum d_k = 0;
    sum_k Re(Gamma zeta^k)^2 = (3/2)|Gamma|^2, so Q = 1/3 + |Gamma|^2/(6 a^2) and Q = 2/3 iff |Gamma|^2 = 2a^2.
    tan delta = Im Gamma / Re Gamma satisfies 3 (v_2 - v_1)^2 (Re Gamma)^2 = (Im Gamma)^2 (2 v_0 - v_1 - v_2)^2.
    Lepton data (k = 0, 1, 2 = tau, e, mu): |Gamma|^2/a^2 = 6Q - 2 lies inside 2 +- 10^-4, |Gamma|/a lies in
    [1.41415, 1.41425) (prints as 1.4142, as does sqrt 2); 2 v_0 - v_1 - v_2 = 3 Re Gamma and v_2 - v_1 has the
    sign of Im Gamma (checked at the samples), and for the leptons 2 v_0 > v_1 + v_2 and v_2 > v_1, so delta lies
    in (0, pi/2), where tan increases; tan^2 delta lies between tan^2(0.2215) and tan^2(0.2225), so
    delta = 0.222.
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

QI = GA.QI
ARRAYS = [[[QI(1), QI(2, 1)], [QI(0, 1), QI(3)], [QI(2), QI(-1, 2)]],
          [[QI(F(1, 2)), QI(0, -1)], [QI(4, 1), QI(-2)], [QI(1, 1), QI(F(5, 3))]]]
PERMS = [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0), (2, 0, 1)]
GAMMAS = [CY(1), CY(0, 1), CY(2, -3), CY(F(1, 2), F(5, 7))]
AVALS = [F(3), F(-1, 2)]
REAL_V = [[F(1), F(2), F(3)], [F(3), F(-1), F(5, 2)], [F(7), F(0), F(-2)]]
F_PLUS = [CY(1), ZETA, Z2]
F_MINUS = [CY(1), Z2, ZETA]


def sgn(p):
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return -1 if inv % 2 else 1


def face_vec(arr):
    def minor(i, j):
        return arr[i][0] * arr[j][1] - arr[i][1] * arr[j][0]
    return [minor(1, 2), minor(2, 0), minor(0, 1)]


def cform(v, w=None):
    w = v if w is None else w
    tot = CY(0)
    for x, y in zip(v, w):
        tot = tot + x * y
    return tot


def sin_cos_bounds(x, terms=8):
    sp, cp = [], []
    s, term = F(0), x
    for k in range(terms):
        s += term
        sp.append(s)
        term = -term * x * x / ((2 * k + 2) * (2 * k + 3))
    c, term = F(0), F(1)
    for k in range(terms):
        c += term
        cp.append(c)
        term = -term * x * x / ((2 * k + 1) * (2 * k + 2))
    return (min(sp[-2:]), max(sp[-2:])), (min(cp[-2:]), max(cp[-2:]))


def check_sign_twist():
    ok = True
    for arr in ARRAYS:
        Om = face_vec(arr)
        for p in PERMS:
            Om2 = face_vec([arr[p[i]] for i in range(3)])
            ok = ok and all(Om2[k] == QI(sgn(p)) * Om[p[k]] for k in range(3))
    # character of the twisted representation and its multiplicities (order 6)
    chi = [sgn(p) * sum(1 for i in range(3) if p[i] == i) for p in PERMS]
    triv = [1] * 6
    sign = [sgn(p) for p in PERMS]
    std = [sum(1 for i in range(3) if p[i] == i) - 1 for p in PERMS]
    mult = [F(sum(a * b for a, b in zip(chi, rep)), 6) for rep in (triv, sign, std)]
    ok = ok and mult == [0, 1, 1]
    # the democratic vector transforms by the sign: T_pi (1,1,1) = sgn(pi) (1,1,1)
    for p in PERMS:
        ones = [F(1)] * 3
        ok = ok and [sgn(p) * ones[p[k]] for k in range(3)] == [sgn(p)] * 3
    _tp_rv = (ok); assert _tp_rv is not False, "check_sign_twist"; return _tp_rv


def check_bracket_form():
    ok = True
    for arr in ARRAYS:
        Om = face_vec(arr)
        C = sum((x * x for x in Om), QI(0))
        WtW = [[sum((arr[k][i] * arr[k][j] for k in range(3)), QI(0)) for j in range(2)] for i in range(2)]
        ok = ok and C == WtW[0][0] * WtW[1][1] - WtW[0][1] * WtW[1][0]
        for p in PERMS:
            Om2 = face_vec([arr[p[i]] for i in range(3)])
            ok = ok and sum((x * x for x in Om2), QI(0)) == C
    for v in REAL_V:
        s2 = sum(v) ** 2 / 3
        nv = sum(x * x for x in v)
        d = [x - sum(v) / 3 for x in v]
        ok = ok and s2 + sum(x * x for x in d) == nv and sum(d) == 0
    # invariant symmetric tensors: delta and J, exactly two-dimensional
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
            col += [X[p[i]][p[j]] - X[i][j] for i in range(3) for j in range(3)]
        cols.append(col)
    ok = ok and 6 - GA.rank_of_vectors(cols) == 2
    ok = ok and ME + MU + MT == F(188309937445, 10 ** 8) and ME + MU + MT != 0
    ok = ok and cform(F_PLUS) == CY(0) and cform(F_MINUS) == CY(0) and cform(F_PLUS, F_MINUS) == CY(3)
    for a in (F(0), F(2), F(-5, 3)):
        for b in (F(0), F(1, 2), F(-3)):
            w = [CY(a) * x + CY(b) * y for x, y in zip(F_PLUS, F_MINUS)]
            val = cform(w)
            ok = ok and val == CY(6 * a * b) and (val == CY(0)) == (a * b == 0)
    # Gamma f_+ real (all imaginary parts zero) forces Gamma = 0: the map Gamma -> Im parts has rank 2
    rows = []
    for Gam in (CY(1), CY(0, 1)):
        rows.append([(Gam * z).b for z in F_PLUS])
    ok = ok and GA.rank_of_vectors(rows) == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_bracket_form"; return _tp_rv


def check_fourier_coordinates_and_the_one_number():
    ok = True
    imgs = []
    for Gam in GAMMAS:
        comps = [(Gam * z).re() for z in F_PLUS]
        ok = ok and sum(comps) == 0
        ok = ok and sum(c * c for c in comps) == F(3, 2) * Gam.nsq()
        for a in AVALS:
            v = [a + c for c in comps]
            Q = sum(x * x for x in v) / sum(v) ** 2
            ok = ok and Q == F(1, 3) + Gam.nsq() / (6 * a * a)
            reG, imG2 = Gam.re(), F(3, 4) * Gam.b * Gam.b
            ok = ok and 3 * (v[2] - v[1]) ** 2 * reG * reG == imG2 * (2 * v[0] - v[1] - v[2]) ** 2
            # the signs: 2 v0 - v1 - v2 = 3 Re Gamma and v2 - v1 = (3/2) b, with Im Gamma = (sqrt 3/2) b
            ok = ok and 2 * v[0] - v[1] - v[2] == 3 * reG and v[2] - v[1] == F(3, 2) * Gam.b
        imgs.append(comps)
    ok = ok and GA.rank_of_vectors(imgs) == 2
    # lepton data, labelling (tau, e, mu) = k = 0, 1, 2
    bs = [sqrt_bounds(m) for m in (MT, ME, MU)]
    S_lo, S_hi = sum(b[0] for b in bs), sum(b[1] for b in bs)
    M = ME + MU + MT
    Q_lo, Q_hi = M / (S_hi * S_hi), M / (S_lo * S_lo)
    r_lo, r_hi = 6 * Q_lo - 2, 6 * Q_hi - 2
    ok = ok and 2 - F(1, 10 ** 4) < r_lo and r_hi < 2 + F(1, 10 ** 4)
    ok = ok and F(141415, 10 ** 5) ** 2 <= r_lo and r_hi < F(141425, 10 ** 5) ** 2
    ok = ok and F(141415, 10 ** 5) ** 2 <= 2 < F(141425, 10 ** 5) ** 2
    num_lo, num_hi = 3 * (bs[2][0] - bs[1][1]) ** 2, 3 * (bs[2][1] - bs[1][0]) ** 2
    den_lo = 2 * bs[0][0] - bs[1][1] - bs[2][1]
    den_hi = 2 * bs[0][1] - bs[1][0] - bs[2][0]
    # Re Gamma > 0 (2 v0 > v1 + v2) and Im Gamma > 0 (v2 > v1): delta lies in (0, pi/2), where tan increases
    ok = ok and den_lo > 0 and bs[2][0] - bs[1][1] > 0
    t2_lo, t2_hi = num_lo / (den_hi * den_hi), num_hi / (den_lo * den_lo)
    (s1, s1h), (c1, c1h) = sin_cos_bounds(F(2215, 10 ** 4))
    (s2, s2h), (c2, c2h) = sin_cos_bounds(F(2225, 10 ** 4))
    ok = ok and (s1h / c1) ** 2 < t2_lo and t2_hi < (s2 / c2h) ** 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_fourier_coordinates_and_the_one_number"; return _tp_rv
