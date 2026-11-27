from engine import *
from sol import *

NV = (1, 0, 0, 1); NB = (1, 0, 0, -1); M1 = (0, 1, 0, 0); M2 = (0, 0, 1, 0)

def vdot4(u, v):
    return sum(F(ETA[i]) * F(u[i]) * F(v[i]) for i in range(D))

def lc_waves():
    """null momenta with n.p != 0 and polarisation vectors m_i' = m_i - (m_i.n)/(p.n) p, orthogonal to p and n."""
    out = []
    for p, m1, m2 in WAVES:
        pn = vdot4(p, NV)
        ms = []
        for m in (m1, m2):
            c = -vdot4(m, NV) / pn
            ms.append(tuple(F(m[i]) + c * F(p[i]) for i in range(D)))
        out.append((p, ms[0], ms[1]))
    out.append(((1, 0, 0, -1), M1, M2))
    return out

def lc_h(X, coeffs, nu_k=0):
    h = [[jz() for _ in range(D)] for _ in range(D)]
    for (p, m1, m2), (a, b, c, d) in zip(lc_waves(), coeffs):
        pl = low(p)
        phi = sum((X[i] * pl[i] for i in range(D)), jz())
        f = phi * phi * a + phi * phi * phi * b + phi * F(1, 3)
        npl = madd(const_mat(outer_map(m1, m1)), const_mat(outer_map(m2, m2)), -1)
        ncr = madd(const_mat(outer_map(m1, m2)), const_mat(outer_map(m2, m1)))
        T = madd(mscal(c, npl), mscal(d, ncr))
        h = madd(h, [[T[m][k] * f for k in range(D)] for m in range(D)])
    return h

def residual(X4, k):
    """xi = 1/2 nu nbar - 1/2 (nbar.x) grad nu, nu a polynomial of the transverse labels: keeps h(n) = 0, theta != 0."""
    t, x, y, z = X4
    nu = x * x * F(k + 1, 3) + x * y * F(1, 4) - y * y * y * F(1, 5) + x * x * y * y * F(1, 7)
    nbx = t + z                                     # nbar.x = t + z (nbar = e0 - e3, x.e3 = -z)
    gradnu = [jz(), -nu.d(1), -nu.d(2), jz()]       # grad^k = eta_k d_k
    xi = [nu * F(1, 2) * NB[i] - nbx * gradnu[i] * F(1, 2) for i in range(D)]
    xb = grad_map(xi)
    return madd(xb, transpose(xb))                  # h = xi_ + xi_^T

def pairm(A, B):
    """<A, B> = sum_a A(e_a).B(e^a) = sum eta_k eta_a A[k][a] B[k][a]"""
    return sum((A[k][a] * B[k][a] * (ETA[k] * ETA[a]) for k in range(D) for a in range(D)), jz())

def dn(f):
    return f.d(0) + f.d(3)                          # n.grad = d_t + d_z  (n = e0 + e3: n.grad = n^mu d_mu)

def nn(M):
    """n . M(n): n_k M[k][a] n^a"""
    nl = low(NV)
    return sum((M[k][a] * (nl[k] * NV[a]) for k in range(D) for a in range(D)), jz())

EPSP = madd(const_mat(outer_map(M1, M1)), const_mat(outer_map(M2, M2)), -1)
EPSX = madd(const_mat(outer_map(M1, M2)), const_mat(outer_map(M2, M1)))

LC = [((F(1, 2), F(1, 3), 2, -1), (F(-1, 3), F(1, 4), 1, 3), (F(1, 5), F(-1, 6), -2, 1), (F(1, 4), F(1, 5), 1, -2)),
      ((F(2, 3), F(-1, 5), 1, 2), (F(1, 4), F(1, 7), -3, 1), (F(-1, 2), F(1, 9), 2, 5), (F(-1, 3), F(1, 2), 3, 1))]

if __name__ == "__main__":
    X = labels(X0, 3); X4 = labels(X0, 4)
    for i, cf in enumerate(LC):
        h = madd(lc_h(X, cf), residual(X4, i))
        H1 = mscal(F(-1, 2), h)
        # gauge and solution
        hn = [sum((h[k][a] * NV[a] for a in range(D)), jz()) for k in range(D)]
        print("h(n) = 0:", all(not x for x in hn), "E[h] = 0:", all(not x for row in first_order_einstein(h) for x in row))
        hp, hx, tau = pairm(h, EPSP) * F(1, 2), pairm(h, EPSX) * F(1, 2), mtrace(h)
        sig2 = (dn(hp) * dn(hp) + dn(hx) * dn(hx)) * F(1, 2)
        theta = dn(tau) * F(1, 2)
        hh = pairm(h, h)
        d2 = dn(dn(hh))
        print("  dn theta:", dn(theta).v if theta.order >= 1 else None, "theta", theta.v, "sig2", sig2.v, "d2<h,h>", d2.v)
        H1sq = mmul(H1, H1)
        for name, c2, coef in (("hb = 1 + eps H1", None, F(1, 8)), ("hb^-1 = 1 + eps s", F(1), F(-1, 8)), ("exp", F(1, 2), F(0))):
            H2 = None if c2 is None else mscal(c2, H1sq)
            G1, G2, _ = einstein_orders(H1, H2)
            got = nn(G2).v
            want = sig2.v + theta.v * theta.v * F(1, 2) + coef * d2.v
            print("  ", name, got == want, got, "G1=0", all(not x for row in G1 for x in row))
