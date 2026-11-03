"""dark-tower-matter.where-mass-begins: exact checks.

Setting (T14c, Definition of ideals, fields and momentum): a causal tower V = R^(p,q), min(p,q) = 1,
e_t the basis vector of the minority sign, f = (1 + e_t e_a)/2 for a space direction e_a, the
spinor ideal S = Cl^0(V) f, the adjoint x^dag = e_t rev(x) e_t^-1, the momentum
j(psi) = <psi e_t rev(psi)>_1, and the squared mass m^2(P) = Q(e_t) Q(P). Everything is built in
GA.py; spinors are symbolic (a small polynomial ring over Q as GA coefficients), so the laws are
verified as polynomial identities in the coordinates of psi (resp. psi_1, psi_2) on a basis of S,
in all six causal towers (1,2), (2,1), (1,3), (3,1), (1,4), (4,1).

(i)   n = 3, 4: rev(psi) psi = 0 identically, Q(j(psi)) = 0, and
      m^2(j(psi_1) + j(psi_2)) = 2 <x x^dag>_0 with x = rev(psi_1) psi_2; <x x^dag>_0 is the sum of
      the squares of x's blade coordinates, so the mass vanishes exactly when x = 0. The sandwich
      structure of the proof is also checked: rev(phi) phi has grades 0 and 4 only, and in
      dimension four its grade-4 part is a multiple of the pseudoscalar (commuting with e_t e_a).
(ii)  n = 5: m^2(j(psi)) = (1/2) <x x^dag>_0 with x = rev(psi) psi; the pairing is not alternating
      (rev(psi) psi is not identically zero) and a nonzero psi with rev(psi) psi = 0 exists (found
      by a search over coefficients in {-1, 0, 1}), so the zero set is a nonzero proper cone.
(iii) Every tower: Q(e_t) (j(psi) . e_t) = <psi psi^dag>_0, a sum of squares, so all momenta lie
      in one closed half-space; on rational samples of three constituents the total momentum has
      m^2 > 0 (never spacelike) and Q(e_t) (P . e_t) equals the summed squares of their coordinates.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise


class Poly(object):
    """Polynomials over Q in nv variables: {exponent tuple: Fraction}."""
    __slots__ = ('t',)

    def __init__(self, t=None):
        self.t = {k: v for k, v in (t or {}).items() if v != 0}

    @staticmethod
    def var(i, n):
        e = [0] * n
        e[i] = 1
        return Poly({tuple(e): F(1)})

    def _co(self, o):
        if isinstance(o, Poly):
            return o
        o = F(o)
        if o == 0:
            return Poly()
        n = len(next(iter(self.t))) if self.t else 0
        return Poly({(0,) * n: o})

    def __add__(self, o):
        o = self._co(o)
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, 0) + v
        return Poly(r)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()})

    def __sub__(self, o):
        return self + (-self._co(o))

    def __rsub__(self, o):
        return self._co(o) + (-self)

    def __mul__(self, o):
        if not isinstance(o, Poly):
            o = F(o)
            return Poly({k: v * o for k, v in self.t.items()}) if o != 0 else Poly()
        r = {}
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                r[k] = r.get(k, 0) + v1 * v2
        return Poly(r)

    __rmul__ = __mul__

    def __eq__(self, o):
        return (self - self._co(o)).t == {}

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return id(self)


def mv_eq(x, y):
    keys = set(x) | set(y)
    return all((x.get(k, 0) - y.get(k, 0)) == 0 for k in keys)


def is_zero_mv(x):
    return all(v == 0 for v in x.values())


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def scal_mv(c, x):
    return {b: c * v for b, v in x.items()}


# the six causal towers: (p, q, index of e_t, index of the space direction e_a)
CAUSAL = [(1, 2, 0, 1), (2, 1, 2, 0), (1, 3, 0, 1), (3, 1, 3, 0), (1, 4, 0, 1), (4, 1, 4, 0)]


def tower(p, q, t, a):
    S = GA.sig(p, q)
    n = p + q
    ev = [b for b in GA.all_blades(n) if len(b) % 2 == 0]
    f = GA.add(GA.sc(F(1, 2)), GA.scal(F(1, 2), GA.mul(GA.gen(t), GA.gen(a), S)))
    vecs, B = [], []
    for K in ev:
        x = GA.mul({K: F(1)}, f, S)
        v = [x.get(b, F(0)) for b in ev]
        if GA.rank_of_vectors(vecs + [v]) > len(vecs):
            vecs.append(v)
            B.append(x)
    et = GA.gen(t)
    Qt = S[t]
    inv = GA.scal(F(1, Qt), et)

    def dag(x):
        return GA.mul(GA.mul(et, GA.reverse(x), S), inv, S)

    def j(psi):
        return grade(GA.mul(GA.mul(psi, et, S), GA.reverse(psi), S), 1)

    def Q(v):
        return GA.mul(v, v, S).get((), F(0))

    return dict(S=S, n=n, f=f, ev=ev, B=B, et=et, Qt=Qt, dag=dag, j=j, Q=Q)


def sym(B, offset, nv):
    out = {}
    for i, b in enumerate(B):
        a = Poly.var(offset + i, nv)
        for k, v in b.items():
            out[k] = out.get(k, F(0)) + a * v
    return {k: v for k, v in out.items() if v != 0}


def sum_sq_coords(x):
    s = Poly()
    for c in x.values():
        s = s + c * c
    return s


# rational sample spinors (coefficients on the basis of S) for the many-constituent clause
SAMPLES = [[F(1), F(-2), F(1, 3), F(0), F(3), F(-1), F(2, 5), F(1)],
           [F(-1), F(1, 2), F(2), F(-3), F(0), F(1), F(1), F(-2, 3)],
           [F(2), F(1), F(-1), F(1, 4), F(-1), F(0), F(3), F(1)]]


def check_dimensions_three_four_pair_law():
    premise("dark-tower-matter.adjoint-norm")
    for (p, q, t, a) in CAUSAL[:4]:
        T = tower(p, q, t, a)
        S, B, dag, j, Q, Qt = T['S'], T['B'], T['dag'], T['j'], T['Q'], T['Qt']
        d = len(B)
        assert d == {3: 2, 4: 4}[T['n']]
        nv = 2 * d
        psi1, psi2 = sym(B, 0, nv), sym(B, d, nv)
        # the reversion pairing is alternating and single momenta are null
        assert is_zero_mv(GA.mul(GA.reverse(psi1), psi1, S))
        assert Q(T['j'](psi1)) == 0
        # the pair law m^2 = Q(e_t) Q(P) = 2 <x x^dag>_0, x = rev(psi1) psi2
        x = GA.mul(GA.reverse(psi1), psi2, S)
        P = GA.add(j(psi1), j(psi2))
        m2 = Q(P) * Qt
        xxd0 = GA.mul(x, dag(x), S).get((), Poly())
        assert m2 == xxd0 * 2
        # <x x^dag>_0 is the sum of squares of x's coordinates: m^2 = 0 exactly when x = 0
        assert xxd0 == sum_sq_coords(x)
        assert not is_zero_mv(x)
        # the sandwich: rev(phi) phi has grades 0 and 4 only; in dimension four the 4-part is
        # a multiple of the pseudoscalar, which commutes with e_t e_a
        phi = sym([{K: F(1)} for K in T['ev']], 0, len(T['ev']))
        rp = GA.mul(GA.reverse(phi), phi, S)
        assert set(len(b) for b in rp) <= {0, 4}
        assert set(len(b) for b in rp if len(b) > 0) == ({4} if T['n'] == 4 else set())
    return True


def check_dimension_five_single_law():
    premise("dark-tower-matter.adjoint-norm")
    for (p, q, t, a) in CAUSAL[4:]:
        T = tower(p, q, t, a)
        S, B, dag, j, Q, Qt = T['S'], T['B'], T['dag'], T['j'], T['Q'], T['Qt']
        d = len(B)
        assert d == 8
        psi = sym(B, 0, d)
        x = GA.mul(GA.reverse(psi), psi, S)
        assert not is_zero_mv(x)                      # not alternating
        m2 = Q(j(psi)) * Qt
        xxd0 = GA.mul(x, dag(x), S).get((), Poly())
        assert m2 == xxd0 * F(1, 2)
        assert xxd0 == sum_sq_coords(x)
        # a nonzero massless constituent: rev(psi) psi = 0 for some psi != 0
        found = 0
        for coeffs in product((-1, 0, 1), repeat=d):
            if not any(coeffs):
                continue
            ps = GA.add(*[GA.scal(c, b) for c, b in zip(coeffs, B) if c])
            if ps and GA.mul(GA.reverse(ps), ps, S) == {}:
                found += 1
                assert Q(j(ps)) == 0                  # massless indeed
                break
        assert found == 1
    return True


def check_momenta_in_one_half_space():
    premise("dark-tower-matter.adjoint-norm")
    for (p, q, t, a) in CAUSAL:
        T = tower(p, q, t, a)
        S, B, dag, j, Q, Qt, et = T['S'], T['B'], T['dag'], T['j'], T['Q'], T['Qt'], T['et']
        d = len(B)
        psi = sym(B, 0, d)
        lhs = GA.mul(j(psi), et, S).get((), Poly()) * Qt
        rhs = GA.mul(psi, dag(psi), S).get((), Poly())
        assert lhs == rhs
        assert rhs == sum_sq_coords(psi)              # >= 0, = 0 only at psi = 0
        # three rational constituents: the total momentum is timelike or null, future side
        P, energy = {}, F(0)
        for s in SAMPLES:
            ps = GA.add(*[GA.scal(c, b) for c, b in zip(s[:d], B)])
            P = GA.add(P, j(ps))
            energy += sum(c * c for c in ps.values())
        assert Q(P) * Qt > 0
        assert GA.mul(P, et, S).get((), F(0)) * Qt == energy
    return True
