import numpy as np
from scipy.integrate import solve_ivp
def run(k, mu, L=40.0):
    def f(eta, s):
        h = np.array([k, 0.0, mu*eta])
        return 2*np.cross(h, s)
    # adiabatic start at eta=L with first-order correction d1 = (1/2) c delta sigma2
    om = np.hypot(k, mu*L); hh = np.array([k, 0, mu*L])/om; c = k/om; d = mu/om**2
    s0 = hh + 0.5*c*d*np.array([0,1,0]); s0/=np.linalg.norm(s0)
    sol = solve_ivp(f, (L, 0.0), s0, rtol=1e-12, atol=1e-13, method='DOP853')
    s = sol.y[:, -1]
    x = s[2]; q = x*x
    sin_ = np.array([s[0], s[1], -s[2]])
    n0 = 0.5*(1-np.sqrt(1-q))
    wall = 0.5*(1 - s[0])   # occupation of wall-instant vacuum sigma1 over s_out
    return q, np.exp(-np.pi*k*k/mu), abs(x), np.exp(-np.pi*k*k/(2*mu)), wall, mu**2/(16*k**4)
for k, mu in [(0.3,1),(0.6,1),(1.0,1),(1.3,1),(1.0,2.5),(2.0,1)]:
    print(k, mu, ["%.6e"%v for v in run(k,mu)])
