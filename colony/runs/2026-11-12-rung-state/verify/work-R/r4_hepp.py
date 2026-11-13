"""Candidate E2: a Coleman-Hepp record on the tower (matrix route, exact).
System: one quantum on rungs S0, S1 with amplitudes 3/5, 4/5. Apparatus: N pairs (a_k, b_k), each holding
one quantum on a_k. Even coupling U = off_S0 + on_S0 * prod_k R_k, R_k the even pair rotor that moves the
quantum a_k -> b_k with amplitudes (c, s). Interference between the two system branches, as seen by ANY
observable on the system and the first k pairs, is measured by the off-diagonal block of the reduced
state on those rungs. Prediction (mine, before running): block = alpha*beta*c^(N-k) times a rank-one
partial isometry, so its squared Frobenius norm is (12/25)^2 * c^(2(N-k)); zero for c = 0 unless k = N."""
from myalg import *
half = F(1, 2)

def run(N, c, s):
    n = 2 + 2 * N
    es, fs = jw(n)
    dim = 2 ** n
    I = SM.eye(dim)
    v = [(es[j] + fs[j]).sc(half) for j in range(n)]
    w = [(es[j] - fs[j]).sc(half) for j in range(n)]
    on = [v[j] * w[j] for j in range(n)]
    off = [w[j] * v[j] for j in range(n)]
    allR = I
    for k in range(N):
        a, b = 2 + 2 * k, 3 + 2 * k
        Pi = on[a] * off[b] + off[a] * on[b]
        h = v[b] * w[a] - v[a] * w[b]
        Rk = (I - Pi) + Pi.sc(c) + h.sc(s)
        assert Rk * Rk.T() == I
        allR = allR * Rk
    U = off[0] + on[0] * allR
    assert U * U.T() == I
    vac = {dim - 1: F(1)}                       # all rungs off (bit 1 = off in this representation)
    psi = vac
    for k in range(N):
        psi = v[2 + 2 * k].apply(psi)
    psi = (v[0].sc(F(3, 5)) + v[1].sc(F(4, 5))).apply(psi)
    psi = U.apply(psi)
    assert sum(x * x for x in psi.values()) == 1
    out = []
    for k in range(N + 1):
        r = 2 + 2 * k                           # keep system + first k pairs
        tail = n - r
        red = {}
        groups = {}
        for idx, amp in psi.items():
            groups.setdefault(idx & ((1 << tail) - 1), []).append((idx >> tail, amp))
        for lst in groups.values():
            for i, ai in lst:
                for i2, a2 in lst:
                    red[(i, i2)] = red.get((i, i2), F(0)) + ai * a2
        # system bits are the two leading bits of the kept index; on = bit 0
        def sysstate(i):
            b0 = (i >> (r - 1)) & 1; b1 = (i >> (r - 2)) & 1
            return (b0, b1)
        blockA = (0, 1)    # S0 on, S1 off
        blockB = (1, 0)    # S0 off, S1 on
        fro2 = sum(val * val for (i, i2), val in red.items() if sysstate(i) == blockA and sysstate(i2) == blockB)
        pred = (F(12, 25) ** 2) * (c ** (2 * (N - k)) if N - k > 0 else F(1))
        out.append((k, fro2, pred, fro2 == pred))
    return out

for (c, s) in ((F(3, 5), F(4, 5)), (F(0), F(1))):
    for N in (1, 2, 3):
        print(f"c = {c}, N = {N}:", [(f"k={k}", str(x), "pred ok" if okk else f"PRED {p}") for k, x, p, okk in run(N, c, s)])
