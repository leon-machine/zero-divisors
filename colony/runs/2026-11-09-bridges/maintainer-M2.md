# Maintainer pass M2, run 2026-11-09-bridges (10 November 2026)

Scope: the thirteen entities accepted in this run, store/open_problems.yaml and store/open_problems_settled.yaml
(MAINTAINER.md, "M2 owns", items 1 to 5, and the coordinator's six follow-up points). No other entity, no
tombstone and no Fact was edited. No commit, no repin, no lock, no build, no full check.

## Validation

`tp check --store store --layers 1,2,3 --keep-going --author leon`, last run after all edits:
**1 error, 0 warnings** (baseline 0 / 0). The one error is M1's expected one and not on my files:

- `E205 synthesis.imported-haar-average-purity`: the tombstone is in place and the folder is still there. It goes
  when the orchestrator removes the folder. No reference to that id is left in an edge, a premise() call, a
  \claimref or an `entities` list of my files (plain-text historical mentions in notes remain, see below).

Both YAML files load; every \claimref and every `entities` id in both names a stored entity.

Checks: three check.py files changed, each rerun with runcheck (all functions pass) and then check4
("0 error(s), 0 other finding(s); check result: pass"): the design entity, the finite-averages entity, the
Catalan eviction entity. check4 was also run on the six other entities whose premise lists or coverage changed
(no check.py change): result in the last section.

## Entities changed (all keep their version: accepted in this pass, not in the lock at that version)

Each carries a new `extraction.maintainer_pass_2026_11_10` entry.

- synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components: v1 -> v1. Uses the Steenrod Fact @1;
  (S) keeps its label and is "the imported Fact, clause (iii)" at every level; (G), (P) stay in-statement. Names
  the definite-side result by id (text reference, no edge). coverage: Fact under untouched_premises.
- synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five: v1 -> v1. Clause (4) takes the
  lower bound from the no-odd-map result (uses @1), so k = 5 on the definite side holds given the Steenrod Fact and
  the backgrounds (G), (P); the Thom-space argument is kept as a second route conditional on (T). Clause (3) cites
  the three-rung result (uses @1) for the twisted cohomology. `assumes: sheaf.tameness@1`. Title now ends "five given
  Steenrod's theorem". coverage: three untouched premises recorded.
- synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side: v1 -> v1. "Companion result" sentences
  replaced by the stored id (a \claimref in the formal level and the id in the note; no edge, since the definite-side
  result uses this one). It already had `assumes: sheaf.tameness@1`.
- synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four:
  v1 -> v1. Pins the Epstein-Glaser Fact @2 and cites its clause (vi) for (SD1)-(SD4) in clause (iii); uses the
  local-covariance Fact @1 and cites its clause (iii) in clause (iv). Clauses (iii), (iv) stay argued. The note says
  the id's phrase "no weyl term of degree four" holds only in the stated scope. The first Hadamard transport equation
  and the protraction identity stay stated hypotheses.
- synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt: v1 -> v1. `assumes` the Krein
  premise @3, with the sentence that under (K1) the gauge parameter is one, so the no-go is the stored statement and
  the free-gauge-parameter clause is the counter-statement outside the premise; the stored reading xi = 0 for the
  rung doublets recorded (formal, technical, note). Repinned: capacity entity @2, attachment entity @4; the note
  says both now state the K1 and xi = 0 readings themselves. No sentence calling the gauge-parameter zeros
  "admissible" was present.
- synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element: v1 -> v1. Cross-reference to the
  mass-terms result by id (note) and \claimref (technical). No edge.
- synthesis.mass-terms-are-pair-terms-of-the-arrays-and-only-the-charge-separates-majorana-from-dirac: v1 -> v1.
  Cross-reference to the order-four result by id and \claimref. No edge (mutual edges would be a circle).
- synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three: v1 -> v1. The retired
  mean-purity Fact removed from uses, lineage, formal text, proof and check; the comparison of clause (v) now
  points to the n = 2 case of the all-moment Fact (pinned @3). The note records the retirement in its favour with
  the powers-of-two scope. check.py: one premise() call repointed.
- synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector: v1 -> v1. Uses the
  design entity @1 and cites it in clause (ii). Retired Fact removed everywhere (edge, two premise() calls, three
  claimrefs), repointed to the all-moment Fact @3 with the powers-of-two caveat kept. The three eviction results
  left the premise list (comparison targets, referee R2's item (f)); they stay as claimrefs and lineage. This is
  what lets the eviction side cite its clause (iv) without a circle. check.py: premise() calls changed only.
- synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product: v1 -> v1. Sector lemma of
  clause (vi) cut to a citation of clause (iv) of the finite-averages result (uses @1). Fate table: the deficit row
  now reads "at version 4 (version 5 carries the sector column itself)". Still cites the two eviction results at
  version 3 and the deficit theorem at version 4 (pins left at those versions on purpose, see below).
- synthesis.eviction-keeps-one-of-catalan-many-replica-saddles: v4 -> v4. Repinned to version 4 of the one-saddle
  result; all-moment Fact @3; deficit theorem @5. Sector lemma in the proof of (iii) cut to a citation of the
  finite-averages result (uses @1; one premise() call added to the check).
- synthesis.eviction-keeps-one-replica-saddle: v4 -> v4. Notes only, plus one parenthesis in the proof and the pin
  on the deficit theorem moved to @5. Lemma left inline (below).
- synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio: v1 -> v1. Note only:
  op.dark-tower-running is settled on it.

### Inline lemmas: cut or left

- Cut to a citation: the mode-split entity's clause (vi) and the Catalan eviction proof of clause (iii). Both
  already applied the imported all-moment Fact to the sector, which is what clause (iv) of the finite-averages
  result does, so nothing new is assumed and the proofs stay complete. The genus form, Catalan limit, bounds and
  each entity's own enumeration check stay where they were.
- Left inline: the sector count in the one-saddle proof of clause (iii). It is a four-line Schur argument on the
  symmetric square of the sector and does not use the all-moment import; citing the finite-averages clause would
  make the index-two value rest on that import. Said so in its note.
- Left inline: the preliminary "split" paragraphs of both eviction proofs. Direction as R3 ruled: the eviction
  entities are self-contained and the mode-split entity cites them.

## Open problems (store/open_problems.yaml)

Dated "(10 November.)" paragraphs in `known`, `source` and `entities` extended, in every case below.

- op.wall-class-invariant (stays reformulated): the bounds as listed in MAINTAINER.md; attack item 1 annotated; the
  equivariant-index item marked done as a reduction and restated to the four things that remain.
- op.qft-loops-and-renormalisation (stays partial): item 3 marked started with what remains; new attack item 6:
  derive the protraction identity in the algebra core from vanishing torsion (coordinator's point 5).
- op.order-four-anomaly-and-sixteen: open -> reformulated. **Statement, attack list and success clause rewritten**
  around the pseudoscalar; items 1 and 2 answered negatively (argued); the modulo-16 statement not imported.
- op.curvature-coupling-across-subjects: open -> reformulated. **Statement, attack list and success clause
  rewritten**: three objects; what remains is the tilt's scalar and the doublets' coupling beyond tree level.
- op.island-dictionary (stays partial): the retired Fact's \claimref and `entities` id repointed to the design
  entity with the powers-of-two caveat; one paragraph on the split, the sector column and the finite averages.
  Attack items unchanged.
- op.qft-structural-inputs (stays partial): one paragraph (number-current lead closed, the order-four result, the
  gauge-parameter zeros not admissible under K1); one sentence added to attack item 1.
- op.pair-sector-current (chosen over the generation problems: the mass-terms entity names it, and its subject is
  the Majorana element's pair component, the B - L current): one paragraph; Premise (M) untouched.
- op.odd-towers, op.thickness-deposit-rule: one sentence each pointing at the coefficient table and what it does
  not decide.
- op.dark-tower-running: **settled** (negative), moved to the end of store/open_problems_settled.yaml with status
  settled, a settling paragraph and its three attack items marked, as earlier settled problems were. The open list
  has 34 problems, the settled list 27.

The original statements of the two reformulated problems are no longer in the file (they are in git history);
their content is carried in `why` and the older `known` text.

## Dependants whose content may be affected (not only pins)

- synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields: its "Results that use it" list does not
  name the curvature-coupling result, which now has an assumes edge to it. Not mine to edit.
- The mode-split entity's fate table describes the two eviction results at version 3 and the deficit theorem at
  version 4, and its pins are left there. If `tp repin` moves them, the text still says which versions it reads.
- synthesis.imported-haar-moments-of-random-pure-state (M1, v3) is now the only home of the general mean purity;
  five of my entities pin it @3.
- Nothing outside the run depends on the thirteen entities except M1's text references.

## Not done, and why

- synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike
  and synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off still present the gauge
  parameter and the doublets' curvature coupling as free. Neither maintainer owns them. **Left for Leon**: a note
  on each under decisions 7 and 10.
- No `merged_from` on the design entity: earlier retirements of an imported Fact in favour of a derived result
  wrote none; the retirement is in its note and in the tombstone.
- Plain-text mentions of the retired id remain in notes and amendment records of the two eviction entities, the
  design entity and the finite-averages entity (history of what was removed). They are not references.
- The id of the design entity still says "rotors" and the kernel entity's id still says "no weyl term of degree
  four": ids are never renamed; both notes state the scope.
- Check function names that say "imported value" were kept (renaming would change checked_by and coverage for no
  gain; the value is still the n = 2 case of an imported Fact).
- No new premise() calls for the edges added to the no-odd-map, definite-side, kernel, curvature and mode-split
  entities: recorded under `untouched_premises` in each coverage.yaml instead, with reasons.
- Nothing in the two new Facts was checked against a source by me; I cite them as M1 wrote them.

## check4 on entities with changed premise lists (no check.py change)

All six pass with 0 errors and no warning: the curvature-coupling, definite-side, mode-split, kernel and
no-odd-map entities (the only findings are I405 notices that each new premise is "declared and untouched, as
expected", from the coverage records) and the one-saddle eviction entity (0 findings). With the three whose
check.py changed, nine of the thirteen entities were rerun through layer 4; the other four (three-rungs,
order-four, mass-terms, dark-tower table) had notes or text references changed only.
