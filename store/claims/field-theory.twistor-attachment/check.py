"""field-theory.twistor-attachment: exact checks of the finite core.

(1) The oscillator model of the palatial storey (premise: the palatial algebra is realised on
polynomials): operators on polynomials in y1..y4, Z = (y1, y2, d3, d4), Zbar = (-d1, -d2, y3, y4).
The relations [Z^a, Zbar_b] = delta_ab hold on all monomials of degree <= 3; in the Fock inner product
Zbar_a = Sigma_aa (Z^a)^dagger with Sigma = diag(-1, -1, 1, 1), the reversion form h on CS of
signature (2,2). With q(M) = sum M_ba (Z^a Zbar_b + Zbar_b Z^a)/2, helicity q(1)/2 = (N_b - N_a)/2
and the conformal energy q(Sigma)/2 = (N_a + N_b)/2 + 1, the palatial quadratic of h, on all monomials
of degree <= 4. Counting monomials: the helicity-s module has energies |s| + 1 + n with multiplicity
(n + 1)(n + 2|s| + 1) for 2s = -4..4, n <= 4, and E >= |s| + 1 on every monomial (positive energy).
(2) The sixteen q(E_ab), a basis of u(2,2)_C, commute with helicity on all monomials of degree <= 3,
change the energy only by -1, 0, +1 and keep every image in the positive-energy Fock module, so each
fixed-helicity module is preserved.
(3) Spin-statistics on the attachment (premise: the Penrose transform's kernels and the Jost-point
theorem): in the chart M^{BA'} the helicity kernels chi^{A'_1}..chi^{A'_m}/D^{m+1} (D = det M,
chi^{A'} = mu_B M^{BA'}) solve the zero-rest-mass equation for 2s = m = 1, 2 (s = 0: 1/D solves the
wave equation), the epsilon contraction does not vanish (control); under x -> -x the kernel numerator
picks up (-1)^{2s} and D is even, and at the spacelike point x = (1, 2, 1, 1) (det M = x^2 = -5)
W(-x) = (-1)^{2s} W(x) != 0 for 2s = 0..4: a CAR lift is local exactly for odd 2s, which the
series' fermions (2s = 1) satisfy.
That the tower's floors are energy cut-offs rather than regions is an interpretation with no finite
content beyond (1) and (2), and is not checked.
"""
from fractions import Fraction as F
from itertools import product

from GA import QI
from tp_premise import premise

NV = 4
SIG = [F(-1), F(-1), F(1), F(1)]
MU = [F(2), F(3)]
XPT = (F(1), F(2), F(1), F(1))


class Poly(object):
    def __init__(self, d=None, n=4):
        self.n = n
        self.d = {k: v for k, v in (d or {}).items() if v != 0}

    @staticmethod
    def var(i, n=4):
        e = [0] * n
        e[i] = 1
        return Poly({tuple(e): F(1)}, n)

    @staticmethod
    def const(c, n=4):
        return Poly({tuple([0] * n): c}, n)

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, F(0)) + v
        return Poly(d, self.n)

    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()}, self.n)

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if not isinstance(o, Poly):
            return Poly({k: o * v for k, v in self.d.items()}, self.n)
        d = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                d[k] = d.get(k, F(0)) + v1 * v2
        return Poly(d, self.n)

    def deriv(self, i):
        d = {}
        for k, v in self.d.items():
            if k[i] > 0:
                kk = list(k)
                kk[i] -= 1
                d[tuple(kk)] = d.get(tuple(kk), F(0)) + v * k[i]
        return Poly(d, self.n)

    def is_zero(self):
        return not self.d

    def ev(self, pt):
        tot = QI(0)
        for k, v in self.d.items():
            t = QI(v)
            for x, e in zip(pt, k):
                for _ in range(e):
                    t = t * x
            tot = tot + t
        return tot

    def subst_neg(self):
        return Poly({k: v * (-1) ** sum(k) for k, v in self.d.items()}, self.n)


def mono_basis(deg):
    return [Poly({e: F(1)}, NV) for e in product(range(deg + 1), repeat=NV) if sum(e) <= deg]


def op_Z(a):
    return (lambda p: Poly.var(a, NV) * p) if a < 2 else (lambda p: p.deriv(a))


def op_Zb(b):
    return (lambda p: -p.deriv(b)) if b < 2 else (lambda p: Poly.var(b, NV) * p)


def fock_ip(p, q):
    tot = F(0)
    for k, v in p.d.items():
        if k in q.d:
            f = 1
            for e in k:
                for j in range(2, e + 1):
                    f *= j
            tot += v * q.d[k] * f
    return tot


def qM(Mm):
    def f(p):
        tot = Poly(n=NV)
        for a in range(4):
            for b in range(4):
                c = Mm[b][a]
                if c != 0:
                    tot = tot + (op_Z(a)(op_Zb(b)(p)) + op_Zb(b)(op_Z(a)(p))) * (c / 2)
        return tot
    return f


def energy(k):
    return F(sum(k), 2) + 1


