# Dynamics on 17^3 (clause 8): own evolution and own cone bookkeeping. Dyadic floats: exact.
import sys; sys.path.insert(0,'/home/claude/leon-machine/zero-divisors/colony/runs/2026-11-24-three-routes/verify/work-R-G')
from p1_lat import *
L=17; c=(8,8,8); tau=0.5; nd=3; NS=7
Z=lambda: np.zeros((L,L,L))
M=Z(); M[7,8,8]=M[8,8,8]=M[9,8,8]=1
f=[0.5*M,-0.5*M,-0.5*M,Z(),Z(),Z()]
G=lambda h:[0.5*g for g in G2(h)]
def step(h,pi):
    g=G(h); pi=[pi[k]-tau*g[k] for k in range(6)]
    tr=pi[0]+pi[1]+pi[2]; p=[pi[k]-(0.5*tr if k<3 else 0) for k in range(6)]
    return [h[k]+2*tau*p[k] for k in range(6)], pi
def unstep(h,pi):
    tr=pi[0]+pi[1]+pi[2]; p=[pi[k]-(0.5*tr if k<3 else 0) for k in range(6)]
    h0=[h[k]-2*tau*p[k] for k in range(6)]; g=G(h0)
    return h0,[pi[k]+tau*g[k] for k in range(6)]
# R: data f at step 0;  S: data f at step nd
R=[]; h,pi=f,[Z() for _ in range(6)]
for n in range(NS):
    R.append(h); h,pi=step(h,pi)
S={nd:f}; h,pi=f,[Z() for _ in range(6)]
for n in range(nd+1,NS): h,pi=step(h,pi); S[n]=h
h,pi=f,[Z() for _ in range(6)]
for n in range(nd-1,-1,-1): h,pi=unstep(h,pi); S[n]=h
# check the step is inverted
hh,pp=step(*unstep(f,[Z() for _ in range(6)])); assert all((hh[k]==f[k]).all() for k in range(6))
# influence: which h components does a unit h_y reach in one step (generic support), as offsets
def influence():
    inf={}
    for y in range(6):
        u=[Z() for _ in range(6)]; u[y][c]=1.0
        g=G2(u); diag_any=(g[0]!=0)|(g[1]!=0)|(g[2]!=0)
        reach=[(g[z]!=0)|(diag_any if z<3 else False) for z in range(6)]
        if y<6: reach[y]=reach[y]|(np.arange(L**3).reshape(L,L,L)==np.ravel_multi_index(c,(L,L,L)))
        inf[y]=[np.argwhere(r)-np.array(c) for r in reach]
    return inf
INF=influence()
def depth(start):
    INFD=10**6; d=[np.full((L,L,L),INFD) for _ in range(6)]
    fr=[s.copy() for s in start]
    for z in range(6): d[z][fr[z]]=0
    for k in range(1,NS+2):
        new=[np.zeros((L,L,L),bool) for _ in range(6)]
        for y in range(6):
            src=fr[y]
            if not src.any(): continue
            for z in range(6):
                for off in INF[y][z]:
                    new[z]|=np.roll(src,tuple(off),axis=(0,1,2))
        fr=[new[z]&(d[z]==INFD) for z in range(6)]
        for z in range(6): d[z][fr[z]]=k
    return d
# components of h entering the curvature component z at site: from G2 stencil (adjoint relation)
def enters():
    ent={}
    for z in range(6):
        ent[z]=[]
        for y in range(6):
            u=[Z() for _ in range(6)]; u[y][c]=1.0
            g=G2(u)[z]
            for off in np.argwhere(g!=0)-np.array(c):   # G_z at c+off depends on h_y at c  => G_z at x uses h_y at x-off
                ent[z].append((y,-off))
    return ent
ENT=enters()
def mindepth_entering(d):
    out=[]
    for z in range(6):
        m=np.full((L,L,L),10**6)
        for y,off in ENT[z]:
            m=np.minimum(m,np.roll(d[y],tuple(-off),axis=(0,1,2)))   # value at x of d[y](x+off)
        out.append(m)
    return out
for label,start in (('f-components',[f[z]!=0 for z in range(6)]),('all comps at string sites',[M!=0]*6)):
    d=depth(start); md=mindepth_entering(d)
    out=[[md[z]>abs(n-nd) for z in range(6)] for n in range(NS)]
    insrc=[[md[z]<=n for z in range(6)] for n in range(NS)]
    tot=sum(int(o.sum()) for row in out for o in row)
    GR=[G(R[n]) for n in range(NS)]; GS=[G(S[n]) for n in range(NS)]
    fail=sum(int(((GR[n][z]!=0)&out[n][z]).sum()) for n in range(NS) for z in range(6))
    failS=sum(int(((GS[n][z]!=0)&out[n][z]).sum()) for n in range(NS) for z in range(6))
    early=sum(int(((GR[n][z]!=0)&out[n][z]).sum()) for n in range(nd+1) for z in range(6))
    out_in_src=sum(int((out[n][z]&insrc[n][z]).sum()) for n in range(NS) for z in range(6))
    first=[n for n in range(NS) if any(((GR[n][z]!=0)&out[n][z]).any() for z in range(6))]
    notlater=sum(int(o.sum()) for n in range(nd+1) for o in out[n])
    print(label,': events',6*L**3*NS,'outside',tot,'| G[S] nonzero outside',failS,'| G[R] fails',fail,'first step',first[:1],
          'not later than nd',early,'| outside & in source cone',out_in_src,'| outside & not later',notlater)
# unit-speed cone: Euclidean distance from the support of G[f] (the curvature of the data), speed tau per step = 0.5 site
G0=G(f); suppx=np.argwhere(sum((g!=0).astype(int) for g in G0)>0)
X=np.indices((L,L,L)).reshape(3,-1).T
dist=np.min(np.linalg.norm(X[:,None,:]-suppx[None,:,:],axis=2),axis=1).reshape(L,L,L)
for n in range(NS):
    GR=G(R[n]); nz=sum((g!=0).astype(int) for g in GR)>0
    print('step',n,': sites with G[R] != 0:',int(nz.sum()),' max distance from source support',float(dist[nz].max()) if nz.any() else None,
          ' unit-speed radius',0.5*n,' sites beyond radius+0:',int((nz&(dist>0.5*n)).sum()))
# how many of the failures lie outside the unit-speed cone of the source (distance from supp G[f] > 0.5 n)?
d=depth([f[z]!=0 for z in range(6)]); md=mindepth_entering(d)
GRl=[G(R[n]) for n in range(NS)]
cnt=0; cnt_tot=0
for n in range(NS):
    for z in range(6):
        failm=(GRl[n][z]!=0)&(md[z]>abs(n-nd))
        cnt_tot+=int(failm.sum()); cnt+=int((failm&(dist>0.5*n)).sum())
print('failures',cnt_tot,'of which outside the unit-speed cone of the source (dist > n/2):',cnt)
