"""R3: independent recomputation for the colour-angle proposal (new or changed statements).

Kill conditions (written before running):
 K1 mirror: if sigma (b_mn -> -b'_mn) is not multiplicative, or sigma(I4) != +I4', or if sigma o Ad(g0) is not
    multiplicative or does not send I4 -> -I4' and Theta -> -Theta', the restated clause (iii) is wrong.
 K2 duality: if Theta(I4 F) != -Theta(F), or if some linear g of the vectors induces F -> I4 F on bivectors
    (tested via the determinant argument: det(L2 g) = det(g)^3, det(duality on bivectors) = +1, det(g) on
    grade four), the counterexample is wrong.
 K3 further maps: if the imaginary rung boost moves a spacetime bivector or I4, or omega fails to commute with
    a bivector of Cl(10,0), or Ad(D) fails to keep <XY>_0, the claim that each fixes the term fails.
"""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as Fr
from itertools import combinations
import GA

ok_all = True
def rep(label, ok):
    global ok_all
    ok_all = ok_all and ok
    print(("ok   " if ok else "FAIL ") + label)

S = GA.sig(1, 3)
Sp = tuple(-s for s in S)
def g4(x): return {b: c for b, c in x.items() if len(b) == 4}
def th(x, y, sq):  # grade-4 part of symmetrised product
    return g4(GA.scal(Fr(1, 2), GA.add(GA.mul(x, y, sq), GA.mul(y, x, sq))))
I4 = {(0, 1, 2, 3): Fr(1)}
pairs = list(combinations(range(4), 2))
def biv(cs): return {p: Fr(c) for p, c in zip(pairs, cs) if c}
Fa = biv([3, -2, 1, 4, -7, 2]); Fb = biv([-1, 5, 6, -3, 2, 1])

# even basis as products of generators
even = [()] + pairs + [(0, 1, 2, 3)]
def sigma(x):
    # defined through generator-pair images: e_m e_n -> -e'_m e'_n ; I4 = (e0e1)(e2e3) -> (+)e'0e'1e'2e'3
    out = {}
    for b, c in x.items():
        k = len(b)
        out[b] = c * (-1) ** (k // 2)
    return {b: c for b, c in out.items() if c}
mult = all(sigma(GA.mul({a: Fr(1)}, {b: Fr(1)}, S)) == GA.mul(sigma({a: Fr(1)}), sigma({b: Fr(1)}), Sp)
           for a in even for b in even)
rep("K1 sigma multiplicative on Cl+(1,3) -> Cl+(3,1)", mult)
rep("K1 sigma(I4) = +I4'", sigma(I4) == I4)
t = th(Fa, Fb, S); tp = th(sigma(Fa), sigma(Fb), Sp)
rep("K1 Theta'(sigma F) has the same I4' coefficient: %s vs %s" % (t, tp), t == tp and t != {})
for v in range(4):
    gv = GA.gen(v); gvi = GA.scal(Fr(1, S[v]), gv)
    adv = lambda x: GA.mul(GA.mul(gv, x, S), gvi, S)
    tau = lambda x: sigma(adv(x))
    m2 = all(tau(GA.mul({a: Fr(1)}, {b: Fr(1)}, S)) == GA.mul(tau({a: Fr(1)}), tau({b: Fr(1)}), Sp)
             for a in even for b in even)
    rep("K1 sigma o Ad(gamma_%d): multiplicative, I4 -> -I4', Theta -> -Theta'" % v,
        m2 and tau(I4) == GA.scal(-1, I4) and th(tau(Fa), tau(Fb), Sp) == GA.scal(-1, t))
# centre of the even algebra is span{1, I4}: any automorphism sends I4 to +-I4; so exactly two signs
cen = [b for b in even if all(GA.commutes({b: Fr(1)}, {a: Fr(1)}, S) for a in even)]
rep("K1 centre of Cl+(1,3) spanned by 1 and I4: %s" % cen, cen == [(), (0, 1, 2, 3)])

# K2 duality
d = lambda x: GA.mul(I4, x, S)
rep("K2 I4 F is a bivector", all(len(b) == 2 for b in d(Fa)))
rep("K2 Theta(I4 Fa, I4 Fb) = -Theta(Fa, Fb)", th(d(Fa), d(Fb), S) == GA.scal(-1, t))
# matrix of duality on bivectors
def col(x): return [x.get(p, Fr(0)) for p in pairs]
Dm = [list(r) for r in zip(*[col(d({p: Fr(1)})) for p in pairs])]
def det(M):
    M = [r[:] for r in M]; n = len(M); dd = Fr(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if M[r][i] != 0), None)
        if piv is None: return Fr(0)
        if piv != i: M[i], M[piv] = M[piv], M[i]; dd = -dd
        dd *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            M[r] = [a - f * b for a, b in zip(M[r], M[i])]
    return dd
