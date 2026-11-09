from own1 import *
from collections import Counter
def rev_sign(g): return -1 if (g*(g-1)//2)%2 else 1
for (p,q) in ((6,0),(7,1),(10,0)):
    S=setup(p,q); n,sq,full,units,cls=S; m=len(units)
    kg=Counter(); norm=Counter()
    kgr=[]
    for h in units:
        k=full^h; g=bin(k).count('1'); kg[g]+=1; kgr.append(g)
        norm[(g,'R~R scalar' if rev_sign(g)==-1 else 'R~R not scalar')]+=1
    print((p,q),'classes',m,'grade of k=I h_c:',dict(kg)); print('   ',dict(norm))
    # orbits on classes under transvections by k of grade 2 only, and all
    anti=[[bsign(units[c],units[d],sq)!=bsign(units[d],units[c],sq) for d in range(m)] for c in range(m)]
    def tv(c,d): return cls[units[c]^units[d]] if anti[c][d] else d
    for label,gs in (('bivector k only',[c for c in range(m) if kgr[c]==2]),('R~R scalar only',[c for c in range(m) if rev_sign(kgr[c])==-1]),('all',list(range(m)))):
        left=set(range(m)); orbs=[]
        while left:
            s=next(iter(left)); o={s}; fr=[s]
            while fr:
                nw=[]
                for d in fr:
                    for c in gs:
                        y=tv(c,d)
                        if y not in o: o.add(y); nw.append(y)
                fr=nw
            orbs.append(len(o)); left-=o
        print('   ',label,len(gs),'gens; class orbits',sorted(orbs))
