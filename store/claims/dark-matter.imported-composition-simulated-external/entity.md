---
id: dark-matter.imported-composition-simulated-external
kind: claim
version: 2
title: 'Imported: the composition simulated (external ingredients)'
status: imported
region: dark-matter
subject: dark-matter
tags:
- halos-and-clusters
- confronted-with-data
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 2
  source: maintainer pass 2026-11-07 (decisions)
review: typed
imported_from:
- citation: S. W. Randall, M. Markevitch, D. Clowe, A. H. Gonzalez, and M. Bradac, Constraints on the
    self-interaction cross section of dark matter from numerical simulations of the merging galaxy cluster
    1E 0657-56, Astrophys. J. 679 (2008), 1173--1180.
  key: Randall2008
- citation: D. Clowe et al., A direct empirical proof of the existence of dark matter, Astrophys. J. Lett.
    648 (2006), L109--L113.
  key: Clowe2006
locators:
  paper: T14
  number: Fact 7.32
  label: ''
  line: 1237
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. Decision item E10 (routine; no retirement): link to simulations.imported-bullet-cluster, which imports these two sources with content and is the home, recorded under extraction.overlaps_with (a citation list against a Fact, no pinned link).'
  overlaps_with:
  - id: simulations.imported-bullet-cluster
    note: 'Decision E10: this is a citation list of Randall et al. 2008 and Clowe et al. 2006, which simulations.imported-bullet-cluster imports with content; that entity is kept as the home.'
  env: fact
  context_refs:
  - simulations.confinement-scale-does-not-matter
  - simulations.effective-cross-section-sheet-matter
  - simulations.halo-shapes
  - simulations.merger
  - simulations.mirror-galaxy
  unresolved_refs:
  - rem:forms
  flags:
  - external ingredients of dark-matter.imported-composition-simulated
  typing:
    by: ai-typing-pass
    note: Imported observational ingredients; levels only.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Imported observational ingredients reached by lineage from the composition fact; no definition
      bears on it, and it repeats the Randall and Clowe citations of simulations.imported-bullet-cluster.
---

## formal
The results from outside the series on which \claimref{dark-matter.imported-composition-simulated} draws, as cited there: S. W. Randall, M. Markevitch, D. Clowe, A. H. Gonzalez, and M. Bradac, Constraints on the self-interaction cross section of dark matter from numerical simulations of the merging galaxy cluster 1E 0657-56, Astrophys. J. 679 (2008), 1173--1180.; D. Clowe et al., A direct empirical proof of the existence of dark matter, Astrophys. J. Lett. 648 (2006), L109--L113..

## technical
These are the results from outside the series that the simulated composition draws on: the numerical-simulation constraints of Randall and collaborators on the self-interaction cross-section of dark matter in the merging galaxy cluster 1E 0657-56, which supply the observed mass-to-light ratio $0.84 \pm 0.07$ the merger simulation is compared with, and the weak-lensing study of the same cluster by Clowe and collaborators, which is the observation of the merger compared.

## lay
Two published studies of a famous pair of colliding galaxy clusters supply the observations that the hidden-world simulations are checked against. One mapped where the cluster's mass sits; the other used simulations to limit how strongly dark matter can scatter off itself.

## one-liner
The external inputs to the simulated composition are the Randall et al. self-interaction constraints and the Clowe et al. lensing observation of the merging cluster 1E 0657-56.
