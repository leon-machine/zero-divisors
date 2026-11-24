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
t0 = time.time()
# structural neighbours: sources -> targets of the Einstein stencils
def gn(S):
    out = set()
    for (s, x) in S:
        for t, row in GS.items():
            stn = row.get(s)
            if stn:
                for o in stn:
                    out.add((t, T.sh(x, o, -1)))
    return out
def tmix(S):
    out = set(S)
    for (c, x) in S:
        if c < 3:
            out.update({(0, x), (1, x), (2, x)})
    return out
def cone(S0, m):
    """depth[(c,x)] = first step at which an h component can differ from zero, data h on S0, pi = 0."""
    Sh, Sp = set(S0), set()
    depth = {k: 0 for k in Sh}
    for n in range(1, m + 1):
        Sp = Sp | gn(Sh)
        new = tmix(Sp) - Sh
        for k in new: depth[k] = n
        Sh |= new
    return depth
depth = cone(set(f), NMAX)
BIG = NMAX + 1
def dG(c, x):
    """least depth over the h components that enter the curvature component (c, x)."""
    best = BIG
    for s, stn in GS[c].items():
        for o in stn:
            d = depth.get((s, T.sh(x, o)), BIG)
            if d < best: best = d
    return best
dGm = {(c, x): dG(c, x) for c in range(6) for x in T.sites}
print("cone built", time.time()-t0, "depth hist", {d: sum(1 for v in depth.values() if v == d) for d in range(NMAX+1)})
S = {ND: (dict(f), {})}
h, pi = dict(f), {}
for n in range(ND, NMAX):
    h, pi = T.step(h, pi, tau); S[n+1] = (h, pi)
h, pi = dict(f), {}
for n in range(ND, 0, -1):
    h, pi = T.unstep(h, pi, tau); S[n-1] = (h, pi)
D = {0: (dict(f), {})}
h, pi = dict(f), {}
for n in range(NMAX):
    h, pi = T.step(h, pi, tau); D[n+1] = (h, pi)
ok_supp = all(depth.get(k, BIG) <= abs(n-ND) for n in S for k in S[n][0])
print("canonical h support inside structural cone:", ok_supp)
ev = 0; bad = 0; badn = {}; cbad = 0; win = 0; winbad = 0
for n in range(NMAX+1):
    Gd = T.einstein(D[n][0]); Gs = T.einstein(S[n][0])
    m = abs(n - ND)
    for k, d in dGm.items():
        if d > m:
            ev += 1
            if Gd.get(k, 0) != 0:
                bad += 1; badn[n] = badn.get(n, 0) + 1
            if Gs.get(k, 0) != 0: cbad += 1
            if d <= NMAX:
                win += 1
                if Gd.get(k, 0) != 0: winbad += 1
print("events", ev, "slaved fails", bad, badn, "canon fails", cbad, "| within depth<=NMAX window:", win, winbad, time.time()-t0)
# timelike sanity: canonical nonzero somewhere inside cone off the string
ins = sum(1 for n in S for k, v in T.einstein(S[n][0]).items() if 0 < dGm[k] <= abs(n-ND))
print("canonical nonzero inside cone:", ins)
