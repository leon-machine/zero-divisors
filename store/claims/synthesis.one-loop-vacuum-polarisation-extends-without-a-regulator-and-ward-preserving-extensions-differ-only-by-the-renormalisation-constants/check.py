"""Exact checks: the one-loop vacuum polarisation extended without a regulator, and the difference spaces of
Ward-preserving covariant one-loop extensions, in the spacetime algebra (standard method: Epstein and Glaser;
Freedman, Johnson and Latorre). Numbering below is the check's own; the formal clauses are (i) traces, (ii)
vacuum polarisation, (iii) difference spaces, (vi) scalar bubble, (vii) floors (closure beyond the stored commutant).

Units hbar = c = 1; Euclidean section; s = Q(x) the square of the vector x; L = ln(mu^2 s). Off the origin a radial
expression is a dict {(a, k): Fraction} for sum c s^a L^k; a symmetric tensor is (A, B) for A g + B x x; a vector
field C x is the dict C. Powers of pi are carried as an explicit integer exponent next to a Fraction. Rules used
(signature-free, from d_mu s = 2 x_mu and d_mu x^mu = 4): d_mu d_nu f = 2 f' g + 4 f'' x x, box f = 8 f' + 4 s f'',
dslash f = 2 f' x, div(A g + B x x) = (2 A' + 2 s B' + 5 B) x, mu d/dmu (s^a L^k) = 2 k s^a L^(k-1).
(1) Spin traces in Cl(4,0) and Cl(1,3): <e_mu x e_nu x>_0 = 2 x_mu x_nu - g_mu_nu Q(x), <e_mu x e_nu>_0 = 0,
    e^mu x e_mu = -2 x, e^mu e_mu = 4 (complete by polarisation); the real trace of left multiplication on the algebra
    is 16 <X>_0 (complete over blades); the massless propagator x / (2 pi^2 s^2) is homogeneous of degree -3.
(2) The vacuum polarisation: with S(x) = alpha x + beta, alpha = 1/(2 pi^2 s^2) - m^2/(8 pi^2 s), beta = m/(4 pi^2 s)
    (the m^2 coefficient from the Klein-Gordon recursion), -e^2 tr(g_mu S(x) g_nu S(-x)) has scaling-degree-6 part
    (e^2/pi^4)(2xx - g s)/s^4 = (e^2/(12 pi^4))(dd - g box) s^-2 and scaling-degree-4 part
    -(e^2 m^2/(8 pi^4))(dd - g box)(1/s); both divergence-free; s^-2 = -(1/4) box(L/s) off the origin; with
    box(1/s) = -4 pi^2 delta (flux of grad(1/s) through the 3-sphere of area 2 pi^2 r^3) the extension's mu-derivative
    is (e^2/(6 pi^2))(dd - g box) delta, giving the log coefficient e^2/(12 pi^2) per Dirac fermion.
(3) Covariant local differences between extensions (existence of Ward-preserving ones is not checked) in Cl(1,3) (polynomials in the components of the momenta and polarisations, Lorentz
    covariance under the six bivector generators, exact sparse rank): photon two-point (omega 2) 3, transverse 1;
    self-energy (omega 1) 4, with the reflection 2; vertex (omega 0) 2, with the reflection 1; self-energy and vertex
    under the Ward-Takahashi identity 2 (with the reflection), 4 (without), and c_V = -c_2 forced; three-current
    (omega 1) 8, transverse on any two legs 0; four-photon (omega 0) 4, transverse on one leg 0.
(4) The scalar bubble Delta_0^2 = 1/(16 pi^4 s^2): extension mu-derivative delta/(8 pi^2); three channels with
    symmetry factor 1/2 give the quartic coefficient 3/(16 pi^2).
(5) Cl(2,4): the commutant k of the conformal Hamiltonian gamma_0 e_+ among the 15 bivectors is 7-dimensional and
    k together with any one boost, translation, special conformal generator or the dilation generates all 15.
(6) Scaling degrees (homogeneity) of the one-loop kernels: 6, 4 (vacuum polarisation), 5 (self-energy numerator
    structure x/s^3), 4 (scalar bubble); omega = sd - 4.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


# ---------------------------------------------------------------- radial algebra off the origin
def radd(*fs):
    out = {}
    for f in fs:
        for k, v in f.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def rscl(c, f):
    return {k: c * v for k, v in f.items() if c * v != 0}


def rmul(f, g):
    out = {}
    for (a, k), v in f.items():
        for (b, l), w in g.items():
            out[(a + b, k + l)] = out.get((a + b, k + l), F(0)) + v * w
    return {k: v for k, v in out.items() if v != 0}


def dds(f):
    out = {}
    for (a, k), v in f.items():
        if a != 0:
            out[(a - 1, k)] = out.get((a - 1, k), F(0)) + a * v
        if k != 0:
            out[(a - 1, k - 1)] = out.get((a - 1, k - 1), F(0)) + k * v
    return {k: v for k, v in out.items() if v != 0}


S1 = {(1, 0): F(1)}


def box(f):
    return radd(rscl(F(8), dds(f)), rscl(F(4), rmul(S1, dds(dds(f)))))


def trans_t(f):
    """(d_mu d_nu - g box) f as (A, B)."""
    return (radd(rscl(F(2), dds(f)), rscl(F(-1), box(f))), rscl(F(4), dds(dds(f))))


def div_t(t):
    a, b = t
    return radd(rscl(F(2), dds(a)), rscl(F(2), rmul(S1, dds(b))), rscl(F(5), b))


def dslash(f):
    return rscl(F(2), dds(f))


def mu_dmu(f):
    out = {}
    for (a, k), v in f.items():
        if k:
            out[(a, k - 1)] = out.get((a, k - 1), F(0)) + 2 * k * v
    return {k: v for k, v in out.items() if v != 0}


def teq(t, u):
    return t[0] == u[0] and t[1] == u[1]


def tscl(c, t):
    return (rscl(c, t[0]), rscl(c, t[1]))


def sd_of(f, xdeg=0):
    """Scaling degree of sum c s^a L^k (x-degree xdeg): -2a - xdeg for the most singular term (logs do not count)."""
    return max(-2 * a - xdeg for (a, k) in f)


def delta_coefficient_of_box_inv_s():
    """box(1/s) = c pi^2 delta: c = (d/dr r^-2) r^3 times the 3-sphere area 2 pi^2 r^3 / r^3, read at any r."""
    radial_derivative = {(-3,): F(-2)}            # d/dr r^-2 = -2 r^-3
    area = {(3,): F(2)}                            # |S^3| r^3 = 2 pi^2 r^3 (pi^2 carried)
    prod = {}
    for (p,), v in radial_derivative.items():
        for (q,), w in area.items():
            prod[(p + q,)] = prod.get((p + q,), F(0)) + v * w
    assert list(prod) == [(0,)]                    # independent of r
    return prod[(0,)]


# ---------------------------------------------------------------- spin traces
def _vec(c):
    return {(i,): F(v) for i, v in enumerate(c) if v != 0}


def _trace_identities(sig):
    m = lambda x, y: GA.mul(x, y, sig)
    g = [GA.gen(i) for i in range(4)]
    up = [GA.scal(F(sig[i]), g[i]) for i in range(4)]       # reciprocal frame
    xs = []
    for i in range(4):
        xs.append([1 if k == i else 0 for k in range(4)])
        for j in range(i + 1, 4):
            xs.append([1 if k in (i, j) else 0 for k in range(4)])
    xs.append([3, -2, 5, 7])
    ok = True
    for c in xs:
        x = _vec(c)
        q = sum(F(sig[i]) * c[i] * c[i] for i in range(4))
        xlow = [F(sig[i]) * c[i] for i in range(4)]
        for mu in range(4):
            for nu in range(4):
                lhs = m(m(m(g[mu], x), g[nu]), x).get((), F(0))
                rhs = 2 * xlow[mu] * xlow[nu] - (F(sig[mu]) if mu == nu else F(0)) * q
                ok = ok and lhs == rhs
                ok = ok and m(m(g[mu], x), g[nu]).get((), F(0)) == 0
        sw = GA.add(*[m(m(up[k], x), g[k]) for k in range(4)])
        ok = ok and GA.eq(sw, GA.scal(F(-2), x))
    ok = ok and GA.eq(GA.add(*[m(up[k], g[k]) for k in range(4)]), {(): F(4)})
    return ok


def check_spin_traces_and_homogeneity_in_the_spacetime_algebra():
    premise("field-theory.second-quantisation")
    premise("field-theory.coupled-system-tree-level")
    ok = _trace_identities((1, 1, 1, 1)) and _trace_identities((1, -1, -1, -1))
    sig = (1, -1, -1, -1)
    blades = GA.all_blades(4)
    for bl in blades:
        tr = F(0)
        for b2 in blades:
            tr += GA.mul({bl: F(1)}, {b2: F(1)}, sig).get(b2, F(0))
        ok = ok and tr == (F(16) if bl == () else F(0))
    # homogeneity of the massless propagator x / (2 pi^2 Q(x)^2): S(l x) = l^-3 S(x)
    for c in ([1, 2, 0, 3], [2, -1, 1, 1]):
        x = _vec(c)
        q = sum(F(s) * v * v for s, v in zip(sig, c))
        for lam in (F(2), F(1, 3), F(-5, 2)):
            xl = GA.scal(lam, x)
            s_l = GA.scal(F(1, 2) / (lam * lam * q) ** 2, xl)
            s_1 = GA.scal(F(1, 2) / q ** 2, x)
            ok = ok and GA.eq(s_l, GA.scal(lam ** -3, s_1))
    GA.check("spin traces <g x g x>_0 = 2xx - gQ, sandwich -2x, trace 4<X>_0 (16 on the algebra); propagator degree -3", ok)
    return ok


# ---------------------------------------------------------------- vacuum polarisation
def _vacuum_polarisation_parts():
    """Return (sd6 part, sd4 part) of -tr(g S(x) g S(-x)) / (e^2 / pi^4) with S = alpha x + beta.
    Trace: 4[-alpha^2 (2xx - g s) + beta^2 g] (from the spin traces). alpha, beta in units pi^-2."""
    # Klein-Gordon recursion on the flat field: Delta = 1/(4 pi^2 s) + A m^2 ln s + ...; -box(A ln s) + 1/(4 s) = 0
    box_ln = box({(0, 1): F(1)})                     # = 4/s (L and ln s differ by a constant)
    A = F(1, 4) / box_ln[(-1, 0)]                    # in units pi^-2
    alpha0 = F(1, 2)                                  # -dslash(1/(4 pi^2 s)) = x/(2 pi^2 s^2)
    alpha2 = -2 * A                                   # -dslash(A m^2 ln s) = -2 A m^2 x / s
    beta1 = F(1, 4)                                   # m Delta_0
    # alpha^2 = alpha0^2 s^-4 + 2 alpha0 alpha2 m^2 s^-3 ; beta^2 = beta1^2 m^2 s^-2
    # -tr = -4[-alpha^2 (2xx - g s) + beta^2 g] = 4 alpha^2 (2xx - g s) - 4 beta^2 g
    lead = (rscl(F(4) * alpha0 ** 2, {(-3, 0): F(-1)}), rscl(F(4) * alpha0 ** 2, {(-4, 0): F(2)}))
    a2 = 2 * alpha0 * alpha2
    m2 = (radd(rscl(F(4) * a2, {(-2, 0): F(-1)}), rscl(F(-4) * beta1 ** 2, {(-2, 0): F(1)})),
          rscl(F(4) * a2, {(-3, 0): F(2)}))
    return A, lead, m2


def check_vacuum_polarisation_extension_is_transverse_and_gives_the_log_coefficient():
    premise("field-theory.second-quantisation")
    premise("field-theory.coupled-system-tree-level")
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    A, lead, m2 = _vacuum_polarisation_parts()
    ok = A == F(1, 16)                                                # m^2 ln s coefficient 1/(16 pi^2)
    ok = ok and lead == ({(-3, 0): F(-1)}, {(-4, 0): F(2)})          # (e^2/pi^4)(2xx - g s)/s^4
    inv_s2, inv_s, ls = {(-2, 0): F(1)}, {(-1, 0): F(1)}, {(-1, 1): F(1)}
    ok = ok and teq(lead, tscl(F(1, 12), trans_t(inv_s2)))           # = (1/12)(dd - g box) s^-2
    ok = ok and teq(m2, tscl(F(-1, 8), trans_t(inv_s)))              # = -(m^2/8)(dd - g box)(1/s)
    ok = ok and div_t(lead) == {} and div_t(m2) == {}
    ok = ok and rscl(F(-1, 4), box(ls)) == inv_s2 and box(inv_s) == {}
    # extension: lead = (1/12)(dd - g box)(-1/4) box(L/s); mu d/dmu acts on L/s only
    c_ext = F(1, 12) * F(-1, 4)
    mu_ls = mu_dmu(ls)                                               # = 2/s
    ok = ok and mu_ls == {(-1, 0): F(2)}
    dbox = delta_coefficient_of_box_inv_s()                          # box(1/s) = -4 pi^2 delta
    ok = ok and dbox == F(-4)
    coef_delta = c_ext * mu_ls[(-1, 0)] * dbox                        # times pi^-4 pi^2 = pi^-2
    ok = ok and coef_delta == F(1, 6)                                # (e^2/(6 pi^2))(dd - g box) delta
    # Fourier (d -> i q): (dd - g box) delta -> q^2 g - q q; mu d/dmu Pi(q^2) = 1/6; Pi = -c ln(q^2/mu^2): 2c = 1/6
    c_log = coef_delta / 2
    ok = ok and c_log == F(1, 12)
    # the scaling-degree-4 part extends uniquely among transverse extensions: its ambiguity c g delta has
    # divergence c d delta, zero only for c = 0; the part is mu-independent
    ok = ok and mu_dmu(m2[0]) == {} and mu_dmu(m2[1]) == {}
    GA.check("vacuum polarisation: (1/12)(dd - g box)s^-2 - (m^2/8)(dd - g box)(1/s), transverse; "
             "mu-derivative (1/6)(dd - g box)delta pi^-2; log coefficient e^2/(12 pi^2)", ok)
    return ok


# ---------------------------------------------------------------- scalar bubble
def check_scalar_bubble_extension_gives_the_quartic_coefficient():
    premise("field-theory.second-quantisation")
    bubble = rmul({(-1, 0): F(1, 4)}, {(-1, 0): F(1, 4)})           # Delta_0^2 = 1/(16 pi^4 s^2)
    ok = bubble == {(-2, 0): F(1, 16)}
    ext = F(1, 16) * F(-1, 4)                                        # times box(L/s)
    ok = ok and rscl(ext, box({(-1, 1): F(1)})) == bubble
    coef = ext * mu_dmu({(-1, 1): F(1)})[(-1, 0)] * delta_coefficient_of_box_inv_s()   # pi^-4 pi^2
    ok = ok and coef == F(1, 8)                                      # delta / (8 pi^2)
    beta = 3 * F(1, 2) * coef                                         # three channels, symmetry factor 1/2
    ok = ok and beta == F(3, 16)
    ok = ok and sd_of(bubble) == 4
    GA.check("scalar bubble: mu-derivative delta/(8 pi^2); quartic coefficient 3/(16 pi^2) for lambda phi^4/4!", ok)
    return ok


# ---------------------------------------------------------------- scaling degrees
def check_scaling_degrees_and_degrees_of_divergence():
    premise("field-theory.second-quantisation")
    premise("synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field")
    A, lead, m2 = _vacuum_polarisation_parts()
    ok = max(sd_of(lead[0]), sd_of(lead[1], 2)) == 6
    ok = ok and max(sd_of(m2[0]), sd_of(m2[1], 2)) == 4
    # self-energy numerator structure (Feynman-gauge photon line): x/(2 pi^2 s^2) * 1/(4 pi^2 s) -> x / s^3
    se = rmul({(-2, 0): F(1, 2)}, {(-1, 0): F(1, 4)})
    ok = ok and sd_of(se, 1) == 5
    ok = ok and rscl(F(1, 16), dslash(box({(-1, 1): F(1)}))) == {(-3, 0): F(1)}
    # omega = sd - d with d = 4, and the power-counting values for the vertex, three- and four-photon kernels
    sd_dirac, sd_photon = 3, 2
    omegas = {"vac": 6 - 4, "self": 5 - 4, "bubble": 4 - 4,
              "vertex": 2 * sd_dirac + sd_photon - 8, "three": 3 * sd_dirac - 8, "four": 4 * sd_dirac - 12}
    ok = ok and omegas == {"vac": 2, "self": 1, "bubble": 0, "vertex": 0, "three": 1, "four": 0}
    GA.check("scaling degrees 6, 4, 5, 4 and omega = 2, 1, 0, 0, 1, 0", ok)
    return ok


# ---------------------------------------------------------------- covariant ambiguities
SIG = (1, -1, -1, -1)
G = [GA.gen(i) for i in range(4)]
GENS = [GA.mul(G[i], G[j], SIG) for i in range(4) for j in range(i + 1, 4)]
BL = GA.all_blades(4)


def _m(x, y):
    return GA.mul(x, y, SIG)


def _ch(b, x):
    return GA.scal(F(1, 2), GA.sub(_m(b, x), _m(x, b)))


def _vec_matrix(b):
    mm = [[F(0)] * 4 for _ in range(4)]
    for d in range(4):
        r = _ch(b, G[d])
        for c in range(4):
            mm[c][d] = r.get((c,), F(0))
    return mm


MATS = [_vec_matrix(b) for b in GENS]


def _put(p, key, v):
    w = p.get(key, F(0)) + v
    if w:
        p[key] = w
    else:
        p.pop(key, None)


def _cov(p, nv, b, mm):
    out = {}
    for (e, bl), c in p.items():
        for i in range(nv):
            for cc in range(4):
                k = e[4 * i + cc]
                if not k:
                    continue
                for d in range(4):
                    if mm[cc][d] == 0:
                        continue
                    e2 = list(e)
                    e2[4 * i + cc] -= 1
                    e2[4 * i + d] += 1
                    _put(out, (tuple(e2), bl), c * k * mm[cc][d])
        for b2, v in _ch(b, {bl: F(1)}).items():
            _put(out, (e, b2), -c * v)
    return out


def _subst(p, rule):
    out = {}
    for (e, bl), c in p.items():
        terms = [(tuple(e), c)]
        for i, lin in rule.items():
            new = []
            for ee, cc in terms:
                deg = [ee[4 * i + k] for k in range(4)]
                if sum(deg) == 0:
                    new.append((ee, cc))
                    continue
                comp = deg.index(1)
                for coef, j in lin:
                    e2 = list(ee)
                    e2[4 * i + comp] -= 1
                    e2[4 * j + comp] += 1
                    new.append((tuple(e2), cc * coef))
            terms = new
        for ee, cc in terms:
            _put(out, (ee, bl), cc)
    return out


def _parity(p, nv):
    out = {}
    s = [1, -1, -1, -1]
    for (e, bl), c in p.items():
        sign = 1
        for i in range(nv):
            for k in range(4):
                if e[4 * i + k] % 2 and s[k] < 0:
                    sign = -sign
        _put(out, (e, bl), c * sign)
        for b2, v in _m(_m(G[0], {bl: F(1)}), G[0]).items():
            _put(out, (e, b2), -c * v)
    return out


def _monos(idx, nv, degmax, exact=False):
    comps = [4 * i + k for i in idx for k in range(4)]
    res = []

    def rec(pos, left, cur):
        if pos == len(comps):
            if (not exact) or left == 0:
                res.append(tuple(cur))
            return
        for k in range(left + 1):
            cur[comps[pos]] += k
            rec(pos + 1, left - k, cur)
            cur[comps[pos]] -= k
    rec(0, degmax, [0] * (4 * nv))
    return res


def _basis(nv, mom, pol, degmax, blades):
    mons = _monos(mom, nv, degmax) if mom else [tuple([0] * (4 * nv))]
    pm = [tuple([0] * (4 * nv))]
    for i in pol:
        pm = [tuple(x + y for x, y in zip(a, b)) for a in pm for b in _monos([i], nv, 1, exact=True)]
    return [{(tuple(x + y for x, y in zip(a, b)), bl): F(1)} for a in mons for b in pm for bl in blades]


def _rank(rows):
    piv, rank = {}, 0
    for r in rows:
        r = dict(r)
        while r:
            col = min(r)
            if col in piv:
                f = r[col]
                for k, v in piv[col].items():
                    w = r.get(k, F(0)) - f * v
                    if w:
                        r[k] = w
                    else:
                        r.pop(k, None)
            else:
                f = r[col]
                piv[col] = {k: v / f for k, v in r.items()}
                rank += 1
                break
    return rank


def _dim(bas, cons):
    rows = []
    for p in bas:
        row = {}
        for ci, fn in enumerate(cons):
            for key, v in fn(p).items():
                row[repr((ci, key))] = v
        rows.append(row)
    return len(bas) - _rank(rows)


def _covs(nv):
    return [(lambda p, b=b, mm=mm: _cov(p, nv, b, mm)) for b, mm in zip(GENS, MATS)]


def _sigma_vertex_ward(par):
    bs, bv = _basis(1, [0], [], 1, BL), _basis(1, [], [0], 0, BL)
    cons = _covs(1) + ([lambda p: _parity(p, 1)] if par else [])
    rows = []
    for tag, p in [("S", p) for p in bs] + [("V", p) for p in bv]:
        row = {}
        for ci, fn in enumerate(cons):
            for key, v in fn(p).items():
                row[repr((tag, ci, key))] = v
        for (e, bl), c in p.items():                 # Ward-Takahashi: Lambda(q) + Sigma_1(q) = 0
            if tag == "V" or sum(e) == 1:
                k = repr(("WT", e, bl))
                row[k] = row.get(k, F(0)) + c
        rows.append({k: v for k, v in row.items() if v})
    return len(rows) - _rank(rows)


def check_covariant_ambiguities_are_the_renormalisation_constants():
    premise("field-theory.second-quantisation")
    premise("field-theory.coupled-system-tree-level")
    ok = True
    # photon two-point: q (0), a (1), b (2); omega 2
    bas = _basis(3, [0], [1, 2], 2, [()])
    tr = lambda p: _subst(p, {1: [(F(1), 0)]})
    ok = ok and len(bas) == 240 and _dim(bas, _covs(3)) == 3 and _dim(bas, _covs(3) + [tr]) == 1
    # self-energy: q (0), Clifford valued, omega 1
    bas = _basis(1, [0], [], 1, BL)
    par = lambda p: _parity(p, 1)
    ok = ok and len(bas) == 80 and _dim(bas, _covs(1)) == 4 and _dim(bas, _covs(1) + [par]) == 2
    # vertex: a (0), omega 0
    bas = _basis(1, [], [0], 0, BL)
    ok = ok and len(bas) == 64 and _dim(bas, _covs(1)) == 2 and _dim(bas, _covs(1) + [par]) == 1
    # self-energy and vertex tied by the Ward-Takahashi identity
    ok = ok and _sigma_vertex_ward(True) == 2 and _sigma_vertex_ward(False) == 4
    # the explicit solution: Sigma = c_m + c_2 q, Lambda = c_V a; Ward-Takahashi residual c_V q + c_2 q = 0
    for c2, cv in ((F(1), F(-1)), (F(1), F(1))):
        res = GA.add(GA.scal(cv, G[1]), GA.scal(c2, G[1]))
        ok = ok and (GA.is_zero(res) == (cv == -c2))
    # three-current: q1 (0), q2 (1), a1 (2), a2 (3), a3 (4); omega 1
    bas = _basis(5, [0, 1], [2, 3, 4], 1, [()])
    w1 = lambda p: _subst(p, {2: [(F(1), 0)]})
    w2 = lambda p: _subst(p, {3: [(F(1), 1)]})
    w3 = lambda p: _subst(p, {4: [(F(-1), 0), (F(-1), 1)]})
    ok = ok and len(bas) == 576 and _dim(bas, _covs(5)) == 8
    ok = ok and _dim(bas, _covs(5) + [w1, w2]) == 0 and _dim(bas, _covs(5) + [w2, w3]) == 0
    ok = ok and _dim(bas, _covs(5) + [w1, w3]) == 0
    ok = ok and _dim(bas, _covs(5) + [w1]) > 0
    # four-photon: a1..a4 (0..3), q1 (4) for the transversality substitution; omega 0
    bas = _basis(5, [], [0, 1, 2, 3], 0, [()])
    ok = ok and len(bas) == 256 and _dim(bas, _covs(5)) == 4
    ok = ok and _dim(bas, _covs(5) + [lambda p: _subst(p, {0: [(F(1), 4)]})]) == 0
    GA.check("covariant ambiguities: photon 3 -> 1, self-energy 4 -> 2, vertex 2 -> 1, Ward-Takahashi 2 (4), "
             "three-current 8 -> 0 on two legs, four-photon 4 -> 0", ok)
    return ok


# ---------------------------------------------------------------- floors
S6 = (1, -1, -1, -1, 1, -1)
BIV6 = [b for b in GA.all_blades(6) if len(b) == 2]


def _m6(x, y):
    return GA.mul(x, y, S6)


def _br6(x, y):
    return GA.sub(_m6(x, y), _m6(y, x))


def _v6(x):
    return [x.get(b, F(0)) for b in BIV6]


def _closure(gens):
    basis = []

    def addv(x):
        if GA.rank_of_vectors(basis + [_v6(x)]) > len(basis):
            basis.append(_v6(x))
            return True
        return False
    for g in gens:
        addv(g)
    changed = True
    while changed:
        changed = False
        els = [{b: c for b, c in zip(BIV6, v) if c} for v in basis]
        for x in els:
            for y in els:
                if addv(_br6(x, y)):
                    changed = True
    return len(basis)


def check_no_weighting_of_the_conformal_energy_keeps_a_boost():
    premise("synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off")
    premise("field-theory.twistor-attachment")
    h = _m6(GA.gen(0), GA.gen(4))
    k = [{b: F(1)} for b in BIV6 if GA.is_zero(_br6(h, {b: F(1)}))]
    ok = len(k) == 7 and _closure(k) == 7
    ninf, n0 = GA.add(GA.gen(4), GA.gen(5)), GA.sub(GA.gen(4), GA.gen(5))
    tests = [_m6(GA.gen(0), GA.gen(1)), _m6(GA.gen(0), GA.gen(3)),
             GA.add(_m6(GA.gen(0), GA.gen(1)), GA.scal(F(2), _m6(GA.gen(0), GA.gen(2)))),
             _m6(GA.gen(1), ninf), _m6(GA.gen(0), ninf), _m6(GA.gen(2), n0), _m6(GA.gen(4), GA.gen(5))]
    for x in tests:
        ok = ok and not GA.is_zero(_br6(h, x)) and _closure(k + [x]) == 15
    # every bivector either commutes or anticommutes with h; the anticommuting ones span the 8-dim complement
    anti = [b for b in BIV6 if GA.is_zero(GA.add(_m6(h, {b: F(1)}), _m6({b: F(1)}, h)))]
    ok = ok and len(anti) == 8
    GA.check("Cl(2,4): commutant of gamma_0 e_+ is 7-dim and closed; with any one boost, translation, special "
             "conformal generator or the dilation it generates all 15 bivectors", ok)
    return ok
