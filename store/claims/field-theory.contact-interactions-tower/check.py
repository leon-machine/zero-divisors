"""field-theory.contact-interactions-tower: exact checks.

Cl(1,3) ground with four tower planes (generators 4..11): modes A k1 (plane 0), B k2 (1), A k3 (2), B k4 (3);
v = (e + f)/2 creates, w = (e - f)/2 annihilates; fields Psi_A = u1 w_0 + u3 w_2, Psi_B = u2 w_1 + u4 w_3 with u
massless chi_+ spinors in ker k; currents J^mu = proj(Psi* g0 g^mu Psi); H = g J_A . J_B (g = 1).
(1) H* = H; H commutes with both charges Q_A = n_0 + n_2, Q_B = n_1 + n_3; H has tower components of grade 4.
(2) The vacuum matrix element <A3 B4|H|A1 B2> lies in span{1, I4} times the vacuum and equals J_A(3,1) . J_B(4,2)
    from the GA spinor currents (three configurations); each J(f, f) = c k with c > 0; and the normalised
    |M|^2 / (c1 c2 c3 c4 s^2) is exactly 1/4 at six configurations (three angles at energy 10, energies 26 and 6).
(3) With the second species as antiparticles (Psi_B = u2 v_1 + u4 v_3), the amplitude is the crossed
    -J_A(3,1) . J_B(2,4), and |M|^2 / (c1 c2 c3 c4 u^2) = 1/4 at the six configurations.
(4) A boost of a whole configuration keeps the spinors chiral and in ker k', keeps |M|^2 and s; fresh spinors built
    in the boosted (non-centre-of-mass) frame give the same normalised 1/4.
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



NPL = 4
ST = tuple(list(S4) + [1, -1] * NPL)
CONFIGS = [((5, 3, 4, 0), (5, -3, -4, 0), (5, 0, 0, 5), (5, 0, 0, -5)),
           ((5, 3, 4, 0), (5, -3, -4, 0), (5, 4, 0, 3), (5, -4, 0, -3)),
           ((5, 3, 4, 0), (5, -3, -4, 0), (5, 0, 3, 4), (5, 0, -3, -4)),
           ((5, 3, 4, 0), (5, -3, -4, 0), (5, -3, 4, 0), (5, 3, -4, 0)),
           ((13, 5, 12, 0), (13, -5, -12, 0), (13, 12, 0, 5), (13, -12, 0, -5)),
           ((3, 1, 2, 2), (3, -1, -2, -2), (3, 2, 2, 1), (3, -2, -2, -1))]
BOOST = (F(5, 4), F(3, 4))


def _m(x, y):
    return GA.mul(x, y, ST)


def _pl():
    return [_plane(q) for q in range(NPL)]


def _fieldcur(Psi):
    return [_proj(_m(_m(_m(_star(Psi, ST), G0), GUP[mu]), Psi)) for mu in range(4)]


def _H(us, anti=False):
    PL = _pl()
    PsiA = GA.add(_m(us[0], PL[0][1]), _m(us[2], PL[2][1]))
    k = 0 if anti else 1
    PsiB = GA.add(_m(us[1], PL[1][k]), _m(us[3], PL[3][k]))
    JA, JB = _fieldcur(PsiA), _fieldcur(PsiB)
    H = _m(JA[0], JB[0])
    for i in range(1, 4):
        H = GA.sub(H, _m(JA[i], JB[i]))
    return H


def _vac():
    P0 = GA.sc(1)
    for (v, w) in _pl():
        P0 = _m(P0, _m(w, v))
    return P0


def _amplitude(H):
    PL = _pl()
    P0 = _vac()
    X = _m(_m(_m(_m(_m(_m(P0, PL[3][1]), PL[2][1]), H), PL[0][0]), PL[1][0]), P0)
    b0, c0 = next(iter(P0.items()))
    a_ = X.get(b0, F(0)) / c0
    I4P0 = GA.mul(I4, P0, ST)
    bb, cc = next(iter(I4P0.items()))
    b_ = GA.sub(X, _scl(a_, P0)).get(bb, F(0)) / cc
    return QI(a_, b_), GA.eq(X, GA.add(_scl(a_, P0), _scl(b_, I4P0)))


def _cnorm(k, f):
    J = _cur(f, f)
    c = J[0].re / F(k[0])
    return c, all(J[mu] == QI(c * F(k[mu])) for mu in range(4)) and c > 0


def _mink(p):
    return p[0] * p[0] - p[1] * p[1] - p[2] * p[2] - p[3] * p[3]


def _ratio(cf, crossed=False):
    us = [_spinor(k) for k in cf]
    z = _mdot(_cur(us[2], us[0]), _cur(us[3], us[1]))
    cs = [_cnorm(k, f) for k, f in zip(cf, us)]
    if crossed:
        z = _mdot(_cur(us[2], us[0]), _cur(us[1], us[3]))
        p = [cf[0][i] - cf[3][i] for i in range(4)]
    else:
        p = [cf[0][i] + cf[1][i] for i in range(4)]
    c = cs[0][0] * cs[1][0] * cs[2][0] * cs[3][0]
    return (z.re ** 2 + z.im ** 2) / (c * F(_mink(p)) ** 2), all(o for _, o in cs)


def _boost_k(k):
    R = GA.add(GA.sc(BOOST[0]), _scl(BOOST[1], {(0, 3): F(1)}))
    kv = GA.mul(GA.mul(R, _kvec(k), S4), GA.reverse(R), S4)
    return tuple(kv.get((i,), F(0)) for i in range(4)), R


def check_contact_term_structure():
    cf = CONFIGS[0]
    H = _H([_spinor(k) for k in cf])
    PL = _pl()
    QA = GA.add(_m(PL[0][0], PL[0][1]), _m(PL[2][0], PL[2][1]))
    QB = GA.add(_m(PL[1][0], PL[1][1]), _m(PL[3][0], PL[3][1]))
    grades = {len([i for i in b if i >= 4]) for b in H}
    ok = GA.eq(_star(H, ST), H) and GA.commutes(H, QA, ST) and GA.commutes(H, QB, ST) and 4 in grades
    ok = ok and all(cf[0][t] + cf[1][t] == cf[2][t] + cf[3][t] for cf in CONFIGS for t in range(4))
    GA.check("H = J_A . J_B is self-adjoint, commutes with Q_A and Q_B, and has tower grade four", ok)
    return ok


def check_matrix_element_and_s_squared_law():
    ok = True
    for cf in CONFIGS[:3]:
        us = [_spinor(k) for k in cf]
        amp, form = _amplitude(_H(us))
        ga = _mdot(_cur(us[2], us[0]), _cur(us[3], us[1]))
        ok = ok and form and amp == ga and ga != QI(0)
    rats = [_ratio(c) for c in CONFIGS]
    ok = ok and all(o for _, o in rats) and {r for r, _ in rats} == {F(1, 4)}
    GA.check("<A3 B4|H|A1 B2> = J_A(3,1).J_B(4,2); |M|^2/(c1 c2 c3 c4 s^2) = 1/4 at six configurations", ok)
    return ok


def check_crossed_amplitude_u_squared_law():
    ok = True
    for cf in CONFIGS[:2]:
        us = [_spinor(k) for k in cf]
        amp, form = _amplitude(_H(us, anti=True))
        z = _mdot(_cur(us[2], us[0]), _cur(us[1], us[3]))
        ok = ok and form and amp == QI(0) - z
    rats = [_ratio(c, crossed=True) for c in CONFIGS]
    ok = ok and all(o for _, o in rats) and {r for r, _ in rats} == {F(1, 4)}
    GA.check("antiparticles: amplitude -J_A(3,1).J_B(2,4), |M|^2/(c1 c2 c3 c4 u^2) = 1/4 at six configurations", ok)
    return ok


def check_boosted_frames():
    cf = CONFIGS[1]
    bk, R = zip(*[_boost_k(k) for k in cf])
    R = R[0]
    us_b = [GA.mul(R, _spinor(k), S4) for k in cf]
    z0 = _mdot(_cur(_spinor(cf[2]), _spinor(cf[0])), _cur(_spinor(cf[3]), _spinor(cf[1])))
    z1 = _mdot(_cur(us_b[2], us_b[0]), _cur(us_b[3], us_b[1]))
    ok = z0.re ** 2 + z0.im ** 2 == z1.re ** 2 + z1.im ** 2
    ok = ok and all(GA.eq(_chi(1, f), f) for f in us_b) and (len(bk) == len(us_b) and all(GA.is_zero(GA.mul(_kvec(k), f, S4)) for k, f in zip(bk, us_b)))
    s0 = _mink([cf[0][i] + cf[1][i] for i in range(4)])
    s1 = _mink([bk[0][i] + bk[1][i] for i in range(4)])
    r, o = _ratio(bk)
    ok = ok and s0 == s1 and bk[0] != cf[0] and r == F(1, 4) and o
    GA.check("a boost keeps chirality, ker k', |M|^2 and s; fresh boosted-frame spinors give the normalised 1/4 again", ok)
    return ok
