# Fixes H-B, run 2026-11-24-three-routes

Referee report: verify/R-H.md, section 1 and "Overlaps and conflicts". Bridge entries: B1, B2, B6, B7.

## synthesis.trace-anomaly-leaves-no-exact-radiation-field-at-a-tame-wall

Verdict: SOUND WITH FIXES. All applied except fix 7 (see "Not applied"). Nothing rebutted. The title and status are
unchanged; no clause was weakened or strengthened except (iv), which now states the range of b exactly.

What changed (entity.md at every level concerned, proof-main.tex, check.py, coverage.yaml):
1. Lay (referee fix 1): "it ends earlier" now holds only "with the one free coefficient set to zero"; with it
   nonzero "it starts from an origin of a different kind, which is not the tame wall"; one sentence added that the
   result assumes the averaged stress of the quantum fields, the extra part included, shapes the field.
2. Formal (v), technical, proof (fix 2): the bounded branch credited to Fischetti, Hartle and Hu and to Anderson,
   the de Sitter root to Starobinsky, "cited from memory", "not as new". The one-liner says "(standard) branch".
3. Formal (vi), proof, coverage (fix 3): C/a^4 is identified with the thermal density (pi^2/30) g T^4, which
   defines T; 6 x 10^14 GeV is the upper end of the stored rung-scale range, a mass conditional on that result's
   Hypothesis (U), used by the stored mirror and seeding results as the ceiling of the descent temperature and
   used here as a temperature. One-liner: "the stored ceiling read as a temperature".
4. Formal (iv), proof (fix 4): "b outside [0, 2 alpha/3)" replaced by the exact statement: an origin with
   0 < p < 1 exists exactly for b < 0 (then p < 1/2) or b > 2 alpha/3 (then p > 1/2), with the proof by the signs
   of q(p) = 2 alpha p^2 - 6 b p + 3 b at p = 0, 1/2, 1. New check block: the sign pattern on a grid, the negative
   discriminant between, the double root p = 1 at b = 2 alpha/3, one rational origin on each side (p = 1/3 at
   b = -2 alpha/9, p = 3/4 at b = 3 alpha/4). The one-liner now also says that with b nonzero power-law origins
   have p != 1/2.
5. Formal (i) (fix 5): the square of the field strength defined, K = 4 Tr(R^2) over bivectors (in components
   Riem^2), and the Euler density written K - 4 Ric^2 + R^2.
6. Provenance of (A) (fix 6): the remembered de Sitter anchor is replaced, in the heading of (A), in the proof of
   (ii) and in the extraction note, by Mottola and Vaulin, arXiv:gr-qc/0604051, Eqs. (3.6b) and (4.12); the note
   says the check on the arXiv text was made in review and that the proposer did not read the paper. The proof now
   says plainly that the store fixes the size and relative signs and that the overall sign is an input of (A).
7. Cross-reference (overlaps section): in the Reading, beside "a mass term linear in conformal time through it or a
   continuation across it", the wall-conjugation result is named "filed alongside", by its id in plain text, as a
   result that assumes both (an exactly linear scale factor on the two sides of the wall, for a Dirac field on a
   prescribed field) and is therefore not available jointly with (A) and (E). No uses edge, no \claimref.
