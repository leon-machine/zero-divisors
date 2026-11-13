import sys, random
sys.path.insert(0, '.')
from fock import *
random.seed(20261112)

def model(N, c, s, coupled):
    """Branch vectors A (system on rung 0) and B (system on rung 1) with the pairs in `coupled` rotated in A."""
    def pair(j): return 2 + 2 * j, 3 + 2 * j
    vac = {(): F(1)}
    A = ap_v(0, vac); B = ap_v(1, vac)
    for j in range(N):
        a, b = pair(j)
        B = ap_v(a, B)
        if j in coupled:
            # R_j v_a |.> = c v_a - s v_b  (h v_a = -v_b on the pair)
            A = vadd(vscal(c, ap_v(a, A)), vscal(-s, ap_v(b, A)))
        else:
            A = ap_v(a, A)
    return A, B

def interference(x, A, B, al, be):
    return al * be * (ip(A, ap(x, B)) + ip(B, ap(x, A)))

def rand_el(rungs, parity, nterms=4, maxlen=4):
    el = {}
    for _ in range(nterms):
        L = random.randint(1, maxlen)
        while True:
            wd = tuple((random.choice('vw'), random.choice(rungs)) for _ in range(L))
            if len(wd) % 2 == parity: break
            L = L + 1 if L < maxlen else L - 1
        el[wd] = el.get(wd, F(0)) + random.randint(-3, 3)
    return {k: c for k, c in el.items() if c != 0}

al, be = F(3, 5), F(4, 5)
for (c, s) in ((F(3, 5), F(4, 5)), (F(0), F(1)), (F(5, 13), F(12, 13))):
    N = 3
    bad = 0; tested = 0; nonzero = 0
    A_N, B_N = model(N, c, s, set(range(N)))
    for mask in range(8):
        K = {j for j in range(N) if (mask >> j) & 1}
        rungs = [0, 1] + [r for j in sorted(K) for r in (2 + 2 * j, 3 + 2 * j)]
        A_K, B_K = model(N, c, s, K)
        for parity in (0, 1):
            for _ in range(150):
                x = rand_el(rungs, parity)
                if not x: continue
                lhs = interference(x, A_N, B_N, al, be)
                rhs = c ** (N - len(K)) * interference(x, A_K, B_K, al, be)
                tested += 1
                if rhs != 0: nonzero += 1
                if lhs != rhs: bad += 1
    print("c =", c, "tested", tested, "nonzero rhs", nonzero, "failures", bad)
