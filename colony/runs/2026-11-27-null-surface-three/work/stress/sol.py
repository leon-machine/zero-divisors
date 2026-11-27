"""generic first-order vacuum solutions: superposed null polynomial waves + displacement + rotation gauge."""
from engine import *

E = [GA.gen(i) for i in range(D)]
REC = [GA.scal(ETA[i], E[i]) for i in range(D)]

WAVES = [((5, 3, 4, 0), (0, F(4, 5), F(-3, 5), 0), (0, 0, 0, 1)),
         ((3, 2, 1, 2), (0, F(2, 3), F(-2, 3), F(-1, 3)), (0, F(1, 3), F(2, 3), F(-2, 3))),
         ((9, 1, 4, 8), (0, F(8, 9), F(-4, 9), F(1, 9)), (0, F(4, 9), F(7, 9), F(-4, 9)))]


def up(v):
    return [F(x) for x in v]


def low(v):
    return [F(ETA[i]) * F(v[i]) for i in range(D)]


def outer_map(u, v):
    """matrix of a -> (a.u) v: M[mu][a] = v^mu u_a."""
    ul = low(u)
    return [[F(v[m]) * ul[a] for a in range(D)] for m in range(D)]


def const_mat(M):
    return [[gtg.Jet.const(M[m][a], D) for a in range(D)] for m in range(D)]


def wave_h(X, coeffs):
    """h = sum_j f_j(p_j.x) (c_j n_plus + d_j n_cross), f_j(u) = a_j u^2 + b_j u^3: symmetric, E[h] = 0."""
    h = [[jz() for _ in range(D)] for _ in range(D)]
    for (p, m1, m2), (a, b, c, d) in zip(WAVES, coeffs):
        pl = low(p)
        phi = sum((X[i] * pl[i] for i in range(D)), jz())
        f = phi * phi * a + phi * phi * phi * b
        npl = madd(const_mat(outer_map(m1, m1)), const_mat(outer_map(m2, m2)), -1)
        ncr = madd(const_mat(outer_map(m1, m2)), const_mat(outer_map(m2, m1)))
        T = madd(mscal(c, npl), mscal(d, ncr))
        h = madd(h, [[T[m][k] * f for k in range(D)] for m in range(D)])
    return h


def grad_map(xi):
    """xi_(a) = (a.grad) xi for a vector field xi (list of 4 jets, upper components): M[mu][a] = d_a xi^mu."""
    return [[xi[m].d(a) for a in range(D)] for m in range(D)]


def biv_map(B):
    """beta(a) = a.B for a bivector field B (dict blade -> jet): M[mu][a] = (e_a . B)^mu."""
    out = [[jz() for _ in range(D)] for _ in range(D)]
    for a in range(D):
        img = gtg.inner_vb(E[a], B, S)
        for (m,), c in img.items():
            out[m][a] = c
    return out


def xi_field(X4, k):
    t, x, y, z = X4
    polys = [t * x * F(1, 3) + y * y * z * F(1, 5) - z * z * z * z * F(1, 7) + t * t * y * F(2, 9),
             x * y * F(-1, 4) + t * z * z * F(1, 6) + x * x * x * t * F(1, 8) + y * z * F(1, 5),
             z * t * F(2, 5) - x * x * y * F(1, 7) + t * t * t * z * F(1, 9) + x * x * F(1, 11),
             y * y * F(1, 6) + t * x * z * F(-1, 5) + y * y * x * x * F(1, 10) + t * z * F(3, 7)]
    return [polys[(i + k) % 4] * F(k + 1, 2) for i in range(D)]


def biv_field(X, k):
    t, x, y, z = X
    co = [t * F(1, 4) + x * y * F(1, 6), z * F(-1, 5) + t * t * F(1, 7), x * F(1, 3) - y * z * t * F(1, 8),
          y * F(2, 7) + x * x * F(1, 9), t * z * F(1, 5) - x * F(1, 6), z * z * F(1, 4) + y * F(1, 10) + x * y * z * F(1, 3)]
    bl = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    return {bl[i]: co[(i + k) % 6] * F(k + 2, 3) for i in range(6)}


def solution(x0, coeffs, kxi=0, kb=0, gauge=True, rot=True, order=3):
    """H1 = -1/2 h + xi_ + beta: G1[H1] = 0, not symmetric."""
    X = labels(x0, order)
    X4 = labels(x0, order + 1)
    H1 = mscal(F(-1, 2), wave_h(X, coeffs))
    if gauge:
        H1 = madd(H1, grad_map(xi_field(X4, kxi)))
    if rot:
        H1 = madd(H1, biv_map(biv_field(X, kb)))
    return H1


COEFFS = [((F(1, 2), F(1, 3), 2, -1), (F(-1, 3), F(1, 4), 1, 3), (F(1, 5), F(-1, 6), -2, 1)),
          ((F(2, 3), F(-1, 5), 1, 2), (F(1, 4), F(1, 7), -3, 1), (F(-1, 2), F(1, 9), 2, 5))]
X0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))

if __name__ == "__main__":
    import time
    for i, cf in enumerate(COEFFS):
        t0 = time.time()
        H1 = solution(X0, cf, i, i)
        G1, G2, fld = einstein_orders(H1)
        print("G1 = 0:", all(not G1[k][c] for k in range(D) for c in range(D)),
              "torsion:", fld.torsion_free(),
              "H1 symmetric?", all(ETA[k] * H1[k][c] == ETA[c] * H1[c][k] for k in range(D) for c in range(D)))
        print("G2 symmetric:", all(ETA[k] * G2[k][c] == ETA[c] * G2[c][k] for k in range(D) for c in range(D)),
              "nonzero entries:", sum(1 for k in range(D) for c in range(D) if G2[k][c].v != 0))
        print("div G2 (K1):", [d.v for d in flat_div(G2)], time.time() - t0)
        print("G2 row0:", [str(G2[0][c].v) for c in range(D)])
