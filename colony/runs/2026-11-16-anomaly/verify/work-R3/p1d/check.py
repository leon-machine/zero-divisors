"""The colour angle term under the stored conjugations, and phase symmetries of the covariant rung coupling.

(1) Spacetime algebra Cl(1,3): the grade-four part of a bivector square is the outer square, 2 (E.B) I_4 for
    F = E + I_4 B; reversal and grade involution fix it; an isometry of the vectors acting by outermorphism
    multiplies it by its determinant.
(2) Cl(2,4): I_6 squares to -1 and conjugation by it is the grade involution, so the vector part -1 of the
    stored conjugation fixes every even element; a reflection reverses the six-form and the four-forms that
    contain its direction; reversal fixes grade four and reverses grade six.
(3) The even-subalgebra map of signature reversal, e_mu e_nu -> -e'_mu e'_nu, is an algebra isomorphism of
    Cl+(1,3) onto Cl+(3,1) carrying I_4 to I'_4 and outer squares to outer squares.
(4) The colour form: the trace form on su(3) is invariant under the outer automorphism, an inner one and
    the transposition (an anti-automorphism).
(4') Further stored maps: the duality map F -> I_4 F reverses the four-form and is induced by no vector map;
    the rung boost at I_4-imaginary rapidity moves gamma_0 and fixes every spacetime bivector and I_4; in the
    algebra of the ten Majoranas conjugation by the left-right parity D and by omega keeps the scalar part of
    a product of bivectors, omega fixing every bivector and D moving the colour algebra.
(5) Phase symmetries of sum_k Phi_k Q A_k u + conj(Phi_k) Q B_k d with (A_1, A_2) = (Y, Yt) = (B_2, B_1):
    exact kernels for n = 2, 3. Y and Yt invertible: colour coefficient zero and equal doublet weights.
    Counter-models with a nonzero coefficient: Yt = 0, Yt nilpotent, a family split; each has
    det(a Y + b Yt) = c a^j b^(n-j) and coefficient -(2j - n)(q_1 - q_2).
(6) One family in the five-mode module: the Dirac rows of the stored charge list with independent slot
    charges, then the rows of the coupling to the conjugate vector. The fourth charge goes; the unit of the
    module is kept only by its quarter turn; its colour coefficient 8 gives one whole turn per family.
(7) The scalar sector: the axial phase fixes N, m, |Q|^2 and the sum of squared moment maps, multiplies Q by
    its square, and moves the terms linear in Q; with hypercharge it fixes the cone's family point.
(8) The determinant phase as a function of the field: first-order coefficients of det(M_u) det(M_d) at the
    cone's family point are traces of Yt^-1 Y and Y^-1 Yt; on the lift locus a monomial determinant makes the
    product of the masses |c|^2 H^(2n).
"""
from fractions import Fraction as F
from itertools import combinations, permutations

import GA
from GA import QI
from tp_premise import premise

S13 = GA.sig(1, 3)
S31 = tuple(-s for s in S13)      # the reversed signature on the same generators: squares (-1, 1, 1, 1)
S24 = GA.sig(2, 4)
UNIT = QI(0, 1)


# ---------------------------------------------------------------------------------------------------------
# Clifford helpers
# ---------------------------------------------------------------------------------------------------------
def grade(x, g):
    return {b: c for b, c in x.items() if len(b) == g}


def blade(idx):
    return {tuple(idx): F(1)}


def bivector(coeffs, n=4):
    out = {}
    for (i, j), c in zip(combinations(range(n), 2), coeffs):
        if c:
            out[(i, j)] = F(c)
    return out


def outermorphism(x, images, squares):
    """Extend a linear map of the generators (images[i] the image of e_i) to the algebra by the outer product,
    computed as the antisymmetrised geometric product."""
    out = {}
    for b, c in x.items():
        k = len(b)
        if k == 0:
            out = GA.add(out, {(): c})
            continue
        acc = {}
        count = 0
        for perm in permutations(range(k)):
            sign = 1
            for a in range(k):
                for d in range(a + 1, k):
                    if perm[a] > perm[d]:
                        sign = -sign
            term = GA.sc(1)
            for a in perm:
                term = GA.mul(term, images[b[a]], squares)
            acc = GA.add(acc, GA.scal(sign, term))
            count += 1
        out = GA.add(out, GA.scal(c * F(1, count), acc))
    return out


F1 = bivector([2, -1, 3, 5, 1, -4])
F2 = bivector([1, 4, -2, 0, 3, 7])
I4 = blade((0, 1, 2, 3))


def four_form(x, y, squares):
    """Grade-four part of the symmetrised product of two bivectors."""
    return grade(GA.scal(F(1, 2), GA.add(GA.mul(x, y, squares), GA.mul(y, x, squares))), 4)


