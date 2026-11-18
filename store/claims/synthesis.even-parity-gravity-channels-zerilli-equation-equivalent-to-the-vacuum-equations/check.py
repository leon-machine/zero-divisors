"""synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations: exact checks.

The Schwarzschild field in the static gauge of Gauge Theory Gravity (gtg.static_field, the stored connection forms),
perturbed to first order: hb^{-1}(e_mu) = g_mu + eps k_mu, Omega = Omega_0 + eps Omega_1 with Omega_1 solved exactly
from the linearised torsion-free condition, and the first-order Ricci vectors calR_1(gamma_b) read from the
linearised field strength (the construction of the stored odd-parity result, repeated here).

Two exact rings carry the identities, both with division by units only, so a computation that completes is an
identity in the variables:
  U = Q[z, 1/z, 1/(1 - z^2), s, 1/s, c]/(c^2 = 1 - s^2): z = sqrt f with M = 1 (r = 2/(1 - z^2)), s and c the
      sine and cosine of the polar angle; jets with coefficients in U give the first-order Ricci vectors as
      identities in the radius and the polar angle together;
  A = Q[r, lam, w][1/r, 1/(r - 2), 1/(lam r + 3), 1/w]: M = 1, lam = (L - 2)/2, w = omega^2; linear forms LF in
      the jet symbols d_t^p d_r^q X with coefficients in A carry the radial differential identities.
Checks:
  (1) even parity: every component of every calR_1(gamma_b) equals its closed form, for each of the 24 basis jets
      of (H0, H1, H2, K) and each basis 2-jet of the angular function, identically in sqrt f and the angle;
  (2) odd parity: the stored closed forms, identically in sqrt f and the angle (the stored grid had three angles);
  (3) sampled controls at rational points with other masses and generic jets; a wrong coefficient fails;
  (4) the converse: the reconstructed field of any Phi has vacuum equations that are differential multiples of
      the Zerilli operator on Phi, and its Zerilli-Moncrief function is (lam + 1) Phi;
  (5) an oscillating channel: the vacuum equations give a first-order system and one algebraic relation, the
      Zerilli operator on the Zerilli-Moncrief function is a multiple of that relation, and the field is the
      reconstruction of its own master function.
"""
from fractions import Fraction as F
import GA
import gtg
from gtg import Jet, m_add, m_scal, m_neg, m_d, comm
from tp_premise import premise

SCHW = "pairing.imported-schwarzschild-connection-curvature"
STORED = "synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional"

MONOMIALS = [(p, q) for p in range(3) for q in range(3 - p)]      # the six second-order jet monomials t^p R^q
ANGULAR_BASIS = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]                 # (P, P', P'') at the point
ODD_SEPARATION = [F(7, 2), F(6)]                                  # two values of L decide a degree-one dependence
POINTS = [(F(3), F(1, 2), F(3, 5), F(4, 5)), (F(5), F(2, 3), F(5, 13), F(12, 13))]   # r0, sqrt f, sin, cos
H_COEF = [(1, 2, 3, -1, 5, 7), (2, -1, 1, 3, -2, 5), (0, 1, -2, 4, 1, -3), (3, 2, -5, 1, 4, 1)]
P_DATA = [(F(2), F(-1), F(3)), (F(1), F(3), F(-2))]


# ---------------------------------------------------------------------------
# the ring U (radius and angle)
# ---------------------------------------------------------------------------

def _padd(a, b):
    out = dict(a)
    for m, x in b.items():
        y = out.get(m, 0) + x
        if y:
            out[m] = y
        else:
            out.pop(m, None)
    return out


def _umul(a, b):
    out = {}
    for (i1, j1, k1), x in a.items():
        for (i2, j2, k2), y in b.items():
            v = x * y
            if k1 + k2 == 2:                       # c^2 = 1 - s^2
                terms = (((i1 + i2, j1 + j2, 0), v), ((i1 + i2, j1 + j2 + 2, 0), -v))
            else:
                terms = (((i1 + i2, j1 + j2, k1 + k2), v),)
            for m, t in terms:
                t = out.get(m, 0) + t
                if t:
                    out[m] = t
                else:
                    out.pop(m, None)
    return out


def _div_1mz2(p):
    """p / (1 - z^2) if the division is exact, else None (long division from the top degree in z)."""
    groups = {}
    for (i, j, k), x in p.items():
        groups.setdefault((j, k), {})[i] = x
    out = {}
    for (j, k), co in groups.items():
        while co:
            n = max(co)
            if n < 2:
                return None
            x = co.pop(n)
            out[(n - 2, j, k)] = -x                 # -x z^(n-2) (1 - z^2) = x z^n - x z^(n-2)
            t = co.get(n - 2, 0) + x
            if t:
                co[n - 2] = t
            else:
                co.pop(n - 2, None)
    return out


_1MZ2 = {(0, 0, 0): F(1), (2, 0, 0): F(-1)}


