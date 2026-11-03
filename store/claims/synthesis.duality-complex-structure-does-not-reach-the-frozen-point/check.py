"""The duality complex structure does not reach the frozen point.

Cl(2,4), generators e0..e5 with squares (+,-,-,-,+,-); n0 = (e4 + e5)/2, ninf = e4 - e5; i6 = e0..e5;
X = n0, I = ninf + rho n0.  J = left multiplication by the spacetime pseudoscalar i4 = e0 e1 e2 e3 (i4^2 = -1),
the Hodge star on spacetime bivectors (stored Lorentzian duality lemma).  The commutant of a Lie algebra g of
bivectors is {T in End(g): T ad_x = ad_x T for all x in g}; a complex structure commuting with ad lies in it.
Slot computations: the unreduced connection -ninf ^ e + n0 ^ S(e) at a point with frame the identity; Lorentz
block F(e, f) = -R(e ^ f) + [Theta(e) x Theta(f)]_L, Theta(e) = -ninf ^ e + n0 ^ S(e), as 6-vectors on the
blades e_a e_b (a < b < 4).  Pairings on the Lorentz block: eps_X(B, B') = eps(I, X, B, B') (coefficient of i6),
K(B, B') = <B B'>_0; four-form value of a pairing beta on two two-forms: 1/4 sum_p sgn(p) beta(F_p0p1, G_p2p3).
The slot S is a mixed tensor S[a][j] (S(e_a) = sum_j S[a][j] e_j); Schouten slot S = P_aj eta^jj.
Exact arithmetic only (Fractions); fixed tables, no randomness.
"""
from fractions import Fraction as Fr
from itertools import permutations
import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
ETA = (1, -1, -1, -1)
R4 = range(4)
PS = (0, 1, 2, 3, 4, 5)
E = [GA.gen(i) for i in range(6)]
N0 = GA.scal(Fr(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
X = N0
LB = [(a, b) for a in R4 for b in R4 if a < b]


def _m(x, y):
    return GA.mul(x, y, SQ)


def _grade(x, g):
    return {b: c for b, c in x.items() if len(b) == g}


def _deg(x):
    return max((len(b) for b in x), default=0)


def _wedge(*xs):
    out = xs[0]
    g = _deg(out)
    for y in xs[1:]:
        g += _deg(y)
        out = _grade(_m(out, y), g)
    return out


def _cp(x, y):
    return GA.scal(Fr(1, 2), GA.sub(_m(x, y), _m(y, x)))


def _sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


PERMS = [(p, _sign(p)) for p in permutations(range(4))]
I4 = _m(_m(E[0], E[1]), _m(E[2], E[3]))
LOR = [_wedge(E[a], E[b]) for (a, b) in LB]
ALLB = [_wedge(E[a], E[b]) for a in range(6) for b in range(a + 1, 6)]


def _comb(c, space):
    out = {}
    for ci, s in zip(c, space):
        if ci:
            out = GA.add(out, GA.scal(ci, s))
    return out


def _rref_null(rows, n):
    M = [list(r) for r in rows]
    piv, r = [], 0
    for col in range(n):
        p = next((k for k in range(r, len(M)) if M[k][col] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][col]
        M[r] = [a / pv for a in M[r]]
        for k in range(len(M)):
            if k != r and M[k][col] != 0:
                f = M[k][col]
                M[k] = [a - f * b for a, b in zip(M[k], M[r])]
        piv.append(col)
        r += 1
    out = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for k, pc in enumerate(piv):
            v[pc] = -M[k][fc]
        out.append(v)
    return out


def _coords(x, space):
    keys = sorted({k for v in space for k in v} | set(x))
    n = len(space)
    rows = [[space[i].get(b, Fr(0)) for i in range(n)] + [-x.get(b, Fr(0))] for b in keys]
    ns = _rref_null(rows, n + 1)
    sol = [v for v in ns if v[n] != 0]
    if len(sol) != 1:
        raise ValueError("not uniquely in span")
    v = sol[0]
    return [c / v[n] for c in v[:n]]


def _ad_mats(space):
    n = len(space)
    return [[[_coords(_cp(g, space[j]), space)[i] for j in range(n)] for i in range(n)] for g in space]


def _commutant(space):
    n = len(space)
    rows = []
    for A in _ad_mats(space):
        for i in range(n):
            for j in range(n):
                row = [Fr(0)] * (n * n)
                for k in range(n):
                    row[i * n + k] += A[k][j]
                    row[k * n + j] -= A[i][k]
                rows.append(row)
    return _rref_null(rows, n * n)


def _stab(I):
    cols = [_cp(B, I) for B in ALLB]
    keys = sorted({k for c in cols for k in c})
    ns = _rref_null([[c.get(b, Fr(0)) for c in cols] for b in keys], 15)
    return [_comb(v, ALLB) for v in ns]


def _vec(c):
    out = {}
    for a in R4:
        if c[a]:
            out = GA.add(out, GA.scal(c[a], E[a]))
    return out


def _biv6(B):
    return [B.get(k, Fr(0)) for k in LB]


def _gram(pair):
    return [[pair(Bi, Bj) for Bj in LOR] for Bi in LOR]


def _form(F, G, M):
    tot = Fr(0)
    for p, s in PERMS:
        f, g = F[(p[0], p[1])], G[(p[2], p[3])]
        tot += s * sum(f[i] * M[i][j] * g[j] for i in range(6) for j in range(6) if f[i] and g[j])
    return tot / 4


def _unit(i, j):
    return [[Fr(1) if (a, b) == (i, j) else Fr(0) for b in R4] for a in R4]


def _tblock(S):
    th = [GA.add(GA.neg(_wedge(NI, E[a])), _wedge(N0, _vec(S[a]))) for a in R4]
    return {(e, f): _biv6(_cp(th[e], th[f])) for e in R4 for f in R4 if e != f}


def _rblock(R):
    return {(e, f): [R[(a, b, e, f)] * ETA[a] * ETA[b] for (a, b) in LB] for e in R4 for f in R4 if e != f}


def _lin(blocks, c):
    keys = blocks[0].keys()
    return {k: [sum(c[q] * blocks[q][k][i] for q in range(len(c)) if c[q]) for i in range(6)] for k in keys}


def _kn(h, k):
    return {(a, b, c, d): h[a][c] * k[b][d] + h[b][d] * k[a][c] - h[a][d] * k[b][c] - h[b][c] * k[a][d]
            for a in R4 for b in R4 for c in R4 for d in R4}


def _schouten_slot(R):
    Ric = [[sum(Fr(ETA[a]) * R[(a, d, a, b)] for a in R4) for d in R4] for b in R4]
    sc = sum(Fr(ETA[b]) * Ric[b][b] for b in R4)
    P = [[(Ric[i][j] - (sc / 6 if i == j else 0) * ETA[i]) / 2 for j in R4] for i in R4]
    return [P[a][j] * ETA[j] for a in R4 for j in R4]


def _det(M):
    M = [list(r) for r in M]
    n, d = len(M), Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d


def _setup(rho):
    I = GA.add(NI, GA.scal(rho, N0))
    G6 = _gram(lambda B, C: _wedge(I, X, B, C).get(PS, Fr(0)))
    K6 = _gram(lambda B, C: _m(B, C).get((), Fr(0)))
    T = [_tblock(_unit(i, j)) for i in R4 for j in R4]
    H = [[_form(T[k], T[l], G6) for l in range(16)] for k in range(16)]
    HK = [[_form(T[k], T[l], K6) for l in range(16)] for k in range(16)]
    return I, G6, K6, T, H, HK


GK_TORSION = [Fr(4), Fr(3), Fr(-5, 2), Fr(1, 2), Fr(-3), Fr(5), Fr(5, 2), Fr(-1), Fr(5, 2), Fr(5, 2), Fr(-2), Fr(7),
              Fr(-1, 2), Fr(-1), Fr(7), Fr(3)]


SYM = [(i, j) for i in R4 for j in R4 if i <= j]
ASYM = [(i, j) for i in R4 for j in R4 if i < j]


def _slotvec(i, j, sgn):
    """Mixed slot vector of the lowered-index symmetric (sgn = +1) or antisymmetric (sgn = -1) unit."""
    v = [Fr(0)] * 16
    v[4 * i + j] += ETA[j]
    if i != j:
        v[4 * j + i] += sgn * ETA[i]
    return v


def _bil(A, u, v):
    return sum(u[k] * A[k][l] * v[l] for k in range(16) for l in range(16) if u[k] and v[l])


# ---------------------------------------------------------------------------------------------------------


def check_duality_is_the_lorentz_commutant():
    """(i) commutant dims: so(1,3) 2 (spanned by 1 and J), stab(I) 1 at rho in {3/7, -2/5, 0}, the parabolic
    algebra of the line of X (dimension 11) 1, so(2,4) 1; J
    preserves the Lorentz bivectors, squares to -1 there, and sends part of stab(I) out of the bivectors."""
    premise("correspondence.lorentzian-duality-complex-structure")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = _m(I4, I4) == {(): Fr(-1)}
    cl = _commutant(LOR)
    ok = ok and len(cl) == 2
    Jm = [[_coords(_m(I4, LOR[j]), LOR)[i] for j in range(6)] for i in range(6)]
    J2 = [[sum(Jm[i][k] * Jm[k][j] for k in range(6)) for j in range(6)] for i in range(6)]
    ok = ok and all(J2[i][j] == (-1 if i == j else 0) for i in range(6) for j in range(6))
    flatJ = [Jm[i][j] for i in range(6) for j in range(6)]
    flatI = [Fr(1 if i == j else 0) for i in range(6) for j in range(6)]
    ok = ok and GA.rank_of_vectors(cl + [flatJ, flatI]) == 2
    dims = []
    for rho in (Fr(3, 7), Fr(-2, 5), Fr(0)):
        I = GA.add(NI, GA.scal(rho, N0))
        st = _stab(I)
        nout = sum(1 for B in st if any(len(k) != 2 for k in _m(I4, B)))
        dims.append((len(st), len(_commutant(st)), nout))
    dims.append((15, len(_commutant(ALLB)), None))
    # parabolic algebra: bivectors B with B x X a multiple of X (stabiliser of the line of X)
    cols = [_cp(B, X) for B in ALLB]
    keys = [(k,) for k in range(6)]
    rows = [[cols[i].get(k, Fr(0)) for i in range(15)] + [-X.get(k, Fr(0))] for k in keys]
    ns = _rref_null(rows, 16)
    par = [_comb(v[:15], ALLB) for v in ns]
    nout_par = sum(1 for B in par if any(len(k) != 2 for k in _m(I4, B)))
    dims.append((len(par), len(_commutant(par)), nout_par))
    ok = ok and dims[:4] == [(10, 1, 4), (10, 1, 4), (10, 1, 4), (15, 1, None)]
    ok = ok and dims[4] == (11, 1, 5)
    GA.check("(i) commutants: so(1,3) 2 = <1, J>; stab(I) 1 (rho = 3/7, -2/5, 0); parabolic 1; so(2,4) 1", ok)
    return ok


def check_frozen_point_pairing_is_the_duality_pairing():
    """(ii) On the Lorentz block eps_X(B, B') = -K(B, J B') = -<B i4 B'>_0, for every rho."""
    premise("correspondence.lorentzian-duality-complex-structure")
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    ok = True
    for rho in (Fr(3, 7), Fr(-2, 5)):
        I, G6, K6, _, _, _ = _setup(rho)
        J6 = _gram(lambda B, C: _m(_m(B, I4), C).get((), Fr(0)))
        ok = ok and all(G6[i][j] == -J6[i][j] for i in range(6) for j in range(6))
        ok = ok and any(G6[i][j] != 0 for i in range(6) for j in range(6))
        ok = ok and all(K6[i][j] == K6[j][i] for i in range(6) for j in range(6))
        anti = [1, -1, 1, 1, -1, 1]
        diag = [1, 1, 1, -1, -1, -1]
        ok = ok and all(G6[i][j] == (anti[i] if i + j == 5 else 0) for i in range(6) for j in range(6))
        ok = ok and all(K6[i][j] == (diag[i] if i == j else 0) for i in range(6) for j in range(6))
    GA.check("(ii) eps_X = -<B i4 B'>_0 on the Lorentz block", ok)
    return ok


def check_chiral_slot_hessian():
    """(iii) Slot Hessians: K blind to the symmetric slot, sym/antisym blocks decouple; on the antisymmetric
    block det(H + tau HK) = -4096 (1 + tau^2)^3 (eight points, degree six); at tau = +-j the 32 x 32 real form
    has rank 26, a three-dimensional complex kernel."""
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    premise("correspondence.lorentzian-duality-complex-structure")
    _, _, _, _, H, HK = _setup(Fr(3, 7))
    sym = [_slotvec(i, j, 1) for (i, j) in SYM]
    asym = [_slotvec(i, j, -1) for (i, j) in ASYM]
    ok = GA.rank_of_vectors([list(r) for r in H]) == 16 and GA.rank_of_vectors([list(r) for r in HK]) == 6
    ok = ok and all(_bil(HK, u, v) == 0 for u in sym for v in sym + asym)
    ok = ok and all(_bil(H, u, v) == 0 for u in sym for v in asym)
    HA = [[_bil(H, u, v) for v in asym] for u in asym]
    KA = [[_bil(HK, u, v) for v in asym] for u in asym]
    for t in range(-3, 5):
        tau = Fr(t)
        ok = ok and _det([[HA[i][j] + tau * KA[i][j] for j in range(6)] for i in range(6)]) == \
            -4096 * (1 + tau * tau) ** 3
    ranks = []
    for s in (Fr(1), Fr(-1), Fr(2)):
        big = [[H[k][l] for l in range(16)] + [-s * HK[k][l] for l in range(16)] for k in range(16)]
        big += [[s * HK[k][l] for l in range(16)] + [H[k][l] for l in range(16)] for k in range(16)]
        ranks.append(GA.rank_of_vectors(big))
    ok = ok and ranks == [26, 26, 32]
    GA.check("(iii) det = -4096(1 + tau^2)^3 on the antisymmetric slot; chiral values tau = +-j: rank 26", ok)
    return ok


def check_schouten_slot_is_stationary_for_every_chirality():
    """(iv) On torsion-free curvature (spanned by the 100 Kulkarni-Nomizu products of basis symmetric matrices)
    both the eps_X and the K slot gradients vanish at the Schouten slot, so the Schouten slot is stationary for
    eps_X + tau K for every tau; with torsion the K gradient at the generalised Schouten slot does not vanish."""
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form")
    _, G6, K6, T, H, HK = _setup(Fr(3, 7))
    basis_sym = []
    for i in R4:
        for j in range(i, 4):
            M = [[Fr(0)] * 4 for _ in R4]
            M[i][j] = M[j][i] = Fr(1)
            basis_sym.append(M)
    n, nz = 0, 0
    for h in basis_sym:
        for k in basis_sym:
            R = _kn(h, k)
            mR = {kk: [-x for x in v] for kk, v in _rblock(R).items()}
            P = _schouten_slot(R)
            F = {kk: [mR[kk][i] + _lin(T, P)[kk][i] for i in range(6)] for kk in mR} if any(P) else mR
            for q in range(16):
                ok_e = _form(F, T[q], G6) == 0
                ok_k = _form(F, T[q], K6) == 0
                if not (ok_e and ok_k):
                    GA.check("(iv) gradient at Schouten", False)
                    return False
            n += 1
            nz += any(x != 0 for v in F.values() for x in v)
    vals = [Fr(x) for x in [3, -1, 2, 5, -4, 1, 0, 7, -2, 6, 1, -3, 2, 2, -5, 4, 1, 0, 3, -6, 2, 1, -1, 4, 5,
                            -2, 3, 1, 0, 2, -3, 1, 4, -1, 2, 6]]
    Rg = {(a, b, c, d): Fr(0) for a in R4 for b in R4 for c in R4 for d in R4}
    t = 0
    for (a, b) in LB:
        for (c, d) in LB:
            v = vals[t]
            t += 1
            Rg[(a, b, c, d)], Rg[(b, a, c, d)], Rg[(a, b, d, c)], Rg[(b, a, d, c)] = v, -v, -v, v
    mR = {kk: [-x for x in v] for kk, v in _rblock(Rg).items()}
    P = _schouten_slot(Rg)
    F = {kk: [mR[kk][i] + _lin(T, P)[kk][i] for i in range(6)] for kk in mR}
    ge = [_form(F, T[q], G6) for q in range(16)]
    gk = [_form(F, T[q], K6) for q in range(16)]
    ok = n == 100 and nz > 0 and all(x == 0 for x in ge) and any(x != 0 for x in gk)
    ok = ok and gk == GK_TORSION and nz == 72
    GA.check("(iv) Schouten slot stationary for eps_X and K on all torsion-free curvatures; K fails with torsion", ok)
    return ok


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("check_") and callable(fn):
            print(name, fn())
