---
id: singularity.kms-uniqueness-factor
kind: claim
version: 5
title: KMS uniqueness at a factor
status: proved
region: singularity
subject: descent
tags: [modular-theory, forcing-and-uniqueness, classical-theorem]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 5
  source: maintainer pass 2026-11-07 (GA units)
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.13
- kind: check
  ref: check.py::check_kms_iff_gibbs
- kind: check
  ref: check.py::check_kms_states_form_a_line_in_beta
locators:
  paper: T05
  number: Thm 7.13
  label: thm:kmsunique
  line: 1806
outside_ga:
  kind: complex-analysis
  why: 'the inner flow Ad(e^{itK}) and its continuation alpha_{i beta} are taken on a general complex matrix factor, not on a space the store ties to I_4'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the inner flow Ad(e^{itK}) and its continuation alpha_{i beta} are taken on a general complex matrix factor, not on a space the store ties to I_4.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the KMS constraints on Mat_n (n <= 4, non-diagonal and degenerate K, both signs of beta) have exactly the Gibbs solution, and distinct beta give distinct states. Version 2 -> 3. Wording fix (Leon 2026-10-23): the line of KMS states is stated for K not a multiple of 1 (a trivial flow gives the tracial state for every beta), at formal, technical and lay. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'no edges remain, the proof being a self-contained trace computation on a matrix factor; removed
      the mechanical repair edge to the transport algorithm: the section frames its results as a step
      of that algorithm, but the proof is a self-contained computation and does not use it as a premise;
      the source places the general simplex form of KMS states right after it but does not say it recovers
      this theorem, so no standard route was added'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - $\alpha_{i\beta}$ in the KMS condition (complex analysis)
  merged_from:
  - id: state-selection.kms-uniqueness-factor
    version: 1
    locators:
      paper: T05-state-selection
      number: Thm 4.2
      label: thm:kmsunique
      line: 217
    uses:
    - state-selection.imported-general-statement@2
    checked_by: verify_state_selection.py num:4.2
    proof_files:
    - proof-main.tex (kept here as merged-state-selection.kms-uniqueness-factor-proof-main.tex)
    - proof-standard-route.tex (kept here as merged-state-selection.kms-uniqueness-factor-proof-standard-route.tex)
    formal: Let $\Aa$ be a matrix factor, $\alpha_t = \operatorname{Ad}(e^{itK})$ a flow, and $\beta \neq 0$. A state
      $\omega = \tr(\rho\,\cdot\,)$ is $(\alpha, \beta)$-KMS if and only if $\rho = e^{-\beta K}/\tr e^{-\beta K}$.
      In particular, for each $\beta$ there is exactly one KMS state, and the set of KMS states of the flow, over
      all $\beta$, is a line parametrised by $\beta$.
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Thm 4.2 (state-selection.kms-uniqueness-factor, retired to tombstones.yaml)
      into this entity: the same theorem. Kept this statement, levels and checks; the note''s entity is recorded above
      and its proof files are kept in this folder. References to the note''s id were repointed here. Extraction-only
      change, so the version and the dependants'' pins are unchanged.'
---

## formal
Let $\Aa$ be a matrix factor, $\alpha_t = \operatorname{Ad}(e^{itK})$ a flow and $\beta \neq 0$. A state $\omega = \tr(\varrho\,\cdot\,)$ is $(\alpha,\beta)$-KMS if and only if $\varrho = e^{-\beta K}/\tr e^{-\beta K}$. In particular there is exactly one KMS state for each $\beta$, and, for $K$ not a multiple of $1$, the KMS states of the flow form a line parametrised by $\beta$.

## technical
On a matrix factor $\Aa$ with the inner flow $\alpha_t = \operatorname{Ad}(e^{itK})$ and any $\beta \neq 0$, a state $\omega = \tr(\varrho\,\cdot\,)$ satisfies the $(\alpha,\beta)$-KMS condition exactly when $\varrho = e^{-\beta K}/\tr e^{-\beta K}$. Writing the KMS identity $\omega(ab) = \omega(b\,e^{-\beta K}a\,e^{\beta K})$ as traces and using cyclicity shows that $\varrho\,e^{\beta K}$ commutes with every element, so it is central and therefore scalar because the algebra is a factor; normalisation fixes the constant, and the converse is the same computation read backwards.

So for each nonzero $\beta$ there is exactly one KMS state, and, for $K$ not a multiple of $1$, the KMS states of the flow form a single line parametrised by $\beta$.

## lay
In a finite quantum system described by a full matrix algebra, a time evolution generated by an operator K singles out equilibrium states, one for each temperature. This result shows that for each nonzero inverse temperature there is exactly one such state, and it is the familiar Gibbs (Boltzmann) state built from K. Unless K is a multiple of the identity (when every temperature gives the same state), the equilibrium states therefore form a single family labelled by temperature.

## one-liner
On a matrix factor, for each nonzero inverse temperature the only KMS state of an inner flow is the Gibbs state of its generator.
