"""On the tractor gauge field of a torsion-free field the frozen-point integrand is a quarter Weyl square.

Cl(2,4) with orthonormal generators e0..e5, squares (+,-,-,-,+,-); e0..e3 the spacetime vectors in the
store signature, n0 = (e4 + e5)/2, ninf = e4 - e5 (n0 . ninf = 1, both null; the chart of the stored check of
the frozen-point Stelle-West theorem), so n0 ^ ninf = -e4 e5, and the orientation is I6 = e0 e1 e2 e3 e4 e5. eps(a, b, F, G) is the coefficient of that pseudoscalar in
a ^ b ^ F ^ G (vectors a, b; bivectors F, G). A bivector-valued two-form F has frame components F_{ef}
(e < f); the 4-form value of a bilinear pairing B on F ^ G is 1/4 sum over permutations p of 0123 of
sign(p) B(F_{p0 p1}, G_{p2 p3}), the coefficient of e^0 ^ e^1 ^ e^2 ^ e^3.
X = n0 is the canonical tractor; the frozen point I = ninf + (Lambda/6) n0, V = X - (3/Lambda) I.
Curvature tensors R_{abcd} (orthonormal, indices down) are sums of Kulkarni-Nomizu products of fixed
rational symmetric matrices; W is the Weyl part, R - KN(P, eta) with P the Schouten tensor.
(1) The tractor field strength of a torsion-free field, Lorentz block -W and n0 block the Cotton term
    (stored GTG tractor theorem (iv)), satisfies F . X = 0; a torsion (ninf) block breaks it.
(2) On bivectors with F . X = 0, eps_X(F, G) := eps(Y, X, F, G)/(X . Y) does not depend on Y (X fixed);
    off that locus it does. Hence eps(I, V, F, F) = eps(I, X, F, F) = (X . I) eps_X(F, F) for every tractor I
    and Lambda.
(3) eps_X(F, F) = (1/4) W_abcd W^abcd: the bilinear identity on a basis of the ten-dimensional Weyl
    space (complete), and with an arbitrary Cotton block (the Cotton block drops out).
(4) The invariant bilinear forms on Lambda^2(X^perp) under the stabiliser of X: symmetric dimension 2,
    spanned by K = <FG>_0 and eps_X; antisymmetric dimension 0; eps_X is odd and K even under the
    internal reflection in e1 (spacetime orientation fixed). For contrast so(2,4) has one symmetric invariant form and so(1,3) two.
(5) The frame-leg pairings K(e ^ e, F) and eps_X(e ^ e, F) vanish on the Weyl block, on all ten basis
    Weyl tensors (complete, both are linear in W), and not on a general curvature.
(6) Not topological: on S^2(K1) x S^2(K2) (Riemannian) the Weyl-square integral over 16 pi^2 is
    (4/3)(K1 + K2)^2/(K1 K2), which changes with K2/K1, while the Euler integral over 16 pi^2 is 8.
(7) The Chern form is exact: <F ^ F>_0 = d CS(A), CS = <A ^ dA> + (1/3)<A ^ (A x A)>, on a fixed
    2-jet of a so(2,4) connection.
(8) The proof's GTG route: ten independent Weyl maps of Cl(1,3) as linear functions on bivectors (lib/gtg.py,
    Weyl parts of Kulkarni-Nomizu operators), eps_X(F1, F2) = (1/2) <W1(a ^ b) W2(d_b ^ d_a)> on all 55 pairs;
    the S^2 x S^2 densities pointwise from the product operator of Cl(4,0).
Exact arithmetic only (Fractions); fixed tables, no randomness.
"""
from fractions import Fraction as Fr
from itertools import combinations, permutations
import GA
from tp_premise import premise
import gtg

SQ = (1, -1, -1, -1, 1, -1)
ETA = (1, -1, -1, -1)
R4 = range(4)
PS = (0, 1, 2, 3, 4, 5)


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


