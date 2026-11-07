---
id: one-relation.imported-single-mode-thermality-modular-period
kind: claim
version: 6
title: 'Imported: the single-mode thermality and the modular period'
status: proved
region: one-relation
subject: thermality
tags: [needs-continuum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
derivations:
- name: main
  uses:
  - scrambling.clock-inventory-boundary-modes@6
  - sheaf.one-sided-completion-singularity@4
  - singularity.imported-descent-one-way-conditional-expectation@7
  - singularity.modular-descent@7
  - transport.door-one-way@5
  - transport.pinching-kernel@3
  - singularity.why-calibration-cannot-be-internal@6
  assumes:
  - singularity.p-univalence@2
  - singularity.r-regularity-fixed-locus@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_single_mode_thermality
- kind: check
  ref: check.py::check_clock_period_is_eight_pi_m
- kind: check
  ref: check.py::check_descent_is_a_one_way_conditional_expectation
locators:
  paper: T16
  number: Fact 2.4
  label: fact:thermality
  line: 517
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: single-mode KMS uniqueness for the ladder pair, the clock period 8 pi M, and the pinching as a conditional expectation killing the ladder sector. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  env: fact
  context_refs:
  - scrambling.clock-inventory-boundary-modes
  - sheaf.one-sided-completion-singularity
  - singularity.imported-descent-one-way-conditional-expectation
  - singularity.modular-descent
  - transport.door-one-way
  - transport.pinching-kernel
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - singularity.p-univalence
    - singularity.r-regularity-fixed-locus
    note: 'Kept all six restated sources, which match the provenance line; added (P) and (R) as assumes because
      the restated thermality holds only under them, a judgement call since the Fact names them in words rather
      than by reference. Levels pass: lay now names premises (P) and (R) and says the modular period needs neither.'
  source_formal: Thermality at the Hawking temperature is a single-mode theorem, the mode being the ladder pair
    of the ascent, one per point of the singular boundary; its exactness holds under the singularity paper's declared
    premises (P) and (R), and the value of $T_{H}$ follows from (R). The entropy paper's clock inventory of the
    singularity's boundary modes gives the modular period $\beta = 8\pi M$ unconditionally. The descent is a one-way
    conditional expectation. \emph{Provenance:} \cite[Thm.~7.3, Rem.~7.33]{ButlerT5}, the ladder pair per point
    being \cite[Thm.~8.12]{ButlerT4}; \cite[Lem.~4.2]{ButlerT8}; \cite[Prop.~7.5, Thm.~7.6]{ButlerT1} via \cite[Fact~5.9]{ButlerT5}.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 9
    note: T16's Fact said the clock inventory gives the modular period 'unconditionally', beside 'the value of T_H
      follows from (R)'; T05 proves the state's modular period equals 8 pi M only under (R) and that nothing at
      the singular boundary supplies (R). The clock period is now distinguished from the modular period, which holds
      under (R) (already assumed); T05 Prop 7.25 is cited.
  flow_note: 'both: the clocks are the rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2) via T08''s clock
    inventory; the period beta = 8 pi M is that of the phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07
    Def 2.7), the Euclidean rotation of T05 Prop 7.21, converted at the horizon rate.'
---

## formal
Thermality at the Hawking temperature is a single-mode theorem, the mode being the ladder pair of the ascent, one per point of the singular boundary; its exactness holds under the singularity paper's declared premises (P) and (R), and the value of $T_{H}$ follows from (R). The entropy paper's clock inventory of the singularity's boundary modes gives their clocks the period $\beta = 8\pi M$, the flow's Euclidean period converted at the horizon rate; that it is the state's modular period is premise (R) again, which no statement at the singular boundary can supply. The descent is a one-way conditional expectation. \emph{Provenance:} \cite[Thm.~7.3, Rem.~7.33]{ButlerT5}, the ladder pair per point being \cite[Thm.~8.12]{ButlerT4}; \cite[Lem.~4.2]{ButlerT8}; \cite[Prop.~7.5, Thm.~7.6]{ButlerT1} via \cite[Fact~5.9]{ButlerT5}.

## technical
Restated from the series: thermality at the Hawking temperature is a single-mode theorem, the mode being the ladder pair of the ascent, one at each point of the singular boundary. Its exactness holds under the singularity paper's premises (P) and (R), and the value of $\TH$ follows from (R).

Separately, the clock inventory of the singularity's boundary modes gives the clocks the period $\beta = 8\pi M$, the Euclidean period of the flow at the horizon rate; that this is the state's modular period is again premise (R), which nothing at the singular boundary supplies. The descent from the completed algebra is a one-way conditional expectation.

## lay
Earlier papers in the series show that the black hole's thermal glow can be traced to one quantum mode at a time, one pair of mode operators per point of the singular boundary. That result is exact given two stated premises of the singularity paper, univalence (P) and regularity (R), and the second of them fixes the actual temperature. A separate count of the boundary modes' clocks gives the matching period, though it is the regularity premise (R) again that makes it the period of the state itself, and the step back down from the enlarged algebra can only be taken one way.

## one-liner
Under premises (P) and (R), thermality at $\TH$ is a single-mode theorem for the ladder pair at each point of the singular boundary; the modular period is $\beta = 8\pi M$, and the descent is a one-way conditional expectation.
