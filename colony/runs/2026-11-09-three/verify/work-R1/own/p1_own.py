# Independent route: group-ring algebra Z[G x G], G = Z_m; the four parity identities of the chain-map condition.
import itertools
def run(m):
    # elements of Z[GxG] as dict {(a,b):n}
    def mul(A,B):
        C={}
        for (a,b),x in A.items():
            for (c,d),y in B.items():
                k=((a+c)%m,(b+d)%m); C[k]=C.get(k,0)+x*y
        return {k:v for k,v in C.items() if v}
    def add(*As):
        C={}
        for A in As:
            for k,v in A.items(): C[k]=C.get(k,0)+v
        return {k:v for k,v in C.items() if v}
    def sc(s,A): return {k:s*v for k,v in A.items()}
    one={(0,0):1}; g1={(1,0):1}; g2={(0,1):1}; gg={(1,1):1}
    N1={(a,0):1 for a in range(m)}; N2={(0,a):1 for a in range(m)}; NN={(a,a):1 for a in range(m)}
    T={(i,j):1 for i in range(m) for j in range(i+1,m)}
    D=lambda p,q: one if p%2==0 else (g2 if q%2==0 else T)   # Delta_{p,q} coefficient
    d1=lambda p: add(g1,sc(-1,one)) if p%2 else N1            # boundary of e_p in first factor
    d2=lambda q: add(g2,sc(-1,one)) if q%2 else N2
    dd=lambda k: add(gg,sc(-1,one)) if k%2 else NN            # boundary of e_k, diagonal action
    ok=True
    for p,q in itertools.product(range(2),range(2)):          # component (p,q) of d Delta(e_k), k=p+q+1; parity only
        k=p+q+1
        lhs=add(mul(D(p+1,q),d1(p+1)), sc((-1)**p, mul(D(p,q+1),d2(q+1))))
        rhs=mul(dd(k),D(p,q))
        ok&=(lhs==rhs)
    return ok
print({m:run(m) for m in (2,3,4,5,6,8)})

from math import comb
def hnf(rows):
    rows=[r[:] for r in rows]; out=[]; col=0; nc=len(rows[0])
    for col in range(nc):
        while True:
            nz=[r for r in rows if r[col]!=0]
            if len(nz)<=1: break
            nz.sort(key=lambda r:abs(r[col])); p=nz[0]
            for r in nz[1:]:
                q=r[col]//p[col]
                for i in range(nc): r[i]-=q*p[i]
        nz=[r for r in rows if r[col]!=0]
        if nz:
            out.append(nz[0]); rows=[r for r in rows if r is not nz[0]]
    return out
def member(H,v):
    v=v[:]
    for r in H:
        c=next(i for i,x in enumerate(r) if x)
        if any(v[i] for i in range(c)): return False
        if v[c]%r[c]: return False
        q=v[c]//r[c]; v=[a-q*b for a,b in zip(v,r)]
    return not any(v)
for n in range(1,15):
    rows=[]
    for j in range(4):
        v=[0]*4
        for e in range(n+2): v[(e+j)%4]+=comb(n+1,e)*(-1)**(n+1-e)
        rows.append(v)
    H=hnf(rows)
    # reduced order: index of L in the augmentation lattice {sum=0}: change basis s-part: use piv product / index of aug lattice
    aug=hnf([[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]])
    idx=1
    for r in H: idx*=abs(next(x for x in r if x))
    idxa=1
    for r in aug: idxa*=abs(next(x for x in r if x))
    N=1
    while not member(H,[N,0,-N,0]): N+=1
    print(n, idx//idxa==4**n, N, 2**((n+1)//2))
