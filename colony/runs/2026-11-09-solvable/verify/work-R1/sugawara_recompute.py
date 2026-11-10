"""R1: adjoint Casimirs lambda of su(3), su(2), so(10) relative to tr_16 on the even part of Lambda C^5, computed
from explicit fermion bilinears (own construction), and the central charges 2 dim/(2 + lambda), compared with the
level-k formula k dim/(k + h) with k read from the Dynkin index (k = tr_16 / tr_fund for su(N); for so(10) the
vector-index normalisation tr_16 = k * tr_10 / 2 * 2^(...) is avoided by using lambda directly)."""
from fractions import Fraction as F
from itertools import combinations

NM = 5
states = [S for S in range(1 << NM) if bin(S).count("1") % 2 == 0]
idx = {S: i for i, S in enumerate(states)}
n = len(states)


def sign(S, a):
    return -1 if bin(S & ((1 << a) - 1)).count("1") % 2 else 1


def op_cdag(a, S):
    if S >> a & 1:
        return None
    return sign(S, a), S | (1 << a)


def op_c(a, S):
    if not S >> a & 1:
        return None
    return sign(S, a), S & ~(1 << a)


def bil(ops):
    """matrix of a product of fermion ops (applied right to left) restricted to even states"""
    M = [[F(0)] * n for _ in range(n)]
    for S in states:
        s, T = 1, S
        okk = True
        for kind, a in reversed(ops):
            r = (op_cdag if kind == "+" else op_c)(a, T)
            if r is None:
                okk = False
                break
            s *= r[0]
            T = r[1]
        if okk:
            M[idx[T]][idx[S]] += s
    return M


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def sub(A, B):
    return [[a - b for a, b in zip(r, s)] for r, s in zip(A, B)]


def lin(*terms):
    M = [[F(0)] * n for _ in range(n)]
    for c, X in terms:
        M = [[m + c * x for m, x in zip(r, s)] for r, s in zip(M, X)]
    return M


def tr(A):
    return sum(A[i][i] for i in range(n))


def comm(A, B):
    return sub(mm(A, B), mm(B, A))


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


def casimir(B, X):
    G = [[tr(mm(a, b)) for b in B] for a in B]
    Gi = inv(G)
    out = [[F(0)] * n for _ in range(n)]
    for i, a in enumerate(B):
        for j, b in enumerate(B):
            if Gi[i][j] != 0:
                out = lin((1, out), (Gi[i][j], comm(a, comm(b, X))))
    # out = lambda X
    for i in range(n):
        for j in range(n):
            if X[i][j] != 0:
                return out[i][j] / X[i][j], G
    return None, G


E = lambda a, b: bil([("+", a), ("-", b)])
su2 = [E(0, 1), E(1, 0), sub(E(0, 0), E(1, 1))]
su3 = [E(a, b) for a in (2, 3, 4) for b in (2, 3, 4) if a != b] + [sub(E(2, 2), E(3, 3)), sub(E(3, 3), E(4, 4))]
one = [[F(int(i == j)) for j in range(n)] for i in range(n)]
so10 = [lin((1, E(a, b)), (F(-1, 2) if a == b else 0, one)) for a in range(5) for b in range(5)]
so10 += [bil([("+", a), ("+", b)]) for a, b in combinations(range(5), 2)]
so10 += [bil([("-", a), ("-", b)]) for a, b in combinations(range(5), 2)]
res = {}
for name, B, h, dimfund in (("su3", su3, 3, 3), ("su2", su2, 2, 2), ("so10", so10, 8, None)):
    lam, G = casimir(B, B[0])
    d = len(B)
    c = 2 * F(d) / (2 + lam)
    res[name] = (lam, c)
    print(f"{name}: dim {d}, lambda = {lam}, c = 2 dim/(2 + lambda) = {c}")
cY = F(1)
cN = F(1)
c_rem = 16 - res["su3"][1] - res["su2"][1] - cY - cN
print("remainder c =", c_rem, "; so10 c - gauge c =", res["so10"][1] - res["su3"][1] - res["su2"][1] - cY)
print("level-k check: su(3)_4:", F(4 * 8, 4 + 3), " su(2)_4:", F(4 * 3, 4 + 2), " so(10)_4:", F(4 * 45, 4 + 8))
