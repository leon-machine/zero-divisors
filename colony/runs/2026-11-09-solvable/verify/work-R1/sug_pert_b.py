"""synthesis.gauge-factor-sugawara-parts-satisfy-virasoro-relations-on-the-band: exact checks.

The band domain D of n channels: a vector is a finite combination of states Delta, a state being a finite set of
flipped modes (k, x) relative to the sea {k < 0} of every channel; (k, x) is occupied iff (k < 0) xor (k, x) in
Delta. Modes are ordered top first (descending level, then channel), so the sign of c or c* at a mode,
(-1)^(occupied modes before it), is finite. The check verifies that these operators satisfy the canonical
anticommutation relations (the Clifford relations of the tower planes e = c* + c, f = c* - c, built in GA).
j^{xy}_m = sum_k c*_{x,k} c_{y,k+m}, zero modes counted from the sea; J(M)_m = sum M_xy j^{xy}_m.
The sixteen channels are the even states of Lambda C^5 (occupation basis); rho(X) is the action of X in gl(5) by
sum X_ab a*_a a_b on them; the gauge factors su(3), su(2), Y and the number current N as in the stored split.
L^f_n = (2 + lam_f)^{-1} sum_A sum_q :J(M^A)_{n-q} J(M_A)_q: (larger index on the right), M^A the tr_16-dual basis;
L_n = sum_{x,k} (k + 1/2 + n/2) :c*_{x,k} c_{x,k+n}: the band energy (L_0 = H counted from the sea);
L^c_n = L_n - sum_f L^f_n; L^so10_n the Sugawara sum of the 45 bilinears of the five modes.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise


# ------------------------------------------------------------------ the band domain
def _before(D, k, x, n):
    p = (n * (-1 - k) + x) if k < 0 else 0
    for (k2, x2) in D:
        if k2 > k or (k2 == k and x2 < x):
            p += 1
    return p % 2


def _occ(D, k, x):
    return (k < 0) != ((k, x) in D)


def _ann(D, k, x, n):
    if not _occ(D, k, x):
        return None
    return (-1 if _before(D, k, x, n) else 1), D ^ frozenset([(k, x)])


def _cre(D, k, x, n):
    if _occ(D, k, x):
        return None
    return (-1 if _before(D, k, x, n) else 1), D ^ frozenset([(k, x)])


def vadd(*vs):
    out = {}
    for v in vs:
        for s, c in v.items():
            out[s] = out.get(s, 0) + c
    return {s: c for s, c in out.items() if c}


def vsc(a, v):
    return {s: a * c for s, c in v.items() if a * c}


def ip(u, v):
    return sum((c * v.get(s, 0) for s, c in u.items()), F(0))


def energy_of(D):
    e = F(0)
    for (k, x) in D:
        e += F(2 * k + 1, 2) if k >= 0 else F(-2 * k - 1, 2)
    return e


def op_ann(k, x, n, v):
    out = {}
    for D, c in v.items():
        r = _ann(D, k, x, n)
        if r:
            out[r[1]] = out.get(r[1], 0) + r[0] * c
    return out


def op_cre(k, x, n, v):
    out = {}
    for D, c in v.items():
        r = _cre(D, k, x, n)
        if r:
            out[r[1]] = out.get(r[1], 0) + r[0] * c
    return out


class Band(object):
    def __init__(self, n):
        self.n = n

    def _hop(self, x, y, m, D):
        """the levels k at which c*_{x,k} c_{y,k+m} can act on D (all others give zero)"""
        ks = set(k for (k, xx) in D if xx == x and k < 0)
        ks |= set(k - m for (k, yy) in D if yy == y and k >= 0)
        if m < 0:
            ks |= set(range(0, -m))
        return ks

    def j(self, x, y, m, v, weight=None):
        n = self.n
        out = {}
        for D, c in v.items():
            if x == y and m == 0 and weight is None:
                q = sum(1 if k >= 0 else -1 for (k, xx) in D if xx == x)
                if q:
                    out[D] = out.get(D, 0) + q * c
                continue
            for k in self._hop(x, y, m, D):
                r = _ann(D, k + m, y, n)
                if r is None:
                    continue
                r2 = _cre(r[1], k, x, n)
                if r2 is None:
                    continue
                w = 1 if weight is None else weight(k)
                out[r2[1]] = out.get(r2[1], 0) + r[0] * r2[0] * c * w
        return {s: c for s, c in out.items() if c}

    def J(self, M, m, v):
        out = {}
        for (x, y, a) in M:
            for s, c in self.j(x, y, m, v).items():
                out[s] = out.get(s, 0) + a * c
        return {s: c for s, c in out.items() if c}

    def L(self, nn, v, shift=F(1, 2)):
        """band energy L_n = sum (k + shift + n/2) :c*_{x,k} c_{x,k+n}:, L_0 = H"""
        if nn == 0:
            return {D: energy_of(D) * c for D, c in v.items() if energy_of(D)}
        out = {}
        for x in range(self.n):
            out = vadd(out, self.j(x, x, nn, v, weight=lambda k: k + shift + F(nn, 2)))
        return out

    def sug(self, fac, nn, v, lam=None):
        """L^f_n for fac = (basis, dual, lam): normal ordered, larger mode index on the right"""
        B, Dl, lf = fac[0], fac[1], (fac[2] if lam is None else lam)
        E = max((energy_of(D) for D in v), default=F(0))
        Ei = E.numerator // E.denominator + 1
        out = {}
        for q in range(nn - Ei - 1, Ei + 2):
            r = nn - q
            for M, Md in zip(B, Dl):
                if q >= r:
                    t = self.J(M, q, v)
                    if t:
                        out = vadd(out, self.J(Md, r, t))
                else:
                    t = self.J(Md, r, v)
                    if t:
                        out = vadd(out, self.J(M, q, t))
        return vsc(F(1) / (2 + lf), out)


def comm_on(A, B, v):
    return vadd(A(B(v)), vsc(-1, B(A(v))))


def vir_defect(Lop, m, nn, c, v):
    lhs = comm_on(lambda w: Lop(m, w), lambda w: Lop(nn, w), v)
    rhs = vsc(m - nn, Lop(m + nn, v))
    if m + nn == 0:
        rhs = vadd(rhs, vsc(c * F(m * m * m - m, 12), v))
    return vadd(lhs, vsc(-1, rhs))


# ------------------------------------------------------------------ the sixteen channels and the factors
NM = 5
CH = sorted([S for S in range(1 << NM) if fock.popcount(S) % 2 == 0], key=lambda S: (fock.popcount(S), S))
POS = {S: i for i, S in enumerate(CH)}
NC = len(CH)


def _zero(n):
    return [[F(0)] * n for _ in range(n)]


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
    return [[sum((A[i][l] * B[l][j] for l in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def _tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def _comm(A, B):
    return _lin((1, _mm(A, B)), (-1, _mm(B, A)))


def _rep(X, kind="ab"):
    M = _zero(NC)
    for a in range(NM):
        for b in range(NM):
            if not X[a][b]:
                continue
            for j, S in enumerate(CH):
                if kind == "ab":
                    w = fock.cre_on(a, fock.ann_on(b, {S: F(1)}))
                elif kind == "cc":
                    w = fock.cre_on(a, fock.cre_on(b, {S: F(1)}))
                else:
                    w = fock.ann_on(a, fock.ann_on(b, {S: F(1)}))
                for T, c in w.items():
                    M[POS[T]][j] += X[a][b] * c
    return M


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


def _trprod(A, B):
    Sa = [(i, j, A[i][j]) for i in range(len(A)) for j in range(len(A)) if A[i][j]]
    return sum((a * B[j][i] for (i, j, a) in Sa), F(0))


def _dual(B16):
    Gi = _inv([[_trprod(A, B) for B in B16] for A in B16])
    out = []
    for a in range(len(B16)):
        acc = _zero(len(B16[0]))
        for b in range(len(B16)):
            if Gi[a][b]:
                acc = _lin((1, acc), (Gi[a][b], B16[b]))
        out.append(acc)
    return out


def _lam(B, Dl, X):
    acc = _zero(len(X))
    for M, Md in zip(B, Dl):
        acc = _lin((1, acc), (1, _comm(Md, _comm(M, X))))
    vals = {acc[i][j] / X[i][j] for i in range(len(X)) for j in range(len(X)) if X[i][j]}
    ok = all(acc[i][j] == 0 for i in range(len(X)) for j in range(len(X)) if X[i][j] == 0)
    return vals.pop() if len(vals) == 1 and ok else None


def _sparse(M):
    return [(i, j, M[i][j]) for i in range(len(M)) for j in range(len(M)) if M[i][j]]


SU2 = [_e5(0, 1), _e5(1, 0), _lin((1, _e5(0, 0)), (-1, _e5(1, 1)))]
SU3 = [_e5(a, b) for a in (2, 3, 4) for b in (2, 3, 4) if a != b] + \
      [_lin((1, _e5(2, 2)), (-1, _e5(3, 3)))]
Y5 = _lin((F(1, 2), _e5(0, 0)), (F(1, 2), _e5(1, 1)), (F(-1, 3), _e5(2, 2)), (F(-1, 3), _e5(3, 3)),
          (F(-1, 3), _e5(4, 4)))
_CACHE = {}


def factors():
    """[(name, sparse basis, sparse dual, lam, dim)] for su(3), su(2), Y, N"""
    if 'f' not in _CACHE:
        out = []
        for name, B5 in (("su3", SU3), ("su2", SU2), ("Y", [Y5])):
            B = [_rep(X) for X in B5]
            Dl = _dual(B)
            lam = _lam(B, Dl, B[0]) if len(B) > 1 else F(0)
            out.append((name, [_sparse(M) for M in B], [_sparse(M) for M in Dl], lam, len(B)))
        one = [[F(int(i == j)) for j in range(NC)] for i in range(NC)]
        out.append(("N", [_sparse(one)], [_sparse([[x / NC for x in r] for r in one])], F(0), 1))
        _CACHE['f'] = out
    return _CACHE['f']


def so10():
    if 'so' not in _CACHE:
        one = [[F(int(i == j)) for j in range(NC)] for i in range(NC)]
        B = []
        for a in range(NM):
            for b in range(NM):
                M = _rep(_e5(a, b))
                B.append(_lin((1, M), (F(-1, 2), one)) if a == b else M)
        for a in range(NM):
            for b in range(a + 1, NM):
                B.append(_rep(_e5(a, b), "cc"))
                B.append(_rep(_e5(a, b), "aa"))
        Dl = _dual(B)
        _CACHE['so'] = ("so10", [_sparse(M) for M in B], [_sparse(M) for M in Dl], _lam(B, Dl, B[3]), len(B),
                        all(_tr(M) == 0 for M in B))
    return _CACHE['so']


def fac3(d):
    return (d[1], d[2], d[3])


BAND = Band(NC)
OMEGA = {frozenset(): F(1)}


def sample_vectors():
    """the sea, a particle-hole excitation of su(2), a charged vector, a two-level hop between channels 5 and 9"""
    fd = factors()
    return [OMEGA, BAND.J(fd[1][1][0], -1, OMEGA), {frozenset([(0, 3)]): F(1)}, BAND.j(5, 9, -2, OMEGA)]


PAIRS = [(-2, 2), (-1, 1), (-3, 3), (-2, 1), (-1, 2), (1, 2), (-2, -1)]
PAIRS_F = [(-2, 2), (-1, 1), (-2, 1), (1, 2)]
SHIFTS = [(-2, 1), (-1, -1), (1, 2), (2, -1), (1, -1)]


# ------------------------------------------------------------------ test runners (sample data live here)
CAR_N = 3
CAR_MODES = [(k, x) for k in (-2, -1, 0, 1) for x in range(CAR_N)]
CAR_VECS = [{frozenset(): F(1)}, {frozenset([(0, 1), (-1, 2)]): F(1)}, {frozenset([(1, 0), (-2, 0), (0, 2)]): F(1)}]


def run_car():
    """returns (tests, failures) for the plane relations e^2 = 1, f^2 = -1, {e, f} = 0 at one mode and all
    anticommutators between distinct modes, with e = c* + c, f = c* - c; the scalars come from GA"""
    n = CAR_N
    sq = GA.sig(1, 1)
    e, f = GA.gen(0), GA.gen(1)
    se = GA.mul(e, e, sq).get((), F(0))
    sf = GA.mul(f, f, sq).get((), F(0))
    sef = GA.add(GA.mul(e, f, sq), GA.mul(f, e, sq)).get((), F(0))

    def E(md, v):
        return vadd(op_cre(md[0], md[1], n, v), op_ann(md[0], md[1], n, v))

    def Fm(md, v):
        return vadd(op_cre(md[0], md[1], n, v), vsc(-1, op_ann(md[0], md[1], n, v)))
    tests = bad = 0
    for v in CAR_VECS:
        for a in CAR_MODES:
            for lhs, rhs in ((E(a, E(a, v)), vsc(se, v)), (Fm(a, Fm(a, v)), vsc(sf, v)),
                             (vadd(E(a, Fm(a, v)), Fm(a, E(a, v))), vsc(sef, v))):
                tests += 1
                bad += 1 if vadd(lhs, vsc(-1, rhs)) else 0
            for b in CAR_MODES:
                if a == b:
                    continue
                for X in (E, Fm):
                    for Yy in (E, Fm):
                        tests += 1
                        bad += 1 if vadd(X(a, Yy(b, v)), Yy(b, X(a, v))) else 0
    return tests, bad


def run_zero_mode():
    """charge and energy of a sample state: (j^{11}_0 eigenvalue, H eigenvalue)"""
    D = frozenset([(0, 1), (-1, 1), (-2, 1), (-1, 2)])
    w = Band(CAR_N).j(1, 1, 0, {D: F(1)})
    return w.get(D, F(0)), energy_of(D)


def run_band_virasoro(c, shift=F(1, 2), pairs=None):
    vs = sample_vectors()
    tests = bad = 0
    for v in vs:
        for (m, nn) in (PAIRS if pairs is None else pairs):
            tests += 1
            bad += 1 if vir_defect(lambda a, w: BAND.L(a, w, shift=shift), m, nn, c, v) else 0
    return tests, bad


def run_band_shifts():
    vs = sample_vectors()[:3]
    tests = bad = 0
    for v in vs:
        for (nn, m) in SHIFTS:
            for (x, y) in ((0, 7), (4, 4), (12, 2)):
                tests += 1
                d = vadd(comm_on(lambda w: BAND.L(nn, w), lambda w: BAND.j(x, y, m, w), v),
                         vsc(m, BAND.j(x, y, m + nn, v)))
                bad += 1 if d else 0
    return tests, bad


def run_factor_shifts(lam_shift=F(0), which=None):
    """own-current shift and commutation with the next factor's first current; returns (tests, failures)"""
    fd = factors()
    vs = sample_vectors()[:2]
    tests = bad = 0
    for i, d in enumerate(fd):
        if which is not None and i != which:
            continue
        own = d[1][0]
        other = fd[(i + 1) % len(fd)][1][0]
        for v in vs:
            for (nn, m) in SHIFTS:
                tests += 2
                Lf = (lambda w: BAND.sug(fac3(d), nn, w, lam=d[3] + lam_shift))
                lhs = comm_on(Lf, lambda w: BAND.J(own, m, w), v)
                bad += 1 if vadd(lhs, vsc(m, BAND.J(own, m + nn, v))) else 0
                bad += 1 if comm_on(Lf, lambda w: BAND.J(other, m, w), v) else 0
    return tests, bad


