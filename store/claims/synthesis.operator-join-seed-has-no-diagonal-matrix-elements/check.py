"""synthesis.operator-join-seed-has-no-diagonal-matrix-elements: exact checks.

Palatial oscillators for two constituents in the realisation Z^alpha_i = multiplication by x_{i alpha},
Zbar_{i alpha} = -hbar d/dx_{i alpha} (hbar = 1), so [Z^alpha_i, Zbar_{l beta}] = delta delta, on polynomials
(dicts monomial exponent tuple -> Fraction). Components: omega = (Z^0, Z^1), pi = (Z^2, Z^3); the conjugates
pair as pibar_A = Zbar_A (A = 0, 1), omegabar^A' = Zbar_A' (A' = 2, 3).
B = <pi^1 pi^2> + lam [omega^1 omega^2], Bdag = its conjugate (a polynomial in the Zbar), lam = Lambda/6;
h_il = (Zbar_i . Z^l + Z^l . Zbar_i)/2; C = (1/2) sum h_il h_li - (1/4)(tr h)^2;
m2 = Bdag B + B Bdag + (Lambda/3) C - (2 Lambda/3) (the stored palatial form, N = 2).
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

LAM = F(3)            # Lambda; lam = Lambda/6 = 1/2
lam = LAM / 6
NV = 8                # variable index 4*i + alpha


def var(i, a):
    return 4 * i + a


def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def pscale(c, p):
    return {k: c * v for k, v in p.items() if c * v != 0}


def mulvar(j, p):
    out = {}
    for k, v in p.items():
        kk = list(k)
        kk[j] += 1
        out[tuple(kk)] = out.get(tuple(kk), F(0)) + v
    return out


def dvar(j, p):            # Zbar = -d/dx
    out = {}
    for k, v in p.items():
        if k[j]:
            kk = list(k)
            kk[j] -= 1
            out[tuple(kk)] = out.get(tuple(kk), F(0)) - k[j] * v
    return {k: v for k, v in out.items() if v != 0}


# operators are functions p -> p; build linear combinations of words
def Zop(i, a):
    return lambda p: mulvar(var(i, a), p)


def Zbop(i, a):
    return lambda p: dvar(var(i, a), p)


def comp(*ops):
    def f(p):
        for o in reversed(ops):
            p = o(p)
        return p
    return f


def lin(*terms):
    """terms: (coef, op)"""
    return lambda p: padd(*[pscale(c, o(p)) for c, o in terms])


def bracket2(op, i, l, a, b):
    """op(i,a) op(l,b) - op(i,b) op(l,a)"""
    return lin((F(1), comp(op(i, a), op(l, b))), (F(-1), comp(op(i, b), op(l, a))))


b_hat = bracket2(Zop, 0, 1, 2, 3)                  # <pi^1 pi^2>
om_hat = bracket2(Zop, 0, 1, 0, 1)                 # [omega^1 omega^2]
bdag = bracket2(Zbop, 0, 1, 0, 1)                  # conj <pi pi>: pibar = Zbar_{0,1}
omdag = bracket2(Zbop, 0, 1, 2, 3)                 # conj [omega omega]: omegabar = Zbar_{2,3}
B = lin((F(1), b_hat), (lam, om_hat))
Bd = lin((F(1), bdag), (lam, omdag))


def h(i, l):
    terms = []
    for a in range(4):
        terms.append((F(1, 2), comp(Zbop(i, a), Zop(l, a))))
        terms.append((F(1, 2), comp(Zop(l, a), Zbop(i, a))))
    return lin(*terms)


H = [[h(i, l) for l in range(2)] for i in range(2)]
trh = lin((F(1), H[0][0]), (F(1), H[1][1]))
Cop = lin(*([(F(1, 2), comp(H[i][l], H[l][i])) for i in range(2) for l in range(2)]
            + [(F(-1, 4), comp(trh, trh))]))
m2 = lin((F(1), comp(Bd, B)), (F(1), comp(B, Bd)), (LAM / 3, Cop), (-2 * LAM / 3, lambda p: dict(p)))


def monomials(maxdeg):
    for k in product(range(maxdeg + 1), repeat=NV):
        if sum(k) <= maxdeg:
            yield {k: F(1)}


MONOS = list(monomials(3))


def comm(A, Bo):
    return lin((F(1), comp(A, Bo)), (F(-1), comp(Bo, A)))


def bideg(k):
    return (sum(k[0:4]), sum(k[4:8]))


def check_join_commutes_with_internal_u2():
    premise("synthesis.operator-join-ordering-constants")
    premise("mass.imported-palatial-quadratics-homogeneity-charge")
    # consistency with the stored commutator [B, Bdag] = hbar lam (h11 + h22)
    for p in MONOS:
        GA.check("[B, Bdag] = lam tr h", comm(B, Bd)(p) == pscale(lam, trh(p)))
    # h_ii acts on bidegree (n1, n2) as -(n_i + 2)
    for p in MONOS:
        (k, _), = p.items()
        n1, n2 = bideg(k)
        GA.check("h11 = -(n1 + 2)", H[0][0](p) == pscale(F(-(n1 + 2)), p))
        GA.check("h22 = -(n2 + 2)", H[1][1](p) == pscale(F(-(n2 + 2)), p))
    for i in range(2):
        for l in range(2):
            for p in MONOS:
                GA.check("[h_il, m2] = 0", comm(H[i][l], m2)(p) == {})
    return True


def check_source_carries_determinant_charge():
    premise("families.source-term-linear-tilt-mass-functional")
    premise("families.imported-face-valued-bracket-quantum-numbers")
    for p in MONOS:
        for X in (b_hat, om_hat):
            GA.check("[h_ii, X] = -X", all(comm(H[i][i], X)(p) == pscale(F(-1), X(p)) for i in range(2)))
            GA.check("[h_12, X] = 0", comm(H[0][1], X)(p) == {} and comm(H[1][0], X)(p) == {})
        for X in (bdag, omdag):
            GA.check("[h_ii, Xdag] = +Xdag", all(comm(H[i][i], X)(p) == X(p) for i in range(2)))
    # the source S = (Lambda/3)(Abar b + A bdag), A a c-number: no block-diagonal part in bidegree
    A, Abar = F(5, 7), F(5, 7)
    S = lin((LAM / 3 * Abar, b_hat), (LAM / 3 * A, bdag))
    for p in MONOS:
        (k, _), = p.items()
        d = bideg(k)
        img = S(p)
        GA.check("source shifts bidegree by +-(1,1)",
                 all(bideg(kk) in ((d[0] + 1, d[1] + 1), (d[0] - 1, d[1] - 1)) for kk in img))
    # a generic state of fixed bidegree (2, 1): the bidegree-(2,1) component of S psi vanishes
    psi = padd(*[pscale(F(j + 1, 3), q) for j, q in enumerate(MONOS) if bideg(next(iter(q)))== (2, 1)])
    img = S(psi)
    GA.check("no diagonal block", all(bideg(kk) != (2, 1) for kk in img) and len(img) > 0)
    # while the join keeps it
    GA.check("join preserves bidegree", all(bideg(kk) == (2, 1) for kk in m2(psi)))
    return True
