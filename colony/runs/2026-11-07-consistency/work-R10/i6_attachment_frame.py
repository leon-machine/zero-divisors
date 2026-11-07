"""C4: orientation of I_6 = I_4 E in the attachment's frame (e0, e1, e2, e3, nu, e_-), exact Gaussian rationals,
in the entity's own Jordan-Wigner realisation (copied from its check.py)."""
import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from GA import QI
from fractions import Fraction as F
Z0, ONE, I = QI(0), QI(1), QI(0, 1)
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))] for i in range(len(A))]
def kron(A,B):
    n,m=len(A),len(B); return [[A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)] for i in range(n*m)]
def sc(c,A): return [[c*x for x in r] for r in A]
def eq(A,B): return all(a==b for r,s in zip(A,B) for a,b in zip(r,s))
def idm(n): return [[ONE if i==j else Z0 for j in range(n)] for i in range(n)]
SX=[[Z0,ONE],[ONE,Z0]]; SY=[[Z0,QI(0,-1)],[I,Z0]]; SZ=[[ONE,Z0],[Z0,QI(-1)]]; S1=idm(2)
k3=lambda a,b,c: kron(kron(a,b),c)
g=[k3(SX,S1,S1),k3(SY,S1,S1),k3(SZ,SX,S1),k3(SZ,SY,S1),k3(SZ,SZ,SX),k3(SZ,SZ,SY)]
e0,e1,e2,e3,nu,em = g[0],sc(I,g[2]),sc(I,g[3]),sc(I,g[4]),g[1],sc(I,g[5])
CHIR=k3(SZ,SZ,SZ)
EVEN=[i for i in range(8) if CHIR[i][i]==ONE]
def prod(*xs):
    r=xs[0]
    for x in xs[1:]: r=mm(r,x)
    return r
# squares
for name,v,s in [('e0',e0,1),('e1',e1,-1),('e2',e2,-1),('e3',e3,-1),('nu',nu,1),('e-',em,-1)]:
    assert eq(mm(v,v), sc(QI(s),idm(8))), name
I4=prod(e0,e1,e2,e3); E=mm(nu,em)       # nu plays e_+ (nu^2 = 1, n_inf = nu + e_-)
I6=mm(I4,E)
print('I6^2 = -1:', eq(mm(I6,I6), sc(QI(-1),idm(8))))
print('I6 = I7 * chirality (I7 the scalar unit of C^8):', eq(I6, sc(I,CHIR)))
# on CS (EVEN): left I6 = +I7 ; on CS^- : -I7
onCS = all(I6[i][j]==(I if i==j else Z0) for i in EVEN for j in EVEN)
print('left I6 on CS = +I7:', onCS)
# opposite orientation (e.g. nu and e_- swapped, E' = e_- nu = -E) gives -I7
I6o=mm(I4,mm(em,nu))
print('opposite orientation I4 (e_- nu) on CS = -I7:', all(I6o[i][j]==(QI(0,-1) if i==j else Z0) for i in EVEN for j in EVEN))
# Z = e0 nu on CS, and e = chirality is the odd-extension vector with I6 e = I7
print('e := chirality: e^2 = 1 and I6 e = I7:', eq(mm(CHIR,CHIR),idm(8)), eq(mm(I6,CHIR), sc(I,idm(8))))
print('e anticommutes with the six generators:', all(eq(mm(CHIR,x), sc(QI(-1),mm(x,CHIR))) for x in (e0,e1,e2,e3,nu,em)))
