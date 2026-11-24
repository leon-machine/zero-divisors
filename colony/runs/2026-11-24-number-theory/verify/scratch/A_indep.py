from fractions import Fraction as F
import random
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    # Hamilton i j = k
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
conj=lambda a:(a[0],-a[1],-a[2],-a[3])
N=lambda a:sum(c*c for c in a)
def primes(n): return [p for p in range(3,n) if all(p%q for q in range(2,int(p**.5)+1))]
def lagr(p):
    h=(p-1)//2
    sq={(a*a)%p:a for a in range(h+1)}
    for b in range(h+1):
        t=(-1-b*b)%p
        if t in sq: a=sq[t]; break
    x=(a,b,1,0); m=N(x)//p
    while m>1:
        if m%2==0:
            ev=sorted(x,key=lambda c:c%2)
            x=((ev[0]+ev[1])//2,(ev[0]-ev[1])//2,(ev[2]+ev[3])//2,(ev[2]-ev[3])//2); m//=2; continue
        y=tuple(((c+m//2)%m)-m//2 for c in x)
        z=qmul(x,conj(y)); assert all(c%m==0 for c in z)
        x=tuple(c//m for c in z); m2=N(x)//p; assert N(x)==m2*p and 0<m2<m; m=m2
    assert N(x)==p; return x
ps=primes(5000); [lagr(p) for p in ps]; print("descent ok for",len(ps),"odd primes <5000")
# PSD with vanishing pivots: LDL with zero-pivot rule
def ldl(A):
    n=len(A); W=[r[:] for r in A]; L=[[F(int(i==j)) for j in range(n)] for i in range(n)]; D=[F(0)]*n
    for j in range(n):
        D[j]=W[j][j]
        if D[j]==0:
            assert all(W[i][j]==0 for i in range(j,n)), "row not zero"
            continue
        assert D[j]>0
        for i in range(j+1,n): L[i][j]=W[i][j]/D[j]
        for i in range(j+1,n):
            for k in range(j+1,n): W[i][k]-=L[i][j]*L[k][j]*D[j]
    return L,D
random.seed(1)
cnt=0
for trial in range(300):
    n=random.randint(2,6); k=random.randint(1,n)
    Y=[[F(random.randint(-3,3),random.randint(1,3)) for _ in range(n)] for _ in range(k)]
    A=[[sum(y[i]*y[j] for y in Y) for j in range(n)] for i in range(n)]
    # random permutation so zero pivots occur early
    L,D=ldl(A)
    S=[[sum(L[i][j]*D[j]*L[k2][j] for j in range(n)) for k2 in range(n)] for i in range(n)]
    assert S==A; cnt+=sum(1 for d in D if d==0)
print("ldl ok; zero pivots met:",cnt)
