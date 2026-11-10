"""Scratch: GA split of modes in Cl(m,m), Klein twist, reductions, eviction states. Exact."""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
from itertools import product
import GA

def setup(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    v = [GA.scal(F(1, 2), GA.add(e[k], f[k])) for k in range(m)]      # annihilator
    w = [GA.scal(F(1, 2), GA.sub(e[k], f[k])) for k in range(m)]      # creator
    g = [GA.mul(e[k], f[k], sq) for k in range(m)]                    # mode parity
    return sq, e, f, v, w, g

def prod(xs, sq):
    r = GA.sc(F(1))
    for x in xs:
        r = GA.mul(r, x, sq)
    return r

def dagger(x):
    r = GA.reverse(x)
    return {b: (c if sum(1 for i in b if i % 2 == 1) % 2 == 0 else -c) for b, c in r.items()}

def proj(x, modes):
    ok = set()
    for k in modes:
        ok |= {2 * k, 2 * k + 1}
    return {b: c for b, c in x.items() if set(b) <= ok and c != 0}

def s0(x):
    return x.get((), F(0))

def state(amps, m, sq, v, w):
    """amps: dict occupation tuple -> rational amplitude. rho = Psi Omega Psi^dagger / norm."""
    Om = prod([GA.mul(v[k], w[k], sq) for k in range(m)], sq)
    Psi = {}
    for occ, a in amps.items():
        Psi = GA.add(Psi, GA.scal(F(a), prod([w[k] for k in range(m) if occ[k]], sq)))
    rho = GA.mul(GA.mul(Psi, Om, sq), dagger(Psi), sq)
    nrm = 2 ** m * s0(rho)
    return GA.scal(1 / nrm, rho)

def moments(rho, modes, m, sq, nmax=4):
    a = len(modes)
    red = GA.scal(F(2 ** (m - a)), proj(rho, modes))
    out = []
    p = red
    for n in range(2, nmax + 1):
        p = GA.mul(p, red, sq)
        out.append(2 ** a * s0(p))
    return out

# ---- 1. Klein twist
for m, A in ((2, [0]), (3, [0]), (3, [0, 1])):
    sq, e, f, v, w, g = setup(m)
    B = [k for k in range(m) if k not in A]
    GamA = prod([g[k] for k in A], sq)
    assert GA.eq(GA.mul(GamA, GamA, sq), GA.sc(F(1)))
    genA = [x for k in A for x in (e[k], f[k])]
    genB = [x for k in B for x in (e[k], f[k])]
    tw = [GA.mul(y, GamA, sq) for y in genB]
    for y, t in zip(genB, tw):
        assert GA.eq(GA.mul(t, t, sq), GA.mul(y, y, sq))
        assert all(GA.commutes(t, x, sq) for x in genA)
        assert all(GA.anticommutes(y, x, sq) for x in genA)
    for i in range(len(tw)):
        for j in range(i):
            assert GA.anticommutes(tw[i], tw[j], sq)
    # blades x_S * tw_T: a bijection onto blades; in Cl(A) only if T empty; in Cl(B) iff S empty and |T| even
    seen = set()
    for S in product((0, 1), repeat=len(genA)):
        for T in product((0, 1), repeat=len(genB)):
            x = prod([genA[i] for i in range(len(genA)) if S[i]] + [tw[i] for i in range(len(genB)) if T[i]], sq)
            assert len(x) == 1
            b = next(iter(x))
            seen.add(b)
            inA = set(b) <= {i for k in A for i in (2 * k, 2 * k + 1)}
            inB = set(b) <= {i for k in B for i in (2 * k, 2 * k + 1)}
            assert inA == (sum(T) == 0)
            if sum(S) == 0:
                assert inB == (sum(T) % 2 == 0), (b, T)
            else:
                assert inB == (sum(S) == len(genA) and sum(T) % 2 == 1)
    assert len(seen) == 4 ** m
    print("twist ok", m, A)

# ---- 2. even pure states: spectra agree; non-even: differ
m = 3
sq, e, f, v, w, g = setup(m)
amps_even = {(0,0,0): 1, (1,1,0): 2, (1,0,1): -3, (0,1,1): 5}
rho = state(amps_even, m, sq, v, w)
assert GA.eq(GA.mul(rho, rho, sq), rho)
for A in ([0], [1], [0, 1]):
    B = [k for k in range(m) if k not in A]
    print("even", A, moments(rho, A, m, sq), moments(rho, B, m, sq))
amps_gen = {(0,0,0): 1, (1,0,0): 2, (0,1,0): -3, (1,1,0): 1, (0,0,1): 2, (1,1,1): 1}
rho = state(amps_gen, m, sq, v, w)
assert GA.eq(GA.mul(rho, rho, sq), rho)
for A in ([0], [1], [0, 1]):
    B = [k for k in range(m) if k not in A]
    print("generic", A, moments(rho, A, m, sq), moments(rho, B, m, sq))
m = 2
sq, e, f, v, w, g = setup(m)
rho = state({(0,0): 1, (1,0): 1, (0,1): 1, (1,1): 1}, m, sq, v, w)
print("1|1 all ones", moments(rho, [0], m, sq), moments(rho, [1], m, sq))
rho = state({(0,0): 1, (1,0): 1}, m, sq, v, w)
print("1|1 (|0>+|1>)|0>", moments(rho, [0], m, sq), moments(rho, [1], m, sq))
rho = state({(0,0): 1, (0,1): 1}, m, sq, v, w)
print("1|1 |0>(|0>+|1>)", moments(rho, [0], m, sq), moments(rho, [1], m, sq), rho)

# ---- 3. eviction pair states: modes 0,1 window; 2,3 radiation partners
m = 4
sq, e, f, v, w, g = setup(m)
def pair(kL, kR, c, s):
    # c|00> + s|11> on modes kL, kR as an even idempotent of the pair's algebra
    one = GA.sc(F(1))
    Om = GA.mul(GA.mul(v[kL], w[kL], sq), GA.mul(v[kR], w[kR], sq), sq)
    Psi = GA.add(GA.scal(c, one), GA.scal(s, GA.mul(w[kL], w[kR], sq)))
    return GA.mul(GA.mul(Psi, Om, sq), dagger(Psi), sq)
c1, s1 = F(3, 5), F(4, 5)
c2, s2 = F(5, 13), F(12, 13)
p1 = pair(0, 2, c1, s1)
p2 = pair(1, 3, c2, s2)
assert GA.eq(GA.mul(p1, p1, sq), p1) and GA.commutes(p1, p2, sq)
rho = GA.mul(p1, p2, sq)
Gam = prod(g, sq)
assert GA.commutes(rho, Gam, sq) and 16 * s0(rho) == 1
print("pair blades", {b: c for b, c in p1.items()})
print("eviction L", moments(rho, [0, 1], m, sq), "R", moments(rho, [2, 3], m, sq),
      (c1**4 + s1**4) * (c2**4 + s2**4))
redL = GA.scal(F(4), proj(rho, [0, 1]))
r1, r2 = c1**2 - s1**2, c2**2 - s2**2
target = GA.mul(GA.scal(F(1, 2), GA.add(GA.sc(F(1)), GA.scal(-r1, g[0]))), GA.scal(F(1, 2), GA.add(GA.sc(F(1)), GA.scal(-r2, g[1]))), sq)
print("window = product of marginals:", GA.eq(redL, target))
