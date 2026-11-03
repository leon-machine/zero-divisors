---
id: angle.within-supplied-class-spectrum-condition-selects
kind: claim
version: 4
title: Within the supplied class the spectrum condition selects Boulware, or nothing
status: proved
region: angle
subject: thermality
tags: [thermal-premises, entanglement, no-go]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-angle, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - singularity.class-relative-no-go-no-supplied@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_unique_ground_state_is_a_product_number_state
- kind: check
  ref: check.py::check_degenerate_ground_space_selects_nothing
locators:
  paper: T05-angle
  number: Prop 4.1
  label: prop:boulware
  line: 167
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: unique ground states of number-polynomial generators are product number states with pure marginals, and the degenerate ground space of (N0 - N1)^2. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: the supplied class enters as an explicit hypothesis (a polynomial in the number operators),
      so the singularity paper''s results defining it are vocabulary rather than premises.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - singularity.class-relative-no-go-no-supplied
    added_dependants: []
    added_about: []
    verdict: connected
    note: Applying the computation to the supplied class rests on the singularity paper's theorem that the
      class is ultralocal, cited directly rather than through the note's Fact 1.1 so that (L), (Q) and (R)
      are not inherited; no result of the store uses the proposition, the verdict being drawn in a setting
      note.
---

## formal
Let $H$ be a generator in the supplied class on $\nu$ modes, a polynomial in the number operators, and let a cut divide the modes into two sides.
\begin{enumerate}
\item[(i)] $H$ is diagonal in the joint number basis. If its ground state is unique, that state is a number basis state: a product across the cut, with a pure marginal on each side, an eigenvector of every $N_{k}$ and hence of every boost generator $\sum_{k}\omega_{k}(N_{k} - \tfrac12)$, and Gibbs on a side at no finite $\beta$: a Boulware-type state, a product with pure marginals.
\item[(ii)] If the ground state is not unique, the ground space may contain entangled states, but the spectrum condition selects none of them: for $H = (N_{0} - N_{1})^{2} = N_{0} + N_{1} - 2N_{0}N_{1}$ on the pair, the ground space is $\operatorname{span}\{\ket{00}, \ket{11}\}$, which contains the thermofield pair $\tfrac45\ket{00} + \tfrac35\ket{11}$ and the product state $\ket{00}$ alike.
\end{enumerate}
Within the supplied class, therefore, positivity of the energy selects a Boulware-type state or selects no state, and Claim G is dead at the state-selection step.

## technical
Let $H$ be a generator in the supplied class on $\nu$ modes, a polynomial in the number operators, and let a cut divide the modes into two sides. Then $H$ is diagonal in the joint number basis, so a unique ground state is a number basis state: a product across the cut with a pure marginal on each side, an eigenvector of every $N_{k}$ and of every boost generator $\sum_{k}\omega_{k}(N_{k} - \tfrac12)$, and Gibbs on a side at no finite $\beta$. This is a Boulware-type state.

If the ground state is not unique, the ground space may contain entangled states, but the spectrum condition singles out none of them: for $H = (N_{0} - N_{1})^{2}$ on the pair, the ground space $\operatorname{span}\{\ket{00}, \ket{11}\}$ contains both the thermofield pair $\tfrac45\ket{00} + \tfrac35\ket{11}$ and the product state $\ket{00}$. Within the supplied class, positivity of the energy selects a Boulware-type state or no state, so Claim G fails at the state-selection step.

## lay
The framework's own dynamics for the horizon modes never moves particles from one mode to another. This result shows that with only such dynamics, asking for the lowest-energy state either picks out a state with no correlation across the horizon, which is not thermal on either side, or picks out nothing because several states tie. So within that dynamics the requirement of positive energy cannot by itself select a thermal state.

## one-liner
For generators in the supplied class, the spectrum condition selects either a Boulware-type product state with pure marginals or no state at all.
