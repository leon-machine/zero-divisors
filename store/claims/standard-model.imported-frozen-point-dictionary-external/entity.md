---
id: standard-model.imported-frozen-point-dictionary-external
kind: claim
version: 2
title: 'Imported: the frozen point and the dictionary (external ingredients)'
status: imported
region: standard-model
subject: dark-energy
tags: [the-number-n]
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
imported_from:
- citation: S. Navas et al. (Particle Data Group), Review of particle physics, Phys. Rev. D 110 (2024),
    030001.
  key: PDG2024
locators:
  paper: T12
  number: Fact 2.5
  label: ''
  line: 883
extraction:
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'A5 largeness follow-up: the measured M_P/H is about 1.0e61 (1.03e61 for G = M_P^-2), not of order 1e60; technical, lay and one-liner corrected.'
  env: fact
  context_refs:
  - interior.covariant-form-vacuum-equations
  - interior.scale-tractor-leaves-cone
  - mass.de-sitter-scale-frozen-point
  - mass.mass-weight-dictionary
  - mass.weight-polynomial-two-series
  flags:
  - external ingredients of standard-model.imported-frozen-point-dictionary
  typing:
    by: ai-typing-pass
    note: External-ingredient record; levels describe only the cited measured value.
---

## formal
The results from outside the series on which \claimref{standard-model.imported-frozen-point-dictionary} draws, as cited there: S. Navas et al. (Particle Data Group), Review of particle physics, Phys. Rev. D 110 (2024), 030001..

## technical
The one outside ingredient is the measured value of the ratio $M_{P}/H$ of the Planck mass to the Hubble rate, about $1.0 \times 10^{61}$ (for $G = M_{P}^{-2}$), taken from the Particle Data Group's Review of Particle Physics. The number $N$ of the frozen-point dictionary inherits the status of that record.

## lay
The size of the large number $N$ is not computed by the framework but taken from measurement. The Planck mass and the present expansion rate of the universe come from the standard compilation of particle physics data, and their ratio is about $10^{61}$.

## one-liner
The measured value of $M_{P}/H$, about $10^{61}$, used in the frozen-point dictionary is taken from the Particle Data Group review.
