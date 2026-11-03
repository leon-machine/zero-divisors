"""descent-lift.pairing-creator-under-transport-algorithm: exact checks in Cl(2,2) (GA blade engine).

Generators e1, e2 (square +1) and e3, e4 (square -1) are GA indices 0, 1, 2, 3. f_k = (e_k + e_{k+2})/2,
f_k^* = (e_k - e_{k+2})/2, n = f1^* f2^*, h = f1^* f2, dagger = reversion composed with e3, e4 -> -e3, -e4.
(i)   n != 0 is a pure bivector, n^2 = 0, Cl(2,2) has centre R (only the scalar blade is central);
      e = f2 f2^*, f = f1^* f1 are idempotents, non-central, with n(1 - e) = 0 and (1 - f) n = 0; n is no
      vector and no central idempotent, so Step 2 returns type P; f2 f2^* = wv for (v, w) = (f2^*, f2)
      and f1^* f1 = vw for (v, w) = (f1^*, f1), with v, w null and vw + wv = 1 (hyperbolic pairs).
(ii)  dagger is an anti-automorphism (all 256 blade pairs) and an involution, exchanging f_k and f_k^*;
      n^dag = f2 f1 satisfies the four Penrose equations with n; n n^dag = P11, n^dag n = P00, and
      n^dag P00 = 0.
(iii) f wedge f^* = (f f^* - f^* f)/2 squares to 1/4 and commutes with N = f^* f, for each rung.
(iv)  e4 -> -e4 is multiplicative on all blade pairs, fixes f1, sends f2 to f2^*, h to n, X_h to X_p and
      P00 to P01.
(v)   X_p^2 = -P_even, X_h^2 = -P_odd, X^3 = -X, P = -X^2 idempotent, X P = X; at (cos, sin) = (3/5, 4/5)
      (1 - P) + cos P + sin X is even with R R~ = 1 and R^dag R = 1 for both; the pairing rotor sends P00
      to (3/5) P00 + (4/5) n P00, the hop rotor fixes P00; X_p = (e1e2 + e3e4)/2, X_h = (e1e2 - e3e4)/2.
(vi)  n^2 = (n^dag)^2 = 0, n n^dag + n^dag n = P_even, X_p = n - n^dag.
(vii) The pinching x -> P_k x P_k + (1 - P_k) x (1 - P_k), P_k = f_k^* f_k, of either rung erases n, h, X_p
      and X_h and fixes sigma_1, sigma_2 and sigma_1 sigma_2, sigma_k = f_k f_k^* - f_k^* f_k.
The readings of Step 3 and the no-go (which repair the algorithm would attempt) are the imported Fact's;
the check covers the identities on which they are applied.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = GA.sig(2, 2)
BLADES = GA.all_blades(4)
SAMPLES = [{(): F(2), (0, 1): F(-1), (2,): F(3, 2)}, {(1, 2, 3): F(1), (0,): F(-5, 3), (0, 3): F(1, 4)}]


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def half(x):
    return GA.scal(F(1, 2), x)


E = [GA.gen(i) for i in range(4)]
f1, f1s = half(GA.add(E[0], E[2])), half(GA.sub(E[0], E[2]))
f2, f2s = half(GA.add(E[1], E[3])), half(GA.sub(E[1], E[3]))
ONE = GA.sc(1)


def dg(x):
    r = GA.reverse(x)
    return {b: c * (-1) ** sum(1 for i in b if i >= 2) for b, c in r.items()}


def refl(x):
    return {b: c * (-1) ** sum(1 for i in b if i == 3) for b, c in x.items()}


def projs():
    v1, o1 = m(f1, f1s), m(f1s, f1)       # mode 1 empty / occupied
    v2, o2 = m(f2, f2s), m(f2s, f2)
    return {"00": m(v1, v2), "01": m(v1, o2), "10": m(o1, v2), "11": m(o1, o2)}


def central(x):
    return all(GA.commutes(x, e, SQ) for e in E)


def check_type_p_and_annihilating_idempotents():
    premise("descent-lift.imported-taxonomy-type-p-rule-algorithm")
    ok = True
    n = m(f1s, f2s)
    ok = ok and n != {} and all(len(b) == 2 for b in n) and m(n, n) == {}
    ok = ok and [b for b in BLADES if central({b: F(1)})] == [()]
    e, f = m(f2, f2s), m(f1s, f1)
    ok = ok and m(e, e) == e and m(f, f) == f
    ok = ok and not central(e) and not central(f)
    ok = ok and m(n, GA.sub(ONE, e)) == {} and m(GA.sub(ONE, f), n) == {}
    ok = ok and m(n, f2s, f2) == {} and m(f1, f1s, n) == {}
    is_vector = all(len(b) == 1 for b in n)
    is_central_idem = central(n) and m(n, n) == n
    ok = ok and not is_vector and not is_central_idem
    for v, w, idem, order in ((f2s, f2, e, "wv"), (f1s, f1, f, "vw")):
        ok = ok and m(v, v) == {} and m(w, w) == {}
        ok = ok and GA.add(m(v, w), m(w, v)) == ONE
        ok = ok and idem == (m(w, v) if order == "wv" else m(v, w))
    GA.check("(i) n = f1* f2* nilpotent bivector, type P, annihilating idempotents of hyperbolic-pair form", ok)
    return ok


def check_moore_penrose_and_fock_adjoint():
    premise("descent-lift.imported-taxonomy-type-p-rule-algorithm")
    ok = True
    for a in BLADES:
        for b in BLADES:
            x, y = {a: F(1)}, {b: F(1)}
            ok = ok and dg(m(x, y)) == m(dg(y), dg(x))
    ok = ok and all(dg(dg(s)) == s for s in SAMPLES)
    ok = ok and dg(f1) == f1s and dg(f2) == f2s and dg(f1s) == f1
    n = m(f1s, f2s)
    nd = dg(n)
    P = projs()
    ok = ok and nd == m(f2, f1)
    # by hand: f2 f1 = (e2 + e4)(e1 + e3)/4 = (-e1e2 + e2e3 - e1e4 - e3e4)/4
    ok = ok and nd == {(0, 1): F(-1, 4), (1, 2): F(1, 4), (0, 3): F(-1, 4), (2, 3): F(-1, 4)}
    ok = ok and m(n, nd).get(()) == F(1, 4)              # a primitive idempotent of Mat_4: scalar part 1/4
    ok = ok and m(n, nd, n) == n and m(nd, n, nd) == nd
    ok = ok and dg(m(n, nd)) == m(n, nd) and dg(m(nd, n)) == m(nd, n)
    ok = ok and m(n, nd) == P["11"] and m(nd, n) == P["00"]
    ok = ok and m(nd, P["00"]) == {}
    GA.check("(ii) dagger anti-automorphism; n^dag = f2 f1 is the Moore-Penrose inverse; nn^dag = P11, n^dag n = P00", ok)
    return ok


def check_rung_bivector_is_cartan():
    ok = True
    for f, fs in ((f1, f1s), (f2, f2s)):
        w = half(GA.sub(m(f, fs), m(fs, f)))
        ok = ok and m(w, w) == GA.sc(F(1, 4))
        ok = ok and GA.commutes(w, m(fs, f), SQ)
    GA.check("(iii) f wedge f* squares to 1/4 and commutes with N", ok)
    return ok


def check_reflection_exchanges_hop_and_pairing():
    ok = True
    for a in BLADES:
        for b in BLADES:
            x, y = {a: F(1)}, {b: F(1)}
            ok = ok and refl(m(x, y)) == m(refl(x), refl(y))
    n, h = m(f1s, f2s), m(f1s, f2)
    Xh, Xp = GA.sub(h, dg(h)), GA.sub(n, dg(n))
    P = projs()
    ok = ok and refl(f1) == f1 and refl(f2) == f2s
    ok = ok and refl(h) == n and refl(Xh) == Xp and refl(P["00"]) == P["01"]
    # by hand: h = (e1 - e3)(e2 + e4)/4 = (e1e2 + e1e4 + e2e3 - e3e4)/4, n = (e1e2 - e1e4 + e2e3 + e3e4)/4
    ok = ok and h == {(0, 1): F(1, 4), (0, 3): F(1, 4), (1, 2): F(1, 4), (2, 3): F(-1, 4)}
    ok = ok and n == {(0, 1): F(1, 4), (0, 3): F(-1, 4), (1, 2): F(1, 4), (2, 3): F(1, 4)}
    GA.check("(iv) e4 -> -e4: automorphism fixing f1, f2 -> f2*, h -> n, X_h -> X_p, P00 -> P01", ok)
    return ok


def rotor(X, c, s):
    P = GA.neg(m(X, X))
    return GA.add(GA.sub(ONE, P), GA.scal(c, P), GA.scal(s, X)), P


def check_generators_square_and_rotors():
    ok = True
    n, h = m(f1s, f2s), m(f1s, f2)
    Xp, Xh = GA.sub(n, dg(n)), GA.sub(h, dg(h))
    P = projs()
    Pe, Po = GA.add(P["00"], P["11"]), GA.add(P["01"], P["10"])
    ok = ok and m(Xp, Xp) == GA.neg(Pe) and m(Xh, Xh) == GA.neg(Po)
    ok = ok and Xp == {(0, 1): F(1, 2), (2, 3): F(1, 2)} and Xh == {(0, 1): F(1, 2), (2, 3): F(-1, 2)}
    rots = []
    for X in (Xp, Xh):
        ok = ok and m(X, X, X) == GA.neg(X)
        R, Pr = rotor(X, F(3, 5), F(4, 5))
        ok = ok and m(Pr, Pr) == Pr and m(X, Pr) == X
        ok = ok and all(len(b) % 2 == 0 for b in R)
        ok = ok and m(R, GA.reverse(R)) == ONE and m(dg(R), R) == ONE
        rots.append(R)
    ok = ok and m(rots[0], P["00"]) == GA.add(GA.scal(F(3, 5), P["00"]), GA.scal(F(4, 5), m(n, P["00"])))
    ok = ok and m(rots[1], P["00"]) == P["00"]
    GA.check("(v) X_p^2 = -P_even, X_h^2 = -P_odd; (3/5, 4/5) rotors of Spin(2,2), unitary; witness state", ok)
    return ok


def check_pairing_pair_identities():
    ok = True
    n = m(f1s, f2s)
    nd = dg(n)
    P = projs()
    ok = ok and m(n, n) == {} and m(nd, nd) == {}
    ok = ok and GA.add(m(n, nd), m(nd, n)) == GA.add(P["00"], P["11"])
    ok = ok and GA.sub(n, nd) == {(0, 1): F(1, 2), (2, 3): F(1, 2)}
    GA.check("(vi) n, n^dag: hyperbolic-pair identities on the even sector", ok)
    return ok


def check_pinching_erases_ladder_words():
    premise("descent-lift.imported-pinching-one-way-door")
    ok = True
    n, h = m(f1s, f2s), m(f1s, f2)
    words = [n, h, GA.sub(n, dg(n)), GA.sub(h, dg(h))]
    s1 = GA.sub(m(f1, f1s), m(f1s, f1))
    s2 = GA.sub(m(f2, f2s), m(f2s, f2))
    fixed = [s1, s2, m(s1, s2)]
    for f, fs in ((f1, f1s), (f2, f2s)):
        Pk = m(fs, f)
        Qk = GA.sub(ONE, Pk)
        pin = lambda x: GA.add(m(Pk, x, Pk), m(Qk, x, Qk))
        ok = ok and all(pin(x) == {} for x in words)
        ok = ok and all(pin(x) == x for x in fixed)
    ok = ok and s1 == {(0, 2): F(-1)} and s2 == {(1, 3): F(-1)}
    GA.check("(vii) each rung's pinching erases n, h, X_p, X_h and fixes sigma_1, sigma_2, sigma_1 sigma_2", ok)
    return ok
