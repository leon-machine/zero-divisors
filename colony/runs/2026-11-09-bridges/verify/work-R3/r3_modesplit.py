import numpy as np, itertools, math
from fractions import Fraction as Fr
rng=np.random.default_rng(7)
X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1.,-1.]).astype(complex); I2=np.eye(2,dtype=complex)
def kron(*a):
    r=np.eye(1,dtype=complex)
    for x in a: r=np.kron(r,x)
    return r
def gens(l):
    e=[];f=[]
    for k in range(l):
        e.append(kron(*([Z]*k+[X]+[I2]*(l-k-1))))
        f.append(kron(*([Z]*k+[1j*Y]+[I2]*(l-k-1))))
    return e,f
def blades(gl):
    # all products of subsets of generator list, with squares sign for dual
    out=[]
    n=len(gl); dim=gl[0].shape[0] if gl else None
    for r in range(n+1):
        for S in itertools.combinations(range(n),r):
            M=np.eye(dim,dtype=complex)
            for i in S: M=M@gl[i]
            out.append(M)
    return out
def proj(x,bl):
    # projection onto span of blades (orthonormal under <a b^dagger>_0 = tr(a b^H)/dim since blades are +-unitary real)
    d=x.shape[0]
    return sum(np.trace(x@b.conj().T)/d*b for b in bl)
def ptrace(rho,dA,dB,keep):
    r=rho.reshape(dA,dB,dA,dB)
    return np.einsum('ibjb->ij',r) if keep=='A' else np.einsum('aiaj->ij',r)
l=3
e,f=gens(l)
for e_,f_ in zip(e,f):
    assert np.allclose(e_@e_,np.eye(8)) and np.allclose(f_@f_,-np.eye(8))
p=[f[k]@e[k] for k in range(l)]
Gam=p[0]@p[1]@p[2]
print("p_k diag Z-type:",np.allclose(p[0],kron(Z,I2,I2)))
def test(Amodes,label):
    Bmodes=[k for k in range(l) if k not in Amodes]
    gA=[g for k in Amodes for g in (e[k],f[k])]; gB=[g for k in Bmodes for g in (e[k],f[k])]
    bA=blades(gA); bB=blades(gB)
    dA=2**len(Amodes); dB=2**len(Bmodes)
    GA_=np.eye(8,dtype=complex)
    for k in Amodes: GA_=GA_@p[k]
    gBt=[g@GA_ for g in gB]
    bBt=blades(gBt)
    # commuting
    assert all(np.allclose(a@b,b@a) for a in gA for b in gBt)
    assert all(np.allclose(a@a,b@b) for a,b in zip(gB,gBt))
    # random pure states: generic, and even
    def stats(psi):
        rho=np.outer(psi,psi.conj())
        rA=dB*proj(rho,bA); rB=dA*proj(rho,bB); rBt=dA*proj(rho,bBt)
        # normalised traces: tr_A = dA <.>_0 = dA * Tr/8
        mom=lambda r,d,n: (d*np.trace(np.linalg.matrix_power(r,n))/8).real
        herm=np.allclose(rA,rA.conj().T)
        mineig=np.linalg.eigvalsh(rA).min()
        return [mom(rA,dA,n) for n in (2,3)],[mom(rB,dB,n) for n in (2,3)],[mom(rBt,dB,n) for n in (2,3)],herm,mineig
    psi=rng.normal(size=8)+1j*rng.normal(size=8); psi/=np.linalg.norm(psi)
    print(label,"generic:",stats(psi))
    Pp=(np.eye(8)+Gam)/2
    psi2=Pp@psi; psi2/=np.linalg.norm(psi2)
    print(label,"even   :",stats(psi2))
    # conditional expectation property and positivity on random positive x
    for _ in range(20):
        Mx=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8)); pos=Mx@Mx.conj().T
        assert np.linalg.eigvalsh(proj(pos,bA)).min()>-1e-9
        y=sum(rng.normal()*b for b in bA); y2=sum(rng.normal()*b for b in bA)
        assert np.allclose(proj(y@Mx@y2,bA),y@proj(Mx,bA)@y2)
        # E_B is NOT positive in general? test
    mins=[]
    for _ in range(200):
        v=rng.normal(size=8)+1j*rng.normal(size=8); v/=np.linalg.norm(v)
        mins.append(np.linalg.eigvalsh(proj(np.outer(v,v.conj()),bB)).min())
    print(label,"min eig of E_B over pure states (positivity of the untwisted B projection):",min(mins))
test([0],"A={1}")
test([1],"A={2}")
test([0,2],"A={1,3}")
# literal tensor split check for A = first modes: d_B E_A = partial trace over last qubits
gA=[e[0],f[0],e[1],f[1]]; bA=blades(gA)
Mx=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8))
print("A={1,2}: d_B E_A(x) == ptrace_B(x) (x) 1/d_B ?",np.allclose(2*proj(Mx,bA),np.kron(ptrace(Mx,4,2,'A'),np.eye(2))))
# the l=2 example
e2,f2=gens(2)
rho=(np.eye(4)+e2[0]-f2[0]@e2[1]+f2[0]@e2[0]@e2[1])/4
print("example: projector",np.allclose(rho@rho,rho),"trace",np.trace(rho).real,"hermitian",np.allclose(rho,rho.conj().T))
rA=2*proj(rho,blades([e2[0],f2[0]])); rB=2*proj(rho,blades([e2[1],f2[1]]))
print("purities",(2*np.trace(rA@rA)/4).real,(2*np.trace(rB@rB)/4).real)
# sector Monte Carlo, 4 modes, A = first two: m=n=4
def sector_mc(la,lb,N=200000):
    l=la+lb; D=2**l
    idx=[i for i in range(D) if bin(i).count('1')%2==0]
    pur=0;ent=0
    for _ in range(N):
        v=np.zeros(D,complex); v[idx]=rng.normal(size=len(idx))+1j*rng.normal(size=len(idx)); v/=np.linalg.norm(v)
        M=v.reshape(2**la,2**lb); s=np.linalg.svd(M,compute_uv=False)**2
        pur+=(s**2).sum(); s=s[s>1e-300]; ent+=-(s*np.log(s)).sum()
    return pur/N,ent/N
def H(a,b): return sum(Fr(1,k) for k in range(a,b+1))
for la,lb in ((1,1),(1,2),(2,2),(2,3)):
    m,n=2**la,2**lb
    sec=H(n//2+1,m*n//2)-Fr(m-2,2*n); page=H(n+1,m*n)-Fr(m-1,2*n)
    pur,ent=sector_mc(la,lb,60000)
    print(m,n,"purity MC",round(pur,4),"formula",float(Fr(m+n,m*n+2)),"| entropy MC",round(ent,4),"sector formula",sec,float(sec),"Page",float(page),"Delta",sec-page)
