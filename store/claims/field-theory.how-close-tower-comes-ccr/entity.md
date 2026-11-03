---
id: field-theory.how-close-tower-comes-ccr
kind: claim
version: 4
title: How close the tower comes to the CCR
status: proved
region: field-theory
subject: quantum-fields
tags: [car-algebra, limits]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
review: typed
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - field-theory.imported-tower-limit@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_PHO.py
  tags:
  - id:T1
  - id:T2
  - id:T3
- kind: check
  ref: check.py::check_commutator_is_n_minus_number
- kind: check
  ref: check.py::check_quasi_spin_su2
- kind: check
  ref: check.py::check_finite_ladder
locators:
  paper: FT
  number: Prop 8.3
  label: prop:quasispin
  line: 236
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: [B, B*] = n - N, the su(2) quasi-spin relations and the finite ladder of n + 1 states for n = 1..4. Version 2 -> 3. Check strengthened: the sample one-quantum state is asserted nonzero with N one = one, so the n - 1 eigenvalue test cannot pass on zero; plane index moved to module level. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: exact computation. The source calls the quasi-spin a textbook result (Anderson''s)
      reproduced in the algebra; no imported quasi-spin claim is in the store, so no standard-route derivation
      was added. Levels pass: levels written from scratch, keeping every condition and level qualifier
      of the formal statement.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises:
    - field-theory.imported-tower-limit
    added_dependants: []
    added_about:
    - obj.tower.tower
    verdict: connected
    note: Rests on the tower's CAR, as the boost proposition of the same note does; nothing in the store
      uses it, so the link is one way, the ledger's reading of it as the field-theory form of T09's statistics
      no-go being commentary in a setting note.
---

## formal
For $n$ tower pairs, $B = \sum_jw_{c_j}w_{d_j}$ gives $[B, B^*] = n - (N_c + N_d)$; with $K_3 = (N_c + N_d - n)/2$ the triple $(B^*, B, K_3)$ is an $\mathfrak{su}(2)$ quasi-spin, the ladder has $n + 1$ states, and $[b, b^*] = 1 - 2k/n$ on $k$-pair states for $b = B/\sqrt{n}$. The CCR is the Inonu-Wigner contraction $n \to \infty$; the operator limit holds only on states of bounded boson number.

## technical
For $n$ tower pairs, $B = \sum_jw_{c_j}w_{d_j}$ gives $[B, B^*] = n - (N_c + N_d)$; with $K_3 = (N_c + N_d - n)/2$ the triple $(B^*, B, K_3)$ is an $\mathfrak{su}(2)$ quasi-spin, the ladder has $n + 1$ states, and $[b, b^*] = 1 - 2k/n$ on $k$-pair states for $b = B/\sqrt{n}$. The CCR are the Inonu-Wigner contraction $n \to \infty$, and the operator limit holds only on states of bounded boson number.

## lay
Pairs of fermion modes in the tower behave almost like bosons, but not exactly: they form a finite ladder of states, like a quantum spin. The exact boson relations appear only in the limit of infinitely many pairs, and then only for states with a bounded number of bosons.

## one-liner
Tower pair operators form an $\mathfrak{su}(2)$ quasi-spin with $[b, b^*] = 1 - 2k/n$, reaching the CCR only as $n \to \infty$ on states of bounded boson number.
