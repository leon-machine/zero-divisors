"""field-theory.how-close-tower-comes-ccr: exact checks.

Cl(1,3) ground with 2n tower planes (c_j, d_j for j = 1..n), modes v = (e + f)/2, w = (e - f)/2 (the CAR of Fact
field-theory.imported-tower-limit), N_c + N_d the total number, B = sum_j w_cj w_dj, B* by T03's *.
For n = 1, 2, 3, 4:
(1) [B, B*] = n - (N_c + N_d) exactly.
(2) With K3 = (N_c + N_d - n)/2: [K3, B*] = B*, [K3, B] = -B, [B, B*] = -2 K3: an su(2) quasi-spin.
(3) On the symmetric k-pair states (B*)^k vacuum, k = 0..n, [B, B*] acts as n - 2k (so [b, b*] = 1 - 2k/n for
    b = B/sqrt(n)), every such state is nonzero, and (B*)^(n+1) vacuum = 0: a ladder of exactly n + 1 states.
The n -> infinity contraction and the bounded-number limit are read off (3), not computed as limits.
"""
from fractions import Fraction as F

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



NS = [1, 2, 3, 4]
ONE_QUANTUM_PLANE = 0      # the plane whose creation operator makes the sample one-quantum state


def _system(n):
    STn = tuple(list(S4) + [1, -1] * (2 * n))
    pl = [_plane(j) for j in range(2 * n)]
    m = lambda x, y: GA.mul(x, y, STn)
    B = GA.add(*[m(pl[2 * j][1], pl[2 * j + 1][1]) for j in range(n)])
    Bd = _star(B, STn)
    N = GA.add(*[m(v, w) for (v, w) in pl])
    vac = {(): F(1)}
    for (v, w) in pl:
        vac = m(vac, m(w, v))
    return STn, m, B, Bd, N, vac


def check_commutator_is_n_minus_number():
    premise("field-theory.imported-tower-limit")
    ok = True
    for n in NS:
        STn, m, B, Bd, N, vac = _system(n)
        c = GA.sub(m(B, Bd), m(Bd, B))
        ok = ok and GA.eq(c, GA.sub(GA.sc(n), N))
        v, _w = _plane(ONE_QUANTUM_PLANE)
        one = m(v, vac)
        # one is a nonzero one-quantum state (N one = one), on which [B, B*] acts as n - 1
        ok = ok and not GA.is_zero(one) and GA.eq(m(N, one), one)
        ok = ok and GA.eq(m(c, one), _scl(F(n - 1), one))
    GA.check("[B, B*] = n - (N_c + N_d) for n = 1..4", ok)
    return ok


def check_quasi_spin_su2():
    premise("field-theory.imported-tower-limit")
    ok = True
    for n in NS:
        STn, m, B, Bd, N, vac = _system(n)
        K3 = _scl(F(1, 2), GA.sub(N, GA.sc(n)))
        c = GA.sub(m(B, Bd), m(Bd, B))
        ok = ok and GA.eq(GA.sub(m(K3, Bd), m(Bd, K3)), Bd) and GA.eq(GA.sub(m(K3, B), m(B, K3)), GA.neg(B))
        ok = ok and GA.eq(c, _scl(F(-2), K3))
    GA.check("(B*, B, K3) close as su(2): [K3, B*] = B*, [K3, B] = -B, [B, B*] = -2 K3", ok)
    return ok


def check_finite_ladder():
    premise("field-theory.imported-tower-limit")
    ok = True
    for n in NS:
        STn, m, B, Bd, N, vac = _system(n)
        c = GA.sub(m(B, Bd), m(Bd, B))
        st = vac
        for k in range(n + 1):
            ok = ok and not GA.is_zero(st) and GA.eq(m(c, st), _scl(F(n - 2 * k), st))
            st = m(Bd, st)
        ok = ok and GA.is_zero(st)
    GA.check("[B, B*] = n - 2k on k-pair states, (B*)^(n+1) vacuum = 0: n + 1 states", ok)
    return ok
