---
id: rungs.imported-fock-representation-bogoliubov-group
kind: claim
version: 4
title: 'Imported: the Fock representation and its Bogoliubov group'
status: proved
region: rungs
subject: one-relation
tags: [spinor-modules, pairing-and-bogoliubov, car-algebra]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - rungs.imported-fock-representation-bogoliubov-group-external@2
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_rungs.py
  tags:
  - label:fact:fock
- kind: check
  ref: check.py::check_car_and_irreducible_spinor_module
- kind: check
  ref: check.py::check_parity_grading_is_chirality
- kind: check
  ref: check.py::check_orthogonal_group_preserves_car_and_pin_implements_it
- kind: check
  ref: check.py::check_unitary_group_is_number_preserving_part
locators:
  paper: T12-rungs
  number: Fact 1.6
  label: fact:fock
  line: 221
extraction:
  env: fact
  context_refs:
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: Fact restating the series' imported Fock fact; both edges kept as its provenance.
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for n <= 3 modes the CAR, irreducibility (monomials of rank 4^n), parity as chirality, O(2n) preserving the CAR with Pin and Spin implementers, and Lambda(g) for g in U(n). Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
---

## formal
For a complex Hermitian space $E$ of dimension $n$, the Fock space $\Lambda^{\bullet}E$ is the irreducible spinor module of the complex Clifford algebra on $2n$ generators, its parity grading the chirality decomposition; the orthogonal transformations of the $2n$ Majorana generators preserving the canonical anticommutation relations form the compact $O(2n)$, implemented by $\mathrm{Pin}(2n)$, with $SO(2n)$ implemented by $\mathrm{Spin}(2n)$; those preserving the complex structure form $U(n)$, acting as $\Lambda^{\bullet}(g)$ up to a determinant phase. \emph{Provenance:} \cite[Fact~2.11]{ButlerT12}; \cite[Lecture~20]{FultonHarris1991}; \cite[Ch.~I, \S\S 2, 5]{LawsonMichelsohn1989}.

## technical
For a complex Hermitian space $E$ of dimension $n$, the Fock space $\Lambda^{\bullet}E$ is the irreducible spinor module of the complex Clifford algebra on $2n$ generators, its parity grading being the chirality decomposition. The orthogonal transformations of the $2n$ Majorana generators, which preserve the canonical anticommutation relations, form $O(2n)$, implemented by $\mathrm{Pin}(2n)$, with $SO(2n)$ implemented by $\mathrm{Spin}(2n)$; those preserving the complex structure form $U(n)$, acting as $\Lambda^{\bullet}(g)$ up to a determinant phase.

The fact restates the series' imported Fock-representation fact together with its classical sources.

## lay
The states of n fermion modes can be described by the exterior algebra of an n-dimensional complex space, and this is exactly the spinor representation of a Clifford algebra with 2n generators. The symmetries that keep the particle rules intact form a rotation group, and those that also keep the particle number fixed form a unitary group.

## one-liner
The Fock space $\Lambda^{\bullet}E$ of $n$ modes is the irreducible spinor module of the complex Clifford algebra on $2n$ generators, with Bogoliubov group $O(2n)$ implemented by $\mathrm{Pin}(2n)$ and number-preserving subgroup $U(n)$.
