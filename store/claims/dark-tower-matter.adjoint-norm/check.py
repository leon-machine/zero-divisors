"""dark-tower-matter.adjoint-norm: exact checks, as polynomial identities.

The six causal towers (1,2), (2,1), (1,3), (3,1), (1,4), (4,1), with time direction e_t (the generator
of the minority sign). The adjoint is x^dag = e_t rev(x) e_t^-1. A primitive idempotent f of the even
subalgebra Cl^0(V) is built greedily from commuting even blades of square +1 (f = prod (1 + e_T)/2, each
factor lowering dim Cl^0 f); S = Cl^0(V) f with an exact basis, the corner f Cl^0 f with an exact basis
(the field, premise: the imported Clifford structure, its (iii)). j(psi) = <psi e_t rev(psi)>_1.
A small polynomial ring over Q (dict of exponent tuples) is used as the coefficient ring of GA.mul, so
each identity below holds for every value of the coordinates, not on samples.
(i) e_K e_K^dag = Q(e_t)^|K| for every basis blade; = 1 on even blades; for a general even x with
symbolic coordinates, <x x^dag>_0 is the sum of the squares of the coordinates.
(ii) f^dag = f; for x in f Cl^0 f with symbolic coordinates, x^dag x = x x^dag = N(x) f with
N(x) = 2 <x x^dag>_0, and N is a positive multiple of the sum of squares of x's coordinates in the
corner basis (so N(x) = 0 only at x = 0).
(iii) j(psi x) = N(x) j(psi) for symbolic psi in S and x in the corner.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

CAUSAL = [(1, 2, 0), (2, 1, 2), (1, 3, 0), (3, 1, 3), (1, 4, 0), (4, 1, 4)]
# Variable layout in check_norm_law: psi takes polynomial variables PSI_FIRST_VAR.., x the c after psi's d.
PSI_FIRST_VAR = 0


class Poly(object):
    """Polynomials over Q in nv variables: {exponent tuple: Fraction}."""
    __slots__ = ("t",)

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
        if o == 0 or not self.t:
            return Poly() if o == 0 else Poly({(): o})
        return Poly({(0,) * len(next(iter(self.t))): o})

    def __add__(self, o):
        o = self._co(o)
        if not self.t:
            return o
        if not o.t:
            return self
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, 0) + v
        return Poly(r)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()})

    def __sub__(self, o):
        return self + (-self._co(o))

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

    __hash__ = None


def mv_eq(x, y):
    return all((x.get(k, 0) - y.get(k, 0)) == 0 for k in set(x) | set(y))


def scal_mv(c, x):
    return {b: c * v for b, v in x.items()}


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def setup(p, q, t):
    sq = GA.sig(p, q)
    n = p + q
    ev = [b for b in GA.all_blades(n) if len(b) % 2 == 0]

    def co(x):
        return [x.get(b, F(0)) for b in ev]

    def dim_left(f):
        return GA.rank_of_vectors([co(GA.mul({b: F(1)}, f, sq)) for b in ev])
    f, d, chosen = GA.sc(1), len(ev), []
    for b in ev:
        if b and GA.mul({b: F(1)}, {b: F(1)}, sq) == {(): F(1)} and \
                all(GA.commutes({b: F(1)}, {c: F(1)}, sq) for c in chosen):
            f2 = GA.mul(f, GA.scal(F(1, 2), GA.add(GA.sc(1), {b: F(1)})), sq)
            d2 = dim_left(f2)
            if 0 < d2 < d:
                f, d, chosen = f2, d2, chosen + [b]

    def basis_of(elts):
        rows, out = [], []
        for x in elts:
            if x and GA.rank_of_vectors(rows + [co(x)]) > len(rows):
                rows.append(co(x))
                out.append(x)
        return out
    S = basis_of([GA.mul({b: F(1)}, f, sq) for b in ev])
    C = basis_of([GA.mul(GA.mul(f, {b: F(1)}, sq), f, sq) for b in ev])
    et = GA.gen(t)
    inv = {(t,): F(1) / sq[t]}

    def dag(x):
        return GA.mul(GA.mul(et, GA.reverse(x), sq), inv, sq)

    def j(psi):
        return grade(GA.mul(GA.mul(psi, et, sq), GA.reverse(psi), sq), 1)
    return dict(sq=sq, n=n, ev=ev, f=f, S=S, C=C, et=et, Qt=sq[t], dag=dag, j=j)


def sym_combo(B, offset, nv):
    out = {}
    for i, b in enumerate(B):
        a = Poly.var(offset + i, nv)
        for k, v in b.items():
            out[k] = out.get(k, F(0)) + a * v
    return {k: v for k, v in out.items() if v != 0}


def check_blade_adjoint_norms():
    premise("dark-tower-matter.imported-clifford-structure")
    ok = True
    for p, q, t in CAUSAL:
        sq = GA.sig(p, q)
        et = GA.gen(t)
        inv = {(t,): F(1) / sq[t]}
        ok = ok and sq[t] == (1 if p == 1 else -1)
        for K in GA.all_blades(p + q):
            eK = {K: F(1)}
            prod_ = GA.mul(eK, GA.mul(GA.mul(et, GA.reverse(eK), sq), inv, sq), sq)
            ok = ok and prod_ == {(): F(sq[t]) ** len(K)}
            if len(K) % 2 == 0:
                ok = ok and prod_ == {(): F(1)}
        T = setup(p, q, t)
        nv = len(T["ev"])
        x = sym_combo([{b: F(1)} for b in T["ev"]], 0, nv)
        s0 = GA.mul(x, T["dag"](x), sq).get((), Poly())
        ssq = Poly()
        for i in range(nv):
            ssq = ssq + Poly.var(i, nv) * Poly.var(i, nv)
        ok = ok and s0 == ssq
    GA.check("lem:norm(i): e_K e_K^dag = Q(e_t)^|K|, 1 on even blades; <x x^dag>_0 = sum of squares for even x "
             "(polynomial identity, six causal towers)", ok)
    return ok


def check_corner_conjugation_and_positive_norm():
    premise("dark-tower-matter.imported-clifford-structure")
    ok = True
    dims = []
    for p, q, t in CAUSAL:
        T = setup(p, q, t)
        sq, f, C, dag = T["sq"], T["f"], T["C"], T["dag"]
        c = len(C)
        dims.append(c)
        x = sym_combo(C, 0, c)
        xdx = GA.mul(dag(x), x, sq)
        xxd = GA.mul(x, dag(x), sq)
        Nx = xxd.get((), Poly()) * 2
        ok = ok and mv_eq(dag(f), f) and mv_eq(xdx, scal_mv(Nx, f)) and mv_eq(xxd, scal_mv(Nx, f))
        ssq = Poly()
        for i in range(c):
            ssq = ssq + Poly.var(i, c) * Poly.var(i, c)
        lead = Nx.t.get(tuple(2 if k == 0 else 0 for k in range(c)), F(0))
        ok = ok and lead > 0 and Nx == ssq * lead
    ok = ok and dims == [1, 1, 2, 2, 4, 4]
    GA.check("lem:norm(ii): f^dag = f; x^dag x = x x^dag = N(x) f on the corner, N a positive multiple of the sum "
             "of squares (fields R, R, C, C, H, H)", ok)
    return ok


def check_norm_law():
    premise("dark-tower-matter.imported-clifford-structure")
    ok = True
    for p, q, t in CAUSAL:
        T = setup(p, q, t)
        sq, B, C, dag, j = T["sq"], T["S"], T["C"], T["dag"], T["j"]
        d, c = len(B), len(C)
        nv = d + c
        psi = sym_combo(B, PSI_FIRST_VAR, nv)
        x = sym_combo(C, PSI_FIRST_VAR + d, nv)
        Nx = GA.mul(x, dag(x), sq).get((), Poly()) * 2
        ok = ok and mv_eq(j(GA.mul(psi, x, sq)), scal_mv(Nx, j(psi)))
        ok = ok and not mv_eq(j(psi), {})
    GA.check("lem:norm(iii): j(psi x) = N(x) j(psi) (polynomial identity, six causal towers)", ok)
    return ok
