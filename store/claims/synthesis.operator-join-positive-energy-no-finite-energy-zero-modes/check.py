"""synthesis.operator-join-positive-energy-no-finite-energy-zero-modes: exact checks.

The positive-energy (oscillator) realisation of the palatial oscillators of two constituents i = 0, 1:
per constituent two a-modes (variables x_{iA}, A = 0, 1; a_A = d/dx_A, a_A* = x_A) and two b-modes
(variables y_{iA}; b_A = d/dy_A, b_A* = y_A), Fock inner product <x^m y^n, x^m y^n> = m! n!.
With hbar = 2 (so that no square roots enter):
  omega^A = Z^A = d/dx_A + y_A,   pi_{A'} = Z^{A+2} = d/dx_A - y_A,
  Zbar_A = x_A - d/dy_A,          Zbar_{A+2} = x_A + d/dy_A,
so [Z^alpha, Zbar_beta] = hbar delta, (Z^alpha)* = Zbar_{sigma(alpha)} with sigma = (0 2)(1 3), the
stored twistor conjugation. Stored objects (synthesis.operator-join-ordering-constants, palatial form):
B = <pi^1 pi^2> + lam [omega^1 omega^2], lam = Lambda/6, B-dagger its conjugate, h_il the symmetrised
Gram operators, C = (1/2) sum h_il h_li - (1/4)(tr h)^2,
m2 = B-dagger B + B B-dagger + (Lambda/3) C - (2 Lambda/3) hbar^2.
Polynomials are dicts {exponent tuple: Fraction}; operators are functions on them. Exact throughout.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

HBAR = F(2)
LAM = F(3)
lam = LAM / 6
NV = 8


def xv(i, A):
    return 4 * i + A


def yv(i, A):
    return 4 * i + 2 + A


def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def pscale(c, p):
    return {k: c * v for k, v in p.items() if c * v != 0}


def mul(j, p):
    out = {}
    for k, v in p.items():
        kk = list(k)
        kk[j] += 1
        out[tuple(kk)] = out.get(tuple(kk), F(0)) + v
    return out


def der(j, p):
    out = {}
    for k, v in p.items():
        if k[j]:
            kk = list(k)
            kk[j] -= 1
            out[tuple(kk)] = out.get(tuple(kk), F(0)) + k[j] * v
    return {k: v for k, v in out.items() if v != 0}


def comp(*ops):
    def f(p):
        for o in reversed(ops):
            p = o(p)
        return p
    return f


def lin(*terms):
    return lambda p: padd(*[pscale(c, o(p)) for c, o in terms])


def ID(p):
    return dict(p)


def Z(i, al):
    A = al % 2
    sgn = F(1) if al < 2 else F(-1)
    return lin((F(1), lambda p: der(xv(i, A), p)), (sgn, lambda p: mul(yv(i, A), p)))


def Zb(i, al):
    A = al % 2
    sgn = F(-1) if al < 2 else F(1)
    return lin((F(1), lambda p: mul(xv(i, A), p)), (sgn, lambda p: der(yv(i, A), p)))


def bracket2(op, i, l, a, b):
    return lin((F(1), comp(op(i, a), op(l, b))), (F(-1), comp(op(i, b), op(l, a))))


def build(LAM_):
    """All stored operators at cosmological constant LAM_ (lam = LAM_/6), as a dict."""
    lam_ = LAM_ / 6
    b_hat = bracket2(Z, 0, 1, 2, 3)        # <pi^1 pi^2>
    om_hat = bracket2(Z, 0, 1, 0, 1)       # [omega^1 omega^2]
    bdag = bracket2(Zb, 0, 1, 0, 1)        # conjugate of <pi pi> (pibar_A = Zbar_A)
    omdag = bracket2(Zb, 0, 1, 2, 3)       # conjugate of [omega omega]
    B = lin((F(1), b_hat), (lam_, om_hat))
    Bd = lin((F(1), bdag), (lam_, omdag))

    def h(i, l):
        terms = []
        for a in range(4):
            terms.append((F(1, 2), comp(Zb(i, a), Z(l, a))))
            terms.append((F(1, 2), comp(Z(l, a), Zb(i, a))))
        return lin(*terms)

    H = [[h(i, l) for l in range(2)] for i in range(2)]
    trh = lin((F(1), H[0][0]), (F(1), H[1][1]))
    Cop = lin(*([(F(1, 2), comp(H[i][l], H[l][i])) for i in range(2) for l in range(2)]
                + [(F(-1, 4), comp(trh, trh))]))
    m2 = lin((F(1), comp(Bd, B)), (F(1), comp(B, Bd)), (LAM_ / 3, Cop), (-2 * LAM_ / 3 * HBAR ** 2, ID))
    REST = lin((HBAR * lam_, trh), (LAM_ / 3, Cop), (-2 * LAM_ / 3 * HBAR ** 2, ID))
    J3 = lin((F(1, 2), H[0][0]), (F(-1, 2), H[1][1]))
    return dict(B=B, Bd=Bd, H=H, trh=trh, Cop=Cop, m2=m2, REST=REST, J3=J3)


OPS = build(LAM)
B, Bd, H, trh, Cop, m2, REST, J3 = (OPS[k] for k in ("B", "Bd", "H", "trh", "Cop", "m2", "REST", "J3"))


def comm(A, Bo):
    return lin((F(1), comp(A, Bo)), (F(-1), comp(Bo, A)))


def monomials(maxdeg):
    return [{k: F(1)} for k in product(range(maxdeg + 1), repeat=NV) if sum(k) <= maxdeg]


def mono_of(p):
    (k, _), = p.items()
    return k


def deg(k):
    return sum(k)


def na(k, i):
    return k[xv(i, 0)] + k[xv(i, 1)]


def nb(k, i):
    return k[yv(i, 0)] + k[yv(i, 1)]


def factorial(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def fock_ip(p, q):
    s = F(0)
    for k, v in p.items():
        if k in q:
            w = 1
            for e in k:
                w *= factorial(e)
            s += v * q[k] * w
    return s


def xx(p):
    return padd(comp(lambda q: mul(xv(0, 0), q), lambda q: mul(xv(1, 1), q))(p),
                pscale(F(-1), comp(lambda q: mul(xv(0, 1), q), lambda q: mul(xv(1, 0), q))(p)))


def yy(p):
    return padd(comp(lambda q: mul(yv(0, 0), q), lambda q: mul(yv(1, 1), q))(p),
                pscale(F(-1), comp(lambda q: mul(yv(0, 1), q), lambda q: mul(yv(1, 0), q))(p)))


MON1 = monomials(1)
MON2 = monomials(2)
SIG = {0: 2, 1: 3, 2: 0, 3: 1}


def kernel_dim(op, basis):
    cols = [op(p) for p in basis]
    rows = sorted({kk for c in cols for kk in c})
    ridx = {r: n for n, r in enumerate(rows)}
    M = [[F(0)] * len(basis) for _ in rows]
    for j, c in enumerate(cols):
        for kk, v in c.items():
            M[ridx[kk]][j] = v
    rank, r = 0, 0
    for cidx in range(len(basis)):
        piv = None
        for rr in range(r, len(M)):
            if M[rr][cidx] != 0:
                piv = rr
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][cidx]
        M[r] = [v / pv for v in M[r]]
        for rr in range(len(M)):
            if rr != r and M[rr][cidx] != 0:
                f = M[rr][cidx]
                M[rr] = [a - f * b for a, b in zip(M[rr], M[r])]
        r += 1
        rank += 1
    return len(basis) - rank


def check_positive_energy_realisation_bookkeeping():
    """Setting: the realisation obeys the canonical relations with hbar, h_ii = hbar (N_a - N_b) = 2 s hbar, and
    the h_il preserve the oscillator number. (That the stored conjugation is the Hilbert adjoint on this model,
    with the energies and multiplicities of the attachment, is the companion result on the attachment's
    conformal energy and is not re-proved here; it is used in the form (Z^A)* = a* + b = Zbar_{A+2}, which
    holds by construction once a, b are annihilation operators.)"""
    premise("field-theory.twistor-attachment")
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    premise("mass.imported-palatial-quadratics-homogeneity-charge")
    for p in MON1:
        for i in range(2):
            for l in range(2):
                for al in range(4):
                    for be in range(4):
                        want = pscale(HBAR, p) if (i == l and al == be) else {}
                        GA.check("[Z, Zbar] = hbar delta", comm(Z(i, al), Zb(l, be))(p) == want)
                        GA.check("[Z, Z] = 0", comm(Z(i, al), Z(l, be))(p) == {})
    for p in MON2:
        k = mono_of(p)
        for i in range(2):
            GA.check("h_ii = hbar (N_a - N_b)", H[i][i](p) == pscale(HBAR * (na(k, i) - nb(k, i)), p))
            for l in range(2):
                GA.check("h_il keeps the oscillator number", all(deg(kk) == deg(k) for kk in H[i][l](p)))
    # the realisation's adjoint pairs, as used: (Z^al)* = Zbar_{sigma(al)} on the Fock product, one monomial pair
    # per index as a consistency sample (the lemma itself is the companion's)
    p, qm = MON1[1], MON2[7]
    for i in range(2):
        for al in range(4):
            GA.check("(Z^alpha)* = Zbar_{sigma(alpha)} (sample)",
                     fock_ip(Z(i, al)(p), qm) == fock_ip(p, Zb(i, SIG[al])(qm)))
    return True


def check_join_is_positive_part_plus_isotype_constant():
    """(ii): m2 = 2 B-dagger B + hbar lam tr h + (Lambda/3) C - (2 Lambda/3) hbar^2 (exact identity),
    [B, B-dagger] = hbar lam tr h, [h_il, m2] = 0, [J3, h12] = hbar h12 and C = j(j + 1) hbar^2 on
    highest-weight vectors, where the constant is (Lambda/3) hbar^2 (s1 + s2 + j(j + 1) - 2)."""
    premise("synthesis.operator-join-ordering-constants")
    premise("mass.imported-palatial-quadratics-homogeneity-charge")
    premise("synthesis.operator-join-casimir-shifts")
    for p in MON2:
        GA.check("m2 = 2 B*B + rest", m2(p) == padd(pscale(F(2), comp(Bd, B)(p)), REST(p)))
        GA.check("[B, B*] = hbar lam tr h", comm(B, Bd)(p) == pscale(HBAR * lam, trh(p)))
        for i in range(2):
            for l in range(2):
                GA.check("[h_il, m2] = 0", comm(H[i][l], m2)(p) == {})
        GA.check("[J3, h12] = hbar h12", comm(J3, H[0][1])(p) == pscale(HBAR, H[0][1](p)))
    found = 0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                k = [0] * NV
                k[xv(0, 0)], k[xv(0, 1)], k[yv(1, 0)] = a, b, c
                p = {tuple(k): F(1)}
                if H[0][1](p) != {}:
                    continue                   # not a highest-weight vector
                j = F(a + b + c, 2)
                s0, s1 = F(a + b, 2), F(-c, 2)
                GA.check("J3 = j hbar on a highest-weight vector", J3(p) == pscale(HBAR * j, p))
                GA.check("C = j(j+1) hbar^2", Cop(p) == pscale(j * (j + 1) * HBAR ** 2, p))
                GA.check("isotype constant",
                         REST(p) == pscale(LAM / 3 * HBAR ** 2 * (s0 + s1 + j * (j + 1) - 2), p))
                found += 1
    GA.check("highest-weight vectors found", found == 27)
    # the one-constituent consistency of the constant: s1 = s2 = s, j = 0 gives (2s - 2); the two
    # readings agree at s = 1 (zero) and the shift -2 is the N = 2 value of -N Lambda/3 hbar^2 relative to
    # the Casimir term (Lambda/3) C (checked as numbers)
    GA.check("constant at (1, 1, 0) is zero", F(1) + F(1) + 0 - 2 == 0)
    return True


def check_top_band_and_no_finite_energy_eigenvectors():
    """(iii), (iv): the join shifts the oscillator number by -4, -2, 0, 2, 4 only; its +4 band is
    2 (1 + lam)^2 [x1 x2][y1 y2], multiplication by a nonzero polynomial; the kernel of m2 - mu on the
    polynomials of degree <= 2 is trivial for mu = 0 and for the isotype constants of the low sectors,
    and so is the kernel of the top band."""
    premise("synthesis.operator-join-ordering-constants")
    premise("synthesis.operator-join-seed-has-no-diagonal-matrix-elements")
    top = lin((2 * (1 + lam) ** 2, comp(xx, yy)))
    for p in MON2:
        k = mono_of(p)
        img = m2(p)
        GA.check("band -4..4", all(deg(kk) - deg(k) in (-4, -2, 0, 2, 4) for kk in img))
        GA.check("top band", {kk: v for kk, v in img.items() if deg(kk) == deg(k) + 4} == top(p))
        GA.check("top band nonzero on every monomial", top(p) != {})
    GA.check("ker m2 trivial on degree <= 2", kernel_dim(m2, MON2) == 0)
    for mu in (F(0), -LAM / 3 * HBAR ** 2, -2 * LAM / 3 * HBAR ** 2, -4 * LAM / 3 * HBAR ** 2):
        shifted = lin((F(1), m2), (-mu, ID))
        GA.check("ker (m2 - mu) trivial on degree <= 2", kernel_dim(shifted, MON2) == 0)
    GA.check("ker [xx][yy] trivial on degree <= 2", kernel_dim(comp(xx, yy), MON2) == 0)
    # the sector condition: constant <= 0 forces max(s1, s2) <= 1 and 2 max + (s1 - s2)^2 <= 2
    ok = True
    for n1 in range(-8, 9):
        for n2 in range(-8, 9):
            s1, s2 = F(n1, 2), F(n2, 2)
            j = abs(s1 - s2)
            if s1 + s2 + j * (j + 1) - 2 <= 0:
                ok = ok and max(s1, s2) <= 1 and 2 * max(s1, s2) + (s1 - s2) ** 2 <= 2
            else:
                ok = ok and 2 * max(s1, s2) + (s1 - s2) ** 2 > 2
    GA.check("sector condition", ok)
    return True


def check_controls():
    """Controls: in the polynomial realisation Zbar = -hbar d/dZ (hbar = 1) the constant is a zero mode of
    the join (so the two realisations do not share zero modes); and at Lambda = -6 (lam = -1) the top band
    vanishes, the join preserves the oscillator number and has three zero modes of finite energy content at
    degree 2 (sectors (1/2, -1/2), (-1/2, 1/2), (0, 0), internal spin 1, all in ker B)."""
    premise("synthesis.operator-join-ordering-constants")

    def Zp(i, al):
        return lambda p: mul(4 * i + al, p)

    def Zbp(i, al):
        return lambda p: pscale(F(-1), der(4 * i + al, p))

    bp = bracket2(Zp, 0, 1, 2, 3)
    omp = bracket2(Zp, 0, 1, 0, 1)
    bdp = bracket2(Zbp, 0, 1, 0, 1)
    omdp = bracket2(Zbp, 0, 1, 2, 3)
    Bp = lin((F(1), bp), (lam, omp))
    Bdp = lin((F(1), bdp), (lam, omdp))

    def hp(i, l):
        terms = []
        for a in range(4):
            terms.append((F(1, 2), comp(Zbp(i, a), Zp(l, a))))
            terms.append((F(1, 2), comp(Zp(l, a), Zbp(i, a))))
        return lin(*terms)

    Hp = [[hp(i, l) for l in range(2)] for i in range(2)]
    trp = lin((F(1), Hp[0][0]), (F(1), Hp[1][1]))
    Cp = lin(*([(F(1, 2), comp(Hp[i][l], Hp[l][i])) for i in range(2) for l in range(2)]
               + [(F(-1, 4), comp(trp, trp))]))
    m2p = lin((F(1), comp(Bdp, Bp)), (F(1), comp(Bp, Bdp)), (LAM / 3, Cp), (-2 * LAM / 3, ID))
    one = {(0,) * NV: F(1)}
    GA.check("polynomial realisation: constant is a zero mode", m2p(one) == {})
    GA.check("polynomial realisation: h_ii = -2 on the constant", Hp[0][0](one) == pscale(F(-2), one))
    GA.check("polynomial realisation: 2 B*B(1) = 8 lam = 4 Lambda/3, cancelling the constant -4 Lambda/3",
             pscale(F(2), comp(Bdp, Bp)(one)) == pscale(8 * lam, one))
    # Lambda = -6 (lam = -1, the scale matched to a frozen point of negative Lambda): the top band vanishes,
    # the join preserves the oscillator number, and its kernel on degree 2 is three-dimensional, one zero mode
    # in each of the sectors (1/2, -1/2), (-1/2, 1/2), (0, 0), all of internal spin 1 and in ker B
    GA.check("top band coefficient 2(1 + lam)^2 vanishes only at lam = -1",
             2 * (1 + F(-1)) ** 2 == 0 and 2 * (1 + lam) ** 2 != 0)
    neg = build(F(-6))
    deg2 = [p for p in MON2 if deg(mono_of(p)) == 2]
    for p in deg2:
        GA.check("at lam = -1 the join preserves the oscillator number",
                 all(deg(kk) == 2 for kk in neg["m2"](p)))
    GA.check("ker m2 at Lambda = -6 on degree 2 is three-dimensional", kernel_dim(neg["m2"], deg2) == 3)
    GA.check("ker m2 at Lambda = -6 on degree <= 2 is still three-dimensional", kernel_dim(neg["m2"], MON2) == 3)
    # explicit zero modes: psi = x_{1A} y_{2B} eps^{AB} type combinations; find them by sector
    found = set()
    for s1, s2 in ((F(1, 2), F(-1, 2)), (F(-1, 2), F(1, 2)), (F(0), F(0))):
        sec = [p for p in deg2 if F(na(mono_of(p), 0) - nb(mono_of(p), 0), 2) == s1
               and F(na(mono_of(p), 1) - nb(mono_of(p), 1), 2) == s2]
        if kernel_dim(neg["m2"], sec) == 1:
            found.add((s1, s2))
    GA.check("one zero mode in each of the three sectors", len(found) == 3)
    # the (0, 0) zero mode is a1*.b1* - a2*.b2* (each constituent's own a-b pair, antisymmetric in the
    # constituents): in ker B, internal spin 1, m2 = 0
    def mono(**kw):
        k = [0] * NV
        for name, e in kw.items():
            k[int(name[1:])] = e
        return tuple(k)
    psi = padd({mono(v0=1, v2=1): F(1)}, {mono(v1=1, v3=1): F(1)},
               {mono(v4=1, v6=1): F(-1)}, {mono(v5=1, v7=1): F(-1)})
    GA.check("explicit (0,0) zero mode: m2 psi = 0", neg["m2"](psi) == {})
    GA.check("explicit (0,0) zero mode: B psi = 0", neg["B"](psi) == {})
    GA.check("explicit (0,0) zero mode has internal spin 1", neg["Cop"](psi) == pscale(2 * HBAR ** 2, psi))
    GA.check("at Lambda = 3 the same vector is not a zero mode", m2(psi) != {})
    return True
