# own route for proposal 2: direct enumeration of maximal totally isotropic subspaces (not via orbits)
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial
def wt(x): return bin(x).count('1')
def b(x,y): return (wt(x)*wt(y)+wt(x&y))&1
def lagr(m):
    n=2*m; res=set()
    def rec(sp,dim):
        if dim==m: res.add(sp); return
        mx=max(sp)
        for x in range(1,1<<n):
            if x in sp: continue
            if all(b(x,y)==0 for y in sp):
                new=frozenset(sp|{x^y for y in sp})
                # canonical: only extend if x is the min of new\sp ... simpler: dedupe by set
                if min(new-sp)==x: rec(new,dim+1)
    # enumerate chains with increasing 'min of the added coset' is not unique; dedupe with visited set
    seen=set()
    def rec2(sp,dim):
        if sp in seen: return
        seen.add(sp)
        if dim==m: res.add(sp); return
        for x in range(1,1<<n):
            if x in sp: continue
            if all(b(x,y)==0 for y in sp):
                rec2(frozenset(sp|{x^y for y in sp}),dim+1)
    rec2(frozenset([0]),0)
    return res
def haar(dA,dB,n,sector=False):
    eta=[(i+1)%n for i in range(n)]
    def cyc(p):
        s=set(); c=0
        for i in range(n):
            if i not in s:
                c+=1; j=i
                while j not in s: s.add(j); j=p[j]
        return c
    tot=F(0)
    for sg in permutations(range(n)):
        inv=[0]*n
        for i,x in enumerate(sg): inv[x]=i
        tau=[inv[eta[i]] for i in range(n)]   # sigma^{-1} eta
        if sector: tot+=2*F(dA,2)**cyc(tau)*F(dB,2)**cyc(sg)
        else: tot+=F(dA)**cyc(tau)*F(dB)**cyc(sg)
    D=F(dA*dB,2) if sector else F(dA*dB)
    den=F(1)
    for l in range(n): den*=D+l
    return tot/den
for m in (2,3,4):
    Ls=lagr(m); full=(1<<2*m)-1
    print('m',m,'families',len(Ls))
    sec=[L for L in Ls if full in L]
    for a in range(1,m):
        low=(1<<2*a)-1
        cnt={}
        for L in Ls:
            k=sum(1 for x in L if x&~low==0); cnt[k]=cnt.get(k,0)+1
        dA,dB=2**a,2**(m-a)
        mom={n:sum(F(k,dA)**(n-1)*c for k,c in cnt.items())/len(Ls) for n in (2,3,4)}
        print('  a',a,'|L_A| counts',dict(sorted(cnt.items())),'fin',[str(mom[n]) for n in (2,3,4)],'haar',[str(haar(dA,dB,n)) for n in (2,3,4)])
        cs={}
        for L in sec:
            k=sum(1 for x in L if x&~low==0); cs[k]=cs.get(k,0)+1
        ms={n:sum(F(k,dA)**(n-1)*c for k,c in cs.items())/len(sec) for n in (2,3,4)}
        print('     sector fams',len(sec),dict(sorted(cs.items())),'sec',[str(ms[n]) for n in (2,3,4)],'sector haar',[str(haar(dA,dB,n,True)) for n in (2,3,4)],'(dA+dB)/(D+2)=',F(dA+dB,dA*dB+2))
# sector Haar by direct integration at m=2 (sector dim 2 = span{|00>,|11>}): state cos|00>+e^{i}sin|11>, rho_A=diag(p,1-p), p uniform on [0,1]
print('direct sector m=2: E[p^2+(1-p)^2]=',F(2,3),' E[p^3+(1-p)^3]=',F(1,2),' E[p^4+q^4]=',F(2,5),' formula:',haar(2,2,2,True),haar(2,2,3,True),haar(2,2,4,True))
# limit weights
def phi(k):
    r=F(1)
    for i in range(1,k+1): r*=1-F(1,2**i)
    return r
ph=float(phi(200))
for n in range(2,8):
    s=sum(2.0**((n-1)*k-k*k)/float(phi(k))**2 for k in range(0,60))*ph
    print('n',n,'limit series',s)
