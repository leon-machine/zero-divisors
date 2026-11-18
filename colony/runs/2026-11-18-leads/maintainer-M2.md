# Maintainer pass M2, run 2026-11-18-leads: store/open_problems.yaml

One file edited, `store/open_problems.yaml`, by exact replacements inside twelve problem blocks. Nothing else under
`store/` was touched; no commit, no push, no agents, no process killed.

- Before: 6174 lines, 41 problems. After: 6578 lines, 41 problems, same ids in the same order.
- The 29 other blocks are identical to the copy taken at the start, so the earlier session's edits of today are
  kept: `op.the-number-n` (last entry), the three entity additions, and the reworded sentence in
  `op.matter-asymmetry-origin`.
- YAML loaded after each group of edits (`yaml.safe_load`), with a comparison against the starting copy.
- Every statement was taken from the stored entities as accepted (their formal and technical levels and extraction
  notes), not from the first drafts. Labels proved / computed / argued / cited from memory follow the entities.
- Exact old and new text: `work/M2/open_problems.diff` (unified diff against `work/M2/open_problems.before.yaml`).
  The edit scripts are `work/M2/g1_walls.py`, `g2_gravity.py`, `g3_horizons.py`, `g4_rest.py` and three small
  corrections made on reading back (`g1b_patch.py`, `g3b_patch.py`, `g4b_patch.py`), with helpers in `oplib.py`.

## Check
`python -m tp check --store store --layers 1-3 --keep-going --author leon`, run once after the last edit and after
all thirteen ids were in `store/claims` (the acceptance process had ended): **0 errors, 0 warnings**, 121
information findings (I213 x 119, I126, I305; none about open problems). 13 seconds. Log:
`work/M2/tp_check_layers_1-3.log`. No E216 or E217: every `\claimref` and every entity id in the file resolves.

## Changes, problem by problem (old -> new)

### op.eigenbundle-class-of-degenerations
- status: `open` -> `reformulated` (the statement is restated around what remains).
- source: + the three results accepted 18 November and Leon's decisions (conjecture restated; periodicity not
  imported).
- statement: "Determine this class ... say when its vanishing is sufficient ..., classify it for an isolated
  degeneration in codimension m, and relate it to the wall class and the rung count" -> "Restated 18 November":
  three of the four questions answered (sufficiency over a ball with flat directions added; order two in
  codimension three on the least module; the dying line across the collar of a corank-one wall). Open: codimension
  five and beyond and whether the period-eight clock governs it; the class relative to the whole base; two-sided
  against one-sided rung count.
- known: + paragraph "(18 November, second pass.)" on the three results with their limits, the restated
  conjecture, and the Kerr reading labelled "computed in a working file; not stored, not refereed" with its argued
  part marked.
- attack 1 (m = 3): -> "Answered (18 November; ...)", item as posed kept, what remains (codimension five and
  beyond; infinite order in codimension five is "classical, from memory").
- attack 2 (tame walls): -> "Answered ...: agreement, for two-sided completions only"; one-sided counts not
  rederived; what remains.
- attack 3 (Kerr): -> "Closed negatively as posed (18 November; computed, not stored)".
- attack 4 (sufficiency): -> "Answered ..."; yes over R^m with flat directions added, not for the given form on
  the given bundle; what remains.
- success: restated (done for codimension three and across the collar; what would complete it).
- entities: + the three new ids (7 -> 10).

### op.wall-class-invariant
- source: + the corank-one wall result and the decision restating the conjecture.
- known: + "(18 November, second pass.)": what the new result says of tame walls (class across the collar is the
  dying line, the information of W(Sigma); lower bounds on the two-sided number of rungs of the stored form) and
  what it does not (nothing on the one-sided k(Sigma) asked for here, no new rung count, not the class relative to
  the base, not naturality or conservation); `sheaf.wall-class` restated in clauses (a) and (c), still conjectured.
- entities: + `synthesis.eigenbundle-class-of-a-corank-one-wall-is-the-dying-line` (17 -> 18).
- statement, status (`reformulated`), attack, success: unchanged; the question asked there is not touched by the
  new result.

### op.kerr-ring
- attack 1: + a dated note "(18 November; a reading computed in a working file, not stored and not refereed.)":
  the same negative reading (cover = the degree-one class of the plane family pulled back; three = degree of the
  field strength, only its parity a class; no completion statement applies), that it does not decide the item, and
  the first step. Nothing else changed; the statement keeps the conjecture's wording, as decided.

