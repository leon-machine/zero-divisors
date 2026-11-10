# Fixes SA, step 1: synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources

Verdict received: OVERSTATED (one false sentence at four levels). Accepted; nothing rebutted. The id is unchanged.
All edits in place in proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml).
runcheck: 5 of 5 pass. check4: pending (orchestrator). validate: pending (orchestrator).

## Referee fixes (verify/R1.md, section 2)
1. (F1) Restated to the true weaker statement at every level. Formal closing: "none gives an index within three
   standard deviations of the measured one on three observed axes alike without a number chosen for that purpose",
   plus the sentence that the Kaluza-Klein transverse potential at the vacuum end p = 1/2 is red with no chosen
   number (index -1, far too red; field strength +1). Technical: "where no stored source reaches" deleted; now
   "beyond five elevenths, reached by stored fields only at the vacuum end one half (index -1, far too red)". Lay:
   "tilted the wrong way, or not at all, or far too much". One-liner: "all miss the measured index or reach it only
   through a chosen number", with the p = 1/2 row named. Extraction note: the kill condition's outcome restated the
   same way. Check: the vacuum-end row (order 2, index -1, field strength +1) is now asserted.
2. (F2) Title now "... the index ledger of the stored mode equations" (88 characters). Tag `no-go` dropped. The
   note names, as outside the ledger, the five stored results the referee lists (holographic thermal reading with
   the string-gas Fact, sudden descent, Hadamard band data, local conversion of a Gaussian field, the joint
   curvature-coupling condition). Completeness labelled argued in formal, technical, one-liner and note; lay now
   says "as far as a search of the collection shows".
3. (F3) Clause (iii): "every wall of the cited theorems (unit trace is part of their setting; for vacuum, scalar
   and stiff walls it is stored in ...)". The three entities are added to `uses` (pinned @8, @2, @3), cited by
   claimref in formal and proof, and touched by premise() in the ledger check. The proof says it is not an audit
   of every stored field.
4. (F4) Clause (vi): heading "the one stored content reported red in the literature"; "if G'(0) > 0, as Cai and
   Wilson-Ewing report ... the sign is not derived here, and the criterion of (i) does not apply since the stage is
   not a power law"; G'(0) != 0 added to the hypotheses of alpha = -6N at formal, technical, one-liner and proof.
   New control in the check: with G'(0) = 0 the ratio tends to -12.
5. (F6) Clause (i): "extended here beyond P < 1, to q < 0 and to the de Sitter row, by the same normalisation",
   and the Wronskian sentence in the proof (weight T^(1+f) with a coefficient free of k).
6. (F5) One-liner: "a contracting dust stage with the frozen point's constant, which the store does not hold".

## FIXROUND rules and bridge leads applied
- Numbers from memory: none stood at a statement level (the referee confirmed). The Planck running is now named
  in the extraction note only, flagged from memory, with no significance.
- Bridge B1: the exact frozen-point stage and the promoted norm are cited to
  synthesis.frozen-phase-spectrum-not-red (iii), (iv) and not restated (note; clause (v) already cites it).
- Bridge B5: the note says which (P1) is meant (the pre-descent Kasner stage premise).
- Graviton decision and bridge B6: the note now says that the rows for the cross modes and the Kaluza-Klein vector
  quote the stored theorem's orders, and that the index attached to them presupposes a vacuum state for modes of
  the gravitational field, which this result does not adopt as the series' own structure. The formal rows state
  the friction excess and the order. FLAG for the maintainer: the corrected F1 sentence (the red row at p = 1/2)
  is itself an index of a Kaluza-Klein mode of the five-dimensional gravitational field, taken from the stored
  theorem synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling; if that
  stored theorem is restated under the decision, this row follows it.
- Rule 4: "no further stored structure has a mode equation" is labelled argued at every level.

## Not done (step 2)
The row citing the Kasner scalar-sector result (SB's proposal) is not added; it waits for that result's acceptance.

## Rebuttals
None.

## Step 2 (after acceptance of the Kasner scalar-sector result)
- Added the row the referee asked for to clause (iv): the scalar sector at the isotropic point of the scalar disk,
  (f, kappa, P) = (0, 0, 1/3), order 0 by clause (ii) of
  synthesis.scalar-sector-at-the-isotropic-scalar-kasner-point-obeys-the-spectator-equation, local index in [2, 3]
  for the comoving curvature perturbation by its clauses (iii), (iv), under its hypothesis of the stored adiabatic
  vacuum with a normalisation independent of k. Quoted, not re-proved.
- uses edge @1; claimref in formal and proof; premise() call and an assertion of the row in
  check_ledger_of_kasner_rows_from_residue_weights; coverage.yaml clause added; technical level and the "Not
  covered" sentence aligned (the conversion is no longer wholly uncovered: this row is the curvature perturbation
  at that one point).
- runcheck: 5 of 5 pass. check4 and validate: pending (orchestrator).
