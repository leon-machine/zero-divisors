"""one-relation.odd-square-roots-chiral-phase: exact checks in Cl(1,3) (GA.py, gamma_0^2 = +1,
gamma_i^2 = -1, I = gamma_0 gamma_1 gamma_2 gamma_3).

(1) The square: (v + I w)^2 = Q(v) + Q(w) - 2 I (v ^ w) on six rational vector pairs; every odd
    element is v + I w (the odd blades are spanned by vectors and I times vectors). C^2 = -1 holds on
    (cos t, sin t) u for four rational points of the circle and unit spacelike u (gamma_3 and two
    non-basis ones), and fails for pairs with Q(v) + Q(w) = -1 but v ^ w != 0, and for dependent
    pairs off the unit circle.
(2) Rotor covariance and transitivity on the unit spacelike hyperboloid: for each of four rational
    unit spacelike targets u' the rotor R = 1 - u' gamma_3 (even, R R~ a positive scalar) carries
    gamma_3 to u' (R gamma_3 R~ = (R R~) u'), and R~ (I gamma_3) R is a square root of -1 up to the
    positive factor; the stated rotor 5/4 + 3/4 gamma_0 gamma_3 gives a unit spacelike u' with a time
    component.
(3) The chiral phase at (cos t, sin t) = (3/5, 4/5): I anticommutes with every odd blade,
    e^{-tI} C e^{tI} = C e^{2tI} for three odd C, e^{tI} e^{-tI} = 1, the reverse of e^{tI} is
    itself and not its inverse (so not a rotor), and (psi e^{tI})(psi e^{tI})~ = e^{2tI} psi psi~.
(4) Parity: for even psi and a C with nonzero even part C_+, the even part of the law forces
    psi C_+ = 0; the left annihilator {psi in Cl^+ : psi C_+ = 0} is computed as an exact kernel for
    four C_+: zero for invertible C_+, and a proper subspace (dimension 4 of 8) whose generic element
    is not invertible otherwise. So invertible even solutions need C_+ = 0.
No premises: the claim has no uses.
"""
from fractions import Fraction as F

import GA

SQ = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]
BL = GA.all_blades(4)
EVEN = [b for b in BL if len(b) % 2 == 0]
ODD = [b for b in BL if len(b) % 2 == 1]


def m(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out


def vec(c):
    return GA.add(*[GA.scal(c[i], E[i]) for i in range(4)]) if any(c) else {}


I4 = m(E[0], E[1], E[2], E[3])
PAIRS = [([1, 2, -1, 3], [2, -1, 1, 1]), ([0, 1, 0, 0], [0, 0, 1, 0]), ([3, 1, 4, 1], [1, 0, -2, 5]),
         ([2, 2, 2, 2], [1, 1, 1, 1]), ([0, 0, 0, 0], [5, 1, 0, 0]), ([1, 0, 0, 0], [0, 0, 0, 0])]
CIRCLE = [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13))]
UNITS = [[0, 0, 0, 1], [1, 1, 1, 0], [2, 2, 0, 1]]
TARGETS = [[0, 0, F(3, 5), F(4, 5)], [1, 1, 1, 0], [2, 2, 0, 1], [0, 1, 0, 0]]
PSI = GA.add(GA.sc(2), GA.scal(F(1, 3), m(E[1], E[2])), GA.scal(F(-1, 2), m(E[0], E[1])), GA.scal(F(1, 5), I4))
CPLUS = [GA.sc(1), GA.add(GA.sc(1), m(E[0], E[3])), GA.add(GA.sc(2), m(E[1], E[2])),
         m(GA.add(GA.sc(1), m(E[0], E[1])), GA.add(GA.sc(2), m(E[1], E[2])))]


def wedge(v, w):
    return GA.scal(F(1, 2), GA.sub(m(v, w), m(w, v)))


def is_scalar(x, val):
    return GA.eq(x, GA.sc(val))


def check_square_of_an_odd_element():
    ok = True
    for vc, wc in PAIRS:
        v, w = vec(vc), vec(wc)
        C = GA.add(v, m(I4, w))
        rhs = GA.add(GA.sc(GA.dot(v, v, SQ) + GA.dot(w, w, SQ)), GA.scal(-2, m(I4, wedge(v, w))))
        ok = ok and GA.eq(m(C, C), rhs)
    # odd part of Cl(1,3) = vectors + I vectors: rank 8
    gens = [E[i] for i in range(4)] + [m(I4, E[i]) for i in range(4)]
    ok = ok and GA.field_rank([[x.get(b, F(0)) for b in ODD] for x in gens]) == 8
    for uc in UNITS:
        u = vec(uc)
        ok = ok and GA.dot(u, u, SQ) == -1
        for c, s in CIRCLE:
            C = m(GA.add(GA.sc(c), GA.scal(s, I4)), u)
            ok = ok and is_scalar(m(C, C), -1)
            # the same element as v + I w with (v, w) = (cos t, sin t) u
            ok = ok and GA.eq(C, GA.add(GA.scal(c, u), m(I4, GA.scal(s, u))))
    # Q(v) + Q(w) = -1 with v ^ w != 0: e1 and (e0 + e2)... Q(e1) = -1, Q(e0 + e2) = 0
    v, w = E[1], GA.add(E[0], E[2])
    C = GA.add(v, m(I4, w))
    ok = ok and GA.dot(v, v, SQ) + GA.dot(w, w, SQ) == -1 and not is_scalar(m(C, C), -1)
    # dependent but off the circle: (2 e3, 0)
    C = GA.scal(2, E[3])
    ok = ok and is_scalar(m(C, C), -4)
    GA.check("(v + Iw)^2 = Q(v) + Q(w) - 2I(v^w); C^2 = -1 exactly on (cos t + sin t I) u", ok)
    return ok


