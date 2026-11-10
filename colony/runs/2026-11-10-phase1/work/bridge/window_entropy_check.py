# Scratch (floats, decimal 60 digits): not evidence for the store, a recomputation for bridges.md.
from decimal import Decimal as D, getcontext
getcontext().prec = 60
pi = D('3.14159265358979323846264338327950288419716939937510582097494')
ln2 = D(2).ln()
def s(x):   # entropy of a Fermi mode at x = beta*omega
    e = (-x).exp(); n = e/(1+e)
    return -(n*n.ln() + (1-n)*(1-n).ln())
def n(x):
    e = (-x).exp(); return e/(1+e)
K = 40
# array at offset 1/2, beta*omega_k = 2 pi (k+1/2)
S_arr = 2*sum(s(pi*(2*k+1)) for k in range(K))
bE_arr = 2*sum(pi*(2*k+1)*n(pi*(2*k+1)) for k in range(K))
lnZ_above = 2*sum((1+(-pi*(2*k+1)).exp()).ln() for k in range(K))
print('array  S        ', S_arr, ' minus ln2/2:', S_arr-ln2/2)
print('array  beta E   ', bE_arr, ' minus pi/12:', bE_arr-pi/12)
print('array  lnZ above sea', lnZ_above, ' minus (ln2/2 - pi/12):', lnZ_above-(ln2/2-pi/12))
# continuum, one complex chiral component, window L = beta: density of modes L dw/(2 pi) = dx/(2 pi)
# int_0^inf ln(1+e^-x) dx = pi^2/12 ; int_0^inf x/(e^x+1) dx = pi^2/12  (eta(2) = pi^2/12)
eta2 = sum(D((-1)**(m+1))/D(m*m) for m in range(1,200001))
print('eta(2) partial', eta2, ' pi^2/12', pi*pi/12)
print('continuum per window: beta E = pi/12 =', pi/12, ' lnZ = pi/12, S = pi/6 =', pi/6)
print('ratio S_cont/S_arr = pi/(3 ln2) =', pi/(3*ln2), ' ; stored E/(TS) per unit pi/(6 ln2) =', pi/(6*ln2))
# general window ratio r = L/beta: array on circle L (antiperiodic) at beta: x_k = 2 pi (k+1/2)/r
for r in (D(1), D(2), D(4), D(8)):
    S = 2*sum(s(pi*(2*k+1)/r) for k in range(400))
    print('r=',r,' S_circle=',S,' extensive pi r/6=',pi*r/6,' diff=',S-pi*r/6)
# CHSH of the stored pair state, c^2 = 1-n, s^2 = n, r = c^2-s^2 = tanh(x/2); max CHSH = 2 sqrt(1+4c^2s^2) = 2 sqrt(2-r^2)
for x in (D(0), pi, 3*pi):
    nn = n(x); r_ = 1-2*nn
    print('x=',x,' r=',r_,' CHSH max=',2*(2-r_*r_).sqrt())
