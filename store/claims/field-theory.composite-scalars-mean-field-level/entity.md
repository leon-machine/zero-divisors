---
id: field-theory.composite-scalars-mean-field-level
kind: claim
version: 4
title: Composite scalars, at mean-field level
status: proved
region: field-theory
subject: quantum-fields
tags: [symmetry-breaking, mass-generation, pairing-and-bogoliubov, recovers-known-physics]
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
- obj.field-theory.single-algebra-field
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_BOS.py
  tags:
  - id:S1.1
  - id:S1.2
  - id:S1.3
  - id:S2.1
  - id:S2.2
  - id:S2.3
  - id:S2.4
  - id:S2.5
  - id:S3
- kind: check
  ref: check.py::check_block_spectrum_and_dispersion
- kind: check
  ref: check.py::check_pairing_tower_threshold
- kind: check
  ref: check.py::check_gap_equation
- kind: check
  ref: check.py::check_axial_phase_flat_direction
locators:
  paper: FT
  number: Prop 7.1
  label: prop:njl
  line: 182
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the block spectrum and dispersion, the pairing tower''s exact pair states and threshold with the mean field, the gap equation, and the flat axial phase. Version 2 -> 3. Check strengthened: mean-field energies at the five sample amplitudes pinned exactly above, at and below G_c (at G_c equal to n_b (E - K)^2/(2K)); shell inputs moved to module level. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'No edges: the four clauses are exact computations on tower elements. The source calls the Nambu-Jona-Lasinio
      condensate a textbook result reproduced in the series'' algebra, but the store''s standard field-theory
      fact imports only its random-phase Goldstone pole, not the mean-field condensate, so no standard-route
      derivation was added. Levels pass: levels written from scratch, keeping every condition and level
      qualifier of the formal statement.'
---

## formal
\begin{enumerate}
\item The two-mode block $H = K(n_a + n_c) + \mu w_aw_c + \mu^*v_cv_a$, $\mu \in \mathrm{span}\{1, I_4\}$, is self-adjoint, with $\operatorname{ad}_H^2 = K^2 + |\mu|^2$ on all four mode operators and block spectrum $\{K - E, K, K, K + E\}$, $E = \sqrt{K^2 + |\mu|^2}$; with $\mu = mB$ the dispersion is $E^2 = K^2 + m^2$.
\item The tower element $H_4 = \sum_b K(n_a + n_c) - GP^*P$, $P = \sum_b w_aw_c$, is self-adjoint, conserves the axial number, and has exact pair states of energy $2Kn - Gn(n_b - n + 1)$; pairs enter the ground state exactly when $G > 2K/n_b$, the threshold of the mean-field energy.
\item In the block ground state $\langle w_aw_c\rangle = -\mu^*/(2E)$, so the gap equation holds: the fermion mass is $G$ times the pair condensate.
\item The axial phase is an inner unitary of the tower, $U H(\mu) U^* = H(\mu e^{-2\theta I_4})$: the mean-field energy has an exactly flat phase direction.
\end{enumerate}

## technical
At mean-field level. The two-mode block $H = K(n_a + n_c) + \mu w_aw_c + \mu^*v_cv_a$ with $\mu \in \mathrm{span}\{1, I_4\}$ is self-adjoint, with $\operatorname{ad}_H^2 = K^2 + |\mu|^2$ on all four mode operators and block spectrum $\{K - E, K, K, K + E\}$, $E = \sqrt{K^2 + |\mu|^2}$; with $\mu = mB$ the dispersion is $E^2 = K^2 + m^2$. The tower element $H_4 = \sum_b K(n_a + n_c) - GP^*P$, $P = \sum_b w_aw_c$, is self-adjoint, conserves the axial number and has exact pair states of energy $2Kn - Gn(n_b - n + 1)$; pairs enter the ground state exactly when $G > 2K/n_b$, the threshold of the mean-field energy.

In the block ground state $\langle w_aw_c\rangle = -\mu^*/(2E)$, so the gap equation holds: the fermion mass is $G$ times the pair condensate. The axial phase is an inner unitary of the tower, $UH(\mu)U^* = H(\mu e^{-2\theta I_4})$, so the mean-field energy has an exactly flat phase direction.

## lay
A pair of fermion modes in the tower can bind into a scalar condensate that gives the fermions mass, the mechanism of Nambu and Jona-Lasinio. At mean-field level these exact computations reproduce its ingredients: the massive energy relation, the coupling above which pairs condense, the gap equation, and a direction in which the condensate's phase can turn at no cost.

## one-liner
At mean-field level the tower reproduces the Nambu-Jona-Lasinio mechanism: a self-adjoint mass block with $E^2 = K^2 + m^2$, pairing above $G = 2K/n_b$, the gap equation and a flat axial phase.
