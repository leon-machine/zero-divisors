import sys; sys.path.insert(0,'.')
from fock import *
import numpy as np
def E(nb,nS,n,Kp,Kc,GS,GD):
    P=nS+n; return Kp*(2*nS+n)+Kc*n-(GS*nS+GD*n)*(nb-P+1)
def sectors(nb,N):
    for n1 in range(nb+1):
        for n2 in range(nb+1):
            n3=N-n1-n2
            if 0<=n3<=nb: yield (n1,n2,n3)
for cp in [(0,0,3,1),(0,0,1,3),(0,0,2,2.5),(1,0,3,2),(0,1,3,1),(0,0,3,2.9),(0,0,3,3.1)]:
    Kp,Kc,GS,GD=cp
    for nb in (2,3,4):
        for P in range(1,nb+1):
            N=2*P
            best=None
            for s in sectors(nb,N):
                bs,M=matrix(nb,s,*cp)
                ev=np.linalg.eigvalsh(M)[0]
                if best is None or ev<best[0]-1e-9: best=(ev,s)
                elif abs(ev-best[0])<1e-9: best=(best[0],best[1]+s) if False else best
            band=min(E(nb,P-n,n,*cp) for n in range(P+1))
            wD=(Kc-Kp)+(GS-GD)*(nb-P+1)
            print(cp,'nb',nb,'P',P,'wD',round(wD,3),'global',round(best[0],4),best[1],'band',round(band,4), 'BAND NOT GROUND' if best[0]<band-1e-9 else '')
