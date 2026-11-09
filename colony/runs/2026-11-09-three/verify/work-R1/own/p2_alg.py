import sys; sys.path.insert(0,'../pylib')
import sympy as sp
t,r,M,L=sp.symbols('t r M L',positive=True)
lam=(L-2)/2; f=1-2*M/r
h0=sp.Function('h0')(t,r); h1=sp.Function('h1')(t,r)
Eth=sp.diff(h0,t)/f-sp.diff(f*h1,r)
Er=sp.diff(h1,t,2)-sp.diff(h0,t,r)+2*sp.diff(h0,t)/r+(L-2)*f*h1/r**2
Et=f*(sp.diff(h0,r,2)-sp.diff(h1,t,r)-2*sp.diff(h1,t)/r)-(L/r**2-4*M/r**3)*h0
Q=f*h1/r; Vo=f*(L/r**2-6*M/r**3)
D=lambda u: f*sp.diff(u,r)
print('RW identity', sp.simplify(sp.diff(Q,t,2)-D(D(Q))+Vo*Q-(f/r)*(Er+sp.diff(f*Eth,r)-2*f*Eth/r)))
print('Bianchi', sp.simplify(sp.diff(Et,t)+f*sp.diff(Er,r)+2*f*Er/r+(L-2)*f*Eth/r**2))
Ve=f*(2*lam**2*(lam+1)*r**3+6*lam**2*M*r**2+18*lam*M**2*r+18*M**3)/(r**3*(lam*r+3*M)**2)
c=lam*(lam+1)/(3*M); W=3*M*f/(r*(lam*r+3*M))+c
print('W odd', sp.simplify(W**2-D(W)-c**2-Vo), 'W even', sp.simplify(W**2+D(W)-c**2-Ve))
print('Vo/f at 2M', sp.simplify((Vo/f).subs(r,2*M)), ' l=2:', sp.simplify((Vo/f).subs(r,2*M).subs(L,6)))
print('Ve/f at 2M', sp.factor(sp.simplify((Ve/f).subs(r,2*M))), ' l=2:', sp.simplify((Ve/f).subs(r,2*M).subs(L,6)))
l=sp.symbols('l'); print('c in l:', sp.factor(c.subs(L,l*(l+1))))
