---
id: synthesis.imported-kibble-preskill-causal-monopole-estimate
kind: claim
version: 1
title: 'Imported: a broken phase formed by a causal process leaves about one defect per correlation volume, at most a Hubble volume, with probability of order one tenth per volume for monopoles (Kibble 1976, Preskill 1979)'
status: imported
region: synthesis
subject: dark-matter
tags: [symmetry-breaking, confronted-with-data, classical-theorem]
proposed_by:
  kind: ai
  session: maintainer-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
imported_from:
- citation: 'T. W. B. Kibble, Topology of cosmic domains and strings, J. Phys. A 9 (1976), 1387--1398.'
  key: Kibble1976
- citation: 'J. P. Preskill, Cosmological production of superheavy magnetic monopoles, Phys. Rev. Lett. 43 (1979), 1365--1368.'
  key: Preskill1979
  doi: 10.1103/PhysRevLett.43.1365
extraction:
  note: >-
    Imported as input (b) of synthesis.pati-salam-monopoles-bound-descent-history (the estimate
    behind its hypothesis (K)), which cites it from memory. Checked on 2026-10-26 against the Caltech
    repository record of Preskill 1979 (title, author, publication date 5 November 1979, and the abstract:
    grand-unified models contain stable superheavy monopoles, their density in the early universe is
    estimated to be unacceptably large, and production may be suppressed if the transition is strongly
    first order); the volume and pages (Phys. Rev. Lett. 43, 1365) and the DOI from memory, consistent with
    the issue listing. The probability p of about 1/10 per correlation volume and Kibble 1976 are cited
    from memory; the per-correlation-volume form with a geometric factor of order 1/10 is consistent with
    arXiv:hep-ph/0607129, Section 2.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: monopole input (b), cited from memory by the Pati-Salam monopole result, to be imported as a Fact).'
---

## formal
When a phase with topologically nontrivial vacuum manifold forms by a causal process (a thermal transition at $T_{c}$, or any formation in which the Higgs field's orientation is uncorrelated beyond a length $\xi$), the orientations in distinct correlation volumes are independent, and a defect forms at a meeting point with a probability fixed by the geometry of the vacuum manifold. Causality bounds the correlation length by the horizon distance, $\xi \lesssim H^{-1}$ at formation. For monopoles the probability is about $p \approx \tfrac{1}{10}$ per correlation volume, so the initial number density is at least about $p\,\xi^{-3} \ge p\,H^{3}$, and with entropy density $s$ the ratio $n_{M}/s$ is at least about $p\,H^{3}/s$ at formation. \emph{Provenance:} \cite{Kibble1976} (the causal mechanism); \cite{Preskill1979} (the monopole estimate).

## technical
The Kibble mechanism: regions that have not been in causal contact cannot coordinate the direction in which a symmetry breaks, so where independent regions meet, topological defects are left. For monopoles Preskill estimated about one per ten correlation volumes, and the correlation length is at most the horizon distance. So a causal transition leaves at least about $p H^{3}$ monopoles per unit volume, a lower bound that depends only on the temperature at which the broken phase forms. It is the estimate that makes the monopole problem of grand unification: in a universe that is not diluted afterwards, the predicted abundance far exceeds what is observed.

## lay
As the early universe cooled and a unified force split apart, distant regions could not agree on how to split it, and magnetic poles were left where they met. This estimate says how many: about one for every ten regions the size of the horizon, or more.

## one-liner
A causally formed broken phase leaves at least about $p\,\xi^{-3} \ge p H^{3}$ monopoles per unit volume, $p \approx 1/10$, since causality bounds the correlation length by the horizon (Kibble 1976, Preskill 1979).
