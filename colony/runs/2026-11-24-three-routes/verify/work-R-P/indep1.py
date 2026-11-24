# Independent checks for proposal 1 (own route, Fractions only)
from fractions import Fraction as F
from itertools import combinations, product
import random, math
random.seed(7)
def dot(a,b): return sum(F(x)*F(y) for x,y in zip(a,b))
def rank(M):
    M=[list(map(F,r)) for r in M]; r=0
    if not M: return 0
    n=len(M[0])
    for c in range(n):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                k=M[i][c]/M[r][c]; M[i]=[a-k*b for a,b in zip(M[i],M[r])]
        r+=1
    return r
def kernel(rows,n):
    # basis of {x: rows x = 0}
    M=[list(map(F,r)) for r in rows]; piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; M[r]=[a/M[r][c] for a in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                k=M[i][c]; M[i]=[a-k*b for a,b in zip(M[i],M[r])]
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]; out=[]
    for f in free:
        x=[F(0)]*n; x[f]=F(1)
        for i,c in enumerate(piv): x[c]=-M[i][f]
        out.append(x)
    return out
# brute-force four squares (independent of the rotor induction): integer n as sum of 4 squares
def four_sq(n):
    for a in range(int(math.isqrt(n))+1):
        for b in range(a,int(math.isqrt(n-a*a))+1):
            for c in range(b,int(math.isqrt(n-a*a-b*b))+1):
                d2=n-a*a-b*b-c*c; d=math.isqrt(d2)
                if d*d==d2: return (a,b,c,d)
def rat_four(q):
    q=F(q); t=four_sq(q.numerator*q.denominator); return [F(x,q.denominator) for x in t]
results=[]
for trial in range(12):
    N=random.choice([5,6,7,8])
    r=[F(random.choice([-5,-3,-2,-1,1,2,3,4,7]),random.choice([1,2,3])) for _ in range(N)]
    S=sorted(random.sample(range(N),4))
    t=rat_four(dot(r,r)); s=[F(0)]*N
    for k,i in enumerate(S): s[i]=t[k]
    assert dot(s,s)==dot(r,r)
    m=[a-b for a,b in zip(r,s)]; mm=dot(m,m)
    R=[[ (1 if i==j else 0) - 2*m[i]*m[j]/mm for j in range(N)] for i in range(N)]
    RT=list(zip(*R))
    assert all(sum(R[i][k]*R[j][k] for k in range(N))==(1 if i==j else 0) for i in range(N) for j in range(N))
    Rs=[sum(R[i][k]*s[k] for k in range(N)) for i in range(N)]; assert Rs==r
    basis=[[R[i][j] for i in range(N)] for j in S]   # images of e_j, j in S
    # projector of a standard projector conjugated is a symmetric idempotent of rank 1
    e=[F(0)]*N; e[S[0]]=F(1); P=[[ (1 if (i==S[0] and j==S[0]) else 0) for j in range(N)] for i in range(N)]
    RPR=[[sum(R[i][a]*P[a][b]*R[j][b] for a in range(N) for b in range(N)) for j in range(N)] for i in range(N)]
    assert all(RPR[i][j]==RPR[j][i] for i in range(N) for j in range(N))
    assert all(sum(RPR[i][k]*RPR[k][j] for k in range(N))==RPR[i][j] for i in range(N) for j in range(N))
    # coordinate functionals on W in the basis
    forms=[[basis[a][k] for a in range(4)] for k in range(N)]
    assert all(any(f) for f in forms) and rank(forms)==4
    classes=[]
    for f in forms:
        if not any(rank([f,g])==1 for g in classes): classes.append(f)
    # vectors of W in kernels of all classes; quad eval rank
    ev=[]
    for f in classes:
        for c in kernel([f],4):
            pass
        K=kernel([f],4); vecs=K+[[a+b for a,b in zip(K[i],K[j])] for i,j in combinations(range(3),2)]
        for c in vecs:
            # support of the actual vector in Q^N is smaller than r's
            x=[sum(c[a]*basis[a][k] for a in range(4)) for k in range(N)]
            assert sum(1 for z in x if z!=0) < sum(1 for z in r if z!=0)
            ev.append([c[a]*c[b] for a in range(4) for b in range(a,4)])
    results.append((N,len(classes),rank(ev)))
    assert rank(ev)==10
print("reflection/induction trials (N, #classes, rank of evals):",results)
# Plucker route for the determinant obstruction
for _ in range(200):
    a=[F(random.randint(-9,9),random.randint(1,5)) for _ in range(4)]
    b=[F(random.randint(-9,9),random.randint(1,5)) for _ in range(4)]
    p={(i,j):a[i]*b[j]-a[j]*b[i] for i in range(4) for j in range(i+1,4)}
    lhs=dot(a,a)*dot(b,b)-dot(a,b)**2
    rhs=(p[0,1]+p[2,3])**2+(p[0,2]-p[1,3])**2+(p[0,3]+p[1,2])**2
    assert lhs==rhs
print("Plucker identity: det of two vectors of Q^4 is a sum of three squares (200 random pairs)")
# 7 n^2 never a sum of three squares, n<=60, exhaustive
bad=[]
for n in range(1,61):
    t=7*n*n; ok=False
    for x in range(math.isqrt(t)+1):
        for y in range(x,math.isqrt(t-x*x)+1):
            z2=t-x*x-y*y; z=math.isqrt(z2)
            if z>=y and z*z==z2: ok=True;break
        if ok: break
    if ok: bad.append(n)
print("n<=60 with 7n^2 a sum of 3 squares:",bad)
u=[1,0,0,0,0,0,0,0]; v=[0,1,1,1,2,0,0,0]
print("det(u,v)=",dot(u,u)*dot(v,v)-dot(u,v)**2)
