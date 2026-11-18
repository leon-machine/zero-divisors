"""A lattice model with a constraint: the slaved field, the dressed detection and the transverse part.

Field: a lattice Maxwell field on a box of sites. Each link l carries (A_l, E_l); W(f) = exp(I sum_l f_l A_l) is
the Weyl operator that shifts the electric field, [E_l, W(f)] = f_l W(f), the unit I written as in the field
theory. The constraint at a site s is G_s = (div E)_s - g rho_s, rho the matter's charge.
Matter: one quantum on two sites a, b, in the algebra of a completed pair Cl(1,1): P1 = vw (site a), P2 = wv
(site b), v = P1 v P2 the hop from b to a. Operators of the model are sums of (matter element) x W(f), held as
dictionaries {f: matter element}.

(1) the bare recombiner does not commute with the constraint; the string-dressed one does;
(2) with the field's own variables, the string-dressed detection commutes with E on every link off the string;
(3) the constrained (gradient) part of E alone, which on the constraint surface is g K rho, an element of the
    matter algebra, fails on most links; the transverse part alone fails by the opposite amount; the static slaved
    field (no transverse part: the Coulomb field) is that constrained part and fails with every matter element
    that does not commute with the charge; the detection dressed by the constrained field fails also when the
    field has its own variables;
(3b) a slaved field need not be the Coulomb one: g chi P1 satisfies the constraint and commutes with the bare
    detection off the string, but it is not a static solution of the field equation, and under that equation
    its gradient part stays kappa while the rest spreads;
(4) in one space dimension the constrained part of the string is the string;
(5) dynamics with an exact cone: the string-dressed detection commutes with the field at every spacelike event;
    the slaved retarded field of the constrained model does not, at events that all lie in the forward cone of
    the source event.
"""
from fractions import Fraction as F

import GA
from GA import add, gen, mul, scal, sc, sub
from tp_premise import premise

S11 = GA.sig(1, 1)

# ---------------------------------------------------------------------------------------------------------
# sample geometry and constants (module level)
# ---------------------------------------------------------------------------------------------------------
KBOX = (7, 7)                    # box of the equal-time clauses
KA, KB = (2, 3), (4, 3)          # the two sites of the quantum
CHAIN = (13, 1)
CA, CB = (4, 0), (8, 0)
DBOX = (13, 13)                  # box of the dynamics
DA, DO, DB = (5, 6), (6, 6), (7, 6)
STEP = F(1, 2)                   # time step in units of the lattice spacing
ND, NMAX = 5, 10                 # detection step and last step
ND_OTHER = 7                     # a second detection step, for the remark on a fitted slaved field
COUPLING = F(2, 3)
PQ = (F(3, 5), F(4, 5))
L_ON, L_FAR, L_CORNER, L_AXIS = ('x', 2, 3), ('x', 5, 3), ('y', 0, 0), ('y', 3, 5)   # links of the small box
D_EAST, D_DIAG = ('x', 8, 6), ('y', 7, 8)                 # links of the large box
CANON_LINKS = [('x', 3, 3), ('y', 6, 6)]
STATIC_STEPS = [1, 2, 3]                # steps at which the gradient part of the evolved string is recomputed


