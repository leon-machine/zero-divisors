"""Lead 4: duality on the two free directions; symmetry of the Einstein map for the pairing; kernel condition."""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA
from GA import mul, scal, sub, add
from null_kernel import ST, madd, mscal, rank
from null_kernel2 import tt_maps, conserved_basis, bar, tt_project, gauge, Bform

st = ST(4)
I4 = {(0, 1, 2, 3): F(1)}
print("I4^2 =", mul(I4, I4, st.S))
for kc, trans in [((1, 0, 0, 1), [(0, 1, 0, 0), (0, 0, 1, 0)]),
                  ((5, 3, 0, 4), [(0, 0, 1, 0), (0, F(4, 5), 0, F(-3, 5))]),
                  ((5, -3, 0, -4), [(0, 0, 1, 0), (0, F(4, 5), 0, F(-3, 5))])]:
    k = st.vec(kc)
    ncross, nplus = tt_maps(trans)
    sig = set()
    ok = True
    for a in range(4):
        for b in range(a + 1, 4):
            B = st.wedge(st.e[a], st.e[b])
            Rp, Rc = st.riem(nplus, k, B), st.riem(ncross, k, B)
            left = mul(I4, Rp, st.S)
            if GA.eq(left, Rc):
                sig.add(1)
            elif GA.eq(left, GA.neg(Rc)):
                sig.add(-1)
            else:
                ok = False
            # and I4 R[cross] = -sigma R[plus]
            # duality on the argument
            IB = mul(I4, B, st.S)
            ok = ok and GA.eq(st.riem(nplus, k, IB), left)
    nonzero = any(not GA.is_zero(st.riem(nplus, k, st.wedge(st.e[a], st.e[b]))) for a in range(4) for b in range(a + 1, 4))
    print(f"k={kc}: I4 R[n+] = sigma R[nx] with sigma in {sig}; R[n+](I4 B) = I4 R[n+](B) and consistent: {ok}; curvature nonzero: {nonzero}")

# symmetry of the Einstein map for the pairing, at several momenta
basis = st.sym_basis()
for kc in [(2, 0, 0, 0), (3, 1, 0, 2), (0, 1, 1, 3), (1, 0, 0, 1), (5, 3, 0, 4)]:
    k = st.vec(kc)
    G = [st.einstein(H, k) for H in basis]
    sym = all(st.pair(basis[i], G[j]) == st.pair(basis[j], G[i]) for i in range(10) for j in range(10))
    print(f"k={kc}: <h', G[h]> symmetric: {sym}")

# kernel condition at null k: h(k) = 1/2 tr(h) k
for kc in [(1, 0, 0, 1), (5, 3, 0, 4)]:
    k = st.vec(kc)
    rows = []
    for H in basis:
        v = sub(st.apply(H, k), scal(F(1, 2) * st.trace(H), k))
        rows.append([st.dot(v, st.rec[i]) for i in range(4)])
    print(f"k={kc}: rank of h -> h(k) - 1/2 tr(h) k: {rank(rows)}")
    G = [st.einstein(H, k) for H in basis]
    # G[h] = 0 iff h(k) = tr(h) k / 2: compare kernels by rank of stacked rows
    stacked = [rows[i] + st.flat(G[i]) for i in range(10)]
    print("   rank Einstein:", rank([st.flat(g) for g in G]), " rank stacked:", rank(stacked))