class U(object):
    """numerator {(i, j, k): x} for x z^i s^j c^k (k = 0, 1) over z^a (1 - z^2)^b s^e."""
    __slots__ = ("n", "d")

    def __init__(self, n, d=(0, 0, 0)):
        a, b, e = d
        if not n:
            self.n, self.d = {}, (0, 0, 0)
            return
        m = min(min(i for (i, _, _) in n), a)
        if m:
            n, a = {(i - m, j, k): x for (i, j, k), x in n.items()}, a - m
        m = min(min(j for (_, j, _) in n), e)
        if m:
            n, e = {(i, j - m, k): x for (i, j, k), x in n.items()}, e - m
        while b:
            q = _div_1mz2(n)
            if q is None:
                break
            n, b = q, b - 1
        self.n, self.d = n, (a, b, e)

    @staticmethod
    def const(x):
        x = F(x)
        return U({(0, 0, 0): x} if x else {})

    @staticmethod
    def gen(i):
        return U({tuple(1 if k == i else 0 for k in range(3)): F(1)})

    @staticmethod
    def _c(o):
        return o if isinstance(o, U) else U.const(o)

    @staticmethod
    def _den(d):
        a, b, e = d
        p = {(a, e, 0): F(1)}
        for _ in range(b):
            p = _umul(p, _1MZ2)
        return p

    def __add__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        o = U._c(o)
        if not self.n:
            return o
        if not o.n:
            return self
        d = tuple(max(x, y) for x, y in zip(self.d, o.d))
        n1 = _umul(self.n, U._den(tuple(x - y for x, y in zip(d, self.d))))
        n2 = _umul(o.n, U._den(tuple(x - y for x, y in zip(d, o.d))))
        return U(_padd(n1, n2), d)
    __radd__ = __add__

    def __neg__(self):
        r = U({})
        r.n, r.d = {m: -x for m, x in self.n.items()}, self.d
        return r

    def __sub__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        return self + (-U._c(o))

    def __rsub__(self, o):
        return U._c(o) + (-self)

    def __mul__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        o = U._c(o)
        if not self.n or not o.n:
            return U({})
        return U(_umul(self.n, o.n), tuple(x + y for x, y in zip(self.d, o.d)))
    __rmul__ = __mul__

    def inv(self):
        if not self.n:
            raise ZeroDivisionError
        n, pw = self.n, 0
        while len(n) > 1:
            q = _div_1mz2(n)
            if q is None:
                raise ArithmeticError("U: division by a non-unit")
            n, pw = q, pw + 1
        ((i, j, k), x), = n.items()
        if k:
            raise ArithmeticError("U: division by a non-unit")
        a, b, e = self.d
        return U(_umul({(a, e, 0): 1 / x}, U._den((0, b, 0))), (i, pw, j))

    def __truediv__(self, o):
        if isinstance(o, Jet):
            return NotImplemented
        return self * U._c(o).inv()

    def __rtruediv__(self, o):
        return U._c(o) * self.inv()

    def __pow__(self, n):
        if n < 0:
            return self.inv() ** (-n)
        out = U.const(1)
        for _ in range(n):
            out = out * self
        return out

    def __bool__(self):
        return bool(self.n)

    def __eq__(self, o):
        return not (self - U._c(o)).n

    def __ne__(self, o):
        return not self.__eq__(o)
    __hash__ = None


# ---------------------------------------------------------------------------
# the first-order Ricci vectors (the stored construction)
# ---------------------------------------------------------------------------

def lin_ricci(fld, TH1):
    """Jets of the first-order Ricci vectors calR_1(gamma_b) of the field TH0 + eps TH1 (torsion-free)."""
    d, sq = fld.d, fld.sq
    g1 = [{(a,): TH1[a][mu] for a in range(d) if TH1[a][mu]} for mu in range(d)]
    bl = gtg.bivector_blades(d)
    nb = len(bl)
    rhs = []
    for p in range(d):
        for q in range(p + 1, d):
            t = m_add(m_d(g1[q], p), m_neg(m_d(g1[p], q)),
                      comm(fld.Om[p], g1[q], sq), m_neg(comm(fld.Om[q], g1[p], sq)))
            for a in range(d):
                rhs.append(-t.get((a,), F(0)))
    sol = gtg.ring_solve(gtg._torsion_matrix(fld.g, sq), rhs)
    Om1 = [{bl[j]: sol[mu * nb + j] for j in range(nb) if sol[mu * nb + j]} for mu in range(d)]
    H0 = fld.hb_matrix_jet()
    H1 = [[-sum((H0[mu][a] * TH1[a][nu] * H0[nu][b] for a in range(d) for nu in range(d)), F(0))
           for b in range(d)] for mu in range(d)]
    Rc1 = {}
    for a in range(d):
        for b in range(a + 1, d):
            acc = {}
            for mu in range(d):
                for nu in range(mu + 1, d):
                    R0 = fld.strength_jet(mu, nu)
                    R1 = m_add(m_d(Om1[nu], mu), m_neg(m_d(Om1[mu], nu)),
                               comm(fld.Om[mu], Om1[nu], sq), comm(Om1[mu], fld.Om[nu], sq))
                    c0 = H0[mu][a] * H0[nu][b] - H0[nu][a] * H0[mu][b]
                    c1 = (H1[mu][a] * H0[nu][b] + H0[mu][a] * H1[nu][b]
                          - H1[nu][a] * H0[mu][b] - H0[nu][a] * H1[mu][b])
                    if R1:
                        acc = m_add(acc, m_scal(c0, R1))
                    if R0:
                        acc = m_add(acc, m_scal(c1, R0))
            Rc1[(a, b)] = m_scal(gtg.STORE_SIGN, acc)
    return [gtg.ricci(Rc1, GA.gen(b), sq) for b in range(d)]


