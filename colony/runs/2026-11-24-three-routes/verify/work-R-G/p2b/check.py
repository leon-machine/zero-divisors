"""Helicity-two composites of light-ray fermions: exact checks.

Part A (the algebra, GA): one null generator, window levels {-1, 0}, four channels (helicity sign, flavour),
each mode a tower plane (e, f) with squares (+1, -1), a* = v = (e + f)/2, a = w = (e - f)/2, numbers in
span{1, J}, J = g_1 g_2 the kernel bivector. The adjoint * fixes generators of square +1 and negates those of
square -1 and reverses products. Rotation about the generator: a_{k, alpha} -> e^{-theta w_alpha J} a_{k, alpha},
w = +1/2, -1/2.
Part B (larger windows): the same modes as an exact Fock space on occupation bit masks (integers only), with
the chiral sea (levels k < 0 filled in every channel) as the reference vector. Part B is tied to Part A by
computing the same number both ways on the smallest window.

(i)   weights +1/2 and -1/2: every pair mode a*_alpha a_beta has helicity w_alpha - w_beta in {-1, 0, 1};
      the rotation multiplies rho(E_{+-}) by e^{theta J} and the four-fermion mode X_2 by e^{2 theta J};
(ii)  sea values: two flavours, X_q = sum_{a+b=q} rho_a(E^1_{+-}) rho_b(E^2_{+-}): C(q+1, 3), q = 1..5;
      one species, V_q with the weights (k_2 - k_1)(l_2 - l_1): C(q+3, 7), q = 1..7; both annihilate the sea;
      the counting identity sum_{x_1 < x_2, x_1 + x_2 = s} (x_2 - x_1)^2 = C(s+2, 3);
(iii) the commutator [X_q, X_q*] is not a number on edge-clean vectors: 1, 0, 3 at q = 2 and 4, 2, 10 at
      q = 3 on the sea and on two one-pair vectors, while the total density mode gives 4q on all of them;
      X_q*^2 annihilates the sea at q = 2, 3;
(iv)  in Cl(1,3): for future null p_1, p_2 written with the null directions of a generator,
      Q(p_1 + p_2) = |alpha_2 p_1perp - alpha_1 p_2perp|^2 / (alpha_1 alpha_2), zero only for parallel momenta;
(v)   a medium of five tower modes on a ring with shift dynamics, coupled at one site to the stored two-path
      matter factor by unitary kicks: the field commutes exactly with the detection at every event whose
      field element commutes with the later source elements; the mean response is 0 in the empty medium
      and -4/5 (not -a for the kick angle a) on a one-quantum vector.
Exact arithmetic only (Fractions and integers).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


# ----------------------------------------------------------------------------------------------------
# small exact helpers
# ----------------------------------------------------------------------------------------------------

def binom(n, k):
    if k < 0 or k > n:
        return 0
    out = 1
    for j in range(k):
        out = out * (n - j) // (j + 1)
    return out


def star(x, sq):
    out = {}
    for b, c in x.items():
        k = len(b)
        s = (-1) ** (k * (k - 1) // 2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        if c * s != 0:
            out[b] = c * s
    return out


def prod(sq, *xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def comm(sq, a, b):
    return GA.sub(GA.mul(a, b, sq), GA.mul(b, a, sq))


def scalar_part(x):
    return x.get((), 0)


# ----------------------------------------------------------------------------------------------------
# Part A: the smallest window in the algebra
# ----------------------------------------------------------------------------------------------------

A_LEVELS = [-1, 0]
A_CHANNELS = [('+', 1), ('-', 1), ('+', 2), ('-', 2)]
A_MODES = [(k, c) for k in A_LEVELS for c in A_CHANNELS]
A_SQ = tuple([-1, -1] + [1, -1] * len(A_MODES))
A_POS = {md: 2 + 2 * i for i, md in enumerate(A_MODES)}
A_J = GA.mul(GA.gen(0), GA.gen(1), A_SQ)
WEIGHT = {'+': F(1, 2), '-': F(-1, 2)}


def a_cr(md):
    i = A_POS[md]
    return GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(i + 1)))


def a_an(md):
    i = A_POS[md]
    return GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(i + 1)))


def a_rho(q, ca, cb):
    out = {}
    for k in A_LEVELS:
        if k + q in A_LEVELS:
            out = GA.add(out, prod(A_SQ, a_cr((k, ca)), a_an((k + q, cb))))
    return out


def a_sea_projector():
    out = GA.sc(1)
    for md in A_MODES:
        n = prod(A_SQ, a_cr(md), a_an(md))
        out = GA.mul(out, n if md[0] < 0 else GA.sub(GA.sc(1), n), A_SQ)
    return out


def a_rotation(c, s):
    """U = exp(theta J sum w n) at the half angle (c, s) = (cos(theta/2), sin(theta/2))."""
    out = GA.sc(1)
    for md in A_MODES:
        n = prod(A_SQ, a_cr(md), a_an(md))
        sign = 1 if md[1][0] == '+' else -1
        fac = GA.add(GA.sc(1), GA.mul(GA.add(GA.sc(c - 1), GA.scal(sign * s, A_J)), n, A_SQ))
        out = GA.mul(out, fac, A_SQ)
    return out


def check_no_pair_mode_has_helicity_two_and_the_quartic_turns_twice():
    """(i): weight differences; the rotation acts on rho(E_{+-}) by e^{theta J} and on X_2 by e^{2 theta J}."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    premise("synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins")
    for md in A_MODES:
        assert GA.eq(GA.add(prod(A_SQ, a_an(md), a_cr(md)), prod(A_SQ, a_cr(md), a_an(md))), GA.sc(1))
        assert GA.eq(star(a_cr(md), A_SQ), a_an(md)) and GA.commutes(A_J, a_cr(md), A_SQ)
    assert GA.eq(GA.mul(A_J, A_J, A_SQ), GA.sc(-1))
    # helicities of the pair modes: two channels, and sixteen channels with eight of each weight
    for weights in ([F(1, 2), F(-1, 2)], [F(1, 2)] * 8 + [F(-1, 2)] * 8):
        diffs = {wa - wb for wa in weights for wb in weights}
        assert diffs == {F(-1), F(0), F(1)} and F(2) not in diffs and F(-2) not in diffs
    # the mode rotation at the half angle (4/5, 3/5): theta has (cos, sin) = (7/25, 24/25)
    c, s = F(4, 5), F(3, 5)
    U = a_rotation(c, s)
    Uinv = star(U, A_SQ)
    assert GA.eq(GA.mul(U, Uinv, A_SQ), GA.sc(1))
    c1, s1 = c * c - s * s, 2 * c * s
    c2, s2 = c1 * c1 - s1 * s1, 2 * c1 * s1
    e1 = GA.add(GA.sc(c1), GA.scal(s1, A_J))
    e2 = GA.add(GA.sc(c2), GA.scal(s2, A_J))
    flip1 = a_rho(1, ('+', 1), ('-', 1))
    flip2 = a_rho(1, ('+', 2), ('-', 2))
    X2 = GA.mul(flip1, flip2, A_SQ)
    assert not GA.is_zero(X2)
    assert GA.eq(prod(A_SQ, U, flip1, Uinv), GA.mul(e1, flip1, A_SQ))
    assert GA.eq(prod(A_SQ, U, X2, Uinv), GA.mul(e2, X2, A_SQ))
    assert not GA.eq(prod(A_SQ, U, X2, Uinv), GA.mul(e1, X2, A_SQ))
    dens = a_rho(1, ('+', 1), ('+', 1))
    assert GA.eq(prod(A_SQ, U, dens, Uinv), dens)
    # the sea value of [X_2, X_2*] in the algebra: 1 = C(3, 3), and X_2 annihilates the sea
    P = a_sea_projector()
    assert GA.is_zero(GA.mul(X2, P, A_SQ))
    cm = comm(A_SQ, X2, star(X2, A_SQ))
    assert scalar_part(GA.mul(cm, P, A_SQ)) == binom(3, 3) * scalar_part(P)
    assert scalar_part(GA.mul(prod(A_SQ, GA.neg(A_J), cm), P, A_SQ)) == 0
    # the same number from the bit-mask Fock space of Part B
    assert sea_value_two_flavours(2) == 1
    return True


