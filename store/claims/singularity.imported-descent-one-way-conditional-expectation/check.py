"""singularity.imported-descent-one-way-conditional-expectation: exact checks in Cl(p+1, q+1) (GA engine).

E is the pinching x -> PxP + (1-P)x(1-P), P = f^* f, f = (e+ + e-)/2, f^* = (e+ - e-)/2.
(1) For the six signatures with p + q <= 2: E is idempotent, unital, has image the commutant of P
    (dimension 2^(n+1)), fixes it pointwise and is a bimodule map over it: a conditional expectation.
(2) ker E = A f^* + A f (dimension 2^(n+1)), the adjoined ladder sector.
(3) No unital homomorphism B -> A: every Wedderburn block of B is larger than A (p + q <= 3).
(4) Uniqueness: for (p, q) = (0,0), (1,0), (0,1) the linear maps T : B -> B (all (dim B)^2 entries
    unknown) with T = id on the commutant C, T(B) in C, T(cx) = c T(x), T(xc) = T(x) c (c in a basis of C)
    and scalar part (normalised trace) preserved form an affine space of dimension 0, and E is its point.
    The trace condition is not needed for this finite case: the bimodule conditions alone already force
    T = E (also checked), which is the order-two instance the Fact cites.
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
from tp_premise import premise

SIGS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]


def setup(p, q):
    """B = Cl(p+1, q+1): A's generators 0..n-1, e+ = n (square +1), e- = n+1 (square -1)."""
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    f = GA.scal(F(1, 2), GA.add(ep, em))
    fs = GA.scal(F(1, 2), GA.sub(ep, em))
    P = GA.mul(fs, f, sq)
    return n, sq, f, fs, P


def mul(sq, *xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def pinch(x, P, sq):
    Q = GA.sub(GA.sc(1), P)
    return GA.add(mul(sq, P, x, P), mul(sq, Q, x, Q))


def rank(elems, m):
    rows = [GA.basis_vector_of(x, GA.all_blades(m)) for x in elems if x]
    return GA.rank_of_vectors(rows) if rows else 0


def blocks(sq, m):
    """Dimensions of the Wedderburn blocks of the (nondegenerate) Clifford algebra with squares sq."""
    cb = [b for b in GA.all_blades(m) if all(GA.commutes(GA.gen(i), {b: F(1)}, sq) for i in range(m))]
    if cb == [()]:
        return [2 ** m]
    om = {tuple(range(m)): F(1)}
    if GA.eq(GA.mul(om, om, sq), GA.sc(-1)):
        return [2 ** m]
    return [rank([GA.mul(GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(s, om))), {b: F(1)}, sq)
                  for b in GA.all_blades(m)], m) for s in (1, -1)]


def comm_basis(n, sq, f, fs):
    """A + A f f^*: the A blades and their products with f f^*."""
    ffs = GA.mul(f, fs, sq)
    base = [{b: F(1)} for b in GA.all_blades(n)]
    return base + [GA.mul(a, ffs, sq) for a in base]


def check_pinching_is_conditional_expectation():
    premise("transport.pinching-kernel")
    ok = True
    for (p, q) in SIGS:
        n, sq, f, fs, P = setup(p, q)
        m_ = n + 2
        ok = ok and GA.mul(f, f, sq) == {} and GA.mul(fs, fs, sq) == {}
        ok = ok and GA.add(GA.mul(f, fs, sq), GA.mul(fs, f, sq)) == GA.sc(1)
        ok = ok and GA.mul(P, P, sq) == P
        imgs = []
        for b in GA.all_blades(m_):
            x = {b: F(1)}
            Ex = pinch(x, P, sq)
            ok = ok and pinch(Ex, P, sq) == Ex and GA.commutes(Ex, P, sq)
            imgs.append(Ex)
        ok = ok and pinch(GA.sc(1), P, sq) == GA.sc(1)
        ok = ok and rank(imgs, m_) == 2 ** (n + 1)
        comm = [GA.sub(GA.mul({b: F(1)}, P, sq), GA.mul(P, {b: F(1)}, sq)) for b in GA.all_blades(m_)]
        ok = ok and 2 ** m_ - rank(comm, m_) == 2 ** (n + 1)
        C = comm_basis(n, sq, f, fs)
        ok = ok and rank(C, m_) == 2 ** (n + 1) and all(pinch(c, P, sq) == c for c in C)
        if n <= 1:
            for c in C:
                for c2 in C:
                    for b in GA.all_blades(m_):
                        x = {b: F(1)}
                        ok = ok and pinch(mul(sq, c, x, c2), P, sq) == mul(sq, c, pinch(x, P, sq), c2)
        else:
            for c in C[:4]:
                for c2 in C[-4:]:
                    for b in GA.all_blades(m_):
                        x = {b: F(1)}
                        ok = ok and pinch(mul(sq, c, x, c2), P, sq) == mul(sq, c, pinch(x, P, sq), c2)
    GA.check("pinching: idempotent conditional expectation onto the commutant of P (dimension 2 dim A)", ok)
    return ok


def check_kernel_is_ladder_sector():
    premise("transport.pinching-kernel")
    ok = True
    for (p, q) in SIGS:
        n, sq, f, fs, P = setup(p, q)
        m_ = n + 2
        ladder = [GA.mul({b: F(1)}, y, sq) for b in GA.all_blades(n) for y in (f, fs)]
        ok = ok and all(pinch(x, P, sq) == {} for x in ladder)
        ok = ok and rank(ladder, m_) == 2 ** (n + 1)
        imgs = [pinch({b: F(1)}, P, sq) for b in GA.all_blades(m_)]
        ok = ok and 2 ** m_ - rank(imgs, m_) == 2 ** (n + 1)
        ok = ok and pinch(f, P, sq) == {} and pinch(fs, P, sq) == {}
    GA.check("ker E = A f^* + A f, of dimension 2 dim A; E(f) = E(f^*) = 0", ok)
    return ok


