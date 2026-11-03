#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T05.py: exact-arithmetic verification of the computational identities of

    "Division by Zero at the Gravitational Singularity: The Transport
     Principle Applied to the Black Hole, and the Information Paradox as a
     Category Error"  (Transport Papers T5)

in the style of the series' scripts: a basis-blade Clifford engine over exact
rationals, a fermionic Fock engine for the current algebra, an exact
multi-qubit simulator (rational amplitudes; controlled-Z scrambling uses only
signs) for the finite-mode model, and (new in v1.1) an exact engine for the
field Q(r)[beta] with beta^2 = 2M/r, in which the gauge sector (the connection
bivector, the torsion equations, the radial curvature, and the rescaled limit)
is verified as identities rather than at samples, and (new in v1.5) a formal-
logarithm engine in which von Neumann entropies of rational spectra are exact
vectors over the primes, with inequalities decided by rigorous rational bounds.  Every check is PASS/FAIL;
nonzero exit on any failure; no floating point anywhere.
Shared machinery (the blade engine, exact linear algebra, rational functions,
the exterior model and the check harness) lives in GA.py, deposited alongside.

Coverage (labels refer to the paper's current numbering, v3.1; the [App
SA.1]-[App SA.3] labels name SUBSECTIONS of Appendix A, not result numbers):
  [Prop 2.2]  P^2 = 0 and hbar^{-1} = 1 + beta P exactly (rational beta)
  [Prop 2.3]  the connection bivector: beta' = -beta/2r; beta beta' = -M/r^2
              (the Newtonian anchor); the torsion equations of the PG coframe
              in the (t, r, theta) sector as exact identities in Q(r)[beta];
              the divergence rate |Omega(e_r)| = sqrt(M/2r^3)
  [Prop 2.4]  the radial curvature from the gauge field alone:
              R(dt ^ dr) = (beta beta')' sigma_r = (2M/r^3) sigma_r, with the
              commutator term vanishing identically (abelian plane);
              det hbar = 1 at every radius, the determinant computed from the
              map a -> a - beta (a.e_t) e_r itself, horizon included
  [Prop 2.5]  null directions at lambda = -beta +- 1, computed through
              hbar^{-1}; folding coefficients
  [Prop 2.6]  the degeneration, exactly: beta^{-1} hbar = beta^{-1} - P;
              rank P = 1, ker P = e_t-perp, im P = R e_r; the rescaled metric
              identity beta^{-2} g(a,b) + (a.e_t)(b.e_t) -> 0; the limit form
              ghat has signature (0,1,3), radical containing e_r, and the
              limit direction e_r is ghat-null while g(e_r,e_r) = -1
  [Prop 2.7]  the curvature invariant: R_abcd R^abcd = 48 M^2 / r^6 as an
              exact rational-function identity (non-removability)
  [Prop 3.1]  mod-8 arithmetic; Cl(1,3) centre = span{1} (exhaustive)
  [Def 5.1]   the fibrewise conformal lift X_p(x) = n0 + x + (1/2)Q_p(x) ninf;
              with n0.ninf = -1 the lift is null, X^2 = 0, blade-exactly in
              Cl(2,4), and with -1/2 it is not; parts L1 to L10 below carry
              the vector slot as actual Cl(2,4) multivector data
  [Prop 5.2]  the point-level transport, instantiated on the Schwarzschild
              fibre: incidence and its preservation under iota; the involution;
              descent recovering x/Q(x) on the invertible locus; the radial
              null direction landing on the ideal point [x + (1/2) ninf] with
              the read-out undefined; the radical generator k of T04 Thm 8.7
              with dual norm Q*(k) = -r exactly (static chart, as rational
              functions; PG frame, k^T G k against T04's Gram built over
              Q(r), with a multi-entry control contraction and det G = -r,
              and the dual through the Gram: Gk = (-r, 0, 0, 0), k-sharp
              radial with vanishing PG-time component), Q*(k) rebuilt
              pointwise from its unreduced terms off the horizon, the horizon
              value certified by the L12 identity (the failure locus is E,
              not a wall); the static norm 1/f of dt_s probed for its
              horizon pole
  [Lem 4.1]   the hyperbolic atom: CAR with rational normalisation;
              pseudo-inverse identities; v has no inverse (exact rank)
  [Prop 5.5]  descent projectors and the pinching in 2x2 matrices
  [Thm 5.7]   the descent is the parity average E(x) = (x + sigma x sigma)/2;
              idempotence; E(a x b) = a E(x) b for even a, b; range the even
              span, kernel the odd span
  [Thm 6.1]   the shape operator: S = -1/2 (B + 3 sigma_r B sigma_r) = 1 - 3 Pi
              on all six frame planes; S^2 + S = 2; spectrum (-2,-2,1,1,1,1);
              trace 0; eigenvalue ratio -2 : 1 matching the appendix values
              2M/r^3 : -M/r^3; the SIGN of R = -(M/r^3) S fixed on the radial
              and mixed planes; h-bar invariance of the radial plane
  [Thm 6.3]   sigma = e0 e1; sigma^2 = 1; rational rotor flow (5/3, 4/3)
              scales v by exactly 1/9 and v* by 9; spectral projectors = descent
  [Cor 6.4]   the weld: the atom's sigma = e0 e1 is, among the six frame
              planes, the unique one with S-eigenvalue -2 and square +1
  [Lem 7.1]   finite-dimensional KMS identity on all 16 matrix-unit pairs, at
              e^{-omega/T} = 9/16 (physical) and 16/9 (population-inverted)
  [Thm 7.3]   TFD partial trace = Fermi-Dirac with tan^2 theta = 9/16 and 16/9; the
              two examples bounding the hypotheses: c|01> + s|10> (violates
              (ii), descends thermally) and c|+0> + s|-1> (violates (ii),
              descends with nonzero coherence)
  [Thm 7.6]   the descended form is state independent: E(rho) diagonal for any
              rho, equal to diag(1, x)/(1+x) at the x the theorem names
  [Thm 7.10]  univalence: omega(v_k) = 0 and every single-mode marginal diagonal
              for an even state, with a parity-mixed control that fails
  [Thm 7.13]  KMS uniqueness at a factor; the tracial state fails the identity
  [Cor 7.15]  universality under (G): equal inverse temperatures as the exact
              condition x_2 = x_1^{w2/w1}, with a witness pair for which it fails
  [Thm 7.16]  rate rigidity: flow-preserving automorphisms fix the Gibbs state,
              the exchange sends beta to -beta and does not commute with K;
              reparametrisation K -> 2K halves beta for the same state
  [Prop 7.18] the Euclidean section: sqrt(f) d sqrt(f)/dr = f'/2 as rational
              functions, f(2M) = 0, f'(2M) = 2 kappa = 1/2M exactly
  [Thm 7.20]  the gluing condition of (R): e^{p omega} n = 1 - n has the unique
              solution n = 1/(e^{p omega} + 1); the boundary cases n = 0 and
              n = 1/2 fail it
  [Prop 7.21] the Euclidean rotor: the complexified rotor cos + i sigma sin is
              unitary, obeys the composition law, R_{2 pi i} = -1 on the
              module and conjugation by it is trivial; I sigma_r = e2 e3
              blade-exactly, its rotor fixes e0, e1 and sigma_r and rotates
              e2 into e3; the real bivectors of span{sigma_r, I sigma_r} with
              square -1 are +- I sigma_r only
  [Prop 7.23] the two KMS functionals: the Gibbs state satisfies the ungraded
              identity and fails the graded one; the parity-twisted functional
              satisfies the graded identity, fails the ungraded one, and has
              negative occupancy
  [Prop 7.25] the connection rate's pole at r = 0 (no finite period on the
              singular side) against the finite horizon kappa; f(2M) = 0
  [Thm 7.27]  the canonical purification and its modular data
  [Thm 7.28]  exact equilibrium over-determines: the product Gibbs state is a
              fixed point of E_N, against a correlated control
  [Prop 7.31] number-diagonal dynamics: controlled-Z preserves populations and
              marginals; a hopping rotation does not
  [Cor 7.32]  the chain's state class: an entangled even state with Gibbs
              marginals is in the class, is not a product, survives a
              controlled-Z, and the product member satisfies (G)
  [Thm 8.2]   current algebra on a finite fermion array: [a_1, a_-1] = id and
              [a_1, a_2] = 0 on bulk states; Planck factor as an exact
              geometric identity with explicit rational tail bound; premise
              (Q) isolated as an operator computation (traces of
              number-operator products; the connected correlator computed
              outright): the Planck summand factorises exactly on a
              quasi-free product state at [Thm 7.20]'s gluing occupancy
              n = 9/25 and shifts by exactly the connected correlator on a
              correlated even state with identical marginals
  [Lem 10.4]  the causal-epoch integral: the geodesic integrand, the
              substitution r = 2M u^2, the partial-fraction identity and the
              antiderivative as exact rational-function identities; the closed
              form bracketed by exact Riemann sums at a rational endpoint, with
              the former closed form 2M(ln(1/eps) - 1 + eps) shown to lie
              outside the bracket
  [Prop 10.6] the slice arithmetic as rational-function identities along the
              whole (C1) locus (2M = r_c^3, r_c an indeterminate), with a
              mass-independent-cutoff control failing the linear-in-M form;
              (dN/dt)^2 = (nu/T_H)^2 (1 - r_c/2M) with pi cancelled
  [Prop 10.7] capacity calibration with ln 2 carried as a formal
              indeterminate: C = N ln 2 = 4 pi M^2 iff nu Delta t =
              M/(2 ln 2), the old calibration nu Delta t = M/2 failing by
              exactly ln 2
  [Fact 11.1]  the envelope on the thermal model: S_R <= min(S_th, C) at
              every stage, the rising branch exact, the crossing exhibited
  [Prop 11.4] no attic: the two sectors exhaust the qubits at every stage;
              trace moments of rho_R against rho_L
  [Thm 11.5]  ALSO: the window marginal is the product (G) member at every
              stage (internal total correlation exactly zero), and the
              saturation boundary h = ln 2 is attained exactly at c = s
              (omega = 0), every physical pair lying strictly below
  [Rem 9.5]   the deficit is blind to the message: identical final
              configuration distributions and deficit S_th in the scrambled
              and unscrambled histories, amplitude signs alone differing
  [Prop 9.6]  the composite argument: mode-wise parity averages idempotent,
              commuting, composing in either order to the pinching E_N; and
              its antecedent doing real work: Ad(Gamma) fixes the model's
              even radiation state outright (zero deficit under the total
              parity alone), the parity average fixes the scrambled pair
              marginal coherence included while E_N kills it, and XXZ
              commutes with the total parity yet is annihilated by E_N
  [Lem 7.2]   Schmidt forcing as an exact eigenspace computation over Q: the
              +-1 eigenvectors of G are product vectors failing separation
              or cyclicity by exact rank; a 0-eigenvector with both
              coefficients nonzero passes both
  [Prop 6.2]  the plane and the rate directly: kappa = f'(2M)/2 = 1/4M from
              the derivative, 2 pi / kappa = 8 pi M with pi cancelled, and
              sigma_r^2 = +1 against (I sigma_r)^2 = -1 blade-exactly
  [Thm 11.5]  (1) rho_L is the thermal product of its members and S_R = S_L =
              sum_{k in W} h_k at every stage, from exact spectra, as formal
              logarithms; (4) S_R = C - sum_{k in W}(ln 2 - h_k) and S_R <= C;
              the maximally entangled idealisation simulated on exact density
              matrices along a decreasing capacity schedule, S_R = min(S_th, C)
              at every event, window exactly maximally mixed, ending at zero
  [Cor 11.6]  (L_E) is necessary: a non-diagonal window rotation before the
              first eviction gives S_R > S_th, exact rationals + rigorous bounds
  [Cor 11.7]  at every event, from exact spectra: S(A) = h_k + sum_evicted h_j
              and I(A:R_<) = 2 sum_evicted h_j
  [Lem 12.1]  parity protection: every single-qubit marginal exactly thermal
              at every stage of the full model, arbitrary CZ scrambling
  [Prop 12.3] purity; coherence damping gamma = c2^2 - s2^2; correlator
              decoding (<XX>, <XXZ>) with pinned single-qubit states;
              Schmidt purity equality at every stage; final S_2(R) = 0
  [Prop 12.4] the model's entropy sequence: rho_L diagonal with the product
              distribution at every stage; S_R = S_L = sum_{k in W} H(c_k^2)
              as an identity of formal logarithms; S_R = S_th in Phase I;
              S_R < C strictly in Phase II (decided by exact rational bounds
              on the logarithms of the primes involved); S_R = 0 at the end
  [Prop 12.5] the descent applied to the radiation: tr(E rho_R)^2 =
              prod_k (c_k^4 + s_k^4) = 817544276833/6972900390625 while
              tr rho_R^2 = 1; S(E rho_R) = sum_k H(c_k^2) = S_th exactly, as
              formal logarithms; the descended entropy is monotone (no falling
              branch); the decoding correlators are annihilated exactly;
              intra-pair classical records survive, every inter-pair
              correlation is destroyed; single-qubit marginals identical in
              the two ledgers
  [Def 9.1]   the multi-mode descent E_N: idempotent, trace-preserving,
              Hilbert-Schmidt self-adjoint, dephasing in the joint number
              basis (verified on a generic rational matrix)
  [Prop 9.2]  pinching vs partial trace: coincidence on a single thermofield
              mode; failure on two modes, priced by the coherence c1 s1 gamma
  [Thm 9.3]   the deficit theorem's key lemma: tr(rho f(E rho)) =
              tr(E(rho) f(E rho)) in moment form, exact
  [Cor 9.4]   marginals pass through E_N unchanged when diagonal; the deficit
              is carried by correlations alone
  [App SA.1-SA.3] the PG metric, the static form, the Cartan block with a
              perturbed-connection negative control, the three curvature
              eigenvalues and kappa = 1/4M as exact rational-function
              identities (SA.n = subsection A.n of the appendix)
  [App C.1]   the metric-level sheaf, on the two-mode Jordan-Wigner ledger:
              CAR exact; the strings cancel in sigma_k = v*v - vv*, single-
              site both (the locality in the proof of Prop 9.6); Ad(sigma_x)
              fixes v_y while Ad(sigma_y) negates it (Thm C.4); the composite
              of the two parity averages, either order, is the joint-
              diagonal pinching; both fibres and both assemblies computed by
              exact kernels and ranks: big fibres dim 8 containing small
              fibres dim 2, meet(big) = join(small) = range(E_N), dim 4
              (Thm C.3); words in the generators span the full 16-dimensional
              ledger and the net assembly is isotone (Thm C.4)
  [App C.2]   the hopping exclusion: commuting with every point multiplier
              forces diagonality, the tensoriality lemma's finite model (all
              nine matrix units, Lem C.6); dGamma of a bundle map built from
              psi^dagger a psi equals a_x N_x + a_y N_y and conserves both
              occupations, while a hop carries (0,1) to (1,0) (Prop C.7);
              the controlled-Z generator conserves both occupations; the
              pairing generator v_x* v_y* + v_y v_x commutes with Gamma, is
              off-diagonal and fails to commute with N_x and N_x + N_y, the
              witness fixing Thm C.8's scope; Cor 11.6's rotation is a
              pairing rotation, Delta N = 2, no hop component (Rem C.9).
              Facts B.3 and B.4 are imports, verified in verify_T04.py; not
              re-verified here.
