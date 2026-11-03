"""dark-matter.residue-soldered-invariant-not-algebraic-one: exact checks.

(i) The soldered invariant. An algebra map phi carrying V onto V' satisfies phi(v)^2 = phi(v^2) = v^2,
so the Gram matrix of the images of a basis of V equals that of the basis: the signature of the
quadratic form v -> v^2 on the generating subspace is what an isomorphism of soldered algebras
must preserve. Checked: for every nondegenerate (p,q) with n <= 4 and four rational changes of basis
of V, the Gram matrix of the new generators, computed in GA, has congruence signature (p,q,0)
(Sylvester), so the residue p - q mod 8 is read off (A, V) whatever generating basis is used.
(ii) Abstract isomorphisms: explicit generator images satisfying the defining relations and spanning
the whole target give Cl(1,1) = Cl(2,0) (e0 -> e0, e1 -> e0 e1), Cl(1,2) = Cl(3,0) (e0 -> e0,
e_i -> e0 e_i) and Cl(1,3) = Cl(0,4) (e0 -> e0 e1 e2 e3, e_i -> e_i), between residues 0 and 2,
7 and 3, 6 and 4. Each map sends some vector outside the vectors, and no map can do otherwise: the
generating subspaces have different signatures ((1,1) vs (2,0), (1,2) vs (3,0), (1,3) vs (0,4)); in
Cl(0,4) every vector squares to -|c|^2 <= 0 while e0 of Cl(1,3) squares to +1.
(iii) Cl(1,3) = Mat_2(H), and through the map of (ii) Cl(0,4) = Mat_2(H): the null pair
v = (e0 + e1)/2, v* = (e0 - e1)/2 gives matrix units, i = e0 e1 e2 and j = e0 e1 e3 are anticommuting
square -1 elements commuting with them, and E_ab {1, i, j, ij} spans all 16 dimensions; the
transported elements do the same in Cl(0,4). This is the premise's D = H at r = 4, 6, with k = 2.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise

BASIS_CHANGES = [
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    [[1, 2, 0, 0], [0, 1, 0, 0], [0, 3, 1, 0], [1, 0, 0, 1]],
    [[2, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1], [1, 0, 1, 2]],
    [[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, 3, -1], [0, 0, 1, 2]],
]


def det(M):
    n = len(M)
    if n == 1:
        return F(M[0][0])
    return sum((-1) ** j * M[0][j] * det([row[:j] + row[j + 1:] for row in M[1:]]) for j in range(n))


def rank(xs, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in xs])


def check_signature_is_read_off_the_generating_subspace():
    ok = True
    count = 0
    for n in range(1, 5):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p, q)
            for T in BASIS_CHANGES:
                Tn = [row[:n] for row in T[:n]]
                if det(Tn) == 0:
                    continue
                fs = [{(j,): F(Tn[i][j]) for j in range(n) if Tn[i][j] != 0} for i in range(n)]
                G = [[GA.dot(fs[i], fs[j], sq) for j in range(n)] for i in range(n)]
                # f_i f_j + f_j f_i = 2 G_ij exactly (the quadratic form is v -> v^2)
                ok = ok and all(GA.eq(GA.add(GA.mul(fs[i], fs[j], sq), GA.mul(fs[j], fs[i], sq)),
                                      GA.sc(2 * G[i][j])) for i in range(n) for j in range(n))
                ok = ok and GA.congruence_signature(G) == (p, q, 0)
                count += 1
    ok = ok and count == 14 * 4
    GA.check("the signature (p,q), hence the residue, is the Sylvester invariant of v -> v^2 on V", ok)
    return ok


ISOS = [
    # (source signature, target signature, generator images as blades of the target)
    ((1, 1), (2, 0), [(0,), (0, 1)]),
    ((1, 2), (3, 0), [(0,), (0, 1), (0, 2)]),
    ((1, 3), (0, 4), [(0, 1, 2, 3), (1,), (2,), (3,)]),
]


def iso_data(src, tgt, imgs_b):
    sqs, sqt = GA.sig(*src), GA.sig(*tgt)
    imgs = [{b: F(1)} for b in imgs_b]
    return sqs, sqt, imgs


def transport(x, imgs, sqt):
    out = {}
    for S, c in x.items():
        y = GA.sc(1)
        for i in S:
            y = GA.mul(y, imgs[i], sqt)
        out = GA.add(out, GA.scal(c, y))
    return out


def check_abstract_isomorphisms_not_soldered():
    ok = True
    residues = []
    for src, tgt, imgs_b in ISOS:
        sqs, sqt, imgs = iso_data(src, tgt, imgs_b)
        n = len(sqs)
        ok = ok and all(GA.eq(GA.mul(imgs[i], imgs[i], sqt), GA.sc(sqs[i])) for i in range(n))
        ok = ok and all(GA.anticommutes(imgs[i], imgs[j], sqt) for i in range(n) for j in range(i + 1, n))
        prods = [transport({S: F(1)}, imgs, sqt) for S in GA.all_blades(n)]
        ok = ok and rank(prods, n) == 2 ** n
        # the map does not carry vectors to vectors
        ok = ok and any(len(b) != 1 for x in imgs for b in x)
        # and no map can: the generating subspaces have different signatures
        Gs = [[GA.dot(GA.gen(i), GA.gen(j), sqs) for j in range(n)] for i in range(n)]
        Gt = [[GA.dot(GA.gen(i), GA.gen(j), sqt) for j in range(n)] for i in range(n)]
        ok = ok and GA.congruence_signature(Gs) == src + (0,) and GA.congruence_signature(Gt) == tgt + (0,)
        ok = ok and src != tgt
        residues.append(((src[0] - src[1]) % 8, (tgt[0] - tgt[1]) % 8))
    ok = ok and residues == [(0, 2), (7, 3), (6, 4)]
    # in Cl(0,4) every vector squares to -|c|^2; e0 of Cl(1,3) squares to +1
    sq04, sq13 = GA.sig(0, 4), GA.sig(1, 3)
    for c in [(1, 0, 0, 0), (1, 1, 0, 0), (2, -1, 3, 1), (1, 2, 2, -3)]:
        v = {(i,): F(x) for i, x in enumerate(c) if x != 0}
        ok = ok and GA.mul(v, v, sq04) == GA.sc(-sum(x * x for x in c))
        ok = ok and GA.mul(v, v, sq13) == GA.sc(c[0] ** 2 - c[1] ** 2 - c[2] ** 2 - c[3] ** 2)
    GA.check("residues 0~2, 7~3, 6~4 are abstractly isomorphic but no isomorphism keeps vectors", ok)
    return ok


def mat2H_ok(E, i, j, sq, n):
    ok = GA.eq(GA.add(E[(1, 1)], E[(2, 2)]), GA.sc(1))
    for (a, b) in E:
        for (c, d) in E:
            want = E[(a, d)] if b == c else {}
            ok = ok and GA.eq(GA.mul(E[(a, b)], E[(c, d)], sq), want)
    k = GA.mul(i, j, sq)
    ok = ok and GA.eq(GA.mul(i, i, sq), GA.sc(-1)) and GA.eq(GA.mul(j, j, sq), GA.sc(-1))
    ok = ok and GA.anticommutes(i, j, sq)
    ok = ok and all(GA.commutes(x, Eab, sq) for x in (i, j) for Eab in E.values())
    span = [GA.mul(Eab, h, sq) for Eab in E.values() for h in (GA.sc(1), i, j, k)]
    return ok and rank(span, n) == 16


def check_this_world_and_r4_are_mat2_quaternions():
    premise("dark-matter.type-residue-what-each-tower-can")
    sq13 = GA.sig(1, 3)
    v = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(1)))
    vs = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(1)))
    E = {(1, 1): GA.mul(v, vs, sq13), (2, 2): GA.mul(vs, v, sq13), (1, 2): v, (2, 1): vs}
    i = GA.mul(GA.mul(GA.gen(0), GA.gen(1), sq13), GA.gen(2), sq13)
    j = GA.mul(GA.mul(GA.gen(0), GA.gen(1), sq13), GA.gen(3), sq13)
    ok = mat2H_ok(E, i, j, sq13, 4)
    # transported to Cl(0,4) by the abstract isomorphism of (ii)
    src, tgt, imgs_b = ISOS[2]
    sqs, sqt, imgs = iso_data(src, tgt, imgs_b)
    Et = {key: transport(x, imgs, sqt) for key, x in E.items()}
    ok = ok and mat2H_ok(Et, transport(i, imgs, sqt), transport(j, imgs, sqt), sqt, 4)
    # dimension count: Mat_k(H) has dimension 4 k^2 = 2^4, so k = 2
    ok = ok and [k for k in range(1, 5) if 4 * k * k == 2 ** 4] == [2]
    GA.check("Cl(1,3) = Cl(0,4) = Mat_2(H), exhibited with matrix units and quaternion units", ok)
    return ok
