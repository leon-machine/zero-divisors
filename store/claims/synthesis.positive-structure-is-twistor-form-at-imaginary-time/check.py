"""synthesis.positive-structure-is-twistor-form-at-imaginary-time: exact checks.

Model: the eight-dimensional Fock module of Cl(2,4) of synthesis.incidence-vacua-thermofield-real-capacity,
three modes in the Jordan-Wigner basis, ground generators e1 (square +1, the time direction t),
e2, e3, e4 (square -1), ascent plane e+ (+1), e- (-1); the positive Hermitian structure h is the identity
Gram matrix, for which every generator is unitary; nO = (e+ + e-)/2, ninf = e+ - e-,
X(m) = nO + m - Q(m) ninf / 2. J = i e1 e+, Sigma = h(., J .).
Exact Gaussian rationals (GA.QI) throughout.
"""
from fractions import Fraction as F

import GA as g
import fock
from tp_premise import premise

Z = g.QI(0)
ONE = g.QI(1)
IU = g.QI(0, 1)
N = 8


def zeros(n=N):
    return [[g.QI(0) for _ in range(n)] for _ in range(n)]


def eye(n=N):
    M = zeros(n)
    for i in range(n):
        M[i][i] = g.QI(1)
    return M


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def ms(c, A):
    c = c if isinstance(c, g.QI) else g.QI(c)
    return [[c * x for x in r] for r in A]


def mm(A, B):
    return g.field_mat_mul(A, B)


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(len(v))), Z) for i in range(len(M))]


CR = [[[g.QI(x) for x in r] for r in fock.to_dense(fock.cre(j, 3), N)] for j in range(3)]   # Jordan-Wigner, LSB
AN = [dag(c) for c in CR]
HERM = []
for _j in range(3):
    HERM.append(madd(CR[_j], AN[_j]))
    HERM.append(ms(IU, madd(CR[_j], ms(-1, AN[_j]))))
GEN = {"e1": HERM[0], "e2": ms(IU, HERM[1]), "e3": ms(IU, HERM[2]), "e4": ms(IU, HERM[3]),
       "ep": HERM[4], "em": ms(IU, HERM[5])}
SQ = {"e1": 1, "e2": -1, "e3": -1, "e4": -1, "ep": 1, "em": -1}
NAMES = ["e1", "e2", "e3", "e4", "ep", "em"]
J = ms(IU, mm(GEN["e1"], GEN["ep"]))
NO = ms(g.QI(F(1, 2)), madd(GEN["ep"], GEN["em"]))
NINF = madd(GEN["ep"], ms(-1, GEN["em"]))
BIV = [mm(GEN[a], GEN[b]) for i, a in enumerate(NAMES) for b in NAMES[i + 1:]]
_G = eye()
for _a in NAMES:
    _G = mm(_G, GEN[_a])
GAMMA = ms(IU, _G)                      # chirality: GAMMA^2 = 1 (checked)
PPLUS = ms(g.QI(F(1, 2)), madd(eye(), GAMMA))


def span_basis(vectors):
    out = []
    for v in vectors:
        if any(x != Z for x in v) and g.field_rank(out + [v]) > len(out):
            out.append(v)
    return out


HALF = span_basis([[PPLUS[i][j] for i in range(N)] for j in range(N)])


def vec(coef):
    M = zeros()
    for a, c in coef.items():
        M = madd(M, ms(c, GEN[a]))
    return M


def Qm(coef):
    return sum((coef.get(a, Z) * coef.get(a, Z) * g.QI(SQ[a]) for a in ["e1", "e2", "e3", "e4"]), Z)


def X_of(m):
    return madd(madd(NO, vec(m)), ms(g.QI(F(-1, 2)) * Qm(m), NINF))


def line(m, basis=None):
    """incidence line: vacua of X(m) in the chirality half."""
    basis = HALF if basis is None else basis
    X = X_of(m)
    images = [apply(X, b) for b in basis]
    Mt = [[images[j][i] for j in range(len(basis))] for i in range(N)]
    ker = g.field_kernel(Mt)
    return [[sum((k[j] * basis[j][i] for j in range(len(basis))), Z) for i in range(N)] for k in ker]


def sigma(u, v):
    Jv = apply(J, v)
    return sum((u[i].conj() * Jv[i] for i in range(N)), Z)


def gram(A, B):
    return [[sigma(a, b) for b in B] for a in A]


