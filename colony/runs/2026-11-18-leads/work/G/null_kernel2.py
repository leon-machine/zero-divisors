"""Leads 4 and 5, second part: residue on the null cone, the constraint split, the bilinear's signature, channels."""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA
from null_kernel import ST, madd, mscal, rank

st = ST(4)
ID = st.idmat()


def conserved_basis(kc):
    """basis of symmetric maps T with T(k) = 0, by exact kernel computation."""
    basis = st.sym_basis()
    k = st.vec(kc)
    rows = []
    for H in basis:
        img = st.apply(H, k)
        rows.append([st.dot(img, st.rec[i]) for i in range(4)])
    # kernel of the 10 x 4 system (combinations c with sum c_i rows_i = 0)
    A = [[rows[i][j] for i in range(10)] for j in range(4)]      # 4 x 10
    ker = GA.field_kernel(A) if hasattr(GA, 'field_kernel') else None
    out = []
    for c in ker:
        T = [[F(0)] * 4 for _ in range(4)]
        for ci, H in zip(c, basis):
            T = madd(T, mscal(F(ci), H))
        out.append(T)
    return out


def tt_maps(trans):
    return [st.outer(trans[0], trans[1]),
            madd(mscal(F(1, 2), st.outer(trans[0], trans[0])), mscal(F(1, 2), st.outer(trans[1], trans[1])), -1)]


def tt_project(T, tt):
    out = [[F(0)] * 4 for _ in range(4)]
    for n in tt:
        out = madd(out, mscal(st.pair(T, n) / st.pair(n, n), n))
    return out


def bar(T):
    return madd(T, mscal(F(1, 2) * st.trace(T), ID), -1)


def gauge(kc):
    return [st.outer(kc, [1 if i == j else 0 for i in range(4)]) for j in range(4)]


def Bform(T1, T2):
    return st.pair(T1, T2) - F(1, 2) * st.trace(T1) * st.trace(T2)


print("== (K4c) at null k, for every conserved source: T - 1/2 id tr T - P_tt T is a displacement")
for kc, trans in [((1, 0, 0, 1), [(0, 1, 0, 0), (0, 0, 1, 0)]),
                  ((5, 3, 0, 4), [(0, 0, 1, 0), (0, F(4, 5), 0, F(-3, 5))]),
                  ((-5, 3, 0, 4), [(0, 0, 1, 0), (0, F(4, 5), 0, F(-3, 5))])]:
    cb = conserved_basis(kc)
    tt = tt_maps(trans)
    g = gauge(kc)
    rg = rank([st.flat(M) for M in g])
    ok = True
    for T in cb:
        x = madd(bar(T), tt_project(T, tt), -1)
        ok = ok and rank([st.flat(M) for M in g + [x]]) == rg
    # curvature equality on the six bivectors
    k = st.vec(kc)
    okR = True
    for T in cb:
        x = madd(bar(T), tt_project(T, tt), -1)
        for a in range(4):
            for b in range(a + 1, 4):
                okR = okR and GA.is_zero(st.riem(x, k, st.wedge(st.e[a], st.e[b])))
    # B on conserved sources at null k: Gram matrix, signature, equals the tt norm
    gram = [[Bform(a, b) for b in cb] for a in cb]
    sigB = GA.congruence_signature(gram)
    okB = all(Bform(a, b) == st.pair(tt_project(a, tt), tt_project(b, tt)) for a in cb for b in cb)
    okB2 = all(Bform(a, a) == sum(st.pair(a, n) ** 2 / st.pair(n, n) for n in tt) for a in cb)
    print(f"  k={kc}: conserved dim {len(cb)}; all displacement: {ok}; curvature of remainder zero: {okR}; "
          f"signature of B on conserved sources: {sigB}; B = <P_tt T1, P_tt T2>: {okB}; tt norms {[st.pair(n, n) for n in tt]}; sum of squares form {okB2}")