class Box:
    def __init__(self, nx, ny):
        self.sites = [(x, y) for x in range(nx) for y in range(ny)]
        self.links = [('x', x, y) for x in range(nx - 1) for y in range(ny)] + \
                     [('y', x, y) for x in range(nx) for y in range(ny - 1)]
        self.plaq = [(x, y) for x in range(nx - 1) for y in range(ny - 1)]
        self.pl = {p: [(('x', p[0], p[1]), 1), (('y', p[0] + 1, p[1]), 1), (('x', p[0], p[1] + 1), -1),
                       (('y', p[0], p[1]), -1)] for p in self.plaq}
        self.lp = {l: [] for l in self.links}
        for p, bd in self.pl.items():
            for l, s in bd:
                self.lp[l].append((p, s))
        self.nb = {l: sorted({m for p, _ in self.lp[l] for m, _ in self.pl[p]} - {l}) for l in self.links}

    def ends(self, l):
        k, x, y = l
        return ((x, y), (x + 1, y)) if k == 'x' else ((x, y), (x, y + 1))

    def div(self, f):
        out = {}
        for l, val in f.items():
            s0, s1 = self.ends(l)
            out[s0] = out.get(s0, 0) + val
            out[s1] = out.get(s1, 0) - val
        return {s: c for s, c in out.items() if c != 0}

    def grad(self, u):
        return {l: u[self.ends(l)[0]] - u[self.ends(l)[1]] for l in self.links}

    def curl(self, A):
        return {p: sum(s * A.get(l, 0) for l, s in bd) for p, bd in self.pl.items()}

    def curlT(self, B):
        return {l: sum(s * B.get(p, 0) for p, s in self.lp[l]) for l in self.links}

    def solve_poisson(self, rho):
        """u with (div grad u) = rho for a source of zero total, u = 0 at the first site; exact."""
        n = len(self.sites)
        sidx = {s: i for i, s in enumerate(self.sites)}
        M = [[F(0)] * (n + 1) for _ in range(n)]
        for l in self.links:
            i, j = sidx[self.ends(l)[0]], sidx[self.ends(l)[1]]
            M[i][i] += 1
            M[j][j] += 1
            M[i][j] -= 1
            M[j][i] -= 1
        for s, c in rho.items():
            M[sidx[s]][n] = F(c)
        M[0] = [F(1)] + [F(0)] * n
        for c in range(n):
            piv = next(r for r in range(c, n) if M[r][c] != 0)
            M[c], M[piv] = M[piv], M[c]
            pv = M[c][c]
            M[c] = [x / pv for x in M[c]]
            for r in range(n):
                if r != c and M[r][c] != 0:
                    fac = M[r][c]
                    M[r] = [x - fac * y for x, y in zip(M[r], M[c])]
        return {s: M[sidx[s]][n] for s in self.sites}

    def longitudinal(self, f):
        """the gradient part of f: the solution of the constraint with the divergence of f and no curl."""
        return self.grad(self.solve_poisson(self.div(f)))

    def dist_from(self, links):
        d = {l: 0 for l in links}
        frontier = list(links)
        while frontier:
            nxt = []
            for l in frontier:
                for m in self.nb[l]:
                    if m not in d:
                        d[m] = d[l] + 1
                        nxt.append(m)
            frontier = nxt
        return d

    # one step of the lattice Maxwell equations in the temporal gauge, and its inverse
    def step(self, E, A, h):
        cc = self.curlT(self.curl(A))
        E2 = {l: E.get(l, 0) + h * cc[l] for l in self.links}
        A2 = {l: A.get(l, 0) - h * E2[l] for l in self.links}
        return E2, A2

    def unstep(self, E2, A2, h):
        A = {l: A2.get(l, 0) + h * E2.get(l, 0) for l in self.links}
        cc = self.curlT(self.curl(A))
        E = {l: E2.get(l, 0) - h * cc[l] for l in self.links}
        return E, A


def string_x(y, x0, x1):
    """unit flux on the links from (x0, y) to (x1, y): divergence +1 at (x0, y) and -1 at (x1, y)."""
    return {('x', x, y): F(1) for x in range(x0, x1)}


# ---- matter: Cl(1,1) --------------------------------------------------------------------------------------
E1, E2 = gen(0), gen(1)
V = scal(F(1, 2), add(E1, E2))
W_ = scal(F(1, 2), sub(E1, E2))
P1, P2 = mul(V, W_, S11), mul(W_, V, S11)


# ---- operators: sums of (matter) x W(f) ---------------------------------------------------------------------
def key(f):
    return tuple(sorted((l, c) for l, c in f.items() if c != 0))


def op(m, f=None):
    return {key(f or {}): m}


def oadd(*xs):
    out = {}
    for x in xs:
        for k, m in x.items():
            out[k] = add(out.get(k, {}), m)
    return {k: m for k, m in out.items() if not GA.is_zero(m)}


def oscal(c, x):
    return {k: scal(c, m) for k, m in x.items() if c != 0}