def q(re, im=0):
    return g.QI(F(re), F(im))


def hermitian_invariant_dim(mats, basis_dim, mode):
    """Real dimension of Hermitian M (basis_dim x basis_dim) with
    mode 'unitary': R^dag M R = M for every R in mats;  mode 'anti': R^dag M + M R = 0."""
    n = basis_dim
    idx = {}
    for p in range(n):
        for r in range(n):
            idx[(p, r, 0)] = len(idx)
            idx[(p, r, 1)] = len(idx)
    nv = len(idx)
    rows = []

    def push(terms):
        re = [F(0)] * nv
        im = [F(0)] * nv
        for c, p, r in terms:
            re[idx[(p, r, 0)]] += c.re
            re[idx[(p, r, 1)]] -= c.im
            im[idx[(p, r, 0)]] += c.im
            im[idx[(p, r, 1)]] += c.re
        rows.append(re)
        rows.append(im)

    for R in mats:
        for p in range(n):
            for r in range(n):
                terms = []
                if mode == "anti":
                    for k in range(n):
                        terms.append((R[k][p].conj(), k, r))
                        terms.append((R[k][r], p, k))
                else:
                    for k in range(n):
                        for l in range(n):
                            c = R[k][p].conj() * R[l][r]
                            if c != Z:
                                terms.append((c, k, l))
                    terms.append((g.QI(-1), p, r))
                push(terms)
    for p in range(n):
        for r in range(n):
            re = [F(0)] * nv
            im = [F(0)] * nv
            re[idx[(p, r, 0)]] += 1
            re[idx[(r, p, 0)]] -= 1
            im[idx[(p, r, 1)]] += 1
            im[idx[(r, p, 1)]] += 1
            rows.append(re)
            rows.append(im)
    return len(g.field_kernel(rows))


def restrict(X, basis):
    """matrix of X on span(basis) (X must preserve it)."""
    k = len(basis)
    Mt = [[basis[j][i] for j in range(k)] for i in range(N)]
    rows = span_basis_rows(Mt)
    out = []
    for b in basis:
        img = apply(X, b)
        c = g.field_solve([Mt[r][:] for r in rows], [img[r] for r in rows])
        assert all(sum((Mt[i][j] * c[j] for j in range(k)), Z) == img[i] for i in range(N))
        out.append(c)
    return [[out[j][i] for j in range(k)] for i in range(k)]


def span_basis_rows(Mt):
    rows = []
    for i in range(len(Mt)):
        if g.field_rank([Mt[r] for r in rows] + [Mt[i]]) > len(rows):
            rows.append(i)
    return rows


def check_positive_structure_is_polarised_at_imaginary_time():
    premise("synthesis.incidence-vacua-thermofield-real-capacity")
    premise("one-relation.spacetime-manifold-vacuum-lines")
    for a in NAMES:
        g.check(a + " squares to its sign", meq(mm(GEN[a], GEN[a]), ms(SQ[a], eye())))
        g.check(a + " unitary for h", meq(mm(dag(GEN[a]), GEN[a]), eye()))
        for b in NAMES:
            if NAMES.index(a) < NAMES.index(b):
                g.check(a + b + " anticommute", meq(madd(mm(GEN[a], GEN[b]), mm(GEN[b], GEN[a])), zeros()))
    # the positive structure with every generator unitary is unique up to a positive factor
    g.check("generator-unitary Hermitian forms: one real line",
            hermitian_invariant_dim([GEN[a] for a in NAMES], N, "unitary") == 1)
    g.check("J^2 = 1", meq(mm(J, J), eye()))
    g.check("J h-Hermitian", meq(dag(J), J))
    g.check("GAMMA^2 = 1", meq(mm(GAMMA, GAMMA), eye()))
    g.check("J even", meq(mm(J, GAMMA), mm(GAMMA, J)))
    # X(i e1) = e+ (1 - J), X(-i e1) = e+ (1 + J)
    Xp = X_of({"e1": q(0, 1)})
    Xm_ = X_of({"e1": q(0, -1)})
    g.check("X(i e1) = e+(1 - J)", meq(Xp, mm(GEN["ep"], madd(eye(), ms(-1, J)))))
    g.check("X(-i e1) = e+(1 + J)", meq(Xm_, mm(GEN["ep"], madd(eye(), J))))
    Lp, Lm = line({"e1": q(0, 1)}), line({"e1": q(0, -1)})
    g.check("lines of +-i e1 are planes", len(Lp) == 2 and len(Lm) == 2)
    g.check("J = +1 on L(i e1)", all(apply(J, v) == v for v in Lp))
    g.check("J = -1 on L(-i e1)", all(apply(J, v) == [-x for x in v] for v in Lm))
    g.check("half = L(i e1) + L(-i e1)", g.field_rank(Lp + Lm) == 4)
    # h = Sigma on L(i e1), h = -Sigma on L(-i e1)
    hp = [[sum((a[i].conj() * b[i] for i in range(N)), Z) for b in Lp] for a in Lp]
    hm = [[sum((a[i].conj() * b[i] for i in range(N)), Z) for b in Lm] for a in Lm]
    g.check("h = Sigma on L(i e1)", meq(hp, gram(Lp, Lp)))
    g.check("h = -Sigma on L(-i e1)", meq(hm, ms(-1, gram(Lm, Lm))))
    g.check("L(i e1) and L(-i e1) Sigma-orthogonal", all(x == Z for r in gram(Lp, Lm) for x in r))
    return True


