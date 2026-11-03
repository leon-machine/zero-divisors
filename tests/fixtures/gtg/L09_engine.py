# ---- GTG engine (exact): first-order jets, multivectors with jet coefficients, torsion, field strength ----
S13 = GA.sig(1, 3)
NV = 4                                   # background labels x^0..x^3


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


# multivectors with jet coefficients: dict blade -> J
def m_add(*xs):
    out = {}
    for x in xs:
        for b, c in x.items():
            out[b] = out[b] + c if b in out else c
    return out


def m_scal(c, x):
    return {b: c * v for b, v in x.items()}


def m_mul(x, y):
    out = {}
    for b1, c1 in x.items():
        for b2, c2 in y.items():
            s, b = GA.blade_mul(b1, b2, S13)
            if s:
                t = c1 * c2 * s
                out[b] = out[b] + t if b in out else t
    return out


def m_comm(x, y):
    """Commutator product x X y = (xy - yx)/2."""
    return m_scal(F(1, 2), m_add(m_mul(x, y), m_scal(-1, m_mul(y, x))))


def m_d(x, i):
    return {b: c.d(i) for b, c in x.items()}


def m_val(x):
    return {b: c.v for b, c in x.items() if c.v != 0}


def vec(comps):
    return {(a,): c for a, c in enumerate(comps)}


def biv(pairs):
    """Bivector sum c * gamma_a gamma_b from {(a, b): c}, a < b."""
    return {(a, b): c for (a, b), c in pairs.items()}


class Field(object):
    """A gravitational field (hb, Omega) on flat spacetime in a gauge where the physical frame is the
    constant orthonormal frame gamma_a of Cl(1,3): hb^{-1}(e_mu) = g_mu = sum_a TH[a][mu] gamma_a, and
    om[c] = Omega(hb(gamma_c)), the rotation-gauge field along the physical frame vector gamma_c."""

    def __init__(self, TH, om):
        self.TH, self.om = TH, om
        self.g = [vec([TH[a][mu] for a in range(4)]) for mu in range(4)]
        self.Om = [m_add(*[m_scal(TH[c][mu], om[c]) for c in range(4)]) for mu in range(4)]

    def torsion(self, mu, nu):
        """D_{e_mu} g_nu - D_{e_nu} g_mu (value): zero for the torsion-free field."""
        t = m_add(m_d(self.g[nu], mu), m_scal(-1, m_d(self.g[mu], nu)),
                  m_comm(self.Om[mu], self.g[nu]), m_scal(-1, m_comm(self.Om[nu], self.g[mu])))
        return m_val(t)

    def torsion_free(self):
        return all(self.torsion(mu, nu) == {} for mu in range(4) for nu in range(mu + 1, 4))

    def strength(self, mu, nu):
        """Background field strength R(e_mu ^ e_nu) (LDG sign), value."""
        t = m_add(m_d(self.Om[nu], mu), m_scal(-1, m_d(self.Om[mu], nu)), m_comm(self.Om[mu], self.Om[nu]))
        return m_val(t)

    def hb_matrix(self):
        """Hi[mu][a]: hb(gamma_a) = sum_mu Hi[mu][a] e_mu (the inverse of the coframe matrix), values."""
        M = [[self.TH[a][mu].v for mu in range(4)] for a in range(4)]
        return mat_inv(M)

    def curvature(self):
        """The store's curvature operator on the physical frame planes, Rc[(a, b)] = calR(gamma_a ^ gamma_b)
        = -R(hb(gamma_a) ^ hb(gamma_b)) (Definition, item (c))."""
        Hi = self.hb_matrix()
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


def gvec(a):
    return GA.gen(a)


def gbiv(a, b):
    return GA.mul(GA.gen(a), GA.gen(b), S13)


def apply_op(Rc, B):
    """Extend calR linearly from the frame planes to a bivector B (Fraction coefficients)."""
    out = {}
    for (a, b), c in B.items():
        out = GA.add(out, GA.scal(c, Rc[(a, b)]))
    return out
ETA = [1, -1, -1, -1]


def omega_forms(spec):
    """om[c] = Omega(hb(gamma_c)) from connection forms: each (c, a, b, w) says that
    (gamma_c . D) gamma_b has component w along gamma_a (w = omega^a_b(gamma_c)); the bivector is
    sum_{a<b} omega^a_b eta_bb gamma_a gamma_b (metric compatibility fixes the partner component)."""
    om = [{} for _ in range(4)]
    for c, a, b, w in spec:
        if a < b:
            om[c] = m_add(om[c], {(a, b): w * ETA[b]})
        else:
            om[c] = m_add(om[c], {(b, a): -w * ETA[b]})
    return om