# ----------------------------------------------------------------------------------------------------
# Part B: exact Fock space on occupation bit masks
# ----------------------------------------------------------------------------------------------------

def f_sign(mask, i):
    return -1 if bin(mask & ((1 << i) - 1)).count('1') % 2 else 1


def f_apply(op, st):
    """op: list of (coefficient, word); word = [(kind, mode)], applied right to left; kind 'c' or 'a'."""
    out = {}
    for coef, word in op:
        cur = st
        for kind, i in reversed(word):
            nxt = {}
            for msk, c in cur.items():
                occ = (msk >> i) & 1
                if kind == 'c' and not occ:
                    nxt[msk | (1 << i)] = c * f_sign(msk, i)
                if kind == 'a' and occ:
                    nxt[msk & ~(1 << i)] = c * f_sign(msk, i)
            cur = nxt
            if not cur:
                break
        for msk, c in cur.items():
            v = out.get(msk, 0) + coef * c
            if v == 0:
                out.pop(msk, None)
            else:
                out[msk] = v
    return out


def f_dagger(op):
    return [(coef, [('a' if k == 'c' else 'c', i) for k, i in reversed(word)]) for coef, word in op]


def f_ip(a, b):
    return sum(c * b.get(msk, 0) for msk, c in a.items())


def f_setup(N, channels):
    levels = list(range(-N, N))
    idx = {}
    for k in levels:
        for c in channels:
            idx[(k, c)] = len(idx)
    sea = 0
    for (k, c), i in idx.items():
        if k < 0:
            sea |= 1 << i
    return levels, idx, {sea: 1}


