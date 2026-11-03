---
id: singularity.eviction-window-thermal-product-radiation-entropy
kind: claim
version: 7
title: 'Eviction: the window is a thermal product, and the radiation entropy is its content'
status: proved
region: singularity
subject: entropy
tags: [radiation-spectrum, boundary-modes]
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
  - singularity.no-attic-derived-model@6
  assumes:
  - singularity.rate-models-kinematic-inputs-l-u@2
  - singularity.l-boundary-mode-locality@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:11.5
- kind: check
  ref: check.py::check_window_is_thermal_product
- kind: check
  ref: check.py::check_envelope_endpoint_and_rising_branch
- kind: check
  ref: check.py::check_falling_branch_and_idealisation
locators:
  paper: T05
  number: Thm 11.5
  label: thm:eviction
  line: 2263
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: on three exact rate-model runs: the thermal product window, envelope, endpoint, rising branch, falling-branch identity and the idealisation S_R = min(S_th, C). Version 5 -> 6. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 6 -> 7.'
  env: theorem
  context_refs:
  - singularity.no-attic-derived-model
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    added:
    - singularity.no-attic-derived-model
    - singularity.rate-models-kinematic-inputs-l-u
    - singularity.l-boundary-mode-locality
    note: 'Removed the transport-algorithm repair edge (framing); added the no-attic proposition, which
      the hypothesis line says supplies the no-attic property, and the (L), (U), (C), (I) and (L_E) postulates
      the statement assumes. Levels pass: lay now lists the postulates (L), (U), (C), (I), (L_E) and the
      setting conditions.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - singularity.no-attic-derived-model
    - singularity.rate-models-kinematic-inputs-l-u
---

## formal
Under (L), (U), (C), (I) and (L$_E$), the window dynamics diagonal in the joint number basis and the radiation quanta free and never returning, with the no-attic property supplied by Proposition \claimref{singularity.no-attic-derived-model}, write $W(t)$ for the set of pairs whose window half is in the window at stage $t$ and $C(t) = |W(t)|\ln 2$ for the capacity. Then, in the rate model:
\begin{enumerate}
\item (The identity.) At every stage the window state is the product of its members' thermal marginals, $\rho_L = \bigotimes_{k \in W(t)}\operatorname{diag}(c_k^{2}, s_k^{2})$, and consequently
\[
S_R(t) \;=\; S_L(t) \;=\; \sum_{k \in W(t)} h_k \qquad \text{exactly.}
\]
\item (Envelope and endpoint.) $S_R(t) \leq \min(\Sth(t), C(t))$ at every stage, and $S_R = 0$ at complete evaporation.
\item (Rising branch, exact.) While no eviction has occurred, $W(t)$ is the set of all injected pairs and $S_R(t) = \Sth(t)$ exactly.
\item (Falling branch, quantified.) $S_R(t) = C(t) - \sum_{k \in W(t)}(\ln 2 - h_k)$: the radiation entropy lies below the capacity by exactly the sum of the window members' per-quantum shortfalls, with equality $S_R = C$ if and only if every window member is maximally entangled. In the maximally entangled idealisation, every $h_k = \ln 2$, this gives $S_R(t) = \min(\Sth(t), C(t))$ exactly at every stage.
\end{enumerate}

## technical
Under the rate-model inputs (L), (U), (C), (I) and (L$_E$), with number-diagonal window dynamics, free radiation quanta that never return, and the no-attic property, let $W(t)$ be the set of pairs whose window half is still in the window and $C(t) = |W(t)|\ln 2$. Then the window state is the product of its members' thermal marginals, and $S_R(t) = S_L(t) = \sum_{k \in W(t)} h_k$ exactly.

Consequently $S_R \leq \min(\Sth, C)$ with $S_R = 0$ at complete evaporation; $S_R = \Sth$ exactly before any eviction; and $S_R = C - \sum_{k \in W(t)}(\ln 2 - h_k)$, with $S_R = C$ exactly when every window member is maximally entangled.

## lay
In the framework's rate model, on its stated postulates (two sectors, global purity, a fixed window capacity, fresh thermal injection and boundary-mode locality), with internal dynamics that only changes phases and emitted quanta that never return, a black hole emits quanta that are each entangled with a partner mode kept inside, and partners are later pushed out as the hole shrinks. This result shows the inside state is always a simple product of thermal pieces, so the radiation's entropy is just the sum of the entropies of the partners still inside. That gives a rising branch, a ceiling set by the shrinking capacity, and zero entropy at the end.

## one-liner
In the rate model under (L), (U), (C), (I) and (L$_E$), the window is a product of thermal marginals and $S_R(t) = \sum_{k \in W(t)} h_k$ exactly.
