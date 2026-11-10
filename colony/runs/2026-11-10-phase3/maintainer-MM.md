# Maintainer pass MM (dark matter), run 2026-11-10-phase3 (10 November 2026)

Scope: MAINTAINER.md, general rules and section "MM: dark matter" (M1 to M5). No file of sections MD or MQ was
edited; dark-matter.imported-massless-graviton-production-rate was not touched (M5). In store/open_problems.yaml only
op.thickness-deposit-rule was edited (one dated paragraph in `known`, `source`, three ids in `entities`). No commit,
no repin, no lock, no build, no full check, no agents, no shell removal.

## Validation

`tp check --store store --layers 1,2,3 --keep-going --author leon`, last run after all edits:
**1 error, 0 warnings** (baseline 0 / 0). The one error is expected and not fixable by me:

- `E205 dark-matter.p4-democracy-asymmetry-over-oriented-towers`: "this id is retired and can never be reused". The
  tombstone is in place and the folder is still there, as instructed. On a scratch copy of the store with that
  folder taken out the same command gives **0 errors, 0 warnings** (that copy first showed one E214, a P4 reference
  left in the proof of dark-matter.mirror-share-assembled, which is fixed).

No check.py was changed. coverage.yaml changed in seven entities (untouched-premise lines added or removed);
`check4` rerun on each, one at a time, all "0 error(s) ... check result: pass": dark-matter.unit-ball-rule,
dark-matter.total-function-thickness, dark-matter.democracy-de-sitter-radius-unit-ball,
synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball,
dark-matter.asymmetry-arrow-counted-fifteenth-refutation, dark-matter.population-count-one-share-half-percent,
dark-matter.mirror-tower-copy-one.

## Entities changed

New (version 1, status postulate, `review: draft`):
- dark-matter.single-ideal-at-residues-zero-and-four ("SI"): clause (vi) of dark-matter.status-rule registered in
  that clause's words, with its cost (about 6.16, 8.254), its support and its limits, and "chosen knowing that the
  unit-ball fit needs it".
- dark-matter.odd-towers-populated ("Pop"): the population of the four odd towers, with the statement that it is
  inferred from the number it helps fit and adds no independent support.

Changed (old -> new):
- dark-matter.mirror-tower-copy-one 9 -> 10. Clause (v), first route, now states its premises: the common-N clause of
  P1 (already an assumes edge) and the charge reading "(C epsilon)" (epsilon a datum of the descent, the stance
  registered as synthesis.matter-asymmetry-registered-free-input), held as an in-statement hypothesis; the downstream
  proposition dark-matter.stored-asymmetry-charge-not-number (i) is cited as a later elaboration that is not used.
  P4 named as retired, its fork clause kept as a remark. (iii), technical, lay, one-liner, proof to match.
- dark-matter.asymmetry-arrow-counted-fifteenth-refutation 7 -> 8. assumes P4 removed; mirror-copy repinned 9 -> 10;
  (iii) and the other levels cite clause (v); coverage line for P4 removed.
- dark-matter.population-count-one-share-half-percent 6 -> 7. The same; hypotheses now read P1 to P3 and the common
  ceiling coupling.
