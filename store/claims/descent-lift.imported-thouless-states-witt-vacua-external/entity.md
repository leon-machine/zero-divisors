---
id: descent-lift.imported-thouless-states-witt-vacua-external
kind: claim
version: 1
title: 'Imported: Thouless states and Witt vacua (external ingredients)'
status: imported
region: descent-lift
subject: descent
tags: [classical-theorem, pairing-and-bogoliubov]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
review: typed
imported_from:
- citation: D. J. Thouless, Stability conditions and nuclear rotations in the Hartree-Fock theory, Nucl.
    Phys. 21 (1960) 225--232.
  key: Thouless1960
locators:
  paper: T05-descent-lift
  number: Fact 1.5
  label: ''
  line: 167
extraction:
  env: fact
  context_refs:
  - one-relation.imported-cartans-purity-theorem-thouless-form
  flags:
  - external ingredients of descent-lift.imported-thouless-states-witt-vacua
  typing:
    by: ai-typing-pass
    note: external ingredient only (Thouless 1960); levels written, nothing else changed.
---

## formal
The results from outside the series on which \claimref{descent-lift.imported-thouless-states-witt-vacua} draws, as cited there: D. J. Thouless, Stability conditions and nuclear rotations in the Hartree-Fock theory, Nucl. Phys. 21 (1960) 225--232..

## technical
The external ingredient is Thouless's theorem from Hartree-Fock theory: an exponential of pair creation operators $\exp(\sum_{i<j}A_{ij}a^{\dagger}_{i}a^{\dagger}_{j})$ applied to a vacuum gives the vacuum of a Bogoliubov-rotated mode decomposition. The series' statement on Thouless states and Witt vacua draws on it, alongside Cartan's purity theorem.

## lay
In many-body physics, Thouless showed that adding pairs of particles to an empty state in a controlled exponential way gives the empty state of a different, rotated set of modes. That theorem is the outside ingredient here.

## one-liner
Thouless's theorem: exponentials of pair creators applied to a vacuum are the vacua of Bogoliubov-rotated mode decompositions.
