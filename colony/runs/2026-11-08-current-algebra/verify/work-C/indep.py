"""Referee C independent recomputations (exact, Fractions). Own exterior-algebra code, own so(10) basis
(Majorana bilinears), own halving enumeration."""
from fractions import Fraction as F
from itertools import combinations, product

NM = 5
STATES = [S for r in range(6) for S in combinations(range(NM), r)]
EVEN = [S for S in STATES if len(S) % 2 == 0]
IDX = {S: i for i, S in enumerate(EVEN)}


def cre(i, S):
    if i in S:
        return None
    return (-1) ** sum(1 for x in S if x < i), tuple(sorted(S + (i,)))


def ann(i, S):
    if i not in S:
        return None
    return (-1) ** sum(1 for x in S if x < i), tuple(x for x in S if x != i)


def op_on(word, S):
    """word: list of ('c'|'a', mode) applied right to left"""
    sgn, T = 1, S
    for kind, m in reversed(word):
        r = (cre if kind == 'c' else ann)(m, T)
        if r is None:
            return None
        s, T = r
        sgn *= s
    return sgn, T


def mat(terms, basis=EVEN):
    """terms: list of (coef, word); returns dense matrix on basis (must preserve it)"""
    idx = {S: i for i, S in enumerate(basis)}
    n = len(basis)
    M = [[F(0)] * n for _ in range(n)]
    for j, S in enumerate(basis):
        for c, w in terms:
            r = op_on(w, S)
            if r is None:
                continue
            s, T = r
            assert T in idx, "leaves the half"
            M[idx[T]][j] += c * s
    return M


def mm(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n) if A[i][k]), F(0)) for j in range(n)] for i in range(n)]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def add(A, B, b=1):
    return [[A[i][j] + b * B[i][j] for j in range(len(A))] for i in range(len(A))]


def comm(A, B):
    return add(mm(A, B), mm(B, A), -1)