def field_cov(fld, A, V):
    """(A . D) V = D_{hb(A)} V for a constant-component physical vector A (list of 4 Fractions) and a
    physical vector field V (dict blade -> J); returns the value (Fraction multivector)."""
    Hi = fld.hb_matrix()
    out = m_add(*[m_scal(A[c], fld.om[c]) for c in range(4)]) if any(A) else {}
    res = m_val(m_comm(out, V)) if out else {}
    for mu in range(4):
        h = sum(Hi[mu][c] * A[c] for c in range(4))
        if h:
            res = GA.add(res, GA.scal(h, m_val(m_d(V, mu))))
    return res


def bdot(B, v):
    """B . v = (Bv - vB)/2 for a bivector B and a vector v (Fraction multivectors)."""
    return GA.scal(F(1, 2), GA.sub(GA.mul(B, v, S13), GA.mul(v, B, S13)))


def ricci(Rc, b):
    """calR(gamma_b) = sum_a gamma^a . calR(gamma_a ^ gamma_b) (left contraction: gamma^a . B = -B . gamma^a)."""
    out = {}
    for a in range(4):
        if a == b:
            continue
        Rab = Rc[(a, b)] if a < b else GA.neg(Rc[(b, a)])
        out = GA.add(out, GA.scal(F(-1) / ETA[a], bdot(Rab, GA.gen(a))))
    return out


def lie_dim(gens, sq):
    """Dimension of the Lie algebra generated by bivectors under the commutator."""
    blades = [(a, b) for a in range(4) for b in range(a + 1, 4)]

    def rank(xs):
        return GA.field_rank([[x.get(bl, F(0)) for bl in blades] for x in xs]) if xs else 0
    span = [g for g in gens if g]
    while True:
        new = span + [GA.scal(F(1, 2), GA.sub(GA.mul(a, b, sq), GA.mul(b, a, sq))) for a in span for b in span]
        if rank(new) == rank(span):
            return rank(span)
        basis = []
        for x in new:
            if rank(basis + [x]) > len(basis):
                basis.append(x)
        span = basis


def torsion_rank(fld):
    """Rank of the algebraic torsion map Omega -> (Omega_mu . g_nu - Omega_nu . g_mu) at the point (24 = injective:
    the torsion equation then fixes Omega uniquely)."""
    gv = [m_val(g) for g in fld.g]
    cols = []
    for mu in range(4):
        for bl in [(a, b) for a in range(4) for b in range(a + 1, 4)]:
            col = []
            for p in range(4):
                for q in range(p + 1, 4):
                    t = {}
                    if p == mu:
                        t = GA.add(t, bdot({bl: F(1)}, gv[q]))
                    if q == mu:
                        t = GA.sub(t, bdot({bl: F(1)}, gv[p]))
                    col.extend(t.get((a,), F(0)) for a in range(4))
            cols.append(col)
    return GA.field_rank([list(row) for row in zip(*cols)])


# ---- the Schwarzschild(-de Sitter) interior field in synchronous gauge, labels (r, t, theta, phi), 2M = 1 ----
def interior_field(r0, w, s0, c0):
    """hb^{-1}(e_r) = gamma0/sqrt(A), hb^{-1}(e_t) = sqrt(A) gamma1, hb^{-1}(e_theta) = r gamma2,
    hb^{-1}(e_phi) = r sin(theta) gamma3, A = (1 - r + (Lambda/3) r^3)/r with Lambda fixed by sqrt(A(r0)) = w
    (Lambda = 0 when w^2 = (1 - r0)/r0). Rotation-gauge field in the Definition's sign:
    Omega(e_i) = -sigma_i e_0 ^ e_i, plus (cot(theta)/r) e_2 ^ e_3 on e_3; sigma_1 = A'/(2 sqrt A),
    sigma_2 = sigma_3 = sqrt(A)/r. Returns (field, Lambda, jets)."""
    r0, w = F(r0), F(w)
    lam = 3 * (w * w * r0 - 1 + r0) / (r0 * r0 * r0)
    r = J.var(0, r0)
    A = (1 - r + (lam / 3) * r * r * r) / r
    sA = A.pw(F(1, 2))
    sn, cs = sincos(2, s0, c0)
    TH = [[J(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][1], TH[2][2], TH[3][3] = 1 / sA, sA, r, r * sn
    Ap = -1 / (r * r) + (2 * lam / 3) * r
    s1, s2 = Ap / (2 * sA), sA / r
    om = [{}, {(0, 1): -s1}, {(0, 2): -s2}, {(0, 3): -s2, (2, 3): cs / (sn * r)}]
    return Field(TH, om), lam, (r, A, sA, s1, s2, sn, cs)
# ---- end of engine ----