def f_rho(q, ca, cb, levels, idx):
    return [(1, [('c', idx[(k, ca)]), ('a', idx[(k + q, cb)])]) for k in levels if (k + q) in levels]


def f_mul(A, B):
    return [(x * y, wa + wb) for x, wa in A for y, wb in B]


def f_comm_value(X, st):
    up = f_apply(f_dagger(X), st)
    dn = f_apply(X, st)
    return F(f_ip(up, up) - f_ip(dn, dn), f_ip(st, st))


def two_flavour_mode(q, levels, idx):
    X = []
    for a in range(1, q):
        X += f_mul(f_rho(a, ('+', 1), ('-', 1), levels, idx), f_rho(q - a, ('+', 2), ('-', 2), levels, idx))
    return X


def sea_value_two_flavours(q):
    levels, idx, sea = f_setup(max(q, 1), A_CHANNELS)
    X = two_flavour_mode(q, levels, idx)
    if not X:
        return 0
    assert not f_apply(X, sea)
    return f_comm_value(X, sea)


def one_species_mode(q, levels, idx):
    V = []
    for k1 in levels:
        for k2 in levels:
            if k1 < k2:
                for l1 in levels:
                    for l2 in levels:
                        if l1 < l2 and l1 + l2 - k1 - k2 == q:
                            V.append(((k2 - k1) * (l2 - l1),
                                      [('c', idx[(k1, '+')]), ('c', idx[(k2, '+')]),
                                       ('a', idx[(l2, '-')]), ('a', idx[(l1, '-')])]))
    return V


def sea_value_one_species(q):
    levels, idx, sea = f_setup(max(2, q - 2), ['+', '-'])
    V = one_species_mode(q, levels, idx)
    assert not f_apply(V, sea)
    return f_comm_value(V, sea)


def check_sea_values_of_the_helicity_two_modes():
    """(ii): C(q+1, 3) for two flavours and C(q+3, 7) for one species; the counting identity."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    assert [sea_value_two_flavours(q) for q in range(1, 6)] == [binom(q + 1, 3) for q in range(1, 6)]
    assert [sea_value_two_flavours(q) for q in range(1, 6)] == [0, 1, 4, 10, 20]
    assert [sea_value_one_species(q) for q in range(1, 8)] == [binom(q + 3, 7) for q in range(1, 8)]
    assert [sea_value_one_species(q) for q in range(1, 8)] == [0, 0, 0, 1, 8, 36, 120]
    # a weight-one current has the value q: the pair mode of one channel on the same windows
    for q in range(1, 5):
        levels, idx, sea = f_setup(q, A_CHANNELS)
        assert f_comm_value(f_rho(q, ('+', 1), ('-', 1), levels, idx), sea) == q
    # the counting identity behind both values
    for s in range(0, 12):
        tot = sum((x2 - x1) ** 2 for x1 in range(0, s + 1) for x2 in range(x1 + 1, s + 1) if x1 + x2 == s)
        assert tot == binom(s + 2, 3)
    for q in range(4, 12):
        conv = sum(binom(s + 2, 3) * binom(q - 2 - s + 2, 3) for s in range(0, q - 1))
        assert conv == binom(q + 3, 7)
    for q in range(2, 12):
        assert sum(a * (q - a) for a in range(1, q)) == binom(q + 1, 3)
    return True


def check_commutator_of_the_composite_is_not_a_number():
    """(iii): [X_q, X_q*] on the sea and on two edge-clean one-pair vectors; X_q*^2 on the sea."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins")
    expected = {2: (1, 0, 3), 3: (4, 2, 10)}
    for q, (v_sea, v_same, v_opp) in expected.items():
        levels, idx, sea = f_setup(q + 2, A_CHANNELS)
        X = two_flavour_mode(q, levels, idx)
        same = f_apply(f_dagger(f_rho(2, ('+', 2), ('-', 2), levels, idx)), sea)
        opp = f_apply(f_dagger(f_rho(1, ('-', 2), ('+', 2), levels, idx)), sea)
        assert same and opp
        assert (f_comm_value(X, sea), f_comm_value(X, same), f_comm_value(X, opp)) == (v_sea, v_same, v_opp)
        assert v_sea == binom(q + 1, 3) and len({v_sea, v_same, v_opp}) == 3
        # control: the total density mode is a canonical boson on the same vectors
        R = []
        for c in A_CHANNELS:
            R += f_rho(q, c, c, levels, idx)
        assert {f_comm_value(R, st) for st in (sea, same, opp)} == {4 * q}
        # no second quantum
        one = f_apply(f_dagger(X), sea)
        assert f_ip(one, one) == v_sea and not f_apply(f_dagger(X), one)
    return True


