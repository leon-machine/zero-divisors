---
id: hawking.current-commutator-exactly-edge-split
kind: claim
version: 4
title: The current commutator, exactly, with its edge split
status: proved
region: hawking
subject: thermality
tags: [bosonisation, boundary-modes]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
derivations:
- name: main
  uses:
  - std-algebra.witt-basis-car@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T07.py
  tags:
  - label:prop:edge
- kind: check
  ref: check.py::check_commutator_is_edge_difference
- kind: check
  ref: check.py::check_edge_clean_scalar
- kind: check
  ref: check.py::check_currents_commute
- kind: check
  ref: check.py::check_cross_commutator_edge_supported
locators:
  paper: T07
  number: Prop 6.1
  label: prop:edge
  line: 633
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.witt-basis-car where the proof uses them. Version 3 -> 4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: [a_m, a_m^dagger] = B_m - T_m on all Fock states (L = 6, 7, every m), the scalar m on edge-clean states, [a_m, a_m''] = 0, and the edge support of the cross commutator. Version 1 -> 2. Check strengthened: the case count (every m = 1..L-1 on all 2^L states, 1088 in all) is asserted; basis states built by a module helper. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: the proof uses only the canonical anticommutation relations of the window, which
      the statement sets up itself.'
---

## formal
In the finite window, exactly and as an operator identity,
\[
[\,a_m,\, a_m^\dagger\,] \;=\; B_m - T_m, \qquad
B_m := \sum_{k=1}^{m} N_k, \qquad T_m := \sum_{k=L-m+1}^{L} N_k ,
\]
with $N_k = \psi_k^\dagger\psi_k$: the deviation from the infinite-volume central value is a difference of \emph{edge operators}, supported on the lowest and highest $m$ modes. Consequently, for $2m \le L$, on every state in which the bottom $m$ levels are filled and the top $m$ levels are empty (an \emph{edge-clean} state), $[a_m, a_m^\dagger]$ acts as the scalar $m$: the free-boson relation holds exactly, not asymptotically, on the edge-clean subspace. Moreover $[a_m, a_{m'}] = 0$ for all $m, m'$, exactly; and for $m \neq m'$ the cross commutator $[a_m, a_{m'}^\dagger]$ is a difference of bilinears supported on the lowest and highest $\max(m, m')$ modes, which annihilates every state that is edge-clean at depth $\max(m, m')$.

## technical
Take a window of $L$ fermionic modes and the currents $a_{m} = \sum_{k=1}^{L-m}\psi_{k}^{\dagger}\psi_{k+m}$. Then, exactly, $[a_{m}, a_{m}^{\dagger}] = B_{m} - T_{m}$, where $B_{m}$ and $T_{m}$ are the total occupations of the lowest and highest $m$ modes. The deviation from the infinite-volume central value is therefore a difference of edge operators, and on every edge-clean state (bottom $m$ levels filled, top $m$ levels empty, with $2m \le L$) the commutator is exactly the scalar $m$.

Moreover $[a_{m}, a_{m'}] = 0$ exactly, and for $m \neq m'$ the cross commutator $[a_{m}, a_{m'}^{\dagger}]$ is a difference of bilinears supported on the lowest and highest $\max(m, m')$ modes, which annihilates every state that is edge-clean at that depth.

## lay
On a finite set of fermion levels, certain collective operators behave almost like a free boson field. This result locates the discrepancy exactly: it comes only from the lowest and highest few levels. Whenever the bottom levels are full and the top levels empty, the boson relations hold exactly rather than approximately.

## one-liner
On a finite window the current commutator is exactly $[a_{m}, a_{m}^{\dagger}] = B_{m} - T_{m}$, a difference of edge occupations, so the free-boson relation holds exactly on edge-clean states.
