# Fixes P-A, run 2026-11-24-three-routes

Referee report: verify/R-P.md, sections 1 and 2 and "Overlaps and conflicts". Bridge entry: B5. Nothing rebutted.
Edits are in place in proposals/<id>/. Nothing under store/ was edited.

## 1. synthesis.additive-weights-on-the-rational-projectors-of-two-or-more-modes-are-linear
Verdict: SOUND WITH FIXES. Both fixes applied; statement unchanged at every level.
- Fix 1 (proof, clause (iv)): the greatest-common-divisor phrasing is replaced by a least solution: among the
  integer solutions of 7n^2 = a1^2 + a2^2 + a3^2 take n least; n odd is excluded modulo 8; n even forces all a_i
  even, and (n/2, a_i/2) is then a smaller solution.
- Fix 2 (note and coverage): "integers below 300" now reads "up to 293", which is what the loop covers.
- Own correction, not asked by the referee: coverage.yaml described two functions as they were before they were
  tightened at the filing gate (three pairs, seven sample rationals, three frames); it now says what the check
  does (one pair with exact values, the rational 15/28, one orthogonalised frame with its five exact values and
  the coordinate frame).
- From "Overlaps": the note now says that clause (vii) answers the sentence of
  synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them that leaves open
  whether three modes suffice for the even subalgebra.
- Rule 9: the note's "in this session" (on the unread 2001 paper) is reworded; the prior-art flag is unchanged.
- runcheck: 6 PASS. check4: pending (orchestrator).

## 2. synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes
Verdict: SOUND WITH FIXES. All four fixes applied; title and one-liner unchanged ((RP) is named in both).
- Fix 1 (formal, (RP)): the residual postulate is now cited,
  \claimref{one-relation.measure-indifference-borns-rule-located}.
- Fix 2 (formal (ii) and proof): the sentence on rational spectral projectors was false as worded. It now says: the
  only spectral projector of a single eigenvalue with rational coefficients is the kernel's, (1 - K)/2; with its
  complement C^2/8 = (1 + K)/2 (the pair of eigenvalues +-2 sqrt 2) these are the only rational ones besides 0 and
  1. The proof lists all sums of the three single-eigenvalue projectors. The check now also verifies that C^2/8 is
  a projector, equals (1 + K)/2 and fixes C; coverage updated.
- Fix 3 (lay): "with nothing further assumed" now reads "with nothing assumed beyond that reading".
- Fix 4 (note, cross-cite in text only): "what is new" now says that the core of (iv) is one line ((RP) gives a
  state by the two-mode theorem, a state gives the bound), that clause (ii) and the reading are the separate
  content, and that the projectors that are not products of local outcomes are essential to (RP), citing the result
  filed alongside, synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them,
  clauses (iv) to (vi). Not put in uses.
- Referee's noted weakness (clause (iii) is tested only on linear functionals, where S = L(C) is a tautology): left
  as it is, as the referee says; the content of (iii) is the stored theorem and the coverage says so.
- runcheck: 3 PASS. check4: pending (orchestrator).

## Repin on acceptance
- None needed now: both proposals pin only stored versions.
- If proposal 1 is accepted: proposal 2's note sentence "it is not stored at this version" should be replaced by
  a reference to proposal 1, and its clauses (iii), (iv) can then be stated for commuting pairs of self-adjoint
  elements of square one in any number of modes (a version 2 with a uses edge to proposal 1; maintainer or a
  later run). The stored no-two-valued-weights entity could cite proposal 1 clause (vii) in its reading.

