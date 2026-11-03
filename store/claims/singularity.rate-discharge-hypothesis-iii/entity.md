---
id: singularity.rate-discharge-hypothesis-iii
kind: claim
version: 4
title: The rate, and the discharge of hypothesis (iii)
status: proved
region: singularity
subject: thermality
tags: [hawking-temperature, recovers-known-physics, modular-theory]
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
  - singularity.ascended-marginals-are-diagonal@5
  - singularity.computed@4
  - singularity.descended-form-state-independent@4
  - singularity.modular-structure-completed-pair@5
  - singularity.plane-rate@4
  assumes:
  - singularity.p-univalence@2
  - singularity.r-regularity-fixed-locus@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.20
- kind: check
  ref: check.py::check_gluing_fixes_fermi_dirac_gibbs_marginal
- kind: check
  ref: check.py::check_faithful_marginal_cyclic_separating
- kind: check
  ref: check.py::check_hawking_temperature_from_the_connection
- kind: check
  ref: check.py::check_one_beta_at_every_mode
locators:
  paper: T05
  number: Thm 7.20
  label: thm:rate
  line: 1880
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the gluing condition fixes n = x/(1 + x) uniquely and the marginal is the unique KMS state, the faithful marginal is cyclic and separating by rank, kappa = 1/(4M) from (K.D)K in GTG with beta = 8 pi M and T = 1/(8 pi M), and one beta at every mode for a correlated joint state. Version 3 -> 4.'
  env: theorem
  context_refs:
  - singularity.modular-descent
  typing:
    by: ai-typing-pass
    removed:
    - singularity.q-joint-quasi-freeness-s-wave
    - transport.transport-algorithm
    added:
    - singularity.p-univalence
    - singularity.r-regularity-fixed-locus
    note: 'The theorem assumes (P) and (R) and explicitly no condition on the joint state, so (Q) (cited
      only for the zero-weight remark, and itself citing this theorem) was replaced by the (P) and (R)
      premises; the completed-pair edge is kept although the proof offers a direct alternative for the
      flow action; v2 review: removed the mechanical transport-algorithm edge, since the proof is the
      gluing computation on the mode factor; the standard derivations the paper compares with (Gibbons-Hawking,
      Unruh, Kay-Wald) share only the premise, not this mode-level statement, and none is in the store
      in that form, so no standard route was added. Levels pass: conditions already kept.'
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
---

## formal
Assume (P) and (R). Then at every mode $k$ the marginal is the Gibbs state of $K_k$ at the same inverse temperature,
\[
\beta_k \;=\; \beta \;=\; \frac{2\pi}{\kappa} \;=\; 8\pi M , \qquad T \;=\; \frac{\kappa}{2\pi} \;=\; \frac{1}{8\pi M} \;=\; \TH ,
\]
with occupancy $\omega(v_k^{*}v_k) = (e^{\beta\omega_k} + 1)^{-1} \in (0,1)$. In particular every marginal is faithful, hence cyclic and separating for its mode factor: hypothesis (iii) of Theorem \claimref{singularity.modular-descent} is a consequence of (R), not an assumption; and the temperature is the same at every mode without any condition on the joint state.

## technical
Assume (P) and (R). At each mode the marginal is diagonal in the number basis, $\operatorname{diag}(1 - n, n)$ with $n = \omega(v^*v)$, and the gluing condition of (R) on the ladder pair reduces to $e^{p\omega}n = 1 - n$, so $n = (e^{p\omega} + 1)^{-1}$ with period $p = 2\pi/\kappa$. The marginal is therefore the Gibbs state of $K_k$ at $\beta_k = \beta = 2\pi/\kappa = 8\pi M$, that is $T = \kappa/2\pi = 1/8\pi M = \TH$, with occupancy $\omega(v_k^*v_k) = (e^{\beta\omega_k} + 1)^{-1} \in (0,1)$.

Since the occupancy lies strictly between $0$ and $1$, every marginal is faithful, hence cyclic and separating for its mode factor: the cyclic-and-separating hypothesis of the modular descent theorem is a consequence of (R), not an assumption. The temperature is the same at every mode without any condition on the joint state, because each mode sees the same $\kappa$, which is constant over the bifurcation sphere.

## lay
Two physical premises, one restricting which states are allowed and one requiring smoothness of the geometry at the horizon, force each boundary mode of the black hole into a thermal state. Every mode comes out at the same temperature, the Hawking temperature, without any assumption about correlations between the modes. As a by-product, a condition that previously had to be assumed, that each mode is genuinely entangled with its partner, now follows from the premises.

## one-liner
Under (P) and (R) every mode's marginal is the Gibbs state at the Hawking temperature $T = 1/8\pi M$, so each marginal is faithful and the cyclic-and-separating hypothesis of modular descent is derived rather than assumed.
