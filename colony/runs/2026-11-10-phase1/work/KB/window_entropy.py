# scratch (floats; not evidence): entropy of one array (weights kappa(k+1/2), beta = 2 pi/kappa) against the
# entropy of the continuum of one chiral complex component over one window of Killing time 2 pi/kappa
import math
h=lambda x: (math.log(1+math.exp(-abs(x)))+abs(x)/(math.exp(abs(x))+1)) if abs(x)<700 else 0.0
arr=sum(h(2*math.pi*(k+.5)) for k in range(-60,60))
N=400000; L=60.0
integ=sum(h(-L+(i+.5)*2*L/N) for i in range(N))*2*L/N
print('array', arr, 'half ln2', .5*math.log(2))
print('integral', integ, 'pi^2/3', math.pi**2/3, 'per window = integral/2pi', integ/(2*math.pi), 'pi/6', math.pi/6)
print('ratio continuum/array', (math.pi/6)/(.5*math.log(2)))
# SdS Smarr check (exact): M = 2 T_b S_b - 2 P V with 2TS = kappa_b r_b^2 = 3M - r_b, so stored factor u/(3u-2) = M/(2 T_b S_b)
from fractions import Fraction as F
for M,rb in [(F(1),F(9,4)),(F(2),F(5)),(F(3),F(7))]:
    Lam=3*(1-2*M/rb)/rb**2; assert Lam>0
    kap=(3*M-rb)/rb**2; f1=2*M/rb**2-2*Lam*rb/3; assert kap==f1/2
    u=2*M/rb; assert M/(kap*rb*rb)==u/(3*u-2)
    assert kap*rb*rb + Lam*rb**3/3 == M      # Smarr with the Lambda work term
print('SdS ok')
