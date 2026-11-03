"""field-theory.elementary-photon-ga: exact checks.

Cl(1,3), i = I4 with complex coefficients on the left; massless chi_+ spinors and GA transition currents
J(out, in) = proj(f_out* g0 g^mu f_in) as Gaussian rationals. Ten exact configurations k1 + k2 = k3 + k4 (all
null, k1 not collinear with k3, k2 not with k4, |q| rational for q = k1 - k3, J_A^0 J_B^0 != 0; eight with
q_0 != 0). Current conservation (k_out - k_in) . J = 0 holds for every current used.
(1) A rational right-handed orthonormal frame (t1, t2, q/|q|) (a reflection taking e3 to q/|q|, e1 and e2 swapped)
    at every configuration; eps_h = t1 - h I4 t2 satisfies B_q . eps_h = h I4 eps_h for the rotation bivector
    B_q about q (on and off the axes); control: t1 + h I4 t2 fails.
(2) proj(J eps) = J . conj(eps) for both currents and both helicities (sesquilinear, as I4 anticommutes with
    vectors).
(3) (1/2) sum_h proj(J_A eps_h) proj(J_B eps_-h) = J_A_perp . J_B_perp; pairing each helicity with itself does not.
(4) Coulomb-gauge exchange, (J_A_perp . J_B_perp) (1/2|q|)(1/(q0 - |q|) + 1/(-q0 - |q|)) + J_A^0 J_B^0/|q|^2,
    equals the covariant -J_A . J_B / t at all ten configurations, with the analytic projector and with the GA
    polarisations of (3); controls: without the transverse projection, or with a non-conserved current, the
    equality fails at every q_0 != 0 configuration.
(5) Massive exchange -J.J/(t - M^2) = (J.J/M^2)(1 + t/(M^2 - t)) (M^2 = 10^6) at three configurations, i.e. the
    contact term of field-theory.contact-interactions-tower with G = e^2/M^2 plus a relative correction
    t/(M^2 - t); q . J = 0 at both vertices, so the Proca q q / M^2 term drops.
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



PICK = [((3, 3, 0, 0), (5, 0, 3, -4), (5, 3, 0, -4), (3, 0, 3, 0)),
        ((3, 0, 0, -3), (5, 3, 4, 0), (5, 0, 4, -3), (3, 3, 0, 0)),
        ((4, 0, 4, 0), (5, 4, 0, -3), (5, 0, 4, -3), (4, 4, 0, 0)),
        ((3, 3, 0, 0), (5, -3, -4, 0), (5, 3, -4, 0), (3, -3, 0, 0)),
        ((4, 0, 0, 4), (2, -2, 0, 0), (3, -1, 2, 2), (3, -1, -2, 2)),
        ((4, 0, -4, 0), (5, 0, 4, 3), (3, 0, 0, -3), (6, 0, 0, 6)),
        ((4, 0, 0, -4), (3, -2, 1, 2), (3, 2, 1, -2), (4, -4, 0, 0)),
        ((5, 4, 0, -3), (4, -4, 0, 0), (6, 0, 0, -6), (3, 0, 0, 3)),
        ((3, 1, -2, 2), (3, 2, 2, -1), (3, 1, 2, 2), (3, 2, -2, -1)),
        ((5, 3, -4, 0), (5, 0, 4, 3), (5, 3, 4, 0), (5, 0, -4, 3))]
MV2 = F(10) ** 6


def _collinear(x, y):
    return (x[2] * y[3] - x[3] * y[2], x[3] * y[1] - x[1] * y[3], x[1] * y[2] - x[2] * y[1]) == (0, 0, 0)


def _frame(qs, Qr):
    n = [F(x, Qr) for x in qs]
    E = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    if n == E[2]:
        return E[0], E[1], n
    if n == [F(0), F(0), F(-1)]:
        return E[1], E[0], n
    m = [n[0], n[1], n[2] - 1]
    mm = sum(x * x for x in m)
    R = lambda x: [x[i] - 2 * sum(x[j] * m[j] for j in range(3)) * m[i] / mm for i in range(3)]
    return R(E[1]), R(E[0]), n


def _svec(t):
    return GA.add(*[_scl(t[i], GA.gen(1 + i)) for i in range(3) if t[i] != 0])


def _cross(x, y):
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]


def _gavec(J):
    return GA.add(*[GA.mul(_qmv(J[mu]), GA.gen(mu), S4) for mu in range(4) if J[mu] != QI(0)])


def _half_comm(Bv, x):
    return _scl(F(1, 2), GA.sub(GA.mul(Bv, x, S4), GA.mul(x, Bv, S4)))


def _configs():
    out = []
    for (k1, k2, k3, k4) in PICK:
        q = [k1[i] - k3[i] for i in range(4)]
        Q2 = q[1] ** 2 + q[2] ** 2 + q[3] ** 2
        out.append((k1, k2, k3, k4, q, _isqrt(Q2), Q2))
    return out


def _currents(c):
    k1, k2, k3, k4 = c[:4]
    return _cur(_spinor(k3), _spinor(k1)), _cur(_spinor(k4), _spinor(k2))


def _perp(JA, JB, q, Q2):
    dot = JA[1] * JB[1] + JA[2] * JB[2] + JA[3] * JB[3]
    qA = JA[1] * QI(q[1]) + JA[2] * QI(q[2]) + JA[3] * QI(q[3])
    qB = JB[1] * QI(q[1]) + JB[2] * QI(q[2]) + JB[3] * QI(q[3])
    return dot - qA * qB * QI(F(1) / Q2)


def _eps(t1, t2, h):
    return GA.sub(_svec(t1), _scl(F(h), GA.mul(I4, _svec(t2), S4)))


def check_kinematics_and_conservation():
    ok = True
    for (k1, k2, k3, k4, q, Qr, Q2) in _configs():
        ok = ok and all(k[0] > 0 and k[0] ** 2 == k[1] ** 2 + k[2] ** 2 + k[3] ** 2 for k in (k1, k2, k3, k4))
        ok = ok and all(k1[i] + k2[i] == k3[i] + k4[i] for i in range(4)) and Qr * Qr == Q2 and q[0] ** 2 != Q2
        ok = ok and not _collinear(k1, k3) and not _collinear(k2, k4)
        for (ka, kb) in ((k1, k3), (k2, k4)):
            J = _cur(_spinor(kb), _spinor(ka))
            dq = [kb[i] - ka[i] for i in range(4)]
            ok = ok and J[0] * QI(dq[0]) - J[1] * QI(dq[1]) - J[2] * QI(dq[2]) - J[3] * QI(dq[3]) == QI(0)
        JA, JB = _currents((k1, k2, k3, k4))
        ok = ok and JA[0] * JB[0] != QI(0)
    ok = ok and sum(1 for c in _configs() if c[4][0] != 0) == 8
    GA.check("ten exact configurations with rational |q|; every GA transition current is conserved", ok)
    return ok


def check_helicity_eigen_relation():
    ok = True
    for (k1, k2, k3, k4, q, Qr, Q2) in _configs():
        t1, t2, n = _frame(q[1:], Qr)
        ok = ok and _cross(t1, t2) == n and all(sum(x * y for x, y in zip(u, v)) == (1 if u is v else 0)
                                                for u in (t1, t2, n) for v in (t1, t2, n))
        Bq = GA.add(_scl(n[0], {(2, 3): F(1)}), _scl(-n[1], {(1, 3): F(1)}), _scl(n[2], {(1, 2): F(1)}))
        for h in (1, -1):
            e = _eps(t1, t2, h)
            ok = ok and GA.eq(_half_comm(Bq, e), _scl(F(h), GA.mul(I4, e, S4)))
            wrong = GA.add(_svec(t1), _scl(F(h), GA.mul(I4, _svec(t2), S4)))
            ok = ok and not GA.eq(_half_comm(Bq, wrong), _scl(F(h), GA.mul(I4, wrong, S4)))
    GA.check("B_q . eps_h = h I4 eps_h on rational frames (control t1 + h I4 t2 fails)", ok)
    return ok


def check_sesquilinear_and_helicity_sum():
    ok = True
    for c in _configs():
        k1, k2, k3, k4, q, Qr, Q2 = c
        t1, t2, n = _frame(q[1:], Qr)
        JA, JB = _currents(c)
        gA, gB = _gavec(JA), _gavec(JB)
        eps = {h: _eps(t1, t2, h) for h in (1, -1)}
        for h in (1, -1):
            epsc = [QI(0)] + [QI(t1[i], h * t2[i]) for i in range(3)]
            ok = ok and _to_q(_proj(GA.mul(gA, eps[h], S4))) == _mdot(JA, epsc)
            ok = ok and _to_q(_proj(GA.mul(gB, eps[h], S4))) == _mdot(JB, epsc)
        hs = sum((_to_q(_proj(GA.mul(gA, eps[h], S4))) * _to_q(_proj(GA.mul(gB, eps[-h], S4))) * QI(F(1, 2))
                  for h in (1, -1)), QI(0))
        naive = sum((_to_q(_proj(GA.mul(gA, eps[h], S4))) * _to_q(_proj(GA.mul(gB, eps[h], S4))) * QI(F(1, 2))
                     for h in (1, -1)), QI(0))
        perp = _perp(JA, JB, q, F(Q2))
        ok = ok and hs == perp and naive != perp
    GA.check("proj(J eps) = J . conj(eps); the opposite-label helicity sum is the transverse product", ok)
    return ok


def check_coulomb_gauge_equals_covariant():
    premise("field-theory.imported-standard-field-theory")
    ok = True
    nonc = 0
    for c in _configs():
        k1, k2, k3, k4, q, Qr, Q2 = c
        JA, JB = _currents(c)
        q0 = F(q[0])
        t = q0 * q0 - F(Q2)
        den = QI(F(1) / (2 * Qr)) * (QI(1 / (q0 - Qr)) + QI(1 / (-q0 - Qr)))
        coul = JA[0] * JB[0] * QI(F(1) / Q2)
        cov = _mdot(JA, JB) * QI(-1 / t)
        ok = ok and _perp(JA, JB, q, F(Q2)) * den + coul == cov
        if q[0] != 0:
            nonc += 1
            dot = JA[1] * JB[1] + JA[2] * JB[2] + JA[3] * JB[3]
            ok = ok and dot * den + coul != cov
            JF = [JA[0] + QI(1)] + JA[1:]
            ok = ok and _perp(JF, JB, q, F(Q2)) * den + JF[0] * JB[0] * QI(F(1) / Q2) != _mdot(JF, JB) * QI(-1 / t)
    ok = ok and nonc == 8
    GA.check("Coulomb-gauge exchange = -J_A . J_B / t at ten configurations; controls fail", ok)
    return ok


def check_massive_vector_contact_limit():
    premise("field-theory.contact-interactions-tower")
    ok = True
    for c in _configs()[:3]:
        k1, k2, k3, k4, q, Qr, Q2 = c
        JA, JB = _currents(c)
        t = F(q[0]) ** 2 - F(Q2)
        massive = _mdot(JA, JB) * QI(-1 / (t - MV2))
        contact = _mdot(JA, JB) * QI(1 / MV2)
        ok = ok and massive - contact == contact * QI(t / (MV2 - t)) and contact != QI(0)
        qq = [QI(x) for x in q]
        ok = ok and _mdot(JA, qq) == QI(0) and _mdot(JB, qq) == QI(0)
    GA.check("massive exchange = contact J.J/M^2 times (1 + t/(M^2 - t)); the Proca term drops", ok)
    return ok
