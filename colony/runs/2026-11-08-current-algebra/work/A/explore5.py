import sys, time
sys.path.insert(0, '.')
from embed import *
from explore4 import inv, gram
from fock import Win, add, scal
from fractions import Fraction as F

L = 4
W = Win(16, L)
Om = {sum(1 << W.idx(x, k) for x in range(16) for k in range(2)): F(1)}

def cas_vec(B16, st, m=-1):
    G = gram(B16)
    Gi = inv(G)
    out = {}
    for a in range(len(B16)):
        inner = W.cur(B16[a], m, st)
        for b in range(len(B16)):
            if Gi[a][b]:
                out = add(out, scal(Gi[a][b], W.cur(B16[b], m, inner)))
    return out

def norm2(v):
    return sum(c * c for c in v.values())
def ip(u, v):
    return sum(c * v.get(k, 0) for k, c in u.items())

t = time.time()
parts = {}
for name, B5, lam in (('su2', su2, F(1)), ('su3', su3, F(3, 2)), ('Y', [Y5], F(0))):
    B16 = [rep(X) for X in B5]
    parts[name] = scal(1 / (2 + lam), cas_vec(B16, Om))
    print(name, norm2(parts[name]), time.time() - t)
one = [[F(int(i == j)) for j in range(16)] for i in range(16)]
parts['N'] = scal(F(1, 2 * 16), W.cur(one, -1, W.cur(one, -1, Om)))
print('N', norm2(parts['N']))
# total u(16): (1/34)[sum_xy j^{yx}_{-1} j^{xy}_{-1} + N N]
tot = {}
for x in range(16):
    for y in range(16):
        tot = add(tot, W.cur(W.E(y, x), -1, W.cur(W.E(x, y), -1, Om)))
tot = scal(F(1, 34), add(tot, W.cur(one, -1, W.cur(one, -1, Om))))
print('total', norm2(tot), time.time() - t)
names = list(parts)
print('orthogonality', [(a, b, ip(parts[a], parts[b])) for i, a in enumerate(names) for b in names[i+1:]])
cos = add(tot, scal(-1, add(*parts.values())))
print('coset', norm2(cos), [ (a, ip(cos, parts[a])) for a in names])
import pickle
pickle.dump((parts, tot), open('/tmp/claude-0/-home-claude/0546f519-7a06-5a66-9286-3db1fa7e460f/scratchpad/l2.pkl', 'wb'))