def central_values():
    return [2 * F(d[4]) / (2 + d[3]) for d in factors()]


def run_factor_virasoro(which, c_shift=F(0), lam_shift=F(0), pairs=None):
    fd = factors()
    vs = sample_vectors()[:3]
    tests = bad = 0
    for i, (d, c) in enumerate(zip(fd, central_values())):
        if i not in which:
            continue
        Lf = (lambda nn, w, d=d: BAND.sug(fac3(d), nn, w, lam=d[3] + lam_shift))
        for v in vs:
            for (m, nn) in (PAIRS_F if pairs is None else pairs):
                tests += 1
                bad += 1 if vir_defect(Lf, m, nn, c + c_shift, v) else 0
    return tests, bad


def _Lc(nn, v):
    out = BAND.L(nn, v)
    for d in factors():
        out = vadd(out, vsc(-1, BAND.sug(fac3(d), nn, v)))
    return out


def coset_charge():
    return NC - sum(central_values())


def run_coset_virasoro(c_shift=F(0)):
    vs = sample_vectors()
    tests = bad = 0
    for v, (m, nn) in ((vs[0], (-2, 2)), (vs[0], (-3, 3)), (vs[1], (-1, 2)), (vs[2], (-1, 1))):
        tests += 1
        bad += 1 if vir_defect(_Lc, m, nn, coset_charge() + c_shift, v) else 0
    return tests, bad