def omul(x, y):
    out = {}
    for kf, m in x.items():
        for kg, n in y.items():
            f = dict(kf)
            for l, c in kg:
                f[l] = f.get(l, 0) + c
            k = key(f)
            out[k] = add(out.get(k, {}), mul(m, n, S11))
    return {k: m for k, m in out.items() if not GA.is_zero(m)}


def oeq(x, y):
    return oadd(x, oscal(-1, y)) == {}


def comm_field(lam, x):
    """[sum_l lam_l E_l, x]: each term (matter) x W(f) is multiplied by sum_l lam_l f_l."""
    out = {}
    for kf, m in x.items():
        c = sum(lam.get(l, 0) * val for l, val in kf)
        if c != 0:
            out[kf] = scal(c, m)
    return out


def comm_gauss(box, s, rho, g, x):
    """[G_s, x] with G_s = (div E)_s - g rho_s, rho a dictionary site -> matter element."""
    out = {}
    for kf, m in x.items():
        term = scal(box.div(dict(kf)).get(s, 0), m)
        if s in rho:
            term = sub(term, scal(g, sub(mul(rho[s], m, S11), mul(m, rho[s], S11))))
        if not GA.is_zero(term):
            out[kf] = term
    return out


def recombiner(f, p, q):
    """U = p + q (v W(f) - w W(-f)) and its inverse; f = {} is the bare recombiner p + q e2."""
    neg = {l: -c for l, c in f.items()}
    X = oadd(op(V, f), oscal(-1, op(W_, neg)))
    return oadd(op(sc(p)), oscal(q, X)), oadd(op(sc(p)), oscal(-q, X)), X


def detection(f, p, q):
    U, Uinv, X = recombiner(f, p, q)
    return omul(omul(Uinv, op(P1)), U), U, Uinv, X


def kin():
    box = Box(*KBOX)
    chi = string_x(KA[1], KA[0], KB[0])
    return box, chi, box.longitudinal(chi), {KA: P1, KB: P2}


# ---------------------------------------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------------------------------------
def check_bare_recombiner_breaks_the_constraint_and_the_string_dressed_one_keeps_it():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    box, chi, kap, rho = kin()
    g, (p, q) = COUPLING, PQ
    ok = True
    ok = ok and box.div(chi) == {KA: 1, KB: -1} and len(box.links) == 84 and len(chi) == 2
    Ub, Ubinv, _ = recombiner({}, p, q)
    Ud, Udinv, X = recombiner(scal(g, chi), p, q)
    one = op(sc(1))
    ok = ok and oeq(omul(Ub, Ubinv), one) and oeq(omul(Ud, Udinv), one) and oeq(omul(X, X), oscal(-1, one))
    # bare: [G_s, U] = -g q [rho_s, e2], nonzero at the two sites and nowhere else
    bad = [s for s in box.sites if comm_gauss(box, s, rho, g, Ub) != {}]
    ok = ok and sorted(bad) == [KA, KB]
    ok = ok and oeq(comm_gauss(box, KA, rho, g, Ub), op(scal(-g * q, E1)))
    # dressed: commutes with the constraint at all 49 sites, and so does the detection built from it
    Od, _, _, _ = detection(scal(g, chi), p, q)
    ok = ok and len(box.sites) == 49
    ok = ok and all(comm_gauss(box, s, rho, g, Ud) == {} for s in box.sites)
    ok = ok and all(comm_gauss(box, s, rho, g, Od) == {} for s in box.sites)
    ok = ok and oeq(omul(Od, Od), Od)
    GA.check("the bare recombiner p + q e2 fails to commute with the constraint at the two sites of the quantum; the "
             "string-dressed recombiner and its detection commute with it at all 49 sites of the box", ok)
    return ok


