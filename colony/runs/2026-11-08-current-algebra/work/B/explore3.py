from explore2_lib import *
import sys
n,L=int(sys.argv[1]),int(sys.argv[2])
M,idx,CD,C,jcur=setup(n,L)
num={k:mul(CD[k],C[k]) for k in CD}
Hk=add(*[scal(j,num[(x,j)]) for x in range(n) for j in range(L)])
N=add(*[num[k] for k in num])
A={};B={}
for q in range(1,L):
    for x in range(n):
        for y in range(n):
            J=jcur(x,y,q); A=add(A,mul(dag(J),J))
    J0=add(*[jcur(x,x,q) for x in range(n)]); B=add(B,mul(dag(J0),J0))
Z1={}
for x in range(n):
    for y in range(n): Z1=add(Z1,mul(jcur(x,y,0),jcur(y,x,0)))
Z2=mul(N,N); I=ident(M)
basis={'A':A,'B':B,'Z1':Z1,'Z2':Z2,'N':N,'I':I}
names=list(basis)
keys=sorted(set().union(*[set(b) for b in basis.values()])|set(Hk))
print(solve(names,[[basis[nm].get(k,0) for nm in names] for k in keys],[Hk.get(k,0) for k in keys]))
# u(1) Sugawara part T1 = (1/n)(B + Z2/2); does it commute with su(n) current E_{01} at q?
for q in range(0,L):
    Ja=jcur(0,1,q)
    cm=comm(B,Ja)
    print('q',q,'[B, j01_q] nonzero entries:',len(cm))
    Jm=dag(jcur(0,1,q)) if q>0 else None
