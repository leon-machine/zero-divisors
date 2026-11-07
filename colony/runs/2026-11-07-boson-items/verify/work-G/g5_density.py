"""Referee G, own route (Fock space, exact) for the dimension proposal:
(a) the strip identity in d = 2 as an operator identity on every basis vector (irregular window, one channel;
    and a 2 x 2 window with two channels and J-valued arrays M, M');
(b) counting: seas that are not half-spaces in one direction with nonzero form; the bounded sea at large q;
(c) the d = 3 density-current sum and its bounds, recomputed in floating point as a cross-check of the stated interval."""
import sys; sys.path.insert(0, sys.path[0])
from fock import *
import itertools, math

def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
def rho(fk, W, chans, q, M):
    Ws = set(W)
    return Bilinear(fk, [(M[a][b], (k, chans[a]), (vadd(k, q), chans[b])) for k in W if vadd(k, q) in Ws
                         for a in range(len(chans)) for b in range(len(chans))])
def site(fk, ks, chans, M):
    return Bilinear(fk, [(M[a][b], (k, chans[a]), (k, chans[b])) for k in ks for a in range(len(chans)) for b in range(len(chans))])
def madj(M): return [[nconj(M[j][i]) for j in range(len(M))] for i in range(len(M))]
def mmul(A, B):
    n = len(A); return [[(lambda s: s)(sum_n([nmul(A[i][k], B[k][j]) for k in range(n)])) for j in range(n)] for i in range(n)]
def sum_n(xs):
    s = ZERO
    for x in xs: s = nadd(s, x)
    return s

# (a1) irregular d = 2 window, one channel, all 2^|W| basis vectors
W = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (3, 1)]
fk = Fock([(k, 0) for k in W]); one = [[ONE]]
ok_all = True
for q in [(1, 0), (1, 1), (1, -1), (2, 0), (3, 1), (0, 1)]:
    lo = [k for k in W if vadd(k, q) in set(W)]; hi = [k for k in W if tuple(x - y for x, y in zip(k, q)) in set(W)]
    A = rho(fk, W, [0], q, one); L = site(fk, lo, [0], one); H = site(fk, hi, [0], one)
    for bits in itertools.product((0, 1), repeat=len(W)):
        st = {frozenset((k, 0) for k, b in zip(W, bits) if b): ONE}
        if comm(A, A.adj(), st) != sadd(L(st), sneg(H(st))): ok_all = False
print('(a1) strip identity, irregular d = 2 window, 6 momenta x 64 basis vectors x 6 q:', ok_all)
# (a2) 2 x 2 window, two channels, M and M' with J entries
J = num(0, 1)
W2 = [(x, y) for x in range(2) for y in range(2)]; ch = ['u', 'd']
fk2 = Fock([(k, c) for k in W2 for c in ch])
Mlist = [[[num(1), J], [num(2), num(0, -1)]], [[num(0), num(1, 1)], [num(1), num(3)]]]
ok2 = True
for q in [(1, 0), (0, 1), (1, 1), (1, -1)]:
    lo = [k for k in W2 if vadd(k, q) in set(W2)]; hi = [k for k in W2 if tuple(x - y for x, y in zip(k, q)) in set(W2)]
    for M, Mp in itertools.product(Mlist, repeat=2):
        A = rho(fk2, W2, ch, q, M); Bd = rho(fk2, W2, ch, q, Mp).adj()
        L = site(fk2, lo, ch, mmul(M, madj(Mp))); H = site(fk2, hi, ch, mmul(madj(Mp), M))
        for bits in itertools.product((0, 1), repeat=8):
            st = {frozenset(md for md, b in zip(fk2.modes, bits) if b): ONE}
            if comm(A, Bd, st) != sadd(L(st), sneg(H(st))): ok2 = False
print('(a2) strip identity with J-valued channel arrays, 2 x 2 window, 2 channels, 4 q x 4 (M, M\') x 256 vectors:', ok2)

# (b) counting values omega([rho_q, rho_q*]) = sum_{E-} n - sum_{E+} n for momentum-diagonal seas, one channel
def value(W, q, sea):
    Ws = set(W)
    lo = [k for k in W if vadd(k, q) in Ws]; hi = [k for k in W if tuple(x - y for x, y in zip(k, q)) in Ws]
    return sum(1 for k in lo if sea(k)) - sum(1 for k in hi if sea(k))
N = 3; W = list(itertools.product(range(-N, N), repeat=2))
print('(b) d = 2, N = 3:')
print('    half-space k1 < 0,      q = (1, 0):', value(W, (1, 0), lambda k: k[0] < 0), ' (formula 1 * 6 = 6)')
print('    quadrant k1 < 0, k2 < 0, q = (1, 0):', value(W, (1, 0), lambda k: k[0] < 0 and k[1] < 0))
print('    quadrant k1 < 0, k2 < 0, q = (1, 1):', value(W, (1, 1), lambda k: k[0] < 0 and k[1] < 0))
print('    tilted half-space k1 + k2 < 0, q = (1, 0):', value(W, (1, 0), lambda k: k[0] + k[1] < 0))
print('    disc |k|^2 <= 10 (meets the window edge), q = (1, 0):', value(W, (1, 0), lambda k: k[0] ** 2 + k[1] ** 2 <= 10))
print('    disc |k|^2 <= 10, q = (2, 0):', value(W, (2, 0), lambda k: k[0] ** 2 + k[1] ** 2 <= 10))
print('    disc |k|^2 <= 10 shifted by (-1, 0), q = (1, 0):', value(W, (1, 0), lambda k: (k[0] + 1) ** 2 + k[1] ** 2 <= 10))
I1 = [(k,) for k in range(-3, 3)]
print('    d = 1, bounded sea {-2, -1, 0}, N = 3: q = 1, 2, 3 ->', [value(I1, (q,), lambda k: -2 <= k[0] <= 0) for q in (1, 2, 3)],
      ' (zero only while the sea avoids the strips)')

# (c) d = 3 density-current sum S = sum over strips |k3|/|k|, q along axis 3
print('(c) d = 3 density-current sum S(N, q) and the stated interval (4qN(N - q), 8qN^2]; S / (2N)^2 per transverse momentum:')
for N in range(2, 8):
    row = []
    for q in range(1, N):
        S = 0.0
        for k1, k2 in itertools.product(range(-N, N), repeat=2):
            for k3 in list(range(-N, -N + q)) + list(range(N - q, N)):
                S += abs(k3) / math.sqrt(k1 * k1 + k2 * k2 + k3 * k3)
        lo, hi = 4 * q * N * (N - q), 8 * q * N * N
        row.append((q, round(S, 3), lo < S <= hi, round(S / (2 * N) ** 2, 3)))
    print('   N =', N, row)
