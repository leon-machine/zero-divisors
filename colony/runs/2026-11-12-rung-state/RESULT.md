# Result: is a new rung's set/clear value forced by the completion, or a datum?

Pre-registration: PREREGISTRATION.md (commit 4bdb5a0, before any computation).
Stored as synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight.

| hypothesis | kill condition | outcome |
|---|---|---|
| forced | both on and off extend the state under (P) | killed: every weight in [0,1] extends, none outside |
| datum | a symmetry of the step exchanges on and off; all strings one orbit; two classes under rotors | killed: all three hold (3 rungs: 8 strings, one orbit, classes 4 and 4) |
| coin | several invariant extensions, or an invariant one that is sharp or integer valued | holds: exactly one invariant extension, weight 1/2, not sharp, not integer |

Prediction made before computing: forced killed, datum killed, coin holds. Outcome as predicted.

One failure during the work, recorded: the first run of the positivity check failed for the sharp extensions. The
cause was an error in my exact positive-semidefinite routine (a wrong symmetrisation step), not in the claim; the
routine was replaced by plain Schur-complement elimination and tested on five small matrices of known definiteness.

Not reviewed by an independent referee. Depends on Premise (P) (a new assumes edge, for the maintainer) and on the
reading of "symmetry of the step" as the sign changes of the new generators.

# Second result and independent review (added later the same day)

Second pre-registration: PREREGISTRATION-2.md (commit 7eb1d04, before computing). Stored as
synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws. Outcome as predicted: integer
states, parity sectors and a deterministic law on strings killed as selectors; unread rungs available only as new
premises.

One failure during the work, recorded: the first interference element chosen for the even coupling had value 0;
the indices of the record pair were the wrong way round. The corrected element has value 24/25.

Independent review by Claude Opus 5.5: verify/R-opus.md. Both claims SOUND WITH FIXES; all fixes applied.
What the review changed:
- Claim 1 (ii) depends on the group: unique under the sign changes and under all isometries of the plane; fails
  under the sign change of f alone (a sharp invariant state exists) and under boosts with the joint flip (every
  weight invariant). Now stated at every level.
- Claim 1 (iv) needed tests of mixed parity; for even tests on two modes a two-valued weight exists. Now stated.
- Claim 1 restricted to finite towers; the infinite tower may differ.
- Claim 2 (ii) wrongly suggested parity-changing couplings are excluded: an odd coupling is allowed, and still
  leaves interference 24/25. Corrected, and recomputed here.
- Claim 2 omitted the stored multi-mode descent, which ends interference between records and selects nothing.
  Added, and recomputed here.
- "The stored content holds no selector" narrowed to "none of these four on finite towers".
The review's judgement of the pre-registrations: the outcomes were nearly fixed in advance. Of the three
hypotheses of the first, only "coin" was open; "datum" was killed by the choice of group. Of the four candidates of
the second, C1 was near-tautological, C2 tested total parity only, C3 is fair only with C4, and C4's kill condition
was a statement about the store.
The review's own candidates, not stored as results: records of unbounded length on the infinite tower (branches
disjoint in the limit; interference present at every finite stage); tail classes of the infinite tower; the
descent's corner read-out (a fixed branch, not a weighted one); a pseudo-random law seeded by stored data.
None selects with the weights of (P).

# Third result: the infinite tower, and the reviews of it (added later the same day)

Third pre-registration: PREREGISTRATION-3.md (commit c4e2381, before computing). Stored as
synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit and
synthesis.infinite-strings-tail-classes-and-reading-rules-linear-and-not.

Reviews by Claude Opus 5.5: verify/R2-opus.md (second review), verify/R3-opus.md (a pass on the fixes, then a
confirmation pass). Final state: all four claims READY, no problems outstanding.

What the reviews found in this round, by kind:
- Wrong mathematics, three: the c = 0 sentence of the records claim (off by one; then, after the fix, still missing
  the condition that every pair the element involves is coupled); the group-dependence sentence added to the
  rung-state claim after the first review.
- Overstated: the first draft of the strings claim said there is no reading law inside the algebra. False. The
  lemma excludes only rules whose outcome is the value of an element; a rule declaring the outcome by the sign of
  the value of one element selects with the weights of (P) to within 2^-n. The claim was restated and renamed.
- Wording corrections: about two dozen across the four claims and the summary given to the maintainer.
- Weak or tautological checks: five, tightened or described as such in coverage.
- Pre-registration: two items marked as tests were not tests (2c, conceded by the author; 1a, found by the review).

What changed in the answer: a deterministic rule that selects outcomes with the right weights can be written in the
framework's terms. It needs an actual, typical string of rung values independent of the system, the rule as a law
(the state enters it, as in pilot-wave theories), and an order of reading. None is stored.
