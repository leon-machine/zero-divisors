import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
from itertools import product
ONE=GA.sc(1)
def setup(m):
    sq=tuple(s for _ in range(m) for s in (1,-1))
    e=[GA.gen(2*k) for k in range(m)]; f=[GA.gen(2*k+1) for k in range(m)]
    p=[GA.mul(f[k],e[k],sq) for k in range(m)]
    return sq,e,f,p
def dag(x):
    r=GA.reverse(x)
    return {b:(c if sum(1 for i in b if i%2==1)%2==0 else -c) for b,c in r.items()}
def s0(x): return x.get((),F(0))
sq,e,f,p=setup(2)
M=lambda *xs: __import__('functools').reduce(lambda a,b: GA.mul(a,b,sq), xs)
def lin(c,x,s,y): return GA.add(GA.scal(F(c),x),GA.scal(F(s),y))
def comm(x,y): return GA.sub(M(x,y),M(y,x))
def acomm(x,y): return GA.add(M(x,y),M(y,x))
def chsh(A1,A2,B1,B2): return GA.add(M(A1,GA.add(B1,B2)),M(A2,GA.sub(B1,B2)))
E2=M(e[1],p[0])  # twisted
# rational unit pairs
pts=[(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(-5,13),F(12,13)),(F(8,17),F(-15,17))]
bad=0
for a1,a2,b1,b2 in product(pts,repeat=4):
    A1=lin(a1[0],e[0],a1[1],p[0]);A2=lin(a2[0],e[0],a2[1],p[0])
    B1=lin(b1[0],E2,b1[1],p[1]);B2=lin(b2[0],E2,b2[1],p[1])
    for X in (A1,A2,B1,B2):
        assert GA.eq(M(X,X),ONE) and GA.eq(dag(X),X)
    assert GA.is_zero(comm(A1,B1)) and GA.is_zero(comm(A2,B2))
    C=chsh(A1,A2,B1,B2)
    X=comm(A1,A2);Y=comm(B1,B2)
    if not GA.eq(M(C,C),GA.sub(GA.sc(4),M(X,Y))): bad+=1
    Z=GA.sub(X,Y); SA=acomm(A1,A2);SB=acomm(B1,B2)
    rhs=GA.scal(F(1,2),GA.add(M(dag(Z),Z),M(SA,SA),M(SB,SB)))
    if not GA.eq(GA.sub(GA.sc(8),M(C,C)),rhs): bad+=1
print('bad',bad)
A1,A2,B1,B2=e[0],p[0],E2,p[1]
C=chsh(A1,A2,B1,B2); print('C',C); C2=M(C,C); print('C2',C2)
X=comm(A1,A2);Y=comm(B1,B2); print('X',X,'Y',Y,'XY',M(X,Y))
J=M(f[1],e[0]); print('J',J, M(J,J), 'dagJ', dag(J))
# positivity of blades
bl=GA.all_blades(4)
print(all(GA.eq(M(dag({b:F(1)}),{b:F(1)}),ONE) for b in bl))
# blade inverse = dagger
