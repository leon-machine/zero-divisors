# Attempted counterexample to B(iii) in Q^5: a weight depending only on the class of the primitive integer vector
# modulo M (up to sign).  Collect many rational frames of Q^5 (coordinate frames moved by products of random
# reflections), impose "sum over the frame = constant", and compute the dimension of the solution space mod a prime.
from fractions import Fraction as F
import random, math, sys
M=int(sys.argv[1]); NF=int(sys.argv[2]); n=5; P=1000003
random.seed(3)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def refl(u,x):
    c=2*dot(x,u)/dot(u,u); return [a-c*b for a,b in zip(x,u)]
def prim(v):
    d=1
    for c in v: d=d*c.denominator//math.gcd(d,c.denominator)
    w=[int(c*d) for c in v]; g=0
    for c in w: g=math.gcd(g,abs(c))
    return [c//g for c in w]
def key(w):
    a=tuple(c%M for c in w); b=tuple((-c)%M for c in w); return min(a,b)
classes={}
rows=[]
for f in range(NF):
    frame=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for _ in range(random.randint(1,3)):
        u=[F(random.randint(-3,3)) for _ in range(n)]
        if not any(u): continue
        frame=[refl(u,x) for x in frame]
    random.shuffle(frame)
    row={}
    for x in frame:
        k=key(prim(x)); idx=classes.setdefault(k,len(classes)); row[idx]=row.get(idx,0)+1
    rows.append(row)
nc=len(classes)
# unknowns: f on classes and constant c; equation sum f - c = 0.  Count solution dimension.
mat=[]
for r in rows:
    v=[0]*(nc+1)
    for i,c in r.items(): v[i]=c%P
    v[nc]=P-1; mat.append(v)
rk=0; piv_rows=[]
A=mat
cols=nc+1
# modular elimination
basis={}
for v in A:
    v=v[:]
    for c in range(cols):
        if v[c]:
            if c in basis:
                b=basis[c]; f=v[c]
                v=[(x-f*y)%P for x,y in zip(v,b)]
            else:
                inv=pow(v[c],P-2,P); v=[(x*inv)%P for x in v]; basis[c]=v; break
print("M",M,"classes met",nc,"frames",NF,"rank",len(basis),"solution dim",cols-len(basis))
