"""Referee H: single shell H_4 = K N - G P*P on n_b blocks (modes 2b = a, 2b+1 = c), all sectors, exact-ish numerics.
(1) degenerate couplings K/G = n_b/2 - n with n > n_b/2 (K < 0, outside the hypothesis K >= 0);
(2) n_b = 2, K = 0 (gamma = 3/2: the proof's inequality gamma < n_b - 1/2 fails);
(3) own route for the second difference: E(s+h)+E(s-h)-2E(s) over all sectors, max over sectors, vs 2G."""
import sys; sys.path.insert(0,'.')
from fock import cre, ann, apply_word
from itertools import combinations
import numpy as np
def H4(nb,na,nc,K,G):
    bs=[]
    for A in combinations(range(nb),na):
        for C in combinations(range(nb),nc):
            s=0
            for b in A: s|=1<<(2*b)
            for b in C: s|=1<<(2*b+1)
            bs.append(s)
    idx={s:i for i,s in enumerate(bs)}; M=np.zeros((len(bs),len(bs)))
    for j,s in enumerate(bs):
        M[j,j]+=K*(na+nc)
        for b in range(nb):
            for c in range(nb):
                r=apply_word([('c',2*b+1),('c',2*b),('a',2*c),('a',2*c+1)],s)
                if r: M[idx[r[1]],j]+=-G*r[0]
    return M
def ground(nb,K,G):
    res=[]
    for na in range(nb+1):
        for nc in range(nb+1):
            res.append((np.linalg.eigvalsh(H4(nb,na,nc,K,G))[0],(na,nc)))
    res.sort(); return res
for nb,n in [(4,3),(5,4),(6,5),(4,2),(5,3)]:
    G=1.0; K=G*(nb/2-n)
    res=ground(nb,K,G)
    En=2*K*n-G*n*(nb-n+1)
    print(f"n_b={nb} n={n} K/G={K}: E(n)=E(n+1)={En:.4f}; global ground {res[0][0]:.4f} in {res[0][1]}; next sectors {[(round(e,4),s) for e,s in res[1:4]]}")
res=ground(2,0.0,1.0); print("n_b=2 K=0:",[(round(e,4),s) for e,s in res[:4]])
# second difference over all sectors (n, n) with own route
for nb,K,G in [(3,0.5,1.0),(4,1.0,1.0),(5,0.3,0.7)]:
    E={}
    for na in range(nb+1):
        for nc in range(nb+1):
            E[(na,nc)]=np.linalg.eigvalsh(H4(nb,na,nc,K,G))[0]
    sd=max(E[(a+1,c+1)]+E[(a-1,c-1)]-2*E[(a,c)] for a in range(1,nb) for c in range(1,nb))
    print(f"n_b={nb} K={K} G={G}: max second difference over sectors {sd:.6f}, bound 2G={2*G}")
