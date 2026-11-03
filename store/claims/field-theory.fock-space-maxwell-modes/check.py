"""field-theory.fock-space-maxwell-modes: exact checks.

(1) Bargmann-Fock: polynomials in four variables with span{1, I4} coefficients (Gaussian rationals),
    a_m = d/dz_m, a_m* = z_m: [a_m, a_n*] = delta_mn, [a_m, a_n] = [a_m*, a_n*] = 0 exactly on all 210 monomials of
    degree <= 6 (with the coefficient 2/3 - (5/7) i), and <a_m* p, q> = <p, a_m q> for
    <z^n, z^n'> = n! delta (antilinear in the first slot) on a sample of monomial pairs; the form is positive.
(2) For null k = g0 + n (six unit directions n, four off the axes) the bivectors f with k f = 0 form a real
    2-dimensional space (6 - rank 4), and it is I4-stable (k I4 f = 0, I4 f != f): one I4-complex mode.
(3) With a rational right-handed frame (t1, t2, n): A = t1 cos + t2 sin has F = grad A = f(cos - sigma I4 sin), and
    sigma is the same (+1) in every direction, i.e. f exp(-I4 k.x); a rotation by theta about n (half angle with
    cos, sin = 4/5, 3/5) acts on the mode space as cos theta + lam sin theta I4 with lam = -sigma (helicity +1); every
    massless even spinor in ker k, chi_+ and chi_- alike, satisfies R phi = (cos a + mu sin a I4) phi with one mu
    in every direction, and mu has the sign that makes the helicity -mu/2 = +1/2 (same sign as the photon's).
(4) With i = I4 the quantised helicity +1 wave keeps only its annihilation coefficient (X + I4 Y) and the
    helicity -1 wave only its creation coefficient (X - I4 Y), in all six directions: the Riemann-Silberstein form.
    On bivectors T03's * is +1 on the electric g_k g_0 blades and -1 on the magnetic g_i g_j blades.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

QI = GA.QI
S4 = (1, -1, -1, -1)
I4 = {(0, 1, 2, 3): F(1)}
IS3 = {(1, 2): F(-1)}                      # I sigma_3 = gamma_2 gamma_1
G0 = GA.gen(0)
EVEN = [{b: F(1)} for b in GA.all_blades(4) if len(b) % 2 == 0]
GUP = [GA.gen(0), GA.neg(GA.gen(1)), GA.neg(GA.gen(2)), GA.neg(GA.gen(3))]


def _scl(c, x):
    out = {}
    for b, v in x.items():
        w = c * v
        if w != 0:
            out[b] = w
    return out


def _star(x, s):
    """T03's *: reversion, sign -1 per negative-square generator, conjugation of Q(i) coefficients."""
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        out[b] = sign * (c.conj() if isinstance(c, QI) else c)
    return {b: c for b, c in out.items() if c != 0}


def _chi(e, p):
    return _scl(F(1, 2), GA.sub(p, _scl(F(e), GA.mul(GA.mul(I4, p, S4), IS3, S4))))


def _proj(x):
    """span{1, I4} part over the ground (tower blades carried along)."""
    out = {}
    for b, c in x.items():
        g = tuple(i for i in b if i < 4)
        if g == () or g == (0, 1, 2, 3):
            out[b] = c
    return out


def _kvec(k):
    return GA.add(*[_scl(F(k[i]), GA.gen(i)) for i in range(4) if k[i] != 0])


def _spinor(k, e=1):
    """The first nonzero (k g0 / 2k^0) chi_e(even blade): a chirality-e massless spinor in ker k."""
    for b in EVEN:
        f = _scl(F(1) / (2 * F(k[0])), GA.mul(GA.mul(_kvec(k), G0, S4), _chi(e, b), S4))
        if not GA.is_zero(f):
            return f


def _to_q(x):
    return QI(x.get((), F(0)), x.get((0, 1, 2, 3), F(0)))


def _qmv(z):
    return GA.add(GA.sc(z.re), _scl(z.im, I4))


def _cur(a, b):
    """GA current J^mu(a, b) = proj(a* g0 g^mu b) in span{1, I4}, as Gaussian rationals."""
    return [_to_q(_proj(GA.mul(GA.mul(GA.mul(_star(a, S4), G0, S4), GUP[mu], S4), b, S4))) for mu in range(4)]


