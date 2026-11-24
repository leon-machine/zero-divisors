import sys; sys.path.insert(0,'/home/claude/leon-machine/zero-divisors/colony/runs/2026-11-24-three-routes/verify/work-R-G')
from p1_lat import *
L=9; c=(4,4,4)
Z=lambda: np.zeros((L,L,L),dtype=np.int64)
def delta(x): a=Z(); a[x]=1; return a
e1=lambda d:(c[0]+d,c[1],c[2])
rw=delta(e1(-2))+delta(e1(2)); rn=delta(e1(-1))+delta(e1(1)); M=delta(e1(-1))+delta(c)+delta(e1(1))
f2=[M,-M,-M,Z(),Z(),Z()]           # 2f
assert (D(f2)==2*(rw-rn)).all(); print('Df = rho_w - rho_n: ok')
Gf4=G2(f2)                          # 4 G[f]
nzc=sum(int((g!=0).sum()) for g in Gf4); sites=int((sum((g!=0).astype(int) for g in Gf4)>0).sum())
print('support of G[f]:',nzc,'components at',sites,'sites; f on',sum(int((a!=0).sum()) for a in f2),'components')
supp=[g!=0 for g in Gf4]
# moments of the two arrangements
xs=np.arange(L)-c[0]
for name,r in (('w',rw),('n',rn)):
    m0=r.sum(); m1=(r.sum(axis=(1,2))*xs).sum(); m2=(r.sum(axis=(1,2))*xs**2).sum(); print(name,'mono',m0,'dip',m1,'second',m2)
# exact potential mod p by elimination
def lap_matrix():
    n=L**3; A=np.zeros((n,n),dtype=np.int64)
    for x in range(n):
        u=Z(); u.flat[x]=1
        A[:,x]=sum(Dl(u,i) for i in range(3)).ravel()
    return A
def solve_mod(A,bvec,p):
    n=A.shape[0]
    A=A.copy()%p; b=bvec.copy()%p
    # replace last equation (redundant: rows of Laplacian sum to 0) by phi[0]=0
    A[-1,:]=0; A[-1,0]=1; b[-1]=0
    Mx=np.concatenate([A,b[:,None]],axis=1)
    for col in range(n):
        piv=col+np.nonzero(Mx[col:,col])[0][0]
        if piv!=col: Mx[[col,piv]]=Mx[[piv,col]]
        Mx[col]=(Mx[col]*pow(int(Mx[col,col]),p-2,p))%p
        fac=Mx[:,col].copy(); fac[col]=0
        nz=np.nonzero(fac)[0]
        if len(nz): Mx[nz]=(Mx[nz]-(fac[nz,None]*Mx[col][None,:])%p)%p
    return Mx[:,-1]
A=lap_matrix()
for p in (2147483629, 2147483587):
    # -2 Lap phi = rw - rn  ->  Lap phi = -(rw-rn)/2
    inv2=pow(2,p-2,p)
    rhs=((-(rw-rn).ravel())%p*inv2)%p
    phi=solve_mod(A,rhs,p).reshape(L,L,L)
    assert (((sum(Dl(phi,i) for i in range(3))*(-2))-(rw-rn))%p==0).all()
    # kappa = G[phi delta]; 2kappa = G2
    k2=[g%p for g in G2([phi,phi,phi,Z(),Z(),Z()])]
    off=sum(int(((k2[ci]!=0)&(~supp[ci])).sum()) for ci in range(6))
    tot_off=sum(int((~supp[ci]).sum()) for ci in range(6))
    print('p',p,': kappa nonzero on',off,'of',tot_off,'components off supp G[f]')
# float cross-check by FFT
k=2*np.pi*np.fft.fftfreq(L); KX,KY,KZ=np.meshgrid(k,k,k,indexing='ij')
lam=-(2-2*np.cos(KX))-(2-2*np.cos(KY))-(2-2*np.cos(KZ)); lam[0,0,0]=1
R=np.fft.fftn(-(rw-rn)/2.0); R[0,0,0]=0; phif=np.real(np.fft.ifftn(R/lam))
kf=G2([phif,phif,phif,0*phif,0*phif,0*phif])
print('float: kappa |.|>1e-9 off supp:',sum(int(((abs(kf[ci])>1e-9)&(~supp[ci])).sum()) for ci in range(6)),
      ' min nonzero magnitude', min(abs(kf[ci][(abs(kf[ci])>1e-12)]).min() for ci in range(6)))
np.save('/home/claude/leon-machine/zero-divisors/colony/runs/2026-11-24-three-routes/verify/work-R-G/phif.npy',phif)
