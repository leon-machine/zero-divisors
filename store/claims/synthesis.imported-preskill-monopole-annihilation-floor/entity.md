---
id: synthesis.imported-preskill-monopole-annihilation-floor
kind: claim
version: 1
title: 'Imported: monopole-antimonopole annihilation in the hot plasma acts only above a monopole-to-entropy ratio of about 10^-10 and reduces it no further (Preskill 1979)'
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
- citation: 'J. P. Preskill, Cosmological production of superheavy magnetic monopoles, Phys. Rev. Lett. 43 (1979), 1365--1368.'
  key: Preskill1979
  doi: 10.1103/PhysRevLett.43.1365
extraction:
  note: >-
    Imported as input (c) of synthesis.pati-salam-monopoles-bound-descent-history, which cites it
    from memory as a floor of about 10^-10 (M_M/10^14 GeV). Checked on 2026-10-26 against the statement of
    Preskill's result in arXiv:2509.23726 (Appendix A, footnote 9: annihilation is significant only if
    n_M/s is above about 10^-10, and then reduces the ratio to about 10^-10). The dependence on the monopole
    mass, and the mass at which the floor is normalised, are cited from memory and not checked; the
    Pati-Salam result uses only that the floor exceeds 10^-12 for M_M > 10^12 GeV, which holds for a
    floor of 10^-10 at grand-unified masses falling at most linearly with the mass.
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Created by the maintainer pass (fix round of 26 October: monopole input (c), cited from memory by the Pati-Salam monopole result, to be imported as a Fact).'
---

## formal
In a radiation-dominated plasma, monopoles and antimonopoles annihilate by diffusing towards one another through the charged particles of the bath and capturing into bound states. The annihilation rate per monopole is proportional to $n_{M}$ and falls faster than the expansion rate once $n_{M}/s$ is below a value of order $10^{-10}$ (for grand-unified monopole masses; Preskill's estimate grows with the monopole mass, a dependence cited here from memory). So annihilation reduces an initial $n_{M}/s$ above that value to about that value, and does not change one below it. \emph{Provenance:} \cite{Preskill1979}.

## technical
Monopoles and antimonopoles left by a transition can find each other and annihilate, but only while they are dense: the rate of encounters drops with the density, and below a monopole-to-entropy ratio of order $10^{-10}$ for grand-unified masses it is slower than the expansion. So annihilation can cure an overabundance only down to that value, which is still far above what observation allows; it cannot lower an abundance that starts below it.

## lay
Magnetic poles and their opposites can destroy each other, but only while they are crowded together. Preskill showed that this stops long before their number is small enough to agree with observation.

## one-liner
Monopole-antimonopole annihilation acts only above $n_{M}/s \sim 10^{-10}$ (for grand-unified masses) and reduces the ratio to about that value, no further (Preskill 1979).