def run_coset_commutation():
    fd = factors()
    v = sample_vectors()[1]
    tests = bad = 0
    for (nn, m) in ((-1, 1), (1, -1)):
        for d in fd:
            X = d[1][0]
            tests += 1
            bad += 1 if comm_on(lambda w: _Lc(nn, w), lambda w: BAND.J(X, m, w), v) else 0
    for i, d in enumerate(fd):
        e = fd[(i + 1) % len(fd)]
        tests += 2
        bad += 1 if comm_on(lambda w: _Lc(-1, w), lambda w: BAND.sug(fac3(d), 1, w), v) else 0
        bad += 1 if comm_on(lambda w: BAND.sug(fac3(e), -1, w), lambda w: BAND.sug(fac3(d), 2, w), v) else 0
    return tests, bad


def run_so10(n_u5=None):
    """L_n = L^so10_n + L^N_n on three sample vectors for n in MODES_SO10; with n_u5 the so(10) family is cut to its
    first n_u5 elements (the u(5) bilinears for 25)"""
    so = so10()
    N = factors()[-1]
    fam = (so[1], so[2], so[3]) if n_u5 is None else (so[1][:n_u5], so[2][:n_u5], so[3])
    vs = sample_vectors()
    tests = bad = 0
    for v in (vs[0], vs[2], vs[3]):
        for nn in MODES_SO10:
            tests += 1
            s = vadd(BAND.sug(fam, nn, v), BAND.sug(fac3(N), nn, v))
            bad += 1 if vadd(s, vsc(-1, BAND.L(nn, v))) else 0
    return tests, bad