def components(ric):
    out = {}
    for b in range(4):
        for (a,), v in ric[b].items():
            v = gtg._val(v)
            if v:
                out[(a, b)] = v                    # the gamma_a component of calR_1(gamma_b)
    return out


def even_parts(H0, H1, H2, K, r, f, M):
    """The radial pieces of the even-parity closed forms; .d(0) = d/dt, .d(1) = d/dr (gtg.Jet or LF)."""
    r2 = r * r
    t, x = 0, 1
    c00 = (f / 2 * H0.d(x).d(x) + (2 * r - M) / (2 * r2) * H0.d(x) - H1.d(t).d(x)
           - (2 * r - 3 * M) / (r2 * f) * H1.d(t) + M / (2 * r2) * H2.d(x) + H2.d(t).d(t) / (2 * f)
           - M / r2 * K.d(x) + K.d(t).d(t) / f)
    d00 = H0 / (2 * r2)
    c01 = K.d(t).d(x) + (r - 3 * M) / (r2 * f) * K.d(t) - H2.d(t) / r
    d01 = H1 / (2 * r2)
    c02 = (f * H1).d(x) - H2.d(t) - K.d(t)
    c12 = f * (H0.d(x) - K.d(x)) - H1.d(t) - (r - 3 * M) / r2 * H0 + (r - M) / r2 * H2
    c11 = (f / 2 * H0.d(x).d(x) + 3 * M / (2 * r2) * H0.d(x) - H1.d(t).d(x) - M / (r2 * f) * H1.d(t)
           + (2 * r - 3 * M) / (2 * r2) * H2.d(x) + H2.d(t).d(t) / (2 * f)
           - (2 * r - 3 * M) / r2 * K.d(x) - f * K.d(x).d(x))
    d11 = -H2 / (2 * r2)
    c22 = (f / (2 * r) * (H0.d(x) + H2.d(x)) - H1.d(t) / r + (H2 - K) / r2
           - (2 * r - 3 * M) / r2 * K.d(x) - f / 2 * K.d(x).d(x) + K.d(t).d(t) / (2 * f))
    dK = -K / (2 * r2)
    cHH = (H0 - H2) / (2 * r2)
    return dict(c00=c00, d00=d00, c01=c01, d01=d01, c02=c02, c12=c12, c11=c11, d11=d11, c22=c22, dK=dK, cHH=cHH)


def even_expected(parts, ang, r0, sqf, cot):
    """The closed forms of the components from the radial pieces and the 2-jet (P, P', P'') at the point."""
    a, b, p2 = ang
    DP = p2 + cot * b                              # P'' + cot P'
    pre = b / (2 * r0 * sqf)
    return {(0, 0): a * parts["c00"] + DP * parts["d00"],
            (0, 1): a * parts["c01"] + DP * parts["d01"],
            (1, 0): -(a * parts["c01"] + DP * parts["d01"]),
            (0, 2): -pre * parts["c02"],
            (2, 0): pre * parts["c02"],
            (1, 2): pre * parts["c12"],
            (2, 1): pre * parts["c12"],
            (1, 1): a * parts["c11"] + DP * parts["d11"],
            (2, 2): a * parts["c22"] + DP * parts["dK"] + p2 * parts["cHH"],
            (3, 3): a * parts["c22"] + DP * parts["dK"] + cot * b * parts["cHH"]}


