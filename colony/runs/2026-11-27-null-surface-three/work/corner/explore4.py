import random
from poly import *
exec(open('explore3.py').read().split("xiB = [z, ZJ, ZJ, t]")[0].split("random.seed(11)")[1])
random.seed(5)
xiB = [z, ZJ, ZJ, t]
nvec = [ONE, ZJ, ZJ, ONE]
def ndot(v): return v[0] - v[3]
def dn(f): return f.d(0) + f.d(3)
def dnM(H): return [[dn(H[m][k]) for k in range(D)] for m in range(D)]
Hg = rgauge(2)
L = lie(xiB, Hg)
print("L preserves gauge:", all(not bool(c) for c in papply(L, nvec)))
w = ndot(pomega(Hg, L))
tau = ptrace(Hg)
lam = t
dH = dnM(Hg)
want = lam * (ppair(dH, dH) - dn(tau) * dn(tau)) - dn(lam * (ppair(Hg, dH) - tau * dn(tau)) * F(1, 2))
print("n.omega(h, L h) on N:", subst_N(w - want) == {})
# and L h on N equals lam d_n h for transverse comps; trace
print("tr L = xi.grad tau:", (ptrace(L) - sum((xiB[a]*tau.d(a) for a in range(D)), ZJ)) == 0)
