"""Two-loop electrodynamics in the spacetime algebra continued in dimension: exact checks.

The Dirac algebra is the Clifford algebra of the (Wick-rotated) spacetime vectors; in d dimensions it is
handled symbolically by the contraction rule gamma_a X b gamma_a = -(gamma_a X gamma_a) b + 2 b X with
gamma_a gamma_a = d, checked against the Clifford algebras Cl(D,0) and Cl(1,D-1) for integer D. Traces are
4 <.>_0 (tr 1 = 4). The two-loop vacuum polarisation of one massless Dirac fermion (three diagrams, covariant
gauge with parameter xi) is reduced exactly: scalar products to the five denominators, integration by parts
(the triangle rule) and Gamma-function bubbles, to two masters M1 = G(1,1)^2 and M2 = G(1,1) G(1, 3 - d/2),
with coefficients rational functions of d (GA.RF). Laurent expansion in eps (d = 4 - 2 eps) is exact, zeta_3
kept symbolic. Results: one loop beta0 = 4/3; two loops: transverse, xi independent, a simple pole only,
beta1 = 4 (a = alpha/(4 pi), mu^2 da/dmu^2 = beta0 a^2 + beta1 a^3); MS-bar finite part 16 zeta_3 - 55/3.
The Ward-Takahashi identity at two loops at integrand level (Z1 = Z2) in Cl(1,3) with massive lines and the
unit outside the product. Exact arithmetic only.
"""
from fractions import Fraction as Fr
from functools import lru_cache

import GA
from tp_premise import premise


def factorial(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

RF = GA.RF
D = RF.var()                     # the dimension d


def rfc(c):
    return RF.const(Fr(c))


def lin(c0, c1):
    """c0 + c1 d as an RF."""
    return RF([Fr(c0), Fr(c1)])


# ---------------------------------------------------------------------------
# 1. polynomials in d (coefficient lists) and in the scalar products
# ---------------------------------------------------------------------------
# scalar-product symbols: index 0 kk, 1 ll, 2 qq, 3 kl, 4 kq, 5 lq
SYM = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (0, 1): 3, (0, 2): 4, (1, 2): 5}


def padd(p, q):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, Fr(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def pscale(p, c):
    if c == 0:
        return {}
    return {m: v * c for m, v in p.items()}


def pmulmono(p, mono):
    """multiply polynomial (keys: (dpow, e0..e5)) by monomial key."""
    out = {}
    for m, c in p.items():
        k = tuple(a + b for a, b in zip(m, mono))
        out[k] = out.get(k, Fr(0)) + c
    return {m: c for m, c in out.items() if c != 0}


def pmul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            k = tuple(a + b for a, b in zip(m1, m2))
            out[k] = out.get(k, Fr(0)) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}


ONE = {(0, 0, 0, 0, 0, 0, 0): Fr(1)}
DPOLY = {(1, 0, 0, 0, 0, 0, 0): Fr(1)}


def dot(a, b):
    """scalar product of momentum vectors a, b (3-tuples over k, l, q) as polynomial."""
    out = {}
    for i in range(3):
        for j in range(3):
            c = a[i] * b[j]
            if c == 0:
                continue
            s = SYM[(min(i, j), max(i, j))]
            key = [0] * 7
            key[1 + s] = 1
            key = tuple(key)
            out[key] = out.get(key, Fr(0)) + c
    return {m: c for m, c in out.items() if c != 0}


# ---------------------------------------------------------------------------
# 2. d-dimensional Clifford algebra: contraction of a repeated index, traces
# ---------------------------------------------------------------------------
# A word is a tuple of symbols: ('v', (ck, cl, cq)) a momentum vector, ('i', label) a basis vector
# gamma_label. Linear combinations of words: dict word -> polynomial.

@lru_cache(maxsize=None)
def contract(X):
    """gamma_a X gamma_a (a not in X) as a tuple of (dpoly-key-coefficient, word) pairs.
    gamma_a gamma_a = d; gamma_a X' b gamma_a = -(gamma_a X' gamma_a) b + 2 b X'."""
    if len(X) == 0:
        return (((1, 0, 0, 0, 0, 0, 0), Fr(1), ()),)
    Xp, b = X[:-1], X[-1]
    out = {}
    for mono, c, w in contract(Xp):
        key = (mono, w + (b,))
        out[key] = out.get(key, Fr(0)) - c
    key = ((0, 0, 0, 0, 0, 0, 0), (b,) + Xp)
    out[key] = out.get(key, Fr(0)) + 2
    return tuple((m, c, w) for (m, w), c in out.items() if c != 0)


def eliminate_indices(word):
    """Return dict word -> poly in d with all repeated labels contracted (trace context, cyclic)."""
    todo = {word: ONE}
    done = {}
    while todo:
        w, p = todo.popitem()
        labels = [s[1] for s in w if s[0] == 'i']
        rep = None
        for lab in labels:
            if labels.count(lab) == 2:
                rep = lab
                break
        if rep is None:
            done[w] = padd(done.get(w, {}), p)
            continue
        i = next(j for j, s in enumerate(w) if s == ('i', rep))
        w = w[i:] + w[:i]                      # cyclic rotation
        j = next(t for t in range(1, len(w)) if w[t] == ('i', rep))
        X, Y = w[1:j], w[j + 1:]
        for mono, c, wx in contract(X):
            nw = wx + Y
            todo[nw] = padd(todo.get(nw, {}), pmulmono(pscale(p, c), mono))
    return done


