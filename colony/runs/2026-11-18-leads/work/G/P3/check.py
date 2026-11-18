"""The slaved field's failure read as a signal: a classical source shifts the fringe at first order.

Matter: one quantum on two paths. The stored model's Cl(1,1) (e1^2 = 1, e2^2 = -1) sits in Cl(1,2) (e3^2 = -1),
whose pseudoscalar I = e1 e2 e3 is central with I^2 = -1: the unit of the phases. P1 = vw, P2 = wv, J = c1 P1 + c2 P2,
recombiner U = p + q e2, detection O = U^-1 P1 U. States are idempotents rho = (1 + a e1 + b I e2)/2, a^2 + b^2 = 1,
with expectation <x> = 2 <rho x>_0.

Slaved field of the stored model: phi_n(t) = g J S(n, t), S = sum_t' G(n, t; t'), G the retarded response of the
lattice field phi_n(t+1) = phi_{n+1}(t) + phi_{n-1}(t) - phi_n(t-1) to a unit source at site 0, time t'.
Bob's device is a classical source of strength lam at the event (n, t): the unit V = exp(-I lam phi_n(t)).

(1) Cl(1,2): the central unit, the states, V a unit with V^-1 its conjugate;
(2) the change of Alice's detection probability under V is p q [a (cos th - 1) + b sin th], th = lam g S (c1 - c2):
    first order in lam, with coefficient g S (c1 - c2) p q b = <I [phi_n(t), O]> ; at most |sin(th/2)|;
(3) S is nonzero at 172 of the 502 events of the stored grid spacelike to the detection; at the 32 of them not
    later than the detection the device, acting first, changes Alice's probability;
(4) the gravitational size of th for the proposed experiments and for a source mass in Bob's hands;
(5) the curvature level of the cutoff premise is not reached anywhere in such a configuration.
"""
from fractions import Fraction as F

import GA
from GA import add, gen, mul, scal, sc, sub
from tp_premise import premise

S12 = GA.sig(1, 2)

# ---------------------------------------------------------------------------------------------------------
# constants (module level)
# ---------------------------------------------------------------------------------------------------------
L, TMAX = 40, 18
N = 2 * L + 1
KICKS = list(range(0, 6))
TDET = 8
WINDOW = range(-18, 19)
C1C2 = (F(7), F(2))
PQ = (F(3, 5), F(4, 5))
HALF_ANGLE = (F(4, 5), F(3, 5))            # cos(th/2), sin(th/2)
STATE = (F(-3, 5), F(4, 5))                # (a, b): the state at which the change is largest for this angle
STATE_REAL = (F(1), F(0))                  # the stored model's real state: no first-order change
COUPLING = F(1, 3)
EVENT_A, EVENT_B = (7, 8), (3, 8)          # two events spacelike to the detection (0, 8), at its time

# gravitational sizes, SI units, as rational enclosures
G_OVER_HBAR_C = (F(211, 100) * 10 ** 15, F(212, 100) * 10 ** 15)   # 1/m_P^2 in kg^-2: 2.111e15
M_A = F(1, 10 ** 14)                       # kg, the superposed mass of the proposed experiments
SEP = F(250, 10 ** 6)                      # m, separation of its two paths
D_NEAR = F(450, 10 ** 6)                   # m, distance of the second mass in the proposed experiments
D_FAR = F(1)                               # m, distance of a source mass in Bob's hands
THRESHOLD = F(1, 1000)                     # registered: a change of probability below this is unobservable
PLANCK_LENGTH = (F(161, 100) / 10 ** 35, F(162, 100) / 10 ** 35)   # m
PLANCK_MASS = (F(217, 100) / 10 ** 8, F(218, 100) / 10 ** 8)       # kg


def idx(n):
    return n + L


