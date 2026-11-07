---
id: hawking.imported-s-wave-bosonic-sector
kind: claim
version: 6
title: 'Imported: the s-wave bosonic sector'
status: proved
region: hawking
subject: thermality
tags: [bosonisation, boundary-modes, radiation-spectrum]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
derivations:
- name: main
  uses:
  - hawking.imported-s-wave-bosonic-sector-external@1
  - singularity.bosonisation-bridge-s-wave-sector@8
  - hawking.kms-restricts-invariant-subalgebras@3
  assumes:
  - singularity.q-joint-quasi-freeness-s-wave@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_edge_identity_on_the_window
- kind: check
  ref: check.py::check_bilinear_subalgebra_invariant_under_boost
- kind: check
  ref: check.py::check_restriction_to_currents_is_kms
- kind: check
  ref: check.py::check_bose_einstein_occupancy_of_the_currents
locators:
  paper: T07
  number: Fact 2.4
  label: fact:boson
  line: 416
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the edge identity, boost invariance of the bilinears, KMS of the restriction to currents, and the Bose-Einstein occupancy with Wick and window sums. Version 4 -> 5. check_bilinear_subalgebra_invariant_under_boost: loop over all 128 window states (was every fifth) (fix round 2026-10-23). Version 5 -> 6.'
  env: fact
  context_refs:
  - hawking.current-commutator-exactly-edge-split
  - hawking.kms-restricts-invariant-subalgebras
  - singularity.bosonisation-bridge-s-wave-sector
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Kept the source theorem, the external companion and Premise (Q); the KMS-restriction lemma
      (the statement calls this an instance of it) and the edge-split proposition (a later reproof) appear
      below the fact and were not added as premises. Levels pass: conditions already kept.'
---

## formal
Two halves, at two levels. \emph{Unconditional:} on a window of the boundary mode space, the number-conserving bilinears (currents) satisfy the free-boson commutation relations exactly in the completed limit, with an exact finite-window operator identity whose deviation is a difference of edge operators; and the bilinear subalgebra is globally invariant under the modular boost. \emph{Conditional on T5's Premise (Q), joint quasi-freeness with the s-wave weights:} the restriction of the Fermi-Dirac KMS state to the bilinear subalgebra is KMS at the same temperature (an instance of Lemma \claimref{hawking.kms-restricts-invariant-subalgebras} below), giving the Bose-Einstein occupancy at $\TH$ for the s-wave sector; the linear weight assignment is the s-wave reduction's convention, adopted there as part of the premise. \emph{Provenance:} T5 \cite[Prem.~8.1, Thm.~8.2]{ButlerT5}; the correspondence itself is classical \cite{FrenkelKac1980}. The exact edge identity is reproved, in the form this paper needs, as Proposition \claimref{hawking.current-commutator-exactly-edge-split} below.

## technical
Unconditionally, on a window of the boundary mode space the number-conserving bilinears (currents) satisfy the free-boson commutation relations exactly in the completed limit, the finite-window deviation being an exact difference of edge operators, and the bilinear subalgebra is globally invariant under the modular boost.

Conditionally on Premise (Q), joint quasi-freeness with linear s-wave weights, the restriction of the Fermi-Dirac KMS state to the bilinear subalgebra is KMS at the same temperature, which gives Bose-Einstein occupancy at $\TH$ for the s-wave sector. The boson-fermion correspondence behind this is classical.

## lay
This imports an earlier result of the series: pairs of fermion-like boundary modes behave exactly like bosons, up to precisely identified edge effects on any finite window. If the boundary modes are assumed to be jointly in the simplest kind of thermal state, these pairs are thermal at the Hawking temperature and follow the Bose-Einstein occupation law, for the spherically symmetric (s-wave) sector.

## one-liner
Boundary-mode currents satisfy the free-boson relations exactly up to an edge term, and under Premise (Q) they carry Bose-Einstein occupancy at $\TH$ in the s-wave sector.
