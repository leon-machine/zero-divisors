# attack-EB (cluster E, angle B: adversarial and cross-pollinating), run 2026-11-10-phase1

Status: COMPLETE (attack round). Pre-registration below was written before any computation and is unchanged;
results follow it. Three proposals filed, all check4 0 errors 0 findings, validate ok, registered.

## Conventions fixed before computing
- Algebra: A = Z[G]/(c+1) of F1 to F3 (the integer Clifford algebra), base-changed to Q. The dagger is the
  linear extension of the group inverse g -> g^{-1} of G (reverse, with a sign on every generator of square c);
  <x x^dagger>_0 is then the sum of squares of the coefficients of x. This is the stored dagger of the mode-split
  claim on Cl(l,l) and it is canonical from F2, F3.
- Observable: x with x^dagger = x and x^2 = 1. State: linear phi, phi(1) = 1, phi(x x^dagger) >= 0.
- CHSH element: C = A1 B1 + A1 B2 + A2 B1 - A2 B2 with [Ai, Bj] = 0; then C^2 = 4 - [A1,A2][B1,B2].

## Pre-registered kill conditions (one per target, written first)
- E1a (is the Klein-twisted split the right two-party notion; superselection; graded product).
  Conjecture EB-1: with parity-even local observables, one mode per party gives |phi(C)| <= 2 for every state
  (the even subalgebra of one mode is commutative); with two modes per party the even subalgebras commute with no
  twist and reach C^2 = 8; in the twisted one-mode split 2 sqrt 2 is reached on an even state only with observables
  that mix parity. KILL: an exact pair of non-commuting even Hermitian involutions in one mode Cl(1,1), or failure to
  find even observables with C^2 having eigenvalue 8 on two modes per party.
  Conjecture EB-2 (signature): with four directions the value 2 sqrt 2 is reachable only in signatures (2,2) and
  (3,1); in (4,0), (0,4), (1,3) and for at most three directions in any signature every commuting CHSH
  configuration has [A1,A2] = 0 or [B1,B2] = 0, so C^2 = 4. KILL: an explicit commuting configuration with
  [A1,A2][B1,B2] != 0 in one of the excluded algebras, or the Hermitian involutions there not being the unit sphere
  of an anticommuting 5-frame (resp. the rank-two structure failing for n <= 3).
- E1b (positivity). Conjecture EB-3: the operator identity is F1 to F3 only; the bound on values is not: there is a
  normalised linear functional on the integer algebra (the PR functional) with value 4 on C, value in [-1,1] on each
  party observable and each product Ai Bj, and it fails phi(x x^dagger) >= 0 on exactly one named element. So the
  premise needed is positivity of the value functional for the group-inverse dagger. KILL: the identity C^2 = 4 - ...
  alone forcing |phi(C)| <= 2 sqrt 2 for all normalised functionals (it cannot if the functional exists), or the
  bound needing more than positivity (for example a trace or a faithful state).
- E1c (anticommutation forced?). Conjecture EB-4: for vectors (directions) of square one, value 2 sqrt 2 forces
  A1 A2 + A2 A1 = 0 as elements; for general Hermitian square-one elements it does not: a counterexample with
  {A1, A2} != 0 and phi(C)^2 = 8 on a state supported where the anticommutator vanishes. KILL: no such element pair
  exists in a small Clifford algebra (search Cl(3,1) x extra pair), or the vector statement fails.
- E2 (collapse of the attainment question). Conjecture EB-5: non-attainment over Q is a one-line rationality
  statement (value of a rational functional on a rational element is rational) and survives unnormalised states and
  ratios; what IS attained over Z is the operator statement C^2 = 8, and Q[C] is a copy of Q(sqrt 2) inside the
  algebra; C - lambda is invertible for every rational lambda. KILL: a rational state notion in which a value is not
  a ratio of rationals (then attainment must be re-examined), or C - lambda singular for a rational lambda.
- E3 (monogamy). Test only: whether the pairwise statement "two pairs cannot both exceed 2" needs positivity in the
  same named form and whether the commutation of B with C across the split survives the twist with three parties
  (two Klein twists). KILL for any EA monogamy claim: an exact state with both CHSH values above 2 under EA's own
  definitions.
- E4: findings only. Question tested: does the CHSH bound rest on the Born rule (the imported envariance Fact)
  through the value functional. No Born-rule claim will be filed.


## Orientation and routes (all targets)
Read in full: F1 to F4, signed-directions, mode-split (dagger, states rho = sum x x^dagger, Klein twist),
descent-parity-average, the one-liners of the classification, envariance Born rule, univalence superselection.
Routes considered: (R1) the problem's own: Landau identity plus positivity in Cl(2,2) with the twist (left to EA);
(R2) from another subject: the stored classification and the stored parity average / superselection results as
obstructions (which algebras and which observables allow a violation at all); (R3) own: counter-models, a
functional that keeps the identity and breaks the bound, and observables that keep the value and break
anticommutation. Chosen: R2 and R3, because they test hypotheses that R1 takes for granted (signature, parity of
observables, positivity) and each has a sharp exact kill condition.

