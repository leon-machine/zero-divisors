import sys, time, pickle
sys.path.insert(0, '.')
from embed import *
from explore4 import inv, gram
from explore5 import W, Om, cas_vec, norm2, ip, add, scal
from fractions import Fraction as F

I16 = [[F(int(i == j)) for j in range(16)] for i in range(16)]
so10 = []
for a in range(5):
    for b in range(5):
        M = rep_bil(a, b, 'ab')
        if a == b:
            M = [[M[i][j] - F(1, 2) * I16[i][j] for j in range(16)] for i in range(16)]
        so10.append(M)
for a in range(5):
    for b in range(a + 1, 5):
        so10.append(rep_bil(a, b, 'cc'))
        so10.append(rep_bil(a, b, 'aa'))
print('traceless', all(tr(M) == 0 for M in so10))
G = gram(so10)
Gi = inv(G)
# lambda via adjoint Casimir on a generator, in 16-dim matrices
Z = so10[1]
acc = [[F(0)] * 16 for _ in range(16)]
dual = []
for a in range(45):
    D = [[sum(Gi[a][b] * so10[b][i][j] for b in range(45) if Gi[a][b]) for j in range(16)] for i in range(16)]
    dual.append(D)
for a in range(45):
    t = comm(dual[a], comm(so10[a], Z))
    acc = [[acc[i][j] + t[i][j] for j in range(16)] for i in range(16)]
print('lambda', set(acc[i][j] / Z[i][j] for i in range(16) for j in range(16) if Z[i][j]))
lam = set(acc[i][j] / Z[i][j] for i in range(16) for j in range(16) if Z[i][j]).pop()
t = time.time()
v = scal(1 / (2 + lam), cas_vec(so10, Om))
print('so10 norm', norm2(v), time.time() - t)
parts, tot = pickle.load(open('/tmp/claude-0/-home-claude/0546f519-7a06-5a66-9286-3db1fa7e460f/scratchpad/l2.pkl', 'rb'))
d = add(tot, scal(-1, add(v, parts['N'])))
print('su16 - so10 at level 2 on Omega:', len(d), norm2(d))