print("== signature of B on conserved sources at non-null k")
for kc in [(2, 0, 0, 0), (3, 1, 0, 2), (1, 2, 0, 0), (0, 1, 1, 3)]:
    cb = conserved_basis(kc)
    gram = [[Bform(a, b) for b in cb] for a in cb]
    print(f"  k={kc} Q={st.Q(kc)}: signature {GA.congruence_signature(gram)}")

print("== (K4c) constraint split: components of the Einstein map along e_0 against the frequency")
basis = st.sym_basis()
kap = (0, 3, 0, 4)
maxdeg_time, maxdeg_space = 0, 0


def poly_degree(vals):
    """degree of the polynomial through vals at omega = 0,1,2,..., by finite differences."""
    d = list(vals)
    deg = -1
    n = 0
    while d:
        if any(x != 0 for x in d):
            deg = n
        d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
        n += 1
    return deg


degs = {}
for H in basis:
    Es = [st.einstein(H, st.vec((w,) + kap[1:])) for w in range(0, 5)]
    for m in range(4):
        for n in range(m, 4):
            dg = poly_degree([E[m][n] for E in Es])
            key = '00' if (m, n) == (0, 0) else ('0i' if m == 0 else 'ij')
            degs[key] = max(degs.get(key, -1), dg)
print("  highest power of the frequency, over the ten symmetric maps, at kappa = (3, 0, 4):", degs)

print("== (K5) channels of the static coupling and of pair sources")


def theta(kc):
    q = st.Q(kc)
    kk = mscal(F(1, 2), st.outer(kc, kc))
    return madd(ID, mscal(F(1) / q, kk), -1)


def channels(T1, T2, kc):
    th = theta(kc)
    t1, t2 = st.trace(T1), st.trace(T2)
    tf1 = madd(T1, mscal(t1 / 3, th), -1)
    tf2 = madd(T2, mscal(t2 / 3, th), -1)
    return st.pair(tf1, tf2), -t1 * t2 / 6, Bform(T1, T2), F(1, 2) * t1 * t2


kc = (0, 1, 2, 2)
e0 = (1, 0, 0, 0)
T1 = mscal(F(7, 2), st.outer(e0, e0))      # m (a.e0) e0 with m = 7
T2 = mscal(F(3, 2), st.outer(e0, e0))      # m = 3
print("  static bodies m = 7, 3 at k =", kc, ": (trace-free part, trace part, B, trace-only B_N) =", channels(T1, T2, kc),
      " m1 m2 =", 21)


def scalar_pair(p1, p2, xi=F(0)):
    kc = [a + b for a, b in zip(p1, p2)]
    s = st.Q(kc)
    A = st.outer(p1, p2)
    T = madd(mscal(st.mdot(p1, p2), ID), A, -1)
    imp = madd(mscal(F(1, 2), st.outer(kc, kc)), mscal(s, ID), -1)
    return madd(T, mscal(2 * xi, imp)), kc


# centre-of-mass configuration with rational angle
p1, p2 = (5, 0, 0, 5), (5, 0, 0, -5)
p3, p4 = (5, 3, 0, 4), (5, -3, 0, -4)
Ta, kc = scalar_pair(p1, p2)
Tb, _ = scalar_pair(p3, p4)
s = st.Q(kc)
t = st.Q([a - b for a, b in zip(p1, p3)])
u = st.Q([a - b for a, b in zip(p1, p4)])
print("  scalar pair to scalar pair, xi = 0: s, t, u =", s, t, u, "; conserved:", GA.is_zero(st.apply(Ta, st.vec(kc))),
      "; channels:", channels(Ta, Tb, kc), "; -t u =", -t * u, "; s^2/2 =", s * s / 2)
Tc, _ = scalar_pair(p1, p2, F(1, 6))
print("  conformally coupled scalar pair: trace =", st.trace(Tc), "; channels with a minimal pair:", channels(Tc, Tb, kc))