def check_four_form_of_a_field_square_in_the_spacetime_algebra():
    premise("synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation")
    ok = GA.mul(I4, I4, S13) == GA.sc(-1)
    # F = E + I_4 B with E = sum E_i e_i e_0, B = sum B_i e_i e_0 (relative vectors)
    E, B = (2, -3, 5), (7, 1, -4)
    rel = [GA.mul(GA.gen(i), GA.gen(0), S13) for i in (1, 2, 3)]
    Ev = GA.add(*[GA.scal(c, r) for c, r in zip(E, rel)])
    Bv = GA.add(*[GA.scal(c, r) for c, r in zip(B, rel)])
    Fd = GA.add(Ev, GA.mul(I4, Bv, S13))
    edotb = sum(a * b for a, b in zip(E, B))
    sq = GA.mul(Fd, Fd, S13)
    ok = ok and edotb == -9 and grade(sq, 4) == GA.scal(2 * edotb, I4)
    ok = ok and grade(sq, 0) == GA.sc(sum(a * a for a in E) - sum(b * b for b in B)) and grade(sq, 2) == {}
    ok = ok and GA.mul(I4, grade(sq, 4), S13) == GA.sc(-2 * edotb)
    # reversal and grade involution fix the four-form of a square
    for X, Y in ((F1, F1), (F1, F2), (Fd, F2)):
        t = four_form(X, Y, S13)
        ok = ok and t != {} and GA.reverse(t) == t and GA.grade_inv(t) == t
        ok = ok and four_form(GA.reverse(X), GA.reverse(Y), S13) == t
    # isometries of the vectors: a reflection (det -1), the total inversion (det +1), a boost and a rotation
    refl = [GA.gen(0), GA.scal(-1, GA.gen(1)), GA.gen(2), GA.gen(3)]
    minus = [GA.scal(-1, GA.gen(i)) for i in range(4)]
    time_rev = [GA.scal(-1, GA.gen(0)), GA.gen(1), GA.gen(2), GA.gen(3)]
    boost = [GA.add(GA.scal(F(5, 3), GA.gen(0)), GA.scal(F(4, 3), GA.gen(1))),
             GA.add(GA.scal(F(4, 3), GA.gen(0)), GA.scal(F(5, 3), GA.gen(1))), GA.gen(2), GA.gen(3)]
    rot = [GA.gen(0), GA.gen(1), GA.add(GA.scal(F(3, 5), GA.gen(2)), GA.scal(F(4, 5), GA.gen(3))),
           GA.add(GA.scal(F(-4, 5), GA.gen(2)), GA.scal(F(3, 5), GA.gen(3)))]
    t0 = four_form(F1, F2, S13)
    for images, det in ((refl, -1), (minus, 1), (time_rev, -1), (boost, 1), (rot, 1)):
        isometry = all(GA.mul(images[i], images[i], S13) == GA.sc(S13[i]) for i in range(4))
        isometry = isometry and all(GA.anticommutes(images[i], images[j], S13)
                                    for i in range(4) for j in range(i + 1, 4))
        g1, g2 = outermorphism(F1, images, S13), outermorphism(F2, images, S13)
        ok = ok and isometry and outermorphism(I4, images, S13) == GA.scal(det, I4)
        ok = ok and four_form(g1, g2, S13) == GA.scal(det, t0)
    # the duality map F -> I_4 F: bivectors to bivectors, reverses the four-form, and is no outermorphism:
    # it does not preserve the scalar part <F1 F2>_0, which every isometry does
    d1, d2 = GA.mul(I4, F1, S13), GA.mul(I4, F2, S13)
    ok = ok and all(len(b) == 2 for b in d1) and all(len(b) == 2 for b in d2)
    ok = ok and four_form(d1, d2, S13) == GA.scal(-1, t0) and t0 == GA.scal(-1, I4)
    s0 = grade(GA.mul(F1, F2, S13), 0)
    ok = ok and s0 == GA.sc(17) and grade(GA.mul(d1, d2, S13), 0) == GA.scal(-1, s0)
    for images, det in ((refl, -1), (minus, 1), (time_rev, -1), (boost, 1), (rot, 1)):
        g1, g2 = outermorphism(F1, images, S13), outermorphism(F2, images, S13)
        ok = ok and grade(GA.mul(g1, g2, S13), 0) == s0
    GA.check("Cl(1,3): <F^2>_4 = 2 (E.B) I_4; reversal fixes it; an isometry multiplies it by its determinant", ok)
    return ok


