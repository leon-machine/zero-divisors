---
id: pairing.imported-stabiliser-tangent
kind: claim
version: 4
title: 'Imported: the stabiliser and the tangent'
status: proved
region: pairing
subject: one-relation
tags: [pairing-and-bogoliubov, rotors-and-stabilisers, witt-index]
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
  - pairing.imported-stabiliser-tangent-external@1
  - singularity.envelope-endpoint-why-boundary-mode-locality@7
  - singularity.l-stabiliser-tangent@6
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_quadratic_operators_span_the_bivectors
- kind: check
  ref: check.py::check_action_on_the_vacuum
- kind: check
  ref: check.py::check_stabiliser_and_tangent_dimensions
- kind: check
  ref: check.py::check_hop_rotation_fixes_and_pairing_rotation_moves_the_vacuum
locators:
  paper: T05-pairing
  number: Fact 1.1
  label: fact:stabtangent
  line: 184
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on the Fock space of 2, 3, 4 modes, hops, Cartan elements, pair annihilations and creations span so(2 nu), the vacuum stabiliser has dimension nu^2 + nu(nu-1)/2 and the tangent nu(nu-1)/2, a hop rotation fixes |0> and the pairing rotation gives 3/5|0> + 4/5|12>. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: fact
  context_refs:
  - one-relation.imported-cartans-purity-theorem-thouless-form
  - singularity.envelope-endpoint-why-boundary-mode-locality
  - singularity.l-stabiliser-tangent
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Fact restating series results; all four edges kept as its stated provenance (T05 singularity
      results, Cartan-Thouless Fact and external ingredients). Levels pass: the lay now keeps the two-or-more-modes
      condition and says the tangent statement is first order.'
---

## formal
On the Fock space of $\nu \geq 2$ boundary modes the bivectors of $\so(2\nu)$ split as hops $a_i^{\dagger}a_j$ (with the Cartan elements $a_i^{\dagger}a_i - \tfrac12$), pair annihilations $a_ia_j$ and pair creations $a_i^{\dagger}a_j^{\dagger}$. On the vacuum every hop with $i \neq j$ and every annihilation vanishes and every Cartan element is a scalar, so hops and annihilations are the stabiliser of the vacuum ray; the creations span the tangent of the orbit of Witt vacua, of dimension $\nu(\nu-1)/2$. A hop rotation fixes the vacuum, a pairing rotation moves it, and the necessity witness of the singularity paper's envelope corollary, $\ket{00} \mapsto \tfrac35\ket{00} + \tfrac45\ket{11}$, is the pairing rotation on one pair at $(\cos\theta, \sin\theta) = (\tfrac35, \tfrac45)$. \emph{Provenance:} \cite[Prop.~13.4, Cor.~11.6]{ButlerT5}; the orbit is the spinor variety of \cite{Cartan1938, Chevalley1954}, imported there, and the exponential form of a rotated vacuum is Thouless's \cite{Thouless1960}, imported by the laboratory paper \cite[Fact~2.10]{ButlerT16}.

## technical
On the Fock space of $\nu \geq 2$ boundary modes the bivectors of $\so(2\nu)$ split into hops $a_i^{\dagger}a_j$ (with the Cartan elements $a_i^{\dagger}a_i - \tfrac12$), pair annihilations $a_ia_j$ and pair creations $a_i^{\dagger}a_j^{\dagger}$. Hops with $i \neq j$ and annihilations kill the vacuum and Cartan elements act as scalars, so these form the stabiliser of the vacuum ray, while the creations span the tangent to the orbit of Witt vacua, of dimension $\nu(\nu-1)/2$.

A hop rotation fixes the vacuum and a pairing rotation moves it; the witness $\ket{00} \mapsto \tfrac35\ket{00} + \tfrac45\ket{11}$ is the pairing rotation on one pair. The fact restates series results; the orbit is the classical spinor variety and a rotated vacuum has the Thouless exponential form.

## lay
In a system of two or more fermion modes, the basic symmetry operations come in three kinds: moving a particle from one mode to another, removing a pair, and creating a pair. On the empty state the first two leave its direction unchanged, while creating pairs genuinely moves it. So, to first order, the ways the vacuum can be changed are exactly the pair creations.

## one-liner
On the Fock space of $\nu \geq 2$ modes, hops and pair annihilations stabilise the vacuum ray while pair creations span the $\nu(\nu-1)/2$-dimensional tangent to the orbit of Witt vacua.
