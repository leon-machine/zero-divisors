"""synthesis.face-mass-form-unit-plus-gram: exact checks.

Six bosonic modes p = (i, A), i in {0,1,2} (family), A in {0,1} (spinor slot). States are finite
combinations of unnormalised monomials (a^dag)^m |0>, with <m|m'> = delta_{m m'} prod_p m_p!, so
a_p (a^dag)^m|0> = m_p (a^dag)^{m - e_p}|0> and every amplitude stays rational (complex
rationals as pairs of Fractions). Theta_k[(i,A),(j,B)] = (1/2) eps_{kij} eps_{AB}, and
Omega_k = sum_{pq} Theta_k[p,q] a_p a_q, as in the skeleton theorem.
"""
from fractions import Fraction as F
from itertools import product
from tp_premise import premise
from GA import mul, gen, sig


def factorial(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out

MODES = [(i, A) for i in range(3) for A in range(2)]


CL3 = sig(3, 0)                          # Cl(3,0): e_k e_i e_j = eps_kij e_1 e_2 e_3 for distinct k, i, j


def eps3(k, i, j):
    """Levi-Civita symbol read off the Clifford product in Cl(3,0): the coefficient of the
    pseudoscalar in e_k e_i e_j when k, i, j are distinct, zero otherwise."""
    if len({k, i, j}) < 3:
        return 0
    prod = mul(mul(gen(k), gen(i), CL3), gen(j), CL3)
    return int(prod.get((0, 1, 2), 0))


def eps2(A, B):
    return 0 if A == B else (1 if (A, B) == (0, 1) else -1)


THETA = [[[F(1, 2) * eps3(k, p[0], q[0]) * eps2(p[1], q[1]) for q in MODES] for p in MODES] for k in range(3)]


# complex rationals
def cadd(x, y): return (x[0] + y[0], x[1] + y[1])
def cmul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def cconj(x): return (x[0], -x[1])
Z = (F(0), F(0))


def sadd(s, m, c):
    s[m] = cadd(s.get(m, Z), c)
    if s[m] == Z:
        del s[m]


def ann(p, st):                          # a_p
    out = {}
    for m, c in st.items():
        if m[p]:
            mm = list(m); mm[p] -= 1
            sadd(out, tuple(mm), cmul((F(m[p]), F(0)), c))
    return out


def cre(p, st):                          # a_p^dag
    out = {}
    for m, c in st.items():
        mm = list(m); mm[p] += 1
        sadd(out, tuple(mm), c)
    return out


def lin(terms):                          # sum of (coefficient, state)
    out = {}
    for coef, st in terms:
        for m, c in st.items():
            sadd(out, m, cmul(coef, c))
    return out


def inner(s, t):                         # <s|t>
    tot = Z
    for m, c in s.items():
        if m in t:
            w = 1
            for x in m:
                w *= factorial(x)
            tot = cadd(tot, cmul(cconj(c), cmul((F(w), F(0)), t[m])))
    return tot


def omega(k, st):
    return lin([((THETA[k][p][q], F(0)), ann(p, ann(q, st))) for p in range(6) for q in range(6) if THETA[k][p][q]])


def omega_dag(k, st):
    return lin([((THETA[k][p][q], F(0)), cre(q, cre(p, st))) for p in range(6) for q in range(6) if THETA[k][p][q]])


def theta_a(k, st):                      # the 6-vector of operators (Theta_k a)_p applied to st
    return [lin([((THETA[k][p][q], F(0)), ann(q, st)) for q in range(6) if THETA[k][p][q]]) for p in range(6)]


def states():
    vac = tuple([0] * 6)
    def mono(*m): return tuple(m)
    yield {vac: (F(1), F(0))}
    yield {vac: (F(1), F(0)), mono(1, 0, 0, 1, 0, 0): (F(2), F(-1)), mono(0, 1, 1, 0, 0, 0): (F(0), F(3, 2))}
    yield {mono(1, 0, 0, 0, 0, 0): (F(1), F(1)), mono(0, 0, 1, 1, 1, 0): (F(-2, 3), F(0)),
           mono(2, 1, 0, 0, 0, 1): (F(1, 5), F(-1, 7)), mono(0, 0, 0, 0, 2, 0): (F(4), F(1))}
    yield {mono(1, 1, 1, 1, 0, 0): (F(1), F(0)), mono(0, 0, 1, 1, 1, 1): (F(-1), F(2)),
           mono(1, 0, 0, 0, 0, 1): (F(3, 4), F(0)), vac: (F(0), F(-5, 2)), mono(0, 2, 0, 1, 0, 0): (F(1), F(1))}


def check_theta_normalisation():
    premise("families.skeleton-rank-one-plus-ordering-shift")
    for k in range(3):
        for l in range(3):
            t = sum(THETA[k][p][q] * THETA[l][q][p] for p in range(6) for q in range(6))
            assert t == (1 if k == l else 0)
            for p in range(6):
                for q in range(6):
                    assert THETA[k][p][q] == THETA[k][q][p]


def check_unit_plus_gram():
    """For every state psi: H_kl = (1/2)<Omega_k^dag Omega_l + Omega_l Omega_k^dag>
    equals <psi|psi> delta_kl + <Omega_k psi, Omega_l psi> + 2 sum_p <(Theta_k a)_p psi, (Theta_l a)_p psi>."""
    premise("families.skeleton-rank-one-plus-ordering-shift")
    premise("families.imported-squeezed-vacuum-bosonic-pairing")
    for psi in states():
        n2 = inner(psi, psi)
        Om = [omega(k, psi) for k in range(3)]
        Od = [omega_dag(k, psi) for k in range(3)]
        Ta = [theta_a(k, psi) for k in range(3)]
        for k in range(3):
            for l in range(3):
                H = cmul((F(1, 2), F(0)), cadd(inner(Om[k], Om[l]), inner(Od[l], Od[k])))
                G = inner(Om[k], Om[l])
                for p in range(6):
                    G = cadd(G, cmul((F(2), F(0)), inner(Ta[k][p], Ta[l][p])))
                rhs = cadd(G, n2 if k == l else Z)
                assert H == rhs, (k, l)


EXPORTS = {}
