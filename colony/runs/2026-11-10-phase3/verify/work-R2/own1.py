# own route: numbers a + b/pi as pairs of Fractions; V_D via gamma numerically as cross-check
from fractions import Fraction as F
from math import pi, gamma
V=lambda D: pi**(D/2)/gamma(D/2+1)
S=lambda n: 2*pi**((n+1)/2)/gamma((n+1)/2)
for D in range(0,9): assert abs(S(D+1)-2*pi*V(D))<1e-9
# ratios V3/VD exactly: V2=pi, V3=4pi/3, V4=pi^2/2
sh={2:(F(4,3),F(0)),3:(F(1),F(0)),4:(F(0),F(8,3))}  # a + b/pi
towers={'mirror':3,'r1':2,'r7':2,'r3':4,'r5':4}
def tot(s=None,own_cell=False,lam=1,mu=1,d=1.0):
    # general filling: m_r = s_r m, nu_r = 1/(s_r V_D d^D); thickness = common d (times lam/mu) or own WS radius
    s=s or {}
    t=0.0
    m6=s.get('us',1); nu6=1/(m6*V(3)*d**3)
    for k,D in towers.items():
        sr=s.get(k,1); m=sr; nu=1/(sr*V(D)*d**D)
        a=(sr**(1/D))*d           # own Wigner-Seitz radius
        th=a if own_cell else d
        f=m*nu/(m6*nu6)
        if D==4: f*=lam*th
        if D==2: f/=mu*th
        t+=f
    return t
closed=(11*pi+16)/(3*pi)
print('closed',closed, tot(), tot(d=3.7))
sc={'us':2,'mirror':5/3,'r1':1/9,'r7':4,'r3':1,'r5':13/7}
print('rescaled, common-length thickness:',tot(sc), ' own-cell thickness:',tot(sc,own_cell=True))
ex={'r3':16,'r5':16}
print('s=16 on D=4 towers: common',tot(ex),' own-cell',tot(ex,own_cell=True),' claimed 11/3+32/(3pi)=',11/3+32/(3*pi))
# own-cell law: f_r = (m_r/m_6) (V3/V_D) (a_6/a_r)^3
for k,D in towers.items():
    sr=sc.get(k,1); a=sr**(1/D); a6=sc['us']**(1/3)
    print(k, sr/sc['us']*V(3)/V(D)*(a6/a)**3)
print('thick (2,1)',tot(lam=2),11/3+32/(3*pi),' (1,2)',tot(mu=2),7/3+16/(3*pi))
obs=0.1200/0.02237; sig=0.065
print('obs',obs,'closed-obs',(closed-obs)/sig,'burn',(closed-1/200-obs)/sig,'(2,1)',(tot(lam=2)-obs)/sig,'(1,2)',(tot(mu=2)-obs)/sig,'cube',(5-obs)/sig, 'moved',7/3+8/pi,(7/3+8/pi-obs)/sig)
# cubes side 2d, thickness 2d
c=0
for k,D in towers.items():
    f=(1/2**D)/(1/2**3)
    if D==4:f*=2
    if D==2:f/=2
    c+=f
print('cube',c)
# sphere masses: M_r = (l/L) m (l/d)^D
for l,d in [(2,1),(1,3)]:
    print([ (1/(V(D)*d**D))/(2*pi*d)*S(D+1)*l**(D+1) for D in (2,3,4)], [(l/d)**(D+1) for D in (2,3,4)])
# helium: 931.8/936.7
print(931.8/936.7)
