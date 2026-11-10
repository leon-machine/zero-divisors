from own import *
B=[[(0,0,0,1),(0,0,1,0),(1,1,0,0),(1,-1,0,0)],[(0,0,0,1),(0,1,0,0),(1,0,1,0),(1,0,-1,0)],
[(1,-1,1,-1),(1,-1,-1,1),(1,1,0,0),(0,0,1,1)],[(1,-1,1,-1),(1,1,1,1),(1,0,-1,0),(0,1,0,-1)],
[(0,0,1,0),(0,1,0,0),(1,0,0,1),(1,0,0,-1)],[(1,-1,-1,1),(1,1,1,1),(1,0,0,-1),(0,1,-1,0)],
[(1,1,-1,1),(1,1,1,-1),(1,-1,0,0),(0,0,1,1)],[(1,1,-1,1),(-1,1,1,1),(1,0,1,0),(0,1,0,-1)],
[(1,1,1,-1),(-1,1,1,1),(1,0,0,1),(0,1,-1,0)]]
def canon(r):
    for c in r:
        if c!=0: return r if c>0 else tuple(-x for x in r)
rays={canon(r) for b in B for r in b}
print('distinct rays up to sign',len(rays))
print('all rows orthogonal',all(sum(a*b for a,b in zip(r,t))==0 for row in B for r in row for t in row if r!=t))
from collections import Counter
cnt=Counter(canon(r) for b in B for r in b); print('multiplicities',sorted(set(cnt.values())))
# own exhaustive: backtracking over contexts choosing the unique 1
rl=sorted(rays); idx={r:i for i,r in enumerate(rl)}; ctx=[[idx[canon(r)] for r in b] for b in B]
sols=0
def rec(k,val):
    global sols
    if k==9: sols+=1; return
    ones=[i for i in ctx[k] if val.get(i)==1]; 
    if len(ones)>1: return
    for ch in ctx[k]:
        if val.get(ch)==0: continue
        if ones and ch!=ones[0]: continue
        nv=dict(val); ok=True
        for i in ctx[k]:
            want=1 if i==ch else 0
            if nv.get(i,want)!=want: ok=False;break
            nv[i]=want
        if ok: rec(k+1,nv)
rec(0,{}); print('assignments',sols)
# atoms with my engine
A=Alg((1,-1,1,-1)); e=[A.g(0),A.g(2)]; f=[A.g(1),A.g(3)]
v=[L((F(1,2),e[j]),(F(1,2),f[j])) for j in range(2)]; w=[L((F(1,2),e[j]),(F(-1,2),f[j])) for j in range(2)]
P0=A.P(w[0],v[0],w[1],v[1]); s=[P0,A.mul(v[0],P0),A.mul(v[1],P0),A.P(v[0],v[1],P0)]
p=[A.mul(f[j],e[j]) for j in range(2)]
print('P0 == (1-p1)(1-p2)/4 (the fully occupied projector, not the vacuum (1+p)(1+p)/4):',P0==L((F(1,4),A.mul(L((1,ONE),(-1,p[0])),L((1,ONE),(-1,p[1]))))), ' v_j P0 !=0:',bool(A.mul(v[0],P0)),' w_j P0==0:',not A.mul(w[0],P0))
def atom(r):
    y=L(*[(r[i],s[i]) for i in range(4)]); return L((F(1,sum(c*c for c in r)),A.mul(y,A.dag(y))))
at={r:atom(r) for r in rl}
ok=all(A.mul(q,q)==q and A.dag(q)==q and tau(q)==F(1,4) for q in at.values())
ok2=all(L(*[(1,at[canon(r)]) for r in b])==ONE and all(not A.mul(at[canon(r)],at[canon(t)]) for r in b for t in b if canon(r)!=canon(t)) for b in B)
print('atoms proj',ok,'contexts orthogonal & complete',ok2,'#even atoms',sum(all(not par(b) for b in q) for q in at.values()))
# records (v) in Cl(4,4)
A=Alg((1,-1)*4); e=[A.g(2*j) for j in range(4)]; f=[A.g(2*j+1) for j in range(4)]; p=[A.mul(f[j],e[j]) for j in range(4)]
tw=A.mul(p[0],p[1]); A1,A2,B1,B2=e[0],e[1],A.mul(e[2],tw),A.mul(e[3],tw)
C=L((1,A.mul(A1,L((1,B1),(1,B2)))),(1,A.mul(A2,L((1,B1),(-1,B2)))))
Kk=L((-1,A.P(A1,A2,B1,B2)))
print('obs',all(A.dag(o)==o and A.mul(o,o)==ONE and all(par(b) for b in o) for o in (A1,A2,B1,B2)),'commute',all(A.mul(a,b)==A.mul(b,a) for a in (A1,A2) for b in (B1,B2)))
rho=A.mul(L((1,ONE),(1,Kk)),L((1,ONE),(F(1,3),C)))
R=A.mul(L((1,ONE),(1,Kk)),L((F(2,3),ONE),(F(1,6),C)))
print('C^2=4+4K',A.mul(C,C)==L((4,ONE),(4,Kk)),'omega(C)',tau(A.mul(rho,C)),'rho=3/4 R^2',rho==L((F(3,4),A.mul(R,R))),'R sa',A.dag(R)==R,'rho even',all(not par(b) for b in rho),'tau',tau(rho))
