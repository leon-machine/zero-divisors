from own2 import setup,action,group,blade_state,coords,F
from collections import Counter
for (p,q) in ((1,3),(6,0)):
    S=setup(p,q); n,sq,full,units,cls=S; D=2**(n//2-1); m=len(units)
    G=group([action(c,*S) for c in range(m)])
    x=coords(S,blade_state(S))
    orb={tuple(g[i][1]*x[g[i][0]] for i in range(m)) for g in G}
    orb=list(orb)
    # overlaps tr(rho rho') = (1+x.y)/D ; frame potentials
    fp={t:F(0) for t in (1,2,3,4)}
    for a in orb:
        for b_ in orb:
            ov=(1+sum(u*v for u,v in zip(a,b_)))/D
            for t in fp: fp[t]+=ov**t
    from math import comb
    print((p,q),'orbit of blade state',len(orb),{t:(str(fp[t]/len(orb)**2),'haar',str(F(1,comb(D+t-1,t)))) for t in fp})
