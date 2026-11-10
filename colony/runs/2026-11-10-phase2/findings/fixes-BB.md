# fixes-BB, fix round step 1 (referee R1), run 2026-11-10-phase2

check4: pending (orchestrator). validate: pending (orchestrator). Only colony/runcheck.py was run: all nine
functions of the three proposals PASS after the edits. No fix is rebutted. No id renamed. No sibling reference was
turned into a citation (step 2); each is left as a "sibling result of the same run, intended citation" sentence.

## 1. synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values (SOUND WITH FIXES)
- L1 title: now "One twisted mode per party: local weights bound CHSH; they and total parity give no (P)" (87
  characters; the referee's wording is over 90). Technical level: "for k a subfield of the reals". One-liner: field,
  "directions as observables", "products of local observables".
- L2 edges: no assumes edge (compared, not assumed); the note says so; the premise stays in lineage; the formal level
  keeps "Neither is assumed here".
- L3: the stored sentence of synthesis.premise-positivity-of-values is quoted in the Reading, with "for this
  realisation only" and what the counter-model does and does not show. The two further stored phrases the referee
  names are listed in the note for the maintainer.
- L4: "local products" defined as products of local observables, not of local elements; K = -(X1Z1)(X2Z2) =
  -f1 . f2 p1 stated in formal level and proof and ADDED TO THE CHECK (with anti-self-adjointness of the two
  factors); the result is said at formal, technical, lay and note levels to be the failure of local tomography over
  the reals.
- L5: technical level now "on this algebra". Argued labels unchanged (already as the referee wants).
- L6: proof of (ii) rewritten with the bilinear form beta(a, b) = lambda(ab) on the two planes of directions; no
  matrix, no transpose.
- L7: step 2. A sentence in the Reading names the effects result as the home of the general statement; clause (v)
  is unchanged until the citation can be made.
- L8: note updated (both papers' existence confirmed on the web; complex field is the note's statement).

## 2. synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables (SOUND WITH FIXES)
- R1: assumes edge to synthesis.premise-positivity-of-values@1 NOT added by me (FIXROUND rule 2); named in the
  note under "premises used, assumes edge for the maintainer", with the clauses that use it. Clause (i) heading now
  says "under (P) for its statements about states".
- R2 title: now "Sector average (x + axa)/2 keeps even states of (P) even iff a is parity-homogeneous" (84
  characters). Formal level defines E_a as the sector average and says that calling it a record map is a reading;
  technical and one-liner likewise.
- R3: the sentence added to clause (iv) (as a sibling reference to effects, plus stored clause (viii)).
- R4: Remark added after the Reading citing synthesis.univalence-from-even-stationary-dynamics (clause 3, read in
  the store at version 5), with the referee's three-point comparison, labelled argued; one sentence in the technical
  level. It is a claimref in a remark outside the theorem, not a uses edge (the result does not depend on it): the
  orchestrator may see W215-type or edge findings and should decide whether a lineage entry is wanted.
- R5: step 2; recorded in the note (clause (iv) to cite effects for E(C) and the value, keeping 12/25).
- R6: Wick, Wightman, Wigner stays "from memory".
- Overlap item 3 of the referee: one sentence in the Reading lists the three sufficient conditions for "at most 2".

## 3. synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them (SOUND WITH FIXES)
- K1: Meyer 1999 added as prior art over the rationals (note, Reading, technical); title now "No two-valued weights
  on the rational atoms of two modes; the even subalgebra admits them" (89); "no square root of 2" restated as true
  of the projectors and not of the unit vectors; "nine of the eighteen have r.r = 2" ADDED TO THE CHECK; one-liner
  and lay carry "rational coefficients".
- K2: pointer for size 2 corrected to clause (iii) of the effects result.
- K3: atom defined as in the base (self-adjoint part of the corner), with the form used here said to imply it;
  agreement of the two forms on all atoms labelled argued and not needed. Citation of the base is step 2.
- K4: P_0 = (1 - p1)(1 - p2)/4 stated, with the convention sentence; ADDED TO THE CHECK.
- K5: "whether three suffice is not shown here" at technical level and in the note.
- K6: Q(v_j) = Q(w_j) = 0 in the proof.
- K7: the claimref to (P) in the Reading replaced by plain text.
- K8: full references given, with what was checked on the web (by the referee) and what is from memory.

## For the orchestrator
- Step 2 items waiting on acceptance of the bases: local (iv) to cite the base for lambda_{-1} as the state sharp on
  P_s; local (v) to cite effects (iv); records (iv) to cite effects (v); Kochen-Specker to cite the base's atom
  definition and effects (iii).
- Maintainer: assumes edge (P)@1 on the records proposal; the three stored phrases affected by the local-weights
  result.

# Step 2 (sibling citations), after the base and the effects result were stored at version 1

check4: pending (orchestrator). validate: pending (orchestrator). runcheck: all nine functions PASS.
Abbreviations: BASE = synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional,
EFF = synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects.

## Local weights
- uses: BASE@1 and EFF@1 added. premise(BASE) in check_local_values_do_not_fix_positivity, premise(EFF) in the
  descent check.
- (iv): P_s is now "an atom in the sense of BASE" and lambda_{-1} = omega_{P_s}, the one state sharp on it by BASE
  (iii); added lambda_c(P_s) = (3 - c)/4 (already in the check). Proof cites BASE.
- (v) (L7): the general statement (lambda o E_N satisfies (P) iff the four sector weights are non-negative; the
  total-parity average adds no positivity) is now cited from the rider and statement of EFF (iv); its derivation is
  removed from statement and proof. Kept: the two-mode instances (the box and lambda_c) and the checked formula.
- Sibling sentences removed from the Reading and the note.

## Records
- uses: EFF@1 added, premise(EFF) in the one-mode check. lineage: synthesis.univalence-from-even-stationary-dynamics
  added (comparison only, as instructed); the Remark keeps its claimref.
- (iv) (R5): cites EFF (v) for the even state, E(C) and the value 14/5 (with u = U, Gamma = V; the check asserts
  U = e2 f1 and still recomputes 14/5 as a consistency test); only the record computation 12/25 is the clause's own
  content. The duplicated derivation is removed from statement and proof.
- Reading: the list of consistent "at most 2" conditions now cites EFF (v) for the formula; the splits condition
  (not one of the two stored results) is moved to the note as plain text.
- The assumes edge to (P)@1 remains for the maintainer (unchanged from step 1).

## Kochen-Specker
- uses: BASE@1 and EFF@1 added. premise(BASE) in the 18-atom check. EFF is cited only for the size-2 comparison in
  the Reading and is declared in coverage.yaml under untouched_premises with that reason; if the gate prefers, it can
  be moved to lineage instead (nothing in the proof depends on it).
- Atom definition (K3): now BASE's, with the special form (corner Q Pi) named in BASE's Definitions; the proof says
  each Pi_r is an atom of the orbit of P_0 in BASE (ii). The step-1 "argued" sentence about the two forms is gone.
- Size 2 (K2): a sentence in the Reading citing EFF (iii).

References among my own three proposals: plain text in notes only; none in formal text.