def check_oscillator_module_spectrum_and_twistor_form():
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    b3 = mono_basis(3)
    for a in range(4):
        for b in range(4):
            for p in b3:
                c = op_Z(a)(op_Zb(b)(p)) - op_Zb(b)(op_Z(a)(p))
                assert (c - (p if a == b else Poly(n=NV))).is_zero()
                assert (op_Z(a)(op_Z(b)(p)) - op_Z(b)(op_Z(a)(p))).is_zero()
        for p in b3:
            for q in b3:
                assert fock_ip(p, op_Zb(a)(q)) == SIG[a] * fock_ip(op_Z(a)(p), q)
    assert sum(1 for s in SIG if s > 0) == 2 and sum(1 for s in SIG if s < 0) == 2
    Id = [[F(int(i == j)) for j in range(4)] for i in range(4)]
    SigM = [[SIG[i] if i == j else F(0) for j in range(4)] for i in range(4)]
    qid, qsig = qM(Id), qM(SigM)
    for p in mono_basis(4):
        (k, _), = p.d.items()
        Na, Nb = k[0] + k[1], k[2] + k[3]
        assert (qid(p) * F(1, 2) - p * F(Nb - Na, 2)).is_zero()
        assert (qsig(p) * F(1, 2) - p * (F(Na + Nb, 2) + 1)).is_zero()
    tally = {}
    for e in product(range(13), repeat=4):
        Na, Nb = e[0] + e[1], e[2] + e[3]
        if Na + Nb <= 12:
            key = (Nb - Na, F(Na + Nb, 2) + 1)
            tally[key] = tally.get(key, 0) + 1
    for twos in range(-4, 5):
        for n in range(0, 5):
            assert tally.get((twos, F(abs(twos), 2) + 1 + n), 0) == (n + 1) * (n + abs(twos) + 1)
        assert tally.get((twos, F(abs(twos), 2)), 0) == 0          # nothing below |s| + 1
    for e in product(range(7), repeat=4):
        Na, Nb = e[0] + e[1], e[2] + e[3]
        assert energy(e) >= F(abs(Nb - Na), 2) + 1


def check_u22_preserves_positive_energy_helicity_modules():
    premise("field-theory.imported-statistics-no-go-palatial-algebra")
    qid = qM([[F(int(i == j)) for j in range(4)] for i in range(4)])
    moves = set()
    gens = 0
    for a in range(4):
        for b in range(4):
            qe = qM([[F(int(i == b and j == a)) for j in range(4)] for i in range(4)])
            gens += 1
            for pp in mono_basis(3):
                (k0, _), = pp.d.items()
                img = qe(pp)
                assert (qid(img) - qe(qid(pp))).is_zero()
                for k1 in img.d:
                    moves.add(energy(k1) - energy(k0))
                    assert energy(k1) >= F(abs(k1[2] + k1[3] - k1[0] - k1[1]), 2) + 1
    assert gens == 16 and moves == {F(-1), F(0), F(1)}


def check_kernels_exchange_parity_is_spin_statistics():
    premise("field-theory.imported-standard-field-theory")
    m00, m01, m10, m11 = (Poly.var(i) for i in range(4))
    Mv = [[m00, m01], [m10, m11]]
    idx = [[0, 1], [2, 3]]
    D = m00 * m11 - m01 * m10
    chi = [Mv[0][a] * MU[0] + Mv[1][a] * MU[1] for a in range(2)]
    lap = ((D.deriv(0) * D.deriv(3)) * F(2) - D * D.deriv(0).deriv(3)) - \
          ((D.deriv(1) * D.deriv(2)) * F(2) - D * D.deriv(1).deriv(2))
    assert lap.is_zero()
    for m in (1, 2):
        for contraction in ("trace", "eps"):
            outs = []
            for B in range(2):
                for rest in product(range(2), repeat=m - 1):
                    Pi = Poly.const(F(1))
                    for c in rest:
                        Pi = Pi * chi[c]
                    tot = Poly()
                    for A in range(2):
                        if contraction == "trace":
                            dv, sgn = idx[B][A], F(1)
                        else:
                            dv, sgn = idx[B][1 - A], F(1) if A == 0 else F(-1)
                        num = chi[A] * Pi
                        tot = tot + (num.deriv(dv) * D - (num * D.deriv(dv)) * F(m + 1)) * sgn
                    outs.append(tot)
            if contraction == "trace":
                assert all(p.is_zero() for p in outs)
            else:
                assert any(not p.is_zero() for p in outs)
    x0, x1, x2, x3 = XPT
    pt = [QI(x0 + x3), QI(x1, -x2), QI(x1, x2), QI(x0 - x3)]
    Dv = D.ev(pt)
    assert Dv == QI(-5)
    assert (D.subst_neg() - D).is_zero()
    for m in range(0, 5):
        num = Poly.const(F(1))
        for _ in range(m):
            num = num * chi[0]
        assert (num.subst_neg() - num * F((-1) ** m)).is_zero()
        den = QI(1)
        for _ in range(m + 1):
            den = den * Dv
        Wx = num.ev(pt) / den
        Wmx = num.ev([-p for p in pt]) / den
        assert Wx != 0 and Wmx == Wx * ((-1) ** m)
        assert (Wmx == -Wx) == (m % 2 == 1)          # odd 2s: the kernel is odd, the CAR lift is local
