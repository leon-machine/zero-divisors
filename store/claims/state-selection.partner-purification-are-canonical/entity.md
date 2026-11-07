---
id: state-selection.partner-purification-are-canonical
kind: claim
version: 5
title: The partner and the purification are canonical
status: proved
region: state-selection
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
  source: 'authorship disclosure of T05-state-selection, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: consistency pass, scalars of the mode factor and the meaning of J stated
  version: 5
  source: maintainer pass 2026-11-07 (consistency)
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 5
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - singularity.modular-theory-matrix-factor-proved-outright@6
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_state_selection.py
  tags:
  - num:7.1
- kind: check
  ref: check.py::check_gns_vector_cyclic_and_separating
- kind: check
  ref: check.py::check_commutant_is_partner_copy_via_modular_conjugation
- kind: check
  ref: check.py::check_purifications_differ_by_partner_unitary
- kind: check
  ref: check.py::check_gibbs_state_gives_thermofield_double
locators:
  paper: T05-state-selection
  number: Thm 6.1
  label: thm:gns
  line: 314
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version kept at 5 (already raised in this run). Decision item E6 (routine; no retirement): equivalent_to singularity.purity-output-partner-commutant@5 added. The same result as the singularity entity, which is kept as the home.'
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: "The formal level now says that the scalars of the mode factor are span{1, e2e3}, the radial atom's complex unit (unit principle U2), and that J here is the modular conjugation, not that unit; no mathematical change."
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: GNS vector cyclic and separating, the commutant computed as a kernel and equal to J pi(A) J, Tomita''s S = J Delta^{1/2}, purifications related by a partner unitary, and the thermofield double for Gibbs states (Pythagorean samples). Version 2 -> 3. Legacy tag corrected (2026-10-23): num:6.1 -> num:7.1, the purification block [Thm 7.1] of verify_state_selection.py. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  typing:
    by: ai-typing-pass
    removed:
    - singularity.schmidt-forcing-proved-outright
    note: Removed the Schmidt-forcing lemma because clause (4) only compares the GNS vector with the state that lemma produces and the proof does not use it; the GNS, Tomita and thermofield-double results are standard but no imported claim for them exists in the store, so no standard route was added.
  env: theorem
equivalent_to:
- singularity.purity-output-partner-commutant@5
---

## formal
Let $\omega$ be a faithful state on the mode factor $\Aa \cong \Mat_2(\C)$ (scalars $\mathrm{span}\{1, e_{2}e_{3}\}$, the complex unit of the radial atom, \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}; below, $J$ is the modular conjugation of Lemma \claimref{singularity.modular-theory-matrix-factor-proved-outright}, not that unit), with density matrix $\rho = \operatorname{diag}(\lambda_0^{2}, \lambda_1^{2})$, $\lambda_i > 0$. Then in the GNS representation of $\omega$:
\begin{enumerate}
\item the representation space is $\C^{2}\otimes\C^{2}$, the cyclic vector is $\Omega = \sum_i \lambda_i |ii\rangle$, and $\Omega$ is cyclic and separating for $\pi(\Aa) = \Aa \otimes 1$;
\item the commutant $\pi(\Aa)' = 1 \otimes \Aa$ is the partner copy, and is generated from $\pi(\Aa)$ by the modular conjugation, $\pi(\Aa)' = J\pi(\Aa)J$;
\item any two purifications of $\omega$ are related by a unitary acting on the purifying factor alone, so $\Omega$ is unique up to a unitary in the commutant;
\item when $\omega$ is the Gibbs state at $\beta$, $\Omega$ is the thermofield double, $\lambda_0 = \cos\theta$, $\lambda_1 = \sin\theta$ with $\tan\theta = e^{-\omega_k/2T}$, which is exactly the state produced by \cite[Lem.~7.2]{ButlerT5}.
\end{enumerate}
Consequently the global purity of hypothesis (i), the existence of the partner, and the thermofield form of the global state are consequences of the one-sided state, not independent choices; and the ``two ends of the pair'' of Step 4d are the algebra and its commutant in the state's own GNS representation.

## technical
For a faithful state $\omega$ on $\Aa \cong \Mat_2(\C)$ with $\rho = \operatorname{diag}(\lambda_0^{2}, \lambda_1^{2})$, the GNS representation is $\C^2 \otimes \C^2$ with vector $\Omega = \sum_i \lambda_i |ii\rangle$, cyclic and separating for $\pi(\Aa) = \Aa \otimes 1$. The commutant $1 \otimes \Aa = J\pi(\Aa)J$ is the partner copy, and any two purifications of $\omega$ differ by a unitary on the purifying factor, so $\Omega$ is unique up to a unitary in the commutant.

For the Gibbs state, $\lambda_0 = \cos\theta$ and $\lambda_1 = \sin\theta$ with $\tan\theta = e^{-\omega_k/2T}$, so $\Omega$ is the thermofield double. Global purity, the partner and the thermofield form are thus consequences of the one-sided state, and the two ends of the pair are the algebra and its commutant in the state's own GNS representation.

## lay
Given only the state of one mode, a standard construction builds a larger pure state in which that mode is entangled with a partner. The partner turns out to be the mirror image of the mode's own algebra, and the construction is unique up to changes made on the partner side. For a thermal mode the result is the thermofield double, so purity and the partner do not have to be assumed separately.

## one-liner
The GNS construction of a faithful single-mode state supplies the partner as the commutant and, for a Gibbs state, the thermofield double, unique up to a unitary on the partner.
