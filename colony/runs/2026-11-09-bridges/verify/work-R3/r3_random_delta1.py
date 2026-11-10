# Independent route: do NOT use the proposer's Delta_1. Solve for a random G-equivariant Delta_1 on the product
# complex directly (carried by closed product cells), inductively over dimension <= 5, then recompute a cup_1 a.
import random, sys
from r3_oddmap import Prod, span_solve
from collections import defaultdict

def solve_random(P, seed):
    rnd=random.Random(seed)
    Dg=P.ext(P.diag)
    H={}   # rep -> set of pairs
    def Hfull(x):
        a=x[0][1]; r=P.g(x,-a)
        return {(P.g(u,a),P.g(v,a)) for (u,v) in H[r]}
    for n in range(0,6):
        for x in P.reps(n):
            cl=sorted(P.clos(x))
            var=[(u,v) for u in cl for v in cl if P.dim(u)+P.dim(v)==n+1]
            rows={}
            def rid(p):
                if p not in rows: rows[p]=len(rows)
                return rows[p]
            R=set(Dg(x)); R^={(v,u) for (u,v) in Dg(x)}
            for z in P.bd2(x): R^=Hfull(z)
            cols=[]
            for j,(u,v) in enumerate(var):
                c=0
                for z in P.bd2(u): c^=1<<rid((z,v))
                for z in P.bd2(v): c^=1<<rid((u,z))
                cols.append(c)
            Rb=0
            for p in R: Rb^=1<<rid(p)
            piv={}; ker=[]
            order=list(range(len(var))); rnd.shuffle(order)
            for j in order:
                c=cols[j]; idv=1<<j
                while c:
                    low=c&-c
                    if low in piv:
                        pc,pi=piv[low]; c^=pc; idv^=pi
                    else:
                        piv[low]=(c,idv); break
                if c==0: ker.append(idv)
            sol=0; c=Rb
            while c:
                low=c&-c
                assert low in piv,("no solution",x)
                pc,pi=piv[low]; c^=pc; sol^=pi
            for kv in ker:
                if rnd.random()<0.5: sol^=kv
            H[x]={var[j] for j in range(len(var)) if sol>>j&1}
            # verify
            lhs=P.bdpairs(H[x])
            assert lhs==R
    return H

def square(P,H,m):
    th=defaultdict(int)
    for x in P.cells:
        (k,a),(q,b)=x
        if (k,q) in ((0,3),(1,2)) and (b-a)%2==0: th[x]=1
        if (k,q)==(2,1): th[x]=-(m//4)
    a={x for x in P.cells if th[x]%2}
    sq={x for x in P.reps(5) if sum(1 for (u,v) in H[x] if u in a and v in a)%2}
    def cob(rep4):
        orb={P.g(rep4,n) for n in range(m)}
        return {x for x in P.reps(5) if sum(1 for y in P.bd2(x) if y in orb)%2}
    gens=[cob(r) for r in P.reps(4)]
    pt={x for x in P.reps(5) if x[0][0]==5}
    return sorted(sq), span_solve(gens,sq), span_solve(gens,sq^pt)

for m in (4,8):
    P=Prod(m)
    for seed in range(4):
        H=solve_random(P,seed)
        print(m,seed,sum(len(v) for v in H.values()),square(P,H,m))