E = [GA.gen(i) for i in range(6)]
N0 = GA.scal(Fr(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
X = N0


def _eps(a, b, F, G):
    if not F or not G:
        return Fr(0)
    return _wedge(a, b, F, G).get(PS, Fr(0))


def _sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def _form(Fc, Gc, pair):
    tot = Fr(0)
    for p in permutations(range(4)):
        tot += _sign(p) * pair(Fc(p[0], p[1]), Gc(p[2], p[3]))
    return tot / 4


def _kn(h, k):
    return {(a, b, c, d): h[a][c] * k[b][d] + h[b][d] * k[a][c] - h[a][d] * k[b][c] - h[b][c] * k[a][d]
            for a in R4 for b in R4 for c in R4 for d in R4}


def _eta_mat(sig):
    return [[Fr(sig[i]) if i == j else Fr(0) for j in R4] for i in R4]


def _basis_sym():
    out = []
    for i in R4:
        for j in range(i, 4):
            M = [[Fr(0)] * 4 for _ in R4]
            M[i][j] = M[j][i] = Fr(1)
            out.append(M)
    return out


def _ricci(R, sig):
    return [[sum(Fr(sig[a]) * R[(a, b, a, d)] for a in R4) for d in R4] for b in R4]


def _weyl(R, sig=ETA):
    Ric = _ricci(R, sig)
    sc = sum(Fr(sig[b]) * Ric[b][b] for b in R4)
    eta = _eta_mat(sig)
    P = [[(Ric[i][j] - sc / 6 * eta[i][j]) / 2 for j in R4] for i in R4]
    PK = _kn(P, eta)
    return {k: R[k] - PK[k] for k in R}


def _sq(T, U, sig=ETA):
    return sum(T[(a, b, c, d)] * U[(a, b, c, d)] * sig[a] * sig[b] * sig[c] * sig[d]
               for a in R4 for b in R4 for c in R4 for d in R4)


TABLE = [[[2, 1, 0, -3], [1, -1, 4, 0], [0, 4, 5, 2], [-3, 0, 2, 7]],
         [[1, 0, 1, 0], [0, -5, 0, 1], [1, 0, 2, 0], [0, 1, 0, 3]],
         [[0, 2, -1, 1], [2, 3, 0, 0], [-1, 0, -2, 4], [1, 0, 4, 1]]]


def _curv(i, j):
    h = [[Fr(x) for x in r] for r in TABLE[i]]
    k = [[Fr(x) for x in r] for r in TABLE[j]]
    return _kn(h, k)


def _sample_weyls():
    out = []
    for (i, j) in ((0, 1), (1, 2), (0, 2)):
        R = _curv(i, j)
        R2 = _curv(j, j)
        out.append(_weyl({k: R[k] + R2[k] for k in R}))
    return out


COTTON = [[Fr(3), Fr(-1), Fr(2), Fr(0)], [Fr(1, 2), Fr(4), Fr(-3), Fr(1)],
          [Fr(0), Fr(2), Fr(5), Fr(-2)], [Fr(-1), Fr(1), Fr(1, 3), Fr(2)]]


def _lorentz_block(T, e, f):
    out = {}
    for a in R4:
        for b in range(a + 1, 4):
            c = T[(a, b, e, f)] * ETA[a] * ETA[b]
            if c:
                out = GA.add(out, GA.scal(c, _wedge(E[a], E[b])))
    return out


def _tractor_F(W, C=None, torsion=None):
    """Frame component F_{ef} of the tractor field strength: -W, plus n0 ^ (Cotton), plus ninf ^ (torsion)."""
    def Fc(e, f):
        if e == f:
            return {}
        out = GA.neg(_lorentz_block(W, e, f))
        if C is not None:
            c = {}
            for a in R4:
                c = GA.add(c, GA.scal(C[e][a] - C[f][a], E[a]))
            out = GA.add(out, _wedge(N0, c))
        if torsion is not None:
            out = GA.add(out, GA.scal(torsion[e] - torsion[f], _wedge(NI, E[(e + f) % 4])))
        return out
    return Fc


def _eps_X(Fc, Gc, Y=NI):
    return _form(Fc, Gc, lambda F, G: _eps(Y, X, F, G)) / _dot(X, Y)


def _premises_locus():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("synthesis.imported-gtg-dictionary")


def _run_tractor_field_strength_of_torsion_free_field_annihilates_x():
    _premises_locus()
    ok, ncomp = True, 0
    for W in _sample_weyls():
        ok = ok and any(v != 0 for v in W.values())
        ok = ok and all(x == 0 for r in _ricci(W, ETA) for x in r)
        Fc = _tractor_F(W, COTTON)
        for e in R4:
            for f in R4:
                if e != f:
                    ok = ok and GA.is_zero(GA.sub(_m(Fc(e, f), X), _m(X, Fc(e, f))))
                    ncomp += 1
        Ft = _tractor_F(W, COTTON, torsion=[Fr(1), Fr(-2), Fr(3), Fr(1, 2)])
        ok = ok and not GA.is_zero(GA.sub(_m(Ft(0, 1), X), _m(X, Ft(0, 1))))
    return ok, ncomp


def _run_eps_contraction_is_independent_of_the_second_vector_on_the_locus():
    _premises_locus()
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ys = [NI, GA.add(NI, GA.scal(3, E[1]), GA.scal(Fr(-2, 5), E[0]), GA.scal(7, N0)),
          GA.scal(Fr(2), GA.add(NI, E[2], GA.scal(Fr(1, 3), E[3])))]
    ok, found = True, []
    for W in _sample_weyls():
        Fc = _tractor_F(W, COTTON)
        vals = [_eps_X(Fc, Fc, Y) for Y in ys]
        found.append(vals[0])
        ok = ok and vals[0] != 0 and vals[0] == vals[1] == vals[2]
        for lam in (Fr(3), Fr(-3), Fr(9, 7)):
            I = GA.add(NI, GA.scal(lam / 6, N0))
            V = GA.sub(X, GA.scal(3 / lam, I))
            ok = ok and _dot(I, I) == lam / 3 and _dot(V, V) == -3 / lam and _dot(I, V) == 0
            eIV = _form(Fc, Fc, lambda F, G: _eps(I, V, F, G))
            eIX = _form(Fc, Fc, lambda F, G: _eps(I, X, F, G))
            ok = ok and eIV == eIX == _dot(X, I) * vals[0]
        Ig = GA.add(GA.scal(Fr(5, 2), NI), E[1], GA.scal(Fr(-4), N0))
        ok = ok and _form(Fc, Fc, lambda F, G: _eps(Ig, X, F, G)) == Fr(5, 2) * vals[0]
        Ft = _tractor_F(W, COTTON, torsion=[Fr(1), Fr(-2), Fr(3), Fr(1, 2)])
        off = [_eps_X(Ft, Ft, Y) for Y in ys]
        ok = ok and off[0] != off[1]
    return ok, found


def _weyl_basis():
    cands = []
    for h in _basis_sym():
        for k in _basis_sym():
            cands.append(_weyl(_kn(h, k)))
    keys = sorted(cands[0])
    basis, rows = [], []
    for W in cands:
        trial = rows + [[W[k] for k in keys]]
        if GA.rank_of_vectors([list(r) for r in trial]) > len(rows):
            rows = trial
            basis.append(W)
    return basis


def _run_frozen_point_integrand_is_a_quarter_weyl_square():
    _premises_locus()
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    basis = _weyl_basis()
    ok = len(basis) == 10
    Fs = [_tractor_F(W) for W in basis]
    npairs = 0
    for i in range(len(basis)):
        for j in range(i, len(basis)):
            ok = ok and _eps_X(Fs[i], Fs[j]) == Fr(1, 4) * _sq(basis[i], basis[j])
            npairs += 1
    for W in _sample_weyls():
        ok = ok and _eps_X(_tractor_F(W, COTTON), _tractor_F(W, COTTON)) == Fr(1, 4) * _sq(W, W)
    R = _curv(0, 1)
    ok = ok and _eps_X(_tractor_F(R), _tractor_F(R)) != Fr(1, 4) * _sq(R, R)
    return ok, len(basis), npairs, [_sq(W, W) for W in _sample_weyls()]


def _coords(x, basis, blades):
    n = len(basis)
    A = [[basis[i].get(b, Fr(0)) for i in range(n)] + [x.get(b, Fr(0))] for b in blades]
    r, piv = 0, []
    for col in range(n):
        p = next((k for k in range(r, len(A)) if A[k][col] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][col]
        A[r] = [a / pv for a in A[r]]
        for k in range(len(A)):
            if k != r and A[k][col] != 0:
                f = A[k][col]
                A[k] = [a - f * b for a, b in zip(A[k], A[r])]
        piv.append(col)
        r += 1
    if any(A[k][n] != 0 for k in range(r, len(A))):
        raise ValueError("not in span")
    c = [Fr(0)] * n
    for k, col in enumerate(piv):
        c[col] = A[k][n]
    return c


def _invariant_dim(gens, space, sym):
    n = len(space)
    blades = sorted({b for v in space for b in v})
    ads = [[_coords(_cp(g, v), space, blades) for v in space] for g in gens]
    idx = {}
    for i in range(n):
        for j in range(i if sym else i + 1, n):
            idx[(i, j)] = len(idx)

    def M(i, j):
        if (i, j) in idx:
            return {idx[(i, j)]: Fr(1)}
        if (j, i) in idx:
            return {idx[(j, i)]: Fr(1) if sym else Fr(-1)}
        return {}
    rows = []
    for ad in ads:
        for i in range(n):
            for j in range(n):
                row = {}
                for k in range(n):
                    for (u, v) in M(k, j).items():
                        row[u] = row.get(u, 0) + ad[i][k] * v
                    for (u, v) in M(i, k).items():
                        row[u] = row.get(u, 0) + ad[j][k] * v
                if any(row.values()):
                    rows.append([row.get(t, Fr(0)) for t in range(len(idx))])
    return len(idx) - (GA.rank_of_vectors(rows) if rows else 0)


def _reflect(x, a):
    """Reflection of a multivector in the hyperplane orthogonal to the unit vector a: x -> a xhat a^{-1}."""
    ainv = GA.scal(1 / _dot(a, a), a)
    return _m(_m(a, GA.grade_inv(x)), ainv)


def _run_invariant_forms_on_the_locus_are_chern_and_weyl():
    _premises_locus()
    xperp = [E[0], E[1], E[2], E[3], N0]
    locus = [_wedge(a, b) for a, b in combinations(xperp, 2)]
    ok = all(GA.is_zero(GA.sub(_m(B, X), _m(X, B))) for B in locus)
    biv6 = [_wedge(E[i], E[j]) for i, j in combinations(range(6), 2)]
    dims = (len(locus), _invariant_dim(locus, locus, True), _invariant_dim(locus, locus, False),
            _invariant_dim(biv6, biv6, True))
    sq4 = (1, -1, -1, -1)
    biv4 = [GA.mul(GA.gen(i), GA.gen(j), sq4) for i, j in combinations(range(4), 2)]
    blades4 = sorted({b for v in biv4 for b in v})

    def ad4(g, v):
        return GA.scal(Fr(1, 2), GA.sub(GA.mul(g, v, sq4), GA.mul(v, g, sq4)))
    # so(1,3) has two (Pontryagin and Euler): verify the two forms are invariant and independent
    K4 = [[GA.mul(a, b, sq4).get((), Fr(0)) for b in biv4] for a in biv4]
    P4 = [[GA.mul(a, b, sq4).get((0, 1, 2, 3), Fr(0)) for b in biv4] for a in biv4]
    ok = ok and GA.rank_of_vectors([sum(K4, []), sum(P4, [])]) == 2
    for g in biv4:
        for M4, pick in ((K4, ()), (P4, (0, 1, 2, 3))):
            for i, a in enumerate(biv4):
                for j, b in enumerate(biv4):
                    lhs = GA.mul(ad4(g, a), b, sq4).get(pick, Fr(0)) + GA.mul(a, ad4(g, b), sq4).get(pick, Fr(0))
                    ok = ok and lhs == 0
    ok = ok and len(blades4) == 6
    # K and eps_X are invariant, independent, and of opposite sign under the internal reflection in e1
    Kf = [[_m(a, b).get((), Fr(0)) for b in locus] for a in locus]
    Ef = [[_eps(X, NI, a, b) for b in locus] for a in locus]
    ok = ok and GA.rank_of_vectors([sum(Kf, []), sum(Ef, [])]) == 2
    for g in locus:
        for i, a in enumerate(locus):
            for j, b in enumerate(locus):
                ok = ok and _m(_cp(g, a), b).get((), Fr(0)) + _m(a, _cp(g, b)).get((), Fr(0)) == 0
                ok = ok and _eps(X, NI, _cp(g, a), b) + _eps(X, NI, a, _cp(g, b)) == 0
    a, b = locus[0], locus[7]
    ra, rb = _reflect(a, E[1]), _reflect(b, E[1])
    ok = ok and _m(ra, rb).get((), Fr(0)) == _m(a, b).get((), Fr(0))
    ok = ok and _eps(X, NI, ra, rb) == -_eps(X, NI, a, b) and _eps(X, NI, a, b) != 0
    return ok, dims


def _run_frame_leg_pairings_vanish_on_the_locus():
    _premises_locus()

    def ee(e, f):
        return {} if e == f else GA.scal(2, _wedge(E[e], E[f]))
    ok = True
    for W in _weyl_basis() + _sample_weyls():
        Fc = _tractor_F(W, COTTON)
        ok = ok and _form(ee, Fc, lambda F, G: _m(F, G).get((), Fr(0))) == 0
        ok = ok and _eps_X(ee, Fc) == 0
    R = _curv(0, 2)
    Fr_ = _tractor_F(R)
    ok = ok and _eps_X(ee, Fr_) != 0
    T = {k: R[k] for k in R}
    T[(0, 1, 2, 3)] += 1
    T[(1, 0, 2, 3)] -= 1
    T[(0, 1, 3, 2)] -= 1
    T[(1, 0, 3, 2)] += 1
    ok = ok and _form(ee, _tractor_F(T), lambda F, G: _m(F, G).get((), Fr(0))) != 0
    vol = _eps_X(ee, ee)
    ok = ok and vol != 0
    return ok, (_eps_X(ee, Fr_), _form(ee, _tractor_F(T), lambda F, G: _m(F, G).get((), Fr(0))), vol)


def _run_weyl_square_integral_is_not_topological():
    premise("synthesis.imported-gtg-dictionary")
    eu = (1, 1, 1, 1)

    def product(k1, k2):
        R = {(a, b, c, d): Fr(0) for a in R4 for b in R4 for c in R4 for d in R4}
        for blk, k in (((0, 1), k1), ((2, 3), k2)):
            for a in blk:
                for b in blk:
                    for c in blk:
                        for d in blk:
                            R[(a, b, c, d)] = k * ((a == c) * (b == d) - (a == d) * (b == c))
        return R

    def integrals(k1, k2):
        R = product(k1, k2)
        W = _weyl(R, eu)
        Ric = _ricci(R, eu)
        sc = sum(Ric[i][i] for i in R4)
        euler = _sq(R, R, eu) - 4 * sum(Ric[i][j] ** 2 for i in R4 for j in R4) + sc ** 2
        area = 1 / (k1 * k2)  # (4 pi/K1)(4 pi/K2) over 16 pi^2
        return _sq(W, W, eu) * area, euler * area
    w11, e11 = integrals(Fr(1), Fr(1))
    w12, e12 = integrals(Fr(1), Fr(2))
    w13, e13 = integrals(Fr(2), Fr(6))
    ok = e11 == e12 == e13 == 8
    ok = ok and w11 == Fr(16, 3) and w12 == 6 and w13 == Fr(16, 3) * Fr(4, 3)
    ok = ok and w11 == Fr(4, 3) * 4 and w12 == Fr(4, 3) * Fr(9, 2)
    # the four-dimensional identity behind it: |W|^2 - Euler = 2 |Ric|^2 - (2/3) R^2 on the product
    ok = ok and w11 != w12 and e11 == e12
    return ok, (w11, w12, w13, e11)


def _run_chern_form_is_the_chern_simons_derivative():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    bl = [(i, j) for i, j in combinations(range(6), 2)]

    def biv(seed):
        return {b: Fr((seed * (3 * k + 1)) % 7 - 3, 1 + (seed + k) % 3) for k, b in enumerate(bl)
                if (seed * (3 * k + 1)) % 7 != 3}
    a = [biv(m + 1) for m in R4]
    b = [[biv(5 + 4 * m + n) for n in R4] for m in R4]
    c = {}
    for m in R4:
        for n in R4:
            for r in range(n, 4):
                c[(m, n, r)] = c[(m, r, n)] = biv(23 + 16 * m + 4 * n + r)

    def jadd(*js):
        return (GA.add(*[j[0] for j in js]), [GA.add(*[j[1][r] for j in js]) for r in R4])

    def jmul(f, x, y):
        return (f(x[0], y[0]), [GA.add(f(x[1][r], y[0]), f(x[0], y[1][r])) for r in R4])

    def jsc(k, x):
        return (GA.scal(k, x[0]), [GA.scal(k, g) for g in x[1]])
    A = [(a[m], [b[m][r] for r in R4]) for m in R4]
    dA = [[(b[m][n], [c[(m, n, r)] for r in R4]) for n in R4] for m in R4]
    Fv = {(m, n): jadd(dA[n][m], jsc(-1, dA[m][n]), jmul(_cp, A[m], A[n])) for m in R4 for n in R4}
    ff = Fr(0)
    for p in permutations(range(4)):
        ff += _sign(p) * _m(Fv[(p[0], p[1])][0], Fv[(p[2], p[3])][0]).get((), Fr(0))
    ff = ff / 4

    def s0(x, y):
        return _grade(_m(x, y), 0)

    def cs(idx, k):
        tot = None
        for p in permutations(idx):
            s = _sign([idx.index(q) for q in p])
            t = jadd(jmul(s0, A[p[0]], dA[p[2]][p[1]]), jsc(k, jmul(s0, A[p[0]], jmul(_cp, A[p[1]], A[p[2]]))))
            t = jsc(s, t)
            tot = t if tot is None else jadd(tot, t)
        return tot

    def dcs(k):
        out = Fr(0)
        for idx, r, s in (((1, 2, 3), 0, 1), ((0, 2, 3), 1, -1), ((0, 1, 3), 2, 1), ((0, 1, 2), 3, -1)):
            out += s * cs(idx, k)[1][r].get((), Fr(0))
        return out
    return ff != 0 and dcs(Fr(1, 3)) == ff and dcs(Fr(2, 3)) != ff and dcs(Fr(0)) != ff, (ff, dcs(Fr(2, 3)))


def check_tractor_field_strength_of_torsion_free_field_annihilates_x():
    _premises_locus()
    ok, ncomp = _run_tractor_field_strength_of_torsion_free_field_annihilates_x()
    ok = ok and ncomp == 36
    GA.check("(i) F . X = 0 on 36 frame components of three torsion-free samples; torsion breaks it", ok)
    return ok


def check_eps_contraction_is_independent_of_the_second_vector_on_the_locus():
    _premises_locus()
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok, found = _run_eps_contraction_is_independent_of_the_second_vector_on_the_locus()
    ok = ok and found == [Fr(16366, 3), Fr(-702), Fr(638)]
    GA.check("(ii) eps_X independent of Y on the locus; eps(I, V, F, F) = (X.I) eps_X(F, F)", ok)
    return ok


def check_frozen_point_integrand_is_a_quarter_weyl_square():
    _premises_locus()
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok, nb, npairs, squares = _run_frozen_point_integrand_is_a_quarter_weyl_square()
    ok = ok and nb == 10 and npairs == 55 and squares == [Fr(65464, 3), Fr(-2808), Fr(2552)]
    GA.check("(iii) eps_X(F, F) = W.W/4 on all 55 pairs of a Weyl basis and on the samples", ok)
    return ok


def check_invariant_forms_on_the_locus_are_chern_and_weyl():
    _premises_locus()
    ok, dims = _run_invariant_forms_on_the_locus_are_chern_and_weyl()
    ok = ok and dims == (10, 2, 0, 1)
    GA.check("(iv) stab(X) on wedge^2 X^perp: symmetric 2 (K, eps_X), antisymmetric 0; so(2,4): 1", ok)
    return ok


def check_frame_leg_pairings_vanish_on_the_locus():
    _premises_locus()
    ok, vals = _run_frame_leg_pairings_vanish_on_the_locus()
    ok = ok and vals == (Fr(-12), Fr(2), Fr(24))
    GA.check("(iv) frame-leg pairings vanish on the locus, not off it; the volume pairing is 24", ok)
    return ok


def check_weyl_square_integral_is_not_topological():
    premise("synthesis.imported-gtg-dictionary")
    ok, vals = _run_weyl_square_integral_is_not_topological()
    ok = ok and vals == (Fr(16, 3), Fr(6), Fr(64, 9), Fr(8))
    GA.check("(v) Weyl-square integral over S2 x S2 is 16/3, 6, 64/9 (per 16 pi^2); Euler 8", ok)
    return ok


def check_chern_form_is_the_chern_simons_derivative():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    ok, vals = _run_chern_form_is_the_chern_simons_derivative()
    ok = ok and vals == (Fr(10867, 108), Fr(13159, 54))
    GA.check("(iv) <F ^ F>_0 = d CS(A) at a 2-jet (coefficient 1/3; 2/3 fails)", ok)
    return ok

if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("check_") and callable(fn):
            fn()


# ---- the proof's GTG route: Weyl maps as linear functions on bivectors (lib/gtg.py) ----
def _sym_maps():
    """The ten basis symmetric maps T of spacetime vectors (T(e_a) . e_b symmetric), as callables."""
    out = []
    for i in R4:
        for j in range(i, 4):
            def T(v, i=i, j=j):
                res = {}
                for (k,), c in v.items():
                    # matrix with (i, j) and (j, i) entries 1 on lowered components: T(e_k) = sum_l M_kl e^l
                    for (a, b) in ({(i, j), (j, i)}):
                        if a == k:
                            res = GA.add(res, GA.scal(c * Fr(1, ETA[b]), GA.gen(b)))
                return res
            out.append(T)
    return out


def _weyl_map_basis():
    """Ten independent Weyl maps W = weyl_op(KN(S, T)) of Cl(1,3), as frame-plane dicts."""
    S = _sym_maps()
    blades = gtg.bivector_blades(4)
    basis, rows = [], []
    for A in S:
        for B in S:
            Wp = gtg.weyl_op(_kn_pair(A, B), gtg.S13)
            row = [c for pl in sorted(Wp) for c in [Wp[pl].get(bl, Fr(0)) for bl in blades]]
            trial = rows + [row]
            if GA.rank_of_vectors([list(r) for r in trial]) > len(rows):
                rows, basis = trial, basis + [Wp]
    return basis


def _kn_pair(A, B):
    """The Kulkarni-Nomizu-type operator a ^ b -> A(a) ^ B(b) + B(a) ^ A(b) (symmetric in A, B)."""
    def R(Xb):
        out = {}
        for (m, n), c in Xb.items():
            em, en = GA.gen(m), GA.gen(n)
            out = GA.add(out, GA.scal(c, GA.add(gtg.wedge(A(em), B(en)), gtg.wedge(B(em), A(en)))))
        return out
    return R


def _F_from_weyl_map(W, C=None):
    """Frame components F_ef = -W(e_e ^ e_f) (plus the Cotton block n0 ^ c) in Cl(2,4)."""
    def Fc(e, f):
        if e == f:
            return {}
        out = GA.neg(gtg.apply_op(W, gtg.biv(e, f)))
        if C is not None:
            c = {}
            for a in R4:
                c = GA.add(c, GA.scal(C[e][a] - C[f][a], E[a]))
            out = GA.add(out, _wedge(N0, c))
        return out
    return Fc


def _half_weyl_square(W1, W2):
    """(1/2) <W1(a ^ b) W2(d_b ^ d_a)>, summed over the frame (the scalar of the Weyl map pair)."""
    tot = Fr(0)
    for a in R4:
        for b in R4:
            if a != b:
                rb = GA.scal(Fr(1, ETA[a] * ETA[b]), gtg.biv(b, a))
                tot += gtg.sp(GA.mul(gtg.apply_op(W1, gtg.biv(a, b)), gtg.apply_op(W2, rb), gtg.S13))
    return tot / 2


def check_gtg_weyl_square_of_weyl_maps():
    """(iii) with the Weyl part as a linear map on bivectors: on ten independent Weyl maps of Cl(1,3) (built by
    the library from Kulkarni-Nomizu operators) and their 55 pairs, eps_X(F1, F2) = (1/2) <W1(a ^ b) W2(d_b ^ d_a)>
    for F = -W (and with a Cotton block); the Weyl maps are trace-free and I-linear. (v) pointwise, on the
    product operator calR = K1 on e1 ^ e2, K2 on e3 ^ e4 of Cl(4,0): Weyl square 2 <W W> = (4/3)(K1 + K2)^2 and
    Euler density 8 K1 K2, so the integrals over 16 pi^2 are (4/3)(K1 + K2)^2/(K1 K2) and 8."""
    _premises_locus()
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    basis = _weyl_map_basis()
    ok = len(basis) == 10
    I4 = gtg.pseudoscalar(gtg.S13)
    for W in basis:
        ok = ok and all(gtg.ricci(W, GA.gen(m)) == {} for m in R4)
        ok = ok and all(GA.eq(gtg.apply_op(W, GA.mul(I4, gtg.biv(a, b), gtg.S13)),
                              GA.mul(I4, gtg.apply_op(W, gtg.biv(a, b)), gtg.S13)) for a in R4 for b in range(a + 1, 4))
    Fs = [_F_from_weyl_map(W) for W in basis]
    n = 0
    for i in range(len(basis)):
        for j in range(i, len(basis)):
            ok = ok and _eps_X(Fs[i], Fs[j]) == _half_weyl_square(basis[i], basis[j])
            n += 1
    ok = ok and n == 55
    ok = ok and _eps_X(_F_from_weyl_map(basis[3], COTTON), _F_from_weyl_map(basis[3], COTTON)) == \
        _half_weyl_square(basis[3], basis[3])
    sq4 = GA.sig(4, 0)
    for k1, k2 in ((Fr(1), Fr(1)), (Fr(1), Fr(2)), (Fr(2), Fr(6))):
        def R(Xb, k1=k1, k2=k2):
            return GA.add(GA.scal(k1 * Xb.get((0, 1), Fr(0)), gtg.biv(0, 1, sq4)),
                          GA.scal(k2 * Xb.get((2, 3), Fr(0)), gtg.biv(2, 3, sq4)))
        Wp = gtg.weyl_op(R, sq4)
        ok = ok and gtg.kretschmann(Wp, sq4) == Fr(4, 3) * (k1 + k2) ** 2
        ok = ok and gtg.euler_density(R, sq4) == 8 * k1 * k2
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_weyl_square_of_weyl_maps"; return _tp_rv


def _frame_plane_op(R):
    """The frame-plane dict {(a, b): R(e_a ^ e_b)} of a callable bivector map R of Cl(1,3)."""
    return {bl: R(gtg.biv(*bl)) for bl in gtg.bivector_blades(4)}


def _bianchi_free(W):
    """First Bianchi identity d_a ^ W(a ^ b) = 0 for every frame vector b."""
    for m in R4:
        tot = {}
        for a in R4:
            if a != m:
                tot = gtg.m_add(tot, gtg.outer(gtg.er(a), gtg.apply_op(W, gtg.wedge(GA.gen(a), GA.gen(m))), gtg.S13))
        if tot:
            return False
    return True


def _leg_traces(W):
    """(<W(a ^ b)(d_b ^ d_a)>, <I4 W(a ^ b)(d_b ^ d_a)>) summed over the frame."""
    I4 = gtg.pseudoscalar(gtg.S13)
    s0, sI = Fr(0), Fr(0)
    for a in R4:
        for b in R4:
            if a != b:
                rb = GA.scal(Fr(1, ETA[a] * ETA[b]), gtg.biv(b, a))
                P = GA.mul(gtg.apply_op(W, gtg.biv(a, b)), rb, gtg.S13)
                s0 += gtg.sp(P)
                sI += gtg.sp(GA.mul(I4, P, gtg.S13))
    return s0, sI


def check_gtg_frame_legs_and_weyl_space():
    """(iv) frame legs in GA: for a bivector map R with Lorentz block F = -R (Cotton block present),
    K(DX ^ DX, F) = -<I4 R(a ^ b)(d_b ^ d_a)> and eps_X(DX ^ DX, F) = -<R(a ^ b)(d_b ^ d_a)> = -calR (the scalar),
    on a Kulkarni-Nomizu map with a Ricci part, on B -> I4 B and on their sum (both sides nonzero there), and both
    vanish on the ten basis Weyl maps (first Bianchi identity, trace-freeness). (iii) the Weyl space: the basis
    Weyl maps obey the first Bianchi identity d_a ^ W(a ^ b) = 0; B -> I4 B is symmetric, trace-free and I-linear
    but violates it, so those three conditions alone do not cut out the Weyl maps."""
    _premises_locus()
    I4 = gtg.pseudoscalar(gtg.S13)
    S = _sym_maps()
    kn = _frame_plane_op(_kn_pair(S[0], S[4]))
    imap = _frame_plane_op(lambda B: GA.mul(I4, B, gtg.S13))
    both = {bl: GA.add(kn[bl], imap[bl]) for bl in kn}

    def ee(e, f):
        return {} if e == f else GA.scal(2, _wedge(E[e], E[f]))

    def legs(W):
        Fc = _F_from_weyl_map(W, COTTON)
        return _form(ee, Fc, lambda F1, F2: _m(F1, F2).get((), Fr(0))), _eps_X(ee, Fc)
    ok = True
    vals = []
    for W in (kn, imap, both):
        K, ex = legs(W)
        s0, sI = _leg_traces(W)
        ok = ok and K == -sI and ex == -s0 and s0 == gtg.ricci_scalar(W, gtg.S13)
        vals.append((K, ex))
    ok = ok and vals == [(Fr(0), Fr(2)), (Fr(12), Fr(0)), (Fr(12), Fr(2))]
    ok = ok and _bianchi_free(kn) and not _bianchi_free(imap)
    for bl in gtg.bivector_blades(4):
        for bl2 in gtg.bivector_blades(4):
            A, B = gtg.biv(*bl), gtg.biv(*bl2)
            ok = ok and gtg.sp(GA.mul(A, gtg.apply_op(imap, B), gtg.S13)) == gtg.sp(GA.mul(gtg.apply_op(imap, A), B, gtg.S13))
    ok = ok and all(gtg.ricci(imap, GA.gen(m)) == {} for m in R4)
    for W in _weyl_map_basis():
        ok = ok and _bianchi_free(W) and legs(W) == (Fr(0), Fr(0))
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_frame_legs_and_weyl_space"; return _tp_rv