def response(tp):
    """the stored model's retarded response: zero data and a unit source into phi_0(tp + 1)."""
    field = {0: [0] * N, 1: [0] * N}
    if tp == 0:
        field[1][idx(0)] += 1
    for t in range(1, TMAX):
        nxt = []
        for i in range(N):
            s = -field[t - 1][i]
            if i - 1 >= 0:
                s += field[t][i - 1]
            if i + 1 < N:
                s += field[t][i + 1]
            nxt.append(s)
        if t == tp:
            nxt[idx(0)] += 1
        field[t + 1] = nxt
    return field


def slaved_sum():
    G = {tp: response(tp) for tp in KICKS}
    return lambda n, t: sum(G[tp][t][idx(n)] for tp in KICKS)


def spacelike_events():
    return [(n, t) for t in range(0, TMAX + 1) for n in WINDOW if abs(n) > abs(TDET - t)]


# ---- matter in Cl(1,2) ---------------------------------------------------------------------------------------
E1, E2, E3 = gen(0), gen(1), gen(2)
I3 = mul(mul(E1, E2, S12), E3, S12)
V_ = scal(F(1, 2), add(E1, E2))
W_ = scal(F(1, 2), sub(E1, E2))
P1, P2 = mul(V_, W_, S12), mul(W_, V_, S12)
ONE = sc(1)


