"""synthesis.wick-rotated-boost-selects-observer-tube-point: exact checks.

Model: the eight-dimensional Fock module of Cl(2,4) of synthesis.incidence-vacua-thermofield-real-capacity
(three modes, Jordan-Wigner basis), ground generators e1 (square +1, time t), e2, e3, e4 (square -1),
ascent plane e+ (+1), e- (-1); nO = (e+ + e-)/2, ninf = e+ - e-, X(m) = nO + m - Q(m) ninf / 2.
J = i e1 e+, Sigma = h(., J .) the twistor form, h the identity Gram matrix (h = h_{i e1},
synthesis.positive-structure-is-twistor-form-at-imaginary-time). For a forward-tube point m the positive
structure h_m is Sigma on L(m) and -Sigma on L(mbar). The boost of the (t, r) = (e1, e2) plane has generator
K = e1 e2 / 2; its Wick rotation is exp(i theta K) = cos(theta/2) + i sin(theta/2) e1 e2.
Exact Gaussian rationals (GA.QI) throughout.
"""
from fractions import Fraction as F

import GA as g
import fock
from tp_premise import premise

Z = g.QI(0)
IU = g.QI(0, 1)
N = 8


def zeros(n=N):
    return [[g.QI(0) for _ in range(n)] for _ in range(n)]


def eye(n=N):
    M = zeros(n)
    for i in range(n):
        M[i][i] = g.QI(1)
    return M


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def ms(c, A):
    c = c if isinstance(c, g.QI) else g.QI(c)
    return [[c * x for x in r] for r in A]


def mm(A, B):
    return g.field_mat_mul(A, B)


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(len(v))), Z) for i in range(len(M))]


def ip(u, v):
    return sum((u[i].conj() * v[i] for i in range(N)), Z)


CR = [[[g.QI(x) for x in r] for r in fock.to_dense(fock.cre(j, 3), N)] for j in range(3)]
AN = [dag(c) for c in CR]
HERM = []
for _j in range(3):
    HERM.append(madd(CR[_j], AN[_j]))
    HERM.append(ms(IU, madd(CR[_j], ms(-1, AN[_j]))))
GEN = {"e1": HERM[0], "e2": ms(IU, HERM[1]), "e3": ms(IU, HERM[2]), "e4": ms(IU, HERM[3]),
       "ep": HERM[4], "em": ms(IU, HERM[5])}
SQ = {"e1": 1, "e2": -1, "e3": -1, "e4": -1, "ep": 1, "em": -1}
NAMES = ["e1", "e2", "e3", "e4", "ep", "em"]
J = ms(IU, mm(GEN["e1"], GEN["ep"]))
NO = ms(g.QI(F(1, 2)), madd(GEN["ep"], GEN["em"]))
NINF = madd(GEN["ep"], ms(-1, GEN["em"]))
NUM = mm(ms(g.QI(F(1, 2)), NINF), NO)          # N = a* a, a = nO, a* = ninf / 2
E12 = mm(GEN["e1"], GEN["e2"])                  # 2K
DIL = mm(GEN["ep"], GEN["em"])                  # dilation bivector
_G = eye()
for _a in NAMES:
    _G = mm(_G, GEN[_a])
GAMMA = ms(IU, _G)
PPLUS = ms(g.QI(F(1, 2)), madd(eye(), GAMMA))


def span_basis(vectors):
    out = []
    for v in vectors:
        if any(x != Z for x in v) and g.field_rank(out + [v]) > len(out):
            out.append(v)
    return out


HALF = span_basis([[PPLUS[i][j] for i in range(N)] for j in range(N)])


def q(re, im=0):
    return g.QI(F(re), F(im))


def vec(coef):
    M = zeros()
    for a, c in coef.items():
        M = madd(M, ms(c, GEN[a]))
    return M


def Qm(coef):
    return sum((coef.get(a, Z) * coef.get(a, Z) * g.QI(SQ[a]) for a in ["e1", "e2", "e3", "e4"]), Z)


def X_of(m):
    return madd(madd(NO, vec(m)), ms(g.QI(F(-1, 2)) * Qm(m), NINF))


def line(m):
    X = X_of(m)
    images = [apply(X, b) for b in HALF]
    Mt = [[images[j][i] for j in range(len(HALF))] for i in range(N)]
    ker = g.field_kernel(Mt)
    return [[sum((k[j] * HALF[j][i] for j in range(len(HALF))), Z) for i in range(N)] for k in ker]


def conjp(m):
    return {a: c.conj() for a, c in m.items()}


def sigma(u, v):
    return ip(u, apply(J, v))


def rows_basis(B):
    rows = []
    for i in range(N):
        if g.field_rank([[B[k][r] for k in range(len(B))] for r in rows + [i]]) > len(rows):
            rows.append(i)
    return rows


