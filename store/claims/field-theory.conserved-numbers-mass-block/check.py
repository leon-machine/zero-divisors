"""field-theory.conserved-numbers-mass-block: exact checks.

The mass block of Proposition field-theory.composite-scalars-mean-field-level(1): Cl(1,3) ground, tower planes
a, c (generators 4..7), v = (e + f)/2, w = (e - f)/2, n = v w, H = K(n_a + n_c) + mu w_a w_c + mu^* v_c v_a with
mu in span{1, I4}; five cases including K = 0 (rest) and complex mu, E^2 = K^2 + |mu|^2 rational.
(1) gamma_a = alpha w_a + beta v_c, gamma_c = alpha' w_c + beta' v_a with alpha = alpha' = 2,
    beta = (K - E) alpha mu^*/|mu|^2, beta' = (E - K) alpha' mu^*/|mu|^2: [H, gamma] = -E gamma for both,
    {gamma, gamma*} is the scalar |alpha|^2 + |beta|^2, and H = E (N_a + N_c) + (K - E) exactly with
    N = gamma* gamma / {gamma, gamma*}.
(2) N_a, N_c commute with each other and with H; n_a, n_c commute with each other but not with H; the massive
    vacuum Om = -(mu/(K - E)) P0 + v_a v_c P0 is annihilated by both gammas, and <n_a> = (E - K)/(2E) exactly.
(3) Q = n_a - n_c commutes with H, equals N_a - N_c and kills Om; the rung state v_a P0 has H = K, N_a = 1, N_c = 0.
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



ST2 = tuple(list(S4) + [1, -1, 1, -1])
CASES = [(3, QI(4)), (3, QI(F(12, 5), F(16, 5))), (5, QI(12)), (0, QI(1)), (0, QI(F(3, 5), F(4, 5)))]


def _m(x, y):
    return GA.mul(x, y, ST2)


def _comm(x, y):
    return GA.sub(_m(x, y), _m(y, x))


def _setup(K, mu):
    (va, wa), (vc, wc) = _plane(0), _plane(1)
    H = GA.add(_scl(F(K), _m(va, wa)), _scl(F(K), _m(vc, wc)), _m(_qmv(mu), _m(wa, wc)),
               _m(_qmv(mu.conj()), _m(vc, va)))
    m2 = mu.re ** 2 + mu.im ** 2
    e2 = F(K) ** 2 + m2
    E = F(_isqrt(e2.numerator), _isqrt(e2.denominator))
    al = alp = QI(2)
    be = al * QI(F(K) - E) * mu.conj() * QI(1 / m2)
    bep = alp * QI(E - F(K)) * mu.conj() * QI(1 / m2)
    ga = GA.add(_m(_qmv(al), wa), _m(_qmv(be), vc))
    gc = GA.add(_m(_qmv(alp), wc), _m(_qmv(bep), va))
    na_, nc_ = (al * al.conj() + be * be.conj()).re, (alp * alp.conj() + bep * bep.conj()).re
    Na = _scl(1 / na_, _m(_star(ga, ST2), ga))
    Nc = _scl(1 / nc_, _m(_star(gc, ST2), gc))
    P0 = _m(_m(wa, va), _m(wc, vc))
    Om = GA.add(_m(_qmv(QI(0) - mu * QI(1 / (F(K) - E))), P0), _m(_m(va, vc), P0))
    return dict(va=va, wa=wa, vc=vc, wc=wc, H=H, E=E, e2=e2, ga=ga, gc=gc, Na=Na, Nc=Nc, nrm_a=na_, P0=P0, Om=Om)


def _coeff(Y, X):
    """z in span{1, I4} with Y = z X (X = P0), or None."""
    IX = GA.mul(I4, X, ST2)
    b0 = next(iter(X))
    bI = next(iter(IX))
    z = QI(Y.get(b0, F(0)) / X[b0], Y.get(bI, F(0)) / IX[bI])
    return z if GA.eq(Y, _m(_qmv(z), X)) else None


def check_quasiparticles_diagonalise_the_block():
    premise("field-theory.composite-scalars-mean-field-level")
    ok = [_setup(K, mu)["E"] for (K, mu) in CASES] == [5, 5, 13, 1, 1]
    for (K, mu) in CASES:
        d = _setup(K, mu)
        E = d["E"]
        ok = ok and E * E == d["e2"]
        ok = ok and GA.eq(_comm(d["H"], d["ga"]), _scl(-E, d["ga"])) and GA.eq(_comm(d["H"], d["gc"]), _scl(-E, d["gc"]))
        ok = ok and GA.eq(GA.add(_m(d["ga"], _star(d["ga"], ST2)), _m(_star(d["ga"], ST2), d["ga"])), GA.sc(d["nrm_a"]))
        ok = ok and GA.eq(d["H"], GA.add(_scl(E, GA.add(d["Na"], d["Nc"])), GA.sc(F(K) - E)))
    GA.check("[H, gamma] = -E gamma and H = E (N_a + N_c) + (K - E) on five mass blocks", ok)
    return ok


def check_rung_numbers_not_conserved_massive_vacuum():
    premise("field-theory.composite-scalars-mean-field-level")
    ok = True
    for (K, mu) in CASES:
        d = _setup(K, mu)
        na, nc = _m(d["va"], d["wa"]), _m(d["vc"], d["wc"])
        ok = ok and GA.is_zero(_comm(d["Na"], d["Nc"])) and GA.is_zero(_comm(d["H"], d["Na"]))
        ok = ok and GA.is_zero(_comm(d["H"], d["Nc"])) and GA.is_zero(_comm(na, nc))
        ok = ok and not GA.is_zero(_comm(d["H"], na)) and not GA.is_zero(_comm(d["H"], nc))
        Om = d["Om"]
        ok = ok and GA.is_zero(_m(d["ga"], Om)) and GA.is_zero(_m(d["gc"], Om))
        bra = _m(d["P0"], _star(GA.add(_qmv(QI(0) - mu * QI(1 / (F(K) - d["E"]))), _m(d["va"], d["vc"])), ST2))
        nrm = _coeff(_m(bra, Om), d["P0"])
        nav = _coeff(_m(bra, _m(na, Om)), d["P0"])
        ok = ok and nrm is not None and nav is not None and nav * QI(1 / nrm.re) == QI((d["E"] - F(K)) / (2 * d["E"]))
    GA.check("N_a, N_c conserved, n_a, n_c not; massive vacuum killed by both gammas with <n_a> = (E - K)/(2E)", ok)
    return ok


def check_charge_in_rung_algebra():
    premise("field-theory.composite-scalars-mean-field-level")
    ok = True
    for (K, mu) in CASES:
        d = _setup(K, mu)
        na, nc = _m(d["va"], d["wa"]), _m(d["vc"], d["wc"])
        Q = GA.sub(na, nc)
        ok = ok and GA.is_zero(_comm(d["H"], Q)) and GA.eq(Q, GA.sub(d["Na"], d["Nc"])) and GA.is_zero(_m(Q, d["Om"]))
        one = _m(d["va"], d["P0"])
        ok = ok and GA.eq(_m(d["H"], one), _scl(F(K), one)) and GA.eq(_m(d["Na"], one), one)
        ok = ok and GA.is_zero(_m(d["Nc"], one)) and GA.eq(_m(Q, one), _scl(F(1), one))
        other = _m(d["vc"], d["P0"])
        ok = ok and GA.eq(_m(Q, other), _scl(F(-1), other))
    GA.check("Q = n_a - n_c is conserved, equals N_a - N_c, vanishes on the vacuum; v_a P0 is one quantum", ok)
    return ok
