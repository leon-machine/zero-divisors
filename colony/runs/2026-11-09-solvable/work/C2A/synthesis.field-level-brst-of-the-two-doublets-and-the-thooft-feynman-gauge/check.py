"""synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge: exact checks.

The jet algebra and differential of the stored field-level BRST result (A^a_mu, B^a even, c^a, cb^a odd, the gauge
algebra su(2) + su(3) + u(1) as bivectors of Cl(9,0) with T_1..T_3 = (1/2) e_12, e_20, e_01 and T_12 = J/2), extended
by eight even scalar fields h^i, the two doublets: each doublet is an even element phi = phi^0 + phi^1 e_12 +
phi^2 e_02 + phi^3 e_01 of Cl(3,0) on e_0, e_1, e_2 (a GA quaternion); su(2) acts by left multiplication by T_a,
colour trivially, and the u(1) generator T_12 by right multiplication by y e_12 (y the hypercharge normalisation).
rho_a are the resulting real 8 x 8 matrices (GA products), <.,.> the scalar part of phi~ psi (the Euclidean form on
the components). phi = v + h with a constant vacuum v (eight formal constants v_i, or rational numbers).
s h = -g rho(c)(v + h), s A, s c, s cb, s B as stored; D_mu phi = d_mu h + g rho(A_mu)(v + h).
't Hooft fermion Psi = kappa_ab cb^a (nabla.A^b + (xi/2) B^b) - xi g cb^a <rho_a v, h>.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


class _Zero(object):
    def __getitem__(self, k):
        return F(0)


ZSQ = _Zero()          # Grassmann generators: degenerate Clifford generators of square 0
G4 = (1, -1, -1, -1)   # spacetime signature of the store

# ---------------------------------------------------------------- the gauge algebra as bivectors
E9 = GA.sig(9, 0)


def _bv(i, j):
    return GA.mul(GA.gen(i), GA.gen(j), E9)


def _comm(x, y):
    return GA.sub(GA.mul(x, y, E9), GA.mul(y, x, E9))


def gauge_bivectors():
    half = lambda x: GA.scal(F(1, 2), x)
    su2 = [half(_bv(1, 2)), half(_bv(2, 0)), half(_bv(0, 1))]
    J = GA.add(_bv(3, 4), _bv(5, 6), _bv(7, 8))
    so6 = [_bv(i, j) for i in range(3, 9) for j in range(i + 1, 9)]
    # commutant of J in so(6): kernel of B -> [B, J]
    rows = sorted({b for x in so6 for b in _comm(x, J)})
    M = [[_comm(x, J).get(r, F(0)) for x in so6] for r in rows]
    ker = GA.field_kernel(M) if rows else None
    u3 = [GA.add(*[GA.scal(v[i], so6[i]) for i in range(len(so6)) if v[i] != 0]) for v in ker]
    # traceless part: orthogonal to J for <X Y>_0
    ip = lambda x, y: GA.mul(x, y, E9).get((), F(0))
    jj = ip(J, J)
    su3 = []
    for x in u3:
        y = GA.sub(x, GA.scal(ip(x, J) / jj, J))
        if not GA.is_zero(y):
            su3.append(y)
    # independent 8
    basis = []
    for y in su3:
        trial = basis + [y]
        keys = sorted({b for z in trial for b in z})
        if GA.field_rank([[z.get(k, F(0)) for k in keys] for z in trial]) == len(trial):
            basis.append(y)
    return su2 + basis + [half(J)]


def structure_constants(gens):
    keys = sorted({b for z in gens for b in z})
    n = len(gens)
    fs = {}
    for a in range(n):
        for b in range(n):
            cm = _comm(gens[a], gens[b])
            if GA.is_zero(cm):
                continue
            ks = sorted(set(keys) | set(cm))
            M = [[gens[c].get(k, F(0)) for c in range(n)] for k in ks]
            rhs = [cm.get(k, F(0)) for k in ks]
            ker = GA.field_kernel([M[i] + [rhs[i]] for i in range(len(ks))])
            pick = [v for v in ker if v[n] != 0]
            if len(pick) != 1:
                raise ValueError("commutator leaves the span")
            sol = [-x / pick[0][n] for x in pick[0][:n]]
            for c in range(n):
                if sol[c] != 0:
                    fs[(a, b, c)] = sol[c]
    return fs


# ---------------------------------------------------------------- superpolynomials on jets
_ODD = {}
_ODDK = []


def oid(key):
    if key not in _ODD:
        _ODD[key] = len(_ODDK)
        _ODDK.append(key)
    return _ODD[key]


def _odd_sort(lst):
    return GA.blade_mul(tuple(lst), (), ZSQ) if lst else (F(1), ())


def P_even(key):
    return {((key,), ()): F(1)}


def P_odd(key):
    return {((), (oid(key),)): F(1)}


def P_const(c):
    return {((), ()): F(c)} if c != 0 else {}


def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def psc(c, p):
    c = F(c)
    return {k: c * v for k, v in p.items()} if c != 0 else {}


def pmul(p, q):
    out = {}
    for (e1, o1), v1 in p.items():
        for (e2, o2), v2 in q.items():
            s, o = GA.blade_mul(o1, o2, ZSQ)
            if s == 0:
                continue
            e = tuple(sorted(e1 + e2))
            k = (e, o)
            out[k] = out.get(k, F(0)) + s * v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def _shift(key, mu):
    J = list(key[-1])
    J[mu] += 1
    return key[:-1] + (tuple(J),)


def _is_jet(key):
    return key[0] in ('A', 'B', 'c', 'cb', 'h')


def D(mu, p):
    """Total derivative d_mu (even derivation; the coupling and gauge parameters are constants)."""
    out = {}
    for (e, o), v in p.items():
        for i, x in enumerate(e):
            if not _is_jet(x):
                continue
            e2 = tuple(sorted(e[:i] + e[i + 1:] + (_shift(x, mu),)))
            out[(e2, o)] = out.get((e2, o), F(0)) + v
        for j, y in enumerate(o):
            lst = list(o)
            lst[j] = oid(_shift(_ODDK[y], mu))
            s, o2 = _odd_sort(lst)
            if s == 0:
                continue
            out[(e, o2)] = out.get((e, o2), F(0)) + s * v
    return {k: v for k, v in out.items() if v != 0}


def DJ(J, p):
    for mu in range(4):
        for _ in range(J[mu]):
            p = D(mu, p)
    return p


Z4 = (0, 0, 0, 0)


def unit(mu):
    return tuple(1 if i == mu else 0 for i in range(4))


class BRST(object):
    """s on generators: s A^a_mu = d_mu c^a + g f_bc^a A^b_mu c^c, s c^a = -(g/2) f_bc^a c^b c^c,
    s cb^a = B^a, s B^a = 0; s(x_J) = d_J (s x); s an odd derivation from the left."""

    def __init__(self, fs, n, half=F(1, 2), cov=True, rho=None, vev=None, sign=-1):
        self.fs, self.n, self.half, self.cov = fs, n, half, cov
        self.rho, self.vev, self.sign = rho, vev, sign
        self.memo = {}
        self.g = P_even(('g',))

    def gen(self, key):
        if key in self.memo:
            return self.memo[key]
        kind, J = key[0], key[-1]
        if J != Z4:
            base = list(key[:-1]) + [Z4]
            r = DJ(J, self.gen(tuple(base)))
        elif kind == 'A':
            a, mu = key[1], key[2]
            r = D(mu, P_odd(('c', a, Z4)))
            if self.cov:
                for (b, c, aa), v in self.fs.items():
                    if aa == a:
                        r = padd(r, psc(v, pmul(self.g, pmul(P_even(('A', b, mu, Z4)), P_odd(('c', c, Z4))))))
        elif kind == 'c':
            a = key[1]
            r = {}
            for (b, c, aa), v in self.fs.items():
                if aa == a:
                    r = padd(r, psc(-self.half * v, pmul(self.g, pmul(P_odd(('c', b, Z4)), P_odd(('c', c, Z4))))))
        elif kind == 'cb':
            r = P_even(('B', key[1], Z4))
        elif kind == 'h':
            # s h^i = sign g sum_a c^a (rho_a (v + h))^i
            i = key[1]
            r = {}
            for a in range(self.n):
                for j in range(len(self.rho[a])):
                    w = self.rho[a][i][j]
                    if w:
                        phij = padd(self.vev[j], P_even(('h', j, Z4)))
                        r = padd(r, psc(self.sign * w, pmul(self.g, pmul(P_odd(('c', a, Z4)), phij))))
        else:
            r = {}
        self.memo[key] = r
        return r

    def __call__(self, p):
        out = {}
        for (e, o), v in p.items():
            evenpart = {(e, ()): F(1)}
            for i, x in enumerate(e):
                if not _is_jet(x):
                    continue
                rest = {(e[:i] + e[i + 1:], o): v}
                out = padd(out, pmul(self.gen(x), rest))
            for j, y in enumerate(o):
                sign = (-1) ** j
                left = {(e, o[:j]): v * sign}
                right = {((), o[j + 1:]): F(1)}
                out = padd(out, pmul(pmul(left, self.gen(_ODDK[y])), right))
        return out


def jets(order):
    out = [Z4]
    if order >= 1:
        out += [unit(m) for m in range(4)]
    if order >= 2:
        for m in range(4):
            for n in range(m, 4):
                J = [0] * 4
                J[m] += 1
                J[n] += 1
                out.append(tuple(J))
    return out


def s2_zero_on_generators(s, n, order):
    for J in jets(order):
        for a in range(n):
            for mu in range(4):
                if s(s.gen(('A', a, mu, J))):
                    return False
            if s(s.gen(('c', a, J))):
                return False
    return True


# ---------------------------------------------------------------- GA multivectors with polynomial coefficients
def mv_mul(X, Y):
    out = {}
    for b1, p in X.items():
        for b2, q in Y.items():
            sg, b = GA.blade_mul(b1, b2, G4)
            if sg == 0:
                continue
            out[b] = padd(out.get(b, {}), psc(sg, pmul(p, q)))
    return {b: p for b, p in out.items() if p}


def grade(X, r):
    return {b: p for b, p in X.items() if len(b) == r}


def mv_add(*Xs):
    out = {}
    for X in Xs:
        for b, p in X.items():
            out[b] = padd(out.get(b, {}), p)
    return {b: p for b, p in out.items() if p}


def mv_sc(c, X):
    return {b: psc(c, p) for b, p in X.items() if c != 0}


def mv_s(s, X):
    return {b: q for b, q in ((b, s(p)) for b, p in X.items()) if q}


def vecfield(a):
    # A^a = A^a_mu g^mu, g^mu = g^{mu mu} g_mu
    return {(mu,): psc(G4[mu], P_even(('A', a, mu, Z4))) for mu in range(4)}


def nabla(X):
    out = {}
    for mu in range(4):
        dX = {b: D(mu, p) for b, p in X.items()}
        out = mv_add(out, mv_mul({(mu,): P_const(G4[mu])}, dX))
    return out


def field_strength(fs, n, a):
    Fa = grade(nabla(vecfield(a)), 2)
    g = P_even(('g',))
    for (b, c, aa), v in fs.items():
        if aa == a:
            Fa = mv_add(Fa, mv_sc(F(1, 2) * v, mv_mul({(): g}, grade(mv_mul(vecfield(b), vecfield(c)), 2))))
    return Fa






# ---------------------------------------------------------------- the gauge algebra (as stored) and the doublets
_CACHE = {}


def _algebra():
    if 'g' not in _CACHE:
        gens = gauge_bivectors()
        _CACHE['g'] = gens
        _CACHE['f'] = structure_constants(gens)
    return _CACHE['g'], _CACHE['f']


def _ip9(x, y):
    return GA.mul(x, y, E9).get((), F(0))


def kappa():
    gens, _ = _algebra()
    return [[-_ip9(x, y) for y in gens] for x in gens]


E3 = GA.sig(3, 0)
QB = [(), (1, 2), (0, 2), (0, 1)]      # the even blades of Cl(3,0) on e_0, e_1, e_2


def _blade(b):
    return {b: F(1)} if b else GA.sc(1)


def _coords(x):
    return [x.get(b, F(0)) for b in QB]


def _left(T):
    cols = [_coords(GA.mul(T, _blade(b), E3)) for b in QB]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def _right(T):
    cols = [_coords(GA.mul(_blade(b), T, E3)) for b in QB]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


E12 = GA.mul(GA.gen(1), GA.gen(2), E3)


def doublet_rep(y, hyper_side="right"):
    """the 12 generators on two doublets (8 x 8): su(2) by left multiplication, colour 0, u(1) by y e_12 on the
    right (hyper_side='left' puts it on the left, which breaks the commutation with su(2))"""
    gens, _ = _algebra()
    out = []
    for a, T in enumerate(gens):
        if a < 3:
            R4 = _left(T)
        elif a == 11:
            R4 = _right(GA.scal(y, E12)) if hyper_side == "right" else _left(GA.scal(y, E12))
        else:
            R4 = [[F(0)] * 4 for _ in range(4)]
        M = [[F(0)] * 8 for _ in range(8)]
        for blk in (0, 4):
            for i in range(4):
                for j in range(4):
                    M[blk + i][blk + j] = R4[i][j]
        out.append(M)
    return out


def _mmul(A, B):
    return [[sum((A[i][l] * B[l][j] for l in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]


def rep_defects(rho):
    """(homomorphism failures, antisymmetry failures) of rho against the stored structure constants"""
    _, fs = _algebra()
    n = len(rho)
    hom = anti = 0
    for a in range(n):
        anti += 0 if all(rho[a][i][j] == -rho[a][j][i] for i in range(8) for j in range(8)) else 1
        for b in range(n):
            lhs = [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(_mmul(rho[a], rho[b]), _mmul(rho[b], rho[a]))]
            rhs = [[sum((fs.get((a, b, c), F(0)) * rho[c][i][j] for c in range(n)), F(0)) for j in range(8)]
                   for i in range(8)]
            hom += 0 if lhs == rhs else 1
    return hom, anti


def formal_vev():
    return [P_even(('v', i)) for i in range(8)]


def numeric_vev(v1, v2):
    vals = [v1, 0, 0, 0, v2, 0, 0, 0]
    return [P_const(x) for x in vals]


def make_s(y=F(1, 2), vev=None, sign=-1, hyper_side="right"):
    gens, fs = _algebra()
    rho = doublet_rep(y, hyper_side)
    return BRST(fs, len(gens), rho=rho, vev=formal_vev() if vev is None else vev, sign=sign), rho


def phi(s, i):
    return padd(s.vev[i], P_even(('h', i, Z4)))


def cov_phi(s, mu, i):
    """(D_mu phi)^i = d_mu h^i + g sum_a A^a_mu (rho_a (v + h))^i"""
    out = P_even(('h', i, unit(mu)))
    for a in range(s.n):
        for j in range(8):
            w = s.rho[a][i][j]
            if w:
                out = padd(out, psc(w, pmul(s.g, pmul(P_even(('A', a, mu, Z4)), phi(s, j)))))
    return out


def rho_c_on(s, vec):
    """-g sum_a c^a rho_a applied to a list of eight even polynomials"""
    out = []
    for i in range(8):
        r = {}
        for a in range(s.n):
            for j in range(8):
                w = s.rho[a][i][j]
                if w and vec[j]:
                    r = padd(r, psc(-w, pmul(s.g, pmul(P_odd(('c', a, Z4)), vec[j]))))
        out.append(r)
    return out


def nilpotency_failures(s, with_gauge=True):
    """(tests, failures) of s^2 = 0 on h^i with at most one derivative, and on the underived A^a_mu, c^a, cb^a"""
    tests = bad = 0
    for J in jets(1):
        for i in range(8):
            tests += 1
            bad += 1 if s(s.gen(('h', i, J))) else 0
    if with_gauge:
        for a in range(s.n):
            for mu in range(4):
                tests += 1
                bad += 1 if s(s.gen(('A', a, mu, Z4))) else 0
            for key in (('c', a, Z4), ('cb', a, Z4)):
                tests += 1
                bad += 1 if s(s.gen(key)) else 0
    return tests, bad


def kinetic(s):
    out = {}
    for mu in range(4):
        for i in range(8):
            d = cov_phi(s, mu, i)
            out = padd(out, psc(F(G4[mu], 2), pmul(d, d)))
    return out


def invariants(s, extra=None):
    """|phi_1|^2, |phi_2|^2, <phi_1, phi_2>, <phi_1, phi_2 e_12> (and an extra bilinear matrix if given)"""
    ph = [phi(s, i) for i in range(8)]
    R = _right(E12)
    mats = []
    for blk in ((0, 0), (4, 4), (0, 4)):
        mats.append([[F(int(i == j)) for j in range(4)] for i in range(4)] + [blk])
    mats.append(R + [(0, 4)])
    if extra is not None:
        mats.append(extra + [(0, 4)])
    out = []
    for M in mats:
        (o1, o2) = M[4]
        p = {}
        for i in range(4):
            for j in range(4):
                if M[i][j]:
                    p = padd(p, psc(M[i][j], pmul(ph[o1 + i], ph[o2 + j])))
        out.append(p)
    return out


def G_lin(s, a):
    """<rho_a v, h> = sum_i (rho_a v)_i h^i"""
    out = {}
    for i in range(8):
        for j in range(8):
            w = s.rho[a][i][j]
            if w and s.vev[j]:
                out = padd(out, psc(w, pmul(s.vev[j], P_even(('h', i, Z4)))))
    return out


def div_lower(vec):
    return padd(*[psc(G4[mu], D(mu, vec[mu])) for mu in range(4)])


def thooft_fermion(s, sign=-1):
    kap = kappa()
    xi = P_even(('xi',))
    out = {}
    for a in range(s.n):
        for b in range(s.n):
            if kap[a][b]:
                divA = div_lower([P_even(('A', b, mu, Z4)) for mu in range(4)])
                out = padd(out, psc(kap[a][b], pmul(P_odd(('cb', a, Z4)),
                                                    padd(divA, pmul(psc(F(1, 2), xi), P_even(('B', b, Z4)))))))
        out = padd(out, psc(sign, pmul(xi, pmul(s.g, pmul(P_odd(('cb', a, Z4)), G_lin(s, a))))))
    return out


def thooft_expected(s):
    """s Psi = s Psi_0 - xi g sum_a (B^a <rho_a v, h> - cb^a <rho_a v, s h>)"""
    kap = kappa()
    xi = P_even(('xi',))
    out = {}
    for a in range(s.n):
        for b in range(s.n):
            if not kap[a][b]:
                continue
            divA = div_lower([P_even(('A', b, mu, Z4)) for mu in range(4)])
            Dc = [s.gen(('A', b, mu, Z4)) for mu in range(4)]
            e = padd(pmul(P_even(('B', a, Z4)), divA),
                     pmul(psc(F(1, 2), xi), pmul(P_even(('B', a, Z4)), P_even(('B', b, Z4)))),
                     psc(-1, pmul(P_odd(('cb', a, Z4)), div_lower(Dc))))
            out = padd(out, psc(kap[a][b], e))
        sh = {}
        for i in range(8):
            for j in range(8):
                w = s.rho[a][i][j]
                if w and s.vev[j]:
                    sh = padd(sh, psc(w, pmul(s.vev[j], s.gen(('h', i, Z4)))))
        out = padd(out, psc(-1, pmul(xi, pmul(s.g, pmul(P_even(('B', a, Z4)), G_lin(s, a))))),
                   pmul(xi, pmul(s.g, pmul(P_odd(('cb', a, Z4)), sh))))
    return out


def _kinv():
    kap = kappa()
    k = len(kap)
    A = [list(row) + [F(int(i == j)) for j in range(k)] for i, row in enumerate(kap)]
    for c in range(k):
        p = next(r for r in range(c, k) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(k):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * yy for x, yy in zip(A[r], A[c])]
    return [row[k:] for row in A]


def gauge_fixing_lagrangian(s, xi, sign=-1):
    """-(1/(2 xi)) kappa_ab F^a F^b with F^a = nabla.A^a + sign xi g kappa^{ab} <rho_b v, h>, xi a rational"""
    kap, ki = kappa(), _kinv()
    Fs = []
    for a in range(s.n):
        f = div_lower([P_even(('A', a, mu, Z4)) for mu in range(4)])
        for b in range(s.n):
            if ki[a][b]:
                f = padd(f, psc(sign * xi * ki[a][b], pmul(s.g, G_lin(s, b))))
        Fs.append(f)
    out = {}
    for a in range(s.n):
        for b in range(s.n):
            if kap[a][b]:
                out = padd(out, psc(-kap[a][b] / (2 * xi), pmul(Fs[a], Fs[b])))
    return out


def _count(p, kind):
    return lambda e: sum(1 for x in e if x[0] == kind)


def bilinear_part(p, k1, k2):
    """monomials with exactly one field of kind k1 and one of kind k2 and no other jet field, no odd part"""
    out = {}
    for (e, o), c in p.items():
        if o:
            continue
        jets_ = [x for x in e if _is_jet(x)]
        kinds = sorted(x[0] for x in jets_)
        if kinds == sorted([k1, k2]):
            out[(e, o)] = c
    return out


def mixing_total_derivative(s):
    """g sum_mu G4[mu] d_mu (sum_a A^a_mu <rho_a v, h>)"""
    out = {}
    for mu in range(4):
        inner = {}
        for a in range(s.n):
            inner = padd(inner, pmul(P_even(('A', a, mu, Z4)), G_lin(s, a)))
        out = padd(out, psc(G4[mu], D(mu, pmul(s.g, inner))))
    return out


def pdiff(p, key):
    out = {}
    for (e, o), c in p.items():
        k = e.count(key)
        if not k:
            continue
        lst = list(e)
        lst.remove(key)
        m = (tuple(lst), o)
        out[m] = out.get(m, F(0)) + k * c
    return {m: c for m, c in out.items() if c}


def euler_A(p, a, mu):
    """Euler-Lagrange derivative of a first-order density with respect to A^a_mu"""
    out = pdiff(p, ('A', a, mu, Z4))
    for nu in range(4):
        out = padd(out, psc(-1, D(nu, pdiff(p, ('A', a, mu, unit(nu))))))
    return out


def mass_matrices(s, xi):
    """from the quadratic Lagrangian at numeric vacuum: vector (g^2 A^a.A^b coefficients, symmetrised), Goldstone
    (g^2 h^i h^j), ghost (g^2 cb^a c^b in s Psi); returned as matrices with the sign conventions removed"""
    n = s.n
    K = kinetic(s)
    Lg = gauge_fixing_lagrangian(s, xi)
    sP = s(thooft_fermion(s))
    gg = ('g',)
    Vm = [[F(0)] * n for _ in range(n)]
    Gm = [[F(0)] * 8 for _ in range(8)]
    Hm = [[F(0)] * n for _ in range(n)]
    for (e, o), c in K.items():
        if o or e.count(gg) != 2:
            continue
        rest = [x for x in e if x != gg]
        if len(rest) == 2 and all(x[0] == 'A' for x in rest) and rest[0][2] == rest[1][2] == 0:
            a, b = rest[0][1], rest[1][1]
            if a == b:
                Vm[a][a] += 2 * c
            else:
                Vm[a][b] += c
                Vm[b][a] += c
    for (e, o), c in Lg.items():
        if o or e.count(gg) != 2:
            continue
        rest = [x for x in e if x != gg]
        if len(rest) == 2 and all(x[0] == 'h' and x[2] == Z4 for x in rest):
            i, j = rest[0][1], rest[1][1]
            if i == j:
                Gm[i][i] += -2 * c / xi
            else:
                Gm[i][j] += -c / xi
                Gm[j][i] += -c / xi
    for (e, o), c in sP.items():
        if e.count(gg) != 2 or len(o) != 2:
            continue
        rest = [x for x in e if x != gg and x[0] != 'xi']
        if rest:
            continue
        k1, k2 = _ODDK[o[0]], _ODDK[o[1]]
        if k1[0] == 'c' and k2[0] == 'cb' and k1[-1] == Z4 and k2[-1] == Z4:
            Hm[k2[1]][k1[1]] += c
        elif k1[0] == 'cb' and k2[0] == 'c' and k1[-1] == Z4 and k2[-1] == Z4:
            Hm[k1[1]][k2[1]] += -c
    return Vm, Gm, Hm


def gram_and_W(s):
    """W: R^12 -> R^8, W e_a = rho_a v (numeric v); Gamma = W^T W"""
    vv = [s.vev[j].get(((), ()), F(0)) for j in range(8)]
    W = [[sum((s.rho[a][i][j] * vv[j] for j in range(8)), F(0)) for a in range(s.n)] for i in range(8)]
    Gam = [[sum((W[i][a] * W[i][b] for i in range(8)), F(0)) for b in range(s.n)] for a in range(s.n)]
    return W, Gam


def charpoly(M):
    """Faddeev-LeVerrier: coefficients of det(t - M), highest first"""
    n = len(M)
    I = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    coeffs = [F(1)]
    Mk = [row[:] for row in I]
    for k in range(1, n + 1):
        AM = _mmul(M, Mk)
        ck = -sum((AM[i][i] for i in range(n)), F(0)) / k
        coeffs.append(ck)
        Mk = [[AM[i][j] + (ck if i == j else 0) for j in range(n)] for i in range(n)]
    return coeffs


def rank(M):
    return GA.field_rank([row[:] for row in M])


# ---------------------------------------------------------------- sample data and runners
Y_STORED = F(1, 2)        # hypercharge of the doublets in the normalisation Y = (3n - 2k)/6
Y_OTHER = F(1, 3)         # a second normalisation: nothing below depends on it
XI_SAMPLES = (F(1), F(3))
VACUUM = (F(1), F(2))     # the neutral aligned vacuum (v_1, 0, 0, 0), (v_2, 0, 0, 0) of the two doublets
E01 = GA.mul(GA.gen(0), GA.gen(1), E3)


def run_rep():
    gens, _ = _algebra()
    good = rep_defects(doublet_rep(Y_STORED))
    other = rep_defects(doublet_rep(Y_OTHER))
    left = rep_defects(doublet_rep(Y_STORED, hyper_side="left"))
    return len(gens), good, other, left


def run_nilpotency():
    s, _ = make_s(Y_STORED)
    s2, _ = make_s(Y_OTHER)
    s3, _ = make_s(Y_STORED, sign=1)
    return nilpotency_failures(s), nilpotency_failures(s2, with_gauge=False), nilpotency_failures(s3, with_gauge=False)


def run_covariance():
    s, _ = make_s(Y_STORED)
    tests = bad = 0
    for mu in range(4):
        Dp = [cov_phi(s, mu, i) for i in range(8)]
        rc = rho_c_on(s, Dp)
        for i in range(8):
            tests += 1
            bad += 1 if padd(s(Dp[i]), psc(-1, rc[i])) else 0
    K = kinetic(s)
    inv = invariants(s)
    bad_right = s(invariants(s, extra=_right(E01))[-1])
    bad_left = s(invariants(s, extra=_left(E12))[-1])
    return tests, bad, bool(K) and not s(K), [bool(s(p)) for p in inv], bool(bad_right), bool(bad_left)


def run_thooft():
    s, _ = make_s(Y_STORED)
    sP = s(thooft_fermion(s))
    exact = bool(sP) and not padd(sP, psc(-1, thooft_expected(s))) and not s(sP)
    K = kinetic(s)
    TD = mixing_total_derivative(s)
    sizes, cancels = [], []
    for xi in XI_SAMPLES:
        mix = bilinear_part(padd(K, gauge_fixing_lagrangian(s, xi)), 'A', 'h')
        sizes.append(len(mix))
        cancels.append(not padd(mix, psc(-1, TD)))
    td_null = not any(euler_A(TD, a, mu) for a in range(s.n) for mu in range(4))
    wrong = padd(bilinear_part(padd(K, gauge_fixing_lagrangian(s, XI_SAMPLES[0], sign=1)), 'A', 'h'), psc(-1, TD))
    wrong_live = any(euler_A(wrong, a, mu) for a in range(s.n) for mu in range(4))
    return exact, sizes, cancels, td_null, wrong_live


def run_masses():
    sn, _ = make_s(Y_STORED, vev=numeric_vev(*VACUUM))
    Vm, Gm, Hm = mass_matrices(sn, XI_SAMPLES[0])
    W, Gam = gram_and_W(sn)
    WKW = _mmul(_mmul(W, _kinv()), [list(r) for r in zip(*W)])
    pv = charpoly(_mmul(_kinv(), Gam))
    pg = charpoly(WKW)
    return Vm == Gam, Hm == Gam, Gm == WKW, rank(Gam), len(Gam) - rank(Gam), pv, pg


# ---------------------------------------------------------------- checks
def check_doublets_as_ga_quaternions_carry_the_gauge_algebra():
    """rho is a real orthogonal representation of the stored su(2) + su(3) + u(1) on two doublets for each
    hypercharge normalisation; hypercharge on the left fails to commute with su(2)."""
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent")
    n, good, other, left = run_rep()
    ok = n == 12 and good == (0, 0) and other == (0, 0) and left == (4, 0)
    GA.check("two doublets as even elements of Cl(3,0): su(2) on the left, hypercharge on the right, a real orthogonal"
             " representation of the stored gauge algebra", ok)
    return ok


def check_scalar_brst_is_nilpotent_for_every_vacuum():
    """s^2 = 0 on the 40 generators h^i with at most one derivative, as polynomials in g and eight formal vacuum
    components, and on the 72 underived gauge, ghost and antighost generators; s h = +g rho(c) phi fails on all 40."""
    premise("synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent")
    premise("synthesis.imported-brst-kugo-ojima-strocchi-and-gribov")
    full, other, wrong = run_nilpotency()
    ok = full == (112, 0) and other == (40, 0) and wrong == (40, 40)
    GA.check("s^2 = 0 on all scalar generators for every vacuum and both normalisations; the opposite sign fails", ok)
    return ok


def check_covariant_derivative_kinetic_term_and_invariants():
    """s D_mu phi = -g rho(c) D_mu phi (32 components), s(1/2 <D phi, D phi>) = 0, and s annihilates the four
    quadratic invariants |phi_1|^2, |phi_2|^2, <phi_1, phi_2>, <phi_1, phi_2 e_12>; <phi_1, phi_2 e_01> and
    <phi_1, e_12 phi_2> are not invariant."""
    premise("synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent")
    tests, bad, kin_ok, inv, br, bl = run_covariance()
    ok = (tests, bad) == (32, 0) and kin_ok and inv == [False, False, False, False] and br and bl
    GA.check("covariant derivative of the doublets transforms covariantly; kinetic term and four invariants s-closed", ok)
    return ok


def check_thooft_fermion_is_exact_and_cancels_the_mixing():
    """s Psi has the stated expansion and s(s Psi) = 0; for xi = 1, 3 the vector-Goldstone bilinear of
    1/2 <D phi, D phi> - (1/(2 xi)) kappa F F is exactly g d_mu(A^a_mu <rho_a v, h>) (256 monomials, formal v), a
    total derivative; with the opposite sign of the 't Hooft term the remainder has nonzero Euler derivative."""
    premise("synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent")
    premise("synthesis.imported-brst-kugo-ojima-strocchi-and-gribov")
    exact, sizes, cancels, td_null, wrong_live = run_thooft()
    ok = exact and sizes == [256, 256] and cancels == [True, True] and td_null and wrong_live
    GA.check("'t Hooft gauge fixing is s-exact and cancels the vector-Goldstone mixing up to a total derivative", ok)
    return ok