class Polarisation(object):
    """h_m = Sigma on L(m), -Sigma on L(mbar)."""

    def __init__(self, m):
        self.L, self.Lb = line(m), line(conjp(m))
        self.B = self.L + self.Lb
        self.rows = rows_basis(self.B)

    def J(self, v):
        M = [[self.B[k][r] for k in range(4)] for r in self.rows]
        c = g.field_solve(M, [v[r] for r in self.rows])
        w = [sum(((c[k] if k < 2 else -c[k]) * self.B[k][i] for k in range(4)), Z) for i in range(N)]
        return w

    def h(self, u, v):
        return sigma(u, self.J(v))

    def gram(self, A, Bv, op=None):
        return [[self.h(a, apply(op, b) if op is not None else b) for b in Bv] for a in A]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def positive_definite(G):
    # Sylvester on a Hermitian matrix with Gaussian-rational entries
    n = len(G)
    for k in range(1, n + 1):
        sub = [r[:k] for r in G[:k]]
        d = det(sub)
        if not (d.im == 0 and d.re > 0):
            return False
    return True


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    return sum(((g.QI(-1) if j % 2 else g.QI(1)) * M[0][j] * det([r[:j] + r[j + 1:] for r in M[1:]])
                for j in range(n)), Z)


def wick_unitary(P):
    """i K is h_m-anti-Hermitian on the half: h_m(iK u, v) + h_m(u, iK v) = 0."""
    iK = ms(g.QI(0, F(1, 2)), E12)
    for u in HALF:
        for v in HALF:
            if P.h(apply(iK, u), v) + P.h(u, apply(iK, v)) != Z:
                return False
    return True


def ue(c, s):
    return {"e1": q(c), "e2": q(s)}


# compatible tube points x_perp + i rho u, u = cosh e1 + sinh e2 (rational: (5/4,3/4), (17/8,15/8), (1,0))
COMPATIBLE = [{"e1": q(0, 1)},
              {"e1": q(0, F(5, 2)), "e2": q(0, F(3, 2))},
              {"e1": q(0, F(17, 24)), "e2": q(0, F(-15, 24)), "e3": q(1)},
              {"e1": q(0, 3), "e3": q(F(1, 2)), "e4": q(-2)}]
# tube points violating it: real part with a boost-plane component, or imaginary part off the boost plane
INCOMPATIBLE = [{"e1": q(0, 1), "e2": q(F(1, 2))},
                {"e1": q(F(1, 3), 2)},
                {"e1": q(0, 2), "e3": q(0, 1)},
                {"e1": q(0, 2), "e2": q(0, 1), "e4": q(0, 1)},
                {"e1": q(0, 1), "e2": q(1), "e3": q(1)}]


def check_wick_rotated_boost_unitary_exactly_over_the_bifurcation_plane():
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    premise("one-relation.spacetime-manifold-vacuum-lines")
    g.check("(e1 e2)^2 = 1", meq(mm(E12, E12), eye()))
    # the polarisation at i e1 is the stored positive structure (identity Gram on the half)
    P0 = Polarisation({"e1": q(0, 1)})
    g.check("h_{i e1} = h on the half", all(P0.h(u, v) == ip(u, v) for u in HALF for v in HALF))
    for m in COMPATIBLE:
        P = Polarisation(m)
        G = [[P.h(u, v) for v in HALF] for u in HALF]
        g.check("h_m positive definite", positive_definite(G))
        g.check("Wick-rotated boost h_m-unitary at a compatible point", wick_unitary(P))
        # equivalently 2K swaps L(m) and L(mbar)
        Xb, Xm_ = X_of(conjp(m)), X_of(m)
        g.check("e1e2 maps L(m) into L(mbar)",
                all(x == Z for v in P.L for x in apply(Xb, apply(E12, v))))
        g.check("e1e2 maps L(mbar) into L(m)",
                all(x == Z for v in P.Lb for x in apply(Xm_, apply(E12, v))))
        # fixed by the wedge reflection m -> R(mbar), R = -1 on e1, e2
        Rfix = {a: (-c.conj() if a in ("e1", "e2") else c.conj()) for a, c in m.items()}
        g.check("compatible point fixed by the wedge reflection",
                all(Rfix.get(a, Z) == m.get(a, Z) for a in ["e1", "e2", "e3", "e4"]))
    for m in INCOMPATIBLE:
        P = Polarisation(m)
        G = [[P.h(u, v) for v in HALF] for u in HALF]
        g.check("h_m positive definite (tube point)", positive_definite(G))
        g.check("Wick-rotated boost not h_m-unitary off the set", not wick_unitary(P))
        Rfix = {a: (-c.conj() if a in ("e1", "e2") else c.conj()) for a, c in m.items()}
        g.check("incompatible point not fixed by the wedge reflection",
                not all(Rfix.get(a, Z) == m.get(a, Z) for a in ["e1", "e2", "e3", "e4"]))
    return True


