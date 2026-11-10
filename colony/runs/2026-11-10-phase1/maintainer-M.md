# Maintainer pass M, run 2026-11-10-phase1 (10 November 2026)

Tasks 1 to 6 of MAINTAINER.md carried out in `store/` on branch run/2026-11-10-phase1. Nothing committed.
`maintainer_pass` key used everywhere: `maintainer_pass_2026_11_10`, `by: maintainer-2026-11-10` (the key was not
present on any entity touched). No check.py was changed.

## Validation
- `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`: 0 errors, 0 warnings (120
  information findings: I213 x118, I126, I305 "this change touches 16 entities; 42 claims and 11 documents depend on
  them and need re-confirmation"). Baseline before the pass was also 0 / 0.
- W503 (a layer-5 rule) run on its own through `tp.validate.plain_levels_keep_conditions`: 0 findings. One finding
  existed on a file of this pass (the lay level of the Kerr modulus result) and is fixed.
- After the assumes edges: runcheck and check4, one entity at a time, on the six entanglement entities. All check
  functions pass (8, 3, 4, 3, 3, 1); check4: 0 errors each, the only finding the expected I405 (the postulate is
  declared and untouched, excused in coverage.yaml).
- Not run, as instructed: the full check, layers 4 to 6 store-wide, tp repin, tp lock, tp build.

## New entity
- synthesis.premise-positivity-of-values, version 1, status postulate (new folder, entity.md only). Not a foundation
  postulate: no `foundation: true`, no `founded_on`; the text says so. `about: obj.std-algebra.clifford-algebra`;
  lineage motivated_by the base, the counter-model and the mode-split theorem. All four levels written.
  Final formal wording of the premise: "values are given by a \emph{state}, a $k$-linear
  $\omega : \Cl_{k}(p,q) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and
  $\omega(x^{\dagger}) = \omega(x)$ for all $x$", with $\dagger$ the linear extension of the inverse on blades
  ("the blade inverse: the anti-automorphism that fixes each generator of square 1 and negates each generator of
  square -1"), the three clauses named normalisation, positivity and reality, "stated relative to a split of the
  generators into those of square +1 and those of square -1. The split meant is the one that defines the modes: in
  $\Cl_{k}(\ell,\ell)$ the generators $e_{j}$, $f_{j}$ ... of the null pairs $v_{j} = \tfrac12(e_{j} + f_{j})$,
  $w_{j} = \tfrac12(e_{j} - f_{j})$". In indefinite signature another split gives another adjoint (base clause
  (vi), with the 17/4 example). Recorded: what it does (identity to Tsirelson's bound, base (i) to (iii); value 4
  without positivity, base (v) and the counter-model; F1 to F3 suffice for the identity, F4 not needed, the bound
  attained only with sqrt 2 adjoined), what it extends (the stored definition of a state, from elements to
  functionals), what it costs and leaves open (not derived, independence not shown, observables not fixed).
  The letter (P) is also the univalence premise's; the formal level and the note say so.

## Entities changed (old -> new version)
Accepted in this run, kept at version 1 (not in the lock; layers 1 to 3 accept):
- synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate 1 -> 1: assumes edge to the
  postulate @1; formal and proof cite it, label (P) kept; note names the related results by id; coverage.yaml
  untouched_premises.
- synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records 1 -> 1: same.
- synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two 1 -> 1: same.
- synthesis.signatures-in-which-commuting-observables-exceed-the-chsh-value-two 1 -> 1: same.
- synthesis.chsh-with-parity-even-observables-needs-two-modes-per-party-and-no-klein-twist 1 -> 1: same.
- synthesis.chsh-bound-needs-positivity-across-settings-and-anticommutation-holds-only-on-the-state 1 -> 1: same.
- synthesis.no-spin-independent-modulus-level-set-gives-the-area-law-exactly-on-slow-kerr 1 -> 1: note names the
  stretched-horizon result by id; lay level gains "assuming the same counting rule" (W503).
- synthesis.stretched-horizon-count-on-kerr-is-a-multiple-of-the-area-by-construction 1 -> 1: note wording only.
Existing entities (each with a maintainer_pass entry and a credit entry for the new version; see "Notes" below):
- synthesis.kerr-ring-count-misses-area-law 6 -> 7: closing sentence of item 4 corrected (closed surface between the
  horizon loci only for a < rho_c with sqrt(rho_c^2 - a^2) > r_-; for rho_c < a the locus passes through the disc);
  cites the modulus result for the small-spin end; amendments entry, kind restatement.
- singularity.c1-curvature-cutoff 4 -> 5: scope note (formal and technical): the class called forced fails on Kerr at
  both ends of the spin range; the horizon count is a hypothesis, not adopted. Premise unchanged.
- synthesis.c1-c2-forms-forced-one-number 3 -> 4: scope paragraph (formal and technical), same content.
- scrambling.mode-count 2 -> 3: scope paragraph: "accrual rate nu/T_H" is a Schwarzschild coincidence; on Kerr the
  three forms give M/s, M r_+/(2 s^2), 1 (stretched-horizon result, clause (v)).
- singularity.stretched-singularity-count 8 -> 9: scope paragraph: "keeps time with the horizon's own clock", same.
  orig-proof-main.tex kept.
- pred.boundary-mode-density 2 -> 3: a dated internal observation (the Kerr entropy neither meets nor probes the kill
  condition). Statement, kill condition and basis unchanged.
- synthesis.window-reading-array-killing-energy 1 -> 2: scope paragraph in the formal level (mean Killing energy
  only), one sentence in technical, lay and one-liner.
- note.singularity.monogamy-firewalls-small-corrections-theorem 1 -> 2: dated sentence naming the three-party
  trade-off, with its two caveats (same settings; parity-odd elements).
Other store files:
- store/open_problems.yaml: new op.positivity-of-values (area clifford-structure, kind research, difficulty
  frontier, status open; five attack items (a) to (e); placed under a new "clifford structure" heading before
  "completion"). op.kerr-ring: `why` restated, superradiance sentence qualified, "(10 November.)" paragraph, attack
  item 2 marked answered with what remains, new attack item (inner-locus factor three), two entities and a source
  clause added. op.residue-killing-weights: dated sentence, new attack item 4 (which object's entropy), source
  clause. op.island-dictionary: one dated sentence. op.qft-structural-inputs not touched.
- store/conventions.md: one clause in "Same names" (the two premises lettered (P)). Not asked for; added because
  the new postulate shares its letter with singularity.p-univalence. Remove if unwanted.

## Dependants whose content may be affected (not only pins)
- The six entanglement results now hold given the postulate; so will anything built on them. Nothing else in the
  store uses them yet.
- synthesis.kerr-ring-count-misses-area-law@6 is pinned by the modulus result and by
  synthesis.c-loc-is-a-second-placement-of-the-count. Both use items (1), (2), (4) for a >= 2 rho_c^2 only; neither
  uses the corrected sentence. Its own extraction note still calls the small-spin behaviour "argued"; the
  maintainer_pass note says it is now proved in the modulus result.
- singularity.c1-curvature-cutoff@4 (assumed by singularity.stretched-singularity-count, singularity.area-law-test,
  scrambling.no-echo-prediction-registered): premise unchanged, pins only.
- singularity.stretched-singularity-count@8 (nine dependants) and scrambling.mode-count@2 (six): Schwarzschild
  statements unchanged. Worth a reader's look: any dependant that carries the form nu/T_H off Schwarzschild.
  synthesis.cutoff-count-is-not-a-local-density-on-sds already treats the mass form on Schwarzschild-de Sitter.
- synthesis.window-reading-array-killing-energy@1 (assumed by synthesis.null-ordering-of-counted-units-is-zeta-symmetric,
  synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping,
  synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays,
  synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content): the reading is unchanged;
  the scope sentence bears on any text that reads the array as the continuum for more than mean energy. The
  recurrence results use the one-window evolution, not entropy; not re-read in full here.

## Notes and judgement calls
- Credit entries: every version bump carries a credit entry for the new version, including the scope notes and the
  prediction's observation. The brief says none for notes, but W221 fires on a bump without one, and earlier passes
  did the same.
- pred.boundary-mode-density: the observation is placed last in `observations`, out of date order, because the site
  takes the first entry as the prediction's headline; the GW250114 entry stays first. Move it up if the Kerr note
  should lead.
- Kerr ring sentence: the store now says the locus is a closed surface between the horizon loci "only if" the
  corrected condition holds, and that it is spacelike in the regime the modulus result proves (a <= 4 rho_c/5,
  M >= 8). Spacelike character on the rest of the corrected range is not asserted (not proved anywhere).
- op.positivity-of-values item (e): the stored check covers denominators up to 400; the range 1200 is quoted as "a
  separate computation".
- op.residue-killing-weights item 4: the numbers (pi/6, -0.177, -0.020, 0.798, 3/(2 pi c)) are restated from the
  bridge notes as "computed, not a stored result"; none was recomputed in this pass.
- House style in notes touched: "sibling", "same run", "referee", "the maintainer creates" removed from the eight
  new entities' extraction notes.

## Not done
- Nothing in tasks 1 to 6 is left out.
- Pins of dependants to the bumped versions were not moved (tp repin is the orchestrator's).
- Layer 4 store-wide and the mutation tests were not rerun beyond check4 on the six entities.
- R1's item C3 alternative (splitting the stored mode-split theorem) and R2's items 6 to 8 are not in the brief and
  were not touched.
