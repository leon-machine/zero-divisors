# Maintainer pass M, run 2026-11-09-three (9 November 2026, second pass)

Tasks 1 to 6 of MAINTAINER.md carried out in `store/`. Nothing committed, pushed, repinned, locked or built.
No check.py was changed, so runcheck and check4 were not needed and were not run.

Validation: `tp check --store store --layers 1,2,3 --keep-going --author leon`: 0 errors, 0 warnings, 120
information findings (118 I213 and I126 as in the baseline; I305 now reads "this change touches 12 entities; 18
claims and 5 documents depend on them and need re-confirmation"). Baseline before the pass: 0 errors, 0 warnings.
`store/open_problems.yaml` parses (35 problems, was 32).

## Entities changed (old -> new version)

New:
- synthesis.imported-atiyah-hirzebruch-filtration-of-complex-k-theory: new, version 1, status imported, subject
  walls. Clauses (i) filtration, (ii) spectral sequence with torsion differentials, (iii) line bundles, (iv) the
  form the lens-space proof uses (a consequence of (ii), argument in the technical level). Provenance
  Atiyah-Hirzebruch 1961 and Atiyah, K-Theory (1967), flagged as cited from memory and NOT checked against the
  sources (bibliographic data included). No keys were added to store/references.yaml (as for Witten1982).

Version raised (each with a credit entry for Claude Fable 5.2 and a `maintainer_pass_2026_11_09b` entry):
- hawking.joint-j3-s-wave-reduction: 2 -> 3. Restatement. Channel-reduction clause premise for even-parity spin 2
  only (odd parity cited as derived, given its stated hypotheses, in the spin-2 result); "s-wave reduction" reworded
  to "each partial-wave channel, l >= |s|" at every level and in the title (now "Joint J3: the partial-wave
  reduction (modelling)"; the id stays; "the s-wave theory", the name of the two-dimensional theory, is kept);
  new sentence that the identification is not one array tower per helicity channel, citing the capacity result.
- hawking.helicity-lift-joints-itemised: 6 -> 7. Joint J3 item restated to J3 version 3 at all four levels and in
  proof-main.tex; orig-proof-main.tex kept; coverage.yaml wording.
- synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature: 4 -> 5. The formal and
  technical "Note (the channel-reduction step)" now says derived for spins 0, 1/2, 1 and odd-parity spin 2,
  assumed through J3 (version 3) for even-parity spin 2 only; "the s-wave reduction of the postulate J3" reworded
  to "the partial-wave reduction of the postulate J3" (levels, proof, note).
- synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet: 5 -> 6. Same two changes;
  orig-proof-main.tex kept.
- synthesis.array-ln2-is-zero-mode-doublet-one-tower: 5 -> 6. Wording only at the formal and technical levels:
  J3 identifies the current boson with "the partial-wave channels" of a field (was "the s-wave"; "s-wave photons").
  Formal text is hashed as substantive, so the version had to go up. Clause (iv) unchanged.
- synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional: 1 -> 2. Task 4: scope
  sentence in clause (4) (static, Killing, frame and its null coordinates; in Kruskal-type null coordinates the
  scalar and Maxwell coupling at the horizon is -4M^2 C(2M) v(2M), nonzero, C(2M) = 1/e for the usual tortoise
  coordinate), a derivation paragraph in the proof (direct substitution, not in the check), one sentence each at
  the technical and lay levels, the one-liner; reference to J3 aligned with version 3.
- synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial: 1 -> 2. Restatement. New uses edge to the
  cohomology result @1. (L1) (cohomology rings, stable tangent bundle) is its clauses (3), (5); (L3) (K-ring, one
  remark) is its clause (6), given the imported filtration. Remains conditional on (L2), the spin class q1
  (with p1 = e^2 and the orientable/spin criteria), cited from memory. Labels (L1) to (L3) kept.
- synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height: 1 -> 2. Restatement. New uses edge to the
  cohomology result @1. (L2) (K-ring) is its clause (6), a stored theorem given the new Fact; (L3) (Sq^1) is
  dropped, x^2 = 0 being its clause (3); a sentence added to the proof that any orthogonal complex structure is
  conjugate to the quarter turn, so the cited theorem applies to the walls built here. Remains conditional on
  (L1), the lambda-operations, which clause (1) uses.

Kept at version 1 (accepted today, not yet in the lock; layers 1 to 3 accept it):
- synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure: uses edge to the new
  Fact @1; clause (6) now reads "(AH) is the imported Fact ..." with the label (AH) kept; proof cites it;
  coverage.yaml gains an untouched_premises entry; extraction note updated. The lambda-operations, q1 and the
  background (G) stay in-statement hypotheses.
- synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free: the "intended citation ... sibling"
  sentence replaced by a plain cross-reference to the spin-2 result; the sentences on J3 in the formal setting, the
  Reading, the technical level and proof (iii) follow J3 version 3 (premise for even-parity spin 2; J3 states the
  identification is not one tower per channel, so the inequality is a reading, not a consequence). Clauses (i) to
  (v) and the check unchanged.
- synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional: extraction note only (id
  kept, rename B4 not applied; J3 version 3 recorded; the generation result named).
- synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content: extraction note only
  (one sentence on J3 version 3); version 1 kept.

The three coverage.yaml files of the lens entities gained `untouched_premises` entries for the new premises (the
checks compute in the presented rings and do not call them), so that the evidence layer does not raise W405.

## store/open_problems.yaml
- op.wall-class-invariant: "(9 November, second pass.)" paragraph in known; attack item 1 restated; item 4
  restated to what remains (q1, lambda-operations; cellular background a stated hypothesis); new item 5 (rung count
  on a definite side as an equivariant, Borsuk-Ulam, index; first computation the primary obstruction in twisted
  integral H^3 of L^5(4)); success clause sharpened as decision 7 words it; entities and source extended.
- op.helicity-per-boundary-mode: second-pass paragraph (odd parity derived, even one way, one superpotential,
  horizon values, J3 version 3, Killing-frame scope); item 1 restated; entities and source extended.
- op.qft-structural-inputs: second-pass paragraph (both leads closed negatively; independence argued, 2 of 24
  postulates audited; J3 not injective); item 1 keeps a premise or dynamics fixing n_g, or a two-model proof over
  the full joint cone; entities and source extended.
- New, status open, kind research: op.curvature-coupling-across-subjects (area quantum-fields, placed after
  op.qft-structural-inputs), op.order-four-anomaly-and-sixteen (area standard-model, placed after op.rung-unit),
  op.dark-tower-running (area dark-matter, placed last in that area). Every entity id was checked to exist.

## Dependants whose CONTENT may be affected (not only pins)
- synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping (version 1, not changed):
  clause (i) and proof say J3 "with (Q) version 3, puts one array in each helicity channel" and "partitions the
  arrays into channels". J3 version 3 now says the identification is not one array tower per helicity channel.
  The result's conclusion (no premise fixes the grouping) is not weakened, but that sentence should be re-read
  against J3 version 3. For Leon.
- synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays and
  synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content: they use only J3's
  reading "integer-weight channels are currents of the arrays, adding no array", which version 3 keeps and now
  states more strongly; no change needed. The first one's proof lists J3 at @1 in its audit of the cone.
- synthesis.n-plus-null-ground-state (postulate, version 12) and synthesis.hadamard-deposit-premise: formal text
  names "the s-wave reduction J3" / "the s-wave reduction of its modes". Name only; see "Not done".
- synthesis.null-ordering-of-counted-units-is-zeta-symmetric: pins the null-shell collapse result @4; the statement
  it uses is unchanged (only the note on the channel step moved).
- Pins left for the repin (statements re-read here, pins not touched, as in this morning's pass):
  J3@2 in hawking.helicity-lift-joints-itemised and both collapse results; helicity-lift@6 in
  scrambling.imported-collars-coframe-exceptional-set-helicity, synthesis.array-ln2-is-zero-mode-doublet-one-tower,
  synthesis.attachment-conformal-energy-is-generated-by-z and the capacity result; array-ln2@5 in the capacity
  result; the lower-spin horizon result @1 in the spin-2 result. J3 and the lower-spin result are restatements
  (formal changed), so by the rules their dependants are re-checked before repinning: the five that quote J3 were
  re-read and reworded here; the spin-2 result uses only clause (4)'s f = C e^{2 kappa r_*}, which is unchanged.

## Not done, and why
- lens K-theory result, check.py docstring (line 7) still says "(L2) of the statement, cited from memory". Not
  edited: a change to check.py would need the evidence layer rerun; the coverage.yaml wording was updated instead.
- The (K2) and (K3) literature paragraphs remain in that result's proof, marked there as not used.
- "the s-wave reduction J3" as a NAME is left in: synthesis.n-plus-null-ground-state (formal; a core postulate,
  version 12, with a large cone: a bump for a name was judged disproportionate), synthesis.hadamard-deposit-premise
  (formal), op.derive-loc-and-r-loc (known, line 166, which mirrors the N+ wording), store/tags.yaml (two tag
  descriptions) and two notes. For Leon whether to sweep them.
- No `amendments` entries were written (not required of the maintainer; J3 version 2 has none either).
- The two-rung and K-theory results cite the cohomology result only; the new Fact reaches them through it (no
  direct uses edge).
- Referee's B4 (rename the spin-2 id): not applied, as instructed.
- The Killing-frame sentence is not machine-checked; for the Dirac channel only the static-frame statement is made
  (the Kruskal-coordinate coupling is computed for the scalar and Maxwell channels only).
- Three numbers in op.curvature-coupling-across-subjects (B about -65 to -66 at the tilt window; the zero of B
  between seven and eight generations) are my arithmetic on stored formulas, labelled there as not a stored result
  and conditional on the tilt's scalar being the doublets.
- The new Fact's clause (iv) is my derivation from (ii), from memory like the rest; nothing was checked online.