### op.gravitational-field-at-null-momentum
- status: `open` -> `reformulated`.
- source: + the three results and the decision (no signal outside the light cone; how it is met is the problem).
- statement: "Decide what the series says of those two components, and whether it requires its gravitational field
  to commute ..." -> "Restated 18 November": the requirement is adopted; the slaved field is not the full account;
  no quantum is held or posited; two free directions and four constraints at null momentum; open is how the
  requirement is met. It does not say the two components carry states or variables, and does not say they carry
  none ("not decided, in either sense").
- known: + "(18 November, second pass.)": the decision, then each of the three results with its labels and
  numbers (76 of 82 links; 878 of 2750 events; 32 of 252 and 172 of 502; about 1.3e-13 in the proposed experiments;
  order one near 190 kg at a metre against 1e-14 kg, argued, under hypothesis (D)); the survey called a survey.
- attack 1: -> "Answered": no stored premise found implies commutation (survey); unitarity does not (proved).
- attack 2: -> "Answered": no localisation floor is relevant; no stored bound; the size.
- attack 3: -> "Answered (... as restated after review)": the lattice Maxwell result; what remains for gravity.
- attack 4: -> "Restated": the count; burst ratio (2 + g_h + o)/(1 + g_s), that is (2 + g + o)/(1 + g) if the two
  components emit and (2 + o)/(1 + g) if not; the earlier "restate the burst baseline with g = 0" corrected.
- success: restated to "how the requirement is met".
- entities: + the three new ids (7 -> 10).
- title and why: unchanged.

### op.einstein-from-the-field-theory
- attack 2 (the trace-free channel): the one-line quoted string -> a folded block with the same first sentence
  plus "Narrowed (18 November; ..., clause (vii))": (OS) assumes the clause and does not derive it; the static
  coupling and the entangling phase do not test it (2/3 - 1/6, proved); the rate does (15360/1519247, about one
  percent, and no vectors; computed given (OS)); neither derivation nor independence obtained. The item was changed
  to a block scalar because a `\claimref` cannot stand in a double-quoted YAML string.
- source: + one clause. entities: + the null-momentum result (8 -> 9).

### op.which-capacity
- source: + the black-hole result and the decision.
- statement: "Under the adopted costed clause ... rho is decided for fields with one horizon ... Open: (a) fields
  with more than one horizon ... (b) the Schwarzschild field" -> "Restated 18 November": the clause as restated
  (rotations commuting with the wedge's boost, the boost a positive multiple of the horizon's Killing flow); de
  Sitter stands on that reading; silent on the Schwarzschild exterior and the static region of Schwarzschild-de
  Sitter, rho free; other multi-horizon fields not computed; left: the norm and free-fall candidates
  (r_0^3 = 3M/Lambda, one scale per horizon), not adopted.
- known: + "(18 November.)": the result (three readings, the twisted gauge, the candidates), the decision, and a
  sentence that the earlier "decides fields with one horizon" is superseded.
- attack 1 and 2: -> "Answered (18 November; ...)", items as posed kept. attack 3: unchanged.
- success: restated (rho free on the two fields under the present premises; what would close the problem).
- entities: + the new id (8 -> 9). status stays `reformulated`.

### op.helicity-per-boundary-mode
- source: + one clause.
- statement, last sentence: "What is open is joint J3: ... by proving the identification of each channel with a
  two-dimensional mode, at the horizon" -> the channel reduction is derived for spins 0, 1/2, 1 and, since 18
  November, both parities of spin 2 on oscillating channels with l >= 2, given cited facts; what remains of J3 is
  the current-boson identification and the partial-wave lift (premise) and those cited facts.
- known: + "(18 November.)": even parity proved in both directions; (C3) proved; clause (3) superseded on
  oscillating channels only; (C1), (C2) still cited from memory; the degree bound no longer needed; not attempted:
  l = 0, 1, regular charts, the fuzzy-sphere identification.
- attack 1: "restated 9 November, second pass" -> "restated 18 November": done since then; what remains.
- attack 2 (fuzzy sphere): unchanged. entities: + the new id (10 -> 11). status stays `partial`.

### op.positivity-of-values
- source: + one clause.
- known: + "(18 November.)": both results, the limit on what the first says of (P), the prior art flagged as read
  through abstracts and a summary, and "the sentence above that linearity is undecided is superseded".
- attack 5 (Gleason type): -> "Done (18 November; ...): yes, and without the sign condition".
- attack 6 (running maxima): -> "Done (18 November; ...)".
- attack 7: new, "New (18 November)": which projectors can label a record (all rational projectors, or local
  products only), tied to the parity item; more than two modes (needs an imported representation fact, named as a
  candidate, not checked); Mushtari 2001 to be read, so far through a summary.
