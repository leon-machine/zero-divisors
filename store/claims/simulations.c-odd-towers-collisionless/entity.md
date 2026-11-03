---
id: simulations.c-odd-towers-collisionless
kind: claim
version: 2
title: 'C: the odd towers collisionless'
status: postulate
region: simulations
subject: dark-matter
tags:
- halos-and-clusters
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
locators:
  paper: T14b
  number: Premise 2.12
  label: prem:C
  line: 150
extraction:
  env: premise
  context_refs:
  - simulations.confinement-scale-does-not-matter
  typing:
    by: ai-typing-pass
    note: Postulate; no edges. The confinement-scale corollary supplies the quoted numbers but is not
      a premise of a premise.
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - simulations.confinement-scale-does-not-matter (motivated_by)
    added_dependants:
    - simulations.merger
    - simulations.halo-shapes
    added_about: []
    verdict: connected
    note: The merger and cluster-assembly observations hold for reading (C) under this premise; lineage
      to the confinement corollary that supplies its phase-shift numbers.
lineage:
  motivated_by:
  - simulations.confinement-scale-does-not-matter
---

## formal
The matter of the four odd towers (the two three-dimensional and the two five-dimensional towers) has no self-interaction of order one. For the three-dimensional towers this means an in-sheet s-wave phase shift below about $2 \times 10^{-7}$ at cluster speeds for isotropic compression, $4 \times 10^{-6}$ for compression normal to the sheets (Corollary \claimref{simulations.confinement-scale-does-not-matter}).

## technical
The premise is that the matter of the four odd towers, the two three-dimensional and the two five-dimensional towers, has no self-interaction of order one. For the three-dimensional towers this is quantified as an in-sheet s-wave phase shift below about $2 \times 10^{-7}$ at cluster speeds for isotropic compression, and below $4 \times 10^{-6}$ for compression normal to the sheets, the values given by the confinement-scale corollary.

## lay
The simulations assume that dark matter in the four odd towers passes through itself without significant collisions. For the towers that live on sheets this is made precise as a very weak scattering strength at the speeds typical of galaxy clusters. It is stated as a premise of the simulations, not derived.

## one-liner
Premise: the odd towers' matter has no self-interaction of order one, which for the three-dimensional towers means an in-sheet s-wave phase shift below about $2 \times 10^{-7}$ (isotropic) or $4 \times 10^{-6}$ (normal compression) at cluster speeds.
