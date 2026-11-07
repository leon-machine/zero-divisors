---
id: singularity.descent-parity-average
kind: claim
version: 5
title: The descent is the parity average
status: proved
region: singularity
subject: descent
tags: [descent-map, grading-and-parity]
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
  role: 'GA rewrite (the matrix conjugation replaced by the CAR computation)'
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.singularity.grading-parity-automorphism
derivations:
- name: main
  uses:
  - singularity.descent-what-it-erases@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:5.7
- kind: check
  ref: check.py::check_descent_is_parity_average
- kind: check
  ref: check.py::check_range_kernel_and_uniqueness
- kind: check
  ref: check.py::check_preserves_alpha_invariant_states
locators:
  paper: T05
  number: Thm 5.7
  label: thm:parityavg
  line: 1583
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 4 -> 5. The proof computes alpha(x) = sigma x sigma from the CAR on x = a vv* + b v + c v* + d v*v (sigma = v*v - vv* commutes with vv*, v*v and anticommutes with v, v*) in place of the 2 x 2 matrix product, which stays as a labelled reading. Verified exactly with lib/GA.py in Cl(1,1) (sigma = e0e1 there). The stored copies of the merged entity''s proofs are kept unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: E = (x + sigma x sigma)/2 on all matrix units, range and kernel, uniqueness of the conditional expectation by solving the bimodule constraints, and preservation of alpha-invariant states. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - obj.singularity.grading-parity-automorphism
    note: 'the proof identifies the parity average with the value of the descent computed in the earlier
      proposition, so that edge is a real premise; added the grading definition to about, since the statement
      is about its parity automorphism and even part; removed the mechanical repair edge to the transport
      algorithm: the section frames its results as a step of that algorithm, but the proof is a self-contained
      computation and does not use it as a premise Levels pass: conditions already kept; the W503 warning
      on the lay level is a false positive, triggered by the phrase "conditional expectation" in the formal,
      which names an operator rather than a condition.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  merged_from:
  - id: state-selection.descent-parity-average
    version: 3
    locators:
      paper: T05-state-selection
      number: Thm 2.2
      label: thm:parity
      line: 135
    about:
    - obj.state-selection.grading-parity-automorphism
    uses:
    - singularity.descent-what-it-erases@5
    checked_by: verify_state_selection.py num:2.2
    proof_files:
    - orig-proof-main.tex (kept here as merged-state-selection.descent-parity-average-orig-proof-main.tex)
    - proof-main.tex (kept here as merged-state-selection.descent-parity-average-proof-main.tex)
    formal: 'For every $x \in \Aa$,

      \[

      E(x) \;=\; \tfrac12\bigl(x + \alpha(x)\bigr) .

      \]

      Consequently: $E$ is the group average over the two-element group $\{\id, \alpha\}$, hence the unique conditional
      expectation of $\Aa$ onto its fixed-point algebra $\Aev$; its range is $\Aev$ and its kernel is exactly $\Aod$,
      the adjoined ladder sector; and $E$ preserves every state that is even, that is every $\omega$ with $\omega
      \circ \alpha = \omega$.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Thm 2.2 (state-selection.descent-parity-average, retired to tombstones.yaml)
      into this entity: the same theorem (T05 adds the sigma-times-sigma form). Kept this statement, levels and checks;
      the note''s entity is recorded above and its proof files are kept in this folder. References to the note''s
      id were repointed here. Extraction-only change, so the version and the dependants'' pins are unchanged.'
---

## formal
For every $x \in \Aa$,
\[
E(x) \;=\; \tfrac12\bigl(x + \alpha(x)\bigr) \;=\; \tfrac12\bigl(x + \sigma x \sigma\bigr) .
\]
Consequently $E$ is the group average over $\{\id, \alpha\}$, hence the unique conditional expectation of $\Aa$ onto its fixed-point algebra $\Aev$; its range is $\Aev$ and its kernel is exactly $\Aod$, the adjoined ladder sector; and $E$ preserves every state $\omega$ with $\omega \circ \alpha = \omega$.

## technical
On the single-mode algebra $\Aa$ the descent equals the parity average: $E(x) = \tfrac12\bigl(x + \alpha(x)\bigr) = \tfrac12(x + \sigma x \sigma)$. Hence $E$ is the group average over $\{\id, \alpha\}$ and the unique conditional expectation of $\Aa$ onto its fixed-point algebra $\Aev$.

Its range is $\Aev$, its kernel is exactly the adjoined ladder sector $\Aod$, and it preserves every state with $\omega \circ \alpha = \omega$.

## lay
The descent, which keeps a mode's occupation data and discards its coherences, is the same thing as averaging over fermion parity: take an observable and its parity-flipped version and average the two. This makes it the only consistent projection onto the parity-even observables, and it leaves every parity-even state unchanged.

## one-liner
The descent is the parity average $E(x) = \tfrac12\bigl(x + \alpha(x)\bigr)$, the unique conditional expectation onto the even subalgebra, with kernel the odd ladder sector.