def check_sigma_is_the_twistor_form():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    g.check("Sigma Hermitian", meq(dag(J), J))
    for X in BIV:
        g.check("bivector Sigma-anti-Hermitian", meq(madd(mm(dag(X), J), mm(J, X)), zeros()))
    # signature (2,2) on the half: J = +1 on a plane, -1 on a plane
    plus = span_basis([apply(madd(eye(), J), v) for v in HALF])
    minus = span_basis([apply(madd(eye(), ms(-1, J)), v) for v in HALF])
    g.check("signature (2,2) on the half", len(plus) == 2 and len(minus) == 2)
    # uniqueness: invariant Hermitian forms on the half form one real line
    R = [restrict(X, HALF) for X in BIV]
    g.check("invariant Hermitian forms on the half: one real line", hermitian_invariant_dim(R, 4, "anti") == 1)
    return True


TUBE = [({"e1": q(0, 1)}, 1), ({"e1": q(0, -1)}, -1),
        ({"e2": q(F(1, 2)), "e1": q(0, 2), "e3": q(0, 1)}, 1),
        ({"e2": q(1), "e3": q(3), "e1": q(0, 3), "e4": q(0, 2)}, 1),
        ({"e2": q(1), "e1": q(0, -2), "e4": q(0, 1)}, -1),
        ({"e2": q(1), "e1": q(0, 1), "e3": q(0, 2)}, 0),
        ({"e2": q(1), "e3": q(3)}, None)]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def check_tube_points_polarise_sigma():
    premise("correspondence.incidence-relation-chart")
    premise("synthesis.twistor-form-states-only-off-the-real-slice")
    premise("correspondence.reality-conjugation-twistor-form-factor")
    # the Sigma-adjoint of every real vector is minus itself
    for a in NAMES:
        g.check(a + "# = -" + a, meq(mm(J, mm(dag(GEN[a]), J)), ms(-1, GEN[a])))
    # the line at infinity: vacua of ninf in the half, Sigma-null, skew to every affine incidence line
    images = [apply(NINF, b) for b in HALF]
    kinf = g.field_kernel([[images[j][i] for j in range(4)] for i in range(N)])
    Linf = [[sum((k[j] * HALF[j][i] for j in range(4)), Z) for i in range(N)] for k in kinf]
    g.check("line at infinity is a plane", len(Linf) == 2)
    g.check("line at infinity Sigma-null", all(x == Z for r in gram(Linf, Linf) for x in r))
    for m, kind in TUBE:
        g.check("affine line skew to the line at infinity", g.field_rank(line(m) + Linf) == 4)
        X = X_of(m)
        g.check("X(m) null", meq(mm(X, X), zeros()))
        g.check("X(m) of rank four (ker = im)", g.field_rank(X) == 4)
        L = line(m)
        mbar = {a: c.conj() for a, c in m.items()}
        Lb = line(mbar)
        g.check("lines are planes", len(L) == 2 and len(Lb) == 2)
        g.check("Sigma(L(m), L(mbar)) = 0", all(x == Z for r in gram(L, Lb) for x in r))
        G = gram(L, L)
        d, t = det2(G), G[0][0] + G[1][1]
        # basis-free ratio det(Sigma|L) / det(h|L) = 4 Q(y) / (|1 - Q(m)|^2 + 4 |m^1|^2 - 4 Q(y))
        Hg = [[sum((a[i].conj() * b[i] for i in range(N)), Z) for b in L] for a in L]
        y = {a: g.QI(c.im) for a, c in m.items()}
        Qy, Qmm, m1 = Qm(y), Qm(m), m.get("e1", Z)
        one_minus = g.QI(1) - Qmm
        den = one_minus * one_minus.conj() + g.QI(4) * m1 * m1.conj() - g.QI(4) * Qy
        g.check("Gram ratio formula", d / det2(Hg) == g.QI(4) * Qy / den)
        if kind == 1:
            g.check("future tube point: Sigma positive on L(m)", d.re > 0 and t.re > 0 and d.im == 0)
            g.check("future tube point: L(m) + L(mbar) is the half", g.field_rank(L + Lb) == 4)
        elif kind == -1:
            g.check("past tube point: Sigma negative on L(m)", d.re > 0 and t.re < 0)
        elif kind == 0:
            g.check("spacelike imaginary part: split line", d.re < 0)
        else:
            g.check("real point: null line", all(x == Z for r in G for x in r))
    # imaginary boost of the real point e2: x(theta) = cos e2 + i sin e1, at (cos, sin) = (3/5, 4/5) and (0, 1)
    for c, s in [(F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)), (F(0), F(1))]:
        L = line({"e2": q(c), "e1": q(0, s)})
        G = gram(L, L)
        g.check("upper half strip positive", det2(G).re > 0 and (G[0][0] + G[1][1]).re > 0)
    Lmid = line({"e1": q(0, 1)})
    g.check("midpoint of the strip is the centre i e1", all(apply(J, v) == v for v in Lmid))
    return True


