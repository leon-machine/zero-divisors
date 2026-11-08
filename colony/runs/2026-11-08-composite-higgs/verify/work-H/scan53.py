import sys; sys.path.insert(0,'.')
from fock import *
import numpy as np
for nb,P in [(5,3),(6,3),(7,3),(4,2),(6,2)]:
    secs=[(a,b,2*P-a-b) for a in range(nb+1) for b in range(a+1) if 0<=2*P-a-b<=nb]
    parts={s:(matrix(nb,s,0,0,1.0,0)[1],matrix(nb,s,0,0,0,1.0)[1]) for s in secs}
    thr=None
    for GD in np.arange(0.0,1.001,0.02):
        g=min(np.linalg.eigvalsh(A+GD*B)[0] for A,B in parts.values())
        if g < -P*(nb-P+1)-1e-9: thr=round(GD,2); break
    print(nb,P,'smallest G_D/G_S on a 0.02 grid (K=0) where the singlet band is not the ground state at N=2P:',thr,flush=True)
