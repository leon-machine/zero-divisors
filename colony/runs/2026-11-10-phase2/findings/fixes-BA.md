# fixes-BA, fix round step 1, run 2026-11-10-phase2

All fixes applied in place in proposals/<id>/. Only runcheck was run (all functions PASS in the three proposals).
check4: pending (orchestrator). validate: pending (orchestrator). Sibling references are left as text (step 2).
Nothing is rebutted.

## 1. Base: synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional
- B1 (lay): the sentence "the Born rule follows ..." replaced by the referee's wording; added "It does not show that
  physical states are of this kind, nor which questions are measurements."
- Leon's decision (every level): lay now also says the assumption that chances do not depend on which other
  questions are asked alongside is moved into (P), not removed, and that certainty on an atom is itself assumed;
  one-liner says the non-contextuality assumption is relocated and not removed and physical states are not shown to
  be sharp; formal scope and technical already said so. No sentence at any level says the Born rule follows or is
  derived without "under (P)" and sharpness on an atom (text search for follow/deriv done).
- B2: "given sharpness on an atom, which is itself assumed" added in the formal scope and the technical level.
- B3: definition sentence added: a projector with Pi x Pi = <Pi x>_0 Pi/<Pi>_0 (corner k Pi) is an atom, and in
  Cl_k(l,l) the vacuum projector and its orbit are of this form. Written this way round because "every atom of
  Cl_k(l,l) has corner k Pi" would need the classification of the algebras, which the proof does not use. One line
  added to the proof of (ii): the orbit of an atom with corner k Pi has corner k R.
- B4: literature flags unchanged (from memory).
- Clause labels, final: (i) atoms exist in every signature: proved (blade argument, table computed, sampled, not
  used); (ii) orbit and hermitian squares: proved; (iii) the weights under (P): proved; (iv) each hypothesis needed,
  atom condition necessary and sufficient: proved by examples and a general argument. Check: 4 functions, kinds
  sampled, sampled, partial, partial; no check change.

## 2. Effects: synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects
- E1: synthesis.univalence-even-extension-split@3 added to uses, cited in clause (iv) of the formal text, in the
  technical level and in the proof; premise() call added to the parity-average check function.
- E2 (lay): "with one mode for each party" added to the limit 2.
- E3: not done, step 2.
- E4: the last part of (iv) restated for the grading automorphism alpha and E = (id + alpha)/2, with the remark that
  the grading need not be inner; proof sentence adjusted.
- E5: no change needed. Kept: the parity-average lemma with its rider, and the formula E(C) = X u + Z Gamma.

## 3. Splits: synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them (OVERSTATED, restated)
The referee is right: the null pairs as vectors fix the split; only the two isotropic subspaces leave a positive
definite form free. Restated at every level:
- Title (88 characters): "Splits adapted to the isotropic subspaces of the null pairs; states of (P) common to all".
- One-liner: the referee's text (with "for one mode a scale; the stored boosted frame is one case").
- Formal: "adapted (to the isotropic subspaces W, W')"; clause (i) heading and a first sentence that the pairs as
  vectors determine the stored split; closing sentence as the referee's; scope says (P) as stored names the vectors,
  so no datum is shown missing from the stored premise.
- Technical, lay, extraction note: restated the same way (lay with the referee's two replacements).
- S1: one mode: adapted splits are the lines k(v + c w), k(v - c w), c > 0; an orthonormal frame exists iff c is a
  square; c = 2 over Q computed in the check (Q = 2 and -2) and in the proof.
- S2: stored twistor-form theorem, clause (iv), named in the formal scope and the proof; added to uses @5 (comparison
  only; coverage lists it as untouched). If the gate objects to an unused uses entry, move it back to lineage.
- S3: unchanged (note only). S4: scope sentence added (positivity without reality for every split: not addressed).
- S5: sentence added in (iv) and in the proof. S6: flags unchanged.
- Not added: the referee's remark that the pair state also fails positivity for the second split (-171/80); I did not
  recompute it, so it is not in the text.
