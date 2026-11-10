# R1 independent engine: blades as bitmasks, exact Fractions. No GA.py.
from fractions import Fraction as F
from itertools import product as iprod, combinations
import sys
class Alg:
    def __init__(s, sq): s.sq=sq; s.n=len(sq)
    def bm(s,a,b):
        sign=1; t=a>>1
        while t:
            if bin(t&b).count('1')&1: sign=-sign
            t>>=1
        c=a&b; i=0
        while c:
            if c&1: sign*=s.sq[i]
            c>>=1; i+=1
        return sign, a^b
    def mul(s,x,y):
        r={}
        for a,ca in x.items():
            for b,cb in y.items():
                sg,c=s.bm(a,b); r[c]=r.get(c,0)+sg*ca*cb
        return {k:v for k,v in r.items() if v!=0}
    def P(s,*xs):
        r={0:F(1)}
        for x in xs: r=s.mul(r,x)
        return r
    def dag(s,x):
        r={}
        for b,c in x.items():
            g=bin(b).count('1'); sg=(-1)**(g*(g-1)//2)
            for i in range(s.n):
                if b>>i&1: sg*=s.sq[i]
            r[b]=c*sg
        return r
    def g(s,i): return {1<<i:F(1)}
def L(*t):
    r={}
    for c,x in t:
        for b,v in x.items(): r[b]=r.get(b,0)+F(c)*v
    return {k:v for k,v in r.items() if v!=0}
ONE={0:F(1)}
def tau(x): return x.get(0,F(0))
def rank(rows):
    rows=[list(r) for r in rows]; rk=0; ncol=len(rows[0]) if rows else 0
    for c in range(ncol):
        piv=None
        for i in range(rk,len(rows)):
            if rows[i][c]!=0: piv=i;break
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        pv=rows[rk][c]
        for i in range(len(rows)):
            if i!=rk and rows[i][c]!=0:
                f=rows[i][c]/pv; rows[i]=[a-f*b for a,b in zip(rows[i],rows[rk])]
        rk+=1
    return rk
def par(b): return bin(b).count('1')&1
