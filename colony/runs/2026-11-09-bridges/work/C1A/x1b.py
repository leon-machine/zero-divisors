import sys, time
sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations
import GA
exec(open('x1.py').read().split("for (p,q) in")[0])

def state(p,q,SQ,nz,blade,D,I,n):
    ONE=GA.sc(1)
    # start: product of (1+h)/2 over a maximal commuting independent set
    comm=[]
    for h in nz:
        if all(GA.commutes(h,c,SQ) for c in comm):
            # independent: h not in generated group -> test by building projector rank later; pick greedily until D = 2^len
            comm.append(h)
            if 2**len(comm)==D: break
    # check independence through scalar part of product of projectors
    rho=ONE
    for c in comm: rho = GA.scal(F(1,2), GA.mul(rho, GA.add(ONE,c),SQ))
    return rho
def x_of(rho,nz,SQ,D):
    return [D*GA.mul(rho,h,SQ).get((),F(0)) for h in nz]
def rot(rho,B,t,SQ):
    ONE=GA.sc(1)
    assert GA.eq(GA.mul(B,B,SQ),GA.sc(-1))
    V=GA.add(ONE,GA.scal(t,B)); Vi=GA.scal(1/(1+t*t),GA.sub(ONE,GA.scal(t,B)))
    return GA.mul(GA.mul(V,rho,SQ),Vi,SQ)

for (p,q) in [(1,3),(6,0)]:
    SQ,n,I,nz,gens,group,D,blade = analyse(p,q)
    ONE=GA.sc(1)
    rho0=state(p,q,SQ,nz,blade,D,I,n)
    assert GA.eq(GA.mul(rho0,rho0,SQ),rho0) and rho0.get((),0)==F(1,D), rho0.get(())
    rho=rho0
    ks=[GA.mul(I,h,SQ) for h in nz]
    for j,t in enumerate([F(1,2),F(2,3),F(3,5),F(1,3),F(5,7),F(2,5)]):
        rho=rot(rho,ks[(5*j+1)%len(ks)],t,SQ)
    assert GA.eq(GA.mul(rho,rho,SQ),rho)
    for name,r in (('blade state',rho0),('generic',rho)):
        x=x_of(r,nz,SQ,D)
        print((p,q),name,'x=',[str(v) for v in x][:6],'sum x^2 =',sum(v*v for v in x),'(D-1=',D-1,')')
        G=len(group); m=len(nz)
        # second moments
        M2=[[F(0)]*m for _ in range(m)]
        m4=F(0)
        for g in group:
            y=[g[i][1]*x[g[i][0]] for i in range(m)]
            for a in range(m):
                ya=y[a]
                if ya:
                    for b in range(m): M2[a][b]+=ya*y[b]
            m4+=y[0]**4
        ok=all(M2[a][b]/G==(F(1,D+1) if a==b else 0) for a in range(m) for b in range(m))
        print('  second moment = delta/(D+1):',ok,'  avg x0^4 =',m4/G,' Haar 3/((D+1)(D+3)) =',F(3,(D+1)*(D+3)))
