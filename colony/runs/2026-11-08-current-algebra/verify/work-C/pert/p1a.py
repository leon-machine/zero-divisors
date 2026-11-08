"""synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split: exact checks.

Five modes 0, 1 (slots) and 2, 3, 4 (pairs); V = Lambda C^5 in the occupation (bitmask) basis, V_+ the sixteen
states of even mode number (the halving (-1)^(n + k) with the empty state as neutral singlet), ordered by degree.
rho(X) is the action of X in gl(5) by the number-conserving bilinears sum X_ab a*_a a_b, restricted to V_+.
A window of L levels k = 0..L-1 carries 16 channels x; mode (x, k) is bit x L + k; c*, c act by the Jordan-Wigner
signs of lib/fock.py (checked against the Clifford relations of the tower planes, e = c* + c, f = c* - c).
J(M)_m = sum_{x,y} M_xy sum_k c*_{x,k} c_{y,k+m}. The sea Omega_s fills levels 0..s-1 of every channel.
H = sum_{x,k} (k + 1/2) n_{x,k}. For a factor with basis M_A and trace-dual basis M^A (tr_16 form),
H_f = (2 + lam_f)^{-1} (2 sum_{q >= 1} J(M^A)_{-q} J(M_A)_q + J(M^A)_0 J(M_A)_0), lam_f the adjoint Casimir.
(1) rho maps the gauge algebra into traceless 16 x 16 matrices, preserves V_+, is a homomorphism, commutes with
    transposition; the compact generators (unit J of a tower level, GA element of square -1) give anti-Hermitian
    channel matrices; the hypercharges on V_+ are the stored list.
(2) tr_16(rho X rho Y) = 4 tr_5(XY) on the whole gauge algebra; tr Y^2 = 10/3; distinct factors and the number
    current are trace-orthogonal; the window commutator of two gauge currents on edge-clean vectors has central
    term 4 m tr_5.
(3) Adjoint Casimirs lam = 3/2 (su(3)), 1 (su(2)), 2n on su(n); c = 2 dim / (2 + lam).
(4) On localised window vectors [H_f, J(X)_m] = -m J(X)_m for X in the factor, 0 for X in another factor;
    [H - sum H_f, J(X)_m] = 0; the relation fails on a vector at the window edge.
(5) ||L^f_{-2} Omega||^2 = dim f / (2 + lam_f): 16/7, 1, 1/2, 1/2; total 8; parts orthogonal; remainder 26/7.
"""
import itertools
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

# ------------------------------------------------------------------ the five-mode module and its even half
NM = 5
CH = sorted([S for S in range(1 << NM) if fock.popcount(S) % 2 == 0], key=lambda S: (fock.popcount(S), S))
ODD = [S for S in range(1 << NM) if fock.popcount(S) % 2 == 1]
POS = {S: i for i, S in enumerate(CH)}
NC = len(CH)


def _zero(n):
    return [[F(0)] * n for _ in range(n)]


