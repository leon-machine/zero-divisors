---
id: state-selection.where-fermi-dirac-comes
kind: claim
version: 5
title: Where the $+1$ of Fermi-Dirac comes from
status: proved
region: state-selection
subject: thermality
tags: [recovers-known-physics, grading-and-parity, radiation-spectrum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-state-selection, the series'' standard disclaimer'
review: typed
about:
- obj.singularity.grading-parity-automorphism
derivations:
- name: main
  uses:
  - singularity.descent-parity-average@4
  - state-selection.euclidean-partner-curvature-selected@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_euclidean_rotor_period
- kind: check
  ref: check.py::check_even_sector_periodic_odd_sector_antiperiodic
- kind: check
  ref: check.py::check_anticommutator_gives_fermi_dirac
locators:
  paper: T05-state-selection
  number: Cor 5.4
  label: cor:statistics
  line: 294
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: R_2pi = -1 with conjugation period 2 pi, even and odd sectors under the parity average, and the Fermi-Dirac versus Bose-Einstein denominators. Version 3 -> 4. check_even_sector_periodic_odd_sector_antiperiodic strengthened: factorwise R_2pi on ladder words equals the parity automorphism on every word up to length 4; one-mode ordered thermal correlator computed antiperiodic (ratio = grading sign -1). Version 4 -> 5.'
  env: corollary
  outside_pilot_cites:
  - ButlerT5
  typing:
    by: ai-typing-pass
    note: Kept both edges; the Matsubara step is quoted as the standard reading and is not in the store
      as an imported claim, so no standard route was added.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 2
    note: 'Level wording only (technical): the Euclidean-period rotor is placed on spinors, matching the
      narrowing of state-selection.euclidean-partner-curvature-selected to the action on each chiral half;
      the result already uses only R_{2 pi} = -1 in the spinor module, so formal and proof are unchanged.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: The state-selection note's duplicates of T05 entities were retired to tombstones.yaml (merged into the T05
      entities). References moved from the retired obj.state-selection.grading-parity-automorphism, state-selection.descent-parity-average
      to obj.singularity.grading-parity-automorphism, singularity.descent-parity-average; version 2 -> 3.
---

## formal
The rotor implementing one Euclidean period is $R_{2\pi} = -1$, which acts as $+1$ on the even sector $\Aev$ and as $-1$ on the odd sector $\Aod$. The ladder's own generators are odd, so their correlation functions are antiperiodic around the modular period while the metric-level observables are periodic. This is the structural origin of the Fermi-Dirac denominator $e^{\omega/T} + 1$ rather than the Bose-Einstein $e^{\omega/T} - 1$, and hence of the first wrinkle recorded in \cite[Rem.~7.5]{ButlerT5}: the statistics of the directly produced spectrum is fixed by the double cover, and the bosonic sector has to be reached by bosonisation, as Step 4e does.

## technical
The rotor implementing one Euclidean period on spinors, where the curvature-selected Euclidean rotor carries the continued boost on each chiral half, is $R_{2\pi} = -1$, which acts as $+1$ on the even sector $\Aev$ and as $-1$ on the odd sector $\Aod$. The ladder's generators are odd, so their correlation functions are antiperiodic around the modular period, while the metric-level observables, which live in the even sector, are periodic.

Read through the standard Matsubara correspondence, this antiperiodicity is the structural origin of the Fermi-Dirac denominator $e^{\omega/T} + 1$ rather than the Bose-Einstein $e^{\omega/T} - 1$: the statistics of the directly produced spectrum is fixed by the double cover, and the bosonic sector has to be reached by bosonisation.

## lay
A full turn of the Euclidean rotation leaves ordinary geometric quantities unchanged but flips the sign of fermion operators. Through a standard correspondence, quoted rather than proved here, that sign flip is why the directly produced radiation follows Fermi-Dirac rather than Bose-Einstein statistics. Reaching photon-like Bose-Einstein radiation therefore needs a separate step, bosonisation.

## one-liner
Because the Euclidean-period rotor is $R_{2\pi} = -1$, odd ladder correlators are antiperiodic and even observables periodic, which through the standard Matsubara reading is the origin of the Fermi-Dirac $+1$, leaving the bosonic sector to bosonisation.
