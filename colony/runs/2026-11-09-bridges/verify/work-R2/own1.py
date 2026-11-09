# Referee R2 independent route: bitmask Clifford algebra, no GA.py.
from fractions import Fraction as F
from itertools import combinations
import sys
def bsign(a,b,sq):
    # sign of blade product e_a e_b (bitmasks), sq[i]=square of generator i
    s=0; t=a>>1
    while t:
        s+=bin(t&b).count('1'); t>>=1
    sign=-1 if s&1 else 1
    c=a&b; i=0
    while c:
        if c&1: sign*=sq[i]
        c>>=1; i+=1
    return sign
def mul(x,y,sq):
    out={}
    for a,ca in x.items():
        for b,cb in y.items():
            k=a^b; out[k]=out.get(k,0)+ca*cb*bsign(a,b,sq)
    return {k:v for k,v in out.items() if v!=0}
def setup(p,q):
    n=p+q; sq=[1]*p+[-1]*q; full=(1<<n)-1
    Isq=bsign(full,full,sq)
    assert Isq==-1
    units=[]  # (mask, sign) meaning h = sign*e_mask with square +1 ; nonzero classes
    cls={}
    for m in range(1,full):
        if bin(m).count('1')%2: continue
        comp=full^m
        if comp in cls or m in cls: continue
        if m==0 or m==full: continue
        h = m if bsign(m,m,sq)==1 else comp
        assert bsign(h,h,sq)==1
        cls[m]=cls[comp]=len(units); units.append(h)
    return n,sq,full,units,cls
def action(c,n,sq,full,units,cls):
    # conjugation by R_c=1+I h_c : h_d -> h_d if commute else -I h_d h_c
    hc=units[c]; out=[]
    for d,hd in enumerate(units):
        comm = bsign(hc,hd,sq)==bsign(hd,hc,sq)
        if comm: out.append((d,1)); continue
        # (1+k) hd (1-k)/2 computed directly
        k={full^hc: bsign(full,hc,sq)}
        up=dict(k); up[0]=1
        dn={a:-v for a,v in k.items()}; dn[0]=1
        r=mul(mul(up,{hd:1},sq),dn,sq)
        assert len(r)==1
        (mk,v),=r.items(); v=F(v,2)
        e=cls[mk]
        # express in terms of units[e]
        if mk==units[e]: out.append((e,int(v)))
        else: raise Exception('landed on I h')
    return tuple(out)
def group(gens):
    m=len(gens[0]); ident=tuple((i,1) for i in range(m))
    seen={ident}; fr=[ident]
    while fr:
        new=[]
        for g in fr:
            for h in gens:
                x=tuple((h[j][0],h[j][1]*s) for (j,s) in g)
                if x not in seen: seen.add(x); new.append(x)
        fr=new
    return seen
if __name__=='__main__':
    for (p,q) in ((1,3),(3,1),(6,0)):
        S=setup(p,q); n,sq,full,units,cls=S
        gens=[action(c,*S) for c in range(len(units))]
        G=group(gens)
        print((p,q),'classes',len(units),'|Gamma|',len(G))
