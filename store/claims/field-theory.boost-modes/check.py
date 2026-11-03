"""field-theory.boost-modes: exact checks.

One plane, the atom Cl(1,1) (e0^2 = 1, e1^2 = -1), modes v = (e0 + e1)/2, v* = (e0 - e1)/2 (the CAR of Fact
field-theory.imported-tower-limit), sigma = v* v - v v* = e0 e1, and T03's * (x* = x on e0, -x on e1, reversing,
conjugate-linear).
(1) Real rapidity, e^(lambda/2) = r for r = 2, 3/2, 5: R = cosh + sinh sigma (rational) gives Ad(R) v = v/r^2,
    Ad(R) v* = r^2 v*, the CAR is preserved, R* = R, R* R = R^2 != 1, and Ad(R) is not a *-map; R = (1/r)(1 +
    (r^2 - 1) N), N = v* v: the imaginary-time evolution e^(-lambda/2) e^(lambda N).
(2) Uniformly over k = 1..4 planes (Jordan-Wigner matrices): the product c_1* ... c_k* is a partial isometry of
    norm 1 (its square modulus is a rank-one projector), and conjugation by the product of the one-plane rotors of
    (1) (as Fock matrices) sends it to r^(2k) times itself, of norm r^(2k): unbounded in k, so no bounded extension to the CAR algebra.
(3) Imaginary rapidity, (cos, sin)(phi/2) = (3/5, 4/5), (5/13, 12/13), (8/17, 15/17), coefficients in Q(i):
    R = cos + i sin sigma is unitary (R* = R^-1), Ad(R) v = e^(-i phi) v, Ad(R) is a *-map, and
    R = e^(-i phi/2) e^(i phi N) = e^(-i phi/2)(1 + (e^(i phi) - 1) N): the unitary flow of the number operator.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
S1 = (1, -1)
REAL_R = [F(2), F(3, 2), F(5)]
PHASES = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17))]


def _scl(c, x):
    out = {}
    for b, v in x.items():
        w = c * v
        if w != 0:
            out[b] = w
    return out


def _star(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        cc = c.conj() if isinstance(c, QI) else c
        out[b] = sign * cc
    return {b: c for b, c in out.items() if c != 0}


def _mul(x, y):
    return GA.mul(x, y, S1)


def _ad(R, Ri, x):
    return _mul(_mul(R, x), Ri)


def _q(x):
    return {b: QI(c) for b, c in x.items()}


def _modes():
    v = GA.add(_scl(F(1, 2), GA.gen(0)), _scl(F(1, 2), GA.gen(1)))
    vs = GA.add(_scl(F(1, 2), GA.gen(0)), _scl(F(-1, 2), GA.gen(1)))
    return v, vs


def _jw(k):
    dim = 2 ** k
    ops = []
    for j in range(k):
        C = [[F(0)] * dim for _ in range(dim)]
        for st in range(dim):
            if (st >> j) & 1:
                C[st ^ (1 << j)][st] = F(-1 if bin(st & ((1 << j) - 1)).count("1") % 2 else 1)
        ops.append(C)
    return ops


def _T(A):
    return [list(r) for r in zip(*A)]


def check_real_rapidity_is_not_a_star_map():
    premise("field-theory.imported-tower-limit")
    v, vs = _modes()
    sig = GA.sub(_mul(vs, v), _mul(v, vs))
    ok = GA.eq(sig, _mul(GA.gen(0), GA.gen(1))) and GA.eq(_mul(sig, sig), GA.sc(1)) and GA.eq(_star(v, S1), vs)
    ok = ok and GA.eq(GA.add(_mul(v, vs), _mul(vs, v)), GA.sc(1)) and GA.is_zero(_mul(v, v))
    N = _mul(vs, v)
    for r in REAL_R:
        ch, sh = (r + 1 / r) / 2, (r - 1 / r) / 2
        R, Ri = GA.add(GA.sc(ch), _scl(sh, sig)), GA.add(GA.sc(ch), _scl(-sh, sig))
        Av, Avs = _ad(R, Ri, v), _ad(R, Ri, vs)
        ok = ok and GA.eq(_mul(R, Ri), GA.sc(1))
        ok = ok and GA.eq(Av, _scl(1 / (r * r), v)) and GA.eq(Avs, _scl(r * r, vs))
        ok = ok and GA.eq(GA.add(_mul(Av, Avs), _mul(Avs, Av)), GA.sc(1))
        ok = ok and not GA.eq(_star(Av, S1), Avs)
        ok = ok and GA.eq(_star(R, S1), R) and not GA.eq(_mul(_star(R, S1), R), GA.sc(1))
        ok = ok and GA.eq(R, _scl(1 / r, GA.add(GA.sc(1), _scl(r * r - 1, N))))
    GA.check("real rapidity: Ad(R) v = v/r^2, v* -> r^2 v*, CAR kept, not a *-map; R = e^(-l/2) e^(l N)", ok)
    return ok


def check_uniform_real_boost_unbounded():
    premise("field-theory.imported-tower-limit")
    ok = True
    r = REAL_R[0]
    for k in range(1, 5):
        C = _jw(k)
        dim = 2 ** k
        ident = [[F(1) if i == j else F(0) for j in range(dim)] for i in range(dim)]
        Bm = ident
        R, Ri = ident, ident
        for j in range(k):
            Bm = GA.mat_mul(Bm, _T(C[j]))
            n = GA.mat_mul(_T(C[j]), C[j])
            # the one-plane rotor of (1), (1/r)(1 + (r^2 - 1) n), and its inverse r(1 + (1/r^2 - 1) n)
            R = GA.mat_mul(R, [[(ident[a][b] + (r * r - 1) * n[a][b]) / r for b in range(dim)] for a in range(dim)])
            Ri = GA.mat_mul(Ri, [[r * (ident[a][b] + (1 / (r * r) - 1) * n[a][b]) for b in range(dim)]
                                 for a in range(dim)])
        P = GA.mat_mul(_T(Bm), Bm)
        ok = ok and GA.mat_mul(R, Ri) == ident and GA.mat_mul(P, P) == P and sum(P[i][i] for i in range(dim)) == 1
        Bb = GA.mat_mul(GA.mat_mul(R, Bm), Ri)
        ok = ok and Bb == [[r ** (2 * k) * x for x in row] for row in Bm]
        ok = ok and GA.mat_mul(_T(Bb), Bb) == [[r ** (4 * k) * x for x in row] for row in P]
    GA.check("uniform real boost on k planes: norm-one c_1*...c_k* goes to norm r^(2k): unbounded", ok)
    return ok


def check_imaginary_rapidity_is_unitary_phase():
    premise("field-theory.imported-tower-limit")
    v, vs = _modes()
    vq, vsq = _q(v), _q(vs)
    Nq = _mul(vsq, vq)
    ok = True
    for (c, s) in PHASES:
        R = {(): QI(c), (0, 1): QI(0, s)}
        Ri = {(): QI(c), (0, 1): QI(0, -s)}
        half = QI(c, -s)                          # e^(-i phi/2)
        emi = half * half                         # e^(-i phi)
        ok = ok and GA.eq(_star(R, S1), Ri) and GA.eq(_mul(R, Ri), {(): QI(1)})
        Av = _ad(R, Ri, vq)
        ok = ok and GA.eq(Av, _scl(emi, vq)) and GA.eq(_star(Av, S1), _ad(R, Ri, vsq))
        G = GA.add({(): QI(1)}, _scl(emi.conj() - QI(1), Nq))
        ok = ok and GA.eq(R, _scl(half, G))
    GA.check("imaginary rapidity: R unitary, Ad(R) v = e^(-i phi) v, a *-map; R = e^(-i phi/2) e^(i phi N)", ok)
    return ok
