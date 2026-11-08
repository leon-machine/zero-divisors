from fock import *
import itertools
n=2; L=4
M=n*L
idx=lambda x,j: x*L+j
CD={(x,j):cdag(idx(x,j),M) for x in range(n) for j in range(L)}
C={(x,j):c(idx(x,j),M) for x in range(n) for j in range(L)}
def jcur(x,y,q):  # lowers level by q: sum_j c*_{x,j} c_{y,j+q}
    out={}
    for j in range(L):
        if 0<=j+q<L: out=add(out,mul(CD[(x,j)],C[(y,j+q)]))
    return out
num={k:mul(CD[k],C[k]) for k in CD}
Hk=add(*[scal(j,num[(x,j)]) for x in range(n) for j in range(L)])
Nx=[add(*[num[(x,j)] for j in range(L)]) for x in range(n)]
N=add(*Nx)
A={} ; B={}
for q in range(1,L):
    for x in range(n):
        for y in range(n):
            J=jcur(x,y,q); A=add(A,mul(dag(J),J))
    J0=add(*[jcur(x,x,q) for x in range(n)]); B=add(B,mul(dag(J0),J0))
Z1={}
for x in range(n):
    for y in range(n): Z1=add(Z1,mul(jcur(x,y,0),jcur(y,x,0)))
Z2=mul(N,N)
I=ident(M)
basis={'A':A,'B':B,'Z1':Z1,'Z2':Z2,'N':N,'I':I}
# fit Hk = sum c_i basis_i via exact solve on collected matrix entries
keys=sorted(set().union(*[set(b) for b in basis.values()])|set(Hk))
names=list(basis)
rows=[[basis[nm].get(k,0) for nm in names] for k in keys]
rhs=[Hk.get(k,0) for k in keys]
# least squares not allowed; do exact gaussian elimination for consistency
import copy
def solve(rows,rhs):
    m=[ [F(v) for v in r]+[F(b)] for r,b in zip(rows,rhs)]
    ncol=len(rows[0]); piv=[]; r=0
    for col in range(ncol):
        p=next((i for i in range(r,len(m)) if m[i][col]!=0),None)
        if p is None: continue
        m[r],m[p]=m[p],m[r]
        pv=m[r][col]; m[r]=[v/pv for v in m[r]]
        for i in range(len(m)):
            if i!=r and m[i][col]!=0:
                f=m[i][col]; m[i]=[a-f*b for a,b in zip(m[i],m[r])]
        piv.append(col); r+=1
    incons=any(all(v==0 for v in row[:-1]) and row[-1]!=0 for row in m)
    sol={names[c]:m[i][-1] for i,c in enumerate(piv)}
    return incons,sol
print(solve(rows,rhs))
# try restricted to edge-clean depth d states
def edgeclean(s,d):
    for x in range(n):
        for j in range(d):
            if not s>>idx(x,j)&1: return False
            if s>>idx(x,L-1-j)&1: return False
    return True
for d in (1,2):
    ks=[k for k in keys if edgeclean(k[1],d)]
    rows=[[basis[nm].get(k,0) for nm in names] for k in ks]; rhs=[Hk.get(k,0) for k in ks]
    print(d,len(ks),solve(rows,rhs))
