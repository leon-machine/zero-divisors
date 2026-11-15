"""synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state: exact checks.

m anticommuting switches are modelled in Cl(m,m) over the rationals with GA.py: generators
e_1..e_m of square +1 (indices 0..m-1), f_1..f_m of square -1 (indices m..2m-1),
v_a = (e_a + f_a)/2, w_a = (e_a - f_a)/2. The integer switch algebra is the integer span of the
ordered monomials v_S w_T inside it.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise


class Switches:
    def __init__(self, m):
        self.m = m
        self.sq = GA.sig(m, m)
        self.one = GA.sc(1)
        self.e = [GA.gen(a) for a in range(m)]
        self.f = [GA.gen(m + a) for a in range(m)]
        self.v = [GA.scal(F(1, 2), GA.add(self.e[a], self.f[a])) for a in range(m)]
        self.w = [GA.scal(F(1, 2), GA.sub(self.e[a], self.f[a])) for a in range(m)]
        self.n = [self.mul(self.v[a], self.w[a]) for a in range(m)]
        self.u = self.mul(*(self.e if m % 2 == 1 else self.f))
        s = self.mul(self.u, self.u)
        self.uinv = GA.scal(1 / s[()], self.u)

    def mul(self, *xs):
        r = xs[0]
        for x in xs[1:]:
            r = GA.mul(r, x, self.sq)
        return r

    def X(self, x):
        return self.mul(self.u, x, self.uinv)

    def flip(self, x):
        m = self.m
        return {b: (c if sum(1 for i in b if i >= m) % 2 == 0 else -c) for b, c in x.items()}

    def dagger(self, x):
        return self.flip(GA.reverse(x))

    def monomials(self):
        subsets = [s for r in range(self.m + 1) for s in combinations(range(self.m), r)]
        return [self.mul(self.one, *[self.v[a] for a in s], *[self.w[a] for a in t])
                for s in subsets for t in subsets]

    def state(self, sigma):
        """The integer state of the configuration sigma (1 = on): x -> 2^m sc(p_sigma x)."""
        p = self.mul(self.one, *[self.n[a] if sigma[a] else GA.sub(self.one, self.n[a])
                                 for a in range(self.m)])
        return lambda x: 2 ** (self.m - 1) * self.mul(p, x).get((), F(0))


def check_exchange_is_conjugation_by_a_product_of_directions():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    for m in range(1, 6):
        A = Switches(m)
        for a in range(m):
            assert A.mul(A.v[a], A.v[a]) == {} and A.mul(A.w[a], A.w[a]) == {}
            assert GA.add(A.mul(A.v[a], A.w[a]), A.mul(A.w[a], A.v[a])) == A.one
            assert A.mul(A.e[a], A.e[a]) == A.one and A.mul(A.f[a], A.f[a]) == GA.neg(A.one)
            for b in range(m):
                if a != b:
                    assert GA.anticommutes(A.v[a], A.v[b], A.sq) and GA.anticommutes(A.v[a], A.w[b], A.sq)
        uu = A.mul(A.u, A.u)
        sign = (-1) ** (m * (m - 1) // 2) if m % 2 == 1 else (-1) ** (m // 2)
        assert uu == GA.sc(sign)
        for a in range(m):
            assert GA.eq(A.X(A.v[a]), A.w[a]) and GA.eq(A.X(A.w[a]), A.v[a])
            assert GA.eq(A.X(A.e[a]), A.e[a]) and GA.eq(A.X(A.f[a]), GA.neg(A.f[a]))
            assert GA.eq(A.X(A.X(A.v[a])), A.v[a])
        # the other product of directions does not exchange: it sends v_a to -w_a
        other = A.mul(*(A.f if m % 2 == 1 else A.e))
        oinv = GA.scal(1 / A.mul(other, other)[()], other)
        assert GA.eq(A.mul(other, A.v[0], oinv), GA.neg(A.w[0]))
    return True


def check_what_the_exchange_fixes():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    premise("synthesis.integer-clifford-algebras-contain-no-switch")
    for m in range(1, 4):
        A = Switches(m)
        # every blade e_S f_T goes to (-1)^|T| times itself: the configuration is fixed
        for blade in GA.all_blades(2 * m):
            x = {blade: F(1)}
            t = sum(1 for i in blade if i >= m)
            assert GA.eq(A.X(x), GA.scal((-1) ** t, x))
            assert GA.eq(A.X(x), A.flip(x))
        # the implementer is a blade, an element of the integer ladder algebra
        assert len(A.u) == 1 and set(A.u.values()) == {F(1)}
        # the hyperbolic form on each plane
        for a in range(m):
            for al, be in product(range(-3, 4), repeat=2):
                x = GA.add(GA.scal(al, A.v[a]), GA.scal(be, A.w[a]))
                assert A.mul(x, x) == GA.sc(al * be)
                assert A.mul(A.X(x), A.X(x)) == GA.sc(al * be)
        # reversal commutes with the exchange; adjoint = exchange after reversal, an anti-automorphism
        mons = A.monomials()
        assert len(mons) == 4 ** m
        for x in mons:
            assert GA.eq(A.X(GA.reverse(x)), GA.reverse(A.X(x)))
            assert GA.eq(A.X(GA.grade_inv(x)), GA.grade_inv(A.X(x)))
        for a in range(m):
            assert GA.eq(A.dagger(A.v[a]), A.w[a]) and GA.eq(A.dagger(A.w[a]), A.v[a])
        x, y = mons[3], mons[-2]
        assert GA.eq(A.dagger(A.mul(x, y)), A.mul(A.dagger(y), A.dagger(x)))
    return True


def check_what_the_exchange_moves():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    for m in range(1, 6):
        A = Switches(m)
        h = [GA.sub(A.one, GA.scal(2, A.n[a])) for a in range(m)]
        for a in range(m):
            assert GA.eq(h[a], A.mul(A.e[a], A.f[a]))
            assert GA.eq(A.X(A.n[a]), GA.sub(A.one, A.n[a]))
            assert GA.eq(A.X(h[a]), GA.neg(h[a]))
        number = GA.add(*A.n)
        assert GA.eq(A.X(number), GA.sub(GA.sc(m), number))
        omega = A.mul(*h)
        assert GA.eq(A.X(omega), GA.scal((-1) ** m, omega))
        p_off = A.mul(A.one, *[GA.sub(A.one, A.n[a]) for a in range(m)])
        p_on = A.mul(A.one, *A.n)
        assert GA.eq(A.X(p_off), p_on) and GA.eq(A.X(p_on), p_off) and not GA.eq(p_off, p_on)
        for a in range(m):
            assert A.mul(A.w[a], p_off) == {} and A.mul(A.v[a], p_on) == {}
            assert A.mul(A.v[a], p_off) != {}
    return True


def check_integer_states_choose_an_orientation():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    premise("synthesis.integer-clifford-algebras-contain-no-switch")
    for m in range(1, 4):
        A = Switches(m)
        mons = A.monomials()
        charges = set()
        for sigma in product((0, 1), repeat=m):
            st = A.state(sigma)
            assert st(A.one) == 1
            assert all(st(x) in (0, 1, -1) for x in mons)          # integer on the integer span
            for a in range(m):
                assert st(A.n[a]) == sigma[a]
                assert st(A.mul(A.v[a], A.dagger(A.v[a]))) == sigma[a]
                assert st(A.mul(A.w[a], A.dagger(A.w[a]))) == 1 - sigma[a]
            q = sum(st(GA.sub(GA.scal(2, A.n[a]), A.one)) for a in range(m))
            assert q == 2 * sum(sigma) - m and (q - m) % 2 == 0
            bar = A.state(tuple(1 - s for s in sigma))
            assert all(st(A.X(x)) == bar(x) for x in mons)          # the exchange reverses the charge
            charges.add(q)
        assert charges == set(range(-m, m + 1, 2))
        assert (0 in charges) == (m % 2 == 0)
        # the scalar part is exchange-invariant, takes the value 1/2 on each n_a, and is integral
        # on the blades (the integer ladder algebra) but not on the integer switch algebra
        tau = lambda x: x.get((), F(0))
        assert all(tau(A.X(x)) == tau(x) for x in mons)
        assert all(2 * tau(A.n[a]) == 1 for a in range(m))
        assert all(tau({b: F(1)}) in (0, 1) for b in GA.all_blades(2 * m))
    return True
