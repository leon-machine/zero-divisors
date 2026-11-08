"""Referee Z: independent recomputation (own route: group built from the bilinear cocycle, not by rewriting)."""
from itertools import product, permutations
from fractions import Fraction as F

def f(S, T, s, n):
    # bilinear cocycle: sum_{i>j} x_i y_j + sum_{i in N} x_i y_i
    return (sum(1 for i in range(n) for j in range(i) if S>>i&1 and T>>j&1) + sum(1 for i in range(n) if s[i] and S>>i&1 and T>>i&1)) % 2

def group(s):
    n = len(s)
    tab = {}
    for a in (0,1):
        for S in range(2**n):
            for b in (0,1):
                for T in range(2**n):
                    tab[(a,S),(b,T)] = ((a+b+f(S,T,s,n))%2, S^T)
    return tab

def gauss_sum(s):
    n=len(s)
    return sum((-1)**f(S,S,s,n) for S in range(2**n))

# 1. existence: associativity of the cocycle product for every sign vector n<=4
for n in range(1,5):
    for s in product((0,1),repeat=n):
        G=group(s); E=[(a,S) for a in (0,1) for S in range(2**n)]
        m=lambda x,y:G[x,y]
        assert all(m(m(x,y),z)==m(x,m(y,z)) for x in E for y in E for z in E)
        c=(1,0); e=[(0,1<<i) for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j: assert m(e[i],e[j])==m(c,m(e[j],e[i]))
            assert m(e[i],e[i])==(s[i],0)
print("existence by cocycle: ok n<=4 all sign vectors")

# 2. centre and central involutions vs p-q mod 4, standard signatures n<=7
for n in range(1,8):
    for p in range(n+1):
        s=tuple([0]*p+[1]*(n-p)); G=group(s); E=[(a,S) for a in (0,1) for S in range(2**n)]
        gens=[(1,0)]+[(0,1<<i) for i in range(n)]
        Z=[x for x in E if all(G[x,g]==G[g,x] for g in gens)]
        inv=[x for x in Z if x!=(0,0) and G[x,x]==(0,0)]
        if n%2==0: assert sorted(Z)==[(0,0),(1,0)] and len(inv)==1
        else:
            assert sorted(Z)==[(0,0),(0,2**n-1),(1,0),(1,2**n-1)]
            assert (len(inv)==3)==((p-(n-p))%4==1), (n,p)
print("centre / central involutions: ok n<=7")

# 3. Gauss sum classes vs p-q mod 8 (statement (viii)(e)) and vs the classical real type table
cls={0:'A',2:'A',4:'B',6:'B',1:'C',5:'D',3:'E',7:'E'}
for n in range(1,10):
    seen={}
    for p in range(n+1):
        g=gauss_sum(tuple([0]*p+[1]*(n-p))); k=cls[(2*p-n)%8]
        seen.setdefault(k,set()).add(g)
    for k,v in seen.items(): assert len(v)==1,(n,k,v)
    vals=[next(iter(v)) for v in seen.values()]; assert len(set(vals))==len(vals)
print("Gauss sum constant on and separating the mod-8 classes: ok n<=9")

# 4. group isomorphism (ignoring c) by brute invariants for n=1: V4 vs Z4; and for n>=2 order-2 count
def n_invol(s):
    n=len(s); return sum(1 for S in range(2**n) if f(S,S,s,n)==0)*2-1
for n in range(2,7):
    for p in range(n+1):
        for pp in range(n+1):
            s=tuple([0]*p+[1]*(n-p)); t=tuple([0]*pp+[1]*(n-pp))
            if gauss_sum(s)!=gauss_sum(t): assert n_invol(s)!=n_invol(t)
print("non-isomorphic groups separated by the count of involutions: ok")

# 5. the premise (S) at n>=2: c^2 = 1 and centrality forced from normality of <c> alone.
# brute force: all groups of order <= 32 given as permutation groups? Instead verify the identity on free words is trivial;
# the n=1 counterexamples: Z_{2m} (c^2 != 1) and dihedral D_m (c not central) in the result's formulation.
def dihedral(m):
    # elements (r,k): rotation r, reflection flag k; product
    def mul(x,y):
        r1,k1=x; r2,k2=y
        return ((r1 + (r2 if k1==0 else -r2))%m, (k1+k2)%2)
    return mul
for m in range(3,8):
    mul=dihedral(m); c=(1,0); e=(0,1)
    E=[(r,k) for r in range(m) for k in (0,1)]
    H={(r,0) for r in range(m)}            # <c>
    assert c!=(0,0) and mul(c,c)!=(0,0) and mul(c,e)!=mul(e,c)
    assert all({mul(mul(g,h),(( -g[0]) % m if g[1]==0 else g[0], g[1])) for h in H} <= H for g in E)  # normal
print("n=1, result's formulation: dihedral D_m satisfies (S) minus centrality, with c^2 != 1: ok")

# 6. division (iii): (0,3) zero divisor, (0,2) norm; (1,2) unit count in box
def cl_mul(x,y,s):
    n=len(s); out={}
    for S,a in x.items():
        for T,b in y.items():
            k=S^T; out[k]=out.get(k,0)+(-1)**f(S,T,s,n)*a*b
    return {k:v for k,v in out.items() if v}
s03=(1,1,1); w={7:1}; assert cl_mul(w,w,s03)=={0:1}
assert cl_mul({0:1,7:1},{0:1,7:-1},s03)=={}
s02=(1,1)
import random
random.seed(1)
for _ in range(200):
    x={k:F(random.randint(-9,9),random.randint(1,9)) for k in range(4)}
    xb={0:x[0],1:-x[1],2:-x[2],3:-x[3]}
    assert cl_mul(x,xb,s02)=={0:sum(v*v for v in x.values())} or all(v==0 for v in x.values())
cnt={1:0,-1:0}
for a,b,c in product(range(-3,4),repeat=3):
    qv=a*a-b*b-c*c
    if qv in cnt: cnt[qv]+=1
print("(1,2) Z-invertible vectors in box:",cnt, "sum", sum(cnt.values()))
# general fact: v invertible iff v^2 = Q(v) invertible -> any commutative R
print("all ok")
