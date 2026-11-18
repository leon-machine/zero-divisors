"""Lead 1: the curvature coupling in the heating. Exact arithmetic; pi bracketed by rationals.
Run: python3 lead1.py"""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, gen, dot

S = GA.sig(1, 3); ETA = [1, -1, -1, -1]
E = [gen(i) for i in range(4)]
def vec(c): return {(i,): F(x) for i, x in enumerate(c) if x}
def d(a, b): return dot(a, b, S)

# ---------- K1a: scalar pair to scalar pair with two different couplings, directly in the algebra
def Tscalar(p, q, xi):
    k = add(p, q); k2 = d(k, k)
    return lambda a: add(scal(-d(a, q), p), scal(-d(a, p), q), scal(d(p, q), a), scal(2*xi*d(a, k), k), scal(-2*xi*k2, a))
REC = [E[0]] + [GA.neg(x) for x in E[1:]]
def ip(T1, T2): return sum(d(T1(E[a]), T2(REC[a])) for a in range(4))
def tr(T): return sum(d(REC[a], T(E[a])) for a in range(4))
def B(T1, T2): return ip(T1, T2) - F(1, 2)*tr(T1)*tr(T2)
PTS = [(F(3,5),F(4,5)), (F(5,13),F(12,13)), (F(-7,25),F(24,25)), (F(-8,17),F(15,17)), (F(20,29),F(21,29))]
def kin(c, s_): return vec([1,0,0,1]), vec([1,0,0,-1]), vec([1,s_,0,c]), vec([1,-s_,0,-c])
def integrate_even_quartic(vals):
    """integral over cos in [-1,1] of a polynomial of degree <= 4 through five exact points."""
    n = len(vals); M = [[c**k for k in range(n)] for c, _ in vals]; rhs = [v for _, v in vals]
    for i in range(n):
        piv = next(r for r in range(i, n) if M[r][i] != 0); M[i], M[piv] = M[piv], M[i]; rhs[i], rhs[piv] = rhs[piv], rhs[i]
        for r in range(n):
            if r != i and M[r][i] != 0:
                f = M[r][i]/M[i][i]; M[r] = [a - f*b for a, b in zip(M[r], M[i])]; rhs[r] -= f*rhs[i]
    co = [rhs[i]/M[i][i] for i in range(n)]
    return sum(co[k]*F(2, k+1) for k in range(0, n, 2))
def W_ss(x1, x2):
    vals = []
    for c, s_ in PTS:
        p1, p2, p3, p4 = kin(c, s_)
        vals.append((c, B(Tscalar(p1, p2, x1), Tscalar(p3, p4, x2))**2 / F(4)**4))
    return integrate_even_quartic(vals)*2*F(1, 4)      # times pi; 2 pi from azimuth, 1/2 per identical pair
print('K1a: W_ss/pi for pairs of couplings, against (1 + 5 t1 t2)/180')
ok = True
for x1, x2 in [(F(0), F(0)), (F(0), F(1,6)), (F(1,6), F(1,6)), (F(0), F(153,100)), (F(153,100), F(153,100)), (F(-1,3), F(2,7)), (F(1522584375, 10**9), F(1548079215, 10**9))]:
    t1, t2 = (1 - 6*x1)**2, (1 - 6*x2)**2
    w = W_ss(x1, x2); pred = (1 + 5*t1*t2)/180
    ok = ok and w == pred
    print('  xi =', x1, x2, ' W/pi =', w, ' pred =', pred, w == pred)
print('  K1a holds:', ok)

# ---------- the coefficient for a produced content D from a bath B
def r(CD, tauD, Ns, Nw, Nv, tauB):
    """alpha/pi^3 for produced content with summed spin-two weight CD and summed trace weight tauD."""
    return (F(CD*(Ns + 12*Nv) + 5*tauD*tauB, 225) + F(49*CD*Nw, 4800))/17280
PI_LO, PI_HI = F(314159265358979, 10**14), F(314159265358980, 10**14)
def val(x): return float(x*PI_LO**3)           # display only
C_SM = 4 + 3*45 + 12*12
assert r(C_SM, 4, 4, 45, 12, 4) == F(1519247, 82944000)
assert r(1, 1, 4, 45, 12, 4) == F(5789, 82944000)
print('\nstored: one real scalar', val(r(1,1,4,45,12,4)), ' SM content', val(r(C_SM,4,4,45,12,4)), 'C_SM =', C_SM)

def tau(x): return (1 - 6*x)**2
XLO, XHI = F(1522584375, 10**9), F(1548079215, 10**9)        # stored tilt window
print('tau over the tilt window:', float(tau(XLO)), float(tau(XHI)))
r0 = r(C_SM, 4, 4, 45, 12, 4)
print('\nMirror (one Standard-Model content) from the Standard-Model bath (4,45,12):')
cases = [('stored: all doublets xi=0', 4, 4),
         ('bath doublets conformal, mirror 0', 4, 0),
         ('mirror doublets conformal, bath 0', 0, 4),
         ('both conformal', 0, 0),
         ('both at tilt lower end', 4*tau(XLO), 4*tau(XLO)),
         ('both at tilt upper end', 4*tau(XHI), 4*tau(XHI)),
         ('bath at tilt lower end, mirror 0', 4, 4*tau(XLO)),
         ('bath at tilt upper end, mirror 0', 4, 4*tau(XHI))]
for name, tD, tB in cases:
    x = r(C_SM, tD, 4, 45, 12, tB)
    print('  %-38s c = %.6f  ratio to stored %.6f  floor ratio (c^(1/4)) %.5f' % (name, val(x), float(x/r0), float(x/r0)**0.25))

