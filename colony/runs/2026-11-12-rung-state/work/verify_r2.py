import sys, types
sys.path.insert(0, '/home/claude/phys-graph/lib')
m = types.ModuleType("tp_premise"); m.premise = lambda i: None; sys.modules["tp_premise"] = m
from fractions import Fraction as F
from itertools import product
sys.path.insert(0, 'store/claims/synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit')
import check as c3
# 1. off-by-one: c = 0, N = 1, x = O_1
A, B = c3.branches(1, F(0), F(1), [0]); psi = c3.vadd(c3.vsc(F(3,5), A), c3.vsc(F(4,5), B))
print("c=0, N=1: value of O_1", c3.ip(psi, c3.bell_element(1, F(0), F(1), psi)), " mixture value", F(9,25)*c3.ip(A, c3.bell_element(1,F(0),F(1),A)) + F(16,25)*c3.ip(B, c3.bell_element(1,F(0),F(1),B)))
# 2. one-particle operators from the branch vectors; Hilbert-Schmidt difference
def one_particle(vec, m):
    return [[c3.ip(vec, c3.cre(i, c3.ann(j, vec))) for j in range(m)] for i in range(m)]
for (c, s) in ((F(3,5), F(4,5)), (F(0), F(1)), (F(5,13), F(12,13))):
    for N in (1, 2, 3):
        mm = 2 + 2*N
        A, B = c3.branches(N, c, s, range(N))
        GA_, GB_ = one_particle(A, mm), one_particle(B, mm)
        sq = lambda G: [[sum(G[i][k]*G[k][j] for k in range(mm)) for j in range(mm)] for i in range(mm)]
        projA, projB = sq(GA_) == GA_, sq(GB_) == GB_
        hs2 = sum((GA_[i][j]-GB_[i][j])**2 for i in range(mm) for j in range(mm))
        print("c", c, "N", N, "projections:", projA, projB, " HS^2:", hs2, " 2 + 2 s^2 N:", 2 + 2*s*s*N)
# 3. threshold rule: outcome 1 iff y(s) < a^2, y = sum 2^-k s_k over n data rungs
n = 4
for a2 in (F(9,25), F(16,25), F(25,169), F(64,289)):
    cnt = sum(1 for bits in product((0,1), repeat=n) if sum(F(b, 2**(k+1)) for k, b in enumerate(bits)) < a2)
    print("a^2 =", a2, " frequency over 16 strings:", F(cnt, 2**n), " |diff| <= 2^-4:", abs(F(cnt,2**n)-a2) <= F(1,16))
