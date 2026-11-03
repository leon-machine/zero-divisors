"""synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation: exact checks.

All arithmetic over Fractions and Gaussian rationals (GA.QI). Cl(2,4): e0, e1 square +1,
e2..e5 square -1. The Witt flag W is the +i eigenspace of the orthogonal complex structure
J: e0 -> e1, e2 -> e3, e4 -> e5; w_k = e_{2k} - i e_{2k+1}.
  (1) grade involution composed with reversal reverses products (anti-automorphism) and is not
      multiplicative; its vector action is -1; grade involution is Ad(I6) with
      I6 = (e0e1)(e2e3)(e4e5), each factor squaring to -1 and I6 rev(I6) = 1 (a rotor; each factor is
      the rotor exp(pi B_k / 2)); control: in Cl(1,3), I4 rev(I4) = -1;
  (2) W is maximal isotropic, B(w_a, conj w_b) = diag(2,-2,-2) so W + conj W = C^6, the null blade
      N = w1w2w3 is annihilated by W, I6 N = i N and I6 conj(N) = -i conj(N): the complex
      conjugate flag is in the other family; control: in Cl(3,3), I6^2 = +1 (real chirality);
  (3) the real reflection g in e1, e3, e5 carries w_k to conj(w_k), has g(I6) = -I6, and reverses the
      MacDowell-Mansouri integrand eps(I, V, F, F) under the fibre action; complex conjugation fixes
      it (value -152 pinned); the complex-linear Witt swap does not preserve R^{2,4};
  (4) C = Ad(I6) o kappa is multiplicative, antilinear, involutive, fixes I6 and carries N to -conj(N).
"""
from fractions import Fraction as F
import GA
from GA import mul, add, gen, grade_inv, reverse, sig, QI
from tp_premise import premise

SQ = sig(2, 4)
I_ = QI(0, 1)


def cs(c, x):
    out = {}
    for b, v in x.items():
        p = c * v
        if p != 0:
            out[b] = p
    return out


def conj(x):
    return {b: (v.conj() if isinstance(v, QI) else v) for b, v in x.items()}


def eqx(x, y):
    return add(x, cs(F(-1), y)) == {} or all(v == 0 for v in add(x, cs(F(-1), y)).values())


def gpart(x, k):
    return {b: v for b, v in x.items() if len(b) == k}


def flag():
    w = [add(gen(2 * k), cs(-I_, gen(2 * k + 1))) for k in range(3)]
    return w, [conj(x) for x in w]


def pseudo():
    return {(0, 1, 2, 3, 4, 5): F(1)}


def vec(c):
    out = {}
    for k, a in enumerate(c):
        out = add(out, cs(F(a), gen(k)))
    return out


def biv(c):
    out = {}
    n = 0
    for a in range(6):
        for b in range(a + 1, 6):
            out = add(out, cs(F(c[n]), mul(gen(a), gen(b), SQ)))
            n += 1
    return out


def integrand(I, V, Fb):
    top = gpart(mul(mul(mul(I, V, SQ), Fb, SQ), Fb, SQ), 6)
    return top.get((0, 1, 2, 3, 4, 5), F(0))


def gref(x):
    """Outermorphism of the real reflection negating e1, e3, e5."""
    out = {}
    for b, v in x.items():
        s = F(-1) ** sum(1 for j in b if j % 2 == 1)
        out[b] = s * v
    return out


def check_anti_automorphism_and_rotor():
    premise("singularity.euclidean-rotor-where-it-lies")
    C = lambda z: grade_inv(reverse(z))
    X = add(gen(0), mul(gen(1), gen(2), SQ), cs(F(3), gen(4)))
    Y = add(gen(3), cs(F(2), mul(gen(0), gen(5), SQ)), {(): F(1)})
    assert eqx(C(mul(X, Y, SQ)), mul(C(Y), C(X), SQ))
    assert not eqx(C(mul(X, Y, SQ)), mul(C(X), C(Y), SQ))
    for k in range(6):
        assert eqx(C(gen(k)), cs(F(-1), gen(k)))
    B = [mul(gen(0), gen(1), SQ), mul(gen(2), gen(3), SQ), mul(gen(4), gen(5), SQ)]
    for b in B:
        assert mul(b, b, SQ) == {(): F(-1)}
    I6 = mul(mul(B[0], B[1], SQ), B[2], SQ)
    assert I6 == pseudo()
    assert mul(I6, reverse(I6), SQ) == {(): F(1)}
    I6inv = reverse(I6)
    for k in range(6):
        assert eqx(mul(mul(I6, gen(k), SQ), I6inv, SQ), cs(F(-1), gen(k)))
    for z in (X, Y, mul(X, Y, SQ)):
        assert eqx(mul(mul(I6, z, SQ), I6inv, SQ), grade_inv(z))
    sq13 = sig(1, 3)
    I4 = {(0, 1, 2, 3): F(1)}
    assert mul(I4, reverse(I4), sq13) == {(): F(-1)}
    return True


def check_conjugate_flag_other_family():
    premise("dark-matter.two-families-are-two-chiralities")
    w, wb = flag()
    for a in range(3):
        for b in range(3):
            assert gpart(add(mul(w[a], w[b], SQ), mul(w[b], w[a], SQ)), 0) == {}
    gram = [[gpart(add(mul(w[a], wb[b], SQ), mul(wb[b], w[a], SQ)), 0).get((), F(0))
             for b in range(3)] for a in range(3)]
    assert gram == [[4, 0, 0], [0, -4, 0], [0, 0, -4]]
    N = mul(mul(w[0], w[1], SQ), w[2], SQ)
    Nb = conj(N)
    assert N != {} and not eqx(N, Nb)
    for k in range(3):
        assert mul(w[k], N, SQ) == {} and mul(wb[k], Nb, SQ) == {}
        assert mul(wb[k], N, SQ) != {}
    I6 = pseudo()
    assert eqx(mul(I6, N, SQ), cs(I_, N))
    assert eqx(mul(I6, Nb, SQ), cs(-I_, Nb))
    assert mul(I6, I6, SQ) == {(): F(-1)}
    assert mul(I6, I6, sig(3, 3)) == {(): F(1)}
    return True


