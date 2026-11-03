"""angle.wedge-reflection-translations-are-ascent: exact checks.

Cl(1,3) in GA.py with e_t = e0 (square +1), e_r, e_theta, e_phi = e1, e2, e3 (square -1); B = e_t e_r.
(i) B^2 = 1; R = 5/4 + 3/4 B has R R~ = 1, sends (e_t, e_r) by the symmetric matrix [[17/8, -15/8], [-15/8, 17/8]],
    fixes e_theta, e_phi, and rescales e_t + e_r by 1/4 and e_t - e_r by 4.
(ii) Complex multivectors as pairs (real part, imaginary part). The rotor family c + s B with c^2 - s^2 = 1
    contains (c, s) = (0, i), i.e. iB (the value at eta = i pi/2), whose reverse is -iB and (iB)(-iB) = 1; its
    action x -> (iB) x (-iB) equals x -> B x B, is -1 on e_t, e_r and +1 on e_theta, e_phi, commutes with the
    boost action of R, and squares to the identity; (iB)^2 = -1, the family's value at eta = i pi.
(iii) Cl(2,4) with e+ = e4 (square +1), e- = e5 (square -1), nO = (e- - e+)/2, nInf = e- + e+ and
    X(x) = nO + x + Q(x)/2 nInf (Fact angle.imported-conformal-model-null-rotations). For sample a, x in the base:
    T_a = 1 + nInf a / 2 is even, T_a (1 - nInf a / 2) = 1, T_a fixes nInf, equals R_u = 1 + v u with v = nInf,
    u = a/2 (u orthogonal to v), and T_a X(x) T_a^{-1} = X(x + a); the base boost rotor R fixes nO and nInf and
    sends X(x) to X(R x R~).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
S24 = GA.sig(1, 3) + (1, -1)
E = [GA.gen(i) for i in range(6)]
AS = [(1, 2, 0, -1), (0, 1, 1, 1), (3, -1, 2, 0)]
XS = [(2, 0, 1, 1), (1, 1, 0, 0), (-1, 3, 2, 5)]


def vec(c):
    return {(i,): F(v) for i, v in enumerate(c) if v != 0}


def cmul(x, y, sq):
    (a, b), (c, d) = x, y
    return (GA.sub(GA.mul(a, c, sq), GA.mul(b, d, sq)), GA.add(GA.mul(a, d, sq), GA.mul(b, c, sq)))


def check_boost_rotor():
    B = GA.mul(E[0], E[1], S13)
    ok = GA.mul(B, B, S13) == {(): F(1)}
    R = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), B))
    Rr = GA.reverse(R)
    ok = ok and GA.mul(R, Rr, S13) == {(): F(1)}

    def act(v):
        return GA.mul(GA.mul(R, v, S13), Rr, S13)
    mat = [[F(17, 8), F(-15, 8)], [F(-15, 8), F(17, 8)]]
    for j in range(2):
        img = act(E[j])
        ok = ok and GA.eq(img, GA.add(GA.scal(mat[0][j], E[0]), GA.scal(mat[1][j], E[1])))
    ok = ok and GA.eq(act(E[2]), E[2]) and GA.eq(act(E[3]), E[3])
    lp, lm = GA.add(E[0], E[1]), GA.sub(E[0], E[1])
    ok = ok and GA.eq(act(lp), GA.scal(F(1, 4), lp)) and GA.eq(act(lm), GA.scal(4, lm))
    _tp_rv = (ok); assert _tp_rv is not False, "check_boost_rotor"; return _tp_rv


def check_imaginary_rapidity_is_the_wedge_reflection():
    B = GA.mul(E[0], E[1], S13)
    zero = {}
    iB = (zero, B)
    c, s = (F(0), F(1))                     # (cosh, sinh) at i pi / 2 = (0, i): c^2 - (i s)^2 = 1
    ok = c * c + s * s == 1
    rot = (GA.sc(c), GA.scal(s, B))          # c + (i s) B
    ok = ok and GA.eq(rot[0], iB[0]) and GA.eq(rot[1], iB[1])
    rev = (GA.reverse(iB[0]), GA.reverse(iB[1]))
    ok = ok and GA.eq(rev[1], GA.neg(B)) and rev[0] == {}
    prod = cmul(iB, rev, S13)
    ok = ok and prod == ({(): F(1)}, {})
    sq = cmul(iB, iB, S13)
    ok = ok and sq == ({(): F(-1)}, {})
    R = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), B))
    for i in range(4):
        x = (E[i], zero)
        twisted = cmul(cmul(iB, x, S13), rev, S13)
        refl = GA.mul(GA.mul(B, E[i], S13), B, S13)
        ok = ok and twisted[1] == {} and GA.eq(twisted[0], refl)
        ok = ok and GA.eq(refl, GA.neg(E[i]) if i < 2 else E[i])
        ok = ok and GA.eq(GA.mul(GA.mul(B, refl, S13), B, S13), E[i])
        boosted = GA.mul(GA.mul(R, E[i], S13), GA.reverse(R), S13)
        ok = ok and GA.eq(GA.mul(GA.mul(B, boosted, S13), B, S13),
                          GA.mul(GA.mul(R, refl, S13), GA.reverse(R), S13))
    _tp_rv = (ok); assert _tp_rv is not False, "check_imaginary_rapidity_is_the_wedge_reflection"; return _tp_rv


def check_null_rotations_translate_points_in_the_completion():
    premise("angle.imported-conformal-model-null-rotations")
    no = GA.scal(F(1, 2), GA.sub(E[5], E[4]))
    ninf = GA.add(E[5], E[4])
    ok = GA.dot(no, ninf, S24) == -1 and GA.mul(ninf, ninf, S24) == {} and GA.mul(no, no, S24) == {}

    def lift(x):
        return GA.add(no, x, GA.scal(GA.mul(x, x, S24).get((), F(0)) / 2, ninf))
    B = GA.mul(E[0], E[1], S24)
    R = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), B))
    Rr = GA.reverse(R)
    ok = ok and GA.eq(GA.mul(GA.mul(R, no, S24), Rr, S24), no)
    ok = ok and GA.eq(GA.mul(GA.mul(R, ninf, S24), Rr, S24), ninf)
    for ac in AS:
        a = vec(ac)
        half = GA.scal(F(1, 2), GA.mul(ninf, a, S24))
        T = GA.add(GA.sc(1), half)
        Ti = GA.sub(GA.sc(1), half)
        ok = ok and all(len(b) % 2 == 0 for b in T)
        ok = ok and GA.mul(T, Ti, S24) == {(): F(1)} and GA.mul(Ti, T, S24) == {(): F(1)}
        ok = ok and GA.eq(GA.mul(GA.mul(T, ninf, S24), Ti, S24), ninf)
        u = GA.scal(F(1, 2), a)
        ok = ok and GA.dot(u, ninf, S24) == 0 and GA.eq(T, GA.add(GA.sc(1), GA.mul(ninf, u, S24)))
        for xc in XS:
            x = vec(xc)
            ok = ok and GA.eq(GA.mul(GA.mul(T, lift(x), S24), Ti, S24), lift(GA.add(x, a)))
            ok = ok and GA.eq(GA.mul(GA.mul(R, lift(x), S24), Rr, S24),
                              lift(GA.mul(GA.mul(R, x, S24), Rr, S24)))
    _tp_rv = (ok); assert _tp_rv is not False, "check_null_rotations_translate_points_in_the_completion"; return _tp_rv
