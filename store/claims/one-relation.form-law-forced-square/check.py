"""one-relation.form-law-forced-square: exact checks in Cl(1,3) (GA.py, gamma_0^2 = +1,
gamma_i^2 = -1, I = gamma_0 gamma_1 gamma_2 gamma_3).

(1) The operator identity behind nabla(nabla psi) = m^2 psi C^2: on polynomial multivector fields
    psi(x) (exact dicts of monomials), nabla = sum gamma^mu d_mu satisfies
    nabla(nabla psi) = box psi with box = d_0^2 - d_1^2 - d_2^2 - d_3^2 (a scalar operator), and
    nabla(psi C) = (nabla psi) C for constant C. Tested on three sample fields and three C.
(2) The converse, through the t-only solution of the proof: nabla psi = m psi C reads
    psi' = m gamma_0 psi C, solved exactly as a power series psi = sum psi_k t^k with psi(0) = psi_0
    (order 8, m = 2 and m = 1/3, psi_0 = 1 and an invertible even psi_0). Its coefficients satisfy
    box psi = d_t^2 psi = m^2 psi C^2 order by order; for Hestenes' C this is -m^2 psi (Klein-Gordon),
    for C = I gamma_0 it is +m^2 psi (tachyonic), and for C = gamma_3 + I gamma_2 the second
    coefficient psi_0 C^2 is not a scalar multiple of psi_0 (no scalar equation).
(3) The stated squares: I sigma_3 = gamma_2 gamma_1, (I sigma_3)^-1 = -I sigma_3,
    C = gamma_0 (I sigma_3)^-1 has C^2 = -1, (I gamma_0)^2 = +1, and
    (gamma_3 + I gamma_2)^2 = -2 - 2 I gamma_3 gamma_2, not a scalar.
No premises: the claim has no uses.
"""
from fractions import Fraction as F

import GA

SQ = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]
RECIP = [1, -1, -1, -1]                     # gamma^mu = RECIP[mu] gamma_mu


