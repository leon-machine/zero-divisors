from fractions import Fraction as F
# exact Kerr data in (r_+, t), t = a/r_+
def kerr(rp,t):
    M=rp*(1+t*t)/2; a=t*rp; rm=t*t*rp; s=rp*(1-t*t)/2
    assert s*s==M*M-a*a and rp+rm==2*M and rp*rm==a*a
    kap=(rp-rm)/(2*(rp*rp+a*a)); A4pi=rp*rp+a*a   # A/(4 pi)
    Om=a/(rp*rp+a*a); J=a*M
    return M,a,rm,s,kap,A4pi,Om,J
for rp,t in [(F(9),F(1,3)),(F(8),F(1,2)),(F(65536,1025),F(1,32)),(F(25),F(3,5)),(F(10),F(9,10))]:
    M,a,rm,s,kap,A,Om,J=kerr(rp,t)
    assert 4*kap*M==1-t*t and A/(4*M*M)==1/(1+t*t) and 2*M*Om==t
    assert Om/kap==2*t/(1-t*t)                       # windings of a generator per modular period
    assert a/M==2*t/(1+t*t) and s/M==(1-t*t)/(1+t*t)  # rational point of the circle: t is the half-angle parameter
    # monomial carries N_{p,q}/(4 pi nu A) = (A/16 pi M^2)^p (4 kappa M)^q
    for p,q,val in [(-1,-2,(1+t*t)/(1-t*t)**2),(-1,-1,(1+t*t)/(1-t*t)),(0,0,1)]:
        assert (A/(4*M*M))**p*(4*kap*M)**q==val
    assert (1+t*t)/(1-t*t)==M/s and (1+t*t)/(1-t*t)**2==M*rp/(2*s*s)
    assert 2*A*kap==2*s==2*(M-2*Om*J)                  # rate/(4 pi nu): 2 nu kappa A = 8 pi nu s (A here is A/4pi)
    Am=rm*rm+a*a; kapm=(rp-rm)/(2*Am)
    assert A*Am==4*J*J and kap*A==kapm*Am              # A_+ A_- = (8 pi J)^2 ; kappa_+A_+ = kappa_-A_-
    # fitted slice by IVT: V'(M)/(2 pi) = s * I(M) >= 2 s M >= 4 s  iff M >= 2
    print(rp,t,'M',M,'a/M',a/M,'forms',(1+t*t)/(1-t*t)**2,(1+t*t)/(1-t*t),'windings',Om/kap, 'M>=2',M>=2)
