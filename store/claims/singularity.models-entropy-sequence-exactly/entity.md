---
id: singularity.models-entropy-sequence-exactly
kind: claim
version: 4
title: The model's entropy sequence, exactly
status: proved
region: singularity
subject: entropy
tags: [finite-models, radiation-spectrum]
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
  - singularity.parity-protection@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:12.4
- kind: check
  ref: check.py::check_window_product_and_entropy_identity
- kind: check
  ref: check.py::check_phase_one_two_and_completion
locators:
  paper: T05
  number: Prop 12.4
  label: prop:modelentropy
  line: 2395
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the model run''s window product, entropy identity, purity sequence, Phase I equality, strict Phase II bound and completion. Version 1 -> 2. check_window_product_and_entropy_identity: S_R = S_L now tested as equality of the nonzero spectra of rho_R and rho_L (explicit orthogonal eigenvectors of rho_R) at all six stages, replacing the m = 2, 3 trace-moment comparison at <= 6 radiation qubits; docstring reworded. Version 2 -> 3. Check maintenance: dict.setdefault in the check replaced by pyutil.get_or_set (same behaviour, and the same in the browser engine); no change to what is claimed. Version 3 -> 4.'
  env: proposition
  context_refs:
  - singularity.eviction-window-thermal-product-radiation-entropy
  typing:
    by: ai-typing-pass
    note: Kept parity protection (the support constraint drives the proof); the eviction theorem is specialised
      in the statement but the proof recomputes it in the model, so it was not added.
---

## formal
In the run of Table \ref{tab:model}, Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}(1) reads as follows: at every stage the window state $\rho_L$ is diagonal in the number basis, with the product distribution of its current members, so that, with $W(t)$ the set of pairs whose window half is still in the window,
\[
S_R(t) \;=\; S_L(t) \;=\; \sum_{k \in W(t)} H(c_k^{2}) \qquad \text{exactly, and} \qquad \tr\rho_R(t)^{2} \;=\; \prod_{k \in W(t)}\bigl(c_k^{4} + s_k^{4}\bigr) .
\]
Consequently $S_R = \Sth$ exactly through Phase I; in Phase II, $S_R \leq C$ with equality if and only if every window member is maximally entangled, so that with the model's pairs the inequality is strict at every Phase II stage with a nonempty window; and $S_R = 0$ at completion. The model therefore realises the envelope, the exact rising branch and the endpoint of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}, and exhibits the falling branch's departure from exact saturation, not its saturation.

## technical
In the finite model's run, at every stage the window state $\rho_L$ is diagonal in the number basis with the product distribution of its current members. Hence $S_R(t) = S_L(t) = \sum_{k \in W(t)} H(c_k^2)$ and $\tr\rho_R(t)^2 = \prod_{k \in W(t)}(c_k^4 + s_k^4)$ exactly.

So $S_R = \Sth$ exactly through the first phase; in the second phase $S_R \leq C$, strictly at every stage with a nonempty window since the model's pairs are not maximally entangled; and $S_R = 0$ at completion.

## lay
In the explicit small model of evaporation, the entropy of the radiation can be computed exactly at every step. It equals the thermal value while the window fills, stays strictly below the capacity as the hole shrinks, and returns to zero at the end. The model thus shows the general bounds at work, but not the idealised case in which the capacity is reached exactly.

## one-liner
In the finite model $S_R(t) = \sum_{k \in W(t)} H(c_k^2)$ exactly at every stage: equal to $\Sth$ at first, strictly below capacity later, and zero at completion.
