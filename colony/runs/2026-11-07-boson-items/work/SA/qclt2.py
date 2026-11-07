import sys
sys.path.insert(0, '/home/claude/phys-graph/lib'); sys.path.insert(0, '.')
from fractions import Fraction as F
import GA
from galib import level, dag, comm, acomm, chk
import galib
from qclt import partitions, cumulant, copy, setup
# polarised blocks p1 = 1, p2 = 0
for NB in (1, 2, 3):
    s, mul, J, v, w, n, omega = setup(NB)
    rho = GA.sc(1)
    for blk in range(NB):
        rho = mul(rho, mul(n[2*blk], GA.sub(GA.sc(1), n[2*blk+1])))
    b = mul(v[0], w[1]); bd = dag(b, s)
    B = GA.add(*[copy(b, k) for k in range(NB)]); Bd = dag(B, s)
    phi = GA.add(B, Bd); pi = mul(J, GA.sub(Bd, B))
    # anti-normal moments omega(B^k B*^k) and normal ones
    for k in range(1, NB + 2):
        X = GA.sc(1)
        for _ in range(k): X = mul(X, B)
        for _ in range(k): X = mul(X, Bd)
        Y = GA.sc(1)
        for _ in range(k): Y = mul(Y, Bd)
        for _ in range(k): Y = mul(Y, B)
        exp = 1
        for j in range(k): exp *= (j + 1) * (NB - j)
        chk(f"NB={NB} k={k}: omega(B^k B*^k) = k! N!/(N-k)! = {exp}, omega(B*^k B^k) = 0", omega(rho, X) == (exp, 0) and omega(rho, Y) == (0, 0))
    for seq in ((phi,phi),(phi,pi),(pi,pi),(phi,phi,phi),(phi,phi,phi,phi),(phi,pi,phi,pi)):
        def mom(idx, ops=seq):
            X = GA.sc(1)
            for i in idx: X = mul(X, ops[i])
            return omega(rho, X)
        print(NB, len(seq), cumulant(mom, len(seq)))
print(galib.OK)
