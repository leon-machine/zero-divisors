"""Referee R2, own route (numeric, mpmath installed outside the repository).
(1) exact volume rate of the surface at proper distance rho0 from a horizon locus, against kappa rho0 A;
(2) the inner locus as a -> 0; (3) Schwarzschild three roots; (4) level-set ratio against the stated bounds."""
import mpmath as mp
mp.mp.dps = 18
import sys
PART1 = '--skip1' not in sys.argv

def stretched(M, a, rho0, which='+', side=+1, nu=9):
    """V' of the surface at proper distance rho0 from r_which, on the side r = r0 + side*delta.
    det h = -Sigma (Delta + (1-u^2) delta'^2) (general slope, own symbolic result B2)."""
    s = mp.sqrt(M*M - a*a); rp, rm = M + s, M - s
    r0 = rp if which == '+' else rm
    def absDelta_over_x(x):          # |Delta|/x with r = r0 + side*x
        # Delta = (r-rp)(r-rm)
        if which == '+':
            return abs(2*s + side*x)
        return abs(2*s - side*x)
    def ell(x, u):                   # proper length from the locus to r0 + side*x, substitution x' = t^2
        f = lambda t: 2*mp.sqrt(((r0 + side*t*t)**2 + a*a*u*u)/absDelta_over_x(t*t))
        return mp.quad(f, [0, mp.sqrt(x)])
    def dell_du(x, u):
        f = lambda t: 2*a*a*u/mp.sqrt(((r0 + side*t*t)**2 + a*a*u*u)*absDelta_over_x(t*t))
        return mp.quad(f, [0, mp.sqrt(x)])
    def integrand(u):
        Sig0 = r0*r0 + a*a*u*u
        x0 = rho0**2*2*s/(4*Sig0)
        if which == '-' and side > 0:
            # between the loci: ell is increasing in x on (0, 2s); bracket and bisect (the leading guess fails at small a)
            lo_, hi_ = mp.mpf(0), 2*s
            if ell(hi_, u) < rho0:
                return mp.nan
            for _ in range(70):
                mid = (lo_ + hi_)/2
                if ell(mid, u) < rho0:
                    lo_ = mid
                else:
                    hi_ = mid
            x = (lo_ + hi_)/2
        else:
            x = mp.findroot(lambda y: ell(y, u) - rho0, x0)
        r = r0 + side*x
        Sig = r*r + a*a*u*u
        Dl = (r - rp)*(r - rm)
        dxdu = -dell_du(x, u)/mp.sqrt(Sig/abs(Dl))
        slope = side*dxdu
        return mp.sqrt(abs(Sig*(Dl + (1 - u*u)*slope**2)))
    V = 2*mp.pi*2*mp.quad(integrand, mp.linspace(0, 1, 5))
    P0 = r0*r0 + a*a
    kappa = (rp - rm)/(2*P0)
    return V/(kappa*rho0*4*mp.pi*P0)

print("(1) V'_{rho0}/(kappa_+ rho0 A_+), outer locus, outside | inside")
for (M, a, rho0) in [] if not PART1 else [(50, 0, 2), (50, 30, 2), (50, 48, 2), (500, 300, 2), (500, 480, 2), (500, 499.9, 2), (50, 30, 8)]:
    M, a, rho0 = mp.mpf(M), mp.mpf(a), mp.mpf(rho0)
    o = stretched(M, a, rho0, '+', +1); i = stretched(M, a, rho0, '+', -1)
    print(f"  M={M} a={a} rho0={rho0}: {mp.nstr(o, 12)} | {mp.nstr(i, 12)}   (M/rho0)^2 (ratio-1) = {mp.nstr((o-1)*(M/rho0)**2, 6)} | {mp.nstr((i-1)*(M/rho0)**2, 6)}")
print("    Schwarzschild expansion predicts (M/rho0)^2 (ratio - 1) -> 1/12 outside:", mp.nstr(mp.mpf(1)/12, 6))

