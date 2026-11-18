# Referee report, group B (horizons), run 2026-11-18-leads

Read: REFEREE.md (common part, Group B), colony/BRIEF.md (Standards, referee role), POLICIES.md section 2, the two
proposal folders, the cited store entities at their pinned versions, and the check4 logs. Not read: findings/,
work/, RUN.md, ATTACK.md, LEADS-source.md. Scratch scripts are in /tmp/referee-B/ (b1_perturb.py, b1_own.py,
b1_helical.py, b2_ricci.py, b2_recon.py, b2_perturb.py). Every computation uses exact Fractions; no sympy.

check4 logs: both proposals `0 error(s), 0 other finding(s); check result: pass` (EXIT 0 in check4_summary.txt).
runcheck: B1 five PASS (1.8 s), B2 five PASS (11 s).

---------------------------------------------------------------------------------------------------------------

## B1. synthesis.tube-point-clause-fixes-no-observer-where-rotations-have-no-fixed-point

**Verdict: OVERSTATED.** (i), (ii), (iii), (v) and (vi) are correct, and I recomputed them. (iv) and the closing
paragraph ("in every gauge where the clause can be read", "these are the gauges in which K generates a symmetry
... the hypotheses of the clause") claim more than the proof gives. The adapted-gauge definition adds a hypothesis
the stored clause does not have: that K generates the flow of the horizon's Killing field, xi/kappa. The stored
clause only asks that K generate *a* symmetry. There are gauges that meet the clause's hypotheses, are not
adapted, and in which observers of U do meet the condition (counterexample below).

**True weaker statement.** Take a gauge in which K generates a positive multiple of the horizon Killing field xi
(the normalisation by kappa is not needed) and the symmetries commuting with K act by bivectors. In every such
gauge the so(3) is so(3)_I, and no compatible tube point whose observer lies in U is fixed by it. Hence for
Schwarzschild, and for Schwarzschild-de Sitter with either horizon, the clause *read with K the horizon's Killing
flow* is met by no observer of U. (v) and (vi) are unchanged.

### Counterexample to "every gauge where the clause can be read"
Start from an adapted gauge (iv), with chart (eta, sigma, n). Pick J in so(3)_I, for example J = e3 e4 when
I = e+. Displace by psi(eta, sigma, n) = (eta, sigma, R_J(-c eta) n), c != 0. This is a diffeomorphism of the
wedge and so a displacement (Definition, clause (e)). Conjugating the old boost by psi gives the boost composed
with the rotation R_J(-c tau). So in the new gauge:
- K generates the symmetry xi/kappa + cJ;
- J commutes with psi and stays a bivector;
- xi/kappa = K - cJ is linear too;
- the other rotations become eta-dependent and nonlinear, but they do not commute with K.

So every symmetry commuting with K (the span of K and J) acts linearly, and the clause's hypotheses hold.
Modulo K, the transverse symmetry is J. That is the reading the stored de Sitter theorem uses: "fixed by the three
transverse symmetries", with K left out. J fixes every wedge point on its axis (n = +-e-, any sigma > 0;
b1_helical.py confirms null and fixed at sigma = 3/5 and 5/13). By (ii), J fixes the tube points of those
observers. So in this gauge the clause is met by every observer of U on the rotation axis. It fixes the foot and
leaves rho free along the axis.

Physically this K is a helical Killing field with no bifurcate Killing horizon at r = 2M. So "the wedge's boost is
the horizon's Killing flow" is a natural reading. But it is a premise reading the proof needs, and it is not what
the clause says. It belongs in decision (1).

### Two further reading issues the proposal should state
1. **The literal clause can never be met.** The clause asks that m be invariant under *every* symmetry commuting
   with K, and K is one of them. K moves every compatible tube point: K . X(m) = I7 rho K.u, which is not a
   multiple of X(m). The proposal's own check asserts `not fixes_tube(K, ...)`. So read literally, the clause is
   met in no field, de Sitter included. The store (de Sitter theorem (ii), clause "What it is for") reads it as
   invariance under the transverse symmetries. The closing paragraph should say "the symmetries commuting with
   the boost other than the boost" (transverse).
