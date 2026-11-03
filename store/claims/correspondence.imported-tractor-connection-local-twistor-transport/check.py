"""correspondence.imported-tractor-connection-local-twistor-transport: exact checks in Cl(2,4).

Generators e0 (square +1), e1, e2, e3 (square -1), e+ (square +1), e- (square -1); n0 = (e+ + e-)/2,
ninf = e+ - e-, so Q(n0) = Q(ninf) = 0 and n0 . ninf = 1. A tractor in the splitting of the scale is
V = sigma ninf + mu + rho n0. The gravitational field on flat spacetime is a sample position-gauge
field hb (a linear map, given through hb^{-1}), a sample rotation-gauge field Omega(a) (spacetime
bivectors) and a sample symmetric Schouten map P; Omega_T(a) = Omega(a) - ninf ^ A + n0 ^ P(A), A = hb^{-1}(a).
  (i)  D^T_a V = a.grad V + Omega_T(a) x V has the slots (a.grad sigma - mu.A, a.grad mu + Omega(a) x mu
       + rho A - sigma P(A), a.grad rho + P(A).mu) of the displayed connection, on affine tractor fields
       (a.grad by the central difference, exact on them), nothing outside the slots, and it is metric:
       a.grad Q(V) = 2 V . D^T_a V.
  (ii) The conformal spinor space CS = Cl^+(2,4) P, P = (1 + e0e1)(1 + e2e+)/4: real dimension 8, stable
       under I6 with I6^2 = -1, so C^4 over I6. The pi-plane is the kernel of the point's null vector n0
       in CS and the omega-plane the kernel of ninf; each is an I6-stable plane (complex dimension 2) and
       CS is their sum; the grading ninf ^ n0 acts by -1 and +1 on them. The spin action rho(B) = B/2 of
       Omega_T(a) commutes with I6 (so the factor i of the transport is I6), keeps the Lorentz part
       inside each plane, its soldering part maps pi -> omega and kills omega, its Schouten part maps
       omega -> pi and kills pi, with composite (1/2) A P(C) on omega; and rho is the spin form of the
       tractor action: rho(B)(v psi) - v rho(B) psi = (B x v) psi.
       Under a change of scale (the null rotation U = 1 - n0 Y/2 that fixes n0) the tractor slots move by
       (sigma, mu + sigma Y, rho - Y.mu - sigma Q(Y)/2), the pi-plane is carried to itself, omega is
       invariant (U psi - psi lies in the pi-plane) and pi shifts.
The Penrose-Rindler 2-spinor index form of (ii) is not computed: the check works with the planes and
the block form that it expresses.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
BLADES = GA.all_blades(6)


def mul(*xs):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, S)
    return r


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def linmap(M):
    """A -> sum_n (sum_m M[m][n] A.e^m) e_n on spacetime vectors."""
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), E[n])
                              for n in range(4)])

def symmap(M):
    """A -> sum_n (sum_m M[m][n] A.e^m) e^n: for symmetric M a metric-symmetric map (P(e_m).e_n = M[m][n])."""
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), ER[n])
                              for n in range(4)])


def tractor(sig, mu, rho):
    return GA.add(GA.scal(sig, NI), mu, GA.scal(rho, N0))


def slots(V):
    return dot(V, N0), {b: c for b, c in V.items() if len(b) == 1 and b[0] < 4}, dot(V, NI)


def coords(xs):
    return [GA.basis_vector_of(x, BLADES) for x in xs]


def rank(xs):
    return GA.rank_of_vectors(coords(xs)) if xs else 0


# ------------------------------------------------------------------ generic field data (module level)
HINV = [[2, 1, 0, 0], [0, 1, 0, -1], [1, 0, 3, 0], [0, 0, 1, 1]]        # hb^{-1}, invertible
PSYM = [[2, 1, 0, -3], [1, -1, 4, 0], [0, 4, 5, 2], [-3, 0, 2, 7]]      # Schouten components
OMEGA = {0: [(0, 1, 2), (2, 3, -1)], 1: [(1, 2, 1)], 2: [(0, 3, 3), (1, 3, 1)], 3: [(0, 2, -2)]}
DIRS = ([1, 0, 0, 0], [0, 1, 2, 0], [3, 1, -2, 5])
# affine tractor fields: sigma = s0 + s.x, mu = m0 + M x, rho = r0 + r.x
FIELDS = [((2, [1, 0, -1, 0]), ([1, 0, 3, -1], [[0, 1, 0, 0], [2, 0, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0]]),
           (-7, [0, 2, 0, 1])),
          ((-1, [0, 0, 2, 1]), ([0, 4, 1, 1], [[1, 0, 0, 0], [0, 0, 0, 0], [0, 3, 0, 0], [0, 0, 0, 2]]),
           (5, [1, 0, 0, 0]))]
UPS = [[1, 2, 0, -1], [0, 1, 1, 3], [2, 0, -1, 0]]
POINTS = ([0, 0, 0, 0], [1, -1, 2, 0])      # sample points where the connection is evaluated
X_HAND, A_HAND = [0, 0, 0, 0], [1, 0, 0, 0]  # point and direction of the by-hand value (x = 0, a = e0)


def omega_of(a):
    """Omega(a) = sum_m a^m Omega(e_m), a sample linear map to spacetime bivectors."""
    out = {}
    for m in range(4):
        am = dot(a, ER[m])
        for (i, j, c) in OMEGA[m]:
            out = GA.add(out, GA.scal(am * c, mul(E[i], E[j])))
    return out


def field_at(fd, x):
    (s0, s), (m0, M), (r0, r) = fd
    sig = F(s0) + sum(F(s[i]) * x[i] for i in range(4))
    mu = vec([F(m0[n]) + sum(F(M[n][i]) * x[i] for i in range(4)) for n in range(4)])
    rho = F(r0) + sum(F(r[i]) * x[i] for i in range(4))
    return tractor(sig, mu, rho)


def deriv(fd, x, a):
    """a.grad of the field at x by the central difference (exact on affine fields)."""
    xp = [x[i] + a[i] for i in range(4)]
    xm = [x[i] - a[i] for i in range(4)]
    return GA.scal(F(1, 2), GA.sub(field_at(fd, xp), field_at(fd, xm)))


def omega_T(a, P, hinv):
    A = hinv(vec(a))
    return GA.add(omega_of(vec(a)), GA.neg(comm(NI, A)), comm(N0, P(A)))


def check_tractor_connection_in_a_scale():
    premise("interior.imported-tractor-connection")
    P, hinv = symmap(PSYM), linmap(HINV)
    ok = True
    for fd in FIELDS:
        for x in POINTS:
            V = field_at(fd, x)
            sig, mu, rho = slots(V)
            for a in DIRS:
                A = hinv(vec(a))
                dV = deriv(fd, x, a)
                ds, dmu, dr = slots(dV)
                DV = GA.add(dV, comm(omega_T(a, P, hinv), V))
                s1, m1, r1 = slots(DV)
                ok = ok and s1 == ds - dot(mu, A)
                ok = ok and GA.eq(m1, GA.add(dmu, comm(omega_of(vec(a)), mu), GA.scal(rho, A),
                                             GA.scal(-sig, P(A))))
                ok = ok and r1 == dr + dot(P(A), mu)
                ok = ok and GA.eq(DV, tractor(s1, m1, r1))
                # metric: a.grad Q(V) = 2 V . D^T_a V (Q(V) quadratic, so the central difference is exact)
                xp = [x[i] + a[i] for i in range(4)]
                xm = [x[i] - a[i] for i in range(4)]
                Vp, Vm = field_at(fd, xp), field_at(fd, xm)
                dQ = (dot(Vp, Vp) - dot(Vm, Vm)) / 2
                ok = ok and dQ == 2 * dot(V, DV)
    # by hand: first field at x = 0 along a = e0: A = hb^{-1}(e0) = 2 e0 + e1; sigma = 2, mu = (1,0,3,-1),
    # rho = -7; a.grad sigma = 1 and mu.A = 2, so the sigma slot is 1 - 2 = -1
    V = field_at(FIELDS[0], X_HAND)
    DV = GA.add(deriv(FIELDS[0], X_HAND, A_HAND), comm(omega_T(A_HAND, P, hinv), V))
    ok = ok and slots(DV)[0] == -1
    ok = ok and GA.eq(hinv(E[0]), GA.add(GA.scal(2, E[0]), E[1]))
    GA.check("tractor gauge field reproduces the displayed connection in the scale and is metric", ok)
    assert ok


# ------------------------------------------------------------------ the conformal spinor space
I6 = mul(*E)
SPIN_VECS = (E[0], E[2], N0, NI)            # sample vectors (timelike, spacelike, both null) for the spin form
PID = GA.scal(F(1, 4), mul(GA.add(GA.sc(1), mul(E[0], E[1])), GA.add(GA.sc(1), mul(E[2], E[4]))))


def _cs_basis():
    out = []
    for b in BLADES:
        if len(b) % 2:
            continue
        c = GA.mul({b: F(1)}, PID, S)
        if rank(out + [c]) == len(out) + 1:
            out.append(c)
    return out


CS = _cs_basis()


def kernel_in_cs(v):
    """Real basis of {psi in CS : v psi = 0}."""
    cols = coords([mul(v, psi) for psi in CS])
    M = [[F(cols[j][r]) for j in range(len(CS))] for r in range(len(BLADES))]
    M = [row for row in M if any(row)]
    if not M:
        return list(CS)
    ker = GA.field_kernel(M)
    return [GA.add(*[GA.scal(k[j], CS[j]) for j in range(len(CS)) if k[j]]) for k in ker]


def in_span(x, basis):
    return rank(basis + [x]) == rank(basis)


def rho(B, psi):
    return GA.scal(F(1, 2), mul(B, psi))


def check_conformal_spinor_space_and_its_planes():
    premise("correspondence.imported-tractor-connection-local-twistor-transport-external")
    ok = GA.eq(mul(PID, PID), PID) and mul(I6, I6) == {(): F(-1)}
    ok = ok and len(CS) == 8                                     # real dimension 8: C^4 over I6
    ok = ok and all(in_span(mul(I6, psi), CS) for psi in CS)
    pi_plane, om_plane = kernel_in_cs(N0), kernel_in_cs(NI)
    ok = ok and len(pi_plane) == 4 and len(om_plane) == 4       # complex dimension 2 each
    ok = ok and all(in_span(mul(I6, p), pi_plane) for p in pi_plane)
    ok = ok and all(in_span(mul(I6, p), om_plane) for p in om_plane)
    ok = ok and rank(pi_plane + om_plane) == 8                   # CS = omega-plane + pi-plane
    grading = comm(NI, N0)
    ok = ok and all(GA.eq(mul(grading, p), GA.neg(p)) for p in pi_plane)
    ok = ok and all(GA.eq(mul(grading, p), p) for p in om_plane)
    # a non-null vector has no kernel in CS
    ok = ok and kernel_in_cs(GA.add(NI, GA.scal(F(1, 3), N0))) == []
    GA.check("conformal spinor space is C^4 over I6, split into the pi-plane ker n0 and the omega-plane ker ninf", ok)
    assert ok


def check_conformal_spinor_connection_block_form():
    premise("correspondence.imported-tractor-connection-local-twistor-transport-external")
    premise("interior.imported-tractor-connection")
    P, hinv = symmap(PSYM), linmap(HINV)
    pi_plane, om_plane = kernel_in_cs(N0), kernel_in_cs(NI)
    ok = True
    for a in DIRS:
        A = hinv(vec(a))
        lor, sold, sch = omega_of(vec(a)), GA.neg(comm(NI, A)), comm(N0, P(A))
        full = GA.add(lor, sold, sch)
        for psi in CS:
            ok = ok and GA.eq(mul(full, I6, psi), mul(I6, full, psi))          # complex-linear
            ok = ok and in_span(rho(full, psi), CS)
        for p in pi_plane:
            ok = ok and in_span(rho(lor, p), pi_plane)
            ok = ok and in_span(rho(sold, p), om_plane) and not GA.is_zero(rho(sold, p))
            ok = ok and GA.is_zero(rho(sch, p))
        for w in om_plane:
            ok = ok and in_span(rho(lor, w), om_plane)
            ok = ok and GA.is_zero(rho(sold, w))
            ok = ok and in_span(rho(sch, w), pi_plane)
            for c in DIRS:
                C = hinv(vec(c))
                comp = rho(GA.neg(comm(NI, A)), rho(comm(N0, P(C)), w))
                ok = ok and GA.eq(comp, GA.scal(F(1, 2), mul(A, P(C), w)))
        # spin form of the tractor action, on all of CS and the sample vectors SPIN_VECS
        for psi in CS:
            for v in SPIN_VECS:
                lhs = GA.sub(rho(full, mul(v, psi)), mul(v, rho(full, psi)))
                ok = ok and GA.eq(lhs, mul(comm(full, v), psi))
    GA.check("conformal spinor connection: Lorentz part diagonal, soldering pi -> omega, Schouten omega -> pi", ok)
    assert ok


def check_change_of_scale_fixes_omega_and_shifts_pi():
    premise("correspondence.imported-tractor-connection-local-twistor-transport-external")
    premise("interior.imported-tractor-connection")
    pi_plane, om_plane = kernel_in_cs(N0), kernel_in_cs(NI)
    ok = True
    for y in UPS:
        Y = vec(y)
        U = GA.sub(GA.sc(1), GA.scal(F(1, 2), mul(N0, Y)))
        Ut = GA.reverse(U)
        ok = ok and GA.eq(mul(U, Ut), GA.sc(1)) and GA.eq(mul(U, N0, Ut), N0)
        for fd in FIELDS:
            V = field_at(fd, [1, 0, 2, -1])
            sig, mu, rh = slots(V)
            s1, m1, r1 = slots(mul(U, V, Ut))
            ok = ok and s1 == sig and GA.eq(m1, GA.add(mu, GA.scal(sig, Y)))
            ok = ok and r1 == rh - dot(Y, mu) - sig * dot(Y, Y) / 2
        for p in pi_plane:
            ok = ok and in_span(mul(U, p), pi_plane)
        for psi in CS:
            ok = ok and in_span(GA.sub(mul(U, psi), psi), pi_plane)            # omega invariant
        ok = ok and any(not GA.is_zero(GA.sub(mul(U, w), w)) for w in om_plane)  # pi shifts
    # by hand: Y = (1,2,0,-1) has Q(Y) = 1 - 4 - 0 - 1 = -4
    ok = ok and dot(vec(UPS[0]), vec(UPS[0])) == -4
    GA.check("change of scale: null rotation fixing n0 keeps omega and the pi-plane, shifts pi", ok)
    assert ok


EXPORTS = {"S": S, "E": E, "N0": N0, "NI": NI, "I6": I6, "PID": PID, "CS": CS, "mul": mul,
           "comm": comm, "rank": rank, "in_span": in_span, "kernel_in_cs": kernel_in_cs, "rho": rho}
