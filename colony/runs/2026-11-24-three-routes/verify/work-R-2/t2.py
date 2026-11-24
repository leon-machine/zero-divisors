import numpy as np
L=9
a=(5,4,4); bb=(4,4,4)  # a = b+e1
rho=np.zeros((L,L,L)); rho[a]=1; rho[bb]=-1
k=2*np.pi*np.fft.fftfreq(L)
K=np.meshgrid(k,k,k,indexing='ij')
lam=sum(2*np.cos(Ki)-2 for Ki in K)  # symbol of Delta
rh=np.fft.fftn(rho); ph=np.zeros_like(rh); m=lam!=0
ph[m]=rh[m]/(-2*lam[m]); phi=np.real(np.fft.ifftn(ph))
s=lambda x,i: np.roll(x,-1,i)-x
bk=lambda x,i: x-np.roll(x,1,i)
Dl=lambda x,i: bk(s(x,i),i)
G=[]
for i in range(3):
    j,kk=[m for m in range(3) if m!=i]; G.append(0.5*(Dl(phi,kk)+Dl(phi,j)))
for (i,j) in [(0,1),(0,2),(1,2)]:
    G.append(-0.5*s(s(phi,j),i))
# check D(phi delta) = rho: D = -sum_i sum_{k!=i} Delta_k phi = -2 Delta phi
print(np.abs(-2*sum(Dl(phi,i) for i in range(3))-rho).max())
mask=np.ones((L,L,L),bool)
for x in np.ndindex(L,L,L):
    if max(abs(((x[i]-bb[i]+4)%9)-4) for i in range(3))<=1: mask[x]=False
vals=np.concatenate([np.abs(g[mask]) for g in G])
print(len(vals), (vals>1e-9).sum(), np.sort(vals)[[0,len(vals)-3591,len(vals)-3590]])
