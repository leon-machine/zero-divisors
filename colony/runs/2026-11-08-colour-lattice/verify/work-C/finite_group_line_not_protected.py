"""Referee C: the order-96 group G has no centre, so a fundamental line is not protected.

Exact computation, N_t = 1 periodic, links in G (the J-commuting signed permutations of e3..e8 fixing Re Omega,
J-complex monomial matrices with entries in {+-1, +-j} and determinant 1). Spatial graph: the 'theta' made of the
edge x-b and two length-3 paths x-p1-q1-b, x-p2-q2-b (two unit squares sharing the edge x-b). With temporal links
U_y and spatial links S_yz, the temporal plaquette of edge yz is S U_z S^-1 U_y^-1. We compute

    T = avg over all links in G of  P(x) * prod_{7 edges} w(plaquette),   P = t/3,  w = Re t / 3,

i.e. the coefficient of beta^7 from these seven plaquettes at first order in <P(x)>. For SU(3) every such term is
exactly zero (centre symmetry, proposal A (vi)); for G the degree-four invariant t^4 (average 1) lets three sheets
end on the line. Expected: (1/3)(1/18)^7.
"""
from fractions import Fraction as F
from itertools import permutations, product

N = 6


def jimg(m):
    return (m + 1, 1) if m % 2 == 0 else (m - 1, -1)


def cmat(g):
    M = [[(0, 0)] * 3 for _ in range(3)]
    for col in range(3):
        n, s = g[2 * col]
        M[n // 2][col] = (s, 0) if n % 2 == 0 else (0, s)
    return M


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def det(g):
    M = cmat(g)
    perm = [next(r for r in range(3) if M[r][c] != (0, 0)) for c in range(3)]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
    d = ((-1) ** inv, 0)
    for c in range(3):
        d = cmul(d, M[perm[c]][c])
    return d


def jcomm(g):
    for m in range(N):
        a, sa = jimg(m)
        n1, s1 = g[a]
        n2, s2 = g[m]
        b, sb = jimg(n2)
        if (n1, s1 * sa) != (b, sb * s2):
            return False
    return True


G = []
for p in permutations(range(N)):
    for sg in product((1, -1), repeat=N):
        g = tuple((p[m], sg[m]) for m in range(N))
        if jcomm(g) and det(g) == (1, 0):
            G.append(g)
assert len(G) == 96
idx = {g: i for i, g in enumerate(G)}


def compose(g, h):
    return tuple((g[h[m][0]][0], h[m][1] * g[h[m][0]][1]) for m in range(N))


def inverse(g):
    out = [None] * N
    for m, (n, s) in enumerate(g):
        out[n] = (m, s)
    return tuple(out)


n = len(G)
MUL = [[idx[compose(a, b)] for b in G] for a in G]
INV = [idx[inverse(a)] for a in G]


def tJ(g):
    M = cmat(g)
    return (sum(M[k][k][0] for k in range(3)), sum(M[k][k][1] for k in range(3)))


T = [tJ(g) for g in G]
W = [F(t[0], 3) for t in T]
# K[y][z] = avg_S w(S U_z S^-1 U_y^-1)
K = [[F(0)] * n for _ in range(n)]
for y in range(n):
    iy = INV[y]
    for z in range(n):
        acc = 0
        for s in range(n):
            acc += T[MUL[MUL[MUL[s][z]][INV[s]]][iy]][0]
        K[y][z] = F(acc, 3 * n)


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(n)) / n for j in range(n)] for i in range(n)]


K3 = matmul(matmul(K, K), K)          # path x-p-q-b, averaged over U_p, U_q
re = F(0)
im = F(0)
for x in range(n):
    for b in range(n):
        f = K[x][b] * K3[x][b] * K3[x][b]
        re += F(T[x][0], 3) * f
        im += F(T[x][1], 3) * f
re /= n * n
im /= n * n
print('theta-graph coefficient of beta^7 in <P(x)> for G:', re, '+ j', im)
assert (re, im) == (F(1, 3) * F(1, 18) ** 7, 0)
# control: the same seven plaquettes with the junction replaced by a Z3-allowed one cannot end a single line;
# and the pair-of-paths (no direct edge) gives zero: a line needs the t^4 vertex
re2 = sum(F(T[x][0], 3) * K3[x][b] * K3[x][b] for x in range(n) for b in range(n)) / (n * n)
assert re2 == 0
print('control (two paths only, junction t^3 at x): 0. For SU(3) the term is exactly 0 by centre symmetry.')
