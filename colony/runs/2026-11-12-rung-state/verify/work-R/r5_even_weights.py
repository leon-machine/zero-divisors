"""Claim 1 (iv) hidden hypothesis: the no-two-valued-weight obstruction needs ODD tests.
(a) The atom of weight 1/2 used in (iv) is not even.
(b) On the even subalgebra of Cl(2,2) a string DOES extend to a two-valued additive weight on all even
    self-adjoint idempotents: explicit rule, checked on a sample (proof in the report)."""
from myalg import *
half = F(1, 2)
es, fs = jw(2)
I = SM.eye(4)
v = [(es[j] + fs[j]).sc(half) for j in range(2)]
w = [(es[j] - fs[j]).sc(half) for j in range(2)]
on = [v[j] * w[j] for j in range(2)]; off = [w[j] * v[j] for j in range(2)]
P = {(a, b): (on[0] if a else off[0]) * (on[1] if b else off[1]) for a in (0, 1) for b in (0, 1)}
Gam = fs[0] * es[0] * fs[1] * es[1]
is_even = lambda x: Gam * x == x * Gam            # for n even the even subalgebra is the centraliser of Gamma
# check that claim: centraliser of Gamma has dimension 8 and equals the span of even blades
gens = es + fs
evb = []
for r in (0, 2, 4):
    for c in combinations(range(4), r):
        x = I
        for g in c:
            x = x * gens[g]
        evb.append(x)
print("all even blades commute with Gamma:", all(is_even(x) for x in evb),
      "; odd generators do not:", not any(is_even(g) for g in gens))
# (a) the author's atom: string s = (1,0) (rung 0 on, rung 1 off); y = P_s + v_1 P_s
s = (1, 0)
y = P[s] + v[1] * P[s]
Pi = (y * y.T()).sc(half)
st = lambda x: (P[s] * x).tr()
print("(a) atom idempotent, self-adjoint:", Pi * Pi == Pi, Pi.T() == Pi, "; weight from the string:", st(Pi),
      "; is the atom even?", is_even(Pi))
# (b) the corner containing s: strings of the same parity, here (1,0) and (0,1). Partial isometry
# between them inside the even algebra: t = v_1 w_0 (moves the quantum from rung 0 to rung 1).
t = v[1] * w[0]
print("    t even:", is_even(t), "; t P_s t^T = P_(0,1):", t * P[s] * t.T() == P[(0, 1)])
other = {(1, 0): (0, 1)}
def line_proj(corner_basis, x, y_):
    """Projector onto the line (x, y) in the 2x2 corner with basis strings (b1, b2), via t."""
    b1, b2, tt = corner_basis
    nrm = F(x * x + y_ * y_)
    return (P[b1].sc(x * x) + P[b2].sc(y_ * y_) + (tt * P[b1]).sc(x * y_) + (P[b1] * tt.T()).sc(x * y_)).sc(1 / nrm)
cornA = ((1, 0), (0, 1), v[1] * w[0])          # contains the chosen string s
cornB = ((0, 0), (1, 1), v[1] * v[0])          # the other parity sector
def g_rank1(corner, x, y_):
    if corner is not cornA:
        return 0
    if x == 0:
        return 0
    m = F(y_, x)
    return 1 if (-1 < m <= 1) else 0
dirs = [(x, y_) for x in range(-3, 4) for y_ in range(-3, 4) if (x, y_) != (0, 0)]
# normalise directions to lines
lines = {}
for x, y_ in dirs:
    from math import gcd
    gg = gcd(abs(x), abs(y_))
    x2, y2 = x // gg, y_ // gg
    if x2 < 0 or (x2 == 0 and y2 < 0):
        x2, y2 = -x2, -y2
    lines[(x2, y2)] = True
lines = list(lines)
ok = True
projs = []
for corner in (cornA, cornB):
    for (x, y_) in lines:
        Q = line_proj(corner, x, y_)
        ok &= Q * Q == Q and Q.T() == Q and is_even(Q) and Q.tr() == 1
        projs.append((corner, (x, y_), Q))
print("    sample: all", len(projs), "line projectors are even rank-one self-adjoint idempotents:", ok)
# additivity on every context of four rank-one even atoms (two orthogonal lines in each corner)
ctx_ok, nctx = True, 0
for (cA, lA, QA) in projs:
    if cA is not cornA:
        continue
    lA2 = (-lA[1], lA[0])
    for (cB, lB, QB) in projs:
        if cB is not cornB:
            continue
        lB2 = (-lB[1], lB[0])
        QA2 = line_proj(cornA, *lA2); QB2 = line_proj(cornB, *lB2)
        tot = QA + QA2 + QB + QB2
        if not (tot == I):
            ctx_ok = False
        val = g_rank1(cornA, *lA) + g_rank1(cornA, *lA2) + g_rank1(cornB, *lB) + g_rank1(cornB, *lB2)
        ctx_ok &= val == 1
        nctx += 1
print(f"    two-valued rule sums to 1 on all {nctx} sampled even contexts:", ctx_ok,
      "; g(P_s) =", g_rank1(cornA, 1, 0), "; g(P_(0,1)) =", g_rank1(cornA, 0, 1))
