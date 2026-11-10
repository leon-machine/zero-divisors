# independent route: own bitmask Clifford algebra, floats, full (unsymmetrised) intertwiner space by SVD
import numpy as np, itertools, sys
def make(p,q):
    n=p+q; sq=[1]*p+[-1]*q; N=1<<n
    def bm(a,b):
        s=1
        for i in range(n):
            if b>>i&1:
                # move e_i past higher bits of a
                if bin(a>>(i+1)).count('1')%2: s=-s
                if a>>i&1: s*=sq[i]
                a^=1<<i
        return a,s
    T=np.zeros((N,N,N))
    for a in range(N):
        for b in range(N):
            c,s=bm(a,b); T[a,b,c]=s
    mul=lambda x,y: np.einsum('a,b,abc->c',x,y,T)
    gr=lambda a: bin(a).count('1')
    rev=lambda x: np.array([x[a]*(-1)**(gr(a)*(gr(a)-1)//2) for a in range(N)])
    return n,sq,N,mul,gr,rev
def run(p,q,copies=1):
    n,sq,N,mul,gr,rev=make(p,q)
    t=sq.index(1) if p==1 else sq.index(-1)
    a=[i for i in range(n) if i!=t][0]
    E=lambda *idx: (lambda v:(v.__setitem__(sum(1<<i for i in idx),1.0),v)[1])(np.zeros(N))
    one=np.zeros(N); one[0]=1
    et=E(t); f=0.5*(one+mul(E(t),E(a)))
    assert np.allclose(mul(f,f),f)
    cols=[mul(E(*[i for i in range(n) if m>>i&1]),f) for m in range(N) if gr(m)%2==0]
    M=np.array(cols).T; U,s,Vt=np.linalg.svd(M,full_matrices=False); d1=int((s>1e-9).sum()); Bs=U[:,:d1]   # orthonormal basis of S
    bivs=[E(i,k) for i in range(n) for k in range(i+1,n)]
    L1=[Bs.T@np.array([mul(B,Bs[:,i]) for i in range(d1)]).T for B in bivs]  # matrices on S
    for B,Lm in zip(bivs,L1):  # closure check
        assert np.allclose(Bs@Lm, np.array([mul(B,Bs[:,i]) for i in range(d1)]).T)
    L=[np.kron(np.eye(copies),Lm) for Lm in L1]; d=d1*copies
    Ad=[np.array([[ (mul(B,E(m))-mul(E(m),B))[1<<k] for m in range(n)] for k in range(n)]) for B in bivs]
    res={}
    for name,A in (('vec',Ad),('scal',[np.zeros((1,1))]*len(bivs))):
        w=A[0].shape[0]
        # beta tensor b[k,i,j]; eq: sum_l L[l,i] b[k,l,j] + L[l,j] b[k,i,l] - A[k,m] b[m,i,j] = 0
        I_d=np.eye(d); I_w=np.eye(w)
        rows=[np.kron(I_w,np.kron(Lm.T,I_d))+np.kron(I_w,np.kron(I_d,Lm.T))-np.kron(Am,np.kron(I_d,I_d)) for Lm,Am in zip(L,A)]
        K=np.vstack(rows); sv=np.linalg.svd(K,compute_uv=True); 
        null=sv[2][(sv[1]>1e-8).sum():]
        # swap operator
        sols=null.reshape(-1,w,d,d)
        sym=np.linalg.matrix_rank((sols+sols.transpose(0,1,3,2)).reshape(len(sols),-1),tol=1e-8) if len(sols) else 0
        asym=np.linalg.matrix_rank((sols-sols.transpose(0,1,3,2)).reshape(len(sols),-1),tol=1e-8) if len(sols) else 0
        res[name]=(len(sols),sym,asym)
    # j checks on a random psi
    rng=np.random.default_rng(1); psi=Bs@rng.integers(-3,4,d1).astype(float)
    y=mul(mul(psi,et),rev(psi)); grades=sorted({gr(m) for m in range(N) if abs(y[m])>1e-9})
    out=dict(sig=(p,q),dimS=d1,copies=copies,sols_total_sym_asym=res,grades_y=grades)
    if n==5 and copies==1:
        s=y[N-1]; j=np.array([y[1<<k] for k in range(n)]); Qj=sum(sq[k]*j[k]**2 for k in range(n))
        Ivec=np.zeros(N); Ivec[N-1]=1; I2=mul(Ivec,Ivec)[0]
        out.update(s=s,Qet_Qj=sq[t]*Qj,s2=s*s,I2=I2,Qet=sq[t])
    print(out)
for (p,q) in [(2,1),(1,2),(1,3),(3,1),(4,1),(1,4)]: run(p,q)
for (p,q) in [(2,1),(1,3),(3,1)]: run(p,q,2)
if len(sys.argv)>1: run(4,1,2)