def even_case(M, r0, sqf, s0, c0, Hjets, ang):
    """Engine components and closed forms of the even-parity field at the point; Hjets(t, R) returns the four
    jets (H0, H1, H2, K); ang = (P, P', P'') at the point. The base point may lie in Q or in U."""
    f = gtg.f_static(M)
    fld = gtg.static_field(r0, s0, c0, f, order=1, sqrt_f=sqf)
    t = Jet.var(0, F(0), 4, 2)
    r = Jet.var(1, r0, 4, 2)
    th = Jet.var(2, F(0), 4, 2)
    sn, cs = gtg.sincos(2, s0, c0, 4, 2)
    fj = f(r)
    sf = fj.pw(F(1, 2), sqf)
    H0, H1, H2, K = Hjets(t, r - r0)
    P = ang[0] + ang[1] * th + F(ang[2]) / 2 * th * th
    Z = Jet.const(0, 4)
    TH1 = [[Z] * 4 for _ in range(4)]
    TH1[0][0] = -sf * H0 * P / 2                   # f (1 - H0 P) dt^2
    TH1[1][0] = sf * H1 * P                        # -2 H1 P dt dr
    TH1[1][1] = H2 * P / (2 * sf)                  # -(1 + H2 P) dr^2 / f
    TH1[2][2] = r * K * P / 2                      # -r^2 (1 + K P) dOmega^2
    TH1[3][3] = r * sn * K * P / 2
    got = components(lin_ricci(fld, TH1))
    parts = {k: gtg._val(v) for k, v in even_parts(H0, H1, H2, K, r, fj, M).items()}
    return got, even_expected(parts, ang, r0, sqf, c0 / s0)


def basis_jets(fn, mono, n):
    def Hjets(t, R):
        zero = Jet(0, None, 4, 2)
        out = [zero] * n
        out[fn] = Jet(1, None, 4, 2) * (t ** mono[0]) * (R ** mono[1])
        return out
    return Hjets


def generic_jets(coefs):
    def Hjets(t, R):
        return [c[0] + c[1] * t + c[2] * R + c[3] * t * t + c[4] * t * R + c[5] * R * R for c in coefs]
    return Hjets


def same(got, want, zero):
    return all(got.get(k, zero) == want.get(k, zero) for k in set(got) | set(want))


def check_even_parity_closed_forms_identically_in_radius_and_angle():
    """(1): 24 basis jets of (H0, H1, H2, K) times 3 basis 2-jets of P, every one of the sixteen components,
    as identities in U (z = sqrt f, r = 2/(1 - z^2), M = 1, and the sine and cosine of the polar angle)."""
    premise(SCHW)
    z, s0, c0 = U.gen(0), U.gen(1), U.gen(2)
    assert c0 * c0 + s0 * s0 == 1 and 1 - 2 * ((1 - z * z) / 2) == z * z
    r0 = 2 / (1 - z * z)
    zero = U.const(0)
    cases = nonzero = 0
    for fn in range(4):
        for mono in MONOMIALS:
            for ang in ANGULAR_BASIS:
                got, want = even_case(F(1), r0, z, s0, c0, basis_jets(fn, mono, 4), ang)
                assert same(got, want, zero)
                cases += 1
                nonzero += len(got)
    assert cases == 72 and nonzero == 72
    # the ring refuses a division by a non-unit, so the comparisons above never left it
    try:
        1 / (1 + z)
        refused = False
    except ArithmeticError:
        refused = True
    assert refused


def odd_equations(h0, h1, fj, r, M, L):
    Eth = h0.d(0) / fj - (fj * h1).d(1)
    Er = h1.d(0).d(0) - h0.d(0).d(1) + 2 * h0.d(0) / r + (L - 2) * fj * h1 / (r * r)
    Et = fj * (h0.d(1).d(1) - h1.d(0).d(1) - 2 * h1.d(0) / r) - (L / (r * r) - 4 * M / (r * r * r)) * h0
    return Et, Er, Eth


def odd_case(M, r0, sqf, s0, c0, L, hjets, a, b):
    """Engine components and stored closed forms of the odd-parity field; (a, b) = (S, S') at the point and
    S'' = cot S' - L S."""
    f = gtg.f_static(M)
    fld = gtg.static_field(r0, s0, c0, f, order=1, sqrt_f=sqf)
    t = Jet.var(0, F(0), 4, 2)
    r = Jet.var(1, r0, 4, 2)
    th = Jet.var(2, F(0), 4, 2)
    sn, cs = gtg.sincos(2, s0, c0, 4, 2)
    fj = f(r)
    sf = fj.pw(F(1, 2), sqf)
    h0, h1 = hjets(t, r - r0)
    cot = c0 / s0
    S = a + b * th + (cot * b - L * a) / 2 * th * th
    Z = Jet.const(0, 4)
    TH1 = [[Z] * 4 for _ in range(4)]
    TH1[0][3] = h0 * S / sf
    TH1[1][3] = -h1 * S * sf
    got = components(lin_ricci(fld, TH1))
    Et, Er, Eth = [x.v for x in odd_equations(h0, h1, fj, r, M, L)]
    pre = -a / (2 * r0 * s0 * sqf)
    ang = (b - 2 * cot * a) / (2 * r0 * r0 * s0)
    want = {(0, 3): pre * Et, (1, 3): pre * Er, (2, 3): ang * Eth,
            (3, 0): -(pre * Et), (3, 1): pre * Er, (3, 2): ang * Eth}
    return got, want


