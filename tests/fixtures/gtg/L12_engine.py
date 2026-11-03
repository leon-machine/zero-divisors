# ---- GTG engine (exact): first-order jets, fields (hb, Omega), field strength, store-sign curvature,
# ---- Ricci and Schouten maps, and the Cl(2,4) tractor gauge field Omega_T. Standalone copy (L12).
S13 = GA.sig(1, 3)
NV = 4                                   # background labels x^0..x^3
ETA = [1, -1, -1, -1]


def iroot(n, k):
    """Exact integer k-th root of n >= 0, or None."""
    if n < 0:
        return None
    lo, hi = 0, 1
    while hi ** k <= n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo if lo ** k == n else None


def qpow(x, a):
    """x ** a for Fraction x > 0 and rational a, exact; raises if irrational."""
    x, a = F(x), F(a)
    num, den = iroot(x.numerator, a.denominator), iroot(x.denominator, a.denominator)
    if num is None or den is None:
        raise ValueError("irrational power")
    return F(num, den) ** a.numerator


class J(object):
    """First-order jet in NV variables: value v and gradient g (exact Fractions)."""
    __slots__ = ("v", "g")

    def __init__(self, v, g=None):
        self.v = F(v)
        self.g = tuple(F(x) for x in g) if g is not None else (F(0),) * NV

    @staticmethod
    def var(i, x0):
        return J(x0, tuple(1 if k == i else 0 for k in range(NV)))

    def _c(self, o):
        return o if isinstance(o, J) else J(o)

    def __add__(self, o):
        o = self._c(o)
        return J(self.v + o.v, tuple(a + b for a, b in zip(self.g, o.g)))
    __radd__ = __add__

    def __neg__(self):
        return J(-self.v, tuple(-a for a in self.g))

    def __sub__(self, o):
        return self + (-self._c(o))

    def __rsub__(self, o):
        return self._c(o) - self

    def __mul__(self, o):
        o = self._c(o)
        return J(self.v * o.v, tuple(self.v * b + o.v * a for a, b in zip(self.g, o.g)))
    __rmul__ = __mul__

    def inv(self):
        return J(1 / self.v, tuple(-a / (self.v * self.v) for a in self.g))

    def __truediv__(self, o):
        return self * self._c(o).inv()

    def __rtruediv__(self, o):
        return self._c(o) * self.inv()

    def pw(self, a):
        """self ** a, rational a, with exact rational value."""
        a = F(a)
        val = qpow(self.v, a)
        return J(val, tuple(a * val / self.v * x for x in self.g))

    def d(self, i):
        return J(self.g[i])


def sincos(i, s0, c0):
    """sin and cos of the variable x^i at a point with sin = s0, cos = c0 (s0^2 + c0^2 = 1)."""
    e = tuple(1 if k == i else 0 for k in range(NV))
    return J(s0, tuple(c0 * x for x in e)), J(c0, tuple(-s0 * x for x in e))


def m_add(*xs):
    out = {}
    for x in xs:
        for b, c in x.items():
            out[b] = out[b] + c if b in out else c
    return out


def m_scal(c, x):
    return {b: c * v for b, v in x.items()}


def m_mul(x, y, sq=S13):
    out = {}
    for b1, c1 in x.items():
        for b2, c2 in y.items():
            s, b = GA.blade_mul(b1, b2, sq)
            if s:
                t = c1 * c2 * s
                out[b] = out[b] + t if b in out else t
    return out


def m_comm(x, y, sq=S13):
    """Commutator product x X y = (xy - yx)/2."""
    return m_scal(F(1, 2), m_add(m_mul(x, y, sq), m_scal(-1, m_mul(y, x, sq))))


def m_d(x, i):
    return {b: c.d(i) for b, c in x.items()}


def m_val(x):
    return {b: c.v for b, c in x.items() if c.v != 0}


def jvec(comps):
    return {(a,): c for a, c in enumerate(comps)}


