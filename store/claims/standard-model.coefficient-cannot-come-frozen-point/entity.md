---
id: standard-model.coefficient-cannot-come-frozen-point
kind: claim
version: 4
title: The coefficient cannot come from the frozen point
status: proved
region: standard-model
subject: generations
tags: [frozen-point, no-go, flavour-and-mixing]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - standard-model.no-go-frozen-point-lifts-do@4
  - standard-model.space-symmetric-doublet-mass-forms-two@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_no_rung_count_reaches_pair_bivector
- kind: check
  ref: check.py::check_frozen_point_forms_are_the_ten
- kind: check
  ref: check.py::check_t_gj_needs_the_pair_bivector
- kind: proof
  derivation: main
locators:
  paper: T12
  number: Cor 9.34
  label: cor:coeff
  line: 1831
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: frozen point plus any number of rung vectors (2, 3, 4 rungs) never reaches the pair bivector; on the module its doublet forms are the 10 only; each blade of T_GJ carries one pair bivector. Version 3 -> 4.'
  env: corollary
  context_refs:
  - standard-model.under-s-bracket-direction-charged-not
  outside_pilot_cites:
  - ButlerT9
  typing:
    by: ai-typing-pass
    removed:
    - standard-model.bracket-composite-lands
    note: 'Removed the bracket theorem, which the proof cites only as the later answer to the closing
      reading; the bracket-direction Proposition in the context refs is likewise part of the reading,
      not a premise. Levels pass: conditions already kept.'
  source_title: 'The coefficient cannot come from the frozen point'
  source_formal: |-
    No polynomial in the frozen point and its lifts produces the $126$ doublet direction, so the Georgi-Jarlskog coefficient cannot be derived from the transported frozen point alone, however many rungs it is lifted through: the lifts add rung vectors, and rung vectors wedge to grade at most one per rung, never to the pair-sector bivector. The mass mechanism can produce the coefficient only if the pair sector enters it, through $\sum_{i}v_{i}\wedge w_{i}$, which is the $B - L$ generator and, in the twistor paper's language, the charge of the twistor storey. The weight programme's first deliverable is therefore restated more precisely once more: not ``a pair-number-dependent rung coupling'' in general, but specifically a coupling of the rung vector to the pair-sector $u(1)$ current, and the object in the series that already couples to that current is the mass bracket, whose direction Proposition \claimref{standard-model.under-s-bracket-direction-charged-not} located in $120 \oplus 126$; its charge is wrong for a vev, but its $B - L$ structure is the right kind. Whether a neutral composite of bracket and rung vector reaches $T_{\mathrm{GJ}}$ is the next computation, and it is a computation, not a decision.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'The twistor storey and its charge are now the conformal spinor storey and its charge, with the T09 name as an aside; nothing else was in twistor form.'
---

## formal
No polynomial in the frozen point and its lifts produces the $126$ doublet direction, so the Georgi-Jarlskog coefficient cannot be derived from the transported frozen point alone, however many rungs it is lifted through: the lifts add rung vectors, and rung vectors wedge to grade at most one per rung, never to the pair-sector bivector. The mass mechanism can produce the coefficient only if the pair sector enters it, through $\sum_{i}v_{i}\wedge w_{i}$, which is the $B - L$ generator and, in the correspondence paper's language, the charge of the conformal spinor storey (the twistor storey). The weight programme's first deliverable is therefore restated more precisely once more: not ``a pair-number-dependent rung coupling'' in general, but specifically a coupling of the rung vector to the pair-sector $u(1)$ current, and the object in the series that already couples to that current is the mass bracket, whose direction Proposition \claimref{standard-model.under-s-bracket-direction-charged-not} located in $120 \oplus 126$; its charge is wrong for a vev, but its $B - L$ structure is the right kind. Whether a neutral composite of bracket and rung vector reaches $T_{\mathrm{GJ}}$ is the next computation, and it is a computation, not a decision.

## technical
The frozen point and its lifts generate only rung vectors and products that never reach the pair-sector bivector, so no polynomial in them produces the $126$ doublet direction $T_{\mathrm{GJ}}$, and the Georgi-Jarlskog coefficient cannot come from the transported frozen point, however many rungs it is lifted through. Since the symmetric doublet mass forms are spanned by the $10$ direction and $T_{\mathrm{GJ}}$, the coefficient can arise only if the pair sector enters the mass mechanism through $\sum_{i} v_{i} \wedge w_{i}$, the $B - L$ generator.

The remaining sentences are a reading: what is needed is a coupling of the rung vector to the pair-sector $u(1)$ current, and the object that already couples to it is the mass bracket, whose direction lies in $120 \oplus 126$; whether a neutral composite of bracket and rung vector reaches $T_{\mathrm{GJ}}$ is posed as the next computation.

## lay
In unified theories a factor of three between certain lepton and quark masses, the Georgi-Jarlskog factor, needs a specific ingredient. This result shows that the framework's frozen point, however far it is carried up the tower, cannot supply that ingredient. Only something tied to the charge that distinguishes quarks from leptons could, and the paper names the mass bracket as the natural candidate to test next.

## one-liner
No polynomial in the frozen point and its lifts yields the $126$ doublet direction, so the Georgi-Jarlskog coefficient requires the pair-sector $B - L$ generator to enter the mass mechanism.
