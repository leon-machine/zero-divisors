# Referee R3, own route: tiny Clifford algebra with sympy coefficients; no lib/gtg.py.
import sympy as sp, itertools, sys
def mk(sig):
    d=len(sig)
    def bl(a,b):
        s=1
        for i in range(d):
            if b>>i&1:
                s*= (-1)**bin(a>>(i+1)).count('1')
                if a>>i&1: s*=sig[i]
        return a^b,s
    def gp(A,B):
        o={}
        for a,x in A.items():
            for b,y in B.items():
                k,s=bl(a,b); o[k]=o.get(k,0)+s*x*y
        return {k:sp.expand(v) for k,v in o.items() if sp.expand(v)!=0}
    return gp
def add(*Ms):
    o={}
    for M in Ms:
        for k,v in M.items(): o[k]=o.get(k,0)+v
    return {k:sp.expand(v) for k,v in o.items() if sp.expand(v)!=0}
def sc(c,M): return {k:sp.expand(c*v) for k,v in M.items() if sp.expand(c*v)!=0}
def gr(M,r): return {k:v for k,v in M.items() if bin(k).count('1')==r}
def grades(M): return sorted({bin(k).count('1') for k in M})
def run(sig, G, Om, X, label):
    d=len(sig); gp=mk(sig)
    def wedge(A,B):
        o={}
        for ra in grades(A):
            for rb in grades(B):
                o=add(o,gr(gp(gr(A,ra),gr(B,rb)),ra+rb))
        return o
    def comm(A,B): return sc(sp.Rational(1,2),add(gp(A,B),sc(-1,gp(B,A))))
    def dd(M,mu): return {k:sp.diff(v,X[mu]) for k,v in M.items() if sp.diff(v,X[mu])!=0}
    def D(mu,M): return add(dd(M,mu),comm(Om[mu],M))
    g=[{1<<a:G[mu,a] for a in range(d) if G[mu,a]!=0} for mu in range(d)]   # g^mu
    Th=[add(*[wedge(g[l],D(l,g[mu])) for l in range(d)]) for mu in range(d)]
    R=lambda l,n: add(dd(Om[n],l),sc(-1,dd(Om[l],n)),comm(Om[l],Om[n]))
    calR=lambda l,n: sc(-1,R(l,n))        # calR(g_l ^ g_n)
    res=[]
    for mu in range(d):
        C=add(*[wedge(wedge(g[n],g[l]),comm(calR(l,n),g[mu])) for l in range(d) for n in range(d) if l!=n])
        rhs=add(add(*[wedge(g[l],D(l,Th[mu])) for l in range(d)]),sc(-1,add(*[wedge(Th[n],D(n,g[mu])) for n in range(d)])))
        diff=add(sc(sp.Rational(1,2),C),sc(-1,rhs))
        res.append((bool(C),diff=={}))
    P=[add(*[wedge(g[l],calR(l,r)) for l in range(d) if l!=r]) for r in range(d)]
    print(label,'torsion nonzero:',any(Th),'| (C nonzero, (ii) holds) per mu:',res,'| P nonzero:',[bool(p) for p in P],'| curvature nonzero:',any(R(l,n) for l in range(d) for n in range(l)))
    return Th,P
t,x,y,z=sp.symbols('t x y z')
X=[t,x,y,z]; sig=[1,-1,-1,-1]
G=sp.Matrix([[1+x*y,t/2,0,0],[0,1-t,x,0],[0,0,1+y,x/5],[t*x,0,0,1+z**2]])
Om=[{3:x+2*y,6:z},{5:1+z,10:y*t},{9:x,6:2*t-z},{12:x+y,5:t}]
run(sig,G,Om,X,'A torsion Cl(1,3):'); sys.stdout.flush()
run(sig,G,[{},{},{},{}],X,'B Omega=0 nonholonomic:'); sys.stdout.flush()
# C: g^mu = exp(phi) e^mu, Omega(e_mu) = k grad(phi) ^ e_mu ; torsion-free iff k = 1 (referee's hand derivation)
phi=x*y+t*z+t**2*x/3-y**3/2
E=sp.exp(phi)
gp=mk(sig)
grad={1<<a:sig[a]*sp.diff(phi,X[a]) for a in range(4)}   # nabla phi = e^a d_a phi, e^a = sig e_a
def wedge2(A,B):
    P=gp(A,B); return {k:v for k,v in P.items() if bin(k).count('1')==2}
for k in (1,2):
    Omc=[sc(k,wedge2(grad,{1<<m:sig[m]*0+1})) for m in range(4)]   # Omega(e_mu), e_mu = basis vector
    Gc=sp.Matrix(4,4,lambda m,a: E*sig[a] if m==a else 0)        # g^mu = E e^mu
    run(sig,Gc,Omc,X,'C conformal k=%d:'%k); sys.stdout.flush()