def mat_inv(M):
    n = len(M)
    A = [[F(x) for x in row] + [F(1 if i == j else 0) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        A[c] = [x / piv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


class Field(object):
    """A gravitational field (hb, Omega) on flat spacetime in a gauge where the physical frame is the
    constant orthonormal frame gamma_a of Cl(1,3): hb^{-1}(e_mu) = g_mu = sum_a TH[a][mu] gamma_a, and
    om[c] = Omega(hb(gamma_c)), the rotation-gauge field along the physical frame vector gamma_c."""

    def __init__(self, TH, om):
        self.TH, self.om = TH, om
        self.g = [jvec([TH[a][mu] for a in range(4)]) for mu in range(4)]
        self.Om = [m_add(*[m_scal(TH[c][mu], om[c]) for c in range(4)]) for mu in range(4)]
        self.Hi = mat_inv([[TH[a][mu].v for mu in range(4)] for a in range(4)])

    def torsion_free(self):
        """D_{e_mu} g_nu - D_{e_nu} g_mu = 0 for all mu < nu (values)."""
        for mu in range(4):
            for nu in range(mu + 1, 4):
                t = m_add(m_d(self.g[nu], mu), m_scal(-1, m_d(self.g[mu], nu)),
                          m_comm(self.Om[mu], self.g[nu]), m_scal(-1, m_comm(self.Om[nu], self.g[mu])))
                if m_val(t):
                    return False
        return True

    def strength(self, mu, nu):
        """Background field strength R(e_mu ^ e_nu) (LDG sign), value."""
        t = m_add(m_d(self.Om[nu], mu), m_scal(-1, m_d(self.Om[mu], nu)), m_comm(self.Om[mu], self.Om[nu]))
        return m_val(t)

    def curvature(self):
        """The store's curvature operator on the physical frame planes,
        Rc[(a, b)] = calR(gamma_a ^ gamma_b) = -R(hb(gamma_a) ^ hb(gamma_b))."""
        Hi = self.Hi
        Rb = {(mu, nu): self.strength(mu, nu) for mu in range(4) for nu in range(4) if mu != nu}
        out = {}
        for a in range(4):
            for b in range(a + 1, 4):
                acc = {}
                for mu in range(4):
                    for nu in range(4):
                        c = Hi[mu][a] * Hi[nu][b]
                        if c and mu != nu:
                            acc = GA.add(acc, GA.scal(c, Rb[(mu, nu)]))
                out[(a, b)] = GA.neg(acc)
        return out


def omega_forms(spec):
    """om[c] = Omega(hb(gamma_c)) from connection forms: each (c, a, b, w) says that (gamma_c . D) gamma_b
    has component w along gamma_a (w = omega^a_b(gamma_c)); the bivector is sum_{a<b} omega^a_b eta_bb
    gamma_a gamma_b (metric compatibility fixes the partner component)."""
    om = [{} for _ in range(4)]
    for c, a, b, w in spec:
        if a < b:
            om[c] = m_add(om[c], {(a, b): w * ETA[b]})
        else:
            om[c] = m_add(om[c], {(b, a): -w * ETA[b]})
    return om


def static_field(r0, s0, c0, fdf):
    """Static spherically symmetric field, derived metric f dt^2 - dr^2/f - r^2 dOmega^2, labels
    (t, r, theta, phi), at the point r = r0, sin(theta) = s0, cos(theta) = c0; fdf(r) returns the jets
    (f, f'). sqrt(f(r0)) must be rational."""
    r = J.var(1, r0)
    f, fp = fdf(r)
    sf = f.pw(F(1, 2))
    sn, cs = sincos(2, s0, c0)
    TH = [[J(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][1], TH[2][2], TH[3][3] = sf, 1 / sf, r, r * sn
    om = omega_forms([(0, 0, 1, fp / (2 * sf)), (2, 2, 1, sf / r), (3, 3, 1, sf / r), (3, 3, 2, (cs / sn) / r)])
    return Field(TH, om)


def pg_field(r0, s0, c0, M):
    """Schwarzschild in the Painleve-Gullstrand gauge hb = 1 - beta P: coframe dt, dr + beta dt, r dtheta,
    r sin(theta) dphi, beta = sqrt(2M/r); connection forms from the Cartan equations
    (omega^0_1 = -beta' e^1, omega^i_0 = -(beta/r) e^i, omega^i_1 = e^i/r, omega^3_2 = cot e^3/r)."""
    r = J.var(1, r0)
    beta = (2 * M / r).pw(F(1, 2))
    sn, cs = sincos(2, s0, c0)
    TH = [[J(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][0], TH[1][1], TH[2][2], TH[3][3] = J(1), beta, J(1), r, r * sn
    dbeta = -beta / (2 * r)
    om = omega_forms([(1, 0, 1, -dbeta), (2, 0, 2, -beta / r), (3, 0, 3, -beta / r),
                      (2, 2, 1, 1 / r), (3, 3, 1, 1 / r), (3, 3, 2, (cs / sn) / r)])
    return Field(TH, om)


def ds_flat_field(H, E):
    """de Sitter in the flat slicing: hb^{-1}(e_t) = e_t, hb^{-1}(e_i) = e^{Ht} e_i, at a point where
    e^{Ht} = E; Omega(hb(gamma_i)) = -H gamma_0 ^ gamma_i (the GTG sign of the dictionary, C10)."""
    a = J(E, (H * E, 0, 0, 0))
    TH = [[J(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][1], TH[2][2], TH[3][3] = J(1), a, a, a
    om = [{}] + [{(0, i): J(-H)} for i in (1, 2, 3)]
    return Field(TH, om)


def fv(a):
    return GA.gen(a)


def fb(a, b):
    return GA.mul(GA.gen(a), GA.gen(b), S13)


def wedge13(u, v):
    return GA.scal(F(1, 2), GA.sub(GA.mul(u, v, S13), GA.mul(v, u, S13)))


def apply_op(Rc, B):
    """Extend calR linearly from the frame planes to a bivector B (Fraction coefficients)."""
    out = {}
    for (a, b), c in B.items():
        out = GA.add(out, GA.scal(c, Rc[(a, b)]))
    return out


def vdot_b(v, B):
    """v . B = (vB - Bv)/2 for a vector v and a bivector B."""
    return GA.scal(F(1, 2), GA.sub(GA.mul(v, B, S13), GA.mul(B, v, S13)))


def ricci(Rc, b):
    """calR(b) = sum_a gamma^a . calR(gamma_a ^ b) for a physical vector b (Fraction multivector)."""
    out = {}
    for a in range(4):
        out = GA.add(out, GA.scal(ETA[a], vdot_b(fv(a), apply_op(Rc, wedge13(fv(a), b)))))
    return out


def ricci_scalar(Rc):
    return sum(ETA[a] * GA.dot(fv(a), ricci(Rc, fv(a)), S13) for a in range(4))


def schouten(Rc):
    """P(a) = (calR(a) - a calR/6)/2 (four dimensions)."""
    R = ricci_scalar(Rc)
    return lambda a: GA.scal(F(1, 2), GA.sub(ricci(Rc, a), GA.scal(R / 6, a)))


# Cl(2,4): generators 0..3 as Cl(1,3), 4 = e+ (square +1), 5 = e- (square -1)
S24 = (1, -1, -1, -1, 1, -1)
N0 = GA.scal(F(1, 2), GA.add(GA.gen(4), GA.gen(5)))
NI = GA.sub(GA.gen(4), GA.gen(5))


def comm6(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S24), GA.mul(Y, X, S24)))


def dot6(a, b):
    return GA.dot(a, b, S24)


def tractor(sig, mu, rho):
    return GA.add(GA.scal(sig, NI), mu, GA.scal(rho, N0))


def slots(V):
    """(sigma, mu, rho) of V = sigma ninf + mu + rho n0."""
    return dot6(V, N0), {b: c for b, c in V.items() if len(b) == 1 and b[0] < 4}, dot6(V, NI)


def omega_T(fld, c, P):
    """Omega_T(hb(gamma_c)) = Omega(hb(gamma_c)) - ninf ^ gamma_c + n0 ^ P(gamma_c) in Cl(2,4)."""
    A = fv(c)
    return GA.add(m_val(fld.om[c]), GA.neg(comm6(NI, A)), comm6(N0, P(A)))


def dT_const(fld, c, P, V):
    """D^T along hb(gamma_c) of a constant tractor V: Omega_T x V."""
    return comm6(omega_T(fld, c, P), V)
# ---- end of engine ----
