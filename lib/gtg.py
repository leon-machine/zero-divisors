#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""gtg.py: Gauge Theory Gravity on flat spacetime, exact, with the store's conventions encoded once
(ROADMAP item 6). Section numbers C1-C11 and 1-16 refer to docs/gtg-dictionary.md.

Conventions (each is a decision recorded in DICTIONARY.md; change it here and nowhere else):

- C1, C16. Background: the vectors of Cl(1,3), signature (+,-,-,-) (GA.sig(1, 3) = S13); in d
  dimensions Cl(1, d-1) (lorentz_sig(d)), any diagonal signature accepted. Generators are GA.py
  generator indices: e(mu) = GA.gen(mu). Q(a) = a^2.
- C2. The gauge field hb acts on background vectors; the physical frame is a CONSTANT orthonormal
  frame gamma_a (the GA generators) and a field is given by its coframe matrix TH:
  hb^{-1}(e_mu) = g_mu = sum_a TH[a][mu] gamma_a, so the derived metric is g_mu . g_nu
  (the L12 engine's design; Field.TH, Field.g). Labels x^mu (t, r, theta, phi or Cartesian) are
  coordinates of the flat background only.
- C3. om[c] := Omega(hb(gamma_c)) (Omega along the physical frame vector gamma_c); Om[mu] :=
  Omega(e_mu) = sum_c TH[c][mu] om[c] (background components).
- C4. D_a M = a.grad M + Omega(a) x M with x the commutator product (AB - BA)/2 (comm()).
- C5. Background field strength (LDG sign) R(a ^ b) = a.grad Omega(b) - b.grad Omega(a)
  + Omega(a) x Omega(b) (Field.strength). Store curvature calR(B) := -R(hb(B)) (STORE_SIGN = -1,
  Field.curvature, on the physical frame planes gamma_a ^ gamma_b, a < b). Ricci
  calR(b) = d_a . calR(a ^ b), scalar calR = d_a . calR(a), Einstein G(a) = calR(a) - a calR/2.
- C6. Store sign: de Sitter calR(B) = (Lambda/3) B, calR(a) = Lambda a, scalar 4 Lambda;
  Schwarzschild calR(sigma_r) = +2M/r^3 sigma_r with sigma_r = e_r e_t (= gamma_1 gamma_0).
  Field equation G(a) + Lambda a = -8 pi T(a).
- C10. Omega is displayed in the GTG (left-action) sign: synchronous fields have
  Omega(gamma_i) = -H_i gamma_0 ^ gamma_i = -sigma_i B_i (B_i = e_0 ^ e_i); the Cartan right-action
  value is Omega_C = -Omega (omega_from_right_action).
- C11. Riem^o(u,v,w,z) = (w ^ z) . calR(u ^ v) (riem_o); R(u,v)w = -calR(u ^ v) . w as an
  endomorphism (riemann_endo_apply); C(k,a,k,b) = (k ^ b) . W(k ^ a) (weyl_null);
  Ric^o_{mu nu} = -g_mu . calR(g_nu) (ric_o).
- Section 5 and 16. Schouten P(a) = (calR(a) - a calR/(2(d-1)))/(d-2) (d = 4: (calR(a) - a calR/6)/2);
  Weyl W(a ^ b) = calR(a ^ b) - P(a) ^ b - a ^ P(b); Kretschmann 2 <calR(a ^ b) calR(d_b ^ d_a)>;
  de Sitter_d calR(B) = 2 Lambda B/((d-1)(d-2)).
- Section 11. Schwarzschild PG: hb = 1 - beta P, beta = sqrt(2M/r), hb^{-1}(e_t) = e_t + beta e_r;
  de Sitter static PG chart beta = -rH (expanding); flat-slicing de Sitter
  hb^{-1}(e_i) = e^{Ht} e_i, Omega(gamma_i) = -H B_i; Kasner hb^{-1}(e_i) = t^{p_i} e_i;
  Kerr-Schild hb^{-1}(a) = a - H (a.k) k, Q(k) = 0 (g = eta - 2H k k).
- Section 12 (with referee GR2's fix). Conformal model Cl(2,4) = Cl(1,3) + plane {e+, e-}:
  generators 0..3 spacetime, 4 = e+ (square +1), 5 = e- (square -1) (S24); n0 = (e+ + e-)/2,
  ninf = e+ - e-, n0 . ninf = 1; tractor sigma ninf + mu + rho n0; canonical tractor X = n0
  (the parabolic subgroup stabilises the line of n0); X(x) = n0 + x - Q(x)/2 ninf;
  Omega_T(a) = Omega(a) - ninf ^ hb^{-1}(a) + n0 ^ P(hb^{-1}(a)); scale tractor
  I = ninf + (Lambda/6) n0 (Q(I) = Lambda/3; d dims: ninf + Lambda/((d-1)(d-2)) n0).

Jets (exactness at rational points): a Jet is a truncated multivariate Taylor polynomial in the
labels about a rational point (order 1 = the L12 engine's value-and-gradient jet; higher orders
give curvature jets and the tractor field strength). Irrational values (sqrt(2M/r)) are avoided by
choosing points where they are rational, or supplied in an exact extension (series.QS) through
Jet.pw(a, val=...). Pure functions; no I/O at import; Brython-safe (no dict.setdefault).
"""

from fractions import Fraction

import GA
import series

F = Fraction
NV = 4                      # default number of background labels
S13 = GA.sig(1, 3)          # (+,-,-,-)
ETA = S13
STORE_SIGN = -1             # C5: calR(B) = STORE_SIGN * R(hb(B)); the GTG literature (LDG) uses +1
RIC_O_SIGN = -1             # C6/C11: Ric^o = RIC_O_SIGN * (store Ricci); Ric^o_{mu nu} = -g_mu . calR(g_nu)
OMEGA_SIGN_DISPLAYED = +1   # C10: the store displays Omega in the GTG (left-action) sign


def lorentz_sig(d):
    """Signature tuple (+,-,...,-) of Cl(1, d-1)."""
    return GA.sig(1, d - 1)


def _num(x):
    if isinstance(x, (int, Fraction)) and not isinstance(x, bool):
        return F(x)
    if isinstance(x, bool):
        return F(int(x))
    return x


def _omin(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return a if a < b else b


def _unit(i, nv):
    return tuple(1 if k == i else 0 for k in range(nv))


# ---------------------------------------------------------------------------
# 1. jets: truncated multivariate Taylor polynomials about a rational point
# ---------------------------------------------------------------------------

class Jet(object):
    """Truncated Taylor polynomial in nv labels: coefficients {exponent tuple: exact number}."""
    __slots__ = ("c", "nv", "order")

    def __init__(self, v=0, g=None, nv=None, order=None, c=None):
        nv = NV if nv is None else nv
        self.nv = nv
        if c is not None:
            self.c, self.order = c, order
            return
        z = (0,) * nv
        cc = {}
        v = _num(v)
        if v:
            cc[z] = v
        if g is not None:
            for i, x in enumerate(g):
                x = _num(x)
                if x:
                    cc[_unit(i, nv)] = x
            self.order = 1 if order is None else order
        else:
            self.order = order          # None: an exact constant (infinite order)
        self.c = cc

    @staticmethod
    def var(i, x0, nv=None, order=1):
        """The label x^i as a jet about x^i = x0."""
        nv = NV if nv is None else nv
        j = Jet(x0, None, nv, order)
        if order is None or order >= 1:
            j.c[_unit(i, nv)] = F(1)
        return j

    @staticmethod
    def const(v, nv=None):
        """An exact constant jet."""
        return Jet(v, None, nv, None)

    @staticmethod
    def from_taylor(i, coeffs, nv=None):
        """The one-variable jet sum coeffs[k] (x^i - x^i_0)^k, order len(coeffs) - 1."""
        nv = NV if nv is None else nv
        cc = {}
        for k, x in enumerate(coeffs):
            x = _num(x)
            if x:
                cc[tuple(k if m == i else 0 for m in range(nv))] = x
        return Jet(c=cc, nv=nv, order=len(coeffs) - 1)

    # -- access ------------------------------------------------------------
    @property
    def v(self):
        """The value at the point."""
        return self.c.get((0,) * self.nv, F(0))

    @property
    def g(self):
        """The gradient (first partial derivatives) at the point, a tuple."""
        return tuple(self.c.get(_unit(i, self.nv), F(0)) for i in range(self.nv))

    def coeff(self, e):
        """Taylor coefficient of the monomial with exponent tuple e."""
        return self.c.get(tuple(e), F(0))

    def is_const(self):
        """True when only the constant term can be nonzero."""
        z = (0,) * self.nv
        return all(k == z for k in self.c)

    def trunc(self, order):
        """The jet truncated to the given order."""
        order = _omin(self.order, order)
        cc = {e: x for e, x in self.c.items() if order is None or sum(e) <= order}
        return Jet(c=cc, nv=self.nv, order=order)

    def d(self, i):
        """Partial derivative along label i (order drops by one)."""
        if self.order is not None and self.order < 1:
            raise ValueError("Jet.d: derivative beyond the jet's order")
        cc = {}
        for e, x in self.c.items():
            if e[i]:
                f = list(e)
                f[i] -= 1
                cc[tuple(f)] = x * e[i]
        return Jet(c=cc, nv=self.nv, order=None if self.order is None else self.order - 1)

    # -- arithmetic ----------------------------------------------------------
    def _co(self, o):
        if isinstance(o, Jet):
            if o.nv == self.nv:
                return o
            if o.is_const():
                return Jet(o.v, None, self.nv, o.order)
            raise ValueError("Jet: mismatched numbers of labels")
        return Jet(o, None, self.nv, None)

    def _me(self, o):
        if isinstance(o, Jet) and o.nv != self.nv and self.is_const():
            return Jet(self.v, None, o.nv, self.order)
        return self

    def __add__(self, o):
        s = self._me(o)
        o = s._co(o)
        order = _omin(s.order, o.order)
        cc = dict(s.c)
        for e, x in o.c.items():
            y = cc.get(e, 0) + x
            if y:
                cc[e] = y
            elif e in cc:
                del cc[e]
        if order is not None:
            cc = {e: x for e, x in cc.items() if sum(e) <= order}
        return Jet(c=cc, nv=s.nv, order=order)

    __radd__ = __add__

    def __neg__(self):
        return Jet(c={e: -x for e, x in self.c.items()}, nv=self.nv, order=self.order)

    def __sub__(self, o):
        return self + (-self._me(o)._co(o))

    def __rsub__(self, o):
        return self._co(o) - self

    def __mul__(self, o):
        if not isinstance(o, Jet):
            o = _num(o)
            if not o:
                return Jet(c={}, nv=self.nv, order=self.order)
            return Jet(c={e: x * o for e, x in self.c.items()}, nv=self.nv, order=self.order)
        s = self._me(o)
        o = s._co(o)
        order = _omin(s.order, o.order)
        cc = {}
        oi = [(e2, sum(e2), x2) for e2, x2 in o.c.items()]
        for e1, x1 in s.c.items():
            d1 = sum(e1)
            for e2, d2, x2 in oi:
                if order is not None and d1 + d2 > order:
                    continue
                e = tuple(a + b for a, b in zip(e1, e2))
                y = cc.get(e, 0) + x1 * x2
                if y:
                    cc[e] = y
                elif e in cc:
                    del cc[e]
        return Jet(c=cc, nv=s.nv, order=order)

    def __rmul__(self, o):
        return self.__mul__(o)

    def _apply(self, coeffs):
        """sum coeffs[k] (self - value)^k, k up to the order (coeffs: callable k -> number)."""
        v = self.v
        h = self - v
        out = Jet(coeffs(0), None, self.nv, self.order)
        if self.order is None:
            if not h.c:
                return Jet.const(coeffs(0), self.nv)
            raise ValueError("Jet: non-constant jet of infinite order")
        p = Jet(1, None, self.nv, self.order)
        for k in range(1, self.order + 1):
            p = p * h
            if not p.c:
                break
            out = out + p * coeffs(k)
        return out

    def inv(self):
        """1/self (value must be nonzero)."""
        v = self.v
        if not v:
            raise ZeroDivisionError("Jet.inv at a zero value")
        iv = 1 / v
        pw = [iv]

        def cf(k):
            while len(pw) <= k:
                pw.append(-pw[-1] * iv)
            return pw[k]
        return self._apply(cf)

    def __truediv__(self, o):
        if isinstance(o, Jet):
            s = self._me(o)
            return s * s._co(o).inv()
        o = _num(o)
        return self * (1 / o)

    def __rtruediv__(self, o):
        return self._co(o) * self.inv()

    def pw(self, a, val=None):
        """self ** a for rational a; val = the exact value**a (default: series.qpow, rational)."""
        a = F(a)
        v = self.v
        if val is None:
            val = series.qpow(v, a)
        iv = 1 / v
        bc = series.taylor_binomial(a, self.order if self.order is not None else 0)

        def cf(k):
            return val * bc[k] * iv ** k
        return self._apply(cf)

    def sqrt(self, val=None):
        """self ** (1/2) (rational value, or val supplied in an extension)."""
        return self.pw(F(1, 2), val)

    def __pow__(self, n):
        if isinstance(n, int):
            if n < 0:
                return self.inv() ** (-n)
            out = Jet(1, None, self.nv, None)
            base = self
            while n:
                if n & 1:
                    out = out * base
                n >>= 1
                if n:
                    base = base * base
            return out
        return self.pw(n)

    def __eq__(self, o):
        if not isinstance(o, Jet):
            try:
                o = self._co(o)
            except (TypeError, ValueError):
                return NotImplemented
        s = self._me(o)
        o = s._co(o)
        keys = set(s.c) | set(o.c)
        return all(s.c.get(k, 0) == o.c.get(k, 0) for k in keys)

    def __ne__(self, o):
        r = self.__eq__(o)
        return r if r is NotImplemented else not r

    __hash__ = None

    def __bool__(self):
        return any(bool(x) for x in self.c.values())

    __nonzero__ = __bool__

    def __repr__(self):
        return "Jet(order=%s, %s)" % (self.order, dict(self.c))


J = Jet                      # the engines' name


def jvar(i, x0, nv=None, order=1):
    """The label x^i as a jet about x0 (Jet.var)."""
    return Jet.var(i, x0, nv, order)


def jexp(x, E):
    """exp(x) for a jet x, given the exact value E = exp(x.v)."""
    e = series.taylor_exp(x.order if x.order is not None else 0)
    return x._apply(lambda k: E * e[k])


def jsincos(x, s0, c0):
    """(sin x, cos x) for a jet x, given s0 = sin(x.v), c0 = cos(x.v) (s0^2 + c0^2 = 1)."""
    K = x.order if x.order is not None else 0
    s, c = series.taylor_sin(K), series.taylor_cos(K)
    return (x._apply(lambda k: s0 * c[k] + c0 * s[k]), x._apply(lambda k: c0 * c[k] - s0 * s[k]))


def sincos(i, s0, c0, nv=None, order=1):
    """sin and cos of the label x^i at a point with sin = s0, cos = c0 (the engines' sincos)."""
    nv = NV if nv is None else nv
    return jsincos(Jet.var(i, F(0), nv, order), s0, c0)


def _val(x):
    """The value of a jet (this library's or any object with a .v value), else x itself."""
    if isinstance(x, Jet):
        return x.v
    return x.v if hasattr(x, "v") and hasattr(x, "g") else x


def _jc(x, nv):
    return x if isinstance(x, Jet) else Jet(x, None, nv, None)


# ---------------------------------------------------------------------------
# 2. multivectors with exact (or jet) coefficients: dict {blade tuple: coefficient}
# ---------------------------------------------------------------------------

def e(mu):
    """Background frame vector e_mu (= the physical frame vector gamma_mu): GA.gen(mu)."""
    return GA.gen(mu)


def er(mu, sq=S13):
    """Reciprocal frame vector e^mu = e_mu / Q(e_mu)."""
    return {(mu,): F(1, sq[mu])}


def vec(comps):
    """Vector sum comps[a] gamma_a (jets or numbers; zero entries dropped)."""
    return {(a,): _num(c) for a, c in enumerate(comps) if c}


def biv(a, b, sq=S13):
    """The bivector gamma_a gamma_b (a != b), as a GA blade with its sign (the engines' fb/gbiv)."""
    return GA.mul(GA.gen(a), GA.gen(b), sq)


def m_add(*xs):
    """Sum of multivectors (any exact or jet coefficients), zero terms dropped."""
    out = {}
    for x in xs:
        for b, c in x.items():
            out[b] = out[b] + c if b in out else c
    return {b: c for b, c in out.items() if c}


def m_neg(x):
    """-x."""
    return {b: -c for b, c in x.items()}


def m_sub(x, y):
    """x - y."""
    return m_add(x, m_neg(y))


def m_scal(c, x):
    """c x for a scalar c (number or jet)."""
    c = _num(c)
    out = {}
    for b, v in x.items():
        t = c * v
        if t:
            out[b] = t
    return out


def m_mul(x, y, sq=S13):
    """Geometric product with GA.blade_mul (coefficients may be jets, QI, QS)."""
    out = {}
    for b1, c1 in x.items():
        for b2, c2 in y.items():
            s, b = GA.blade_mul(b1, b2, sq)
            if s:
                t = c1 * c2 * s
                out[b] = out[b] + t if b in out else t
    return {b: c for b, c in out.items() if c}


def comm(x, y, sq=S13):
    """Commutator product x X y = (xy - yx)/2 (C4)."""
    return m_scal(F(1, 2), m_sub(m_mul(x, y, sq), m_mul(y, x, sq)))


m_comm = comm


def sym(x, y, sq=S13):
    """Symmetrised product (xy + yx)/2."""
    return m_scal(F(1, 2), m_add(m_mul(x, y, sq), m_mul(y, x, sq)))


def wedge(a, b, sq=S13):
    """Outer product a ^ b of two vectors (= their commutator product)."""
    return comm(a, b, sq)


def grade(x, k):
    """Grade-k part."""
    return {b: c for b, c in x.items() if len(b) == k}


def outer(x, y, sq=S13):
    """Outer product of multivectors: the grade r + s part of each blade product."""
    out = {}
    for b1, c1 in x.items():
        for b2, c2 in y.items():
            s, b = GA.blade_mul(b1, b2, sq)
            if s and len(b) == len(b1) + len(b2):
                t = c1 * c2 * s
                out[b] = out[b] + t if b in out else t
    return {b: c for b, c in out.items() if c}


def sp(x):
    """Scalar part <x>_0."""
    return x.get((), F(0))


def vdot(a, b, sq=S13):
    """Scalar product of vectors a . b = <ab>_0 (any coefficients)."""
    return sp(sym(a, b, sq))


def inner_vb(a, B, sq=S13):
    """a . B = (aB - Ba)/2 for a vector a and a bivector B (a vector)."""
    return grade(comm(a, B, sq), 1)


def bdot(B, a, sq=S13):
    """B . a = (Ba - aB)/2 = -a . B for a bivector B and a vector a."""
    return grade(comm(B, a, sq), 1)


def bb_dot(X, Y, sq=S13):
    """Scalar <XY>_0 of two bivectors (the C11 pairing (w ^ z) . calR(u ^ v))."""
    return sp(m_mul(X, Y, sq))


def m_d(x, i):
    """Partial derivative along label i of a multivector with jet coefficients."""
    out = {}
    for b, c in x.items():
        if isinstance(c, Jet):
            t = c.d(i)
            if t:
                out[b] = t
    return out


def m_val(x):
    """Values at the point of a multivector with jet coefficients (zero terms dropped)."""
    out = {}
    for b, c in x.items():
        v = _val(c)
        if v:
            out[b] = v
    return out


def m_rev(x):
    """Reversion of a multivector (any coefficients)."""
    return {b: (c if (len(b) * (len(b) - 1) // 2) % 2 == 0 else -c) for b, c in x.items()}


def pseudoscalar(sq=S13):
    """Unit pseudoscalar gamma_0 gamma_1 ... gamma_{d-1}."""
    return {tuple(range(len(sq))): F(1)}


def cdot(u, v, sq=S13):
    """Complex-bilinear product of complex vectors given as (re, im) pairs, as GA.QI (T13 ip)."""
    return GA.QI(vdot(u[0], v[0], sq) - vdot(u[1], v[1], sq), vdot(u[0], v[1], sq) + vdot(u[1], v[0], sq))


def cbdot(B, v, sq=S13):
    """Complex bivector (re, im) dotted with a complex vector (re, im): B . v (T13 cbdot)."""
    return (m_sub(bdot(B[0], v[0], sq), bdot(B[1], v[1], sq)), m_add(bdot(B[0], v[1], sq), bdot(B[1], v[0], sq)))


def bivector_blades(n):
    """The basis bivector blades (a, b), a < b, of n generators."""
    return [(a, b) for a in range(n) for b in range(a + 1, n)]


# ---------------------------------------------------------------------------
# 3. exact linear algebra over rings with a value map (jets) or fields
# ---------------------------------------------------------------------------

def _inv(x):
    return x.inv() if isinstance(x, Jet) else 1 / x


def mat_inv(M):
    """Exact inverse of a square matrix of numbers or jets (pivots chosen by nonzero value)."""
    n = len(M)
    A = [[_num(x) for x in row] + [F(1) if i == j else F(0) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next((r for r in range(c, n) if _val(A[r][c])), None)
        if p is None:
            raise ZeroDivisionError("mat_inv: singular at the point")
        A[c], A[p] = A[p], A[c]
        piv = _inv(A[c][c])
        A[c] = [x * piv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c]:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def ring_solve(M, rhs):
    """Solve M x = rhs exactly (numbers or jets; M invertible at the point)."""
    n = len(M)
    A = [[_num(x) for x in M[i]] + [_num(rhs[i])] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if _val(A[r][c])), None)
        if p is None:
            raise ZeroDivisionError("ring_solve: singular at the point")
        A[c], A[p] = A[p], A[c]
        piv = _inv(A[c][c])
        A[c] = [x * piv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c]:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [A[i][n] for i in range(n)]


# ---------------------------------------------------------------------------
# 4. the gravitational field (hb, Omega)
# ---------------------------------------------------------------------------

def omega_forms(spec, sq=S13):
    """om[c] = Omega(hb(gamma_c)) from connection forms: each (c, a, b, w) says (gamma_c . D) gamma_b has
    component w along gamma_a (w = omega^a_b(gamma_c)); metric compatibility fixes the partner (L12)."""
    om = [{} for _ in range(len(sq))]
    for c, a, b, w in spec:
        if a < b:
            om[c] = m_add(om[c], {(a, b): w * sq[b]})
        else:
            om[c] = m_add(om[c], {(b, a): -w * sq[b]})
    return om


def omega_from_right_action(Om_C):
    """C10: the GTG (displayed) value Omega = -Omega_C from a right-action (Cartan) value Omega_C."""
    return m_neg(Om_C)


class Field(object):
    """Gravitational field (hb, Omega): hb^{-1}(e_mu) = sum_a TH[a][mu] gamma_a, om[c] = Omega(hb(gamma_c));
    om (or background Om) given, else solved from the torsion-free condition (C2-C4)."""

    def __init__(self, TH, om=None, sq=None, Om=None):
        sq = S13 if sq is None else tuple(sq)
        d = len(sq)
        self.sq, self.d = sq, d
        self.TH = [[_jc(TH[a][mu], d) for mu in range(d)] for a in range(d)]
        self.g = [{(a,): self.TH[a][mu] for a in range(d) if self.TH[a][mu]} for mu in range(d)]
        self._Hi, self._HiJ = None, None
        if om is not None:
            self.om = [{b: _jc(c, d) for b, c in om[k].items()} for k in range(d)]
            self.Om = [m_add(*[m_scal(self.TH[c][mu], self.om[c]) for c in range(d)]) for mu in range(d)]
        else:
            if Om is None:
                Om = solve_omega(self.g, sq)
            self.Om = [{b: _jc(c, d) for b, c in Om[k].items()} for k in range(d)]
            HJ = self.hb_matrix_jet()
            self.om = [m_add(*[m_scal(HJ[mu][c], self.Om[mu]) for mu in range(d)]) for c in range(d)]

    # -- hb and its inverse ----------------------------------------------------
    def hb_matrix(self):
        """Hi[mu][a] (values): hb(gamma_a) = sum_mu Hi[mu][a] e_mu, the inverse of the coframe matrix."""
        if self._Hi is None:
            self._Hi = mat_inv([[self.TH[a][mu].v for mu in range(self.d)] for a in range(self.d)])
        return self._Hi

    @property
    def Hi(self):
        """hb_matrix() (the L12 attribute)."""
        return self.hb_matrix()

    def hb_matrix_jet(self):
        """hb_matrix() as jets (same jet order as TH)."""
        if self._HiJ is None:
            self._HiJ = mat_inv([[self.TH[a][mu] for mu in range(self.d)] for a in range(self.d)])
        return self._HiJ

    def hb_inv(self, a):
        """Physical vector hb^{-1}(a) (values) of a background vector a (dict on e_mu)."""
        return m_val(m_add(*[m_scal(c, self.g[b[0]]) for b, c in a.items()]))

    def hb(self, A):
        """Background vector hb(A) (values) of a physical vector A (dict on gamma_a)."""
        Hi = self.hb_matrix()
        out = {}
        for b, c in A.items():
            out = m_add(out, {(mu,): c * Hi[mu][b[0]] for mu in range(self.d) if Hi[mu][b[0]]})
        return out

    def metric(self):
        """Derived metric g_mu nu = g_mu . g_nu (values)."""
        gv = [m_val(x) for x in self.g]
        return [[vdot(gv[m], gv[n], self.sq) for n in range(self.d)] for m in range(self.d)]

    def omega(self, c):
        """Omega(hb(gamma_c)) (value)."""
        return m_val(self.om[c])

    def Omega(self, mu):
        """Omega(e_mu) (value)."""
        return m_val(self.Om[mu])

    # -- covariant derivative, torsion -------------------------------------
    def cov(self, mu, M):
        """D_{e_mu} M = d_mu M + Omega(e_mu) x M (value) for M with jet coefficients (C4)."""
        return m_val(m_add(m_d(M, mu), comm(self.Om[mu], M, self.sq)))

    def cov_phys(self, A, V):
        """(A . D) V = D_{hb(A)} V (value) for constant physical components A (list) and a jet field V."""
        Hi = self.hb_matrix()
        d = self.d
        Oa = m_add(*[m_scal(A[c], self.om[c]) for c in range(d) if A[c]])
        res = m_val(comm(Oa, V, self.sq)) if Oa else {}
        for mu in range(d):
            h = sum((Hi[mu][c] * A[c] for c in range(d)), F(0))
            if h:
                res = m_add(res, m_scal(h, m_val(m_d(V, mu))))
        return res

    def torsion(self, mu, nu):
        """D_{e_mu} g_nu - D_{e_nu} g_mu (value): zero for the torsion-free field."""
        t = m_add(m_d(self.g[nu], mu), m_neg(m_d(self.g[mu], nu)),
                  comm(self.Om[mu], self.g[nu], self.sq), m_neg(comm(self.Om[nu], self.g[mu], self.sq)))
        return m_val(t)

    def torsion_free(self):
        """True when every torsion component vanishes at the point."""
        return all(self.torsion(mu, nu) == {} for mu in range(self.d) for nu in range(mu + 1, self.d))

    def torsion_rank(self):
        """Rank of the algebraic torsion map Omega -> Omega_mu . g_nu - Omega_nu . g_mu (d^2(d-1)/2 = injective)."""
        gv = [m_val(x) for x in self.g]
        return GA.field_rank(_torsion_matrix(gv, self.sq))

    # -- field strength and curvature ---------------------------------------
    def strength_jet(self, mu, nu):
        """Background field strength R(e_mu ^ e_nu) (LDG sign) as jets (C5)."""
        return m_add(m_d(self.Om[nu], mu), m_neg(m_d(self.Om[mu], nu)), comm(self.Om[mu], self.Om[nu], self.sq))

    def strength(self, mu, nu):
        """Background field strength R(e_mu ^ e_nu) (LDG sign), value."""
        return m_val(self.strength_jet(mu, nu))

    def curvature(self):
        """Store curvature on the frame planes: Rc[(a, b)] = calR(gamma_a ^ gamma_b) = -R(hb(gamma_a) ^ hb(gamma_b))."""
        Hi, d = self.hb_matrix(), self.d
        Rb = {}
        for mu in range(d):
            for nu in range(mu + 1, d):
                Rb[(mu, nu)] = self.strength(mu, nu)
        out = {}
        for a in range(d):
            for b in range(a + 1, d):
                acc = {}
                for mu in range(d):
                    for nu in range(mu + 1, d):
                        c = Hi[mu][a] * Hi[nu][b] - Hi[nu][a] * Hi[mu][b]
                        if c and Rb[(mu, nu)]:
                            acc = m_add(acc, m_scal(c, Rb[(mu, nu)]))
                out[(a, b)] = m_scal(STORE_SIGN, acc)
        return out

    def curvature_jet(self):
        """curvature() as jets (needs om of order >= 1 beyond what is consumed; order of om minus one)."""
        HJ, d = self.hb_matrix_jet(), self.d
        Rb = {}
        for mu in range(d):
            for nu in range(mu + 1, d):
                Rb[(mu, nu)] = self.strength_jet(mu, nu)
        out = {}
        for a in range(d):
            for b in range(a + 1, d):
                acc = {}
                for mu in range(d):
                    for nu in range(mu + 1, d):
                        if Rb[(mu, nu)]:
                            c = HJ[mu][a] * HJ[nu][b] - HJ[nu][a] * HJ[mu][b]
                            if c:
                                acc = m_add(acc, m_scal(c, Rb[(mu, nu)]))
                out[(a, b)] = m_scal(STORE_SIGN, acc)
        return out


def _torsion_matrix(gv, sq):
    """Columns: unknowns (mu, blade); rows: torsion components (mu < nu, a)."""
    d = len(sq)
    bl = bivector_blades(d)
    rows = []
    for p in range(d):
        for q in range(p + 1, d):
            for a in range(d):
                row = []
                for mu in range(d):
                    for b in bl:
                        t = {}
                        if p == mu:
                            t = m_add(t, bdot({b: F(1)}, gv[q], sq))
                        if q == mu:
                            t = m_sub(t, bdot({b: F(1)}, gv[p], sq))
                        row.append(t.get((a,), F(0)))
                rows.append(row)
    return rows


def solve_omega(g, sq=S13):
    """Background Omega(e_mu) solved exactly from the torsion-free condition D_mu g_nu = D_nu g_mu (jets)."""
    d = len(sq)
    bl = bivector_blades(d)
    nb = len(bl)
    A = _torsion_matrix(g, sq)
    rhs = []
    for p in range(d):
        for q in range(p + 1, d):
            t = m_sub(m_d(g[q], p), m_d(g[p], q))
            for a in range(d):
                rhs.append(-t.get((a,), F(0)))
    sol = ring_solve(A, rhs)
    return [{bl[j]: sol[mu * nb + j] for j in range(nb) if sol[mu * nb + j]} for mu in range(d)]


def field_from_hbinv(hbinv, x0, sq=S13, order=1, om=None):
    """Field from hbinv(X) -> rows g[mu][a] = TH[a][mu] (X: label jets of order order + 1 about x0);
    om(X) optional (else solved from torsion)."""
    d = len(sq)
    X = [Jet.var(i, x0[i], d, order + 1) for i in range(d)]
    rows = hbinv(X)
    TH = [[_jc(rows[mu][a], d) for mu in range(d)] for a in range(d)]
    return Field(TH, om(X) if om is not None else None, sq)


# ---------------------------------------------------------------------------
# 5. curvature operators: contractions, Schouten, Weyl, invariants (C5, C6, sections 5, 16)
# ---------------------------------------------------------------------------

def apply_op(Rc, B):
    """Extend a frame-plane operator {(a, b): calR(gamma_a ^ gamma_b)} linearly to a bivector B."""
    out = {}
    for (a, b), c in B.items():
        out = m_add(out, m_scal(c, Rc[(a, b)]))
    return out


def as_op(R):
    """A callable B -> calR(B) from a frame-plane dict or a callable."""
    if callable(R):
        return R
    return lambda B: apply_op(R, B)


def op_const(c):
    """The operator B -> c B (de Sitter: c = Lambda/3 in the store sign)."""
    return lambda B: m_scal(c, B)


def op_type_d(c, sigma, sq=S13):
    """The operator B -> c (B + 3 sigma B sigma) (Schwarzschild, store sign: c = M/(2 r^3), sigma = sigma_r)."""
    return lambda B: m_scal(c, m_add(B, m_scal(3, m_mul(m_mul(sigma, B, sq), sigma, sq))))


def op_kn(T, sq=S13):
    """Kulkarni-Nomizu operator B -> T(a) ^ b + a ^ T(b) on a ^ b, T a linear map of vectors."""
    d = len(sq)

    def R(B):
        out = {}
        for (m, n), c in B.items():
            em, en = GA.gen(m), GA.gen(n)
            out = m_add(out, m_scal(c, m_add(wedge(T(em), en, sq), wedge(em, T(en), sq))))
        return out
    return R


def op_add(*Rs):
    """Sum of curvature operators."""
    Rs = [as_op(R) for R in Rs]
    return lambda B: m_add(*[R(B) for R in Rs])


def op_planes(R, sq=S13):
    """The frame-plane dict {(a, b): R(gamma_a ^ gamma_b)} of an operator."""
    R = as_op(R)
    d = len(sq)
    return {(a, b): R({(a, b): F(1)}) for a in range(d) for b in range(a + 1, d)}


def store_from_ldg(R_ldg):
    """C6: the store-sign operator -R_LDG from an operator in the literature's sign."""
    R = as_op(R_ldg)
    return lambda B: m_scal(STORE_SIGN, R(B))


def ricci(R, b, sq=S13):
    """calR(b) = d_a . calR(a ^ b) for a physical vector b (C5)."""
    R = as_op(R)
    d = len(sq)
    out = {}
    for m in range(d):
        Rm = R(wedge(GA.gen(m), b, sq))
        if Rm:
            out = m_add(out, inner_vb(er(m, sq), Rm, sq))
    return out


def ricci_scalar(R, sq=S13):
    """calR = d_a . calR(a)."""
    d = len(sq)
    return sum((vdot(er(m, sq), ricci(R, GA.gen(m), sq), sq) for m in range(d)), F(0))


def einstein(R, a, sq=S13):
    """calG(a) = calR(a) - a calR/2."""
    return m_sub(ricci(R, a, sq), m_scal(ricci_scalar(R, sq) / 2, a))


def einstein_residual(R, a, lam=0, sq=S13):
    """calG(a) + Lambda a: zero for a vacuum solution with cosmological constant Lambda (C6)."""
    return m_add(einstein(R, a, sq), m_scal(lam, a))


def schouten(R, sq=S13):
    """The Schouten map P(a) = (calR(a) - a calR/(2(d-1)))/(d-2) as a callable (d >= 3)."""
    d = len(sq)
    sc = ricci_scalar(R, sq)
    return lambda a: m_scal(F(1, d - 2), m_sub(ricci(R, a, sq), m_scal(sc / (2 * (d - 1)), a)))


def weyl(R, a, b, sq=S13):
    """W(a ^ b) = calR(a ^ b) - P(a) ^ b - a ^ P(b)."""
    P = schouten(R, sq)
    return m_sub(as_op(R)(wedge(a, b, sq)), m_add(wedge(P(a), b, sq), wedge(a, P(b), sq)))


def weyl_op(R, sq=S13):
    """The Weyl operator as a frame-plane dict."""
    d = len(sq)
    P = schouten(R, sq)
    R = as_op(R)
    out = {}
    for a in range(d):
        for b in range(a + 1, d):
            ea, eb = GA.gen(a), GA.gen(b)
            out[(a, b)] = m_sub(R({(a, b): F(1)}), m_add(wedge(P(ea), eb, sq), wedge(ea, P(eb), sq)))
    return out


def kretschmann(R, sq=S13):
    """2 <calR(a ^ b) calR(d_b ^ d_a)> (48 M^2/r^6 on Schwarzschild)."""
    R = as_op(R)
    d = len(sq)
    tot = F(0)
    for m in range(d):
        for n in range(d):
            if m != n:
                tot = tot + sp(m_mul(R(wedge(GA.gen(m), GA.gen(n), sq)), R(wedge(er(n, sq), er(m, sq), sq)), sq))
    return 2 * tot


def ricci_sq(R, sq=S13):
    """calR(d_a) . calR(a) (R_ab R^ab)."""
    d = len(sq)
    return sum((vdot(ricci(R, GA.gen(m), sq), ricci(R, er(m, sq), sq), sq) for m in range(d)), F(0))


def euler_density(R, sq=S13):
    """Kretschmann - 4 Ric^2 + calR^2 (section 13; sign-independent)."""
    return kretschmann(R, sq) - 4 * ricci_sq(R, sq) + ricci_scalar(R, sq) ** 2


def ricci_flat(R, sq=S13):
    """True when calR(a) = 0 for every frame vector."""
    return all(not ricci(R, GA.gen(m), sq) for m in range(len(sq)))


# ---------------------------------------------------------------------------
# 6. sign identifications (C6, C10, C11)
# ---------------------------------------------------------------------------

def riem_o(R, u, v, w, z, sq=S13):
    """C11: Riem^o(u, v, w, z) = (w ^ z) . calR(u ^ v), the round-sphere-positive Riemann tensor."""
    return bb_dot(wedge(w, z, sq), as_op(R)(wedge(u, v, sq)), sq)


def riemann_endo(R, u, v, sq=S13):
    """C11: the Riemann endomorphism R(u, v) as the bivector -calR(u ^ v)."""
    return m_neg(as_op(R)(wedge(u, v, sq)))


def riemann_endo_apply(R, u, v, w, sq=S13):
    """C11: R(u, v) w = (-calR(u ^ v)) . w; then <R(u, v) w, z> = Riem^o(z, w, u, v)."""
    return bdot(riemann_endo(R, u, v, sq), w, sq)


def ric_o(R, u, v, sq=S13):
    """C11 (G2): Ric^o(u, v) = -u . calR(v), the round-sphere-positive Ricci tensor."""
    return RIC_O_SIGN * vdot(u, ricci(R, v, sq), sq)


def weyl_null(R, k, a, b, sq=S13):
    """C11: C(k, a, k, b) = (k ^ b) . W(k ^ a)."""
    return bb_dot(wedge(k, b, sq), weyl(R, k, a, sq), sq)


# ---------------------------------------------------------------------------
# 7. standard fields (section 11). Spherical labels (t, r, theta, phi) = 0..3 unless stated;
#    each constructor's `order` is the jet order of om (1 gives curvature values, 2 curvature jets).
# ---------------------------------------------------------------------------

def f_static(M=0, lam=0, Q=0):
    """f(r) = 1 - 2M/r - Lambda r^2/3 + Q^2/r^2 as a callable on jets (Schwarzschild, SdS/AdS, RN)."""
    M, lam, Q = F(M), F(lam), F(Q)
    return lambda r: 1 - 2 * M / r - (lam / 3) * r * r + Q * Q / (r * r)


def mass_for_root(r0, w, lam=0, Q=0):
    """The mass M with f(r0) = w^2 for f = 1 - 2M/r - Lambda r^2/3 + Q^2/r^2 (rational sqrt f)."""
    r0, w, lam, Q = F(r0), F(w), F(lam), F(Q)
    return r0 * (1 - w * w - lam * r0 * r0 / 3 + Q * Q / (r0 * r0)) / 2


def static_field(r0, s0, c0, f, order=1, sqrt_f=None, fprime=None):
    """Static field f dt^2 - dr^2/f - r^2 dOmega^2 at r = r0, sin(theta) = s0, cos(theta) = c0; f callable on
    jets; sqrt(f(r0)) rational or supplied as sqrt_f; f' by differentiation unless fprime (a callable on jets)
    is given, so a check can state f' as data (L12 static_field)."""
    K = order + 1
    r = Jet.var(1, r0, 4, K)
    fj = _jc(f(r), 4)
    sf = fj.pw(F(1, 2), sqrt_f)
    fp = fj.d(1) if fprime is None else _jc(fprime(r), 4)
    sn, cs = sincos(2, s0, c0, 4, K)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][1], TH[2][2], TH[3][3] = sf, 1 / sf, r, r * sn
    om = omega_forms([(0, 0, 1, fp / (2 * sf)), (2, 2, 1, sf / r), (3, 3, 1, sf / r), (3, 3, 2, (cs / sn) / r)])
    return Field(TH, om)


def schwarzschild_static(M, r0, s0, c0, order=1):
    """Schwarzschild in static coordinates (f = 1 - 2M/r; sqrt f rational at r0)."""
    return static_field(r0, s0, c0, f_static(M), order)


def pg_field(r0, s0, c0, beta, order=1):
    """Painleve-Gullstrand gauge hb = 1 - beta P (hb^{-1}(e_t) = e_t + beta e_r) with beta(r) a callable on jets
    (any sign); coframe dt, dr + beta dt, r dtheta, r sin dphi; Cartan connection (L12 pg_field, general beta)."""
    K = order + 1
    r = Jet.var(1, r0, 4, K)
    b = _jc(beta(r), 4)
    db = b.d(1)
    sn, cs = sincos(2, s0, c0, 4, K)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][0], TH[1][1], TH[2][2], TH[3][3] = Jet.const(1), b, Jet.const(1), r, r * sn
    om = omega_forms([(1, 0, 1, -db), (2, 0, 2, -b / r), (3, 0, 3, -b / r),
                      (2, 2, 1, 1 / r), (3, 3, 1, 1 / r), (3, 3, 2, (cs / sn) / r)])
    return Field(TH, om)


def beta_schwarzschild(M, sign=1):
    """beta(r) = sign sqrt(2M/r) (sign = +1: the stored ingoing, black-hole chart)."""
    M = F(M)
    return lambda r: sign * (2 * M / r).pw(F(1, 2))


def beta_kottler(M=0, lam=0, Q=0, sign=1):
    """beta(r) = sign sqrt(2M/r + Lambda r^2/3 - Q^2/r^2) (SdS/AdS/RN PG; state the sign per region)."""
    M, lam, Q = F(M), F(lam), F(Q)
    return lambda r: sign * (2 * M / r + (lam / 3) * r * r - Q * Q / (r * r)).pw(F(1, 2))


def beta_de_sitter(H):
    """beta(r) = -r H: the expanding static-PG de Sitter chart (contains the future horizon)."""
    H = F(H)
    return lambda r: -H * r


def schwarzschild_pg(M, r0, s0, c0, order=1):
    """Schwarzschild in the stored PG gauge (beta = +sqrt(2M/r) rational at r0)."""
    return pg_field(r0, s0, c0, beta_schwarzschild(M), order)


def de_sitter_pg(H, r0, s0, c0, order=1):
    """de Sitter in the static PG chart beta = -rH."""
    return pg_field(r0, s0, c0, beta_de_sitter(H), order)


def de_sitter_flat(H, E, order=1, d=4):
    """de Sitter, flat slicing, Cartesian labels: hb^{-1}(e_t) = e_t, hb^{-1}(e_i) = e^{Ht} e_i at a point where
    e^{Ht} = E; Omega(hb(gamma_i)) = -H gamma_0 ^ gamma_i (C10; L12 ds_flat_field)."""
    H, E = F(H), F(E)
    K = order + 1
    a = Jet.from_taylor(0, [E * H ** k * c for k, c in enumerate(series.taylor_exp(K))], d)
    TH = [[F(0)] * d for _ in range(d)]
    TH[0][0] = F(1)
    for i in range(1, d):
        TH[i][i] = a
    om = [{}] + [{(0, i): -H} for i in range(1, d)]
    return Field(TH, om, lorentz_sig(d))


ds_flat_field = de_sitter_flat


def synchronous_field(scales, sq=None):
    """Synchronous diagonal field dt^2 - sum a_i^2 dx_i^2 (Cartesian labels, t = label 0): scales[i - 1] = a_i
    as jets in label 0 (order >= om order + 1); om[i] = -(adot_i/a_i) gamma_0 ^ gamma_i (C10)."""
    sq = lorentz_sig(len(scales) + 1) if sq is None else tuple(sq)
    d = len(sq)
    TH = [[F(0)] * d for _ in range(d)]
    TH[0][0] = F(1)
    om = [{}]
    for i in range(1, d):
        a = _jc(scales[i - 1], d)
        TH[i][i] = a
        om.append({(0, i): -(a.d(0) / a)})
    return Field(TH, om, sq)


def synchronous_from_data(data, sq=None):
    """Synchronous field from instant data data[i - 1] = (a_i, adot_i, addot_i) (L10 Synchronous)."""
    sq = lorentz_sig(len(data) + 1) if sq is None else tuple(sq)
    d = len(sq)
    scales = [Jet.from_taylor(0, [F(x[0]), F(x[1]), F(x[2]) / 2], d) for x in data]
    return synchronous_field(scales, sq)


def flrw_flat(a, adot, addot, d=4):
    """Spatially flat FLRW at an instant (a, adot, addot) (comoving gauge, section 11)."""
    return synchronous_from_data([(a, adot, addot)] * (d - 1), lorentz_sig(d))


def kasner_data(p, base):
    """Kasner instant data (tau, data): tau = base^D, D the lcm of the denominators of p, data[i] =
    (tau^p_i, p_i tau^p_i/tau, p_i(p_i - 1) tau^p_i/tau^2), all rational (L10 kasner)."""
    D = 1
    for x in p:
        den = F(x).denominator
        a, b = D, den
        while b:
            a, b = b, a % b
        D = D * den // a
    tau = F(base) ** D
    out = []
    for x in p:
        x = F(x)
        a = F(base) ** int(x * D)
        out.append((a, x * a / tau, x * (x - 1) * a / (tau * tau)))
    return tau, out


def kasner_field(p, base, order=1):
    """(tau, Field) for Kasner hb^{-1}(e_i) = t^{p_i} e_i at t = tau = base^D (rational powers)."""
    tau, _ = kasner_data(p, base)
    d = len(p) + 1
    T = Jet.var(0, tau, d, order + 1)
    return tau, synchronous_field([T.pw(x) for x in p], lorentz_sig(d))


def kerr_schild_field(x0, Hf, kf, order=1, sq=S13):
    """Kerr-Schild field hb^{-1}(a) = a - H (a.k) k, Q(k) = 0 (g = eta - 2H k k), Cartesian labels, gamma_a = e_a:
    Hf(X) -> H, kf(X) -> contravariant components k^a (jets); Omega solved from torsion."""
    d = len(sq)

    def rows(X):
        H = _jc(Hf(X), d)
        k = [_jc(x, d) for x in kf(X)]
        out = []
        for mu in range(d):
            kmu = k[mu] * sq[mu]
            out.append([(1 if a == mu else 0) - H * kmu * k[a] for a in range(d)])
        return out
    return field_from_hbinv(rows, x0, sq, order)


def _radius(X):
    return (X[1] * X[1] + X[2] * X[2] + X[3] * X[3]).pw(F(1, 2))


def schwarzschild_ks(M, x0, order=1):
    """Schwarzschild in ingoing Kerr-Schild form: H = M/r, k = e_t - x/r (needs rational r at x0)."""
    M = F(M)

    def H(X):
        return M / _radius(X)

    def k(X):
        r = _radius(X)
        return [Jet.const(1), -X[1] / r, -X[2] / r, -X[3] / r]
    return kerr_schild_field(x0, H, k, order)


def rn_ks(M, Q, x0, order=1):
    """Reissner-Nordstrom in Kerr-Schild form: H = M/r - Q^2/(2 r^2), k = e_t - x/r."""
    M, Q = F(M), F(Q)

    def H(X):
        r = _radius(X)
        return M / r - Q * Q / (2 * r * r)

    def k(X):
        r = _radius(X)
        return [Jet.const(1), -X[1] / r, -X[2] / r, -X[3] / r]
    return kerr_schild_field(x0, H, k, order)


def sync_interior_field(r0, w, s0, c0, order=1, boost_sign=-1):
    """Schwarzschild(-de Sitter) interior, synchronous gauge, 2M = 1, labels (r, t, theta, phi):
    hb^{-1}(e_r) = gamma0/sqrt(A), hb^{-1}(e_t) = sqrt(A) gamma1, A = (1 - r + (Lambda/3) r^3)/r, Lambda fixed by
    sqrt(A(r0)) = w; Omega(gamma_i) = boost_sign sigma_i B_i (+ (cot/r) gamma2 gamma3 on gamma3). Returns
    (field, Lambda, (r, A, sA, s1, s2, sn, cs)) (L09 interior_field; T13 is r0 = k^2/(1+k^2), w = 1/k)."""
    r0, w = F(r0), F(w)
    lam = 3 * (w * w * r0 - 1 + r0) / (r0 * r0 * r0)
    K = order + 1
    r = Jet.var(0, r0, 4, K)
    A = (1 - r + (lam / 3) * r * r * r) / r
    sA = A.pw(F(1, 2))
    sn, cs = sincos(2, s0, c0, 4, K)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0], TH[1][1], TH[2][2], TH[3][3] = 1 / sA, sA, r, r * sn
    s1, s2 = A.d(0) / (2 * sA), sA / r
    om = [{}, {(0, 1): boost_sign * s1}, {(0, 2): boost_sign * s2},
          {(0, 3): boost_sign * s2, (2, 3): cs / (sn * r)}]
    return Field(TH, om), lam, (r, A, sA, s1, s2, sn, cs)


# ---------------------------------------------------------------------------
# 8. conformal model and tractors (section 12, GR2 fix: canonical tractor X = n0)
# ---------------------------------------------------------------------------

def conformal_sig(sq=S13):
    """Signature of the conformal model: sq + (e+ square +1, e- square -1); S24 for Cl(1,3)."""
    return tuple(sq) + (1, -1)


S24 = conformal_sig(S13)


def null_pair(sqc=S24, plus=None, minus=None):
    """(n0, ninf) = ((e+ + e-)/2, e+ - e-) with n0 . ninf = 1 (defaults: the last two generators)."""
    plus = len(sqc) - 2 if plus is None else plus
    minus = len(sqc) - 1 if minus is None else minus
    return GA.scal(F(1, 2), GA.add(GA.gen(plus), GA.gen(minus))), GA.sub(GA.gen(plus), GA.gen(minus))


N0, NINF = null_pair(S24)
NI = NINF                    # the L10/L12 name


def _conf(sq):
    sqc = conformal_sig(sq)
    n0, ni = null_pair(sqc)
    return sqc, n0, ni


def tractor(sig, mu, rho, sq=S13):
    """The tractor sig ninf + mu + rho n0 (mu a spacetime vector)."""
    _, n0, ni = _conf(sq)
    return m_add(m_scal(sig, ni), mu, m_scal(rho, n0))


def slots(V, sq=S13):
    """(sigma, mu, rho) of V = sigma ninf + mu + rho n0: sigma = V . n0, rho = V . ninf."""
    sqc, n0, ni = _conf(sq)
    d = len(sq)
    return (vdot(V, n0, sqc), {b: c for b, c in V.items() if len(b) == 1 and b[0] < d}, vdot(V, ni, sqc))


def conformal_point(x, sq=S13):
    """X(x) = n0 + x - Q(x)/2 ninf, the null representative of the point x."""
    sqc, n0, ni = _conf(sq)
    return m_add(n0, x, m_scal(-vdot(x, x, sq) / 2, ni))


def scale_tractor(lam, d=4):
    """Scale tractor I = ninf + rho n0 with rho = Lambda/((d-1)(d-2)) (d = 4: Lambda/6; Q(I) = 2 rho)."""
    _, n0, ni = _conf(lorentz_sig(d))
    return m_add(ni, m_scal(F(lam) / ((d - 1) * (d - 2)), n0))


def scale_tractor_dual(lam):
    """n0 + (Lambda/6) ninf: the L09 tractor.py orientation (same norm Lambda/3; the store's I is scale_tractor)."""
    return m_add(N0, m_scal(F(lam) / 6, NINF))


def omega_T(fld, c, P):
    """Omega_T(hb(gamma_c)) = Omega(hb(gamma_c)) - ninf ^ gamma_c + n0 ^ P(gamma_c) in the conformal model (values)."""
    sqc, n0, ni = _conf(fld.sq)
    A = GA.gen(c)
    return m_add(fld.omega(c), m_neg(comm(ni, A, sqc)), comm(n0, P(A), sqc))


def omega_T_bg(fld, mu, P):
    """Omega_T(e_mu) = Omega(e_mu) - ninf ^ hb^{-1}(e_mu) + n0 ^ P(hb^{-1}(e_mu)) (values; L10 omega_T)."""
    sqc, n0, ni = _conf(fld.sq)
    A = m_val(fld.g[mu])
    return m_add(fld.Omega(mu), m_neg(comm(ni, A, sqc)), comm(n0, P(A), sqc))


def dT_const(fld, c, P, V):
    """D^T along hb(gamma_c) of a constant tractor V: Omega_T x V (values)."""
    sqc = conformal_sig(fld.sq)
    return comm(omega_T(fld, c, P), V, sqc)


def tractor_strength(fld, mu, nu):
    """Tractor field strength F_T(e_mu ^ e_nu) = d_mu Omega_T(e_nu) - d_nu Omega_T(e_mu) + Omega_T(e_mu) x Omega_T(e_nu)
    (value; P from the field's curvature jets, so the field's om needs jet order >= 2)."""
    sqc, n0, ni = _conf(fld.sq)
    P = schouten(fld.curvature_jet(), fld.sq)
    d = fld.d
    OT = []
    for m in (mu, nu):
        A = fld.g[m]
        PA = m_add(*[m_scal(fld.TH[a][m], P(GA.gen(a))) for a in range(d) if fld.TH[a][m]])
        OT.append(m_add(fld.Om[m], m_neg(comm(ni, A, sqc)), comm(n0, PA, sqc)))
    return m_val(m_add(m_d(OT[1], mu), m_neg(m_d(OT[0], nu)), comm(OT[0], OT[1], sqc)))


def tractor_curvature(fld):
    """Covariant tractor field strength on the frame planes: {(a, b): F_T(hb(gamma_a) ^ hb(gamma_b))} (values);
    Lorentz block -W, soldering block the torsion (zero), n0 block the Cotton term."""
    Hi, d = fld.hb_matrix(), fld.d
    Fb = {(mu, nu): tractor_strength(fld, mu, nu) for mu in range(d) for nu in range(mu + 1, d)}
    out = {}
    for a in range(d):
        for b in range(a + 1, d):
            acc = {}
            for (mu, nu), Fm in Fb.items():
                c = Hi[mu][a] * Hi[nu][b] - Hi[nu][a] * Hi[mu][b]
                if c and Fm:
                    acc = m_add(acc, m_scal(c, Fm))
            out[(a, b)] = acc
    return out


# -- Lie-algebra tools on bivectors (L09 tractor.py / engine.py) -----------------------------------

def mv_coords(x, blades):
    """Coordinates of x on a list of blades."""
    return [x.get(bl, F(0)) for bl in blades]


def biv_rank(xs, sq):
    """Rank of a list of bivectors."""
    bl = bivector_blades(len(sq))
    return GA.rank_of_vectors([mv_coords(x, bl) for x in xs]) if xs else 0


def lie_closure(gens, sq):
    """A basis of the Lie algebra generated by bivectors under the commutator product."""
    basis = []
    for x in gens:
        if x and biv_rank(basis + [x], sq) > len(basis):
            basis.append(x)
    while True:
        grown = False
        for a in list(basis):
            for b in list(basis):
                c = comm(a, b, sq)
                if c and biv_rank(basis + [c], sq) > len(basis):
                    basis.append(c)
                    grown = True
        if not grown:
            return basis


def lie_dim(gens, sq):
    """Dimension of the Lie algebra generated by bivectors."""
    return len(lie_closure(gens, sq))


def annihilates(B, I, sq):
    """True when B . I = 0 for a bivector B and a vector I."""
    return not comm(B, I, sq)


def stabiliser(I, sq):
    """Basis of {X bivector : X . I = 0} (the kernel on the basis bivectors)."""
    bl = bivector_blades(len(sq))
    cols = []
    for b in bl:
        v = comm({b: F(1)}, I, sq)
        cols.append([v.get((a,), F(0)) for a in range(len(sq))])
    M = [list(r) for r in zip(*cols)]
    ker = GA.field_kernel(M)
    return [{b: c for b, c in zip(bl, k) if c != 0} for k in ker]


def killing_rank(L, sq):
    """Rank of the Killing form tr(ad_X ad_Y) of the Lie algebra with basis L."""
    bl = bivector_blades(len(sq))
    k = len(L)
    mat = [mv_coords(x, bl) for x in L]
    piv = []
    for c in range(len(bl)):
        trial = [[row[j] for j in piv + [c]] for row in mat]
        if GA.rank_of_vectors(trial) > len(piv):
            piv.append(c)
        if len(piv) == k:
            break
    sqm = [[mat[j][piv[i]] for j in range(k)] for i in range(k)]

    def coords(v):
        cv = mv_coords(v, bl)
        return GA.field_solve(sqm, [cv[p] for p in piv])
    ad = []
    for X in L:
        cols = [coords(comm(X, Y, sq)) for Y in L]
        ad.append([[cols[j][i] for j in range(k)] for i in range(k)])
    kil = [[sum(ad[a][i][j] * ad[b][j][i] for i in range(k) for j in range(k)) for b in range(k)] for a in range(k)]
    return GA.mat_rank(kil)


# ---------------------------------------------------------------------------
# 9. the twistor model of the conformal model (L10 twcore, ported from legacy/verify_T11.py Parts B-D):
#    CS = C^4 with basis e1, e2 (omega-plane), e3, e4 (pi-plane); ambient Lambda^2 CS in the basis
#    e_i ^ e_j (i < j), n_inf = e1^e2, n_0 = e3^e4, <P, P'> = coefficient of e1^e2^e3^e4 in P ^ P';
#    everything over GA.QI. Names carry the prefix tw_ (TW_ for constants).
# ---------------------------------------------------------------------------

TW_QZ = GA.qi(0)
TW_QO = GA.qi(1)
TW_PAIRS4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def tw_q(re, im=0):
    """GA.qi(re, im)."""
    return GA.qi(re, im)


def tw_eps2(a, b):
    """<ab> = a_0 b_1 - a_1 b_0."""
    return a[0] * b[1] - a[1] * b[0]


def tw_wedge2(z1, z2):
    """z1 ^ z2 in Lambda^2 C^4 (coefficients on TW_PAIRS4)."""
    return [z1[i] * z2[j] - z1[j] * z2[i] for (i, j) in TW_PAIRS4]


def tw_perm_sign(perm):
    """Sign of a permutation (list)."""
    s, p = 1, list(perm)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def tw_amb_pair(P, R):
    """<P, R>: the e1^e2^e3^e4 coefficient of P ^ R."""
    tot = TW_QZ
    for a, (i, j) in enumerate(TW_PAIRS4):
        if not P[a]:
            continue
        for b, (k, l) in enumerate(TW_PAIRS4):
            if R[b] and len({i, j, k, l}) == 4:
                tot = tot + tw_q(tw_perm_sign((i, j, k, l))) * P[a] * R[b]
    return tot


def tw_biv(i, j):
    """The ambient basis vector e_i ^ e_j."""
    out = [TW_QZ] * 6
    out[TW_PAIRS4.index((min(i, j), max(i, j)))] = TW_QO if i < j else -TW_QO
    return out


def tw_vadd(*us):
    """Sum of lists of QI."""
    return [sum((u[k] for u in us), TW_QZ) for k in range(len(us[0]))]


def tw_vscal(c, u):
    """c u for a list of QI."""
    return [c * a for a in u]


TW_N_INF, TW_N_0 = tw_biv(0, 1), tw_biv(2, 3)
TW_EAMB = [tw_biv(i, j) for (i, j) in TW_PAIRS4]
TW_X_SLOT = [tw_biv(0, 2), tw_biv(0, 3), tw_biv(1, 2), tw_biv(1, 3)]


def tw_twistor(om, pi):
    """The twistor (omega, pi) as a 4-list."""
    return [om[0], om[1], pi[0], pi[1]]


def tw_i_lam(lam):
    """I = n_inf + lam n_0 (lam = Lambda/6)."""
    return tw_vadd(TW_N_INF, tw_vscal(tw_q(lam), TW_N_0))


def tw_xslot(co):
    """sum co[k] X_SLOT[k]."""
    return tw_vadd(*[tw_vscal(tw_q(c), v) for c, v in zip(co, TW_X_SLOT)])


def tw_xpoint(x):
    """X(x) = n_0 + x - (1/2) <x, x> n_inf."""
    return tw_vadd(TW_N_0, x, tw_vscal(-tw_amb_pair(x, x) / tw_q(2), TW_N_INF))


def tw_on_line(co, pi):
    """The twistor (mu_x pi, pi) on the incidence line of x = (x13, x14, x23, x24)."""
    x13, x14, x23, x24 = co
    om = [-tw_q(x13) * pi[1] + tw_q(x14) * pi[0], -tw_q(x23) * pi[1] + tw_q(x24) * pi[0]]
    return tw_twistor(om, pi)


def tw_act(A, P):
    """A.(u^v) = Au^v + u^Av, extended linearly to bivectors."""
    out = [TW_QZ] * 6
    for a, (i, j) in enumerate(TW_PAIRS4):
        if not P[a]:
            continue
        Aei = [A[r][i] for r in range(4)]
        Aej = [A[r][j] for r in range(4)]
        ei = [TW_QO if r == i else TW_QZ for r in range(4)]
        ej = [TW_QO if r == j else TW_QZ for r in range(4)]
        out = tw_vadd(out, tw_vscal(P[a], tw_vadd(tw_wedge2(Aei, ej), tw_wedge2(ei, Aej))))
    return out


def tw_rot(U, V, W):
    """R_{U^V}(W) = <U,W> V - <V,W> U."""
    return tw_vadd(tw_vscal(tw_amb_pair(U, W), V), tw_vscal(-tw_amb_pair(V, W), U))


def tw_gsolve(rows, rhs):
    """Exact solution of a consistent (possibly overdetermined) system over Q(i)."""
    m, n = len(rows), len(rows[0])
    A = [rows[i][:] + [rhs[i]] for i in range(m)]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = TW_QO / A[r][c]
        A[r] = [x * inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    if any(A[i][n] for i in range(r, m)):
        raise ValueError("inconsistent linear system")
    if len(piv) != n:
        raise ValueError("underdetermined linear system")
    sol = [TW_QZ] * n
    for i, c in enumerate(piv):
        sol[c] = A[i][n]
    return sol


_TW_UNIT_ACT = []


def _tw_unit_act():
    if not _TW_UNIT_ACT:
        for r in range(4):
            for c in range(4):
                A = [[TW_QZ] * 4 for _ in range(4)]
                A[r][c] = TW_QO
                _TW_UNIT_ACT.append([tw_act(A, TW_EAMB[b]) for b in range(6)])
    return _TW_UNIT_ACT


_TW_SP = {}


def tw_spin_preimage(U, V):
    """The traceless A in gl(4) whose action on Lambda^2 CS is the rotation R_{U^V} (memoised)."""
    key = tuple((c.re, c.im) for c in U + V)
    if key not in _TW_SP:
        _TW_SP[key] = _tw_spin_preimage(U, V)
    return [row[:] for row in _TW_SP[key]]


def _tw_spin_preimage(U, V):
    ua = _tw_unit_act()
    rows, rhs = [], []
    for b in range(6):
        target = tw_rot(U, V, TW_EAMB[b])
        for comp in range(6):
            rows.append([ua[k][b][comp] for k in range(16)])
            rhs.append(target[comp])
    rows.append([TW_QO if r == c else TW_QZ for r in range(4) for c in range(4)])
    rhs.append(TW_QZ)
    sol = tw_gsolve(rows, rhs)
    return [[sol[4 * r + c] for c in range(4)] for r in range(4)]


TW_SIG = [[TW_QO if abs(a - b) == 2 else TW_QZ for b in range(4)] for a in range(4)]


def tw_herm(zi, zj):
    """conj(zi)^T Sigma zj: the (2,2) Hermitian form pairing omega with conj(pi)."""
    return sum((zi[a].conj() * zj[b] for a in range(4) for b in range(4) if TW_SIG[a][b]), TW_QZ)


def tw_moment(A, Zs):
    """M_A = i sum_i conj(Z_i)^T Sigma A Z_i."""
    tot = TW_QZ
    for z in Zs:
        Az = [sum((A[r][c] * z[c] for c in range(4)), TW_QZ) for r in range(4)]
        tot = tot + tw_herm(z, Az)
    return GA.QI_I * tot


def tw_gram_inverse(basis):
    """Inverse of the Gram matrix of the ambient pairing on a basis."""
    n = len(basis)
    Gs = [[tw_amb_pair(u, v) for v in basis] for u in basis]
    cols = [tw_gsolve([row[:] for row in Gs], [TW_QO if r == c else TW_QZ for r in range(n)]) for c in range(n)]
    return [[cols[c][r] for c in range(n)] for r in range(n)]


_TW_GI = []


def tw_grip(Zs, I):
    """P = M(I): the ambient vector with <P, U> = M_{A(U ^ I)} for every U."""
    if not _TW_GI:
        _TW_GI.append(tw_gram_inverse(TW_EAMB))
    vals = [tw_moment(tw_spin_preimage(TW_EAMB[a], I), Zs) for a in range(6)]
    P = [sum((vals[a] * _TW_GI[0][a][j] for a in range(6)), TW_QZ) for j in range(6)]
    if not all(tw_amb_pair(P, TW_EAMB[a]) == vals[a] for a in range(6)):
        raise ArithmeticError("tw_grip: pairing check failed")
    return P


def tw_gram_h(Zs):
    """Hermitian Gram matrix of the twistors under tw_herm."""
    return [[tw_herm(a, b) for b in Zs] for a in Zs]


def tw_internal_casimir(Z1, Z2):
    """C = (h11 - h22)^2/4 + |h12|^2 = tr(h_0^2)/2."""
    h11, h22, h12 = tw_herm(Z1, Z1), tw_herm(Z2, Z2), tw_herm(Z1, Z2)
    return (h11 - h22) * (h11 - h22) / tw_q(4) + h12 * h12.conj()


def tw_casimir(Zs, basis):
    """C2(W) = (1/2) g^{ac} g^{bd} M_ab M_cd over the span of basis."""
    n = len(basis)
    Gi = tw_gram_inverse(basis)
    Mm = [[tw_moment(tw_spin_preimage(u, v), Zs) if a != b else TW_QZ for b, v in enumerate(basis)]
          for a, u in enumerate(basis)]
    tot = TW_QZ
    for a in range(n):
        for b in range(n):
            if not Mm[a][b]:
                continue
            for c in range(n):
                if not Gi[a][c]:
                    continue
                for d in range(n):
                    if Gi[b][d] and Mm[c][d]:
                        tot = tot + Gi[a][c] * Gi[b][d] * Mm[a][b] * Mm[c][d]
    return tot / tw_q(2)


def tw_xreal(t, x_, y, z):
    """The real slice x = i K eps, K the Hermitian matrix of (t, x, y, z)."""
    K = [[tw_q(t + z), tw_q(x_, -y)], [tw_q(x_, y), tw_q(t - z)]]
    eps = [[TW_QZ, TW_QO], [-TW_QO, TW_QZ]]
    X = [[sum((K[a][b] * eps[b][c] for b in range(2)), TW_QZ) * GA.QI_I for c in range(2)] for a in range(2)]
    return tw_vadd(*[tw_vscal(c_, v) for c_, v in zip((X[0][0], X[0][1], X[1][0], X[1][1]), TW_X_SLOT)])


def tw_in_su22(A):
    """True when A is in su(2,2) for the form TW_SIG."""
    SA = [[sum((TW_SIG[i][k] * A[k][j] for k in range(4)), TW_QZ) for j in range(4)] for i in range(4)]
    return all(SA[i][j] + SA[j][i].conj() == TW_QZ for i in range(4) for j in range(4))
