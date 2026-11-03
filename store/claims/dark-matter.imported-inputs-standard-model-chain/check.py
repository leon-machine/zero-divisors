"""dark-matter.imported-inputs-standard-model-chain: exact checks of the computable inputs in the list.

The statement is a provenance list (the data the Standard-Model chain uses, carried as a hypothesis); the
claim that nothing else is used, the tractor bundle (h), the two-kinds-of-action fact (i), the one-loop
remark (j), the Segre lemma and Hypothesis (S) are not computable here. Checked:
(a, c) In Cl(2, 4) (GA, signature (+, +, -, -, -, -)): the even subalgebra is Cl(2, 3) (the elements
    e_i e_5, i < 5, satisfy the Cl(2, 3) relations and their products span all 32 even blades); the unit
    I6 = e_0 ... e_5 has I6^2 = -1 and the centre of Cl^0(2, 4) is span(1, I6) (blade-wise), so Cl^0 is
    complex over I6; for the self-reverse even primitive idempotent f = (1 + e0e1e2e3)(1 + e0e1e4e5)/4 the
    ideal Cl^0 f has real dimension 8 and f Cl^0 f = span(f, I6 f) (dimension 2, (I6 f)^2 = -f): C^4 over
    C, so Cl^0(2, 4) = Mat(4, C) (dimension 32 = 2 x 16).
(c, helicity) The form psi~ phi (reversion) on Cl^0 f is nonzero, Hermitian (the reverse of the Gram matrix
    is its transpose), nondegenerate (Gram map of rank 8) and invariant under two exact unit even versors
    (a rotation and a boost); on the null-blade Fock ideal of Cl(m, m), m = 1, 2, 3, the scalar part of
    psi~ phi vanishes for every pair of Fock basis states.
(d) The mass formula as an exact identity over Q(i): for p = pi1 pi1^dag + pi2 pi2^dag (Hermitian 2 x 2),
    det p = |<pi1 pi2>|^2 with <pi1 pi2> = pi1_0 pi2_1 - pi1_1 pi2_0, so m^2 = 2 det p = 2 |<pi1 pi2>|^2;
    a single spinor and aligned spinors give det p = 0 (null), misaligned ones det p > 0.
(g) The Fock representation for three modes: Jordan-Wigner a_i on Lambda C^3 (exact integers) satisfy the
    CAR, the six real Majorana combinations a + a^dag, a - a^dag satisfy Clifford relations of signature
    (3, 3), their 64 monomials have rank 64 = dim Mat_8 (irreducible), and (-1)^N anticommutes with each
    (the parity grading is the chirality).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ24 = GA.sig(2, 4)
SPINORS = [((GA.qi(1, 2), GA.qi(-1, 0)), (GA.qi(0, 3), GA.qi(2, -1))),
           ((GA.qi(3, 0), GA.qi(1, 1)), (GA.qi(-2, 5), GA.qi(0, -1))),
           ((GA.qi(1, -1), GA.qi(2, 2)), (GA.qi(4, 1), GA.qi(F(1, 2), 3)))]


def _bl(*idx, sq=SQ24):
    x = {(): F(1)}
    for i in idx:
        x = GA.mul(x, GA.gen(i), sq)
    return x


def _dim(xs):
    bs = sorted({b for x in xs for b in x})
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bs] for x in xs]) if xs else 0


ONE = {(): F(1)}
I6 = _bl(0, 1, 2, 3, 4, 5)
F24 = GA.scal(F(1, 4), GA.mul(GA.add(ONE, _bl(0, 1, 2, 3)), GA.add(ONE, _bl(0, 1, 4, 5)), SQ24))
EVEN = [b for b in GA.all_blades(6) if len(b) % 2 == 0]


def check_even_subalgebra_is_mat4_c():
    gens = [GA.mul(GA.gen(i), GA.gen(5), SQ24) for i in range(5)]
    ok = all(GA.eq(GA.add(GA.mul(gens[i], gens[j], SQ24), GA.mul(gens[j], gens[i], SQ24)),
                   GA.scal(2 * ((1 if i < 2 else -1) if i == j else 0), ONE)) for i in range(5) for j in range(5))
    prods = []
    for k in range(6):
        for S in combinations(range(5), k):
            x = dict(ONE)
            for i in S:
                x = GA.mul(x, gens[i], SQ24)
            prods.append(x)
    ok = ok and len(prods) == 32 and _dim(prods) == 32 and all(len(b) % 2 == 0 for x in prods for b in x)
    ok = ok and GA.eq(GA.mul(I6, I6, SQ24), GA.neg(ONE))
    biv = [_bl(i, j) for i in range(6) for j in range(i + 1, 6)]
    centre = [b for b in EVEN if all(GA.commutes({b: F(1)}, x, SQ24) for x in biv)]
    ok = ok and centre == [(), (0, 1, 2, 3, 4, 5)]
    ok = ok and GA.eq(GA.mul(F24, F24, SQ24), F24) and GA.eq(GA.reverse(F24), F24)
    ok = ok and _dim([GA.mul({b: F(1)}, F24, SQ24) for b in EVEN]) == 8
    corner = [GA.mul(GA.mul(F24, {b: F(1)}, SQ24), F24, SQ24) for b in EVEN]
    jf = GA.mul(I6, F24, SQ24)
    ok = ok and _dim(corner) == 2 == _dim(corner + [F24, jf]) and GA.eq(GA.mul(jf, jf, SQ24), GA.neg(F24))
    _tp_rv = (ok); assert _tp_rv is not False, "check_even_subalgebra_is_mat4_c"; return _tp_rv


def _fock_states(m):
    sq = tuple([1] * m + [-1] * m)
    w = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(m + i))) for i in range(m)]
    v = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(m + i))) for i in range(m)]
    f = w[0]
    for x in w[1:]:
        f = GA.mul(f, x, sq)
    states = []
    for k in range(m + 1):
        for S in combinations(range(m), k):
            st = f
            for i in reversed(S):
                st = GA.mul(v[i], st, sq)
            states.append(st)
    return sq, states


def check_helicity_form_lives_on_the_twistor_ideal():
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    ok = True
    for m in (1, 2, 3):
        sq, states = _fock_states(m)
        ok = ok and _dim(states) == 2 ** m
        ok = ok and all(GA.mul(GA.reverse(a), b, sq).get((), F(0)) == 0 for a in states for b in states)
    ideal = [GA.mul({b: F(1)}, F24, SQ24) for b in EVEN]
    basis = []
    for x in ideal:
        if _dim(basis + [x]) > len(basis):
            basis.append(x)
    ok = ok and len(basis) == 8

    def form(a, b):
        return GA.mul(GA.reverse(a), b, SQ24)
    gram = [[form(a, b) for b in basis] for a in basis]
    ok = ok and any(x for row in gram for x in row)
    ok = ok and all(GA.eq(GA.reverse(gram[i][j]), gram[j][i]) for i in range(8) for j in range(8))
    cb = sorted({b for row in gram for x in row for b in x})
    ok = ok and GA.rank_of_vectors([[x.get(b, F(0)) for x in row for b in cb] for row in gram]) == 8
    R1 = GA.add(GA.scal(F(3, 5), ONE), GA.scal(F(4, 5), _bl(0, 1)))
    R2 = GA.add(GA.scal(F(5, 3), ONE), GA.scal(F(4, 3), _bl(0, 2)))
    for R in (R1, R2):
        ok = ok and GA.eq(GA.mul(R, GA.reverse(R), SQ24), ONE)
        ok = ok and all(GA.eq(form(GA.mul(R, a, SQ24), GA.mul(R, b, SQ24)), form(a, b)) for a in basis for b in basis)
    _tp_rv = (ok); assert _tp_rv is not False, "check_helicity_form_lives_on_the_twistor_ideal"; return _tp_rv


def check_mass_formula_identity():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    ok = True

    def mom(spinors):
        return [[sum((s[A] * s[B].conj() for s in spinors), GA.qi(0)) for B in range(2)] for A in range(2)]

    def det2(p):
        return p[0][0] * p[1][1] - p[0][1] * p[1][0]
    for p1, p2 in SPINORS:
        br = p1[0] * p2[1] - p1[1] * p2[0]
        p = mom([p1, p2])
        d = det2(p)
        ok = ok and p[0][1] == p[1][0].conj() and d.im == 0
        ok = ok and d == br * br.conj() and 2 * d.re == 2 * (br.re * br.re + br.im * br.im) and d.re > 0
        ok = ok and det2(mom([p1])) == GA.qi(0)
        c = GA.qi(2, -3)
        ok = ok and det2(mom([p1, (c * p1[0], c * p1[1])])) == GA.qi(0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_mass_formula_identity"; return _tp_rv


def _zeros(d):
    return [[0] * d for _ in range(d)]


def _imm(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def check_fock_module_is_irreducible_spinor_module():
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    nm, d = 3, 8
    a = []
    for i in range(nm):
        M = _zeros(d)
        for b in range(d):
            if b >> i & 1:
                M[b ^ (1 << i)][b] = (-1) ** bin(b & ((1 << i) - 1)).count("1")
        a.append(M)
    ad = [[list(r) for r in zip(*x)] for x in a]
    eye = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    add = lambda A, B, s=1: [[A[i][j] + s * B[i][j] for j in range(d)] for i in range(d)]
    ok = all(add(_imm(a[i], ad[j]), _imm(ad[j], a[i])) == (eye if i == j else _zeros(d)) for i in range(nm) for j in range(nm))
    gam = []
    for i in range(nm):
        gam.append(add(a[i], ad[i]))
        gam.append(add(a[i], ad[i], -1))
    sqs = [1, -1] * nm
    ok = ok and all(add(_imm(gam[p], gam[q]), _imm(gam[q], gam[p])) ==
                    ([[2 * sqs[p] * x for x in r] for r in eye] if p == q else _zeros(d)) for p in range(6) for q in range(6))
    monos = []
    for k in range(7):
        for S in combinations(range(6), k):
            M = eye
            for t in S:
                M = _imm(M, gam[t])
            monos.append([F(x) for r in M for x in r])
    ok = ok and GA.rank_of_vectors(monos) == 64
    chir = [[(-1) ** bin(i).count("1") if i == j else 0 for j in range(d)] for i in range(d)]
    ok = ok and all(add(_imm(chir, g_), _imm(g_, chir)) == _zeros(d) for g_ in gam)
    _tp_rv = (ok); assert _tp_rv is not False, "check_fock_module_is_irreducible_spinor_module"; return _tp_rv
