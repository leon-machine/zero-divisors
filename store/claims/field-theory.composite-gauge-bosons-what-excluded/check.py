"""field-theory.composite-gauge-bosons-what-excluded: exact checks of the computable part.

Spacetime algebra Cl(1,3) (GA, Fraction), complex numbers as the span{1, I4} parts; spinors are massless chi_+
spinors in ker k for rational null k, the GA current J^mu(f, g) = proj(f* g0 g^mu g) (T03's *).
(1) Covariance J(S f, S g) = S J(f, g) S~ (real and I4 parts of J as vectors) for six rotors (two boosts, two
    rotations, boost x rotation in non-commuting planes, a product of three) and three spinor pairs; and as an
    identity of the bilinear for three further elements of definite parity (an odd vector, an even 1 + I4/3, an
    even sum of bivectors). Control: it fails for the mixed-parity 1 + g0.
(2) A nonzero vector condensate picks a direction: each computed current vector is moved by one of two boost
    rotors, while a Lorentz scalar (span{1, I4}) is fixed by every rotor.
The Weinberg-Witten exclusion, the Bjorken route and the author's choice of the elementary route are literature
and narrative, not computed.
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



PAIRS = [((5, 3, 4, 0), (3, 2, 1, 2)), ((9, 1, 4, 8), (7, 2, 3, 6)), ((13, 5, 12, 0), (5, 0, -3, 4))]


def _rotors():
    Rb = GA.add(GA.sc(F(5, 4)), _scl(F(3, 4), {(0, 1): F(1)}))
    Rr = GA.add(GA.sc(F(3, 5)), _scl(F(4, 5), {(1, 2): F(1)}))
    Rb2 = GA.add(GA.sc(F(13, 5)), _scl(F(12, 5), {(0, 2): F(1)}))
    Rr2 = GA.add(GA.sc(F(5, 13)), _scl(F(12, 13), {(2, 3): F(1)}))
    return [Rb, Rr, Rb2, Rr2, GA.mul(Rb, Rr, S4), GA.mul(GA.mul(Rb2, Rr2, S4), Rr, S4)]


def _vecs(J):
    a = {(mu,): J[mu].re for mu in range(4) if J[mu].re != 0}
    b = {(mu,): J[mu].im for mu in range(4) if J[mu].im != 0}
    return a, b


def _covariant(S, k1, k3):
    f1, f3 = _spinor(k1), _spinor(k3)
    a, b = _vecs(_cur(f3, f1))
    ar, br = _vecs(_cur(GA.mul(S, f3, S4), GA.mul(S, f1, S4)))
    St = GA.reverse(S)
    return GA.eq(ar, GA.mul(GA.mul(S, a, S4), St, S4)) and GA.eq(br, GA.mul(GA.mul(S, b, S4), St, S4))


# Sample definite-parity elements (odd g1, even 1 + I4/3, even bivector sum) for the covariance law,
# and a mixed-parity control 1 + g0 with the spinor pair it is tested on.
DEFINITE_PARITY = [GA.gen(1), GA.add(GA.sc(1), _scl(F(1, 3), I4)),
                   GA.add({(0, 1): F(1)}, {(2, 3): F(1)}, {(1, 3): F(1)})]
MIXED_CONTROL = GA.add(GA.sc(1), GA.gen(0))
CONTROL_PAIR = PAIRS[0]


def check_current_transforms_as_a_vector():
    ok = True
    for R in _rotors():
        ok = ok and GA.eq(GA.mul(R, GA.reverse(R), S4), GA.sc(1))
        for k1, k3 in PAIRS:
            ok = ok and _covariant(R, k1, k3)
    for S in DEFINITE_PARITY:
        ok = ok and all(_covariant(S, k1, k3) for k1, k3 in PAIRS)
    ok = ok and not _covariant(MIXED_CONTROL, *CONTROL_PAIR)
    GA.check("J(S f, S g) = S J S~ for rotors and definite-parity elements; fails for 1 + g0", ok)
    return ok


BOOSTS = [_rotors()[0], _rotors()[2]]
SCALAR_Z = GA.add(GA.sc(F(2)), _scl(F(-3), I4))
BIVS = [{(m, n): F(1)} for m in range(4) for n in range(m + 1, 4)]


def _moved(R, v):
    return GA.mul(GA.mul(R, v, S4), GA.reverse(R), S4)


def _broken_rank(v):
    """Rank of {B x v} over the six generators B of so(1,3), x the commutator product."""
    rows = []
    for B in BIVS:
        c = _scl(F(1, 2), GA.sub(GA.mul(B, v, S4), GA.mul(v, B, S4)))
        rows.append([c.get(b, F(0)) for b in GA.all_blades(4)])
    return GA.field_rank(rows)


def check_vector_condensate_breaks_lorentz():
    ok = True
    # By hand: R = a + b g0g1 with (a, b) = (5/4, 3/4) gives R g0 R~ = (a^2 + b^2) g0 - 2ab g1 = 17/8 g0 - 15/8 g1;
    # (a, b) = (13/5, 12/5) in the g0g2 plane gives 313/25 g0 - 312/25 g2. The time direction is moved.
    ok = ok and GA.eq(_moved(BOOSTS[0], G0), {(0,): F(17, 8), (1,): F(-15, 8)})
    ok = ok and GA.eq(_moved(BOOSTS[1], G0), {(0,): F(313, 25), (2,): F(-312, 25)})
    for k1, k3 in PAIRS:
        a, b = _vecs(_cur(_spinor(k3), _spinor(k1)))
        ok = ok and not (GA.is_zero(a) and GA.is_zero(b))
        for v in (a, b):
            if not GA.is_zero(v):
                ok = ok and any(not GA.eq(_moved(R, v), v) for R in BOOSTS)
                # a nonzero vector's stabiliser in so(1,3) is 3-dimensional: 6 - 3 = 3 generators broken
                ok = ok and _broken_rank(v) == 3
    ok = ok and _broken_rank(SCALAR_Z) == 0
    ok = ok and all(GA.eq(_moved(R, SCALAR_Z), SCALAR_Z) for R in _rotors())
    GA.check("a nonzero current vector is moved by a boost; span{1, I4} is fixed by every rotor", ok)
    return ok
