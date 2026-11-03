---
id: singularity.ascended-marginals-are-diagonal
kind: claim
version: 5
title: Ascended marginals are diagonal
status: proved
region: singularity
subject: descent
tags: [descent-map]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
about:
- obj.singularity.grading-parity-automorphism
derivations:
- name: main
  uses:
  - singularity.descended-form-state-independent@4
  assumes:
  - singularity.p-univalence@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.10
- kind: check
  ref: check.py::check_even_units_have_zero_ladder_expectation_and_diagonal_marginals
- kind: check
  ref: check.py::check_even_state_marginals_are_descended_gibbs
- kind: check
  ref: check.py::check_parity_protection_is_special_case
locators:
  paper: T05
  number: Thm 7.10
  label: thm:even
  line: 1786
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: every even matrix unit has zero ladder expectations and diagonal marginals (N <= 4), even states'' marginals are the descended Gibbs matrices, and the model states as the parity-protection case. Version 4 -> 5.'
  env: theorem
  context_refs:
  - singularity.modular-descent
  - singularity.parity-protection
  - singularity.pinching-against-partial-trace-scope-coincidence
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.p-univalence
    note: 'added the univalence premise (P) to assumes as the statement''s hypothesis; removed the mechanical
      repair edge to the transport algorithm: the section frames its results as a step of that algorithm,
      but the proof is a self-contained computation and does not use it as a premise; the pinching-scope
      proposition, the modular-descent theorem and the parity protection lemma are cited only for comparison
      or as consequences, so they were not added Levels pass: the lay now names premise (P).'
  repair:
    notes:
    - 'lay text corrected after independent review: per-mode temperature only; the common temperature
      needs (R)'
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  merged_from:
  - id: state-selection.ascended-marginals-are-diagonal
    version: 4
    locators:
      paper: T05-state-selection
      number: Thm 3.5
      label: thm:even
      line: 193
    about:
    - obj.state-selection.grading-parity-automorphism
    uses:
    - singularity.parity-protection@2
    - state-selection.descended-form-state-independent@1
    assumes:
    - singularity.p-univalence@2
    proof_files:
    - orig-proof-main.tex (kept here as merged-state-selection.ascended-marginals-are-diagonal-orig-proof-main.tex)
    - proof-main.tex (kept here as merged-state-selection.ascended-marginals-are-diagonal-proof-main.tex)
    formal: 'Let $\omega$ satisfy (P). Then for every mode $k$,

      \[

      \omega(v_k) \;=\; \omega(v_k^{*}) \;=\; 0 ,

      \]

      so the ascended marginal $\rho_k$ is diagonal in the number basis, coincides with $E_k(\rho_k)$, and is by Theorem
      \claimref{state-selection.descended-form-state-independent} the Gibbs state of $K_k$ at a unique $\beta_k$.
      Consequently, on every single-mode marginal, partial trace and pinching coincide, which is \cite[Prop.~9.2(i)]{ButlerT5}
      with hypothesis (ii) removed; and the parity protection lemma of the finite-ledger model, \cite[Lem.~12.1]{ButlerT5},
      is the special case of this theorem for the model''s states, which are even because every configuration in their
      support has even total occupation.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Thm 3.5 (state-selection.ascended-marginals-are-diagonal, retired to
      tombstones.yaml) into this entity: the same theorem; the T05 statement adds the zero-weight scope (the note''s
      unique beta fails at zero weight). Kept this statement, levels and checks; the note''s entity is recorded above
      and its proof files are kept in this folder. References to the note''s id were repointed here. Extraction-only
      change, so the version and the dependants'' pins are unchanged.'
---

## formal
Let $\omega$ satisfy (P). Then $\omega(v_k) = \omega(v_k^{*}) = 0$ at every mode, so the ascended marginal $\varrho_k$ is diagonal in the number basis, coincides with $E_k(\varrho_k)$, and is by Theorem \claimref{singularity.descended-form-state-independent} the Gibbs state of $K_k$ at a unique $\beta_k$ for $\omega_k \neq 0$ (at a zero-weight mode diagonality still holds, and the Gibbs form requires $p_k = \tfrac12$, Theorem \claimref{singularity.descended-form-state-independent}'s parenthesis). Consequently partial trace and pinching coincide on every single-mode marginal, which is Proposition \claimref{singularity.pinching-against-partial-trace-scope-coincidence}(i) with hypothesis (ii) of Theorem \claimref{singularity.modular-descent} removed; and the parity protection lemma of the finite-mode model, Lemma \claimref{singularity.parity-protection}, is the special case of this theorem for the model's states, which are even because every configuration in their support has even total occupation.

## technical
For a state $\omega$ satisfying univalence, $\omega \circ \alpha = \omega$, the odd ladder elements of each mode have vanishing expectation: $\omega(v_k) = \omega(\alpha(v_k)) = -\omega(v_k)$, so $\omega(v_k) = \omega(v_k^{*}) = 0$. These are exactly the off-diagonal entries of the single-mode marginal $\varrho_k$ in the number basis, so $\varrho_k$ is diagonal and equals $E_k(\varrho_k)$. By the state independence of the descended form it is then the Gibbs state of $K_k$ at a unique $\beta_k$ when $\omega_k \neq 0$; at a zero-weight mode diagonality still holds, but the Gibbs form requires $p_k = \tfrac12$.

Consequently partial trace and pinching coincide on every single-mode marginal of such a state, without the extra hypothesis that was needed before. The parity protection lemma of the finite-mode model is the special case of the model's states, which are even because every configuration in their support has even total occupation.

## lay
If the physical states of the boundary modes are required to be even under fermion parity (premise (P)), then each mode, looked at on its own, carries no coherence between being empty and being occupied. Its description reduces to a pair of probabilities. When the mode has nonzero weight, that pair is exactly a thermal distribution at a temperature of its own, so the thermal form of each single mode follows from parity rather than being assumed. That every mode shares the Hawking temperature needs a further premise and is not part of this result.

## one-liner
Under univalence every single-mode marginal is diagonal in the number basis, hence equal to its descent and, at nonzero weight, a Gibbs state of the boost generator at a unique $\beta_k$.
