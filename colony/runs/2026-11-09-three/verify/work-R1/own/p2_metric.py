# Independent route (metric, coordinate Ricci, sympy): linearised Ricci of Schwarzschild + odd-parity RW-gauge perturbation,
# jointly symbolic in (t, r, theta, M, L).
import sys; sys.path.insert(0,'../pylib')
import sympy as sp
t,r,th,ph,M,L,eps=sp.symbols('t r theta phi M L epsilon')
f=1-2*M/r
h0=sp.Function('h0')(t,r); h1=sp.Function('h1')(t,r); S=sp.Function('S')(th)
X=[t,r,th,ph]
g=sp.diag(f,-1/f,-r**2,-r**2*sp.sin(th)**2)
h=sp.zeros(4,4); h[0,3]=h[3,0]=h0*S; h[1,3]=h[3,1]=h1*S
G=g+eps*h
# inverse to first order
gi=g.inv(); Gi=gi-eps*gi*h*gi
def series1(e): return sp.expand(sp.series(sp.expand(e),eps,0,2).removeO()) if e.has(eps) else e
Gam=[[[None]*4 for _ in range(4)] for _ in range(4)]
for a in range(4):
    for b in range(4):
        for c in range(4):
            e=sum(Gi[a,d]*(sp.diff(G[d,b],X[c])+sp.diff(G[d,c],X[b])-sp.diff(G[b,c],X[d])) for d in range(4))/2
            e=sp.expand(e); Gam[a][b][c]=e.coeff(eps,0)+eps*e.coeff(eps,1)
def ric(b,c):
    e=0
    for a in range(4):
        e+=sp.diff(Gam[a][b][c],X[a])-sp.diff(Gam[a][b][a],X[c])
        for d in range(4):
            e+=Gam[a][a][d]*Gam[d][b][c]-Gam[a][c][d]*Gam[d][b][a]
    e=sp.expand(e)
    return e.coeff(eps,0), e.coeff(eps,1)
Eth=sp.diff(h0,t)/f-sp.diff(f*h1,r)
Er=sp.diff(h1,t,2)-sp.diff(h0,t,r)+2*sp.diff(h0,t)/r+(L-2)*f*h1/r**2
Et=f*(sp.diff(h0,r,2)-sp.diff(h1,t,r)-2*sp.diff(h1,t)/r)-(L/r**2-4*M/r**3)*h0
sub={sp.Derivative(S,(th,2)): sp.cot(th)*sp.diff(S,th)-L*S}
for (b,c,name,want) in ((0,3,'t phi',S*Et/2),(1,3,'r phi',S*Er/(2*f)),(2,3,'theta phi',(sp.diff(S,th)-2*sp.cot(th)*S)*Eth/2)):
    r0,r1=ric(b,c)
    r1=r1.subs(sub)
    print(name,'background',sp.simplify(r0),'ratio to claim:',sp.simplify(sp.simplify(r1)/want))
others=[(b,c) for b in range(4) for c in range(b,4) if (b,c) not in ((0,3),(1,3),(2,3))]
print('other components vanish:',all(sp.simplify(ric(b,c)[1].subs(sub))==0 for b,c in others))
