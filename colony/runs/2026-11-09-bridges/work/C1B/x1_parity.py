from fractions import Fraction as F
from itertools import combinations
import sys
sys.path.insert(0,'.')
from x1_explore import haar
def wt(x): return bin(x).count('1')
def b(x,y): return (wt(x)*wt(y)+wt(x&y))&1
def span(gens):
    s={0}
    for g in gens:
        s|={x^g for x in s}
    return frozenset(s)
def orbit(L0,ws):
    seen={L0}; todo=[L0]
    while todo:
        L=todo.pop()
        for w in ws:
            M=frozenset(x^w if b(x,w) else x for x in L)
            if M not in seen: seen.add(M); todo.append(M)
    return seen
def mean(orb,a,m,n):
    maskB=((1<<(2*m))-1)^((1<<(2*a))-1)
    tot=F(0)
    for L in orb:
        k=sum(1 for x in L if x&maskB==0)
        tot+=F(k,2**a)**(n-1)
    return tot/len(orb)
for m in (2,3,4):
    N=2*m
    L0=span([3<<(2*i) for i in range(m)])
    even=[x for x in range(1,1<<N) if wt(x)%2==0]
    w2=[x for x in even if wt(x)==2]
    full=orbit(L0,even); rot=orbit(L0,w2)
    print("m",m,"orbit full",len(full),"rotor-only",len(rot))
    for a in range(1,m):
        bb=m-a
        for n in (2,3,4):
            print("  a|b",a,bb,"n",n,"full",mean(full,a,m,n),"rotor",mean(rot,a,m,n),"haar-even",haar(2**a,2**bb,n,even=True),"lubkin",haar(2**a,2**bb,n))
