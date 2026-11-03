---
id: one-relation.form-law-forced-square
kind: claim
version: 3
title: The form of the law is forced by its square
status: proved
region: one-relation
subject: one-relation
tags: [forcing-and-uniqueness, pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
review: typed
about:
- obj.std-algebra.spacetime-algebra
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_operator_identities_on_polynomial_fields
- kind: check
  ref: check.py::check_t_only_solution_klein_gordon_iff_c_squared_minus_one
- kind: check
  ref: check.py::check_the_three_right_factors
locators:
  paper: T16
  number: Lem 5.4
  label: lem:square
  line: 771
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites obj.std-algebra.spacetime-algebra where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: nabla nabla = box and nabla(psi C) = (nabla psi) C on polynomial fields, the exact t-only power-series solution giving -m^2 psi for Hestenes C and +m^2 psi for I gamma_0, and the three stated squares. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'No edges; the proof is self-contained.'
---

## formal
Let $C \in \Cl(1,3)$ be constant. Every solution of $\nabla\psi = m\,\psi\,C$ satisfies the Klein-Gordon equation $\nabla^{2}\psi = -m^{2}\psi$ if and only if $C^{2} = -1$; $C^{2} = +1$ gives $\nabla^{2}\psi = +m^{2}\psi$, the tachyonic sign, and a non-scalar $C^{2}$ gives no scalar second-order equation at all. Hestenes' right factor $C = \gamma_{0}(I\sigma_{3})^{-1}$ has $C^{2} = -1$; $C = I\gamma_{0}$ has $C^{2} = +1$; $C = \gamma_{3} + I\gamma_{2}$ has a non-scalar square.

## technical
For a constant $C \in \Cl(1,3)$, applying the vector derivative twice to $\nabla\psi = m\psi C$ gives $\nabla^{2}\psi = m^{2}\psi C^{2}$, since $\nabla$ acts on the left and $C$ on the right. So every solution is Klein-Gordon, $\nabla^{2}\psi = -m^{2}\psi$, if and only if $C^{2} = -1$; $C^{2} = +1$ gives the tachyonic sign, and a non-scalar $C^{2}$ gives no scalar second-order equation.

Hestenes' factor $C = \gamma_{0}(I\sigma_{3})^{-1}$ squares to $-1$; $I\gamma_{0}$ squares to $+1$; $\gamma_{3} + I\gamma_{2}$ has a non-scalar square.

## lay
A first-order wave equation of this type, applied twice, should give the familiar relativistic relation between energy, momentum and mass. Whether it does depends only on the square of one constant factor in the law. That square must be minus one; any other choice gives faster-than-light behaviour or no sensible equation at all.

## one-liner
A first-order law $\nabla\psi = m\psi C$ with constant $C \in \Cl(1,3)$ squares to Klein-Gordon at mass $m$ exactly when $C^{2} = -1$.
