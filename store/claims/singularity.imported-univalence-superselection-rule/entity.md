---
id: singularity.imported-univalence-superselection-rule
kind: claim
version: 2
title: 'Imported: the univalence superselection rule'
status: imported
region: singularity
subject: descent
tags: [univalence, superselection, classical-theorem]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
imported_from:
- citation: G. C. Wick, A. S. Wightman and E. P. Wigner, The intrinsic parity of elementary particles,
    Phys. Rev. 88 (1952), 101--105.
  key: WWW1952
- citation: 'O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2: Equilibrium
    States. Models in Quantum Statistical Mechanics, 2nd ed., Springer (1997).'
  key: BR2
  locator: \S 5.2
about:
- obj.singularity.grading-parity-automorphism
locators:
  paper: T05
  number: Fact 7.9
  label: fact:www
  line: 1780
extraction:
  env: fact
  context_refs:
  - singularity.p-reduced-metric-level-reading-many
  typing:
    by: ai-typing-pass
    note: external import; no edges to review
  merged_from:
  - id: state-selection.imported-univalence-superselection-rule
    version: 2
    locators:
      paper: T05-state-selection
      number: Fact 3.4
      label: fact:www
      line: 187
    about:
    - obj.state-selection.grading-parity-automorphism
    imported_from:
    - citation: G. C. Wick, A. S. Wightman and E. P. Wigner, The intrinsic parity of elementary particles, Phys. Rev.
        88 (1952), 101--105.
      key: WWW1952
    - citation: 'O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2: Equilibrium
        States. Models in Quantum Statistical Mechanics, 2nd ed., Springer (1997).'
      key: BR2
      locator: \S 5.2
    proof_files: []
    formal: 'In a theory whose field algebra is $\mathbb{Z}_2$ graded by fermion number, coherent superpositions of
      states of opposite fermion parity are not observable: the observable algebra is the even subalgebra, and physical
      states are even. \emph{Provenance:} Wick, Wightman and Wigner \cite{WWW1952}; the standard modern treatment
      of the graded structure of CAR algebras and their even subalgebras is \cite[\S 5.2]{BR2}.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Fact 3.4 (state-selection.imported-univalence-superselection-rule, retired
      to tombstones.yaml) into this entity: the same imported rule (T05 adds a scope remark). Kept this statement,
      levels and checks; the note''s entity is recorded above and its proof files are kept in this folder. References
      to the note''s id were repointed here. Extraction-only change, so the version and the dependants'' pins are
      unchanged.'
---

## formal
In a theory whose field algebra is $\mathbb{Z}_2$ graded by fermion number, coherent superpositions of states of opposite fermion parity are not observable: the observable algebra is the even subalgebra and physical states are even. \emph{Provenance:} Wick, Wightman and Wigner \cite{WWW1952}; the graded structure of CAR algebras and their even subalgebras is \cite[\S 5.2]{BR2}. What the rule superselects is the total parity, a single $\mathbb{Z}_2$; the mode-wise strengthening that the multi-mode descent of Step 5 needs is Proposition \claimref{singularity.p-reduced-metric-level-reading-many}, stated there, and is not part of this import.

## technical
In a theory whose field algebra is $\Z_2$ graded by fermion number, coherent superpositions of states of opposite fermion parity are not observable: the observable algebra is the even subalgebra and physical states are even (Wick, Wightman and Wigner, with the graded structure of CAR algebras and their even subalgebras from the standard literature). The rule superselects only the total parity, a single $\Z_2$; the mode-wise strengthening that the multi-mode descent needs is a separate statement and not part of this import.

## lay
A classic rule of quantum theory says that one can never observe a superposition of a state with an even number of fermions and one with an odd number. So the observable quantities are those unchanged by flipping fermion parity, and physical states respect this. The rule concerns the total count of fermions only, not each mode separately.

## one-liner
Imported: in a theory graded by fermion number, superpositions across total fermion parity are unobservable, so observables and physical states are even; the rule concerns total parity only.
