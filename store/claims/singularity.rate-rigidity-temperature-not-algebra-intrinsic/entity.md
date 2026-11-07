---
id: singularity.rate-rigidity-temperature-not-algebra-intrinsic
kind: claim
version: 5
title: 'Rate rigidity: the temperature is not algebra intrinsic'
status: proved
region: singularity
subject: thermality
tags: [undetermined-input, hawking-temperature, modular-theory]
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
  uses:
  - singularity.kms-uniqueness-factor@4
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.16
- kind: check
  ref: check.py::check_commuting_automorphisms_fix_gibbs
- kind: check
  ref: check.py::check_reversing_automorphisms_flip_beta
- kind: check
  ref: check.py::check_reparametrisation_rescales_beta
- kind: check
  ref: check.py::check_only_orientation_flip_intertwines
locators:
  paper: T05
  number: Thm 7.16
  label: thm:rigidity
  line: 1830
outside_ga:
  kind: complex-analysis
  why: 'the phase flow Ad(e^{itK}) acts on the complex single-mode matrix factor of the atom, whose modes anticommute with I_4 (conventions, known limit 1); the proof also uses complex determinants of e^{itK}'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the phase flow Ad(e^{itK}) acts on the complex single-mode matrix factor of the atom, whose modes anticommute with I_4 (conventions, known limit 1); the proof also uses complex determinants of e^{itK}.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: intertwiners of the boost flow on Mat_2(C) exist only for c = +-1 (commuting: diagonal, fixing Gibbs; reversing: anti-diagonal, beta -> -beta), and the KMS solution rescales under reparametrisation. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: theorem
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: 'Kept the KMS-uniqueness edge, used in clauses (3) and (4); v2 review: removed the mechanical
      transport-algorithm edge, since the proof is matrix-factor algebra. Levels pass: the lay level now
      restricts the claim to automorphisms that intertwine the flow (commute with or reverse it), as the
      formal does, instead of all symmetries of the algebra.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
  flow_note: phase flow e^{-i omega t} on the modes (T05 Thm 7.16, T07 Def 2.7), the Euclidean rotation
    of T05 Prop 7.21. The theorem defines alpha_t = Ad(e^{itK}), a unitary group with imaginary adjoint
    eigenvalues, and its KMS states; this is the flow T05 Prop 7.21 calls the boost rotor continued to imaginary
    rapidity.
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 4
    note: 'The two boost flows: flow_note recorded; one-liner, technical now name the flow.'
  merged_from:
  - id: state-selection.rate-rigidity-temperature-not-algebra-intrinsic
    version: 2
    locators:
      paper: T05-state-selection
      number: Thm 4.5
      label: thm:rigidity
      line: 243
    uses:
    - state-selection.kms-uniqueness-factor@1
    checked_by: verify_state_selection.py num:4.5
    proof_files:
    - proof-main.tex (kept here as merged-state-selection.rate-rigidity-temperature-not-algebra-intrinsic-proof-main.tex)
    formal: 'Let $\theta$ be a $*$-automorphism of the single-mode algebra $\Aa$.

      \begin{enumerate}

      \item If $\theta$ commutes with the boost''s phase flow $\alpha_t = \operatorname{Ad}(e^{itK})$, $\theta \circ
      \alpha_t = \alpha_t \circ \theta$ for all $t$, then $\theta$ fixes every Gibbs state of $K$: $\omega_\beta \circ
      \theta = \omega_\beta$ for every $\beta$.

      \item If $\theta$ reverses the flow, $\theta \circ \alpha_t = \alpha_{-t}\circ\theta$, then $\omega_\beta \circ
      \theta = \omega_{-\beta}$.

      \item Consequently no automorphism of $\Aa$ carries the $\beta$-KMS state of the phase flow to the $\beta''$-KMS
      state for $|\beta''| \neq |\beta|$, and $|\beta|$ is an invariant of the pair (state, flow). No condition formulated
      in the algebra and its flow alone can fix the value of $\beta$.

      \end{enumerate}'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Merged the state-selection note''s Thm 4.5 (state-selection.rate-rigidity-temperature-not-algebra-intrinsic,
      retired to tombstones.yaml) into this entity: T05''s statement is the note''s clauses (1) and (2) with a reparametrisation
      clause; the note''s clause (3), quantified over all automorphisms, is not carried. Kept this statement, levels
      and checks; the note''s entity is recorded above and its proof files are kept in this folder. References to
      the note''s id were repointed here. Extraction-only change, so the version and the dependants'' pins are unchanged.'