def m(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out


I4 = m(E[0], E[1], E[2], E[3])
SIG3 = m(E[3], E[0])
ISIG3 = m(I4, SIG3)
C_HEST = m(E[0], GA.neg(ISIG3))
C_TACH = m(I4, E[0])
C_MIXED = GA.add(E[3], m(I4, E[2]))

# polynomial fields: {exponent tuple (a0, a1, a2, a3): multivector}
FIELDS = [
    {(1, 0, 0, 0): GA.sc(1), (0, 2, 1, 0): m(E[1], E[2]), (3, 0, 0, 1): GA.scal(2, I4)},
    {(0, 0, 0, 0): GA.sc(3), (1, 1, 1, 1): m(E[0], E[3]), (2, 0, 2, 0): GA.sc(-1), (0, 3, 0, 0): I4},
    {(2, 1, 0, 0): GA.add(GA.sc(1), m(E[1], E[3])), (0, 0, 3, 1): GA.scal(5, m(E[0], E[2]))},
]
PSI0 = [GA.sc(1), GA.add(GA.sc(2), GA.scal(F(1, 3), m(E[1], E[2])), GA.scal(F(-1, 2), m(E[0], E[1])),
                         GA.scal(F(1, 5), I4))]
MASSES = [F(2), F(1, 3)]
ORDER = 8                                   # series order of the t-only solution
KG_ORDERS = range(ORDER - 1)


def fadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = GA.add(out.get(k, {}), v)
    return {k: v for k, v in out.items() if v}


def deriv(f, mu):
    out = {}
    for k, v in f.items():
        if k[mu]:
            k2 = list(k)
            k2[mu] -= 1
            out = fadd(out, {tuple(k2): GA.scal(k[mu], v)})
    return out


def nabla(f):
    out = {}
    for mu in range(4):
        d = deriv(f, mu)
        out = fadd(out, {k: GA.scal(RECIP[mu], m(E[mu], v)) for k, v in d.items()})
    return out


def box(f):
    out = {}
    for mu in range(4):
        d2 = deriv(deriv(f, mu), mu)
        out = fadd(out, {k: GA.scal(RECIP[mu], v) for k, v in d2.items()})
    return out


def rmul(f, C):
    return {k: v for k, v in ((k, m(v, C)) for k, v in f.items()) if v}


def feq(a, b):
    return fadd(a, {k: GA.neg(v) for k, v in b.items()}) == {}


def series(psi0, mass, C, order):
    co = [psi0]
    for k in range(order):
        co.append(GA.scal(mass / (k + 1), m(E[0], co[-1], C)))
    return co


def check_operator_identities_on_polynomial_fields():
    ok = True
    for f in FIELDS:
        ok = ok and feq(nabla(nabla(f)), box(f))
        for C in (C_HEST, C_TACH, C_MIXED):
            ok = ok and feq(nabla(rmul(f, C)), rmul(nabla(f), C))
    # hand value: box(x0 + x1^2 x2 e12 + 2 x0^3 x3 I) = 12 x0 x3 I - 2 x2 e12
    ok = ok and feq(box(FIELDS[0]), {(1, 0, 0, 1): GA.scal(12, I4), (0, 0, 1, 0): GA.scal(-2, m(E[1], E[2]))})
    GA.check("nabla nabla = box (scalar) and nabla(psi C) = (nabla psi) C on polynomial fields", ok)
    return ok


def check_t_only_solution_klein_gordon_iff_c_squared_minus_one():
    ok = True
    for psi0 in PSI0:
        for mass in MASSES:
            for C, kg in ((C_HEST, -1), (C_TACH, 1)):
                co = series(psi0, mass, C, ORDER)
                # law: gamma_0 psi' = m psi C, coefficientwise
                for k in range(ORDER):
                    ok = ok and GA.eq(m(E[0], GA.scal(k + 1, co[k + 1])), GA.scal(mass, m(co[k], C)))
                # box psi = d_t^2 psi: coefficient (k+2)(k+1) psi_{k+2} = kg m^2 psi_k
                for k in KG_ORDERS:
                    lhs = GA.scal((k + 2) * (k + 1), co[k + 2])
                    ok = ok and GA.eq(lhs, GA.scal(kg * mass * mass, co[k]))
                    ok = ok and GA.eq(lhs, GA.scal(mass * mass, m(co[k], C, C)))
            co = series(psi0, mass, C_MIXED, ORDER)
            lhs = GA.scal(2, co[2])
            ok = ok and GA.eq(lhs, GA.scal(mass * mass, m(psi0, C_MIXED, C_MIXED)))
            # not a scalar multiple of psi_0
            c0 = lhs.get((), F(0)) / psi0[()]
            ok = ok and not GA.eq(lhs, GA.scal(c0, psi0))
    GA.check("t-only solution: d_t^2 psi = m^2 psi C^2, so -m^2 psi for Hestenes' C, +m^2 psi for I gamma_0", ok)
    return ok


def check_the_three_right_factors():
    ok = GA.eq(ISIG3, m(E[2], E[1]))
    ok = ok and GA.eq(m(ISIG3, GA.neg(ISIG3)), GA.sc(1))
    ok = ok and GA.eq(m(C_HEST, C_HEST), GA.sc(-1))
    ok = ok and GA.eq(m(C_TACH, C_TACH), GA.sc(1))
    want = GA.add(GA.sc(-2), GA.scal(-2, m(I4, E[3], E[2])))
    ok = ok and GA.eq(m(C_MIXED, C_MIXED), want) and len(want) == 2
    GA.check("I sigma_3 = gamma_2 gamma_1; C_Hestenes^2 = -1, (I gamma_0)^2 = +1, (gamma_3 + I gamma_2)^2 non-scalar", ok)
    return ok
