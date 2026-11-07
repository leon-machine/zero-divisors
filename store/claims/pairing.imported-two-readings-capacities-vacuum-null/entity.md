---
id: pairing.imported-two-readings-capacities-vacuum-null
kind: claim
version: 3
title: 'Imported: the two readings, the capacities, and the vacuum as a null direction'
status: proved
region: pairing
subject: one-relation
tags: [two-readings, witt-index, null-directions, spinor-modules]
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
review: typed
derivations:
- name: main
  uses:
  - one-relation.imported-cartans-purity-theorem-thouless-form@1
  - one-relation.spacetime-manifold-vacuum-lines@6
  - one-relation.two-capacities-three-consequences@6
  - one-relation.two-presentations@5
  - tower.witt-index-quantum-capacity@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_witt_basis_relations_are_the_car
- kind: check
  ref: check.py::check_real_and_complex_capacities
- kind: check
  ref: check.py::check_every_weyl_spinor_pure_up_to_six
locators:
  paper: T05-pairing
  number: Fact 1.2
  label: fact:readings
  line: 188
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Witt bases give the CAR with floor(n/2) modes for n <= 6, real and complex capacities min(p,q) and floor(n/2) as maximal isotropic subspaces, and purity of every sample parity-definite state at nu = 2, 3 with a non-pure control at nu = 4. Version 2 -> 3.'
  env: fact
  context_refs:
  - one-relation.imported-cartans-purity-theorem-thouless-form
  - one-relation.spacetime-manifold-vacuum-lines
  - one-relation.two-capacities-three-consequences
  - one-relation.two-presentations
  - tower.witt-index-quantum-capacity
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Fact restating series results; all five edges kept as its stated provenance. Levels pass: conditions
      already kept.'
---

## formal
The relation $\{e_a, e_b\} = 2g_{ab}$ on a Witt basis is the canonical anticommutation relations, the Fock module being supplied by the pure-spinor construction. A real quadratic space of signature $(p,q)$ has real capacity $\min(p,q)$ and complex capacity $\lfloor (p+q)/2 \rfloor$; for $(1,3)$ these are one and two, the complex reading being the Dirac spinor as a two-mode Fock space. A vacuum at a point of spacetime is an extra datum, a null direction at the point, which the reading must supply. Every Weyl spinor of $\mathrm{Spin}(2\nu, \C)$ is pure for $2\nu \leq 6$, so at $\nu = 2$ and $\nu = 3$ every parity-definite state is the vacuum of some Witt decomposition. \emph{Provenance:} \cite[Props.~3.1, 3.2, 4.1(3), Fact~2.10]{ButlerT16}; the capacity count is \cite[Thm.~4.3]{ButlerT3}.

## technical
The Clifford relation $\{e_a, e_b\} = 2g_{ab}$ on a Witt basis is the canonical anticommutation relations, with the Fock module supplied by the pure-spinor construction. A real quadratic space of signature $(p,q)$ has real capacity $\min(p,q)$ and complex capacity $\lfloor (p+q)/2 \rfloor$, which for $(1,3)$ are one and two, the complex reading being the Dirac spinor as a two-mode Fock space.

A vacuum at a spacetime point is an extra datum, a null direction at that point, which the reading must supply. Since every Weyl spinor of $\mathrm{Spin}(2\nu, \C)$ is pure for $2\nu \leq 6$, at $\nu = 2$ and $\nu = 3$ every parity-definite state is the vacuum of some Witt decomposition.

## lay
This fact gathers earlier results. The algebra of spacetime can be read as a system of fermion modes; ordinary spacetime supports one mode by the real count and two by the complex count; and choosing an empty state at a point means choosing a light-like direction there. For small numbers of modes, every state of definite parity is such an empty state for some choice.

## one-liner
The Witt reading of the Clifford relation is the canonical anticommutation relations, signature $(p,q)$ has capacities $\min(p,q)$ and $\lfloor (p+q)/2 \rfloor$, a vacuum is a null direction, and for $\nu \leq 3$ every parity-definite state is a Witt vacuum.