# ----------------------------------------------------------------------------------------------------
# (iv) two null momenta in the spacetime algebra
# ----------------------------------------------------------------------------------------------------

ST_SQ = (1, -1, -1, -1)


def null_momentum(alpha, a, b):
    """alpha (g0 - g3) + a g1 + b g2 + ((a^2 + b^2) / (4 alpha)) (g0 + g3)."""
    beta = F(a * a + b * b) / (4 * alpha)
    return GA.add(GA.scal(F(alpha) + beta, GA.gen(0)), GA.scal(F(a), GA.gen(1)), GA.scal(F(b), GA.gen(2)),
                  GA.scal(beta - F(alpha), GA.gen(3)))


def quad(x):
    return scalar_part(GA.mul(x, x, ST_SQ))


def check_sum_of_two_null_momenta_is_null_only_when_parallel():
    """(iv): Q(p_1 + p_2) = |alpha_2 p_1perp - alpha_1 p_2perp|^2 / (alpha_1 alpha_2)."""
    premise("std-algebra.orthogonal-anticommute")
    samples = [(F(1, 2), 1, 0, F(3, 2), 0, 0), (1, 2, -1, 3, 1, 4), (F(1, 2), 0, 3, F(5, 2), -2, 1),
               (2, 1, 1, 1, -1, 2), (1, 1, 2, 2, 2, 4), (F(3, 2), 3, -3, F(1, 2), 1, -1), (1, 0, 0, 4, 0, 0)]
    n_null = 0
    for (a1, x1, y1, a2, x2, y2) in samples:
        p1, p2 = null_momentum(a1, x1, y1), null_momentum(a2, x2, y2)
        assert quad(p1) == 0 and quad(p2) == 0
        rel = (a2 * x1 - a1 * x2) ** 2 + (a2 * y1 - a1 * y2) ** 2
        assert quad(GA.add(p1, p2)) == F(rel) / (a1 * a2)
        assert quad(GA.add(p1, p2)) >= 0
        parallel = GA.eq(GA.scal(F(a2), p1), GA.scal(F(a1), p2))
        assert (quad(GA.add(p1, p2)) == 0) == parallel
        n_null += 1 if parallel else 0
    assert n_null == 3
    # a pair at one transverse point: total (alpha, P) = (2, (2, 0)), halves (1, 1), p_1perp on a grid
    count = 0
    excess = F(0)
    for x in range(-2, 3):
        for y in range(-2, 3):
            tot = GA.add(null_momentum(1, x, y), null_momentum(1, 2 - x, -y))
            count += 1 if quad(tot) == 0 else 0
            excess += quad(tot)
    assert count == 1 and excess == 4 * (75 + 50)
    return True


# ----------------------------------------------------------------------------------------------------
# (v) a causal medium with no canonical pair
# ----------------------------------------------------------------------------------------------------

M_SITES = 5
M_SQ = tuple([-1, -1, 1, -1] + [1, -1] * M_SITES)
M_J = GA.mul(GA.gen(0), GA.gen(1), M_SQ)
M_E1, M_E2 = GA.gen(2), GA.gen(3)


