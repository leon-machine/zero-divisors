---
id: lepton.imported-twistor-state-pair-system-excitations
kind: claim
version: 4
title: "Imported: a conformal spinor is a state of its pair system, and its excitations are the Dirac module"
status: proved
region: lepton
subject: conformal-spacetime
tags: [conformal-spinors, ladder-pairs, spinor-modules, two-readings]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-lepton, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - correspondence.fock-model-complexified-ascended-algebra@7
  - correspondence.twistors-are-states-three-ladder-pairs@6
  - standard-model.imported-pair-systems-two-chirality-halves@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_fock_module_irreducible_with_two_halves
- kind: check
  ref: check.py::check_each_conformal_spinor_is_a_fock_vacuum
- kind: check
  ref: check.py::check_excitations_from_a_dual_complement_span_the_module
locators:
  paper: T12-lepton
  number: Fact 1.2
  label: fact:pairs
  line: 184
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Statement corrected to its source''s form (complement dual to W_u, not to W: for u the Fock vacuum of W the old map has rank 1); also own exact check added: Fock model of Cl(2,4)_C irreducible with halves of dimension four, each sample conformal spinor the vacuum of its three-dimensional isotropic annihilator, and its excitations from a dual complement of W_u spanning the module. Version 3 -> 4.'
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.twistors-are-states-three-ladder-pairs
  - standard-model.imported-pair-systems-two-chirality-halves
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: Fact restating series results; the three uses are exactly the cited sources (Fock model, twistors-as-states,
      and the standard-model restatement), all kept.
  source_title: "Imported: a twistor is a state of its pair system, and its excitations are the Dirac module"
  source_formal: |-
    Let $W$ be a maximal isotropic subspace of the complexified ambient space $V_{\C}$ of the completion $\Cl(2,4)$. The complexified ascended algebra acts irreducibly on the eight-dimensional Dirac module $\Sp := \Lambda^{\bullet}W$, whose chirality halves are $\T = \Lambda^{\mathrm{even}}W$ and $\T' = \Lambda^{\mathrm{odd}}W$. Every nonzero twistor $u \in \T$ is the Fock vacuum of the three fermionic ladder pairs built on its annihilator space $W_{u}$, and for any maximal isotropic complement $U'$ dual to $W_u$ the map $\Lambda^{\bullet}U' \to \Sp$, $\xi \mapsto c(\xi)u$, is a linear isomorphism: every state of the module is generated from $u$ by its own pair operators, the even products landing in $\T$ and the odd ones in $\T'$. Twistors are states of the pair algebra, not its operators. \emph{Provenance:} \cite[Thms.~3.1, 5.3]{ButlerT9}; \cite[Fact~2.2]{ButlerT12}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistors to conformal spinors (\\CS, \\CSm) in all levels and in the restating proof; the Dirac module $\\Sp$ and the complexified Fock model are kept as in the source."
---

## formal
Let $W$ be a maximal isotropic subspace of the complexified ambient space $V_{\C}$ of the completion $\Cl(2,4)$. The complexified ascended algebra acts irreducibly on the eight-dimensional Dirac module $\Sp := \Lambda^{\bullet}W$, whose chirality halves are $\CS = \Lambda^{\mathrm{even}}W$ and $\CSm = \Lambda^{\mathrm{odd}}W$. Every nonzero conformal spinor (twistor) $u \in \CS$ is the Fock vacuum of the three fermionic ladder pairs built on its annihilator space $W_{u}$, and for any maximal isotropic complement $U'$ dual to $W_u$ the map $\Lambda^{\bullet}U' \to \Sp$, $\xi \mapsto c(\xi)u$, is a linear isomorphism: every state of the module is generated from $u$ by its own pair operators, the even products landing in $\CS$ and the odd ones in $\CSm$. Conformal spinors are states of the pair algebra, not its operators. \emph{Provenance:} \cite[Thms.~3.1, 5.3]{ButlerT9}; \cite[Fact~2.2]{ButlerT12}.

## technical
Let $W$ be a maximal isotropic subspace of $V_\C$ for the completion $\Cl(2,4)$. The complexified ascended algebra acts irreducibly on the eight-dimensional Dirac module $\Sp = \Lambda^\bullet W$, whose chirality halves are $\CS = \Lambda^{\mathrm{even}}W$ and $\CSm = \Lambda^{\mathrm{odd}}W$.

Each nonzero conformal spinor $u \in \CS$ is the Fock vacuum of the three ladder pairs built on its annihilator $W_u$, and for any maximal isotropic complement $U'$ dual to $W_u$ the map $\xi \mapsto c(\xi)u$ is a linear isomorphism $\Lambda^\bullet U' \to \Sp$, even products landing in $\CS$ and odd ones in $\CSm$. This restates earlier results of the series for use in the lepton setting.

## lay
This restates earlier results of the series. A four-component spinor of the conformal algebra is the empty state of its own small system of fermionic ladder operators, and applying those operators to it produces every state of the eight-dimensional Dirac module. These spinors are therefore states, not operators.

## one-liner
Imported from the series: each nonzero conformal spinor is the Fock vacuum of its own three ladder pairs, and its excitations span the whole eight-dimensional Dirac module.
