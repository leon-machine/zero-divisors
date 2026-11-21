---
id: dark-tower-matter.ladder
kind: claim
version: 2
title: The momentum-preserving mixings of constituents
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [flavour-and-mixing]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.adjoint-norm@3
  - dark-tower-matter.constituents-field@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:C1
  - id:C2
- kind: check
  ref: check.py::check_unitary_mixings_preserve_momentum
- kind: check
  ref: check.py::check_only_unitary_mixings
- kind: check
  ref: check.py::check_momentum_preserving_groups
locators:
  paper: T14c
  number: Thm 3.7
  label: thm:ladder
  line: 374
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: F-unitary mixings (rotations and phases through every unit, n = 2, 3) preserve total momentum as polynomial identities in all six causal towers; non-unitary ones do not; Hermitian polarisation injective; anti-Hermitian algebra dimensions give O(n), U(n), Sp(n). Version 1 -> 2.'
  env: theorem
  typing:
    by: ai-typing-pass
    added:
    - obj.dark-tower-matter.ideals-fields-momentum
    note: 'Both edges are cited in the proof (the norm law and the assignment of fields) and were kept;
      added the definition as about. Levels pass: levels written from scratch, keeping every condition
      and level qualifier of the formal statement.'
about:
- obj.dark-tower-matter.ideals-fields-momentum
---

## formal
Let $\F = f\Cl^{0}(V)f$ act on $S$ on the right and on $S^{n}$ by $\psi'_{i} = \sum_{k}\psi_{k}U_{ki}$ for $U \in M_{n}(\F)$. Then $U$ preserves the total momentum of every $n$-tuple if and only if $UU^{\dagger} = 1$, where $(U^{\dagger})_{ik} = (U_{ki})^{\dagger}$. The momentum-preserving group is $O(n)$, $U(n)$ or $Sp(n)$ as $\F = \R$, $\C$, $\HH$: $O(n)$ in the three-dimensional towers, $U(n)$ in this tower and the mirror, $Sp(n)$ in the five-dimensional towers.

## technical
Let the corner field $\F = f\Cl^0(V)f$ act on the spinor ideal $S$ on the right and on $n$-tuples by $\psi'_i = \sum_k \psi_kU_{ki}$ with $U \in M_n(\F)$. Then $U$ preserves the total momentum of every $n$-tuple if and only if $UU^\dagger = 1$, with $(U^\dagger)_{ik} = (U_{ki})^\dagger$: by the norm law, preserving momentum is preserving the positive form $\sum_k N(a_k)$ on $\F^n$.

So the momentum-preserving group is $O(n)$, $U(n)$ or $Sp(n)$ as $\F$ is $\R$, $\C$ or $\HH$: $O(n)$ in the three-dimensional towers, $U(n)$ in this tower and the mirror, and $Sp(n)$ in the five-dimensional towers.

## lay
Several constituents can be mixed into one another using the tower's own kind of number. This theorem shows that the mixings that keep their total momentum are exactly the unitary ones for that kind of number: rotations for real numbers, unitary matrices for complex numbers, and their quaternionic analogue for quaternions.

## one-liner
A mixing $U \in M_n(\F)$ of $n$ constituents preserves total momentum if and only if $UU^\dagger = 1$, giving $O(n)$, $U(n)$ or $Sp(n)$ in the three-, four- and five-dimensional towers.