## Results

### E1a, signature (EB-2). PROVED. Kill condition did not fire.
Proposal: synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two (filed; gate clean).
With parties = ANY two commuting pairs of self-adjoint square-one elements (no subsystem structure assumed),
dagger = blade inverse, rational or real coefficients: every CHSH configuration has [A1,A2][B1,B2] = 0, hence
C^2 = 4 and value <= 2 in every state, in exactly fourteen signatures: all with n <= 3, and (4,0), (1,3), (0,4),
(5,0), (1,4). In every other signature blades give C^2 = 4 + 4K and rational states <(1+K)(1+rC) x>_0 with values
8r for all 8 r^2 <= 1 (sup 2 sqrt 2, not attained over Q, attained once sqrt 2 is a coefficient). The excluded list
is "matrix size at most two" in the stored classification. Cl(3,0) and the spacetime algebra Cl(1,3) are excluded;
Cl(3,1) and Cl(2,2) are the only four-direction signatures with a violation. Proof is elementary (the self-adjoint
blades of an excluded algebra are one anticommuting frame per block; checked by complete enumeration for the
fourteen; n >= 7 by restriction to six generators). Classical mathematics (classification; a quaternionic
two-level system is not two rebits); transport-absent. Scope: no commuting imaginary unit.

### E1a, superselection and the twist (EB-1). PROVED. Kill condition did not fire.
Proposal: synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist (filed; gate clean).
Even observables of disjoint mode sets commute with no twist and the twisted even algebra equals the untwisted one;
a one-mode party has only +-1, +-p as even observables, so C^2 = 4; two modes per party (A1 = p1, A2 = e1 f2,
B1 = p3, B2 = e3 f4) give C^2 = 4 + 4K with even states of values 8r. The twisted one-mode split reaches 2(c+s) on
the stored even pair state (14/5, 82/29, 478/169 at rational points) but only through e1 and e2 p1, which
anticommute with the parity and are sent to 0 by the stored parity average. Without the twist: e1 e2 is
anti-self-adjoint, value 0 in symmetric states, and the self-adjoint part of the untwisted CHSH expression has
square 3. Literature (web-checked): Dasenbrook et al. NJP 18 043036 (2016); Debarba, Iemini, Giedke, Friis PRA 101
052326 (2020): a single fermionic mode pair gives no Bell violation under parity superselection, two copies do.
From memory: Wick-Wightman-Wigner 1952; Banuls-Cirac-Wolf 2007; Friis-Lee-Bruschi 2013.
Answer to "does the graded tensor product or superselection change the bound": the BOUND 2 sqrt 2 is unchanged;
what changes is ATTAINABILITY: 2 with one even mode per party, 2 sqrt 2 from two modes per party.
Caught while drafting: over real coefficients positivity does not imply phi(x^dagger) = phi(x); clause (v) carries
that as a hypothesis.

### E1b, positivity (EB-3), and E1c, anticommutation (EB-4). PROVED. Kill conditions did not fire.
Proposal: synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state (filed; gate clean).
- lambda(x) = <(1 + C) x>_0 on Cl_Z(2,2) is integer-valued, normalised, symmetric, gives probabilities 0 or 1/2 at
  every setting pair with marginals 1/2 (no signalling) and lambda(C) = 4: the PR box as a functional on the integer
  algebra. lambda((C - t)^2) = t^2 - 8t + 4 < 0 for t = 1..7. The bound phi(C)^2 <= 8 uses positivity on exactly
  (C - t)^2 and (1 - K)^2. So the premise is: the value functional is non-negative on x x^dagger for x that add
  products across setting pairs. PROVED as a counter-model for "algebra plus linearity plus per-context
  probabilities"; that no stored premise supplies positivity is ARGUED, not audited over the store.
