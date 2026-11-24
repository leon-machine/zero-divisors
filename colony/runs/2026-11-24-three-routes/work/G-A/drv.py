import sys, time
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
import tp_premise
tp_premise.configure('/home/claude/leon-machine/zero-divisors/store')
sys.path.insert(0, 'P1')
import check as C
from fractions import Fraction as F
t0 = time.time()
T, f, diff, depth, cd, S, R = C.dynamics()
print("dyn", time.time() - t0)
ND, NMAX = C.ND, C.NMAX
GS_ = {n: T.einstein(S[n][0]) for n in S}; GR_ = {n: T.einstein(R[n][0]) for n in R}
space = [(k, n) for n in S for k, d in cd.items() if d > abs(n - ND)]
bad = [(k, n) for (k, n) in space if GR_[n].get(k, 0) != 0]
fwd = [(k, n) for (k, n) in space if cd[k] <= n]
print("space", len(space), "bad", len(bad), "fwd", len(fwd), "bad n<=ND", sum(1 for (k, n) in bad if n <= ND), "min n", min(n for k, n in bad))
print("inside", sum(1 for n in S for k, v in GS_[n].items() if 0 < cd[k] <= abs(n - ND)))
print("D_AXIS", GR_[ND].get(C.D_AXIS), cd[C.D_AXIS], (C.D_AXIS, ND) in bad)
for cand in [(0, (12, 8, 8)), (0, (11, 8, 8)), (1, (11, 8, 8)), (0, (8, 11, 8)), (1, (8, 10, 8)), (3, (10, 9, 8)), (0, (10, 10, 8))]:
    print(cand, cd[cand], [GR_[n].get(cand, 0) for n in range(7)], [GS_[n].get(cand, 0) for n in range(7)])
other = [(k, n) for n in S for k, d in cd.items() if d > abs(n - C.ND_OTHER)]
print("other", len(other), sum(1 for (k, n) in other if GS_[n].get(k, 0) != 0))
early = [(k, n) for n in range(ND + 1) for k, d in cd.items() if d > abs(n - ND)]
print("early", len(early))
print("fwd early", sum(1 for (k, n) in early if cd[k] <= n))
print(time.time() - t0)
