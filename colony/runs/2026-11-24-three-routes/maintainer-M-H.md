# Maintainer M-H, run 2026-11-24-three-routes: the deposit state and the values results

Carried out: section "M-H" of MAINTAINER.md, on Leon's decisions D3 (the radiation-type descent hypothesis is
restated for the collar only) and D1 ((RP) stays a named hypothesis, written into no premise). Text only: no
mathematics, status, uses or assumes edge, check or coverage file was changed. Ten entities changed. The six that
were stored before this run have version + 1, an `amendments` entry and a credit entry (Claude Fable 5.2, source
'maintainer pass of 2026-11-24 (run 2026-11-24-three-routes)') with earlier credit entries unchanged. This run's
four results (5 to 8 below) stay at version 1, with no `amendments` entry and their credit as filed (coordinator's
instruction: they have never been on main and enter at version 1). All ten carry an `extraction` entry
`maintainer_pass_2026_11_24_three_routes`. Every stored file kept.

## The one sentence used for D3
"The radiation-type descent hypothesis is a hypothesis about a Cauchy collar of the descent and nothing more
(restated for the collar only by Leon's decision of 24 November 2026): on the collar the scale factor is smooth,
the field is Weyl-flat and the conformal vacuum is an admissible reference. It does not say that the field is the
exact radiation field down to the wall, and a result that uses the wall itself (a mass term linear in conformal
time through it, a continuation across it, the wall as the initial slice of half of Minkowski space) must name
what it assumes there." Where the prescribed field is concerned it is followed by: "With the whole expected
stress as the source the exact radiation field is not a solution of the field equation, given hypotheses (A) and
(E) of Theorem \claimref{synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall}, which are named
hypotheses of that result and not stored premises."

## Entities changed (old -> new version; 5 to 8 are new in this run and stay at version 1)
1. synthesis.hadamard-deposit-premise, 3 -> 4. The paragraph "Relation to the descent's normal form" (formal) and
   its sentence at the technical level restated with the D3 sentence. The three statements it used to attach to
   the hypothesis (conformally a radical-normal tame wall; Cauchy slices from any collar; M = ma smooth at the
   origin) are now said to be statements about the exact radiation field as a prescribed field, with the
   trace-anomaly result cited. The premise (HD), its equivalent form, uses and refutation condition: unchanged.
2. synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state, 3 -> 4. No
   clause changed (a theorem about prescribed fields). Dated note after the clauses: the clauses are about
   prescribed fields; the D3 sentence; clause (i)'s flat half-space with Cauchy slices and clause (iv)'s "initial
   slice of half of Minkowski space" are uses of the wall itself when read of the descended field; the
   trace-anomaly sentence. One technical sentence restated.
3. synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite, 3 -> 4.
   "As for a descent of radiation type" replaced by the D3 sentence at the formal, technical and one-liner levels
   and in a flag, with "the present result uses the collar only and assumes nothing at the wall" (true of its
   hypothesis and proof: a smooth positive scale factor on the collar). Clauses unchanged.
4. synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard, 4 -> 5. The technical
   remark "at a radiation-type origin M vanishes linearly in conformal time ... this clause does not fire there"
   restated: on the collar M is smooth by the hypothesis; linearity at the origin is a statement about the wall
   itself for the exact radiation field as a prescribed field. Dated note at the formal level saying the same,
   with the trace-anomaly sentence. Clauses unchanged.
5. synthesis.wall-conjugation-invariance-on-a-radiation-type-descent-floors-the-dirac-deposit-and-selects-none,
   version 1 (kept). (a) "the result filed alongside, <id>" turned into \claimref at the formal and technical levels, in the
   proof's Reading, in the note and a flag (the reciprocal sentence the referee worded was already there). (b) D3:
   NOT restated for the collar, because the theorem needs the wall (see "Not done"); a dated note, one technical
   sentence, the one-liner and a new flag say that (RD) is more than the collar hypothesis and name what the
   result assumes at the wall: the scale factor exactly a' eta down to eta = 0 (RD) and the continuation across it
   (DF), so that M = mu eta is linear through the wall. (CW) stays a named hypothesis.
6. synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall, version 1 (kept). (a) "a result filed alongside,
   <id>" in the Reading turned into \claimref, naming that result's (RD) and (DF); the note updated. (b) Dated note
   after the Reading and one technical sentence: the Reading's "cannot hold exactly" addresses the hypothesis in
   its earlier form (exact radiation field down to the wall); as restated for the collar, the Reading's own
   sentence on the collar applies (argued). (A) and (E) stay named hypotheses; nothing imported.
7. synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes, version 1 (kept). The "filed alongside"
   citation existed only in the note: it is now a \claimref there, and the sentence it carried (why (RP) must
   include projectors that are not products of local outcomes, from clauses (iv) to (vi) of the local-records
   result) is added to the Reading with a \claimref, labelled argued. Dated sentence (D1): (RP) stays a named
   hypothesis of this result, neither adopted nor rejected, written into no premise; (P) stays the postulate. The
   "not carried out or checked here" sentence stays. In the note "one party holds two modes" corrected to "two or
   more modes" (the local-records result as stored).
8. synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them, version 1
   (kept).   The "filed alongside" citation existed only in the note: now a \claimref there, and the relation it stated is
   added to the Reading as item (e) with a \claimref to the (RP) result; one clause that (RP) stays a named
   hypothesis (D1). Clauses unchanged.
9. synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them, 1 -> 2. One dated
   sentence in the Reading and a parenthesis in the technical level: three modes suffice, by clause (v) of
   synthesis.additive-weights-on-the-even-projectors-are-linear-from-three-modes-on.
10. synthesis.premise-positivity-of-values, 2 -> 3. One dated note at the formal level and one at the technical
    level: the bound omega(C)^2 <= 8 follows already from Hypothesis (CP) of the local-records result (clause
    (ii)); (P) implies (CP); (CP) does not imply (P) (its clauses (iv), (v)). The three clauses of the premise and
    the split are unchanged. (RP) is not mentioned in the premise (D1).

The six amendments (entities 1 to 4, 9, 10) are declared `restatement`. This is the validator's sense only
(tp/amend.py: the formal level changed); in no case did a clause, hypothesis letter or conclusion change.
Evidence fields: for 1 to 4 the trace-anomaly result's check
(check_no_power_law_origin_is_tame_unless_the_anomaly_vanishes), for 9 the corollary's check on two-valued
weights, for 10 the local-records result's certificate check, written '<id>: check.py::<function>' as stored
postulates do.

## Looked at and not changed
- synthesis.additive-weights-on-the-even-projectors-are-linear-from-three-modes-on (version 1): it has no "filed
  alongside" citation and already cites by \claimref at its levels. Unchanged.
- synthesis.spin-product-state-of-the-massless-dirac-field-is-odd-under-chirality-and-never-hadamard: says "on the
  radiation-type collar" throughout; already in the collar form. Unchanged.
- synthesis.weyl-flat-fields-need-no-scaling-limit-premise-and-robertson-walker-generators-see-the-schwarzian: the
  phrase "the Weyl-flat descent region (a descent of radiation type, a stated hypothesis)" is in its extraction
  note only, no level states the hypothesis, and it uses nothing at the wall. Unchanged (a note-only edit would
  be a version bump with nothing substantive changed).
- synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit: one argued survey sentence in its
  proof ("the Hadamard premise and its Weyl-flat collar under the radiation-type descent, the radical-normal tame
  wall ... are statements about the background field"); collar form already. Unchanged.
- synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points: speaks of the radical-normal wall as
  geometry of the isotropic Kasner point, not of the hypothesis. Unchanged.
- synthesis.attachment-transport-is-flat-only-where-weyl-vanishes: "radiation type" there is the algebraic type of
  a Weyl curvature, unrelated. Unchanged.
- documents/trail-thermality (prose.json and rendered files) quotes the old one-liner of entity 3 ("as for a
  descent of radiation type"). Not in my ownership; to be regenerated or reworded at close-out.

## Validator
`python -m tp check --store store --layers 1-3 --keep-going --author leon` after the last edit: 0 errors, 0
warnings, 120 information findings (118 I213, I126, I305), the same as layers123-after-accept.log except that I305
now counts 87 changed entities with 38 claims and 7 documents depending on them (all maintainers' edits together).
Log: layers123-M-H.log. A run a few minutes earlier showed 4 errors E216, all on op.einstein-from-the-field-theory
and op.gravitational-field-at-null-momentum (a reference to the postulate
synthesis.premise-canonical-pair-on-the-two-null-directions before it existed); not in my ownership, and gone in
the final run. The validator objected to nothing on the ten entities. No check was touched; as a sanity pass
runcheck was run on the checks of entities 5, 6 and 7: all PASS. No layer 4, check4, accept, repin, lock or commit.

Pins left for the orchestrator's repin (content of the pinned statements unchanged in every case, so each is a
formality): 16 entities assume synthesis.premise-positivity-of-values@2 (now 3); the spin-product result uses the
massive result @4 (now 5) and the moment result @3 (now 4); synthesis.state-of-a-new-rung-unique-symmetric-
extension-... uses the no-two-valued result @1 (now 2); the trace-anomaly result uses the tame wall @3 (now 4);
the wall-conjugation result uses the massive result @4 (now 5), the tame wall @3 (now 4) and the moment result
@3 (now 4).

## Numbers to recompute
None. No number was changed or quoted anew, except that entity 1 refers to clause (vi) of the trace-anomaly
result without repeating its figure (that figure rests on a ceiling conditional on Hypothesis (U) of its source).

## Not done, and why
- D3 on the wall-conjugation theorem: not restated for the collar. The theorem needs the wall itself (the
  reflection is a symmetry exactly when M is odd, which needs a = a' eta through eta = 0 and the continuation
  (DF)); a collar hypothesis would not give its clauses. Its hypotheses (RD), (DF), (CW) stand as stated; the dated
  note names them as what it assumes at the wall. Its title still reads "on a radiation-type descent".
- This run's four results (5 to 8) were first bumped 1 -> 2 and then, on the coordinator's instruction, reset to
  version 1 with the version-2 amendments and credit entries removed; every text change and the extraction entry
  are kept.
- No \claimref was put into the plain-id citations of the extraction notes other than the "filed alongside" ones.
- The Mottola and Vaulin reference was not added to store/references.yaml (not in my ownership; the default of
  this pass is that no literature is imported).
- No lineage link was added between the two deposit-state results (the referee offered it as an option); the
  cross-references are in text, both directions.
- (P): the scope sentence on Krein expectation values was not written (see Decisions).

## Decisions for Leon
1. Scope of (P) against the Krein form: whether to add to (P) the sentence that it is not asserted for Krein
   expectation values on floors carrying ghost or regulator modes. It is not a plain consequence of stored text:
   it rests on a computation of this run that is in findings only (a vector of positive Krein norm whose Krein
   expectation gives a self-adjoint idempotent the value -1), and it is a statement of the premise's scope, which
   is a premise decision. No stored result rests on both premises.
2. The four hypotheses (A), (E), (RD), (DF) cannot all hold. With D3 the collar hypothesis is compatible with (A)
   and (E) (argued in the trace-anomaly Reading); the incompatibility now sits only between the trace-anomaly
   result and the wall-conjugation result, which say so in both directions. If any of the four is ever made a
   postulate, a pairwise contradiction record is needed.
3. Whether the wall-conjugation result's title should drop "radiation-type descent" in favour of wording that
   says the exact radiation field through the wall, now that the hypothesis of that name is collar-only. Not
   changed here (a title change was not asked for).
4. The words "radiation-type origin" (massive result, technical level and note) and "radiation origin" (tame wall,
   clause (iv)) remain as names of the origin of the exact radiation field as a prescribed field; say if they
   should be renamed.
