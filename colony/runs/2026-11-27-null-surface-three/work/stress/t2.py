import time, sys
from engine import *
from t1 import generic_H, x0

E = [GA.gen(i) for i in range(D)]
REC = [GA.scal(ETA[i], E[i]) for i in range(D)]

def om1_of(fld):
    return [{b: part(c, 1) for b, c in fld.om[k].items() if part(c, 1)} for k in range(D)]

def colvec(M, c):
    return {(k,): M[k][c] for k in range(D) if M[k][c]}

def rhs_div(H1, G1, om1):
    """-[ grad-dot . H1(G1-dot(C)) + G1(C).w + C.(Omega1(d_a).G1(a)) ] at the point, for C = e_c"""
    om1v = [gtg.m_val(o) for o in om1]
    w = {}
    for a in range(D):
        w = gtg.m_add(w, gtg.inner_vb(REC[a], om1v[a], S))
    G1v = mval(G1)
    H1v = mval(H1)
    out = []
    # sum_a Omega1(gamma_a) . G1(gamma^a)
    acc = {}
    for a in range(D):
        ga = {(k,): ETA[a] * G1v[k][a] for k in range(D) if G1v[k][a]}
        acc = gtg.m_add(acc, gtg.bdot(om1v[a], ga, S))
    for c in range(D):
        A = sum(G1[j][c].d(mu).v * H1v[mu][j] for mu in range(D) for j in range(D))
        gc = {(k,): G1v[k][c] for k in range(D) if G1v[k][c]}
        B = gtg.vdot(gc, w, S)
        Cc = gtg.vdot(E[c], acc, S)
        out.append(-(A + B + Cc))
    return out

if __name__ == "__main__":
    X = labels(x0, 3)
    for seed in (5, 11):
        H1 = generic_H(X, seed)
        G1, G2, fld = einstein_orders(H1)
        om1 = om1_of(fld)
        lhs = [d.v for d in flat_div(G2)]
        rhs = rhs_div(H1, G1, om1)
        print(seed, lhs == rhs, lhs)
        # Omega1 formula: Omega1(a) = grad ^ S(a) - (a.grad) B, S = sym H1, B = 1/2 d_b ^ H1(b)
        Ssym = mscal(F(1,2), madd(H1, transpose(H1)))
        ok = True
        for a in range(D):
            pred = {}
            # grad ^ S(e_a): sum_mu e^mu ^ d_mu S(e_a)
            for mu in range(D):
                dS = {(k,): Ssym[k][a].d(mu) for k in range(D) if Ssym[k][a].d(mu)}
                pred = gtg.m_add(pred, gtg.wedge(REC[mu], dS, S))
            # B = 1/2 sum_b e^b ^ H1(e_b)
            Bv = {}
            for b in range(D):
                hb_ = {(k,): H1[k][b] for k in range(D) if H1[k][b]}
                Bv = gtg.m_add(Bv, gtg.m_scal(F(1,2), gtg.wedge(REC[b], hb_, S)))
            pred = gtg.m_sub(pred, gtg.m_d(Bv, a))
            got = om1[a]
            diff = gtg.m_sub(pred, got)
            ok = ok and all(not x for x in diff.values())
        print("Omega1 formula:", ok)