def check_string_dressed_detection_commutes_with_the_field_off_the_string():
    premise("field-theory.no-canonical-commutation-relations-tower")
    box, chi, kap, rho = kin()
    g, (p, q) = COUPLING, PQ
    Od, U, Uinv, X = detection(scal(g, chi), p, q)
    ok = True
    # O = p^2 P1 + q^2 P2 + p q (v W + w W^-1)
    neg = {l: -g * c for l, c in chi.items()}
    ok = ok and oeq(Od, oadd(op(scal(p * p, P1)), op(scal(q * q, P2)),
                             oscal(p * q, oadd(op(V, scal(g, chi)), op(W_, neg)))))
    off = [l for l in box.links if l not in chi]
    ok = ok and len(off) == 82
    ok = ok and all(comm_field({l: 1}, Od) == {} for l in off)
    # on the string: [E_l, O] = g p q (v W - w W^-1)
    ok = ok and all(oeq(comm_field({l: 1}, Od), oscal(g * p * q, X)) for l in chi)
    ok = ok and oscal(g * p * q, X) != {}
    GA.check("with the field's own variables the string-dressed detection commutes with E on all 82 links off the "
             "string, and on the two links of the string [E, O] = g p q (v W - w W^-1)", ok)
    return ok


def check_constrained_part_alone_fails_and_the_transverse_part_cancels_it():
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    premise("field-theory.operator-newtonian-coupling")
    box, chi, kap, rho = kin()
    g, (p, q) = COUPLING, PQ
    Od, U, Uinv, X = detection(scal(g, chi), p, q)
    ok = True
    ok = ok and box.div(kap) == box.div(chi)
    trans = {l: chi.get(l, 0) - kap[l] for l in box.links}
    ok = ok and box.div(trans) == {} and all(box.curl(kap)[pl] == 0 for pl in box.plaq)
    off = [l for l in box.links if l not in chi]
    fail = [l for l in off if kap[l] != 0]
    ok = ok and len(fail) == 76
    ok = ok and kap[L_ON] == F(963, 2494) and kap[L_FAR] == F(-54, 1247) and kap[L_CORNER] == F(-41, 2494)
    ok = ok and kap[L_AXIS] == 0                       # the bisector of the two sites, by symmetry
    # the gradient part of E: E_L(l) = sum_s K(l, s) (div E)_s; its commutator with (matter) x W(f) is the
    # gradient part of f at l. Assemble it as a combination of the E's: lam = column of the projector.
    for l in [L_FAR, L_CORNER, L_AXIS, L_ON]:
        lam = box.longitudinal({l: F(1)})          # the projector is symmetric: row l = column l
        cL = comm_field(lam, Od)
        ok = ok and oeq(cL, oscal(g * p * q * kap[l], X))
        cT = oadd(comm_field({l: 1}, Od), oscal(-1, cL))
        ok = ok and oeq(cT, oscal(g * p * q * (chi.get(l, 0) - kap[l]), X))
        ok = ok and (l in chi or oeq(oadd(cL, cT), {}))
    # the field with no variable of its own: E_l = g (K(l,a) P1 + K(l,b) P2) + number, with K(l,a) - K(l,b) = kap_l;
    # its commutator with the bare detection (every matter element is then an observable) is g kap_l p q e2
    Ob, _, _, _ = detection({}, p, q)
    slaved_fail = 0
    for l in off:
        ES = op(scal(g * kap[l], P1))
        c = oadd(omul(ES, Ob), oscal(-1, omul(Ob, ES)))
        ok = ok and oeq(c, op(scal(g * kap[l] * p * q, E2)))
        slaved_fail += 0 if c == {} else 1
    ok = ok and slaved_fail == 76
    # the same for every matter element: [g kap_l P1, m] = g kap_l [P1, m]; it vanishes on all links exactly when
    # m commutes with the charge (m = P2, m = 1 + 3 P1), and fails on the 76 links otherwise (m = e1, m = 2 v + e2)
    for m_el, commutes_with_charge in ((P2, True), (add(sc(1), scal(3, P1)), True), (E1, False),
                                       (add(scal(2, V), E2), False)):
        cP = sub(mul(P1, m_el, S11), mul(m_el, P1, S11))
        ok = ok and GA.is_zero(cP) == commutes_with_charge
        nfail = 0
        for l in off:
            ES = scal(g * kap[l], P1)
            c = sub(mul(ES, m_el, S11), mul(m_el, ES, S11))
            ok = ok and GA.eq(c, scal(g * kap[l], cP))
            nfail += 0 if GA.is_zero(c) else 1
        ok = ok and nfail == (0 if commutes_with_charge else 76)
    # the detection dressed by the constrained field: commutes with the constraint, fails on the same links
    Ok, Uk, _, Xk = detection(scal(g, kap), p, q)
    ok = ok and all(comm_gauss(box, s, rho, g, Ok) == {} for s in box.sites)
    ok = ok and sum(1 for l in off if comm_field({l: 1}, Ok) != {}) == 76
    ok = ok and oeq(comm_field({L_CORNER: 1}, Ok), oscal(g * p * q * kap[L_CORNER], Xk))
    GA.check("the constrained part of E fails to commute with the string-dressed detection on 76 of the 82 links off "
             "the string, the transverse part by the opposite amount; the Coulomb slaved field fails on the same 76 "
             "with the bare detection and with every sampled matter element that does not commute with the charge, "
             "and so does the full field with the detection dressed by the constrained field", ok)
    return ok


