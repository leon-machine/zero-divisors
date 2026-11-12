# Maintainer agent M1, pass after run 2026-11-12-asymmetry (decisions D1 and D4)

Nothing committed. Validation after the edits:
`python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon` gives 0 errors, 0 warnings
(121 information findings; the I213 on the conjugation claim is in the run's baseline.log).

## Entities changed

1. `synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation` 4 -> 5 (restatement, D1).
   - entity.md: last sentence of clause (3) of the formal level replaced by the referee's corrected text
     (R1 section G), with the dual basis and the Gram matrix defined inline. Front matter: version,
     amendments entry (kind restatement, evidence the new check), two credit entries, new checked_by entry,
     extraction.maintainer_pass_2026_11_12. The technical, lay and one-liner levels and the notes do not repeat
     the false sentence and are unchanged. The first sentence of (3) and the last of (4) are unchanged.
   - proof-main.tex, paragraph (3): final sentence replaced as the referee wrote it, followed by a short
     proof of the general criterion (the exchange commutes with complex conjugation exactly when
     c conj(c) = 1), that the exchange is always a complex isometry and an involution of trace 0, and hence,
     when real, a real isometry of determinant -1 with a three-dimensional nondegenerate -1 eigenspace
     (three reflections).
   - check.py: new `check_witt_exchange_real_exactly_for_unit_gram` (exact, Gaussian rationals; own small
     matrix inverse and determinant). Six bases of the flag: the proof's (c = diag(2,-2,-2), e_0 ->
     5/4 e_0 - 3/4 I_7 e_1, not real); that basis rescaled by (1 + I_7)/2 (v_k = +conj w_1, -conj w_2,
     -conj w_3; the exchange is exactly e_0 <-> e_1, e_2 <-> -e_3, e_4 <-> -e_5, an isometry, determinant -1);
     three more with c conj(c) = 1 (a phase, a real rotation, and one with c not diagonal); one generic basis.
     On all six: real exactly when c conj(c) = 1. Module docstring updated. No existing check changed.
   - coverage.yaml: entry for the new function (kind sampled, clause (3), with what is not enumerated);
     the old function's omits line now says "in the proof's normalisation".
   - `runcheck.py`: 6 of 6 pass. `check4.py`: 0 errors, check result pass (3 I405 notes, as before).

   Deviation from the referee's text, deliberate: section G defines the Gram matrix as
   `c_jk = 2 B(conj w_j, w_k)`. With the duality B(w_j, v_k) = delta_jk that the proof and the referee's own
   example use, the factor 2 is wrong: the rescaled basis has B(w'_k, conj w'_k) = 1, -1, -1, so 2B would give
   c conj(c) = 4. The criterion is c_jk = B(w_j, conj w_k), c conj(c) = 1 (derived in the proof, and checked on
   the six bases, including one with c not diagonal, which the referee's script did not test: it computed only
   the two diagonal normalisations). The replacement sentence itself did not carry the factor; the stored text
   states c without it. The referee's remark about a real factor 1/sqrt 2 is not stored (not rational, not
   checked).

2. `dark-matter.premise-cpt-covariance` 3 -> 4 (restatement of a postulate, D4).
   - Formal level, action clause: three sentences added. On the family (Yukawa and mass-matrix) terms the
     clause is premised in the adjoint reading only (C takes each term to its adjoint, does not conjugate the
     family matrices); in that reading it is consistent with non-zero J and C is a symmetry of the laws that
     also reverses the arrow (labelled argued, pointing at the Reading of
     `synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog`); the other
     reading sends J to -J (clause (iii) of that claim) so would require J = 0, and is not premised.
   - Technical level: the same in three plain sentences. Lay and one-liner unchanged (they stay true).
   - Front matter: version, amendments entry (restatement; evidence named as the new claim's
     `check_commutator_determinant_is_odd_under_conjugation`), two credit entries,
     extraction.maintainer_pass_2026_11_12. Nothing else in the premise touched; the fermion sector stays
     premised. No `derivations` block exists on this postulate, so the new claim is cited by claimref only.

