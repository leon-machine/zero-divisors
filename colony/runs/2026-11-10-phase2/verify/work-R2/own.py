# R2 own route: integer matrices (Chevalley action on subsets), no GA.py
import itertools, sys
import numpy as np
from fractions import Fraction as Fr
def subsets(k): return [frozenset(c) for r in range(k+1) for c in itertools.combinations(range(k), r)]
def ops(k):
    st=subsets(k); ix={S:i for i,S in enumerate(st)}; n=len(st)
    V=[];Wd=[]
    for j in range(k):
        A=np.zeros((n,n),dtype=np.int64); B=np.zeros((n,n),dtype=np.int64)
        for S in st:
            s=(-1)**len([i for i in S if i<j])
            if j not in S: A[ix[S|{j}],ix[S]]=s
            else: B[ix[S-{j}],ix[S]]=s
        V.append(A);Wd.append(B)
    return st,ix,V,Wd
def ac(a,b): return a@b+b@a
def rank_exact(rows):
    # fraction-free gaussian elimination over Q using python ints
    M=[list(map(int,r)) for r in rows if any(r)]
    rk=0; ncol=len(M[0]) if M else 0
    piv_rows=[]
    for c in range(ncol):
        p=None
        for i in range(rk,len(M)):
            if M[i][c]!=0: p=i;break
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        pr=M[rk]
        for i in range(rk+1,len(M)):
            if M[i][c]!=0:
                f=M[i][c]; g=pr[c]
                M[i]=[g*x-f*y for x,y in zip(M[i],pr)]
                from math import gcd
                d=0
                for x in M[i]: d=gcd(d,x)
                if d>1: M[i]=[x//d for x in M[i]]
        rk+=1
    return rk
# (1) 3 pairs -> 8 states; CAR; algebra generated = all 64 matrices
for k in (1,2,3,4):
    st,ix,V,Wd=ops(k); n=2**k; I=np.eye(n,dtype=np.int64)
    assert all((ac(V[i],V[j])==0).all() and (ac(Wd[i],Wd[j])==0).all() and (ac(V[i],Wd[j])==(i==j)*I).all() for i in range(k) for j in range(k))
    if k<=3:
        gens=V+Wd; mons=[]
        for r in range(2*k+1):
            for c in itertools.combinations(range(2*k),r):
                m=I.copy()
                for i in c: m=m@gens[i]
                mons.append(m.flatten())
        print('k',k,'module dim',n,'rank of generated algebra',np.linalg.matrix_rank(np.array(mons,dtype=float)),'=',4**k)
# (2) invariant forms: all G with A^T G = eps G A for all vectors; nullity, symmetry, signature
for k in (1,2,3,4):
    st,ix,V,Wd=ops(k); n=2**k
    for eps in (1,-1):
        rows=[]
        for A in V+Wd:
            for i in range(n):
                for j in range(n):
                    row=[0]*(n*n)
                    for u in range(n):
                        row[u*n+j]+=int(A[u,i]); row[i*n+u]-=eps*int(A[u,j])
                    rows.append(row)
        R=np.array(rows,dtype=float)
        # null space numerically (entries 0,+-1), then exact confirm
        u,s,vt=np.linalg.svd(R,full_matrices=True)
        nullity=n*n-int((s>1e-9).sum())
        G=vt[-1].reshape(n,n); G=G/np.abs(G).max(); Gi=np.rint(G).astype(np.int64)
        assert np.abs(G-Gi).max()<1e-9
        assert all((A.T@Gi==eps*Gi@A).all() for A in V+Wd)
        sym=1 if (Gi==Gi.T).all() else (-1 if (Gi==-Gi.T).all() else 0)
        law=eps**k*(-1)**(k*(k-1)//2)
        ex = rank_exact(rows) if k<=3 else None
        sig=None
        if sym==1:
            ev=np.linalg.eigvalsh(Gi.astype(float)); sig=(int((ev>1e-9).sum()),int((ev<-1e-9).sum()))
        supp=all((Gi[ix[S],ix[T]]!=0)==(T==frozenset(range(k))-S) for S in st for T in st)
        print('k',k,'eps',eps,'nullity',nullity,'exact nullity',None if ex is None else n*n-ex,'sym',sym,'law',law,'signature',sig,'pairs S with S^c only',supp)
        assert nullity==1 and sym==law
        if k==3 and eps==-1:
            G3=Gi
# (3) k=3: bivectors of Cl(3,3) on F_3: invariant vectors? ; parity halves null
st,ix,V,Wd=ops(3); n=8
e=[V[j]+Wd[j] for j in range(3)]+[V[j]-Wd[j] for j in range(3)]
biv=[e[a]@e[b] for a in range(6) for b in range(a+1,6)]
assert all((b.T@G3==-G3@b).all() for b in biv)   # bivectors skew for beta_-: form is Spin-invariant
K=np.vstack(biv).astype(float)
print('k=3: number of bivectors',len(biv),'common kernel dim on F_3 =',8-np.linalg.matrix_rank(K))
for par in (0,1):
    idx=[ix[S] for S in st if len(S)%2==par]
    print(' parity',par,'half null:',(G3[np.ix_(idx,idx)]==0).all())
# so(3,3) on the vector space of Cl(4,4) = R^{3,3}+H fixes H: invariant vectors dim 2 (generators J_ab = E_ab g - E_ba g on first 6 coords)
g=np.diag([1,1,1,-1,-1,-1,1,-1]).astype(float); gens=[]
for a in range(6):
    for b in range(a+1,6):
        X=np.zeros((8,8)); X[a,b]=g[b,b]; X[b,a]=-g[a,a]; assert np.allclose(X.T@g+g@X,0); gens.append(X)
print('so(3,3) inside so(4,4) on R^{4,4}: invariant vectors dim =',8-np.linalg.matrix_rank(np.vstack(gens)))
# (4) second-quantised lift for k=2,3: derivation of Lambda(F_k)
for k in (1,2,3):
    st,ix,V,Wd=ops(k); n=2**k
    stU,ixU,VU,WU=ops(n)
    def L(X): 
        out=np.zeros((2**n,2**n),dtype=np.int64)
        for T in range(n):
            for S in range(n):
                if X[T,S]!=0: out+=int(X[T,S])*(VU[T]@WU[S])
        return out
    if k==3:
        # 256x256 int matrices fine
        pass
    a=L(V[0]); b=L(Wd[0]); c=L(V[0]@Wd[0]-Wd[0]@V[0])
    print('k',k,'[L v1,L w1]=L[v1,w1]:',(a@b-b@a==c).all(),'| {Lv1,Lw1}=1:',(ac(a,b)==np.eye(2**n,dtype=np.int64)).all(),'| {Lv1,Lw1} vac=0:',(ac(a,b)[:,ixU[frozenset()]]==0).all(),'| (Lv1)^2=0:',(a@a==0).all(), '| {Lv1,Lv2}=0:', (ac(a,L(V[1]))==0).all() if k>1 else None)
    # derivation property on one-letter states
    vac=ixU[frozenset()]
    ok=all(((a@VU[T])[:,vac]==sum(int(V[0][Tp,T])*VU[Tp][:,vac] for Tp in range(n))).all() for T in range(n))
    print('   L(v1) acts as v1 on one-letter states:',ok)
# (5) non-vector CAR pair in Cl(2,0) (Witt index 0): matrices e1=[[1,0],[0,-1]], e2=[[0,1],[1,0]]
e1=np.array([[1,0],[0,-1]]);e2=np.array([[0,1],[1,0]]);e12=e1@e2
a2=(e1+e12);b2=(e1-e12)  # doubled
print('Cl(2,0): a^2=0',(a2@a2==0).all(),'b^2=0',(b2@b2==0).all(),'{a,b}=1',(ac(a2,b2)==4*np.eye(2)).all())
