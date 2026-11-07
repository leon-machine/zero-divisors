---
id: singularity.descended-form-state-independent
kind: claim
version: 4
title: The descended form is state independent
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
derivations:
- name: main
  uses:
  - singularity.descent-parity-average@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.6
- kind: check
  ref: check.py::check_descended_marginal_is_diagonal_gibbs
- kind: check
  ref: check.py::check_beta_unique_and_endpoints
- kind: check
  ref: check.py::check_zero_weight_mode
locators:
  paper: T05
  number: Thm 7.6
  label: thm:form
  line: 1760
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the descended marginal of arbitrary states on 1 to 3 modes is the Gibbs matrix with x = (1 - p)/p, uniqueness and endpoints of beta, and the zero-weight case. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'the parity-average theorem supplies the range of the descent and is a real premise; removed
      the mechanical repair edge to the transport algorithm: the section frames its results as a step
      of that algorithm, but the proof is a self-contained computation and does not use it as a premise'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  merged_from:
  - id: state-selection.descended-form-state-independent
    version: 1
    locators:
      paper: T05-state-selection
      number: Thm 3.1
      label: thm:form
      line: 161
    uses:
    - state-selection.descent-parity-average@3
    checked_by: verify_state_selection.py num:3.1
    proof_files:
    - proof-main.tex (kept here as merged-state-selection.descended-form-state-independent-proof-main.tex)
    formal: 'Let $\omega$ be \emph{any} state on the ledger algebra, with density matrix $\rho$, and let $\rho_k$
      be the marginal of mode $k$. Then $E_k(\rho_k)$ is diagonal in the number basis of mode $k$, and therefore

      \[

      E_k(\rho_k) \;=\; \frac{e^{-\beta_k \omega_k N_k}}{Z_k}

      \]

      for a unique $\beta_k \in [-\infty, +\infty]$, namely $\beta_k \omega_k = \log\bigl(p_k/(1-p_k)\bigr)$ with
      $p_k$ the descended vacancy probability. The descended single-mode state is a Gibbs state of the boost generator
      $K_k$ whatever the ascended state was; no hypothesis on $\omega$ is used.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Thm 3.1 (state-selection.descended-form-state-independent, retired to
      tombstones.yaml) into this entity: the same theorem; the T05 statement adds the zero-weight scope. Kept this
      statement, levels and checks; the note''s entity is recorded above and its proof files are kept in this folder.
      References to the note''s id were repointed here. Extraction-only change, so the version and the dependants''
      pins are unchanged.'
---

## formal
Let $\varrho$ be the density matrix of \emph{any} state on the boundary mode space, and $\varrho_k$ its marginal at mode $k$. Then $E_k(\varrho_k)$ is diagonal in that mode's number basis, and therefore
\[
E_k(\varrho_k) \;=\; \frac{e^{-\beta_k \omega_k N_k}}{Z_k}
\]
for a unique $\beta_k \in [-\infty, +\infty]$, determined by $\beta_k\omega_k = \log\bigl(p_k/(1-p_k)\bigr)$ with $p_k$ the descended vacancy probability. (Stated for $\omega_k \neq 0$: at a zero-weight mode the right side is $\tfrac12\,\mathrm{id}$ for every $\beta_k$, so uniqueness always fails there, and existence fails unless $p_k = \tfrac12$.) The descended single-mode state is a Gibbs state of the boost generator $K_k$ whatever the ascended state was: no hypothesis on the state is used.

## technical
For any state on the boundary mode space and any mode $k$, the descended marginal $E_k(\varrho_k)$ is diagonal in the number basis, because the range of $E_k$ is the even subalgebra. A diagonal density matrix $\operatorname{diag}(p_k, 1 - p_k)$ is then the Gibbs state $e^{-\beta_k\omega_k N_k}/Z_k$ for a unique $\beta_k \in [-\infty, +\infty]$, fixed by $\beta_k\omega_k = \log\bigl(p_k/(1-p_k)\bigr)$, provided $\omega_k \neq 0$.

At a zero-weight mode the right side is $\tfrac12\,\id$ for every $\beta_k$, so uniqueness fails there and existence requires $p_k = \tfrac12$. No hypothesis on the ascended state is used.

## lay
Once the descent has removed a mode's coherences, what remains is just the probability of the mode being empty or occupied. Any such pair of probabilities can be read as a thermal state at exactly one temperature, allowing the extreme cases at either end. This holds whatever state the system started in, provided the mode has nonzero weight.

## one-liner
Whatever the ascended state, each descended single-mode marginal is a Gibbs state of the boost generator at a unique $\beta_k$, for every mode of nonzero weight.
