# attack-BA (cluster B, angle A constructive), run 2026-11-10-phase2

Status: FINAL for the attack round (three proposals filed). Pre-registration below was written before any computation; results follow it.

## Orientation (direct lookups)
Read in full: op.positivity-of-values; synthesis.premise-positivity-of-values; the base CHSH result (clauses (iii), (v),
(vi), (vii), (viii)); the mode split; one-relation.measure-indifference-borns-rule-located (statement, proof, check);
one-relation.imported-envariance-born-rule; the record-chain vote; the four premises (indifference, irreversible
recording, recorded sectors superselected, supervenience); singularity.p-univalence; singularity.descent-parity-average;
synthesis.indifference-is-curie-plus-single-valuedness; dark-matter.premise-flag-as-datum;
synthesis.positive-structure-is-twistor-form-at-imaginary-time (found by lookup: bears on B4).
Notation here: A = Cl_k(p,q), tau = <.>_0, dagger = blade inverse, Sym(S) = self-adjoint elements of S.

## B1. Born weights from (P)
Routes.
 1. (the problem's own) Generalise clause (viii) of the base: Cauchy-Schwarz for the form omega(x y^dagger) with
    N = 1 - P of value zero; needs: P self-adjoint idempotent, a condition on the corner PAP. Fails if the corner
    condition cannot be stated without importing the Wedderburn classification.
 2. (from another subject) The Fock module: P the vacuum projector of Cl(l,l), states as vectors x P, weights as
    squared norms in the stored coefficient form; delivers the mode algebras only.
 3. (own) Characterise exactly the idempotents on which sharpness fixes the state: Sym(PAP) = k P ("atom"), prove
    it is necessary and sufficient, and prove existence in every signature from maximal commuting sets of
    self-adjoint blades, with no classification theorem.
Choice: route 3 containing 1 and 2, because it gives an if-and-only-if and works over Q.
Claim to test: for omega with (P) and P an atom, omega(P) = 1 implies omega = tau(P .)/tau(P); reality is needed
(without it only on self-adjoint elements); positivity is needed; uniqueness holds iff Sym(PAP) = kP.
KILL CONDITION B1: an exact functional satisfying all three clauses of (P), with omega(P) = 1 for a self-adjoint
idempotent P with Sym(PAP) = kP, that differs from tau(P x)/tau(P) on some x; or a signature (p,q) with p+q <= 6 in
which a maximal commuting set of self-adjoint blades gives a P with dim Sym(PAP) > 1. Either kills the theorem as
stated. Secondary kill (for the "no square roots" remark): a rational atom of the vacuum orbit with a non-rational
weight.
Gleason part, claims to test: (a) on projectors only, additivity over orthogonal families does not give linearity
when all atoms come in complementary pairs (one mode Cl(1,1), Cl(2,0), and the size-2 algebras Cl(3,0), Cl(1,3));
(b) on effects, additivity alone gives a state of (P) over Q (Busch-type), with no continuity. KILL: (a) dies if the
candidate frame function fails additivity on some orthogonal family or is linear; (b) dies if 1 is not an order
unit for the cone used, or the extension is not well defined.

## B2. (P) against the stored measurement premises
Routes.
 1. Derive (P) from the descent: the parity average is a positive map. Expected to fail: E maps positive to
    positive, so omega o E is positive iff omega is positive on the even part; no positivity is created.
 2. Derive (P) from "weights exist and add" (the residual postulate of the stored Born result): (P) iff additive
    non-negative weights on effects (uses B1 (b)); iff non-negative value on every atom.
 3. Independence: an exact finite model satisfying formalised versions of univalence, descent invariance, symmetry
    invariance, block-diagonality on recorded sectors and non-negative additive weights in every context of
    commuting observables, and violating positivity, differing from a (P)-model on the CHSH bound.
Choice: 2 and 3 together; 1 as a lemma.
KILL CONDITION B2: independence (route 3) dies if every even, real, normalised functional that is block-diagonal on
a complete commuting family of even self-adjoint idempotents and gives non-negative weights in every context of the
configuration is positive (search the even analogue of the box functional in Cl(4,4) with parity-even observables;
if lambda(C) = 4 cannot be reached by an even functional, the model fails). Derivation (route 2) dies if some
functional is non-negative on all atoms and not positive.
Label rule: faithfulness of any formalisation of the informal premises is "argued"; only the finite statements are
proved/computed. Independence is OF a named finite list of formal conditions, not of the store.

## B3. Audit of the four measurement premises
Formalise each in a finite record model (system modes plus record modes, a family of record projectors R_i, a set
of later evolutions, a weight assignment, a symmetry group): I = weights invariant under the stabiliser of the
datum; R = record projectors fixed by every later evolution; S = values vanish on R_i x R_j, i != j; V = the subject
predicate is a function of the record data. For each: a model where it fails and the others hold, or a derivation.
KILL CONDITION B3: an audit entry dies if the model offered violates a second premise as formalised, or if the
premise is derivable from the other three as formalised. Expected: S is stated with R as hypothesis (dependence of
statement, not derivability); under (P) plus sharpness I for weights is a theorem (B1 uniqueness), so I is
redundant for branch weights given (P). All of this "argued" except the finite facts.

## B4 (findings)
Questions: does the flag (a pair of complementary isotropic subspaces, or J) fix the split E+ + E-; what does.
Test: the boost of clause (vi) of the base preserves the null pair v, w of the mode and changes the split. If so the
null pairs (the polarisation) do not fix the adjoint. KILL: if the stabiliser of the polarisation fixes the split.
Parity-odd observables: test whether E(ab) = E(a)E(b) for odd a, b; if not, even states see the correlations of odd
elements and univalence plus the average do not select the even setting. KILL: an even state cannot exceed 2 at one
mode per party with the Klein-twisted directions.

## RESULTS (interim, kept current)

### B1: filed, synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional
Gate: check4 exit 0, no findings; validate ok, no warnings; registered with propose_claim.
Kill condition B1 did not fire (22 signatures: p+q <= 5, (2,4), (3,3); corner dims 1, 2, 4, self-adjoint part 1).
- PROVED: atoms (self-adjoint idempotents with Sym(PAP) = kP) exist in every signature, from maximal independent
  commuting sets of blades of square 1; no classification theorem used. Premises: the blade basis only.
- PROVED: under (P) (all three clauses), a state sharp on an atom Pi is <Pi x>_0/<Pi>_0; weights are ratios of sums
  of squares of coefficients, in k, no square root. Uses: Cauchy-Schwarz over an ordered field, reality, positivity.
- PROVED: each clause needed (reality: only self-adjoint elements fixed otherwise; positivity; atom condition iff).
- PROVED: every y y-dagger is a positive combination of atoms, so given linearity positivity = non-negative
  weights on atoms.
- COMPUTED: the table of corner dimensions (sampled: two greedy maximal sets per signature).
- Candid status: classical (support-projection argument; trace form of the Born rule; Lounesto's idempotents).
  Placement only. It RELOCATES the envariance argument's residual postulate into (P); it does not reduce it.
  Under (P) no indifference, environment, fine-graining or continuity is needed for the weights.

### B2: filed, synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects
Gate: check4 exit 0, no findings; validate ok, no warnings; registered with propose_claim.
- PROVED (Busch-type, classical): states of (P) = non-negative normalised additive weights on effects, over Q and
  Archimedean ordered fields; over Q additivity alone gives linearity (no continuity). So (P) is equivalent to a
  strong reading of the stored residual postulate "weights exist and add". ARGUED: that this is the right reading.
- PROVED: the parity average maps the positive cone onto its fixed part; it creates no positivity (route 1 dead as
  expected: the descent gives (P) only for functionals already positive on even elements). For functionals
  vanishing on odd elements, (P) is (P) on the even subalgebra (odd hermitian squares are even hermitian squares).
- PROVED: for even states the value of the CHSH element of mixed-parity one-mode directions is that of
  X u + Z Gamma, u = e2 f1; an even atom gives 14/5. Kill condition B4 (parity part) did not fire: univalence plus
  the parity average do not select the even-observable setting. Complementary to BB's result (parity-homogeneous
  settings give at most 2).
- Independence, stated precisely: positivity is independent of {linearity, normalisation, reality, evenness,
  invariance under the parity average} on one algebra (trivial example, weight -1/2). BB's filed result is the
  strong version (non-negative local weights everywhere, (P) still not fixed). Independence OF THE STORE is not
  claimed by either: the four measurement premises are informal and say nothing about values of sums of
  non-commuting elements (ARGUED from reading them in full; not audited over the joint cone).
- NOT derived: (P) from indifference + record premises. Verdict: not derivable as stored (argued); equivalent to the
  strong residual postulate (proved).

### B3 (findings, no proposal from this side; BB files finite models if any)
Formal reading and verdicts (all ARGUED except where a finite fact is named):
- Indifference (I). For branch weights it is REDUNDANT given (P) and sharpness: by B1 uniqueness the weights of the
  state sharp on an atom are invariant under every automorphism fixing the atom and commuting with dagger (proved
  consequence of B1 (iii)). Its other clause (no uncaused selection: all sectors occupied) is not touched by (P).
  Without (P), I does not give the weights at one mode: the cubic function of B2 (iii) is invariant under the
  stabiliser of the atom (z -> z, x -> -x) and is not the Born weight (computed). This meets the stored refutation
  condition of one-relation.measure-indifference-borns-rule-located only if fine-graining through an ancilla is
  dropped; with it, over Q every squared amplitude is rational and the stored argument's continuity step (iv) is
  not needed (remark).
- Irreversible recording (R) and superselection of recorded sectors (S). S is stated with R as its hypothesis
  ("Grant ... Then ..."), so as stored S is a conditional and cannot fail when R fails: the pair is not
  independent as statements; the content of S beyond R is the exactness of decoherence. Finite model R true, S
  false: record projectors (1 +- p2)/2 fixed by trivial later evolution, state the pair state of the stored mode
  split with c s != 0, which has nonzero value on an element R+ x R- (e.g. w1 w2 + v2 v1): records are never
  unwritten and interference between record sectors is present. So S is not derivable from R (the store says so).
  R is not derivable from S, I, V: a later evolution that swaps the record sectors (conjugation by e2) unwrites
  the record while S, as a conditional, holds vacuously.
- Supervenience (V) carries no statement about values; it is independent of the other three in the trivial sense
  that no finite model of values can test it (argued). Its only stored use is one-relation.character-experience...
- None of the four implies or uses positivity; none is needed for B1 or B2.

### B4: filed, synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them
Gate: check4 exit 0, no findings; validate ok, no warnings; propose_claim submitted (see final report for status).
- The null pairs do not fix the split: v -> t v, w -> w/t keeps the two null lines and the parity p and sends
  e to (t + 1/t)/2 e + (t - 1/t)/2 f; t = 4 is the boosted frame of clause (vi) of the base (17/8, 15/8). Kill
  condition B4 (split part) did not fire. COMPUTED.
- Parity-odd elements: see B2 third bullet.
- PROVED: splits adapted to the null pairs (adjoint exchanges W = span v_j and W' = span w_j) correspond one to one
  to positive definite forms on W: l(l+1)/2 numbers are missing; the null pairs fix N, its sector projectors, the
  vacuum projector and the total parity.
- PROVED (l = 2 step by a complete finite computation, l = 3 confirmed): the functionals real for every adapted
  split are <h(N) x>_0, dimension l + 1; the (P)-states common to all adapted splits are the mixtures of the
  normalised sector projectors. Not predicted before computing (no kill condition was registered for it; the
  registered one, "the stabiliser of the polarisation fixes the split", did not fire).
- PROVED: stored pair states with c s != 0 need the split; split-independent states give the one-mode-per-party
  CHSH element at most 2. Mode-wise scales only: number-diagonal functionals (2^l), which contain all stored
  thermal products.
- ARGUED only: the flag of dark-matter.premise-flag-as-datum (one sign of J, in the complexified Cl(2,4)) cannot
  supply a continuous datum; the stored theorem synthesis.positive-structure-is-twistor-form-at-imaginary-time
  already classifies positive Hermitian structures with every generator unitary (these are adjoints of splits)
  by points of the forward tube, so the natural supplier of the split in the series is the observer's tube point
  (fixed up to the scale rho by synthesis.wick-rotated-boost-selects-observer-tube-point), not the flag. Not
  computed here: no check that "h^{-1} Sigma an involution" is the adaptedness condition used above.

## What failed or was not done
- No derivation of (P) from the stored measurement premises or from the descent: route 1 of B2 is dead (the
  average creates no positivity), and nothing in indifference, recording, superselection, supervenience speaks of
  values of sums of non-commuting elements (argued).
- Gleason proper over Q in size >= 3 (non-negative additive weights on atoms only): not decided by either sibling.
- The converse "every primitive self-adjoint idempotent is an atom" is not proved without the classification of
  the algebras (classical; not needed: the theorem is stated for atoms, and atoms exist in every signature).
- B3 has no proposal: the four premises are informal; the audit is argued with three small finite facts
  (computed in work/BA/c3.py: pair state value 12/25 on R+ x R-; e2 swaps the record sectors).
- The reading of the stored residual postulate "weights exist and add" as additivity on all effects is argued, and
  the sibling's objection stands: the effects theorem is close to definitional over Q, effects are not outcomes of
  the stored record account, and its content is that reading. Referees should weigh whether it deserves an entity
  or a note on the premise.
- Literature: Busch 2003 and the rational-sphere colouring paper (Havlicek, Krenn, Summhammer, Svozil) checked for
  existence and abstract on the web; Gleason 1957, Caves-Fuchs-Manne-Renes 2004, Lounesto, the support-projection
  argument and Zurek's steps (already checked in the store's import) are from memory.

## Unexpected links
1. The split of (P) and the observer's tube point: synthesis.positive-structure-is-twistor-form-at-imaginary-time
   clause (iv) ("only positive structures carry states") is a positivity-of-values statement already in the store,
   in the Hermitian setting of Cl(2,4); (P)'s "which stored datum supplies the split" may already be answered there
   (tube point), with the scale rho the same kind of free datum as the scale t of one mode found here.
2. Split-independence and thermal states (bridge item "(P) and thermal states"): the states that need no split
   datum are exactly functions of N (all adapted splits) or number-diagonal (mode-wise scales): the stored
   thermal products prod (1 + r_k p_k)/2 are split-independent in the second sense, and entangled pair states are
   not. With one mode per party the split-independent states cannot violate CHSH.
3. For one mode, "real for every adapted split" = "even" (omega(e) = omega(f) = 0): univalence for one mode is the
   same condition as independence of the unsupplied scale.
4. Over Q the continuity step (iv) of the imported envariance argument is not needed: all weights of rational
   atoms are rational (B1 (iii)).
5. Indifference for branch weights is a theorem under (P) plus sharpness (uniqueness of the sharp state).

## Decisions for Leon
1. Whether one-relation.measure-indifference-borns-rule-located should cite the B1 result (under (P)) in place of,
   or beside, the imported envariance argument; and whether its residual postulate "weights exist and add" is to
   be identified with (P) (the strong reading, additivity on all effects). Recommendation: beside, not in place of;
   record that under (P) the weights need no indifference, and that (P) is the strong form of the residual
   postulate. This is a premise decision.
2. Whether "sharp" in the series means "value 1 on an atom" (self-adjoint idempotent with one-dimensional
   self-adjoint corner); the B1 result uses that definition.
3. The observables question is not settled by univalence or the parity average (B2 (v), and the sibling's record
   result): a rule on observables is needed if parity-odd or mixed-parity elements are to be excluded. Leon's
   earlier decision to keep both settings side by side stands unless he adopts such a rule.
4. Which datum supplies the split: adopt (or not) the reading that it is the observer's tube point / positive
   structure of the stored twistor-form theorem; the flag does not supply it (argued). Possible new attack item
   on op.positivity-of-values: prove or refute that the positive structures h_m of that theorem are exactly the
   adjoints of splits of Cl(2,4) and relate the scale rho to the scale t.
5. Imported Facts that the three proposals cite from memory and that a maintainer may wish to import: Gleason 1957;
   Busch 2003; Caves, Fuchs, Manne, Renes 2004 (none is used in a proof).
6. Whether the effects result should be an entity or be folded into the premise entity as a note (see "What
   failed").

## Exposures raised by the sibling, and what was changed (in place, after registration)
(a) Effects result: title now carries "(reading argued)"; one-liner and Scope say it is close to a restatement of
    (P) over Q, that effects are not outcomes of the stored record account, and that the content of the envariance
    argument is relocated, not reduced.
(b) Base: clause (i) now says the existence proof is a blade argument for every signature and does not use the
    table (the table is a sample confirming it).
(c) Base and split result: Scope says weights are in [0,1] only for projectors self-adjoint for the same split;
    example value 9/8 on a boosted idempotent (recomputed by hand: (1 + 5/4)/2).
(d) Effects result (v): says 14/5 uses mixed-parity directions; with parity-homogeneous directions |X| + |Z| <= 2
    (checked case by case from the formula), sibling's record result named as intended citation.
(e) Effects result (iv): rider added and proved: the mode-wise average reduces (P) to 2^l non-negative weights; the
    total-parity average does not.
Relocation, stated plainly in the base at technical level and in the one-liner: (P)'s linearity across
non-commuting elements carries the content of the imported argument. I cannot show otherwise.
Gate after these text edits: see final report.
Gate after the text edits: check4 exit 0 with no findings and validate ok with no warnings, all three (the registered folders in proposals/ carry the edited text; propose_claim was not rerun).
