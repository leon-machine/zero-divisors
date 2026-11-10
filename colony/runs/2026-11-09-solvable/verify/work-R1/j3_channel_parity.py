"""R1: parity of the Dirac channel operator in the horizon-channels proposal, and a repaired operator.

T = gamma^0 gamma^1 K maps even multivector fields to odd ones (K is left multiplication by vectors), so
T Phi = lambda Phi has no nonzero even solution. Repaired operator: T~ Phi := (T Phi) gamma_0, which
  - maps even to even,
  - commutes with A (left) and with right multiplication by I sigma_3 and by gamma_0,
  - squares to K^2 (= T^2),
and the channel equation K Phi = lambda gamma^{01} Phi gamma_0 gives the squared operator
  d_t^2 - d_{r*}^2 + lambda^2 W^2 + lambda (d_{r*} W) [Phi -> gamma^0 Phi gamma_0],
with the same potentials V_+- on the +-1 eigenspaces of the even involution Phi -> gamma^0 Phi gamma_0.
Exact jets from lib/gtg.py at the proposal's first sample point.
"""
import sys
import importlib.util
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
import GA
import gtg
from gtg import m_add, m_scal, m_mul, m_d, m_val, er, S13

spec = importlib.util.spec_from_file_location(
    "hc", "/home/claude/phys-graph/proposals/"
    "synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional/check.py")
hc = importlib.util.module_from_spec(spec)
import tp_premise
tp_premise.configure("/home/claude/phys-graph/store")
spec.loader.exec_module(hc)


def grades(X):
    return sorted({len(k) for k, v in X.items() if v != 0})


def rmul(X, B):
    """Right multiplication of a jet-valued multivector by a constant multivector B."""
    out = {}
    for k, v in X.items():
        prod = GA.mul({k: F(1)}, B, S13)
        for kk, c in prod.items():
            out[kk] = out[kk] + c * v if kk in out else c * v
    return {k: v for k, v in out.items()}


def main():
    r0, w, s0, c0, sp, cp = hc.POINTS[0]
    M, f, fld, t, r, th, ph = hc.setup(r0, w, s0, c0, order=3)
    sn, cs = gtg.sincos(2, s0, c0, 4, 3)
    fj = f(r)
    Phi = hc.generic_phi(t, r, th, ph, r0)
    g01 = GA.mul(er(0), er(1), S13)
    g0 = er(0)                                    # gamma^0 = gamma_0
    Is3 = GA.mul(er(2), er(1), S13)               # I sigma_3 = gamma_2 gamma_1 (gamma^i = -gamma_i: sign irrelevant)
    K = lambda X: hc.K_op(X, cs / sn, 1 / sn)
    T = lambda X: m_mul(g01, K(X))
    Tt = lambda X: rmul(T(X), g0)
    A = lambda X: hc.A_op(X, fj)

    print("grades of Phi:", grades(m_val(Phi)))
    print("grades of T Phi (proposal's T):", grades(m_val(T(Phi))), "-> T maps even to odd")
    print("grades of T~ Phi (repaired):   ", grades(m_val(Tt(Phi))))
    assert set(grades(m_val(T(Phi)))) <= {1, 3}
    assert set(grades(m_val(Tt(Phi)))) <= {0, 2, 4}
    # commutations
    assert GA.sub(m_val(Tt(A(Phi))), m_val(A(Tt(Phi)))) == {}
    assert GA.sub(m_val(Tt(rmul(Phi, Is3))), m_val(rmul(Tt(Phi), Is3))) == {}
    assert GA.sub(m_val(Tt(rmul(Phi, g0))), m_val(rmul(Tt(Phi), g0))) == {}
    assert GA.sub(m_val(Tt(Tt(Phi))), m_val(K(K(Phi)))) == {}
    print("T~ commutes with A, with right mult by I sigma_3 and gamma_0; T~^2 = K^2: OK")
    # squared repaired channel operator
    W = fj.pw(F(1, 2), w * w) / r
    dW = fj * W.d(1)
    for lam in (1, -2, 3):
        C = lambda X: m_add(A(X), m_scal(lam * W, rmul(m_mul(g01, X), g0)))
        lhs = m_val(C(C(Phi)))
        box = m_add(m_d(m_d(Phi, 0), 0), m_scal(-1, m_scal(fj, m_d(m_scal(fj, m_d(Phi, 1)), 1))))
        rhs = m_val(m_add(box, m_scal(lam * lam * W * W, Phi), m_scal(lam * dW, rmul(m_mul(g0, Phi), g0))))
        assert GA.sub(lhs, rhs) == {}
        assert set(grades(lhs)) <= {0, 2, 4}
    print("repaired squared channel: d_t^2 - d_r*^2 + lam^2 W^2 + lam dW (gamma^0 . gamma_0), lam = 1, -2, 3: OK")
    # the proposal's squared operator applied to an even field has odd part (parity mixing)
    lam = 1
    C = lambda X: m_add(A(X), m_scal(lam * W, m_mul(g01, X)))
    print("proposal's channel operator on even Phi has grades:", grades(m_val(C(Phi))), "(mixed)")
    # perturbation: the repaired squared identity fails without the right factor gamma_0 in the potential term
    rhs_bad = m_val(m_add(box, m_scal(W * W, Phi), m_scal(dW, m_mul(g0, Phi))))
    lhs1 = m_val(m_add(A(m_add(A(Phi), m_scal(W, rmul(m_mul(g01, Phi), g0)))),
                       m_scal(W, rmul(m_mul(g01, m_add(A(Phi), m_scal(W, rmul(m_mul(g01, Phi), g0)))), g0))))
    assert GA.sub(lhs1, rhs_bad) != {}
    print("perturbation (drop the right factor): identity fails, as it should")


if __name__ == "__main__":
    main()
