"""scrambling.boundary-mode-space-matrix: exact checks.

(1) Fock model: on the full Fock space of n = 4 modes (16 states, Jordan-Wigner signs), the
    bilinears E_ij = psi_i^dag psi_j satisfy [E_ij, E_kl] = delta_jk E_il - delta_li E_kj for every
    index quadruple, as operator identities on every basis state; the CAR of the psi_i are
    verified on the same space.
(2) One-particle restriction: for n = 3, 4, 5 each E_ij maps psi_k^dag|0> to delta_jk psi_i^dag|0>
    (so preserves the one-particle subspace and acts as the matrix unit e_ij), and the restricted
    operators span all of Mat_n (rank n^2).
(3) The doubling, in GA.py: in Cl(n,n) (n = 2, 3) each real mode e_i (square +1) with its adjoined
    partner f_i (square -1) gives psi_i = (e_i + f_i)/2, psi_i^dag = (e_i - f_i)/2 obeying the CAR;
    the GA elements E_ij = psi_i^dag psi_j satisfy the gl(n) relations and span n^2 dimensions,
    while the real directions alone give the bivectors e_i e_j (i < j) spanning only
    n(n-1)/2 = dim so(n).
"""
from fractions import Fraction as F

import GA
import fock


ann, cre = fock.ann_on, fock.cre_on


def vadd(*vs, signs=None):
    return fock.vadd(*(vs if signs is None else [fock.vsc(sg, v) for sg, v in zip(signs, vs)]))


def E(i, j, vec):
    return cre(i, ann(j, vec))


def check_gl_relations_on_fock_space():
    n = 4
    for s in range(1 << n):
        v = {s: F(1)}
        for i in range(n):
            for j in range(n):
                # CAR on this state
                ac = vadd(ann(i, cre(j, v)), cre(j, ann(i, v)))
                assert ac == (v if i == j else {})
                assert vadd(ann(i, ann(j, v)), ann(j, ann(i, v))) == {}
                for k in range(n):
                    for l in range(n):
                        lhs = vadd(E(i, j, E(k, l, v)), E(k, l, E(i, j, v)), signs=[1, -1])
                        terms, sg = [], []
                        if j == k:
                            terms.append(E(i, l, v))
                            sg.append(1)
                        if l == i:
                            terms.append(E(k, j, v))
                            sg.append(-1)
                        rhs = vadd(*terms, signs=sg) if terms else {}
                        assert lhs == rhs
    return True


def check_one_particle_restriction_is_onto():
    for n in (3, 4, 5):
        rows = []
        for i in range(n):
            for j in range(n):
                mat = []
                for k in range(n):
                    img = E(i, j, {1 << k: F(1)})
                    assert img == ({1 << i: F(1)} if j == k else {})
                    mat.extend([img.get(1 << r, F(0)) for r in range(n)])
                rows.append(mat)
        assert GA.rank_of_vectors(rows) == n * n
    return True


def check_doubling_gives_gl_n_in_clifford_algebra():
    for n in (2, 3):
        S = GA.sig(n, n)
        e = [GA.gen(i) for i in range(n)]
        f = [GA.gen(n + i) for i in range(n)]
        psi = [GA.scal(F(1, 2), GA.add(e[i], f[i])) for i in range(n)]
        psd = [GA.scal(F(1, 2), GA.sub(e[i], f[i])) for i in range(n)]
        one = GA.sc(1)
        for i in range(n):
            for j in range(n):
                assert GA.eq(GA.add(GA.mul(psi[i], psd[j], S), GA.mul(psd[j], psi[i], S)), one if i == j else {})
                assert GA.is_zero(GA.add(GA.mul(psi[i], psi[j], S), GA.mul(psi[j], psi[i], S)))
        Em = {(i, j): GA.mul(psd[i], psi[j], S) for i in range(n) for j in range(n)}
        for (i, j), A in Em.items():
            for (k, l), B in Em.items():
                lhs = GA.sub(GA.mul(A, B, S), GA.mul(B, A, S))
                rhs = {}
                if j == k:
                    rhs = GA.add(rhs, Em[(i, l)])
                if l == i:
                    rhs = GA.sub(rhs, Em[(k, j)])
                assert GA.eq(lhs, rhs)
        blades = GA.all_blades(2 * n)
        rk = lambda xs: GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in xs])
        assert rk(list(Em.values())) == n * n
        real = [GA.mul(e[i], e[j], S) for i in range(n) for j in range(i + 1, n)]
        assert rk(real) == n * (n - 1) // 2
    return True