## Next steps
- Bridge B5 (lead, not pursued): the recording premises do not say (RP); (RP) exceeds them in three respects
  (which projectors, their self-adjointness, non-negative additive weights). The restricted hypothesis (RP-flag),
  record labels are the sector projectors of Witt flags adapted to the split, names only parity-even projectors.
  Exact test to run at three modes: are the vacua of the maximal isotropic subspaces of Q^{3,3} exactly the
  rational rays of the two blocks of size four of the even subalgebra (Klein correspondence, cited from memory in
  the bridge note)? If yes, clause (vii) of proposal 1 applies and (RP-flag) with non-negative additive
  frequencies is equivalent to (P) on the even subalgebra of three modes. Kill condition to register before
  computing: a rational ray of a block that is the vacuum of no maximal isotropic subspace defined over Q, or flag
  vacua whose frames do not include all orthogonal frames of the block. At four or more modes the flag vacua are
  a proper subfamily and the question is open.
- Unchanged from the attack round: other ordered fields; size N = 3; sufficiency of the three-square criterion for
  pairs.

## Decisions for Leon
1. (RP): adopt or not, and in which form. Three forms now on the table: all rational self-adjoint projectors; from
   three modes on, the parity-even ones (proposal 1, clause (vii)); the flag-sector form of bridge B5, untested.
   Recommendation unchanged: keep it a named hypothesis; as a premise it would replace (P), not derive it.
2. What "the CHSH value" means in stored statements: the sum of four correlators, or the value of the element C.
   Recommendation: state both, as proposal 2 does.
3. Open-problem record: attack item 7's "first step" is false (two vectors need not lie in one standard
   four-space); item 5's "not done: more than two modes" is done if proposal 1 is accepted; "tied to the parity
   item" holds only at two modes.
4. Prior art: Mushtari 2001 still unread beyond the abstract. The referee notes that no level of proposal 1 says
   "new" or "answers Problem G"; saying so later needs the paper read first.
5. No imports are needed by either proposal.

## After the change of base
The run branch was rebased onto main at f9f3bee, which stores
synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four (v1) and
synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three: the same theorem as my first
proposal, by the same route (one reflection per vector, four squares, induction on the support) and with the same
counterexample to the pairwise step. My first proposal is withdrawn as a duplicate (its folder is in withdrawn/).
Section 1 above is kept as history only.

### New proposal (replaces the one clause main lacks)
synthesis.additive-weights-on-the-even-projectors-are-linear-from-three-modes-on
Title: "Additive weights on parity-even rational projectors are linear from three modes on" (82 characters).
A corollary; uses the stored size-four theorem @1 (its clause (i) for the identification with matrices, its clause
(iii) on each block), synthesis.signed-directions-and-the-integer-clifford-algebra @2 and
tower.ladder-pairs-satisfy-car-vectors @4. Transport-absent. extraction.open_problem: op.positivity-of-values.
- (i) PROVED for every l >= 1, COMPUTED for l = 3: the even subalgebra is the commutant of the pseudoscalar
  Gamma = e_1 f_1 ... e_l f_l (Gamma^2 = 1, self-adjoint, Gamma s_I = (-1)^|I| s_I), two blocks of size 2^(l-1)
  with identities (1 +- Gamma)/2. The store did not hold this block decomposition, so it is proved in the entity.
  The proof is by the commutant, which replaces the dimension count of the withdrawn clause.
- (ii) PROVED, given the stored theorem: for l >= 3 an additive function on the even projectors alone is the
  restriction of a linear map on the even subalgebra, unique among those with L(x^dagger) = L(x).
- (iii) PROVED: with non-negativity and normalisation, the restriction of exactly one state of (P) that vanishes on
  odd elements (new against the withdrawn clause, two lines on the blocks of M M^T).
- (iv) PROVED: l = 1 trivial; l = 2 fails (blocks of size two), with the parity weight of the stored theorem's
  one-mode note placed on a block.
- Settles: the open sentence of
  synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them (three modes suffice);
  the tie between "all rational projectors label records" and parity-odd projectors holds on two modes only.
  Does not settle: whether odd elements are observables, which projectors label records, the sign, (P).
- Gates: runcheck 3 PASS; check4 0 errors, 0 other findings; validate_draft ok (E610 warning and I305 info only).
  coverage.yaml copied by hand into proposals/<id>/.

