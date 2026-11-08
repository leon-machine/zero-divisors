import sys; sys.path.insert(0,'.')
from fock import *
import numpy as np
def E(nb,nS,n,Kp,Kc,GS,GD):
    P=nS+n; return Kp*(2*nS+n)+Kc*n-(GS*nS+GD*n)*(nb-P+1)
def sectors(nb,N):
    for n1 in range(nb+1):
        for n2 in range(n1+1):   # isospin: sectors with n1>=n2 suffice
            n3=N-n1-n2
            if 0<=n3<=nb: yield (n1,n2,n3)
for nb,P in [(4,1),(4,2),(5,1),(5,2),(6,2),(6,3)]:
    N=2*P
    mats={s:matrix(nb,s,0,0,0,0)[1]*0 for s in []}
    # build S*S and W parts separately once
    parts={}
    for s in sectors(nb,N):
        _,A=matrix(nb,s,0,0,1,0); _,B=matrix(nb,s,0,0,0,1)
        parts[s]=(A,B)
    for GD in [0.0,0.3,0.6,0.8,0.9,0.95,1.0,1.05,1.2]:
        GS=1.0
        res=[]
        for s,(A,B) in parts.items():
            ev=np.linalg.eigvalsh(A*GS/1+B*GD)[0]  # matrix(...,GS=1,GD=0) gives -S*S ; scale
            res.append((ev,s))
        res.sort()
        band=min(E(nb,P-n,n,0,0,GS,GD) for n in range(P+1))
        wD=(GS-GD)*(nb-P+1)
        print(nb,P,'GD',GD,'wD',round(wD,3),'ground',round(res[0][0],4),res[0][1],'band',round(band,4),'' if res[0][0]>band-1e-9 else 'BAND NOT GROUND')