def _one(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def _e5(a, b):
    M = _zero(NM)
    M[a][b] = F(1)
    return M


def _lin(*pairs):
    n = len(pairs[0][1])
    out = _zero(n)
    for c, X in pairs:
        for i in range(n):
            for j in range(n):
                out[i][j] += F(c) * X[i][j]
    return out


def _mm(A, B):
    return [[sum((A[i][l] * B[l][j] for l in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]


def _tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def _comm(A, B):
    return _lin((1, _mm(A, B)), (-1, _mm(B, A)))


def _T(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def _bil_on(kind, a, b, v):
    if kind == "ab":
        return fock.cre_on(a, fock.ann_on(b, v))
    if kind == "cc":
        return fock.cre_on(a, fock.cre_on(b, v))
    return fock.ann_on(a, fock.ann_on(b, v))


def _rep_bil(kind, a, b, rows=CH, cols=CH):
    pos = {S: i for i, S in enumerate(rows)}
    M = [[F(0)] * len(cols) for _ in rows]
    for j, S in enumerate(cols):
        for T, c in _bil_on(kind, a, b, {S: F(1)}).items():
            if T not in pos:
                return None
            M[pos[T]][j] += c
    return M


def _rep(X):
    M = _zero(NC)
    for a in range(NM):
        for b in range(NM):
            if X[a][b]:
                R = _rep_bil("ab", a, b)
                M = _lin((1, M), (X[a][b], R))
    return M


SU2 = [_e5(0, 1), _e5(1, 0), _lin((1, _e5(0, 0)), (-1, _e5(1, 1)))]
SU3 = [_e5(a, b) for a in (2, 3, 4) for b in (2, 3, 4) if a != b] + \
      [_lin((1, _e5(2, 2)), (-1, _e5(3, 3))), _lin((1, _e5(3, 3)), (-1, _e5(4, 4)))]
Y5 = _lin((F(1, 2), _e5(0, 0)), (F(1, 2), _e5(1, 1)), (F(-1, 3), _e5(2, 2)), (F(-1, 3), _e5(3, 3)),
          (F(-1, 2), _e5(4, 4)))
FACTORS = (("su3", SU3), ("su2", SU2), ("Y", [Y5]))


def _inv(G):
    k = len(G)
    A = [list(row) + [F(int(i == j)) for j in range(k)] for i, row in enumerate(G)]
    for c in range(k):
        p = next(r for r in range(c, k) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(k):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[k:] for row in A]


def _dual(B16):
    """trace-dual basis (tr_16 form) of a list of 16 x 16 matrices"""
    Gi = _inv([[_tr(_mm(A, B)) for B in B16] for A in B16])
    return [_lin(*[(Gi[a][b], B16[b]) for b in range(len(B16)) if Gi[a][b]] or [(0, B16[0])]) for a in range(len(B16))]


def _lam(B, D, X):
    """adjoint Casimir sum_A [M^A, [M_A, X]] = lam X: returns lam"""
    acc = _zero(len(X))
    for M, Md in zip(B, D):
        acc = _lin((1, acc), (1, _comm(Md, _comm(M, X))))
    vals = {acc[i][j] / X[i][j] for i in range(len(X)) for j in range(len(X)) if X[i][j]}
    zero_ok = all(acc[i][j] == 0 for i in range(len(X)) for j in range(len(X)) if X[i][j] == 0)
    return vals.pop() if len(vals) == 1 and zero_ok else None


# ------------------------------------------------------------------ windows
class _Win(object):
    def __init__(self, n, L):
        self.n, self.L = n, L

    def idx(self, x, k):
        return x * self.L + k

    def sea(self, s):
        return {sum(1 << self.idx(x, k) for x in range(self.n) for k in range(s)): F(1)}

    def cur(self, M, m, v):
        out = {}
        for x in range(self.n):
            for y in range(self.n):
                a = M[x][y]
                if not a:
                    continue
                for k in range(self.L):
                    if 0 <= k + m < self.L:
                        for s, c in fock.cre_on(self.idx(x, k), fock.ann_on(self.idx(y, k + m), v)).items():
                            out[s] = out.get(s, 0) + a * c
        return {s: c for s, c in out.items() if c}

    def energy(self, v):
        out = {}
        for S, c in v.items():
            e = sum((F(2 * k + 1, 2) for x in range(self.n) for k in range(self.L) if S >> self.idx(x, k) & 1), F(0))
            if e:
                out[S] = e * c
        return out

    def sug(self, B, D, v, maxq=None):
        """2 sum_{q>=1} J(D_A)_{-q} J(B_A)_q v + J(D_A)_0 J(B_A)_0 v"""
        out = {}
        for q in range(0, self.L if maxq is None else maxq + 1):
            for M, Md in zip(B, D):
                inner = self.cur(M, q, v)
                if inner:
                    out = _vadd(out, _vsc(2 if q else 1, self.cur(Md, -q, inner)))
        return out


def _vadd(*vs):
    out = {}
    for v in vs:
        for s, c in v.items():
            out[s] = out.get(s, 0) + c
    return {s: c for s, c in out.items() if c}


def _vsc(a, v):
    return {s: a * c for s, c in v.items() if a * c}


def _norm2(v):
    return sum((c * c for c in v.values()), F(0))


def _ip(u, v):
    return sum((c * v.get(s, 0) for s, c in u.items()), F(0))


def _E(n, x, y):
    M = _zero(n)
    M[x][y] = F(1)
    return M


def _factor_data():
    out = []
    for name, B5 in FACTORS:
        B = [_rep(X) for X in B5]
        D = _dual(B)
        lam = _lam(B, D, B[0]) if len(B) > 1 else F(0)
        out.append((name, B, D, lam))
    out.append(("N", [_one(NC)], [_vsc_m(F(1, NC), _one(NC))], F(0)))
    return out


def _vsc_m(a, M):
    return [[a * x for x in row] for row in M]


# ------------------------------------------------------------------ helpers for the checks
def _gauge_reps():
    return [_rep(X) for X in SU3 + SU2 + [Y5]]


def _preserves_v_plus(B5):
    for X in B5:
        for a in range(NM):
            for b in range(NM):
                if X[a][b] and _rep_bil("ab", a, b) is None:
                    return False
    return True


def _hypercharges():
    R = _rep(Y5)
    diag = all(R[i][j] == 0 for i in range(NC) for j in range(NC) if i != j)
    return sorted(R[i][i] for i in range(NC)) if diag else None


def _compact_generator_is_anti_hermitian():
    sq = (-1, -1)
    J = GA.mul(GA.gen(0), GA.gen(1), sq)
    H1 = _lin((1, _rep(SU2[0])), (1, _rep(SU2[1])))
    Tm = [[GA.scal(H1[i][j], J) for j in range(NC)] for i in range(NC)]
    unit = GA.eq(GA.mul(J, J, sq), GA.sc(-1)) and GA.eq(GA.reverse(J), GA.neg(J))
    anti = all(GA.eq(GA.reverse(Tm[j][i]), GA.neg(Tm[i][j])) for i in range(NC) for j in range(NC))
    nonzero = any(Tm[i][j] for i in range(NC) for j in range(NC))
    return unit and anti and nonzero


def _common_phase(num, den):
    """the pair-current phase z_x conj(z_y) when all channels carry the same weight z = (num + den J)/5"""
    sq = (-1, -1)
    J = GA.mul(GA.gen(0), GA.gen(1), sq)
    z = GA.add(GA.sc(F(num, 5)), GA.scal(F(den, 5), J))
    return GA.mul(z, GA.reverse(z), sq)


def _edge_clean_vectors(W):
    base = sum(1 << W.idx(x, 0) for x in range(W.n))
    return [base, base + sum(1 << W.idx(x, 1) for x in range(0, W.n, 3)),
            base + sum(1 << W.idx(x, 1) for x in range(W.n) if x % 2)]


def _window_central_values(R, pairs):
    """[J(X)_1, J(Y*)_-1] - J([X, Y*])_0 on edge-clean vectors: returns the scalar, or None if not scalar"""
    W = _Win(NC, 3)
    out = []
    for i, j in pairs:
        X, Yy = R[i], _T(R[j])
        C = _comm(X, Yy)
        vals = set()
        for S in _edge_clean_vectors(W):
            v = {S: F(1)}
            lhs = _vadd(W.cur(X, 1, W.cur(Yy, -1, v)), _vsc(-1, W.cur(Yy, -1, W.cur(X, 1, v))))
            d = _vadd(lhs, _vsc(-1, W.cur(C, 0, v)))
            if d and set(d) != {S}:
                return None
            vals.add(d.get(S, F(0)))
        if len(vals) != 1:
            return None
        out.append(vals.pop())
    return out


def _gl_casimir_value(n):
    X = _E(n, 0, 3)
    acc = _zero(n)
    for x in range(n):
        for y in range(n):
            acc = _lin((1, acc), (1, _comm(_E(n, y, x), _comm(_E(n, x, y), X))))
    vals = {acc[i][j] / X[i][j] for i in range(n) for j in range(n) if X[i][j]}
    zero_ok = all(acc[i][j] == 0 for i in range(n) for j in range(n) if X[i][j] == 0)
    return vals.pop() if len(vals) == 1 and zero_ok else None


def _split_relations(data):
    """on localised vectors of the window WIN_LOCAL: [H_f, J(X)_m] + m J(X)_m (own factor), [H_f, J(X)_m]
    (other factors), [H_c, J(X)_m]; returns the three booleans 'all zero'"""
    L, s = WIN_LOCAL
    W = _Win(NC, L)
    Om = W.sea(s)
    psis = [Om, W.cur(_E(NC, SAMPLE_PAIRS[0][0], SAMPLE_PAIRS[0][1]), -1, Om)]

    def Hf(d, v):
        return _vsc(1 / (2 + d[3]), W.sug(d[1], d[2], v))

    def Hc(v):
        out = W.energy(v)
        for d in data:
            out = _vadd(out, _vsc(-1, Hf(d, v)))
        return out
    ok_own = ok_other = ok_coset = True
    for psi in psis:
        hc = Hc(psi)
        hf = [Hf(d, psi) for d in data]
        for i, d in enumerate(data):
            Xm = d[1][0]
            for m in (1, -1):
                Xp = W.cur(Xm, m, psi)
                for j, d2 in enumerate(data):
                    lhs = _vadd(Hf(d2, Xp), _vsc(-1, W.cur(Xm, m, hf[j])))
                    if i == j:
                        ok_own = ok_own and lhs == _vsc(-m, Xp)
                    else:
                        ok_other = ok_other and lhs == {}
                ok_coset = ok_coset and _vadd(Hc(Xp), _vsc(-1, W.cur(Xm, m, hc))) == {}
    return ok_own, ok_other, ok_coset


def _edge_vector_breaks(data, channel, top, low):
    L, s = WIN_SMALL
    W = _Win(NC, L)
    psi = fock.cre_on(W.idx(channel, top), fock.ann_on(W.idx(channel, low), W.sea(s)))
    d = data[0]
    Xm = d[1][0]
    Xp = W.cur(Xm, -1, psi)
    lhs = _vadd(_vsc(1 / (2 + d[3]), W.sug(d[1], d[2], Xp)),
                _vsc(-1, W.cur(Xm, -1, _vsc(1 / (2 + d[3]), W.sug(d[1], d[2], psi)))))
    return Xp != {} and lhs != Xp


def _level_two_vectors(data):
    L, s = WIN_SMALL
    W = _Win(NC, L)
    Om = W.sea(s)
    parts = {}
    for name, B, D, lam in data:
        v = {}
        for M, Md in zip(B, D):
            v = _vadd(v, W.cur(Md, -1, W.cur(M, -1, Om)))
        parts[name] = _vsc(1 / (2 + lam), v)
    tot = {}
    for x in range(NC):
        for y in range(NC):
            tot = _vadd(tot, W.cur(_E(NC, y, x), -1, W.cur(_E(NC, x, y), -1, Om)))
    one = _one(NC)
    nn = W.cur(one, -1, W.cur(one, -1, Om))
    tot = _vsc(F(1, 2 * (NC + 1)), _vadd(tot, nn))
    return parts, tot, nn, W, Om


def _sp(M):
    return {(i, j): c for i, row in enumerate(M) for j, c in enumerate(row) if c}


def _spmm(A, B):
    rows = {}
    for (k, j), c in B.items():
        rows.setdefault(k, []).append((j, c))
    out = {}
    for (i, k), a in A.items():
        for j, c in rows.get(k, ()):
            out[(i, j)] = out.get((i, j), 0) + a * c
    return {k: v for k, v in out.items() if v}


def _spadd(*Ms):
    out = {}
    for M in Ms:
        for k, v in M.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def _spsc(a, M):
    return {k: a * v for k, v in M.items() if a * v}


def _gl5_trace_identity():
    """tr_16(rho E_ab rho E_cd) - 4 tr_5(E_ab E_cd) - 4 tr E_ab tr E_cd over all 625 pairs, and tr rho E_ab - 8 tr E_ab"""
    E = [_e5(a, b) for a in range(NM) for b in range(NM)]
    R = [_rep(X) for X in E]
    bad2 = {_tr(_mm(R[i], R[j])) - 4 * _tr(_mm(E[i], E[j])) - 4 * _tr(E[i]) * _tr(E[j])
            for i in range(len(E)) for j in range(len(E))}
    bad1 = {_tr(R[i]) - 8 * _tr(E[i]) for i in range(len(E))}
    return bad2, bad1


def _tower_planes_ok(m):
    def e(w, j):
        return _vadd(fock.cre_on(j, w), fock.ann_on(j, w))

    def f(w, j):
        return _vadd(fock.cre_on(j, w), _vsc(-1, fock.ann_on(j, w)))
    for S in range(1 << m):
        v = {S: F(1)}
        for k in range(m):
            for l in range(m):
                ee = _vadd(e(e(v, k), l), e(e(v, l), k))
                ff = _vadd(f(f(v, k), l), f(f(v, l), k))
                ef = _vadd(e(f(v, k), l), f(e(v, l), k))
                if ee != (_vsc(2, v) if k == l else {}) or ff != (_vsc(-2, v) if k == l else {}) or ef != {}:
                    return False
    return True



# module-level data (any choice satisfying the stated conditions must pass)
WIN_SMALL = (4, 2)       # L, s for level-two norms and the edge counterexample
WIN_LOCAL = (12, 6)      # L, s with min(s, L - s) >= 3(K + |m|) for K = |m| = 1
SAMPLE_PAIRS = ((0, 7), (3, 12), (14, 1))
PLANES = 3
CENTRAL_PAIRS = ((0, 0), (6, 6), (8, 8), (10, 10), (11, 11), (2, 9))


# ------------------------------------------------------------------ checks
def check_gauge_algebra_acts_on_the_sixteen_channels_by_channel_unitary_matrices():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    B5 = SU3 + SU2 + [Y5]
    R = _gauge_reps()
    GA.check("sixteen channels: the even-degree states of Lambda C^5", NC == 16 and len(B5) == 12)
    GA.check("every gauge bilinear maps V_+ into V_+ (no mixing with the conjugate half)", _preserves_v_plus(B5))
    GA.check("every rho(X) is traceless (rho lands in su(16))", sum(1 for M in R if _tr(M) == 0) == 12)
    GA.check("rho(X^T) = rho(X)^T (rho commutes with the CAR adjoint)",
             all(_rep(_T(X)) == _T(_rep(X)) for X in B5))
    GA.check("rho is a homomorphism on all 12 x 12 basis pairs",
             all(_rep(_comm(X, Yy)) == _comm(_rep(X), _rep(Yy)) for X in B5 for Yy in B5))
    want = sorted([F(0)] + [F(-2, 3)] * 3 + [F(1, 6)] * 6 + [F(-1, 2)] * 2 + [F(1)] + [F(1, 3)] * 3)
    GA.check("hypercharges on V_+: 0, -2/3 (x3), 1/6 (x6), -1/2 (x2), 1, 1/3 (x3)", _hypercharges() == want)
    GA.check("compact generator J rho(E01 + E10) is anti-Hermitian over span{1, J}",
             _compact_generator_is_anti_hermitian())
    GA.check("one weight z = (3 + 4J)/5 on every channel: each pair current has phase z z* = 1",
             GA.eq(_common_phase(3, 4), GA.sc(1)))
    return True


def check_levels_trace_form_is_four_times_the_slot_form():
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    premise("field-theory.imported-tower-limit")
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    GA.check("the Jordan-Wigner modes satisfy the Clifford relations of the tower planes", _tower_planes_ok(PLANES))
    B5 = SU3 + SU2 + [Y5]
    R = _gauge_reps()
    ratios = {_tr(_mm(R[i], R[j])) / _tr(_mm(B5[i], B5[j]))
              for i in range(12) for j in range(12) if _tr(_mm(B5[i], B5[j]))}
    zeros = all(_tr(_mm(R[i], R[j])) == 0 for i in range(12) for j in range(12) if _tr(_mm(B5[i], B5[j])) == 0)
    GA.check("tr_16(rho X rho Y) = 4 tr_5(XY) for all X, Y in the gauge algebra", ratios == {4} and zeros)
    bad2, bad1 = _gl5_trace_identity()
    GA.check("on gl(5): tr_16(rho X rho X') = 4 tr_5(X X') + 4 tr X tr X' and tr rho X = 8 tr X (all E_ab)",
             bad2 == {0} and bad1 == {0})
    GA.check("tr_16(rho Y)^2 = 10/3 and tr_5(Y^2) = 5/6", _tr(_mm(R[11], R[11])) == F(10, 3) and
             _tr(_mm(Y5, Y5)) == F(5, 6))
    GA.check("factors trace-orthogonal and traceless (decoupled from the number current)",
             all(_tr(_mm(R[i], R[j])) == 0 for i in range(8) for j in range(8, 12))
             and all(_tr(_mm(R[i], R[11])) == 0 for i in range(8, 11)))
    GA.check("window central values on edge-clean vectors: 4, 8, 4, 8, 10/3, 0",
             _window_central_values(R, CENTRAL_PAIRS) == [4, 8, 4, 8, F(10, 3), 0])
    return True


def check_adjoint_casimirs_and_central_charges():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    data = _factor_data()
    lam = {d[0]: d[3] for d in data}
    GA.check("adjoint Casimirs in the trace-dual basis: su(3) 3/2, su(2) 1, abelian 0",
             [lam["su3"], lam["su2"], lam["Y"], lam["N"]] == [F(3, 2), 1, 0, 0])
    GA.check("gl(16) Casimir on a traceless element: 32", _gl_casimir_value(NC) == 32)
    c = lambda d, l: F(2 * d, 1) / (2 + l)
    GA.check("c = 2 dim / (2 + lam): su(3) 32/7, su(2) 2, u(1) 1, su(16) 15",
             [c(8, lam["su3"]), c(3, lam["su2"]), c(1, lam["Y"]), c(255, _gl_casimir_value(NC))]
             == [F(32, 7), 2, 1, 15])
    GA.check("coset: 16 - 32/7 - 2 - 1 - 1 = 52/7", 16 - c(8, lam["su3"]) - c(3, lam["su2"]) - 2 == F(52, 7))
    return True


def check_split_commutes_on_localised_window_vectors():
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    premise("synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves")
    data = _factor_data()
    own, other, coset = _split_relations(data)
    GA.check("[H_f, J(X)_m] = -m J(X)_m for X in the factor, m = +-1, on localised vectors", own)
    GA.check("[H_f, J(X)_m] = 0 for X in another factor", other)
    GA.check("[H - sum_f H_f, J(X)_m] = 0 for X in every factor (the coset part commutes)", coset)
    GA.check("on a vector with a particle at the top level of a 4-level window the relation fails",
             _edge_vector_breaks(data, 5, 3, 1))
    return True


def check_central_charges_from_level_two_vacuum_norms():
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    data = _factor_data()
    parts, tot, nn, W, Om = _level_two_vectors(data)
    nrm = {k: _norm2(v) for k, v in parts.items()}
    GA.check("||L_-2 Omega||^2 = dim / (2 + lam): su(3) 16/7, su(2) 1, Y 1/2, N 1/2",
             [nrm["su3"], nrm["su2"], nrm["Y"], nrm["N"]] == [F(16, 7), 1, F(1, 2), F(1, 2)])
    GA.check("u(16): ||L_-2 Omega||^2 = 8", _norm2(tot) == 8)
    names = sorted(parts)
    GA.check("the factors' level-two vectors are mutually orthogonal",
             all(_ip(parts[a], parts[b]) == 0 for a in names for b in names if a < b))
    GA.check("<L^f_-2 Omega, L_-2 Omega> = ||L^f_-2 Omega||^2 for every factor",
             all(_ip(parts[a], tot) == nrm[a] for a in names))
    rest = _vadd(tot, _vsc(-1, _vadd(*parts.values())))
    GA.check("coset vector: ||.||^2 = 26/7, orthogonal to every factor",
             _norm2(rest) == F(26, 7) and all(_ip(rest, parts[a]) == 0 for a in names))
    return True
