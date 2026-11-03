"""The field-level BRST differential of the gauge fields of the minimal massive composite: exact checks.

Fields at a point and all their derivatives (the jet algebra): A^a_mu, B^a even, ghosts c^a and antighosts cb^a odd,
the odd ones generators of a Grassmann algebra (the degenerate Clifford algebra, every generator of square 0, in
GA's blade engine); the coupling g and the gauge parameter xi formal even constants. The gauge algebra
su(2) + su(3) + u(1) of the minimal massive composite is realised, up to isomorphism, by bivectors of Cl(9,0): T_1..T_3 = (1/2) e_ij in Cl(3,0) on e_0, e_1, e_2; the eight
traceless bivectors of so(6) on e_3..e_8 commuting with J = e_34 + e_56 + e_78; T_12 = J/2; [T_a, T_b] = f_ab^c T_c.
s A^a_mu = d_mu c^a + g f_bc^a A^b_mu c^c, s c^a = -(g/2) f_bc^a c^b c^c, s cb^a = B^a, s B^a = 0, s(x_J) = d_J(s x),
s an odd derivation acting from the left. A^a = A^a_mu g^mu is a GA vector field (signature +,-,-,-),
nabla = g^mu d_mu, F^a = nabla^A^a + (g/2) f_bc^a A^b^A^c a bivector field.
(1) The bivectors close into su(2) + su(3) + u(1): 12 independent generators, 58 nonzero f; the Cl(3,0) block and
    the 8-block are ideals, J spans the centre, the derived algebra has dimension 11, kappa_ab = -<T_a T_b>_0 is positive
    definite and ad-invariant, the 8-block's adjoint commutant is one-dimensional (simple, so su(3)).
(2) s^2 = 0 on every generator with at most one derivative (300 generators), as a polynomial identity in g.
(3) Without the term g[A, c] in s A, with s c = -g f c c (no 1/2), or with one antisymmetric pair of structure
    constants perturbed (Jacobi broken), s^2 != 0.
(4) s F^a = g f_bc^a F^b c^c for all twelve a; a non-invariant kappa fails ad-invariance.
(5) On the su(2) + u(1) block: s <kappa F F>_0 = 0 and s <kappa F F>_4 = 0; a non-invariant kappa gives s <F F>_0 != 0.
(6) Psi = kappa_ab cb^a (nabla.A^b + (xi/2) B^b): s Psi = kappa_ab (B^a nabla.A^b + (xi/2) B^a B^b - cb^a nabla.(D c)^b)
    with (D c)^b = nabla c^b + g f_cd^b A^c c^d, and s(s Psi) = 0, for the full algebra.
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
    return key[0] in ('A', 'B', 'c', 'cb')


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

    def __init__(self, fs, n, half=F(1, 2), cov=True):
        self.fs, self.n, self.half, self.cov = fs, n, half, cov
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




# ---------------------------------------------------------------- cached data
_CACHE = {}


def _algebra():
    if 'g' not in _CACHE:
        gens = gauge_bivectors()
        _CACHE['g'] = gens
        _CACHE['f'] = structure_constants(gens)
    return _CACHE['g'], _CACHE['f']


def _ip(x, y):
    return GA.mul(x, y, E9).get((), F(0))


def _kappa(gens):
    return [[-_ip(x, y) for y in gens] for x in gens]


def _ad_invariant(fs, kap, n):
    # kappa([T_a, T_b], T_c) + kappa(T_b, [T_a, T_c]) = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                v = sum((fs.get((a, b, d), F(0)) * kap[d][c] + fs.get((a, c, d), F(0)) * kap[b][d]
                         for d in range(n)), F(0))
                if v != 0:
                    return False
    return True


def _closed(fs, idx):
    return all(c in idx for (a, b, c) in fs if a in idx and b in idx)


def check_gauge_algebra_as_bivectors():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    gens, fs = _algebra()
    n = len(gens)
    ok = n == 12 and len(fs) == 58
    keys = sorted({b for z in gens for b in z})
    ok = ok and GA.field_rank([[z.get(k, F(0)) for k in keys] for z in gens]) == 12
    ok = ok and all(len(b) == 2 for z in gens for b in z)
    s2, s3 = set(range(0, 3)), set(range(3, 11))
    ok = ok and _closed(fs, s2) and _closed(fs, s3)
    ok = ok and not any((a, b, c) for (a, b, c) in fs if (a in s2 and b in s3) or (a in s3 and b in s2))
    # centre: kernel of x -> [x, T_b] for all b
    rows = [[fs.get((a, b, c), F(0)) for a in range(n)] for b in range(n) for c in range(n)]
    ok = ok and len(GA.field_kernel(rows)) == 1 and not any(k[0] == 11 or k[1] == 11 for k in fs)
    # derived algebra [g, g] has dimension 11
    ok = ok and GA.field_rank([[fs.get((a, b, c), F(0)) for c in range(n)]
                               for a in range(n) for b in range(n)]) == 11
    kap = _kappa(gens)
    ok = ok and GA.congruence_signature(kap) == (12, 0, 0) and _ad_invariant(fs, kap, n)
    # Schur: the commutant of ad(su(3)) in gl(8) is one-dimensional, so the 8-block is simple
    idx = sorted(s3)
    ad = [[[fs.get((a, b, c), F(0)) for b in idx] for c in idx] for a in idx]
    eqs = []
    for A in ad:
        for i in range(8):
            for j in range(8):
                row = [F(0)] * 64
                for k in range(8):
                    row[i * 8 + k] += A[k][j]
                    row[k * 8 + j] -= A[i][k]
                eqs.append(row)
    ok = ok and len(GA.field_kernel(eqs)) == 1
    GA.check("bivectors of Cl(9,0) realise su(2) + su(3) + u(1): 12 generators, 58 structure constants, centre J,"
             " derived algebra of dimension 11, invariant positive kappa, simple 8-block", ok)
    return ok


def check_brst_differential_is_nilpotent():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.imported-brst-kugo-ojima-strocchi-and-gribov")
    gens, fs = _algebra()
    n = len(gens)
    s = BRST(fs, n)
    count = 0
    ok = True
    for J in jets(1):
        for a in range(n):
            for mu in range(4):
                ok = ok and not s(s.gen(('A', a, mu, J)))
                count += 1
            ok = ok and not s(s.gen(('c', a, J)))
            ok = ok and not s(s.gen(('cb', a, J))) and s.gen(('cb', a, J)) == P_even(('B', a, J))
            count += 1
    # the differential is not trivial: s A carries the ghost's covariant derivative
    ok = ok and len(s.gen(('A', 3, 2, Z4))) == 1 + len([k for k in fs if k[2] == 3])
    ok = ok and count == 300
    GA.check("s^2 = 0 on all 300 generators A^a_mu, c^a with at most one derivative, for every g", ok)
    return ok


def _cov_der(fs, mu, a, Y):
    """(D_mu Y)^a = d_mu Y^a + g f_bc^a A^b_mu Y^c for a Lie-algebra-valued polynomial Y."""
    out = D(mu, Y[a])
    g = P_even(('g',))
    for (b, c, aa), v in fs.items():
        if aa == a:
            out = padd(out, psc(v, pmul(g, pmul(P_even(('A', b, mu, Z4)), Y[c]))))
    return out


def _bad_count(s, n):
    k = 0
    for a in range(n):
        for mu in range(4):
            k += 1 if s(s.gen(('A', a, mu, Z4))) else 0
        k += 1 if s(s.gen(('c', a, Z4))) else 0
    return k


def check_nilpotency_needs_jacobi_the_half_and_the_covariant_term():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    gens, fs = _algebra()
    n = len(gens)
    good = BRST(fs, n)
    Y = [good.gen(('c', a, Z4)) for a in range(n)]
    ok = _bad_count(good, n) == 0
    # s c = -2 g f c c / 2 (factor 2 instead of 1/2): s^2 A = 3 D Y, Y = s c with the factor 1/2; s^2 c = 0
    s2 = BRST(fs, n, half=F(2))
    for a in range(n):
        ok = ok and not s2(s2.gen(('c', a, Z4)))
        for mu in range(4):
            ok = ok and s2(s2.gen(('A', a, mu, Z4))) == psc(3, _cov_der(fs, mu, a, Y))
    # without the covariant term: s^2 A^a_mu = d_mu (s c^a), nonzero on the 11 non-abelian generators
    s0 = BRST(fs, n, cov=False)
    for a in range(n):
        for mu in range(4):
            ok = ok and s0(s0.gen(('A', a, mu, Z4))) == D(mu, Y[a])
    ok = ok and _bad_count(s0, n) == 44
    # Jacobi broken: one antisymmetric pair of su(3) structure constants shifted
    key = sorted(k for k in fs if 3 <= k[0] < 11 and 3 <= k[1] < 11)[0]
    bad = dict(fs)
    a, b, c = key
    bad[(a, b, c)] = bad[(a, b, c)] + 1
    bad[(b, a, c)] = bad.get((b, a, c), F(0)) - 1
    ok = ok and key == (3, 4, 5) and _bad_count(BRST(bad, n), n) == 30
    GA.check("s^2 = 3 D(s c) with the factor 2 for 1/2, s^2 A = d(s c) without g[A, c] (44 generators), Jacobi broken"
             " gives 30 failing generators; s^2 = 0 as stated", ok)
    return ok


def check_field_strength_is_covariant():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    gens, fs = _algebra()
    n = len(gens)
    s = BRST(fs, n)
    g = P_even(('g',))
    Fs = [field_strength(fs, n, a) for a in range(n)]
    ok = all(set(len(b) for b in X) == {2} for X in Fs)
    ok = ok and sum(len(X) for X in Fs) == 72 and sum(len(q) for X in Fs for q in X.values()) == 492
    for a in range(n):
        rhs = {}
        for (b, c, aa), v in fs.items():
            if aa == a:
                rhs = mv_add(rhs, mv_sc(v, mv_mul(Fs[b], {(): pmul(g, P_odd(('c', c, Z4)))})))
        ok = ok and not mv_add(mv_s(s, Fs[a]), mv_sc(-1, rhs))
    kap = _kappa(gens)
    bad = [r[:] for r in kap]
    bad[0][0] = bad[0][0] + 1
    ok = ok and _ad_invariant(fs, kap, n) and not _ad_invariant(fs, bad, n)
    ok = ok and kap[0][0] == F(1, 4) and kap[3][3] == F(2, 3) and kap[11][11] == F(3, 4)
    GA.check("s F^a = g f_bc^a F^b c^c for the bivector field strength; kappa ad-invariant, a perturbed one not", ok)
    return ok


def check_yang_mills_density_is_invariant_on_the_weak_block():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    gens, fs = _algebra()
    sub = [0, 1, 2, 11]
    m = len(sub)
    fsub = {(sub.index(a), sub.index(b), sub.index(c)): v for (a, b, c), v in fs.items()
            if a in sub and b in sub and c in sub}
    s = BRST(fsub, m)
    Fs = [field_strength(fsub, m, a) for a in range(m)]
    kap = [[-_ip(gens[i], gens[j]) for j in sub] for i in sub]

    def dens(kp, r, blade):
        out = {}
        for i in range(m):
            for j in range(m):
                if kp[i][j]:
                    out = padd(out, psc(kp[i][j], grade(mv_mul(Fs[i], Fs[j]), r).get(blade, {})))
        return out
    L0 = dens(kap, 0, ())
    L4 = dens(kap, 4, (0, 1, 2, 3))
    ok = len(fsub) == 6 and bool(L0) and bool(L4) and not s(L0) and not s(L4)
    bad = [r[:] for r in kap]
    bad[0][0] = bad[0][0] + 1
    ok = ok and bool(s(dens(bad, 0, ())))
    GA.check("on su(2) + u(1): s <kappa F F>_0 = 0 and s <kappa F F>_4 = 0; a non-invariant kappa breaks it", ok)
    return ok


def check_gauge_fixing_term_is_exact_with_the_faddeev_popov_operator():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.imported-brst-kugo-ojima-strocchi-and-gribov")
    gens, fs = _algebra()
    n = len(gens)
    s = BRST(fs, n)
    kap = _kappa(gens)
    g = P_even(('g',))
    xi = P_even(('xi',))

    def div(vec):
        # nabla . V for V = sum_mu V_mu g^mu given lower components V_mu
        return padd(*[psc(G4[mu], D(mu, vec[mu])) for mu in range(4)])
    Psi, expect = {}, {}
    for a in range(n):
        for b in range(n):
            if kap[a][b] == 0:
                continue
            divA = div([P_even(('A', b, mu, Z4)) for mu in range(4)])
            Psi = padd(Psi, psc(kap[a][b], pmul(P_odd(('cb', a, Z4)),
                                                padd(divA, pmul(psc(F(1, 2), xi), P_even(('B', b, Z4)))))))
            Dc = []
            for mu in range(4):
                t = D(mu, P_odd(('c', b, Z4)))
                for (c, d, bb), v in fs.items():
                    if bb == b:
                        t = padd(t, psc(v, pmul(g, pmul(P_even(('A', c, mu, Z4)), P_odd(('c', d, Z4))))))
                Dc.append(t)
            e = padd(pmul(P_even(('B', a, Z4)), divA),
                     pmul(psc(F(1, 2), xi), pmul(P_even(('B', a, Z4)), P_even(('B', b, Z4)))),
                     psc(-1, pmul(P_odd(('cb', a, Z4)), div(Dc))))
            expect = padd(expect, psc(kap[a][b], e))
    sPsi = s(Psi)
    ok = bool(sPsi) and not padd(sPsi, psc(-1, expect)) and not s(sPsi)
    ok = ok and len([k for k in sPsi if len(k[1]) == 2]) > 0 and n == 12
    GA.check("s Psi = kappa(B, nabla.A) + (xi/2) kappa(B, B) - kappa(cb, nabla.(D c)) and s(s Psi) = 0", ok)
    return ok


if __name__ == "__main__":
    check_gauge_algebra_as_bivectors()
    check_brst_differential_is_nilpotent()
    check_nilpotency_needs_jacobi_the_half_and_the_covariant_term()
    check_field_strength_is_covariant()
    check_yang_mills_density_is_invariant_on_the_weak_block()
    check_gauge_fixing_term_is_exact_with_the_faddeev_popov_operator()