"""

from fractions import Fraction
from itertools import combinations
import sys

import GA as g


STA = (1, -1, -1, -1)   # Cl(1,3): e_t = gen(0), e_r = gen(1)
CL11 = (1, -1)          # the hyperbolic atom

MASS = Fraction(3, 2)   # the rational mass used throughout the gauge sector


# ---------------------------------------------------------------------------
# The field Q(r)[beta], beta^2 = 2M/r: elements even + odd*beta with even, odd
# rational functions of r.  Derivative uses beta' = -beta/(2r).
# ---------------------------------------------------------------------------

class BR(object):
    __slots__ = ("ev", "od")

    def __init__(self, ev=None, od=None):
        self.ev = ev if ev is not None else g.RF0
        self.od = od if od is not None else g.RF0

    @staticmethod
    def const(c):
        return BR(g.RF.const(c), g.RF0)

    @staticmethod
    def rf(f):
        return BR(f, g.RF0)

    @staticmethod
    def beta():
        return BR(g.RF0, g.RF1)

    def __add__(self, o):
        return BR(self.ev + o.ev, self.od + o.od)

    def __sub__(self, o):
        return BR(self.ev - o.ev, self.od - o.od)

    def __neg__(self):
        return BR(-self.ev, -self.od)

    def __mul__(self, o):
        b2 = g.RF.const(2 * MASS) / g.RF.var()          # beta^2 = 2M/r
        return BR(self.ev * o.ev + self.od * o.od * b2,
                  self.ev * o.od + self.od * o.ev)

    def deriv(self):
        r = g.RF.var()
        half = g.RF.const(Fraction(1, 2))
        return BR(self.ev.deriv(), self.od.deriv() - self.od * half / r)

    def is_zero(self):
        return self.ev.is_zero() and self.od.is_zero()

    def eqbr(self, o):
        return (self - o).is_zero()


def br_form_zero():
    return {}


def form1(**kw):
    """One-form over the basis dt (0), dr (1), dtheta (2), coefficients BR."""
    out = {}
    for k, v in kw.items():
        out[{"dt": 0, "dr": 1, "dth": 2}[k]] = v
    return out


def form1_scal(c, w):
    return {i: c * v for i, v in w.items()}


def form1_add(a, b):
    out = dict(a)
    for i, v in b.items():
        out[i] = out.get(i, BR()) + v
    return out


def wedge(a, b):
    """Wedge of two one-forms: two-form over pairs (i, j), i < j."""
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            if i == j:
                continue
            key, sign = ((i, j), 1) if i < j else ((j, i), -1)
            term = ai * bj if sign > 0 else -(ai * bj)
            out[key] = out.get(key, BR()) + term
    return out


def dform(a):
    """Exterior derivative of a one-form with r-dependent coefficients."""
    out = {}
    for i, ai in a.items():
        da = ai.deriv()           # coefficient of dr ^ (basis i)
        if i == 0:                # dr ^ dt = -(dt ^ dr)
            out[(0, 1)] = out.get((0, 1), BR()) - da
        elif i == 2:              # dr ^ dtheta = +(dr ^ dtheta) key (1,2)
            out[(1, 2)] = out.get((1, 2), BR()) + da
        # i == 1: d(f dr) = f' dr ^ dr = 0
    return out


def form2_sub(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, BR()) - v
    return out


def form2_zero(a):
    return all(v.is_zero() for v in a.values())


# ---------------------------------------------------------------------------
# [Prop 2.2] / [Prop 2.5]: the unipotent ray and the folding cones
# ---------------------------------------------------------------------------

def step1_checks():
    et, er = g.gen(0), g.gen(1)
    beta = Fraction(3, 7)

    def P(a):
        return g.scal(g.dotv(a, et, STA), er)

    def hbar(a, b=beta):
        return g.sub(a, g.scal(b, P(a)))

    def hbar_inv(a, b=beta):
        return g.add(a, g.scal(b, P(a)))

    basis = [g.gen(i) for i in range(4)]
    ok = all(g.is_zero(P(P(a))) for a in basis)
    g.check("[Prop 2.2] P^2 = 0 on every basis vector (exact, any radius)", ok)
    ok = all(g.eq(hbar_inv(hbar(a)), a) and g.eq(hbar(hbar_inv(a)), a) for a in basis)
    g.check("[Prop 2.2] hbar^{-1} = 1 + beta P exactly (beta = 3/7, all basis vectors)", ok)
    # horizon: beta = 1 still invertible
    ok = all(g.eq(g.add(hbar(a, Fraction(1)), g.scal(Fraction(1), P(hbar(a, Fraction(1))))), a) for a in basis)
    g.check("[Prop 2.2] the horizon (beta = 1) is algebraically unremarkable: still invertible", ok)
    # null directions of the metric g(a,a) = hbar^{-1}(a)^2 (eq. 2.4): lambda = -beta +- 1
    ok = True
    for b in (Fraction(3, 7), Fraction(5, 2), Fraction(1)):
        for sgn in (1, -1):
            lam = -b + sgn
            a = g.add(et, g.scal(lam, er))
            img = hbar_inv(a, b)
            ok = ok and g.is_zero(g.mul(img, img, STA))
            # the candidate lambda = beta + sgn is NOT g-null (away from the coincidence beta = 1, sgn = -1)
            if b != 1:
                a_wrong = g.add(et, g.scal(b + sgn, er))
                img_w = hbar_inv(a_wrong, b)
                ok = ok and not g.is_zero(g.mul(img_w, img_w, STA))
        lam = -b + Fraction(1, 3)  # not -beta +- 1: must NOT be null
        a = g.add(et, g.scal(lam, er))
        img = hbar_inv(a, b)
        ok = ok and not g.is_zero(g.mul(img, img, STA))
        # structurally: the g-null vectors are the hbar-images of the flat null vectors e_t +- e_r
        for sgn in (1, -1):
            flat_null = g.add(et, g.scal(sgn, er))
            gn = hbar(flat_null, b)
            back = hbar_inv(gn, b)
            ok = ok and g.is_zero(g.mul(back, back, STA)) \
                and g.eq(gn, g.add(et, g.scal(sgn - b, er)))
    g.check("[Prop 2.5] e_t + lambda e_r is g-null (hbar^{-1}-image null) exactly when lambda = -beta +- 1; "
            "lambda = beta +- 1 is not; the g-null vectors are the hbar-images of e_t +- e_r", ok)
    # at the horizon the pair is {0, -2}: the hovering ray and an ingoing one
    ok = True
    for lam in (Fraction(0), Fraction(-2)):
        img = hbar_inv(g.add(et, g.scal(lam, er)), Fraction(1))
        ok = ok and g.is_zero(g.mul(img, img, STA))
    img = hbar_inv(g.add(et, g.scal(Fraction(2), er)), Fraction(1))
    ok = ok and not g.is_zero(g.mul(img, img, STA))
    g.check("[Prop 2.5] at the horizon (beta = 1) the null pair is lambda = 0 (hovering) and lambda = -2 "
            "(ingoing); lambda = +2 is not null", ok)
    ok = True
    prev = None
    for b in (Fraction(10), Fraction(100), Fraction(1000)):
        coeff = 1 / (-b + 1)
        if prev is not None:
            ok = ok and abs(coeff) < abs(prev)
        prev = coeff
        ok = ok and coeff < 0 and 1 / (-b - 1) < 0
    ok = ok and abs(prev) < Fraction(1, 900)
    g.check("[Prop 2.5] folding: the normalised e_t coefficients 1/(-beta +- 1) are negative (both branches tip "
            "inward) and shrink monotonically to 0", ok)


# ---------------------------------------------------------------------------
# [Prop 2.3] / [Prop 2.4]: the connection bivector, torsion, radial curvature,
# unimodularity.  All identities in Q(r)[beta], beta^2 = 2M/r.
# ---------------------------------------------------------------------------

def exact_det(M):
    """Determinant of a square matrix of Fractions by Gaussian elimination."""
    A = [row[:] for row in M]
    n = len(A)
    det = Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        for r in range(c + 1, n):
            fct = A[r][c] / A[c][c]
            if fct:
                A[r] = [x - fct * y for x, y in zip(A[r], A[c])]
    return det


def gauge_checks():
    r = g.RF.var()
    b = BR.beta()
    bp = b.deriv()                                     # beta'
    # beta' = -beta/(2r)
    want = BR(g.RF0, -(g.RF.const(Fraction(1, 2)) / r))
    g.check("[Prop 2.3] beta' = -beta/(2r) exactly in Q(r)[beta]", bp.eqbr(want))
    # beta beta' = -M/r^2: the Newtonian anchor
    bbp = b * bp
    anchor = BR(-(g.RF.const(MASS) / (r * r)), g.RF0)
    g.check("[Prop 2.3] beta beta' = -M/r^2 exactly: Omega(dt) carries the Newtonian field", bbp.eqbr(anchor))
    # the divergence rate: Omega(e_r) coefficient -beta' has square M/(2 r^3)
    div2 = bp * bp
    rate = BR(g.RF.const(MASS) / (g.RF.const(2) * r * r * r), g.RF0)
    g.check("[Prop 2.3] |Omega(e_r)|^2 = (beta')^2 = M/(2 r^3): the divergence lives in the connection",
            div2.eqbr(rate))

    # PG coframe: th0 = dt, th1 = beta dt + dr, th2 = r dtheta
    th0 = form1(dt=BR.const(1))
    th1 = form1(dt=b, dr=BR.const(1))
    th2 = form1(dth=BR.rf(r))
    # connection: w10 = -beta' th1 ; w20 = -(beta/r) th2 ; w21 = (1/r) th2
    w10 = form1_scal(-bp, th1)
    w20 = form1_scal(-(b * BR.rf(g.RF1 / r)), th2)
    w21 = form1_scal(BR.rf(g.RF1 / r), th2)
    # torsion 0: d th0 = -w01 ^ th1 with w01 = w10
    lhs = dform(th0)
    rhs = form2_sub(br_form_zero(), wedge(w10, th1))
    g.check("[Prop 2.3] torsion, theta^0 leg: d theta^0 = -omega^0_1 ^ theta^1 exactly", form2_zero(form2_sub(lhs, rhs)))
    # torsion 1: d th1 = -w10 ^ th0
    lhs = dform(th1)
    rhs = form2_sub(br_form_zero(), wedge(w10, th0))
    g.check("[Prop 2.3] torsion, theta^1 leg: d theta^1 = -omega^1_0 ^ theta^0 exactly", form2_zero(form2_sub(lhs, rhs)))
    # torsion 2: d th2 = -w20 ^ th0 - w21 ^ th1
    lhs = dform(th2)
    rhs = form2_sub(form2_sub(br_form_zero(), wedge(w20, th0)), wedge(w21, th1))
    g.check("[Prop 2.3] torsion, theta^2 leg: d theta^2 = -omega^2_0 ^ theta^0 - omega^2_1 ^ theta^1 exactly",
            form2_zero(form2_sub(lhs, rhs)))

    # [Prop 2.4] radial curvature from the gauge field alone:
    # R^1_0 = d w10 (the angular contributions wedge to zero), and the
    # coefficient of theta^0 ^ theta^1 = dt ^ dr is (beta beta')' = 2M/r^3.
    Rform = dform(w10)
    coeff = Rform.get((0, 1), BR())
    twoM_r3 = BR(g.RF.const(2 * MASS) / (r * r * r), g.RF0)
    g.check("[Prop 2.4] R(radial plane) = (beta beta')' theta^0 ^ theta^1 = (2M/r^3) sigma_r, exactly",
            coeff.eqbr(twoM_r3) and all(k == (0, 1) or v.is_zero() for k, v in Rform.items()))
    # the angular wedge contribution w12 ^ w20 vanishes identically (both along th2)
    w12 = form1_scal(-BR.const(1), w21)   # omega^1_2 = -omega^2_1
    g.check("[Prop 2.4] the commutator/wedge term omega^1_2 ^ omega^2_0 = 0 identically: the radial "
            "sector is abelian", form2_zero(wedge(w12, w20)))
    # (beta beta')' = 2M/r^3 also directly
    g.check("[Prop 2.4] (beta beta')' = 2M/r^3 as an exact identity", bbp.deriv().eqbr(twoM_r3))

    # unimodularity: det hbar = 1 at rational beta including the horizon, with
    # the matrix of hbar(a) = a - beta (a.e_t) e_r computed from the map itself
    # (columns = images of the frame vectors) and the determinant by exact
    # Gaussian elimination.
    et, er = g.gen(0), g.gen(1)
    frame = [g.gen(i) for i in range(4)]
    ok = True
    for beta in (Fraction(3, 7), Fraction(1), Fraction(5, 2), Fraction(100)):
        hb = lambda a, b=beta: g.sub(a, g.scal(b * g.dotv(a, et, STA), er))
        cols = [hb(v) for v in frame]
        Mh = [[cols[j].get((i,), Fraction(0)) for j in range(4)] for i in range(4)]
        d = exact_det(Mh)
        # the inverse claimed in Prop 2.2, a -> a + beta (a.e_t) e_r, composes to the identity
        hinv = lambda a, b=beta: g.add(a, g.scal(b * g.dotv(a, et, STA), er))
        comp_ok = all(g.eq(hinv(hb(v)), v) for v in frame)
        # the entry beta really is in the matrix (control against a hollow check)
        ok = ok and d == 1 and comp_ok and Mh[1][0] == -beta
    g.check("[Prop 2.4] det hbar = 1 at every radius, horizon included, the determinant computed from "
            "the map a -> a - beta (a.e_t) e_r itself; hbar^{-1} = 1 + beta P composes to the identity", ok)


# ---------------------------------------------------------------------------
# [Prop 2.6]: the degeneration, exactly (rescaled map and metric limits)
# [Prop 2.7]: the curvature invariant
# ---------------------------------------------------------------------------

def limit_checks():
    et, er = g.gen(0), g.gen(1)
    basis = [g.gen(i) for i in range(4)]

    def P_mat():
        # matrix of P(a) = (a.e_t) e_r on the basis (columns = images)
        cols = []
        for a in basis:
            img = g.scal(g.dotv(a, et, STA), er)
            cols.append([img.get((i,), Fraction(0)) for i in range(4)])
        return [[cols[j][i] for j in range(4)] for i in range(4)]

    Pm = P_mat()
    g.check("[Prop 2.6] rank P = 1: the rescaled limit -P of beta^{-1} hbar is rank one",
            g.mat_rank(Pm) == 1)
    # kernel = e_t-perp = span(e_r, e_th, e_ph); image = R e_r
    kernel_ok = all(all(sum(Pm[i][j] * v[j] for j in range(4)) == 0 for i in range(4))
                    for v in ([0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]))
    image_ok = [Pm[i][0] for i in range(4)] == [Fraction(0), Fraction(1), Fraction(0), Fraction(0)]
    g.check("[Prop 2.6] ker P = span(e_r, e_th, e_ph) = e_t-perp and im P = R e_r", kernel_ok and image_ok)
    # beta^{-1} hbar = beta^{-1} id - P exactly (algebraic identity at rational beta)
    ok = True
    for beta in (Fraction(10), Fraction(100)):
        for a in basis:
            lhs = g.scal(1 / beta, g.sub(a, g.scal(beta, g.scal(g.dotv(a, et, STA), er))))
            rhs = g.sub(g.scal(1 / beta, a), g.scal(g.dotv(a, et, STA), er))
            ok = ok and g.eq(lhs, rhs)
    g.check("[Prop 2.6] beta^{-1} hbar = beta^{-1} - P exactly: the rescaled maps converge to -P", ok)
    # rescaled metric: beta^{-2} g(a,b) + (a.e_t)(b.e_t) = beta^{-2}(a.b)
    #                  + beta^{-1}[(b.e_t)(a.e_r) + (a.e_t)(b.e_r)]  on all pairs
    ok = True
    for beta in (Fraction(7), Fraction(50)):
        him = lambda a: g.add(a, g.scal(beta, g.scal(g.dotv(a, et, STA), er)))
        for a in basis:
            for c in basis:
                lhs = (g.dotv(him(a), him(c), STA) / beta ** 2
                       + g.dotv(a, et, STA) * g.dotv(c, et, STA))
                rhs = (g.dotv(a, c, STA) / beta ** 2
                       + (g.dotv(c, et, STA) * g.dotv(a, er, STA)
                          + g.dotv(a, et, STA) * g.dotv(c, er, STA)) / beta)
                ok = ok and lhs == rhs
    g.check("[Prop 2.6] rescaled-metric identity: beta^{-2} g + (a.e_t)(b.e_t) = O(beta^{-1}) exactly "
            "on all 16 basis pairs", ok)
    # the limit form ghat(a,b) = -(a.e_t)(b.e_t): signature (0,1,3), radical contains e_r
    ghat = [[-(g.dotv(a, et, STA) * g.dotv(c, et, STA)) for c in basis] for a in basis]
    sig = g.congruence_signature(ghat)
    radical_ok = all(ghat[1][j] == 0 for j in range(4)) and all(ghat[i][1] == 0 for i in range(4))
    g.check("[Prop 2.6] the limit form ghat = -(a.e_t)(b.e_t) has signature (0,1,3): rank one, "
            "radical of dimension three containing e_r", sig == (0, 1, 3) and radical_ok)
    # the limit of the null directions is e_r: ghat-null, g-spacelike
    g.check("[Prop 2.6] the limit direction e_r is null for the limit form (ghat(e_r,e_r) = 0) while "
            "g(e_r,e_r) = -1 at every radius: nullity of the limit lives in the limit form",
            ghat[1][1] == 0 and g.dotv(er, er, STA) == -1)

    # [Prop 2.7] Kretschmann invariant from the eigenvalues, as an RF identity
    r = g.RF.var()
    lam_rad = g.RF.const(2 * MASS) / (r * r * r)
    lam_mix = g.RF.const(MASS) / (r * r * r)
    K = g.RF.const(4) * (g.RF.const(2) * lam_rad * lam_rad + g.RF.const(4) * lam_mix * lam_mix)
    want = g.RF.const(48 * MASS * MASS) / (r * r * r * r * r * r)
    g.check("[Prop 2.7] Kretschmann: 4(2 lam_rad^2 + 4 lam_mix^2) = 48 M^2 / r^6 as an exact identity "
            "(divergent, gauge-invariant: no gauge repairs the singularity)", K.eqrf(want))


def step2_checks():
    g.check("[Prop 3.1] p - q = -2 = 6 mod 8, and 6 != 1 mod 4 (no type C)",
            (1 - 3) % 8 == 6 and 6 % 4 != 1)
    central = [b for b in g.all_blades(4)
               if all(g.eq(g.mul({b: Fraction(1)}, g.gen(i), STA), g.mul(g.gen(i), {b: Fraction(1)}, STA))
                      for i in range(4))]
    g.check("[Prop 3.1] Cl(1,3) centre = span{1} (blade-wise, exhaustive): simple, type N operative",
            central == [()])


# ---------------------------------------------------------------------------
# [Lem 4.1] the atom; [Prop 5.5] descent; [Thm 6.3] modular structure
# ---------------------------------------------------------------------------

def atom_checks():
    e0, e1 = g.gen(0), g.gen(1)
    v = g.scal(Fraction(1, 2), g.add(e0, e1))
    vs = g.scal(Fraction(1, 2), g.sub(e0, e1))
    ok = g.is_zero(g.mul(v, v, CL11)) and g.is_zero(g.mul(vs, vs, CL11))
    anti = g.add(g.mul(v, vs, CL11), g.mul(vs, v, CL11))
    ok = ok and g.eq(anti, g.sc(1))
    g.check("[Lem 4.1] atom: v = (e0+e1)/2, v* = (e0-e1)/2 satisfy the CAR exactly", ok)
    ok = g.eq(g.mul(g.mul(v, vs, CL11), v, CL11), v) and g.eq(g.mul(g.mul(vs, v, CL11), vs, CL11), vs)
    g.check("[Lem 4.1] pseudo-inverse identities v v* v = v and v* v v* = v*", ok)
    blades = g.all_blades(2)
    imgs = [g.mul(v, {b: Fraction(1)}, CL11) for b in blades]
    vecs = [[x.get(b, Fraction(0)) for b in blades] for x in imgs]
    one_vec = [[Fraction(1) if b == () else Fraction(0) for b in blades]]
    g.check("[Lem 4.1] v has no inverse: rank(v Cl(1,1)) = 2 < 4 and 1 is not in v Cl(1,1)",
            g.rank_of_vectors(vecs) == 2 and g.rank_of_vectors(vecs + one_vec) == 3)
    P = g.mul(vs, v, CL11)
    Q = g.mul(v, vs, CL11)
    ok = g.eq(g.mul(P, P, CL11), P) and g.eq(g.mul(Q, Q, CL11), Q) and g.eq(g.add(P, Q), g.sc(1))
    g.check("[Prop 5.5] P = v*v and 1-P = vv* are complementary idempotents", ok)
    sigma = g.sub(P, Q)
    ok = g.eq(sigma, g.mul(e0, e1, CL11)) and g.eq(g.mul(sigma, sigma, CL11), g.sc(1))
    g.check("[Thm 6.3] sigma = v*v - vv* = e0 e1 exactly, and sigma^2 = 1", ok)
    ok = g.eq(g.mul(sigma, v, CL11), g.scal(-1, v)) and g.eq(g.mul(v, sigma, CL11), v)
    g.check("[Thm 6.3] sigma v = -v and v sigma = v", ok)
    # rational rotor: cosh = 5/3, sinh = 4/3, e^{-lambda} = cosh - sinh = 1/3
    ch, sh = Fraction(5, 3), Fraction(4, 3)
    # R_lambda = cosh(l/2) + sinh(l/2) sigma; use half-angle rational pair (c2, s2) with
    # c2^2 + s2^2 = ch and 2 c2 s2 = sh: (c2, s2) = (3/sqrt5, ...) is irrational, so verify
    # the SQUARED rotor action instead: R^2 v R^{-2} = e^{-2 lambda} v with R^2 = ch + sh*sigma.
    R2 = g.add(g.sc(ch), g.scal(sh, sigma))
    R2inv = g.sub(g.sc(ch), g.scal(sh, sigma))
    ok = g.eq(g.mul(R2, R2inv, CL11), g.sc(1))
    conj = g.mul(g.mul(R2, v, CL11), R2inv, CL11)
    ok = ok and g.eq(conj, g.scal(Fraction(1, 9), v))
    conj2 = g.mul(g.mul(R2, vs, CL11), R2inv, CL11)
    ok = ok and g.eq(conj2, g.scal(Fraction(9), vs))
    g.check("[Thm 6.3] rotor flow: (cosh,sinh) = (5/3,4/3) scales v by (1/3)^2 and v* by 3^2 exactly", ok)
    half = Fraction(1, 2)
    ok = g.eq(g.scal(half, g.add(g.sc(1), sigma)), P) and g.eq(g.scal(half, g.sub(g.sc(1), sigma)), Q)
    g.check("[Thm 6.3] spectral projectors (1 +- sigma)/2 = descent projectors", ok)


# ---------------------------------------------------------------------------
# [Thm 6.1] the shape operator, blade-exact; [Cor 6.4] the weld
# ---------------------------------------------------------------------------

def shape_checks():
    sr = g.mul(g.gen(0), g.gen(1), STA)     # sigma_r = e_t e_r (radial boost blade)
    g.check("[Thm 6.1] sigma_r^2 = +1 (boost plane)", g.eq(g.mul(sr, sr, STA), g.sc(1)))

    def S(B):
        return g.scal(Fraction(-1, 2), g.add(B, g.scal(3, g.mul(g.mul(sr, B, STA), sr, STA))))

    planes = [(0, 1), (2, 3), (0, 2), (0, 3), (1, 2), (1, 3)]
    expected = {(0, 1): -2, (2, 3): -2, (0, 2): 1, (0, 3): 1, (1, 2): 1, (1, 3): 1}
    ok = True
    for pl in planes:
        B = {pl: Fraction(1)}
        ok = ok and g.eq(S(B), g.scal(expected[pl], B))
    g.check("[Thm 6.1] S = -1/2(B + 3 sigma_r B sigma_r) has eigenvalue -2 on {sigma_r, I sigma_r} "
            "and +1 on the four mixed planes, blade-exact", ok)
    # S = 1 - 3 Pi
    ok = True
    for pl in planes:
        B = {pl: Fraction(1)}
        Pi = B if pl in ((0, 1), (2, 3)) else {}
        ok = ok and g.eq(S(B), g.sub(B, g.scal(3, Pi)))
    g.check("[Thm 6.1] S = 1 - 3 Pi with Pi the projection onto span{sigma_r, I sigma_r}", ok)
    # S^2 + S = 2 on every plane; trace = 0
    ok = True
    for pl in planes:
        B = {pl: Fraction(1)}
        ok = ok and g.eq(g.add(S(S(B)), S(B)), g.scal(2, B))
    trace = sum(expected[pl] for pl in planes)
    g.check("[Thm 6.1] S^2 + S = 2 as an operator identity on all six planes; trace = 0 (the trace "
            "vanishes for 1 - 3 Pi with rank-two Pi, as the paper states)",
            ok and trace == 0)
    # ratio of the appendix eigenvalues equals the S-eigenvalue ratio, with the appendix values
    # DERIVED here (lam_rad = -f''/2, lam_mix = -f'/(2r), f = 1 - 2M/r) rather than copied literals,
    # and the S-eigenvalue ratio taken from the expected table verified above
    r = g.RF.var()
    f_rf = (r - g.RF.const(2 * MASS)) / r
    fp_rf = f_rf.deriv()
    fpp_rf = fp_rf.deriv()
    lam_rad = g.RF.const(0) - fpp_rf / g.RF.const(2)
    lam_mix = g.RF.const(0) - fp_rf / (g.RF.const(2) * r)
    s_ratio = g.RF.const(Fraction(expected[(0, 1)], expected[(0, 2)]))
    ok = (lam_rad / lam_mix).eqrf(s_ratio) and lam_rad.eqrf(g.RF.const(2 * MASS) / (r * r * r))
    g.check("[Thm 6.1] the appendix eigenvalue ratio, derived as (-f''/2)/(-f'/2r), equals the "
            "S-eigenvalue ratio -2 : 1 from the conjugation table, as rational functions", ok)
    # the SIGN: R = -(M/r^3) S.  On the radial plane the gauge computation (Prop 2.4) and the appendix
    # both give +2M/r^3, and S(sigma_r) = -2 sigma_r; on a mixed plane the appendix gives -M/r^3 and S = +1.
    minus_M_r3_S = lambda pl: (g.RF.const(0) - g.RF.const(MASS) / (r * r * r)) * g.RF.const(expected[pl])
    ok = minus_M_r3_S((0, 1)).eqrf(lam_rad) and minus_M_r3_S((0, 2)).eqrf(lam_mix) \
        and minus_M_r3_S((2, 3)).eqrf(lam_rad)
    g.check("[Thm 6.1] the sign: -(M/r^3) S reproduces +2M/r^3 on the radial plane and its dual and "
            "-M/r^3 on the mixed planes, as rational-function identities: R = -(M/r^3) S, not +", ok)
    # h-bar invariance of the radial plane: hbar(e_t) ^ hbar(e_r) = e_t ^ e_r
    beta = Fraction(3, 7)
    a = g.sub(g.gen(0), g.scal(beta, g.gen(1)))     # hbar(e_t)
    bvec = g.gen(1)                                  # hbar(e_r) = e_r
    wedge_ab = g.scal(Fraction(1, 2), g.sub(g.mul(a, bvec, STA), g.mul(bvec, a, STA)))
    g.check("[Thm 6.1] the radial plane is hbar-invariant: hbar(e_t) ^ hbar(e_r) = e_t ^ e_r exactly",
            g.eq(wedge_ab, g.mul(g.gen(0), g.gen(1), STA)))
    # [Cor 6.4] the weld: among the six frame planes, eigenvalue -2 and square +1
    # single out the radial plane alone; the atom's sigma lands on it
    ok = True
    for pl in planes:
        B = {pl: Fraction(1)}
        sq = g.mul(B, B, STA)
        is_minus2 = expected[pl] == -2
        is_boost = g.eq(sq, g.sc(1))
        ok = ok and ((is_minus2 and is_boost) == (pl == (0, 1)))
    g.check("[Cor 6.4] the matching: S-eigenvalue -2 and square +1 characterise the radial boost plane "
            "uniquely among the six frame planes: sigma of Thm 6.3 = +-sigma_r by equation", ok)


# ---------------------------------------------------------------------------
# [Lem 7.1] / [Thm 7.3]: finite-dimensional KMS and the TFD reduction
# ---------------------------------------------------------------------------

def kms_checks():
    # Two sample points, so that both signs of beta are exercised: e^{-omega/T} = 9/16 (tan theta
    # = 3/4, the physical, positive-temperature point, populations decreasing with energy) and
    # e^{-omega/T} = 16/9 (tan theta = 4/3, population-inverted, the same identities with beta < 0).
    samples = [(Fraction(9, 16), Fraction(4, 5), Fraction(3, 5)),
               (Fraction(16, 9), Fraction(3, 5), Fraction(4, 5))]

    def unit(i, j):
        M = [[Fraction(0)] * 2 for _ in range(2)]
        M[i][j] = Fraction(1)
        return M

    ok_kms = True
    ok_tfd = True
    for q, c, s in samples:
        Z = 1 + q
        rho = [[Fraction(1) / Z, Fraction(0)], [Fraction(0), q / Z]]
        rho_inv = [[Z, Fraction(0)], [Fraction(0), Z / q]]

        def omega(M, rho=rho):
            P = g.mat_mul(rho, M)
            return P[0][0] + P[1][1]

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        a, b = unit(i, j), unit(k, l)
                        lhs = omega(g.mat_mul(a, b))
                        rhs = omega(g.mat_mul(b, g.mat_mul(rho, g.mat_mul(a, rho_inv))))
                        ok_kms = ok_kms and lhs == rhs
        # |Omega> = c|00> + s|11>; partial trace over partner = diag(c^2, s^2)
        red = [[c * c, Fraction(0)], [Fraction(0), s * s]]
        ok_tfd = ok_tfd and red[0][0] == 1 / Z and red[1][1] == q / Z and (s / c) ** 2 == q
    g.check("[Lem 7.1] KMS identity omega(ab) = omega(b rho a rho^{-1}) on all 16 matrix-unit pairs, "
            "at the physical point e^{-omega/T} = 9/16 and at the population-inverted point 16/9", ok_kms)
    g.check("[Thm 7.3] TFD reduction: diag(16/25, 9/25) = Fermi-Dirac with tan^2 theta = e^{-omega/T} "
            "= 9/16 (physical), and diag(9/25, 16/25) with tan^2 theta = 16/9 (population-inverted)", ok_tfd)


# ---------------------------------------------------------------------------
# [Thm 8.2] the current algebra on a finite fermion array
# states: frozenset of occupied sites among SITES; sea = sites < 0 occupied
# ---------------------------------------------------------------------------

SITES = list(range(-4, 4))


def ferm_apply(op_list, state_dict):
    """op_list: sequence of ('c', k) creation / ('a', k) annihilation, applied right-to-left.
    States: dict {frozenset: Fraction} with sign convention by sorted site order."""
    for kind, k in reversed(op_list):
        out = {}
        for occ, amp in state_dict.items():
            if kind == 'c':
                if k in occ:
                    continue
                sign = Fraction(-1) ** len([j for j in occ if j < k])
                new = frozenset(occ | {k})
            else:
                if k not in occ:
                    continue
                sign = Fraction(-1) ** len([j for j in occ if j < k])
                new = frozenset(occ - {k})
            out[new] = out.get(new, Fraction(0)) + sign * amp
        state_dict = {o: a for o, a in out.items() if a != 0}
    return state_dict


def current(m, state_dict):
    """a_m = sum_k :psi^dag_k psi_{k+m}: acting on a state (m = 0 not used).
    With the sea filled below zero, a_m annihilates the sea for m > 0 and
    [a_m, a_{-m}] = +m on bulk states: the paper's convention."""
    out = {}
    for k in SITES:
        if k + m not in SITES:
            continue
        for occ, amp in ferm_apply([('c', k), ('a', k + m)], dict(state_dict)).items():
            out[occ] = out.get(occ, Fraction(0)) + amp
    return {o: a for o, a in out.items() if a != 0}


def st_eq(x, y):
    ks = set(x) | set(y)
    return all(x.get(k, Fraction(0)) == y.get(k, Fraction(0)) for k in ks)


def sub_state(x, y):
    out = dict(x)
    for k, v in y.items():
        out[k] = out.get(k, Fraction(0)) - v
    return {k: v for k, v in out.items() if v != 0}


def current_checks():
    sea = frozenset(k for k in SITES if k < 0)
    # bulk states: sea with particle-hole modifications within |k| <= 1
    bulk_states = [
        {sea: Fraction(1)},
        {frozenset((sea - {-1}) | {0}): Fraction(1)},
        {frozenset((sea - {-1}) | {1}): Fraction(1)},
    ]
    ok = True
    for st in bulk_states:
        lhs = sub_state(current(1, current(-1, dict(st))), current(-1, current(1, dict(st))))
        ok = ok and st_eq(lhs, st)   # [a_1, a_{-1}] = 1 * id on bulk states
    g.check("[Thm 8.2] [a_1, a_{-1}] = id on bulk states of the finite array (edge terms absent there)", ok)
    ok = True
    for st in bulk_states:
        lhs = sub_state(current(1, current(2, dict(st))), current(2, current(1, dict(st))))
        ok = ok and st_eq(lhs, {})
    g.check("[Thm 8.2] [a_1, a_2] = 0 on bulk states", ok)
    # Planck factor: sum_k n_{k+m}(1 - n_k) = m x^m/(1 - x^m), x = e^{-beta kappa}
    x = Fraction(1, 2)
    for m in (1, 2):
        K = 80

        def n(k):
            return x ** k / (1 + x ** k) if k >= 0 else 1 / (1 + x ** (-k))

        total = sum(n(k + m) * (1 - n(k)) for k in range(-K, K + 1))
        planck = Fraction(m) * x ** m / (1 - x ** m)
        tail = 4 * x ** K / (1 - x)   # explicit geometric tail bound for the truncation error
        ok = abs(total - planck) <= tail
        g.check("[Thm 8.2] Planck factor: |sum n_{k+%d}(1-n_k) - %d x^%d/(1-x^%d)| <= exact tail bound (x = 1/2)"
                % (m, m, m, m), ok)


# ---------------------------------------------------------------------------
# [Prop 10.6] slice arithmetic; [Thm 11.5] rate model
# ---------------------------------------------------------------------------

def capacity_checks():
    # [Prop 10.6] along the WHOLE (C1) locus: parametrise the stretched singularity by an
    # indeterminate c standing for r_c, with 2M := c^3 (the honest parametrisation of the
    # cutoff surface).  The two sides of the slice-volume identity come from different
    # formulas: the slice geometry gives c^4 |f(c)| with |f| = 2M/c - 1, the claim gives
    # (2M)^2 (1 - c/2M).  Both are rational functions in c; equality is an identity, not
    # a sample, and nothing is defined to be its own assertion.
    c = g.RF.var()
    one = g.RF.const(1)
    twoM = c * c * c                                   # (C1): 2M = r_c^3
    absf = twoM / c - one
    slice_side = (c * c * c * c) * absf                # r_c^4 |f(r_c)| from the slice geometry
    claim_side = twoM * twoM * (one - c / twoM)        # (2M)^2 (1 - r_c/2M): the linear-in-M form
    g.check("[Prop 10.6] slice volume per unit Killing time along the whole (C1) locus: "
            "r_c^4 |f(r_c)| = (2M)^2 (1 - r_c/2M) as an identity of rational functions in r_c "
            "(2M = r_c^3, r_c an indeterminate)", slice_side.eqrf(claim_side))
    # rate identity with pi cancelled, same parametrisation, nu rational
    nu = Fraction(3)
    lhs = g.RF.const(nu * nu * 16) * (c * c * c * c) * absf       # (dN/dt / pi)^2
    rhs = g.RF.const(nu * nu * 16) * twoM * twoM * (one - c / twoM)  # (nu/(pi T_H))^2 (1 - r_c/2M)
    g.check("[Prop 10.6] (dN_6a/dt)^2 = (nu/T_H)^2 (1 - r_c/2M), pi cancelled, as rational functions "
            "along the (C1) locus", lhs.eqrf(rhs))
    # negative control: a MASS-INDEPENDENT cutoff radius r_0 cannot reach the area law.  With r_0
    # fixed and m = M the variable, the squared volume r_0^4 (2m/r_0 - 1) is degree 1 in m while
    # the area-law form (2m)^2 (1 - r_0/2m) is degree 2: the two disagree as rational functions.
    m = g.RF.var()
    r0 = g.RF.const(Fraction(9, 4))
    vol_sq_fixed = (r0 * r0 * r0 * r0) * (g.RF.const(2) * m / r0 - g.RF.const(1))
    area_form = (g.RF.const(2) * m) * (g.RF.const(2) * m) * (g.RF.const(1) - r0 / (g.RF.const(2) * m))
    g.check("[Prop 10.6] control: a mass-independent cutoff radius fails the linear-in-M form "
            "(M^{1/2} scaling, the area law unreachable), as rational functions in M",
            not vol_sq_fixed.eqrf(area_form))
    # [Prop 10.7] the capacity calibration, with ln 2 carried as a formal indeterminate L.
    # C = N ln 2 = 8 pi nu M dt L; with nu dt = M/(2L) the capacity is 4 pi M^2 identically in L,
    # and with the FORMER calibration nu dt = M/2 it is 4 pi M^2 L: off by exactly ln 2.
    L = g.RF.var()
    for Mval in (Fraction(3, 2), Fraction(5), Fraction(1, 7)):
        Mc = g.RF.const(Mval)
        nudt_new = Mc / (g.RF.const(2) * L)            # nu dt = M / (2 ln 2)
        cap_new = g.RF.const(8) * Mc * nudt_new * L    # C / pi
        nudt_old = Mc / g.RF.const(2)                  # the old calibration nu dt = M/2
        cap_old = g.RF.const(8) * Mc * nudt_old * L
        ok = cap_new.eqrf(g.RF.const(4) * Mc * Mc) \
            and cap_old.eqrf(g.RF.const(4) * Mc * Mc * L) \
            and not cap_old.eqrf(g.RF.const(4) * Mc * Mc)
        g.check("[Prop 10.7] C = N ln 2 = 4 pi M^2 iff nu Delta t = M/(2 ln 2), ln 2 formal, M = %s; "
                "the old calibration nu Delta t = M/2 gives C = S_BH ln 2, off by exactly ln 2" % Mval, ok)