# a produced real scalar alone, and a vector (no dependence)
print('\nOne produced real scalar from the bath (4,45,12):')
for name, tj, tB in [('xi=0, bath 0', 1, 4), ('conformal', 0, 4), ('tilt lo, bath 0', tau(XLO), 4), ('tilt hi, bath 0', tau(XHI), 4),
                     ('tilt lo, bath tilt lo', tau(XLO), 4*tau(XLO)), ('tilt hi, bath tilt hi', tau(XHI), 4*tau(XHI))]:
    x = r(1, tj, 4, 45, 12, tB); print('  %-28s alpha = %.6e  ratio %.4f' % (name, val(x), float(x/r(1,1,4,45,12,4))))
print('  vector for comparison: %.6e' % val(r(12, 0, 4, 45, 12, 4)))

# working branch: two doublets (8 real scalars) in bath and in each copy
print('\nTwo doublets (8 real scalars), xi = 0:')
C2 = 8 + 3*45 + 12*12
x = r(C2, 8, 8, 45, 12, 8); print('  copy with 8 scalars from bath (8,45,12): c = %.6f ratio %.5f floor %.5f' % (val(x), float(x/r0), float(x/r0)**0.25))
x = r(C_SM, 4, 8, 45, 12, 8); print('  SM copy from bath (8,45,12):           c = %.6f ratio %.5f' % (val(x), float(x/r0)))
x = r(12*22, 0, 8, 45, 12, 8); y = r(12*22, 0, 4, 45, 12, 4); print('  22 vectors: bath (8,45,12) %.6f against %.6f ratio %.5f' % (val(x), val(y), float(x/y)))
C3 = 8 + 3*48 + 12*12
x = r(C3, 8, 8, 48, 12, 8); print('  with three right-handed neutrinos too (8,48,12) both sides: c = %.6f ratio %.5f floor %.5f' % (val(x), float(x/r0), float(x/r0)**0.25))
x = r(12*22, 0, 8, 48, 12, 8); print('  22 vectors from (8,48,12): %.6f ratio %.5f' % (val(x), float(x/y)))

# one extra real scalar carrying the tilt coupling
print('\nOne extra real singlet at the tilt coupling (tilt lo / hi):')
for nm, x in (('lo', XLO), ('hi', XHI)):
    t = tau(x)
    a = r(C_SM, 4, 5, 45, 12, 4 + t)           # in the bath only; mirror = SM content
    b = r(C_SM + 1, 4 + t, 5, 45, 12, 4 + t)   # in the bath and in the mirror copy
    c = r(1, t, 4, 45, 12, 4)                  # produced alone from the SM bath
    print('  %s: bath only c_mirror %.6f (ratio %.5f); both %.6f (ratio %.5f, floor %.5f); as a dark relic alone alpha %.6e'
          % (nm, val(a), float(a/r0), val(b), float(b/r0), float(b/r0)**0.25, val(c)))

# ---------- thresholds in tau^2 (all four real scalars of bath and of each copy at one coupling)
def tau2_at(c_target, pi):
    """tau^2 at which the Standard-Model copy's c equals c_target: c = pi^3 (r_base + tau^2 * 80/(225*17280))."""
    base = r(C_SM, 0, 4, 45, 12, 0)
    return (c_target/pi**3 - base)/F(80, 225*17280)
CSTAR = F(134949, 10**4)
print('\nThresholds (doublets of the bath and of the copies at one coupling):')
for name, ct in [('Pati-Salam (i): four copies reach c* = 13.4949', CSTAR/4), ("eta' = 1 at the mirror's floor (c between 1.539 and 1.54), lower", F(1539, 1000)), ("same, upper", F(154, 100)), ('c = 1 for one copy', F(1))]:
    for pi in (PI_LO, PI_HI):
        t2 = tau2_at(ct, pi)
        # sqrt by bisection on rationals
        lo, hi = F(0), F(1000)
        for _ in range(80):
            mid = (lo + hi)/2
            if mid**4 < t2: lo = mid
            else: hi = mid
        m = lo       # |1 - 6 xi|
        print('  %-62s tau^2 = %.3f |1-6xi| = %.5f  xi = %.6f or %.6f' % (name, float(t2), float(m), float((1 + m)/6), float((1 - m)/6)))
print('  tilt window: tau^2 from %.3f to %.3f' % (float(tau(XLO)**2), float(tau(XHI)**2)))
for x in (XLO, XHI):
    cc = 4*r(C_SM, 4*tau(x), 4, 45, 12, 4*tau(x))
    print('  four copies at xi = %.9f: c in (%.5f, %.5f) against c* = 13.4949; (c*/c)^(1/4) = %.5f' % (float(x), float(cc*PI_LO**3), float(cc*PI_HI**3), (float(CSTAR)/float(cc*PI_LO**3))**0.25))
# untuned fit: margin goes as c^(-1/4)
for x in (XLO, XHI):
    cc = 4*r(C_SM, 4*tau(x), 4, 45, 12, 4*tau(x))
    print('  untuned fit margin at four copies: 1145 x %.4f = %.0f' % ((float(4*r0/cc))**0.25, 1145*(float(4*r0/cc))**0.25))
# radiation: how large must tau be for the floor to reach a visible value
# Delta N_eff at the floor is proportional to c; stored 1.4e-12 at c = 0.568 (energy restatement in progress); threshold 0.01 say
for thr, base_dn in ((F(1, 100), F(14, 10**13)), (F(3, 10), F(14, 10**13))):
    ratio = thr/base_dn
    t2 = tau2_at(r0*PI_LO**3*ratio, PI_LO)
    print('  Delta N_eff = %s at the floor needs c ratio %.3e, tau^2 = %.3e, |1-6xi| about %.0f' % (thr, float(ratio), float(t2), float(t2)**0.25))
