---
id: pairing.imported-stabiliser-tangent-external
kind: claim
version: 2
title: 'Imported: the stabiliser and the tangent (external ingredients)'
status: imported
region: pairing
subject: one-relation
tags: [classical-theorem, spinor-modules, pairing-and-bogoliubov]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-pairing, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: 'consistency pass, citation typography in the formal level'
  version: 2
  source: maintainer pass 2026-11-07 (consistency)
review: typed
imported_from:
- citation: '''E. Cartan, Lecons sur la th''eorie des spineurs, Hermann, Paris (1938).'
  key: Cartan1938
- citation: C. Chevalley, The Algebraic Theory of Spinors, Columbia University Press (1954).
  key: Chevalley1954
- citation: D. J. Thouless, Stability conditions and nuclear rotations in the Hartree-Fock theory, Nucl.
    Phys. 21 (1960) 225--232.
  key: Thouless1960
locators:
  paper: T05-pairing
  number: Fact 1.1
  label: ''
  line: 184
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2. The citation list in the formal level carried stray apostrophes for the accents and doubled full stops; now plain (Lecons, theorie) with single stops; no change of content.'
  env: fact
  context_refs:
  - one-relation.imported-cartans-purity-theorem-thouless-form
  - singularity.envelope-endpoint-why-boundary-mode-locality
  - singularity.l-stabiliser-tangent
  flags:
  - external ingredients of pairing.imported-stabiliser-tangent
  typing:
    by: ai-typing-pass
    note: External-ingredients record; levels only.
---

## formal
The results from outside the series on which \claimref{pairing.imported-stabiliser-tangent} draws, as cited there: E. Cartan, Lecons sur la theorie des spineurs, Hermann, Paris (1938); C. Chevalley, The Algebraic Theory of Spinors, Columbia University Press (1954); D. J. Thouless, Stability conditions and nuclear rotations in the Hartree-Fock theory, Nucl. Phys. 21 (1960) 225--232.

## technical
This entry records the sources from outside the series of the stabiliser-and-tangent fact: Cartan and Chevalley for pure spinors and the spinor variety, the single orbit of Witt vacua of dimension $\nu(\nu-1)/2$, and Thouless for the exponential form $\exp(\sum_{i<j}A_{ij}a^{\dagger}_{i}a^{\dagger}_{j})\ket{0}$ of a Bogoliubov-rotated vacuum.

## lay
Part of the stabiliser-and-tangent fact comes from classical work outside the series: the theory of pure spinors due to Cartan and Chevalley, and Thouless's formula for rotated vacuum states. This entry records those sources so that the dependence is visible.

## one-liner
External ingredients of the stabiliser-and-tangent fact: Cartan and Chevalley on pure spinors and the spinor variety, and Thouless on the exponential form of rotated vacua.