@lru_cache(maxsize=None)
def trace_vectors(w):
    """tr(a1 ... an) / 1 with tr 1 = 4, for momentum vectors only (polynomial as frozen items)."""
    if len(w) == 0:
        return tuple({(0, 0, 0, 0, 0, 0, 0): Fr(4)}.items())
    if len(w) % 2 == 1:
        return ()
    a1 = w[0][1]
    out = {}
    for j in range(1, len(w)):
        aj = w[j][1]
        rest = w[1:j] + w[j + 1:]
        t = dict(trace_vectors(rest))
        if not t:
            continue
        sgn = 1 if j % 2 == 1 else -1
        out = padd(out, pscale(pmul(dot(a1, aj), t), Fr(sgn)))
    return tuple(out.items())


def trace(word):
    total = {}
    for w, p in eliminate_indices(word).items():
        if any(s[0] == 'i' for s in w):
            raise ValueError("unpaired index left in trace")
        total = padd(total, pmul(p, dict(trace_vectors(w))))
    return total


def V(ck, cl, cq):
    return ('v', (Fr(ck), Fr(cl), Fr(cq)))


def G_(lab):
    return ('i', lab)


# ---------------------------------------------------------------------------
# 3. scalar products to denominators (q^2 = 1), then to integrals
# ---------------------------------------------------------------------------
# D-polynomials: dict (n1..n5) -> RF-free poly in d stored as dict dpow -> Fraction

def sp_to_D():
    """each scalar product as dict (n1..n5) -> Fraction (q^2 = 1)."""
    z = (0, 0, 0, 0, 0)
    e = lambda i: tuple(1 if t == i else 0 for t in range(5))
    h = Fr(1, 2)
    return {
        0: {e(0): Fr(1)},                                  # kk = D1
        1: {e(2): Fr(1)},                                  # ll = D3
        2: {z: Fr(1)},                                     # qq = 1
        3: {e(0): h, e(2): h, e(4): -h},                   # kl = (D1 + D3 - D5)/2
        4: {e(0): h, e(1): -h, z: h},                      # kq = (D1 - D2 + 1)/2
        5: {e(2): h, e(3): -h, z: h},                      # lq = (D3 - D4 + 1)/2
    }


SP = sp_to_D()


def dmul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            k = tuple(a + b for a, b in zip(m1, m2))
            out[k] = out.get(k, Fr(0)) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def dpow(p, n):
    out = {(0, 0, 0, 0, 0): Fr(1)}
    for _ in range(n):
        out = dmul(out, p)
    return out


def to_D(poly):
    """polynomial in scalar products and d -> dict (n1..n5) -> RF(d)."""
    out = {}
    for mono, c in poly.items():
        dp, ex = mono[0], mono[1:]
        term = {(0, 0, 0, 0, 0): Fr(1)}
        for s, e in enumerate(ex):
            if e:
                term = dmul(term, dpow(SP[s], e))
        coef_d = RF([Fr(0)] * dp + [Fr(1)])
        for m, v in term.items():
            out[m] = out.get(m, GA.RF0) + coef_d * rfc(v * c)
    return {m: v for m, v in out.items() if not v.is_zero()}


# ---------------------------------------------------------------------------
# 4. Gamma bookkeeping: Gamma(n + c d/2) keyed (n, c); ratios to the masters are RF(d)
# ---------------------------------------------------------------------------

def gamma_shift(n, c):
    """Gamma(n + c d/2) / Gamma(c d/2) as RF (c != 0)."""
    out = GA.RF1
    if n > 0:
        for i in range(n):
            out = out * lin(i, Fr(c, 2))
    elif n < 0:
        for i in range(1, -n + 1):
            out = out / lin(-i, Fr(c, 2))
    return out


def gfact(n):
    return Fr(factorial(n - 1))


def to_master(gp, master):
    """gp, master: dict (n, c) -> exponent. Returns RF ratio gp/master, or None if zero."""
    groups = {}
    for (n, c), e in gp.items():
        groups.setdefault(c, []).append((n, e))
    for (n, c), e in master.items():
        groups.setdefault(c, []).append((n, -e))
    out = GA.RF1
    for c, lst in groups.items():
        if c == 0:
            for n, e in lst:
                if n <= 0:
                    if e < 0:
                        return None
                    raise ValueError("Gamma pole in numerator")
                out = out * rfc(gfact(n) ** e)
            continue
        if sum(e for _, e in lst) != 0:
            raise ValueError("not a rational multiple of the master (group c=%s)" % c)
        for n, e in lst:
            g = gamma_shift(n, c)
            for _ in range(abs(e)):
                out = out * g if e > 0 else out / g
    return out


def gp_add(gp, key, e):
    gp[key] = gp.get(key, 0) + e
    if gp[key] == 0:
        del gp[key]


def gp_merge(a, b):
    out = dict(a)
    for k, e in b.items():
        gp_add(out, k, e)
    return out


M1 = {(2, -1): 2, (-1, 1): 4, (-2, 2): -2}


def bubble_gp(al, be):
    """G(al, be), al and be as (n, c) meaning n + c d/2; returns gp dict or None if zero."""
    (n1, c1), (n2, c2) = al, be
    if (c1 == 0 and n1 <= 0) or (c2 == 0 and n2 <= 0):
        return None
    gp = {}
    gp_add(gp, (n1 + n2, c1 + c2 - 1), 1)
    gp_add(gp, (-n1, 1 - c1), 1)
    gp_add(gp, (-n2, 1 - c2), 1)
    gp_add(gp, (n1, c1), -1)
    gp_add(gp, (n2, c2), -1)
    gp_add(gp, (-n1 - n2, 2 - c1 - c2), -1)
    return gp


# M2 = G(1,1) G(1, 3 - d/2): the inner bubble raises a line's power to 1 + eps
M2 = gp_merge(bubble_gp((1, 0), (1, 0)), bubble_gp((1, 0), (3, -1)))


