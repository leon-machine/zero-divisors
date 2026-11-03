"""one-relation.dirac-current-conserved-density: exact checks (Gaussian rationals, GA.QI).

Dirac representation over Q(i): gamma^0 = diag(1,1,-1,-1) and the standard gamma^k; m = 5.
(1) The representation: {gamma^mu, gamma^nu} = 2 eta^{mu nu} on all 16 pairs, gamma^0 Hermitian, gamma^k
    anti-Hermitian.
(2) Uniqueness (upper bound): conservation on the two-plane-wave solutions u e^{-ip.x} + v e^{-ip'.x}
    requires (p - p')_mu ubar Gamma^mu v = 0 for all on-shell p != p', u in ker(pslash - m),
    v in ker(p'slash - m). Twelve rational mass-shell momenta (both energy signs, the twelve of the
    proof) give 12 x 11 x 2 x 2 = 528 linear conditions on the 64 complex entries of (Gamma^0..Gamma^3);
    the kernel is one-dimensional over Q(i) and contains Gamma^mu = gamma^mu: gamma^mu satisfies every
    condition exactly, and the integer-scaled system has rank 63 modulo the prime 1000003 (= 3 mod 4,
    so Z[i]/(p) is a field), a lower bound for its rank over Q(i). Each ker(pslash - m) is
    two-dimensional (complete sample of spin states).
(3) Conservation (lower bound): (p - p')_mu ubar gamma^mu v = ubar(pslash - p'slash)v = 0 on every sample
    pair, and the diagonal terms p = p' vanish identically.
(4) Positivity: J^0 = psibar gamma^0 psi = psi^dagger psi, a sum of squared moduli, positive on nonzero
    samples and zero on the zero state.
"""
from fractions import Fraction as F

import GA

QI = GA.QI
Z = QI(0)


def m4(rows):
    return [[QI(*v) if isinstance(v, tuple) else QI(v) for v in r] for r in rows]


G = [m4([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]),
     m4([[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]]),
     m4([[0, 0, 0, (0, -1)], [0, 0, (0, 1), 0], [0, (0, 1), 0, 0], [(0, -1), 0, 0, 0]]),
     m4([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])]
