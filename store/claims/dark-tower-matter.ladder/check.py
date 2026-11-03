"""dark-tower-matter.ladder: exact checks.

Setting as in T14c: causal tower V = R^(p,q), e_t of the minority sign, f = (1 + e_t e_a)/2,
S = Cl^0(V) f, field F = f Cl^0(V) f acting on the right, x^dag = e_t rev(x) e_t^-1,
j(psi) = <psi e_t rev(psi)>_1, N(x) = 2 <x x^dag>_0. A mixing U in M_n(F) acts by
psi'_i = sum_k psi_k U_ki; (U^dag)_ik = (U_ki)^dag. Built in GA.py, spinors symbolic (polynomial
ring over Q), all six causal towers (1,2), (2,1), (1,3), (3,1), (1,4), (4,1).

(1) F-unitary mixings preserve the total momentum, as a polynomial identity in the spinors'
    coordinates: for every unit u of F (the basis f e_K f) the rotation [[c f, -s u^dag],
    [s u, c f]] with (c, s) = (3/5, 4/5) and the phase diag(u, f) (n = 2), and a 3 x 3 signed
    permutation through u (n = 3); each satisfies U U^dag = 1, computed.
(2) Only unitary mixings do: two non-unitary mixings (diag(2f, f) and the shear [[f, f], [0, f]])
    change the momentum. The proof's core is checked: j(psi a) = N(a) j(psi) on samples
    (Lemma adjoint-norm (iii)), and the polarisation step is computed: the linear map from
    Hermitian X in M_2(F) to the quadratic form a -> sum_kl 2 <a_k X_kl a_l^dag>_0 on F^2 is
    injective (rank on sample rows a equals dim Herm_2(F) = 2 + dim F), so preserving every
    momentum forces U U^dag - 1 = 0.
(3) The groups: on F the adjoint is an anti-involution whose fixed space is R f, so the
    momentum-preserving Lie algebra {X : X + X^dag = 0} in M_n(F) has dimension
    n (dim F - 1) + dim F n(n-1)/2, which for n = 1, 2, 3 equals dim o(n), u(n), sp(n) exactly
    when dim F = 1, 2, 4: O(n) in the three-dimensional towers, U(n) in this tower and the
    mirror, Sp(n) in the five-dimensional towers.
"""
from fractions import Fraction as F

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


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


# the six causal towers: (p, q, index of e_t, index of the space direction e_a)
CAUSAL = [(1, 2, 0, 1), (2, 1, 2, 0), (1, 3, 0, 1), (3, 1, 3, 0), (1, 4, 0, 1), (4, 1, 4, 0)]
ROT = (F(3, 5), F(4, 5))
A_SAMPLES = [[F(1), F(2), F(-1), F(1, 2)], [F(0), F(1), F(3), F(-2)], [F(2), F(-1), F(1), F(1)],
             [F(1, 3), F(0), F(-2), F(1)], [F(-1), F(1), F(0), F(2)], [F(1), F(1), F(1), F(-1)],
             [F(2), F(0), F(1), F(3)], [F(0), F(-1), F(2), F(1)]]


def tower(p, q, t, a):
    S = GA.sig(p, q)
    n = p + q
    ev = [b for b in GA.all_blades(n) if len(b) % 2 == 0]
    f = GA.add(GA.sc(F(1, 2)), GA.scal(F(1, 2), GA.mul(GA.gen(t), GA.gen(a), S)))

    def basis_of(xs):
        vecs, B = [], []
        for x in xs:
            v = [x.get(b, F(0)) for b in ev]
            if any(v) and GA.rank_of_vectors(vecs + [v]) > len(vecs):
                vecs.append(v)
                B.append(x)
        return B
    B = basis_of([GA.mul({K: F(1)}, f, S) for K in ev])
    C = basis_of([GA.mul(GA.mul(f, {K: F(1)}, S), f, S) for K in ev])
    et = GA.gen(t)
    inv = GA.scal(F(1, S[t]), et)

    def dag(x):
        return GA.mul(GA.mul(et, GA.reverse(x), S), inv, S)

    def j(psi):
        return grade(GA.mul(GA.mul(psi, et, S), GA.reverse(psi), S), 1)

    def N(x):
        return GA.mul(x, dag(x), S).get((), F(0)) * 2
    return dict(S=S, n=n, f=f, ev=ev, B=B, C=C, dag=dag, j=j, N=N)


def sym(B, offset, nv):
    out = {}
    for i, b in enumerate(B):
        a = Poly.var(offset + i, nv)
        for k, v in b.items():
            out[k] = out.get(k, F(0)) + a * v
    return {k: v for k, v in out.items() if v != 0}


def mix(psis, U, S):
    n = len(psis)
    return [GA.add(*[GA.mul(psis[k], U[k][i], S) for k in range(n)]) for i in range(n)]


def total(psis, j):
    return GA.add(*[j(ps) for ps in psis])


def is_unitary(U, T):
    S, f, dag = T['S'], T['f'], T['dag']
    n = len(U)
    for k in range(n):
        for l in range(n):
            s = GA.add(*[GA.mul(U[k][i], dag(U[l][i]), S) for i in range(n)])
            if not GA.eq(s, f if k == l else {}):
                return False
    return True


