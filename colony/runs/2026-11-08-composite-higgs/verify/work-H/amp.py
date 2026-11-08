"""Referee H: doublet-condensed band, sector (1, P-1, P) (same N_psi = N_chi = P as the stretched sector):
levels of isospin exactly P/2 - 1 (multiset difference against the stretched sector (0,P,P)), against the
doublet band E(0,P) and the stretched threshold E(0,P) + G_D n_b."""
import sys; sys.path.insert(0,'.')
from fock import *
import numpy as np
from collections import Counter
for nb in (3,4,5):
    for P in range(2,nb):
        cp=(0.0,0.0,1.0,3.0)
        Kp,Kc,GS,GD=cp
        e0=np.round(np.linalg.eigvalsh(matrix(nb,(0,P,P),*cp)[1]),7)
        e1=np.round(np.linalg.eigvalsh(matrix(nb,(1,P-1,P),*cp)[1]),7)
        diff=Counter(e1)-Counter(e0)
        low=min(diff) if diff else None
        Eb=(Kp+Kc)*P-GD*P*(nb-P+1)
        print(f"n_b={nb} P={P} (GS,GD)=(1,3): doublet band {Eb}, threshold {Eb+GD*nb}; lowest isospin-(P/2-1) level in (1,P-1,P): {low}",
              'BELOW THRESHOLD' if low is not None and low<Eb+GD*nb-1e-9 else '', 'BELOW BAND' if low is not None and low<Eb-1e-9 else '')
