---
id: lepton.unit-action-cell-action
kind: claim
version: 3
title: The unit action and the cell action
status: proved
region: lepton
subject: standard-model
tags: [representation-theory]
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
  - lepton.content-constituent-space@4
  - lepton.imported-tensor-ledger-contains-no-lepton@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12_lepton.py
  tags:
  - label:prop:twoactions
- kind: check
  ref: check.py::check_one_pair_identification_is_isomorphism
- kind: check
  ref: check.py::check_cell_span_exceeds_constituents
- kind: check
  ref: check.py::check_weights_and_spin_of_the_two_actions
locators:
  paper: T12-lepton
  number: Prop 2.3
  label: prop:twoactions
  line: 247
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the k = 1 identification is an isomorphism; for k = 2, 3 the cell span is S^k C^2 x Lambda^k C^3 (dimensions 9, 4, spin k/2, weight k) and R_k is not invariant. Version 2 -> 3.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: 'Formal level has no twistor language; the lay level and the proof''s twistor wording (two twistors, excited twistors) were converted to conformal spinors. Fact ids that contain the word twistor are left as ids.'
  source_title: |-
    The unit action and the cell action
  source_formal: |-
    Let $R_{k} \subset \Lambda^{k}(\C^{2} \otimes \C^{3})$ be the span of the single-row $k$-pair states $\bigwedge_{a \in S}(e_{i} \otimes f_{a})$, $i \in \{0, 1\}$, $S \subset \{1,2,3\}$ with $|S| = k$, and identify $R_{k}$ with $\Con_{k}$ by $\bigwedge_{a \in S}(e_{i} \otimes f_{a}) \mapsto e_{i} \otimes f_{S}$. Then:
    \begin{enumerate}
    \item For $k = 1$ the identification is an isomorphism of $U(2) \times U(3)$-representations: the cell action $A \otimes B$ on the cells and the unit action on $\Con_{1}$ coincide. The pair-level generators of T12 are the one-pair constituents.
    \item For $k = 2, 3$ the cell action does not preserve $R_{k}$: the $U(2) \times U(3)$-span of $R_{k}$ under the cell action is $S^{k}\C^{2} \otimes \Lambda^{k}\C^{3}$, of dimension $(k+1)\binom{3}{k}$, that is $(3,\bar{3})$ at $k = 2$ and $(4,1)$ at $k = 3$, with abelian weight $k$; under the unit action $\Con_{k} = (2, \Lambda^{k}\C^{3})$ has dimension $2\binom{3}{k}$ and weight $3 - 2k$. The same basis states, the filled rows among them, carry different representations under the two actions.
    \item Consequently the constituent space is not a subrepresentation of the tensor ledger, and the tensor ledger is the Fock space of the pairs, the multi-pair states of the composite counted cell by cell; it is not the space of the composite's constituents.
    \end{enumerate}
  typing:
    by: ai-typing-pass
    removed:
    - lepton.imported-twistor-state-pair-system-excitations
    - standard-model.internal-symmetry-ladder
    note: 'Removed the ladder Fact (cited only as silent on excited twistors, deciding neither way) and
      the pair-system Fact (cited as agreeing with the ledger''s definition, which alone carries clause
      (3)); the second removal is the less certain. Levels pass: conditions already kept.'
  env: proposition
---

## formal
Let $R_{k} \subset \Lambda^{k}(\C^{2} \otimes \C^{3})$ be the span of the single-row $k$-pair states $\bigwedge_{a \in S}(e_{i} \otimes f_{a})$, $i \in \{0, 1\}$, $S \subset \{1,2,3\}$ with $|S| = k$, and identify $R_{k}$ with $\Con_{k}$ by $\bigwedge_{a \in S}(e_{i} \otimes f_{a}) \mapsto e_{i} \otimes f_{S}$. Then:
\begin{enumerate}
\item For $k = 1$ the identification is an isomorphism of $U(2) \times U(3)$-representations: the cell action $A \otimes B$ on the cells and the unit action on $\Con_{1}$ coincide. The pair-level generators of T12 are the one-pair constituents.
\item For $k = 2, 3$ the cell action does not preserve $R_{k}$: the $U(2) \times U(3)$-span of $R_{k}$ under the cell action is $S^{k}\C^{2} \otimes \Lambda^{k}\C^{3}$, of dimension $(k+1)\binom{3}{k}$, that is $(3,\bar{3})$ at $k = 2$ and $(4,1)$ at $k = 3$, with abelian weight $k$; under the unit action $\Con_{k} = (2, \Lambda^{k}\C^{3})$ has dimension $2\binom{3}{k}$ and weight $3 - 2k$. The same basis states, the filled rows among them, carry different representations under the two actions.
\item Consequently the constituent space is not a subrepresentation of the tensor ledger, and the tensor ledger is the Fock space of the pairs, the multi-pair states of the composite counted cell by cell; it is not the space of the composite's constituents.
\end{enumerate}

## technical
Identify the single-row $k$-pair states $R_{k} \subset \Lambda^{k}(\C^{2} \otimes \C^{3})$ with $\Con_{k}$ by $\bigwedge_{a \in S}(e_{i} \otimes f_{a}) \mapsto e_{i} \otimes f_{S}$. At $k = 1$ the cell action $A \otimes B$ and the unit action coincide, so the pair-level generators are the one-pair constituents.

At $k = 2, 3$ the cell action does not preserve $R_{k}$: it spans $S^{k}\C^{2} \otimes \Lambda^{k}\C^{3}$, that is $(3,\bar{3})$ and $(4,1)$, with weight $k$, while under the unit action $\Con_{k} = (2, \Lambda^{k}\C^{3})$ has dimension $2\binom{3}{k}$ and weight $3 - 2k$. Hence the constituent space is not a subrepresentation of the tensor ledger: the ledger is the Fock space of the pairs, counted cell by cell, not the space of the composite's constituents.

## lay
The slot symmetry can act on a basic spinor state with several excited pairs in two ways: once on the state as a whole, or separately on each pair. For one excited pair the two agree. For two or three they give different representations of the same states, so the space of constituents is genuinely different from the cell-by-cell state space, and the difference sits exactly at multiply excited spinor states.

## one-liner
The unit action and the cell action agree on one-pair states but differ on two- and three-pair states, so the constituent space is not a subrepresentation of the tensor ledger.
