"""dark-matter.orientation-arrow-seventeenth-refutation (v7): exact checks of the last step.

The last step does not use the trichotomy's exhaustiveness. It reads the orientation bit
against Definition obj.dark-energy.four-ways-number-enters-theory-shape directly: CPT
conjugation C maps each solution space onto itself (it fixes the action and does not move
the parameter), and the bit is C-odd, so it is not constant on any nonempty solution space:
clause (I). CPT conjugation, the composite of grade involution, reversal and the flag
conjugate, is an anti-automorphism; in the field-action convention (vectors by its vector
part, connections through the induced Lie algebra automorphism, so curvature is fixed) it
acts on fields as C = Ad(I6) o kappa, kappa complex conjugation: antilinear. The checks:
  (a) the parameter is not moved and the action integrand is fixed: C = Ad(I6) o kappa is
      applied explicitly (Gaussian rationals, GA.QI), on vectors and on the curvature bivector;
      on fixed real rational data in R^{2,4} it is -1 on vectors and fixes the bivector, and
      <I,I>, <V,V>, <I,V> and eps(I, V, F, F) are invariant; on complexified data it is
      antilinear and carries each of them to its complex conjugate, so a real action is fixed;
      control: negating I alone flips the integrand, and the real-linear flag conjugate (the
      reflection in e1, e3, e5) in place of kappa reverses it;
  (b) the orientation bit is C-odd under the actual C: on C^{2,4} (Gaussian rationals) the flag
      v_k = e_{2k} + i e_{2k+1} (k = 0, 1, 2) is maximal isotropic, and C = Ad(I6) o kappa, applied
      explicitly, sends v_k to -w_k with w_k = kappa(v_k), so it carries the pure vacuum
      v0 v1 v2 (annihilated by every v_k, not by any w_k) to -w0 w1 w2, the other vacuum
      (annihilated by every w_k, not by any v_k), and C^2 = 1 on both; the same exchange on the
      split real form Cl(3,3) (the swap v_k <-> w_k, an isometry of the three null pairs) is kept
      as the real model; the neutrino-sector flag-covariance remark is not tested;
  (c) the Definition's logic, exhaustively on small finite theories: whenever an involution C
      preserves every solution space and q(Cx) = -q(x), q is (I), not (D), not (P), not (K)
      for any kinematic partition C respects.
"""
from fractions import Fraction as F
from itertools import product
import GA
from GA import mul, add, sub, scal, gen, grade_inv, reverse, dot, sig, QI
from tp_premise import premise


