---
id: simulations.imported-cluster-shapes
kind: claim
version: 1
title: 'Imported: cluster shapes'
status: imported
region: simulations
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
  source: authorship disclosure of T14b, deposited version
review: typed
imported_from:
- citation: M. Oguri, M. Takada, N. Okabe and G. P. Smith, Direct measurement of dark matter halo ellipticity
    from two-dimensional lensing shear maps of 25 massive clusters, Mon. Not. R. Astron. Soc. 405 (2010)
    2215.
  key: Oguri2010
locators:
  paper: T14b
  number: Fact 2.5
  label: fact:oguri
  line: 118
extraction:
  typing:
    by: ai-typing-pass
    note: Imported observational fact; levels only, no edges to review.
  env: fact
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants: []
    added_about: []
    verdict: standalone
    note: Observational import used only as comparison data (lineage from the halo shapes); no proof uses
      it and no definition bears on it.
---

## formal
The mean projected ellipticity $\langle 1 - b/a\rangle$ of massive clusters from weak-lensing shear maps is $0.46 \pm 0.04$, in agreement with cold dark matter \cite{Oguri2010}.

## technical
Weak-lensing shear maps of massive clusters measure the projected shape of their mass distribution directly. The mean projected ellipticity is $\langle 1 - b/a\rangle = 0.46 \pm 0.04$, with $b/a$ the projected axis ratio, in agreement with cold dark matter.

## lay
Massive galaxy clusters are not round: their mass is noticeably elongated, as measured from the way they distort the images of background galaxies. The average elongation matches what standard cold dark matter predicts. This gives a shape test that any alternative form of dark matter has to pass.

## one-liner
Weak lensing gives massive clusters a mean projected ellipticity of $0.46 \pm 0.04$, in agreement with cold dark matter.
