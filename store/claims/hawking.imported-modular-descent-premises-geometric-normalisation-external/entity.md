---
id: hawking.imported-modular-descent-premises-geometric-normalisation-external
kind: claim
version: 1
title: 'Imported: modular descent and its geometric normalisation (external)'
status: imported
region: hawking
subject: descent
tags: [classical-theorem, modular-theory]
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
imported_from:
- citation: J. J. Bisognano and E. H. Wichmann, On the duality condition for quantum fields, J. Math.
    Phys. 17 (1976), 303--321.
  key: BisognanoWichmann1976
- citation: 'G. L. Sewell, Quantum fields on manifolds: PCT and gravitationally induced thermal states,
    Ann. Phys. 141 (1982), 201--224.'
  key: Sewell1982
- citation: W. Israel, Thermo-field dynamics of black holes, Phys. Lett. A 57 (1976), 107--110.
  key: Israel1976
locators:
  paper: T07
  number: Fact 2.2
  label: ''
  line: 408
extraction:
  env: fact
  context_refs:
  - hawking.modular-structure-completed-pair
  - singularity.descended-form-state-independent
  - singularity.euclidean-section-period
  - singularity.matching-steps-4b-4c-join-equation
  - singularity.modular-descent
  - singularity.rate-discharge-hypothesis-iii
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic
  flags:
  - external ingredients of hawking.imported-modular-descent-premises-geometric-normalisation
  - 'statement names postulates: singularity.p-univalence, singularity.r-regularity-fixed-locus'
  typing:
    by: ai-typing-pass
    note: external ingredients only (Bisognano-Wichmann, Sewell, Israel); levels written, nothing else
      changed.
---

## formal
The results from outside the series on which \claimref{hawking.imported-modular-descent-premises-geometric-normalisation} draws, as cited there: J. J. Bisognano and E. H. Wichmann, On the duality condition for quantum fields, J. Math. Phys. 17 (1976), 303--321; G. L. Sewell, Quantum fields on manifolds: PCT and gravitationally induced thermal states, Ann. Phys. 141 (1982), 201--224; W. Israel, Thermo-field dynamics of black holes, Phys. Lett. A 57 (1976), 107--110.

## technical
The external ingredients are the Bisognano-Wichmann theorem, that the modular flow of the vacuum on a wedge algebra is the boost; Sewell's extension of this to black-hole spacetimes, which yields states thermal with respect to the horizon's Killing flow; and Israel's thermofield-double reading of the eternal black hole. The series' statement on modular descent and its geometric normalisation draws on them for the mechanism.

## lay
Three classic results stand behind this entry: in flat space the vacuum seen from one wedge looks thermal with respect to boosts, the same mechanism applies near a black-hole horizon, and the eternal black hole can be read as two entangled copies, each of which looks thermal on its own.

## one-liner
The wedge-modular theorem of Bisognano and Wichmann, Sewell's black-hole reading of it, and Israel's thermofield reading of the eternal black hole.
