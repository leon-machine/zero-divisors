# Maintainer pass M1 after run 2026-11-09-solvable (by: maintainer-2026-11-09)

Scope: the eight stored entities of MAINTAINER.md section M1. The fifteen new synthesis entities and
store/open_problems.yaml were not touched (M2's). No check.py or coverage.yaml was changed, so runcheck/check4 were not
needed. Validation after the edits: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon`:
0 errors, 0 warnings (121 information findings: I213 subject spread, I126, I305 "22 entities touched", the last
covering both agents' edits). Not run: tp repin, lock, build, the full check. Nothing committed.

Each changed entity has a `maintainer_pass_2026_11_09` entry under `extraction` (by: maintainer-2026-11-09) and keeps
proposed_by, its earlier credit entries and every file in its folder.

## Changed
- hawking.joint-j3-s-wave-reduction 1 -> 2 (restatement, postulate kept). The channel-reduction clause is now assumed
  for spin 2 (the graviton) only. For spins 0, 1/2 and 1 the formal text cites
  synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional, which derives that clause at the
  horizon, given its classical facts. The current-boson identification and the partial-wave lift stay premise for
  every massless field, because that theorem does not derive them. All four levels rewritten. Credit entry v2.
- standard-model.slot-module-hypothesis 4 -> 5 (restatement of clause (f), postulate kept). New wording: with the
  slots Klein-twisted, the ten slot and pair Majoranas are distinct directions of one group of signed directions,
  (F2) and (F3), with the sign bit acting as -1. It cites the instance result (i) and the Klein-convention result. The
  five-mode CAR form is kept as the equivalent statement, so the Cl(10) on slots and pairs is unchanged. Reading the
  direction labels as F1's distinctions is flagged as a reading (F1 is only the index set F_2^10). The text adds that
  the clause, so read, holds on V for every fermionic slot module (Klein (v)), so its content is the choice of
  directions (instance (iv)). Technical, lay and one-liner updated; clauses (a), (b), (G) and (CPT) unchanged.
  Credit entry v5.
- synthesis.mass-ordered-dressing-cannot-spoil-koide 1 -> 2 (correction). The last sentence of (iv) said that neither
  (ii) nor (iv) treats D2 > D3 > D1. It now says that (iv) assumes only D3/Dj <= R, so it covers that class with
  R = D3/D1 wherever R mj <= m3/9, and it cites the middle-mass result for the sharp threshold. Proof and check
  unchanged. Credit entry v2.
- dark-matter.stored-asymmetry-charge-not-number 9 -> 10 (wording of the P1 parenthetical at all four levels):
  pi N^2/ln 2 counts registered units; the light rays number 2 pi N^2/(c ln 2) for c arrays per light ray (citing
  the residue result (iii)). "The common count is that of light rays" is now "of registered units, not of light rays
  or of boundary modes". Conclusions unaffected. Credit entry v10.
- dark-matter.r2-one-quantum-per-unit-ball 2 -> 3 (wording). "(2, 3 or 4)" now reads "(under P3, 2, 3 or 4)" at the
  formal level (P3 cited) and at the technical level. Credit entry v3.
- dark-matter.p3-nearest-dimension-representatives 2 -> 3 (note at the formal and technical levels). The
  lowest-causal choice at the odd residues follows from Premise U at residues 1 and 7, and is independent of the
  descent at residues 3 and 5, where the window is an input (synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free
  (ii), (iii)). The premise is unchanged. Credit entry v3.
- synthesis.lens-space-wall-rung-count-sees-the-integral-twist 5 -> 6 (wording). The lay sentence "on an indefinite
  side the simple twist class sets the price" is limited to this three-dimensional wall, adding that on lens-shaped
  walls of dimension 5 and up it fails. The technical level gets a matching sentence that cites
  synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial. The formal level, proof and check are unchanged.
  Credit entry v6.
- synthesis.rung-unit-second-free-number 3 -> 4 (note at the formal and technical levels). It cites
  synthesis.d-term-level-free-at-fixed-n: two models at equal N with different xi G (on the branch W = kappa N^2 that
  the record excludes), so xi G is not a function of N, consistent with the premise. No content change. Credit entry v4.

Deviation from the brief, for Leon: the brief says to add credit entries only for substantive changes, not for
notes. But `tp check` raises W221 on any version bump without a credit entry of its own, and the brief also says to
clear every new warning. So all eight entities got a Claude Opus 5.5 credit entry for their new version, with the
role naming the change. The entries on P3, R2, the lens-space result and the rung unit can be dropped if Leon prefers
to accept the W221s.

## Dependants whose content may be affected (not only pins)
- J3 (future cone 22). Direct assumers:
  - hawking.helicity-lift-joints-itemised@1 pin. Its Joint J3 item restates version 1 in full, including channel
    reduction for every species (photons too). It now overstates what is premise and should be restated to the
    narrowed J3.
  - synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature and
    synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet. Both use "J3 reduces each channel of a
    massless field to a two-dimensional mode" for every massless field. The statements stand, but for spins 0, 1/2
    and 1 that step now comes from the horizon-channels theorem, not J3. Either add a uses edge to it, or say that
    J3 covers spin 2 only. Leon to decide.
  - Unchanged under my reading: synthesis.array-ln2-is-zero-mode-doublet-one-tower ("oscillators become the s-wave
    photons under J3", the current-boson identification, kept) and synthesis.capacity-per-mode-independent-of-helicity
    (the grouping question, kept).
  - Discrepancy, M2's entity: the extraction note of
    synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content says that after the
    narrowing "vectors and scalars are no longer J3 currents". That matches DECISIONS.md 4 ("spin 2 only"), but not
    MAINTAINER.md M1.1, which keeps the current-boson identification for every massless field. I followed
    MAINTAINER.md, so that note now misdescribes J3 v2. The same check applies to the J3 caveats in
    synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays and
    synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping. They read integer-weight
    channels as array currents under J3, which still holds under v2. Leon should confirm which narrowing he meant.
- Slot-module hypothesis (future cone 231; direct assumers standard-model.hyp-s-slot-statistics@4 and
  synthesis.slot-module-makes-the-faces-separate-composites-and-leaves-the-generation-number-free@4).
  - hyp-s-slot-statistics clause (v) is clause (f) applied ("slot and pair operators forming one Clifford system").
    The equivalent CAR form is kept, so it should hold, but it needs re-checking against v5 (restatement): "slot
    operators" now means the Klein-twisted ones.
  - The faces result uses clauses (1) and (2) (the shape) only, so it is unaffected.
  - synthesis.spin10-clause-content-is-the-neutral-singlet-choice refers to clause (f) only historically.
- Koide dressing: synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class (uses @1; M2's). Its
  extraction note calls the old sentence a misstatement, which is now corrected; M2 or the orchestrator may want to
  reword it. Its use of (iv) holds as cited.
- Stored asymmetry: 17 direct dependants (pins @9). This is wording only; no dependant repeats the light-ray wording
  (searched).
- R2: 8 direct assumers (pins @2). This is wording only: the list was already P3's window. Under P3 nothing changes.
- P3: 4 direct assumers (pins @2). This is a note only.
- Lens-space result: the two new wall results (uses @5; M2's). The formal level is unchanged, so their uses hold.
- Rung unit: synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus (assumes @3). This is a note only.

## Not done
- Pins were not moved and nothing was repinned or locked (orchestrator).
- No assumes or uses edges were added to the J3 dependants (Leon's call, above).
- The op.helicity-per-boundary-mode and op.hypothesis-s known texts are M2's.

## Follow-on (orchestrator, after the J3 reading was confirmed)
Validation again, layers 1-3 with `--author leon`: 0 errors, 0 warnings. No check.py was changed, and no edges or
pins were changed: the J3 pins (@1) on the three dependants below are reviewed against J3 v2 and are ready for the
repin. Each entity has a `maintainer_pass_2026_11_09` entry and a credit entry for its new version (W221).
- hawking.helicity-lift-joints-itemised 5 -> 6 (restatement of its Joint J3 item to match J3 v2). The item is changed
  at the formal level and in proof-main.tex; the technical level, lay text and one-liner are changed to match. New
  wording: channel reduction is premise only for spin 2; for the photon, scalar and Dirac fields it is derived (the
  horizon-channels result is cited in the text only). The current-boson identification and the lift stay premise
  for every species. J1, J2, the check, orig-proof-main.tex and extraction.source_formal are unchanged.
- synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature 3 -> 4 and
  synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet 4 -> 5 (notes). Each gets a marked note at the
  end of the formal level and a sentence at the technical level. Their channel-reduction step is derived for spins 0,
  1/2 and 1 by the horizon-channels result, and assumed through J3 only for spin 2; the current-boson identification
  is still J3's for every field. No uses edge was added; statements, premises and checks are unchanged.
- standard-model.hyp-s-slot-statistics 9 -> 10 (note), after re-checking it against slot-module v5. Clause (v)
  holds. The wording needed a fix: the proof said "the slot and pair operators satisfy the CAR" right where the
  untwisted a_i are in play, and those commute with the pairs (Klein (ii)). The new note at the formal level and a
  parenthesis in the proof of (v) say that the five-mode system uses the Klein-twisted slot operators. The
  Pati-Salam step is unaffected: the 21 split-preserving bivectors, the grading and a1^dagger a2^dagger =
  a~1^dagger a~2^dagger are convention-free. The statement is unchanged.
- My earlier note on the M2 discrepancy is settled by the orchestrator's ruling. The extraction note of
  synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content still says that vectors
  and scalars stop being J3 currents, so it should be reworded (M2's file, not touched).
