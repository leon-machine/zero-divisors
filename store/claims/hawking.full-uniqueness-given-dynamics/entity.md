---
id: hawking.full-uniqueness-given-dynamics
kind: claim
version: 3
title: Full uniqueness, given the dynamics
status: proved
region: hawking
subject: thermality
tags: [modular-theory, forcing-and-uniqueness, boundary-modes]
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
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
derivations:
- name: main
  uses:
  - hawking.imported-ideal-fermi-gas-uniqueness@2
  - hawking.imported-quasi-free-states-car-algebra@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_kms_state_unique_among_all_states
- kind: check
  ref: check.py::check_unique_state_is_quasi_free_with_fermi_dirac_symbol
locators:
  paper: T07
  number: Cor 3.8
  label: cor:full
  line: 517
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: uniqueness of the KMS state among all density matrices on two-mode windows with non-diagonal h, and its quasi-free Fermi-Dirac symbol. Version 1 -> 2. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  env: corollary
  typing:
    by: ai-typing-pass
    note: Both edges kept as real premises (the imported Fermi-gas uniqueness and the quasi-free calculus);
      no standard-route derivation, since the main derivation already runs entirely through imported results.
  flow_note: phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07 Def 2.7), the Euclidean rotation
    of T05 Prop 7.21. Its tau is the boost dynamics of T07 Def 2.7, the phase flow on the modes.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
---

## formal
Among all states of $\mathfrak{A}$, $\omega_I$ is the unique $\tau$-KMS state at $\beta$.

## technical
On the boundary-mode algebra $\mathfrak{A}$ with the boost dynamics $\tau$ at inverse temperature $\beta$, the I-state $\omega_{I}$ is the only $\tau$-KMS state at $\beta$, among all states and not only within the quasi-free class.

This follows from the imported uniqueness theorem for the ideal Fermi gas, whose hypotheses the definition of the algebra and its dynamics satisfies: the unique KMS state is the quasi-free state with symbol $(1 + e^{\beta h})^{-1}$, which the quasi-free calculus identifies with $\omega_{I}$. The dynamics and the value of $\beta$ are inputs here, not derived.

## lay
Once the horizon modes' time evolution and the temperature are given, there is exactly one equilibrium state at that temperature, and it is the I-state. This uses a standard result about ideal gases of fermions. It does not explain where the time evolution itself comes from.

## one-liner
Given the boost dynamics and $\beta$, the I-state is the unique $\tau$-KMS state of the boundary-mode algebra among all states.