MODES_SO10 = (-2, -1, 0, 1, 2)


def run_vacuum():
    """(annihilation failures, norms of L^f_{-2} Omega, norms of L^f_{-3} Omega, adjoint failures, remainder norms)"""
    fd = factors()
    vs = sample_vectors()
    ann_bad = adj_bad = 0
    n2, n3 = [], []
    for d in fd:
        Lf = (lambda nn, w, d=d: BAND.sug(fac3(d), nn, w))
        for nn in (-1, 0, 1, 2):
            ann_bad += 1 if Lf(nn, OMEGA) else 0
        w2, w3 = Lf(-2, OMEGA), Lf(-3, OMEGA)
        n2.append(ip(w2, w2))
        n3.append(ip(w3, w3))
        u, w = vs[1], vs[3]
        for nn in (1, 2):
            adj_bad += 0 if ip(u, Lf(nn, w)) == ip(Lf(-nn, u), w) else 1
            adj_bad += 0 if ip(w, Lf(nn, u)) == ip(Lf(-nn, w), u) else 1
    wc, w3 = _Lc(-2, OMEGA), _Lc(-3, OMEGA)
    return ann_bad, n2, n3, adj_bad, (ip(wc, wc), ip(w3, w3))


# ------------------------------------------------------------------ checks
def check_band_operators_realise_the_tower_modes():
    """{c_a, c*_b} = delta_ab, {c_a, c_b} = 0 on D near the sea, as the GA Clifford relations of the tower planes
    e = c* + c, f = c* - c; zero modes and energy counted from the sea."""
    premise("field-theory.imported-tower-limit")
    premise("synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves")
    tests, bad = run_car()
    q, h = run_zero_mode()
    ok = tests == 1692 and bad == 0 and q == -1 and h == 3
    GA.check("band operators: the CAR as the Clifford relations of the tower planes (1692 relations), zero modes"
             " counted from the sea", ok)
    return ok


