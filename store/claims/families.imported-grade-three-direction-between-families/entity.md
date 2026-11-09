---
id: families.imported-grade-three-direction-between-families
kind: claim
version: 7
title: 'Imported: the grade-three direction between families, and the registered route'
status: proved
region: families
subject: generations
tags: [flavour-and-mixing, representation-theory, confronted-with-data]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.imported-decomposition-grade-dictionary@1
  - standard-model.fits-record-level@6
  - standard-model.grade-three-georgi-jarlskog-direction@5
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_grade_three_couplings_ratio_three
- kind: check
  ref: check.py::check_antisymmetric_family_coupling_between_families
- kind: proof
  derivation: main
locators:
  paper: T13
  number: Fact 8.6
  label: fact:gradethree
  line: 943
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the one-sided weightings are pure grade three with antisymmetric forms on the stated pairs, ratio 3, and an antisymmetric family matrix gives a symmetric form only between families (the fits are record level, not recomputed). Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 6 -> 7.'
  env: fact
  context_refs:
  - families.imported-decomposition-grade-dictionary
  - standard-model.fits-record-level
  - standard-model.grade-three-georgi-jarlskog-direction
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - families.imported-decomposition-grade-dictionary
    - standard-model.hyp-s-slot-statistics
    note: 'Added the grade dictionary, by which the grade-three forms are placed in the 120; the record-level
      fits edge is a real premise of the registered-route sentence and was kept, so the remaining E204
      traces to a premise outside this group. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay and one-liner now name
      Hypothesis (S), and the lay says the fits are record level.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The one-sided weightings $w_{4}(B - L)$ and $v_{4}(B - L)$ are pure grade three, so their forms lie in the $120$ component of $16 \otimes 16$ (Fact \claimref{families.imported-decomposition-grade-dictionary}); they couple exactly $(L, e^{c})$ and $(Q, d^{c})$, respectively $(L, \nu^{c})$ and $(Q, u^{c})$, with lepton-to-quark modulus ratio $3$; and with a family matrix antisymmetric in the family indices, as a $120$ couples, the combined form is symmetric and vanishes on the family diagonal, so the direction contributes only to entries between different families. Fitting the charged-fermion and neutrino data at its intermediate scale with complex couplings, the Standard-Model paper finds that a second family's factor $3$ supplied by $T_{\mathrm{GJ}}$ acting on that family leaves the light neutrino masses to a cancellation tuned to about one part in $50$ to several thousand, while the factor coming through mixing with the third family, carried by this direction and the $10$s, needs none; the series registers the second as its route, as a choice, with the coupling between the two families not derived. \emph{Provenance:} \cite[Prop.~11.6, Obs.~11.7, Rem.~11.8]{ButlerT12}, the first proved there on the module under Hypothesis (S), the fits at record level.

## technical
The one-sided weightings $w_{4}(B - L)$ and $v_{4}(B - L)$ are pure grade three, so by the grade dictionary their forms lie in the $120$ of $16 \otimes 16$. They couple exactly $(L, e^{c})$ and $(Q, d^{c})$, respectively $(L, \nu^{c})$ and $(Q, u^{c})$, with lepton-to-quark modulus ratio $3$; combined with a family matrix antisymmetric in the family indices the form is symmetric and vanishes on the family diagonal, so it fills only entries between different families.

The Standard-Model paper's fits at its intermediate scale find that supplying the second family's factor $3$ by $T_{\mathrm{GJ}}$ acting on that family leaves the light neutrino masses to a cancellation tuned to between about one part in $50$ and one in several thousand, while supplying it through mixing with the third family, carried by this direction and the $10$s, needs no tuning. The series registers the second as its route, as a choice, with the coupling between the two families not derived. The module statement is proved under Hypothesis (S); the fits stand at record level.

## lay
Assuming the slots behave like the pairs (Hypothesis (S)), a simpler relative of the factor-of-three operator cannot give mass to a single family, but it can connect two different families. Fits to the measured masses of quarks, charged leptons and neutrinos, carried out earlier in the series and standing at record level rather than as derivations, find that getting the factor of three this way avoids a finely tuned cancellation that the other way needs. The series adopts this route as a choice, noting that the strength of the connection between the families is not yet derived.

## one-liner
Under Hypothesis (S), the grade-three one-sided weightings lie in the $120$ and contribute only between different families, and the series registers as its choice the route through third-family mixing, which the record-level fits find needs no tuning.
