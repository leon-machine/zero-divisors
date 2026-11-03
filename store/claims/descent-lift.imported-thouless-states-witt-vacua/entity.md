---
id: descent-lift.imported-thouless-states-witt-vacua
kind: claim
version: 5
title: 'Imported: Thouless states and Witt vacua'
status: proved
region: descent-lift
subject: descent
tags: [pairing-and-bogoliubov, witt-index, classical-theorem]
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
derivations:
- name: main
  uses:
  - descent-lift.imported-thouless-states-witt-vacua-external@1
  - one-relation.imported-cartans-purity-theorem-thouless-form@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_thouless_states_are_rotated_vacua
- kind: check
  ref: check.py::check_every_even_vector_up_to_three_modes_is_pure
- kind: check
  ref: check.py::check_exponential_form_iff_vacuum_overlap
locators:
  paper: T05-descent-lift
  number: Fact 1.5
  label: fact:thouless
  line: 167
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Thouless states on 2-4 modes killed by the rotated annihilators a_i - A_ij a_j^dag with positive definite anticommutator Gram, annihilator dimension nu for even vectors of 2 and 3 modes (0 for the 4-mode control), and the exponential form iff vacuum overlap. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE L4
    open_problem: op.small-findings
    note: 'Every even state vector of at most three modes is a Witt vacuum (Cartan), but only those overlapping the reference vacuum have the Thouless form; |11> on two modes is a Witt vacuum not of that form. The restatement now says so, as its original does.'
  source_formal: 'For an antisymmetric matrix $A$ the state $\exp(\sum_{i<j}A_{ij}a^{\dagger}_{i}a^{\dagger}_{j})\ket{0}$ is the vacuum of the Witt decomposition obtained from the standard one by the corresponding Bogoliubov rotation; on two modes it is $\ket{00} + A_{12}\ket{11}$, and every even state of at most three modes is such a vacuum. \emph{Provenance:} \cite{Thouless1960}; Cartan''s theorem as imported by the laboratory paper \cite[Fact~2.10]{ButlerT16}.'
  env: fact
  context_refs:
  - one-relation.imported-cartans-purity-theorem-thouless-form
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: restates Thouless's theorem with Cartan's purity theorem as imported in the laboratory paper;
      both uses edges kept.
---

## formal
For an antisymmetric matrix $A$ the state $\exp(\sum_{i<j}A_{ij}a^{\dagger}_{i}a^{\dagger}_{j})\ket{0}$ is the vacuum of the Witt decomposition obtained from the standard one by the corresponding Bogoliubov rotation; on two modes it is $\ket{00} + A_{12}\ket{11}$, and every even state vector of at most three modes is a Witt vacuum (pure, by Cartan's theorem), of this exponential form exactly when its overlap with $\ket{0}$ is nonzero ($\ket{11}$ on two modes is a Witt vacuum not of this form). \emph{Provenance:} \cite{Thouless1960}; Cartan's theorem as imported by the laboratory paper \cite[Fact~2.10]{ButlerT16}.

## technical
For an antisymmetric matrix $A$, the Thouless state $\exp(\sum_{i<j}A_{ij}a^{\dagger}_{i}a^{\dagger}_{j})\ket{0}$ is the vacuum of the Witt decomposition obtained from the standard one by the corresponding Bogoliubov rotation.

On two modes it is $\ket{00} + A_{12}\ket{11}$, and every even state vector of at most three modes is a Witt vacuum (pure, by Cartan's theorem), of this exponential form exactly when its overlap with $\ket{0}$ is nonzero ($\ket{11}$ on two modes is a Witt vacuum not of this form).

## lay
Exponentiating pair creation operators and applying the result to the empty state produces a state that is the empty state of a rotated choice of modes. For two modes this is just a combination of empty and doubly occupied, and for up to three modes every state of even parity is the empty state of some choice of modes, arising from this formula whenever it overlaps the original empty state.

## one-liner
Thouless states $\exp(\sum_{i<j}A_{ij}a^{\dagger}_{i}a^{\dagger}_{j})\ket{0}$ are Witt vacua of Bogoliubov-rotated decompositions; every even state vector of at most three modes is a Witt vacuum, and of Thouless form when it overlaps $\ket{0}$.