- Anticommutation: forced as an identity for directions with scalar anticommutator (EA's result; I verified the
  certificate 8 - C^2 = (Z^dagger Z + {A1,A2}^2 + {B1,B2}^2)/2 and (C^2 - 4)^2 = 16(1 - g^2)(1 - h^2) independently on
  three exact cases, not filed). NOT forced for general observables: A2' = e1 P+ + p1 P-, P+- = (1 +- p3)/2, has
  {A1, A2'} = 1 - p3 != 0 with rational states of C^2-value 8.
- Is it more than Tsirelson restated: no. Identity (Landau), bound (Tsirelson), box (Popescu-Rohrlich), rigidity
  (Summers-Werner) are all classical. What the three proposals add is placement in the series' algebra: the
  signature list, the parity-even statement against the stored twist, and the counter-model on the integer algebra.

### E2 (EB-5). Findings only (EA owns the Pell sequence). Kill condition did not fire.
- PROVED (one line): any value of a rational functional on a rational element is rational, so 2 sqrt 2 is never a
  value over Q; unnormalised states change nothing (ratio of rationals).
- PROVED (in the signature proposal): the value set contains every 8r, r rational, 8 r^2 <= 1; so every rational in
  (-2 sqrt 2, 2 sqrt 2) is a value, with fixed integer directions; no Pell structure is needed for the supremum.
- PROVED: the operator statement IS attained over Z: C^2 = 4 + 4K, C^3 = 8C, C^2 = 8 on the block K = 1, so Q[C P]
  is a copy of Q(sqrt 2) inside the corner algebra. The obstruction to attainment is exactly that 2 is not a rational
  square; Q(sqrt 2) suffices, F4 is not needed (not even a Euclidean field).
- COMPUTED: with integer A-directions (p1, e1) and diagonal B-directions the CHSH element is even and its
  saturating state is the stored even pair state rho = (1 + p1p2 - e1f2 - f1e2)/4, which is RATIONAL; the
  irrationality then sits in the unit B-directions (p2 +- e2p1)/sqrt 2 only. With integer B-directions it sits in
  the state. It can be moved, not removed.

### E3. Not attacked computationally (EA had filed nothing on E3 when I read its file). ARGUED: with parity-even
observables three parties need two modes each and the even subalgebras commute pairwise, so the ordinary proof
applies; with odd observables three parties need nested twists (B by Gamma_A, C by Gamma_A Gamma_B), which the
stored twist theorem covers only for two parts.

### E4. Findings.
The CHSH bound on VALUES rests on positivity of one functional on the whole joint algebra. That is the content of
the Born rule for joint (entangled) measurements, not for the local ones: lambda is fine on every local context.
The stored Born account (imported envariance) presupposes probabilities exist and add; lambda shows that "exist
and add in every local context, linearly across contexts" does not give positivity. So a phase 2 Born derivation
must produce non-negativity on all self-adjoint idempotents of the joint algebra, or it does not give Tsirelson.

## Where EA is exposed (read: findings/attack-EA.md and its filed E1 proposal title and summary)
1. Scope: EA's bound is realised in Cl(2,2) only. "Two subsystems of a Clifford algebra" overstates: in Cl(3,0),
   Cl(4,0), Cl(1,3), Cl(0,4) no commuting configuration exceeds 2. Title and one-liner should carry the signature.
2. EA's two parties use e1 and e2 p1, parity-odd observables, and EA records its saturating state as not
   parity-even. Under the stored parity average these observables vanish and the one-mode value is at most 2.
   Also: "the saturating state is not even" is configuration dependent; for A = (p1, e1), B diagonal, the
   saturating state is the stored even pair state.
3. EA calls positivity a definition (and "premise in substance"); the box functional makes it a premise in fact.
4. EA's refinement inequality and certificate: tested, sound (the Cauchy-Schwarz step is safe because the two
   commutators commute, so no symmetry of the state is needed).

## Unexpected links
- transport.classification-real-clifford-algebras decides CHSH: violation exists iff matrix size >= 4. The physical
  signatures split: Cl(1,3) no, Cl(3,1) yes (compare synthesis.positive-energy-selects-rule-2-sign and any stored
  signature choice).
- singularity.descent-parity-average and singularity.imported-univalence-superselection-rule: the descent keeps
  exactly the observables for which the Klein twist is idle; the mode-split theorem's twist is then needed only for
  states, not for observables.
- The stored eviction pair state (mode-split clause (v)) at equal weights is a CHSH-saturating state.
- Tsirelson's own construction realises extremal correlations with Clifford generators: the F2 group of signed
  directions is that construction's group; nothing new, but it is why the foundation reproduces the bound verbatim.
- one-relation.imported-envariance-born-rule: see E4.

## Decisions for Leon
1. Positivity premise. Adopt, as a named premise, "values are given by a linear functional non-negative on
   x x^dagger (dagger = blade inverse)", or keep it as a definition inside each claim. Recommendation: name it; the
   box functional shows it has content. This is the same decision phase 2 (Born) needs.
2. Are parity-odd elements observables? If no (univalence superselection applied to observables, the descent's
   image), one mode per party is local and CHSH needs two modes per party; EA's realisation then needs restating
   on four modes. If yes, the Klein twist is part of the definition of a party. Recommendation: state both, make
   the even two-mode realisation the headline since it needs no twist and no choice.
3. Signature. F2 leaves the signature free; the CHSH statement is false in fourteen signatures including Cl(3,0)
   and Cl(1,3). Decide whether the headline is stated for Cl(l,l) modes only (recommended) or for a signature list.
4. Imports to consider (maintainer-only): Dasenbrook et al. 2016 and Debarba et al. 2020 as Facts; Landau 1987,
   Tsirelson 1980, Popescu-Rohrlich 1994, Summers-Werner 1987 are cited from memory in my notes.
5. Complex coefficients: all three results are for rational or real coefficients; with a commuting imaginary unit
   the signature list changes (for example Cl(3,0) with complex coefficients is still size two, but Cl(4,0) becomes
   M_4(C)). Not done; say if wanted.
