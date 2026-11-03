"""transport.pseudo-inverse-torsor: exact checks.

Setting (GA.py): V = R^{p,q} mixed with n >= 3 (generators 0..p-1 square +1, p..n-1 square -1); the null
v = (e_0 + e_p)/2 and partner w0 = (e_0 - e_p)/2 (v w0 + w0 v = 1); U = the span of the other generators of
V; the extension V' adds generators of square +1, -1 or 0; U' = U + V-perp. Elements of Cl(V') are
expanded in {1, v, w0, v w0} x blades(U') by an exact solve; the Cl(U')-slot of a pseudo-inverse is its
class label. S(v) = {sigma : v sigma v = v}; L = v Cl(V') the left ideal; R_u = 1 + v u, u in U.
(1) L meets Cl(U') in 0 (rank of the union is dim L + 2^k with dim L = 2^(k+1)); every sampled
    pseudo-inverse (w0 plus sampled elements of the computed kernel of s -> v s v) has gamma-slot 1 and
    differs from w0 + alpha (alpha its Cl(U')-slot) by an element of L; w0 + alpha + xi is again a
    pseudo-inverse for every xi in Cl(U'), so T(v) is affine over Cl(U').
(2) R_u maps S(v) to S(v) and L to L (every basis element v b), and the class of R_u (w0 + alpha) R_u^-1
    is w0 + alpha - u, for sample u (null and non-null) and alpha of mixed grades; the linear part is
    trivial (the class of R_u (w0 + alpha + xi) R_u^-1 is the previous class plus xi).
(3) u -> [sigma0] - u is injective on U; the cocycle [sigma0] - R_u [sigma0] equals u at two base points;
    R_u R_u' = R_{u+u'} and the cocycle is additive.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

CASES = [(1, 2, ()), (2, 1, ()), (2, 2, ()), (1, 3, ()), (3, 1, ()),
         (1, 2, (0,)), (2, 1, (1, -1)), (1, 3, (1,))]
ALPHAS = [[((), 2), ((0,), -1), ((0, 1), 3)], [((1,), 4), ((), F(-1, 2))]]
XIS = [[((0,), 1), ((0, 1), -2)], [((), 3)]]
U_COEFFS = [[1], [2, 1], [1, 1], [1, 0, -1], [3, 1, 2]]


def setup(p, q, extra):
    n = p + q
    sq = GA.sig(p, q) + tuple(extra)
    m = n + len(extra)
    v = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(p)))
    w0 = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(p)))
    ugens = [i for i in range(n) if i not in (0, p)]
    uprime = [i for i in range(m) if i not in (0, p)]
    return sq, m, v, w0, ugens, uprime


def m3(x, y, z, sq):
    return GA.mul(GA.mul(x, y, sq), z, sq)


def ublades(uprime):
    return [tuple(uprime[i] for i in b) for b in GA.all_blades(len(uprime))]


def co(x, blades):
    return [x.get(b, F(0)) for b in blades]


class Frame(object):
    def __init__(self, p, q, extra):
        self.sq, self.m, self.v, self.w0, self.ugens, self.uprime = setup(p, q, extra)
        self.blades = GA.all_blades(self.m)
        self.ub = ublades(self.uprime)
        h = [GA.sc(1), self.v, self.w0, GA.mul(self.v, self.w0, self.sq)]
        self.basis = [GA.mul(hh, {b: F(1)}, self.sq) for hh in h for b in self.ub]
        self.Mx = [[self.basis[j].get(b, F(0)) for j in range(len(self.basis))] for b in self.blades]
        self.L = [GA.mul(self.v, {b: F(1)}, self.sq) for b in self.blades]
        self.rL = GA.rank_of_vectors([co(x, self.blades) for x in self.L])

    def slots(self, x):
        c = GA.field_solve(self.Mx, co(x, self.blades))
        nb = len(self.ub)
        return [{self.ub[i]: c[k * nb + i] for i in range(nb) if c[k * nb + i]} for k in range(4)]

    def in_L(self, x):
        return GA.rank_of_vectors([co(y, self.blades) for y in self.L] + [co(x, self.blades)]) == self.rL

    def elem(self, spec):
        out = {}
        for b, c in spec:
            if all(i < len(self.uprime) for i in b):
                out = GA.add(out, {tuple(self.uprime[i] for i in b): F(c)})
        return out

    def is_pinv(self, s):
        return GA.eq(m3(self.v, s, self.v, self.sq), self.v)

    def conj(self, u, x):
        R = GA.add(GA.sc(1), GA.mul(self.v, u, self.sq))
        Ri = GA.sub(GA.sc(1), GA.mul(self.v, u, self.sq))
        return m3(R, x, Ri, self.sq)

    def us(self):
        out = []
        for uc in U_COEFFS:
            if len(uc) <= len(self.ugens):
                out.append(GA.add(*[GA.scal(c, GA.gen(i)) for c, i in zip(uc, self.ugens) if c]))
        return out


def check_classes_have_unique_normal_form():
    premise("transport.splitting-along-hyperbolic-plane")
    premise("transport.no-go-level-elements")
    ok = True
    for p, q, extra in CASES:
        fr = Frame(p, q, extra)
        k = len(fr.uprime)
        ok = ok and fr.rL == 2 ** (k + 1)
        ok = ok and GA.rank_of_vectors([co(x, fr.blades) for x in fr.L] +
                                       [co({b: F(1)}, fr.blades) for b in fr.ub]) == fr.rL + 2 ** k
        A = [[m3(fr.v, {b: F(1)}, fr.v, fr.sq).get(r, F(0)) for b in fr.blades] for r in fr.blades]
        ker = GA.field_kernel(A)
        for kv in ker[:6] + [[F(j % 3 - 1) for j in range(len(fr.blades))]]:
            x = {b: c for b, c in zip(fr.blades, kv) if c}
            if not GA.is_zero(m3(fr.v, x, fr.v, fr.sq)):
                continue
            s = GA.add(fr.w0, x)
            sl = fr.slots(s)
            ok = ok and fr.is_pinv(s) and GA.eq(sl[2], GA.sc(1))
            ok = ok and fr.in_L(GA.sub(s, GA.add(fr.w0, sl[0])))
        for a in ALPHAS:
            for xi in XIS:
                ok = ok and fr.is_pinv(GA.add(fr.w0, fr.elem(a), fr.elem(xi)))
    _tp_rv = (ok); assert _tp_rv is not False, "check_classes_have_unique_normal_form"; return _tp_rv


def check_null_rotations_translate_classes():
    premise("transport.no-go-level-elements")
    ok = True
    n_tested = 0
    for p, q, extra in CASES:
        fr = Frame(p, q, extra)
        for u in fr.us():
            for b in fr.blades:
                ok = ok and fr.in_L(fr.conj(u, GA.mul(fr.v, {b: F(1)}, fr.sq)))
            for a in ALPHAS:
                al = fr.elem(a)
                s = GA.add(fr.w0, al, GA.mul(fr.v, fr.elem(XIS[0]), fr.sq))
                t = fr.conj(u, s)
                ok = ok and fr.is_pinv(s) and fr.is_pinv(t)
                ok = ok and GA.eq(fr.slots(t)[0], GA.sub(al, u))
                for xi in XIS:
                    t2 = fr.conj(u, GA.add(s, fr.elem(xi)))
                    ok = ok and GA.eq(fr.slots(t2)[0], GA.add(GA.sub(al, u), fr.elem(xi)))
                n_tested += 1
    ok = ok and n_tested == 32
    _tp_rv = (ok); assert _tp_rv is not False, "check_null_rotations_translate_classes"; return _tp_rv


def check_orbit_is_a_torsor_with_tautological_cocycle():
    premise("transport.no-go-level-elements")
    ok = True
    for p, q, extra in CASES:
        fr = Frame(p, q, extra)
        us = fr.us()
        dimU = len(fr.ugens)
        ok = ok and GA.rank_of_vectors([co(u, fr.blades) for u in us]) == min(dimU, len(us))
        for base in ALPHAS:
            s0 = GA.add(fr.w0, fr.elem(base))
            c0 = fr.slots(s0)[0]
            for u in us:
                cu = GA.sub(c0, fr.slots(fr.conj(u, s0))[0])
                ok = ok and GA.eq(cu, u)
                for u2 in us:
                    R1 = GA.add(GA.sc(1), GA.mul(fr.v, u, fr.sq))
                    R2 = GA.add(GA.sc(1), GA.mul(fr.v, u2, fr.sq))
                    R12 = GA.add(GA.sc(1), GA.mul(fr.v, GA.add(u, u2), fr.sq))
                    ok = ok and GA.eq(GA.mul(R1, R2, fr.sq), R12)
                    c12 = GA.sub(c0, fr.slots(fr.conj(GA.add(u, u2), s0))[0])
                    ok = ok and GA.eq(c12, GA.add(u, u2))
    _tp_rv = (ok); assert _tp_rv is not False, "check_orbit_is_a_torsor_with_tautological_cocycle"; return _tp_rv