def check_odd_parity_closed_forms_identically_in_radius_and_angle():
    """(2): the stored odd-parity closed forms as identities in U: 12 basis jets of (h0, h1), 2 basis data of
    (S, S'), 2 values of L (both sides are of degree one in L, through S'' alone)."""
    premise(SCHW)
    premise(STORED)
    z, s0, c0 = U.gen(0), U.gen(1), U.gen(2)
    r0 = 2 / (1 - z * z)
    zero = U.const(0)
    cases = nonzero = 0
    for L in ODD_SEPARATION:
        for which in range(2):
            for mono in MONOMIALS:
                for (a, b) in ((F(1), F(0)), (F(0), F(1))):
                    got, want = odd_case(F(1), r0, z, s0, c0, L, basis_jets(which, mono, 2), a, b)
                    assert same(got, want, zero)
                    cases += 1
                    nonzero += len(got)
    assert cases == 48 and nonzero == 56


def check_sampled_controls_other_masses_and_wrong_coefficients():
    """(3): rational points with f a square, masses 9/8 and 25/18, generic jets and 2-jets of P; the closed
    forms with one coefficient changed fail."""
    premise(SCHW)
    zero = F(0)
    seen = 0
    for (r0, w, s0, c0), ang in zip(POINTS, P_DATA):
        M = gtg.mass_for_root(r0, w)
        assert M in (F(9, 8), F(25, 18)) and 1 - 2 * M / r0 == w * w
        got, want = even_case(M, r0, w, s0, c0, generic_jets(H_COEF), ang)
        assert same(got, want, zero) and len(got) == 10
        bad = dict(want)
        bad[(1, 1)] = want[(1, 1)] + ang[0] * M * H_COEF[2][2] / (r0 * r0)       # 2r - 3M -> 2r - M in H2'
        assert not same(got, bad, zero)
        # the mass enters: the closed forms of another mass fail at this point
        f = gtg.f_static(M)
        t, r = Jet.var(0, F(0), 4, 2), Jet.var(1, r0, 4, 2)
        Hs = generic_jets(H_COEF)(t, r - r0)
        wrong = {k: gtg._val(v) for k, v in even_parts(Hs[0], Hs[1], Hs[2], Hs[3], r, f(r), 2 * M).items()}
        assert not same(got, even_expected(wrong, ang, r0, w, c0 / s0), zero)
        seen += 1
    assert seen == 2


# ---------------------------------------------------------------------------
# the ring A and linear forms in jet symbols (radial identities)
# ---------------------------------------------------------------------------

def _amul(a, b):
    out = {}
    for (i1, j1, k1), x in a.items():
        for (i2, j2, k2), y in b.items():
            m = (i1 + i2, j1 + j2, k1 + k2)
            t = out.get(m, 0) + x * y
            if t:
                out[m] = t
            else:
                out.pop(m, None)
    return out


P_R = {(1, 0, 0): F(1)}
P_RM2 = {(1, 0, 0): F(1), (0, 0, 0): F(-2)}
P_LR3 = {(1, 1, 0): F(1), (0, 0, 0): F(3)}
P_W = {(0, 0, 1): F(1)}
ATOMS = (P_R, P_RM2, P_LR3, P_W)


def _div_linear(p, lead, low, const):
    """Exact quotient of p by (monomial `lead`) + const, where `low` orders the long division; else None."""
    co = dict(p)
    out = {}
    while co:
        m = max(co, key=low)
        q = tuple(x - y for x, y in zip(m, lead))
        if min(q) < 0:
            return None
        x = co.pop(m)
        out[q] = x
        t = co.get(q, 0) - const * x
        if t:
            co[q] = t
        else:
            co.pop(q, None)
    return out


def _div_rm2(p):
    return _div_linear(p, (1, 0, 0), lambda t: t, F(-2))


def _div_lr3(p):
    return _div_linear(p, (1, 1, 0), lambda t: (t[1], t[0], t[2]), F(3))


