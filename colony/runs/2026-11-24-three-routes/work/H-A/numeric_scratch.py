# Scratch only (floats): numerical confirmation of the Landau-Zener value and the midpoint profile.
import numpy as np
from scipy.integrate import solve_ivp, quad
def bloch(eta, s, k, mu):
    h = np.array([k, 0.0, mu*eta])
    return 2*np.cross(h, s)
def s_out_at0(k, mu, T=60.0):
    # start at large eta on the superadiabatic approx: s = hhat + (mu k/(2 w^3)) e2 (first order), integrate back to 0
    w = np.hypot(k, mu*T); hh = np.array([k,0,mu*T])/w
    s = hh + np.array([0, mu*k/(2*w**3), 0]); s/=np.linalg.norm(s)
    sol = solve_ivp(bloch, [T, 0.0], s, args=(k,mu), rtol=1e-11, atol=1e-13, method='DOP853')
    return sol.y[:,-1]
for k,mu in [(0.5,1.0),(1.0,1.0),(1.5,1.0),(1.0,2.0),(2.0,3.0)]:
    so = s_out_at0(k,mu)
    si = so*np.array([1,1,-1])
    q = 0.5*(1-si@so); nu=k*k/mu
    m = si+so; m/=np.linalg.norm(m)
    n0 = 0.5*(1-m@so)
    print(k,mu,'q',q,'exp(-pi nu)',np.exp(-np.pi*nu),'n0',n0,'formula',0.5*(1-np.sqrt(1-np.exp(-np.pi*nu))),
          's3^2',so[2]**2,'phi0',np.arctan2(so[1],so[0]),'mu/2k^2',mu/(2*k*k), 'wall-inst beta^2', 0.5*(1-so[0]), 'mu^2/16k^4', mu**2/16/k**4)
I = quad(lambda x: x*x*(1-np.sqrt(1-np.exp(-x*x))), 0, 12)[0]/(2*np.pi**2)
print('BFT integral I', I)