def _mdot(J1, J2):
    return J1[0] * J2[0] - J1[1] * J2[1] - J1[2] * J2[2] - J1[3] * J2[3]


def _plane(q):
    e_, f_ = 4 + 2 * q, 5 + 2 * q
    return (GA.add(_scl(F(1, 2), GA.gen(e_)), _scl(F(1, 2), GA.gen(f_))),
            GA.add(_scl(F(1, 2), GA.gen(e_)), _scl(F(-1, 2), GA.gen(f_))))


def _isqrt(n):
    """Integer square root by Newton's method (integers only)."""
    if n < 2:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x



NM = 4
ZC = QI(F(2, 3), F(-5, 7))
NDIRS = [(F(1), F(0), F(0)), (F(0), F(0), F(-1)), (F(3, 5), F(4, 5), F(0)), (F(2, 3), F(1, 3), F(2, 3)),
         (F(-6, 9), F(-6, 9), F(3, 9)), (F(1, 9), F(-4, 9), F(-8, 9))]
BIV = [{b: F(1)} for b in GA.all_blades(4) if len(b) == 2]
HALF = (F(4, 5), F(3, 5))
# Bargmann-Fock samples: every monomial in NM variables of degree <= MAX_DEG (C(6 + 4, 4) = 210 of them),
# every ADJ_STRIDE-th one for the adjoint test, with sample complex coefficients for the two states.
MAX_DEG = 6
MONOS = [e for e in product(range(MAX_DEG + 1), repeat=NM) if sum(e) <= MAX_DEG]
ADJ_STRIDE = 7
P_COEF, Q_COEF = QI(1, 2), QI(F(-1, 3), 1)


def _fact(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def _pa(m, p):
    out = {}
    for e, c in p.items():
        if e[m] > 0:
            e2 = e[:m] + (e[m] - 1,) + e[m + 1:]
            out[e2] = out.get(e2, QI(0)) + c * QI(e[m])
    return {e: c for e, c in out.items() if c != QI(0)}


def _pad(m, p):
    out = {}
    for e, c in p.items():
        e2 = e[:m] + (e[m] + 1,) + e[m + 1:]
        out[e2] = out.get(e2, QI(0)) + c
    return out


def _psub(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, QI(0)) - c
    return {e: c for e, c in out.items() if c != QI(0)}


def _ip(p, q):
    tot = QI(0)
    for e, c in p.items():
        if e in q:
            w = 1
            for n in e:
                w *= _fact(n)
            tot = tot + c.conj() * q[e] * QI(w)
    return tot


def _frame(n):
    E = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    n = list(n)
    if n == E[2]:
        return E[0], E[1]
    if n == [F(0), F(0), F(-1)]:
        return E[1], E[0]
    m = [n[0], n[1], n[2] - 1]
    mm = sum(x * x for x in m)
    R = lambda x: [x[i] - 2 * sum(x[j] * m[j] for j in range(3)) * m[i] / mm for i in range(3)]
    return R(E[1]), R(E[0])


def _svec(t):
    return GA.add(*[_scl(F(t[i]), GA.gen(1 + i)) for i in range(3) if t[i] != 0])


def _cross(x, y):
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]


def _m(x, y):
    return GA.mul(x, y, S4)


def check_bargmann_fock_ccr_and_adjoint():
    monos = MONOS
    ok = len(monos) == 210
    for e in monos:
        p = {e: ZC}
        for m in range(NM):
            for n in range(NM):
                ok = ok and _psub(_pa(m, _pad(n, p)), _pad(n, _pa(m, p))) == (p if m == n else {})
                ok = ok and _psub(_pa(m, _pa(n, p)), _pa(n, _pa(m, p))) == {}
                ok = ok and _psub(_pad(m, _pad(n, p)), _pad(n, _pad(m, p))) == {}
    sample = monos[::ADJ_STRIDE]
    for e1 in sample:
        p = {e1: P_COEF}
        for e2 in sample:
            q = {e2: Q_COEF}
            ok = ok and all(_ip(_pad(m, p), q) == _ip(p, _pa(m, q)) for m in range(NM))
        ok = ok and _ip(p, p).im == 0 and _ip(p, p).re > 0
    GA.check("Bargmann-Fock CCR on all monomials of degree <= 6 and a_m* adjoint to a_m for <z^n, z^n'> = n!", ok)
    return ok


