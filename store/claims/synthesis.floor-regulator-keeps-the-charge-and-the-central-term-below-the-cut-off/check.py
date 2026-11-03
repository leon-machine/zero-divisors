"""synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off: exact checks.

Cl(1,3) ground with 2N tower planes; plane j carries the mode of momentum k = j - N (k = -N .. N-1),
a*_k = (e + f)/2, a_k = (e - f)/2 (the CAR of Fact field-theory.imported-tower-limit). H = sum k n_k,
Ntot = sum n_k (the charge), rho(p) = sum a*_{k+p} a_k over k with k, k + p in the window. For N = 1, 2, 3:
(1) [Ntot, H] = 0 and [H, rho(p)] = p rho(p), rho(p) != 0, for every p with 1 <= |p| <= 2N - 1, exactly; rho(2N) = 0.
(2) [rho(p), rho(-p)] = sum_{k >= N - p} n_k - sum_{k < -N + p} n_k for 1 <= p <= 2N, and its scalar part is 0.
(3) On the filled sea (k < 0 occupied): [rho(-p), rho(p)] acts as min(p, 2N - p); rho(-p) annihilates the sea;
    rho(p) sea is an eigenstate of H with eigenvalue E_sea + p and rho(-p) rho(p) sea = min(p, 2N - p) sea.
    On the sea with the top mode also occupied, [rho(-1), rho(1)] acts as 0, not 1.
(4) In Cl(2,4) (gamma_0..gamma_3, e_+, e_-; Q(e_+) = 1, Q(e_-) = -1) the commutant of the conformal
    Hamiltonian gamma_0 e_+ among the 15 bivectors has dimension 7; its intersection with the Lorentz bivectors
    gamma_mu gamma_nu is the span of the three rotations, and it contains no nonzero translation
    gamma_mu n_inf (n_inf = e_+ + e_-) and no nonzero special conformal generator gamma_mu n_0 (n_0 = e_+ - e_-).
(5) That commutant is closed under the commutator, and together with any one of the eight anticommuting basis
    bivectors (the boosts gamma_0 gamma_j, gamma_0 e_-, gamma_j e_+, the dilation e_+ e_-) or of the eleven boosts
    gamma_0 gamma_j, translations gamma_mu n_inf and special conformal generators gamma_mu n_0 it generates all 15.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S4 = (1, -1, -1, -1)
NS = [1, 2, 3]


def _scl(c, x):
    out = {}
    for b, v in x.items():
        w = c * v
        if w != 0:
            out[b] = w
    return out


def _plane(q):
    e_, f_ = 4 + 2 * q, 5 + 2 * q
    return (GA.add(_scl(F(1, 2), GA.gen(e_)), _scl(F(1, 2), GA.gen(f_))),
            GA.add(_scl(F(1, 2), GA.gen(e_)), _scl(F(-1, 2), GA.gen(f_))))


def _system(N):
    ST = tuple(list(S4) + [1, -1] * (2 * N))
    m = lambda x, y: GA.mul(x, y, ST)
    ks = list(range(-N, N))
    pl = {k: _plane(k + N) for k in ks}
    ad = {k: pl[k][0] for k in ks}
    a = {k: pl[k][1] for k in ks}
    n = {k: m(ad[k], a[k]) for k in ks}
    vac = {(): F(1)}
    for k in ks:
        vac = m(vac, m(a[k], ad[k]))
    sea = vac
    for k in ks:
        if k < 0:
            sea = m(ad[k], sea)
    H = GA.add(*[_scl(F(k), n[k]) for k in ks])
    Q = GA.add(*[n[k] for k in ks])
    return m, ks, a, ad, n, sea, H, Q


def _rho(p, ks, a, ad, m):
    terms = [m(ad[k + p], a[k]) for k in ks if (k + p) in a]
    return GA.add(*terms) if terms else {}


def _comm(m, x, y):
    return GA.sub(m(x, y), m(y, x))


def check_floor_keeps_charge_and_continuity():
    premise("field-theory.imported-tower-limit")
    ok = True
    cases = 0
    for N in NS:
        m, ks, a, ad, n, sea, H, Q = _system(N)
        ok = ok and GA.is_zero(_comm(m, Q, H))
        for p in list(range(1, 2 * N)) + list(range(-2 * N + 1, 0)):
            r = _rho(p, ks, a, ad, m)
            ok = ok and not GA.is_zero(r) and GA.eq(_comm(m, H, r), _scl(F(p), r))
            ok = ok and GA.is_zero(_comm(m, Q, r))
            ok = ok and len([k for k in ks if (k + p) in a]) == 2 * N - abs(p)
            cases += 1
        ok = ok and GA.is_zero(_rho(2 * N, ks, a, ad, m)) and GA.is_zero(_rho(-2 * N, ks, a, ad, m))
    ok = ok and cases == 18
    GA.check("each floor: [Ntot, H] = 0, [Ntot, rho(p)] = 0 and [H, rho(p)] = p rho(p) exactly (N = 1, 2, 3)", ok)
    return ok


def check_central_term_is_an_edge_operator():
    premise("field-theory.imported-tower-limit")
    ok = True
    cases = 0
    for N in NS:
        m, ks, a, ad, n, sea, H, Q = _system(N)
        for p in range(1, 2 * N + 1):
            c = _comm(m, _rho(p, ks, a, ad, m), _rho(-p, ks, a, ad, m))
            top = [n[k] for k in ks if k >= N - p]
            bot = [n[k] for k in ks if k < -N + p]
            ok = ok and len(top) == p and len(bot) == p
            ok = ok and GA.eq(c, GA.sub(GA.add(*top), GA.add(*bot)))
            ok = ok and c.get((), F(0)) == 0
            ok = ok and (GA.is_zero(c) == (p == 2 * N))
            cases += 1
    ok = ok and cases == 12
    GA.check("[rho(p), rho(-p)] = (top p numbers) - (bottom p numbers), scalar part 0, for 1 <= p <= 2N", ok)
    return ok


def check_sea_value_and_spectral_weight():
    premise("field-theory.imported-tower-limit")
    ok = True
    for N in NS:
        m, ks, a, ad, n, sea, H, Q = _system(N)
        e_sea = sum(k for k in ks if k < 0)
        ok = ok and GA.eq(m(H, sea), _scl(F(e_sea), sea)) and not GA.is_zero(sea)
        for p in range(1, 2 * N + 1):
            rp, rm = _rho(p, ks, a, ad, m), _rho(-p, ks, a, ad, m)
            w = min(p, 2 * N - p)
            ok = ok and GA.eq(m(_comm(m, rm, rp), sea), _scl(F(w), sea))
            ok = ok and GA.is_zero(m(rm, sea))
            ex = m(rp, sea)
            ok = ok and GA.eq(m(H, ex), _scl(F(e_sea + p), ex))
            ok = ok and GA.eq(m(rm, ex), _scl(F(w), sea))
            if p <= N:
                ok = ok and w == p
        top = m(ad[N - 1], sea)
        r1, rm1 = _rho(1, ks, a, ad, m), _rho(-1, ks, a, ad, m)
        ok = ok and not GA.is_zero(top) and GA.is_zero(m(_comm(m, rm1, r1), top))
    GA.check("filled sea: [rho(-p), rho(p)] = min(p, 2N - p) = p for p <= N; rho(p) sea at energy p, weight min(p, 2N - p);"
             " with the top mode occupied the p = 1 value is 0", ok)
    return ok


S6 = (1, -1, -1, -1, 1, -1)
BIV6 = [b for b in GA.all_blades(6) if len(b) == 2]


def _bv(x):
    return [x.get(b, F(0)) for b in BIV6]


def _kernel_dim_and_basis(cols):
    """Exact null space of the matrix whose columns are the given rational vectors."""
    nrow = len(cols[0])
    ncol = len(cols)
    rows = [[cols[j][i] for j in range(ncol)] for i in range(nrow)]
    piv = []
    r = 0
    for c in range(ncol):
        p = next((i for i in range(r, nrow) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(nrow):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncol
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -rows[i][fc]
        basis.append(v)
    return basis


def check_conformal_energy_cut_keeps_no_boost():
    premise("field-theory.twistor-attachment")
    m = lambda x, y: GA.mul(x, y, S6)
    g = [GA.gen(i) for i in range(6)]
    Hc = m(g[0], g[4])
    ok = GA.eq(m(Hc, Hc), GA.sc(-1))                       # compact: squares to -1
    comm_cols = []
    for b in BIV6:
        x = {b: F(1)}
        comm_cols.append(_bv(GA.sub(m(Hc, x), m(x, Hc))))
    ker = _kernel_dim_and_basis(comm_cols)
    ok = ok and len(ker) == 7
    # intersection with a subspace spanned by given bivectors: solve sum s_i u_i in commutant
    def inter_dim(us):
        cols = [_bv(GA.sub(m(Hc, u), m(u, Hc))) for u in us]
        return len(_kernel_dim_and_basis(cols))
    lor = [m(g[i], g[j]) for i in range(4) for j in range(i + 1, 4)]
    rot = [m(g[i], g[j]) for i in range(1, 4) for j in range(i + 1, 4)]
    boosts = [m(g[0], g[j]) for j in range(1, 4)]
    ninf = GA.add(g[4], g[5])
    n0 = GA.sub(g[4], g[5])
    ok = ok and GA.is_zero(m(ninf, ninf)) and GA.is_zero(m(n0, n0))
    trans = [m(g[mu], ninf) for mu in range(4)]
    spec = [m(g[mu], n0) for mu in range(4)]
    ok = ok and inter_dim(lor) == 3 and inter_dim(rot) == 3 and inter_dim(boosts) == 0
    ok = ok and inter_dim(trans) == 0 and inter_dim(spec) == 0
    # P_0 + K_0 is a multiple of the conformal Hamiltonian (the compact combination)
    ok = ok and GA.eq(GA.add(trans[0], spec[0]), _scl(F(2), Hc))
    GA.check("Cl(2,4): commutant of gamma_0 e_+ among bivectors has dimension 7, meets the Lorentz algebra in the"
             " three rotations only and contains no translation or special conformal generator", ok)
    return ok


def _closure_dim(gens):
    """Dimension of the Lie algebra generated by the given bivectors of Cl(2,4) (exact ranks)."""
    m = lambda x, y: GA.mul(x, y, S6)
    br = lambda x, y: GA.sub(m(x, y), m(y, x))
    basis = []

    def addv(x):
        if GA.rank_of_vectors(basis + [_bv(x)]) > len(basis):
            basis.append(_bv(x))
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
                if addv(br(x, y)):
                    changed = True
    return len(basis)


def check_no_weighting_of_the_conformal_energy_keeps_a_boost():
    """(v) The commutant k of the compact gamma_0 e_+ is 7-dimensional and closed; the anticommuting basis
    bivectors span the 8-dimensional complement, and k together with any one of them, or with any one of the
    eleven boosts gamma_0 gamma_j, translations gamma_mu n_inf and special conformal generators gamma_mu n_0,
    generates all 15 bivectors of Cl(2,4); Schur's lemma then gives (v) (proof)."""
    premise("field-theory.twistor-attachment")
    m = lambda x, y: GA.mul(x, y, S6)
    br = lambda x, y: GA.sub(m(x, y), m(y, x))
    g = [GA.gen(i) for i in range(6)]
    h = m(g[0], g[4])
    ok = GA.eq(m(h, h), GA.sc(-1))
    k = [{b: F(1)} for b in BIV6 if GA.is_zero(br(h, {b: F(1)}))]
    anti = [{b: F(1)} for b in BIV6 if GA.is_zero(GA.add(m(h, {b: F(1)}), m({b: F(1)}, h)))]
    ok = ok and len(k) == 7 and _closure_dim(k) == 7 and len(anti) == 8
    ninf, n0 = GA.add(g[4], g[5]), GA.sub(g[4], g[5])
    ok = ok and GA.is_zero(m(ninf, ninf)) and GA.is_zero(m(n0, n0))
    tests = [m(g[0], g[j]) for j in range(1, 4)] + [m(g[mu], ninf) for mu in range(4)] + \
        [m(g[mu], n0) for mu in range(4)]
    ok = ok and len(tests) == 11
    for x in anti + tests:
        ok = ok and not GA.is_zero(br(h, x)) and _closure_dim(k + [x]) == 15
    GA.check("Cl(2,4): commutant of gamma_0 e_+ is 7-dim and closed; with any one anticommuting basis bivector, "
             "boost, translation or special conformal generator it generates all 15 bivectors", ok)
    return ok

if __name__ == "__main__":
    check_floor_keeps_charge_and_continuity()
    check_central_term_is_an_edge_operator()
    check_sea_value_and_spectral_weight()
    check_conformal_energy_cut_keeps_no_boost()
    check_no_weighting_of_the_conformal_energy_keeps_a_boost()