D2 = [[sum(Dm[i][k] * Dm[k][j] for k in range(6)) for j in range(6)] for i in range(6)]
rep("K2 duality squares to -1 on bivectors, det = %s" % det(Dm),
    D2 == [[Fr(-1) if i == j else Fr(0) for j in range(6)] for i in range(6)] and det(Dm) == 1)
# det of the induced map on bivectors of a generic rational g equals det(g)^3 (outer product, no metric)
g = [[Fr(2), Fr(1), Fr(0), Fr(-1)], [Fr(1, 2), Fr(3), Fr(1), Fr(0)], [Fr(0), Fr(-2), Fr(1), Fr(5)], [Fr(1), Fr(0), Fr(4), Fr(1)]]
def L2(g):
    M = [[Fr(0)] * 6 for _ in range(6)]
    for c, (a, b) in enumerate(pairs):
        for r, (i, j) in enumerate(pairs):
            M[r][c] = g[i][a] * g[j][b] - g[j][a] * g[i][b]
    return M
rep("K2 det(L2 g) = det(g)^3 on a generic g: %s, %s" % (det(L2(g)), det(g) ** 3), det(L2(g)) == det(g) ** 3)
# so a g inducing duality has det g = 1, but g acts on the top grade by det g = 1, while duality acts on
# X ^ Y = <XY>_4 (sym) by -1 (computed above). Contradiction: no such g.

# K3 further maps. Spacetime + two rung planes, choose a different rapidity cos = 3/5, sin = 4/5
sq = (1, -1, -1, -1, -1, 1, 1, -1)  # rung planes (4,5) and (6,7) hyperbolic, other ordering than the check
b1 = {(4, 5): Fr(1)}; b2 = {(6, 7): Fr(1)}
c, s = Fr(3, 5), Fr(4, 5)
def ex(bb, sg): return GA.add(GA.sc(c), GA.scal(sg * s, GA.mul(I4, bb, sq)))
rep("K3 (I4 b)^2 = -1 for each rung plane",
    GA.mul(GA.mul(I4, b1, sq), GA.mul(I4, b1, sq), sq) == GA.sc(-1) and GA.mul(GA.mul(I4, b2, sq), GA.mul(I4, b2, sq), sq) == GA.sc(-1))
R = GA.mul(ex(b1, 1), ex(b2, 1), sq); Ri = GA.mul(ex(b2, -1), ex(b1, -1), sq)
ad = lambda x: GA.mul(GA.mul(R, x, sq), Ri, sq)
rep("K3 rung boost: R R^-1 = 1, moves gamma_0, fixes all 6 spacetime bivectors and I4, keeps Theta",
    GA.mul(R, Ri, sq) == GA.sc(1) and ad(GA.gen(0)) != GA.gen(0)
    and all(ad({p: Fr(1)}) == {p: Fr(1)} for p in pairs) and ad(I4) == I4
    and th(ad(Fa), ad(Fb), sq) == th(Fa, Fb, sq))
s10 = GA.sig(10, 0)
w = {tuple(range(10)): Fr(1)}
rep("K3 omega commutes with all 45 bivectors of Cl(10,0)",
    all(GA.commutes(w, {p: Fr(1)}, s10) for p in combinations(range(10), 2)))
Dd = {(5, 9): Fr(1)}; Di = GA.scal(-1, Dd)
adD = lambda x: GA.mul(GA.mul(Dd, x, s10), Di, s10)
X = {(0, 1): Fr(2), (3, 5): Fr(-1), (6, 9): Fr(4), (2, 7): Fr(1)}
Y = {(0, 1): Fr(1), (3, 5): Fr(3), (6, 9): Fr(-2), (4, 8): Fr(5)}
s0 = {b: c for b, c in GA.mul(X, Y, s10).items() if len(b) == 0}
s0D = {b: c for b, c in GA.mul(adD(X), adD(Y), s10).items() if len(b) == 0}
rep("K3 Ad(D) keeps <XY>_0 (%s) and maps bivectors to bivectors" % s0, s0 == s0D and all(len(b) == 2 for b in adD(X)))
# Ad(D) preserves so(6)+so(4) on indices 0..5 / 6..9: image of a so(6) bivector stays in so(6)
rep("K3 Ad(D) keeps the split 0..5 | 6..9", all(all(set(b) <= set(range(6)) for b in adD({p: Fr(1)}))
                                                for p in combinations(range(6), 2)))
print("ALL OK" if ok_all else "SOME FAILED")
