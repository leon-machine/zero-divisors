# Maintainer pass M1, run 2026-11-09-bridges (10 November 2026)

Scope: the new Facts, the retirement of synthesis.imported-haar-average-purity, and the entities that existed
before the run (MAINTAINER.md, "M1 owns", items 1 to 7). Nothing in the thirteen entities accepted in this run or in
store/open_problems.yaml was edited. No commit, no repin, no lock, no build, no full check.

## Validation

`tp check --store store --layers 1,2,3 --keep-going --author leon`, last run after all edits:
**1 error, 0 warnings** (baseline 0 / 0). The one error is expected and is not fixable by me:

- `E205 synthesis.imported-haar-average-purity`: "this id is retired and can never be reused". It is raised because
  the tombstone is in place and the folder is still there, as instructed. It goes when the folder is removed.

Checks rerun after their check.py changed (runcheck, then check4; both "0 error(s), 0 other finding(s); check
result: pass"): synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free,
synthesis.eviction-deficit-against-page-deficit.

## Entities changed

New (version 1, status imported, `review: draft`):
- synthesis.imported-steenrod-cup-one-square-is-a-natural-cohomology-operation: new, v1. Clause (iii) is hypothesis
  (S) of the no-odd-map result word for word in its mathematical content (Sq^2 on degree 3); (i), (ii) are the same
  statement in every degree k (Sq^{k-1}[a] = [a cup_1 a]). The attribution sentence (equivariant form from the
  acyclic-carrier construction on regular complexes by carrying the deck group along; that passage is part of the
  Fact) is in the formal text. Steenrod 1947 and Steenrod-Epstein 1962, flagged cited from memory, primary texts
  not read (the pages 290-320 of the 1947 paper are from memory too).
- synthesis.imported-local-covariance-with-scaling-of-time-ordered-products: new, v1. Clause (iii) is the form the
  curved-field kernel entity's note asks for (local and covariant functional, almost homogeneous scaling under a
  constant rescaling of the displacement gauge field with the mass rescaled inversely; coefficient of a derivative
  of delta of order j a constant-coefficient polynomial in the curvature operator, its derivatives and the mass of
  dimension omega - j; 2 - j at omega = 2). Hollands-Wald 2001, 2002; Brunetti-Fredenhagen 2000 for the microlocal
  setting; cited from memory, not checked.

Bumped:
- synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products: 1 -> **2**. New
  clause (vi) with (SD1) to (SD4) exactly as the kernel entity's note lists them; Steinmann 1971 added to
  imported_from; clauses (i) to (v) untouched. M2 pins `@2`.
- synthesis.imported-haar-moments-of-random-pure-state: 2 -> 3. The formal text carries the n = 2 value itself
  ((d_A + d_B)/(d_A d_B + 1), and the equivalent variance form) for all dimensions, Lubkin 1978 named as prior art
  and added to imported_from; a sentence says the value is derived in the store at powers of two (text reference
  to the design result, no edge) and rests on this Fact otherwise. The retired Fact's verification record (the
  secondary source's missing factor 1/m) is carried into the note.
- synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free: 1 -> 2. Clause (iv): the zeros in the
  gauge parameter are arithmetic only; under clause (K1) of the Krein premise the gauge parameter is one, so they
  are not admissible (only alpha = 1 at n_g = 3 remains, the stored cancellation); added that at the stored
  tree-level reading xi_R = 0, B = 16 n_g - 40 vanishes at no integer (8 at three). Clause (v): none of the eleven
  variants moves the gauge parameter, so the tally (2 / 2 more / 7) stands. Proof (iv) and the independence
  paragraph, technical and lay levels, coverage follow. Check: one label changed (arithmetic kept), two assertions
  added. Conclusion unchanged. No assumes edge added (the Krein premise is already in the past cone through the
  Krein-quartet result; the premise and the tree-level result are cited by text reference).
- synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations: 3 -> 4. A scope
  paragraph in the formal level (with matching technical and lay sentences): the cancellation is a property of the
  attachment modules (xi = 1/6 by the spectrum of the helicity-zero module), not of the content, whose rung
  doublets carry xi = 0 at tree level (synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point,
  clause (ii)), so B = 8 on the content at gauge parameter one (Krein-quartet result, clause (iv)). Clauses (i) to
  (v), proof and checks untouched.
- synthesis.eviction-deficit-against-page-deficit: 4 -> 5. Clause (i) restated: sector mean entropy and sector
  deficit first, with the bounds of clause (vii) of the mode-split entity
  ((m-2)/(2n) + 2(m-1)/(2mn+m+1) < delta_sec < m/(2n) - 1/(mn) < 1/2), the abstract tensor-product bounds kept
  beside it unchanged, delta_sec = delta_P - Delta; the bound (m-1)/(2n) holds on a sector for m >= 4 and fails at
  m = 2. (ii), (iii) unchanged; the closing paragraph gives both crossing intervals. New check function
  check_sector_deficit_bounds (registered, coverage record added). **The mode-split entity is not a premise**: it
  uses this entity (its fate table), so an edge would be a cycle; the proof of (i) rederives the sector value from
  Page's Fact, and the mode-split entity is named by text reference only.

Edited without a version change (no hashed text touched: technical or lay level and extraction notes only):
- singularity.eviction-window-thermal-product-radiation-entropy (v7): technical sentence and note: the tensor
  product of marginals is the product of commuting even elements; cites the mode-split entity.
- singularity.assembled-page-curve-up-typicality (v3): the same, with the sector remark.
- descent-lift.imported-fermionic-operations-are-even-reduced (v1): note that its content is derived for mode
  algebras in the mode-split entity; not retired.
- synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy (v2): note on clause (iii) (self
  pair term, vocabulary of the mass-terms entity).
- synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants
  (v4): note on clause (v): first half supported by the curved-field kernel entity, clause stays argued; the two
  inputs it cites from memory are now stored imports.
- synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (v2): note citing the two rung-count results; lay
  sentence changed from "three rungs are needed" to "at least three", with the later counts.
- synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height (v2): note citing the two rung-count results.

Store files: store/tombstones.yaml, one entry appended (replaced_by the design entity, date 2026-11-10, reason with
the powers-of-two scope caveat and the pointer to the Haar-moments Fact). No `merged_from` was written: the two
earlier retirements of an imported Fact in favour of a derived result (std-algebra.sylvester-inertia, the
twisted-group-algebra Fact) did not write one, and the kept entity is M2's.

## Folder to remove (orchestrator, with git)

- store/claims/synthesis.imported-haar-average-purity/ (one file, entity.md). Left in place and unedited.

## For M2

References to synthesis.imported-haar-average-purity that remain in M2's files:
- store/open_problems.yaml line 2986: `\claimref{synthesis.imported-haar-average-purity}` (in op.island-dictionary).
  It becomes E216 once the folder is removed.
- store/open_problems.yaml line 3032: the id in an `entities` list. Same.
- Plain-text historical mentions only (no edge, no claimref; no action needed unless M2 wants them reworded):
  synthesis.eviction-keeps-one-replica-saddle/entity.md (amendments defect, notes at lines 72, 89, 104),
  synthesis.eviction-keeps-one-of-catalan-many-replica-saddles/entity.md (lines 31, 73),
  synthesis.finite-normaliser-averages-.../entity.md (note, line 53),
  synthesis.quarter-turn-rotors-.../entity.md (note, line 51).
  At my last run the uses edges, premise() calls and claimrefs in the finite-averages and design entities were
  already gone.

Other items for M2:
- Pin the Epstein-Glaser Fact at `@2` in the curved-field kernel entity (it still read `@1` at my last look) and
  cite its clause (vi) for (SD1)-(SD4).
- The mode-split entity pins synthesis.eviction-deficit-against-page-deficit@4, now at 5, a restatement of clause
  (i). Its fate-table sentence ("(i) with the bounds of (vii) ... the lower bound (m-1)/(2n) lost at m = 2 only")
  describes version 4 against the sector; write "at version 4" as was done for the two eviction results, or say
  that version 5 carries the sector column. The two eviction entities also pin `@4`; they use only delta_ev and
  the half nat at the crossing, both unchanged.
- synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt pins the capacity entity `@1`
  (now 2) and the attachment entity `@3` (now 4). Both now state the K1 reading and the xi = 0 reading themselves,
  so its sentence that the capacity result "treats alpha = 5 - 4 n_g/3 as admissible" (if present) is out of date.
- The protraction identity is **not stored** as a result under any name. Nearest text: the proof of
  synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared (v4), clause (iii), which names "the first
  Bianchi identity, partial_a wedge W(a wedge b) = 0" as one of the conditions defining the ten-dimensional space of
  Weyl maps and checks it on samples (check_gtg_frame_legs_and_weyl_space), and a note of
  pairing.loop-classes-are-weyl-components (the maps on bivectors obeying it form a 20-dimensional space). Neither
  derives it from vanishing torsion, and the GTG object (obj.synthesis.gtg-flat-spacetime-gauge-fields) does not
  state it. It stays a hypothesis of the kernel entity; nothing to cite.
- op.island-dictionary and op.qft-structural-inputs can cite the bumped entities for: the sector deficit bounds
  (eviction-deficit v5 (i)), the K1 reading (capacity v2 (iv)), the scope of the cancellation (attachment v4).

## Dependants whose content may be affected (beyond pins)

- By eviction-deficit v5 (restatement of (i)): the mode-split entity's fate table (above). No pre-existing
  dependant: its only users are the three entities of this run.
- By the Haar-moments Fact v3: none in content (the formula is unchanged; the n = 2 value was already implied).
  Pinned at `@2` by the Catalan eviction entity and the mode-split entity (M2), at `@3` already by the other two.
- By the capacity entity v2 and the attachment entity v4: the no-single-curvature entity (M2, above). Pre-existing
  dependants of the attachment entity (synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off,
  synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content,
  synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike)
  use clauses (i) to (v), which are unchanged; pins only.
- By the Epstein-Glaser Fact v2: none in content (clauses (i) to (v) unchanged). Stale pins `@1` in
  synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number
  and in the one-loop vacuum-polarisation result (both mine, left for the repin), and in the kernel entity (M2).

## Not done, and why

- No pins moved in pre-existing dependants (the capacity entity's pin to the attachment entity, the two `@1` pins
  to the Epstein-Glaser Fact): left to `tp repin`, which I was told not to run. Layers 1-3 raise nothing on them.
- No `assumes` edge to the Krein premise on the capacity entity: the task asked for the statement, not the edge,
  and the premise is already in its cone. If "holds given" should show it directly, that is one line.
- The Krein-quartet result (clause (iv)) and the series-content result still present the gauge parameter and the
  doublets' curvature coupling as free; neither was in my list and neither is contradicted (they state B as a
  function of both), but under decisions 7 and 10 a note on each would be consistent with what the capacity and
  attachment entities now say.
- The local-covariance Fact is the weakest import of the pass: the sources prove it for a scalar field, and its use
  for the Dirac current, and the transcription "mass rescaled inversely", are flagged in its note and formal text
  as the less well sourced part. Nothing in either new Fact was checked against a source.
- Lay level of synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height left as it was ("at least three
  in seven dimensions" is true, and weaker than the new bound of four); only its note was added.
