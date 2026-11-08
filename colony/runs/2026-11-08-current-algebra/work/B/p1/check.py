"""Exact checks: the gauge currents of a generation along a null generator do not see its anomaly cancellation.

Internal module: V = Lambda C^5, modes 0, 1 the slots and 2, 3, 4 the pairs; occupation states are sorted
tuples S; the gauge algebra g = s(u(2) + u(3)) acts by the bilinears sum t_ij a*_i a_j; Y = (3n - 2k)/6.
Numbers are read in span{1, J}, J = g_1 g_2 the kernel bivector (generators 0, 1, squares -1).
Window: channels x (occupation states of chosen components), levels k = 0, ..., L - 1; mode (x, k) is the
tower plane (e, f), squares (+1, -1), a* = v = (e + f)/2, a = w = (e - f)/2.
rho_q(M) = sum_{k, k+q} sum_{x,y} M_xy a*_{x,k} a_{y,k+q} (the stored matrix form of the pair currents).

(i)   partner blocks: on each conjugate pair of components, in the complement basis with the signs
      eps(S) of a*_S a*_{S^c} Omega = eps(S) a*_0 ... a*_4 Omega, rho_B(t) = -rho_A(t)^T for all twelve generators;
(ii)  the particle-hole reversal phi_C (e_{x,k} -> e_{x,L-1-k}, f_{x,k} -> -f_{x,L-1-k} on swapped
      channels) is Ad(u_x) for an even product u_x of eight vectors, maps n_{x,k} to 1 - n_{x,L-1-k},
      fixes the centred energy, and maps rho_q(M) to rho_q(-M^T) + delta_{q0} L tr M exactly;
(iii) over the 32 sign patterns of gauge-commuting halvings the trace form of g on V_+ is the same
      (4 times the trace form on C^5), while the anomaly coefficients vanish for exactly two patterns;
(iv)  the abelian level as a number depends on the scale of Y; the ratios do not;
(v)   tr Y over V_+ (the mixed gravitational coefficient) is the hypercharge constant of (ii) as a difference of the
      seas' hypercharges and the Y-N mixed central term; it vanishes on 8 of the 32 patterns, 2 of them anomaly-free.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F
from itertools import combinations, product
import GA
from tp_premise import premise

# ---------------------------------------------------------------- the internal module
STATES = [S for r in range(6) for S in combinations(range(5), r)]
CONJ_PAIRS = [((1, 0), (1, 3)), ((2, 0), (0, 3)), ((0, 1), (2, 2)), ((1, 1), (1, 2)), ((2, 1), (0, 2))]


def nk(S):
    n = sum(1 for x in S if x < 2)
    return n, len(S) - n


def hyper(S):
    n, k = nk(S)
    return F(3 * n - 2 * k, 6)


def component(c):
    return [S for S in STATES if nk(S) == c]


def complement(S):
    return tuple(x for x in range(5) if x not in S)


def eps(S):
    seq = list(S) + list(complement(S))
    inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])
    return (-1) ** inv


def ann(j, S):
    if j not in S:
        return None
    return (-1) ** S.index(j), tuple(x for x in S if x != j)


def cre(i, S):
    if i in S:
        return None
    return (-1) ** sum(1 for x in S if x < i), tuple(sorted(S + (i,)))


# ---------------------------------------------------------------- numbers span{1, J}
def window_squares(nmodes):
    return tuple([-1, -1] + [1, -1] * nmodes)


SQ5 = window_squares(0)


def jnum(re, im, sq):
    return GA.add(GA.sc(re), GA.scal(im, GA.mul(GA.gen(0), GA.gen(1), sq)))


def gauge_generators(sq):
    """Twelve generators of s(u(2) + u(3)) as 5 x 5 matrices {(i, j): number}, anti-Hermitian."""
    one = GA.sc(1)
    J = GA.mul(GA.gen(0), GA.gen(1), sq)
    mj = GA.neg(one)
    gens = []
    for (a, b) in [(0, 1)] + [(2, 3), (2, 4), (3, 4)]:
        gens.append({(a, b): one, (b, a): mj})
        gens.append({(a, b): J, (b, a): J})
    gens.append({(0, 0): J, (1, 1): GA.neg(J)})
    gens.append({(2, 2): J, (3, 3): GA.neg(J)})
    gens.append({(3, 3): J, (4, 4): GA.neg(J)})
    gens.append({(i, i): GA.scal(F(1, 2) if i < 2 else F(-1, 3), J) for i in range(5)})
    return gens


def induced(t, rows, cols, sq, signs=None):
    """Matrix <R| sum t_ij a*_i a_j |S> on the given occupation states, as {(r, c): number}."""
    out = {}
    for c_i, S in enumerate(cols):
        for (i, j), coef in t.items():
            r1 = ann(j, S)
            if r1 is None:
                continue
            s1, S1 = r1
            r2 = cre(i, S1)
            if r2 is None:
                continue
            s2, S2 = r2
            if S2 in rows:
                r_i = rows.index(S2)
                sgn = s1 * s2
                if signs is not None:
                    sgn *= signs[r_i] * signs[c_i]
                out[(r_i, c_i)] = GA.add(out.get((r_i, c_i), {}), GA.scal(sgn, coef))
    return {k: v for k, v in out.items() if not GA.is_zero(v)}


def mat_eq(A, B):
    keys = set(A) | set(B)
    return all(GA.eq(A.get(k, {}), B.get(k, {})) for k in keys)


def neg_transpose(A):
    return {(c, r): GA.neg(v) for (r, c), v in A.items()}


def trace_form(A, B, n, sq):
    out = {}
    for i in range(n):
        for j in range(n):
            if (i, j) in A and (j, i) in B:
                out = GA.add(out, GA.mul(A[(i, j)], B[(j, i)], sq))
    return out


# ---------------------------------------------------------------- window algebra
def window(channels, L):
    nmodes = channels * L
    sq = window_squares(nmodes)
    pos = {(x, k): 2 + 2 * (x * L + k) for x in range(channels) for k in range(L)}
    return sq, pos


def cr(pos, md):
    i = pos[md]
    return GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(i + 1)))


def an(pos, md):
    i = pos[md]
    return GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(i + 1)))


def rho(q, M, pos, L, sq):
    out = {}
    for k in range(L):
        if 0 <= k + q < L:
            for (x, y), c in M.items():
                out = GA.add(out, GA.mul(c, GA.mul(cr(pos, (x, k)), an(pos, (y, k + q)), sq), sq))
    return out


def phi_images(pos, L, swapped):
    """Images of the generators under the particle-hole reversal on the swapped channels."""
    img = {}
    for (x, k), i in pos.items():
        if x in swapped:
            j = pos[(x, L - 1 - k)]
            img[i] = GA.gen(j)
            img[i + 1] = GA.neg(GA.gen(j + 1))
    return img


def adjoint(x, sq):
    out = {}
    for b, c in x.items():
        k = len(b)
        s = (-1) ** (k * (k - 1) // 2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        out[b] = c * s
    return out


def apply_auto(x, img, sq):
    out = {}
    for blade, c in x.items():
        term = GA.sc(c)
        for g in blade:
            term = GA.mul(term, img.get(g, GA.gen(g)), sq)
        out = GA.add(out, term)
    return out


# ---------------------------------------------------------------- checks
def check_partner_blocks_are_minus_transposes():
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    sq = SQ5
    gens = gauge_generators(sq)
    ok = len(gens) == 12 and len(STATES) == 32
    sizes = []
    for A, B in CONJ_PAIRS:
        SA = component(A)
        SB = [complement(S) for S in SA]
        signs = [eps(S) for S in SA]
        sizes.append(len(SA))
        ok = ok and sorted(SB) == sorted(component(B))
        for t in gens:
            MA = induced(t, SA, SA, sq)
            MB = induced(t, SB, SB, sq, signs)
            ok = ok and mat_eq(MB, neg_transpose(MA))
            # anti-Hermitian over span{1, J}: M* = -M with J -> -J
            star = {(c, r): GA.reverse(v) for (r, c), v in MA.items()}
            ok = ok and mat_eq(star, {k: GA.neg(v) for k, v in MA.items()})
    ok = ok and sorted(sizes) == [1, 2, 3, 3, 6]
    # every generator preserves the component (block diagonal), so its currents conserve each channel block
    for t in gens:
        full = induced(t, STATES, STATES, sq)
        ok = ok and all(nk(STATES[r]) == nk(STATES[c]) for (r, c) in full)
    # the trace on a component: zero for the semisimple generators, J dim Y for the hypercharge
    for A, _ in CONJ_PAIRS:
        SA = component(A)
        for t in gens[:11]:
            MA = induced(t, SA, SA, sq)
            ok = ok and GA.is_zero(GA.add(*[MA.get((i, i), {}) for i in range(len(SA))]))
        MY = induced(gens[11], SA, SA, sq)
        trY = GA.add(*[MY.get((i, i), {}) for i in range(len(SA))])
        ok = ok and GA.eq(trY, jnum(0, len(SA) * hyper(SA[0]), sq))
    GA.check("partner components carry -M^T in the complement basis; traces as stated", ok)
    return ok


def check_particle_hole_reversal_intertwines_window_currents():
    premise("synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins")
    premise("std-algebra.witt-basis-car")
    premise("synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves")
    L = 4
    chans = component((1, 0)) + component((0, 1))
    partners = [complement(S) for S in chans]
    signs = [eps(S) for S in chans]
    n = len(chans)
    sq, pos = window(n, L)
    gens = gauge_generators(sq)
    ok = n == 5
    for swapped in [set(range(n)), {0, 1}, {2, 3, 4}]:
        img = phi_images(pos, L, swapped)
        # the images are an orthonormal set with the same squares: an automorphism
        for i, v in img.items():
            ok = ok and GA.eq(GA.mul(v, v, sq), GA.sc(sq[i]))
            # commutes with the adjoint (fixes square +1 generators, negates square -1 ones)
            ok = ok and GA.eq(adjoint(v, sq), GA.scal(sq[i], v))
        # Ad(u_x) for one swapped channel, u_x a product of eight vectors
        x = min(swapped)
        vecs = [GA.gen(pos[(x, k)] + 1) for k in range(L)]
        for k in range(L // 2):
            a, b = pos[(x, k)], pos[(x, L - 1 - k)]
            vecs.append(GA.sub(GA.gen(a), GA.gen(b)))
            vecs.append(GA.sub(GA.gen(a + 1), GA.gen(b + 1)))
        u = GA.sc(1)
        for v in vecs:
            u = GA.mul(u, v, sq)
        norm = GA.mul(u, GA.reverse(u), sq)
        ok = ok and GA.eq(norm, GA.sc(16))
        uinv = GA.scal(F(1, 16), GA.reverse(u))
        for k in range(L):
            for g in (pos[(x, k)], pos[(x, k)] + 1):
                ok = ok and GA.eq(GA.mul(GA.mul(u, GA.gen(g), sq), uinv, sq), img[g])
        other = pos[(max(set(range(n)) - swapped), 0)] if swapped != set(range(n)) else 0
        ok = ok and GA.eq(GA.mul(GA.mul(u, GA.gen(other), sq), uinv, sq), GA.gen(other))
        # number operators and the centred energy
        energy = {}
        for (y, k) in pos:
            nyk = GA.mul(cr(pos, (y, k)), an(pos, (y, k)), sq)
            energy = GA.add(energy, GA.scal(F(2 * k - (L - 1), 2), nyk))
            if y in swapped:
                target = GA.sub(GA.sc(1), GA.mul(cr(pos, (y, L - 1 - k)), an(pos, (y, L - 1 - k)), sq))
                ok = ok and GA.eq(apply_auto(nyk, img, sq), target)
        ok = ok and GA.eq(apply_auto(energy, img, sq), energy)
        # the currents of the twelve generators
        for t in gens:
            M = induced(t, chans, chans, sq)
            Mp = induced(t, partners, partners, sq, signs)
            Mnew = {(r, c): v for (r, c), v in M.items() if r not in swapped}
            Mnew.update({(r, c): v for (r, c), v in Mp.items() if r in swapped})
            trs = GA.add(*[M.get((i, i), {}) for i in swapped])
            for q in range(L):
                lhs = apply_auto(rho(q, M, pos, L, sq), img, sq)
                rhs = rho(q, Mnew, pos, L, sq)
                if q == 0:
                    rhs = GA.add(rhs, GA.scal(L, trs))
                ok = ok and GA.eq(lhs, rhs)
    GA.check("particle-hole reversal is inner, keeps the sea and energy, and maps the currents", ok)
    return ok


def charges(S):
    n, k = nk(S)
    t3 = sum(F(1, 2) if i == 0 else F(-1, 2) for i in S if i < 2)
    h3 = sum({2: F(1, 2), 3: F(-1, 2), 4: F(0)}[i] for i in S if i >= 2)
    h8 = sum({2: F(1), 3: F(1), 4: F(-2)}[i] for i in S if i >= 2)
    return t3, h3, h8, hyper(S)


def check_trace_form_is_halving_independent_and_anomalies_are_not():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("synthesis.spin10-clause-content-is-the-neutral-singlet-choice")
    sq = SQ5
    gens = gauge_generators(sq)
    base = [list(range(5))]
    gram5 = [[trace_form(induced(a, [(i,) for i in range(5)], [(i,) for i in range(5)], sq),
                         induced(b, [(i,) for i in range(5)], [(i,) for i in range(5)], sq), 5, sq)
              for b in gens] for a in gens]
    ok = len(base) == 1
    free = []
    for signs in product([0, 1], repeat=5):
        Vp = list(component((0, 0)))
        for s, (A, B) in zip(signs, CONJ_PAIRS):
            Vp += component(A if s == 0 else B)
        ok = ok and len(Vp) == 16
        mats = [induced(t, Vp, Vp, sq) for t in gens]
        for a in range(12):
            for b in range(12):
                ok = ok and GA.eq(trace_form(mats[a], mats[b], 16, sq), GA.scal(4, gram5[a][b]))
        ch = [charges(S) for S in Vp]
        anomalies = (sum(y for *_, y in ch),                       # mixed gravitational
                     sum(y ** 3 for *_, y in ch),                  # U(1)^3
                     sum(y * t3 * t3 for t3, _, _, y in ch),       # SU(2)^2 U(1)
                     sum(y * h3 * h3 for _, h3, _, y in ch))       # SU(3)^2 U(1)
        cubic = sum(h8 ** 3 for _, _, h8, _ in ch)                 # SU(3)^3
        levels = (sum(t3 * t3 for t3, _, _, _ in ch), sum(h3 * h3 for _, h3, _, _ in ch),
                  sum(y * y for *_, y in ch))
        ok = ok and levels == (2, 2, F(10, 3))
        doublets = sum(1 for S in Vp if nk(S)[0] == 1) // 2
        ok = ok and doublets == 4
        if all(a == 0 for a in anomalies):
            free.append(signs)
            ok = ok and cubic == 0
            parities = {(sum(nk(S)) % 2) for S in Vp if S not in ((), (0, 1, 2, 3, 4))}
            ok = ok and len(parities) == 1
    ok = ok and len(free) == 2 and free[0] == tuple(1 - s for s in free[1])
    GA.check("trace form 4 tr_5 on all 32 halvings; anomaly-free exactly for the two parities", ok)
    return ok


def check_abelian_level_depends_on_the_scale_of_y():
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    Vp = [S for S in STATES if sum(nk(S)) % 2 == 0]
    ch = [charges(S) for S in Vp]
    t3sq = sum(t3 * t3 for t3, _, _, _ in ch)
    ysq = sum(y * y for *_, y in ch)
    qsq = sum((t3 + y) ** 2 for t3, _, _, y in ch)
    y5 = 2 * F(1, 2) ** 2 + 3 * F(1, 3) ** 2
    ok = len(Vp) == 16 and t3sq == 2 and ysq == F(10, 3) and qsq == F(16, 3)
    ok = ok and ysq / y5 == 4 and t3sq / (2 * F(1, 4)) == 4
    ok = ok and t3sq / qsq == F(3, 8) and ysq / t3sq == F(5, 3)
    integral = [6 * y for *_, y in ch]
    ok = ok and all(v.denominator == 1 for v in integral) and sum(v * v for v in integral) == 120
    third = [3 * (t3 + y) for t3, _, _, y in ch]
    ok = ok and all(v.denominator == 1 for v in third) and sum(v * v for v in third) == 48
    gcd = 0
    for v in integral:
        a, b = abs(int(v)), gcd
        while b:
            a, b = b, a % b
        gcd = a
    ok = ok and gcd == 1
    for lam in (F(2), F(1, 6), F(3, 5)):
        ok = ok and sum((lam * y) ** 2 for *_, y in ch) == lam * lam * ysq
    GA.check("abelian level 10/3, 4, 120 by normalisation; ratios 3 : 5 : 8 fixed", ok)
    return ok


def check_hypercharge_constant_is_the_linear_anomaly_coefficient():
    premise("synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins")
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    # (a) tr Y over V_+ on the 32 sign patterns: values, the 24 / 8 / 2 counts
    dimy = {}
    for A, B in CONJ_PAIRS:
        dimy[A] = sum(hyper(S) for S in component(A))
        dimy[B] = sum(hyper(S) for S in component(B))
    ok = [dimy[A] for A, _ in CONJ_PAIRS] == [1, 1, -1, 1, 2]
    ok = ok and all(dimy[B] == -dimy[A] for A, B in CONJ_PAIRS)
    traces, zero, free = {}, [], []
    for signs in product([0, 1], repeat=5):
        Vp = list(component((0, 0)))
        for s, (A, B) in zip(signs, CONJ_PAIRS):
            Vp += component(A if s == 0 else B)
        ch = [charges(S) for S in Vp]
        tr = sum(y for *_, y in ch)
        traces[signs] = tr
        anomalies = (tr, sum(y ** 3 for *_, y in ch), sum(y * t3 * t3 for t3, _, _, y in ch),
                     sum(y * h3 * h3 for _, h3, _, y in ch))
        if tr == 0:
            zero.append(signs)
        if all(a == 0 for a in anomalies):
            free.append(signs)
    ok = ok and set(traces.values()) == {-6, -4, -2, 0, 2, 4, 6}
    ok = ok and len(zero) == 8 and len(traces) - len(zero) == 24
    ok = ok and len(free) == 2 and all(f in zero for f in free)
    # the constant L tr_C Y of the reversal is the difference of the seas' hypercharges (L / 2) tr Y
    L = 2
    for signs, tr in traces.items():
        for i, (A, B) in enumerate(CONJ_PAIRS):
            other = tuple(1 - s if j == i else s for j, s in enumerate(signs))
            Cc = A if signs[i] == 0 else B
            ok = ok and F(L, 2) * tr - F(L, 2) * traces[other] == L * dimy[Cc]
    # (b) on a window L = 2 with the channels of V_{1,0} and V_{2,0}: the sea's hypercharge and the Y-N central term
    chans = component((1, 0)) + component((2, 0))
    n = len(chans)
    sq, pos = window(n, L)
    J = GA.mul(GA.gen(0), GA.gen(1), sq)
    MY = induced(gauge_generators(sq)[11], chans, chans, sq)
    one = {(x, x): GA.sc(1) for x in range(n)}
    sea = GA.sc(1)
    for x in range(n):
        sea = GA.mul(sea, GA.mul(cr(pos, (x, 0)), an(pos, (x, 0)), sq), sq)
        sea = GA.mul(sea, GA.mul(an(pos, (x, 1)), cr(pos, (x, 1)), sq), sq)
    trY = sum(hyper(S) for S in chans)
    ok = ok and n == 3 and trY == 2
    charge = GA.mul(rho(0, MY, pos, L, sq), sea, sq)
    ok = ok and GA.eq(charge, GA.mul(GA.scal(F(L, 2) * trY, J), sea, sq))
    r1 = rho(1, MY, pos, L, sq)
    r1n = adjoint(rho(1, one, pos, L, sq), sq)
    mixed = GA.sub(GA.mul(r1, r1n, sq), GA.mul(r1n, r1, sq))
    ok = ok and GA.eq(GA.mul(mixed, sea, sq), GA.mul(GA.scal(trY, J), sea, sq))
    ok = ok and not GA.is_zero(GA.mul(mixed, sea, sq))
    GA.check("tr Y: values 0, +-2, +-4, +-6, zero on 8 of 32, the 2 anomaly-free among them; sea charge and Y-N term", ok)
    return ok


if __name__ == "__main__":
    for fn in (check_partner_blocks_are_minus_transposes,
               check_particle_hole_reversal_intertwines_window_currents,
               check_trace_form_is_halving_independent_and_anomalies_are_not,
               check_abelian_level_depends_on_the_scale_of_y,
               check_hypercharge_constant_is_the_linear_anomaly_coefficient):
        fn()
