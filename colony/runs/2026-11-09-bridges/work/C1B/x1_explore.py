from fractions import Fraction as F
from itertools import permutations, combinations
from math import comb

def gbin(n,k):
    num=den=1
    for i in range(k):
        num*= (2**(n-i)-1); den*=(2**(i+1)-1)
    return num//den
def niso(a,k):
    r=gbin(a,k)
    for i in range(k): r*= (2**(a-i)+1)
    return r
def sp(e):
    r=2**(e*e)
    for i in range(1,e+1): r*=(4**i-1)
    return r
def counts(a,b):
    return {e: niso(a,a-e)*niso(b,b-e)*sp(e) for e in range(0,min(a,b)+1)}
def total(m):
    r=1
    for i in range(1,m+1): r*=(2**i+1)
    return r
def stab_mean(a,b,n):
    c=counts(a,b); assert sum(c.values())==total(a+b),(a,b)
    return sum(F(v,2**((n-1)*e)) for e,v in c.items())/total(a+b)
def cycles(p):
    n=len(p); seen=[0]*n; c=0
    for i in range(n):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]: seen[j]=1; j=p[j]
    return c
def haar(dA,dB,n,even=False):
    eta=tuple((i+1)%n for i in range(n))
    s=0
    for sg in permutations(range(n)):
        inv=[0]*n
        for i,x in enumerate(sg): inv[x]=i
        comp=tuple(inv[eta[i]] for i in range(n))
        if even: s+=2*F(dA,2)**cycles(comp)*F(dB,2)**cycles(sg)
        else: s+=dA**cycles(comp)*dB**cycles(sg)
    D=F(dA*dB,2) if even else dA*dB
    den=1
    for l in range(n): den*=(D+l)
    return F(s)/den
for a,b in [(1,1),(1,2),(2,2),(2,3),(3,3)]:
    for n in (2,3,4,5):
        print(a,b,n,stab_mean(a,b,n),haar(2**a,2**b,n), stab_mean(a,b,n)==haar(2**a,2**b,n))
# identity check n=2,3 over a range
ok=all(stab_mean(a,b,n)==haar(2**a,2**b,n) for a in range(1,7) for b in range(1,7) for n in (2,3))
print("n=2,3 agree for a,b<=6:",ok)
print("n=4 differ everywhere:",all(stab_mean(a,b,4)!=haar(2**a,2**b,4) for a in range(1,6) for b in range(1,6)))
# crossing coefficient d^{n-1} <tr rho^n>
for n in (2,3,4,5,6):
    print(n,[float(stab_mean(m,m,n)*2**(m*(n-1))) for m in (2,4,8,12)], [float(haar(2**m,2**m,n)*2**(m*(n-1))) for m in (2,4)] if n<6 else '')