def check_wick_rotation_is_antiperiodic_with_weights_one_half():
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    # exp(i theta K) = cos(theta/2) + i sin(theta/2) e1e2 since (e1e2)^2 = 1; eigenvalues of e1e2 on the half
    plus = span_basis([apply(madd(eye(), E12), v) for v in HALF])
    minus = span_basis([apply(madd(eye(), ms(-1, E12)), v) for v in HALF])
    g.check("e1e2 = +1 on a plane and -1 on a plane of the half", len(plus) == 2 and len(minus) == 2)
    g.check("plus plane is +1", all(apply(E12, v) == v for v in plus))
    # so iK has eigenvalues +- i/2: exp(i theta K) has e^{+- i theta/2}; at theta = 2 pi it is cos(pi) = -1
    # exact rational stand-in: the rotor at a Pythagorean half angle is unitary and its square composes
    c, s = F(3, 5), F(4, 5)
    U = madd(ms(q(c), eye()), ms(q(0, s), E12))
    g.check("Wick rotor unitary for h", meq(mm(dag(U), U), eye()))
    U2 = mm(U, U)
    g.check("double angle rotor", meq(U2, madd(ms(q(c * c - s * s), eye()), ms(q(0, 2 * c * s), E12))))
    # quarter turn and full turn: (1 + i e1e2)^2 = 2 i e1e2, (2 i e1e2)^2 = -4: the 2 pi rotor is -1
    Uq = madd(eye(), ms(IU, E12))
    g.check("half turn of the rotor is i e1e2 (times 2)", meq(mm(Uq, Uq), ms(q(0, 2), E12)))
    g.check("full turn is -1 (times 4): antiperiodic", meq(mm(mm(Uq, Uq), mm(Uq, Uq)), ms(-4, eye())))
    return True


def conj_by(U, Uinv, M):
    return mm(U, mm(M, Uinv))


def check_quarter_turn_takes_tube_point_to_observer():
    premise("one-relation.spacetime-manifold-vacuum-lines")
    premise("synthesis.twistor-form-states-only-off-the-real-slice")
    Uq = madd(eye(), ms(IU, E12))                         # sqrt(2) exp(i pi/4 e1e2)
    Uqi = ms(g.QI(F(1, 2)), madd(eye(), ms(-1, ms(IU, E12))))
    g.check("inverse", meq(mm(Uq, Uqi), eye()))
    # the quarter turn sends i rho u to the real right-wedge point rho s, s = sinh e1 + cosh e2
    for rho, ch, sh in [(1, 1, 0), (2, F(5, 4), F(3, 4)), (F(1, 3), F(17, 8), F(-15, 8))]:
        m = {"e1": q(0, rho * ch), "e2": q(0, rho * sh), "e3": q(F(2, 7))}
        x = {"e1": q(rho * sh), "e2": q(rho * ch), "e3": q(F(2, 7))}
        g.check("rotated null vector is X(observer)", meq(conj_by(Uq, Uqi, X_of(m)), X_of(x)))
        g.check("observer is in the right wedge", Qm({"e1": q(rho * sh), "e2": q(rho * ch)}) == q(-rho * rho))
    # the boost of the (t,r) plane fixes nO, ninf and moves x along its orbit; it commutes with N and DIL
    c, s = F(5, 4), F(3, 4)
    S = madd(ms(q(c), eye()), ms(q(s), E12))
    Si = madd(ms(q(c), eye()), ms(q(-s), E12))
    g.check("boost inverse", meq(mm(S, Si), eye()))
    g.check("boost fixes nO", meq(conj_by(S, Si, NO), NO))
    g.check("boost commutes with N", meq(mm(S, NUM), mm(NUM, S)))
    g.check("dilation commutes with N", meq(mm(DIL, NUM), mm(NUM, DIL)))
    return True


