"""synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy: exact checks.

Windows of L levels k = 0..L-1 on n channels; mode (x, k) is bit x L + k, with the Jordan-Wigner signs of lib/fock.py
(checked against the Clifford relations of the tower planes). j^{xy}_m = sum_k c*_{x,k} c_{y,k+m},
H = sum (k + 1/2) n_{x,k}. For a symmetric tensor C_{xy,zu} = C_{zu,xy},
Phi(C) = sum C_{xy,zu} (2 sum_{q>=1} j^{xy}_{-q} j^{zu}_q + j^{xy}_0 j^{zu}_0),
K_C = sum_y C_{xy,yu}, A_C(a,b,c,d) = C_{ac,bd} - C_{ad,bc}, Q(A) = sum over level-conserving quadruples of modes
A(x_al, x_be, x_ga, x_de) c*_al c*_be c_ga c_de.
(1) Phi(C) = sum_l (2l + 1) (K_C)_{xu} c*_{x,l} c_{u,l} - Q(A_C)/2 on every state, for generic symmetric C.
(2) The u(n) case: (n + 1) H = Phi(gl + 1 x 1)/2 on every state for small cases, and on 16-channel samples.
(3) so(10) of all bilinears of the five modes on the 16 even states: Casimir 45/16 in the 16, A_so = -3 A_N,
    adjoint Casimir 4, so H_so10 = Phi(C_so)/6 and H = H_so10 + H_N.
(4) The operator identity H = H_so10 + H_N on window states of the sixteen channels; the u(5) part alone fails.
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
          (F(-1, 3), _e5(4, 4)))
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


def _so10():
    gens = []
    for a in range(NM):
        for b in range(NM):
            M = _rep_bil("ab", a, b)
            if a == b:
                M = _lin((1, M), (F(-1, 2), _one(NC)))
            gens.append(M)
    for a in range(NM):
        for b in range(a + 1, NM):
            gens.append(_rep_bil("cc", a, b))
            gens.append(_rep_bil("aa", a, b))
    return gens





def _sym_tensor(n, seed):
    """a generic symmetric tensor C_{xy,zu} = C_{zu,xy} with small rational entries"""
    C = {}
    idx = [(x, y) for x in range(n) for y in range(n)]
    for i, p in enumerate(idx):
        for j, r in enumerate(idx):
            if j < i:
                continue
            v = F(((i * 7 + j * 3 + seed) % 9) - 4, 1 + (i + j + seed) % 3)
            if v:
                C[p + r] = v
                C[r + p] = v
    return C


def _phi(C, n, L, v):
    W = _Win(n, L)
    out = {}
    for (x, y, z, u), c in C.items():
        for q in range(0, L):
            inner = W.cur(_E(n, z, u), q, v)
            if inner:
                out = _vadd(out, _vsc(c * (2 if q else 1), W.cur(_E(n, x, y), -q, inner)))
    return out


def _lemma_rhs(C, n, L, v):
    W = _Win(n, L)
    K = {}
    for (x, y, z, u), c in C.items():
        if y == z:
            K[(x, u)] = K.get((x, u), 0) + c
    out = {}
    for (x, u), c in K.items():
        for l in range(L):
            out = _vadd(out, _vsc(c * (2 * l + 1), fock.cre_on(W.idx(x, l), fock.ann_on(W.idx(u, l), v))))
    modes = [(x, k) for x in range(n) for k in range(L)]
    for al, be, ga, de in itertools.product(modes, repeat=4):
        if al[1] + be[1] != ga[1] + de[1]:
            continue
        a = C.get((al[0], ga[0], be[0], de[0]), 0) - C.get((al[0], de[0], be[0], ga[0]), 0)
        if a:
            w = fock.cre_on(W.idx(*al), fock.cre_on(W.idx(*be), fock.ann_on(W.idx(*ga), fock.ann_on(W.idx(*de), v))))
            out = _vadd(out, _vsc(F(-1, 2) * a, w))
    return out


def _lemma_holds(n, L, seed):
    C = _sym_tensor(n, seed)
    return all(_phi(C, n, L, {S: F(1)}) == _lemma_rhs(C, n, L, {S: F(1)}) for S in range(1 << n * L))


def _tensor(B, D):
    C = {}
    for M, Md in zip(B, D):
        sM = [(i, j, c) for i, r in enumerate(M) for j, c in enumerate(r) if c]
        sD = [(i, j, c) for i, r in enumerate(Md) for j, c in enumerate(r) if c]
        for a, c_, x in sD:
            for b, d, y in sM:
                C[(a, c_, b, d)] = C.get((a, c_, b, d), 0) + x * y
    return {k: v for k, v in C.items() if v}


def _casimir_in_16(C):
    K = {}
    for (a, c, b, d), v in C.items():
        if c == b:
            K[(a, d)] = K.get((a, d), 0) + v
    K = {k: v for k, v in K.items() if v}
    vals = {v for (a, d), v in K.items() if a == d}
    if any(a != d for (a, d) in K) or len(vals) != 1 or len(K) != NC:
        return None
    return vals.pop()


def _antisym_ratio(C):
    """the set of ratios A_C(a,b,c,d) / (delta_ac delta_bd - delta_ad delta_bc); 'off' if A_C has other entries"""
    vals = set()
    for a in range(NC):
        for b in range(NC):
            for c in range(NC):
                for d in range(NC):
                    an = (a == c) * (b == d) - (a == d) * (b == c)
                    av = C.get((a, c, b, d), 0) - C.get((a, d, b, c), 0)
                    if an:
                        vals.add(av / an)
                    elif av:
                        vals.add("off")
    return vals


def _so10_identity_residuals(states, L):
    so = _so10()
    D = _dual(so)
    lam = _lam(so, D, so[1])
    W = _Win(NC, L)
    one = _one(NC)
    out = []
    for v in states:
        hso = _vsc(1 / (1 + lam), W.sug(so, D, v))
        hn = _vsc(F(1, 2), W.sug([one], [_vsc_m(F(1, NC), one)], v))
        out.append(_vadd(W.energy(v), _vsc(-1, _vadd(hso, hn))))
    return out


def _sample_states(L, count):
    W = _Win(NC, L)
    return [{sum(1 << W.idx(x, k) for x in range(NC) for k in range(L) if (x * 5 + k * 3 + t) % 4 == 0): F(1)}
            for t in range(count)]

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



def _energy_residual(n, L, v, coeff):
    """coeff H v minus the u(n) Sugawara form applied to v"""
    W = _Win(n, L)
    one = _one(n)
    lhs = _vsc(coeff, W.energy(v))
    r = {}
    for q in range(1, L):
        for x in range(n):
            for y in range(n):
                r = _vadd(r, W.cur(_E(n, y, x), -q, W.cur(_E(n, x, y), q, v)))
        r = _vadd(r, W.cur(one, -q, W.cur(one, q, v)))
    g0 = {}
    for x in range(n):
        for y in range(n):
            g0 = _vadd(g0, W.cur(_E(n, x, y), 0, W.cur(_E(n, y, x), 0, v)))
    r = _vadd(r, _vsc(F(1, 2), _vadd(g0, W.cur(one, 0, W.cur(one, 0, v)))))
    return _vadd(lhs, _vsc(-1, r))



def _identity_on_all_states(n, L, coeff):
    return all(_energy_residual(n, L, {S: F(1)}, coeff) == {} for S in range(1 << n * L))



def _identity_on_samples(coeff):
    W = _Win(NC, 3)
    samples = [sum(1 << W.idx(x, k) for x in range(NC) for k in range(3) if (x * 7 + k * 5 + t) % 3 == 0)
               for t in range(3)]
    return all(_energy_residual(NC, 3, {S: F(1)}, coeff) == {} for S in samples)



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




def _generic_ok(n, seed):
    C = _sym_tensor(n, seed)
    sym = all(C.get(k[2:] + k[:2]) == v for k, v in C.items())
    nonu = any(C.get((a, c, b, d), 0) != C.get((a, d, b, c), 0) for a, b, c, d in itertools.product(range(n), repeat=4))
    return sym and nonu


def _local_states():
    L, s = LOCAL_WIN
    W = _Win(NC, L)
    Om = W.sea(s)
    out = [Om]
    for spec in LOCAL_EXCITATIONS:
        v = Om
        for kind, x, k in spec:
            v = (fock.cre_on if kind == "c" else fock.ann_on)(W.idx(x, k), v)
        out.append(v)
    return out, W, Om


# module-level data
LOCAL_EXCITATIONS = ((("c", 4, 3),), (("a", 9, 2),), (("a", 6, 2), ("c", 1, 4)))
SAMPLE_COUNT = 3
SMALL_CASES = ((1, 4), (2, 3), (3, 3))
PLANES = 3
LEMMA_CASES = ((2, 3, 1), (2, 2, 5), (3, 2, 2))   # n, L, seed of the generic tensor
RAW_L = 2
LOCAL_WIN = (6, 3)


# ------------------------------------------------------------------ checks
def check_window_quadratic_form_lemma():
    premise("field-theory.imported-tower-limit")
    premise("synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves")
    GA.check("the Jordan-Wigner modes satisfy the Clifford relations of the tower planes", _tower_planes_ok(PLANES))
    GA.check("Phi(C) = sum (2l + 1) K_C c* c - Q(A_C)/2 on every state, generic symmetric C",
             all(_lemma_holds(n, L, seed) for n, L, seed in LEMMA_CASES))
    GA.check("144 basis states tested", sum(1 << n * L for n, L, seed in LEMMA_CASES) == 144)
    GA.check("the generic tensors are symmetric and not of u(n) type (A_C != 0)",
             all(_generic_ok(n, seed) for n, L, seed in LEMMA_CASES))
    return True


def check_window_energy_is_the_u_n_sugawara_form():
    premise("synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves")
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    GA.check("(n + 1) H equals the u(n) Sugawara form on every basis state of the small cases",
             all(_identity_on_all_states(n, L, n + 1) for n, L in SMALL_CASES))
    GA.check("592 basis states in the small cases", sum(1 << n * L for n, L in SMALL_CASES) == 592)
    GA.check("the coefficient is n + 1: with n it fails for n >= 2",
             not any(_identity_on_all_states(n, L, n) for n, L in SMALL_CASES if n > 1))
    GA.check("the identity on three sample states of the sixteen channels (coefficient 17)", _identity_on_samples(17))
    return True


def check_so10_casimir_tensor_identity():
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    so = _so10()
    GA.check("45 bilinears preserve V_+ and are traceless there",
             len(so) == 45 and all(M is not None and _tr(M) == 0 for M in so))
    D = _dual(so)
    GA.check("adjoint Casimir of so(10) in the trace-dual basis: 4", _lam(so, D, so[1]) == 4)
    C = _tensor(so, D)
    GA.check("Casimir in the 16: 45/16", _casimir_in_16(C) == F(45, 16))
    GA.check("A_so = -(3/16)(delta delta - delta delta), i.e. A_so = -3 A_N", _antisym_ratio(C) == {F(-3, 16)})
    GA.check("so: 2 (45/16) / 6 + 2 (1/16) / 2 = 1 and -(1/2)(-3/16)/6 - (1/2)(1/16)/2 = 0",
             2 * F(45, 16) / 6 + 2 * F(1, 16) / 2 == 1 and -F(1, 2) * F(-3, 16) / 6 - F(1, 2) * F(1, 16) / 2 == 0)
    u5 = so[:25]
    C5 = _tensor(u5, _dual(u5))
    GA.check("the u(5) part alone: A_C has entries off the support of Delta (the pair bilinears are needed)",
             "off" in _antisym_ratio(C5) and len(u5) == 25)
    return True


def check_window_energy_equals_so10_sugawara_plus_number():
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    res = _so10_identity_residuals(_sample_states(RAW_L, SAMPLE_COUNT), RAW_L)
    GA.check("H = H_so10 + H_N on arbitrary states of a two-level window", all(r == {} for r in res))
    vs, W, Om = _local_states()
    res2 = _so10_identity_residuals(vs, LOCAL_WIN[0])
    GA.check("H = H_so10 + H_N on the sea, charge +1, charge -1 and a particle-hole state", all(r == {} for r in res2))
    GA.check("seven states tested", len(res) + len(res2) == 7)
    GA.check("H = 8 s^2 = 72 on the sea of depth 3 (both sides nonzero)", W.energy(Om) == {list(Om)[0]: F(72)})
    return True