def check_unitary_mixings_preserve_momentum():
    premise("dark-tower-matter.adjoint-norm")
    premise("dark-tower-matter.constituents-field")
    count = 0
    for (p, q, t, a) in CAUSAL:
        T = tower(p, q, t, a)
        S, f, C, dag, j = T['S'], T['f'], T['C'], T['dag'], T['j']
        d = len(T['B'])
        psis2 = [sym(T['B'], 0, 2 * d), sym(T['B'], d, 2 * d)]
        P2 = total(psis2, j)
        cs, sn = ROT
        for u in C:
            rot = [[GA.scal(cs, f), GA.scal(-sn, dag(u))], [GA.scal(sn, u), GA.scal(cs, f)]]
            phase = [[u, {}], [{}, f]]
            for U in (rot, phase):
                assert is_unitary(U, T)
                assert mv_eq(total(mix(psis2, U, S), j), P2)
                count += 1
        # n = 3: a signed permutation through the last unit
        u = C[-1]
        psis3 = [sym(T['B'], 0, 3 * d), sym(T['B'], d, 3 * d), sym(T['B'], 2 * d, 3 * d)]
        U3 = [[{}, u, {}], [{}, {}, GA.scal(-1, f)], [f, {}, {}]]
        assert is_unitary(U3, T)
        assert mv_eq(total(mix(psis3, U3, S), j), total(psis3, j))
        count += 1
    assert count == 2 * (1 + 1 + 2 + 2 + 4 + 4) + 6
    return True


def check_only_unitary_mixings():
    premise("dark-tower-matter.adjoint-norm")
    premise("dark-tower-matter.constituents-field")
    for (p, q, t, a) in CAUSAL:
        T = tower(p, q, t, a)
        S, f, C, dag, j, N = T['S'], T['f'], T['C'], T['dag'], T['j'], T['N']
        d = len(T['B'])
        dimF = len(C)
        assert dimF == {3: 1, 4: 2, 5: 4}[T['n']]
        psis = [sym(T['B'], 0, 2 * d), sym(T['B'], d, 2 * d)]
        P = total(psis, j)
        for U in ([[GA.scal(2, f), {}], [{}, f]], [[f, f], [{}, f]]):
            assert not is_unitary(U, T)
            assert not mv_eq(total(mix(psis, U, S), j), P)
        # j(psi a) = N(a) j(psi) on a sample psi and the units and a mixed corner element
        psi = GA.add(*[GA.scal(F(k + 1, 2), b) for k, b in enumerate(T['B'])])
        amix = GA.add(*[GA.scal(F(k + 2), c) for k, c in enumerate(C)])
        for x in C + [amix]:
            assert GA.eq(j(GA.mul(psi, x, S)), GA.scal(N(x), j(psi)))
        assert N(amix) == sum(F(k + 2) ** 2 for k in range(dimF))
        # polarisation: Hermitian X in M_2(F) -> sum_kl 2 <a_k X_kl a_l^dag>_0 is injective
        herm = []
        for c in C:
            herm.append([[{}, c], [dag(c), {}]])       # off-diagonal pair
        herm.append([[f, {}], [{}, {}]])
        herm.append([[{}, {}], [{}, f]])
        rows = []
        for r, s in enumerate(A_SAMPLES):
            s2 = A_SAMPLES[(r + 3) % len(A_SAMPLES)]
            avec = [GA.add(*[GA.scal(s[i], C[i]) for i in range(dimF)]),
                    GA.add(*[GA.scal(s2[i], C[i]) for i in range(dimF)])]
            row = []
            for X in herm:
                val = F(0)
                for k in range(2):
                    for l in range(2):
                        val += GA.mul(GA.mul(avec[k], X[k][l], S), dag(avec[l]), S).get((), F(0)) * 2
                row.append(val)
            rows.append(row)
        assert GA.rank_of_vectors(rows) == dimF + 2
        assert len(herm) == dimF + 2
    return True


def check_momentum_preserving_groups():
    premise("dark-tower-matter.constituents-field")
    expected = {1: lambda n: n * (n - 1) // 2,          # o(n)
                2: lambda n: n * n,                      # u(n)
                4: lambda n: n * (2 * n + 1)}            # sp(n)
    seen = {}
    for (p, q, t, a) in CAUSAL:
        T = tower(p, q, t, a)
        S, f, C, dag = T['S'], T['f'], T['C'], T['dag']
        dimF = len(C)
        # the adjoint maps F to F and is an anti-involution: (xy)^dag = y^dag x^dag
        for x in C:
            assert GA.eq(dag(dag(x)), x)
            for y in C:
                assert GA.eq(dag(GA.mul(x, y, S)), GA.mul(dag(y), dag(x), S))
        # its fixed space in F is R f; the anti-fixed space has dimension dim F - 1
        fixed = [GA.add(c, dag(c)) for c in C]
        anti = [GA.sub(c, dag(c)) for c in C]
        ev = T['ev']
        rk = lambda xs: GA.rank_of_vectors([[x.get(b, F(0)) for b in ev] for x in xs]) if any(xs) else 0
        assert rk(fixed) == 1 and GA.eq(fixed[0], GA.scal(2, f))
        assert rk(anti) == dimF - 1
        for n in (1, 2, 3):
            dim_alg = n * rk(anti) + dimF * (n * (n - 1) // 2)
            assert dim_alg == expected[dimF](n)
        seen[(p, q)] = dimF
    assert seen == {(1, 2): 1, (2, 1): 1, (1, 3): 2, (3, 1): 2, (1, 4): 4, (4, 1): 4}
    return True
