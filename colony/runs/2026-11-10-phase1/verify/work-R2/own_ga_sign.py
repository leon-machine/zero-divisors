"""Referee R2: one exact point computed in Cl(1,3) with the store's product (signature (+,-,-,-)) through lib/GA.py,
to tie the proposals' hand-entered (-,+,+,+) components to the stored conventions.
Point: M = 7, a = 3, r = 4 (so sqrt(P) = 5), u = 3/5, phi = 0. Cartesian frame e0, e1, e2, e3 of the flat background."""
import sys
from fractions import Fraction as F
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA
SQ = GA.sig(1, 3)
def vec(c):
    return GA.add(*[GA.scal(F(x), GA.gen(i)) for i, x in enumerate(c)])
def dot(x, y):
    return GA.dot(x, y, SQ)
M, a, r, u = F(7), F(3), F(4), F(3, 5)
sq, st = F(5), F(4, 5)                       # sqrt(P), sin theta
S, P, D = r*r + a*a*u*u, r*r + a*a, r*r - 2*M*r + a*a
H = M*r/S
# coordinate vectors of the oblate chart at phi = 0: x = sqrt(P) sin(theta) cos(phi), y = ... sin(phi), z = r u
dt = vec([1, 0, 0, 0])
dr = vec([0, r/sq*st, 0, u])
du = vec([0, -sq*u/st, 0, r])
dp = vec([0, 0, sq*st, 0])
k = GA.add(dt, GA.neg(dr), GA.scal(a/P, dp))          # the vector with eta(-+++)-lowered components (-1, -S/P, 0, a(1-u^2))
print("Q(k) =", dot(k, k))
hinv = lambda b: GA.sub(b, GA.scal(H*dot(b, k), k))    # hb^{-1}(b) = b - H (b.k) k
def gram(vs):
    w = [hinv(v) for v in vs]
    return [[dot(x, y) for y in w] for x in w]
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0]) + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
for Om in (F(0), F(2, 7), a/P):
    T = GA.add(dt, GA.scal(Om, dp))
    d = det3(gram([T, du, dp]))
    print("Omega =", Om, ": Gram det in the store's product =", d, "| +Delta Sigma =", D*S, "| equal:", d == D*S)
# general slope: det = +Sigma (Delta + (1-u^2) R'^2) in the store's product
Rp = F(-5, 11)
d = det3(gram([dt, GA.add(du, GA.scal(Rp, dr)), dp]))
print("slope", Rp, ":", d == S*(D + (1-u*u)*Rp*Rp))
# Killing norm of K = hb^{-1}(d_t + Omega_H d_phi) evaluated off the horizon: Q(K) = Delta Sigma / P^2 with Omega = a/P
K = hinv(GA.add(dt, GA.scal(a/P, dp)))
print("Q(K) at Omega = a/P:", dot(K, K), "| Delta Sigma / P^2 =", D*S/(P*P), "(Delta < 0 here: between the loci, K spacelike, Q(K) < 0)")
Km = hinv(GA.add(dt, GA.scal(-a/P, dp)))
print("Q(K) with Omega = -a/P:", dot(Km, Km))
