from ownlib import *
# (1)
sq, mul, v, w = setup(2)
n = [mul(v[j], w[j]) for j in range(2)]
blades = [b for k in (0, 2, 4) for b in combinations(range(4), k)]
evens = [{b: F(1)} for b in blades]
assert len(evens) == 8
def omega(rho, x, m): return (2**m) * mul(rho, x).get((), F(0))
def prod_state(ps):
    r = GA.sc(1)
    for p, nn in zip(ps, n): r = mul(r, GA.add(GA.scal(p, nn), GA.scal(1-p, GA.sub(GA.sc(1), nn))))
    return r
grid = [F(0), F(1,5), F(1,3), F(1,2), F(2,3), F(4,5), F(1)]
bad = 0
for p1 in grid:
    for p2 in grid:
        rho = prod_state([p1, p2])
        Mx = [[omega(rho, comm(mul, x, y), 2) for y in evens] for x in evens]
        r = GA.rank_of_vectors(Mx)
        if r != 2*(p1 != p2) + 2*(p1 + p2 != 1): bad += 1
print("(1) blade-basis rank formula mismatches over", len(grid)**2, "states:", bad)
# a non-product even state: rho = 1/4 + t * (e1 e2) style element (mixing |00>,|11>) -> still rank <= 4
c = mul(w[0], w[1]); b = mul(v[0], w[1])
rho = GA.add(prod_state([F(1,3), F(3,5)]), GA.scal(F(1,10), GA.add(c, adj(c, sq))))
Mx = [[omega(rho, comm(mul, x, y), 2) for y in evens] for x in evens]
print("(1b) entangled even state rank:", GA.rank_of_vectors(Mx), " trace:", omega(rho, GA.sc(1), 2))

# (5) self-adjoint pairs
sa = [GA.add(x, adj(x, sq)) for x in evens]
rho = prod_state([F(3,4), F(1,4)])
print("(5) max |sigma| on self-adjoint pairs:", max(abs(omega(rho, comm(mul, x, y), 2)) for x in sa for y in sa),
      "; sigma(b, b*) =", omega(rho, comm(mul, b, adj(b, sq)), 2))

# (2) variance from scratch on 2 blocks (4 planes)
sq4, mul4, v4, w4 = setup(4)
n4 = [mul4(v4[j], w4[j]) for j in range(4)]
ps = [F(3,4), F(1,4), F(3,4), F(1,4)]
rho4 = GA.sc(1)
for p, nn in zip(ps, n4): rho4 = mul4(rho4, GA.add(GA.scal(p, nn), GA.scal(1-p, GA.sub(GA.sc(1), nn))))
om4 = lambda x: 16 * mul4(rho4, x).get((), F(0))
bk = [mul4(v4[0], w4[1]), mul4(v4[2], w4[3])]
Qk = [GA.add(x, adj(x, sq4)) for x in bk]; Rk = [GA.sub(x, adj(x, sq4)) for x in bk]
N = 2
FQ = GA.add(*[GA.sub(q, GA.sc(om4(q))) for q in Qk]); FR = GA.add(*[GA.sub(r, GA.sc(om4(r))) for r in Rk])
Cm = GA.scal(F(1, N), comm(mul4, FQ, FR))   # = [F_N(Q), F_N(R)] since F_N = N^{-1/2} * sum
sig = F(-2) * (ps[0] - ps[1])
D = GA.sub(Cm, GA.sc(sig))
var = om4(mul4(adj(D, sq4), D)) - om4(adj(D, sq4)) * om4(D)
pred1 = 4 * (ps[0]*(1-ps[0]) + ps[1]*(1-ps[1]))
print("(2) mean(D) =", om4(D), " var =", var, " predicted single-block", pred1, "/N =", pred1 / N)

# (3)
tot = F(0)
for M in (4, 6):
    p = [1 / (1 + F(2) ** (2*k - M + 1)) for k in range(M)]
    tot += sum(sum(p[:q]) - sum(p[M-q:]) for q in range(1, M))
print("(3) Fermi-Dirac total:", tot, "(check pins 331/33)")

# (4) deeper infinite-band test on a 10-mode window, lower half filled
M = 10
sqM, mulM, vM, wM = setup(M)
vac = GA.sc(1)
for j in range(M): vac = mulM(vac, mulM(wM[j], vM[j]))
sea = vac
for j in reversed(range(M // 2)): sea = mulM(vM[j], sea)
rq = {q: GA.add(*[mulM(vM[k], wM[k+q]) for k in range(M - q)]) for q in (1, 2, 3)}
rqs = {q: adj(rq[q], sqM) for q in rq}
psi = mulM(rqs[2], mulM(rqs[1], sea))
ok_nz = not GA.is_zero(psi)
lhs = GA.sub(mulM(rq[3], mulM(rqs[3], psi)), mulM(rqs[3], mulM(rq[3], psi)))
cross = GA.sub(mulM(rq[1], mulM(rqs[3], psi)), mulM(rqs[3], mulM(rq[1], psi)))
print("(4) psi nonzero:", ok_nz, " [rho3,rho3*]psi == 3 psi:", GA.eq(lhs, GA.scal(3, psi)), " [rho1,rho3*]psi == 0:", GA.is_zero(cross))