def check_rotors_move_u_over_the_hyperboloid():
    ok = True
    e3 = E[3]
    C0 = m(I4, e3)
    for tc in TARGETS:
        up = vec(tc)
        ok = ok and GA.dot(up, up, SQ) == -1
        R = GA.sub(GA.sc(1), m(up, e3))
        RR = m(R, GA.reverse(R))
        ok = ok and len(RR) == 1 and RR.get((), F(0)) > 0
        ok = ok and all(len(b) % 2 == 0 for b in R)
        ok = ok and GA.eq(m(R, e3, GA.reverse(R)), GA.scal(RR[()], up))
        Cp = m(R, C0, GA.reverse(R))
        ok = ok and GA.eq(m(Cp, Cp), GA.sc(-RR[()] * RR[()]))
    R = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), m(E[0], E[3])))
    Rt = GA.reverse(R)
    ok = ok and is_scalar(m(R, Rt), 1)
    u2 = m(Rt, e3, R)
    ok = ok and is_scalar(m(u2, u2), -1) and u2.get((0,), F(0)) == F(15, 8)
    ok = ok and GA.eq(m(I4, u2), m(Rt, C0, R)) and is_scalar(m(m(I4, u2), m(I4, u2)), -1)
    GA.check("rotors 1 - u' gamma_3 carry gamma_3 to each unit spacelike u'; R~ C R is again a root of -1", ok)
    return ok


def check_chiral_phase():
    ok = True
    ct, st = F(3, 5), F(4, 5)
    ph = GA.add(GA.sc(ct), GA.scal(st, I4))
    ph_inv = GA.add(GA.sc(ct), GA.scal(-st, I4))
    ok = ok and all(GA.anticommutes(I4, {b: F(1)}, SQ) for b in ODD)
    ok = ok and is_scalar(m(ph, ph_inv), 1)
    ph2 = GA.add(GA.sc(F(-7, 25)), GA.scal(F(24, 25), I4))
    ok = ok and GA.eq(m(ph, ph), ph2)
    for C in (m(I4, E[3]), m(E[0], E[2], E[1]), GA.add(E[1], m(I4, E[2]))):
        ok = ok and GA.eq(m(ph_inv, C, ph), m(C, ph2))
    ok = ok and GA.eq(GA.reverse(ph), ph) and not is_scalar(m(ph, GA.reverse(ph)), 1)
    lhs = m(m(PSI, ph), GA.reverse(m(PSI, ph)))
    ok = ok and GA.eq(lhs, m(ph2, PSI, GA.reverse(PSI)))
    GA.check("psi -> psi e^{tI}: C -> C e^{2tI}, not a rotor, Takabayasi angle shifted by 2t", ok)
    return ok


# Weights of the kernel basis vectors in the sample element of the annihilator (any nonzero weights
# give a nonzero element of the kernel); at most four are needed (the kernel has dimension 0 or 4).
KERNEL_WEIGHTS = (1, 2, 3, 4)


def unit_blade(b):
    return {b: F(1)}


def check_even_part_of_c_excludes_invertible_even_solutions():
    ok = True
    dims = []
    for Cp in CPLUS:
        cols = [[m(unit_blade(b), Cp).get(c, F(0)) for c in BL] for b in EVEN]
        M = [[cols[j][i] for j in range(len(EVEN))] for i in range(len(BL))]
        ker = GA.field_kernel(M)
        dims.append(len(ker))
        if ker:
            gen = {}
            for w, kv in zip(KERNEL_WEIGHTS, ker):
                gen = GA.add(gen, GA.scal(F(w), {b: c for b, c in zip(EVEN, kv) if c != 0}))
            ok = ok and not GA.is_zero(gen) and GA.is_zero(m(gen, Cp))
            # Cl(1,3) = Mat(2, H): left multiplication by a nonzero singular element has image of real
            # dimension 8 (quaternionic rank 1), half of 16
            L = [[m(gen, unit_blade(b)).get(c, F(0)) for c in BL] for b in BL]
            ok = ok and GA.field_rank(L) * 2 == len(BL)
    ok = ok and dims == [0, 4, 0, 4]
    # nabla psi is odd for even psi: gamma^mu times an even element is odd
    ok = ok and all(len(b) % 2 == 1 for g in E for b in m(g, PSI))
    GA.check("psi C_+ = 0 on Cl^+ has only singular solutions (kernel 0 or 4 of 8): C must be odd", ok)
    return ok
