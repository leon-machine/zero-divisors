"""Is the commutator of the weight-two helicity-two composite a number on the edge-clean vectors? (exact)"""
from fock import *
from c2_sea_values import setup, rho, mul, ch2
from math import comb

def comm_exp(X, st):
    Xd = dagger(X)
    a = apply(Xd, st); b = apply(X, st)
    return F(ip(a, a) - ip(b, b), ip(st, st))

for q in (2, 3):
    N = q + 2
    levels, idx, sea = setup(N, ch2)
    X = []
    for a in range(1, q):
        X += mul(rho(a, ('+', 1), ('-', 1), levels, idx), rho(q - a, ('+', 2), ('-', 2), levels, idx))
    tests = {
        'sea': sea,
        'density pair, flavour 1, channel +': apply(dagger(rho(1, ('+', 1), ('+', 1), levels, idx)), sea),
        'helicity-one pair, flavour 2 (B_1* sea)': apply(dagger(rho(1, ('+', 2), ('-', 2), levels, idx)), sea),
        'helicity-one pair, flavour 2 (B_2* sea)': apply(dagger(rho(2, ('+', 2), ('-', 2), levels, idx)), sea),
        'opposite helicity pair, flavour 2': apply(dagger(rho(1, ('-', 2), ('+', 2), levels, idx)), sea),
    }
    # control: the total density mode of both flavours, a normal bilinear
    R = []
    for c in ch2:
        R += rho(q, c, c, levels, idx)
    print("q =", q, " C(q+1,3) =", comb(q + 1, 3))
    for name, st in tests.items():
        print("   %-45s <[X,X*]> = %s    control <[rho_q,rho_q*]> = %s" % (name, comm_exp(X, st), comm_exp(R, st)))
    # boson defect on the sea: |X*^2 sea|^2 against 2 |X* sea|^4
    Xd = dagger(X)
    v1 = apply(Xd, sea); v2 = apply(Xd, v1)
    print("   |X* sea|^2 =", ip(v1, v1), " |X*^2 sea|^2 =", ip(v2, v2), " canonical value 2|X* sea|^4 =", 2 * ip(v1, v1) ** 2)