def check_stored_conjugation_fixes_even_elements_and_reflections_reverse_the_six_form():
    premise("synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation")
    I6 = blade(range(6))
    I6inv = GA.scal(-1, I6)
    ok = GA.mul(I6, I6, S24) == GA.sc(-1) and GA.mul(I6, GA.reverse(I6), S24) == GA.sc(1)
    factors = [blade((0, 1)), blade((2, 3)), blade((4, 5))]
    prod = GA.mul(GA.mul(factors[0], factors[1], S24), factors[2], S24)
    ok = ok and prod == I6 and all(GA.mul(f, f, S24) == GA.sc(-1) for f in factors)
    ad = lambda x: GA.mul(GA.mul(I6, x, S24), I6inv, S24)
    ok = ok and all(ad(GA.gen(i)) == GA.scal(-1, GA.gen(i)) for i in range(6))
    biv = bivector([1, -2, 3, 4, -5, 6, 7, 8, -9, 10, 11, -12, 13, 14, 15], 6)
    biv2 = bivector([3, 1, -4, 1, 5, -9, 2, 6, -5, 3, 5, 8, -9, 7, 9], 6)
    t = four_form(biv, biv2, S24)
    ok = ok and len(t) == 15 and ad(biv) == biv and ad(t) == t and ad(I6) == I6
    ok = ok and GA.reverse(t) == t and GA.reverse(I6) == GA.scal(-1, I6)
    # the other convention of the stored clause (5): the composite phi = reversal after C applied to the whole
    # Clifford integrand. On the product of two bivectors it gives the product in the other order, so the
    # symmetrised grade-four part is fixed, while the six-form changes sign.
    phi = lambda x: ad(x)
    prod12, prod21 = GA.mul(biv, biv2, S24), GA.mul(biv2, biv, S24)
    ok = ok and phi(prod12) == prod21 and grade(prod12, 2) == GA.scal(-1, grade(prod21, 2)) != {}
    ok = ok and grade(phi(prod12), 4) == grade(prod12, 4)
    ok = ok and GA.scal(F(1, 2), GA.add(grade(phi(prod12), 4), grade(phi(prod21), 4))) == t
    ok = ok and phi(I6) == GA.scal(-1, I6)
    # a reflection in e_5: determinant -1; it reverses I_6 and the four-forms containing e_5, keeps the others
    refl = [GA.gen(i) for i in range(5)] + [GA.scal(-1, GA.gen(5))]
    ok = ok and outermorphism(I6, refl, S24) == GA.scal(-1, I6)
    with5 = {b: c for b, c in t.items() if 5 in b}
    without5 = {b: c for b, c in t.items() if 5 not in b}
    ok = ok and with5 != {} and without5 != {}
    ok = ok and outermorphism(t, refl, S24) == GA.add(without5, GA.scal(-1, with5))
    # three reflections (the Witt exchange of the stored clause) reverse I_6 as well
    refl3 = [GA.gen(0), GA.scal(-1, GA.gen(1)), GA.gen(2), GA.scal(-1, GA.gen(3)), GA.gen(4),
             GA.scal(-1, GA.gen(5))]
    ok = ok and outermorphism(I6, refl3, S24) == GA.scal(-1, I6)
    GA.check("Cl(2,4): Ad(I_6) is the grade involution and fixes even elements; reflections reverse I_6", ok)
    return ok


def check_signature_reversal_carries_the_four_form_with_its_sign():
    premise("synthesis.tower-top-pair-forgets-reversal")
    pairs = list(combinations(range(4), 2))

    def sigma(x):
        """Cl+(1,3) -> Cl+(3,1): scalar to scalar, e_i e_j to -e'_i e'_j, I_4 to I'_4."""
        out = {}
        for b, c in x.items():
            out[b] = -c if len(b) == 2 else c
        return {b: c for b, c in out.items() if c != 0}

    ok = True
    basis = [GA.sc(1)] + [blade(p) for p in pairs] + [I4]
    for x in basis:
        for y in basis:
            ok = ok and sigma(GA.mul(x, y, S13)) == GA.mul(sigma(x), sigma(y), S31)
    ok = ok and GA.mul(I4, I4, S31) == GA.sc(-1) and sigma(I4) == I4
    # the unsigned identification of bivectors is not multiplicative
    ident_fails = any(GA.mul(blade(p), blade(q), S13) != GA.mul(blade(p), blade(q), S31)
                      for p in pairs for q in pairs)
    t13 = four_form(F1, F2, S13)
    ok = ok and ident_fails and four_form(sigma(F1), sigma(F2), S31) == t13
    ok = ok and four_form(F1, F2, S31) == t13 and t13 == GA.scal(F(-1), I4)
    # a second isomorphism: sigma after conjugation by gamma_0, which reverses I_4
    g0 = GA.gen(0)
    ad0 = lambda x: GA.mul(GA.mul(g0, x, S13), g0, S13)          # gamma_0^2 = 1
    tau = lambda x: sigma(ad0(x))
    for x in basis:
        for y in basis:
            ok = ok and tau(GA.mul(x, y, S13)) == GA.mul(tau(x), tau(y), S31)
    ok = ok and tau(I4) == GA.scal(-1, I4)
    ok = ok and four_form(tau(F1), tau(F2), S31) == GA.scal(-1, t13)
    GA.check("signature reversal: e_i e_j -> -e'_i e'_j is an isomorphism of even algebras, I_4 -> I'_4", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# Matrices over span{1, I_4} (Gaussian rationals)
# ---------------------------------------------------------------------------------------------------------
def zeros(r, c):
    return [[QI(0) for _ in range(c)] for _ in range(r)]


def qm(rows):
    return [[x if isinstance(x, QI) else QI(F(x)) for x in r] for r in rows]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def madd(A, B):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(A, B)]


def mscal(c, A):
    return [[c * x for x in r] for r in A]


def mT(A):
    return [list(r) for r in zip(*A)]


