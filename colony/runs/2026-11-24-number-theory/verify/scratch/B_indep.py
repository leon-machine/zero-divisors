# independent check of clause (ii) of B: random rational vectors, random T, random four-square reps (with zeros,
# with r'_t = r_t where possible); count distinct kernels among the five functionals; and test the lemma.
from fractions import Fraction as F
import random, itertools
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def rank(M):
    M=[r[:] for r in M]; rk=0; cols=len(M[0]) if M else 0
    for c in range(cols):
        p=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
def all4sq(n,lim=None):
    out=[]; r=int(n**.5)+1
    for a in range(r+1):
        for b in range(a,r+1):
            for c in range(b,r+1):
                d2=n-a*a-b*b-c*c
                if d2<c*c: continue
                d=int(round(d2**.5))
                if d*d==d2: out.append((a,b,c,d))
    return out
random.seed(7)
minK=99; trials=0; viol=0
for trial in range(4000):
    n=random.randint(5,8); k=random.randint(5,n)
    S=sorted(random.sample(range(n),k))
    r=[F(0)]*n
    for i in S:
        r[i]=F(random.choice([-1,1])*random.randint(1,4),random.randint(1,3))
    T=random.sample(S,4)
    rr=dot(r,r); den=rr.denominator
    reps=all4sq(rr.numerator*den)
    q=list(random.choice(reps)); random.shuffle(q); q=[F(random.choice([-1,1])*c,den) for c in q]
    rp=[F(0)]*n
    for t,c in zip(T,q): rp[t]=c
    u=[a-b for a,b in zip(r,rp)]; uu=dot(u,u)
    # functionals on Q^T (coordinates in order T)
    # c(x)=2 x.u/uu ; lambda_t(x)=x_t - c(x) u_t
    cvec=[2*u[t]/uu for t in T]
    funcs=[[ (1 if s==t else 0) - cvec[j]*u[t] for j,s in enumerate(T)] for t in T]+[cvec]
    assert all(any(x!=0 for x in f) for f in funcs)
    assert rank(funcs)==4
    # distinct kernels = classes of non-proportional functionals
    cls=[]
    for f in funcs:
        if all(rank([f,g])==2 for g in cls): cls.append(f)
    minK=min(minK,len(cls)); trials+=1
    # direct reflection: g_u(r') == r
    g=[a-2*dot(rp,u)/uu*b for a,b in zip(rp,u)]
    assert g==r
print("trials",trials,"min number of distinct kernels",minK)
# Lemma test: for random triples of distinct hyperplanes in Q^4, the only quadratic form vanishing on all is 0
mons=[(a,b) for a in range(4) for b in range(a,4)]
def hyp_pts(f):
    piv=next(i for i in range(4) if f[i]!=0); B=[]
    for i in range(4):
        if i==piv: continue
        x=[F(0)]*4; x[i]=F(1); x[piv]=-f[i]/f[piv]; B.append(x)
    P=list(B)+[[a+b for a,b in zip(B[i],B[j])] for i in range(3) for j in range(i+1,3)]
    return P
bad=0
for t in range(500):
    fs=[]
    while len(fs)<3:
        f=[F(random.randint(-2,2)) for _ in range(4)]
        if any(f) and all(rank([f,g])==2 for g in fs): fs.append(f)
    pts=sum((hyp_pts(f) for f in fs),[])
    if rank([[x[a]*x[b] for a,b in mons] for x in pts])!=10: bad+=1
print("lemma failures",bad)