---

## formal
Let $\alpha_t = \operatorname{Ad}(e^{itK})$ be the boost flow of the single-mode algebra $\Aa$, let $\theta$ be a $*$-automorphism of $\Aa$, and let $\omega_\beta$ denote the $\beta$-KMS state of $\alpha$.
\begin{enumerate}
\item If $\theta$ commutes with the flow then it fixes every Gibbs state of $K$: $\omega_\beta \circ \theta = \omega_\beta$ for every $\beta$.
\item If $\theta$ reverses the flow, $\theta\circ\alpha_t = \alpha_{-t}\circ\theta$, then $\omega_\beta\circ\theta = \omega_{-\beta}$.
\item Under a constant reparametrisation of the flow, $\alpha_t \mapsto \alpha_{ct}$ with $c > 0$, the $\beta$-KMS state of $\alpha$ is the $(\beta/c)$-KMS state of the reparametrised flow: $\omega_\beta$ is unchanged and its inverse temperature is rescaled.
\item Hence no automorphism intertwining the flow carries $\omega_\beta$ to $\omega_{\beta'}$ for $|\beta'| \neq |\beta|$: $|\beta|$ is an invariant of the pair (state, parametrised flow), and the automorphism group acts on the line of KMS states with orbits $\{\beta, -\beta\}$, so that line carries no automorphism-theoretic structure beyond the orientation flip of (2). A condition that singles out one point of the line is therefore either a stipulation of the state itself or a reference to data outside the pair $(\Aa, \alpha)$; by (3), the value of $|\beta|$ is meaningful only relative to a parametrisation of the flow, and it is that parametrisation, the conversion of the flow parameter into geometric time, that the algebra does not supply.
\end{enumerate}

## technical
Let $\alpha_t = \operatorname{Ad}(e^{itK})$ be the boost's phase flow on the single-mode algebra $\Aa$, the rotor flow $\exp(\lambda\sigma/2)$ continued to imaginary rapidity, with $\beta$-KMS states $\omega_\beta$; every automorphism of this matrix factor is inner, $\theta = \operatorname{Ad}(U)$. An automorphism commuting with the flow fixes every $\omega_\beta$; one reversing the flow sends $\omega_\beta$ to $\omega_{-\beta}$; and a constant reparametrisation $\alpha_t \mapsto \alpha_{ct}$ with $c > 0$ leaves $\omega_\beta$ unchanged while rescaling its inverse temperature to $\beta/c$.

Hence automorphisms intertwining the flow act on the line of KMS states with orbits $\{\beta, -\beta\}$: $|\beta|$ is an invariant of the pair (state, parametrised flow), and the line carries no automorphism-theoretic structure beyond the orientation flip. A condition singling out one point of the line must either stipulate the state or refer to data outside $(\Aa, \alpha)$, and the value of $|\beta|$ is meaningful only relative to a parametrisation of the flow, which the algebra does not supply.

## lay
For a single quantum mode with a given time evolution, the symmetries of the algebra that respect the time evolution, or reverse it, can at most flip the sign of an equilibrium state's inverse temperature; they never change its size. Rescaling the clock rescales the temperature while leaving the state itself alone. So the algebra on its own cannot pick out a particular temperature: that needs outside information, namely how the evolution's parameter is converted into physical time.

## one-liner
Automorphisms of the single-mode algebra that intertwine the boost's phase flow $\operatorname{Ad}(e^{itK})$ move its KMS states only by $\beta \mapsto \pm\beta$, so the value of the temperature depends on a parametrisation of the flow that the algebra does not supply.
