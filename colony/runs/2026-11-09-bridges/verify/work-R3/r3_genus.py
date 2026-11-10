import itertools, numpy as np
from fractions import Fraction as Fr
def ncyc(p):
    seen=[False]*len(p); c=0
    for i in range(len(p)):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]: seen[j]=True; j=p[j]
    return c
def genus(n):
    eta=[(i+1)%n for i in range(n)]
    out={}
    for s in itertools.permutations(range(n)):
        inv=[0]*n
        for i,x in enumerate(s): inv[x]=i
        tau=[inv[eta[i]] for i in range(n)]   # sigma^{-1} eta
        k=ncyc(s)+ncyc(tau); assert (n+1-k)%2==0 and k<=n+1
        out[(n+1-k)//2]=out.get((n+1-k)//2,0)+1
    return out
G={n:genus(n) for n in range(2,8)}
for n in G: print(n,G[n])
def sector(n,d):
    num=sum(c*Fr(4,d*d)**g for g,c in G[n].items()); den=1
    for l in range(n): den*=1+Fr(2*l,d*d)
    return num/den/d**(n-1)
def full(n,d):
    num=sum(c*Fr(1,d*d)**g for g,c in G[n].items()); den=1
    for l in range(n): den*=1+Fr(l,d*d)
    return num/den/d**(n-1)
cat={2:2,3:5,4:14,5:42,6:132,7:429}
for n in (2,3,4): print(n,[ (sector(n,d),full(n,d)) for d in (2,4)])
# is the upper bound sector<full<C_n d^{1-n} true further out?
bad=[(n,d) for n in range(2,8) for d in (2,4,8,16,32,64) if not (Fr(1,d**(n-1))<sector(n,d)<full(n,d)<Fr(cat[n],d**(n-1)))]
print("violations n<=7:",bad)
rng=np.random.default_rng(3)
idx=[i for i in range(16) if bin(i).count('1')%2==0]
acc={2:0,3:0,4:0}; N=200000
for _ in range(N):
    v=np.zeros(16,complex); v[idx]=rng.normal(size=8)+1j*rng.normal(size=8); v/=np.linalg.norm(v)
    s=np.linalg.svd(v.reshape(4,4),compute_uv=False)**2
    for n in acc: acc[n]+=(s**n).sum()
print("MC d=4 sector:",{n:acc[n]/N for n in acc},"formula",{n:float(sector(n,4)) for n in acc})