def check_one_complex_mode_per_null_momentum():
    ok = True
    for n in NDIRS:
        ok = ok and sum(x * x for x in n) == 1
        t1, t2 = _frame(n)
        kv = GA.add(GA.gen(0), _svec(n))
        cols = [_m(kv, b) for b in BIV]
        keys = sorted(set(k for c in cols for k in c))
        rk = GA.mat_rank([[c.get(k, F(0)) for c in cols] for k in keys])
        f = _m(kv, _svec(t2))
        ok = ok and _cross(t1, t2) == list(n) and 6 - rk == 2 and GA.is_zero(_m(kv, f))
        ok = ok and GA.is_zero(_m(kv, _m(I4, f))) and not GA.is_zero(f) and all(len(b) == 2 for b in f)
        ok = ok and not GA.eq(_m(I4, f), f)
    GA.check("for null k the bivectors with k f = 0 form a real 2-dimensional I4-stable space", ok)
    return ok


def check_positive_frequency_is_positive_helicity():
    ca, sa = HALF
    ct, st = ca * ca - sa * sa, 2 * sa * ca
    sigs, lams, mus = set(), set(), set()
    ok = True
    count = 0
    for n in NDIRS:
        t1, t2 = _frame(n)
        T1, T2 = _svec(t1), _svec(t2)
        kv = GA.add(GA.gen(0), _svec(n))
        f, g = _m(kv, T2), _m(kv, T1)
        sig = [s for s in (1, -1) if GA.eq(g, _scl(F(s), _m(I4, f)))]
        Bn = _m(T1, T2)
        R = [Rc for Rc in (GA.add(GA.sc(ca), _scl(F(s) * sa, Bn)) for s in (1, -1))
             if GA.eq(_m(_m(Rc, T1), GA.reverse(Rc)), GA.add(_scl(ct, T1), _scl(st, T2)))]
        ok = ok and len(sig) == 1 and len(R) == 1
        R = R[0]
        lam = [s for s in (1, -1) if GA.eq(_m(_m(R, f), GA.reverse(R)), GA.add(_scl(ct, f), _scl(F(s) * st, _m(I4, f))))]
        ok = ok and len(lam) == 1
        sigs.add(sig[0])
        lams.add(lam[0])
        for e in (1, -1):
            for b in EVEN:
                phi = _scl(F(1) / 2, _m(_m(kv, G0), _chi(e, b)))
                if not GA.is_zero(phi):
                    mu = [s for s in (1, -1) if GA.eq(_m(R, phi), GA.add(_scl(ca, phi), _scl(F(s) * sa, _m(I4, phi))))]
                    ok = ok and len(mu) == 1
                    mus.add(mu[0])
                    count += 1
    ok = ok and sigs == {1} and lams == {-1} and mus == {-1} and count > 0
    sigma, mu = next(iter(sigs)), next(iter(mus))
    ok = ok and sigma * F(-mu, 2) > 0
    GA.check("f exp(-I4 k.x) has helicity +1 in every direction; every massless even spinor has helicity +1/2", ok)
    return ok


def check_riemann_silberstein_field():
    ok = True
    for n in NDIRS:
        t1, t2 = _frame(n)
        kv = GA.add(GA.gen(0), _svec(n))
        T1, T2 = _svec(t1), _svec(t2)
        for hel in (1, -1):
            X, Y = _scl(F(hel), _m(kv, T2)), GA.neg(_m(kv, T1))
            ann, cre = GA.add(X, _m(I4, Y)), GA.sub(X, _m(I4, Y))
            if hel == 1:
                ok = ok and GA.is_zero(cre) and not GA.is_zero(ann)
            else:
                ok = ok and GA.is_zero(ann) and not GA.is_zero(cre)
    for b in BIV:
        elec = next(iter(b))[0] == 0
        ok = ok and GA.eq(_star(b, S4), b if elec else GA.neg(b))
    GA.check("i = I4: helicity +1 keeps only a_+, helicity -1 only a_-*; * is +1 electric, -1 magnetic", ok)
    return ok
