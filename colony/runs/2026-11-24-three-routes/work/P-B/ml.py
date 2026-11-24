"""P-B scratch: the Gram criterion of macroscopic locality (Navascues and Wunderlich 2010, from memory) on the box.
Coarse counts of N pairs at settings (x, y) are asymptotically Gaussian with covariance E_xy (unbiased marginals);
a joint Gaussian for the four coarse variables exists iff the 4 x 4 matrix with unit diagonal, off-diagonal blocks
E_xy and free entries u = cov(A0, A1), v = cov(B0, B1) can be made positive semidefinite. Dual certificate: W_t =
[[t, 0, -1, -1], [0, t, -1, 1], [-1, -1, t, 0], [-1, 1, 0, t]] is positive semidefinite for t^2 >= 2 and pairs to
4t - 2(E00 + E01 + E10 - E11) with every such matrix, independently of u and v."""
import sys
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
import GA
def W(t):
    t = F(t)
    return [[t, 0, -1, -1], [0, t, -1, 1], [-1, -1, t, 0], [-1, 1, 0, t]]
def M(E, u, v):
    return [[1, u, E[0], E[1]], [u, 1, E[2], E[3]], [E[0], E[2], 1, v], [E[1], E[3], v, 1]]
def pair(A, B):
    return sum(F(A[i][j]) * F(B[i][j]) for i in range(4) for j in range(4))
for t in [F(3, 2), F(17, 12), F(99, 70)]:
    print('t =', t, 'inertia of W_t:', GA.congruence_signature([[F(x) for x in r] for r in W(t)]), ' t^2 - 2 =', t * t - 2)
box = (1, 1, 1, -1)
for u, v in [(0, 0), (F(1, 2), F(-1, 3)), (1, -1)]:
    print('box: <W_{3/2}, M(u, v)> =', pair(W(F(3, 2)), M(box, u, v)), '(negative: no positive semidefinite completion)')
# the reversed functional lambda_{+1} and the state lambda_{-1} have the same correlations E(a, b) = -(a.b)
s = (F(-4, 5), F(-3, 5), F(-3, 5), F(4, 5))
a0, a1, b0, b1 = (1, 0), (0, 1), (F(4, 5), F(3, 5)), (F(3, 5), F(-4, 5))
G = [[1, 0, s[0], s[1]], [0, 1, s[2], s[3]], [s[0], s[2], 1, sum(x * y for x, y in zip(b0, b1))], [s[1], s[3], sum(x * y for x, y in zip(b0, b1)), 1]]
print('state and reversal at value -14/5: completed matrix inertia', GA.congruence_signature([[F(x) for x in r] for r in G]))
