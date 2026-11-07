---
id: hawking.modular-structure-completed-pair
kind: claim
version: 4
title: Modular structure of the completed pair
status: proved
region: hawking
subject: descent
tags: [modular-theory, hyperbolic-plane, rotors-and-stabilisers]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 4
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - std-algebra.vector-squares@1
  - std-algebra.bivector-exponential@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T07.py
  tags:
  - label:prop:mode
- kind: check
  ref: check.py::check_sigma_square_and_boost_bivector
- kind: check
  ref: check.py::check_boost_weights_and_rotor_flow
- kind: check
  ref: check.py::check_projectors_and_fock_number
- kind: check
  ref: check.py::check_unique_flow_up_to_reparametrisation
locators:
  paper: T07
  number: Prop 2.1
  label: prop:mode
  line: 393
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 3 -> 4. Decision item E6 (routine; no retirement): equivalent_to singularity.modular-structure-completed-pair@5 added. The same result as the singularity entity, kept as the home since it carries the rotor-group caveat.'
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.vector-squares, std-algebra.bivector-exponential where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: sigma^2 = 1 and sigma = e0 e1, opposite boost weights under the rotor flow, the occupation projectors, sigma/2 = N - 1/2, and the one-dimensional bivector space with reparametrised flows. Version 1 -> 2.'
  env: proposition
  unresolved_refs:
  - rem:frontier
  typing:
    by: ai-typing-pass
    note: proved outright with no premises (the paper says the single-mode modular structure is elementary
      and proved here); the unresolved reference to the frontier remark is context only.
  flow_note: 'rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2). T07 restates T05 Thm 6.3: the flow
    is R_lambda = exp(lambda sigma/2), scaling the pair with real weights, unique among rotor flows up to
    reparametrisation and orientation.'
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded.'
equivalent_to:
- singularity.modular-structure-completed-pair@5
---

## formal
Let $(v, v^*)$ be a completed pair and $\sigma := v^*v - vv^*$. Then:
\begin{enumerate}
\item $\sigma^2 = 1$; in the hyperbolic atom $\Cl(1,1)$ with $v = \tfrac12(e_0 + e_1)$, $v^* = \tfrac12(e_0 - e_1)$, one has $\sigma = e_0 e_1$: the unit boost bivector of the plane (relabelling the pair reverses the orientation);
\item the rotor flow $R_\lambda := \exp(\lambda\sigma/2)$ acts by $R_\lambda\, v\, R_\lambda^{-1} = e^{-\lambda}v$ and $R_\lambda\, v^*\, R_\lambda^{-1} = e^{+\lambda}v^*$: the pair diagonalises the boost with opposite weights;
\item the spectral projectors $\tfrac12(1 \pm \sigma)$ are the occupation projectors $v^*v$ and $vv^*$;
\item in the Fock representation the boost generator is the shifted number operator, $\tfrac12\sigma = N - \tfrac12$;
\item the bivector space of $\Cl(1,1)$ is one-dimensional, so the boost flow is the unique one-parameter rotor flow of the atom \emph{up to reparametrisation of the flow parameter and orientation}: the algebra fixes the orbits of any rotor-implemented modular flow, but not its speed, which is exactly the normalisation Remark \ref{rem:frontier} (Section \ref{sec:state}) leaves open.
\end{enumerate}

## technical
For a completed pair $(v, v^{*})$ of null vectors with $vv^{*} + v^{*}v = 1$, set $\sigma = v^{*}v - vv^{*}$. Then $\sigma^{2} = 1$, and in the hyperbolic atom $\Cl(1,1)$ with $v = \tfrac12(e_{0} + e_{1})$ and $v^{*} = \tfrac12(e_{0} - e_{1})$ it is the unit boost bivector $e_{0}e_{1}$. The rotor flow $R_{\lambda} = \exp(\lambda\sigma/2)$ scales $v$ by $e^{-\lambda}$ and $v^{*}$ by $e^{+\lambda}$, the spectral projectors $\tfrac12(1\pm\sigma)$ are the occupation projectors $v^{*}v$ and $vv^{*}$, and in the Fock representation $\tfrac12\sigma = N - \tfrac12$.

Since the bivector space of $\Cl(1,1)$ is one-dimensional, the boost flow is the unique one-parameter rotor flow of the atom up to reparametrisation of the flow parameter and orientation: the algebra fixes the orbits of a rotor-implemented modular flow, but not its speed.

## lay
A single fermionic mode, built from a pair of null directions, carries a natural boost: a flow that stretches one direction and shrinks the other. The two halves of this boost are exactly the empty and occupied states of the mode, and its generator is the particle number shifted by one half. The algebra fixes which flow this is but not how fast it runs, which is the temperature question left open.

## one-liner
The completed pair's bivector $\sigma = v^{*}v - vv^{*}$ is a unit boost whose rotor flow scales the pair with opposite weights, whose spectral projectors are the occupation projectors, and which is unique up to reparametrisation and orientation.