def check_real_linear_swap_reverses_action():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("dark-matter.two-families-are-two-chiralities")
    w, wb = flag()
    for k in range(3):
        assert mul(w[k], w[k], SQ) == {} and mul(wb[k], wb[k], SQ) == {}
        assert mul(gref(w[k]), gref(w[k]), SQ) == {}
    for k in range(3):
        assert eqx(gref(w[k]), wb[k])
    assert gref(pseudo()) == {(0, 1, 2, 3, 4, 5): F(-1)}
    I = vec([2, 1, 0, 1, -1, 3])
    V = vec([1, -2, 3, 0, 2, 1])
    Fb = biv([1, 0, 2, -1, 3, 1, 1, -2, 0, 4, 1, -1, 2, 0, 3])
    e = integrand(I, V, Fb)
    assert e == F(-152)
    CI, CV, CF = grade_inv(reverse(I)), grade_inv(reverse(V)), grade_inv(reverse(Fb))
    assert integrand(CI, CV, CF) == e
    assert integrand(conj(CI), conj(CV), conj(CF)) == e
    assert integrand(gref(CI), gref(CV), gref(CF)) == -e
    assert integrand(gref(I), gref(V), gref(Fb)) == -e
    # complex-linear Witt swap w_k <-> v_k, v_k = conj(w_k)/B_k, B = (2,-2,-2): S(e0) is not real
    v0 = cs(QI(F(1, 2)), wb[0])
    Se0 = add(cs(QI(F(1, 2)), v0), cs(QI(1), w[0]))
    assert any(isinstance(c, QI) and c.im != 0 for c in Se0.values())
    return True


def check_C_antilinear_automorphism():
    premise("dark-matter.two-families-are-two-chiralities")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    I6 = pseudo()
    I6inv = reverse(I6)
    C = lambda z: mul(mul(I6, conj(z), SQ), I6inv, SQ)
    X = add(gen(0), cs(I_, mul(gen(1), gen(2), SQ)), cs(QI(3, 1), gen(4)))
    Y = add(cs(QI(0, 2), gen(3)), cs(F(2), mul(gen(0), gen(5), SQ)), {(): QI(1, -1)})
    assert eqx(C(mul(X, Y, SQ)), mul(C(X), C(Y), SQ))
    assert eqx(C(cs(I_, X)), cs(-I_, C(X)))
    assert eqx(C(C(X)), X) and eqx(C(C(Y)), Y)
    assert eqx(C(I6), I6)
    w, wb = flag()
    N = mul(mul(w[0], w[1], SQ), w[2], SQ)
    assert eqx(C(N), cs(F(-1), conj(N)))
    # pinned values: the image of X and the fixed frame action
    assert C(X) == {(0,): QI(-1), (1, 2): QI(0, -1), (4,): QI(-3, 1)}
    for k in range(6):
        assert C(gen(k)) == {(k,): F(-1)}
    I = vec([2, 1, 0, 1, -1, 3])
    V = vec([1, -2, 3, 0, 2, 1])
    Fb = biv([1, 0, 2, -1, 3, 1, 1, -2, 0, 4, 1, -1, 2, 0, 3])
    assert integrand(C(I), C(V), C(Fb)) == integrand(I, V, Fb) == F(-152)
    return True


def top6(x):
    return gpart(x, 6).get((0, 1, 2, 3, 4, 5), F(0))


def check_reading_convention():
    """Field-action convention against the two other readings, on fixed data (values pinned):
    substitution of phi = grade involution o reversal into a bivector slot flips a functional odd in a
    bivector field (-226 -> +226) while C fixes it; applying phi to the whole integrand IVFF inverts the
    sign statements of clause (3) (kappa: -152 -> +152; real reflection: -152 kept)."""
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("dark-matter.two-families-are-two-chiralities")
    I = vec([2, 1, 0, 1, -1, 3])
    V = vec([1, -2, 3, 0, 2, 1])
    Fb = biv([1, 0, 2, -1, 3, 1, 1, -2, 0, 4, 1, -1, 2, 0, 3])
    a = vec([1, 0, 1, 2, 0, -1])
    b = vec([0, 3, -1, 1, 1, 2])
    phi = lambda z: grade_inv(reverse(z))
    E = gpart(mul(a, b, SQ), 2)
    e4 = lambda x1, x2, x3, x4: top6(mul(mul(mul(x1, x2, SQ), x3, SQ), x4, SQ))
    assert e4(I, V, Fb, E) == F(-226)
    assert e4(grade_inv(I), grade_inv(V), grade_inv(Fb), gpart(mul(grade_inv(a), grade_inv(b), SQ), 2)) == F(-226)
    assert e4(phi(I), phi(V), phi(Fb), gpart(mul(phi(a), phi(b), SQ), 2)) == F(226)
    P = mul(mul(mul(I, V, SQ), Fb, SQ), Fb, SQ)
    assert top6(P) == F(-152)
    assert top6(reverse(grade_inv(conj(P)))) == F(152)
    assert top6(reverse(grade_inv(gref(P)))) == F(-152)
    assert integrand(grade_inv(I), grade_inv(V), Fb) == F(-152)
    assert integrand(gref(grade_inv(I)), gref(grade_inv(V)), gref(Fb)) == F(152)
    return True
