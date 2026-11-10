from own import *
# A1 boosted example Cl(1,1): e index0 (+), f index1 (-)
A=Alg((1,-1)); e,f=A.g(0),A.g(1)
idem=L((F(1,2),ONE),(F(5,8),e),(F(3,8),f))
print('boost idempotent?',A.mul(idem,idem)==idem, 'self-adjoint?',A.dag(idem)==idem)
rho=L((1,ONE),(1,e))
print('value',tau(A.mul(rho,idem)),'complement',tau(A.mul(rho,L((1,ONE),(-1,idem)))))
# is the boosted frame's the t=4 frame: e'=17/8 e+15/8 f ; idem = (1+e'')/2 with e''=5/4e+3/4f  -> t=2
print("e'' = t v + w/t with t=2:", L((2,L((F(1,2),e),(F(1,2),f))),(F(1,2),L((F(1,2),e),(F(-1,2),f)))))
p=A.mul(f,e); Pi=L((F(1,2),ONE),(F(1,2),p))
# (b)
m=L((1,ONE),(1,p),(F(1,3),e)); y=L((-3,ONE),(3,e),(-2,f),(2,p))
print('(b) nu(1),nu(Pi),nu(e),nu(yy+):',tau(m),tau(A.mul(m,Pi)),tau(A.mul(m,e)),tau(A.mul(m,A.mul(y,A.dag(y)))))
# (a) mu positivity on a grid of own choosing, mu(f)
mu=lambda x: tau(A.mul(Pi,x))/tau(Pi)+tau(A.mul(f,x))
import random; random.seed(7); ok=True
for _ in range(500):
    yy=L(*[(F(random.randint(-9,9),random.randint(1,5)),b) for b in (ONE,e,f,p)])
    ok&= mu(A.mul(yy,A.dag(yy)))>=0
print('(a) mu>=0 on 500 random yy+:',ok,' mu(f)=',mu(f),' mu(Pi)=',mu(Pi))
# atoms in signatures outside the table: greedy maximal commuting sets
def atom_test(p_,q_,rev=False):
    A=Alg(tuple([1]*p_+[-1]*q_)); n=p_+q_
    bl=list(range(1,1<<n)); 
    if rev: bl=bl[::-1]
    gens=[]; grp={0}
    for b in bl:
        if b in grp: continue
        if A.bm(b,b)[0]!=1: continue
        if any(A.bm(b,g)[0]!=A.bm(g,b)[0] for g in gens): continue
        gens.append(b); grp|={x^b for x in grp}
    Pm=ONE
    for b in gens: Pm=A.mul(Pm,L((F(1,2),ONE),(F(1,2),{b:F(1)})))
    full=[];sym=[]
    for b in range(1<<n):
        yv=A.P(Pm,{b:F(1)},Pm)
        if yv:
            full.append([yv.get(k,0) for k in range(1<<n)])
            s2=L((1,yv),(1,A.dag(yv)))
            if s2: sym.append([s2.get(k,0) for k in range(1<<n)])
    return len(gens),tau(Pm)*2**len(gens),rank(full),rank(sym)
for s in [(4,2),(0,6),(5,1),(6,0),(1,5),(3,3),(0,4),(7,0)]:
    print(s,atom_test(*s),atom_test(*s,rev=True))
# orbit weight in (2,2) sig order (1,1,-1,-1): P=(1+e0)(1+e1e2)/4 ; reproduce 36/85 by my engine
A=Alg((1,1,-1,-1))
order=[]
for k in range(5):
    for c in combinations(range(4),k): order.append(sum(1<<i for i in c))
seed=[1, 2, 0, -1, 3, 0, 1, 1, -2, 1, 0, 2, 1, -1, 0, 3]
el=lambda sh:{b:F(seed[(i+sh)%16]) for i,b in enumerate(order) if seed[(i+sh)%16]!=0}
Pm=A.mul(L((F(1,2),ONE),(F(1,2),A.g(0))),L((F(1,2),ONE),(F(1,2),A.mul(A.g(1),A.g(2)))))
x,y=el(0),el(5)
# own route: weight = (tau(P x+ y P y+ x))/(tau(P x+x) tau(P y+ y)) * tau(P)
num=tau(A.P(Pm,A.dag(x),y,Pm,A.dag(y),x)); nx=tau(A.P(Pm,A.dag(x),x)); ny=tau(A.P(Pm,A.dag(y),y))
print('weight (2,2) seed0:',num*tau(Pm)/(nx*ny))
