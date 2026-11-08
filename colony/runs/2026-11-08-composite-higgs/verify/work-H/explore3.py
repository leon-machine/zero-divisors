import sys; sys.path.insert(0,'.')
from fock import *
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
def sparse_parts(nb,nums):
    bs=basis(nb,nums); idx={s:i for i,s in enumerate(bs)}; n=len(bs)
    out=[]
    for which in (['SS'],['B0','B1']):
        r=[];c=[];v=[]
        for wh in which:
            for cf,w in op_terms(nb,wh):
                for j,s in enumerate(bs):
                    res=apply_word(w,s)
                    if res: r.append(idx[res[1]]); c.append(j); v.append(-res[0])
        out.append(sp.csr_matrix((v,(r,c)),shape=(n,n)))
    return out
def lowest(M):
    n=M.shape[0]
    if n<400: return np.linalg.eigvalsh(M.toarray())[0]
    return sla.eigsh(M,k=1,which='SA')[0][0]
def sectors(nb,N):
    for n1 in range(nb+1):
        for n2 in range(n1+1):
            n3=N-n1-n2
            if 0<=n3<=nb: yield (n1,n2,n3)
for nb,P in [(5,3),(6,3),(6,4),(7,3),(7,2),(8,3),(8,2)]:
    N=2*P
    parts={s:sparse_parts(nb,s) for s in sectors(nb,N)}
    first=None
    for GD in [0.5,0.6,0.7,0.8,0.85,0.9,0.95,0.99]:
        res=sorted((lowest(A+GD*B),s) for s,(A,B) in parts.items())
        band=-1.0*P*(nb-P+1)
        if res[0][0]<band-1e-7:
            first=(GD,res[0]); break
    print(nb,P,'m',nb-P+1,'first GD (GS=1,K=0) with band not ground:',first, flush=True)