def m_cr(x):
    i = 4 + 2 * (x % M_SITES)
    return GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(i + 1)))


def m_an(x):
    i = 4 + 2 * (x % M_SITES)
    return GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(i + 1)))


def m_hop(x):
    return GA.add(prod(M_SQ, m_cr(x), m_an(x + 1)), prod(M_SQ, m_cr(x + 1), m_an(x)))


def m_exp(cs, h):
    """exp(-a J h) for h^3 = h at (cos a, sin a) = cs: 1 + (cos a - 1) h^2 - sin a J h."""
    c, s = cs
    return GA.add(GA.sc(1), GA.scal(c - 1, GA.mul(h, h, M_SQ)), GA.scal(-s, GA.mul(M_J, h, M_SQ)))


def check_causal_medium_commutes_exactly_and_its_response_depends_on_the_state():
    """(v): exact commutation at events whose field element commutes with the later source elements."""
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    v = GA.scal(F(1, 2), GA.add(M_E1, M_E2))
    w = GA.scal(F(1, 2), GA.sub(M_E1, M_E2))
    P1, P2 = GA.mul(v, w, M_SQ), GA.mul(w, v, M_SQ)
    assert GA.eq(GA.add(P1, P2), GA.sc(1)) and GA.is_zero(GA.mul(P1, P2, M_SQ))
    p, q = F(3, 5), F(4, 5)
    U = GA.add(GA.sc(p), GA.scal(q, M_E2))
    Uinv = GA.sub(GA.sc(p), GA.scal(q, M_E2))
    assert GA.eq(GA.mul(U, Uinv, M_SQ), GA.sc(1))
    O = prod(M_SQ, Uinv, P1, U)
    angle1, angle2 = (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))    # the kick angles on the two paths
    for x in range(M_SITES):
        h = m_hop(x)
        assert GA.eq(prod(M_SQ, h, h, h), h) and GA.eq(star(h, M_SQ), h)
        assert GA.commutes(h, M_E1, M_SQ) and GA.commutes(h, M_E2, M_SQ) and GA.commutes(h, M_J, M_SQ)
    source_times = [0, 2]

    def kick(t):
        h = m_hop(-t)                       # the medium's field at site 0 at time t
        return GA.add(GA.mul(P1, m_exp(angle1, h), M_SQ), GA.mul(P2, m_exp(angle2, h), M_SQ))

    kicks = {t: kick(t) for t in source_times}
    for K in kicks.values():
        assert GA.eq(GA.mul(K, star(K, M_SQ), M_SQ), GA.sc(1))

    def evolve(A, times):
        for t in sorted(times, reverse=True):      # A_H = K_first^* ... K_last^* A K_last ... K_first
            A = prod(M_SQ, star(kicks[t], M_SQ), A, kicks[t])
        return A

    O_H = evolve(O, source_times)
    assert not GA.eq(O_H, O)
    failing = set()
    for t in range(0, 4):
        for n in range(M_SITES):
            X = m_hop(n - t)
            field = evolve(X, [s for s in source_times if s < t])
            later = [s for s in source_times if s >= t]
            touches = any(not GA.commutes(X, m_hop(-s), M_SQ) for s in later)
            nonzero = not GA.is_zero(comm(M_SQ, field, O_H))
            assert nonzero == touches, (n, t)
            if nonzero:
                failing.add((n, t))
    assert failing == {(0, 0), (1, 0), (3, 0), (4, 0), (1, 1), (4, 1)}
    # the mean response of the field at (1, 0)'s element h_1 to one kick by h_0, on path 1
    vac = GA.sc(1)
    for x in range(M_SITES):
        vac = GA.mul(vac, GA.sub(GA.sc(1), prod(M_SQ, m_cr(x), m_an(x))), M_SQ)
    E = m_exp(angle1, m_hop(0))
    resp = prod(M_SQ, star(E, M_SQ), m_hop(1), E)
    assert scalar_part(GA.mul(resp, vac, M_SQ)) == 0
    psi_l = GA.add(m_cr(0), GA.mul(M_J, m_cr(2), M_SQ))           # (b_0* + J b_2*) on the empty medium
    rho_one = prod(M_SQ, psi_l, vac, star(psi_l, M_SQ))
    norm = scalar_part(rho_one)
    assert norm != 0
    assert scalar_part(GA.mul(m_hop(1), rho_one, M_SQ)) == 0
    assert F(scalar_part(GA.mul(resp, rho_one, M_SQ))) / norm == F(-4, 5)
    return True
