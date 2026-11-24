# Attack P-B (adversarial and cross-subject), run 2026-11-24-three-routes

Problem: op.positivity-of-values. Labels: PROVED / COMPUTED / ARGUED / CONJECTURED. Scripts in
colony/runs/2026-11-24-three-routes/work/P-B/. Nothing under store/ is edited.

## Orientation (lookups done)
The problem record; synthesis.premise-positivity-of-values (v2); the two recording premises and supervenience;
singularity.p-univalence; (Q), (N+), (KF), indifference (two forms), the full list of 73 stored postulates; the BRST
result that motivates (KF); earlier findings: 2026-11-10-phase2 attack-BB (the family lambda_c, the record map),
2026-11-18-leads attack-L2 (additive weights on two modes; lead 4 reduced independence to "which projectors label a
record").
What is already settled and not redone: on two modes, one twisted mode per party, the functionals
lambda_c = <(1 - U - V + cK)x>_0 agree on all nine local products and satisfy (P) only at c = -1 (stored, clause (iv));
with all rational projectors as record labels and non-negative additive weights, the weights are a state (stored).
What was left "argued, not audited": that the stored recording premises speak only of local values.

## Routes
- R1 (the problem's own, independence): extend the stored counter-model to a model of the premise set. Delivers a
  two-model independence statement. Needs: an audit of every stored postulate against the model; a model that
  survives many copies (records on many pairs). Fails if some stored premise speaks of the value of a non-local
  element.
- R2 (from another subject: the unit principle and the orientation datum of (N+)): the two-mode algebra is a real
  matrix algebra, and real algebras are not locally tomographic: the reversal (the adjoint) applied on one party's
  algebra only fixes every product of local self-adjoint elements. So for every state omega the functional
  omega o Gamma_B has the state's values on every local record at every number of modes. Delivers: the independence
  model in general form, and a sharpening of the stored family (which of the lambda_c survive two copies).
  Fails if Gamma_B is not well defined or moves a local product.
- R3 (own, against the "why" of the problem): the quantum bound without (P). Macroscopic locality (Navascues and
  Wunderlich 2010, from memory) and "local quantum measurements plus no signalling give quantum correlations" (Barnum,
  Beigi, Boixo, Elliott, Wehner 2010, from memory): positivity of one party's conditional values given the other
  party's record should already give lambda(C)^2 <= 8, at any number of modes. Fails if a functional with positive
  conditional values exceeds the bound.
Choice: R2 as the main line (it decides R1 on a stated scope and is exact), R3 beside it (it says what of (P) the
CHSH results need); then the three-mode search (kill condition P1) and the two cross-subject lookups.

## Kill conditions, registered before computing (24 November, before any script was run)
- K-B1. R2 is dead if, in Cl_Q(4,4) with two modes per party (Bob's twisted by Alice's parity), the multiplication
  map from (Alice's algebra) x (Bob's algebra) is not a bijection onto the algebra, or the reversal on Bob's side
  moves some product of a self-adjoint element of Alice's algebra and one of Bob's, or lambda_{-1} o Gamma_B is not
  lambda_{+1} on two modes, or lambda_{+1} satisfies (P).
- K-B2. The claim "two copies cut the stored family to its end points" is dead if lambda_c x lambda_c has no negative
  weight on a product of a projector of Alice's two modes and one of Bob's for some |c| < 1. Predicted before
  computing: the weight (c^2 - 1)/16 on a product of two atoms.
- K-B3. R3 is dead if a linear normalised functional exists whose conditional functionals on Alice's algebra, given
  each of Bob's four outcomes, are non-negative on hermitian squares and which has lambda(C)^2 > 8.
- K-B4 (run kill condition P1 on a finite family). On the 3280 rays of Q^8 with entries in {0, 1, -1}: if the
  functions that are quadratic forms over the norm on every four-dimensional subspace similar to the standard one
  found in the family form a space of dimension above 36, the family does not decide; P1 itself fires only for a
  function on all rational projectors, which a finite search cannot produce. Dimension 36 means: no counterexample
  can be seen on this family.
- K-B5 (Krein form against (P)). "One premise in two places" is dead if the Krein adjoint of a ghost floor has an
  indefinite trace form (then it is the blade inverse of no split); "conflict" is established if a vector of positive
  Krein norm gives a negative value to a hermitian square of the floor.
- P4 (the run's): fires if a functional violating positivity satisfies every other stored premise, the recording
  premises included.


## Results

Scripts: work/P-B/rev.py (reversal, two copies, certificate, Krein adjoint; 31 exact checks, all pass), ml.py (Gram
criterion), p1_search.py, p1_glue.py, p1_glue2.py (three-mode family). Proposal folder staged in work/P-B/gate/.

### FILED (one proposal): synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them
check4: 0 errors, 0 other findings (on the staged copy and on proposals/<id>); validate_draft ok (E610, the ORCID
warning, is environmental). Ledger: transport-absent. No assumes edge; (P) is not used. Six check functions.
Setting: Cl_k(l,l), l = m + n modes, party 1 holds m modes (algebra A), party 2 the rest through the twisted
generators (algebra B, commuting with A; the multiplication A x B -> Cl is a bijection).
- (i) PROVED. For self-adjoint A_0, A_1 in A and B_0, B_1 in B of square 1, S = A_0 + A_1, D = A_0 - A_1,
  F_+- = (1 +- B_0)/2, G_+- = (1 +- B_1)/2, and every t:
  4 + 2t^2 - 2tC = (S - t)^2 F_+ + (S + t)^2 F_- + (D - t)^2 G_+ + (D + t)^2 G_-, each term y y^dagger with y = sF.
  A certificate linear in C (the stored one is for 8 - C^2 and uses squares that mix both parties' settings).
- (ii) PROVED. Hypothesis (CP): lambda linear, normalised, non-negative on the elements s^2 F (one party's
  self-adjoint element squared, times an outcome idempotent of the other). Then lambda(C)^2 <= 8 (t = lambda(C)/2),
  strict over Q, in any ordered field, at any number of modes, for any observables of square 1. (P) => (CP);
  stored (L) => (CP) for one mode per party. The box functional has -1/2 on each of the four squares at t = 1.
- (iii) PROVED given the stored two-mode theorem on additive weights (version 1). For a party of two modes: weights
  mu(EF) on products of that party's rational projectors E with the other party's four outcomes F, non-negative,
  additive in E on orthogonal projectors and with marginals independent of the other's setting, give V^2 < 8 for
  the sum V of the four recorded correlators. No linear functional and no non-local projector is assumed.
  COMPUTED instance on three modes with a density that is not a state: V = -14/5.
- (iv) PROVED. The reversal theta(ab) = a b^dagger on party 2's factor is a well-defined linear involution, commutes
  with the adjoint, with parity and with local sector averages, and fixes ab whenever b is self-adjoint. So for
  every linear lambda, lambda o theta is linear, normalised, real and even when lambda is, and has lambda's values on
  every product of one observable of each party and lambda's weight on every sequence of local records (and (CP)
  holds for both or neither), at every number of modes. CORRECTED in the fix round: it does NOT have lambda's
  values on every product of local observables; X_1 Z_1 X_2 Z_2 = -K is negated (values 1 and -1).
- (v) PROVED. On two modes lambda_c o theta = lambda_{-c} for the stored family: lambda_{+1} is the reversal of the
  state lambda_{-1}; weights -1/2, 1/2, 1/2, 1/2 on the joint outcomes of U, V; inertia (12,4,0). Two copies shared
  by the same parties: the weight of (joint-outcome idempotent of party 1's two modes)(the same for party 2) is
  (1 + ss' + tt' + ss'tt' c^2)/16, so (c^2 - 1)/16 or (1 - c^2)/16 is negative unless c = +-1. Two copies cut the
  stored one-parameter family to its end points: the state and its reversal.
- (vi) PROVED for k = Q, two modes. A linear lambda is non-negative on all x x^dagger iff ONE atom has non-negative
  weight after every unitary (u u^dagger = 1). Instance: the self-adjoint unitary u = (1 + Z_2 + X_1 - X_1 Z_2)/2
  carries the local atom (1 + Z_1)(1 + X_2)/4 to the joint outcome (1 + U)(1 + V)/4, where lambda_{+1} has -1/2.
- (vii) PROVED. With the field theory's unit I_4 (commuting with mode vectors, I_4^dagger = -I_4), I_4 Y_1 and
  I_4 Y_2 are commuting self-adjoint elements of square 1, one per party, with product K: the separating blade is
  then a product of local observables.
- Reading (ARGUED, stated as argued in the entity): the bound needs only local records; no condition on local
  records gives (P); what separates a state from its reversal is a record of a non-local projector, equivalently a
  local record after a unitary that mixes the parties' modes.
What is NOT new and is said so in the entity: that a real two-party algebra is not fixed by local data (Wootters;
Hardy and Wootters; Caves, Fuchs and Rungta; from memory), and that functionals non-negative on products of local
effects give quantum correlations for two parties (Barnum et al. 2010, from memory). New relative to the store:
the general reversal at any number of modes, the certificate, the cut at two copies, clause (iii), clause (vi).
Relation to P-A's second proposal (synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes):
it bounds the sum of correlators under (RP) on the algebra of BOTH parties (two modes in all); clause (iii) here uses
records of one party's projectors only (that party holding two modes) and so holds for the reversed functional too.
Related, not duplicates; flagged for the orchestrator's duplicate list.

### Independence (kill condition P4): the audit of the 73 stored postulates
Scope S of the two-model statement: the algebra of finitely many modes shared by two fixed parties, and value
assignments on it. Model 1: a state omega of (P) (for two modes lambda_{-1}). Model 2: omega o theta (lambda_{+1}).
The mathematics is PROVED (clauses (iv), (v)); which stored premise says what about values is a READING (ARGUED):
the premises are prose and the store has no formal semantics for "record".
| premise(s) | what it says about values on S | model 2 |
| F1, F2, F3, F4 | supply the algebra and the coefficients; nothing about functionals | passes |
| one-relation.recording-irreversible-stated-so-it-can | records are not unwritten; no weights, no sign, no list of record projectors | passes (nothing to test) |
| one-relation.recorded-sectors-superselected-premise | no interference between recorded sectors; formalised as value after record = lambda o E_o | passes: theta commutes with E_o for local o; after complete local records on both sides the two models coincide and are states |
| one-relation.supervenience-stated-so-it-can-be | a subject is a record chain; nothing about values | passes |
| singularity.p-univalence | states of the boundary modes are even | passes (omega o theta is even when omega is); on S a symmetry condition |
| scrambling.indifference..., dark-matter.p2-indifference, the imported indifference instrument | no uncaused distinctions: equal weights along exact symmetry orbits | passes for local symmetries: theta commutes with conjugation by local unitaries, so model 2 has model 1's local symmetries |
| dark-matter.premise-cpt-covariance, dark-matter.premise-flag-as-datum, synthesis.tube-point-clause... | covariance or invariance conditions on structures and states | pass on S (same argument; they name no value of a non-local projector) |
| singularity.r-regularity-fixed-locus, synthesis.r-lambda-... | single-mode marginals are KMS | pass (marginals of the two models are equal) |
| singularity.q-joint-quasi-freeness-s-wave, synthesis.n-plus-null-ground-state, synthesis.hadamard-deposit-premise, synthesis.c-loc-local-horizon-premise (its KMS clause), singularity.rate-models-kinematic-inputs-l-u (purity (U), injection (I) of a thermofield pair) | each NAMES a positive state of a named system (boundary-mode array, horizon generators, the deposit, window and radiation) | FAILS there: these premises contain positivity for their systems, so on those systems (P) is not independent of them. They say nothing on a laboratory pair not in the named state |
| synthesis.krein-form-premise... | an indefinite form on gauge, ghost and regulator modes, positive on the BRST cohomology | not a premise about (P)'s adjoint; see cross-subject below |
| singularity.l-boundary-mode-locality | boundary-mode dynamics is number-diagonal (no hopping) | relevant to clause (vi): where it holds no unitary mixes the modes; it is stated for boundary modes only |
| the other 50 (free inputs, dark-matter counting rules, simulation specifications, mass-law and neutrino premises, geometric premises C1 to C3, (R) rung reading, (FS), Kasner premises, tameness, slot and face hypotheses, H1, H2, (S), (U) of T14 and T14c, (EW), (IC), P1, P3, P5, D, E, R1 to R3, SI, Pop, J3, (I) interface, (C) constituent, common ceiling, window reading) | no statement about values on a mode algebra | pass vacuously |
Outcome. P4 FIRES on scope S, in this qualified sense: a functional that violates positivity (the reversal of a
state) satisfies every stored premise other than (P) as far as those premises speak about a laboratory pair, the
recording premises included, because none of them names the weight of a projector that is not a product of local
ones, and none says which projectors can label a record. It does NOT fire for the whole store as a formal theory
(the premises are not formal), and it does not fire on the systems whose state a premise names (row 9). The model is
fragile in one stated way (clause (vi)): one unitary that mixes the two parties' modes followed by a local record
gives it a negative weight. So the independence of (P) on S is equivalent to the absence of a premise that such
joint records exist with non-negative weights. That is the same fork as Leon's decision D1 of 18 November and as the
hypothesis (RP) of P-A, now with both branches carried by proved statements: with joint records, (P) on two modes
follows from non-negative frequencies (clause (vi) for linear values; P-A's theorem for weights); without them,
(P) is independent and invisible to every local record at every number of copies.
The box functional is NOT the independence model: it satisfies the recording premises only if the recordable
settings are restricted to its four pairs (weights there are 0 and 1/2; stored), it fails (CP) (-1/2 on each
square, COMPUTED), fails non-negative weights at local directions outside its four (-1/10, stored), and singling
out four directions among the directions of a mode is a distinction nothing determines (indifference; ARGUED).

### Macroscopic locality (Navascues and Wunderlich 2010; prior art cited from memory, flagged)
- Do the stored recording premises imply that coarse counts over many records are classical? NO (ARGUED from the
  wording, with a COMPUTED model). The premises give, for each recorded context, records that are permanent and
  sectors that do not interfere. A joint distribution for coarse counts of settings that are never recorded together
  is not asserted anywhere. Model: N copies of the box, each run recorded at one of its four setting pairs. Every
  run has a non-negative multinomial distribution of records, so the recording premises (formalised as above) hold;
  the limiting Gaussian coarse counts have covariances (1, 1, 1, -1), and no joint Gaussian exists: the matrix W_t
  of ml.py is positive definite at t = 3/2 and pairs to 4t - 2*4 = -2 with every candidate covariance matrix
  (COMPUTED, exact). So the box with four recordable settings is compatible with the recording premises and
  violates macroscopic locality.
- Would macroscopic locality give 2 sqrt 2 without (P)? YES as an added premise (the Gram criterion gives
  C <= 2t for every rational t with t^2 >= 2; the same W_t certifies it; ARGUED from the criterion as remembered, the
  certificate COMPUTED). But it is not needed: (CP) of the filed result gives the bound directly, is a condition on
  single records rather than on a limit of many, and implies the Gram criterion (ARGUED: Gram vectors
  rho^{1/2} A_x and rho^{-1/2} sigma_y, over the reals).
- Macroscopic locality cannot give (P): it is a condition on local records, so the state and its reversal satisfy
  it together (PROVED as a consequence of clause (iv)).

### Kill condition P1 (three modes), on a finite family
P-A has filed a proof that P1 does not fire for any l >= 2 (reduction to the two-mode theorem by one reflection).
My part is an independent finite search, exact modular rank (p = 999983, all integers below 2^53; rank_p <= rank_Q):
- COMPUTED. Family: the 3280 rays of Q^8 with entries in {0, 1, -1}. Using only relations inside the family that
  hold for every additive function (7588 plane relations, and random orthogonal frames until the rank stalled, about
  15000 frames), the solution space has dimension at most 156, against 36 for quadratic forms. So frames inside
  this family do not by themselves force linearity. This is NOT a counterexample: the same happens in dimension
  four (19 against 10 for entries up to 3, stored working history), where the theorem is proved with vectors
  outside the box. A function on the family that extends to all rational projectors is what P1 asks for, and a
  finite search cannot produce one.
- COMPUTED. Adding what the stored two-mode theorem gives (the function times the norm is a quadratic form on every
  four-dimensional subspace spanned by four orthogonal family rays of equal norm; about 19800 such subspaces
  sampled, rank stalled): dimension at most 53.
- COMPUTED (p1_glue2.py, seed 3). The three kinds of relation together (19760 equal-norm subspaces, the 7588 plane
  relations, 3000 random frames): dimension exactly 36. The 36 functions r -> (r^T S r)/(r.r) are solutions and
  are independent on the family, and the rank over F_p bounds the rank over Q from below, so the solution space
  over Q is exactly the quadratic forms. Statement this establishes, given the stored two-mode theorem (version 1)
  and nothing of P-A's proof: every function on the rational self-adjoint idempotents of three modes that adds on
  orthogonal ones is, on the 3280 rays with entries in {0, 1, -1}, a quadratic form divided by the norm. So a
  counterexample to P1 would have to agree with a linear functional on all these rays.
- The decision of P1 for all rays rests on P-A's proof (which uses vectors outside the family); this search is an
  independent confirmation of it on the family and is not filed.
P1 OUTCOME: did not fire. No counterexample on the family; on it linearity is forced (computed, exact).
Side remark for P2 (P-A's): two orthogonal vectors of norms 1 and 7 span a plane of discriminant 7, which lies in no
four-dimensional subspace similar to the standard one (7 is not a sum of three rational squares); P-A proves this.

### Cross-subject lookups
- Krein form (KF) against (P). COMPUTED (rev.py): on a ghost floor Cl_Q(2,2) with the stored involution
  S = 1 - (b^* - d^*)(b - d), the Krein adjoint x -> S x^dagger S has trace form of inertia (8, 8, 0); the blade
  inverse of every split has a positive definite trace form (16, 0, 0). So the Krein adjoint is the adjoint of (P)
  for no split: (KF) and (P) are NOT one premise in two places (kill condition K-B5: "one premise" is dead).
  COMPUTED: the vector psi = (2 + b^* - d^*) Pi_0 has positive Krein norm and its Krein expectation gives the
  self-adjoint idempotent (1 - S)/2 the value -1. So Krein expectations on a floor that carries ghost modes are not
  states of (P) unless the vector is an eigenvector of S (ARGUED: then the Krein expectation is the ordinary one).
  They do not conflict as stored: (P) is stated for the split that defines the modes and (KF) asserts positivity
  only on the BRST cohomology (K4); LOOKUP: no stored result rests on both (the future cones of the two premises
  share no claim). They would conflict if (P) were read on the full algebra of a floor carrying ghosts with Krein
  expectations as values. A scope sentence in (P) would prevent that reading (decision below).
- Does (N+) supply the split that defines the adjoint? NO (ARGUED from the premise's text, no computation). (N+)
  is stated on CAR(L^2(R, du) x K) with fields psi(u), psi^*(v): the adjoint (the positive definite form on one
  isotropic subspace, in the terms of the stored result on splits) is part of the data it is stated on. What (N+)
  selects is the polarisation (which modes annihilate), and the orientation of the unit, which it declares to be an
  assumed datum. On the generator factor the form is nearly forced by other data: a hermitian form invariant under
  the affine translations and covariant of weight 1/2 under the boost is c_+ on positive momenta and c_- on negative
  ones, and locality of the anticommutator forces c_+ = c_-, leaving a scale, which is the one-mode freedom of the
  stored result and does not change number-sector states. The form on the transverse and internal labels K is not
  fixed by (N+). So the second question of the problem is narrowed, not answered: translation and boost covariance
  with locality fix the split along a generator up to scale; K remains a datum.
- The unit principle (clause (vii) of the filed result): the independence model lives in the real algebra. Where the
  field theory's unit I_4 multiplies both parties' elements, K is a product of local observables, the state and its
  reversal differ in a local VALUE, and the reversal is the partial transposition, which still has non-negative
  weights on local records (prior art from memory; not proved here). So with I_4 the two models are distinguishable
  but both remain admissible for local records: (P) stays independent of non-negative local weights.

## Kill conditions: outcomes
- K-B1 did not fire: the multiplication map is a bijection (256 monomials), the reversal fixes the 100 products of
  self-adjoint monomials, lambda_{-1} o theta = lambda_{+1}, and lambda_{+1} violates (P).
- K-B2 did not fire: the predicted weight (c^2 - 1)/16 occurs (and (1 - c^2)/16 for c^2 > 1).
- K-B3 cannot fire: the bound is an identity plus one substitution.
- K-B4: with relations inside the family alone the dimension stays above 36 (156); with the two-mode theorem on
  equal-norm subspaces added it is exactly 36. No counterexample; P1 did not fire.
- K-B5: "one premise in two places" is dead (inertia (8,8,0)); a conflict exists only under a reading of (P) that the
  store does not make.
- P4: fires on scope S in the qualified sense stated above.

## Unexpected links
- Two copies as a filter. The stored family lambda_c, which one copy cannot separate, is cut to c = +-1 by weights
  of local records on two copies. Conjectured (not proved, and I did not try): a functional on two modes whose
  product functionals have non-negative weights of local records for every number of copies is a state or the
  reversal of one. The complex analogue for one qubit per party is a theorem on positivity of maps under tensor
  powers (Mueller-Hermes, Reeb and Wolf 2016, from memory).
- (L_E), the boundary-mode locality premise, forbids exactly the kind of unitary that clause (vi) uses (hopping and
  pairing between modes). Where it holds, the reversed functional could not be exposed by dynamics; but there (Q)
  and the rate model name the state, so the question does not arise. For laboratory modes nothing stored forbids
  bringing two modes together.
- The orientation datum of (N+) (which of the two seas is the state, the sign of the unit against the time
  orientation) and the reversal on one party are the same kind of object: an anti-automorphism applied to part of
  the system. A relative orientation between two parties' algebras is what (P) on the pair fixes and local records
  do not. Exact statement (ARGUED; from the bridge pass, with a two-line check): with the unit I_4 adjoined, a
  self-adjoint element of party 2 is s + I_4 a with s self-adjoint and a anti-self-adjoint in B, and the reversal
  sends it to s - I_4 a, that is I_4 -> -I_4 on party 2's self-adjoint elements only. So the reversal on one party
  is the orientation datum reversed for that party alone; reversed for both it is trivial on real functionals.
  This identifies the model and derives nothing: nothing stored says the parties share an orientation in a sense
  that excludes one of the two functionals. It is a different datum from the split of (P).
- The certificate of clause (i) localises the squares at one party's algebra times the other's recorded outcome,
  which is the form in which the superselection premise would enter a derivation: after the other party's record,
  the first party's values are a positive functional on its own algebra. So "(P) on each party's algebra, after
  records of the other" is the part of (P) the entanglement results need.
- P-A's remark that C is a sum of two anticommuting context elements (C^2 = D_1^2 + D_2^2) and the certificate here
  are two forms of the same Pythagorean fact: S^2 + D^2 = 4.

## Decisions for Leon
1. (Premise reading; the fork of 18 November, now sharp.) Can a projector that is not a product of local ones label a
   record, for instance after the two parties' modes are brought together? If yes (with non-negative frequencies):
   on two modes every linear value assignment satisfies positivity (clause (vi)), and (P) is the statement that
   record frequencies are non-negative, relocated rather than derived. If no: (P) is independent on the two-party
   scope, with the reversal as model, and no local experiment at any number of copies can test it.
   Recommendation: record the fork in the open problem with both branches proved; my lean is that joint records
   cannot be excluded for laboratory modes (only (L_E) forbids mixing, and only for boundary modes), so (P) is
   better described as "non-negative frequencies for all records reachable by unitary dynamics" than as independent.
2. (Wording of the problem's "why".) If the proposal is accepted, the sentence that (P) is the only premise between
   the algebra and the quantum bound should be restated: the bound needs (CP), a condition on one party's values
   given the other's records, which (P) implies and which is strictly weaker. Maintainer edit after acceptance.
3. (Scope of (P) against (KF).) Add to (P) a sentence that it is not asserted for Krein expectation values on floors
   carrying ghost or regulator modes, where (K4) is the positivity statement? Recommendation: yes, one sentence; no
   stored result rests on both premises, so nothing changes downstream.
4. (The unit.) Whether the parties' observables include the elements I_4 Y (the unit of the field theory times an
   anti-self-adjoint element). With them K is a local product and the family lambda_c is separated by a local value;
   without them the real algebra hides it. This belongs with the open item "which observables are physical".
5. (Literature.) Barnum, Beigi, Boixo, Elliott and Wehner 2010; Navascues and Wunderlich 2010; Wootters 1990;
   Hardy and Wootters 2012; Caves, Fuchs and Rungta 2001; Mueller-Hermes, Reeb and Wolf 2016 are all cited from
   memory in the proposal's note as prior art. Import as Facts only if wanted; nothing in the proofs uses them.
6. (Maintainer.) Open-problem record after acceptance: attack item 1 can state the scope S, the two models and the
   fork; the sentence "the independence of (P) from the other premises is not proved" can be replaced by the
   qualified statement above. New `supports` or `motivated_by` edges are the maintainer's.

## Left unfinished
- The conjecture that non-negative weights of local records on every number of copies force a state or the reversal
  of one (not attempted; it would turn the two-copy cut into a classification).
- The premise audit is a reading of prose premises, not a formal proof of independence; a formal one needs a stored
  definition of "record" (which projectors, which weights), which is decision 1.
- Clause (iii) and clause (vi) of the filed result are for k = Q; (iii) is for a first party of exactly two modes
  (more modes would follow from P-A's first proposal once it is stored).
- The answer on (N+) and the split is argued from the premise text; the covariance computation on a generator was
  done on paper only.
- Macroscopic locality is treated through its Gram criterion as remembered; the paper was not read.
- Prior art named from memory throughout; none of it was opened in this pass.
