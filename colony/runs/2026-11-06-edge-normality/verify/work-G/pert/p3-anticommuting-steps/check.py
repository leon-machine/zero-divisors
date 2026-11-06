"""synthesis.limits-as-null-steps: exact checks.

(1) Cl(0,0,1): f(x + rho) = f(x) + f'(x) rho for f = (x^3 + 3x)/(x^2 + 1), against hand-stated
    values.
(2) N commuting square-zero steps b_i: prod (1 + b_i) = exp(eps), eps = sum b_i, and
    eps^k = k! e_k(b), eps^(N+1) = 0; b_i = rho_{2i-1} rho_{2i} in Cl(0,0,2N) for N = 2..6, and
    b_i = n_{2i-1} n_{2i} for six orthogonal null vectors of Cl(6,6) (N = 3).
(3) Cl(1,1): with B = e_t e_r and l_+/- = e_t +/- e_r, an even R = alpha + beta B gives
    R l_+ R~ = (alpha - beta)^2 l_+; a nilpotent rapidity d (d = s rho1 rho2 in Cl(1,1,2)) gives
    exp(d B / 2) l_+ exp(-d B / 2) = (1 - d) l_+; the boost with R^2 = 5/4 + 3/4 B halves l_+ and
    doubles l_-.
(4) Half-angle rotors from the half turn, in the field Q(r_1, r_2, ...), r_1^2 = 2,
    r_(k+1)^2 = 2 + r_k, implemented exactly: R_(k+1)^2 = R_k and R_k R_k~ = 1 for k = 0..5 in
    Cl(2,0); (1 + R)^2 = 2(1 + <R>_0) R at rational rotors; Archimedes' recursion
    U_(k+1) (U_k + L_k) = 2 U_k L_k and L_(k+1)^2 = U_(k+1) L_k for L_k = 2^(k+1) s_k,
    U_k = L_k / c_k.
(5) Taylor coefficients of tan and arctan to degree 21 have odd denominators; exp's 1/k! has
    every prime p <= k in its denominator.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise


# ---------------------------------------------------------------------------
# exact arithmetic in K_j = Q(r_1, ..., r_j), r_1^2 = 2, r_(j+1)^2 = 2 + r_j
# ---------------------------------------------------------------------------
class Tw(object):
    __slots__ = ("lev", "u", "v")

    def __init__(self, lev, u, v=None):
        self.lev = lev
        if lev == 0:
            self.u, self.v = F(u), None
        else:
            self.u = lift(u, lev - 1)
            self.v = lift(0 if v is None else v, lev - 1)

    def rad2(self):
        """r_lev^2 as an element of K_(lev-1)."""
        return Tw(0, 2) if self.lev == 1 else lift(2, self.lev - 1) + root(self.lev - 1)

    def __add__(self, o):
        o = coerce(o)
        L = max(self.lev, o.lev)
        a, b = lift(self, L), lift(o, L)
        return Tw(0, a.u + b.u) if L == 0 else Tw(L, a.u + b.u, a.v + b.v)

    __radd__ = __add__

    def __neg__(self):
        return Tw(0, -self.u) if self.lev == 0 else Tw(self.lev, -self.u, -self.v)

    def __sub__(self, o):
        return self + (-coerce(o))

    def __rsub__(self, o):
        return coerce(o) - self

    def __mul__(self, o):
        o = coerce(o)
        L = max(self.lev, o.lev)
        a, b = lift(self, L), lift(o, L)
        if L == 0:
            return Tw(0, a.u * b.u)
        return Tw(L, a.u * b.u + a.v * b.v * a.rad2(), a.u * b.v + a.v * b.u)

    __rmul__ = __mul__

    def inv(self):
        if self.lev == 0:
            return Tw(0, 1 / self.u)
        nrm = self.u * self.u - self.v * self.v * self.rad2()
        ni = nrm.inv()
        return Tw(self.lev, self.u * ni, -self.v * ni)

    def __truediv__(self, o):
        return self * coerce(o).inv()

    def __rtruediv__(self, o):
        return coerce(o) * self.inv()

    def is_zero(self):
        return self.u == 0 if self.lev == 0 else (self.u.is_zero() and self.v.is_zero())

    def __eq__(self, o):
        return (self - coerce(o)).is_zero()

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return 0

    def num(self):
        """The rational value, for an element that lies in Q."""
        t = self
        while t.lev > 0:
            assert t.v.is_zero()
            t = t.u
        return t.u


def coerce(o):
    return o if isinstance(o, Tw) else Tw(0, o)


def lift(x, L):
    x = coerce(x)
    while x.lev < L:
        x = Tw(x.lev + 1, x, 0)
    return x


def root(j):
    """r_j as an element of K_j."""
    return Tw(j, 0, 1)


def tsc(c):
    return {(): coerce(c)}


# ---------------------------------------------------------------------------
def check_dual_number_derivative():
    premise("std-algebra.radical-ideal-and-quotient")
    D = GA.sig(0, 0, 1)
    rho = GA.gen(0)
    one = GA.sc(1)
    # f = (x^3 + 3x)/(x^2 + 1); hand-stated (x, f(x), f'(x)), f' = (x^4 + 3)/(x^2 + 1)^2
    for x, fx, dfx in ((0, 0, 3), (1, 2, 1), (2, F(14, 5), F(19, 25)), (F(-1, 3), F(-14, 15), F(61, 25))):
        xr = GA.add(GA.sc(x), rho)
        num = GA.add(GA.mul(GA.mul(xr, xr, D), xr, D), GA.scal(3, xr))
        den = GA.add(GA.mul(xr, xr, D), one)
        d0 = den.get((), F(0))
        d1 = den.get((0,), F(0))
        deninv = GA.sub(GA.sc(1 / d0), GA.scal(d1 / (d0 * d0), rho))
        assert GA.eq(GA.mul(den, deninv, D), one)
        val = GA.mul(num, deninv, D)
        assert GA.eq(val, GA.add(GA.sc(fx), GA.scal(dfx, rho)))
    return True


def esym(bs, k, S):
    out = {}
    for c in combinations(bs, k):
        t = GA.sc(1)
        for b in c:
            t = GA.mul(t, b, S)
        out = GA.add(out, t)
    return out


def steps_identity(bs, S):
    N = len(bs)
    eps = GA.add(*bs)
    prod = GA.sc(1)
    for b in bs:
        assert GA.is_zero(GA.mul(b, b, S))
        prod = GA.mul(prod, GA.add(GA.sc(1), b), S)
    for b in bs:
        for c in bs:
            assert GA.commutes(b, c, S)
    expo, pw, fact = {}, GA.sc(1), 1
    for k in range(N + 1):
        if k > 0:
            pw = GA.mul(pw, eps, S)
            fact *= k
        assert GA.eq(pw, GA.scal(fact, esym(bs, k, S)))
        expo = GA.add(expo, GA.scal(F(1, fact), pw))
    assert GA.is_zero(GA.mul(pw, eps, S))
    assert GA.eq(prod, expo)
    return len(expo)


def check_product_of_null_steps_is_the_exponential():
    premise("std-algebra.radical-ideal-and-quotient")
    premise("std-algebra.witt-basis-car")
    sizes = []
    for N in range(2, 7):
        S = GA.sig(0, 0, 2 * N)
        bs = [GA.gen(i) for i in range(N)]
        sizes.append(steps_identity(bs, S))
    assert sizes == [4, 8, 16, 32, 64]
    S = GA.sig(6, 6)
    nulls = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(6 + i))) for i in range(6)]
    for x in nulls:
        for y in nulls:
            assert GA.anticommutes(x, y, S)
    bs = [GA.mul(nulls[2 * i], nulls[2 * i + 1], S) for i in range(3)]
    assert steps_identity(bs, S) > 8
    return True


def check_boost_scales_the_null_vector():
    premise("std-algebra.bivector-exponential")
    S = GA.sig(1, 1, 2)
    et, er = GA.gen(0), GA.gen(1)
    B = GA.mul(et, er, S)
    lp, lm = GA.add(et, er), GA.sub(et, er)
    assert GA.eq(GA.mul(B, lp, S), GA.neg(lp)) and GA.eq(GA.mul(lp, B, S), lp)
    for s in (F(1), F(-3), F(2, 5)):
        d = GA.scal(s, GA.mul(GA.gen(2), GA.gen(3), S))
        assert GA.is_zero(GA.mul(d, d, S)) and GA.commutes(d, et, S) and GA.commutes(d, er, S)
        R = GA.add(GA.sc(1), GA.scal(F(1, 2), GA.mul(d, B, S)))
        Rr = GA.sub(GA.sc(1), GA.scal(F(1, 2), GA.mul(d, B, S)))
        assert GA.eq(GA.mul(R, Rr, S), GA.sc(1))
        assert GA.eq(GA.mul(GA.mul(R, lp, S), Rr, S), GA.sub(lp, GA.mul(d, lp, S)))
        assert GA.eq(GA.mul(GA.mul(R, lm, S), Rr, S), GA.add(lm, GA.mul(d, lm, S)))
    for al, be in ((F(3), F(1)), (F(5, 13), F(-2, 7))):
        R = GA.add(GA.sc(al), GA.scal(be, B))
        Rr = GA.sub(GA.sc(al), GA.scal(be, B))
        assert GA.eq(GA.mul(GA.mul(R, lp, S), Rr, S), GA.scal((al - be) ** 2, lp))
    R2 = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), B))
    assert GA.eq(GA.mul(R2, GA.sub(GA.sc(F(5, 4)), GA.scal(F(3, 4), B)), S), GA.sc(1))
    assert GA.eq(GA.mul(R2, lp, S), GA.scal(F(1, 2), lp))
    assert GA.eq(GA.mul(R2, lm, S), GA.scal(2, lm))
    return True


def check_half_angle_rotors_and_archimedes():
    premise("std-algebra.bivector-exponential")
    E = GA.sig(2, 0)
    I = {(0, 1): F(1)}
    # the identity behind the step: (1 + R)^2 = 2 (1 + <R>_0) R for every plane rotor
    for a, b in ((F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(0), F(-1)), (F(8, 17), F(-15, 17))):
        R = GA.add(GA.sc(a), GA.scal(b, I))
        assert GA.eq(GA.mul(R, GA.reverse(R), E), GA.sc(1))
        onep = GA.add(GA.sc(1), R)
        assert GA.eq(GA.mul(onep, onep, E), GA.scal(2 * (1 + a), R))
    # exact tower: R_0 = I (half turn), R_(k+1) = (1 + R_k) / |1 + R_k|
    cs, ss = [coerce(0)], [coerce(1)]
    for k in range(1, 7):
        ck = Tw(k, 0, F(1, 2))                       # c_k = r_k / 2
        assert ck * ck == (1 + cs[-1]) * F(1, 2)
        ss.append(ss[-1] / (2 * ck))
        cs.append(ck)
    for k in range(6):
        Rk = {(): cs[k], (0, 1): ss[k]}
        Rn = {(): cs[k + 1], (0, 1): ss[k + 1]}
        sq = GA.mul(Rn, Rn, E)
        assert (sq.get((), 0) - cs[k]).is_zero() and (sq.get((0, 1), 0) - ss[k]).is_zero()
        nrm = GA.mul(Rn, GA.reverse(Rn), E)
        assert (nrm.get((), 0) - 1).is_zero() and all(c.is_zero() for b, c in nrm.items() if b != ())
        assert (cs[k + 1] * cs[k + 1] + ss[k + 1] * ss[k + 1] - 1).is_zero()
    assert GA.eq(GA.mul(I, I, E), GA.sc(-1))
    # Archimedes: L_k = 2^(k+1) s_k (inscribed), U_k = L_k / c_k (circumscribed), k >= 1
    L = [None] + [2 ** (k + 1) * ss[k] for k in range(1, 7)]
    U = [None] + [L[k] / cs[k] for k in range(1, 7)]
    assert (L[1] * L[1]).num() == 8 and U[1].num() == 4
    for k in range(1, 6):
        assert U[k + 1] * (U[k] + L[k]) == 2 * U[k] * L[k]
        assert L[k + 1] * L[k + 1] == U[k + 1] * L[k]
    return True


def denominators_odd(series):
    return all(c.denominator % 2 == 1 for c in series)


def check_taylor_denominators():
    premise("std-algebra.bivector-exponential")
    N = 21
    sin = [F(0)] * (N + 1)
    cos = [F(0)] * (N + 1)
    fact = 1
    for k in range(N + 1):
        if k > 0:
            fact *= k
        if k % 2 == 1:
            sin[k] = F((-1) ** ((k - 1) // 2), fact)
        else:
            cos[k] = F((-1) ** (k // 2), fact)
    tan = GA.ps_mul(sin, GA.ps_inv(cos, N), N)
    assert tan[:8] == [0, 1, 0, F(1, 3), 0, F(2, 15), 0, F(17, 315)]
    assert tan[21] == F(18888466084, 194896477400625)
    one_plus_x2 = [F(1), F(0), F(1)]
    atan = GA.ps_int(GA.ps_inv(one_plus_x2, N - 1))
    assert atan[:6] == [0, 1, 0, F(-1, 3), 0, F(1, 5)]
    assert denominators_odd(tan) and denominators_odd(atan)
    expo = [F(1)]
    for k in range(1, N + 1):
        expo.append(expo[-1] / k)
    primes = [p for p in range(2, N + 1) if all(p % d for d in range(2, p))]
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]
    for p in primes:
        assert expo[p].denominator % p == 0
    assert not denominators_odd(expo)
    return True