def check_string_shaped_slaved_field_keeps_the_constraint_and_is_not_static():
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    box, chi, kap, rho = kin()
    g, (p, q) = COUPLING, PQ
    Ob, _, _, _ = detection({}, p, q)
    ok = True
    # E_l = g chi_l P1 + number: its operator part has the divergence of the charge's operator part
    ok = ok and box.div(chi) == {KA: 1, KB: -1} and box.div(chi) == box.div(kap)
    off = [l for l in box.links if l not in chi]
    nz = 0
    for l in box.links:
        ES = op(scal(g * chi.get(l, 0), P1))
        c = oadd(omul(ES, Ob), oscal(-1, omul(Ob, ES)))
        ok = ok and oeq(c, op(scal(g * chi.get(l, 0) * p * q, E2)))
        ok = ok and (l in chi or c == {})
        nz += 0 if c == {} else 1
    ok = ok and nz == 2 and len(off) == 82
    # the Coulomb field is a static solution of the field equation, the string is not
    h = STEP
    Ek, Ak = dict(kap), {}
    Es, As = dict(chi), {}
    for n in range(2):
        Ek, Ak = box.step(Ek, Ak, h)
        Es, As = box.step(Es, As, h)
    ok = ok and all(Ek[l] == kap[l] for l in box.links)
    changed = [l for l in box.links if Es[l] != chi.get(l, 0)]
    ok = ok and len(changed) == 10 and Es[L_ON] == F(1, 2)
    # under the field equation the gradient part of the evolved string is kappa at every step
    E, A = dict(chi), {}
    for n in range(max(STATIC_STEPS)):
        E, A = box.step(E, A, h)
        if n + 1 in STATIC_STEPS:
            lon = box.longitudinal(E)
            ok = ok and all(lon[l] == kap[l] for l in box.links)
    GA.check("the string-shaped slaved field g chi P1 has the divergence the constraint asks and commutes with the "
             "bare detection on all 82 links off the string; it is not static (after two steps it has changed on 10 "
             "links) while the Coulomb field is, and the gradient part of the evolved string is kappa at steps 1, 2, 3", ok)
    return ok


def check_in_one_space_dimension_the_constrained_part_is_the_string():
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    ch = Box(*CHAIN)
    chi = string_x(CA[1], CA[0], CB[0])
    kap = ch.longitudinal(chi)
    ok = len(ch.links) == 12 and len(chi) == 4
    ok = ok and all(kap[l] == chi.get(l, 0) for l in ch.links)
    ok = ok and sum(1 for l in ch.links if kap[l] != 0) == 4
    GA.check("on a chain of 13 sites the constrained part of the string between the two sites is the string: it is "
             "nonzero on the 4 links between them and zero on the 8 others", ok)
    return ok


