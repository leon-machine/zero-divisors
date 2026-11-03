"""synthesis.s-wave-array-is-a-boundary-mode-set: exact checks.

(1) Tower model: in Cl(n,n) (n = 1..4) the adjoined null pairs v_j = (e_j + f_j)/2,
    w_j = (e_j - f_j)/2 satisfy the CAR exactly, and the algebra they generate (spanned by the
    ordered words over subsets of the 2n generators) has computed dimension 4^n, the window dimension of
    the boundary-mode algebra: the tower supplies the window algebras.
(2) The s-wave array: a Jordan-Wigner window k = -K..K (K = 1, 2) with real 2x2 blocks; the
    Gibbs state of H = sum_k k N_k at e^{-beta kappa} = q (rational) has marginals
    n_k = q^k/(1 + q^k); particle-hole conjugation b_k = a_k^dagger for k < 0 is implemented by a
    real orthogonal matrix and turns H into sum_{k>0} k N_k + sum_{k<0} |k| N'_k + sum_{k<0} k,
    so the same density matrix is the Gibbs state of a positive-frequency Hamiltonian in which
    each frequency |k| > 0 occurs twice, and the marginals become Fermi-Dirac at |k|.
(3) The zero mode: on one mode with omega = 0 the KMS relation n = e^{-beta omega}(1 - n) forces
    n = 1/2, the trace, which is the Fermi-Dirac value at omega = 0; for omega > 0 it forces FD.
"""
from fractions import Fraction as F
from GA import mul, add, sub, scal, sc, gen, eq, all_blades, rank_of_vectors
from tp_premise import premise
from pyutil import get_or_set


def smul(A, B):
    """Sparse matrices as dicts {(i, j): value}."""
    rows = {}
    for (k, j), v in B.items():
        get_or_set(rows, k, []).append((j, v))
    out = {}
    for (i, k), u in A.items():
        for j, v in rows.get(k, ()):
            out[(i, j)] = out.get((i, j), F(0)) + u * v
    return {key: v for key, v in out.items() if v != 0}


def sadd(A, B, c=F(1)):
    out = dict(A)
    for key, v in B.items():
        out[key] = out.get(key, F(0)) + c * v
    return {key: v for key, v in out.items() if v != 0}


def sident(dim, c=F(1)):
    return {(i, i): c for i in range(dim)} if c != 0 else {}


def stranspose(A):
    return {(j, i): v for (i, j), v in A.items()}


def jw(n):
    """Annihilators a_0..a_{n-1} on (C^2)^{otimes n}: a_j |s> = (-1)^{#occupied before j} |s - e_j>."""
    dim = 2 ** n
    ops = []
    for j in range(n):
        M = {}
        for s in range(dim):
            occ = [(s >> (n - 1 - i)) & 1 for i in range(n)]
            if occ[j]:
                sign = (-1) ** sum(occ[:j])
                t = s - (1 << (n - 1 - j))
                M[(t, s)] = F(sign)
        ops.append(M)
    return ops


def check_tower_pairs_give_windows():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("hawking.imported-algebra-boundary-modes-car-algebra")
    for n in range(1, 5):
        SQ = tuple([1] * n + [-1] * n)
        e = [gen(i) for i in range(n)]
        f = [gen(n + i) for i in range(n)]
        v = [scal(F(1, 2), add(e[i], f[i])) for i in range(n)]
        w = [scal(F(1, 2), sub(e[i], f[i])) for i in range(n)]
        for i in range(n):
            for j in range(n):
                assert eq(add(mul(v[i], v[j], SQ), mul(v[j], v[i], SQ)), {})
                assert eq(add(mul(w[i], w[j], SQ), mul(w[j], w[i], SQ)), {})
                anti = add(mul(v[i], w[j], SQ), mul(w[j], v[i], SQ))
                assert eq(anti, sc(F(1)) if i == j else {})
        # w_j is the reverse-conjugate partner: v_j w_j and w_j v_j are complementary projections
        P = mul(v[0], w[0], SQ)
        assert eq(mul(P, P, SQ), P) and eq(add(P, mul(w[0], v[0], SQ)), sc(F(1)))
        # dimension of the generated algebra: by the CAR every product of the v's and w's reduces to a
        # combination of the ordered words over subsets of (v_1, w_1, ..., v_n, w_n), so their span is the
        # algebra; its rank is computed
        gens = [x for i in range(n) for x in (v[i], w[i])]
        blades = all_blades(2 * n)
        coords = []
        for mask in range(2 ** (2 * n)):
            word = sc(F(1))
            for i in range(2 * n):
                if (mask >> i) & 1:
                    word = mul(word, gens[i], SQ)
            coords.append([word.get(b, F(0)) for b in blades])
        assert rank_of_vectors(coords) == 4 ** n
    return True


