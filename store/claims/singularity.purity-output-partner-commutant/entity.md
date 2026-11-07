---
id: singularity.purity-output-partner-commutant
kind: claim
version: 4
title: 'Purity is an output: the partner is the commutant'
status: proved
region: singularity
subject: descent
tags: [modular-theory, entanglement]
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
  - singularity.modular-theory-matrix-factor-proved-outright@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:7.27
- kind: check
  ref: check.py::check_gns_vector_cyclic_separating
- kind: check
  ref: check.py::check_commutant_is_partner_copy_and_J_conjugate
- kind: check
  ref: check.py::check_purifications_differ_by_partner_unitary
- kind: check
  ref: check.py::check_gibbs_gives_thermofield_double
locators:
  paper: T05
  number: Thm 7.27
  label: thm:gns
  line: 1948
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the GNS vector cyclic and separating, the commutant computed as 1 (x) Mat_2 = J pi(A) J, purifications differing by a partner unitary, and the thermofield double at the Gibbs state. Version 2 -> 3. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  env: theorem
  context_refs:
  - singularity.modular-descent
  - singularity.schmidt-forcing-proved-outright
  typing:
    by: ai-typing-pass
    removed:
    - transport.transport-algorithm
    note: Removed the mechanical transport-algorithm edge because the proof is the matrix-factor modular lemma plus a Schmidt-coefficient argument; did not add the Schmidt-forcing lemma or the modular descent theorem, which the statement compares with but the proof does not use.
  repair:
    added:
    - transport.transport-algorithm
    instantiates: 'T05 states (its algorithm table) that this section executes a step of the T1 transport
      algorithm from Step 3 on: apply the rule, compute in the completion, descend, iterate'
---

## formal
Let $\omega$ be a faithful state on the mode factor with $\varrho = \operatorname{diag}(\lambda_0^{2}, \lambda_1^{2})$, $\lambda_i > 0$. In its GNS representation: the space is $\C^{2}\otimes\C^{2}$ and the cyclic vector is $\Omega = \sum_i \lambda_i|ii\rangle$, cyclic and separating for $\pi(\Aa) = \Aa\otimes 1$; the commutant $\pi(\Aa)' = 1 \otimes \Aa$ is the partner copy and equals $J\pi(\Aa)J$; any two purifications of $\omega$ differ by a unitary on the purifying factor alone; and when $\omega$ is the Gibbs state at $\beta$, $\Omega$ is the thermofield double with $\tan\theta = e^{-\omega_k/2T}$, which is exactly the vector Lemma \claimref{singularity.schmidt-forcing-proved-outright} produces. Hypothesis (i) of Theorem \claimref{singularity.modular-descent}, the existence of the partner, and the thermofield form are therefore consequences of the one-sided state rather than independent choices.

## technical
Let $\omega$ be a faithful state on the mode factor with $\varrho = \operatorname{diag}(\lambda_0^2, \lambda_1^2)$, $\lambda_i > 0$. Its GNS representation lives on $\C^2 \otimes \C^2$ with cyclic vector $\Omega = \sum_i \lambda_i |ii\rangle$, cyclic and separating for $\pi(\Aa) = \Aa \otimes 1$; the commutant $\pi(\Aa)' = 1 \otimes \Aa = J\pi(\Aa)J$ is the partner copy, and any two purifications of $\omega$ differ by a unitary on the purifying factor alone.

When $\omega$ is the Gibbs state at inverse temperature $\beta$, $\Omega$ is the thermofield double with $\tan\theta = \lambda_1/\lambda_0 = e^{-\omega_k/2T}$, the same vector the Schmidt-forcing argument produces. So purity of the doubled state, the existence of the partner and the thermofield form are consequences of the one-sided state rather than independent choices.

## lay
Starting from a single quantum mode in a mixed state, there is a standard construction that builds a larger system in which that state is one half of a pure entangled state. This result shows that the partner needed for the pure state is not an extra ingredient: it emerges automatically as the mirror copy of the mode's own algebra, and the construction is unique up to changes made on the partner side alone. For a thermal state the resulting pure state is the familiar thermofield double.

## one-liner
For a faithful single-mode state the GNS construction supplies the partner as the commutant and, for a Gibbs state, the thermofield double, so purity and the partner are outputs of the one-sided state.
