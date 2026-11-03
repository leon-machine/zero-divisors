"""field-theory.composite-scalars-mean-field-level: exact checks.

Cl(1,3) ground with tower planes a, c (generators 4..7), modes v = (e + f)/2 (creation), w = (e - f)/2, n = v w,
complex numbers span{1, I4}; T03's * for self-adjointness. Block H(K, mu) = K(n_a + n_c) + mu w_a w_c + mu^* v_c v_a.
(1) For four (K, mu) (mu complex included): H* = H and ad_H^2 x = (K^2 + |mu|^2) x on w_a, v_a, w_c, v_c. On the
    vacuum P0 and s1 = v_a v_c P0: H P0 = -mu^* s1, H s1 = -mu P0 + 2K s1; u = -(mu/lam) P0 + s1 is an eigenvector
    for lam = K - E and lam = K + E (E^2 = K^2 + |mu|^2, E rational at the samples), and the odd states v_a P0,
    v_c P0 have energy K: spectrum {K - E, K, K, K + E}. The pairing |B(f(k), f(-k))|^2/(alpha alpha) is one
    constant over six directions, equal to 1, so mu = m B gives the isotropic E^2 = K^2 + m^2.
(2) H_4 = sum_b K(n_a + n_c) - G P* P, P = sum_b w_a w_c (n_b = 2, 3 blocks): self-adjoint, commutes with the axial
    number, the symmetric n-pair states (P*)^n vacuum are eigenstates of energy 2Kn - G n(n_b - n + 1), and some
    pair energy is negative exactly when G > 2K/n_b. The mean-field energy n_b(K - E) + Delta^2/G (one shell)
    has its minimum away from Delta = 0 above G_c = 2K/(n_b c) and stays positive at G_c and 0.9 G_c.
(3) In the block ground state <w_a w_c> = -mu^*/(2E) exactly (three cases): the gap equation, mass = G x condensate.
(4) U = exp(theta I4 (n_a + n_c)) with exp(theta I4) = (3 + 4 I4)/5 is unitary and U H(mu) U* = H(mu e^(-2 theta I4))
    for three (K, mu); the pairing picks up e^(2 theta I4): a flat phase direction.
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



NB = {(0, 1): F(1)}
ST = tuple(list(S4) + [1, -1, 1, -1])
DIRS = [(3, 0, 0, 3), (5, 3, 4, 0), (3, 2, 1, 2), (9, 1, 4, 8), (7, 2, 3, 6), (5, 0, -3, 4)]
BLOCKS = [(3, QI(4)), (3, QI(F(12, 5), F(16, 5))), (5, QI(F(60, 13), F(144, 13))), (2, QI(F(9, 10), F(6, 5)))]
PAIRING = [(2, 3, 2), (2, 3, 4), (3, 3, 1), (3, 3, 3)]
MF_X = [F(0), F(7), F(16), F(27), F(40)]
# Mean-field sample shell: Ndir directions at K = 3, a coupling G = MF_G_ABOVE/(n_b c) above
# G_c = 2K/(n_b c) = 6/(n_b c), and a coupling MF_G_BELOW G_c below the threshold.
MF_NDIR, MF_K = 6, F(3)
MF_G_ABOVE, MF_G_BELOW = F(10), F(9, 10)


def _B(a, b):
    return _to_q(_proj(GA.mul(GA.mul(GA.reverse(a), b, S4), NB, S4)))


def _alpha(a, b):
    return GA.mul(_star(a, S4), b, S4).get((), F(0))


def _modes():
    (va, wa), (vc, wc) = _plane(0), _plane(1)
    return va, wa, vc, wc


def _block_H(K, mu):
    va, wa, vc, wc = _modes()
    H = GA.add(_scl(F(K), GA.mul(va, wa, ST)), _scl(F(K), GA.mul(vc, wc, ST)))
    return GA.add(H, GA.mul(_qmv(mu), GA.mul(wa, wc, ST), ST), GA.mul(_qmv(mu.conj()), GA.mul(vc, va, ST), ST))


def _vac():
    va, wa, vc, wc = _modes()
    return GA.mul(GA.mul(wa, va, ST), GA.mul(wc, vc, ST), ST)


def _ad(H, x):
    return GA.sub(GA.mul(H, x, ST), GA.mul(x, H, ST))


def _E(K, mu):
    e2 = F(K) ** 2 + mu.re ** 2 + mu.im ** 2
    E = F(_isqrt(e2.numerator), _isqrt(e2.denominator))
    return E if E * E == e2 else None


def _coeff_P0(Y, P0):
    z = QI(4 * Y.get((), F(0)), 4 * Y.get((0, 1, 2, 3), F(0)))
    return z, GA.eq(Y, GA.mul(_qmv(z), P0, ST))


def _c_const():
    vals = set()
    for k in DIRS:
        km = (k[0], -k[1], -k[2], -k[3])
        f, g = _spinor(k), _spinor(km)
        mu = _B(f, g)
        vals.add((mu.re ** 2 + mu.im ** 2) / (_alpha(f, f) * _alpha(g, g)))
    return vals


def _pairing_model(nbk, K, G):
    STm = tuple(list(S4) + [1, -1] * (2 * nbk))
    pl = [_plane(j) for j in range(2 * nbk)]
    P, Hk = {}, {}
    for b in range(nbk):
        (v1, w1), (v2, w2) = pl[2 * b], pl[2 * b + 1]
        P = GA.add(P, GA.mul(w1, w2, STm))
        Hk = GA.add(Hk, _scl(F(K), GA.add(GA.mul(v1, w1, STm), GA.mul(v2, w2, STm))))
    Ps = _star(P, STm)
    H4 = GA.sub(Hk, _scl(F(G), GA.mul(Ps, P, STm)))
    Ntot = GA.add(*[GA.mul(v, w, STm) for (v, w) in pl])
    vac = {(): F(1)}
    for (v, w) in pl:
        vac = GA.mul(vac, GA.mul(w, v, STm), STm)
    ok = GA.eq(_star(H4, STm), H4) and GA.eq(GA.mul(H4, Ntot, STm), GA.mul(Ntot, H4, STm))
    st, energies = vac, []
    for n in range(nbk + 1):
        En = F(2 * K * n) - F(G) * n * (nbk - n + 1)
        ok = ok and not GA.is_zero(st) and GA.eq(GA.mul(H4, st, STm), _scl(En, st))
        energies.append(En)
        st = GA.mul(Ps, st, STm)
    return ok, energies


def check_block_spectrum_and_dispersion():
    va, wa, vc, wc = _modes()
    P0 = _vac()
    s1 = GA.mul(GA.mul(va, vc, ST), P0, ST)
    ok = _c_const() == {F(1)}
    for (K, mu) in BLOCKS:
        H = _block_H(K, mu)
        E = _E(K, mu)
        ok = ok and E is not None and GA.eq(_star(H, ST), H)
        ok = ok and all(GA.eq(_ad(H, _ad(H, x)), _scl(F(K) ** 2 + mu.re ** 2 + mu.im ** 2, x)) for x in (wa, va, wc, vc))
        ok = ok and GA.eq(GA.mul(H, P0, ST), GA.neg(GA.mul(_qmv(mu.conj()), s1, ST)))
        ok = ok and GA.eq(GA.mul(H, s1, ST), GA.add(GA.neg(GA.mul(_qmv(mu), P0, ST)), _scl(F(2 * K), s1)))
        for lam in (F(K) - E, F(K) + E):
            u = GA.add(GA.mul(_qmv(QI(0) - mu * QI(1 / lam)), P0, ST), s1)
            ok = ok and not GA.is_zero(u) and GA.eq(GA.mul(H, u, ST), _scl(lam, u))
        for o in (GA.mul(va, P0, ST), GA.mul(vc, P0, ST)):
            ok = ok and not GA.is_zero(o) and GA.eq(GA.mul(H, o, ST), _scl(F(K), o))
    GA.check("block H: self-adjoint, ad_H^2 = K^2 + |mu|^2, spectrum {K - E, K, K, K + E}; pairing isotropic", ok)
    return ok


def check_pairing_tower_threshold():
    ok = True
    for (nbk, K, G) in PAIRING:
        good, en = _pairing_model(nbk, K, G)
        ok = ok and good and ((min(en) < 0) == (F(G) > F(2 * K, nbk)))
    cB = next(iter(_c_const()))
    Ndir, K = MF_NDIR, MF_K
    nb = 4 * Ndir

    def E_tot(x, G):
        E = _E(K, QI(0)) if x == 0 else F(_isqrt((K * K + cB * x).numerator), _isqrt((K * K + cB * x).denominator))
        return nb * (K - E) + x / G, E * E == K * K + cB * x
    Gc = 2 * K / (nb * cB)
    Gs = MF_G_ABOVE / (nb * cB)
    vals = [E_tot(x, Gs) for x in MF_X]
    ok = ok and all(e for _, e in vals) and min(range(len(MF_X)), key=lambda i: vals[i][0]) == 2
    ok = ok and Gs > Gc
    # By hand (c = 1, n_b = 24, E = 3, 4, 5, 6, 7 at the samples): at G = 10/24 the energy
    # 24(3 - E) + 2.4 x is 0, -36/5, -48/5, -36/5, 0 (minimum away from zero, negative); at G_c = 1/4
    # it is n_b (E - K)^2/(2K) = 4 (E - 3)^2, which vanishes only at Delta = 0 (G_c is the threshold);
    # at 0.9 G_c = 9/40 it is 24(3 - E) + 40x/9 = 0, 64/9, 208/9, 48, 736/9 (positive away from zero).
    # These replace the sign tests they imply.
    ok = ok and cB == 1 and [v for v, _ in vals] == [0, F(-36, 5), F(-48, 5), F(-36, 5), 0]
    ok = ok and [E_tot(x, Gc)[0] for x in MF_X] == [0, 4, 16, 36, 64]
    ok = ok and [E_tot(x, Gc * MF_G_BELOW)[0] for x in MF_X] == [0, F(64, 9), F(208, 9), 48, F(736, 9)]
    GA.check("H_4 pair states have energy 2Kn - G n(n_b - n + 1); pairs condense iff G > 2K/n_b; mean field agrees", ok)
    return ok


def check_gap_equation():
    va, wa, vc, wc = _modes()
    P0 = _vac()
    ok = True
    for (K, mu) in BLOCKS[:3]:
        E = _E(K, mu)
        lam = F(K) - E
        U = GA.add(_qmv(QI(0) - mu * QI(1 / lam)), GA.mul(va, vc, ST))
        nrm, ok1 = _coeff_P0(GA.mul(GA.mul(P0, _star(U, ST), ST), GA.mul(U, P0, ST), ST), P0)
        pr, ok2 = _coeff_P0(GA.mul(GA.mul(P0, _star(U, ST), ST), GA.mul(GA.mul(wa, wc, ST), GA.mul(U, P0, ST), ST), ST), P0)
        ok = ok and ok1 and ok2 and nrm.im == 0 and pr * QI(1 / nrm.re) == QI(0) - mu.conj() * QI(1 / (2 * E))
    GA.check("<w_a w_c> = -mu^*/(2E) in the block ground state: the gap equation", ok)
    return ok


def check_axial_phase_flat_direction():
    va, wa, vc, wc = _modes()
    zq = QI(F(3, 5), F(4, 5))
    zm = _qmv(zq)
    na, nc = GA.mul(va, wa, ST), GA.mul(vc, wc, ST)
    U = GA.mul(GA.add(GA.sc(1), GA.mul(GA.sub(zm, GA.sc(1)), na, ST)),
               GA.add(GA.sc(1), GA.mul(GA.sub(zm, GA.sc(1)), nc, ST)), ST)
    ok = GA.eq(GA.mul(U, _star(U, ST), ST), GA.sc(1)) and GA.eq(GA.mul(_star(U, ST), U, ST), GA.sc(1))
    zinv2 = zq.conj() * zq.conj()
    for (K, mu) in BLOCKS[:3]:
        ok = ok and GA.eq(GA.mul(GA.mul(U, _block_H(K, mu), ST), _star(U, ST), ST), _block_H(K, mu * zinv2))
    f, g = _spinor(DIRS[1]), _spinor((5, -3, -4, 0))
    ok = ok and _B(GA.mul(zm, f, S4), GA.mul(zm, g, S4)) == _B(f, g) * (zq * zq)
    GA.check("U H(mu) U* = H(mu e^(-2 theta I4)): the axial phase is inner and flat", ok)
    return ok