def check_band_energy_is_virasoro_at_sixteen_and_shifts_every_pair_current():
    """L_n of the sixteen channels: [L_m, L_n] = (m - n) L_{m+n} + (16/12)(m^3 - m) delta; [L_n, j^{xy}_m] =
    -m j^{xy}_{m+n}; c = 15 fails, and the weight k + n/2 instead of k + 1/2 + n/2 fails."""
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    premise("synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves")
    t1, b1 = run_band_virasoro(F(16))
    t2, b2 = run_band_shifts()
    t3, b3 = run_band_virasoro(F(15))
    t4, b4 = run_band_virasoro(F(16), shift=F(0))
    ok = (t1, b1, t2, b2) == (28, 0, 45, 0) and b3 == 8 and b4 == 12
    GA.check("band energy of the sixteen channels: Virasoro at c = 16 and the shift of every pair current", ok)
    return ok


def check_factor_parts_shift_their_own_currents_at_every_mode():
    """[L^f_n, J(rho X)_m] = -m J(rho X)_{m+n} for X in f and 0 for X in another factor or N, for n != 0 (the stored
    case is n = 0); lam = 3/2, 1, 0, 0; with lam + 1 in place of lam the shift fails."""
    premise("synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split")
    lams = [d[3] for d in factors()]
    t1, b1 = run_factor_shifts()
    t2, b2 = run_factor_shifts(lam_shift=F(1), which=1)
    ok = lams == [F(3, 2), F(1), F(0), F(0)] and (t1, b1) == (80, 0) and b2 == 4
    GA.check("each factor's Sugawara mode L^f_n shifts its own currents by n and commutes with the other factors",
             ok)
    return ok


