"""Referee G, own route (Fock space, exact): quasi-spin proposal (ii) normality criterion and (iv) quasi-spin norms."""
import sys; sys.path.insert(0, sys.path[0])
from fock import *
import itertools
from math import factorial

J = num(0, 1)
def rho(fk, W, chans, q, M):
    return Bilinear(fk, [(M[a][b], (k, chans[a]), (k + q, chans[b])) for k in W if k + q in W
                         for a in range(len(chans)) for b in range(len(chans))])
def madj(M): return [[nconj(M[j][i]) for j in range(len(M))] for i in range(len(M))]
def mmul(A, B):
    n = len(A); out = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n): out[i][j] = nadd(out[i][j], nmul(A[i][k], B[k][j]))
    return out
def is_normal(M): return mmul(M, madj(M)) == mmul(madj(M), M)

# ---- (ii): window N = 2 (I = {-2, -1, 0, 1}), two channels, q = 1; edge-clean: k = -2 filled, k = 1 empty, k = -1, 0 free
W = [-2, -1, 0, 1]; ch = ['+', '-']
fk = Fock([(k, c) for k in W for c in ch])
free = [(k, c) for k in (-1, 0) for c in ch]
edge_clean = []
for bits in itertools.product((0, 1), repeat=4):
    occ = frozenset([(-2, '+'), (-2, '-')] + [md for md, b in zip(free, bits) if b])
    edge_clean.append({occ: ONE})
Ms = {
    'hermitian [[2, 1+J], [1-J, 0]]': [[num(2), num(1, 1)], [num(1, -1), num(0)]],
    'unitary [[0, J], [J, 0]]': [[num(0), J], [J, num(0)]],
    'normal [[1, J], [J, 1]]': [[num(1), J], [J, num(1)]],
    'non-normal [[1, 1], [0, 1]]': [[num(1), num(1)], [num(0), num(1)]],
    'E_{+-} (helicity +1)': [[num(0), num(1)], [num(0), num(0)]],
    'J E_{-+} (helicity -1)': [[num(0), num(0)], [J, num(0)]],
}
for name, M in Ms.items():
    A = rho(fk, W, ch, 1, M); Ad = A.adj()
    vals = set()
    scalar = True
    for st in edge_clean:
        out = comm(A, Ad, st)
        (occ, z), = st.items()
        # scalar test: out == lambda * st
        lam = out.get(occ, ZERO)
        if sadd(out, sneg(sscale(lam, st))) != {}: scalar = False
        vals.add(lam)
    trMM = sum(nabs2(M[i][j]) for i in range(2) for j in range(2))
    print(f'{name:32s} normal={is_normal(M)!s:5s} eigen on each basis vector={scalar!s:5s} one scalar on the subspace={len(vals)==1!s:5s} values={sorted(v[0] for v in vals) if all(v[1]==0 for v in vals) else vals}  q tr(M*M)={trMM}')

# ---- (iv): four channels, weights (1/2, 1/2, -1/2, -1/2); helicity +1 block M = [[0, K], [0, 0]], K = [[1, J], [0, 2]]
ch4 = ['a', 'b', 'c', 'd']
K = [[num(1), J], [num(0), num(2)]]
M = [[ZERO] * 4 for _ in range(4)]
for i in range(2):
    for j in range(2): M[i][j + 2] = K[i][j]
assert mmul(M, M) == [[ZERO] * 4 for _ in range(4)]
# eigenvalues of K*K: trace 6, det 4 -> generating polynomial (1 + 6t + 4t^2)^q for e_p
def e_poly(q):
    poly = [F(1)]
    for _ in range(q):
        new = [F(0)] * (len(poly) + 2)
        for i, c in enumerate(poly):
            new[i] += c; new[i + 1] += 6 * c; new[i + 2] += 4 * c
        poly = new
    return poly
for N, q in ((2, 1), (2, 2), (3, 2)):
    Wn = list(range(-N, N))
    fk4 = Fock([(k, c) for k in Wn for c in ch4])
    Om = {frozenset((k, c) for k in Wn if k < 0 for c in ch4): ONE}
    B = rho(fk4, Wn, ch4, q, M).adj()
    ep = e_poly(q)
    st = Om; rows = []
    for p in range(0, 2 * q + 2):
        if p: st = B(st)
        want = factorial(p) ** 2 * (ep[p] if p < len(ep) else 0)
        rows.append((p, norm2(st), want))
    b1 = rows[1][1]
    print(f'N={N} q={q}: |B^p Omega|^2 vs (p!)^2 e_p:', [(p, g, w, 'OK' if g == w else 'X') for p, g, w in rows],
          ' Bose comparison p! |B Omega|^(2p):', [factorial(p) * b1 ** p for p, _, _ in rows[:4]])