def rate_model_checks():
    """[Thm 11.5] The rate model in the maximally entangled idealisation, simulated
    on exact density matrices.  Pairs are injected with unnormalised amplitudes
    (1, 1), so every density matrix is rational after division by the norm; the
    window's entropy is computed from its exact spectrum (rho_L is diagonal by
    the support constraint, so the spectrum is its diagonal), and compared with
    min(S_th, C) as formal logarithms."""
    schedule = [3, 3, 3, 3, 2, 2, 1, 1, 0]      # capacity N(t) in qubits, one injection per event
    state = {0: Fraction(1)}
    window, radiation = [], []
    ok_min = ok_maxmix = True
    traj = []
    n_pairs = len(schedule)
    nq = 2 * n_pairs
    S_th = LogVec()
    for t, N in enumerate(schedule):
        state = pair_state(Fraction(1), Fraction(1), t, state)   # maximally entangled, unnormalised
        radiation.append(2 * t)
        window.append(2 * t + 1)
        S_th = S_th + LogVec.ln_int(2)
        while len(window) > N:
            if len(window) >= 2:
                state = apply_cz(window[0], window[1], state)
            radiation.append(window.pop(0))
        norm = sum(a * a for a in state.values())
        if window:
            rhoL = marginal(sorted(window), state, nq)
            rhoL = [[x / norm for x in row] for row in rhoL]
            spec = [rhoL[i][i] for i in range(len(rhoL))]
            diag_ok = all(rhoL[i][j] == 0 for i in range(len(rhoL)) for j in range(len(rhoL)) if i != j)
            S_L = entropy_logvec(spec)
            ok_maxmix = ok_maxmix and diag_ok and all(x == Fraction(1, len(spec)) for x in spec)
        else:
            S_L = LogVec()
        C = LogVec.ln_int(2) * N
        target = S_th if logvec_le(S_th, C) else C
        ok_min = ok_min and S_L == target
        traj.append(S_L)
    g.check("[Thm 11.5] idealised rate model on exact density matrices: the window entropy, from its exact "
            "spectrum, equals min(S_th, C) at every event of a decreasing capacity schedule, and ends at 0",
            ok_min and traj[-1] == LogVec())
    g.check("[Thm 11.5] in the idealisation the window is exactly maximally mixed at every stage: D = 0 "
            "throughout Phase II", ok_maxmix)


# ---------------------------------------------------------------------------
# Formal logarithms (new in v1.5): a LogVec is a finite rational combination
# sum_p alpha_p ln p over the primes.  ln of a positive rational factorises
# uniquely, so identities between such expressions are exact dictionary
# equalities, and von Neumann entropies of rational spectra are LogVecs.
# Inequalities are decided by RIGOROUS rational interval bounds on ln p
# (ln p = sum_{m=2}^{p} ln(m/(m-1)), each term 2 atanh(1/(2m-1)) summed to K
# terms with an explicit geometric tail bound); no floating point anywhere.
# ---------------------------------------------------------------------------

def factorise(n):
    """Prime factorisation of a positive integer by trial division: {p: e}."""
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


