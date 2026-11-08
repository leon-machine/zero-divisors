"""Referee H: the pair sum W on V_P = (P-1, P, 1) for n_b = 7 (beyond the proposal's n_b <= 6), largest eigenvalues
against the conjectured X = (P-1)m + max(m,3) (P>=2), X = n_b (P=1), X2 = (P-1)m + 3 (m > 3 or P = 1; X2 = 0 at P = 1)."""
import sys; sys.path.insert(0,'.')
from fock import *
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
def Wsparse(nb,nums):
    bs=basis(nb,nums); idx={s:i for i,s in enumerate(bs)}; n=len(bs); r=[];c=[];v=[]
    for wh in ('SS','B0','B1'):
        for cf,w in op_terms(nb,wh):
            for j,s in enumerate(bs):
                res=apply_word(w,s)
                if res: r.append(idx[res[1]]); c.append(j); v.append(res[0])
    return sp.csr_matrix((v,(r,c)),shape=(n,n),dtype=float)
nb=7
for P in range(1,nb+1):
    m=nb-P+1
    Wm=Wsparse(nb,(P-1,P,1)); n=Wm.shape[0]
    if n<600: ev=np.sort(np.linalg.eigvalsh(Wm.toarray()))[::-1][:4]
    else: ev=np.sort(sla.eigsh(Wm,k=4,which='LA')[0])[::-1]
    X=nb if P==1 else (P-1)*m+max(m,3); X2=0 if P==1 else (P-1)*m+3
    print(f"n_b=7 P={P} m={m} dim={n} top eigenvalues {np.round(ev,6)} conjectured X={X}"+(f" X2={X2}" if (m>3 or P==1) else ""),flush=True)
