import sys; sys.path.insert(0,'/home/claude/leon-machine/zero-divisors/colony/runs/2026-11-24-three-routes/verify/work-R-G')
from p1_lat import *
rng=np.random.default_rng(3)
# identities on random integer fields, L=5
L=5
def rf(n): return [rng.integers(-4,5,(L,L,L)) for _ in range(n)]
for trial in range(5):
    h=rf(6); xi=rf(3); pi=rf(6)
    assert all((g==0).all() for g in G2(disp(xi)))
    assert (D(disp(xi))==0).all()
    assert pair(pi,disp(xi)) == -2*sum((xi[i]*C(pi)[i]).sum() for i in range(3))
    assert all((c==0).all() for c in C(G2(h)))
    h2=rf(6); assert pair(G2(h),h2)==pair(h,G2(h2))
    assert ((G2(h)[0]+G2(h)[1]+G2(h)[2]) == -D(h)).all()     # tr G = -1/2 D
    # D p = sum b_i C_i[pi], p = pi - 1/2 delta tr pi  (scale by 2)
    tr=pi[0]+pi[1]+pi[2]
    p2=[2*pi[c]-(tr if c<3 else 0) for c in range(6)]
    lhs=D(p2); rhs=2*sum(b_(C(pi)[i],i) for i in range(3))
    assert (lhs==rhs).all()
print('identities of (2) hold on random integer fields, L=5')
# ranks mod p
def rank_mod(M,p=2147483629):
    M=M.copy()%p; r=0; rows,cols=M.shape
    for c in range(cols):
        piv=None
        for i in range(r,rows):
            if M[i,c]: piv=i;break
        if piv is None: continue
        M[[r,piv]]=M[[piv,r]]
        inv=pow(int(M[r,c]),p-2,p)
        M[r]=(M[r]*inv)%p
        nz=np.nonzero(M[:,c])[0]
        for i in nz:
            if i!=r: M[i]=(M[i]-M[i,c]*M[r])%p
        r+=1
        if r==rows: break
    return r
def counts(L):
    n=L**3
    dispcols=[]
    for i in range(3):
        for x in range(n):
            xi=[np.zeros((L,L,L),dtype=np.int64) for _ in range(3)]; xi[i].flat[x]=1
            dispcols.append(np.concatenate([a.ravel() for a in disp(xi)]))
    Dm=[]
    for c in range(6):
        for x in range(n):
            h=[np.zeros((L,L,L),dtype=np.int64) for _ in range(6)]; h[c].flat[x]=1
            Dm.append(D(h).ravel())
    Dm=np.array(Dm,dtype=object).T.astype(np.int64)
    rd=rank_mod(np.array(dispcols,dtype=np.int64)); rD=rank_mod(Dm)
    return 6*n, rd, rD, 6*n-rd-rD
for L in (3,4):
    print('L',L,'(components, rank disp, rank D, free) =',counts(L), ' prediction 2*(L^3-1)+6 =',2*(L**3-1)+6)
# two space dimensions (10): components 11,22,12
def counts2d(L):
    n=L*L; res=[]
    def T2(f,i,s=1): return np.roll(f,-s,axis=i)
    s2=lambda f,i:T2(f,i)-f; b2=lambda f,i:f-T2(f,i,-1)
    def D2(h): return 2*b2(b2(h[2],0),1)-b2(s2(h[0],1),1)-b2(s2(h[1],0),0)
    def disp2(xi): return [2*b2(xi[0],0),2*b2(xi[1],1),s2(xi[1],0)+s2(xi[0],1)]
    dc=[];Dm=[]
    for i in range(2):
        for x in range(n):
            xi=[np.zeros((L,L),dtype=np.int64) for _ in range(2)]; xi[i].flat[x]=1
            dc.append(np.concatenate([a.ravel() for a in disp2(xi)]))
    for c in range(3):
        for x in range(n):
            h=[np.zeros((L,L),dtype=np.int64) for _ in range(3)]; h[c].flat[x]=1
            Dm.append(D2(h).ravel())
    rd=rank_mod(np.array(dc));rD=rank_mod(np.array(Dm).T.copy())
    return 3*n,rd,rD,3*n-rd-rD
print('2d L=4:',counts2d(4),' 2d L=5:',counts2d(5))