2. **A third reading of non-linear rotations.** The parenthesis in (iv) says that where the rotations are not
   bivectors, "the clause's condition is not defined for them". The words "acting on tube points
   complex-linearly" in the clause can also be read as a restriction: only the linearly acting symmetries count.
   Then in a gauge where K = xi/kappa but the rotations are made nonlinear (a sigma-dependent rotation
   displacement), the condition is vacuous and every observer meets it. So the outcome depends on the gauge under
   that reading. The proposal should list this as a third reading. The stored clause is not gauge-covariant as
   worded, and the maintainer should know this.

### Clause-by-clause
- **(i), point (a).** Correct, and it is not a confusion of uniqueness up to conjugacy with equality.
  - K is central in the 7-dimensional commutant, so a perfect subalgebra g lies in biv(T).
  - Complete reducibility gives the faithful real 4-dimensional options: 4 (spin 1/2, quaternionic) or 1 + 3.
  - For the quaternionic 4, the symmetric invariant forms are Re(x-bar y q) with q real, so they are definite. I
    checked this.
  - So every compact so(3) in so(1,3) is literally the stabiliser of the timelike line it fixes. The non-compact
    so(1,2) is not isomorphic to so(3), so it is excluded.
  - Translation formula and Lambda_I = 12 alpha^2/Q(I): rederived by hand.
  - Own route (b1_own.py): conjugate the standard so(3) of e+ by two rational T-boosts and a T-rotation. The image
    annihilates the image I, commutes with K, and has alpha = 53/15, foot (16/53, 60/53) and rho^2 = 225/2809 =
    Q(I)/alpha^2. The Y = I/alpha it predicts is fixed.
  - Uncited standard Lie theory is used in a proof step (classification of real irreps of su(2), complete
    reducibility). It should be labelled as standard.
- **(ii).** The proof is correct: B in biv(T) kills e1 and e2, so lambda rho u = 0 forces lambda = 0. For Q(I) < 0
  and Q(I) = 0 the arguments are fine.
- **(iii).** The bijection onto the right wedge is correct. One point is missing from the proof: the n_O
  coefficient of I-hat + sigma n is positive (same half of the cone), so every (eta, sigma, n) gives a finite
  wedge point. It is one line and should be added.