print("(2) inner locus, surface at proper distance rho0 = 2 on the side between the loci: V'/(kappa_- rho0 A_-)")
for (M, a) in [(500, 480), (500, 300), (500, 150), (500, 100), (500, 60), (500, 30), (500, 10), (500, 1)][: (0 if '--skip2' in sys.argv else 7)]:   # a = 1 is too slow for the bisection; recorded results in R2.md
    M, a = mp.mpf(M), mp.mpf(a)
    rm = M - mp.sqrt(M*M - a*a)
    v = stretched(M, a, mp.mpf(2), '-', +1)
    print(f"  M={M} a={a}: r_-^3/(rho0^2 M) = {mp.nstr(rm**3/(4*M), 5)}  ratio = {mp.nstr(v, 10)}")
print("    a = 0 limit: proper-time level set tau = rho0 of the Schwarzschild interior, V' = 12 pi M rho0, ratio 3")

print("(3) Schwarzschild: roots of r^3 |2M - r| = 4 M^2 and their proper distances from the horizon")
for rc in (2, 4, 10):
    M = mp.mpf(rc)**3/2
    g = lambda r: r**3*abs(2*M - r) - 4*M*M
    r1 = mp.findroot(g, (rc, rc + mp.mpf(1)/rc), solver='anderson')
    r2 = mp.findroot(g, (2*M - 1/M, 2*M - 1/(4*M)), solver='anderson')
    r3 = mp.findroot(g, (2*M + 1/(4*M), 2*M + 1/M), solver='anderson')
    l2 = mp.quad(lambda t: 2*mp.sqrt((2*M - t*t)), [0, mp.sqrt(2*M - r2)])
    l3 = mp.quad(lambda t: 2*mp.sqrt((2*M + t*t)), [0, mp.sqrt(r3 - 2*M)])
    print(f"  r_c={rc} M={M}: root1 - r_c = {mp.nstr(r1 - rc, 8)} (1/r_c = {mp.nstr(mp.mpf(1)/rc, 6)}); inside proper time {mp.nstr(l2, 10)}; outside proper distance {mp.nstr(l3, 10)}")

print("(4) level set |z| = rho: V'(M,a,rho)/V'(M,0,rho), lower bound, G(eps), 1 - eps/12, needed sqrt(1-a^2/M^2), Q ratio")
def levelset(M, a, rho):
    def integrand(u):
        R = mp.sqrt(rho*rho - a*a*u*u)
        B = R*(2*M - R) - a*a - (1 - u*u)*a**4*u*u/(R*R)
        return rho*mp.sqrt(B)
    V = 2*mp.pi*2*mp.quad(integrand, [0, 1])
    V0 = 4*mp.pi*rho**mp.mpf(1.5)*mp.sqrt(2*M - rho)
    eps = a*a/(rho*rho); dl = mp.mpf(5)/2*a*a/(rho*(2*M - rho))
    G = mp.quad(lambda u: (1 - eps*u*u)**mp.mpf(0.25), [0, 1])
    return V/V0, (1 - dl)*(1 - eps/3), (1 - dl)*G, G, 1 - eps/12, mp.sqrt(1 - a*a/(M*M))
for (M, rho, fa) in [(8, None, 0.8), (32, None, 0.8), (500, None, 0.8), (500, None, 0.4), (500, None, 0.1), (10**6, None, 0.8),
                     (10**6, None, 0.01), (30, 10, 0.8), (30, 10, 0.2), (3000, 1000, 0.8), (3000, 5, 0.8)]:
    M = mp.mpf(M); rho = (2*M)**(mp.mpf(1)/3) if rho is None else mp.mpf(rho); a = mp.mpf(fa)*rho
    x, lo, loG, G, up, need = levelset(M, a, rho)
    ok = lo <= loG <= x <= G <= up
    print(f"  M={mp.nstr(M,7)} rho={mp.nstr(rho,6)} a/rho={fa}: ratio={mp.nstr(x,10)} lo={mp.nstr(lo,8)} (1-d)G={mp.nstr(loG,8)} G={mp.nstr(G,10)} up={mp.nstr(up,8)} need={mp.nstr(need,10)} Qratio={mp.nstr(x/need,8)} bounds_ok={ok}")
