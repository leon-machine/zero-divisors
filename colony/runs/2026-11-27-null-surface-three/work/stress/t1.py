import time, sys
from engine import *

x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))

def generic_H(X, seed, deg=3):
    """generic non-symmetric polynomial matrix"""
    t, x, y, z = X
    mons = [t, x, y, z, t*x, y*z, t*t, x*y, z*z, t*z, x*x*y, t*y*z, z*z*z, t*t*x, x*y*z, y*y*y]
    out = [[None]*D for _ in range(D)]
    k = seed
    for m in range(D):
        for a in range(D):
            acc = gtg.Jet.const(0, D)
            for j in range(4):
                k = (k * 7 + 3) % 101
                mon = mons[(k + m*5 + a*3 + j*4) % len(mons)]
                acc = acc + mon * F((k % 9) - 4, (k % 5) + 2)
            out[m][a] = acc
    return out

if __name__ == "__main__":
    t0 = time.time()
    X = labels(x0, 3)
    H1 = generic_H(X, 5)
    G1, G2, fld = einstein_orders(H1)
    print("time", time.time() - t0)
    print("torsion free:", fld.torsion_free())
    G1s = G1_of(H1)
    print("G1 == stored E[-(H1+H1^T)]:", all(G1[k][c] == G1s[k][c] for k in range(D) for c in range(D)))
    print("G1 nonzero:", sum(1 for k in range(D) for c in range(D) if G1[k][c].v != 0))
    print("G1 jets order", G1[0][0].order)
    # symmetry of G2 (as a map for the flat product): eta_k G2[k][c] symmetric
    print("G2 symmetric:", all(ETA[k]*G2[k][c] == ETA[c]*G2[c][k] for k in range(D) for c in range(D)))
    print("G2 nonzero:", sum(1 for k in range(D) for c in range(D) if G2[k][c].v != 0))
    print("div G1:", [d.v for d in flat_div(G1)])
    print("div G2:", [d.v for d in flat_div(G2)])