ETA = (1, -1, -1, -1)
ID4 = m4([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
MASS = F(5)
SHELL = [(5, 0, 0, 0), (-5, 0, 0, 0), (13, 12, 0, 0), (13, 0, -12, 0), (-13, 0, 0, 12), (13, F(36, 5), F(48, 5), 0),
         (7, 2, 4, 2), (-7, -2, 4, 2), (9, 4, 6, 2), (11, 4, 4, -8), (-9, -4, 6, 2), (15, 10, -10, 0)]
PSIS = [[(1, 2), (0, -1), (3, 0), (1, 1)], [(0, 0), (2, 5), (-1, 0), (0, 0)], [(0, 0)] * 4]


def mm(A, B):
    return GA.field_mat_mul(A, B)


def msum(*Ms):
    return [[sum((M[r][c] for M in Ms), Z) for c in range(4)] for r in range(4)]


def msc(c, M):
    c = QI(c)
    return [[c * v for v in row] for row in M]


def dagger(M):
    return [[M[c][r].conj() for c in range(4)] for r in range(4)]


def slash(p):
    return msum(*[msc(ETA[mu] * F(p[mu]), G[mu]) for mu in range(4)])


def bar(u):
    row = [v.conj() for v in u]
    return [sum((row[r] * G[0][r][c] for r in range(4)), Z) for c in range(4)]


def lower(p):
    return [ETA[mu] * F(p[mu]) for mu in range(4)]


def spinors(p):
    return GA.field_kernel(msum(slash(p), msc(-MASS, ID4)))


def check_representation():
    ok = all(msum(mm(G[a], G[b]), mm(G[b], G[a])) == msc(2 * ETA[a] if a == b else 0, ID4)
             for a in range(4) for b in range(4))
    ok = ok and dagger(G[0]) == G[0] and all(dagger(G[k]) == msc(-1, G[k]) for k in (1, 2, 3))
    ok = ok and all(F(p[0]) ** 2 - sum(F(x) ** 2 for x in p[1:]) == MASS ** 2 for p in SHELL)
    ok = ok and sum(1 for p in SHELL if p[0] < 0) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_representation"; return _tp_rv


PRIME = 1000003                       # a prime = 3 mod 4, so Z[i]/(PRIME) is the field F_(PRIME^2)


def gauss_int_row(row):
    """Scale a row of Gaussian rationals by the lcm of its denominators: Gaussian integers (re, im)."""
    den = 1
    for x in row:
        for y in (x.re, x.im):
            den = den * y.denominator // GCD(den, y.denominator)
    return [((x.re * den).numerator, (x.im * den).numerator) for x in row]


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


def rank_mod_p(rows):
    """Rank over F_(p^2) = Z[i]/(p) by incremental elimination (pairs (a, b) = a + b i mod p)."""
    P = PRIME

    def mul(x, y):
        return ((x[0] * y[0] - x[1] * y[1]) % P, (x[0] * y[1] + x[1] * y[0]) % P)

    def inv(x):
        n = pow((x[0] * x[0] + x[1] * x[1]) % P, P - 2, P)
        return (x[0] * n % P, -x[1] * n % P)
    basis = {}                         # pivot column -> normalised row
    for row in rows:
        r = [(a % P, b % P) for a, b in row]
        for col, br in basis.items():
            c = r[col]
            if c != (0, 0):
                r = [((x[0] - mul(c, y)[0]) % P, (x[1] - mul(c, y)[1]) % P) for x, y in zip(r, br)]
        piv = next((j for j, x in enumerate(r) if x != (0, 0)), None)
        if piv is None:
            continue
        iv = inv(r[piv])
        r = [mul(iv, x) for x in r]
        for col in list(basis):
            c = basis[col][piv]
            if c != (0, 0):
                basis[col] = [((x[0] - mul(c, y)[0]) % P, (x[1] - mul(c, y)[1]) % P) for x, y in zip(basis[col], r)]
        basis[piv] = r
    return len(basis)


def check_conserved_currents_are_one_dimensional():
    """The rank over Q(i) is at least the rank mod p of the integer-scaled rows (minors reduce mod p),
    so rank 63 mod p gives a kernel of dimension at most 1 over Q(i); gamma^mu lies in it (exactly)."""
    spin = {p: spinors(p) for p in SHELL}
    ok = all(len(v) == 2 for v in spin.values())
    rows = []
    for p in SHELL:
        for pp in SHELL:
            if p == pp:
                continue
            q = [a - b for a, b in zip(lower(p), lower(pp))]
            for u in spin[p]:
                ub = bar(u)
                for v in spin[pp]:
                    rows.append([QI(q[mu]) * ub[r] * v[c] for mu in range(4) for r in range(4) for c in range(4)])
    ok = ok and len(rows) == 528
    gvec = [G[mu][r][c] for mu in range(4) for r in range(4) for c in range(4)]
    ok = ok and all(sum((row[k] * gvec[k] for k in range(64)), Z) == 0 for row in rows)
    ok = ok and rank_mod_p([gauss_int_row(row) for row in rows]) == 63
    _tp_rv = (ok); assert _tp_rv is not False, "check_conserved_currents_are_one_dimensional"; return _tp_rv


def check_dirac_current_is_conserved():
    spin = {p: spinors(p) for p in SHELL}
    ok = True
    for p in SHELL:
        for pp in SHELL:
            q = [a - b for a, b in zip(lower(p), lower(pp))]
            for u in spin[p]:
                for v in spin[pp]:
                    ub = bar(u)
                    val = sum((QI(q[mu]) * ub[r] * G[mu][r][c] * v[c]
                               for mu in range(4) for r in range(4) for c in range(4)), Z)
                    ok = ok and val == 0
    # ubar pslash = m ubar on one sample
    u = spin[SHELL[2]][0]
    ub = bar(u)
    ps = slash(SHELL[2])
    ok = ok and [sum((ub[r] * ps[r][c] for r in range(4)), Z) for c in range(4)] == [QI(MASS) * x for x in ub]
    _tp_rv = (ok); assert _tp_rv is not False, "check_dirac_current_is_conserved"; return _tp_rv


def check_density_is_sum_of_squared_moduli():
    ok = True
    vals = []
    for spec in PSIS:
        psi = [QI(*v) for v in spec]
        ub = bar(psi)
        J0 = sum((ub[r] * G[0][r][c] * psi[c] for r in range(4) for c in range(4)), Z)
        J0s = sum((v * v.conj() for v in psi), Z)
        ok = ok and J0 == J0s and J0.im == 0 and J0.re >= 0 and (J0.re == 0) == all(not v for v in psi)
        vals.append(J0.re)
    ok = ok and vals == [F(17), F(30), F(0)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_density_is_sum_of_squared_moduli"; return _tp_rv
