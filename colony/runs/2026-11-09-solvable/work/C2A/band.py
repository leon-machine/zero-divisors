"""Exact band domain D (semi-infinite sea) for n channels, and Sugawara/Virasoro operators on it.

A state of D is a finite set Delta of flipped modes (k, x) relative to the sea {k < 0}: (k, x) is occupied iff
(k < 0) xor ((k, x) in Delta). Modes are ordered top first (descending k, then ascending x); the fermion sign of
c or c* at mode (k, x) is (-1)^(number of occupied modes before it), finite since only finitely many modes lie
above any level.
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, '/home/claude/phys-graph/lib')
import fock  # noqa: E402


def _before_parity(D, k, x, n):
    p = (n * (-1 - k) + x) if k < 0 else 0
    for (k2, x2) in D:
        if k2 > k or (k2 == k and x2 < x):
            p += 1
    return p & 1


def occ(D, k, x):
    return (k < 0) != ((k, x) in D)


def ann(D, k, x, n):
    if not occ(D, k, x):
        return None
    s = -1 if _before_parity(D, k, x, n) else 1
    return s, D ^ frozenset([(k, x)])


def cre(D, k, x, n):
    if occ(D, k, x):
        return None
    s = -1 if _before_parity(D, k, x, n) else 1
    return s, D ^ frozenset([(k, x)])


def vadd(*vs):
    out = {}
    for v in vs:
        for s, c in v.items():
            out[s] = out.get(s, 0) + c
    return {s: c for s, c in out.items() if c}


def vsc(a, v):
    return {s: a * c for s, c in v.items() if a * c}


def energy_of(D):
    e = F(0)
    for (k, x) in D:
        e += F(2 * k + 1, 2) if k >= 0 else F(-2 * k - 1, 2)
    return e


def maxE(v):
    return max((energy_of(D) for D in v), default=F(0))


class Band(object):
    def __init__(self, n):
        self.n = n

    def j(self, x, y, m, v):
        """pair current j^{xy}_m = sum_k c*_{x,k} c_{y,k+m}, normal ordered (zero modes from the sea)"""
        n = self.n
        out = {}
        for D, c in v.items():
            if x == y and m == 0:
                q = sum(1 if k >= 0 else -1 for (k, xx) in D if xx == x)
                if q:
                    out[D] = out.get(D, 0) + q * c
                continue
            ks = set(k for (k, xx) in D if xx == x and k < 0)
            ks |= set(k - m for (k, yy) in D if yy == y and k >= 0)
            if m < 0:
                ks |= set(range(0, -m))
            for k in ks:
                r = ann(D, k + m, y, n)
                if r is None:
                    continue
                r2 = cre(r[1], k, x, n)
                if r2 is None:
                    continue
                out[r2[1]] = out.get(r2[1], 0) + r[0] * r2[0] * c
        return {s: c for s, c in out.items() if c}

    def J(self, M, m, v):
        """J(M)_m = sum M_xy j^{xy}_m, M a sparse list [(x, y, a)]"""
        out = {}
        for (x, y, a) in M:
            for s, c in self.j(x, y, m, v).items():
                out[s] = out.get(s, 0) + a * c
        return {s: c for s, c in out.items() if c}

    def Lfree(self, nn, v):
        """L_n = sum_x sum_k (k + 1/2 + n/2) c*_{x,k} c_{x,k+n} (n != 0); L_0 = H normal ordered"""
        if nn == 0:
            return {D: energy_of(D) * c for D, c in v.items() if energy_of(D)}
        out = {}
        for D, c in v.items():
            for x in range(self.n):
                ks = set(k for (k, xx) in D if xx == x and k < 0)
                ks |= set(k - nn for (k, yy) in D if yy == x and k >= 0)
                if nn < 0:
                    ks |= set(range(0, -nn))
                for k in ks:
                    r = ann(D, k + nn, x, self.n)
                    if r is None:
                        continue
                    r2 = cre(r[1], k, x, self.n)
                    if r2 is None:
                        continue
                    w = F(2 * k + 1 + nn, 2)
                    out[r2[1]] = out.get(r2[1], 0) + r[0] * r2[0] * c * w
        return {s: c for s, c in out.items() if c}

    def sug(self, B, Dl, lam, nn, v):
        """L^f_n = (2 + lam)^{-1} sum_A sum_q :J(M^A)_{n-q} J(M_A)_q:, larger index on the right"""
        out = {}
        E = maxE(v)
        Ei = int(E) + 1
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
        return vsc(F(1) / (2 + lam), out)


# ----------------------------------------------------------- the sixteen channels
NM = 5
CH = sorted([S for S in range(1 << NM) if fock.popcount(S) % 2 == 0], key=lambda S: (fock.popcount(S), S))
POS = {S: i for i, S in enumerate(CH)}
NC = len(CH)


def zero(n):
    return [[F(0)] * n for _ in range(n)]


def e5(a, b):
    M = zero(NM)
    M[a][b] = F(1)
    return M


def lin(*pairs):
    n = len(pairs[0][1])
    out = zero(n)
    for c, X in pairs:
        for i in range(n):
            for j in range(n):
                out[i][j] += F(c) * X[i][j]
    return out


def mm(A, B):
    return [[sum((A[i][l] * B[l][j] for l in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def comm(A, B):
    return lin((1, mm(A, B)), (-1, mm(B, A)))


def rep(X, kind="ab"):
    M = zero(NC)
    for a in range(NM):
        for b in range(NM):
            if X[a][b]:
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


def inv(G):
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


def dual(B16):
    Gi = inv([[tr(mm(A, B)) for B in B16] for A in B16])
    out = []
    for a in range(len(B16)):
        acc = zero(len(B16[0]))
        for b in range(len(B16)):
            if Gi[a][b]:
                acc = lin((1, acc), (Gi[a][b], B16[b]))
        out.append(acc)
    return out


def lam_of(B, Dl, X):
    acc = zero(len(X))
    for M, Md in zip(B, Dl):
        acc = lin((1, acc), (1, comm(Md, comm(M, X))))
    vals = {acc[i][j] / X[i][j] for i in range(len(X)) for j in range(len(X)) if X[i][j]}
    ok = all(acc[i][j] == 0 for i in range(len(X)) for j in range(len(X)) if X[i][j] == 0)
    return vals.pop() if len(vals) == 1 and ok else None


def sparse(M):
    return [(i, j, M[i][j]) for i in range(len(M)) for j in range(len(M)) if M[i][j]]


SU2 = [e5(0, 1), e5(1, 0), lin((1, e5(0, 0)), (-1, e5(1, 1)))]
SU3 = [e5(a, b) for a in (2, 3, 4) for b in (2, 3, 4) if a != b] + \
      [lin((1, e5(2, 2)), (-1, e5(3, 3))), lin((1, e5(3, 3)), (-1, e5(4, 4)))]
Y5 = lin((F(1, 2), e5(0, 0)), (F(1, 2), e5(1, 1)), (F(-1, 3), e5(2, 2)), (F(-1, 3), e5(3, 3)),
         (F(-1, 3), e5(4, 4)))


def factor_data():
    out = []
    for name, B5 in (("su3", SU3), ("su2", SU2), ("Y", [Y5])):
        B = [rep(X) for X in B5]
        Dl = dual(B)
        lam = lam_of(B, Dl, B[0]) if len(B) > 1 else F(0)
        out.append((name, [sparse(M) for M in B], [sparse(M) for M in Dl], lam, len(B)))
    one = [[F(int(i == j)) for j in range(NC)] for i in range(NC)]
    out.append(("N", [sparse(one)], [sparse([[x / NC for x in r] for r in one])], F(0), 1))
    return out