- dark-matter.mirror-share-assembled 8 -> 9. Wording only (P4 references in formal and proof; clause (iii) cites the
  premises of the copy theorem's (v)). Pins not moved.
- synthesis.matter-asymmetry-registered-free-input 2 -> 3. P4 references (formal, technical, one-liner, lineage)
  repointed to the copy theorem's (v); records that (v)'s first route takes this stance as a stated hypothesis.
- dark-tower-matter.u-transposition-rule 2 -> 3. Marked as a definition (title and every level). Not re-typed: see
  "Not done as instructed".
- simulations.c-odd-towers-collisionless 2 -> 3, simulations.s1-one-species-per-tower 2 -> 3,
  simulations.s2-sheet-fluid 2 -> 3, simulations.s3-mirror-cluster 1 -> 2, simulations.s4-our-matter 1 -> 2,
  simulations.s5-halos 1 -> 2. Marked "model specification" (title and every level). C and S2 recorded as premises
  of the exclusive readings (C) and (W); S1's second clause cited as the stored theorem
  dark-matter.superselected-hence-dark-exactly-stable (the text called it a Fact), first clause recorded as a
  simplification against the stored five-dimensional content; S3 states its window of xi (about 3e-3 to 2e-2,
  dark-tower-matter.mirrors-composition). Status stays postulate: see "Not done as instructed".
- dark-matter.d-democracy-total-mass 1 -> 2. Note at every level: D with R1 and R2 forces one quantum per de Sitter
  ball (argued); D belongs to the de Sitter reading and is not counted with R1 to R3; it is the one dark-matter
  postulate naming the de Sitter radius, so it shares the exposure of w = -1 (text only). P4 reference reworded.
- dark-matter.p1-single-frozen-point 1 -> 2. Three clauses within the entity: (P1a) metric (theorem up to
  normalisation where the Weyl tensor has no kernel vector; independent choice on conformally flat regions: two
  stored theorems cited), (P1b) orientation (substitutable by P2 on the bit; not needed by the total: argued),
  (P1c) common N (postulated, no derivation). No new entities.
- dark-matter.r3-one-cell-per-unshared-direction 1 -> 2. Unit stated: each tower's own cell radius; R2 also supplies
  R3's unit; the fixed-common-length reading is not adopted.
- dark-tower-matter.h1-momentum 1 -> 2. Note pointing to the constituent-momentum result: formula forced up to a
  real factor given quadraticity and covariance; H1 weakened, not retired; what stays premised listed.
- dark-matter.unit-ball-rule 5 -> 6. assumes SI@1 and Pop@1 added; uses the sourcing lemma
  dark-matter.projection-every-towers-content-dilutes-ones@3 added (R2's "for the maintainer" item: P1 was missing
  from the cone); R3 repinned 1 -> 2. New paragraph "What the total rests on" (M4). Arithmetic and check unchanged.
- dark-matter.total-function-thickness 5 -> 6. assumes SI@1, Pop@1; one sentence on the unit of c d_b.
- dark-matter.democracy-de-sitter-radius-unit-ball 4 -> 5. assumes SI@1, Pop@1; D and R3 repinned to 2; note on
  R3's unit in the de Sitter reading.
- dark-matter.status-rule 4 -> 5. Marked note in (vi) (the two registered premises) and a marked clause (vii) (the
  two readings are alternatives; D not counted with R1 to R3; R3's unit).
- dark-matter.which-towers-are-populated 1 -> 2. Pointer to the registered premise Pop.
- note.dark-matter.setting-dark-matter-ratio-unit-ball 1 -> 2. Marked note after "with three premises added":
  what the audit of the cone found (M4).

Edited without a version change:
- synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball (v1, accepted in this run): assumes
  P1@2, SI@1, Pop@1 added, as its extraction note asked; the same sentence at every level: "This reading is not
  adopted: by Premise R3 as now stated the unit of thickness is each tower's own cell radius, so R2 also supplies
  R3's unit and stays a premise of the total, and the result holds only in the fixed-common-length reading."
  Layers 1-3 accept it at version 1. Its uses pins and the counts of clause (v) are left as audited.
- simulations.halo-shapes, simulations.merger (v2): extraction note only (the six premises are model
  specification; S2 and C are premises of exclusive readings and are listed together only because each result
  reports both readings).

Store files: store/tombstones.yaml (one entry appended, P4, replaced_by dark-matter.mirror-tower-copy-one, with the
scope caveat: the replacement proves only the mirror instance; the fork clause r = 0 is carried by no entity);
store/labels.yaml (the paper label T14:prem:democracy repointed from P4 to dark-matter.mirror-tower-copy-one, one
line); store/open_problems.yaml (op.thickness-deposit-rule only).

## M4: what replaced the count

No stored sentence of the form "N postulates support the ratio" exists on dark-matter.unit-ball-rule or in the
subject's setting notes (searched); the nearest are "Under R1 to R3" and "with three premises added". The audit
statement was added beside them. Checked with `cone` after the edits: the past cone of dark-matter.unit-ball-rule
holds eight postulates of the subject, R1, R2, R3, P1, P2, P3, SI, Pop, and the four foundation premises; D is not
among them. Stated without a count, by name; "the total remains a fit: two shares against one measured number";
chosen with the number known is quoted from dark-matter.status-rule (i), (ii), (vi) and
dark-matter.which-towers-are-populated only.

## Pins the orchestrator must move (stale after this pass)

- dark-matter.mirror-tower-copy-one 9 -> 10 in: dark-matter.coefficients-floors-they-give-what-gravity,
  dark-matter.mirror-share-assembled, dark-matter.mirror-share-one-how-fragile,
  dark-matter.mode-counts-two-modules-which-one, dark-matter.no-coupling-rule-odd-towers-follows,
  dark-matter.open-channels-their-costs, dark-matter.radiation-audit-what-theorem-closes-what,
  dark-matter.stored-asymmetry-charge-not-number, dark-tower-matter.mirrors-composition,
  dark-tower-matter.mirrors-temperature-p2, odd-extensions.imported-copy-theorem-soldered-residue,
  simulations.imported-mirror, standard-model.imported-sectors-superselection-mirror-copy,
  synthesis.dimmed-burst-time-rescaled-copy,
  synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio,
  synthesis.gauge-algebra-by-tower, synthesis.mirror-asymmetry-route-one,
  synthesis.mirror-temperature-measures-deposit-under-r, synthesis.tower-charge-sector-label-temperature-not.
- dark-matter.asymmetry-arrow-counted-fifteenth-refutation 7 -> 8 in: dark-matter.mirror-share-assembled,
  dark-matter.stored-asymmetry-charge-not-number, neutrino.imported-ceiling-under-hypothesis-u-arrow,
  one-relation.imported-flag-arrow-superselection, one-relation.record-chain-votes-measurement-without-collapse.
- dark-matter.population-count-one-share-half-percent 6 -> 7 in: dark-matter.mirror-share-assembled,
  dark-matter.total-function-thickness, synthesis.dark-to-baryon-total-...,
  synthesis.seeding-remainder-excludes-perturbative-pati-salam.
- simulations.c-, s1-, s2- (2 -> 3) and s3-, s4-, s5- (1 -> 2) in: simulations.halo-shapes, simulations.merger.
- dark-tower-matter.u-transposition-rule 2 -> 3 in: dark-tower-matter.five-dimensional-towers,
  dark-tower-matter.gauge-algebras, dark-tower-matter.same-kind-matter,
  synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free, synthesis.gauge-algebra-by-tower.
- dark-matter.d-democracy-total-mass 1 -> 2 in: dark-matter.two-reductions.
- dark-matter.p1-single-frozen-point 1 -> 2 in: dark-matter.imported-gravity-only-coupling,
  dark-matter.mirror-share-assembled, dark-matter.mirror-tower-copy-one,
  dark-matter.mode-counts-two-modules-which-one, dark-matter.parallel-boundary-mode-spaces-one-wall,
  dark-matter.population-count-one-share-half-percent, dark-matter.projection-every-towers-content-dilutes-ones,
  dark-matter.stored-asymmetry-charge-not-number, dark-matter.superselected-hence-dark-exactly-stable,
  odd-extensions.belongs-tower.
- dark-matter.r3-one-cell-per-unshared-direction 1 -> 2 in: dark-tower-matter.five-dimensional-towers,
  dark-tower-matter.imported-unit-ball-rule, simulations.effective-cross-section-sheet-matter,
  simulations.imported-unit-ball-rule-family.
- dark-tower-matter.h1-momentum 1 -> 2 in: dark-tower-matter.gauge-algebras, synthesis.gauge-algebra-by-tower,
  synthesis.lowest-causal-residues-zero-four-content.
- dark-matter.unit-ball-rule 5 -> 6 in: dark-tower-matter.imported-unit-ball-rule,
  simulations.imported-unit-ball-rule-family, synthesis.dark-to-baryon-total-...,
  synthesis.lowest-causal-residues-zero-four-content,
  synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands.
- dark-matter.total-function-thickness 5 -> 6 in: dark-matter.two-roots-are-chord-arc-quarter,
  simulations.imported-unit-ball-rule-family, synthesis.dark-to-baryon-total-...,
  synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3.
- dark-matter.democracy-de-sitter-radius-unit-ball 4 -> 5 in: synthesis.dark-to-baryon-total-....
Pins already set by this pass (no action): mirror-copy@10 in the fifteenth refutation and the population count;
R3@2 in unit-ball-rule; D@2 and R3@2 in the democracy result; P1@2, SI@1, Pop@1 in the synthesis result.

## Folder to remove (orchestrator)

- store/claims/dark-matter.p4-democracy-asymmetry-over-oriented-towers/ (one file, entity.md; left in place and
  unedited). Removing it clears the E205.

## Dependants whose CONTENT may be affected (not only pins)

- dark-matter.mirror-share-one-how-fragile (v7): still says "under P4, which Theorem ...(v) discharges" (formal (i),
  technical, lay, one-liner, proof), in plain text. True as history; should read "the copy theorem's clause (v)"
  at its pin review. No reference by id, so nothing breaks.
- dark-matter.which-towers-can-carry-arrow (v6): "the asymmetry per mode (P4, a premise on the fork)", twice, plain
  text. The fork clause is now carried by no entity.
- dark-matter.stored-asymmetry-charge-not-number (v10): the copy theorem's (v) now names it as the later
  elaboration of the charge reading; its own "(iv), (v)" citations hold. It assumes P1 for the common N, which P1
  now states as clause (P1c).
- synthesis.dark-to-baryon-total-... (v1): clause (v) counts ("twenty-three", "five (six with P1)", "eight",
  "fourteen") and "a model of P1, P2, P3, P4" are as audited before this pass. The subject now has 24 postulates
  (P4 out, SI and Pop in) and the closed form's cone holds eight. A sentence in the formal level says the counts are
  those of the pinned versions; a restatement of (v) is a new version for a later pass.
- dark-tower-matter.imported-unit-ball-rule, simulations.imported-unit-ball-rule-family: restate the total "under
  R1 to R3"; through dark-matter.unit-ball-rule their cones now also hold P1, SI, Pop, which their text does not
  name.
- synthesis.lowest-causal-residues-zero-four-content and, through it, synthesis.reversion-pairing-vanishes-residues-zero-four
  and synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion: they use dark-matter.unit-ball-rule for a
  number, so SI and Pop are now in their past cones (as R1 to R3 already were), although SI's own statement cites
  two of them as its mathematical basis. There is no cycle (a postulate has no derivation) and their proofs do not
  use SI, but "holds given" will show it. See "For Leon", item 4.
- simulations.halo-shapes, simulations.merger: assume S2 and C together on one derivation; now recorded as
  exclusive readings in the premises and in a note, not in the derivations' structure.
- dark-matter.two-reductions: assumes D, which now says the de Sitter reading and the unit-ball reading are
  alternatives.
- dark-matter.r2-one-quantum-per-unit-ball (not edited): its sentence "presupposes that all six towers are
  populated, which for the odd four is the inference of Observation ..." could now cite Pop.
- store/tags.yaml, tag premises-p1-p5: its title and `about` text still list P4 (shared vocabulary, not edited).
- Extraction fields (`source_formal`, `context_refs`, typing notes) of several entities still name the retired id;
  they are history and are not validated.

## Not done as instructed, and why

1. U as a definition (M1 b): not re-typed as an object. An object needs a new id (obj.*; this id would be retired),
   cannot be the target of an assumes edge (E203), and as a uses target raises W209; so the five results that
   assume U (one edge approved by Leon at acceptance of the Bott-shifted model) would lose the edge, U would leave
   their cones, and two check.py files that call premise() on it would have to change (E404). The fallback of the
   instruction was taken: entity, id, status and edges kept; marked as a definition in title and at every level.
2. Simulation premises as model specification (M1 c): the store has no such type (claim statuses are proved,
   imported, conjectured, refuted, postulate; a note cannot be used; an object cannot be assumed). They stay
   status postulate and are marked. They therefore still count as postulates in holds-given and in any count by
   status. S2 against C is recorded in text, not as two derivations of the two results.
3. Clause (v) of the copy theorem (M1 a): its premises are given as P1's common-N clause (edge present) and the
   charge reading as an in-statement hypothesis. No assumes edge to synthesis.matter-asymmetry-registered-free-input
   was drawn: adding a premise to the copy theorem's cone (and to everything downstream) was not decided, and that
   premise's own text says the count uses only the equality, not the provenance.
4. P1 (M1 e): the version-1 text had no common-N clause although one dependant assumes P1 for it; it is now stated
   as (P1c). This is an addition to the premise's wording, flagged.

## For Leon

1. U: do the full re-typing (new object id, retire this one, move five assumes edges to `about`, edit two checks),
   or keep it marked as now?
2. Model specification: add a type or tag to the store for it (so the six leave the postulate count), merge them
   into one entity, or leave as marked? And should simulations.halo-shapes and simulations.merger get two
   derivations, one per reading?
3. Copy theorem (v): draw an assumes edge to the registered stance (epsilon as initial data), or leave the charge
   reading as a stated hypothesis of the first route?
4. SI and Pop are assumed by the three stored statements of the total and so enter 48 future-cone entities, most of
   them through uses edges that cite dark-matter.unit-ball-rule only for a number (R1 to R3 were already there the
   same way). In particular the theorem that the reversion pairing vanishes at residues 0 and 4 now shows SI in its
   holds-given. Cutting that needs the citing results to stop using the closed form as a premise (a separate edge
   review), not a change to the new postulates.
5. The fork clause of P4 (equal asymmetry at r = 0) is now carried by no entity, only as a remark. Register it as a
   conjectured statement, or let it go?
6. R2's sentence on the population, the plain-text P4 mentions listed above, and clause (v) of the new synthesis
   result (counts) need a wording pass at their next version.
7. Tag premises-p1-p5: retitle now that P4 is retired?