def inv(G):
    k = len(G)
    A = [list(r) + [F(int(i == j)) for j in range(k)] for i, r in enumerate(G)]
    for c in range(k):
        p = next(r for r in range(c, k) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(k):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [r[k:] for r in A]


# ---------------------------------------------------------------- (1) gl(5) trace identity, own code
def rho_E(a, b):
    return mat([(F(1), [('c', a), ('a', b)])])


E5 = {(a, b): rho_E(a, b) for a in range(5) for b in range(5)}
bad = 0
for (a, b), R in E5.items():
    for (c, d), R2 in E5.items():
        lhs = tr(mm(R, R2))
        rhs = 4 * (1 if (b == c and a == d) else 0) + 4 * (1 if a == b else 0) * (1 if c == d else 0)
        bad += lhs != rhs
print("(1) gl(5) identity tr16 = 4 tr5 + 4 tr tr: failures", bad)
Yd = [F(1, 2), F(1, 2), F(-1, 3), F(-1, 3), F(-1, 3)]
RY = [[F(0)] * 16 for _ in range(16)]
for a in range(5):
    RY = add(RY, E5[(a, a)], Yd[a])
print("    tr rho(Y)^2 =", tr(mm(RY, RY)), " tr rho(Y) =", tr(RY))

# ---------------------------------------------------------------- (2) so(10) in a Majorana basis
# gamma_{2a} = c_a + a_a, gamma_{2a+1} = c_a - a_a (squares +1, -1); so(10) spanned by gamma_p gamma_q, p<q
def gam(p):
    a = p // 2
    return [(F(1), [('c', a)]), (F(1) if p % 2 == 0 else F(-1), [('a', a)])]


def prod_terms(t1, t2):
    return [(c1 * c2, w1 + w2) for c1, w1 in t1 for c2, w2 in t2]


SO = [mat(prod_terms(gam(p), gam(q))) for p in range(10) for q in range(p + 1, 10)]
G = [[tr(mm(A, B)) for B in SO] for A in SO]
Gi = inv(G)
DU = []
for a in range(45):
    M = [[F(0)] * 16 for _ in range(16)]
    for b in range(45):
        if Gi[a][b]:
            M = add(M, SO[b], Gi[a][b])
    DU.append(M)
# Casimir tensor C[(x,y),(z,u)] = sum_A (M^A)_{xy} (M_A)_{zu}
C = {}
for M, Md in zip(SO, DU):
    nzM = [(z, u, M[z][u]) for z in range(16) for u in range(16) if M[z][u]]
    nzD = [(x, y, Md[x][y]) for x in range(16) for y in range(16) if Md[x][y]]
    for x, y, v in nzD:
        for z, u, w in nzM:
            C[(x, y, z, u)] = C.get((x, y, z, u), 0) + v * w
C = {k: v for k, v in C.items() if v}
sym = all(C.get((z, u, x, y), 0) == v for (x, y, z, u), v in C.items())
K = {}
for (x, y, z, u), v in C.items():
    if y == z:
        K[(x, u)] = K.get((x, u), 0) + v
K = {k: v for k, v in K.items() if v}
print("(2) Majorana-basis so(10): C symmetric", sym, "; K =", set(K.values()), "diag only", all(a == b for a, b in K))
ratios = set()
for a, b, c, d in product(range(16), repeat=4):
    dl = (a == c) * (b == d) - (a == d) * (b == c)
    av = C.get((a, c, b, d), 0) - C.get((a, d, b, c), 0)
    if dl:
        ratios.add(av / dl)
    elif av:
        ratios.add('off')
print("    A_C / Delta ratios:", ratios)
X = SO[3]
acc = [[F(0)] * 16 for _ in range(16)]
for M, Md in zip(SO, DU):
    acc = add(acc, comm(Md, comm(M, X)))
lams = {acc[i][j] / X[i][j] for i in range(16) for j in range(16) if X[i][j]}
print("    adjoint Casimir lambda:", lams)
# analytic: Casimirs (lambda, lambda + 2 rho) for D5 with rho = (4,3,2,1,0)
rho = [4, 3, 2, 1, 0]
def cas(w):
    return sum(F(x) * x for x in w) + 2 * sum(F(x) * r for x, r in zip(w, rho))
c16, c45, c120 = cas([F(1, 2)] * 5), cas([1, 1, 0, 0, 0]), cas([1, 1, 1, 0, 0])
sc = F(45, 16) / c16
print("    root-normalised C2: 16 ->", c16, " 45 ->", c45, " 120 ->", c120,
      "; trace-form: adj", c45 * sc, " Lambda^2 eigenvalue of C-hat", (c120 - 2 * c16) * sc / 2)
k_level = 2 * 8 / (c45 * sc)  # lambda = 2 h / k, h = 8
print("    level k = 2h/lambda =", k_level, " c(so10_k) =", F(k_level * 45) / (k_level + 8), " +1 =", F(k_level * 45) / (k_level + 8) + 1)
# u(5) subfamily via the Majorana route: number-conserving combos only
# ---------------------------------------------------------------- (3) halvings: tr Y, sea hypercharge, anomalies
def nk(S):
    n = sum(1 for x in S if x < 2)
    return n, len(S) - n

pairs = [((1, 0), (1, 3)), ((2, 0), (0, 3)), ((0, 1), (2, 2)), ((1, 1), (1, 2)), ((2, 1), (0, 2))]
def comp(c):
    return [S for S in STATES if nk(S) == c]
def ch(S):
    n, k = nk(S)
    t3 = sum(F(1, 2) if i == 0 else F(-1, 2) for i in S if i < 2)
    h3 = sum({2: F(1, 2), 3: F(-1, 2), 4: F(0)}[i] for i in S if i >= 2)
    h8 = sum({2: F(1), 3: F(1), 4: F(-2)}[i] for i in S if i >= 2)
    return t3, h3, h8, F(3 * n - 2 * k, 6)
trY0, free = [], []
quad = set()
for sg in product([0, 1], repeat=5):
    Vp = comp((0, 0)) + sum((comp(A if s == 0 else B) for s, (A, B) in zip(sg, pairs)), [])
    cs = [ch(S) for S in Vp]
    tY = sum(c[3] for c in cs)
    an = (tY, sum(c[3] ** 3 for c in cs), sum(c[3] * c[0] ** 2 for c in cs), sum(c[3] * c[1] ** 2 for c in cs),
          sum(c[2] ** 3 for c in cs))
    quad.add((sum(c[0] ** 2 for c in cs), sum(c[1] ** 2 for c in cs), sum(c[3] ** 2 for c in cs)))
    if tY == 0:
        trY0.append(sg)
    if all(x == 0 for x in an):
        free.append(sg)
print("(3) halvings with tr_{V+} Y = 0 (Y-N mixed central term zero, sea hypercharge zero):", len(trY0), "of 32;",
      "anomaly-free:", len(free), "; quadratic traces (T3^2, H3^2, Y^2) over all 32:", quad)
vals = sorted({sum(ch(S)[3] for S in comp((0, 0)) + sum((comp(A if s == 0 else B) for s, (A, B) in zip(sg, pairs)), []))
               for sg in product([0, 1], repeat=5)})
print("    values of tr_{V+} Y over the 32:", vals)