class A(object):
    """numerator {(i, j, k): x} for x r^i lam^j w^k over r^a (r - 2)^b (lam r + 3)^c w^e."""
    __slots__ = ("n", "d")

    def __init__(self, n, d=(0, 0, 0, 0)):
        if not n:
            self.n, self.d = {}, (0, 0, 0, 0)
            return
        a, b, c, e = d
        m = min(min(i for (i, _, _) in n), a)
        if m:
            n, a = {(i - m, j, k): x for (i, j, k), x in n.items()}, a - m
        m = min(min(k for (_, _, k) in n), e)
        if m:
            n, e = {(i, j, k - m): x for (i, j, k), x in n.items()}, e - m
        while b:
            q = _div_rm2(n)
            if q is None:
                break
            n, b = q, b - 1
        while c:
            q = _div_lr3(n)
            if q is None:
                break
            n, c = q, c - 1
        self.n, self.d = n, (a, b, c, e)

    @staticmethod
    def const(x):
        x = F(x)
        return A({(0, 0, 0): x} if x else {})

    @staticmethod
    def gen(i):
        return A({tuple(1 if k == i else 0 for k in range(3)): F(1)})

    @staticmethod
    def _c(o):
        return o if isinstance(o, A) else A.const(o)

    @staticmethod
    def _den(d):
        p = {(0, 0, 0): F(1)}
        for atom, e in zip(ATOMS, d):
            for _ in range(e):
                p = _amul(p, atom)
        return p

    def __add__(self, o):
        if isinstance(o, LF):
            return NotImplemented
        o = A._c(o)
        if not self.n:
            return o
        if not o.n:
            return self
        d = tuple(max(x, y) for x, y in zip(self.d, o.d))
        n1 = _amul(self.n, A._den(tuple(x - y for x, y in zip(d, self.d))))
        n2 = _amul(o.n, A._den(tuple(x - y for x, y in zip(d, o.d))))
        return A(_padd(n1, n2), d)
    __radd__ = __add__

    def __neg__(self):
        r = A({})
        r.n, r.d = {m: -x for m, x in self.n.items()}, self.d
        return r

    def __sub__(self, o):
        if isinstance(o, LF):
            return NotImplemented
        return self + (-A._c(o))

    def __rsub__(self, o):
        return A._c(o) + (-self)

    def __mul__(self, o):
        if isinstance(o, LF):
            return NotImplemented
        o = A._c(o)
        if not self.n or not o.n:
            return A({})
        return A(_amul(self.n, o.n), tuple(x + y for x, y in zip(self.d, o.d)))
    __rmul__ = __mul__

    def inv(self):
        if not self.n:
            raise ZeroDivisionError
        n, e = self.n, [0, 0, 0, 0]
        for slot, div in ((1, _div_rm2), (2, _div_lr3)):
            while True:
                q = div(n)
                if q is None:
                    break
                n, e[slot] = q, e[slot] + 1
        if len(n) != 1:
            raise ArithmeticError("A: division by a non-unit")
        ((i, j, k), x), = n.items()
        if j:
            raise ArithmeticError("A: division by a non-unit")
        e[0], e[3] = i, k
        return A({m: y / x for m, y in A._den(self.d).items()}, tuple(e))

    def __truediv__(self, o):
        if isinstance(o, LF):
            return NotImplemented
        return self * A._c(o).inv()

    def __rtruediv__(self, o):
        return A._c(o) * self.inv()

    def __pow__(self, n):
        out = A.const(1)
        for _ in range(n):
            out = out * self
        return out

    def dr(self):
        """d/dr."""
        if not self.n:
            return self
        a, b, c, e = self.d
        dn = {(i - 1, j, k): i * x for (i, j, k), x in self.n.items() if i}
        lead = _amul(_amul(dn, P_R), _amul(P_RM2, P_LR3))
        corr = {}
        for coef, poly in ((a, _amul(P_RM2, P_LR3)), (b, _amul(P_R, P_LR3)),
                           (c, _amul({(1, 1, 0): F(1)}, P_RM2))):
            corr = _padd(corr, {m: -coef * x for m, x in poly.items()} if coef else {})
        return A(_padd(lead, _amul(self.n, corr)), (a + 1, b + 1, c + 1, e))

    def __bool__(self):
        return bool(self.n)

    def __eq__(self, o):
        return not (self - A._c(o)).n

    def __ne__(self, o):
        return not self.__eq__(o)
    __hash__ = None


