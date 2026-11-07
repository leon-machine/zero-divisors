---
id: standard-model.imported-pair-systems-two-chirality-halves
kind: claim
version: 5
title: "Imported: the pair systems and the two chirality halves"
status: proved
region: standard-model
subject: conformal-spacetime
tags: [conformal-spinors, spinor-modules, ladder-pairs, two-readings]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.fock-model-complexified-ascended-algebra@8
  - correspondence.twistors-are-states-three-ladder-pairs@6
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
  paper: T12
  number: Fact 2.2
  label: fact:pairs
  line: 871
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: Fock model irreducible with halves of dimension four, each sample conformal spinor a pure Fock vacuum, and its pair excitations spanning the module by parity. Version 4 -> 5.'
  small_findings_pass:
    by: ai-small-findings-pass
    date: 2026-10-22
    finding: STRUCTURE M11
    open_problem: op.small-findings
    note: 'Names which chirality is meant: the halves here are the Cl(2,4) (Spin(2,4) Weyl) chirality, the parity of the Fock grade, each four-dimensional; they are not the spacetime chiral halves at a point (Som, Spi of conventions.md and T09 Thm 4.2(iv)), which are two-dimensional and split CS. Level wording only.'
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.twistors-are-states-three-ladder-pairs
  - tower.fock-module-one-qubit-per-rung
  - tower.witt-index-quantum-capacity
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    removed:
    - tower.fock-module-one-qubit-per-rung
    - tower.witt-index-quantum-capacity
    note: The tower results are cited only for the iterated pair structure within which the statement
      sits, not for any clause of it, so they were removed; the two twistor results carry the whole statement.
  source_title: "Imported: the pair systems and the two chirality halves"
  source_formal: |-
    Let $W$ be a maximal isotropic (three-dimensional) subspace of $V_{\C}$ with a dual isotropic complement. The complexified ascended algebra acts irreducibly on $\Lambda^{\bullet}W$, and its two chirality halves are $\T = \Lambda^{\mathrm{even}}W$ and $\T' = \Lambda^{\mathrm{odd}}W$, each of dimension four. Every nonzero twistor $u \in \T$ is a pure spinor: it is the Fock vacuum of the system of three fermionic ladder pairs built on its own annihilator space $W_{u}$, every state of the module is generated from $u$ by those pair operators, and $\T$ (respectively $\T'$) is what the even (respectively odd) products generate. Twistors are states of the pair algebra, not its operators. \emph{Provenance:} \cite[Thm.~3.1]{ButlerT9} for the Fock model and the chirality halves; \cite[Thm.~5.3]{ButlerT9} for the pure-spinor and Fock-vacuum statements; the tower paper \cite[Thms.~4.2, 4.3]{ButlerT3} for the iterated pair structure (one qubit per rung, Witt index as capacity) within which this sits.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistors to conformal spinors (\\CS, \\CSm) in all levels and the restating proof; the complexified Fock model is kept as in the source."
---

## formal
Let $W$ be a maximal isotropic (three-dimensional) subspace of $V_{\C}$ with a dual isotropic complement. The complexified ascended algebra acts irreducibly on $\Lambda^{\bullet}W$, and its two chirality halves are $\CS = \Lambda^{\mathrm{even}}W$ and $\CSm = \Lambda^{\mathrm{odd}}W$, each of dimension four. Every nonzero conformal spinor (twistor) $u \in \CS$ is a pure spinor: it is the Fock vacuum of the system of three fermionic ladder pairs built on its own annihilator space $W_{u}$, every state of the module is generated from $u$ by those pair operators, and $\CS$ (respectively $\CSm$) is what the even (respectively odd) products generate. Conformal spinors are states of the pair algebra, not its operators. \emph{Provenance:} \cite[Thm.~3.1]{ButlerT9} for the Fock model and the chirality halves; \cite[Thm.~5.3]{ButlerT9} for the pure-spinor and Fock-vacuum statements; the tower paper \cite[Thms.~4.2, 4.3]{ButlerT3} for the iterated pair structure (one qubit per rung, Witt index as capacity) within which this sits.

## technical
Let $W$ be a maximal isotropic, three-dimensional subspace of $V_\C$ with a dual isotropic complement. The complexified ascended algebra acts irreducibly on $\Lambda^\bullet W$, whose chirality halves $\CS = \Lambda^{\mathrm{even}}W$ and $\CSm = \Lambda^{\mathrm{odd}}W$ each have dimension four. This is the chirality of the six-dimensional ascended algebra, the parity of the Fock grade; it is not the spacetime chirality at a point, whose two-dimensional halves $\Som$ and $\Spi$ split $\CS$ itself.

Every nonzero conformal spinor $u \in \CS$ is a pure spinor: it is the Fock vacuum of the three fermionic ladder pairs built on its annihilator $W_u$, every state of the module is generated from $u$ by those pair operators, and $\CS$ (respectively $\CSm$) is what the even (respectively odd) products generate. Conformal spinors are states of the pair algebra, not its operators.

## lay
This restates earlier results of the series for the Standard Model paper. The completed algebra acts on an eight-dimensional space that splits into two halves of opposite chirality, four dimensions each (the chirality of the completed algebra, not the left and right handedness of spacetime spinors at a point). Every nonzero spinor in the first half is the empty state of its own three fermionic ladder pairs, and all other states are reached from it by those operators.

## one-liner
Imported: the Fock module splits into the four-dimensional halves $\CS$ and $\CSm$, and every nonzero conformal spinor is a pure spinor, the Fock vacuum of its own three ladder pairs.