def check_no_return_homomorphism():
    premise("transport.door-one-way")
    ok = True
    nsplit = 0
    for n in range(0, 4):
        for p in range(n + 1):
            q = n - p
            sqB = GA.sig(p, q) + (1, -1)
            bl = blocks(sqB, n + 2)
            if len(bl) == 2:
                nsplit += 1
                ok = ok and bl == [2 * 2 ** n, 2 * 2 ** n]
            else:
                ok = ok and bl == [4 * 2 ** n]
            ok = ok and min(bl) > 2 ** n
    ok = ok and nsplit == 3                     # (1,0), (2,1), (0,3)
    for (p, q) in SIGS:
        n, sq, f, fs, P = setup(p, q)
        ok = ok and pinch(GA.mul(f, fs, sq), P, sq) == GA.mul(f, fs, sq)
        ok = ok and GA.mul(pinch(f, P, sq), pinch(fs, P, sq), sq) == {}
        Q = GA.sub(GA.sc(1), P)
        x, y = fs, f
        D = lambda z: mul(sq, P, z, P)
        defect = GA.sub(D(GA.mul(x, y, sq)), GA.mul(D(x), D(y), sq))
        ok = ok and defect == mul(sq, P, x, Q, y, P) and defect == P
    GA.check("blocks of B exceed dim A (no unital B -> A); the pinching and the corner read-out are not multiplicative", ok)
    return ok


def lin_T(x, d, blades, pos):
    """Symbolic T(x): {output blade index: {(i, j): coeff}} for unknown T_ij (coefficient of blade i in T(blade j))."""
    out = {}
    for b, c in x.items():
        j = pos[b]
        for i in range(d):
            get_or_set(out, i, {})[(i, j)] = out.get(i, {}).get((i, j), F(0)) + c
    return out


def lin_mul(c, form, sq, blades, pos, left):
    out = {}
    for i, lf in form.items():
        for cb, cc in c.items():
            if left:
                s, b = GA.blade_mul(cb, blades[i], sq)
            else:
                s, b = GA.blade_mul(blades[i], cb, sq)
            if s == 0:
                continue
            k = pos[b]
            tgt = get_or_set(out, k, {})
            for key, v in lf.items():
                tgt[key] = tgt.get(key, F(0)) + s * cc * v
    return out


def lin_sub(f1, f2):
    out = {}
    for src, sgn in ((f1, 1), (f2, -1)):
        for k, lf in src.items():
            tgt = get_or_set(out, k, {})
            for key, v in lf.items():
                tgt[key] = tgt.get(key, F(0)) + sgn * v
    return out


def solve_space(p, q, with_trace):
    n, sq, f, fs, P = setup(p, q)
    m_ = n + 2
    blades = GA.all_blades(m_)
    d = len(blades)
    pos = {b: i for i, b in enumerate(blades)}
    unknowns = [(i, j) for i in range(d) for j in range(d)]
    col = {u: k for k, u in enumerate(unknowns)}
    rows = []

    def add_forms(forms, rhs):
        for k in range(d):
            lf = forms.get(k, {})
            row = [F(0)] * (len(unknowns) + 1)
            for key, v in lf.items():
                row[col[key]] += v
            row[-1] = rhs.get(blades[k], F(0)) if rhs is not None else F(0)
            if any(row):
                rows.append(row)
    C = comm_basis(n, sq, f, fs)
    for c in C:
        add_forms(lin_T(c, d, blades, pos), c)                        # T(c) = c
    for b in blades:
        x = {b: F(1)}
        Tx = lin_T(x, d, blades, pos)
        add_forms(lin_sub(lin_mul(P, Tx, sq, blades, pos, False), lin_mul(P, Tx, sq, blades, pos, True)), None)
        for c in C:
            add_forms(lin_sub(lin_T(GA.mul(c, x, sq), d, blades, pos), lin_mul(c, Tx, sq, blades, pos, True)), None)
            add_forms(lin_sub(lin_T(GA.mul(x, c, sq), d, blades, pos), lin_mul(c, Tx, sq, blades, pos, False)), None)
        if with_trace:
            row = [F(0)] * (len(unknowns) + 1)
            row[col[(pos[()], pos[b])]] = F(1)
            row[-1] = F(1) if b == () else F(0)
            rows.append(row)
    A = [r[:-1] for r in rows]
    rk, rk_aug = GA.field_rank(A), GA.field_rank(rows)
    Emat = {}
    for j, b in enumerate(blades):
        for bb, v in pinch({b: F(1)}, P, sq).items():
            Emat[(pos[bb], j)] = v
    sat = all(sum(r[col[u]] * Emat.get(u, F(0)) for u in unknowns) == r[-1] for r in rows)
    return d * d - rk, rk == rk_aug, sat


# Signatures (p, q) at which the full linear system for T is solved (dim B = 4, 8, 8).
UNIQ_SIGS = [(0, 0), (1, 0), (0, 1)]


def check_trace_preserving_expectation_is_unique():
    ok = True
    dims = []
    for (p, q) in UNIQ_SIGS:
        for with_trace in (True, False):
            free, consistent, sat = solve_space(p, q, with_trace)
            dims.append(free)
            ok = ok and consistent and sat
    ok = ok and dims == [0] * (2 * len(UNIQ_SIGS))
    GA.check("the trace-preserving conditional expectation onto the commutant of P is unique and equals E", ok)
    return ok