def check_observer_point_tracial_exactly_at_its_tube_point():
    premise("synthesis.incidence-vacua-thermofield-real-capacity")
    premise("synthesis.boost-stationary-incidence-vacua-read-interval")
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    half = g.QI(F(1, 2))
    # KMS for the boost forces <N> = 1/2: a = nO and a* = ninf/2 are boost invariant, {a, a*} = 1
    c, s = F(5, 4), F(3, 4)
    S = madd(ms(q(c), eye()), ms(q(s), E12))
    Si = madd(ms(q(c), eye()), ms(q(-s), E12))
    g.check("boost fixes a", meq(mm(S, mm(NO, Si)), NO))
    g.check("boost fixes a*", meq(mm(S, mm(NINF, Si)), NINF))
    g.check("{a, a*} = 1", meq(madd(mm(NO, ms(half, NINF)), mm(ms(half, NINF), NO)), eye()))
    obs = []
    for rho, ch, sh in [(1, 1, 0), (2, F(5, 4), F(3, 4)), (F(1, 3), F(17, 8), F(-15, 8))]:
        m = {"e1": q(0, rho * ch), "e2": q(0, rho * sh)}
        x = {"e1": q(rho * sh), "e2": q(rho * ch)}
        obs.append((m, x))
    for i, (m, _) in enumerate(obs):
        P = Polarisation(m)
        g.check("N h_m-Hermitian", all(P.h(u, apply(NUM, v)) == P.h(apply(NUM, u), v) for u in HALF for v in HALF))
        for j, (_, x) in enumerate(obs):
            L = line(x)
            G = P.gram(L, L)
            GN = P.gram(L, L, NUM)
            tracial = meq(GN, ms(half, G))
            g.check("h_m positive on the observer's line", positive_definite(G))
            if i == j:
                g.check("every vacuum on the observer's line has occupation 1/2", tracial)
                # Omega_x is a maximally entangled ascent/boost-qubit pair: its ascent marginal is the trace
            else:
                g.check("not tracial at another orbit point or scale", not tracial)
    # a different scale on the same ray, and a point of the same orbit, are not tracial
    P = Polarisation({"e1": q(0, 2)})
    for x in [{"e2": q(1)}, {"e2": q(3)}, {"e1": q(F(3, 4)), "e2": q(F(5, 4))}]:
        L = line(x)
        g.check("tracial only at rho = 2 on the axis",
                not meq(P.gram(L, L, NUM), ms(half, P.gram(L, L))))
    L = line({"e2": q(2)})
    g.check("tracial at rho = 2", meq(P.gram(L, L, NUM), ms(half, P.gram(L, L))))
    return True


def check_ascent_pair_fixes_the_foot():
    premise("synthesis.incidence-vacua-thermofield-real-capacity")
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    half = g.QI(F(1, 2))
    c, s = F(5, 4), F(3, 4)
    S = madd(ms(q(c), eye()), ms(q(s), E12))
    Si = madd(ms(q(c), eye()), ms(q(-s), E12))
    g.check("boost rotor has inverse (pins its entries)", meq(mm(S, Si), eye()))
    P0 = Polarisation({"e1": q(0, 1)})
    g.check("P0 is the stored structure h", all(P0.h(u, v) == ip(u, v) for u in HALF for v in HALF))
    FEET = [({"e3": q(F(1, 2))}, F(-1, 4)), ({"e3": q(1)}, F(-1)), ({"e3": q(2), "e4": q(-1)}, F(-5))]
    SCALES = [((1, 1, 0), 1), ((2, F(5, 4), F(3, 4)), 4)]
    for foot, qf in FEET:
        g.check("tabulated Q(foot)", Qm(foot) == q(qf))
        g.check("N_c - N_0 = ninf c over two",
                meq(madd(mm(ms(half, NINF), X_of(foot)), ms(-1, NUM)), mm(ms(half, NINF), vec(foot))))
        ac = X_of(foot)
        acs = ms(half, NINF)
        Nc = mm(acs, ac)
        g.check("a_c boost invariant", meq(mm(S, mm(ac, Si)), ac))
        g.check("{a_c, a_c*} is the identity", meq(madd(mm(ac, acs), mm(acs, ac)), eye()))
        g.check("N_c not Hermitian at foot zero",
                not all(P0.h(u, apply(Nc, v)) == P0.h(apply(Nc, u), v) for u in HALF for v in HALF))
        for (rho, ch, sh), rho2 in SCALES:
            g.check("unit timelike u (pins cosh, sinh)", ch * ch - sh * sh == q(1).re)
            g.check("tabulated rho squared", rho * rho == rho2)
            m = dict(foot)
            m["e1"] = q(0, rho * ch)
            m["e2"] = q(0, rho * sh)
            x = dict(foot)
            x["e1"] = q(rho * sh)
            x["e2"] = q(rho * ch)
            P = Polarisation(m)
            g.check("N_c h_m-Hermitian over its base point",
                    all(P.h(u, apply(Nc, v)) == P.h(apply(Nc, u), v) for u in HALF for v in HALF))
            g.check("N_0 not h_m-Hermitian over a nonzero foot",
                    not all(P.h(u, apply(NUM, v)) == P.h(apply(NUM, u), v) for u in HALF for v in HALF))
            L = line(x)
            g.check("tracial for N_c on the observer's line", meq(P.gram(L, L, Nc), ms(half, P.gram(L, L))))
            g.check("not tracial for N_0 there", not meq(P.gram(L, L, NUM), ms(half, P.gram(L, L))))
    return True
