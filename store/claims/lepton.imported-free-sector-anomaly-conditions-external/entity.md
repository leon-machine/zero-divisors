---
id: lepton.imported-free-sector-anomaly-conditions-external
kind: claim
version: 2
title: 'Imported: the free sector and the anomaly conditions (external ingredients)'
status: imported
region: lepton
subject: standard-model
tags: [classical-theorem, hypercharge-and-anomalies]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate reference key merged at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
review: typed
imported_from:
- citation: 'S. Weinberg, The Quantum Theory of Fields, Vol. 2: Modern Applications, Cambridge University
    Press (1996).'
  key: WeinbergQFT2
  locator: \S 22.4
locators:
  paper: T12-lepton
  number: Fact 1.5
  label: ''
  line: 196
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Decision item D12 (routine): the reference key WeinbergQFT1 (a duplicate of WeinbergQFT2, both Weinberg QFT Vol. 2, 1996) is merged into WeinbergQFT2.'
  typing:
    by: ai-typing-pass
    note: External-ingredient entry with no derivation; nothing to edge.
  env: fact
  context_refs:
  - standard-model.imported-anomaly-coefficients
  - standard-model.quarks-leptons-two-level-fermion-content
  flags:
  - external ingredients of lepton.imported-free-sector-anomaly-conditions
---

## formal
The results from outside the series on which \claimref{lepton.imported-free-sector-anomaly-conditions} draws, as cited there: S. Weinberg, The Quantum Theory of Fields, Vol. 2: Modern Applications, Cambridge University Press (1996)., \S 22.4.

## technical
This entry stands for the textbook ingredient behind the free-sector and anomaly fact: the treatment of gauge anomalies for chiral fermions in Weinberg's The Quantum Theory of Fields, volume 2, section 22.4, the source of the anomaly-cancellation conditions for fermions listed in one handedness. It is imported from the literature, not proved in the series.

## lay
The conditions that keep a gauge theory free of quantum anomalies are standard textbook physics. This entry records that the lepton note takes them from Weinberg's quantum field theory text, naming the section used.

## one-liner
The textbook treatment of gauge anomalies in Weinberg's The Quantum Theory of Fields, section 22.4, on which the free-sector and anomaly fact draws.