3. `synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog` stays at 1
   (wording only, extraction note): one sentence added saying the decision was made on 12 November 2026, that
   the premise from version 4 premises the adjoint reading, and that the Reading's "the store does not
   choose" describes the premise at version 3.

The other three accepted claims needed no change. The exchange claim
(`synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state`) already cites "clauses (3),
first sentence, and (5)" and describes the exchange in a basis with v_k = plus or minus conj(w_k) as a real
isometry of determinant -1, a product of three reflections, which agrees with the corrected clause. The
baryon-number and abelian-charges claims do not refer to either entity.

## Dependants whose content may be affected

Pins left as they are (not repinned): `dark-matter.orientation-arrow-seventeenth-refutation` pins the
conjugation claim @4 and the premise @3; `neutrino.imported-ceiling-under-hypothesis-u-arrow`,
`one-relation.imported-flag-arrow-superselection` and
`one-relation.record-chain-votes-measurement-without-collapse` pin the premise @3. The layer 1 to 3 check
reported no pin warning for them, only I305 (store-wide re-confirmation count).

Of the conjugation claim (D1):
- `dark-matter.orientation-arrow-seventeenth-refutation` (uses @4): cites the claim for C = Ad(I_6) kappa and
  the antilinear flag conjugate, that is clauses (1), (2), (4), (5). It does not use the last sentence of (3).
  Its proof says the fibre metric is fixed by "the exchange of a null pair, which is an isometry of the
  completion's hyperbolic plane", which agrees with the corrected clause. Suggested: re-confirm and repin, no
  content change.
- `synthesis.z-adapted-witt-flags-energy-sign-follows-the-flag-bit` (mention, proof cites "(2)-(3)"): uses
  that the conjugate flag lies in the other family, the first sentence of (3). No content change.
- `dark-matter.premise-flag-as-datum` (mention of clause (2)): unaffected.
- `dark-matter.premise-cpt-covariance` (mention): cites the claim for the convention and clause (5);
  unaffected by D1.
- `synthesis.exchange-of-set-and-clear-...` (mention): already consistent, see above.

Of the CPT premise (D4):
- `dark-matter.orientation-arrow-seventeenth-refutation` (assumes @3): the one dependant to look at. Its
  formal level quotes the action clause without the family-term restriction and says conjugation "maps each
  solution space onto itself and exchanges the two orientations". With the adjoint reading C also reverses
  the arrow (argued). The claim already says orientation and arrow "are one choice, made once", so I see no
  contradiction, but the sentence that the bit "takes both values on every nonempty solution space" now holds
  for orientation and arrow together, and the new claim's Reading argues the exchange does not reach the sign
  of the baryon excess relative to J and the arrow. Suggested: re-check against premise @4 and add a sentence
  naming the adjoint reading and the joint reversal; whether its conclusion needs a restatement is a decision
  for Leon (it borders on D2 and the open problem, owned by the other agent).
