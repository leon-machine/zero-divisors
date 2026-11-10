import sys, time
sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations, product
import GA

def setup(p,q):
    SQ = GA.sig(p,q); n=p+q
    ONE = GA.sc(1)
    def blade(S):
        x = ONE
        for i in S: x = GA.mul(x, GA.gen(i), SQ)
        return x
    I = blade(range(n))
    assert GA.eq(GA.mul(I,I,SQ), GA.sc(-1))
    even = [S for r in range(0,n+1,2) for S in combinations(range(n),r)]
    # hermitian units: one per class {S, complement}: the representative with square +1
    herm = []; seen=set()
    for S in even:
        comp = tuple(i for i in range(n) if i not in S)
        if S in seen or comp in seen: continue
        seen.add(S); seen.add(comp)
        b = blade(S)
        if GA.eq(GA.mul(b,b,SQ), ONE): h = b
        else:
            h = GA.mul(I,b,SQ); assert GA.eq(GA.mul(h,h,SQ), ONE)
        herm.append(h)
    return SQ, n, I, herm, blade

def analyse(p,q):
    SQ,n,I,herm,blade = setup(p,q)
    D = 2**(n//2-1)
    ONE=GA.sc(1)
    nz = [h for h in herm if not GA.eq(h,ONE)]
    assert len(nz)==D*D-1
    key = lambda x: tuple(sorted(x.items()))
    index = {}
    for i,h in enumerate(nz):
        index[key(h)] = (i,1); index[key(GA.neg(h))]=(i,-1)
    # generators: 1 + k, k = I h (square -1)
    gens=[]
    for h in nz:
        k = GA.mul(I,h,SQ)
        assert GA.eq(GA.mul(k,k,SQ), GA.sc(-1))
        Rp = GA.add(ONE,k); Rm = GA.sub(ONE,k)
        perm=[]
        for t in nz:
            y = GA.scal(F(1,2), GA.mul(GA.mul(Rp,t,SQ),Rm,SQ))
            perm.append(index[key(y)])
        gens.append(tuple(perm))
    # group closure on signed perms
    ident = tuple((i,1) for i in range(len(nz)))
    def comp(a,b):  # apply b then a
        return tuple((a[j][0], a[j][1]*s) for (j,s) in b)
    group={ident}; frontier=[ident]
    while frontier:
        new=[]
        for g in frontier:
            for h in gens:
                x=comp(h,g)
                if x not in group: group.add(x); new.append(x)
        frontier=new
    return SQ,n,I,nz,gens,group,D,blade

for (p,q) in [(1,3),(6,0),(3,1)]:
    t=time.time()
    SQ,n,I,nz,gens,group,D,blade = analyse(p,q)
    print((p,q),'D',D,'classes',len(nz),'group order',len(group), 'time',round(time.time()-t,1))
    orb = {g[0][0] for g in group}
    print(' orbit of class 0 size', len(orb))