class LF(object):
    """Linear form sum c[sym] sym in jet symbols sym = (name, p, q) = d_t^p d_r^q name, coefficients in A."""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {s: x for s, x in (c or {}).items() if x}

    @staticmethod
    def sym(name, p=0, q=0):
        return LF({(name, p, q): A.const(1)})

    def __add__(self, o):
        if not isinstance(o, LF):
            return NotImplemented
        out = dict(self.c)
        for s, x in o.c.items():
            out[s] = out[s] + x if s in out else x
        return LF(out)

    def __neg__(self):
        return LF({s: -x for s, x in self.c.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        o = A._c(o)
        return LF({s: x * o for s, x in self.c.items()})
    __rmul__ = __mul__

    def __truediv__(self, o):
        return self * A._c(o).inv()

    def d(self, i):
        out = LF()
        for (name, p, q), x in self.c.items():
            if i == 0:
                out = out + LF({(name, p + 1, q): x})
            else:
                out = out + LF({(name, p, q + 1): x, (name, p, q): x.dr()})
        return out

    def __bool__(self):
        return bool(self.c)

    def __eq__(self, o):
        return not (self - o).c
    __hash__ = None

    def coef(self, name, p=0, q=0):
        return self.c.get((name, p, q), A.const(0))

    def names(self):
        return sorted(self.c)


def substitute(lf, rule):
    """Replace symbols by linear forms until none is left to replace: rule(sym) -> LF or None."""
    while True:
        out, changed = LF(), False
        for s, x in lf.c.items():
            rep = rule(s)
            if rep is None:
                out = out + LF({s: x})
            else:
                out = out + rep * x
                changed = True
        lf = out
        if not changed:
            return lf


def proportional(x, y):
    """x is a multiple of y over the fraction field: every 2 x 2 minor of the coefficient pair vanishes."""
    keys = sorted(set(x.c) | set(y.c))
    z = A.const(0)
    return all(not (x.c.get(i, z) * y.c.get(j, z) - x.c.get(j, z) * y.c.get(i, z)).n for i in keys for j in keys)


R_, LAM, W_ = A.gen(0), A.gen(1), A.gen(2)                         # r, lam, w = omega^2 (M = 1)
F_ = (R_ - 2) / R_                                                # f = 1 - 2/r
DEN = LAM * R_ + 3                                                # lam r + 3M
L_ = 2 * LAM + 2                                                  # L = 2 lam + 2
V_EVEN = F_ * (2 * LAM * LAM * (LAM + 1) * R_ ** 3 + 6 * LAM * LAM * R_ * R_ + 18 * LAM * R_ + 18) / (R_ ** 3 * DEN * DEN)


def zerilli(u):
    def D(v):
        return F_ * v.d(1)
    return u.d(0).d(0) - D(D(u)) + V_EVEN * u


def radial_equations(H0, H1, H2, K):
    """The seven radial equations of a harmonic with P'' + cot P' = -L P (clause (2) of the statement)."""
    p = even_parts(H0, H1, H2, K, R_, F_, F(1))
    return dict(E1=p["c00"] - L_ * p["d00"], E2=p["c01"] - L_ * p["d01"], E3=p["c02"], E4=p["c12"],
                E5=p["c11"] - L_ * p["d11"], E6=H0 - H2, E7=p["c22"] - L_ * p["dK"])


def master(H2, K):
    """The stored Zerilli-Moncrief function r (K + (f r / (lam r + 3M)) (H2 - r K'))."""
    return R_ * (K + (F_ * R_ / DEN) * (H2 - R_ * K.d(1)))


def reconstruction(Phi):
    """(K, H, H1) of the statement's clause (3), M = 1."""
    K = (LAM * (LAM + 1) * R_ * R_ + 3 * LAM * R_ + 6) / (R_ * R_ * DEN) * Phi + F_ * Phi.d(1)
    H = (-(LAM * LAM * (LAM + 1) * R_ ** 3 + 3 * LAM * LAM * R_ * R_ + 9 * LAM * R_ + 9) / (R_ * R_ * DEN * DEN) * Phi
         + (LAM * R_ * R_ - LAM * R_ + 3) / (R_ * DEN) * Phi.d(1) + (R_ - 2) * Phi.d(1).d(1))
    H1 = R_ * Phi.d(0).d(1) + (LAM * R_ * R_ - 3 * LAM * R_ - 3) / ((R_ - 2) * DEN) * Phi.d(0)
    return K, H, H1


def check_reconstructed_field_of_a_zerilli_solution_is_a_vacuum_solution():
    """(4): with Phi_tt eliminated by Phi_tt = D D Phi - V Phi + Z (Z the Zerilli operator on Phi), every radial
    equation of the reconstructed field is a differential operator applied to Z, with no term in Phi left;
    the Zerilli-Moncrief function of the reconstructed field is (lam + 1) Phi for every Phi."""
    premise(STORED)
    Phi, Z = LF.sym("Phi"), LF.sym("Z")
    assert zerilli(Phi) - (Phi.d(0).d(0) - F_ * (F_ * Phi.d(1)).d(1) + V_EVEN * Phi) == LF()
    base = F_ * (F_ * Phi.d(1)).d(1) - V_EVEN * Phi + Z

    def rule(s):
        name, p, q = s
        if name != "Phi" or p < 2:
            return None
        x = base
        for _ in range(p - 2):
            x = x.d(0)
        for _ in range(q):
            x = x.d(1)
        return x
    K, H, H1 = reconstruction(Phi)
    red = {k: substitute(e, rule) for k, e in radial_equations(H, H1, H, K).items()}
    assert all(all(s[0] == "Z" for s in e.c) for e in red.values())           # no Phi left: multiples of Z
    assert not red["E2"] and not red["E3"] and not red["E6"]                  # these three hold for every Phi
    # the operators: E4 = -(r d_r + a) Z and E7 = -(1/2) Z' + b Z, E1 and E5 of second order in Z
    a = (LAM * R_ * R_ - 3 * LAM * R_ - 3) / ((R_ - 2) * DEN)
    assert red["E4"] == -(R_ * Z.d(1)) - a * Z
    b = (LAM * LAM * R_ * R_ - LAM * R_ * R_ + 9 * LAM * R_ + 12) / (2 * R_ * (R_ - 2) * DEN)
    assert red["E7"] == -(Z.d(1) / 2) + b * Z
    assert red["E1"].coef("Z", 0, 2) == -R_ / 2 and red["E5"].coef("Z", 0, 2) == -R_ / 2
    assert red["E1"].names() == red["E5"].names() == [("Z", 0, 0), ("Z", 0, 1), ("Z", 0, 2)]
    # the master function of the reconstructed field, with no use of the Zerilli equation
    assert master(H, K) == (LAM + 1) * Phi
    assert master(H, K) != LAM * Phi
    # a wrong potential (f/r^2 added) leaves terms in Phi
    bad_v = V_EVEN + F_ / (R_ * R_)
    bad_base = F_ * (F_ * Phi.d(1)).d(1) - bad_v * Phi + Z

    def bad_rule(s):
        name, p, q = s
        if name != "Phi" or p < 2:
            return None
        x = bad_base
        for _ in range(p - 2):
            x = x.d(0)
        for _ in range(q):
            x = x.d(1)
        return x
    assert any(s[0] == "Phi" for s in substitute(radial_equations(H, H1, H, K)["E4"], bad_rule).c)


def check_oscillating_channel_field_is_the_reconstruction_of_its_master_function():
    """(5): on functions with d_t^2 = -w, w = omega^2 a unit, the equations E2, E3, E4 are a first-order system
    in r; under it E1, E5, E7 are multiples of one algebraic relation REL, which the system preserves; the
    Zerilli operator on the master function is a multiple of REL; and (lam + 1)(K, H, H1) is the reconstruction
    of the master function, with no use of REL."""
    premise(STORED)
    K, H, H1 = LF.sym("K"), LF.sym("H"), LF.sym("H1")
    rhs = {"K": -((R_ - 3) / (R_ * R_ * F_)) * K + H / R_ - (L_ / (2 * R_ * R_ * W_)) * H1.d(0)}
    rhs["H"] = rhs["K"] + (H1.d(0) - (2 / (R_ * R_)) * H) / F_
    rhs["H1"] = (H.d(0) + K.d(0)) / F_ - (2 / (R_ * R_ * F_)) * H1

    def time_rule(s):
        name, p, q = s
        return LF({(name, p - 2, q): -W_}) if p >= 2 else None

    def rule(s):
        name, p, q = s
        if p >= 2:
            return LF({(name, p - 2, q): -W_})
        if q >= 1:
            x = rhs[name]
            for _ in range(p):
                x = x.d(0)
            for _ in range(q - 1):
                x = x.d(1)
            return x
        return None

    E = radial_equations(H, H1, H, K)
    # the rules are the equations: E3 and E4 as they stand, E2 after one time derivative
    assert E["E3"] == F_ * (H1.d(1) - rhs["H1"])
    assert E["E4"] == F_ * ((H.d(1) - K.d(1)) - (rhs["H"] - rhs["K"]))
    assert substitute(E["E2"].d(0), time_rule) == -W_ * (K.d(1) - rhs["K"])
    red = {k: substitute(e, rule) for k, e in E.items()}
    assert not red["E2"] and not red["E3"] and not red["E4"] and not red["E6"]
    REL = red["E7"]
    assert REL.names() == [("H", 0, 0), ("H1", 1, 0), ("K", 0, 0)]
    assert REL.coef("H") == -DEN / (2 * R_ ** 3)
    assert REL.coef("H1", 1) == (LAM + 1 - W_ * R_ ** 3) / (2 * R_ ** 4 * W_)
    assert REL.coef("K") == (LAM * R_ * (R_ - 2) + (R_ - 3) - W_ * R_ ** 4) / (2 * R_ ** 3 * (R_ - 2))
    unit = REL.coef("H")                                          # -(lam r + 3)/(2 r^3), a unit of A

    def multiple_of_rel(x):
        """x = mu REL with mu = (coefficient of H in x)/(that of REL), an element of A: regular on r > 2."""
        return bool(x) and proportional(x, REL) and x == (x.coef("H") / unit) * REL
    for k in ("E1", "E5"):
        assert multiple_of_rel(red[k])
    assert multiple_of_rel(substitute(REL.d(1), rule))            # the system preserves the relation
    Psi = master(H, K)
    zr = substitute(zerilli(Psi), rule)
    assert multiple_of_rel(zr)                                    # Zerilli's equation follows from the vacuum equations
    assert not proportional(substitute(zerilli(Psi) + F_ * Psi / (R_ * R_), rule), REL)
    Kr, Hr, H1r = reconstruction(Psi)
    assert substitute((LAM + 1) * K - Kr, rule) == LF()
    assert substitute((LAM + 1) * H - Hr, rule) == LF()
    assert substitute((LAM + 1) * H1 - H1r, rule) == LF()
    assert substitute(LAM * K - Kr, rule) != LF()
    # on the system the master function is a combination of K and d_t H1 alone, with nonzero coefficients
    assert substitute(Psi, rule).names() == [("H1", 1, 0), ("K", 0, 0)]