- `synthesis.flag-conjugate-antilinear-...-reverses-jarlskog` (motivated_by; version 1): its formal Reading
  paragraph, technical and lay levels still say the store does not choose between the readings and that the
  choice is for the maintainer. I changed only the note, as instructed. Suggested: a wording pass on those
  three levels (the Reading is labelled argued and is not a numbered clause, so this may be wording only, but
  it sits in the formal level, so it is the maintainer's call whether it raises the version).
- `one-relation.imported-flag-arrow-superselection`, `one-relation.record-chain-votes-measurement-without-collapse`,
  `neutrino.imported-ceiling-under-hypothesis-u-arrow` (use @3): each restates the premise in one line
  ("leaves every action functional invariant, the gauge couplings included"; "the gauge sector's CPT-evenness
  as a premise"). None mentions family terms, J or the reading. Suggested: re-confirm and repin, no content
  change.
- `dark-matter.premise-flag-as-datum` (mention): unaffected.
- `store/open_problems.yaml` and `store/open_problems_settled.yaml` mention the premise; the open-problem
  record is the other agent's and I did not read into it beyond noting the reference.
- `synthesis.matter-asymmetry-registered-free-input` shows as modified in the working tree; that is the other
  agent's edit, not mine.

## Not done, and why

- The claim that C "also reverses the arrow" in the adjoint reading is stored as argued, with a pointer to
  the new claim's Reading (which rests on `one-relation.arrow-frequency-are-one-bit-level`); no proof or
  check of it exists and I added none.
- The consistency of the adjoint reading with J non-zero is stated as the decision gives it; I added no
  argument for it in the premise (the fermion sector is still premised, and the conjugation result's
  convention does not cover spinor fields).
- Premise version 3 has no amendments entry of its own (it predates this pass); I added only the entry for
  version 4.
- Not run: the full check, repin, lock, build. `store/.tp-lock.json` and `store/.tp-layer4.json` still record
  the old versions.
- The folder id of the flag-conjugate claim still carries its earlier title; renaming is left as its note says.

## Second pass (two wording follow-ups)

Validation after these edits: layers 1,2,3 give 0 errors, 0 warnings. No repin, lock or build.

1. `synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog`, version kept at 1.
   - Formal, Reading paragraph: "the store does not choose" replaced by: the premise
     (`dark-matter.premise-cpt-covariance`, from version 4) takes the second, adjoint reading, the first
     being kept for what it would require. The first-reading sentence is now conditional ("would require
     J = 0: with J non-zero it would not hold in the quark sector ..."), still labelled argued, and "a matter
     for the maintainer" is removed. The adjoint sentence gains "and as the premise now states". "Not shown"
     now notes that the adjoint reading is premised, not derived.
   - Technical: last sentence now says the premise takes the adjoint reading and the other would require the
     invariant to vanish. Lay: one sentence added to the same effect. One-liner unchanged.
   - Extraction note updated to match (it no longer says the Reading describes the premise at version 3).
   - Clauses (i) to (iv), the proof and the check are untouched.
   - Validator: no finding. Reason to know: the version rule (E206) compares the formal level against
     `store/.tp-lock.json`, and this claim is not in the lock yet, so the validator did not judge the edit
     either way. Any formal-level edit to a locked entity is counted as substantive (see item 2).

2. `dark-matter.orientation-arrow-seventeenth-refutation`, version kept at 10, pins not moved.
   - Re-read against the premise at version 4. The formal conclusion is unchanged: the proof needs only
     S_mu o C = S_mu for every mu (the premise, now with the adjoint reading on the family terms) and
     q(Cx) = -q(x); both stand, so the bit still takes both values on every nonempty solution space and is
     initial data. That Cx also has the opposite arrow is what the claim already says ("one choice, made
     once"). No restatement needed.
   - The sentence was first put in the formal level; the validator then raised E206 (substantive fields
     changed without a version bump), because it hashes the whole formal level. Since the instruction was a
     wording change with the version kept, I moved the sentence to the technical level, where the action
     clause is also quoted, and left the formal level byte-identical. If Leon wants the sentence in the
     formal level, that needs version 11 with an amendments entry.
   - Added: the technical sentence (adjoint reading on the family terms, citing the premise; the exchange of
     orientations then also reverses the arrow, argued, citing the flag-conjugate claim) and an
     extraction.maintainer_pass_2026_11_12 note.
   - For Leon's attention, not acted on: the flag-conjugate claim's Reading argues that no stored
     automorphism exchanges two states of the same laws and the same arrow with opposite baryon charge, so
     the exchange argument does not show the sign of the excess relative to J and the arrow to be initial
     data. This does not contradict the refutation's formal conclusion (which is about the orientation bit,
     identified with the arrow), but its lay level ("none of the framework's laws can make that choice")
     reads more broadly than that. I left it as it is.
