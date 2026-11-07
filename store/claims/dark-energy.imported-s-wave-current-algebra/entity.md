---
id: dark-energy.imported-s-wave-current-algebra
kind: claim
version: 5
title: 'Imported: the s-wave current algebra'
status: proved
region: dark-energy
subject: thermality
tags: [bosonisation, boundary-modes, modular-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-energy.imported-s-wave-current-algebra-external@1
  - singularity.bosonisation-bridge-s-wave-sector@8
  - hawking.current-commutator-exactly-edge-split@4
  assumes:
  - singularity.q-joint-quasi-freeness-s-wave@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_current_algebra_with_edge_split
- kind: check
  ref: check.py::check_currents_are_weight_vectors_of_the_boost
- kind: check
  ref: check.py::check_quasi_free_state_restricts_to_kms_on_currents
- kind: check
  ref: check.py::check_charge_zero_levels_are_bosonic_fock_space
locators:
  paper: T10
  number: Fact 2.3
  label: fact:current
  line: 648
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Label: the weights omega_k = kappa k with the sea at k = 0 stated here are the source paper''s convention, version 2 of premise (Q); version 3 of (Q) adopts kappa(k + 1/2), and only the n_0 = 1/2 line of this statement depends on the offset. Version 4 -> 5.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the edge-split current algebra on a 7-mode window, currents as boost weight vectors, KMS of the quasi-free restriction with a non-(Q) control, and the charge-zero levels as bosonic Fock space. Version 3 -> 4.'
  env: fact
  outside_pilot_cites:
  - ButlerT7
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - singularity.bosonisation-bridge-s-wave-sector
    - hawking.current-commutator-exactly-edge-split
    note: 'Restating fact whose series sources were outside the pilot at extraction: added the singularity
      paper''s bosonisation theorem (current algebra, modular invariance, KMS under (Q)) and the Hawking
      paper''s exact edge identity (the finite-window quantification), both now in the store. Levels pass:
      the lay now names premise (Q).'
---

## formal
On the window of the boundary mode space the number-conserving bilinears satisfy the free-boson current algebra exactly in the completed limit (with the finite-window deviation an explicit difference of edge operators), and the current sector is modular-invariant. Under the singularity paper's premise (Q) (\cite[Premise~8.1]{ButlerT5}: the joint state of the mode array is the gauge-invariant quasi-free state with the marginals its premises (P) and (R) fix, with the linear s-wave weights $\omega_k = \kappa k$ and the sea level at $k = 0$), the induced state is KMS, thermal at $\TH$-analogue temperature, for the joint modular flow; without (Q) only the marginals are thermal. The charge-zero sector is canonically the bosonic Fock space, an assembly-level identification the singularity paper bases on the boson-fermion correspondence \cite{PressleySegal1986}. \emph{Provenance:} \cite[\S 8, Premise~8.1]{ButlerT5}; the finite-window quantification \cite[\S 6]{ButlerT7}.

## technical
On a window of the boundary mode space, the number-conserving bilinears of the fermion modes satisfy the free-boson current algebra exactly in the completed limit, and on a finite window the deviation is an explicit difference of edge operators. The current sector is invariant under the modular flow.

Under premise (Q), which takes the joint state of the mode array to be the gauge-invariant quasi-free state with the marginals fixed by (P) and (R), with linear s-wave weights $\omega_{k} = \kappa k$ and sea level at $k = 0$, the induced state on the currents is KMS for the joint modular flow at the $\TH$-analogue temperature; without (Q) only the marginals are thermal. The charge-zero sector is identified with the bosonic Fock space at assembly level, through the boson-fermion correspondence.

## lay
Pairs of fermion operators on the horizon modes behave exactly like a free boson field, with precisely identified corrections at the edges of any finite set of modes. If one further assumes that the modes are jointly in the simplest thermal state (premise (Q)), the boson field is thermal at the Hawking-type temperature; without that assumption only the individual modes are known to be thermal. This entry imports these results from earlier in the series.

## one-liner
The boundary modes' number-conserving bilinears form an exact free-boson current algebra up to explicit edge terms, and under premise (Q) the induced current state is KMS at the $\TH$-analogue temperature.