def check_no_state_for_an_indefinite_form():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    # Sigma-orthonormal basis of the half: from L(i e1) (+) and L(-i e1) (-), Gram-Schmidt in Sigma
    Lp, Lm = line({"e1": q(0, 1)}), line({"e1": q(0, -1)})
    basis, eps = [], []
    for v in Lp + Lm:
        w = v[:]
        for b, e in zip(basis, eps):
            c = sigma(b, w) / g.QI(e)
            w = [w[i] - c * b[i] for i in range(N)]
        nrm = sigma(w, w)
        g.check("Sigma-norm rational and nonzero", nrm.im == 0 and nrm.re != 0)
        basis.append(w)
        eps.append(nrm.re)
    g.check("both signs occur", any(e > 0 for e in eps) and any(e < 0 for e in eps))
    g.check("Sigma-norms of the basis are 2, 2, -2, -2", eps == [2, 2, -2, -2])
    # matrix units E_ij f_k = delta_jk f_i; Sigma-adjoint E_ij^# = (eps_i/eps_j)... check E_ij^# E_ij = (eps_i/eps_j) E_jj
    for i in range(4):
        for j in range(4):
            # in the f-basis: E_ij = unit matrix; Sigma Gram = diag(eps); adjoint A# = G^{-1} A^dag G
            Gd = [[g.QI(eps[r]) if r == s else Z for s in range(4)] for r in range(4)]
            Gi = [[g.QI(1 / eps[r]) if r == s else Z for s in range(4)] for r in range(4)]
            E = [[ONE if (r == i and s == j) else Z for s in range(4)] for r in range(4)]
            Esh = mm(Gi, mm(dag(E), Gd))
            prod = mm(Esh, E)
            Ejj = [[ONE if (r == j and s == j) else Z for s in range(4)] for r in range(4)]
            g.check("E#E = (eps_i/eps_j) E_jj", meq(prod, ms(g.QI(eps[i] / eps[j]), Ejj)))
    # positivity on E_ij^# E_ij for i of both signs forces omega(E_jj) = 0, so omega(1) = sum = 0
    for j in range(4):
        signs = {(eps[i] / eps[j]) > 0 for i in range(4)}
        g.check("both signs multiply omega(E_jj)", signs == {True, False})
    # a boost generator squares to +1 and is not a scalar: real eigenvalues e^(+-theta/2), never unitary
    B = mm(GEN["e1"], GEN["e2"])
    g.check("(e1 e2)^2 = 1", meq(mm(B, B), eye()))
    g.check("e1 e2 is not +-1", not meq(B, eye()) and not meq(B, ms(-1, eye())))
    return True
