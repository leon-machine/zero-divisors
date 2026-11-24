import time, sys
from fractions import Fraction as F
from spin2 import *
L = int(sys.argv[1]); ND = int(sys.argv[2]); NMAX = int(sys.argv[3])
T = Torus(L); tau = F(1, 2)
c0 = (L//2,)*3
string = [(c0[0]+d, c0[1], c0[2]) for d in (-1, 0, 1)]
f = {}
for x in string:
    f[(0, x)] = F(1, 2); f[(1, x)] = F(-1, 2); f[(2, x)] = F(-1, 2)
Df = T.ham(f)
print("D f:", sorted(Df.items()))
Gf = T.einstein(f)
print("supp G[f] comps:", len(Gf), "sites:", len({k[1] for k in Gf}))
t0 = time.time()
dist = T.dist_to(string)
# canonical: evolve (f, 0) from ND forward and backward
S = {ND: (dict(f), {})}
h, pi = dict(f), {}
for n in range(ND, NMAX):
    h, pi = T.step(h, pi, tau); S[n+1] = (h, pi)
h, pi = dict(f), {}
for n in range(ND, 0, -1):
    h, pi = T.unstep(h, pi, tau); S[n-1] = (h, pi)
print("canon evolve", time.time()-t0)
ok = all(dist[x] <= abs(n-ND) for n in S for fld in S[n] for (c, x) in fld)
print("canonical support inside cone:", ok)
# constraints kept
print("constraint kept:", all(T.ham(S[n][0]) == Df for n in S), all(T.mom(S[n][1]) == {} for n in S))
# slaved retarded: evolve (f,0) from step 0
D = {0: (dict(f), {})}
h, pi = dict(f), {}
for n in range(NMAX):
    h, pi = T.step(h, pi, tau); D[n+1] = (h, pi)
print("slaved evolve", time.time()-t0)
ev = 0; bad = 0; badn = {}
canon_bad = 0
for n in range(NMAX+1):
    Gd = T.einstein(D[n][0]); Gs = T.einstein(S[n][0])
    for x in T.sites:
        if dist[x] > abs(n-ND) + 1:
            for c in range(6):
                ev += 1
                if Gd.get((c, x), 0) != 0:
                    bad += 1; badn[n] = badn.get(n, 0) + 1
                if Gs.get((c, x), 0) != 0: canon_bad += 1
print("events", ev, "slaved fails", bad, badn, "canon fails", canon_bad, time.time()-t0)