def mconj(A):
    return [[x.conj() for x in r] for r in A]


def mtr(A):
    return sum((A[i][i] for i in range(len(A))), QI(0))


def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    total = QI(0)
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in A[1:]]
        total = total + (QI(-1) if j % 2 else QI(1)) * A[0][j] * det(minor)
    return total


def minv(A):
    n = len(A)
    d = det(A)
    cof = zeros(n, n)
    for i in range(n):
        for j in range(n):
            minor = [row[:j] + row[j + 1:] for k, row in enumerate(A) if k != i]
            sign = QI(-1) if (i + j) % 2 else QI(1)
            cof[j][i] = sign * (det(minor) if n > 1 else QI(1)) / d
    return cof


def anti_hermitian_basis(n):
    out = []
    for a in range(n):
        M = zeros(n, n)
        M[a][a] = UNIT
        out.append(M)
    for a in range(n):
        for b in range(a + 1, n):
            M = zeros(n, n)
            M[a][b], M[b][a] = QI(1), QI(-1)
            out.append(M)
            M = zeros(n, n)
            M[a][b], M[b][a] = UNIT, UNIT
            out.append(M)
    return out


def check_colour_form_is_invariant_under_automorphisms():
    basis = [B for B in anti_hermitian_basis(3)]
    # traceless: replace the three diagonal generators by two
    d1, d2 = zeros(3, 3), zeros(3, 3)
    d1[0][0], d1[1][1] = UNIT, QI(0, -1)
    d2[1][1], d2[2][2] = UNIT, QI(0, -1)
    basis = [d1, d2] + basis[3:]
    form = lambda X, Y: mtr(mm(X, Y))
    gram = [[form(X, Y) for Y in basis] for X in basis]
    ok = len(basis) == 8 and all(g.im == 0 for row in gram for g in row)
    ok = ok and GA.field_rank([[g.re for g in row] for row in gram]) == 8
    ok = ok and all(gram[i][i].re < 0 for i in range(8))
    outer = lambda X: mconj(X)          # X -> conj X = -X^T on anti-Hermitian X: the outer automorphism
    P = qm([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    inner = lambda X: mm(mm(P, X), mT(P))
    comm = lambda X, Y: madd(mm(X, Y), mscal(QI(-1), mm(Y, X)))
    for tau in (outer, inner):
        ok = ok and all(form(tau(X), tau(Y)) == form(X, Y) for X in basis for Y in basis)
        ok = ok and all(tau(comm(X, Y)) == comm(tau(X), tau(Y)) for X in basis for Y in basis)
    ok = ok and any(outer(X) != X for X in basis)
    # an anti-automorphism: transposition reverses brackets and keeps the form
    ok = ok and all(form(mT(X), mT(Y)) == form(X, Y) for X in basis for Y in basis)
    ok = ok and all(mT(comm(X, Y)) == comm(mT(Y), mT(X)) for X in basis for Y in basis)
    ok = ok and any(mT(comm(X, Y)) != comm(mT(X), mT(Y)) for X in basis for Y in basis)
    GA.check("su(3): the trace form is real, definite, invariant under automorphisms and an anti-automorphism", ok)
    return ok


def check_further_stored_maps_fix_the_four_form():
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("standard-model.left-right-parity-what-breaks-it")
    premise("synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element")
    # spacetime with two rung planes: generators 0..3 spacetime, (4, 5) and (6, 7) hyperbolic planes
    sq = (1, -1, -1, -1, 1, -1, 1, -1)
    i4 = blade((0, 1, 2, 3))
    b4, b5 = blade((4, 5)), blade((6, 7))
    ok = GA.mul(b4, b4, sq) == GA.sc(1) and GA.mul(b5, b5, sq) == GA.sc(1)
    c, sn = F(-7, 25), F(24, 25)
    rot = lambda b, sign: GA.add(GA.sc(c), GA.scal(sign * sn, GA.mul(i4, b, sq)))
    R = GA.mul(rot(b4, 1), rot(b5, 1), sq)
    Rinv = GA.mul(rot(b5, -1), rot(b4, -1), sq)
    ok = ok and c * c + sn * sn == 1 and GA.mul(R, Rinv, sq) == GA.sc(1)
    ad = lambda x: GA.mul(GA.mul(R, x, sq), Rinv, sq)
    ok = ok and ad(GA.gen(0)) != GA.gen(0)
    ok = ok and all(ad(blade(pq)) == blade(pq) for pq in combinations(range(4), 2)) and ad(i4) == i4
    ok = ok and ad(F1) == F1 and four_form(ad(F1), ad(F2), sq) == four_form(F1, F2, sq)
    # it turns the rung null vectors by opposite phases: (e_4 + e_5) -> (cos 2phi + sin 2phi I_4)(e_4 + e_5)
    v = GA.add(GA.gen(4), GA.gen(5))
    c2, s2 = c * c - sn * sn, 2 * c * sn
    ok = ok and ad(v) in (GA.add(GA.scal(c2, v), GA.scal(s2, GA.mul(i4, v, sq))),
                          GA.add(GA.scal(c2, v), GA.scal(-s2, GA.mul(i4, v, sq))))
    # the ten Majoranas: omega fixes every bivector; D = gamma_5 gamma_9 (indices 5, 9 of 0..9, one pair and one
    # slot Majorana) is a rotor; both keep the scalar part of a product of bivectors; D moves a colour bivector
    s10 = GA.sig(10, 0)
    w = blade(range(10))
    winv = GA.scal(-1, w)
    D = blade((5, 9))
    Dinv = GA.scal(-1, D)
    ok = ok and GA.mul(w, winv, s10) == GA.sc(1) and GA.mul(D, Dinv, s10) == GA.sc(1)
    X = GA.add(blade((0, 5)), GA.scal(2, blade((1, 4))), GA.scal(-3, blade((2, 3))))
    Y = GA.add(GA.scal(5, blade((0, 5))), blade((2, 3)), GA.scal(7, blade((4, 5))))
    adw = lambda x: GA.mul(GA.mul(w, x, s10), winv, s10)
    adD = lambda x: GA.mul(GA.mul(D, x, s10), Dinv, s10)
    sc0 = grade(GA.mul(X, Y, s10), 0)
    ok = ok and sc0 == GA.sc(-2) and adw(X) == X and adw(Y) == Y
    ok = ok and adD(X) != X and grade(GA.mul(adD(X), adD(Y), s10), 0) == sc0
    ok = ok and adD(GA.gen(5)) == GA.scal(-1, GA.gen(5)) and adD(GA.gen(9)) == GA.scal(-1, GA.gen(9))
    GA.check("further stored maps: imaginary rung boost, omega and D fix the four-form or the trace form", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# Phase symmetries of the covariant coupling, n families
# ---------------------------------------------------------------------------------------------------------
def symmetry_system(Y, Yt):
    """Unknowns: anti-Hermitian K_Q, K_u, K_d (n x n) and K_Phi (2 x 2). Up term sum_k Phi_k Q^T A_k u with
    A = (Y, Yt); down term sum_k conj(Phi_k) Q^T B_k d with B = (Yt, Y); Phi = (alpha, conj beta).
    Returns the solution space, the colour coefficient (2 tr K_Q + tr K_u + tr K_d) / I_4 and q_1 - q_2."""
    n = len(Y)
    bn, b2 = anti_hermitian_basis(n), anti_hermitian_basis(2)
    A, B = (Y, Yt), (Yt, Y)
    cols = []
    for s in range(3):
        for K in bn:
            col = []
            for j in range(2):
                up, dn = zeros(n, n), zeros(n, n)
                if s == 0:
                    up, dn = mm(mT(K), A[j]), mm(mT(K), B[j])
                if s == 1:
                    up = mm(A[j], K)
                if s == 2:
                    dn = mm(B[j], K)
                col += [up, dn]
            cols.append(col)
    for K in b2:
        col = []
        for j in range(2):
            up, dn = zeros(n, n), zeros(n, n)
            for k in range(2):
                up = madd(up, mscal(K[k][j], A[k]))
                dn = madd(dn, mscal(K[k][j].conj(), B[k]))
            col += [up, dn]
        cols.append(col)
    rows = []
    for blk in range(4):
        for i in range(n):
            for j in range(n):
                rows.append([c[blk][i][j].re for c in cols])
                rows.append([c[blk][i][j].im for c in cols])
    coef = [(2 if s == 0 else 1) * mtr(K).im for s in range(3) for K in bn] + [F(0)] * len(b2)
    dq = [F(0)] * (3 * len(bn)) + [(K[0][0] - K[1][1]).im for K in b2]
    ker = GA.field_kernel([[F(x) for x in r] for r in rows])
    dot = lambda f, v: sum(a * b for a, b in zip(f, v))
    return ker, [dot(coef, v) for v in ker], [dot(dq, v) for v in ker]


def binary_form(Y, Yt):
    """Coefficients p_j of a^j b^(n-j) in det(a Y + b Yt), by exact interpolation at b = 1."""
    n = len(Y)
    pts = [QI(F(t)) for t in range(n + 1)]
    vals = [det(madd(mscal(t, Y), Yt)) for t in pts]
    rows = []
    for t in pts:
        row, acc = [], QI(1)
        for _ in range(n + 1):
            row.append(acc)
            acc = acc * t
        rows.append(row)
    return GA.field_solve(rows, vals)


Y3 = qm([[2, QI(1, 1), 0], [QI(1, 1), 3, QI(0, 2)], [0, QI(0, 2), 5]])
YT3 = qm([[1, 0, QI(2, -1)], [0, QI(0, 3), 1], [QI(2, -1), 1, 7]])
Y2 = qm([[3, QI(1, -2)], [QI(1, -2), QI(0, 1)]])
YT2 = qm([[QI(1, 1), 4], [4, -2]])
N3 = qm([[2, 1, 0], [0, 1, QI(0, 3)], [1, 0, 4]])          # not symmetric
NT3 = qm([[1, QI(0, 1), 2], [3, 1, 0], [0, 5, QI(1, 1)]])


def check_invertible_pair_admits_no_phase_symmetry_with_a_colour_coefficient():
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    ok = True
    for Y, Yt, dim in ((Y3, YT3, 2), (Y2, YT2, 2), (N3, NT3, 2)):
        ok = ok and det(Y) != 0 and det(Yt) != 0
        ker, col, dq = symmetry_system(Y, Yt)
        ok = ok and len(ker) == dim and all(c == 0 for c in col) and all(d == 0 for d in dq)
        p = binary_form(Y, Yt)
        ok = ok and p[0] == det(Yt) and p[-1] == det(Y)
    ok = ok and mT(Y3) == Y3 and mT(YT3) == YT3 and mT(N3) != N3
    ok = ok and [det(M) for M in (Y3, YT3, Y2, YT2, N3, NT3)] == [QI(38, -10), QI(-13, 12), QI(3, 7), QI(-18, -2),
                                                                  QI(8, 3), QI(34, -2)]
    ok = ok and binary_form(Y3, YT3) == [QI(-13, 12), QI(16, 67), QI(57, 20), QI(38, -10)]
    ok = ok and binary_form(Y2, YT2) == [QI(-18, -2), QI(-15, 17), QI(3, 7)]
    ok = ok and binary_form(N3, NT3) == [QI(34, -2), QI(2, -27), QI(-3, -28), QI(8, 3)]
    # one matrix up to a number, and a singular second matrix whose form is not a monomial: still zero
    for Y, Yt in ((Y3, Y3), (Y3, mscal(QI(2), Y3)), (Y3, mscal(UNIT, Y3)),
                  (qm([[1, 0, 0], [0, 2, 0], [0, 0, 3]]), qm([[1, 0, 0], [0, 1, 0], [0, 0, 0]]))):
        ker, col, dq = symmetry_system(Y, Yt)
        ok = ok and all(c == 0 for c in col)
    GA.check("covariant coupling, Y and Y-tilde invertible: every phase symmetry has colour coefficient 0", ok)
    return ok


def check_counter_models_with_a_colour_coefficient_have_monomial_determinant():
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them")
    one2, one3 = qm([[1, 0], [0, 1]]), qm([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    models = [
        (Y3, zeros(3, 3), 3, 3),
        (one2, qm([[0, 1], [0, 0]]), 2, 2),
        (one3, qm([[0, 1, 0], [0, 0, 1], [0, 0, 0]]), 3, 3),
        (qm([[1, 0, 0], [0, 1, 0], [0, 0, 0]]), qm([[0, 0, 0], [0, 0, 0], [0, 0, 1]]), 3, 2),
        (qm([[0, 0, 0], [0, 0, 0], [0, 0, 1]]), qm([[1, 0, 0], [0, 1, 0], [0, 0, 0]]), 3, 1),
    ]
    ok = True
    for Y, Yt, n, j in models:
        ker, col, dq = symmetry_system(Y, Yt)
        p = binary_form(Y, Yt)
        monomial = [k for k in range(n + 1) if p[k] != 0] == [j]
        ok = ok and monomial and any(c != 0 for c in col)
        ok = ok and all(c == -(2 * j - n) * d for c, d in zip(col, dq))
    GA.check("counter-models: nonzero colour coefficient -(2j - n)(q_1 - q_2), det(aY + bY~) = c a^j b^(n-j)", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# One family in the five-mode module
# ---------------------------------------------------------------------------------------------------------
MODES = (1, 2, 3, 4, 5)
PAIR, SLOT = (1, 2, 3), (4, 5)
EVEN = [frozenset(c) for r in (0, 2, 4) for c in combinations(MODES, r)]
SPECIES = ["Q", "u^c", "d^c", "L", "e^c", "nu^c"]
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}


def jk(S):
    return len(S & set(SLOT)), len(S & set(PAIR))


def sp(S):
    return SPECIES.index(NAMES[jk(S)])


def word(ops, st):
    for kind, i in reversed(ops):
        out = {}
        for S, a in st.items():
            if kind == "v" and i not in S:
                T = S | {i}
            elif kind == "w" and i in S:
                T = S - {i}
            else:
                continue
            sign = -1 if sum(1 for j in S if j < i) % 2 else 1
            out[T] = out.get(T, 0) + sign * a
        st = out
    return {k: v for k, v in st.items() if v != 0}


def pairing(S, U):
    if U != frozenset(MODES) - S:
        return 0
    lst = sorted(S) + sorted(U)
    inv = sum(1 for a in range(5) for b in range(a + 1, 5) if lst[a] > lst[b])
    return (-1) ** (len(S) * (len(S) - 1) // 2) * (-1) ** inv


def slot_rows(conjugate):
    """Conservation rows of B(psi, a phi) x (coefficient): columns six species, then the charges of the
    coefficients alpha (of v) and beta (of w). With conjugate, v carries conj(beta) and w carries conj(alpha)."""
    rows = set()
    for kind in ("v", "w"):
        for i in SLOT:
            for T in EVEN:
                for U, c in word([(kind, i)], {T: F(1)}).items():
                    for S in EVEN:
                        if pairing(S, U) * c != 0:
                            r = [0] * 8
                            r[sp(S)] += 1
                            r[sp(T)] += 1
                            if conjugate:
                                r[7 if kind == "v" else 6] -= 1
                            else:
                                r[6 if kind == "v" else 7] += 1
                            rows.add(tuple(r))
    return [list(r) for r in sorted(rows)]


def check_conjugate_coupling_removes_the_fourth_charge_and_keeps_a_quarter_turn_of_the_unit():
    premise("synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them")
    premise("synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element")
    premise("standard-model.invariant-pairing-five-modes")
    D, Dc = slot_rows(False), slot_rows(True)
    kernel = lambda rows: GA.field_kernel([[F(x) for x in r] for r in rows])
    a3 = [F(0)] * 8
    for S in EVEN:
        a3[sp(S)] += ((1 in S) - (2 in S)) ** 2
    dot = lambda r, v: sum(x * y for x, y in zip(r, v))
    ok = len(D) == 4 and len(Dc) == 4 and a3[:6] == [4, 2, 2, 0, 0, 0]
    k_one, k_both = kernel(D), kernel(D + Dc)
    ok = ok and len(k_one) == 4 and len(k_both) == 3
    ok = ok and any(dot(a3, v) != 0 for v in k_one) and all(dot(a3, v) == 0 for v in k_both)
    ok = ok and all(v[6] + v[7] == 0 for v in k_both)
    ok = ok and all(dot(a3, v) == -2 * (v[6] + v[7]) for v in k_one)
    # the unit of the module with slot charges -2: conserved by the coupling to c, charge 4 on the coupling to c*
    unit = [F(1)] * 6 + [F(-2), F(-2)]
    ok = ok and all(dot(r, unit) == 0 for r in D) and all(dot(r, unit) == 4 for r in Dc)
    ok = ok and dot(a3, unit) == 8
    # group elements exp(phi unit), phi = (turn) t: kept by both couplings exactly when 4 t is whole
    kept = [t for t in (F(k, 8) for k in range(8)) if all((dot(r, unit) * t).denominator == 1 for r in D + Dc)]
    ok = ok and kept == [F(0), F(1, 4), F(1, 2), F(3, 4)]
    # the quarter turn acts by the unit on the sixteen (weight 1) and by -1 on the slot coefficients (weight -2);
    # its shift of the angle is (A_3 / 2) x (1/4 turn) = one whole turn per family
    ok = ok and (F(-2) * F(1, 4)) == F(-1, 2) and (dot(a3, unit) / 2) * F(1, 4) == 1
    GA.check("one family: the conjugate coupling leaves span{Y, n_B, n_L}; the unit survives as its quarter turn", ok)
    return ok


# ---------------------------------------------------------------------------------------------------------
# The scalar sector and the field-dependent determinant phase
# ---------------------------------------------------------------------------------------------------------
def invariants(al, be):
    Q = al[0] * be[0] + al[1] * be[1]
    na = sum((x * x.conj() for x in al), QI(0)).re
    nb = sum((x * x.conj() for x in be), QI(0)).re
    return Q, (na + nb) / 2, (na - nb) / 2


def moment_squares(al, be):
    """Sum of the squared moment maps of the three weak generators for the stored Hermitian form: the generators
    act as (I_4/2) sigma_j on alpha and as minus the transpose on beta, so with a = alpha, b = conj(beta) the
    three maps are (a^+ sigma_j a - b^+ sigma_j b)/4."""
    a, b = al, [x.conj() for x in be]
    s3 = (a[0].conj() * a[0] - a[1].conj() * a[1] - b[0].conj() * b[0] + b[1].conj() * b[1]).re
    s = a[0].conj() * a[1] - b[0].conj() * b[1]
    return (s3 * s3 + 4 * (s * s.conj()).re) / 16


def check_axial_phase_is_a_symmetry_of_the_stored_potential_and_unbroken_on_the_cone():
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    u = QI(F(3, 5), F(4, 5))
    ok = u * u.conj() == QI(1) and u * u != QI(1)
    al, be = [QI(2, 1), QI(-1, 3)], [QI(1, -2), QI(4, 1)]
    Q, N, m = invariants(al, be)
    Q2, N2, m2 = invariants([u * x for x in al], [u * x for x in be])
    ok = ok and Q != 0 and (N2, m2) == (N, m) and Q2 == u * u * Q and Q2 != Q
    ok = ok and (Q, N, m) == (QI(-3, 8), F(37, 2), F(-7, 2)) and moment_squares(al, be) == F(1077, 16)
    ok = ok and u * u == QI(F(-7, 25), F(24, 25)) and Q2 == QI(F(-171, 25), F(-128, 25))
    ok = ok and (Q2 * Q2.conj()) == (Q * Q.conj())
    ok = ok and moment_squares(al, be) == (N * N - (Q * Q.conj()).re) / 4
    ok = ok and moment_squares([u * x for x in al], [u * x for x in be]) == moment_squares(al, be)
    ok = ok and Q2.re != Q.re and (Q2 * Q2).re != (Q * Q).re
    # hypercharge: alpha by u, beta by conj u; Q fixed
    Q3, N3_, m3 = invariants([u * x for x in al], [u.conj() * x for x in be])
    ok = ok and (Q3, N3_, m3) == (Q, N, m)
    # the family point of the cone: alpha = 0, beta = (-lambda, 0); axial times inverse hypercharge fixes beta
    lam = F(7)
    be0 = [QI(-lam), QI(0)]
    fixed = [u * u.conj() * x for x in be0] == be0
    al_dir = [QI(1), QI(0)]
    moved = [u * u * x for x in al_dir] != al_dir
    Q0, N0, m0 = invariants([QI(0), QI(0)], be0)
    ok = ok and fixed and moved and Q0 == 0 and N0 == lam * lam / 2 and m0 == -lam * lam / 2
    # first-order change of Q along alpha_1: the two directions of the normal pair, exchanged by the phase
    dQ = lambda da: invariants([da, QI(0)], be0)[0]
    ok = ok and dQ(QI(1)) == QI(-lam) and dQ(UNIT) == QI(0, -lam) and dQ(u * u) == u * u * dQ(QI(1))
    # on the lift locus Q = -H^2 the constraint is moved by the phase
    H2 = F(3)
    alL, beL = [QI(H2 / lam), QI(0)], be0
    QL = invariants(alL, beL)[0]
    ok = ok and QL == QI(-H2) and invariants([u * x for x in alL], [u * x for x in beL])[0] != QL
    GA.check("axial phase: fixes N, m, |Q|, the D-term; turns Q by its square; unbroken at the cone's family point", ok)
    return ok


def check_determinant_phase_of_the_normal_pair_and_mass_product_of_a_monomial():
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.rung-field-on-the-lift-locus")
    lam = QI(F(7))
    be = QI(0) - lam
    Mu = lambda a, b: madd(mscal(a, Y3), mscal(b.conj(), YT3))
    Md = lambda a, b: madd(mscal(b, Y3), mscal(a.conj(), YT3))
    ok = True
    # at alpha = 0: det M_d = beta^n det Y, det M_u = conj(beta)^n det Yt
    ok = ok and det(Md(QI(0), be)) == be * be * be * det(Y3)
    ok = ok and det(Mu(QI(0), be)) == be.conj() * be.conj() * be.conj() * det(YT3)
    # first-order coefficients in alpha and conj(alpha): exact polynomial coefficients by differences
    p = binary_form(Y3, YT3)                       # det(a Y + b Yt) = sum p_j a^j b^(3-j)
    # det M_u(alpha) = p(alpha, conj beta): coefficient of alpha is p_1 conj(beta)^2
    # det M_d(alpha) = p(beta, conj alpha): coefficient of conj(alpha) is p_2 beta^2
    ok = ok and p[1] == det(YT3) * mtr(mm(minv(YT3), Y3)) and p[2] == det(Y3) * mtr(mm(minv(Y3), YT3))
    eps = QI(F(1, 1000))
    du = det(Mu(eps, be)) - det(Mu(QI(0), be))
    exact = p[1] * eps * be.conj() * be.conj() + p[2] * eps * eps * be.conj() + p[3] * eps * eps * eps
    ok = ok and du == exact
    # logarithmic derivatives at the family point
    ok = ok and p[1] * be.conj() * be.conj() / det(Mu(QI(0), be)) == mtr(mm(minv(YT3), Y3)) / be.conj()
    ok = ok and p[2] * be * be / det(Md(QI(0), be)) == mtr(mm(minv(Y3), YT3)) / be
    # a monomial determinant on the lift locus alpha beta = -H^2: product of the masses is |c|^2 H^(2n)
    H2 = F(3)
    al = QI(-H2) / be
    Ys, Yts = qm([[1, 0, 0], [0, 1, 0], [0, 0, 0]]), qm([[0, 0, 0], [0, 0, 0], [0, 0, 2]])
    Mu_s = madd(mscal(al, Ys), mscal(be.conj(), Yts))
    Md_s = madd(mscal(be, Ys), mscal(al.conj(), Yts))
    prod = det(Mu_s) * det(Md_s)
    c = binary_form(Ys, Yts)[2]
    ok = ok and c == QI(2) and (prod * prod.conj()).re == ((c * c.conj()).re * H2 ** 3) ** 2
    ok = ok and det(Mu(al, be)) == QI(F(1620574, 343), F(-938277, 343))
    ok = ok and det(Md(al, be)) == QI(F(-4067498, 343), F(1291327, 343))
    ok = ok and mtr(mm(minv(YT3), Y3)) == QI(F(596, 313), F(-1063, 313))
    ok = ok and mtr(mm(minv(Y3), YT3)) == QI(F(983, 772), F(665, 772))
    GA.check("normal pair: d log det at the family point is tr(Y~^-1 Y)/conj(beta), tr(Y^-1 Y~)/beta", ok)
    return ok