def m3(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = mul(out, x, S12)
    return out


def dagger(x):
    """the conjugation that inverts every generator and reverses products (e1 fixed, e2, e3, I negated)."""
    out = {}
    for blade, c in GA.reverse(x).items():
        sign = 1
        for i in blade:
            if i != 0:
                sign = -sign
        out[blade] = sign * c
    return out


def expect(rho, x):
    return 2 * m3(rho, x).get((), F(0))


def state(a, b):
    return scal(F(1, 2), add(ONE, scal(a, E1), scal(b, m3(I3, E2))))


def detection(p, q):
    U, Uinv = add(sc(p), scal(q, E2)), sub(sc(p), scal(q, E2))
    return m3(Uinv, P1, U)


def kick(c, s):
    """V = P1 + (cos th - I sin th) P2: the unit exp(-I lam phi) up to a phase, th the angle between the paths
    (the factor on P2 relative to P1 is exp(+I th) when th = lam g S (c1 - c2))."""
    return add(P1, m3(add(sc(c), scal(s, I3)), P2))


def comm(x, y):
    return sub(m3(x, y), m3(y, x))


# ---------------------------------------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------------------------------------
def check_matter_algebra_has_a_central_unit_and_the_device_is_a_unit():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    ok = True
    ok = ok and GA.eq(m3(I3, I3), sc(-1))
    ok = ok and all(GA.commutes(I3, x, S12) for x in (E1, E2, E3))
    ok = ok and GA.eq(m3(P1, P1), P1) and GA.eq(add(P1, P2), ONE) and GA.is_zero(m3(P1, P2))
    ch, sh = HALF_ANGLE
    c, s = ch * ch - sh * sh, 2 * ch * sh
    ok = ok and (c, s) == (F(7, 25), F(24, 25)) and c * c + s * s == 1
    V = kick(c, s)
    ok = ok and GA.eq(m3(V, dagger(V)), ONE) and GA.eq(m3(dagger(V), V), ONE)
    ok = ok and GA.eq(dagger(I3), scal(-1, I3)) and GA.eq(dagger(P1), P1)
    for (a, b) in (STATE, STATE_REAL):
        rho = state(a, b)
        ok = ok and GA.eq(m3(rho, rho), rho) and GA.eq(dagger(rho), rho) and expect(rho, ONE) == 1
        ok = ok and expect(rho, P1) == F(1, 2)
        O = detection(*PQ)
        ok = ok and 0 <= expect(rho, O) <= 1 and 0 <= expect(rho, m3(dagger(V), O, V)) <= 1
    GA.check("Cl(1,2): the pseudoscalar is central with square -1; the path projectors, two states and the detection "
             "are as stated; the device's V is a unit with inverse its conjugate; probabilities lie in [0, 1]", ok)
    return ok


def check_classical_source_shifts_the_detection_probability_at_first_order():
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    ok = True
    p, q = PQ
    c1, c2 = C1C2
    O = detection(p, q)
    J = add(scal(c1, P1), scal(c2, P2))
    ch, sh = HALF_ANGLE
    c, s = ch * ch - sh * sh, 2 * ch * sh
    V = kick(c, s)
    # V^-1 e1 V = e1 cos th + I e2 sin th, and the change of <O> is p q [a (cos th - 1) + b sin th]
    ok = ok and GA.eq(m3(dagger(V), E1, V), add(scal(c, E1), scal(s, m3(I3, E2))))
    for (a, b) in (STATE, STATE_REAL):
        rho = state(a, b)
        change = expect(rho, m3(dagger(V), O, V)) - expect(rho, O)
        ok = ok and change == p * q * (a * (c - 1) + b * s)
    a, b = STATE
    change = expect(state(a, b), m3(dagger(V), O, V)) - expect(state(a, b), O)
    ok = ok and change == F(72, 125) and change == 2 * p * q * sh and change <= sh
    # first order: d<O>/d(lam) at lam = 0 is <I [phi, O]> = g S (c1 - c2) p q b
    S = slaved_sum()
    g = COUPLING
    for (ev, sval) in ((EVENT_A, 1), (EVENT_B, 3)):
        ok = ok and S(*ev) == sval and abs(ev[0]) > abs(TDET - ev[1]) and ev[1] <= TDET
        phi = scal(g * S(*ev), J)
        first = expect(state(a, b), m3(I3, comm(phi, O)))
        ok = ok and first == g * sval * (c1 - c2) * p * q * b and first != 0
        ok = ok and expect(state(*STATE_REAL), m3(I3, comm(phi, O))) == 0
    ok = ok and GA.eq(comm(J, O), scal((c1 - c2) * p * q, E2))
    GA.check("slaved field: a classical source at the event changes the detection probability by "
             "p q [a (cos th - 1) + b sin th] (72/125 at the half-angle (4/5, 3/5), within |sin(th/2)| = 3/5); the "
             "first-order coefficient is g S (c1 - c2) p q b, nonzero at the spacelike events (7, 8) and (3, 8)", ok)
    return ok


def check_signal_exists_at_172_of_502_spacelike_events():
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    S = slaved_sum()
    sl = spacelike_events()
    p, q = PQ
    c1, c2 = C1C2
    a, b = STATE
    coeff = {ev: COUPLING * S(*ev) * (c1 - c2) * p * q * b for ev in sl}
    ok = len(sl) == 502 and sum(1 for ev in sl if coeff[ev] != 0) == 172
    # the device acts before the detection at the events with t <= 8: 32 of those 252 carry a signal to Alice;
    # at the 140 later ones the same commutator makes the field depend on whether Alice recombined
    early = [ev for ev in sl if ev[1] <= TDET]
    ok = ok and len(early) == 252 and sum(1 for ev in early if coeff[ev] != 0) == 32
    ok = ok and sum(1 for ev in sl if ev[1] > TDET and coeff[ev] != 0) == 140
    # the earliest such events are at time 5, three steps before the detection; every one is in the forward cone
    # of a source event
    ok = ok and min(t for (n, t) in sl if coeff[(n, t)] != 0) == 5
    ok = ok and all(any(abs(n) <= t - tp - 1 for tp in KICKS) for (n, t) in sl if coeff[(n, t)] != 0)
    ok = ok and max(abs(coeff[ev]) for ev in sl) == COUPLING * 3 * (c1 - c2) * p * q * b
    GA.check("the first-order coefficient g S (c1 - c2) p q b is nonzero at 172 of the 502 spacelike events of the "
             "stored grid: at 32 of the 252 events not later than the detection, where the device acts first, and at "
             "140 later ones; the largest is g 3 (c1 - c2) p q b", ok)
    return ok


def check_gravitational_size_of_the_phase_in_the_window():
    premise("field-theory.operator-newtonian-coupling")
    ok = True
    lo, hi = G_OVER_HBAR_C

    def geometry(dist, sep):
        """D |1/r1 - 1/r2| for a mass on the line of the two paths at distance D from their midpoint."""
        return dist * (1 / (dist - sep / 2) - 1 / (dist + sep / 2))
    # proposed experiments: two masses of 1e-14 kg, 250 micrometres, at 450 micrometres
    geo = geometry(D_NEAR, SEP)
    ok = ok and geo == F(1800, 2990)
    phase = (lo * M_A * M_A * geo, hi * M_A * M_A * geo)
    ok = ok and F(127, 10 ** 15) < phase[0] and phase[1] < F(128, 10 ** 15)
    ok = ok and phase[1] / 2 < THRESHOLD / 10 ** 10                    # ten orders below the registered threshold
    runs = (4 / phase[1] ** 2, 4 / phase[0] ** 2)                      # runs for eps sqrt(N) = 1 with eps = phase/2
    ok = ok and 10 ** 26 < runs[0] and runs[1] < 10 ** 27
    # a source mass of one kilogram at one metre from the same superposition: above the threshold
    geo2 = geometry(D_FAR, SEP)
    ok = ok and F(25, 10 ** 5) < geo2 < F(26, 10 ** 5)
    phase_kg = (lo * M_A * 1 * geo2, hi * M_A * 1 * geo2)
    ok = ok and F(52, 10 ** 4) < phase_kg[0] and phase_kg[1] < F(54, 10 ** 4)
    ok = ok and phase_kg[0] / 2 > THRESHOLD
    # a tonne at one metre: a phase of order one
    ok = ok and 5 < 1000 * phase_kg[0] and 1000 * phase_kg[1] < 6
    # the product of masses at which the phase is one, for geometry factor one: the square of the Planck mass
    ok = ok and F(47, 10 ** 17) < 1 / hi and 1 / lo < F(48, 10 ** 17)
    ok = ok and PLANCK_MASS[0] ** 2 < 1 / hi and 1 / lo < PLANCK_MASS[1] ** 2
    GA.check("phase G m_A m_B D |1/r1 - 1/r2| / (hbar c) accumulated within one light-crossing time: 1.27e-13 for two "
             "masses of 1e-14 kg at 450 micrometres (ten orders below the registered threshold, more than 1e26 runs), "
             "5.3e-3 for a kilogram at a metre (above it), 5.3 for a tonne; it is one when m_A m_B is the Planck "
             "mass squared", ok)
    return ok


def check_curvature_level_of_the_cutoff_premise_is_not_reached_outside_the_bodies():
    premise("field-theory.operator-newtonian-coupling")      # the configuration is that of the static coupling
    ok = True
    # (C1): boundary modes sit where 2M/r^3 = 1 in Planck units. For a body of mass m at distance r:
    # 2 (m/m_P) (l_P/r)^3, largest for the tonne at the surface of a ball of 10 cm
    lP_hi, mP_lo = PLANCK_LENGTH[1], PLANCK_MASS[0]
    level = 2 * (1000 / mP_lo) * (lP_hi / F(1, 10)) ** 3
    ok = ok and level < F(1, 10 ** 90)
    # the radius at which the level would be one, for the tonne: (2M)^(1/3) Planck lengths, below 1e-31 m,
    # and inside the Schwarzschild radius 2M of that mass, itself below 1e-23 m
    two_m = 2 * 1000 / mP_lo
    ok = ok and two_m < (F(1, 10 ** 31) / lP_hi) ** 3 and two_m * lP_hi < F(1, 10 ** 23)
    ok = ok and two_m > 1 and two_m ** 3 > two_m          # (2M)^(1/3) < 2M: the locus is inside the horizon radius
    GA.check("the curvature level 2M/r^3 = 1 of the cutoff premise: for a tonne it is below 1e-90 at ten centimetres, "
             "and is reached only at a radius below 1e-31 m, inside the radius 2M of a hole of that mass", ok)
    return ok
