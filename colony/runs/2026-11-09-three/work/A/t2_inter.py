import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from GA import RF
r = RF.var()
def c(x): return RF.const(F(x))
for M in (F(1), F(9,8), F(2,3)):
  for l in (2, 3, 4, 5):
    lam = F((l-1)*(l+2), 2); L = l*(l+1)
    f = c(1) - c(2*M)/r
    VRW = f * (c(L)/(r*r) - c(6*M)/(r*r*r))
    VZ = f * (c(2*lam*lam*(lam+1))*r*r*r + c(6*lam*lam*M)*r*r + c(18*lam*M*M)*r + c(18*M**3)) / (r*r*r*(c(lam)*r + c(3*M))*(c(lam)*r + c(3*M)))
    cc = lam*(lam+1)/(3*M)
    W = c(3*M)*f/(r*(c(lam)*r + c(3*M))) + c(cc)
    dW = f * W.deriv()
    a = (W*W - dW - c(cc*cc)); b = (W*W + dW - c(cc*cc))
    print(M, l, 'W^2-W-c^2==VRW', a.eqrf(VRW), '==VZ', a.eqrf(VZ), '| W^2+W-c^2==VZ', b.eqrf(VZ), '==VRW', b.eqrf(VRW))
    # horizon values
    print('   VRW/f at 2M', (VRW/f).eval(2*M), 'VZ/f at 2M', (VZ/f).eval(2*M), 'W at 2M', W.eval(2*M), cc)
