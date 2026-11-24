"""Sea values of commutators of composite modes on one generator window (exact).
Channels: (helicity sign, flavour). Levels k in {-N..N-1}; sea = k<0 filled in every channel."""
import sys
from fock import *
from math import comb

def setup(N, channels):
    levels = list(range(-N, N))
    idx = {(k, c): i for i, (k, c) in enumerate((k, c) for k in levels for c in channels)}
    sea = 0
    for (k, c), i in idx.items():
        if k < 0:
            sea |= 1 << i
    return levels, idx, {sea: 1}

def rho(q, ca, cb, levels, idx):
    """rho_q(E_{ca cb}) = sum_k a*_{k,ca} a_{k+q,cb}."""
    return [(1, [('c', idx[(k, ca)]), ('a', idx[(k + q, cb)])]) for k in levels if (k + q) in levels]

def mul(A, B):
    return [(x * y, wa + wb) for x, wa in A for y, wb in B]

# --- two flavours, weight two, helicity two: X_q = sum_{a+b=q} rho_a(E^1_{+-}) rho_b(E^2_{+-})
ch2 = [('+', 1), ('-', 1), ('+', 2), ('-', 2)]
print("two flavours: q, sea value of [X_q, X_q*], C(q+1,3)")
for q in range(1, 6):
    N = q
    levels, idx, sea = setup(N, ch2)
    X = []
    for a in range(1, q):
        X += mul(rho(a, ('+', 1), ('-', 1), levels, idx), rho(q - a, ('+', 2), ('-', 2), levels, idx))
    Xd = dagger(X) if X else []
    v = apply(Xd, sea) if X else {}
    lower = apply(X, sea) if X else {}
    print(q, ip(v, v) - ip(lower, lower), comb(q + 1, 3), "X annihilates sea:", not lower)

# --- one species, weight four: V_q = sum (k2-k1)(l2-l1) a*_{k1+} a*_{k2+} a_{l2-} a_{l1-}, l1+l2-k1-k2 = q
ch1 = ['+', '-']
print("one species: q, sea value of [V_q, V_q*], C(q+3,7)")
for q in range(1, 8):
    N = max(2, q - 2)
    levels, idx, sea = setup(N, ch1)
    V = []
    for k1 in levels:
        for k2 in levels:
            if k1 < k2:
                for l1 in levels:
                    for l2 in levels:
                        if l1 < l2 and l1 + l2 - k1 - k2 == q:
                            V.append(((k2 - k1) * (l2 - l1), [('c', idx[(k1, '+')]), ('c', idx[(k2, '+')]),
                                                               ('a', idx[(l2, '-')]), ('a', idx[(l1, '-')])]))
    v = apply(dagger(V), sea)
    lower = apply(V, sea)
    print(q, ip(v, v) - ip(lower, lower), comb(q + 3, 7), "V annihilates sea:", not lower, "N", N)