def check_factor_parts_satisfy_virasoro_relations():
    """[L^f_m, L^f_n] = (m - n) L^f_{m+n} + (c_f/12)(m^3 - m) delta_{m+n,0}, c_f = 2 dim f/(2 + lam_f) =
    32/7, 2, 1, 1; with c_f + 1 or lam_f + 1 the relations fail."""
    premise("synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split")
    cs = central_values()
    t1, b1 = run_factor_virasoro([0, 1, 2, 3])
    t2, b2 = run_factor_virasoro([1], c_shift=F(1))
    t3, b3 = run_factor_virasoro([1], lam_shift=F(1))
    ok = cs == [F(32, 7), F(2), F(1), F(1)] and (t1, b1) == (48, 0) and b2 == 3 and b3 == 7
    GA.check("su(3), su(2), hypercharge and number Sugawara parts: Virasoro on D with c = 32/7, 2, 1, 1", ok)
    return ok


def check_remainder_is_a_virasoro_algebra_at_fifty_two_sevenths_commuting_with_the_factors():
    """L^c = L - sum_f L^f: Virasoro at c = 16 - 32/7 - 2 - 1 - 1 = 52/7; commutes with every gauge and number
    current and with every L^f_n; distinct factors' parts commute."""
    premise("synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split")
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    t1, b1 = run_coset_virasoro()
    t2, b2 = run_coset_virasoro(c_shift=F(1))
    t3, b3 = run_coset_commutation()
    ok = coset_charge() == F(52, 7) and (t1, b1) == (4, 0) and b2 == 2 and (t3, b3) == (16, 0)
    GA.check("remainder L - sum_f L^f: Virasoro at c = 52/7, commuting with the gauge currents and the factor parts",
             ok)
    return ok


def check_band_energy_is_so10_plus_number_at_every_mode():
    """L_n = L^so10_n + L^N_n on D (the stored identity is n = 0); lam_so10 = 4, c = 15; so the remainder is
    L^so10 - L^su3 - L^su2 - L^Y; the u(5) bilinears alone do not give L_n."""
    premise("synthesis.window-energy-of-one-generation-is-exactly-the-so10-sugawara-energy")
    so = so10()
    t1, b1 = run_so10()
    t2, b2 = run_so10(n_u5=25)
    ok = (so[3], so[4], so[5]) == (4, 45, True) and 2 * F(so[4]) / (2 + so[3]) == 15
    ok = ok and (t1, b1) == (15, 0) and b2 == 8
    GA.check("band energy = so(10) Sugawara + number Sugawara at the modes tested on D; u(5) alone fails", ok)
    return ok


def check_vacuum_norms_and_adjoints():
    """L^f_n Omega = 0 for n >= -1; ||L^f_{-m} Omega||^2 = (c_f/12)(m^3 - m) for m = 2, 3; the remainder's 26/7 and
    104/7; <u, L^f_n w> = <L^f_{-n} u, w>."""
    premise("synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split")
    ann_bad, n2, n3, adj_bad, rem = run_vacuum()
    ok = ann_bad == 0 and adj_bad == 0
    ok = ok and n2 == [F(16, 7), F(1), F(1, 2), F(1, 2)] and n3 == [F(64, 7), F(4), F(2), F(2)]
    ok = ok and rem == (F(26, 7), F(104, 7))
    GA.check("factor and remainder modes annihilate the sea for n >= -1; level-two and level-three norms; adjoints", ok)
    return ok


if __name__ == "__main__":
    import time
    for fn in (check_band_operators_realise_the_tower_modes,
               check_band_energy_is_virasoro_at_sixteen_and_shifts_every_pair_current,
               check_factor_parts_shift_their_own_currents_at_every_mode,
               check_factor_parts_satisfy_virasoro_relations,
               check_remainder_is_a_virasoro_algebra_at_fifty_two_sevenths_commuting_with_the_factors,
               check_band_energy_is_so10_plus_number_at_every_mode,
               check_vacuum_norms_and_adjoints):
        t = time.time()
        print(fn.__name__, fn(), round(time.time() - t, 1))
