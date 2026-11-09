---
id: rungs.imported-results-t12-used-registration
kind: claim
version: 5
title: 'Imported: results of T12 used in the registration'
status: proved
region: rungs
subject: standard-model
tags: [hypercharge-and-anomalies, running-and-unification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.majorana-element@7
  - standard-model.mass-bracket-charged-singlet@4
  - standard-model.spectrum-run@6
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.weak-angle-over-derived-generation@5
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_mass_bracket_slot_factor
- kind: check
  ref: check.py::check_hypercharge_unique_and_family
- kind: check
  ref: check.py::check_weak_angle_and_desert
- kind: check
  ref: check.py::check_abelian_generators_twisted_and_untwisted
locators:
  paper: T12-rungs
  number: Fact 1.8
  label: fact:downstream
  line: 229
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the mass-bracket slot factor (1,1)_1, unique hypercharges and the Y + t(B - L) family, the trace ratios 3/8 and 9/26, the desert miss, and the untwisted and twisted abelian anomaly sums with U(1)_X. Version 4 -> 5.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal level and proof have no twistor language; only the lay level''s two-twistor composite was reworded.'
  source_title: |-
    Imported: results of T12 used in the registration
  source_formal: |-
    The slot factor of the mass bracket transforms as $(1,1)_{1}$, unconditionally, and under (S) the state at $(2,0)$ is that same one-dimensional representation $\Lambda^{2}\C^{2}$. Given the content, with the fourth singlet at hypercharge zero or absent, the hypercharge assignment satisfying the anomaly conditions is unique; with a fourth singlet of free hypercharge a one-parameter family $Y + t(B - L)$ appears. Over the derived generation, which contains the lepton doublet, the trace ratio is $\sin^{2}\theta_{W} = 3/8$ (over the quark doublet and the singlets alone it is $9/26$), and the one-loop run with the measured couplings and the observed spectrum does not meet: the desert is dead and the running between the scales must change, through partner-like content or an intermediate symmetry. Under (S), in the untwisted action every abelian generator in the span of the two mode numbers except hypercharge fails three of the four anomaly conditions over the derived generation; in the action the state space carries, twisted by $\det^{-1/2}$, every abelian generator is anomaly-free, and the thirteenth generator of the five-mode ledger's automorphism algebra is the $U(1)_{X}$ of $\mathrm{Spin}(10)$, broken with the Pati-Salam algebra at the intermediate scale by the Majorana term of $\nu^{c}$, which leaves the determinant-one part of $U(2) \times U(3)$ as the gauge group below that scale. \emph{Provenance:} \cite[Prop.~3.2, Prop.~5.8(1), (3), Thm.~5.5(3), Props.~6.1, 6.2, 10.7]{ButlerT12}.
  env: fact
  context_refs:
  - standard-model.hypercharge-global-form-pair-counting-consistency
  - standard-model.majorana-element
  - standard-model.mass-bracket-charged-singlet
  - standard-model.spectrum-run
  - standard-model.under-s-composites-state-space-spinor
  - standard-model.weak-angle-over-derived-generation
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Kept all six edges, which match the provenance list one for one; the fact restates them. Hypothesis
      pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S). Levels pass: the lay level now keeps the content condition (fourth singlet at hypercharge zero
      or absent) on the uniqueness of hypercharge and names (S).'
    added:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The slot factor of the mass bracket transforms as $(1,1)_{1}$, unconditionally, and under (S) the state at $(2,0)$ is that same one-dimensional representation $\Lambda^{2}\C^{2}$. Given the content, with the fourth singlet at hypercharge zero or absent, the hypercharge assignment satisfying the anomaly conditions is unique; with a fourth singlet of free hypercharge a one-parameter family $Y + t(B - L)$ appears. Over the derived generation, which contains the lepton doublet, the trace ratio is $\sin^{2}\theta_{W} = 3/8$ (over the quark doublet and the singlets alone it is $9/26$), and the one-loop run with the measured couplings and the observed spectrum does not meet: the desert is dead and the running between the scales must change, through partner-like content or an intermediate symmetry. Under (S), in the untwisted action every abelian generator in the span of the two mode numbers except hypercharge fails three of the four anomaly conditions over the derived generation; in the action the state space carries, twisted by $\det^{-1/2}$, every abelian generator is anomaly-free, and the thirteenth generator of the five-mode ledger's automorphism algebra is the $U(1)_{X}$ of $\mathrm{Spin}(10)$, broken with the Pati-Salam algebra at the intermediate scale by the Majorana term of $\nu^{c}$, which leaves the determinant-one part of $U(2) \times U(3)$ as the gauge group below that scale. \emph{Provenance:} \cite[Prop.~3.2, Prop.~5.8(1), (3), Thm.~5.5(3), Props.~6.1, 6.2, 10.7]{ButlerT12}.

## technical
Results imported from the Standard Model paper. The slot factor of the mass bracket transforms as $(1,1)_{1}$, and under (S) the state at $(2,0)$ is the same representation $\Lambda^{2}\C^{2}$. Given the content, with the fourth singlet at hypercharge zero or absent, the anomaly conditions fix hypercharge uniquely, while a fourth singlet of free hypercharge allows the family $Y + t(B - L)$. Over the derived generation, which contains the lepton doublet, $\sin^{2}\theta_{W} = 3/8$ (it is $9/26$ over the quark doublet and the singlets alone), and the one-loop run with the measured couplings and the observed spectrum does not meet, so the running between the scales must change.

Under (S), in the untwisted action every abelian generator in the span of the two mode numbers other than hypercharge fails three of the four anomaly conditions; in the action twisted by $\det^{-1/2}$, which the state space carries, every abelian generator is anomaly-free. The thirteenth generator is then the $U(1)_{X}$ of $\mathrm{Spin}(10)$, broken together with Pati-Salam at the intermediate scale by the Majorana term of $\nu^{c}$, which leaves the determinant-one part of $U(2) \times U(3)$ below that scale.

## lay
This entry gathers several results from the Standard Model paper that the rung note relies on. The mass of a composite of two basic spinor states carries a single unit of the abelian charge, and, given the generation's particle content with the extra neutral singlet uncharged or absent, its hypercharges are fixed by requiring that quantum anomalies cancel. The simplest running of the three force strengths does not bring them together, so something must change between the low and high scales. Under the slot-statistics hypothesis (S), an extra abelian symmetry is broken at an intermediate scale together with the neutral singlet's Majorana mass.

## one-liner
Imported: the mass bracket's slot factor is $(1,1)_{1}$, the anomaly conditions fix hypercharge given the content, the desert run fails with $\sin^{2}\theta_{W} = 3/8$ over the derived generation, and under (S) the thirteenth generator is the $U(1)_{X}$ of $\mathrm{Spin}(10)$, broken at the intermediate scale.