def dfact2(n):
    out = 1
    while n > 1:
        out *= n
        n -= 2
    return out


def tensor_bubble_terms(j, A, B):
    """int d^dk/pi^(d/2) (k.v)^j / ((k^2)^A ((k-P)^2)^B)
       = sum_r coef_r (v^2)^r (v.P)^(j-2r) (P^2)^(d/2 + r - A - B) * Gamma-product_r.
    Returns list of (r, Fraction coef, gp) ; empty if A <= 0 or B <= 0 (scaleless)."""
    if A <= 0 or B <= 0:
        return []
    out = []
    for r in range(j // 2 + 1):
        coef = Fr(comb(j, 2 * r) * dfact2(2 * r - 1), 2 ** r)
        gp = {}
        gp_add(gp, (A + B - r, -1), 1)
        gp_add(gp, (j - r - A, 1), 1)
        gp_add(gp, (r - B, 1), 1)
        gp_add(gp, (j - A - B, 2), -1)
        gp_add(gp, (A, 0), -1)
        gp_add(gp, (B, 0), -1)
        out.append((r, coef, gp))
    return out


def add_res(res, which, rf):
    res[which] = res[which] + rf


def lin_expand(coeffs, n):
    """(c_x X + c_y Y + c_1)^n as dict (i, j) -> Fraction (powers of X, Y)."""
    cx, cy, c1 = coeffs
    out = {}
    for i in range(n + 1):
        for j in range(n - i + 1):
            m = n - i - j
            v = Fr(factorial(n), factorial(i) * factorial(j) * factorial(m)) * cx ** i * cy ** j * c1 ** m
            if v != 0:
                out[(i, j)] = out.get((i, j), Fr(0)) + v
    return out


@lru_cache(maxsize=None)
def I(a1, a2, a3, a4, a5):
    """returns (RF coefficient of M1, RF coefficient of M2)."""
    res = [GA.RF0, GA.RF0]
    if a5 <= 0:
        # factorised: D5^n = (D1 + D3 - 2 k.l)^n
        n = -a5
        for i in range(n + 1):
            for m in range(n - i + 1):
                j = n - i - m
                mult = Fr(factorial(n), factorial(i) * factorial(m) * factorial(j)) * (-2) ** j
                for r, coef, gpk in tensor_bubble_terms(j, a1 - i, a2):
                    # (l^2)^r (l.q)^(j-2r), l.q = (D3 - D4 + 1)/2, l^2 = D3
                    for (s, t), cst in lin_expand((Fr(1, 2), Fr(-1, 2), Fr(1, 2)), j - 2 * r).items():
                        gpl = bubble_gp((a3 - m - r - s, 0), (a4 - t, 0))
                        if gpl is None:
                            continue
                        rat = to_master(gp_merge(gpk, gpl), M1)
                        if rat is None:
                            continue
                        res[0] = res[0] + rat * rfc(mult * coef * cst)
        return tuple(res)
    if (a1 > 0 and a2 > 0) and (a3 <= 0 or a4 <= 0):
        return I(a3, a4, a1, a2, a5)                   # k <-> l
    if a1 <= 0 or a2 <= 0:
        if a1 <= 0 and a2 <= 0:
            return (GA.RF0, GA.RF0)
        if a1 <= 0:
            # k = k' + q: D1 = k'^2 + 2 k'.q + 1, D2 = k'^2, D5 = (k' - P)^2, P = l - q
            n = -a1
            for al in range(n + 1):
                for be in range(n - al + 1):
                    mult = Fr(factorial(n), factorial(al) * factorial(be) * factorial(n - al - be)) * 2 ** be
                    for r, coef, gpk in tensor_bubble_terms(be, a2 - al, a5):
                        A, B = a2 - al, a5
                        # (q^2)^r = 1, (q.P)^(be-2r), q.P = (D3 - D4 - 1)/2, P^2 = D4
                        for (s, t), cst in lin_expand((Fr(1, 2), Fr(-1, 2), Fr(-1, 2)), be - 2 * r).items():
                            gpl = bubble_gp((a3 - s, 0), (a4 - t + A + B - r, -1))
                            if gpl is None:
                                continue
                            rat = to_master(gp_merge(gpk, gpl), M2)
                            if rat is None:
                                continue
                            res[1] = res[1] + rat * rfc(mult * coef * cst)
            return tuple(res)
        # a2 <= 0: D2 = k^2 - 2 k.q + 1, D1 = k^2, D5 = (k - l)^2, P = l
        n = -a2
        for al in range(n + 1):
            for be in range(n - al + 1):
                mult = Fr(factorial(n), factorial(al) * factorial(be) * factorial(n - al - be)) * (-2) ** be
                for r, coef, gpk in tensor_bubble_terms(be, a1 - al, a5):
                    A, B = a1 - al, a5
                    # (q.l)^(be-2r), q.l = (D3 - D4 + 1)/2, P^2 = D3
                    for (s, t), cst in lin_expand((Fr(1, 2), Fr(-1, 2), Fr(1, 2)), be - 2 * r).items():
                        gpl = bubble_gp((a3 - s + A + B - r, -1), (a4 - t, 0))
                        if gpl is None:
                            continue
                        rat = to_master(gp_merge(gpk, gpl), M2)
                        if rat is None:
                            continue
                        res[1] = res[1] + rat * rfc(mult * coef * cst)
        return tuple(res)
    # all positive: triangle rule on the k-loop (lines 1, 2, 5)
    pre = GA.RF1 / lin(-a1 - a2 - 2 * a5, 1)
    terms = [
        (Fr(a1), (a1 + 1, a2, a3, a4, a5 - 1)),
        (Fr(-a1), (a1 + 1, a2, a3 - 1, a4, a5)),
        (Fr(a2), (a1, a2 + 1, a3, a4, a5 - 1)),
        (Fr(-a2), (a1, a2 + 1, a3, a4 - 1, a5)),
    ]
    for c, idx in terms:
        x = I(*idx)
        res[0] = res[0] + x[0] * rfc(c)
        res[1] = res[1] + x[1] * rfc(c)
    return (res[0] * pre, res[1] * pre)


def integrate(dpoly, denom):
    """dpoly: dict (n1..n5) -> RF ; denom: (a1..a5). Returns (RF on M1, RF on M2)."""
    r1, r2 = GA.RF0, GA.RF0
    for m, c in dpoly.items():
        x = I(*[a - n for a, n in zip(denom, m)])
        r1 = r1 + c * x[0]
        r2 = r2 + c * x[1]
    return r1, r2


# ---------------------------------------------------------------------------
# 5. Laurent series in eps
# ---------------------------------------------------------------------------

ZK = (3, 4, 5)          # symbols
Z0 = (0, 0, 0)


def cadd(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Fr(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def cmul(a, b):
    out = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            k = tuple(x + y for x, y in zip(m1, m2))
            out[k] = out.get(k, Fr(0)) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def cconst(c):
    return {Z0: Fr(c)} if c != 0 else {}


class LS(object):
    """sum_{i} c[i] eps^(v + i), i = 0..N-v (kept up to absolute order N)."""
    N = 4

    def __init__(self, v, coeffs):
        self.v = v
        self.c = [dict(x) for x in coeffs][: max(0, LS.N - v + 1)]

    def coef(self, n):
        i = n - self.v
        if 0 <= i < len(self.c):
            return self.c[i]
        return {}

    def __add__(self, o):
        v = min(self.v, o.v)
        return LS(v, [cadd(self.coef(n), o.coef(n)) for n in range(v, LS.N + 1)])

    def __mul__(self, o):
        v = self.v + o.v
        out = []
        for n in range(v, LS.N + 1):
            acc = {}
            for i in range(self.v, n - o.v + 1):
                a = self.coef(i)
                if a:
                    b = o.coef(n - i)
                    if b:
                        acc = cadd(acc, cmul(a, b))
            out.append(acc)
        return LS(v, out)


def poly_at(p, N):
    """polynomial p(d) at d = 4 - 2 eps as a coefficient list in eps."""
    out = []
    for c in reversed(p):
        # out = out*(4 - 2 eps) + c
        new = [Fr(0)] * (len(out) + 1)
        for i, x in enumerate(out):
            new[i] += 4 * x
            new[i + 1] += -2 * x
        new[0] += c
        out = new
    return GA.ptrim(out)


def rf_series(rf):
    """RF in d -> LS in eps."""
    N = LS.N
    num = poly_at(rf.num, N)
    den = poly_at(rf.den, N)
    if not num:
        return LS(0, [])
    vn = next(i for i, x in enumerate(num) if x != 0)
    vd = next(i for i, x in enumerate(den) if x != 0)
    v = vn - vd
    M = N - v + 2
    numr = GA.ps_trunc(num[vn:], M)
    denr = GA.ps_trunc(den[vd:], M)
    s = GA.ps_mul(numr, GA.ps_inv(denr, M), M)
    return LS(v, [cconst(x) for x in s])


def exp_series(lin_terms):
    """exp(sum_n z_n eps^n) with lin_terms dict n -> coefficient dict (no constant)."""
    N = LS.N + 4
    X = LS(1, [lin_terms.get(n, {}) for n in range(1, N + 1)])
    out = LS(0, [cconst(1)])
    term = LS(0, [cconst(1)])
    for k in range(1, N + 1):
        term = term * X
        term = LS(term.v, [{m: c / k for m, c in t.items()} for t in term.c])
        out = out + term
    return out


def lngamma_coeffs(args, n):
    """sum over (sign, a) of sign * [eps^n coefficient / zeta_n] in ln Gamma(1 + a eps):
    ln Gamma(1 + x) = -gamma x + sum_{n>=2} (-1)^n zeta_n x^n / n."""
    return sum(Fr(s * (-1) ** n * a ** n, n) for s, a in args)


def gamma_ratio_series(args, rational_prefactor):
    """prod Gamma(1 + a eps)^s (args: list of (s, a)) times rational_prefactor (LS), with the
    Euler-gamma term required to cancel and zeta_2 terms required to cancel (asserted)."""
    if sum(s * a for s, a in args) != 0:
        raise ValueError("Euler gamma does not cancel")
    lt = {}
    if lngamma_coeffs(args, 2) != 0:
        raise ValueError("zeta_2 does not cancel")
    for n, z in ((3, (1, 0, 0)), (4, (0, 1, 0)), (5, (0, 0, 1))):
        c = lngamma_coeffs(args, n)
        if c != 0:
            lt[n] = {z: c}
    return rational_prefactor * exp_series(lt)


# ---------------------------------------------------------------------------
# 6. the diagrams
# ---------------------------------------------------------------------------
P_QED = 'synthesis.one-loop-qed-in-the-spacetime-algebra'
P_DR = 'synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5'
P_ML = 'synthesis.imported-one-loop-integrals-and-pauli-villars-regulators'
P_TREE = 'field-theory.coupled-system-tree-level'

VK, VL, VQ = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)
VKQ, VLQ, VR = V(1, 0, -1), V(0, 1, -1), V(1, -1, 0)


def two_loop_words(mu, nu, al, be):
    """self-energy insertion on the k line, on the k - q line, and the vertex correction;
    each with its denominator powers (a1..a5), photon line D5 = (k - l)^2."""
    return [
        ('se1', (mu, VK, al, VL, be, VK, nu, VKQ), (2, 1, 1, 0, 1)),
        ('se2', (mu, VK, nu, VKQ, al, VLQ, be, VKQ), (1, 2, 0, 1, 1)),
        ('vx', (mu, VK, al, VL, nu, VLQ, be, VKQ), (1, 1, 1, 1, 1)),
    ]


def project_two_loop(proj, which=None):
    """proj 'delta': mu = nu contracted; 'qq': both replaced by q. Returns
    {'feyn': (R1, R2), 'xi': (R1, R2)} for int int tr(...)/denominators, summed over diagrams
    (or one diagram if which is given). The xi entry is the coefficient of (1 - xi)."""
    mu = nu = G_('m') if proj == 'delta' else VQ
    out = {}
    for part in ('feyn', 'xi'):
        R1, R2 = GA.RF0, GA.RF0
        al, be = (G_('a'), G_('a')) if part == 'feyn' else (VR, VR)
        extra = 0 if part == 'feyn' else 1
        for name, w, den in two_loop_words(mu, nu, al, be):
            if which is not None and name != which:
                continue
            dp = to_D(trace(w))
            x1, x2 = integrate(dp, tuple(den[:4]) + (den[4] + extra,))
            R1, R2 = R1 + x1, R2 + x2
        if part == 'xi':
            R1, R2 = -R1, -R2
        out[part] = (R1, R2)
    return out


def pi2_coefficients(pair):
    """Pi^(2) = a^2 (4 pi)^(2 eps) (q^2)^(-2 eps) [R1 M1 + R2 M2] with the -1/(d-1) projection."""
    dm1 = lin(-1, 1)
    return (rfc(-1) * pair[0]) / dm1, (rfc(-1) * pair[1]) / dm1


def rat_eps(numc, denc):
    M = LS.N + 3
    s = GA.ps_mul(GA.ps_trunc([Fr(x) for x in numc], M), GA.ps_inv([Fr(x) for x in denc], M), M)
    return LS(0, [cconst(x) for x in s])


def master_ratio():
    """r = M2/M1 = G(1, 1 + eps)/G(1, 1)
       = Gamma(1+2e) Gamma(1-2e)^2 (1-2e) / (2 Gamma(1+e)^2 Gamma(1-e) Gamma(1-3e) (1-3e))."""
    return gamma_ratio_series([(1, 2), (2, -2), (-2, 1), (-1, -1), (-1, -3)],
                              rat_eps([Fr(1, 2), -1], [1, -3]))


def sum_series(R1, R2):
    return rf_series(R1) + rf_series(R2) * master_ratio()


def one_loop_R0():
    """Pi^(1) = a (4 pi)^eps (q^2)^(-eps) G(1,1) R0(d)."""
    dp = to_D(trace((G_('m'), VK, G_('m'), VKQ)))
    tot = GA.RF0
    for m, c in dp.items():
        gp = bubble_gp((1 - m[0], 0), (1 - m[1], 0))
        if gp is None:
            continue
        tot = tot + c * to_master(gp, bubble_gp((1, 0), (1, 0)))
    return (rfc(-1) * tot) / lin(-1, 1)


def coeff_is(cdict, rational, zeta3=0):
    want = {}
    if rational != 0:
        want[(0, 0, 0)] = Fr(rational)
    if zeta3 != 0:
        want[(1, 0, 0)] = Fr(zeta3)
    return cdict == want


# ---------------------------------------------------------------------------
# 7. Clifford helpers for the integer-dimension and Cl(1,3) checks
# ---------------------------------------------------------------------------

def cmulv(xs, sq):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, sq)
    return out


def gvec(comps):
    return GA.add(*[GA.scal(Fr(c), GA.gen(i)) for i, c in enumerate(comps)])


def word_to_mv(word, vecs, sq):
    return cmulv([vecs[s] for s in word], sq) if word else GA.sc(1)


# ---------------------------------------------------------------------------
# 8. checks
# ---------------------------------------------------------------------------

FP_CONTRACTION = Fr(-1127)      # sum of all coefficients of the explicit contractions (computed)
FP_CONTROL6 = Fr(-44)
FP_TRACES = Fr(12040)          # sum of the explicit traces over words and dimensions (computed)
CONTR_COMPS = [[1, 2, 0, -1, 3, 1, -2, 1], [2, -1, 1, 0, 1, -3, 1, 2], [0, 1, -2, 3, 1, 1, 0, -1],
               [3, 0, 1, 1, -1, 2, 2, 0]]
CONTR_DIMS = ((0, (4, 5, 6, 7, 8)), (1, (4, 5, 6)))
CONTR_MAXLEN = 4


def contraction_data():
    """returns (all agree, fingerprint): the fingerprint is the sum of every coefficient of every
    sum_a gamma_a X gamma^a computed explicitly."""
    ok, fp = True, Fr(0)
    names = ['x0', 'x1', 'x2', 'x3']
    for sig_minus, Ds in CONTR_DIMS:
        for Dv in Ds:
            sq = tuple([1] + [(-1 if sig_minus else 1)] * (Dv - 1))
            vecs = {('v', n): gvec(CONTR_COMPS[i][:Dv]) for i, n in enumerate(names)}
            basis = [GA.gen(i) for i in range(Dv)]
            recip = [GA.scal(Fr(1, sq[i]), basis[i]) for i in range(Dv)]
            for n in range(CONTR_MAXLEN + 1):
                X = tuple(('v', names[i]) for i in range(n))
                lhs = {}
                Xm = word_to_mv(X, vecs, sq)
                for a in range(Dv):
                    lhs = GA.add(lhs, cmulv([basis[a], Xm, recip[a]], sq))
                rhs = {}
                for mono, c, w in contract(X):
                    rhs = GA.add(rhs, GA.scal(c * Fr(Dv) ** mono[0], word_to_mv(w, vecs, sq)))
                ok = ok and GA.eq(lhs, rhs)
                fp += sum(lhs.values(), Fr(0))
    return ok, fp


def check_contraction_rule_in_integer_dimensions():
    """(1) sum_a gamma_a X gamma^a equals the d-dimensional contraction rule at d = D, in Cl(D,0) for
    D = 4..8 and in Cl(1,D-1) for D = 4..6, for words X of length 0..4; the fingerprint of the explicit sums
    is pinned; control: d = 4 in place of D = 6 fails."""
    premise(P_DR)
    premise(P_QED)
    ok, fp = contraction_data()
    ok = ok and fp == FP_CONTRACTION
    sq = (1,) * 6
    vecs = {('v', 'x0'): gvec([1, 2, 0, -1, 3, 1]), ('v', 'x1'): gvec([2, -1, 1, 0, 1, -3])}
    X = (('v', 'x0'), ('v', 'x1'))
    lhs = {}
    for a in range(6):
        lhs = GA.add(lhs, cmulv([GA.gen(a), word_to_mv(X, vecs, sq), GA.gen(a)], sq))
    wrong = {}
    for mono, c, w in contract(X):
        wrong = GA.add(wrong, GA.scal(c * Fr(4) ** mono[0], word_to_mv(w, vecs, sq)))
    ok = ok and not GA.eq(lhs, wrong) and sum(lhs.values(), Fr(0)) == FP_CONTROL6
    GA.check("contraction rule gamma_a X gamma^a in Cl(D,0), D = 4..8, and Cl(1,D-1), D = 4..6", ok)
    return ok


def _poly_value(poly, Dv, sp):
    tot = Fr(0)
    for mono, c in poly.items():
        t = c * Fr(Dv) ** mono[0]
        for s, e in enumerate(mono[1:]):
            t *= sp[s] ** e
        tot += t
    return tot


TRACE_K, TRACE_L, TRACE_Q = [1, 2, -1, 0, 1, 2], [0, 1, 3, -2, 1, -1], [2, -1, 1, 1, 0, 3]
TRACE_DIMS = (4, 5, 6)


def trace_data():
    """returns (all agree, fingerprint = sum of the explicit traces over words and dimensions)."""
    ok, fp = True, Fr(0)
    for Dv in TRACE_DIMS:
        sq = (1,) * Dv
        kc, lc, qc = TRACE_K[:Dv], TRACE_L[:Dv], TRACE_Q[:Dv]
        k, l, q = gvec(kc), gvec(lc), gvec(qc)
        dotE = lambda a, b: sum(Fr(x) * Fr(y) for x, y in zip(a, b))
        sp = [dotE(kc, kc), dotE(lc, lc), dotE(qc, qc), dotE(kc, lc), dotE(kc, qc), dotE(lc, qc)]
        vecmap = {VK: k, VL: l, VQ: q, VKQ: GA.sub(k, q), VLQ: GA.sub(l, q), VR: GA.sub(k, l)}
        words = [(G_('m'), VK, G_('m'), VKQ)]
        for proj in ('delta', 'qq'):
            mu = nu = G_('m') if proj == 'delta' else VQ
            for al, be in ((G_('a'), G_('a')), (VR, VR)):
                words += [w for _, w, _ in two_loop_words(mu, nu, al, be)]
        for w in words:
            labels = sorted({s_[1] for s_ in w if s_[0] == 'i'})
            idx = [()]
            for _ in labels:
                idx = [t + (i,) for t in idx for i in range(Dv)]
            explicit = Fr(0)
            for t in idx:
                asg = dict(zip(labels, t))
                factors = [GA.gen(asg[s_[1]]) if s_[0] == 'i' else vecmap[s_] for s_ in w]
                explicit += 4 * cmulv(factors, sq).get((), Fr(0))
            ok = ok and explicit == _poly_value(trace(w), Dv, sp)
            fp += explicit
    return ok, fp


def check_diagram_traces_against_clifford_scalar_parts():
    """(1) the d-dimensional traces of the one-loop word and of the three two-loop words (indices
    contracted, Feynman part and gauge part, both projections) equal 4 <.>_0 of the explicit Clifford products
    with the indices summed over a basis, in Cl(D,0) for D = 4, 5, 6; fingerprint pinned; the one-loop trace
    is 4 (2 - d) k.(k - q) exactly."""
    premise(P_DR)
    premise(P_QED)
    ok, fp = trace_data()
    ok = ok and fp == FP_TRACES
    one = trace((G_('m'), VK, G_('m'), VKQ))
    kk = (0, 1, 0, 0, 0, 0, 0)
    kq = (0, 0, 0, 0, 0, 1, 0)
    ok = ok and one == {kk: Fr(8), kq: Fr(-8), (1, 1, 0, 0, 0, 0, 0): Fr(-4), (1, 0, 0, 0, 0, 1, 0): Fr(4)}
    GA.check("d-dimensional traces equal 4 <.>_0 of explicit Clifford products, D = 4, 5, 6", ok)
    return ok


def check_reduction_benchmarks():
    """(2) the reduction: I(1,1,1,1,0) = M1; I(1,1,1,1,-1) = -M1/2; I(0,1,1,1,1) = M2; the kite
    I(1,1,1,1,1) = 6 zeta_3 + O(eps) (the Euler constant and zeta_2 cancel in M2/M1)."""
    premise(P_DR)
    r = [I(1, 1, 1, 1, 0), I(1, 1, 1, 1, -1), I(0, 1, 1, 1, 1)]
    ok = r[0][0].eqrf(rfc(1)) and r[0][1].is_zero()
    ok = ok and r[1][0].eqrf(rfc(Fr(-1, 2))) and r[1][1].is_zero()
    ok = ok and r[2][0].is_zero() and r[2][1].eqrf(rfc(1))
    kite = I(1, 1, 1, 1, 1)
    S = sum_series(kite[0], kite[1])
    ok = ok and all(S.coef(n) == {} for n in range(-3, 2)) and coeff_is(S.coef(2), 0, 6)
    GA.check("reduction benchmarks: products of bubbles, nested bubble, kite = 6 zeta_3", ok)
    return ok


def check_one_loop_beta0_and_finite_part():
    """(3) one loop: Pi^(1) = -(4/3) a/eps + ..., so beta0 = 4/3; MS-bar finite part -20/9."""
    premise(P_QED)
    premise(P_DR)
    premise(P_ML)
    S = rf_series(one_loop_R0())
    # G(1,1) = g(eps)/eps, e^(gamma eps) g = 1 + 2 eps + O(eps^2)
    if lngamma_coeffs([(1, 1), (2, -1), (-1, -2)], 1) != -1:
        return False
    cm1, c0 = S.coef(0), S.coef(1)
    beta0 = -cm1.get((0, 0, 0), Fr(0))
    finite = c0.get((0, 0, 0), Fr(0)) + 2 * cm1.get((0, 0, 0), Fr(0))
    ok = beta0 == Fr(4, 3) and finite == Fr(-20, 9)
    GA.check("one loop: beta0 = 4/3, MS-bar finite part -20/9", ok)
    return ok


def check_two_loop_simple_pole_beta1_and_finite_part():
    """(4) two loops (sum of three diagrams): no 1/eps^3 or 1/eps^2; Pi^(2) = a^2 (-2/eps + ...) so
    beta1 = 4; MS-bar finite part 16 zeta_3 - 55/3; in alpha: 2 alpha^2/(3 pi) + alpha^3/(2 pi^2)."""
    premise(P_QED)
    premise(P_DR)
    premise(P_ML)
    premise(P_TREE)
    R = project_two_loop('delta')
    S = sum_series(*pi2_coefficients(R['feyn']))
    ok = all(S.coef(n) == {} for n in range(-3, 1))
    h1, h2 = S.coef(1), S.coef(2)
    ok = ok and coeff_is(h1, -2)
    beta1 = -2 * h1.get((0, 0, 0), Fr(0))
    beta0 = -rf_series(one_loop_R0()).coef(0).get((0, 0, 0), Fr(0))
    fin_rat = h2.get((0, 0, 0), Fr(0)) + 4 * h1.get((0, 0, 0), Fr(0))
    ok = ok and beta1 == 4 and fin_rat == Fr(-55, 3) and h2.get((1, 0, 0), Fr(0)) == 16
    # mu dalpha/dmu = 2 (4 pi) [beta0 (alpha/4pi)^2 + beta1 (alpha/4pi)^3]: coefficients of
    # alpha^2/pi and alpha^3/pi^2
    c2 = Fr(8) * beta0 / 16
    c3 = Fr(8) * beta1 / 64
    ok = ok and c2 == Fr(2, 3) and c3 == Fr(1, 2)
    GA.check("two loops: simple pole only, beta1 = 4, finite part 16 zeta_3 - 55/3", ok)
    return ok


def check_gauge_independence_and_transversality():
    """(4) the coefficient of (1 - xi) vanishes identically in d (both masters) and q_mu q_nu Pi^{mu nu}
    vanishes identically in d at two loops, in the Feynman part and the gauge part."""
    premise(P_ML)
    premise(P_DR)
    R = project_two_loop('delta')
    Q = project_two_loop('qq')
    ok = R['xi'][0].is_zero() and R['xi'][1].is_zero()
    ok = ok and all(Q[p][i].is_zero() for p in ('feyn', 'xi') for i in (0, 1))
    # control: the gauge part of the vertex diagram alone does not vanish
    one = project_two_loop('delta', 'vx')['xi']
    ok = ok and not (one[0].is_zero() and one[1].is_zero())
    GA.check("two loops: xi independent and transverse, identically in d", ok)
    return ok


def check_subdivergences_cancel_between_vertex_and_self_energy():
    """(5) in the Feynman gauge the self-energy insertions and the vertex correction each have a
    1/eps^2 pole, equal and opposite: the one-loop counterterms cancel in pairs (Z1 = Z2)."""
    premise(P_QED)
    premise(P_DR)
    se = GA.RF0, GA.RF0
    for name in ('se1', 'se2'):
        x = project_two_loop('delta', name)['feyn']
        se = (se[0] + x[0], se[1] + x[1])
    vx = project_two_loop('delta', 'vx')['feyn']
    Sse = sum_series(*pi2_coefficients(se))
    Svx = sum_series(*pi2_coefficients(vx))
    a = Sse.coef(0).get((0, 0, 0), Fr(0))
    b = Svx.coef(0).get((0, 0, 0), Fr(0))
    ok = a != 0 and a + b == 0 and Sse.coef(-1) == {} and Svx.coef(-1) == {}
    ok = ok and a == Fr(4, 3) and b == Fr(-4, 3)
    GA.check("subdivergences: self-energy 1/eps^2 = 4/3 a^2, vertex -4/3 a^2, sum 0", ok)
    return ok


# ---- the Ward-Takahashi identity at two loops in Cl(1,3) (massive, unit outside) ----

S13 = (1, -1, -1, -1)
FP_WARD = Fr(16462924192730412, 55021266940681015)   # sum of coefficients of the insertion sums (computed)


def v13(c):
    return gvec(c)


def Q13(v):
    return GA.mul(v, v, S13).get((), Fr(0))


def prop13(k, m):
    """S(k) = (k - m)^(-1) = (k + m)/(Q(k) - m^2), the unit and the i of the Feynman rule outside."""
    return GA.scal(Fr(1) / (Q13(k) - m * m), GA.add(k, GA.sc(m)))


def chain(verts, moms, m):
    """V0 S(p1) V1 S(p2) ... S(pn) Vn."""
    out = verts[0]
    for p, vv in zip(moms, verts[1:]):
        out = cmulv([out, prop13(p, m), vv], S13)
    return out


def insertion_sum(verts, moms, h, m):
    """sum_j V0 S(p1+h) ... S(pj+h) h S(pj) ... S(pn) Vn."""
    tot = {}
    n = len(moms)
    for j in range(n):
        out = verts[0]
        for i in range(n):
            if i < j:
                out = cmulv([out, prop13(GA.add(moms[i], h), m), verts[i + 1]], S13)
            elif i == j:
                out = cmulv([out, prop13(GA.add(moms[i], h), m), h, prop13(moms[i], m), verts[i + 1]], S13)
            else:
                out = cmulv([out, prop13(moms[i], m), verts[i + 1]], S13)
        tot = GA.add(tot, out)
    return tot


def check_ward_identity_at_two_loops_integrand_by_integrand():
    """(6) Cl(1,3), massive lines, unit outside the product: for the open fermion line of the rainbow, the
    crossed and the polarisation-insertion self-energies, the sum of insertions of h (vertex h) equals
    -(chain(p + h) - chain(p)); for the closed loop the insertions telescope to a difference of the same
    integrand at loop momenta l + h and l (zero after the shift). Derivative: dS(k + t h)/dt = -S h S."""
    premise(P_QED)
    premise(P_TREE)
    premise(P_DR)
    m = Fr(3, 2)
    p, k, l, h = v13([2, 1, 0, 1]), v13([1, -1, 2, 0]), v13([3, 0, 1, -1]), v13([1, 2, -1, 1])
    g = [GA.gen(i) for i in range(4)]
    vt = [g[0], g[2], g[2], g[0]]
    pk, pkl, pl = GA.sub(p, k), GA.sub(GA.sub(p, k), l), GA.sub(p, l)
    ok, fp = True, Fr(0)
    cases = [(vt, [pk, pkl, pk]),                       # rainbow
             ([g[0], g[2], g[0], g[2]], [pk, pkl, pl]),  # crossed
             ([g[1], g[3]], [pk])]                       # open line of the polarisation insertion
    for verts, moms in cases:
        lhs = insertion_sum(verts, moms, h, m)
        shifted = chain(verts, [GA.add(x, h) for x in moms], m)
        ok = ok and GA.eq(lhs, GA.neg(GA.sub(shifted, chain(verts, moms, m))))
        fp += sum(lhs.values(), Fr(0))
    # closed loop tr[g_a S(l) g_b S(l - k)] with insertions on both propagators
    lk = GA.sub(l, k)
    loop_ins = GA.add(cmulv([g[1], prop13(GA.add(l, h), m), h, prop13(l, m), g[3], prop13(lk, m)], S13),
                      cmulv([g[1], prop13(GA.add(l, h), m), g[3], prop13(GA.add(lk, h), m), h,
                             prop13(lk, m)], S13))
    loop_diff = GA.sub(cmulv([g[1], prop13(GA.add(l, h), m), g[3], prop13(GA.add(lk, h), m)], S13),
                       cmulv([g[1], prop13(l, m), g[3], prop13(lk, m)], S13))
    ok = ok and loop_ins.get((), Fr(0)) == -loop_diff.get((), Fr(0))
    ok = ok and GA.eq(loop_ins, GA.neg(loop_diff))
    fp += loop_ins.get((), Fr(0))
    ok = ok and fp == FP_WARD
    # derivative of one propagator along h at t = 0
    den = Q13(k) - m * m
    kh = GA.mul(k, h, S13).get((), Fr(0))
    dS = GA.sub(GA.scal(Fr(1) / den, h), GA.scal(2 * kh / (den * den), GA.add(k, GA.sc(m))))
    ok = ok and GA.eq(dS, GA.neg(cmulv([prop13(k, m), h, prop13(k, m)], S13)))
    # controls: the insertion sum without the middle insertion fails; with the vertex g0 in place of h fails
    verts, moms = cases[0]
    full = insertion_sum(verts, moms, h, m)
    middle = cmulv([verts[0], prop13(GA.add(moms[0], h), m), verts[1], prop13(GA.add(moms[1], h), m), h,
                    prop13(moms[1], m), verts[2], prop13(moms[2], m), verts[3]], S13)
    shifted = chain(verts, [GA.add(x, h) for x in moms], m)
    target = GA.neg(GA.sub(shifted, chain(verts, moms, m)))
    ok = ok and not GA.eq(GA.sub(full, middle), target)
    wrongv = {}
    for jj in range(3):
        fac = [verts[0]]
        for ii in range(3):
            if ii == jj:
                fac += [prop13(GA.add(moms[ii], h), m), g[0], prop13(moms[ii], m), verts[ii + 1]]
            else:
                fac += [prop13(GA.add(moms[ii], h) if ii < jj else moms[ii], m), verts[ii + 1]]
        wrongv = GA.add(wrongv, cmulv(fac, S13))
    ok = ok and not GA.eq(wrongv, target)
    GA.check("two-loop Ward-Takahashi identity integrand by integrand (open lines, closed loop, derivative)", ok)
    return ok
