from fractions import Fraction as F
from spin2 import *
L=21; T=Torus(L); tau=F(1,2); c0=(10,10,10)
string=[(c0[0]+d,10,10) for d in (-1,0,1)]
f={}
for x in string:
    f[(0,x)]=F(1,2); f[(1,x)]=F(-1,2); f[(2,x)]=F(-1,2)
dist=T.dist_to(string)
h,pi=dict(f),{}
for n in range(8):
    h,pi=T.step(h,pi,tau)
    G=T.einstein(h)
    hist={}
    for (c,x) in G: hist[dist[x]]=hist.get(dist[x],0)+1
    hh={}
    for (c,x) in h: hh[dist[x]]=hh.get(dist[x],0)+1
    print(n+1,"nonzero h comps",len(h),"by dist",sorted(hh.items()))
    print("   curvature comps",len(G),"by dist",sorted(hist.items()))