8. Bridge B1 (checked against the store: the Clausius theorem's (H3) reads "classical, or a renormalised
   expectation value"; the inverse-problem result reads "up to a matter-independent term"; both confirmed).
   (E) is renamed "the whole expected stress is the source", states that T_A is included and that nothing is
   assumed on operator equation against exclusive mean field. The Reading has a new passage, inside the part
   labelled argued: "whole" is the content of (E) relative to the store; with C/a^4 alone as source the exact
   radiation field is a solution; the store's routes do not decide (E). Both stored results are cited in text.
9. Bridge B2 (verified: the stored clause (iv) of the pair-production result has c = 1, 3, 12; mine are 3, 9, 36):
   one sentence in formal (ii) and one in the proof, as a check of that part of (A) only, with the statement that
   the Weyl-square weights are not used in this result; one assertion in the check and one coverage line. Cited in
   text only (a uses edge would put that result's hypothesis (OS) in this result's past cone for a test).

runcheck: 5 of 5 PASS after the edits (python3 colony/runcheck.py proposals/<id>/check.py).
check4: pending (orchestrator). validate_draft: pending (orchestrator).

Not applied:
- Referee fix 7 (credit.source names the run). BRIEF.md step 6 prescribes exactly `source: run <run>` for credit
  entries, stored entries carry that form, and FIXROUND rule 9 allows session metadata to keep the run name. Left
  for the maintainer to normalise if wanted.

Points for the central gates to watch: three new \claimref targets in text that are not premises
(synthesis.einstein-equations-from-c-loc-and-clausius, synthesis.inverse-problem-for-the-clausius-route,
synthesis.gravitational-pair-production-from-the-operator-source-at-first-order); all exist in the store.

## Repin on acceptance

- No pin changed. On acceptance of the wall-conjugation result, turn its plain-text id in the Reading into a
  \claimref (text only; still no uses edge), and add the reciprocal sentence the referee words to that result.
- Add the Mottola and Vaulin reference to store/references.yaml and cite it by key in (A) and the proof.

## Next steps (leads, not pursued)

- B7: the map T_A is, from memory, conserved only on conformally flat fields, and off that class Lovelock's theorem
  leaves no such local tensor; not checked here. The result claims conservation on the Robertson-Walker field only.
- B2 (ii): the coefficient of the trace-free vacuum response for the stored content is 48 x 9 + 12 x 36 + 8 x 3 =
  888 in the check's units, 296 in units of c; the stored remark on the rotation-weights result leaves it
  uncomputed. Not used here.
- B6: the mirror tension of my findings (reading (b2)) is with (CW) alone; no stored premise is touched. Recorded
  in attack-H-B.md; nothing in the proposal concerns it.
- The solutions with b != 0 beyond power-law origins; massive and interacting content; the Kasner branch
  (unchanged from the attack round).

## Decisions for Leon

1. Hypothesis (A): import it as a Fact (the anomaly of free conformal fields: weights 1, 11/2, 62 and 3, 9, 36,
   trace rho - 3P = +alpha E + b box R, with the Mottola and Vaulin locator the referee checked, plus the
   gravitational vector operator), or keep it a named hypothesis. Until it is imported the result's "holds given"
   does not show (A). Recommendation: import.
2. Hypothesis (E), reworded: is the state-independent anomalous stress T_A part of the source of the field
   equation? The stored routes leave it open (the Clausius theorem takes T as given; the inverse-problem result
   allows a matter-independent term). This is one ruling, tied to op.einstein-from-the-field-theory, and is not the
   question of operator source against mean field. If the answer is no, the exact radiation field stands and this
   result is a statement about a hypothesis the series does not hold.
3. Scope of the radiation-type hypothesis (unchanged): (a) collar only, (b) content cancelling the Euler weight,
   (c) no field equation imposed at the wall. Recommendation: (a), with (c) recorded for wall-based routes.
4. The free coefficient b: leave free (recommended) or set to zero.
5. Storing this result together with the wall-conjugation result: their hypotheses (A), (E), (RD), (DF) cannot all
   hold; both are conditional and can be stored with the two text cross-references. If any of the four is ever made
   a postulate, a pairwise contradiction record would be needed.
6. The ceiling 6 x 10^14 GeV is a (U)-conditional mass that stored results use as a temperature ceiling; whether
   that reading should be stated once in the store is a maintainer note.

## Second pass (verify/R-2.md, section 3: SOUND WITH FIXES; all four fixes applied, nothing rebutted)

1. Clause (iv), the proof's last sentence of (iv), the check's comment and docstring, coverage: "a power-law origin
   exists exactly when" is now "the order t^-4 balances for a power law with 0 < p < 1 exactly when", with "Whether
   a solution with that leading behaviour exists is not shown." Carried to the Reading ("any power-law origin, if
   one exists, has p != 1/2"), the technical level, the lay level and the one-liner; no level now asserts that an
   origin exists for b != 0. This weakens item 4 of the first pass above, which said "exists".
2. (E): "or the field has no other source" replaced by the referee's parenthesis (the equation has no other source:
   the cosmological constant is neglected and the content is that of (A)).
3. Reading: the stored inverse-problem result is quoted with its condition (the coupled system is variational only
   if the heat tensor is the Hilbert stress up to a matter-independent term, clause (v)); T_A is such a term;
   whether the system with it is variational is not settled there; the store does not require a local action.
4. Clause (ii): the comparison with the stored channel weights is "a check of the stored coefficient and of the
   three operators of (ii) in their Weyl-square combination, which (A) does not use".

runcheck after the second pass: 5 of 5 PASS. check4 and validate_draft: pending (orchestrator).
Decisions for Leon: unchanged, except that Decision 4 (the coefficient b) should now read "with b != 0 the leading
terms can balance only at p != 1/2; existence of such a solution is open".