class LogVec(object):
    def __init__(self, d=None):
        self.d = {p: c for p, c in (d or {}).items() if c != 0}

    @staticmethod
    def ln_int(n):
        return LogVec({p: Fraction(e) for p, e in factorise(n).items()})

    @staticmethod
    def ln_rat(q):
        q = Fraction(q)
        assert q > 0
        return LogVec.ln_int(q.numerator) - LogVec.ln_int(q.denominator)

    def __add__(self, o):
        d = dict(self.d)
        for p, c in o.d.items():
            d[p] = d.get(p, Fraction(0)) + c
        return LogVec(d)

    def __neg__(self):
        return LogVec({p: -c for p, c in self.d.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, c):
        return LogVec({p: v * Fraction(c) for p, v in self.d.items()})

    __rmul__ = __mul__

    def __eq__(self, o):
        return self.d == o.d

    def __ne__(self, o):
        return not self.__eq__(o)

    def __repr__(self):
        return "LogVec(" + " + ".join("%s ln %d" % (c, p) for p, c in sorted(self.d.items())) + ")"


_LN_CACHE = {}


def ln_bounds(n, K=40):
    """Rational (lower, upper) bounds on ln n for a positive integer n."""
    if n in _LN_CACHE:
        return _LN_CACHE[n]
    lo, hi = Fraction(0), Fraction(0)
    for m in range(2, n + 1):
        z = Fraction(1, 2 * m - 1)
        zz = z * z
        term, partial = z, Fraction(0)
        for k in range(K):
            partial += term / (2 * k + 1)
            term *= zz
        # tail: 2 sum_{k>=K} z^{2k+1}/(2k+1) <= 2 z^{2K+1} / ((2K+1)(1 - z^2))
        tail = 2 * term / ((2 * K + 1) * (1 - zz))
        lo += 2 * partial
        hi += 2 * partial + tail
    _LN_CACHE[n] = (lo, hi)
    return lo, hi


def logvec_bounds(v):
    lo, hi = Fraction(0), Fraction(0)
    for p, c in v.d.items():
        a, b = ln_bounds(p)
        if c > 0:
            lo += c * a
            hi += c * b
        else:
            lo += c * b
            hi += c * a
    return lo, hi


def logvec_lt(u, v):
    """True iff u < v, decided rigorously (equal vectors return False)."""
    if u == v:
        return False
    lo, hi = logvec_bounds(v - u)
    if lo > 0:
        return True
    if hi < 0:
        return False
    raise ValueError("interval bounds too weak to decide the inequality")


def logvec_le(u, v):
    return u == v or logvec_lt(u, v)


def entropy_logvec(probs):
    """Von Neumann entropy -sum p ln p of a rational spectrum, as a LogVec (nats)."""
    out = LogVec()
    for p in probs:
        if p != 0:
            assert p > 0
            out = out - LogVec.ln_rat(p) * p
    return out


def binary_entropy_logvec(p):
    return entropy_logvec([Fraction(p), 1 - Fraction(p)])


LN2 = None  # set lazily: LogVec.ln_int(2)


# ---------------------------------------------------------------------------
# The finite-ledger model: exact multi-qubit simulator
# qubits indexed 0..2n-1: R_k = 2k, L_k = 2k+1. States: dict {bitmask: Fraction}.
# ---------------------------------------------------------------------------

def pair_state(c, s, k, state):
    """Tensor a fresh thermofield pair (R_k, L_k) onto the state."""
    out = {}
    for m, a in state.items():
        out[m] = out.get(m, Fraction(0)) + a * c
        m2 = m | (1 << (2 * k)) | (1 << (2 * k + 1))
        out[m2] = out.get(m2, Fraction(0)) + a * s
    return out


def apply_cz(i, j, state):
    return {m: (-a if (m >> i) & 1 and (m >> j) & 1 else a) for m, a in state.items()}


def marginal(qubits, state, nq):
    """Exact reduced density matrix over the listed qubits (dimension 2^len)."""
    d = 1 << len(qubits)
    rho = [[Fraction(0)] * d for _ in range(d)]
    rest = [q for q in range(nq) if q not in qubits]
    for m1, a1 in state.items():
        for m2, a2 in state.items():
            if all(((m1 >> r) & 1) == ((m2 >> r) & 1) for r in rest):
                i = sum(((m1 >> q) & 1) << t for t, q in enumerate(qubits))
                j = sum(((m2 >> q) & 1) << t for t, q in enumerate(qubits))
                rho[i][j] += a1 * a2
    return rho


def purity(rho):
    d = len(rho)
    return sum(rho[i][j] * rho[j][i] for i in range(d) for j in range(d))


def pinch(rho):
    """The multi-mode descent E_N on a density matrix in the joint number basis:
    complete dephasing (zero every off-diagonal entry)."""
    d = len(rho)
    return [[rho[i][j] if i == j else Fraction(0) for j in range(d)] for i in range(d)]


def expect_xstring(xs, zs, state, nq):
    """<prod X_i prod Z_j> for a real-amplitude state."""
    tot = Fraction(0)
    for m, a in state.items():
        m2 = m
        for i in xs:
            m2 ^= (1 << i)
        b = state.get(m2, Fraction(0))
        sign = Fraction(1)
        for j in zs:
            if (m >> j) & 1:
                sign = -sign
        tot += a * b * sign
    return tot


def expect_xstring_rho(xs, zs, rho, qubits):
    """<prod X prod Z> against a density matrix over the listed qubits.
    xs, zs are positions WITHIN the qubit list."""
    d = len(rho)
    xmask = 0
    for i in xs:
        xmask ^= (1 << i)
    tot = Fraction(0)
    for i in range(d):
        sign = Fraction(1)
        for j in zs:
            if (i >> j) & 1:
                sign = -sign
        tot += rho[i ^ xmask][i] * sign
    return tot


MODEL_PAIRS = [(Fraction(4, 5), Fraction(3, 5)), (Fraction(4, 5), Fraction(3, 5)),
               (Fraction(4, 5), Fraction(3, 5)), (Fraction(12, 13), Fraction(5, 13))]
# c_k > s_k throughout, so every tan^2 theta_k = (s_k/c_k)^2 < 1 and every omega_k > 0


def build_model():
    """Run the full model (n = 4 pairs, capacity 2, CZ scrambling before each
    eviction); return the list of stages (state, radiation, window)."""
    pairs = MODEL_PAIRS
    state = {0: Fraction(1)}
    window = []
    radiation = []
    stages = []
    for k, (c, s) in enumerate(pairs):
        state = pair_state(c, s, k, state)
        radiation.append(2 * k)
        window.append(2 * k + 1)
        if len(window) > 2:
            state = apply_cz(window[0], window[1], state)   # scramble
            evicted = window.pop(0)
            radiation.append(evicted)                        # eviction = handover to R
        stages.append((dict(state), list(radiation), list(window)))
    # final flush: evict remaining window qubits (end of evaporation)
    while window:
        if len(window) >= 2:
            state = apply_cz(window[0], window[1], state)
        radiation.append(window.pop(0))
        stages.append((dict(state), list(radiation), list(window)))
    return stages, pairs, 2 * len(pairs)


def model_checks():
    stages, pairs, nq = build_model()
    n = len(pairs)

    # support constraint and normalisation at every stage
    ok_support = ok_norm = True
    for st, rad, win in stages:
        for m, a in st.items():
            ok_support = ok_support and all((((m >> (2 * k)) & 1) == ((m >> (2 * k + 1)) & 1))
                                            for k in range(n))
        ok_norm = ok_norm and sum(a * a for a in st.values()) == 1
    g.check("[Lem 12.1] support constraint R_k = L_k holds in every configuration at every stage", ok_support)
    g.check("[Lem 12.1] global state stays normalised (pure) at every stage", ok_norm)

    # parity protection: every single-qubit marginal exactly thermal, every stage
    ok = True
    for st, rad, win in stages:
        present = sorted(set(rad + win))
        for q in present:
            k = q // 2
            c, s = pairs[k]
            rho = marginal([q], st, nq)
            ok = ok and rho[0][0] == c * c and rho[1][1] == s * s and rho[0][1] == 0 and rho[1][0] == 0
    g.check("[Lem 12.1] parity protection: EVERY single-qubit marginal = diag(c^2, s^2) exactly, "
            "every stage, scrambling included", ok)

    # Schmidt purity equality at every stage: purity(R) = purity(L)
    ok = True
    for st, rad, win in stages:
        if not win:
            continue
        pr = purity(marginal(sorted(rad), st, nq))
        pl = purity(marginal(sorted(win), st, nq))
        ok = ok and pr == pl
    g.check("[Prop 12.3] Schmidt equality: purity(R) = purity(L) exactly at every stage (global purity)", ok)

    # final: radiation = everything, pure
    final_state = stages[-1][0]
    pr = purity(marginal(sorted(stages[-1][1]), final_state, nq))
    g.check("[Prop 12.3] at completion the radiation alone is pure: tr rho_R^2 = 1 (S_2 = 0)", pr == 1)

    # Renyi-2 Page shape: purity of R falls (entropy rises) then returns to 1
    purities = []
    for st, rad, win in stages:
        purities.append(purity(marginal(sorted(rad), st, nq)))
    ok = purities[0] < 1 and min(purities) < purities[0] and purities[-1] == 1
    g.check("[Prop 12.3] Renyi-2 Page shape: purity of the radiation falls, then returns to exactly 1", ok)

    # two-pair damping and decoding instance
    c1, s1 = pairs[0]
    c2, s2 = pairs[1]
    st2 = pair_state(c2, s2, 1, pair_state(c1, s1, 0, {0: Fraction(1)}))
    st2_scr = apply_cz(1, 3, st2)   # CZ between L_1 (qubit 1) and L_2 (qubit 3)
    gamma = c2 * c2 - s2 * s2
    rho = marginal([0, 1], st2_scr, 4)
    ok = rho[0][3] == c1 * s1 * gamma and rho[3][0] == c1 * s1 * gamma \
        and rho[0][0] == c1 * c1 and rho[3][3] == s1 * s1
    g.check("[Prop 12.3] coherence damping: rho_{R1 L1} coherence = c1 s1 gamma with gamma = c2^2 - s2^2, exactly", ok)
    pur = purity(rho)
    ok = pur == c1 ** 4 + s1 ** 4 + 2 * c1 ** 2 * s1 ** 2 * gamma ** 2 and pur < 1
    g.check("[Prop 12.3] pair purity drops to c^4 + s^4 + 2 c^2 s^2 gamma^2 < 1: correlations left the pair", ok)
    xx_scr = expect_xstring([0, 1], [], st2_scr, 4)
    xx_plain = expect_xstring([0, 1], [], st2, 4)
    xxz_scr = expect_xstring([0, 1], [3], st2_scr, 4)
    xxz_plain = expect_xstring([0, 1], [3], st2, 4)
    ok = xx_plain == 2 * c1 * s1 and xx_scr == 2 * c1 * s1 * gamma \
        and xxz_scr == 2 * c1 * s1 and xxz_plain == 2 * c1 * s1 * gamma
    g.check("[Prop 12.3] decoding: (<XX>, <XXZ>) = (2cs, 2cs*gamma) unscrambled vs (2cs*gamma, 2cs) scrambled: "
            "the gate pattern is readable from triples while singles are pinned thermal", ok)

    # ---- [Prop 12.4] the model's entropy sequence, exactly (formal logarithms) ----
    ln2 = LogVec.ln_int(2)
    h = [binary_entropy_logvec(c * c) for c, s_ in pairs]
    S_th_seq, S_R_seq, C_seq, table_ok = [], [], [], True
    ok_diag = ok_ident = ok_phase1 = ok_strict = ok_bound = ok_end = True
    D_prev = None
    purities_R = []
    for t, (st, rad, win) in enumerate(stages):
        injected = min(t + 1, n)
        S_th = LogVec()
        for k in range(injected):
            S_th = S_th + h[k]
        Wset = [q // 2 for q in win]
        C = ln2 * len(win)
        if win:
            rhoL = marginal(sorted(win), st, nq)
            d = len(rhoL)
            diag_ok = all(rhoL[i][j] == 0 for i in range(d) for j in range(d) if i != j)
            spec = [rhoL[i][i] for i in range(d)]
            S_L = entropy_logvec(spec)
            # the product distribution of the window members
            prod_ok = True
            for idx in range(d):
                pr = Fraction(1)
                for pos, q in enumerate(sorted(win)):
                    c, s_ = pairs[q // 2]
                    pr *= (s_ * s_ if (idx >> pos) & 1 else c * c)
                prod_ok = prod_ok and spec[idx] == pr
            ok_diag = ok_diag and diag_ok and prod_ok
        else:
            S_L = LogVec()
        rhoR = marginal(sorted(rad), st, nq)
        # S_R = S_L by purity: checked through the purity equality already; here the entropy identity
        S_sum = LogVec()
        for k in Wset:
            S_sum = S_sum + h[k]
        ok_ident = ok_ident and S_L == S_sum
        purities_R.append(purity(rhoR))
        pur_expected = Fraction(1)
        for k in Wset:
            c, s_ = pairs[k]
            pur_expected *= c ** 4 + s_ ** 4
        table_ok = table_ok and purity(rhoR) == pur_expected
        phase1 = (len(win) == injected) and t < n
        if phase1:
            ok_phase1 = ok_phase1 and S_L == S_th
        elif win:
            # Phase II: S_L < C strictly (no pair is maximally entangled), and S_L <= min(S_th, C)
            ok_strict = ok_strict and logvec_lt(S_L, C) and logvec_le(S_L, S_th)
        # [Thm 11.5](4) the falling branch: S_R = C - sum_{k in W} (ln 2 - h_k), and S_R <= C
        short = LogVec()
        for k in Wset:
            short = short + (ln2 - h[k])
        ok_bound = ok_bound and (S_L == C - short) and logvec_le(S_L, C)
        S_th_seq.append(S_th); S_R_seq.append(S_L); C_seq.append(C)
        if not win:
            ok_end = ok_end and S_L == LogVec() and purity(rhoR) == 1
    g.check("[Thm 11.5](1) / [Prop 12.4] rho_L is diagonal in the number basis with the product distribution "
            "of its members at every stage (exact spectrum)", ok_diag)
    g.check("[Thm 11.5](1) / [Prop 12.4] S_R = S_L = sum_{k in W} H(c_k^2) at every stage, as an identity "
            "of formal logarithms; tr rho_R^2 = prod_{k in W} (c_k^4 + s_k^4) (Table 3)", ok_ident and table_ok)
    g.check("[Prop 12.4] Phase I: S_R = S_th exactly at events 1 and 2", ok_phase1)
    g.check("[Prop 12.4] Phase II: S_R < C strictly and S_R <= S_th at every stage with a nonempty window "
            "(decided by rigorous rational bounds on ln 2, ln 3, ln 5, ln 13)", ok_strict)
    g.check("[Thm 11.5](4) the falling branch: S_R = C - sum_{k in W} (ln 2 - h_k) exactly and S_R <= C at "
            "every stage, on the thermal model", ok_bound)
    g.check("[Prop 12.4] at completion S_R = 0 and tr rho_R^2 = 1", ok_end)

    # ---- [Cor 11.7] what an event returns: S(A) = h_k + sum_evicted h_j and
    #      I(A:R_<) = 2 sum_evicted h_j, all three entropies from exact spectra ----
    ok_mirror = True
    n_events = 0
    for t in range(1, len(stages)):
        st_prev, rad_prev, win_prev = stages[t - 1]
        st, rad, win = stages[t]
        A = sorted(set(rad) - set(rad_prev))
        if not A:
            continue
        n_events += 1
        # rho_A: every member of A has its partner outside A, so it is diagonal (checked)
        rhoA = marginal(A, st, nq)
        d = len(rhoA)
        if not all(rhoA[i][j] == 0 for i in range(d) for j in range(d) if i != j):
            ok_mirror = False
            continue
        S_A = entropy_logvec([rhoA[i][i] for i in range(d)])
        # S(R_<): rho_{R_<} is untouched by the event (nothing acts on it), so its entropy is that of
        # the previous stage's radiation, which by purity is the entropy of the previous window, read
        # from the exact (diagonal) spectrum of rho_W at stage t-1; the purity equality is re-checked.
        rhoW_prev = marginal(sorted(win_prev), st_prev, nq)
        dW = len(rhoW_prev)
        diag_prev = all(rhoW_prev[i][j] == 0 for i in range(dW) for j in range(dW) if i != j)
        S_Rless = entropy_logvec([rhoW_prev[i][i] for i in range(dW)])
        pur_ok = purity(marginal(sorted(rad_prev), st_prev, nq)) == purity(rhoW_prev)
        # S(A u R_<) = S(radiation after) = S(W') by purity, from the exact spectrum of rho_W'
        if win:
            rhoW = marginal(sorted(win), st, nq)
            dW2 = len(rhoW)
            diag_now = all(rhoW[i][j] == 0 for i in range(dW2) for j in range(dW2) if i != j)
            S_all = entropy_logvec([rhoW[i][i] for i in range(dW2)])
            pur_ok = pur_ok and purity(marginal(sorted(rad), st, nq)) == purity(rhoW)
        else:
            diag_now = True
            S_all = LogVec()
        I_mut = S_A + S_Rless - S_all
        new_k = [q // 2 for q in A if q % 2 == 0]
        evicted = [q // 2 for q in A if q % 2 == 1]
        want_SA = LogVec()
        for k in new_k + evicted:
            want_SA = want_SA + h[k]
        want_I = LogVec()
        for j in evicted:
            want_I = want_I + h[j] * 2
        ok_mirror = ok_mirror and diag_prev and diag_now and pur_ok and S_A == want_SA and I_mut == want_I
    g.check("[Cor 11.7] at every event of the model's history, from exact spectra: S(A) = h_k + sum_evicted h_j "
            "and I(A:R_<) = 2 sum_evicted h_j (%d events; the new quantum arrives uncorrelated, each evicted "
            "qubit fully correlated)" % n_events, ok_mirror and n_events == 5)

    # ---- [Cor 11.6] (L_E) cannot be dropped: a non-diagonal window unitary breaks S_R <= S_th ----
    c, s_ = Fraction(24, 25), Fraction(7, 25)
    st2 = pair_state(c, s_, 1, pair_state(c, s_, 0, {0: Fraction(1)}))     # qubits R1=0, L1=1, R2=2, L2=3
    co, si = Fraction(3, 5), Fraction(4, 5)
    rot = {}
    for m, a in st2.items():
        l1, l2 = (m >> 1) & 1, (m >> 3) & 1
        if (l1, l2) == (0, 0):
            rot[m] = rot.get(m, Fraction(0)) + co * a
            m11 = m | (1 << 1) | (1 << 3)
            rot[m11] = rot.get(m11, Fraction(0)) + si * a
        elif (l1, l2) == (1, 1):
            m00 = m & ~((1 << 1) | (1 << 3))
            rot[m00] = rot.get(m00, Fraction(0)) - si * a
            rot[m] = rot.get(m, Fraction(0)) + co * a
        else:
            rot[m] = rot.get(m, Fraction(0)) + a
    norm_ok = sum(a * a for a in rot.values()) == 1
    rhoL2 = marginal([3], rot, 4)                    # after evicting L1 the window is L2 alone
    S_after = entropy_logvec([rhoL2[0][0], rhoL2[1][1]]) if rhoL2[0][1] == 0 else None
    S_th2 = binary_entropy_logvec(c * c) * 2
    marg_moved = not (rhoL2[0][0] == c * c and rhoL2[1][1] == s_ * s_)
    g.check("[Cor 11.6] (L_E) is necessary: with (c,s) = (24/25, 7/25) and a rotation |00> -> 3/5|00> + 4/5|11> "
            "on (L1, L2) before evicting L1, rho_{L2} = diag(5968/15625, 9657/15625) and S_R = S_L > S_th, "
            "by rigorous rational bounds (all other inputs hold)",
            norm_ok and S_after is not None and marg_moved
            and rhoL2[0][0] == Fraction(5968, 15625) and rhoL2[1][1] == Fraction(9657, 15625)
            and logvec_lt(S_th2, S_after))


# ---------------------------------------------------------------------------
# [Def 9.1] / [Prop 9.2] / [Thm 9.3] / [Cor 9.4] / [Prop 12.5]:
# the multi-mode descent, its price, and the two ledgers in numbers
# ---------------------------------------------------------------------------

def descent_checks():
    # [Def 9.1] structural properties of the pinching on a generic rational matrix
    A = [[Fraction(1), Fraction(2), Fraction(3), Fraction(4)],
         [Fraction(5), Fraction(6), Fraction(7), Fraction(8)],
         [Fraction(9), Fraction(1, 2), Fraction(2, 3), Fraction(3, 5)],
         [Fraction(4, 7), Fraction(1, 9), Fraction(8, 3), Fraction(11)]]
    B = [[Fraction(2), Fraction(1), Fraction(0), Fraction(5)],
         [Fraction(3), Fraction(7), Fraction(1, 3), Fraction(2)],
         [Fraction(1, 5), Fraction(4), Fraction(6), Fraction(1)],
         [Fraction(9), Fraction(2, 7), Fraction(3), Fraction(8)]]
    EA, EB = pinch(A), pinch(B)
    ok = EA == pinch(EA)
    ok = ok and sum(A[i][i] for i in range(4)) == sum(EA[i][i] for i in range(4))
    tr = lambda M: sum(M[i][i] for i in range(len(M)))
    ok = ok and tr(g.mat_mul(EA, B)) == tr(g.mat_mul(A, EB))
    g.check("[Def 9.1] E_N is idempotent, trace-preserving, and Hilbert-Schmidt self-adjoint "
            "(tr(E(a)b) = tr(a E(b))), on a generic rational matrix", ok)

    # [Prop 9.2] (i) single-mode coincidence: TFD mode marginal is already diagonal
    c, s = Fraction(3, 5), Fraction(4, 5)
    st = pair_state(c, s, 0, {0: Fraction(1)})
    mode = marginal([0], st, 2)
    g.check("[Prop 9.2] single mode: the partial trace over the partner is diagonal, so pinching "
            "and partial trace coincide (E(rho_mode) = rho_mode)", pinch(mode) == mode)
    # (ii) two modes: the pair marginal carries coherence c1 s1 gamma, which E kills
    c1, s1 = MODEL_PAIRS[0]
    c2, s2 = MODEL_PAIRS[1]
    gamma = c2 * c2 - s2 * s2
    st2 = pair_state(c2, s2, 1, pair_state(c1, s1, 0, {0: Fraction(1)}))
    st2_scr = apply_cz(1, 3, st2)
    rho_pair = marginal([0, 1], st2_scr, 4)
    Erho_pair = pinch(rho_pair)
    ok = rho_pair[0][3] == c1 * s1 * gamma and Erho_pair[0][3] == 0 \
        and Erho_pair[0][0] == rho_pair[0][0] and Erho_pair[3][3] == rho_pair[3][3]
    g.check("[Prop 9.2] two modes: partial trace retains the coherence c1 s1 gamma; the pinching "
            "annihilates it and keeps the populations: the coincidence is single-mode only", ok)

    # [Thm 9.3] key lemma in moment form: tr(rho (E rho)^m) = tr(E(rho) (E rho)^m), computed with full
    # matrix products on the scrambled two-pair state (16 x 16, off-diagonal entries present), and a
    # control showing the identity FAILS when the diagonal factor is replaced by rho itself.
    stages, pairs, nq = build_model()
    final_state, final_rad, _ = stages[-1]
    rho_R = marginal(sorted(final_rad), final_state, nq)
    E_rho = pinch(rho_R)
    rho4 = marginal([0, 1, 2, 3], st2_scr, 4)
    E4 = pinch(rho4)
    has_offdiag = any(rho4[i][j] != 0 for i in range(16) for j in range(16) if i != j)

    def mmul(A, B):
        n = len(A)
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

    def mtrace(A):
        return sum(A[i][i] for i in range(len(A)))

    ok = has_offdiag
    Em = E4
    for m in (1, 2, 3):
        lhs = mtrace(mmul(rho4, Em))          # tr(rho (E rho)^m)
        rhs = mtrace(mmul(E4, Em))            # tr(E rho (E rho)^m)
        ok = ok and lhs == rhs
        Em = mmul(Em, E4)
    control = mtrace(mmul(rho4, rho4)) != mtrace(mmul(E4, rho4))   # tr(rho^2) != tr(E(rho) rho)
    g.check("[Thm 9.3] key lemma, moment form: tr(rho (E rho)^m) = tr(E(rho) (E rho)^m) for m = 1, 2, 3 by "
            "full matrix products on a state with nonzero coherences; control: tr(rho rho) != tr(E(rho) rho), "
            "so the identity rests on f(E rho) being diagonal", ok and control)

    # [Cor 9.4] marginals pass through E_N unchanged (they are diagonal by parity protection)
    ok = True
    for q in range(nq):
        mq = marginal([q], final_state, nq)
        # marginal of the pinched state: pinching commutes with partial trace onto
        # a diagonal marginal; compute directly from E_rho
        d = len(rho_R)
        pos = sorted(final_rad).index(q)
        m00 = sum(E_rho[i][i] for i in range(d) if not (i >> pos) & 1)
        m11 = sum(E_rho[i][i] for i in range(d) if (i >> pos) & 1)
        ok = ok and mq[0][0] == m00 and mq[1][1] == m11 and mq[0][1] == 0
    g.check("[Cor 9.4] every single-quantum marginal is IDENTICAL at the two levels: the deficit "
            "is carried by correlations alone", ok)

    # [Prop 12.5] the two ledgers in numbers
    pur_asc = purity(rho_R)
    pur_desc = purity(E_rho)
    prod_formula = Fraction(1)
    for (ck, sk) in pairs:
        prod_formula *= ck ** 4 + sk ** 4
    g.check("[Prop 12.5] ascended level: tr rho_R^2 = 1 (S_2 = 0); descended level: "
            "tr(E rho_R)^2 = prod_k (c_k^4 + s_k^4) exactly",
            pur_asc == 1 and pur_desc == prod_formula)
    g.check("[Prop 12.5] the printed value: prod_k (c_k^4 + s_k^4) = 817544276833/6972900390625",
            prod_formula == Fraction(817544276833, 6972900390625))
    # the von Neumann entropy of E rho_R is sum_k H(c_k^2) = S_th exactly, as formal logarithms
    d = len(E_rho)
    S_desc = entropy_logvec([E_rho[i][i] for i in range(d)])
    S_th_all = LogVec()
    for (ck, sk) in pairs:
        S_th_all = S_th_all + binary_entropy_logvec(ck * ck)
    g.check("[Prop 12.5] S(E rho_R) = sum_k H(c_k^2) = S_th exactly, as an identity of formal logarithms "
            "(the deficit D(rho_R || E rho_R) = S_th, since S(rho_R) = 0)",
            S_desc == S_th_all and S_desc != LogVec())
    # the descended entropy is monotone: purity of E(rho_R(t)) non-increasing, and
    # pinching never increases purity
    ok_mono = ok_maj = ok_ent = True
    prev = None
    prev_S = None
    for st, rad, win in stages:
        rho_t = marginal(sorted(rad), st, nq)
        nrm = sum(a * a for a in st.values())
        p_desc = purity(pinch(rho_t))
        p_asc = purity(rho_t)
        ok_maj = ok_maj and p_desc <= p_asc
        if prev is not None:
            ok_mono = ok_mono and p_desc <= prev
        prev = p_desc
        S_t = entropy_logvec([rho_t[i][i] / nrm for i in range(len(rho_t)) if rho_t[i][i] != 0])
        if prev_S is not None:
            ok_ent = ok_ent and logvec_le(prev_S, S_t)
        prev_S = S_t
    g.check("[Prop 12.5] the descended radiation entropy is monotone non-decreasing through the run "
            "(no falling branch), verified as formal-logarithm entropies of the descended diagonal "
            "stage by stage, with the Renyi-2 purity non-increasing alongside: Hawking's curve is the "
            "metric-level reading", ok_mono and ok_ent)
    g.check("[Prop 12.5] pinching never increases purity: S_2(E rho) >= S_2(rho) at every stage", ok_maj)
    # the decoding correlators are annihilated exactly by the descent
    rho4_scr = marginal([0, 1, 2, 3], st2_scr, 4)
    rho4_pln = marginal([0, 1, 2, 3], st2, 4)
    ok = True
    for rho4 in (rho4_scr, rho4_pln):
        E4 = pinch(rho4)
        xx = expect_xstring_rho([0, 1], [], E4, [0, 1, 2, 3])
        xxz = expect_xstring_rho([0, 1], [3], E4, [0, 1, 2, 3])
        ok = ok and xx == 0 and xxz == 0
    # while before the descent they carry the signatures
    xx_scr = expect_xstring_rho([0, 1], [], rho4_scr, [0, 1, 2, 3])
    xxz_scr = expect_xstring_rho([0, 1], [3], rho4_scr, [0, 1, 2, 3])
    ok = ok and xx_scr == Fraction(168, 625) and xxz_scr == Fraction(24, 25)
    g.check("[Prop 12.5] the decoding correlators (<XX>, <XXZ>) = (168/625, 24/25) are annihilated "
            "exactly by E_N: 0 in both histories: the message does not descend", ok)
    # intra-pair classical records survive; inter-pair correlations are destroyed
    ok = True
    for k in range(len(pairs)):
        ck, sk = pairs[k]
        qR, qL = sorted(final_rad).index(2 * k), sorted(final_rad).index(2 * k + 1)
        d = len(E_rho)
        pairm = [[Fraction(0)] * 4 for _ in range(4)]
        for i in range(d):
            a = ((i >> qR) & 1) + 2 * ((i >> qL) & 1)
            pairm[a][a] += E_rho[i][i]
        ok = ok and pairm[0][0] == ck * ck and pairm[3][3] == sk * sk \
            and pairm[1][1] == 0 and pairm[2][2] == 0
    g.check("[Prop 12.5] the intra-pair classical record survives descent: each (R_k, L_k) pair of "
            "E rho_R is perfectly correlated, diag(c^2, 0, 0, s^2)", ok)
    ok = True
    d = len(E_rho)
    for (k1, k2) in ((0, 1), (0, 3), (2, 3)):
        q1, q2 = sorted(final_rad).index(2 * k1), sorted(final_rad).index(2 * k2)
        joint = [[Fraction(0)] * 2 for _ in range(2)]
        for i in range(d):
            joint[(i >> q1) & 1][(i >> q2) & 1] += E_rho[i][i]
        p1 = [joint[0][0] + joint[0][1], joint[1][0] + joint[1][1]]
        p2 = [joint[0][0] + joint[1][0], joint[0][1] + joint[1][1]]
        for a in range(2):
            for bb in range(2):
                ok = ok and joint[a][bb] == p1[a] * p2[bb]
    g.check("[Prop 12.5] every inter-pair correlation is destroyed: the joint (R_k, R_l) distributions "
            "of E rho_R factorise exactly: the information rode what descent erased", ok)


def appendix_checks():
    # A.1: the PG metric from hbar^{-1}, blade-exact at rational beta
    beta = Fraction(3, 7)
    et, er = g.gen(0), g.gen(1)
    him = lambda a: g.add(a, g.scal(beta, g.scal(g.dotv(a, et, STA), er)))  # hbar^{-1}
    gmet = lambda a, b: g.dotv(him(a), him(b), STA)
    ok = gmet(et, et) == 1 - beta * beta and gmet(et, er) == -beta and gmet(er, er) == Fraction(-1)
    g.check("[App SA.1] the gauge field's metric is Painleve-Gullstrand: g = (1-b^2, -b; -b, -1) exactly", ok)
    # A.1: static-form substitution as an exact 2x2 congruence, FORMED in Q(r)[beta]:
    # G_PG = [[1 - beta^2, -beta], [-beta, -1]] on (dt_PG, dr); dt_PG = dt_s + (beta/f) dr, so with
    # T = [[1, beta/f], [0, 1]] (rows dt_PG, dr in terms of dt_s, dr) the static metric is T^t G_PG T.
    r = g.RF.var()
    M = MASS
    f = g.RF.const(1) - g.RF.const(2 * M) / r
    bb = BR.beta()
    one_b, zero_b = BR.const(1), BR.const(0)
    G_PG = [[one_b - bb * bb, -bb], [-bb, BR.const(-1)]]
    T = [[one_b, bb * BR.rf(g.RF1 / f)], [zero_b, one_b]]

    def bmm(A, B):
        return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]

    Tt = [[T[j][i] for j in range(2)] for i in range(2)]
    G_static = bmm(bmm(Tt, G_PG), T)
    want = [[BR.rf(f), zero_b], [zero_b, BR.rf(g.RF.const(-1) / f)]]
    ok = all(G_static[i][j].eqbr(want[i][j]) for i in range(2) for j in range(2))
    g.check("[App SA.1] cross-term elimination: T^t G_PG T = diag(f, -1/f) as an exact congruence computed in "
            "Q(r)[beta], beta^2 = 2M/r (the matrices are formed and multiplied)", ok)
    # A.2: curvature eigenvalues as RF identities
    fp = f.deriv()
    fpp = fp.deriv()
    twoM_r3 = g.RF.const(2 * M) / (r * r * r)
    M_r3 = g.RF.const(M) / (r * r * r)
    ok = (g.RF.const(0) - fpp / g.RF.const(2)).eqrf(twoM_r3)
    g.check("[App SA.2] radial-plane eigenvalue: -f''/2 = 2M/r^3 as an exact identity", ok)
    ok = (g.RF.const(0) - fp / (g.RF.const(2) * r)).eqrf(g.RF.const(0) - M_r3)
    g.check("[App SA.2] mixed-plane eigenvalue: -f'/(2r) = -M/r^3 as an exact identity", ok)
    ok = ((g.RF.const(1) - f) / (r * r)).eqrf(twoM_r3)
    g.check("[App SA.2] angular-plane eigenvalue: (1-f)/r^2 = 2M/r^3 as an exact identity", ok)
    lam_rad_d = g.RF.const(0) - fpp / g.RF.const(2)          # -f''/2, derived
    lam_ang_d = (g.RF.const(1) - f) / (r * r)                 # (1-f)/r^2, derived
    lam_mix_d = g.RF.const(0) - fp / (g.RF.const(2) * r)      # -f'/(2r), derived
    ok = lam_rad_d.eqrf(lam_ang_d) and (lam_rad_d / lam_mix_d).eqrf(g.RF.const(-2))
    g.check("[App SA.2] the radial and angular eigenvalues coincide and are -2 times the mixed one, "
            "each side derived from f by differentiation rather than copied: the doubled eigenvalue "
            "sits on the radial plane and its dual", ok)
    # A.2: the Cartan derivation itself, verified.  Parametrise by F = sqrt(f) (an indeterminate w):
    # r = 2M/(1 - w^2), so the static coframe theta^0 = w dt, theta^1 = (r'(w)/w) dw, theta^2 = r dtheta
    # and the connection forms are rational in w.  The exterior engine's variable slot "dr" is used
    # for dw; its coefficients are BR elements with vanishing beta-part (plain rational functions).
    w = g.RF.var()
    one = g.RF.const(1)
    r_w = g.RF.const(2 * M) / (one - w * w)
    rp = r_w.deriv()                                   # dr/dw
    fprime = g.RF.const(2 * M) / (r_w * r_w)           # f'(r) as a function of w
    fpp_w = g.RF.const(-4 * M) / (r_w * r_w * r_w)     # f''(r) as a function of w
    th0 = form1(dt=BR.rf(w))
    th1 = form1(dr=BR.rf(rp / w))
    th2 = form1(dth=BR.rf(r_w))
    # omega^0_1 = (f'/(2 sqrt f)) theta^0 = (f'/2) dt ; omega^2_1 = (sqrt f / r) theta^2 = w dtheta
    w01 = form1(dt=BR.rf(fprime / g.RF.const(2)))
    w21 = form1(dth=BR.rf(w))
    w10 = w01                                          # omega^1_0 = omega^0_1 (mixed signature)
    w12 = form1_scal(BR.const(-1), w21)
    # first structure equations: d theta^a = - omega^a_b ^ theta^b
    e0 = form2_sub(dform(th0), form2_sub(br_form_zero(), wedge(w01, th1)))
    e1 = form2_sub(dform(th1), form2_sub(br_form_zero(), wedge(w10, th0)))
    e2 = form2_sub(dform(th2), form2_sub(br_form_zero(), wedge(w21, th1)))
    g.check("[App SA.2] the static coframe's first structure equations hold on the theta^0, theta^1, theta^2 "
            "legs with the stated connection forms, as exact identities in F = sqrt f", form2_zero(e0) and form2_zero(e1) and form2_zero(e2))
    # second structure equations: R^0_1 = d omega^0_1 (omega^0_2 ^ omega^2_1 = 0 since omega^0_2 = 0),
    # R^0_2 = omega^0_1 ^ omega^1_2, R^1_2 = d omega^1_2; compare with the stated eigenvalue x plane
    R01 = dform(w01)
    R02 = wedge(w01, w12)
    R12 = dform(w12)
    want01 = form1_scal(BR.rf(g.RF.const(0) - fpp_w / g.RF.const(2)), {})   # placeholder, built below
    lam_rad = BR.rf(g.RF.const(0) - fpp_w / g.RF.const(2))                  # -f''/2
    lam_mix = BR.rf(g.RF.const(0) - fprime / (g.RF.const(2) * r_w))         # -f'/(2r)
    want01 = {k: lam_rad * v for k, v in wedge(th0, th1).items()}
    want02 = {k: lam_mix * v for k, v in wedge(th0, th2).items()}
    want12 = {k: lam_mix * v for k, v in wedge(th1, th2).items()}
    ok = form2_zero(form2_sub(R01, want01)) and form2_zero(form2_sub(R02, want02)) \
        and form2_zero(form2_sub(R12, want12))
    g.check("[App SA.2] the second structure equations give R^0_1 = (-f''/2) theta^0^theta^1, "
            "R^0_2 = (-f'/2r) theta^0^theta^2, R^1_2 = (-f'/2r) theta^1^theta^2, computed from the connection "
            "forms as exact identities in F = sqrt f (the f'^2/4f cancellation included)", ok)
    # negative control: perturb the one connection coefficient omega^0_1 by dt/r and both the first
    # structure equation on the theta^0 leg and the second's R^0_1 value fail
    w01_bad = form1(dt=BR.rf(fprime / g.RF.const(2) + one / r_w))
    e0_bad = form2_sub(dform(th0), form2_sub(br_form_zero(), wedge(w01_bad, th1)))
    R01_bad = dform(w01_bad)
    g.check("[App SA.2] negative control: one perturbed connection coefficient (omega^0_1 + dt/r) breaks "
            "both the first structure equation on the theta^0 leg and the second's R^0_1",
            (not form2_zero(e0_bad)) and (not form2_zero(form2_sub(R01_bad, want01))))
    # and the values: -f''/2 = 2M/r^3, -f'/(2r) = -M/r^3 in the w parametrisation
    ok = (g.RF.const(0) - fpp_w / g.RF.const(2)).eqrf(g.RF.const(2 * M) / (r_w * r_w * r_w)) \
        and (g.RF.const(0) - fprime / (g.RF.const(2) * r_w)).eqrf(g.RF.const(0) - g.RF.const(M) / (r_w * r_w * r_w))
    g.check("[App SA.2] those coefficients are 2M/r^3 and -M/r^3 with r = 2M/(1 - F^2)", ok)
    # A.3: kappa
    ok = fp.eval(2 * M) / 2 == 1 / (4 * M)
    g.check("[App SA.3] surface gravity: f'(2M)/2 = 1/4M exactly", ok)


def epoch_checks():
    # [Lem 10.4] the causal-epoch integral, exactly
    M = MASS
    R = 2 * M
    u = g.RF.var()
    one = g.RF.const(1)
    # (a) the geodesic integrand: E = 1 gives dt/dr = 1/(f sqrt(1 - f)); with r = 2M u^2,
    #     sqrt(1 - f) = sqrt(2M/r) = 1/u, |f| = 1/u^2 - 1 for r < 2M, dr = 4M u du, so the integrand
    #     in u is 4M u^4/(1 - u^2).  Check: (1/|f|) * u * 4M u  =  4M u^4/(1 - u^2)  as rational functions.
    absf_u = one / (u * u) - one                 # |f| = 1/u^2 - 1 inside the horizon (u < 1)
    lhs = (one / absf_u) * u * g.RF.const(4 * M) * u
    rhs = g.RF.const(4 * M) * (u * u * u * u) / (one - u * u)
    g.check("[Lem 10.4] the rain-geodesic integrand after r = 2M u^2: sqrt(r/2M) r/(2M - r) dr/du = "
            "4M u^4/(1 - u^2), exact rational functions", lhs.eqrf(rhs))
    # (b) partial fractions: u^4/(1 - u^2) = -u^2 - 1 + 1/(1 - u^2)
    pf = g.RF.const(0) - u * u - one + one / (one - u * u)
    g.check("[Lem 10.4] partial-fraction identity u^4/(1 - u^2) = -u^2 - 1 + 1/(1 - u^2), exact",
            ((u * u * u * u) / (one - u * u)).eqrf(pf))
    # (c) the antiderivative: d/du[-u^3/3 - u] = -u^2 - 1, and d/du[(1/2) ln((1+u)/(1-u))] = 1/(1 - u^2)
    poly = g.RF.const(0) - (u * u * u) / g.RF.const(3) - u
    logpart_deriv = g.RF.const(Fraction(1, 2)) * (one / (one + u) + one / (one - u))
    g.check("[Lem 10.4] antiderivative: (-u^3/3 - u)' = -u^2 - 1 and ((1/2) ln((1+u)/(1-u)))' = 1/(1-u^2), exact",
            poly.deriv().eqrf(g.RF.const(0) - u * u - one) and logpart_deriv.eqrf(one / (one - u * u)))
    # (d) the closed form against the integral, at the rational endpoint u0 = 999/1000
    #     (eps = 1 - u0^2 = 1999/10^6): Riemann sums of the increasing integrand bracket the integral.
    u0 = Fraction(999, 1000)
    eps = 1 - u0 * u0
    Nsub = 20000
    hstep = u0 / Nsub
    integrand = lambda x: 4 * M * x ** 4 / (1 - x * x)
    lower = sum(integrand(hstep * i) for i in range(Nsub)) * hstep
    upper = sum(integrand(hstep * (i + 1)) for i in range(1, Nsub + 1) if i < Nsub) * hstep + integrand(hstep) * hstep
    upper = sum(integrand(hstep * (i + 1)) for i in range(Nsub)) * hstep
    # closed form: 4M[(1/2) ln((1+u0)/(1-u0)) - u0 - u0^3/3], with the logarithm as a LogVec
    L = LogVec.ln_rat((1 + u0) / (1 - u0))
    closed_log = L * (2 * M)                       # 4M * (1/2) ln(...)
    closed_rat = 4 * M * (-u0 - u0 ** 3 / 3)
    lo, hi = logvec_bounds(closed_log)
    ok = lower <= lo + closed_rat and hi + closed_rat <= upper
    g.check("[Lem 10.4] closed form 4M[(1/2) ln((1+u)/(1-u)) - u - u^3/3] lies inside the exact Riemann "
            "bracket of the integral at eps = 1999/10^6 (20000 subintervals; ln bounded rationally)", ok)
    # the former closed form 2M(ln(1/eps) - 1 + eps) lies OUTSIDE the bracket: the check has teeth
    old_log = LogVec.ln_rat(1 / eps) * (2 * M)
    old_rat = 2 * M * (-1 + eps)
    olo, ohi = logvec_bounds(old_log)
    g.check("[Lem 10.4] control: the closed form 2M(ln(1/eps) - 1 + eps) of the un-square-rooted integrand "
            "lies outside the bracket (it is the wrong integral)",
            (ohi + old_rat < lower) or (olo + old_rat > upper))
    # (e) the expansion: 2M(ln(1/eps) - 8/3 + 2 ln 2) differs from the closed form by O(eps):
    #     |closed - expansion| <= 4M eps at this eps (a generous explicit bound)
    exp_log = LogVec.ln_rat(1 / eps) * (2 * M) + LogVec.ln_int(2) * (4 * M)
    exp_rat = 2 * M * Fraction(-8, 3)
    diff = closed_log - exp_log
    dlo, dhi = logvec_bounds(diff)
    dlo, dhi = dlo + closed_rat - exp_rat, dhi + closed_rat - exp_rat
    g.check("[Lem 10.4] expansion: |closed form - 2M(ln(1/eps) - 8/3 + 2 ln 2)| <= 4M eps at eps = 1999/10^6",
            -4 * M * eps <= dlo and dhi <= 4 * M * eps)


def hardening_checks():
    # Step 4e hardening: edge-operator identity [a_m, a_-m] = B_m - T_m on a batch incl. edge states
    sea = frozenset(k for k in SITES if k < 0)
    Kw = 4
    def numop(sites_list, st):
        out = {}
        for occ, amp in st.items():
            cnt = sum(1 for j in sites_list if j in occ)
            if cnt:
                out[occ] = out.get(occ, Fraction(0)) + cnt * amp
        return out
    batch = [
        {sea: Fraction(1)},
        {frozenset((sea - {-1}) | {0}): Fraction(1)},
        {frozenset((sea - {-4}) | {3}): Fraction(1)},          # edge-excited
        {frozenset((sea - {-4, -1}) | {2, 3}): Fraction(1)},   # doubly edge-excited
    ]
    ok = True
    for m in (1, 2):
        bottom = list(range(-Kw, -Kw + m))
        top = list(range(Kw - m, Kw))
        for st in batch:
            lhs = sub_state(current(m, current(-m, dict(st))), current(-m, current(m, dict(st))))
            rhs = sub_state(numop(bottom, dict(st)), numop(top, dict(st)))
            ok = ok and st_eq(lhs, rhs)
    g.check("[Thm 8.2] exact edge-operator identity [a_m, a_-m] = B_m - T_m on sea, bulk AND edge-excited "
            "states (m = 1, 2)", ok)
    # detailed balance pointwise identities and the re-indexing, exact
    x = Fraction(1, 2)
    def n(k):
        return x ** k / (1 + x ** k) if k >= 0 else 1 / (1 + x ** (-k))
    ok = True
    for m in (1, 3):
        for k in (-5, -1, 0, 4):
            gk = n(k + m) * (1 - n(k))
            hk = n(k) * (1 - n(k + m))
            ok = ok and hk == x ** (-m) * gk and gk - hk == n(k + m) - n(k)
    g.check("[Thm 8.2] detailed balance h = x^{-m} g and difference identity g - h = n_{k+m} - n_k, "
            "pointwise exact", ok)
    ok = True
    for m in (1, 2):
        K = 12
        lhs = sum(n(k + m) - n(k) for k in range(-K, K + 1))
        rhs = sum(n(j) for j in range(K + 1, K + m + 1)) - sum(n(j) for j in range(-K, -K + m))
        ok = ok and lhs == rhs
    g.check("[Thm 8.2] telescoping re-indexing of the partial sums, exact at finite K", ok)
    # model correlator numeric signatures
    c1, s1 = MODEL_PAIRS[0]
    c2, s2 = MODEL_PAIRS[1]
    gamma = c2 * c2 - s2 * s2
    ok = 2 * c1 * s1 == Fraction(24, 25) and 2 * c1 * s1 * gamma == Fraction(168, 625)
    g.check("[Prop 12.3] printed decoding signatures: (24/25, 168/625) vs (168/625, 24/25), exact", ok)


def lift_checks():
    """[Def 5.1, Prop 5.2] The point-level transport, instantiated.

    Coordinates on the completion: N = s n0 + x + t ninf, written (s, x, t).
    Incidence:  Q(x) = 2 s t.      Lift:  X(x) = (1, x, Q(x)/2).
    Transported reciprocal: iota(s, x, t) = (2t, x, s/2).
    Read-out: dsc(s, x, t) = x/s, undefined when s = 0.

    Parts L1 to L5 carry the vector slot: x is an actual tangent vector with
    generic rational orthonormal components, X(x) is a Cl(2,4) multivector
    (n0 = e+ + e-, ninf = (e- - e+)/2, n0.ninf = -1), incidence is checked
    both as the coordinate identity Q = 2st on the extracted slots
    (s = -N.ninf, t = -N.n0) and as the blade-exact nullity X^2 = 0, and
    iota is the slot map applied to the extracted components, with negative
    controls.  L6 and L11 to L14 are identities in Q(r) for the Schwarzschild
    fibre, f = 1 - 2M/r = (r - 2M)/r; L7 to L9 run with the vector
    represented, at the rational-orthonormal radius r = 4 (f = 1/4, M = 3/2),
    with a perturbed non-null control.
    """
    # ---- L1 to L5: the vector slot represented, blade-exactly in Cl(2,4) ----
    sq6 = (1, -1, -1, -1, 1, -1)      # e0..e3 of Cl(1,3), then e+^2 = +1, e-^2 = -1
    e6 = [g.gen(i) for i in range(6)]
    n0 = g.add(e6[4], e6[5])
    ninf = g.scal(Fraction(1, 2), g.sub(e6[5], e6[4]))       # n0.ninf = -1

    def slots(N):
        # extract (s, x, t) from N = s n0 + x + t ninf: N.ninf = -s, N.n0 = -t
        s = -g.dotv(N, ninf, sq6)
        tt = -g.dotv(N, n0, sq6)
        x = g.sub(N, g.add(g.scal(s, n0), g.scal(tt, ninf)))
        return s, x, tt

    def assemble(s, x, tt):
        return g.add(g.scal(s, n0), x, g.scal(tt, ninf))

    def iota(N):
        s, x, tt = slots(N)
        return assemble(2 * tt, x, Fraction(s, 2))

    def vec4(a0, a1, a2, a3):
        return g.add(g.scal(a0, e6[0]), g.scal(a1, e6[1]), g.scal(a2, e6[2]), g.scal(a3, e6[3]))

    def lift(x):
        Q = g.dotv(x, x, sq6)
        return g.add(n0, x, g.scal(Q / 2, ninf)), Q

    samples = [vec4(Fraction(3, 2), Fraction(2, 5), Fraction(-1, 3), Fraction(7, 4)),
               vec4(Fraction(1, 7), Fraction(5, 2), Fraction(4, 9), Fraction(-2, 3))]

    ok = True
    for x in samples:
        X, Q = lift(x)
        s, xv, tt = slots(X)
        ok = ok and Q != 0 and (s, tt) == (Fraction(1), Q / 2) and g.eq(xv, x) \
            and Q == 2 * s * tt and g.is_zero(g.mul(X, X, sq6))
        Xbad = g.add(n0, x, g.scal(Q, ninf))                 # wrong coefficient: Q, not Q/2
        ok = ok and g.eq(g.mul(Xbad, Xbad, sq6), g.sc(-Q))
    g.check("[Prop 5.2](1) L1: the lift satisfies incidence with the vector slot represented: slots "
            "(1, x, Q/2) extracted from the multivector, Q = 2st, and X(x)^2 = 0 blade-exactly, on "
            "generic rational tangent vectors; the wrong-coefficient lift squares to -Q, not 0", ok)

    ok = True
    for x in samples:
        X, Q = lift(x)
        s_i, x_i, t_i = slots(iota(X))
        ok = ok and s_i == Q and t_i == Fraction(1, 2) and g.eq(x_i, x)
    g.check("[Prop 5.2](1) L2: iota(X(x)) = (Q(x), x, 1/2), slots and vector part read off the "
            "computed multivector", ok)

    N_gen = assemble(Fraction(3, 4), samples[0], Fraction(-2, 7))    # NOT incident: Q != 2st
    sg, xg, tg = slots(N_gen)
    ok = g.dotv(xg, xg, sq6) != 2 * sg * tg \
        and g.eq(g.mul(iota(N_gen), iota(N_gen), sq6), g.mul(N_gen, N_gen, sq6))
    for x in samples:
        X, Q = lift(x)
        ok = ok and g.is_zero(g.mul(iota(X), iota(X), sq6))
    g.check("[Prop 5.2](1) L3: iota preserves the quadric value of an arbitrary six-component vector "
            "(a non-incident control included), hence preserves incidence: iota(X)^2 = 0 blade-exactly", ok)

    ok = g.eq(iota(iota(N_gen)), N_gen)
    for x in samples:
        X, _ = lift(x)
        ok = ok and g.eq(iota(iota(X)), X)
    g.check("[Prop 5.2](1) L4: iota is an involution, on the lifts and on a generic six-component "
            "vector alike", ok)

    ok = True
    for x in samples:
        X, Q = lift(x)
        s_i, x_i, _ = slots(iota(X))
        ok = ok and g.eq(g.scal(Fraction(1, 1) / s_i, x_i), g.scal(Fraction(1, 1) / Q, x))
    g.check("[Prop 5.2](2) L5: dsc(iota(X(x))) = x/Q(x) componentwise on the represented vector: "
            "the classical reciprocal recovered", ok)
    one = g.RF.const(1)

    # ---- L6 to L14: the Schwarzschild fibre, exact in Q(r) ----
    r = g.RF.var()
    twoM = g.RF.const(2 * MASS)
    f = (r - twoM) / r                       # f = 1 - 2M/r
    finv = one / f

    # static-chart fibre metric diag(f, -1/f, -r^2, -r^2 sin^2 th); the (t, r)
    # block is all that the radial null direction and the Killing direction use.
    def Q_tr(a, b):                          # a e_t + b e_r
        return f * a * a - finv * b * b

    # L6: the radial null direction x = e_t + f e_r is null in the fibre
    g.check("[Prop 5.2](3) L6: Q(e_t + f e_r) = 0 exactly in Q(r): the radial null direction",
            Q_tr(one, f).eqrf(g.RF.const(0)))

    # L7 to L10: the radial null direction with the vector represented, at r = 4 (f = 1/4,
    # M = 3/2), where the static orthonormal frame has exact rational components: the
    # coordinate vector e_t + f e_r has orthonormal components (sqrt(f), f/sqrt(f)) = (1/2, 1/2).
    x_null = vec4(Fraction(1, 2), Fraction(1, 2), Fraction(0), Fraction(0))
    X_null, Q_null = lift(x_null)
    _, _, t_null = slots(X_null)
    g.check("[Prop 5.2](3) L7: the lift of the null direction is (1, x, 0): Q = 0 blade-exactly and "
            "the last slot vanishes, vector represented at r = 4", Q_null == 0 and t_null == 0
            and g.is_zero(g.mul(X_null, X_null, sq6)))

    iX_null = iota(X_null)
    s_null, x_slot, t_slot = slots(iX_null)
    x_pert = vec4(Fraction(9, 14), Fraction(1, 2), Fraction(0), Fraction(0))   # non-null control
    X_pert, Q_pert = lift(x_pert)
    s_pert, _, _ = slots(iota(X_pert))
    g.check("[Prop 5.2](3) L8: iota of the lifted null direction has first slot 0 (ideal point); a "
            "perturbed non-null direction has first slot Q != 0 and descends",
            s_null == 0 and Q_pert != 0 and s_pert == Q_pert)

    # the target is hand-expanded in the raw generator basis, independent of the ninf and assemble
    # constructions: x + (1/2) ninf = (1/2) e0 + (1/2) e1 - (1/4) e4 + (1/4) e5
    target = {(0,): Fraction(1, 2), (1,): Fraction(1, 2), (4,): Fraction(-1, 4), (5,): Fraction(1, 4)}
    g.check("[Prop 5.2](3) L9: the ideal value is exactly [x + (1/2) ninf], compared blade by blade "
            "against the hand-expanded target (1/2)e0 + (1/2)e1 - (1/4)e4 + (1/4)e5", g.eq(iX_null, target))

    undefined = False
    try:
        _ = Fraction(1, 1) / s_null
    except ZeroDivisionError:
        undefined = True
    s_p, x_p, _ = slots(iota(X_pert))
    dsc_ok = g.eq(g.scal(Fraction(1, 1) / s_p, x_p), g.scal(Fraction(1, 1) / Q_pert, x_pert))
    g.check("[Prop 5.2](3) L10: dsc is undefined on the ideal point (division by the vanishing first "
            "slot raises exactly) and returns exactly x/Q on the perturbed non-null control",
            undefined and dsc_ok)

    # L11: the Killing-time direction has fibre norm f; its covector dt_s has static dual norm 1/f,
    #      which has a POLE at the horizon: evaluating it at r = 2M divides by zero (probed), so dt_s is
    #      not a regular generator of the radical off E (T04 Thm 8.7(4))
    pole = False
    try:
        _ = finv.eval(2 * MASS)
    except ZeroDivisionError:
        pole = True
    g.check("[Prop 5.2](4) L11: Q(e_t) = f exactly, and the static dual norm 1/f of dt_s has a pole at r = 2M "
            "(division by zero on evaluation)", Q_tr(one, g.RF.const(0)).eqrf(f) and pole)

    # L12: the radical generator k = sqrt(2M) dt_s + (sqrt r / f) dr of T04 Thm 8.7 has dual norm
    #      Q*(k) = 2M g^{tt} + (r/f^2) g^{rr} = 2M/f - r/f = -r, an identity of rational functions
    #      (the components enter squared, so no square roots appear)
    Qk = twoM * finv + (r / (f * f)) * (g.RF.const(0) - f)
    g.check("[Prop 5.2](4) L12: the dual norm of the radical generator k is Q*(k) = 2M/f - r/f = -r exactly, "
            "no pole at the horizon", Qk.eqrf(g.RF.const(0) - r))

    # L13: the same value from T04 Thm 8.7's Painleve-Gullstrand Gram, built as a matrix over Q(r) on the
    #      frame (rho, dt_PG, mu_1, mu_2) and contracted with the vector k = (1, m, 0, 0): k^T G k = -r.
    #      A control vector (dt_PG alone) gives +1, and the determinant is -r (T04 Thm 8.7(1)).
    ok = True
    for m in (Fraction(1), Fraction(2), Fraction(7, 3)):
        m2 = g.RF.const(m * m)
        mc = g.RF.const(m)
        G = [[m2 - r, g.RF.const(0) - mc, g.RF.const(0), g.RF.const(0)],
             [g.RF.const(0) - mc, g.RF.const(1), g.RF.const(0), g.RF.const(0)],
             [g.RF.const(0), g.RF.const(0), g.RF.const(-1), g.RF.const(0)],
             [g.RF.const(0), g.RF.const(0), g.RF.const(0), g.RF.const(-1)]]
        kvec = [g.RF.const(1), mc, g.RF.const(0), g.RF.const(0)]
        quad = lambda v: sum((v[i] * G[i][j] * v[j] for i in range(4) for j in range(4)), g.RF.const(0))
        mixed = [g.RF.const(1), g.RF.const(0) - mc, g.RF.const(0), g.RF.const(0)]   # rho - m dt_PG
        Gk = [sum((G[i][j] * kvec[j] for j in range(4)), g.RF.const(0)) for i in range(4)]
        ok = ok and quad(kvec).eqrf(g.RF.const(0) - r) \
            and quad(mixed).eqrf(g.RF.const(4) * mc * mc - r) \
            and g.rf_mat_det(G).eqrf(g.RF.const(0) - r) \
            and Gk[0].eqrf(g.RF.const(0) - r) and Gk[1].eqrf(g.RF.const(0)) \
            and Gk[2].eqrf(g.RF.const(0)) and Gk[3].eqrf(g.RF.const(0))
    g.check("[Prop 5.2](4) L13: T04's Painleve-Gullstrand Gram G built over Q(r): k^T G k = -r for k = rho + m dt_PG "
            "(three values of m), the mixed vector rho - m dt_PG contracting to 4m^2 - r as a multi-entry "
            "control, det G = -r; and the dual through the Gram, Gk = (-r, 0, 0, 0): the PG-time component of "
            "k-sharp vanishes identically and k-sharp is radial, closing the Step 1 junction in the PG frame", ok)

    # L14: the value is rebuilt POINTWISE from the two unreduced terms 2M/f and -r/f, each singular at
    #      the horizon separately, so no pre-reduced literal is evaluated (RF arithmetic is gcd-reducing,
    #      so Qk itself already stores -r; L12 is where that reduction IS the claim).  Off the horizon the
    #      two-term sum is -r; at the horizon each term diverges and the value -2M is certified by L12's
    #      identity, whose content is exactly the cancellation; at r = 0 the reduced value is 0.
    ok = True
    for rr in (Fraction(1, 2) * MASS, 3 * MASS, 10 * MASS, Fraction(1, 1000)):
        fval = (rr - 2 * MASS) / rr
        ok = ok and (2 * MASS / fval - rr / fval == -rr)
    horizon_terms_singular = 0
    for term in (twoM * finv, (r / (f * f)) * (g.RF.const(0) - f)):
        try:
            term.eval(2 * MASS)
        except ZeroDivisionError:
            horizon_terms_singular += 1
    ok = ok and horizon_terms_singular == 2 and Qk.eval(2 * MASS) == -2 * MASS \
        and Qk.eval(Fraction(0)) == 0
    g.check("[Prop 5.2](4) L14: Q*(k) rebuilt pointwise from the unreduced terms 2M/f and -r/f equals -r at "
            "r = M/2, 3M, 10M and 1/1000; at the horizon BOTH term evaluations raise ZeroDivisionError "
            "(each term executed and singular separately) and the value -2M comes from L12's "
            "rational-function identity (the cancellation is that identity's content); at r = 0 the value "
            "is 0: the read-out fails on E and nowhere else", ok)


# ---------------------------------------------------------------------------
# STATE SELECTION (Section 7.2, added with v1.4): the descent as the parity
# average, the state-independence of the descended form, univalence, KMS
# uniqueness and rate rigidity, the Euclidean partner, over-determination,
# the canonical purification, and number-diagonal ledger dynamics.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# exact matrix helpers over Q
# ---------------------------------------------------------------------------

def F(a, b=1):
    return Fraction(a, b)


def zeros(n, m=None):
    m = n if m is None else m
    return [[F(0)] * m for _ in range(n)]


def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = F(1)
    return M


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if a == 0:
                continue
            Bt = B[t]
            for j in range(m):
                C[i][j] += a * Bt[j]
    return C


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscal(c, A):
    c = Fraction(c)
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mtr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def diag(*vals):
    n = len(vals)
    M = zeros(n)
    for i in range(n):
        M[i][i] = Fraction(vals[i])
    return M


def kron(A, B):
    na, ma, nb, mb = len(A), len(A[0]), len(B), len(B[0])
    C = zeros(na * nb, ma * mb)
    for i in range(na):
        for j in range(ma):
            a = A[i][j]
            if a == 0:
                continue
            for p in range(nb):
                for q in range(mb):
                    C[i * nb + p][j * mb + q] = a * B[p][q]
    return C


def is_diagonal(A):
    return all(A[i][j] == 0 for i in range(len(A)) for j in range(len(A[0])) if i != j)


# ---------------------------------------------------------------------------
# n-qubit engine: basis index b encodes occupations (b >> (n-1-k)) & 1
# ---------------------------------------------------------------------------

def bit(b, k, n):
    return (b >> (n - 1 - k)) & 1


def popcount(b):
    return bin(b).count("1")


def ket(n, amps):
    """amps: dict {basis index: Fraction}.  Returns the density matrix."""
    D = 2 ** n
    rho = zeros(D)
    for i, ai in amps.items():
        for j, aj in amps.items():
            rho[i][j] += Fraction(ai) * Fraction(aj)
    return rho


def parity_op(n):
    D = 2 ** n
    return diag(*[F((-1) ** popcount(b)) for b in range(D)])


def ss_marginal(rho, k, n):
    """Single-mode marginal of mode k (2 x 2), by partial trace over the rest."""
    D = 2 ** n
    out = zeros(2)
    for b in range(D):
        for c in range(D):
            # b and c must agree off mode k
            agree = all(bit(b, t, n) == bit(c, t, n) for t in range(n) if t != k)
            if agree:
                out[bit(b, k, n)][bit(c, k, n)] += rho[b][c]
    return out


def dephase_joint(rho):
    """E_N: complete dephasing in the joint number basis."""
    D = len(rho)
    out = zeros(D)
    for b in range(D):
        out[b][b] = rho[b][b]
    return out


def dephase_mode(rho, k, n):
    """E_k: dephasing of mode k only (kills matrix elements differing in bit k)."""
    D = 2 ** n
    out = zeros(D)
    for b in range(D):
        for c in range(D):
            if bit(b, k, n) == bit(c, k, n):
                out[b][c] = rho[b][c]
    return out


def cz(n, j, k):
    """Controlled-Z between modes j and k: diagonal, entries +-1."""
    D = 2 ** n
    return diag(*[F(-1) if (bit(b, j, n) and bit(b, k, n)) else F(1) for b in range(D)])


def beam_splitter(n, j, k, c, s):
    """Real hopping rotation exp(theta (v_j* v_k - v_k* v_j)) on modes j, k,
    with (cos, sin) = (c, s): the generator (L_E) does not supply."""
    D = 2 ** n
    U = zeros(D)
    c, s = Fraction(c), Fraction(s)
    for b in range(D):
        bj, bk = bit(b, j, n), bit(b, k, n)
        if bj == bk:
            U[b][b] = F(1)
            continue
        # the two-dimensional block spanned by |1_j 0_k> and |0_j 1_k>
        flipped = b ^ (1 << (n - 1 - j)) ^ (1 << (n - 1 - k))
        if bj == 1:
            U[b][b] = c
            U[flipped][b] = s
        else:
            U[b][b] = c
            U[flipped][b] = -s
    return U


def conj(U, rho):
    Ut = [[U[j][i] for j in range(len(U))] for i in range(len(U))]
    return mm(mm(U, rho), Ut)


# ---------------------------------------------------------------------------
# the single mode: matrix units, the descent, the parity automorphism
# ---------------------------------------------------------------------------

V = [[F(0), F(1)], [F(0), F(0)]]        # v   = E_12  (lowering: |1> -> |0>)
VS = [[F(0), F(0)], [F(1), F(0)]]       # v*  = E_21
P_OCC = mm(VS, V)                       # P = v* v = E_22
SIGMA = madd(mscal(2, P_OCC), mscal(-1, eye(2)))   # sigma = 2P - 1 = diag(-1, 1)
K_GEN = mscal(Fraction(1, 2), SIGMA)    # K = sigma/2 = N - 1/2


def descent(x):
    """E(x) = P x P + (1-P) x (1-P), the map of T5 Prop 5.5."""
    Q = madd(eye(2), mscal(-1, P_OCC))
    return madd(mm(mm(P_OCC, x), P_OCC), mm(mm(Q, x), Q))


def parity_avg(x):
    return mscal(Fraction(1, 2), madd(x, mm(mm(SIGMA, x), SIGMA)))


GENERIC = [[F(2, 3), F(5, 7)], [F(-3, 11), F(4, 9)]]


# ---------------------------------------------------------------------------
# [Thm 5.7] the descent is the parity average
# ---------------------------------------------------------------------------

def ss_parity_checks():
    g.check("[Thm 5.7] E(x) = (x + sigma x sigma)/2 on a generic rational matrix",
            meq(descent(GENERIC), parity_avg(GENERIC)))

    g.check("[Thm 5.7] E is idempotent",
            meq(descent(descent(GENERIC)), descent(GENERIC)))

    # conditional-expectation property for even a, b (diagonal = even)
    a = diag(F(3, 5), F(-2, 7))
    b = diag(F(4, 9), F(11, 13))
    lhs = descent(mm(mm(a, GENERIC), b))
    rhs = mm(mm(a, descent(GENERIC)), b)
    g.check("[Thm 5.7] E(a x b) = a E(x) b for even a, b (conditional expectation)",
            meq(lhs, rhs))

    g.check("[Thm 5.7] range of E is the even span: E(1) = 1 and E(sigma) = sigma",
            meq(descent(eye(2)), eye(2)) and meq(descent(SIGMA), SIGMA))

    g.check("[Thm 5.7] kernel of E is the odd span: E(v) = E(v*) = 0, and E kills "
            "exactly the off-diagonal part",
            meq(descent(V), zeros(2)) and meq(descent(VS), zeros(2))
            and meq(descent(GENERIC), diag(GENERIC[0][0], GENERIC[1][1])))

    # the atom, in the blade engine: CAR and sigma = e0 e1
    sq = g.sig(1, 1)
    e0, e1 = g.gen(0), g.gen(1)
    v = g.scal(Fraction(1, 2), g.add(e0, e1))
    vs = g.scal(Fraction(1, 2), g.sub(e0, e1))
    car = g.add(g.mul(v, vs, sq), g.mul(vs, v, sq))
    sigma_blade = g.sub(g.mul(vs, v, sq), g.mul(v, vs, sq))
    g.check("[Thm 5.7] the hyperbolic atom: v^2 = (v*)^2 = 0, v v* + v* v = 1, "
            "and sigma = v* v - v v* = e0 e1 blade-exactly",
            g.is_zero(g.mul(v, v, sq)) and g.is_zero(g.mul(vs, vs, sq))
            and g.eq(car, g.sc(1))
            and g.eq(sigma_blade, g.mul(e0, e1, sq)))


# ---------------------------------------------------------------------------
# [Thm 7.6] the descended form is state independent
# ---------------------------------------------------------------------------

def ss_form_checks():
    # a generic rational density matrix with nonzero coherences
    rho = [[F(9, 25), F(6, 25)], [F(6, 25), F(16, 25)]]
    g.check("[Thm 7.6] E(rho) is diagonal for a state with nonzero coherences",
            is_diagonal(descent(rho)) and mtr(descent(rho)) == 1)

    # E(rho) = diag(1, x)/(1+x) with x = (1-p)/p, p the vacancy probability
    p = descent(rho)[0][0]
    x = (1 - p) / p
    gibbs = mscal(Fraction(1, 1) / (1 + x), diag(F(1), x))
    g.check("[Thm 7.6] E(rho) = diag(1, x)/(1+x) exactly, with x = e^{-beta omega} "
            "= (1-p)/p = 16/9",
            meq(descent(rho), gibbs) and x == F(16, 9))

    # injectivity of x -> p on a rational witness pair
    def pofx(xx):
        return Fraction(1, 1) / (1 + xx)
    g.check("[Thm 7.6] x -> p = 1/(1+x) is injective (rational witnesses 16/9, 9/16)",
            pofx(F(16, 9)) != pofx(F(9, 16)))


# ---------------------------------------------------------------------------
# [Thm 7.10] univalence: even states have diagonal marginals
# ---------------------------------------------------------------------------

def ss_univalence_checks():
    n = 3
    # an even pure state: every configuration has even total occupation
    psi = {0b000: F(1, 2), 0b011: F(1, 2), 0b101: F(1, 2), 0b110: F(1, 2)}
    rho_even = ket(n, psi)
    # a second even pure state, mixed in with rational weights
    chi = {0b000: F(3, 5), 0b110: F(4, 5)}
    rho_even = madd(mscal(F(1, 2), rho_even), mscal(F(1, 2), ket(n, chi)))

    Gam = parity_op(n)
    g.check("[Thm 7.10] the constructed three-mode state is even: Gamma rho Gamma = rho",
            meq(mm(mm(Gam, rho_even), Gam), rho_even) and mtr(rho_even) == 1)

    ok = all(is_diagonal(ss_marginal(rho_even, k, n)) for k in range(n))
    g.check("[Thm 7.10] every single-mode marginal of an even state is diagonal "
            "(all three modes)", ok)

    # omega(v_k) = 0 for every k: v_k's expectation is the ss_marginal coherence
    ok = all(ss_marginal(rho_even, k, n)[0][1] == 0 and ss_marginal(rho_even, k, n)[1][0] == 0
             for k in range(n))
    g.check("[Thm 7.10] omega(v_k) = omega(v_k*) = 0 for every mode of an even state", ok)

    # control: a parity-mixed state has a nonzero ss_marginal coherence
    phi = {0b000: F(3, 5), 0b001: F(4, 5)}
    rho_odd = ket(n, phi)
    g.check("[Thm 7.10] control: the parity-mixed state (3/5)|000> + (4/5)|001> has "
            "marginal coherence 12/25 on mode 3, so the premise does work",
            ss_marginal(rho_odd, 2, n)[0][1] == F(12, 25)
            and not meq(mm(mm(parity_op(n), rho_odd), parity_op(n)), rho_odd))

    # the model's pair states (T5 Sec 12): support constraint R_k = L_k
    n4 = 4
    c1, s1, c2, s2 = F(3, 5), F(4, 5), F(4, 5), F(3, 5)
    model = {0b0000: c1 * c2, 0b0011: c1 * s2, 0b1100: s1 * c2, 0b1111: -s1 * s2}
    rho_model = ket(n4, model)
    g.check("[Thm 7.10] the finite-mode model's two-pair state (with the CZ sign) is "
            "even, so Lem 12.1 is the special case",
            meq(mm(mm(parity_op(n4), rho_model), parity_op(n4)), rho_model)
            and mtr(rho_model) == 1
            and all(is_diagonal(ss_marginal(rho_model, k, n4)) for k in range(n4)))


# ---------------------------------------------------------------------------
# [Thm 7.13] KMS uniqueness
# ---------------------------------------------------------------------------

def ss_kms_checks():
    units = [[[F(1) if (i, j) == (a, b) else F(0) for j in range(2)] for i in range(2)]
             for a in range(2) for b in range(2)]

    # both signs of beta: x = e^{-beta omega} = 9/16 (physical, beta > 0) and 16/9 (population-
    # inverted, beta < 0); the identity is checked at each, the remaining checks use x = 16/9.
    ok = True
    for x in (F(9, 16), F(16, 9)):
        rho = mscal(Fraction(1, 1) / (1 + x), diag(F(1), x))
        Eb = diag(F(1), x)            # e^{-beta H}, H = omega N, x = e^{-beta omega}
        Ebi = diag(F(1), 1 / x)       # e^{+beta H}
        # alpha_{i beta}(a) = e^{-beta H} a e^{+beta H}
        for A in units:
            for B in units:
                lhs = mtr(mm(rho, mm(A, B)))
                rhs = mtr(mm(rho, mm(B, mm(Eb, mm(A, Ebi)))))
                ok = ok and lhs == rhs
    g.check("[Thm 7.13] the KMS identity omega(ab) = omega(b e^{-betaH} a e^{betaH}) on "
            "all sixteen matrix-unit pairs for rho ~ diag(1, x), at the physical point x = 9/16 "
            "and at the population-inverted point x = 16/9", ok)

    x = F(16, 9)                      # x = e^{-beta omega}, population-inverted sample
    rho = mscal(Fraction(1, 1) / (1 + x), diag(F(1), x))
    Eb = diag(F(1), x)
    Ebi = diag(F(1), 1 / x)

    # a non-Gibbs diagonal state fails it: exhibit a failing pair
    bad = diag(F(1, 2), F(1, 2))
    fails = False
    for A in units:
        for B in units:
            lhs = mtr(mm(bad, mm(A, B)))
            rhs = mtr(mm(bad, mm(B, mm(Eb, mm(A, Ebi)))))
            if lhs != rhs:
                fails = True
    g.check("[Thm 7.13] converse: the tracial state is not KMS for this flow "
            "(an explicit matrix-unit pair fails)", fails)

    g.check("[Thm 7.13] the identity forces [rho, e^{beta H}] = 0 and rho e^{beta H} "
            "central: rho = diag(1, x)/(1+x) commutes with e^{beta H}",
            meq(mm(rho, Eb), mm(Eb, rho)))


# ---------------------------------------------------------------------------
# [Cor 7.15] universality of the temperature
# ---------------------------------------------------------------------------

def ss_universality_checks():
    # weights w1 = 1, w2 = 2; equal beta means x2 = x1^{w2/w1} = x1^2
    x1 = F(2, 3)
    x2_equal = x1 * x1
    x2_other = F(1, 2)

    def two_mode_product(xa, xb):
        ra = mscal(Fraction(1, 1) / (1 + xa), diag(F(1), xa))
        rb = mscal(Fraction(1, 1) / (1 + xb), diag(F(1), xb))
        return ra, rb, kron(ra, rb)

    ra, rb, rho_eq = two_mode_product(x1, x2_equal)
    g.check("[Cor 7.15] equal inverse temperatures: x2 = x1^{w2/w1} = 4/9 exactly, so "
            "the joint populations are those of a single Gibbs state of K_geo",
            x2_equal == F(4, 9)
            and rho_eq[0b11][0b11] / rho_eq[0b00][0b00] == x1 * x2_equal)

    # the (G) condition read off the CONSTRUCTED joint populations: with weights (1, 2) a Gibbs
    # state of K_geo has p01/p00 = (p10/p00)^2.  It holds for rho_eq and fails for rho_ne.
    def gmc_pops(rho):
        p00, p10, p01 = rho[0b00][0b00], rho[0b10][0b10], rho[0b01][0b01]
        return p01 / p00 == (p10 / p00) ** 2
    _, _, rho_ne = two_mode_product(x1, x2_other)
    g.check("[Cor 7.15] witness failure, read off the constructed matrix: with x2 = 1/2 the joint "
            "populations of rho_ne violate p01/p00 = (p10/p00)^2, so they are not those of any "
            "single Gibbs state of K_geo, while rho_eq satisfies it",
            gmc_pops(rho_eq) and not gmc_pops(rho_ne))

    # the GMC state built INDEPENDENTLY from the K_geo spectrum: diagonal entries y^(w1 n1 + w2 n2)
    # with y = x1 and weights (1, 2), normalised; compare with the product of the marginals.
    y = x1
    diag_gmc = [y ** ((b >> 1 & 1) * 1 + (b & 1) * 2) for b in range(4)]
    Z = sum(diag_gmc)
    rho_gmc = diag(*[d / Z for d in diag_gmc])
    g.check("[Cor 7.15] the GMC state factorises: e^{-beta K_geo}, built from the K_geo spectrum "
            "with weights (1, 2), equals rho_1 (x) rho_2 exactly", meq(rho_gmc, kron(ra, rb)))


# ---------------------------------------------------------------------------
# [Thm 7.16] rate rigidity
# ---------------------------------------------------------------------------

def ss_rigidity_checks():
    # both signs of beta are exercised: x = e^{-beta omega} = 9/16 (physical, beta > 0) and 16/9
    # (population-inverted, beta < 0); every check below is run at both and the results conjoined.
    xs = (F(9, 16), F(16, 9))

    def gibbs(x_):
        return mscal(Fraction(1, 1) / (1 + x_), diag(F(1), x_))

    U_diag = diag(F(1), F(-1))
    g.check("[Thm 7.16](1) a diagonal unitary commutes with K and fixes the Gibbs "
            "state exactly (at x = 9/16 and at x = 16/9)",
            meq(mm(U_diag, K_GEN), mm(K_GEN, U_diag))
            and all(meq(conj(U_diag, gibbs(x_)), gibbs(x_)) for x_ in xs))

    X = [[F(0), F(1)], [F(1), F(0)]]
    g.check("[Thm 7.16](2) the exchange unitary reverses the flow (X K X = -K) and "
            "sends the beta-Gibbs state to the (-beta)-Gibbs state (x = 9/16 <-> 16/9, both ways)",
            meq(conj(X, K_GEN), mscal(-1, K_GEN))
            and all(meq(conj(X, gibbs(x_)), gibbs(1 / x_)) for x_ in xs))

    g.check("[Thm 7.16](4) the exchange does not commute with K, so it is not in the "
            "flow-preserving group: |beta| is the invariant",
            not meq(mm(X, K_GEN), mm(K_GEN, X)))

    # (3) reparametrisation: the same state is KMS at beta for K and at beta/2 for 2K, not at beta for 2K
    units = [[[F(1) if (i, j) == (a, b) else F(0) for j in range(2)] for i in range(2)]
             for a in range(2) for b in range(2)]

    def kms_holds(rho_, Eb_):
        Ebi_ = diag(1 / Eb_[0][0], 1 / Eb_[1][1])
        return all(mtr(mm(rho_, mm(A, B))) == mtr(mm(rho_, mm(B, mm(Eb_, mm(A, Ebi_)))))
                   for A in units for B in units)
    # with H = omega N and x = e^{-beta omega}: e^{-beta H} = diag(1, x); for the flow of 2H at beta/2
    # the same matrix diag(1, x) appears; at beta for 2H it is diag(1, x^2)
    # exponent bookkeeping made explicit rather than executing one identity twice: with H = omega N,
    # the Boltzmann matrix for the flow of aH at inverse temperature b is diag(1, x^{ab/(beta omega)});
    # the pairs (H, beta) and (2H, beta/2) give the SAME exponent, (2H, beta) doubles it
    b_, om_ = Fraction(3), Fraction(2)
    g.check("[Thm 7.16](3) reparametrisation: the exponent identities beta omega = (beta/2)(2 omega) and "
            "beta (2 omega) = 2 beta omega hold exactly, so rho ~ diag(1, x) is KMS at beta for H and at "
            "beta/2 for 2H by one and the same executed identity, and not KMS at beta for 2H (Boltzmann "
            "matrix diag(1, x^2)), at x = 9/16 and at x = 16/9",
            b_ * om_ == (b_ / 2) * (2 * om_) and b_ * (2 * om_) == 2 * (b_ * om_)
            and all(kms_holds(gibbs(x_), diag(F(1), x_)) for x_ in xs)
            and all(not kms_holds(gibbs(x_), diag(F(1), x_ * x_)) for x_ in xs))


# ---------------------------------------------------------------------------
# [Prop 7.21] the Euclidean partner of the boost
# ---------------------------------------------------------------------------

def ss_euclid_checks():
    sq = g.sig(1, 3)                       # e0^2 = +1, e1..e3^2 = -1
    e = [g.gen(i) for i in range(4)]
    sigma_r = g.mul(e[0], e[1], sq)        # boost bivector of the radial plane
    I = g.mul(g.mul(e[0], e[1], sq), g.mul(e[2], e[3], sq), sq)
    Isig = g.mul(I, sigma_r, sq)

    # (3) I sigma_r is the ANGULAR plane e2 e3, and its rotor fixes e0, e1 and sigma_r
    g.check("[Prop 7.21](3) I sigma_r = e2 e3 blade-exactly: the dual member of the pair is the angular plane",
            g.eq(Isig, g.mul(e[2], e[3], sq)))
    Rang = g.add(g.sc(Fraction(3, 5)), g.scal(Fraction(4, 5), Isig))     # exp(theta I sigma_r / 2), rational
    Rrev = g.reverse(Rang)
    act = lambda v: g.mul(g.mul(Rang, v, sq), Rrev, sq)
    g.check("[Prop 7.21](3) the rotor of I sigma_r fixes e0 and e1 (hence sigma_r) and rotates e2 into e3: "
            "a rotation along the bifurcation sphere, not around it",
            g.eq(act(e[0]), e[0]) and g.eq(act(e[1]), e[1]) and g.eq(act(sigma_r), sigma_r)
            and g.eq(act(e[2]), g.add(g.scal(Fraction(-7, 25), e[2]), g.scal(Fraction(24, 25), e[3])))
            and g.eq(act(e[3]), g.add(g.scal(Fraction(-24, 25), e[2]), g.scal(Fraction(-7, 25), e[3])))
            and not g.eq(act(e[2]), e[2]))
    # the real bivectors of span{sigma_r, I sigma_r} with square -1 are +- I sigma_r only:
    # (a sigma_r + b I sigma_r)^2 = (a^2 - b^2) + 2ab I, so square -1 forces ab = 0, a^2 - b^2 = -1
    a, b = Fraction(2, 7), Fraction(-5, 3)
    Bab = g.add(g.scal(a, sigma_r), g.scal(b, Isig))
    g.check("[Prop 7.21](3) (a sigma_r + b I sigma_r)^2 = (a^2 - b^2) + 2ab I blade-exactly, so the only real "
            "members of the pair's span with square -1 are +- I sigma_r: no real rotor of Cl(1,3) continues "
            "the boost to a rotation of the radial plane",
            g.eq(g.mul(Bab, Bab, sq), g.add(g.sc(a * a - b * b), g.scal(2 * a * b, I))))

    # (1), (2): the complexified rotor R = cos(theta/2) + i sigma sin(theta/2) in Mat_2(Q(i))
    I2 = [[g.qi(1), g.qi(0)], [g.qi(0), g.qi(1)]]
    sig_c = [[g.qi(-1), g.qi(0)], [g.qi(0), g.qi(1)]]           # sigma = diag(-1, 1) on the module
    isig = [[g.qi(0, -1), g.qi(0)], [g.qi(0), g.qi(0, 1)]]      # i sigma

    def qmm(A, B):
        return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]

    def qeq(A, B):
        return all(A[i][j] == B[i][j] for i in range(2) for j in range(2))

    def qscal(c, A):
        return [[c * A[i][j] for j in range(2)] for i in range(2)]

    def qadd(A, B):
        return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

    def qdag(A):
        return [[A[j][i].conj() for j in range(2)] for i in range(2)]

    g.check("[Prop 7.21](1) (i sigma)^2 = -1 on the module", qeq(qmm(isig, isig), qscal(g.qi(-1), I2)))

    def Rc(c, s_):
        return qadd(qscal(g.qi(c), I2), qscal(g.qi(s_), isig))

    R1 = Rc(Fraction(3, 5), Fraction(4, 5))
    g.check("[Prop 7.21](1) the complexified rotor is unitary and obeys the composition law "
            "R(3/5,4/5)^2 = R(-7/25, 24/25)",
            qeq(qmm(R1, qdag(R1)), I2) and qeq(qmm(R1, R1), Rc(Fraction(-7, 25), Fraction(24, 25))))
    quarter = Rc(0, 1)                         # theta = pi
    half = qmm(quarter, quarter)               # theta = 2 pi
    full = qmm(half, half)                     # theta = 4 pi
    g.check("[Prop 7.21](1),(2) R_{2 pi i} = -1 on the module and R_{4 pi i} = +1: period 4 pi for the "
            "rotor, 2 pi for its conjugation action; R_{i theta} = diag(e^{-i theta/2}, e^{i theta/2})",
            qeq(half, qscal(g.qi(-1), I2)) and qeq(full, I2)
            and R1[0][0] == g.qi(Fraction(3, 5), Fraction(-4, 5)) and R1[1][1] == g.qi(Fraction(3, 5), Fraction(4, 5)))
    generic = [[g.qi(2, 1), g.qi(Fraction(1, 3))], [g.qi(0, -2), g.qi(5)]]
    g.check("[Prop 7.21](2) conjugation by R_{2 pi i} = -1 is the identity on the whole algebra, odd "
            "elements included", qeq(qmm(qmm(half, generic), qdag(half)), generic))


# ---------------------------------------------------------------------------
# [Prop 7.18], [Thm 7.20], [Prop 7.23], [Thm 7.3] examples: the rate, the gluing, the two functionals
# ---------------------------------------------------------------------------

def ss_rate_checks():
    # [Prop 7.18] the Euclidean section.  Parametrise by F = sqrt(f) itself (an indeterminate w):
    # f = w^2 gives r = 2M/(1 - w^2), and d rho = dr/F, so dF/d rho = F / (dr/dw) = w / r'(w).
    # The claim dF/d rho = f'(r)/2 = M/r^2 is then an identity of rational functions in w.
    w = g.RF.var()
    M = MASS
    one = g.RF.const(1)
    r_w = g.RF.const(2 * M) / (one - w * w)
    dF_drho = w / r_w.deriv()
    half_fprime = g.RF.const(M) / (r_w * r_w)
    g.check("[Prop 7.18] dF/d rho = f'/2 as an identity of rational functions in F = sqrt(f) "
            "(both sides (1 - F^2)^2/4M), and its value at the horizon F = 0 is 1/4M = kappa",
            dF_drho.eqrf(half_fprime) and dF_drho.eval(0) == 1 / (4 * M))
    r = g.RF.var()
    f = one - g.RF.const(2 * M) / r
    fp = f.deriv()
    g.check("[Prop 7.18] f(2M) = 0 and f'(2M)/2 = 1/4M exactly", f.eval(2 * M) == 0 and fp.eval(2 * M) / 2 == 1 / (4 * M))
    g.check("[Prop 7.18] the period: kappa p = 2 pi with kappa = 1/4M gives p = 8 pi M, i.e. p/(2 pi) = 4M = 1/kappa "
            "(pi cancelled)", 1 / (fp.eval(2 * M) / 2) == 4 * M)

    # [Prop 7.25] the two rates contrasted: the connection rate offers no finite period on the
    # singular side, the horizon rate is finite, and the boost's fixed locus is where f vanishes,
    # which Step 1's own checks certify as algebraically regular (det hbar = 1 there, [Prop 2.4])
    rate_sq = g.RF.const(Fraction(M, 2)) / (r * r * r)
    pole0 = False
    try:
        _ = rate_sq.eval(Fraction(0))
    except ZeroDivisionError:
        pole0 = True
    grows = rate_sq.eval(F(1, 10)) < rate_sq.eval(F(1, 100)) < rate_sq.eval(F(1, 1000))
    g.check("[Prop 7.25] the connection rate (beta')^2 = (M/2)/r^3 has a pole at r = 0 (no finite "
            "period on the singular side) and grows without saturation toward it, while the horizon "
            "rate kappa = f'(2M)/2 = 1/4M is finite and the boost's fixed locus is f(2M) = 0",
            pole0 and grows and fp.eval(2 * M) / 2 == 1 / (4 * M) and f.eval(2 * M) == 0)

    # [Thm 7.20] the gluing condition e^{p omega} n = 1 - n, with x = e^{-p omega} = 9/16
    x = F(9, 16)
    n = x / (1 + x)                          # Fermi-Dirac at inverse temperature p
    y = 1 / x                                # e^{p omega}
    cands = (n, F(1, 3), F(2, 5), F(24, 25), F(1, 2), F(0))
    g.check("[Thm 7.20] the gluing condition e^{p omega} n = 1 - n has the unique solution "
            "n = 1/(e^{p omega} + 1) = 9/25: linear in n with coefficient 1 + e^{p omega} != 0, every "
            "other candidate on a probe list failing, and both ladder orderings give the same equation",
            y * n == 1 - n and n == 1 / (y + 1) and (x * (1 - n) == n) and (1 + y) != 0
            and all((y * m == 1 - m) == (m == n) for m in cands))
    g.check("[Thm 7.20] the boundary cases fail the gluing: n = 0 (unoccupied) gives 0 != 1, "
            "n = 1/2 (tracial) gives e^{p omega}/2 != 1/2",
            not ((1 / x) * 0 == 1) and not ((1 / x) * F(1, 2) == F(1, 2)))
    # the marginal it fixes is the Gibbs state of K at beta = p, faithful
    rho_p = diag(1 - n, n)
    g.check("[Thm 7.20] the fixed marginal diag(1 - n, n) = diag(1, x)/(1 + x) is the Gibbs state at "
            "beta = p, of full rank (hypothesis (iii) follows)",
            meq(rho_p, mscal(1 / (1 + x), diag(F(1), x))) and rho_p[0][0] > 0 and rho_p[1][1] > 0)

    # [Prop 7.23] the two KMS functionals, on all sixteen matrix-unit pairs
    units = [[[F(1) if (i, j) == (a, b) else F(0) for j in range(2)] for i in range(2)]
             for a in range(2) for b in range(2)]
    Eb = diag(F(1), x)                        # e^{-beta H}, H = omega N
    Ebi = diag(F(1), 1 / x)
    Gam = diag(F(1), F(-1))                   # fermion parity 1 - 2N
    rho_state = mscal(1 / (1 + x), Eb)
    rho_tw = mscal(1 / (1 - x), mm(Gam, Eb))  # the parity-twisted functional, normalised

    def eps(B):                               # +1 even (diagonal unit), -1 odd (off-diagonal unit)
        return 1 if meq(mm(mm(Gam, B), Gam), B) else -1

    def ungraded(ph):
        return all(mtr(mm(ph, mm(A, B))) == mtr(mm(ph, mm(B, mm(Eb, mm(A, Ebi)))))
                   for A in units for B in units)

    def graded(ph):
        return all(mtr(mm(ph, mm(A, B))) == eps(B) * mtr(mm(ph, mm(B, mm(Eb, mm(A, Ebi)))))
                   for A in units for B in units)

    g.check("[Prop 7.23](1) the Gibbs state satisfies the ungraded KMS identity and fails the graded one",
            ungraded(rho_state) and not graded(rho_state))
    g.check("[Prop 7.23](2) the parity-twisted functional tr(Gamma e^{-beta H} .)/tr(Gamma e^{-beta H}) "
            "satisfies the graded identity and fails the ungraded one",
            graded(rho_tw) and not ungraded(rho_tw))
    occ_tw = mtr(mm(rho_tw, P_OCC))
    g.check("[Prop 7.23](2),(3) the twisted functional is not a state: its occupancy is "
            "-e^{-beta omega}/(1 - e^{-beta omega}) = %s < 0, while Z = 1 + x and Z_Gamma = 1 - x" % occ_tw,
            occ_tw == -x / (1 - x) and occ_tw < 0 and mtr(Eb) == 1 + x and mtr(mm(Gam, Eb)) == 1 - x)

    # [Thm 7.3] the two examples bounding the hypotheses (two qubits: pair factor first)
    c, s_ = F(3, 5), F(4, 5)
    omega_a = ket(2, {0b01: c, 0b10: s_})       # c|01> + s|10>: violates (ii), descends thermally
    red_a = ss_marginal(omega_a, 0, 2)
    g.check("[Thm 7.3] c|01> + s|10> is pure with Schmidt rank 2 (cyclic and separating) and reduces to "
            "diag(c^2, s^2): thermal without hypothesis (ii)",
            meq(red_a, diag(c * c, s_ * s_)) and mtr(mm(omega_a, omega_a)) == 1)
    # c|+0> + s|-1>: amplitudes (c/sqrt2, c/sqrt2, s/sqrt2, -s/sqrt2) on |00>,|10>,|01>,|11>; the
    # density matrix is rational (the 1/sqrt2 squares away): build it from the unnormalised vector
    amps = {0b00: c, 0b10: c, 0b01: s_, 0b11: -s_}
    dim = 4
    rho_b = [[amps.get(i, F(0)) * amps.get(j, F(0)) / 2 for j in range(dim)] for i in range(dim)]
    red_b = ss_marginal(rho_b, 0, 2)
    want = [[F(1, 2), (c * c - s_ * s_) / 2], [(c * c - s_ * s_) / 2, F(1, 2)]]
    g.check("[Thm 7.3] c|+0> + s|-1> is pure with full-rank reduction (1/2)[[1, c^2 - s^2],[c^2 - s^2, 1]]: "
            "cyclic and separating, violates (ii), and does NOT descend thermally (nonzero coherence)",
            mtr(rho_b) == 1 and mtr(mm(rho_b, rho_b)) == 1 and meq(red_b, want)
            and red_b[0][1] != 0 and red_b[0][0] * red_b[1][1] - red_b[0][1] * red_b[1][0] > 0)


# ---------------------------------------------------------------------------
# [Cor 7.32] the chain's state class and its stability
# ---------------------------------------------------------------------------

def ss_stateclass_checks():
    n = 2
    # both signs of beta: (c, s) = (4/5, 3/5) gives x = e^{-beta omega} = 9/16 (physical, marginals
    # diag(16/25, 9/25)); (3/5, 4/5) gives x = 16/9 (population-inverted, marginals diag(9/25, 16/25)).
    ok1 = ok2 = ok3 = True
    for c, s_ in ((F(4, 5), F(3, 5)), (F(3, 5), F(4, 5))):
        x = (s_ / c) ** 2                          # e^{-beta omega}, equal for both modes (equal weights)
        gibbs = mscal(1 / (1 + x), diag(F(1), x))
        psi = ket(n, {0b00: c, 0b11: s_})          # entangled even state
        ok1 = ok1 and meq(ss_marginal(psi, 0, n), gibbs) and meq(ss_marginal(psi, 1, n), gibbs) \
            and meq(mm(mm(parity_op(n), psi), parity_op(n)), psi)
        prod = kron(gibbs, gibbs)
        ok3 = ok3 and not meq(psi, prod) and meq(dephase_joint(prod), prod) \
            and meq(ss_marginal(prod, 0, n), gibbs)
        U = cz(n, 0, 1)
        psi2 = conj(U, psi)
        ok2 = ok2 and meq(ss_marginal(psi2, 0, n), gibbs) and meq(ss_marginal(psi2, 1, n), gibbs) \
            and meq(mm(mm(parity_op(n), psi2), parity_op(n)), psi2) and not meq(psi2, psi)
    g.check("[Cor 7.32](1) an entangled even state with both marginals Gibbs at the same beta is in the "
            "class: even, marginals diag(16/25, 9/25) at x = 9/16 and diag(9/25, 16/25) at x = 16/9", ok1)
    g.check("[Cor 7.32](3) it is not a product (total correlation nonzero), while the product member "
            "with the same marginals is in the class and is a fixed point of E_N (the (G) state), at "
            "both sample points", ok3)
    g.check("[Cor 7.32](2) a controlled-Z keeps the state in the class: even, same marginals, and changed, "
            "at both sample points", ok2)


# ---------------------------------------------------------------------------
# [Thm 7.28] exact equilibrium over-determines the ledger
# ---------------------------------------------------------------------------

def ss_overdetermination_checks():
    x1, x2 = F(2, 3), F(4, 9)
    r1 = mscal(Fraction(1, 1) / (1 + x1), diag(F(1), x1))
    r2 = mscal(Fraction(1, 1) / (1 + x2), diag(F(1), x2))
    rho_prod = kron(r1, r2)

    g.check("[Thm 7.28](2) the product Gibbs state is a fixed point of E_N: zero deficit",
            meq(dephase_joint(rho_prod), rho_prod))

    g.check("[Thm 7.28](1) the product Gibbs state has zero total correlation: "
            "rho = rho_1 (x) rho_2 exactly",
            meq(rho_prod, kron(ss_marginal(rho_prod, 0, 2), ss_marginal(rho_prod, 1, 2))))

    # correlated control: an even entangled two-mode state
    ctrl = ket(2, {0b00: F(3, 5), 0b11: F(4, 5)})
    g.check("[Thm 7.28] control: an entangled even state is not a product and is not a "
            "fixed point of E_N, so the purity strictly drops under descent",
            (not meq(ctrl, kron(ss_marginal(ctrl, 0, 2), ss_marginal(ctrl, 1, 2))))
            and (not meq(dephase_joint(ctrl), ctrl))
            and mtr(mm(dephase_joint(ctrl), dephase_joint(ctrl)))
                < mtr(mm(ctrl, ctrl)))


# ---------------------------------------------------------------------------
# [Thm 7.27] the purification is canonical
# ---------------------------------------------------------------------------

def ss_purification_checks():
    c, s = F(3, 5), F(4, 5)
    omega = ket(2, {0b00: c, 0b11: s})
    rho = ss_marginal(omega, 0, 2)
    g.check("[Thm 7.27](1) the thermofield vector purifies rho = diag(9/25, 16/25)",
            meq(rho, diag(F(9, 25), F(16, 25))) and mtr(mm(omega, omega)) == 1)

    g.check("[Thm 7.27](4) the thermofield angle: tan^2 theta = (s/c)^2 = 16/9 = "
            "e^{-omega/T}, matching Lem 7.2",
            (s / c) ** 2 == F(16, 9)
            and rho[1][1] / rho[0][0] == F(16, 9))

    # modular eigenvalues lambda_i^2 / lambda_j^2 on |ij>
    lam = [c, s]
    delta = diag(*[lam[i] ** 2 / lam[j] ** 2 for i in range(2) for j in range(2)])
    g.check("[Thm 7.27](1) the modular operator Delta = rho (x) rhobar^{-1} has "
            "eigenvalues lambda_i^2/lambda_j^2 on |ij> (Lem 7.1)",
            meq(delta, kron(rho, diag(1 / rho[0][0], 1 / rho[1][1]))))

    # purifications differ by a unitary on the purifying factor only
    W = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    omega2 = conj(kron(eye(2), W), omega)
    g.check("[Thm 7.27](3) a unitary on the purifying factor alone leaves the marginal "
            "unchanged: the purification is unique up to the commutant",
            meq(ss_marginal(omega2, 0, 2), rho) and not meq(omega2, omega))


# ---------------------------------------------------------------------------
# [Prop 7.31] number-diagonal dynamics; what (L_E) excludes
# ---------------------------------------------------------------------------

def ss_dynamics_checks():
    # the finite-ledger model's two-pair state, in the order (R1, L1, R2, L2):
    # even, with the support constraint R_k = L_k of Lem 12.1
    n = 4
    c1, s1, c2, s2 = F(3, 5), F(4, 5), F(4, 5), F(3, 5)
    rho = ket(n, {0b0000: c1 * c2, 0b0011: c1 * s2,
                  0b1100: s1 * c2, 0b1111: s1 * s2})

    U = cz(n, 1, 3)                       # controlled-Z between the window qubits
    rho_cz = conj(U, rho)
    same_pops = all(rho_cz[b][b] == rho[b][b] for b in range(2 ** n))
    same_marg = all(meq(ss_marginal(rho_cz, k, n), ss_marginal(rho, k, n)) for k in range(n))
    g.check("[Prop 7.31] a controlled-Z circuit preserves every joint-number probability "
            "and every single-mode marginal of the boundary-mode state", same_pops and same_marg)

    g.check("[Prop 7.31] the controlled-Z circuit commutes with the total parity, so it "
            "maps even states to even states and Thm 7.10 keeps applying",
            meq(mm(U, parity_op(n)), mm(parity_op(n), U)))

    g.check("[Prop 7.31] the controlled-Z does change the joint coherence, so the "
            "dynamics is not trivial: it writes only where the descent cannot read",
            not meq(rho_cz, rho))

    B = beam_splitter(n, 1, 2, F(3, 5), F(4, 5))
    Bt = [[B[j][i] for j in range(len(B))] for i in range(len(B))]
    g.check("[Prop 7.31] the beam splitter is orthogonal (a genuine unitary on the "
            "four-mode space) and parity preserving",
            meq(mm(B, Bt), eye(2 ** n)) and meq(mm(B, parity_op(n)), mm(parity_op(n), B)))

    rho_bs = conj(B, rho)
    g.check("[Prop 7.31] the hopping rotation changes the marginal populations, which is "
            "exactly the generator (L_E) does not supply",
            not meq(ss_marginal(rho_bs, 1, n), ss_marginal(rho, 1, n)))


def schmidt_forcing_checks():
    """[Lem 7.2] Schmidt forcing as an exact eigenspace computation over Q.
    Basis |ij> at index 2i + j; the pair factor acts as A (x) 1 on the first slot."""
    Gdiag = [F(0), F(-1), F(1), F(0)]           # G|ij> = (i - j)|ij>
    Gm = diag(*Gdiag)
    ker_basis = [[F(1), F(0), F(0), F(0)], [F(0), F(0), F(0), F(1)]]
    ok = all(all(sum(Gm[i][j] * v[j] for j in range(4)) == 0 for i in range(4)) for v in ker_basis)
    ok = ok and Gdiag[0b10] == 1 and Gdiag[0b01] == -1
    g.check("[Lem 7.2] G = N(x)1 - 1(x)N is diagonal with eigenvalues (0, -1, +1, 0): the 0-eigenspace "
            "is exactly span{|00>, |11>}, the +-1 eigenspaces the product lines |10> and |01>", ok)

    def act(A, v):                               # (A (x) 1) v
        out = [F(0)] * 4
        for i in range(2):
            for j in range(2):
                for ip in range(2):
                    out[2 * i + j] += A[i][ip] * v[2 * ip + j]
        return out

    def unit(a, b):
        return [[F(1) if (i, j) == (a, b) else F(0) for j in range(2)] for i in range(2)]

    basisM = [unit(0, 0), unit(0, 1), unit(1, 0), unit(1, 1)]
    v10 = [F(0), F(0), F(1), F(0)]
    killed = act(unit(0, 0), v10) == [F(0)] * 4
    imgs10 = [act(A, v10) for A in basisM]
    g.check("[Lem 7.2] the +1 eigenvector |10> is a product vector: the nonzero element E_00 (x) 1 "
            "annihilates it (not separating) and its orbit under the pair factor has exact rank 2 < 4 "
            "(not cyclic)", killed and g.mat_rank(imgs10) == 2)

    c, d = F(3, 5), F(4, 5)
    om = [c, F(0), F(0), d]
    imgs = [act(A, om) for A in basisM]
    g.check("[Lem 7.2] a 0-eigenvector with both coefficients nonzero, (3/5)|00> + (4/5)|11>, is cyclic "
            "and separating: its orbit under the four matrix units has exact rank 4, so the map "
            "A -> (A (x) 1) Omega is injective and onto", g.mat_rank(imgs) == 4)

    x = F(2)                                     # a sample boost 'phase': U = diag(x^{i-j})
    U = [x ** int(gd) for gd in Gdiag]
    Uom = [U[i] * om[i] for i in range(4)]
    w = [c, d, F(0), F(0)]
    Uw = [U[i] * w[i] for i in range(4)]

    def proportional(u, v):
        return all(u[i] * v[j] == u[j] * v[i] for i in range(4) for j in range(4))

    g.check("[Lem 7.2] invariance up to phase under the boost unitary holds exactly for the "
            "0-eigenvector and fails for a mixed-support vector: invariance forces the Schmidt basis "
            "to be the number basis", proportional(Uom, om) and not proportional(Uw, w))


def plane_rate_checks():
    """[Prop 6.2] the plane and the rate, checked directly."""
    r = g.RF.var()
    f = (r - g.RF.const(2 * MASS)) / r
    kappa = f.deriv().eval(2 * MASS) / 2
    g.check("[Prop 6.2] kappa = f'(2M)/2 = 1/4M exactly, from the derivative of f = 1 - 2M/r",
            kappa == Fraction(1, 1) / (4 * MASS))
    g.check("[Prop 6.2] the conversion: 2 pi of rapidity = 8 pi M of Killing time, pi cancelled "
            "(1/kappa = 4M), the chain's single unit-carrying number",
            Fraction(1, 1) / kappa == 4 * MASS)
    sig = g.mul(g.gen(0), g.gen(1), STA)
    Isig = g.mul(g.gen(2), g.gen(3), STA)
    g.check("[Prop 6.2] the invariant separation of the selected pair: sigma_r^2 = +1 and "
            "(I sigma_r)^2 = -1 blade-exactly",
            g.eq(g.mul(sig, sig, STA), g.sc(1)) and g.eq(g.mul(Isig, Isig, STA), g.sc(-1)))


def wick_q_checks():
    """[Thm 8.2]/(Q): the Wick step is the premise's, run as an OPERATOR computation: number
    operators as matrices, expectations as traces, the connected correlator computed outright
    (not read back from the construction)."""
    n1v, n2v = Fraction(9, 25), Fraction(9, 25)
    eps = Fraction(1, 100)
    # two joint number-diagonal states on modes (k, k+m), basis b = 2 b1 + b2: the product member
    # and a correlated even member built by moving eps between the diagonal correlations
    pp = [(1 - n1v) * (1 - n2v), (1 - n1v) * n2v, n1v * (1 - n2v), n1v * n2v]
    qq = [pp[0] + eps, pp[1] - eps, pp[2] - eps, pp[3] + eps]
    rho_p, rho_c = diag(*pp), diag(*qq)
    N1 = diag(F(0), F(0), F(1), F(1))
    N2 = diag(F(0), F(1), F(0), F(1))
    ImN1 = diag(F(1), F(1), F(0), F(0))
    A = mm(N2, ImN1)                       # the Planck summand operator n_{k+m}(1 - n_k)
    ev = lambda rho, Op: mtr(mm(rho, Op))
    marg_ok = ev(rho_p, N1) == n1v and ev(rho_c, N1) == n1v \
        and ev(rho_p, N2) == n2v and ev(rho_c, N2) == n2v \
        and all(v > 0 for v in qq) and sum(qq) == 1
    wick_p = ev(rho_p, A) == ev(rho_p, N2) * ev(rho_p, ImN1)
    connected = ev(rho_c, A) - ev(rho_c, N2) * ev(rho_c, ImN1)
    g.check("[Thm 8.2] premise (Q) isolated, as an operator computation: the Planck summand "
            "<n_{k+m}(1 - n_k)>, a trace against the state, factorises into its two-point pieces "
            "exactly on a quasi-free product state carrying [Thm 7.20]'s gluing occupancy n = 9/25 "
            "(the state-class witnesses elsewhere use the conjugate ladder labelling, occupancy "
            "16/25); on a correlated even state with identical marginals (verified by trace) the "
            "connected correlator, computed outright, is -1/100, and the summand shifts by exactly "
            "it: without (Q) no exact spectrum",
            marg_ok and wick_p and connected == -eps and connected != 0
            and ev(rho_c, A) == ev(rho_p, A) + connected)


def page_noattic_checks():
    """[Fact 11.1] the envelope's two arms on the thermal model; [Prop 11.4] no attic."""
    stages, pairs, nq = build_model()
    hs = [entropy_logvec([c * c, s * s]) for (c, s) in pairs]
    ln2 = LogVec.ln_int(2)
    ok_env = ok_rise = ok_sect = ok_moments = ok_prod = True
    saw_sth_arm = saw_cap_arm = False
    for (state, radiation, window) in stages:
        ninj = (len(radiation) + len(window)) // 2
        S_th = LogVec()
        for k in range(ninj):
            S_th = S_th + hs[k]
        norm = sum(a * a for a in state.values())
        if window:
            rhoL = marginal(sorted(window), state, nq)
            rhoL = [[x / norm for x in row] for row in rhoL]
            spec = [rhoL[i][i] for i in range(len(rhoL))]
            S_L = entropy_logvec(spec)
        else:
            rhoL = None
            S_L = LogVec()
        C = ln2 * len(window)
        ok_env = ok_env and logvec_le(S_L, S_th) and logvec_le(S_L, C)
        rising = all(qb % 2 == 0 for qb in radiation)     # no evicted (odd-label) qubit yet
        if rising:
            ok_rise = ok_rise and S_L == S_th
        if logvec_le(S_th, C) and not S_th == C:
            saw_sth_arm = True
        if logvec_le(C, S_th) and not S_th == C:
            saw_cap_arm = True
        ok_sect = ok_sect and sorted(radiation + window) == list(range(2 * ninj))
        # [Thm 11.5]/[Cor 7.32] the window marginal is the product (G) member at every stage:
        # verified ENTRYWISE (diagonality checked, each diagonal entry equal to the product of the
        # single-mode marginals, and the whole matrix a fixed point of E_N: the ledger reading is free)
        if window:
            nw = len(window)
            diag_zero = all(rhoL[i][j] == 0 for i in range(len(rhoL))
                            for j in range(len(rhoL)) if i != j)
            margs = [sum(spec[b] for b in range(len(spec)) if (b >> j) & 1) for j in range(nw)]
            prod_ok = True
            for b in range(len(spec)):
                val = Fraction(1)
                for j in range(nw):
                    val *= margs[j] if (b >> j) & 1 else 1 - margs[j]
                prod_ok = prod_ok and spec[b] == val
            ok_prod = ok_prod and diag_zero and prod_ok and pinch(rhoL) == rhoL
        # [Prop 11.4] no attic, dynamically: the nonzero spectra of the two sectors match, so no
        # q-number content leaves the two-sector accounting; checked through the second and third
        # trace moments of rho_R against rho_L (skipped only where rho_R exceeds 64 x 64)
        if window and len(radiation) <= 6:
            rhoR = marginal(sorted(radiation), state, nq)
            rhoR = [[x / norm for x in row] for row in rhoR]
            trL = sum(rhoL[i][i] for i in range(len(rhoL)))
            trR = sum(rhoR[i][i] for i in range(len(rhoR)))
            L2 = mm(rhoL, rhoL); R2 = mm(rhoR, rhoR)
            L3 = mm(L2, rhoL); R3 = mm(R2, rhoR)
            tr = lambda A: sum(A[i][i] for i in range(len(A)))
            ok_moments = ok_moments and trL == trR == 1 \
                and tr(L2) == tr(R2) and tr(L3) == tr(R3)
    g.check("[Fact 11.1] the envelope on the thermal model: S_R = S_L <= min(S_th, C) at every stage, "
            "with the rising branch exact (S_L = S_th before any eviction)", ok_env and ok_rise)
    g.check("[Fact 11.1] the two arms cross during the run: stages exist with S_th < C and with "
            "C < S_th, strictly (the turnover of the Page envelope)", saw_sth_arm and saw_cap_arm)
    g.check("[Prop 11.4] two-sector exhaustiveness at every stage: window and radiation are disjoint "
            "and together carry every injected qubit (no attic, kinematically)", ok_sect)
    g.check("[Prop 11.4] no attic, dynamically: tr rho_R^2 = tr rho_L^2 and tr rho_R^3 = tr rho_L^3 "
            "at every checked stage, so the sectors' nonzero spectra agree and nothing leaks out of "
            "the two-sector accounting", ok_moments)
    g.check("[Thm 11.5]/[Cor 7.32] the window marginal, verified diagonal entrywise, equals the "
            "product of its own single-mode marginals entry by entry and is a fixed point of E_N at "
            "every stage: reading the boundary modes costs nothing, and the information lies across the "
            "window/radiation cut", ok_prod)
    # [Thm 11.5] the saturation boundary COMPUTED through the thermofield angle: with x = e^{-omega/T},
    # (c^2, s^2) = (1/(1+x), x/(1+x)); symmetric iff x = 1 iff omega = 0; h(x) = ln 2 iff x = 1,
    # strictly below and monotone toward the boundary otherwise
    def h_of(x):
        return entropy_logvec([Fraction(1, 1) / (1 + x), x / (1 + x)])
    ok_sat = h_of(Fraction(1)) == ln2
    sym = lambda x: Fraction(1, 1) / (1 + x) == x / (1 + x)
    ok_sat = ok_sat and sym(Fraction(1)) and not sym(Fraction(9, 16)) and not sym(Fraction(3, 4))
    hs_x = [h_of(x) for x in (Fraction(9, 16), Fraction(3, 4), Fraction(9, 10))]
    for hh in hs_x:
        ok_sat = ok_sat and logvec_le(hh, ln2) and not hh == ln2
    ok_sat = ok_sat and logvec_le(hs_x[0], hs_x[1]) and not hs_x[0] == hs_x[1] \
        and logvec_le(hs_x[1], hs_x[2]) and not hs_x[1] == hs_x[2]
    for h in hs:
        ok_sat = ok_sat and logvec_le(h, ln2) and not h == ln2
    g.check("[Thm 11.5] saturation boundary through the thermofield angle: with x = e^{-omega/T} the "
            "pair (c^2, s^2) = (1/(1+x), x/(1+x)) is symmetric iff x = 1 (omega = 0, the one "
            "zero-weight mode the linear assignment supplies); h = ln 2 exactly there, h < ln 2 "
            "strictly and monotone toward the boundary at x = 9/16, 3/4, 9/10, and every model pair "
            "lies strictly below", ok_sat)


def deficit_blindness_checks():
    """[Rem 9.5]/[Prop 12.5] the deficit is blind to the message: identical final configuration
    distributions in the scrambled and unscrambled histories, hence identical S(E rho_R) = S_th
    and, with global purity, identical deficit; the histories differ only in amplitude signs."""
    stages_s, pairs, nq = build_model()
    state_s = stages_s[-1][0]
    state_u = {0: Fraction(1)}
    window, radiation = [], []
    for k, (c, s) in enumerate(pairs):
        state_u = pair_state(c, s, k, state_u)
        radiation.append(2 * k)
        window.append(2 * k + 1)
        if len(window) > 2:
            radiation.append(window.pop(0))        # same schedule, no CZ
    while window:
        radiation.append(window.pop(0))
    norm_s = sum(a * a for a in state_s.values())
    norm_u = sum(a * a for a in state_u.values())
    dist_s = {occ: a * a / norm_s for occ, a in state_s.items()}
    dist_u = {occ: a * a / norm_u for occ, a in state_u.items()}
    same_dist = dist_s == dist_u
    keys = set(state_s) | set(state_u)
    diff_state = any(state_s.get(occ, Fraction(0)) != state_u.get(occ, Fraction(0)) for occ in keys)
    S_th = LogVec()
    for (c, s) in pairs:
        S_th = S_th + entropy_logvec([c * c, s * s])
    S_dephased = entropy_logvec(list(dist_s.values()))
    g.check("[Rem 9.5] the deficit is blind to the message: scrambled and unscrambled histories have "
            "identical final configuration distributions (the CZ phases square away), hence identical "
            "S(E rho_R) = S_th and, with global purity, identical deficit D = S_th; the histories "
            "differ only in amplitude signs, the pattern the deficit cannot see",
            same_dist and diff_state and S_dephased == S_th and norm_s == 1 and norm_u == 1)


def local_univalence_checks():
    """[Prop 9.6] E_N against the total-parity average: different maps on two or more modes, and
    under the total-parity average alone the model's two-ledger discrepancy would vanish."""
    stages, pairs, nq = build_model()
    state = stages[-1][0]
    all_even = all(bin(occ).count("1") % 2 == 0 for occ in state)
    c1, s1 = MODEL_PAIRS[0]
    c2, s2 = MODEL_PAIRS[1]
    st2 = apply_cz(1, 3, pair_state(c2, s2, 1, pair_state(c1, s1, 0, {0: Fraction(1)})))
    rho = marginal([0, 1], st2, 4)
    G2 = diag(F(1), F(-1), F(-1), F(1))
    fixed_by_parity = meq(conj(G2, rho), rho)
    coh = rho[0][3]
    killed_by_EN = coh != 0 and pinch(rho)[0][3] == 0
    X = [[F(0), F(1)], [F(1), F(0)]]
    Z = [[F(1), F(0)], [F(0), F(-1)]]
    XXZ = kron(kron(X, X), Z)
    G3 = kron(kron(diag(F(1), F(-1)), diag(F(1), F(-1))), diag(F(1), F(-1)))
    even_corr = meq(mm(G3, XXZ), mm(XXZ, G3))
    annihilated = all(pinch(XXZ)[i][j] == 0 for i in range(8) for j in range(8))
    g.check("[Prop 9.6] its antecedent is doing real work: every configuration of the model's final "
            "radiation state has even total occupation (Ad(Gamma) fixes the state outright, so the "
            "total-parity average alone yields zero deficit); on two modes the parity average fixes "
            "the scrambled pair marginal, coherence included, while E_N kills the coherence; and the "
            "decoding correlator XXZ commutes with the total parity (under (P) alone the message "
            "descends) yet is annihilated entirely by E_N",
            all_even and fixed_by_parity and killed_by_EN and even_corr and annihilated)

    # the composite argument itself: the mode-wise parity averages are idempotent, commute, and
    # compose, in either order, to the joint pinching, on a generic rational two-mode matrix
    A = [[F(1), F(2), F(3), F(4)],
         [F(5), F(6), F(7), F(8)],
         [F(9), F(1, 2), F(2, 3), F(3, 5)],
         [F(4, 7), F(1, 9), F(8, 3), F(11)]]
    S1 = kron(diag(F(1), F(-1)), diag(F(1), F(1)))
    S2 = kron(diag(F(1), F(1)), diag(F(1), F(-1)))

    def m_add(a, b):
        return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]

    Ek = lambda S, x: mscal(F(1, 2), m_add(x, conj(S, x)))
    E1E2 = Ek(S1, Ek(S2, A))
    E2E1 = Ek(S2, Ek(S1, A))
    g.check("[Prop 9.6] the composite argument: the mode-wise parity averages are idempotent, commute, "
            "and compose in either order to the joint pinching E_N on a generic rational two-mode "
            "matrix, so range(E_N) is the intersection of the mode-wise ranges, the joint-diagonal "
            "algebra",
            meq(E1E2, E2E1) and meq(E1E2, pinch(A))
            and meq(Ek(S1, Ek(S1, A)), Ek(S1, A)) and meq(Ek(S2, Ek(S2, A)), Ek(S2, A)))


def lift_null_checks():
    """[Def 5.1] the lift is null with n0.ninf = -1, and not with -1/2, blade-exactly in Cl(2,4)."""
    sq = (1, -1, -1, -1, 1, -1)          # e0..e3 of Cl(1,3), then e_plus^2 = +1, e_minus^2 = -1
    e = [g.gen(i) for i in range(6)]
    n0 = g.add(e[4], e[5])                       # (e+ + e-)^2 = 1 - 1 = 0
    ninf = g.scal(Fraction(1, 2), g.sub(e[5], e[4]))   # (e- - e+)/2, square 0, n0.ninf = -1
    g.check("[Def 5.1] the adjoined pair is null: n0^2 = ninf^2 = 0 blade-exactly in Cl(2,4)",
            g.is_zero(g.mul(n0, n0, sq)) and g.is_zero(g.mul(ninf, ninf, sq)))
    g.check("[Def 5.1] n0 . ninf = -1 (T1's normalisation)", g.dotv(n0, ninf, sq) == -1)
    x = g.add(g.scal(Fraction(3, 2), e[0]), g.scal(Fraction(2, 5), e[1]), g.scal(Fraction(-1, 3), e[2]))
    Q = g.dotv(x, x, sq)
    X = g.add(n0, x, g.scal(Q / 2, ninf))
    g.check("[Def 5.1] the lift X(x) = n0 + x + (1/2) Q(x) ninf is null: X^2 = 0 blade-exactly, Q(x) = %s" % Q,
            g.is_zero(g.mul(X, X, sq)) and Q != 0)
    ninf_half = g.scal(Fraction(1, 2), ninf)      # the normalisation n0 . ninf = -1/2
    X2 = g.add(n0, x, g.scal(Q / 2, ninf_half))
    g.check("[Def 5.1] control: with n0 . ninf = -1/2 the same lift has X^2 = Q/2 != 0 (not null)",
            g.eq(g.mul(X2, X2, sq), g.sc(Q / 2)) and g.dotv(n0, ninf_half, sq) == Fraction(-1, 2))



# ---------------------------------------------------------------------------
# Appendix C: the metric-level sheaf and the hopping exclusion
# ---------------------------------------------------------------------------

def appendix_c_checks():
    """Appendix C on the two-mode Jordan-Wigner ledger and a three-point
    finite model; all matrices exact rational.  Fact B.3 (no equivariant
    value at the wall) is an import, verified in verify_T04.py, and is not
    re-verified here."""
    def T_(A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

    def msub_(A, B):
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def is_zero_(A):
        return all(x == 0 for row in A for x in row)

    def rank_(rows):
        M = [list(r) for r in rows]
        cols = len(M[0]) if M else 0
        r = 0
        for c in range(cols):
            piv = None
            for i in range(r, len(M)):
                if M[i][c] != 0:
                    piv = i
                    break
            if piv is None:
                continue
            M[r], M[piv] = M[piv], M[r]
            pv = M[r][c]
            M[r] = [x / pv for x in M[r]]
            for i in range(len(M)):
                if i != r and M[i][c] != 0:
                    f = M[i][c]
                    M[i] = [M[i][j] - f * M[r][j] for j in range(cols)]
            r += 1
        return r

    A = [[F(0), F(1)], [F(0), F(0)]]
    Adag = T_(A)
    Z = diag(1, -1)
    I2 = eye(2)
    vx, vxd = kron(A, I2), kron(Adag, I2)
    vy, vyd = kron(Z, A), kron(Z, Adag)     # Jordan-Wigner string

    anti = lambda P, Q: madd(mm(P, Q), mm(Q, P))
    ok = meq(anti(vx, vxd), eye(4)) and meq(anti(vy, vyd), eye(4)) \
        and is_zero_(anti(vx, vy)) and is_zero_(anti(vx, vyd)) \
        and is_zero_(mm(vx, vx)) and is_zero_(mm(vy, vy))
    g.check("[Thm C.3] two-mode Jordan-Wigner algebra: {v_x, v_x*} = {v_y, v_y*} = 1, cross "
            "anticommutators and squares zero, exactly", ok)

    sx = msub_(mm(vxd, vx), mm(vx, vxd))
    sy = msub_(mm(vyd, vy), mm(vy, vyd))
    ok = meq(sx, kron(mscal(-1, Z), I2)) and meq(sy, kron(I2, mscal(-1, Z)))
    g.check("[Thm C.3] the strings cancel in sigma_k = v*v - vv*: sigma_x = (-Z)(x)1 and "
            "sigma_y = 1(x)(-Z), single-site both (the Jordan-Wigner locality in the proof "
            "of Prop 9.6)", ok)

    ok = meq(conj(sx, vy), vy) and meq(conj(sy, vy), mscal(-1, vy))
    g.check("[Thm C.4] Ad(sigma_x) fixes v_y while Ad(sigma_y) negates it: v_y lies in the "
            "x-point's fixed algebra and is odd at its own point (the join's wrong stalks)", ok)

    X = [[F(i * 4 + j + 1) + (F(1, 3) if i == j else 0) for j in range(4)] for i in range(4)]
    Ek = lambda S, M: mscal(F(1, 2), madd(M, conj(S, M)))
    comp = Ek(sx, Ek(sy, X))
    pinched = [[X[i][j] if i == j else F(0) for j in range(4)] for i in range(4)]
    ok = meq(comp, Ek(sy, Ek(sx, X))) and meq(comp, pinched)
    g.check("[Thm C.3] the meet realised: the composite of the two parity averages, either "
            "order, is the joint-diagonal pinching E_N on a generic rational matrix "
            "(sections = range of the pinching)", ok)

    gens = [vx, vxd, vy, vyd]
    words = [eye(4)] + list(gens)
    for a in gens:
        for b in gens:
            words.append(mm(a, b))
            for c in gens:
                words.append(mm(a, mm(b, c)))
                for d in gens:
                    words.append(mm(a, mm(b, mm(c, d))))
    rows = [[W[i][j] for i in range(4) for j in range(4)] for W in words]
    g.check("[Thm C.4] the join is everything: words in the generators span the full "
            "16-dimensional two-mode ledger (exact rank), so the join is disqualified by its "
            "stalks, not by its size", rank_(rows) == 16)

    # [Thm C.3] the two fibres and the two assemblies, computed: big fibres
    # Fix(Ad sigma_x), Fix(Ad sigma_y) as subspaces of the 16-dimensional ledger
    # (dimension 8 each), their meet (dimension 4); small fibres span{1, sigma_x},
    # span{1, sigma_y} (dimension 2 each), the algebra they generate (dimension 4);
    # the meet of the big fibres, the join of the small fibres and the joint-
    # diagonal algebra range(E_N) coincide as subspaces.
    def vec_(M):
        return [M[i][j] for i in range(4) for j in range(4)]

    def null_space_(rows_of_map, ncols):
        # exact kernel of the linear map given by its rows (as lists of length ncols)
        M = [list(r) for r in rows_of_map]
        piv_cols = []
        r = 0
        for c in range(ncols):
            piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
            if piv is None:
                continue
            M[r], M[piv] = M[piv], M[r]
            pv = M[r][c]
            M[r] = [x / pv for x in M[r]]
            for i in range(len(M)):
                if i != r and M[i][c] != 0:
                    f = M[i][c]
                    M[i] = [M[i][j] - f * M[r][j] for j in range(ncols)]
            piv_cols.append(c)
            r += 1
        free = [c for c in range(ncols) if c not in piv_cols]
        basis = []
        for fc in free:
            x = [F(0)] * ncols
            x[fc] = F(1)
            for row_i, pc in enumerate(piv_cols):
                x[pc] = -M[row_i][fc]
            basis.append(x)
        return basis

    units = [[[F(1) if (a, b) == (i, j) else F(0) for b in range(4)] for a in range(4)]
             for i in range(4) for j in range(4)]

    def fix_rows_(S):
        # rows of the map M -> S M S - M in the matrix-unit basis
        rows = []
        for U in units:
            rows.append(vec_(msub_(conj(S, U), U)))
        # transpose: we want coefficients c with sum_U c_U (S U S - U) = 0
        return [[rows[u][k] for u in range(16)] for k in range(16)]
    Bx = null_space_(fix_rows_(sx), 16)
    By = null_space_(fix_rows_(sy), 16)
    meet = null_space_(fix_rows_(sx) + fix_rows_(sy), 16)
    small_x = [vec_(eye(4)), vec_(sx)]
    small_y = [vec_(eye(4)), vec_(sy)]
    join_small = [vec_(eye(4)), vec_(sx), vec_(sy), vec_(mm(sx, sy))]
    diag_basis = [vec_(diag(*[F(1) if i == d else F(0) for i in range(4)])) for d in range(4)]
    ok = len(Bx) == 8 and len(By) == 8 and len(meet) == 4 \
        and rank_(small_x) == 2 and rank_(small_y) == 2 and rank_(join_small) == 4 \
        and rank_(meet + join_small) == 4 and rank_(meet + diag_basis) == 4 \
        and rank_(small_x + Bx) == 8 and rank_(small_y + By) == 8
    g.check("[Thm C.3] the two fibres computed on two modes: big fibres Fix(Ad sigma_x), "
            "Fix(Ad sigma_y) of dimension 8, small fibres span{1, sigma} of dimension 2 inside "
            "them; meet of the big fibres (dim 4) = join of the small fibres (dim 4) = the "
            "joint-diagonal algebra range(E_N), as subspaces (exact kernels and ranks)", ok)

    # [Thm C.4] isotony of the net assembly: the one-mode ledger's big fibre, embedded
    # in the two-mode ledger, lies inside the two-mode big fibre at the same point
    one_mode_even = [vec_(kron(eye(2), U2)) for U2 in ([[F(1), F(0)], [F(0), F(0)]],
                                                          [[F(0), F(0)], [F(0), F(1)]])]
    g.check("[Thm C.4] isotony: the even elements of mode y's own factor, embedded in the two-"
            "mode ledger, lie in the two-mode big fibre at y (the net assembly is covariant "
            "under inclusion)", rank_(By + one_mode_even) == 8)

    # the hopping exclusion
    chis = [diag(*[F(1) if i == p else F(0) for i in range(3)]) for p in range(3)]
    ok = True
    for i in range(3):
        for j in range(3):
            Eij = [[F(1) if (a, b) == (i, j) else F(0) for b in range(3)] for a in range(3)]
            commutes = all(meq(mm(Eij, ch), mm(ch, Eij)) for ch in chis)
            ok = ok and (commutes == (i == j))
    g.check("[Lem C.6] tensoriality, finite model: a map of the three-point module commutes "
            "with every point multiplier (is function-linear) exactly when it is diagonal, a "
            "bundle map of the line bundle (all nine matrix units, exhaustive); hopping E_xy "
            "fails, multipliers pass", ok)

    Nx, Ny = mm(vxd, vx), mm(vyd, vy)
    comm = lambda P, Q: msub_(mm(P, Q), mm(Q, P))
    # dGamma of the bundle map a = diag(a_x, a_y) built from the DEFINITION
    # psi^dagger a psi = sum_{ij} a_ij v_i^* v_j, then compared with a_x N_x + a_y N_y
    a_x, a_y = F(2), F(5)
    vs, vds = [vx, vy], [vxd, vyd]
    a_mat = [[a_x, F(0)], [F(0), a_y]]
    dG = [[F(0)] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            if a_mat[i][j] != 0:
                dG = madd(dG, mscal(a_mat[i][j], mm(vds[i], vs[j])))
    dG_block = madd(mscal(a_x, Nx), mscal(a_y, Ny))
    ok = meq(dG, dG_block) and is_zero_(comm(dG_block, Nx)) and is_zero_(comm(dG_block, Ny)) \
        and all(dG[i][j] == 0 for i in range(4) for j in range(4) if i != j)
    g.check("[Prop C.7] dGamma of a bundle map, built from psi^dagger a psi, equals "
            "a_x N_x + a_y N_y, is diagonal in the joint number basis, and conserves both "
            "occupation operators exactly", ok)

    hop = madd(mm(vxd, vy), mm(vyd, vx))
    e01 = [[F(0)], [F(1)], [F(0)], [F(0)]]
    out = mm(hop, e01)
    moved = out[2][0] != 0 and out[1][0] == 0
    ok = (not is_zero_(comm(hop, Nx))) and moved
    g.check("[Prop C.7] dGamma of a hop is what the class excludes: it fails to commute "
            "with N_x and carries |0_x 1_y> into the (1,0) sector, exactly", ok)

    cz = mm(sx, sy)
    ok = is_zero_(comm(cz, Nx)) and is_zero_(comm(cz, Ny))
    g.check("[Thm C.8] the class-relative scope: the controlled-Z generator sigma_x sigma_y "
            "conserves both occupations; cross-point diagonal products are not hopping and "
            "were never excluded", ok)

    # the witness that bites: the pairing generator v_x* v_y* + v_y v_x commutes with
    # the total parity Gamma = sigma_x sigma_y, is NOT diagonal in the joint number basis,
    # and fails to commute with N_x: permitted by parity, not number-conserving, and
    # outside the supplied class (it changes total occupation by two)
    pair = madd(mm(vxd, vyd), mm(vy, vx))
    Gam = cz
    Ntot = madd(Nx, Ny)
    off_diag = any(pair[i][j] != 0 for i in range(4) for j in range(4) if i != j)
    ok = is_zero_(comm(pair, Gam)) and off_diag and (not is_zero_(comm(pair, Nx))) \
        and (not is_zero_(comm(pair, Ntot)))
    g.check("[Thm C.8] the pairing generator v_x* v_y* + v_y v_x commutes with Gamma, is "
            "off-diagonal in the joint number basis, and fails to commute with N_x and with "
            "N_x + N_y: parity-preserving, not number-conserving, not excluded by the theorem", ok)

    # Cor 11.6's necessity witness is a pairing rotation (Delta N = +-2), not a hop:
    # the rotation |00> -> 3/5|00> + 4/5|11>, |11> -> -4/5|00> + 3/5|11> on two modes
    # commutes with Gamma and changes N_x + N_y by two on |00>
    R = eye(4)
    R[0][0], R[0][3], R[3][0], R[3][3] = F(3, 5), F(-4, 5), F(4, 5), F(3, 5)
    e00 = [[F(1)], [F(0)], [F(0)], [F(0)]]
    img = mm(R, e00)
    ok = is_zero_(comm(R, Gam)) and meq(mm(T_(R), R), eye(4)) \
        and img[3][0] == F(4, 5) and img[0][0] == F(3, 5) and img[1][0] == 0 and img[2][0] == 0 \
        and (not is_zero_(comm(R, Ntot)))
    g.check("[Cor 11.6 / Rem C.9] the necessity witness is a pairing rotation: orthogonal, "
            "commutes with Gamma, carries |00> to 3/5|00> + 4/5|11> (Delta N = 2, no (0,1) -> "
            "(1,0) component), and does not commute with N_x + N_y", ok)


# ===========================================================================
# Section 13 (v1.20; rebuilt v1.22): the modular flow of the boundary modes as
# a holonomy (Prop 13.2) and the entangling half of (L_E) (Prop 13.4).
# Twenty-one checks.
# ===========================================================================

def holonomy_checks():
    """Prop 13.2: the t-line holonomy rate, its horizon value, its Hubble-
    normalised limit, the two inverse temperatures read off the constructed
    series, and the non-commuting boosts."""
    F = Fraction
    r = g.RF.var()
    one = g.RF1
    A = one / r - one                                   # A = 1/r - 1, units 2M = 1
    rate = A.deriv() * g.RF.const(F(-1, 2))             # -A'/2 = |A'|/2 (A' < 0 for 0 < r)
    g.check("[Prop 13.2(i)] rapidity per Killing time along a t-line is |A'(r)|/2 = -A'/2 = 1/(2 r^2), an identity in Q(r)",
            rate.eqrf(one / (g.RF.const(F(2)) * r * r)) and A.deriv().eval(F(1, 2)) < 0)
    g.check("[Prop 13.2(i)] at the horizon r = 1 the rate is 1/2 = kappa (units 2M = 1): the modular flow's rate",
            rate.eval(F(1)) == F(1, 2))
    g.check("[Prop 13.2(i)] inside, r = 1/2, 1/4, 1/8 give 2, 8, 32: the Killing-time KMS period 4 pi r^2 shrinks",
            [rate.eval(F(1, 2)), rate.eval(F(1, 4)), rate.eval(F(1, 8))] == [F(2), F(8), F(32)])
    # Hubble-normalised: tau |A'|/(2 sqrt A) = (1/3) S(r) (1-r)^{-1/2}, tau = (2/3) r^{3/2} S(r),
    # where S is the series with (2/3) r^{3/2} S(r) = int_0^r sqrt(u/(1-u)) du, i.e.
    # S = sum_k binom(-1/2, k)(-1)^k (3/2) r^k/(k + 3/2); the sphere rate is
    # tau sqrt(A)/r = (2/3) S(r) (1-r)^{1/2}.
    N = 6
    one_minus = [F(1), F(-1)]
    inv_sqrt = g.ps_pow_rat(one_minus, F(-1, 2), N)
    sqrt_1mr = g.ps_pow_rat(one_minus, F(1, 2), N)
    S = [F(3, 2) * inv_sqrt[k] / (k + F(3, 2)) for k in range(N + 1)]
    hub1 = [F(1, 3) * c for c in g.ps_mul(S, inv_sqrt, N)]    # tau |sigma_1|
    hub2 = [F(2, 3) * c for c in g.ps_mul(S, sqrt_1mr, N)]    # tau sigma_2
    g.check("[Prop 13.2(ii)] Hubble-normalised rate (1/3) S(r)/sqrt(1-r) = 1/3 + (4/15) r + ...: limit |p_1| = 1/3, "
            "the t-direction's Kasner exponent, with S = 1 + (3/10) r + (9/56) r^2 + ...",
            hub1[0] == F(1, 3) and hub1[1] == F(4, 15) and S[1] == F(3, 10) and S[2] == F(9, 56))
    beta_t = F(2) / hub1[0]      # coefficient of pi in 2 pi / (limit rate)
    beta_sph = F(2) / hub2[0]
    g.check("[Prop 13.2(ii)/(iii)] 2 pi divided by the constant terms of the constructed series: t-direction "
            "2 pi/(1/3) = 6 pi, sphere direction (2/3) S(r) sqrt(1-r) = 2/3 - (2/15) r + ... giving 2 pi/(2/3) = 3 pi "
            "(both read off the series, not asserted)",
            beta_t == 6 and beta_sph == 3 and hub2[0] == F(2, 3) and hub2[1] == F(-2, 15)
            and sqrt_1mr[1] == F(-1, 2))
    sq = g.sig(1, 3)
    e = [g.gen(i) for i in range(4)]
    B1 = g.scal(F(1, 2), g.sub(g.mul(e[0], e[1], sq), g.mul(e[1], e[0], sq)))
    B2 = g.scal(F(1, 2), g.sub(g.mul(e[0], e[2], sq), g.mul(e[2], e[0], sq)))
    comm_product = g.scal(F(1, 2), g.sub(g.mul(B1, B2, sq), g.mul(B2, B1, sq)))   # (B1 B2 - B2 B1)/2
    R12 = g.mul(e[1], e[2], sq)
    g.check("[Prop 13.2(iii)] the limiting boosts B_1 = e0^e1 and B_2 = e0^e2 do not commute in Cl(1,3): their "
            "commutator product (B_1 B_2 - B_2 B_1)/2 equals -R_12 = -e1 e2 exactly, so their generators are not "
            "proportional and by uniqueness of the modular group at most one of the two flows is modular",
            g.eq(comm_product, g.neg(R12)) and not g.is_zero(comm_product))


def stabtangent_checks():
    """Prop 13.4: so(2 nu) = hops (Cartan elements v_i* v_i - 1/2 included) +
    pair annihilations + pair creations, closed under the bracket; hops and
    annihilations stabilise the vacuum ray, the creations span the tangent of the
    vacuum orbit (rank 1 + nu(nu-1)/2 for the vector, nu(nu-1)/2 for the ray);
    the rotations, formed as genuine exponentials, fix or move |0>; T5's witness;
    and a hop entangles off the vacuum."""
    F = Fraction
    QI = g.QI
    zero, one = QI(0), QI(1)

    def jw(i, S):
        return (-1) ** len([j for j in S if j < i])

    def cre(i, st):
        o = {}
        for S, c in st.items():
            if i in S:
                continue
            T = frozenset(S | {i})
            o[T] = o.get(T, zero) + QI(jw(i, S)) * c
        return {S: c for S, c in o.items() if c}

    def ann(i, st):
        o = {}
        for S, c in st.items():
            if i not in S:
                continue
            T = frozenset(S - {i})
            o[T] = o.get(T, zero) + QI(jw(i, T)) * c
        return {S: c for S, c in o.items() if c}

    def fs(*xs):
        return frozenset(xs)

    for nu in (2, 3, 4):
        # the full Fock basis, and matrices (rows indexed by the source basis ket, columns by the target)
        allb = [frozenset(S) for k in range(nu + 1) for S in combinations(range(nu), k)]
        idx = {S: n for n, S in enumerate(allb)}
        dim = len(allb)

        # matrices as sparse dicts {(row, col): entry}; rows indexed by the target ket, columns by the source
        def opmat(op):
            M = {}
            for S in allb:
                for T, c in op({S: one}).items():
                    M[(idx[T], idx[S])] = M.get((idx[T], idx[S]), zero) + c
            return {k: v for k, v in M.items() if v}

        def mmul(A, B):
            bycol = {}
            for (k, j), b in B.items():
                bycol.setdefault(k, []).append((j, b))
            out = {}
            for (i, k), a in A.items():
                for j, b in bycol.get(k, ()):
                    out[(i, j)] = out.get((i, j), zero) + a * b
            return {k: v for k, v in out.items() if v}

        def madd_(A, B):
            out = dict(A)
            for k, v in B.items():
                out[k] = out.get(k, zero) + v
            return {k: v for k, v in out.items() if v}

        def mscal_(z, A):
            return {k: z * v for k, v in A.items() if z * v}

        def msub(A, B):
            return madd_(A, mscal_(-one, B))

        def mvec(A, v):
            out = [zero] * dim
            for (i, k), a in A.items():
                if v[k]:
                    out[i] = out[i] + a * v[k]
            return out

        def transpose(A):
            return {(j, i): v for (i, j), v in A.items()}

        def meq_(A, B):
            return not msub(A, B)

        def sparse_rank(rows):
            """Exact rank of a list of sparse vectors (dicts key -> field element) by elimination."""
            pivots = {}          # pivot key -> reduced row (dict)
            rank = 0
            for r in rows:
                r = dict(r)
                while r:
                    k = min(r)
                    if k in pivots:
                        pr = pivots[k]
                        f = r[k] / pr[k]
                        for kk, vv in pr.items():
                            nv = r.get(kk, zero) - f * vv
                            if nv:
                                r[kk] = nv
                            else:
                                r.pop(kk, None)
                    else:
                        pivots[k] = r
                        rank += 1
                        break
            return rank

        def flat(A):
            return A

        def vecd(v):
            return {k: x for k, x in enumerate(v) if x}

        ident = {(i, i): one for i in range(dim)}
        half = {(i, i): QI(F(1, 2)) for i in range(dim)}
        raw_hops = [opmat(lambda st, i=i, j=j: cre(i, ann(j, st))) for i in range(nu) for j in range(nu)]
        anns = [opmat(lambda st, i=i, j=j: ann(j, ann(i, st))) for i in range(nu) for j in range(i + 1, nu)]
        cres = [opmat(lambda st, i=i, j=j: cre(i, cre(j, st))) for i in range(nu) for j in range(i + 1, nu)]
        # the genuine so(2nu) generators: Cartan elements v_i* v_i - 1/2
        hops = [msub(H, half) if i == j else H
                for (i, j), H in zip([(i, j) for i in range(nu) for j in range(nu)], raw_hops)]
        gens = hops + anns + cres
        raw_gens = raw_hops + anns + cres
        n_expected = nu * (2 * nu - 1)
        g.check("[Prop 13.4] nu=%d: the %d hops (Cartan elements v_i* v_i - 1/2 included), %d pair annihilations and "
                "%d pair creations are linearly independent operators on the Fock space: rank %d = dim so(2nu)"
                % (nu, nu * nu, nu * (nu - 1) // 2, nu * (nu - 1) // 2, n_expected),
                sparse_rank([flat(M) for M in gens]) == n_expected)
        # closure under the bracket: every commutator lies in the span (rank unchanged); without the -1/2 the
        # bracket [v_0* v_1*, v_1 v_0] = n_0 + n_1 - 1 leaves the span of the raw elements
        base_rank = sparse_rank([flat(M) for M in gens])
        brackets = [msub(mmul(X, Y), mmul(Y, X)) for a, X in enumerate(gens) for Y in gens[a + 1:]]
        closed = sparse_rank([flat(M) for M in gens + brackets]) == base_rank
        raw_rank = sparse_rank([flat(M) for M in raw_gens])
        c01, a01 = cres[0], anns[0]
        raw_bracket = msub(mmul(c01, a01), mmul(a01, c01))
        escapes = sparse_rank([flat(M) for M in raw_gens + [raw_bracket]]) == raw_rank + 1
        with_identity = sparse_rank([flat(M) for M in raw_gens + [ident, raw_bracket]]) == raw_rank + 1
        g.check("[Prop 13.4] nu=%d: the corrected generators close under the bracket (all %d commutators lie in "
                "their span), while the raw elements v_i* v_j, v_i v_j, v_i* v_j* do not: [v_0* v_1*, v_1 v_0] "
                "leaves their span and lies in the span with the identity" % (nu, len(brackets)),
                closed and escapes and with_identity)
        vac = [one if S == fs() else zero for S in allb]
        vac_idx = idx[fs()]
        offdiag_images = [mvec(H, vac) for (i, j), H in zip([(i, j) for i in range(nu) for j in range(nu)], hops)
                          if i != j] + [mvec(A, vac) for A in anns]
        cartan_images = [mvec(H, vac) for (i, j), H in zip([(i, j) for i in range(nu) for j in range(nu)], hops)
                         if i == j]
        g.check("[Prop 13.4] nu=%d: every off-diagonal hop v_i* v_j and every pair annihilation v_i v_j annihilates "
                "the vacuum, and every Cartan element v_i* v_i - 1/2 acts on it as the scalar -1/2: hops and "
                "annihilations stabilise the vacuum ray" % nu,
                all(all(c == zero for c in v) for v in offdiag_images)
                and all(v == [QI(F(-1, 2)) if k == vac_idx else zero for k in range(dim)] for v in cartan_images))
        images = [mvec(X, vac) for X in gens]
        vec_rank = g.field_rank(images)          # dense rank over the Gaussian rationals (GA.py)
        ray_rank = g.field_rank(images + [vac]) - 1
        g.check("[Prop 13.4] nu=%d: the images X|0> of all %d generators span a space of exact rank %d = 1 + nu(nu-1)/2 "
                "(the tangent of the vector orbit), and modulo |0> of rank %d = nu(nu-1)/2 (the tangent of the "
                "orbit of Witt vacua)" % (nu, n_expected, 1 + nu * (nu - 1) // 2, nu * (nu - 1) // 2),
                vec_rank == 1 + nu * (nu - 1) // 2 and ray_rank == nu * (nu - 1) // 2)

        if nu == 4:
            # rotations as genuine exponentials: for G = v_i* v_j - v_j* v_i or v_i* v_j* - v_j v_i one has
            # G^3 = -G, so exp(theta G) = 1 + sin(theta) G + (1 - cos(theta)) G^2; at a rational point
            # (c, s) of the unit circle every entry is rational.
            c, s = QI(F(3, 5)), QI(F(4, 5))
            assert c * c + s * s == one

            def rot(G):
                G2 = mmul(G, G)
                assert meq_(mmul(G2, G), mscal_(-one, G))
                return madd_(madd_(ident, mscal_(s, G)), mscal_(one - c, G2))

            def orthogonal(R):
                return meq_(mmul(transpose(R), R), ident)

            pairs = [(i, j) for i in range(nu) for j in range(i + 1, nu)]
            hop_gen = {(i, j): msub(raw_hops[i * nu + j], raw_hops[j * nu + i]) for (i, j) in pairs}
            pair_gen = {(i, j): msub(cres[pairs.index((i, j))], anns[pairs.index((i, j))]) for (i, j) in pairs}
            hop_R = {pq: rot(G) for pq, G in hop_gen.items()}
            pair_R = {pq: rot(G) for pq, G in pair_gen.items()}
            all_orth = all(orthogonal(R) for R in list(hop_R.values()) + list(pair_R.values()))
            nontrivial = all(not meq_(R, ident) for R in list(hop_R.values()) + list(pair_R.values()))
            g.check("[Prop 13.4] nu=4: the rotations exp(theta G), formed in closed form from G^3 = -G at "
                    "(cos, sin) = (3/5, 4/5) for every pair, are orthogonal and differ from the identity; every hop "
                    "rotation fixes |0> and every pairing rotation moves it: the supplied class lies in the "
                    "stabiliser, and the pairing part of the premised half of (L_E) is the tangent",
                    all_orth and nontrivial
                    and all(mvec(R, vac) == vac for R in hop_R.values())
                    and all(mvec(R, vac) != vac for R in pair_R.values()))
            target = [zero] * dim
            target[idx[fs()]] = QI(F(3, 5))
            target[idx[fs(0, 1)]] = QI(F(4, 5))
            g.check("[Prop 13.4] the necessity witness of Cor 11.6, |00> -> (3/5)|00> + (4/5)|11>, is the pairing "
                    "rotation exp(theta (v_0* v_1* - v_1 v_0)) on one pair at (c, s) = (3/5, 4/5), applied to |0>",
                    mvec(pair_R[(0, 1)], vac) == target)
            # a hop entangles off the vacuum: the hop rotation on modes (0,1) applied to |10> gives
            # c|10> + s|01> up to sign, whose mode-0 marginal is diag(9/25, 16/25), mixed
            ket10 = [zero] * dim
            ket10[idx[fs(0)]] = one
            out = mvec(hop_R[(0, 1)], ket10)
            support = {allb[k] for k in range(dim) if out[k] != zero}
            p0_occ = sum((out[k] * out[k].conj() for k in range(dim) if 0 in allb[k]), zero)
            p0_emp = sum((out[k] * out[k].conj() for k in range(dim) if 0 not in allb[k]), zero)
            # the output is diagonal-free in mode 0's marginal because the two branches differ in mode 1 too
            g.check("[Prop 13.4 / Rem 13.5] a hop rotation applied OFF the vacuum entangles: on |10> the (0,1) hop at "
                    "(3/5, 4/5) gives a superposition of |10> and |01> whose mode-0 marginal is diag(9/25, 16/25), "
                    "mixed, although the same rotation fixes |0>: a hop cannot move the vacuum, and so cannot create "
                    "entanglement from it, but it does entangle other states",
                    support == {fs(0), fs(1)} and p0_occ == QI(F(9, 25)) and p0_emp == QI(F(16, 25))
                    and mvec(hop_R[(0, 1)], vac) == vac)


def main():
    print("verify_T05.py: exact-arithmetic checks for Transport Papers T5 (v3.1)\n")
    step1_checks()
    gauge_checks()
    limit_checks()
    step2_checks()
    atom_checks()
    lift_checks()
    lift_null_checks()
    shape_checks()
    plane_rate_checks()
    kms_checks()
    schmidt_forcing_checks()
    current_checks()
    wick_q_checks()
    capacity_checks()
    rate_model_checks()
    model_checks()
    page_noattic_checks()
    deficit_blindness_checks()
    local_univalence_checks()
    descent_checks()
    appendix_checks()
    hardening_checks()
    epoch_checks()
    ss_parity_checks()
    ss_form_checks()
    ss_univalence_checks()
    ss_kms_checks()
    ss_universality_checks()
    ss_rigidity_checks()
    ss_euclid_checks()
    ss_rate_checks()
    ss_stateclass_checks()
    ss_overdetermination_checks()
    ss_purification_checks()
    ss_dynamics_checks()
    appendix_c_checks()
    holonomy_checks()
    stabtangent_checks()
    print()
    if g.FAILURES:
        print("FAILURES (%d):" % len(g.FAILURES))
        for f in g.FAILURES:
            print("  " + f)
        sys.exit(1)
    print("ALL CHECKS PASSED.")


if __name__ == "__main__":
    main()
