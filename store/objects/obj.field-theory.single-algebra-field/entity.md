---
id: obj.field-theory.single-algebra-field
kind: object
version: 1
title: The single-algebra field
status: defined
region: field-theory
subject: quantum-fields
tags: [pseudoscalar-and-centre]
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
locators:
  paper: FT
  number: Def 5.1
  label: def:field
  line: 136
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: 'Definition; no edges. Levels pass: levels written from scratch, keeping every condition and
      level qualifier of the formal statement.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - field-theory.elementary-photon-ga
    - field-theory.fock-space-maxwell-modes
    - field-theory.composite-scalars-mean-field-level
    - field-theory.operator-newtonian-coupling
    - field-theory.orientation-relocated
    added_about: []
    verdict: connected
    note: A definition cannot carry uses or assumes; the added links are about edges from the later propositions
      whose statements work with the operator unit i = I_4 and span{1, I_4} coefficients.
---

## formal
Values are even and chiral elements of the ground; modes are tower planes; the operator imaginary unit is $i = I_4$, which commutes with every mode; physical numbers are read by the projection $\proj$ onto $\mathrm{span}\{1, I_4\}$. The pairing of values is $\ip{\phi}{u} = \alpha(\phi, u) + I_4\,\alpha(\phi\IS, u)$ with $\alpha(\phi, u) = \langle \phi^*u\rangle_0$.

## technical
Values are even and chiral elements of the ground $\Cl(1,3)$; modes are tower planes; the operator imaginary unit is $i = I_4$, which commutes with every mode; and physical numbers are read by the projection $\proj$ onto $\mathrm{span}\{1, I_4\}$. The pairing of values is $\ip{\phi}{u} = \alpha(\phi, u) + I_4\,\alpha(\phi\IS, u)$ with $\alpha(\phi, u) = \langle \phi^*u\rangle_0$.

## lay
This definition sets up quantum fields inside a single algebra: the field's values are spinors of the spacetime algebra, its quantum modes come from the tower, and the spacetime volume element plays the role of the imaginary unit. Measurable numbers are read off by keeping only the parts built from one and that volume element.

## one-liner
Defines the single-algebra field: even chiral ground values, tower-plane modes, the unit $i = I_4$, the projection $\proj$ onto $\mathrm{span}\{1, I_4\}$ and the pairing $\alpha(\phi, u) + I_4\,\alpha(\phi\IS, u)$.