### Second proposal (the (RP) bound): edited, not regated
- The note's sentence "once the theorem on additive weights is available there (it is not stored at this version)"
  is replaced: the stored size-four theorem is named, and the extension of clauses (iii) and (iv) to any number of
  modes is stated as following from it and as NOT carried out or checked here. The same sentence, with
  \claimref, is added at the end of the formal Reading. No uses edge added (no proof step needs it).
- No sentence refers to the withdrawn proposal. runcheck: 3 PASS. check4: pending (orchestrator).

### What the withdrawn proposal had that main's entity lacks, besides (vii)
- The block decomposition of the even subalgebra (part of its clause (i)): now in the new proposal.
- The statement that L is the only linear extension with L(x^dagger) = L(x) in the signed case (main states
  uniqueness of rho and, with the sign, of the state): minor.
- In the check, the sharpness of the lemma (two hyperplanes leave rank 9): minor, and main may hold an equivalent.
- An argued remark only (not a result): that for N >= 8 a pair embeds in a standard four-space exactly when its
  determinant is a sum of three rational squares.
Nothing else. Main has more than the withdrawn proposal in two respects: the one-mode counterexample and a fuller
reading of the 2001 paper.

### Repin on acceptance (updated)
None needed. If the new corollary is accepted, the stored no-two-valued-weights entity's reading could cite it,
and op.positivity-of-values attack item 7 ("tied to the parity item") could be narrowed to two modes.

### Decisions for Leon (updated)
Decision 3 above is superseded where main's record already says it (more than two modes done; first step false).
Still open for him: decision 1 ((RP), now with the even form resting on the new corollary), decision 2, and
whether the new corollary's remark on attack item 7 goes into the open-problem record.

## Third pass
Referee report verify/R-3.md, section 1, on
synthesis.additive-weights-on-the-even-projectors-are-linear-from-three-modes-on: SOUND WITH FIXES. All three
applied in place.
1. Quotation. The note now quotes the stored entity's note as the referee words it: a statement of this type about
   parity-even elements needs more than two modes ("whether three suffice is not shown"). For the record, by a
   lookup: the stored entity has the sentence twice. Its note has the wording above; its technical level reads "So
   an argument of this type for parity-even elements needs at least three modes; whether three suffice is not shown
   here." The earlier quotation was exact for the technical level, not for the note. The note now quotes the note
   and says the technical level has the same sentence.
2. New clause (v), with proof: for l >= 3 no additive weight on the even projectors with values in {0, 1} and
   mu(1) = 1 exists. Proof verified before writing: by (ii) the weight is linear; one block has value 1; in a frame
   of that block take r of value 1 and s of value 0; N(t) = (r + ts)^T rho (r + ts) and D(t) = (r + ts).(r + ts)
   satisfy N(N - D) = 0 at every rational t, so N = 0 or N = D identically; t = 0 excludes the first and the t^2
   coefficients (0 against s.s) the second. A finite core is also given and checked: with N = a + 2 beta t and
   D = a + sigma t^2, the points t = 1, -1 force a = sigma, beta = +-a/2, and t = 2 then fails (3a or -a against 0
   and 5a). New check function check_a_quadratic_weight_with_values_zero_and_one_fails_on_the_line_through_two_frame_rays
   (216 grid cases, one explicit case, one control); added to checked_by and coverage. The note and the Reading now
   rest "answers the question left open" on (v).
3. Uniqueness wording. One-liner and technical: "a state of (P), unique among those vanishing on odd elements;
   other states may restrict to the same weight". Formal (iii): the sentence that vanishing on odd elements is a
   choice of extension, with an explicit state that restricts to the same weight and has the value 1 on an odd
   element (the functional of s_I + s_J, |I| even, |J| odd; proved in the proof text).
runcheck: 4 PASS. check4: pending (orchestrator); note that the entity now lists a fourth check function, so the
central gate has one new function to run.