def check_thooft_feynman_masses_for_the_neutral_aligned_vacuum():
    """vacuum (1, 0, 0, 0), (2, 0, 0, 0): vector mass matrix g^2 Gamma, ghost mass matrix xi g^2 Gamma and Goldstone
    mass matrix xi g^2 W kappa^{-1} W^T read off the Lagrangian; Goldstone map of rank 3 (9 massless vectors);
    det(t - kappa^{-1} Gamma) = t^9 (t - 5)^2 (t - 20/3) and det(t - W kappa^{-1} W^T) = t^5 (t - 5)^2 (t - 20/3)."""
    premise("synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    v_ok, h_ok, g_ok, r, massless, pv, pg = run_masses()
    cubic = [F(1), F(-50, 3), F(275, 3), F(-500, 3)]
    ok = v_ok and h_ok and g_ok and r == 3 and massless == 9
    ok = ok and pv == cubic + [F(0)] * 9 and pg == cubic + [F(0)] * 5
    GA.check("'t Hooft-Feynman gauge with two doublets: vector, ghost and Goldstone masses coincide; rank 3", ok)
    return ok


if __name__ == "__main__":
    import time
    for fn in (check_doublets_as_ga_quaternions_carry_the_gauge_algebra,
               check_scalar_brst_is_nilpotent_for_every_vacuum,
               check_covariant_derivative_kinetic_term_and_invariants,
               check_thooft_fermion_is_exact_and_cancels_the_mixing,
               check_thooft_feynman_masses_for_the_neutral_aligned_vacuum):
        t = time.time()
        print(fn.__name__, fn(), round(time.time() - t, 1))
