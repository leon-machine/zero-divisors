---
id: field-theory.conserved-numbers-mass-block
kind: claim
version: 3
title: Conserved numbers in a mass block
status: proved
region: field-theory
subject: quantum-fields
tags: [mass-generation, pairing-and-bogoliubov]
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
derivations:
- name: main
  uses:
  - field-theory.composite-scalars-mean-field-level@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_GRV.py
  tags:
  - id:G2
  - id:G3
  - id:G3b
- kind: check
  ref: check.py::check_quasiparticles_diagonalise_the_block
- kind: check
  ref: check.py::check_rung_numbers_not_conserved_massive_vacuum
- kind: check
  ref: check.py::check_charge_in_rung_algebra
locators:
  paper: FT
  number: Prop 9.1
  label: prop:block
  line: 247
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the quasi-particle diagonalisation of the mass block, the non-conserved rung numbers and <n_a> = (E - K)/(2E), and the conserved charge with the one-quantum state. Version 2 -> 3.'
  env: proposition
  context_refs:
  - field-theory.composite-scalars-mean-field-level
  typing:
    by: ai-typing-pass
    added:
    - field-theory.composite-scalars-mean-field-level
    note: 'Added the composite-scalar proposition, whose mass block (its clause (1)) the statement works
      on. Levels pass: levels written from scratch, keeping every condition and level qualifier of the
      formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - field-theory.composite-scalars-mean-field-level
---

## formal
On the mass block of Proposition \claimref{field-theory.composite-scalars-mean-field-level}(1) the quasi-particle annihilators $\gamma_a = \alpha w_a + \beta v_c$, $\gamma_c = \alpha'w_c + \beta'v_a$ satisfy $[H, \gamma] = -E\gamma$, and $H = E(N_a + N_c) + (K - E)$ exactly, with $N = \gamma^*\gamma/\{\gamma, \gamma^*\}$. A single rung number does not commute with $H$ when $\mu \neq 0$, and the massive vacuum has $\langle n_a\rangle = (E - K)/(2E)$. The charge $Q = n_a - n_c$ lies in the rung algebra, commutes with $H$, equals $N_a - N_c$ and vanishes on the massive vacuum; one massive quantum is the rung state $v_aP_0$ itself.

## technical
On the mass block $H = K(n_a + n_c) + \mu w_aw_c + \mu^*v_cv_a$ the quasi-particle annihilators $\gamma_a = \alpha w_a + \beta v_c$ and $\gamma_c = \alpha'w_c + \beta'v_a$ satisfy $[H, \gamma] = -E\gamma$, and $H = E(N_a + N_c) + (K - E)$ exactly, with $N = \gamma^*\gamma/\{\gamma, \gamma^*\}$. A single rung number does not commute with $H$ when $\mu \neq 0$, and the massive vacuum has $\langle n_a\rangle = (E - K)/(2E)$. The charge $Q = n_a - n_c$ lies in the rung algebra, commutes with $H$, equals $N_a - N_c$ and vanishes on the massive vacuum; one massive quantum is the rung state $v_aP_0$ itself.

## lay
The registered gravity prediction needs numbers that stay fixed while matter evolves. For a massive fermion built in the tower the individual mode occupations change, but the quasi-particle numbers and a charge built from the modes are conserved, and a single massive particle is a single occupied mode.

## one-liner
On a mass block the quasi-particle numbers diagonalise $H$, single rung numbers are not conserved when $\mu \neq 0$, and the charge $n_a - n_c$ in the rung algebra is conserved.