- **(iv).** See above. The existence construction and the dilation argument are right: Q(I') = Q(I) and
  Lambda_I' = s^2 Lambda_I.
- **Point (c), de Sitter.** With I = I_Lambda (alpha = Lambda/6, beta = 1, c = 0), (ii) gives rho^2 = 12/Lambda
  and Lambda_I = Lambda, which reproduces the stored (ii).
  - "Lambda_I is a datum of the gauge" is consistent with the store, but it holds in de Sitter too: under the
    dilation the de Sitter field becomes h = s^{-1} sigma_{s^2 Lambda} a, and the chart value moves with it (stored
    (viii)).
  - What actually separates the cases is that in de Sitter the fixed orbit lies in U (sigma_dS = 2 there). The
    text should say that instead of implying chart-dependence is special to black holes.
- **Point (d), recomputed by hand.**
  - Sample: f = -(r-1)(r-2)(r+3)/(7r), kappa_b = 2/7, kappa_c = 5/28, ratio 8/5.
  - r_0^3 = 3M/Lambda = 3, and f(r_0) = 1 - 3M/r_0, so (1 - f)^3 = 9 Lambda M^2 = 243/343.
  - 36/25 < r_0 < 13/9 gives exactly 3/28 < f(r_0) < 10/91, and f(r_0) is about 0.1086.
  - Schwarzschild: N = 4M sqrt f, and the acceleration is M/(r^2 sqrt f).
  - Hidden step: for general f the connection form omega^0_1 = (f'/2 sqrt f) theta^0 is only checked at three
    sample points, while the cited Fact covers f = 1 - 2M/r only. It is a one-line Cartan computation
    (d theta^0 = (f'/2 sqrt f) theta^1 ^ theta^0), and the proof should give it.
- **Point (e), closing paragraph.** Within what is proved only under the horizon-flow and transverse readings.
  "Fixes neither a foot nor a scale" fails in the helical gauge, which fixes a foot.
- **Status.** "proved" is right for (i) to (iii), (v) and (vi). It is right for (iv) and the closing paragraph only
  after the scope fix.
- **Overclaiming.** The one-liner and technical level repeat "in any gauge where the tube-point clause can be
  read" and need the same fix. The title is acceptable once the scope is fixed.
- **Circularity, duplication, literature.** No circularity: the clause is lineage only, not used. No duplicate in
  the store. Tolman is used in a remark only.
- **Store consequence.** The stored clause says "It decides fields with one horizon only", and op.which-capacity
  says "decided for one-horizon fields". Schwarzschild is a one-horizon field that the clause does not decide.
  Both texts need rewording if this result is accepted.

### Perturbations (b1_perturb.py)
- rho^2 = Q(I)/alpha instead of Q(I)/alpha^2: FAIL (caught).
- kappa_c = 5/27: FAIL (caught).
- Replacing the complex-multiple branch of `fixes_tube` by `return True`: still PASS. That branch never runs on
  the samples, because [B, Im X] = 0 for B in T. This is harmless but dead code: the check tests only B . Re X = 0.

### Fixes that matter
1. Restrict (iv) and the closing paragraph to gauges in which K generates a positive multiple of xi (the horizon
   Killing flow). Delete "these are the gauges in which ... the hypotheses of the clause". Add the helical-gauge
   remark.
2. Say "symmetries commuting with K other than K" (the transverse ones).
3. Add the vacuous reading of non-linear rotations to decision (1).
4. Prove the general-lapse connection form in the proof. Label the Lie-theory facts as standard.
5. Flag the stored clause and op.which-capacity wording ("decides one-horizon fields") as now inaccurate.

---------------------------------------------------------------------------------------------------------------

## B2. synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations

**Verdict: SOUND WITH FIXES** (wording and scope; the mathematics checks out).

### Point (a): what is identical, what is at M = 1
- (1) and (2) are identities in z = sqrt f and the polar angle at M = 1, over a full basis of second-order jets.
  The linearity-in-jets argument is complete: Omega_1 is algebraic in the 1-jet of k, so R_1 is linear in the
  2-jet. The ring argument (division by units only) makes each equality hold for all r > 2M and all sin theta != 0.
- (4) and (5) are identities of linear forms over A = Q[r, lambda, w][...] at M = 1, for arbitrary functions.
- General M comes by homogeneity. The weights stated are: t, r, M weight 1; H0, H1, H2, K weight 0; Phi, Psi
  weight 1; V_e weight -2. One weight is missing: omega has weight -1 (w = omega^2 has weight -2). I checked that
  Rel, a, b, E4 = -(r d_r + a)Z and E7 = -Z'/2 + bZ are homogeneous with these weights.
- The GTG step "dilation carries the mass-M field to a constant multiple of the mass-aM field" is asserted, not
  derived. It is correct: the coordinate metric scales by a^2 and frame Ricci components by a^{-2}. My independent
  checks at M = 7/5 and M = 2 confirm it. The argument is complete once the omega weight is added.

### Point (b): independent exact verification, by my own route
- **b2_ricci.py.** Standard metric perturbation theory with Christoffel symbols, written from scratch. It uses
  exact jets in (t, r, theta) over dual numbers, at M = 7/5, r = 9/2, sin theta = 5/13, with random rational
  2-jets of H0, H1, H2, K and a generic P. The background Ricci is 0. All seven independent nonzero frame
  components agree with the proposal's closed forms (C00, C01, C11, C02, C12, C22, with the Delta P and P'' terms),
  with a uniform ratio of -1, which is the store's curvature sign. The (t,phi), (r,phi) and (theta,phi) components
  vanish. This confirms (1) by a route that does not use lib/gtg.py, and at M != 1.
- **b2_recon.py.** Generic polynomial Phi (Z[Phi] != 0), (M, lambda) = (7/5, 5/3) and (2, 2), r = 9/2 and 23/4.
  The following are exact: Psi - (lambda+1)Phi = 0, E3 = 0, E4 + (r d_r + a)Z = 0, and E7 + Z'/2 - bZ = 0. With
  f/r^2 added to V_e, E4 and E7 fail.

### Point (c): (C3)
- As stored, (C3) says: "every solution of the Zerilli equation in an oscillating channel is the function Psi of
  an even-parity vacuum solution". Clause (4) gives exactly this, and more (no time restriction), with
  Phi = Psi/(lambda+1). The restriction to L > 2 (lambda > 0) excludes l = 0, 1, and clause (3) needs
  L not in {0, 2}.
- (6) describes (C3) as "the surjectivity of (4) together with the injectivity of (5)". The stored (C3) is the
  surjectivity alone. The injectivity and the forward implication are what the stored clause (5) needs on top of
  it. Reword.

### Overstatement to fix
(6) says the stored clause (3) "is superseded by (5)". But (5) proves vacuum => Zerilli only on oscillating
channels. The stored (3) is the time-general implication, at sample points, and that implication is still not
proved identically. Write "superseded on oscillating channels".

A note in the other direction: real omega is not needed. The identities of (5) are algebraic in w with w^{-1}
inverted, so they hold for every omega^2 != 0. That restriction is harmless.

### Point (d): (C1) and (C2)
Neither enters any step of (1) to (5). They enter only the phrase "every even-parity channel" in (6), where the
axisymmetric representative (m = 0) also needs (C1). That is labelled, but (6) should carry "given (C1) and (C2)"
inside the clause, as the stored theorem does.

### Point (e): GTG setting
The first-order field is the stored one:
- `lin_ricci` is byte-identical to the stored check's;
- the k_mu are the stored (3)'s Regge-Wheeler ansatz;
- the background is gtg.static_field.

The proof stays in the GTG variables. The metric is given only as a reading. Zerilli, Moncrief and Lousto-Price
are cited from memory and not used as input: the reconstruction formulas are verified exactly, so memory carries
no weight.

### Proof steps checked
- (3), including the P = C cos^{L/2} theta argument for L not in {0, 2}.
- The bijection logic of (5): injective via the reduction of (lambda+1)(K, H, H1) - recon(Psi) without Rel;
  surjective via (4), whose operators commute with d_t.
- "Regular on r > 2M": every inverted element of A is nonzero there.

Status "proved" is right for (1) to (5). (6) is proved given the cited (C1) and (C2), as stated. There is no
duplicate in the store and no circularity: (C3) is not used.

### Perturbations (b2_perturb.py)
- C22 coefficient of (H2 - K)/r^2 halved: (1) FAIL and (4) FAIL.
- Coefficient a in H1 changed (-3 lambda r to -2 lambda r): (4) FAIL.
- V_e constant 18 changed to 19: (4) FAIL and (5) FAIL.
- d_t^2 = +w in the reduction rule only: (5) FAIL. This is expected, since the system's right-hand sides carry
  -w. It is not evidence that the sign matters.

### Fixes that matter
1. (6): "clause (3) superseded" -> "superseded on oscillating channels". The time-general forward implication
   remains computed at samples.
2. State that omega has weight -1 in the homogeneity paragraph.
3. Reword the description of (C3), and put "given (C1), (C2)" inside (6).
4. Optional: drop "real" from omega, since any omega^2 != 0 works.

Decision (1) of the proposal, narrowing joint J3, is supported for even-parity spin 2 on oscillating channels,
given (C1) and (C2).