def check_particle_hole_turns_array_into_positive_modes():
    premise("singularity.bosonisation-bridge-s-wave-sector")
    premise("hawking.gibbs-states-are-kms-conversely-finite")
    for K in (1, 2):
        ks = list(range(-K, K + 1))
        n = len(ks)
        dim = 2 ** n
        a = jw(n)
        ad = [stranspose(x) for x in a]
        Nk = [smul(ad[i], a[i]) for i in range(n)]
        b = [ad[i] if ks[i] < 0 else a[i] for i in range(n)]
        bd = [stranspose(x) for x in b]
        # CAR on the window, for the array and for its conjugate
        for ops, dags in ((a, ad), (b, bd)):
            for i in range(n):
                for j in range(n):
                    ac = sadd(smul(ops[i], dags[j]), smul(dags[j], ops[i]))
                    assert ac == (sident(dim) if i == j else {})
                    assert sadd(smul(ops[i], ops[j]), smul(ops[j], ops[i])) == {}
        # particle-hole for k < 0: N'_k = 1 - N_k, and H = H' + sum_{k<0} k
        H, Hp, const = {}, {}, F(0)
        for i, k in enumerate(ks):
            H = sadd(H, Nk[i], F(k))
            Np = smul(bd[i], b[i])
            if k < 0:
                assert Np == sadd(sident(dim), Nk[i], F(-1))
                const += k
            Hp = sadd(Hp, Np, F(abs(k)))
        assert H == sadd(Hp, sident(dim, const))
        # frequencies of H': each |k| > 0 twice, one zero mode
        freqs = sorted(abs(k) for k in ks)
        assert freqs.count(0) == 1
        for m in range(1, K + 1):
            assert freqs.count(m) == 2
        for q in (F(1, 2), F(1, 3), F(2, 5)):
            # Gibbs weight e^{-beta H} at e^{-beta kappa} = q, kappa = 1; H is diagonal
            wts = []
            for s_ in range(dim):
                wts.append(q ** H.get((s_, s_), F(0)) if (s_, s_) in H else F(1))
            Zs = sum(wts, F(0))
            for i, k in enumerate(ks):
                nk = sum((wts[s_] * Nk[i].get((s_, s_), F(0)) for s_ in range(dim)), F(0)) / Zs
                assert nk == q ** k / (1 + q ** k)               # Fermi-Dirac at omega_k = k
                if k < 0:
                    assert 1 - nk == q ** (-k) / (1 + q ** (-k))  # hole: Fermi-Dirac at |k|
                if k == 0:
                    assert nk == F(1, 2)
    return True


def check_zero_mode_kms_is_trace():
    premise("hawking.gibbs-states-are-kms-conversely-finite")
    # one mode with tau_t(a) = e^{-i omega t} a: the KMS relation at beta is
    # omega(a^dagger a) = x omega(a a^dagger), x = e^{-beta omega}, i.e. n = x (1 - n), a linear
    # equation with the unique solution n = x/(1 + x). At e^{-beta kappa} = 1/2 and omega = m kappa:
    expected = [F(1, 2), F(1, 3), F(1, 5), F(1, 9)]
    for m in range(4):
        x = F(1, 2) ** m
        n = x / (1 + x)
        assert n == x * (1 - n) and n == expected[m]
    # omega = 0 (m = 0): the trace, n = 1/2, the Fermi-Dirac value at zero frequency;
    # the zero mode of the s-wave array is therefore in its I-state value automatically
    assert expected[0] == 1 - expected[0]
    return True
