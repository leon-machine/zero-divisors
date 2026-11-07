"""synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum: exact checks.

Tower planes only: plane j has e = gen(2j), f = gen(2j + 1), Q(e) = 1, Q(f) = -1, and the mode
a*_j = (e + f)/2, a_j = (e - f)/2 (the CAR of Fact field-theory.imported-tower-limit), n_j = a*_j a_j.
* is T03's adjoint (reversion, a sign per negative-square generator). On m planes the scalar part is the
normalised trace, so a state with density element rho has omega(X) = 2^m <rho X>_0; a gauge-invariant
product state with occupations p_j has rho = prod_j (p_j n_j + (1 - p_j)(1 - n_j)).
A block is two planes (lower mode 1, upper mode 2); hopping b = a*_1 a_2, pairing c = a_1 a_2.
(1) Single-fermion modes of distinct blocks anticommute; S = sum_i a_i has S^2 = 0, {S, S*} = N (N = 1..4);
    hopping and pairing elements of distinct blocks commute.
(2) B = sum_i a*_{1i} a_{2i}: [B, B*] = sum_i (n_{1i} - n_{2i}) = -2 K3, [K3, B*] = B*, [K3, B] = -B; the reflection f -> -f of each lower plane
    (particle-hole on the lower mode) maps B to the pairing sum of field-theory.how-close-tower-comes-ccr and
    [B, B*] to n - (N_c + N_d); on (B*)^k of the polarised state [B, B*] = N - 2k, k = 0..N, (B*)^(N+1) = 0.
(3) [b, b*] = n_1 - n_2, [c, c*] = 1 - n_1 - n_2; in product states omega([b, b*]) = p_1 - p_2,
    omega([c, c*]) = 1 - p_1 - p_2; polarised (1, 0): 1 and 0; trace: 0 and 0; Gibbs state of
    -eps n_1 + eps n_2 with y = e^(eps/T) = 2, 3, 5: p_1 = y/(1 + y), p_2 = 1/(1 + y),
    omega([b, b*]) = (y - 1)/(y + 1) = tanh(eps/2T) (1/2 at y = 3), omega([c, c*]) = 0.
(4) Even matrix units E_st of a block; sigma_omega(X, Y) = omega([X, Y]) on their span has rank
    2[p_1 != p_2] + 2[p_1 + p_2 != 1] for 25 product states and the Gibbs state; zero only for the trace
    state; zero for the tracial states lambda tau_even + (1 - lambda) tau_odd; commutators of even units span
    6 of 8 dimensions; a pure entangled state has rank 2.
(5) Density modes on M = 4, 6 modes, rho_q = sum_k a*_k a_(k+q): [rho_q, rho_q*] = (bottom q numbers) -
    (top q numbers) for q = 1..M-1; on every occupation basis state it acts as the scalar q exactly when the
    state is edge-clean (q <= M/2); omega([rho_q, rho_q*]) = sum of bottom p - sum of top p in product
    states: q on the sea, 0 for the trace state and for constant occupation 1/4, strictly between for a
    Fermi-Dirac profile.
(6) Window of 2N momentum bands of the null vacuum (N = 1..3): band averages of chi(P < 0) are 1, 0; the
    density form on {rho_q, rho_q*} is non-degenerate (rank 2(2N - 1)), diagonal min(q, 2N - q); every
    block of two window modes has a block form of rank 2; for the trace symbol 1/2 the density form is 0,
    and for constant occupation 1/4 the density form is 0 while the block form has rank 2.
(7) Fluctuations on N = 1, 2, 3 blocks in a product state: with F_N(X) = N^(-1/2) sum_k (X_k - phi(X)),
    N [F_N(Q), F_N(R)] = sum_k [Q_k, R_k] exactly; D_N = [F_N(Q), F_N(R)] - phi([Q, R]) has mean 0 and
    variance phi(D_N* D_N) - phi(D_N*) phi(D_N) = (phi(C* C) - phi(C*) phi(C))/N, C = [Q, R], for four
    pairs (Q, R) and three block states; the single-block variance is nonnegative and nonzero in most cases.
(8) On M = 6, 8 modes with the lower half filled: rho_1, rho_2 annihilate the sea; on the sea and on
    rho_1* sea (and on rho_1* rho_1* sea at depth 1), [rho_q, rho_q*] acts as q; on M = 8 the cross
    commutators [rho_1, rho_2*] and [rho_1, rho_2] annihilate the depth-2 states.
(9) The product state with occupations (1/3, 1, 0, 3/4) is the gauge-invariant quasi-free state of its
    diagonal symbol: omega(v_I w_J) = det[delta p] for |I| = |J| <= 3, and products of creators alone or of
    annihilators alone have expectation 0.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def _sig(m):
    return tuple([1, -1] * m)


def _cre(j):
    return GA.add(GA.scal(F(1, 2), GA.gen(2 * j)), GA.scal(F(1, 2), GA.gen(2 * j + 1)))


def _ann(j):
    return GA.add(GA.scal(F(1, 2), GA.gen(2 * j)), GA.scal(F(-1, 2), GA.gen(2 * j + 1)))


def _star(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        out[b] = sign * c
    return {b: c for b, c in out.items() if c != 0}


def _mk(m):
    s = _sig(m)
    mul = lambda x, y: GA.mul(x, y, s)
    num = [mul(_cre(j), _ann(j)) for j in range(m)]
    vac = GA.sc(1)
    for j in range(m):
        vac = mul(vac, mul(_ann(j), _cre(j)))
    return s, mul, num, vac


def _comm(mul, x, y):
    return GA.sub(mul(x, y), mul(y, x))


def _acomm(mul, x, y):
    return GA.add(mul(x, y), mul(y, x))


def _prod(mul, xs):
    out = GA.sc(1)
    for x in xs:
        out = mul(out, x)
    return out


def _product_state(mul, num, ps):
    return _prod(mul, [GA.add(GA.scal(p, n), GA.scal(1 - p, GA.sub(GA.sc(1), n))) for p, n in zip(ps, num)])


def _omega(mul, rho, x, m):
    return (2 ** m) * mul(rho, x).get((), F(0))


def _basis_state(mul, vac, occ):
    st = vac
    for j in reversed(range(len(occ))):
        if occ[j]:
            st = mul(_cre(j), st)
    return st


def _reflect_f(x, planes):
    """The reflection f_j -> -f_j for j in planes: an automorphism (it preserves Q)."""
    idx = {2 * j + 1 for j in planes}
    out = {}
    for b, c in x.items():
        k = sum(1 for i in b if i in idx)
        out[b] = c if k % 2 == 0 else -c
    return out


def _block_units(mul, vac, s):
    """Matrix units E_st = A_s vac A_t* of one block (two planes), s, t in {00, 10, 01, 11}."""
    cfg = [(0, 0), (1, 0), (0, 1), (1, 1)]
    A = {c: _basis_state(mul, GA.sc(1), c) for c in cfg}
    E = {(x, y): mul(mul(A[x], vac), _star(A[y], s)) for x in cfg for y in cfg}
    return cfg, E


def _form_rank(mul, rho, ops, m):
    M = [[_omega(mul, rho, _comm(mul, x, y), m) for y in ops] for x in ops]
    return GA.rank_of_vectors(M), M


def _even_units(cfg, E):
    return [E[(x, y)] for x in cfg for y in cfg if (sum(x) - sum(y)) % 2 == 0]


def check_single_fermions_collect_into_one_fermion():
    premise("field-theory.imported-tower-limit")
    premise("field-theory.no-canonical-commutation-relations-tower")
    ok = True
    for N in [1, 2, 3, 4]:
        s, mul, num, vac = _mk(N)
        S = GA.add(*[_ann(i) for i in range(N)])
        ok = ok and GA.is_zero(mul(S, S)) and GA.eq(_acomm(mul, S, _star(S, s)), GA.sc(N))
        for i in range(N):
            for j in range(N):
                if i != j:
                    ok = ok and GA.is_zero(_acomm(mul, _ann(i), _ann(j)))
                    ok = ok and GA.is_zero(_acomm(mul, _ann(i), _cre(j)))
    for N in [2, 3]:
        s, mul, num, vac = _mk(2 * N)
        hop = [mul(_cre(2 * i), _ann(2 * i + 1)) for i in range(N)]
        pair = [mul(_ann(2 * i), _ann(2 * i + 1)) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    for y in (hop[j], pair[j], _star(hop[j], s), _star(pair[j], s)):
                        ok = ok and GA.is_zero(_comm(mul, hop[i], y)) and GA.is_zero(_comm(mul, pair[i], y))
    GA.check("single-fermion collective mode is one fermion (S^2 = 0, {S, S*} = N); even block elements commute", ok)
    return ok


def check_hopping_ladder_is_the_particle_hole_image_of_the_pairing_ladder():
    premise("field-theory.imported-tower-limit")
    premise("field-theory.how-close-tower-comes-ccr")
    ok = True
    for N in [1, 2, 3, 4]:
        s, mul, num, vac = _mk(2 * N)
        B = GA.add(*[mul(_cre(2 * i), _ann(2 * i + 1)) for i in range(N)])
        Bd = _star(B, s)
        C = _comm(mul, B, Bd)
        ok = ok and GA.eq(C, GA.add(*[GA.sub(num[2 * i], num[2 * i + 1]) for i in range(N)]))
        K3 = GA.scal(F(1, 2), GA.add(*[GA.sub(num[2 * i + 1], num[2 * i]) for i in range(N)]))
        ok = ok and GA.eq(_comm(mul, K3, Bd), Bd) and GA.eq(_comm(mul, K3, B), GA.neg(B)) and GA.eq(C, GA.scal(-2, K3))
        lower = [2 * i for i in range(N)]
        pairB = GA.add(*[mul(_ann(2 * i), _ann(2 * i + 1)) for i in range(N)])
        ok = ok and GA.eq(_reflect_f(B, lower), pairB)
        ok = ok and GA.eq(_reflect_f(C, lower), GA.sub(GA.sc(N), GA.add(*num)))
        ok = ok and GA.eq(_reflect_f(C, lower), _comm(mul, pairB, _star(pairB, s)))
        st = _basis_state(mul, vac, [1 - (j % 2) for j in range(2 * N)])
        for k in range(N + 1):
            ok = ok and not GA.is_zero(st) and GA.eq(mul(C, st), GA.scal(N - 2 * k, st))
            st = mul(Bd, st)
        ok = ok and GA.is_zero(st)
    GA.check("[B, B*] = sum (n_1 - n_2); particle-hole image of the pairing quasi-spin; ladder N - 2k, N + 1 states", ok)
    return ok


def check_block_commutators_and_their_values_in_product_states():
    premise("field-theory.imported-tower-limit")
    premise("field-theory.how-close-tower-comes-ccr")
    s, mul, num, vac = _mk(2)
    b = mul(_cre(0), _ann(1))
    c = mul(_ann(0), _ann(1))
    Cb = _comm(mul, b, _star(b, s))
    Cc = _comm(mul, c, _star(c, s))
    ok = GA.eq(Cb, GA.sub(num[0], num[1])) and GA.eq(Cc, GA.sub(GA.sc(1), GA.add(num[0], num[1])))
    ps = [F(0), F(1, 4), F(1, 3), F(1, 2), F(3, 4), F(1)]
    for p1 in ps:
        for p2 in ps:
            rho = _product_state(mul, num, [p1, p2])
            ok = ok and _omega(mul, rho, GA.sc(1), 2) == 1
            ok = ok and _omega(mul, rho, Cb, 2) == p1 - p2 and _omega(mul, rho, Cc, 2) == 1 - p1 - p2
    pol = _product_state(mul, num, [F(1), F(0)])
    tr = _product_state(mul, num, [F(1, 2), F(1, 2)])
    ok = ok and (_omega(mul, pol, Cb, 2), _omega(mul, pol, Cc, 2)) == (1, 0)
    ok = ok and (_omega(mul, tr, Cb, 2), _omega(mul, tr, Cc, 2)) == (0, 0)
    for y in [F(2), F(3), F(5)]:
        g = mul(GA.add(GA.sc(1), GA.scal(y - 1, num[0])), GA.add(GA.sc(1), GA.scal(F(1) / y - 1, num[1])))
        Z = _omega(mul, g, GA.sc(1), 2)
        rho = GA.scal(F(1) / Z, g)
        ok = ok and _omega(mul, rho, num[0], 2) == y / (1 + y) and _omega(mul, rho, num[1], 2) == F(1) / (1 + y)
        ok = ok and _omega(mul, rho, Cb, 2) == (y - 1) / (y + 1) and _omega(mul, rho, Cc, 2) == 0
        if y == 3:
            ok = ok and _omega(mul, rho, Cb, 2) == F(1, 2)
    GA.check("[b, b*] = n1 - n2, [c, c*] = 1 - n1 - n2; values p1 - p2, 1 - p1 - p2; Gibbs tanh(eps/2T)", ok)
    return ok


def check_block_form_rank_and_its_tracial_kernel():
    premise("field-theory.imported-tower-limit")
    s, mul, num, vac = _mk(2)
    cfg, E = _block_units(mul, vac, s)
    ok = True
    for x in cfg:
        for y in cfg:
            for z in cfg:
                for w in cfg:
                    want = E[(x, w)] if y == z else {}
                    ok = ok and GA.eq(mul(E[(x, y)], E[(z, w)]), want)
    ev = _even_units(cfg, E)
    ok = ok and len(ev) == 8
    comms = [_comm(mul, x, y) for x in ev for y in ev]
    blades = sorted({bl for x in ev for bl in x})
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in comms]) == 6
    ps = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
    states = [(p1, p2) for p1 in ps for p2 in ps] + [(F(3, 4), F(1, 4))]
    for p1, p2 in states:
        r, _M = _form_rank(mul, _product_state(mul, num, [p1, p2]), ev, 2)
        ok = ok and r == 2 * (p1 != p2) + 2 * (p1 + p2 != 1)
        ok = ok and ((r == 0) == (p1 == p2 == F(1, 2)))
    for lam in [F(0), F(1, 3), F(1)]:
        rho = GA.add(GA.scal(lam / 2, GA.add(E[(cfg[0], cfg[0])], E[(cfg[3], cfg[3])])),
                     GA.scal((1 - lam) / 2, GA.add(E[(cfg[1], cfg[1])], E[(cfg[2], cfg[2])])))
        r, _M = _form_rank(mul, rho, ev, 2)
        ok = ok and _omega(mul, rho, GA.sc(1), 2) == 1 and r == 0
    ent = GA.scal(F(1, 2), GA.add(E[(cfg[0], cfg[0])], E[(cfg[0], cfg[3])], E[(cfg[3], cfg[0])], E[(cfg[3], cfg[3])]))
    ok = ok and GA.eq(mul(ent, ent), ent) and _form_rank(mul, ent, ev, 2)[0] == 2
    GA.check("block form rank 2[p1 != p2] + 2[p1 + p2 != 1]; zero exactly on the tracial states", ok)
    return ok


def check_density_form_edge_operator_converse_and_product_values():
    premise("synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off")
    premise("hawking.current-commutator-exactly-edge-split")
    ok = True
    fd_total = F(0)
    clean_count = 0
    for M in [4, 6]:
        s, mul, num, vac = _mk(M)
        occs = [[(c >> j) & 1 for j in range(M)] for c in range(2 ** M)]
        basis = [_basis_state(mul, vac, o) for o in occs]
        sea = _product_state(mul, num, [F(1) if k < M // 2 else F(0) for k in range(M)])
        flat = [_product_state(mul, num, [F(v)] * M) for v in (F(1, 2), F(1, 4))]
        fd_p = [F(1) / (1 + F(2) ** (2 * k - M + 1)) for k in range(M)]
        fd = _product_state(mul, num, fd_p)
        for q in range(1, M):
            r = GA.add(*[mul(_cre(k), _ann(k + q)) for k in range(M - q)])
            C = _comm(mul, r, _star(r, s))
            D = GA.sub(GA.add(*[num[k] for k in range(q)]), GA.add(*[num[k] for k in range(M - q, M)]))
            ok = ok and GA.eq(C, D)
            if 2 * q <= M:
                for o, st in zip(occs, basis):
                    d = sum(o[:q]) - sum(o[M - q:])
                    clean = all(o[k] == 1 for k in range(q)) and all(o[k] == 0 for k in range(M - q, M))
                    ok = ok and GA.eq(mul(C, st), GA.scal(d, st)) and ((d == q) == clean)
                    clean_count += clean
            ok = ok and _omega(mul, sea, C, M) == min(q, M - q)
            ok = ok and all(_omega(mul, f, C, M) == 0 for f in flat)
            v = _omega(mul, fd, C, M)
            fd_total += v
            ok = ok and v == sum(fd_p[:q]) - sum(fd_p[M - q:])
            if 2 * q <= M:
                ok = ok and 0 < v < q
    # pinned: edge-clean states 2^(M - 2q) summed over M = 4 (q = 1, 2) and M = 6 (q = 1, 2, 3); Fermi-Dirac total
    ok = ok and clean_count == 4 + 1 + 16 + 4 + 1 and fd_total == F(331, 33)
    ok = ok and _omega(mul, flat[1], num[0], 6) == F(1, 4) and _omega(mul, flat[0], num[5], 6) == F(1, 2)
    GA.check("[rho_q, rho_q*] = bottom - top; scalar q exactly on edge-clean states; product-state values", ok)
    return ok


def check_null_vacuum_window_has_nondegenerate_density_and_block_forms():
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    premise("synthesis.floor-regulator-keeps-the-charge-and-the-central-term-below-the-cut-off")
    ok = True
    for N in [1, 2, 3]:
        M = 2 * N
        s, mul, num, vac = _mk(M)
        bands = list(range(-N, N))
        # band average of the symbol chi(P < 0) over [k, k + 1): the length of [k, k + 1) below 0
        occ = [max(F(0), min(F(1), F(-k))) for k in bands]
        ok = ok and occ == [F(1)] * N + [F(0)] * N
        dens = []
        for q in range(1, M):
            r = GA.add(*[mul(_cre(k), _ann(k + q)) for k in range(M - q)])
            dens += [r, _star(r, s)]
        for ps, want in ((occ, 2 * (M - 1)), ([F(1, 2)] * M, 0), ([F(1, 4)] * M, 0)):
            rho = _product_state(mul, num, ps)
            r, G = _form_rank(mul, rho, dens, M)
            ok = ok and r == want
            if want:
                ok = ok and all(G[2 * (q - 1)][2 * (q - 1) + 1] == min(q, M - q) for q in range(1, M))
        for ps, want in ((occ, 2), ([F(1, 4)] * M, 2), ([F(1, 2)] * M, 0)):
            rho = _product_state(mul, num, ps)
            for k in range(M - 1):
                cfgu = []
                for x in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                    for y in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                        if (sum(x) - sum(y)) % 2 == 0:
                            ax = _prod(mul, [_cre(k + i) for i in range(2) if x[i]])
                            ay = _prod(mul, [_cre(k + i) for i in range(2) if y[i]])
                            pv = mul(mul(_ann(k), _cre(k)), mul(_ann(k + 1), _cre(k + 1)))
                            cfgu.append(mul(mul(ax, pv), _star(ay, s)))
                ok = ok and _form_rank(mul, rho, cfgu, M)[0] == want
    GA.check("null-vacuum window: density form non-degenerate, diagonal min(q, 2N - q); blocks rank 2; trace 0", ok)
    return ok


def check_fluctuation_commutator_tends_to_the_form():
    premise("field-theory.imported-tower-limit")
    ok = True
    positive = 0
    s1, mul1, num1, vac1 = _mk(2)
    cfg, E = _block_units(mul1, vac1, s1)
    b = mul1(_cre(0), _ann(1))
    c = mul1(_ann(0), _ann(1))
    pairs = [(GA.add(b, _star(b, s1)), GA.sub(b, _star(b, s1))),
             (GA.add(c, _star(c, s1)), num1[0]),
             (E[(cfg[1], cfg[2])], E[(cfg[0], cfg[3])]),
             (E[(cfg[0], cfg[3])], E[(cfg[3], cfg[0])])]
    for p1, p2 in [(F(3, 4), F(1, 4)), (F(1), F(0)), (F(1, 3), F(3, 4))]:
        rho1 = _product_state(mul1, num1, [p1, p2])
        for Q, R in pairs:
            C = _comm(mul1, Q, R)
            sig = _omega(mul1, rho1, C, 2)
            var1 = _omega(mul1, rho1, mul1(_star(C, s1), C), 2) - _omega(mul1, rho1, _star(C, s1), 2) * sig
            for N in [1, 2, 3]:
                s, mul, num, vac = _mk(2 * N)
                sh = lambda x, i: {tuple(j + 4 * i for j in bl): v for bl, v in x.items()}
                rho = _product_state(mul, num, [p1, p2] * N)
                qQ, qR = _omega(mul1, rho1, Q, 2), _omega(mul1, rho1, R, 2)
                SQ = GA.add(*[GA.sub(sh(Q, i), GA.sc(qQ)) for i in range(N)])
                SR = GA.add(*[GA.sub(sh(R, i), GA.sc(qR)) for i in range(N)])
                lhs = GA.scal(F(1, N), _comm(mul, SQ, SR))
                ok = ok and GA.eq(lhs, GA.scal(F(1, N), GA.add(*[sh(C, i) for i in range(N)])))
                D = GA.sub(lhs, GA.sc(sig))
                ok = ok and _omega(mul, rho, D, 2 * N) == 0
                var = _omega(mul, rho, mul(_star(D, s), D), 2 * N) - _omega(mul, rho, _star(D, s), 2 * N) * _omega(mul, rho, D, 2 * N)
                ok = ok and var == var1 / (N * N)
            ok = ok and var1 >= 0
            positive += var1 > 0
    ok = ok and positive >= 6
    GA.check("[F_N(Q), F_N(R)] = (1/N) sum [Q_k, R_k] = sigma(Q, R) + D_N, D_N mean 0, variance (phi(C*C) - |phi(C)|^2)/N", ok)
    return ok


def check_finite_excitations_of_a_deep_sea_see_the_canonical_relation():
    premise("hawking.current-commutator-exactly-edge-split")
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    ok = True
    for M in [6, 8]:
        s, mul, num, vac = _mk(M)
        h = M // 2
        rho = {q: GA.add(*[mul(_cre(k), _ann(k + q)) for k in range(M - q)]) for q in (1, 2)}
        sea = _basis_state(mul, vac, [1] * h + [0] * h)
        ok = ok and GA.is_zero(mul(rho[1], sea)) and GA.is_zero(mul(rho[2], sea))
        exc = [sea, mul(_star(rho[1], s), sea)]
        exc.append(mul(_star(rho[1], s), exc[1]))
        for depth, psis in ((2, exc[:2]), (1, exc)):
            for psi in psis:
                ok = ok and not GA.is_zero(psi)
                for q in range(1, depth + 1):
                    C = _comm(mul, rho[q], _star(rho[q], s))
                    ok = ok and GA.eq(mul(C, psi), GA.scal(q, psi))
                if depth == 2 and M == 8:
                    X = _comm(mul, rho[1], _star(rho[2], s))
                    ok = ok and GA.is_zero(mul(X, psi)) and GA.is_zero(mul(_comm(mul, rho[1], rho[2]), psi))
    GA.check("on finite excitations of a deep sea [rho_q, rho_q*] = q, cross commutators 0: the canonical relation", ok)
    return ok


def check_product_state_is_the_quasi_free_state_of_its_symbol():
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    ok = True
    M = 4
    ps = [F(1, 3), F(1), F(0), F(3, 4)]
    s, mul, num, vac = _mk(M)
    rho = _product_state(mul, num, ps)
    from itertools import combinations, permutations
    count = 0
    for k in [1, 2, 3]:
        for I in combinations(range(M), k):
            for J in combinations(range(M), k):
                X = _prod(mul, [_cre(i) for i in I] + [_ann(j) for j in reversed(J)])
                det = F(0)
                for perm in permutations(range(k)):
                    inv = sum(1 for a in range(k) for b in range(a + 1, k) if perm[a] > perm[b])
                    t = F((-1) ** inv)
                    for a in range(k):
                        t *= ps[I[a]] if I[a] == J[perm[a]] else 0
                    det += t
                ok = ok and _omega(mul, rho, X, M) == det
                count += 1
        for I in combinations(range(M), k):
            ok = ok and _omega(mul, rho, _prod(mul, [_cre(i) for i in I]), M) == 0
            ok = ok and _omega(mul, rho, _prod(mul, [_ann(i) for i in I]), M) == 0
    ok = ok and count == 68
    n03 = mul(mul(_cre(0), _cre(3)), mul(_ann(3), _ann(0)))
    ok = ok and _omega(mul, rho, n03, M) == F(1, 4) and _omega(mul, rho, num[0], M) == F(1, 3)
    ok = ok and _omega(mul, rho, mul(num[1], num[3]), M) == F(3, 4) and _omega(mul, rho, num[2], M) == 0
    GA.check("product state = gauge-invariant quasi-free state of diag(p): Wick determinants, odd and unbalanced 0", ok)
    return ok
