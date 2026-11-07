"""(4) redone: the failure at M = 10 is an undersized window (psi = rho_2* rho_1* sea reaches modes 2 and 7, inside the
depth-3 edges). Confirm (a) at M = 10 the commutator equals the edge operator B_3 - T_3 on psi (so the identity holds and psi
is simply not edge-clean), and (b) at M = 12 (edges clean at depth 3) [rho_3, rho_3*] psi = 3 psi, [rho_1, rho_3*] psi = 0,
[rho_2, rho_3*] psi = 0, [rho_1, rho_2] psi = 0."""
import sys
from fractions import Fraction as F
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA
from ownlib import setup, adj
for M in (10, 12):
    sq, mul, v, w = setup(M)
    n = [mul(v[j], w[j]) for j in range(M)]
    vac = GA.sc(1)
    for j in range(M): vac = mul(vac, mul(w[j], v[j]))
    sea = vac
    for j in reversed(range(M // 2)): sea = mul(v[j], sea)
    rq = {q: GA.add(*[mul(v[k], w[k+q]) for k in range(M - q)]) for q in (1, 2, 3)}
    rqs = {q: adj(rq[q], sq) for q in rq}
    psi = mul(rqs[2], mul(rqs[1], sea))
    C = lambda a, x, y: GA.sub(mul(x, mul(y, a)), mul(y, mul(x, a)))
    c33 = C(psi, rq[3], rqs[3])
    if M == 10:
        edge = GA.sub(GA.add(*[mul(n[k], psi) for k in range(3)]), GA.add(*[mul(n[k], psi) for k in range(M - 3, M)]))
        print("M=10: [rho3,rho3*]psi == (B3 - T3)psi:", GA.eq(c33, edge), "; == 3 psi:", GA.eq(c33, GA.scal(3, psi)))
    else:
        print("M=12: psi nonzero", not GA.is_zero(psi), "; [rho3,rho3*]psi == 3psi:", GA.eq(c33, GA.scal(3, psi)),
              "; [rho1,rho3*]psi == 0:", GA.is_zero(C(psi, rq[1], rqs[3])),
              "; [rho2,rho3*]psi == 0:", GA.is_zero(C(psi, rq[2], rqs[3])),
              "; [rho1,rho2]psi == 0:", GA.is_zero(C(psi, rq[1], rq[2])))