def grade_part(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def vec(cs):
    out = {}
    for k, c in enumerate(cs):
        out = add(out, scal(F(c), gen(k)))
    return out


def biv(cs, sq):
    out = {}
    n = 0
    for a in range(6):
        for b in range(a + 1, 6):
            out = add(out, scal(F(cs[n]), mul(gen(a), gen(b), sq)))
            n += 1
    return out


def integrand(I, V, Fb, sq):
    """eps(I, V, F, F): the grade-6 part of I V F F (the outer product), as its one coefficient."""
    top = grade_part(mul(mul(mul(I, V, sq), Fb, sq), Fb, sq), 6)
    return top.get((0, 1, 2, 3, 4, 5), F(0))


def conj(x):
    """kappa: complex conjugation of the coefficients (antilinear)."""
    return {b: (v.conj() if isinstance(v, QI) else v) for b, v in x.items()}


def cs(c, x):
    out = {}
    for b, v in x.items():
        p = c * v
        if p != 0:
            out[b] = p
    return out


def eqx(x, y):
    return all(v == 0 for v in add(x, cs(F(-1), y)).values())


def gref(x):
    """Outermorphism of the real reflection negating e1, e3, e5 (a real-linear flag conjugate)."""
    return {b: F(-1) ** sum(1 for j in b if j % 2 == 1) * v for b, v in x.items()}


def check_parameter_not_moved():
    """C fixes the frozen-point data the action is built from: the norms <I,I>, <V,V>, <I,V>
    (so the parameter mu is not moved) and the integrand eps(I, V, F, F). C is the field action
    of the CPT composite, C = Ad(I6) o kappa with kappa complex conjugation, applied explicitly
    to the vectors I, V and to the curvature F. Fixed rational data in R^{2,4}, values pinned.
    On complexified data C is antilinear and carries the norms and the integrand to their
    complex conjugates. Controls: negating I alone flips the integrand; the real-linear flag
    conjugate (reflection in e1, e3, e5) in place of kappa reverses it. This tests the
    frozen-point part of the action only; the gauge sector's invariance is the premise's clause."""
    premise("dark-matter.premise-cpt-covariance")
    premise("dark-matter.imported-inputs-standard-model-chain")
    premise("synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation")   # C = Ad(I6) o kappa
    sq = sig(2, 4)
    I6 = mul(mul(mul(gen(0), gen(1), sq), mul(gen(2), gen(3), sq), sq), mul(gen(4), gen(5), sq), sq)
    assert I6 == {(0, 1, 2, 3, 4, 5): F(1)} and mul(I6, reverse(I6), sq) == {(): F(1)}
    C = lambda z: mul(mul(I6, conj(z), sq), reverse(I6), sq)
    i = QI(0, 1)
    I = vec([2, 1, 0, 1, -1, 3])                  # arbitrary rational data
    V = vec([1, -2, 3, 0, 2, 1])
    Fb = biv([1, 0, 2, -1, 3, 1, 1, -2, 0, 4, 1, -1, 2, 0, 3], sq)
    val = integrand(I, V, Fb, sq)
    assert (dot(I, I, sq), dot(V, V, sq), dot(I, V, sq)) == (F(-6), F(-9), F(-1))
    assert val == F(-152)
    # on real data C is -1 on vectors and fixes bivectors (the curvature); it equals grade
    # involution argumentwise there
    CI, CV, CF = C(I), C(V), C(Fb)
    assert eqx(CI, scal(F(-1), I)) and eqx(CV, scal(F(-1), V)) and eqx(CF, Fb)
    assert eqx(CI, grade_inv(I)) and eqx(CF, grade_inv(Fb))
    assert (dot(CI, CI, sq), dot(CV, CV, sq), dot(CI, CV, sq)) == (F(-6), F(-9), F(-1))
    assert integrand(CI, CV, CF, sq) == val
    # C is antilinear and involutive
    assert eqx(C(cs(i, I)), cs(-i, CI)) and eqx(C(C(Fb)), Fb)
    # complexified data: C carries every norm and the integrand to its complex conjugate
    Ic = add(I, cs(i, vec([0, 1, 1, 0, 2, -1])))
    Vc = add(V, cs(i, vec([1, 0, -1, 2, 0, 1])))
    Fc = add(Fb, cs(i, biv([0, 1, 0, 0, -1, 2, 0, 1, 1, 0, 0, -2, 1, 0, 1], sq)))
    vc = integrand(Ic, Vc, Fc, sq)
    assert vc == QI(-118, 150)
    assert integrand(C(Ic), C(Vc), C(Fc), sq) == vc.conj()
    for (x, y) in ((Ic, Ic), (Vc, Vc), (Ic, Vc)):
        d = QI(dot(x, y, sq))
        assert QI(dot(C(x), C(y), sq)) == d.conj()
    # controls: negating I alone flips the integrand; a real-linear flag conjugate reverses it
    assert integrand(scal(F(-1), I), V, Fb, sq) == -val
    assert integrand(gref(CI), gref(CV), gref(CF), sq) == -val
    return True


def check_flag_conjugate_odd():
    premise("standard-model.hyp-s-slot-statistics")
    premise("dark-matter.imported-derived-generation-flag")
    premise("standard-model.chirality-two-halves-spinor-module-conjugation")
    sq = sig(3, 3)                      # e_k square +1 (k = 0,1,2), f_k square -1 (k = 3,4,5)
    v = [scal(F(1, 2), add(gen(k), gen(k + 3))) for k in range(3)]
    w = [sub(gen(k), gen(k + 3)) for k in range(3)]
    for a in range(3):
        for b in range(3):
            assert dot(v[a], v[b], sq) == 0 and dot(w[a], w[b], sq) == 0
            assert dot(v[a], w[b], sq) == (1 if a == b else 0)
    # the swap v_k <-> w_k preserves every pairing (symmetric form): an isometry
    for a in range(3):
        for b in range(3):
            assert dot(w[a], v[b], sq) == dot(v[a], w[b], sq)
    vv = mul(mul(v[0], v[1], sq), v[2], sq)
    ww = mul(mul(w[0], w[1], sq), w[2], sq)
    assert sub(vv, ww) != {} and vv != {} and ww != {}
    # each vacuum is annihilated by its own half: v_k vv = 0, w_k ww = 0, and not by the other
    for k in range(3):
        assert mul(v[k], vv, sq) == {} and mul(w[k], ww, sq) == {}
        assert mul(w[k], vv, sq) != {} and mul(v[k], ww, sq) != {}
    # the actual C = Ad(I6) o kappa on C^{2,4}: it exchanges the flag with its conjugate and the two vacua
    premise("synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation")
    sq = sig(2, 4)
    i = QI(0, 1)
    I6 = mul(mul(mul(gen(0), gen(1), sq), mul(gen(2), gen(3), sq), sq), mul(gen(4), gen(5), sq), sq)
    C = lambda z: mul(mul(I6, conj(z), sq), reverse(I6), sq)
    vc = [add(gen(2 * k), cs(i, gen(2 * k + 1))) for k in range(3)]
    wc = [conj(x) for x in vc]
    for a in range(3):
        for b in range(3):
            assert QI(dot(vc[a], vc[b], sq)) == 0 and QI(dot(wc[a], wc[b], sq)) == 0
        assert eqx(C(vc[a]), cs(F(-1), wc[a])) and eqx(C(wc[a]), cs(F(-1), vc[a]))
    assert [QI(dot(vc[k], wc[k], sq)) for k in range(3)] == [QI(2), QI(-2), QI(-2)]
    vv = mul(mul(vc[0], vc[1], sq), vc[2], sq)
    ww = mul(mul(wc[0], wc[1], sq), wc[2], sq)
    Cvv = C(vv)
    assert eqx(Cvv, cs(F(-1), ww)) and eqx(C(Cvv), vv) and not eqx(vv, ww)
    for k in range(3):
        assert eqx(mul(vc[k], vv, sq), {}) and not eqx(mul(wc[k], vv, sq), {})
        assert eqx(mul(wc[k], Cvv, sq), {}) and not eqx(mul(vc[k], Cvv, sq), {})
    return True


def classify(q, spaces):
    """Definition clauses (D), (P), (I) for q on the solution spaces {mu: set}."""
    nonconst = any(len({q[x] for x in S}) > 1 for S in spaces.values())
    if nonconst:
        return "I"
    vals = {q[x] for S in spaces.values() for x in S}
    return "D" if len(vals) <= 1 else "P"


def check_definition_logic():
    """Exhaustive over small finite theories: configurations (mu, j), mu in {0,1}, j in 0..3,
    C swapping j <-> j^1; solution spaces are unions of C-orbits (C-stability, the premise's
    action clause); q is any C-odd sign. Every such q is (I) and not (K). The number of cases
    enumerated is pinned (3 * 4 * 16 = 192). Control: without C-stability a C-odd q can be (P)."""
    premise("dark-energy.four-alternatives-are-exhaustive-three-are")
    premise("dark-matter.premise-cpt-covariance")
    premise("dark-matter.premise-flag-as-datum")    # q is a function of the solution, C-odd
    X = [(m, j) for m in range(2) for j in range(4)]
    C = {(m, j): (m, j ^ 1) for (m, j) in X}
    assert all(C[C[x]] == x and C[x] != x for x in X)
    count = 0
    for mask0 in range(1, 4):
        for mask1 in range(0, 4):
            spaces = {}
            for m, mask in ((0, mask0), (1, mask1)):
                S = set()
                for orb in range(2):
                    if mask >> orb & 1:
                        S |= {(m, 2 * orb), (m, 2 * orb + 1)}
                spaces[m] = S
            sols = spaces[0] | spaces[1]
            assert all(C[x] in spaces[x[0]] for x in sols)
            for vals in product((1, -1), repeat=4):
                q = {}
                for n, (m, j) in enumerate([x for x in X if x[1] % 2 == 0]):
                    q[(m, j)] = vals[n]
                    q[(m, j + 1)] = -vals[n]
                assert all(q[C[x]] == -q[x] for x in X)
                assert classify(q, spaces) == "I"
                assert any(q[x] != q[C[x]] for x in sols)
                count += 1
    assert count == 192
    q = {(0, 0): 1, (0, 1): -1, (1, 0): 1, (1, 1): -1}
    assert classify(q, {0: {(0, 0)}, 1: {(1, 1)}}) == "P"
    assert classify(q, {0: {(0, 0), (0, 1)}, 1: {(1, 1)}}) == "I"
    assert classify(q, {0: {(0, 0)}, 1: {(1, 0)}}) == "D"
    return True
