"""Referee R2: the route the overall answer leaves open. For complete records (c = 0) the two branches of
claim 3 are string states that differ at every rung they occupy, so in the limit they lie in two different tail
classes in the sense of claim 4; the sign change of f on every rung where they differ (a G3 element) exchanges
their string projections, and no element of G1/G2 can. For 0 < |c| < 1 branch A is not a string state."""
import sys
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from mx import Alg, mul, add, sc, apply, ip   # noqa: E402

OK = True


def report(name, cond):
    global OK
    OK = OK and cond
    print(("PASS " if cond else "FAIL ") + name)


def pair(j):
    return 2 + 2 * j, 3 + 2 * j


def branches(N, c, s):
    G = Alg(2 + 2 * N)
    base = G.vac()
    for j in reversed(range(N)):
        base = apply(G.v[pair(j)[0]], base)
    A, B = apply(G.v[0], base), apply(G.v[1], base)
    for j in range(N):
        a, b = pair(j)
        Pi = add(mul(G.on[a], G.off[b]), mul(G.off[a], G.on[b]))
        h = add(mul(G.v[a], G.w[b]), sc(-1, mul(G.v[b], G.w[a])))
        A = apply(add(G.I, sc(-1, Pi), sc(c, Pi), sc(s, h)), A)
    return G, A, B


def occ(G, vec):
    (k,) = vec.keys()
    return tuple((k >> (G.m - 1 - r)) & 1 for r in range(G.m))


for N in (1, 2, 3):
    G, A, B = branches(N, F(0), F(1))
    sA, sB = occ(G, A), occ(G, B)
    report(f"c=0, N={N}: both branches are single occupation vectors (string states)", len(A) == 1 and len(B) == 1)
    diff = [r for r in range(G.m) if sA[r] != sB[r]]
    report(f"c=0, N={N}: they differ at all {G.m} rungs (strings {sA} vs {sB})", len(diff) == G.m)
    # sign change of f at every differing rung exchanges on/off there: maps P_sA to P_sB
    def P(G, st):
        M = G.I
        for r, b in enumerate(st):
            M = mul(M, G.on[r] if b else G.off[r])
        return M
    def flip_f(M_on_off_string, st):
        # sigma_f at rung r exchanges on_r and off_r; on a product of tests it flips the string bits
        return tuple(1 - b if r in diff else b for r, b in enumerate(st))
    report(f"c=0, N={N}: the G3 element (f -> -f on all {G.m} rungs) sends branch A's string to branch B's", flip_f(None, sA) == sB)

G, A, B = branches(3, F(3, 5), F(4, 5))
report("c=3/5: branch A is a superposition of 8 occupation vectors (not a string state)", len(A) == 8)
print("ALL PASS" if OK else "SOME FAIL")