- entities: + two ids (8 -> 10). statement, status (`open`): unchanged.

### op.curvature-coupling-across-subjects
- source: + one clause. known: + "(18 November.)": the heating does not constrain the open datum; on the chain's
  bath the stored exclusion is conservative (margins from above 2.2 and 1.5 to about 2.83 and 1.96) and is not
  decided by the couplings at either stored assignment; the tilt window on the chain's scalars not treated.
- entities: + the heating result (9 -> 10).

### op.graviton-rate-as-classical-field-process
- source: + one clause.
- known: + "(18 November, second pass.)": no trace part of the fermion (or vector) channel from the stored trace
  statement at the next order; first effect on the scalars' trace term at order G^3 (argued); the fermion
  coefficient is not thereby unchanged at that order; the channel weights rederived without angular integration.
- entities: + the rotation-weights result (10 -> 11).
- Beyond the brief (see "Declined and judgement calls"): two short notes on the burst baseline.

### op.island-dictionary
- known: + one sentence "(18 November.)": the return delay is listed here as the timing half of the question; it
  stays conjectured, with no proved core. entities: + `scrambling.return-delay-scrambling-log-recovered` (11 -> 12).

### op.order-four-anomaly-and-sixteen
- attack 3 (the wall theory item): + one sentence "(18 November: ...)": the link to the eigenbundle class through
  real K-theory was tested and is a resemblance (order eight on RP^5, sixteen first on RP^8: computed, not stored;
  the sixteen here not the order of that class: argued).

## Declined and judgement calls
- **Status.** Two changes, both `open` -> `reformulated`, because those two statements are restated.
  `op.which-capacity` could be read as settled (its third success alternative, rho free under the present
  premises, now holds on both named fields); I left it `reformulated` because the brief names what is left and
  attack item 3 is untouched. `op.positivity-of-values` stays `open` and `op.helicity-per-boundary-mode` `partial`.
- **Titles not changed.** `op.gravitational-field-at-null-momentum` still reads "... and commutation with matter
  at spacelike separation", and `op.which-capacity` still names "more than one horizon, and on Schwarzschild".
  Both still find the problem; say if they should follow the restated statements.
- **Earlier dated paragraphs left as they are**, in the file's manner; where a new paragraph overrides one it
  says so ("superseded").
- **op.island-dictionary: no new attack item.** The findings recommended one (derive the delay from the eviction
  window); the brief asked for one sentence and the entity, so only that was added.
- **op.graviton-rate, beyond the brief.** Its `known` says "At g = 0 the factor is D = 2 + o" and attack item 4
  says "dropped (g = 0, D = 2 + o)". An accepted result now says that is the ratio to a baseline that is not the
  standard expectation. I added one sentence to the new paragraph and a dated parenthesis to item 4, pointing to
  the null-momentum problem. Remove them if this was meant to stand only there.
- **op.graviton-rate attack items 1 and 2** are described as done in its `known` (18 November) but carry no "Done"
  prefix. That predates this pass and I left it.
- **Entities lists** now run to 9 to 18 ids; the header comment says 2 to 8. Several were over before this pass.
- **Not written in this file because M1 owns the entities:** I refer to `sheaf.wall-class` and to the tube-point
  clause "as restated", and to the conventions' paragraph "Requirement (18 November 2026)" (present when I
  checked). If M1's restatements end differently from D3 and D4, those sentences need a second look.

## Needs Leon
1. `op.positivity-of-values`, new item: which projectors can label a record. A reading of the residual postulate,
   tied to the parity setting. Mushtari, Lobachevskii J. Math. 9 (2001) 47, is to be read before the
   additive-weights result is described as new.
2. `op.which-capacity`: whether the norm and free-fall rule is adopted as a further premise on black-hole fields;
   and whether the problem is to be marked settled.
3. `op.gravitational-field-at-null-momentum`: how the requirement is met is the problem. Outside this file, the
   sentence of `pred.dimmed-evaporation-bursts` (and of `synthesis.dimmed-burst-time-rescaled-copy`) on g = 0 gives
   a ratio to a baseline that is not the standard expectation; a wording fix whichever option holds.
4. `op.helicity-per-boundary-mode`: whether (C1) and (C2) are imported as Facts, and whether the postulate J3 is
   narrowed again (a premise restatement).
5. `op.kerr-ring`: whether the conjecture's "winding number three as an invariant" is restated as the parity
   together with the degree of the field.
6. `op.eigenbundle-class-of-degenerations`: whether the two-sided rung count becomes a stored notion beside the
   one-sided k(Sigma).