def check_dynamics_string_dressed_detection_commutes_at_spacelike_events_and_the_slaved_field_does_not():
    premise("synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation")
    box = Box(*DBOX)
    h = STEP
    chi = string_x(DA[1], DA[0], DB[0])
    ok = True
    ok = ok and box.div(chi) == {DA: 1, DB: -1} and len(box.links) == 312
    # the split at step 0 moves the quantum from the middle site to a or to b; the two strings differ by chi
    route_a = string_x(DA[1], DA[0], DO[0])
    route_b = {l: -c for l, c in string_x(DO[1], DO[0], DB[0]).items()}
    ok = ok and box.div(route_a) == {DA: 1, DO: -1} and box.div(route_b) == {DB: 1, DO: -1}
    ok = ok and {l: route_a.get(l, 0) - route_b.get(l, 0) for l in chi} == chi
    dist = box.dist_from(list(chi))
    # (a) full field: coefficient of [E_l(n), W(chi) at step ND] is the string evolved from step ND
    S = {ND: dict(chi)}
    E, A = dict(chi), {}
    for n in range(ND, NMAX):
        E, A = box.step(E, A, h)
        S[n + 1] = E
    E, A = dict(chi), {}
    for n in range(ND, 0, -1):
        E, A = box.unstep(E, A, h)
        S[n - 1] = E
    spacelike = [(l, n) for n in range(NMAX + 1) for l in box.links if dist[l] > abs(n - ND)]
    ok = ok and len(spacelike) == 2750
    ok = ok and all(S[n].get(l, 0) == 0 for (l, n) in spacelike)
    ok = ok and any(S[n].get(l, 0) != 0 for n in S for l in box.links if 0 < dist[l] <= abs(n - ND))
    # remark: the slaved field S P1, string-shaped at step ND, obeys the constraint and the field equation and
    # commutes with the detection at step ND at all 2750 events (above); against a detection at step ND_OTHER it
    # fails at 86 of the 2562 events spacelike to that one
    ok = ok and all(box.div(S[n]) == box.div(chi) for n in S)
    other = [(l, n) for n in range(NMAX + 1) for l in box.links if dist[l] > abs(n - ND_OTHER)]
    ok = ok and len(other) == 2562 and sum(1 for (l, n) in other if S[n].get(l, 0) != 0) == 86
    # (b) slaved retarded field of the constrained model: difference of the two classical fields from step 0
    D = {0: dict(chi)}
    E, A = dict(chi), {}
    for n in range(0, NMAX):
        E, A = box.step(E, A, h)
        D[n + 1] = E
    ok = ok and all(box.div(D[n]) == box.div(chi) for n in D)          # the constraint holds at every step
    bad = [(l, n) for (l, n) in spacelike if D[n].get(l, 0) != 0]
    ok = ok and len(bad) == 878
    ok = ok and D[ND][D_EAST] == F(-7, 64) and D[ND][D_DIAG] == F(-15, 256)
    ok = ok and dist[D_EAST] == 3 and dist[D_DIAG] == 3 and (D_EAST, ND) in bad and (D_DIAG, ND) in bad
    ok = ok and not any(n < 4 for (l, n) in bad)
    # every failing event lies in the forward cone of the source event (the string at step 0) and, being
    # spacelike, outside the cone of the detection: the failure is carried by the charge at the source event
    ok = ok and all(dist[l] <= n - 1 and dist[l] > abs(n - ND) for (l, n) in bad)
    # the steps are inverse to one another, and each is a canonical map: checked on the unit data of two links
    for l in CANON_LINKS:
        E1_, A1_ = box.step({l: F(1)}, {}, h)
        E0_, A0_ = box.unstep(E1_, A1_, h)
        ok = ok and {k: c for k, c in E0_.items() if c != 0} == {l: 1} and all(c == 0 for c in A0_.values())
        Ea, Aa = box.step({}, {l: F(1)}, h)                       # response to unit A-data on l
        # bracket of the evolved pair: sum_m (dE'_l/dE_m dA'_l/dA_m - dE'_l/dA_m dA'_l/dE_m) = 1 for the pair on l
        ok = ok and E1_[l] * Aa[l] - Ea[l] * A1_[l] == 1
    GA.check("13 x 13 box, step 1/2, detection at step 5: the string-dressed detection commutes with E at all 2750 "
             "spacelike events; the slaved retarded field of the constrained model fails at 878 of them while "
             "satisfying the constraint at every step", ok)
    return ok
