"""synthesis.de-sitter-temperature-mirror-and-status: exact checks of clause (b) and of the conversion factor in (c).

Conventions of Theorem synthesis.cosmological-horizon-completed-pair: Cl(2,4) with squares (1, -1, -1, -1, 1, -1)
for e0 | e1 e2 e3 | e+ e-, nO = (e+ + e-)/2, nInf = e+ - e- (nO . nInf = 1), Lambda = 3 H^2 with H rational,
I = nInf + (Lambda/6) nO, W = nInf - (Lambda/6) nO, e_W = W/H, u = e0 e_W, B = H u. The mirror is the reversed
form (all squares negated, signature (4,2)).
(b) In the mirror: Pi = span{e0, e_W} is again a (1,1) plane, B^2 = H^2 = kappa^2 unchanged; the mirror pair
    w = (e0 - e_W)/2, w* = -(e0 + e_W)/2 is null, w w* + w* w = 1, w* w - w w* = u (the same occupation boost);
    its number operator w* w equals the original v* v = (1 + u)/2 blade for blade, so K = u/2 = N - 1/2 is the same
    element and the KMS (Gibbs) state of K at a given Boltzmann factor, and with it the occupation and T_Lambda,
    are the same; the rotor flow (q + 1/q)/2 + (q - 1/q)/2 u contracts w by q^{-2} as it contracts v (rate
    kappa), at sample q. The ladder is reversed: w is a multiple of v* and w* of v.
(c) The conversion factor: kappa_Lambda^2 = Q(I_Lambda) = Lambda/3 = H^2 in the original form, so
    T_Lambda = kappa_Lambda/(2 pi) = H/(2 pi). That T_Lambda is undetermined within the series
    (Lambda a parameter of the laws) has no computable content and is not checked.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
MIRROR = tuple(-s for s in SQ)
HS = [F(1, 2), F(1), F(3), F(5, 3)]
QS = [F(2), F(1, 3), F(7, 4)]


def frame(H):
    L = 3 * H * H
    n0 = GA.scal(F(1, 2), GA.add(GA.gen(4), GA.gen(5)))
    ninf = GA.sub(GA.gen(4), GA.gen(5))
    I = GA.add(ninf, GA.scal(L / 6, n0))
    W = GA.sub(ninf, GA.scal(L / 6, n0))
    return L, n0, ninf, I, GA.scal(1 / H, W)


def sqr(x, sq):
    return GA.mul(x, x, sq).get((), F(0))


def check_mirror_pair_same_rate_same_boost():
    premise("synthesis.cosmological-horizon-completed-pair")
    premise("synthesis.de-sitter-temperature-frozen-point-norm")
    ok = True
    e0 = GA.gen(0)
    for H in HS:
        L, n0, ninf, I, eW = frame(H)
        u_orig = GA.mul(e0, eW, SQ)
        u_mir = GA.mul(e0, eW, MIRROR)
        ok = ok and GA.eq(u_orig, u_mir)
        u = u_orig
        ok = ok and (sqr(e0, MIRROR), sqr(eW, MIRROR)) == (F(-1), F(1)) and GA.dot(e0, eW, MIRROR) == 0
        B = GA.scal(H, u)
        ok = ok and GA.mul(B, B, SQ) == {(): H * H} and GA.mul(B, B, MIRROR) == {(): H * H}
        v = GA.scal(F(1, 2), GA.add(e0, eW))
        vs = GA.scal(F(1, 2), GA.sub(e0, eW))
        w = GA.scal(F(1, 2), GA.sub(e0, eW))
        ws = GA.scal(F(-1, 2), GA.add(e0, eW))
        ok = ok and GA.mul(w, w, MIRROR) == {} and GA.mul(ws, ws, MIRROR) == {}
        ok = ok and GA.add(GA.mul(w, ws, MIRROR), GA.mul(ws, w, MIRROR)) == {(): F(1)}
        ok = ok and GA.eq(GA.sub(GA.mul(ws, w, MIRROR), GA.mul(w, ws, MIRROR)), u)
        Nw = GA.mul(ws, w, MIRROR)
        Nv = GA.mul(vs, v, SQ)
        ok = ok and GA.eq(Nw, Nv) and GA.eq(Nv, GA.scal(F(1, 2), GA.add(GA.sc(1), u)))
        ok = ok and GA.eq(GA.scal(F(1, 2), u), GA.sub(Nw, GA.sc(F(1, 2))))
        # ladder reversed: w = v*, w* = -v
        ok = ok and GA.eq(w, vs) and GA.eq(ws, GA.neg(v))
        for q in QS:
            R = GA.add(GA.sc((q + 1 / q) / 2), GA.scal((q - 1 / q) / 2, u))
            Rr = GA.reverse(R)
            ok = ok and GA.mul(R, Rr, MIRROR) == {(): F(1)} and GA.mul(R, Rr, SQ) == {(): F(1)}
            ok = ok and GA.eq(GA.mul(GA.mul(R, w, MIRROR), Rr, MIRROR), GA.scal(1 / (q * q), w))
            ok = ok and GA.eq(GA.mul(GA.mul(R, v, SQ), Rr, SQ), GA.scal(1 / (q * q), v))
    _tp_rv = (ok); assert _tp_rv is not False, "check_mirror_pair_same_rate_same_boost"; return _tp_rv


def check_conversion_factor_is_the_frozen_point_norm():
    premise("synthesis.de-sitter-temperature-frozen-point-norm")
    ok = True
    for H in HS:
        L, n0, ninf, I, eW = frame(H)
        ok = ok and GA.dot(n0, ninf, SQ) == 1
        kappa2 = sqr(I, SQ)
        ok = ok and kappa2 == L / 3 and kappa2 == H * H
        # mirror: Q(I) changes sign while B^2 does not, so the rate is read from B^2
        ok = ok and sqr(I, MIRROR) == -L / 3
    _tp_rv = (ok); assert _tp_rv is not False, "check_conversion_factor_is_the_frozen_point_norm"; return _tp_rv
