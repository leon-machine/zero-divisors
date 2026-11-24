from lat import *
L=17; c=(8,8,8)
f=[zeros(L) for _ in range(6)]
for dx in (-1,0,1):
    x=(c[0]+dx,c[1],c[2]); f[0][x]=Fr(1,2); f[1][x]=Fr(-1,2); f[2][x]=Fr(-1,2)
rho=zeros(L)
for dx in (2,-2): rho[(c[0]+dx,8,8)]+=1
for dx in (1,-1): rho[(c[0]+dx,8,8)]-=1
print("Df=rho_w-rho_n", np.all(D(f)==rho))
# stencil of G: which (src comp, offset) enter G_c(0): apply G to unit fields on small torus
Ls=7
ent={c2:set() for c2 in range(6)}
for sc in range(6):
    u=[np.full((Ls,)*3,Fr(0),dtype=object) for _ in range(6)]; u[sc][(3,3,3)]=Fr(1)
    g=G(u)
    for c2 in range(6):
        for idx in zip(*np.nonzero(g[c2]!=0)):
            ent[c2].add((sc,tuple(3-np.array(idx))))  # G_c2(x) uses h_sc(x+off), off = 3 - x
# depth by BFS over "step" dependency graph: h component reached in one step if it enters G of some component at same site after trace mixing
# h(n+1)_c(x) depends on pi(n+1)_c(x) and tr pi(n+1)(x) for c<3; pi(n+1)_c(x) depends on G_c(x) of h(n)
def deps_step(c2):
    # components (src, offset) of h(n) that h(n+1)_c2(at 0) depends on (beyond itself)
    cs=[c2]+([0,1,2] if c2<3 else [])
    out=set()
    for cc in cs: out|=ent[cc]
    return out
import itertools
NM=6
S0=set((cc,tuple(np.array(x).tolist())) for cc in range(6) for x in zip(*np.nonzero(f[cc]!=0)))
depth={k:0 for k in S0}
front=set(S0)
for n in range(1,NM+1):
    new=set()
    for cc in range(6):
        for x in itertools.product(range(L),repeat=3):
            k=(cc,x)
            if k in depth: continue
            for (sc,off) in deps_step(cc):
                y=tuple((x[i]+off[i])%L for i in range(3))
                if depth.get((sc,y),99)<n: new.add(k); break
    for k in new: depth[k]=n
print("depth counts",[sum(1 for v in depth.values() if v==n) for n in range(NM+1)])
cd={}
for cc in range(6):
    for x in itertools.product(range(L),repeat=3):
        cd[(cc,x)]=min(depth.get((sc,tuple((x[i]+off[i])%L for i in range(3))),99) for (sc,off) in ent[cc])
ND=3
R={0:(f,[zeros(L) for _ in range(6)])}
h,pi=R[0]
for n in range(NM):
    h,pi=step(h,pi); R[n+1]=(h,pi)
GR={n:G(R[n][0]) for n in R}
space=[(k,n) for n in range(NM+1) for k,v in cd.items() if v>abs(n-ND)]
print("events outside detection lattice cone",len(space))
bad=[(k,n) for (k,n) in space if GR[n][k[0]][k[1]]!=0]
print("bad",len(bad),"n<=ND",sum(1 for k,n in bad if n<=ND))
Gf=G(f); supp=set()
for cc in range(6):
    for x in zip(*np.nonzero(Gf[cc]!=0)): supp.add(tuple(int(t) for t in x))
print("supp G[f]",len(supp))
def d2(x,pts,Lt=L): return min(sum(min((a-bb)%Lt,(bb-a)%Lt)**2 for a,bb in zip(x,y)) for y in pts)
D2={}
ins=[(k,n) for k,n in bad if 4*d2(k[1],supp)<=n*n]
print("ins",len(ins),"out",len(bad)-len(ins),"ins n<=ND",sum(1 for k,n in ins if n<=ND),"ins outside unit cone of det",sum(1 for k,n in ins if 4*d2(k[1],supp)>(n-ND)**2))
# alt: distance measured from the string (3 sites) instead of G[f] support
strg=[(7,8,8),(8,8,8),(9,8,8)]
ins2=[(k,n) for k,n in bad if 4*d2(k[1],strg)<=n*n]
print("alt from string: ins",len(ins2))
# alt: strict
ins3=[(k,n) for k,n in bad if 4*d2(k[1],supp)<n*n]
print("alt strict <:",len(ins3))
both=[(k,n) for k,n in ins if 4*d2(k[1],supp)>(n-ND)**2]
odd=[(k,n) for k,n in ins if 4*d2(k[1],supp)<=(n-ND)**2]
print("3423 set n<=ND:",sum(1 for k,n in both if n<=ND), "by n", {m:sum(1 for k,n in both if n==m) for m in range(7)})
print("67 set by n", {m:sum(1 for k,n in odd if n==m) for m in range(7)}, "example", odd[:3], [d2(k[1],supp) for k,n in odd[:3]], [cd[k] for k,n in odd[:3]])
# perturbation: change detection step to 4 and recount the split
