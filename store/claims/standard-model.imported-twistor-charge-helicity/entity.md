---
id: standard-model.imported-twistor-charge-helicity
kind: claim
version: 4
title: "Imported: the charge on the conformal spinor space is helicity"
status: proved
region: standard-model
subject: conformal-spacetime
tags: [conformal-spinors]
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
  - correspondence.shared-core-ordering-dictionary@4
  - hawking.homogeneity-ordering-shift@6
  - hawking.imported-penrose-transform@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_identity_charge_is_shifted_euler_operator
- kind: check
  ref: check.py::check_homogeneity_is_minus_two_s_minus_two
- kind: check
  ref: check.py::check_offset_is_the_ordering_shift
locators:
  paper: T12
  number: Fact 2.3
  label: fact:helicity
  line: 875
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: q(id) = -hbar (Upsilon + 2), homogeneity h = -2s - 2 on monomials of degree -6..3, and the offset as the ordering shift. Version 3 -> 4.'
  env: fact
  context_refs:
  - correspondence.shared-core-ordering-dictionary
  - hawking.homogeneity-ordering-shift
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    added:
    - hawking.imported-penrose-transform
    note: The identification with helicity is stated to be the Penrose-transform homogeneity, so the imported
      Penrose transform was added as a premise; the source does not say the whole result is obtained classically,
      so no standard-route derivation.
  source_title: "Imported: twistor charge is helicity"
  source_formal: |-
    Twistor charge, the homogeneity of the palatial quadratics, is helicity: the identification is the Penrose-transform homogeneity, whose offset is the ordering shift; the shift is proved in the twistor paper and the homogeneity $-2s-2$ is derived from it in the Hawking paper. \emph{Provenance:} \cite[Thm.~5.7]{ButlerT9}; \cite[Prop.~5.2]{ButlerT7}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor charge to the charge read on the conformal spinor space in all levels and in the restating proof; the Penrose transform keeps its name. The dictionary's further reading (helicity as the $\\pm I_4$ sector) is not added, since the source does not state it."
---

## formal
The charge read on the conformal spinor space $\CS$ (twistor charge), the homogeneity of the palatial quadratics, is helicity: the identification is the Penrose-transform homogeneity, whose offset is the ordering shift; the shift is proved in the twistor correspondence paper and the homogeneity $-2s-2$ is derived from it in the Hawking paper. \emph{Provenance:} \cite[Thm.~5.7]{ButlerT9}; \cite[Prop.~5.2]{ButlerT7}.

## technical
The charge read on the conformal spinor space, the homogeneity measured by the palatial quadratics, is helicity. The identification goes through the Penrose-transform homogeneity $-2s-2$ for helicity $s$, whose offset of $-2$ is the symmetric-ordering shift.

The ordering shift is proved in the twistor correspondence paper, and the homogeneity $-2s-2$ is derived from it in the Hawking setting; the fact quotes both.

## lay
In Penrose's description the helicity of a massless particle, its spin along its direction of motion, shows up as the way a function on the spinor space of the conformal algebra scales. This fact records that the series' own charge on that space is exactly that scaling weight, with an extra shift of two coming from operator ordering. It is quoted from earlier papers of the series.

## one-liner
Imported: the charge on the conformal spinor space is helicity, through the Penrose-transform homogeneity $-2s-2$ whose offset is the ordering shift.
