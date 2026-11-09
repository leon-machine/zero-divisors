from own1 import *
from itertools import combinations_with_replacement as cwr
def blade_state(S):
    n,sq,full,units,cls=S
    D=2**(n//2-1); comm=[]
    rho={0:F(1)}
    for h in units:
        if all(bsign(h,c,sq)==bsign(c,h,sq) for c in comm):
            t=mul(rho,{0:F(1,2),h:F(1,2)},sq)
            if t.get(0,0)==F(1,2**(len(comm)+1)) :
                comm.append(h); rho=t
        if 2**len(comm)==D: break
    return rho
def generic(S,params):
    n,sq,full,units,cls=S
    rho=blade_state(S)
    for j,t in params:
        hc=units[j]; kb=full^hc; ks=bsign(full,hc,sq)
        V={0:F(1),kb:t*ks}; Vi={0:F(1)/(1+t*t),kb:-t*ks/(1+t*t)}
        assert mul(V,Vi,sq)=={0:1}
        rho=mul(mul(V,rho,sq),Vi,sq)
    assert mul(rho,rho,sq)==rho
    return rho
def coords(S,rho):
    n,sq,full,units,cls=S; D=2**(n//2-1)
    x=[]
    for h in units:
        x.append(D*mul(rho,{h:1},sq).get(0,F(0)))
    # check rho is in real span of units (no I h part)
    reb={0:F(1,D)}
    for h,v in zip(units,x):
        if v: reb[h]=v/D
    assert reb==rho, 'state has I h parts'
    return x
def eps(S,c,d):
    n,sq,full,units,cls=S
    hc,hd=units[c],units[d]
    if c==d or bsign(hc,hd,sq)!=bsign(hd,hc,sq): return None
    mk=hc^hd; e=cls[mk]
    if units[e]!=mk: raise Exception
    return e,bsign(hc,hd,sq)
for (p,q),params in (((1,3),[(0,F(1,3)),(1,F(2,7)),(2,F(3,4))]),((6,0),[(0,F(1,3)),(4,F(2,7)),(9,F(3,4)),(13,F(1,5)),(6,F(5,3)),(11,F(2,3)),(2,F(7,4))])):
    S=setup(p,q); n,sq,full,units,cls=S; D=2**(n//2-1); m=len(units)
    gens=[action(c,*S) for c in range(m)]; G=group(gens)
    rho=generic(S,params); x=coords(S,rho)
    print((p,q),'D',D,'nonzero coords',sum(1 for v in x if v),'of',m, 'sum sq',sum(v*v for v in x))
    # integer scaling
    from math import lcm
    L=1
    for v in x: L=lcm(L,v.denominator)
    xi=[int(v*L) for v in x]
    tri=list(cwr(range(m),3))
    s1=[0]*m; s2={t:0 for t in cwr(range(m),2)}; s3={t:0 for t in tri}; s4=[0]*m; s22=0
    for g in G:
        y=[g[i][1]*xi[g[i][0]] for i in range(m)]
        for a in range(m): s1[a]+=y[a]; s4[a]+=y[a]**4
        for t in s2: s2[t]+=y[t[0]]*y[t[1]]
        for t in tri: s3[t]+=y[t[0]]*y[t[1]]*y[t[2]]
    N=len(G); ok=True
    ok&=all(v==0 for v in s1)
    for (a,b),v in s2.items():
        ok&= F(v,N*L*L)==(F(1,D+1) if a==b else 0)
    bad=0
    for (a,b,c),v in s3.items():
        want=F(0)
        if len({a,b,c})==3:
            e=eps(S,a,b)
            if e and e[0]==c: want=F(2*e[1],(D+1)*(D+2))
        if F(v,N*L**3)!=want: bad+=1
    print('  first,second ok:',ok,' third: mismatches',bad,'of',len(tri),'multisets')
    print('  <x_c^4> group:',sorted(set(F(v,N*L**4) for v in s4)),' Haar 3/((D+1)(D+3)) =',F(3,(D+1)*(D+3)))
