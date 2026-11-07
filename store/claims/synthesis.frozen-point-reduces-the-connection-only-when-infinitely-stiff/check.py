"""The frozen point read as a Higgs field: it reduces the connection only in an infinitely stiff limit.

Cl(2,4), generators e0..e5 with squares (+,-,-,-,+,-); e0..e3 spacetime (store signature),
n0 = (e4 + e5)/2, ninf = e4 - e5 (n0 . ninf = 1, both null), unit pseudoscalar i6 = e0 e1 e2 e3 e4 e5;
eps(a, b, ...) is the coefficient of i6 in the wedge.  X = n0 (canonical tractor), I = ninf + rho n0 (the
frozen point, Lambda = 6 rho, Q(I) = 2 rho), V = X - I/(2 rho) (Stelle-West vector, Q(V) = -1/(2 rho)).
Unreduced connection at a point, frame the identity, in the form of the stored GTG tractor theorem with an
independent special-conformal slot S and dilation beta:
    Omega_T(e_a) = Omega(e_a) - ninf ^ e_a + n0 ^ S(e_a) + beta_a ninf ^ n0,   S(e_a) = sum_j S[a][j] e_j.
D Y = Omega_T x Y (commutator product).  Lorentz block of the field strength, algebraic in S:
    F(e, f) = -R(e ^ f) + [Theta(e) x Theta(f)]_Lorentz,  Theta(e) = -ninf ^ e + n0 ^ S(e)
(dOmega_T and the Omega, beta commutators add no Lorentz block).  Four-form conventions: two-form
F = (1/2) F_ef e^e ^ e^f; L1 = 1/4 sum_p sgn(p) eps(I, V, F_p0p1, F_p2p3); L3 = 1/2 sum_p sgn(p)
eps(I, V, DV_p0, DV_p1, F_p2p3); L5 = sum_p sgn(p) eps(I, V, DV_p0, ..., DV_p3); stiffness
St = sum_p sgn(p) eps(I, X, DI_p0, DI_p1, DX_p2, DX_p3).  Q2(M) = 2((tr M)^2 - tr(M M)).
Index readings: Ric_bd = sum_a eta^aa R_abad, sc its trace, G = Ric - sc/2 eta, Schouten P = (Ric - sc/6 eta)/2,
Weyl W = R - KN(P, eta), GB = Riem.Riem - 4 Ric.Ric + sc^2; the slot as a mixed tensor S[a][j] = P_aj eta^jj.
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
RHOS = (Fr(3, 7), Fr(-2, 5))
FINGERPRINT = [Fr(-27, 14), Fr(30, 7), Fr(-293, 14), Fr(-575, 28), Fr(9, 5), Fr(-4), Fr(-57, 5),
               Fr(-137, 10)]


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


def _dot(a, b):
    return _m(a, b).get((), Fr(0))


def _sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


PERMS = [(p, _sign(p)) for p in permutations(range(4))]


def _vec(c):
    out = {}
    for a in R4:
        if c[a]:
            out = GA.add(out, GA.scal(c[a], E[a]))
    return out


def _frozen(rho):
    I = GA.add(NI, GA.scal(rho, N0))
    V = GA.sub(X, GA.scal(1 / (2 * rho), I))
    return I, V


def _ident(c=Fr(1)):
    return [[c if a == j else Fr(0) for j in R4] for a in R4]


def _theta(S, a, H=None, beta=None):
    fr = E[a] if H is None else _vec(H[a])
    out = GA.add(GA.neg(_wedge(NI, fr)), _wedge(N0, _vec(S[a])))
    if beta is not None and beta[a]:
        out = GA.add(out, GA.scal(beta[a], _wedge(NI, N0)))
    return out


def _rbiv(R, e, f):
    out = {}
    for (a, b) in LB:
        c = R[(a, b, e, f)] * ETA[a] * ETA[b]
        if c:
            out = GA.add(out, GA.scal(c, _wedge(E[a], E[b])))
    return out


def _lorentz(B):
    return {k: v for k, v in B.items() if len(k) == 2 and k[1] < 4}


def _F(R, S, H=None):
    return {(e, f): _lorentz(GA.add(GA.neg(_rbiv(R, e, f)), _cp(_theta(S, e, H), _theta(S, f, H))))
            for e in R4 for f in R4 if e != f}


def _eps(*xs):
    if any(not x for x in xs):
        return Fr(0)
    return _wedge(*xs).get(PS, Fr(0))


def _L1(R, S, I, V, H=None):
    F = _F(R, S, H)
    return sum(s * _eps(I, V, F[(p[0], p[1])], F[(p[2], p[3])]) for p, s in PERMS) / 4


def _DV(S, V, beta=None):
    return [_cp(_theta(S, a, None, beta), V) for a in R4]


def _L3(R, S, I, V):
    F = _F(R, S)
    dv = _DV(S, V)
    return sum(s * _eps(I, V, dv[p[0]], dv[p[1]], F[(p[2], p[3])]) for p, s in PERMS) / 2


def _L5(S, I, V):
    dv = _DV(S, V)
    return sum(s * _eps(I, V, dv[p[0]], dv[p[1]], dv[p[2]], dv[p[3]]) for p, s in PERMS)


def _stiff(S, I, beta):
    di = [_cp(_theta(S, a, None, beta), I) for a in R4]
    dx = [_cp(_theta(S, a, None, beta), X) for a in R4]
    return sum(s * _eps(I, X, di[p[0]], di[p[1]], dx[p[2]], dx[p[3]]) for p, s in PERMS)


def _q2(M):
    tr = sum(M[a][a] for a in R4)
    return 2 * (tr * tr - sum(M[a][j] * M[j][a] for a in R4 for j in R4))


def _kn(h, k):
    return {(a, b, c, d): h[a][c] * k[b][d] + h[b][d] * k[a][c] - h[a][d] * k[b][c] - h[b][c] * k[a][d]
            for a in R4 for b in R4 for c in R4 for d in R4}


def _eta():
    return [[Fr(ETA[i]) if i == j else Fr(0) for j in R4] for i in R4]


TABLE = [[[2, 1, 0, -3], [1, -1, 4, 0], [0, 4, 5, 2], [-3, 0, 2, 7]],
         [[1, 0, 1, 0], [0, -5, 0, 1], [1, 0, 2, 0], [0, 1, 0, 3]],
         [[0, 2, -1, 1], [2, 3, 0, 0], [-1, 0, -2, 4], [1, 0, 4, 1]]]


def _mat(t):
    return [[Fr(x) for x in r] for r in t]


def _curv_tf():
    """A torsion-free (algebraic curvature tensor) sample: KN sums of fixed rational symmetric matrices."""
    A = _kn(_mat(TABLE[0]), _mat(TABLE[1]))
    B = _kn(_mat(TABLE[2]), _mat(TABLE[2]))
    return {k: A[k] + B[k] for k in A}


GENERIC = [3, -1, 2, 5, -4, 1, 0, 7, -2, 6, 1, -3, 2, 2, -5, 4, 1, 0, 3, -6, 2, 1, -1, 4, 5, -2, 3, 1, 0, 2,
           -3, 1, 4, -1, 2, 6]


def _curv_generic():
    """Antisymmetric in each pair only (no pair symmetry, no Bianchi): the curvature of a torsionful Omega."""
    R = {(a, b, c, d): Fr(0) for a in R4 for b in R4 for c in R4 for d in R4}
    t = 0
    for (a, b) in LB:
        for (c, d) in LB:
            v = Fr(GENERIC[t])
            t += 1
            R[(a, b, c, d)], R[(b, a, c, d)], R[(a, b, d, c)], R[(b, a, d, c)] = v, -v, -v, v
    return R


def _ricci_t(R):
    """Ric_bd = sum_a eta^aa R_{a d a b} (the contraction the slot equation produces; symmetric when torsion-free)."""
    return [[sum(Fr(ETA[a]) * R[(a, d, a, b)] for a in R4) for d in R4] for b in R4]


def _invariants(R):
    Ric = _ricci_t(R)
    sc = sum(Fr(ETA[b]) * Ric[b][b] for b in R4)
    P = [[(Ric[i][j] - (sc / 6 if i == j else 0) * ETA[i]) / 2 for j in R4] for i in R4]
    G = [[Ric[i][j] - (sc / 2 if i == j else 0) * ETA[i] for j in R4] for i in R4]
    Pm = [[P[a][j] * ETA[j] for j in R4] for a in R4]
    Gm = [[G[a][j] * ETA[a] for j in R4] for a in R4]
    return Ric, sc, Pm, Gm


def _sq(T, U):
    return sum(T[(a, b, c, d)] * U[(a, b, c, d)] * ETA[a] * ETA[b] * ETA[c] * ETA[d]
               for a in R4 for b in R4 for c in R4 for d in R4)


def _gb(R):
    Ric, sc, _, _ = _invariants(R)
    return _sq(R, R) - 4 * sum(Ric[a][b] * Ric[a][b] * ETA[a] * ETA[b] for a in R4 for b in R4) + sc * sc


def _weyl(R):
    _, _, Pm, _ = _invariants(R)
    P = [[Pm[a][j] * ETA[j] for j in R4] for a in R4]
    K = _kn(P, _eta())
    return {k: R[k] - K[k] for k in R}


def _shift(S, a, j, t):
    return [[S[x][y] + (t if (x, y) == (a, j) else 0) for y in R4] for x in R4]


def _grad(fn, S0):
    """Exact derivative along each slot entry for a polynomial of degree <= 4 (five-point stencil)."""
    g = []
    for a in R4:
        for j in R4:
            v = [fn(_shift(S0, a, j, Fr(t))) for t in (-2, -1, 1, 2)]
            g.append((v[0] - 8 * v[1] + 8 * v[2] - v[3]) / 12)
    return [[g[4 * a + j] for j in R4] for a in R4]


def _solve(A, b):
    n = len(A)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            raise ValueError("singular")
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                fct = M[r][c]
                M[r] = [x - fct * y for x, y in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def _unit(i, j, c=Fr(1)):
    return [[c if (a, b) == (i, j) else Fr(0) for b in R4] for a in R4]


def _addm(*Ms):
    return [[sum(M[a][j] for M in Ms) for j in R4] for a in R4]


def _scm(c, M):
    return [[c * M[a][j] for j in R4] for a in R4]


# ---------------------------------------------------------------------------------------------------------


def _premises_field():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")


def check_broken_components_of_the_frozen_point():
    """(i) DI = (rho id - S)(e_a) + beta_a (ninf - rho n0); DX = e_a - beta_a n0 (dilation written beta ninf ^ n0).
    The preservation lemma (DI = 0 iff S = rho id, beta = 0) is not claimed here."""
    _premises_field()
    ok = True
    prints = []
    for rho in RHOS:
        I, V = _frozen(rho)
        ok = ok and _dot(I, I) == 2 * rho and _dot(V, V) == -1 / (2 * rho) and _dot(I, V) == 0
        S = [[Fr(1), Fr(2), Fr(0), Fr(-1)], [Fr(3), Fr(0), Fr(1), Fr(1)],
             [Fr(0), Fr(-2), Fr(5), Fr(1)], [Fr(2), Fr(1), Fr(0), Fr(4)]]
        beta = [Fr(1), Fr(-2), Fr(3), Fr(5, 2)]
        for a in R4:
            th = _theta(S, a, None, beta)
            di = _cp(th, I)
            want = _vec([(rho if j == a else 0) - S[a][j] for j in R4])
            spacetime = {k: v for k, v in di.items() if k[0] < 4}
            ok = ok and GA.is_zero(GA.sub(spacetime, want))
            extra = GA.sub(di, spacetime)
            ok = ok and GA.is_zero(GA.sub(extra, GA.scal(beta[a], GA.sub(NI, GA.scal(rho, N0)))))
            dx = _cp(th, X)
            ok = ok and GA.is_zero(GA.sub(dx, GA.sub(E[a], GA.scal(beta[a], N0))))
            prints.append(sum(k * v for kk, v in di.items() for k in kk) + sum(v for v in dx.values()))
    ok = ok and prints == FINGERPRINT
    GA.check("(i) DI = (rho - S) + beta (ninf - rho n0), DX = frame - beta n0", ok)
    return ok


def check_stelle_west_family_slot_gradient_at_the_frozen_value():
    """(ii) At S = rho id: dL1/dS = 2(G + Lambda), dL3/dS = (G + 2 Lambda)/rho, dL5/dS = (12/rho) id; on the
    line c3 = -2 rho c1, c5 = rho^2 c1 the gradient vanishes for every curvature and the value is GB/4, while
    the density still depends on the slot."""
    _premises_field()
    premise("synthesis.stelle-west-norm-is-no-local-output")
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    R = _curv_tf()
    Ric, sc, Pm, Gm = _invariants(R)
    ok = sc == -154 and all(Ric[a][b] == Ric[b][a] for a in R4 for b in R4)
    for rho in RHOS:
        I, V = _frozen(rho)
        lam = 6 * rho
        S0 = _ident(rho)
        g1 = _grad(lambda S: _L1(R, S, I, V), S0)
        g3 = _grad(lambda S: _L3(R, S, I, V), S0)
        g5 = _grad(lambda S: _L5(S, I, V), S0)
        for a in R4:
            for j in R4:
                d = Fr(1 if a == j else 0)
                ok = ok and g1[a][j] == 2 * (Gm[a][j] + lam * d)
                ok = ok and g3[a][j] == (Gm[a][j] + 2 * lam * d) / rho
                ok = ok and g5[a][j] == 12 * d / rho
        tuned = lambda S: _L1(R, S, I, V) - 2 * rho * _L3(R, S, I, V) + rho * rho * _L5(S, I, V)
        gt = _grad(tuned, S0)
        ok = ok and all(gt[a][j] == 0 for a in R4 for j in R4)
        ok = ok and tuned(S0) == _gb(R) / 4 == -100
        Sr = [[Fr(1), Fr(2), Fr(-1), Fr(0)], [Fr(3), Fr(1, 2), Fr(0), Fr(1)],
              [Fr(0), Fr(-2), Fr(5), Fr(1)], [Fr(2), Fr(1), Fr(0), Fr(-4)]]
        ok = ok and tuned(Sr) != tuned(S0)
        off = lambda S: _L1(R, S, I, V) - 2 * rho * _L3(R, S, I, V) + 2 * rho * rho * _L5(S, I, V)
        ok = ok and any(x != 0 for r in _grad(off, S0) for x in r)
        flat = {k: Fr(0) for k in R}
        f1 = _grad(lambda S: _L1(flat, S, I, V), S0)
        f3 = _grad(lambda S: _L3(flat, S, I, V), S0)
        ok = ok and all(f1[a][j] == (2 * lam if a == j else 0) and f3[a][j] == (2 * lam / rho if a == j else 0)
                        for a in R4 for j in R4)
        Rg = _curv_generic()
        tg = lambda S: _L1(Rg, S, I, V) - 2 * rho * _L3(Rg, S, I, V) + rho * rho * _L5(S, I, V)
        ok = ok and tg(S0) == _L1(Rg, _ident(Fr(0)), I, V)
        ok = ok and all(x == 0 for r in _grad(tg, S0) for x in r)
    GA.check("(ii) Stelle-West family slot gradients 2(G+L), (G+2L)/rho, 12/rho; tuned line Euler-only", ok)
    return ok


def check_stiffness_is_the_slot_hessian_form():
    """(iii) St = Q2(S - rho id) for all S, beta; L1(S) = L1(S*) + Q2(S - S*) with S* the Schouten slot, on a
    basis (complete: both sides quadratic in S), for a torsion-free and a torsionful curvature."""
    _premises_field()
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    premise("synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form")
    ok = True
    for rho in RHOS:
        I, V = _frozen(rho)
        tests = [[[Fr(1), Fr(2), Fr(0), Fr(-1)], [Fr(3), Fr(0), Fr(1), Fr(1)],
                  [Fr(0), Fr(-2), Fr(5), Fr(1)], [Fr(2), Fr(1), Fr(0), Fr(4)]], _ident(rho), _ident(Fr(0))]
        tests += [_addm(_ident(rho), _unit(i, j)) for i in R4 for j in R4]
        tests += [_addm(_ident(rho), _unit(i, j), _unit(k, 3 - k)) for i in R4 for j in R4 for k in (0, 1)
                  if (i, j) != (k, 3 - k)][:20]
        for S in tests:
            M = _addm(S, _ident(-rho))
            for beta in ([Fr(0)] * 4, [Fr(1), Fr(-2), Fr(3), Fr(5, 2)]):
                ok = ok and _stiff(S, I, beta) == _q2(M)
        for R in (_curv_tf(), _curv_generic()):
            _, _, Pm, _ = _invariants(R)
            base = _L1(R, Pm, I, V)
            for S in tests:
                ok = ok and _L1(R, S, I, V) == base + _q2(_addm(S, _scm(-1, Pm)))
        R = _curv_tf()
        ok = ok and _L1(R, _invariants(R)[2], I, V) == _sq(_weyl(R), _weyl(R)) / 4
    # complete: the S-linear term of L1 is bilinear in (R, S); on a basis of curvatures (36) and slots (16)
    # 2 eps(-R, T(S)) = -2 Q2bil(S, S*(R)), Q2bil(A, B) = 2 (trA trB - tr(AB))
    I, V = _frozen(RHOS[0])
    z = _ident(Fr(0))
    Ts = [_F({k: Fr(0) for k in _curv_tf()}, _unit(i, j)) for i in R4 for j in R4]
    nbasis = 0
    for (a, b) in LB:
        for (c, d) in LB:
            Ru = {(p, q, r, s): Fr(0) for p in R4 for q in R4 for r in R4 for s in R4}
            Ru[(a, b, c, d)], Ru[(b, a, c, d)], Ru[(a, b, d, c)], Ru[(b, a, d, c)] = 1, -1, -1, 1
            Fm = _F(Ru, z)
            _, _, Pm, _ = _invariants(Ru)
            for k in range(16):
                i, j = divmod(k, 4)
                lin = sum(s * _eps(I, V, Fm[(p[0], p[1])], Ts[k][(p[2], p[3])]) for p, s in PERMS) / 2
                trP = sum(Pm[x][x] for x in R4)
                q2b = 2 * ((1 if i == j else 0) * trP - Pm[j][i])
                ok = ok and lin == -2 * q2b
            nbasis += 1
    ok = ok and nbasis == 36
    GA.check("(iii) stiffness = Q2(S - rho); L1(S) = L1(Schouten) + Q2(S - Schouten), torsion-free and not", ok)
    return ok


def check_stiffness_interpolates_conformal_gravity_and_the_frozen_functional():
    """(iv) The slot equation of L1 + mu St is solved uniquely by S_mu = (P + mu rho)/(1 + mu); the reduced
    density is (1 - t) W.W/4 + t (GB/4 - (Lambda/3)(sc - 2 Lambda)), t = mu/(1 + mu)."""
    _premises_field()
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    R = _curv_tf()
    _, sc, Pm, _ = _invariants(R)
    W2 = _sq(_weyl(R), _weyl(R))
    ok = True
    vals = []
    for rho in RHOS:
        I, V = _frozen(rho)
        lam = 6 * rho
        mm = _gb(R) / 4 - lam / 3 * (sc - 2 * lam)
        ok = ok and _L1(R, _ident(rho), I, V) == mm
        z = _ident(Fr(0))
        units = [_unit(a, j) for a in R4 for j in R4]

        def quad(fn):
            v0 = fn(z)
            vk = [fn(u) for u in units]
            hs = [[None] * 16 for _ in range(16)]
            for k in range(16):
                for l in range(k, 16):
                    if k == l:
                        hs[k][k] = 2 * (fn(_scm(Fr(2), units[k])) - 2 * vk[k] + v0) / 2
                    else:
                        hs[k][l] = hs[l][k] = fn(_addm(units[k], units[l])) - vk[k] - vk[l] + v0
            return v0, [vk[k] - v0 - hs[k][k] / 2 for k in range(16)], hs
        _, l1g, l1h = quad(lambda S: _L1(R, S, I, V))
        _, stg, sth = quad(lambda S: _stiff(S, I, [Fr(0)] * 4))
        for mu in (Fr(0), Fr(1), Fr(3), Fr(-1, 2)):
            dens = lambda S: _L1(R, S, I, V) + mu * _stiff(S, I, [Fr(0)] * 4)
            hT = [[l1h[k][l] + mu * sth[k][l] for l in range(16)] for k in range(16)]
            sol = _solve(hT, [-(l1g[k] + mu * stg[k]) for k in range(16)])
            want = [(Pm[b][k] + mu * (rho if b == k else 0)) / (1 + mu) for b in R4 for k in R4]
            ok = ok and sol == want
            t = mu / (1 + mu)
            Smu = [[want[4 * b + k] for k in R4] for b in R4]
            red = dens(Smu)
            ok = ok and red == (1 - t) * W2 / 4 + t * mm
            vals.append(red)
    GA.check("(iv) stiffness family: S_mu = (P + mu rho)/(1 + mu), density (1 - t) W.W/4 + t MM", ok)
    return ok and vals[0] == W2 / 4


def check_frame_equation_is_the_frozen_slot_equation():
    """(v) With Omega fixed and the slot tied to the frame (S = rho H), dL1/dH at H = id is 2 rho dL1/dS at
    S = rho id, i.e. 4 rho (G + Lambda); with the prefactor 1/Q(I) = 1/(2 rho) it is the stored 2(G + Lambda)."""
    _premises_field()
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    R = _curv_tf()
    _, _, _, Gm = _invariants(R)
    ok = True
    for rho in RHOS:
        I, V = _frozen(rho)
        lam = 6 * rho
        gS = _grad(lambda S: _L1(R, S, I, V), _ident(rho))
        gH = _grad(lambda H: _L1(R, _scm(rho, H), I, V, H), _ident(Fr(1)))
        for a in R4:
            for j in R4:
                d = Fr(1 if a == j else 0)
                ok = ok and gH[a][j] == 2 * rho * gS[a][j]
                ok = ok and gH[a][j] / _dot(I, I) == 2 * (Gm[a][j] + lam * d)
    GA.check("(v) frame gradient = 2 rho x slot gradient; over Q(I): 2(G + Lambda)", ok)
    return ok


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("check_") and callable(fn):
            print(name, fn())


# ---------------------------------------------------------------------------
# GTG proof (2026-11-07): the readings of the index expressions as maps of the curvature operator
# calR(A ^ B) = sum_{a<b} R^{ab}_{ef} gamma_a ^ gamma_b on the frame planes (store sign; no pair symmetry
# assumed): the Ricci map calR(b) = d_a . calR(a ^ b) is the contraction Ric_bd = sum_a eta^aa R_adab also with
# torsion; Schouten and Einstein maps; (1/4) W_abcd W^abcd = (1/2) <W(a ^ b) W(d_b ^ d_a)>; the Euler density
# 2 <calR(a ^ b) calR(d_b ^ d_a)> - 4 calR(d_a) . calR(a) + calR^2; the slot derivative as the map D with
# dL = tr(D o dS) = d_a . D(dS(a)), so that at the frozen slot D = 2 (calG + Lambda id); Q2 by GA traces.
# ---------------------------------------------------------------------------
import gtg  # noqa: E402

GTG_M = [[Fr(1), Fr(2), Fr(0), Fr(-1)], [Fr(3), Fr(0), Fr(1), Fr(1)], [Fr(0), Fr(-2), Fr(5), Fr(1)],
         [Fr(2), Fr(1), Fr(0), Fr(4)]]


def _op(R):
    return {(e, f): _rbiv(R, e, f) for (e, f) in LB}


def _lin_map(M):
    return lambda a: gtg.m_add(*[gtg.m_scal(c * M[i][j], gtg.e(j)) for (i,), c in a.items() for j in R4 if M[i][j]])


def _ga_trace(f):
    return sum((gtg.vdot(gtg.er(a), f(gtg.e(a))) for a in R4), Fr(0))


def check_gtg_readings_of_the_curvature_operator():
    _premises_field()
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    ok = True
    for R in (_curv_tf(), _curv_generic()):
        op = _op(R)
        Ric, sc, Pm, Gm = _invariants(R)
        ok = ok and all(gtg.vdot(gtg.e(d), gtg.ricci(op, gtg.e(b))) == Ric[b][d] for b in R4 for d in R4)
        ok = ok and gtg.ricci_scalar(op) == sc
        P = gtg.schouten(op)
        ok = ok and all(gtg.m_val(P(gtg.e(a))).get((j,), Fr(0)) == Pm[a][j] for a in R4 for j in R4)
    R = _curv_tf()
    op = _op(R)
    _, sc, Pm, Gm = _invariants(R)
    ok = ok and _sq(_weyl(R), _weyl(R)) / 4 == gtg.kretschmann(gtg.weyl_op(op)) / 4 != 0
    ok = ok and _gb(R) == 2 * sum((gtg.sp(gtg.m_mul(gtg.apply_op(op, gtg.wedge(gtg.e(a), gtg.e(b))),
                                                    gtg.apply_op(op, gtg.wedge(gtg.er(b), gtg.er(a)))))
                                   for a in R4 for b in R4 if a != b), Fr(0)) - 4 * gtg.ricci_sq(op) + sc * sc
    M = _lin_map(GTG_M)
    ok = ok and _q2(GTG_M) == 2 * (_ga_trace(M) ** 2 - _ga_trace(lambda a: M(M(a))))
    for rho in RHOS:
        I, V = _frozen(rho)
        lam = 6 * rho
        # L1 at the Schouten slot is the Weyl square; at the frozen slot Euler/4 - (Lambda/3)(calR - 2 Lambda)
        ok = ok and _L1(R, Pm, I, V) == gtg.kretschmann(gtg.weyl_op(op)) / 4
        ok = ok and _L1(R, _ident(rho), I, V) == gtg.euler_density(op) / 4 - lam / 3 * (gtg.ricci_scalar(op) - 2 * lam)
        # the slot derivative as the map 2 (calG + Lambda id): dL1 = 2 d_a . (calG + Lambda)(dS(a))
        g1 = _grad(lambda S: _L1(R, S, I, V), _ident(rho))
        for a in R4:
            for j in R4:
                want = 2 * (Fr(ETA[a]) * gtg.vdot(gtg.e(a), gtg.einstein(op, gtg.e(j))) + (lam if a == j else 0))
                ok = ok and g1[a][j] == want
    GA.check("GTG readings: Ricci map with torsion, Weyl square, Euler density, Q2, slot derivative 2(calG + Lambda)", ok)
    return ok


# The formal's GA forms against its index readings (Leon's answers, second round, item 7).
TS = (Fr(0), Fr(1, 3), Fr(-2, 5), Fr(1))


def _ga_half_sq(op):
    """(1/2) <W(a ^ b) W(d_b ^ d_a)> written out over the frame."""
    tot = Fr(0)
    for a in R4:
        for b in R4:
            if a != b:
                tot += gtg.sp(gtg.m_mul(gtg.apply_op(op, gtg.wedge(gtg.e(a), gtg.e(b))),
                                        gtg.apply_op(op, gtg.wedge(gtg.er(b), gtg.er(a)))))
    return tot / 2


def check_gtg_formal_forms_equal_their_index_readings():
    """Setting: the GA Weyl map W(a ^ b) = calR(a ^ b) - P*(a) ^ b - a ^ P*(b) is, plane by plane, the index
    W = R - KN(P*) for torsion-free Omega (with torsion it is R - KN of the transposed Schouten matrix; the formal
    uses the Weyl part only torsion-free). (iii)-(iv): (1/2) <W(a ^ b) W(d_b ^ d_a)> = (1/4) W_abcd W^abcd,
    calR(d_a) . calR(a) = R_ab R^ab, and the GA display of (iv), (1 - t)(1/2) <W W> + t((1/4) E - (Lambda/3)(calR - 2 Lambda)),
    E = 2 <calR calR> - 4 calR(d_a) . calR(a) + calR^2, equals the index display and (1 - t) L1(P*) + t L1(rho id)
    at four t and two rho."""
    _premises_field()
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    ok = True
    R = _curv_tf()
    Wga, Wix = gtg.weyl_op(_op(R)), _op(_weyl(R))
    ok = ok and all(gtg.m_sub(Wga[pl], Wix[pl]) == {} for pl in LB)
    # with torsion (no pair symmetry) the GA form is R - KN of the transposed Schouten matrix in this index
    # convention, and differs from R - KN(P*): the formal uses the Weyl part only for torsion-free Omega
    R = _curv_generic()
    _, _, Pm, _ = _invariants(R)
    P = [[Pm[a][j] * ETA[j] for j in R4] for a in R4]
    for PP, same in ((P, False), ([list(x) for x in zip(*P)], True)):
        K = _kn(PP, _eta())
        Wix = _op({k: R[k] - K[k] for k in R})
        Wga = gtg.weyl_op(_op(R))
        ok = ok and all(gtg.m_sub(Wga[pl], Wix[pl]) == {} for pl in LB) == same
    R = _curv_tf()
    op = _op(R)
    Ric, sc, Pm, _ = _invariants(R)
    W = _weyl(R)
    half = _ga_half_sq(gtg.weyl_op(op))
    ok = ok and half == _sq(W, W) / 4 != 0
    ric2 = sum(Ric[a][b] * Ric[a][b] * ETA[a] * ETA[b] for a in R4 for b in R4)
    ok = ok and gtg.ricci_sq(op) == ric2 != 0
    E_ga = 4 * _ga_half_sq(op) - 4 * gtg.ricci_sq(op) + gtg.ricci_scalar(op) ** 2
    ok = ok and gtg.ricci_scalar(op) == sc != 0
    for rho in RHOS:
        I, V = _frozen(rho)
        lam = 6 * rho
        for t in TS:
            ga = (1 - t) * half + t * (E_ga / 4 - lam / 3 * (gtg.ricci_scalar(op) - 2 * lam))
            ix = (1 - t) * _sq(W, W) / 4 + t * ((_sq(R, R) - 4 * ric2 + sc * sc) / 4 - lam / 3 * (sc - 2 * lam))
            ok = ok and ga == ix == (1 - t) * _L1(R, Pm, I, V) + t * _L1(R, _ident(rho), I, V)
    GA.check("GTG forms of the formal = their index readings: Weyl map, Weyl square, Ric^2, the interpolated density", ok)
    return ok
