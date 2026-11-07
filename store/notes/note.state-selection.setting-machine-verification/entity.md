---
id: note.state-selection.setting-machine-verification
kind: note
version: 3
title: Machine verification
status: setting
subject: descent
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-state-selection, the series'' standard disclaimer'
- name: Claude Opus 5.5
  role: consistency pass, pseudoscalar written I_4
  version: 3
  source: maintainer pass 2026-11-07 (consistency)
comments_on:
- singularity.descent-parity-average
- singularity.descended-form-state-independent
- singularity.ascended-marginals-are-diagonal
- singularity.kms-uniqueness-factor
locators:
  paper: T05-state-selection
  number: Setting
  section: Machine verification
  line: 417
extraction:
  maintainer_pass_consistency:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: "The coverage paragraph wrote the pseudoscalar of Cl(1,3) as a bare I; it is now I_4, the store symbol, a pure notation change."
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: The state-selection note's duplicates of T05 entities were retired to tombstones.yaml (merged into the T05
      entities). References moved from the retired state-selection.ascended-marginals-are-diagonal, state-selection.descended-form-state-independent,
      state-selection.descent-parity-average, state-selection.exact-equilibrium-over-determines-ledger, state-selection.kms-uniqueness-factor,
      state-selection.number-diagonal-dynamics-models-scrambling-derived, state-selection.rate-rigidity-temperature-not-algebra-intrinsic,
      state-selection.universality-temperature to singularity.ascended-marginals-are-diagonal, singularity.descended-form-state-independent,
      singularity.descent-parity-average, singularity.exact-equilibrium-over-determines-boundary-modes, singularity.kms-uniqueness-factor,
      singularity.number-diagonal-dynamics-models-scrambling-derived, singularity.rate-rigidity-temperature-not-algebra-intrinsic,
      singularity.universality-temperature-under-g; version 1 -> 2.
---

## formal
Every computational identity in this note has been checked in exact rational arithmetic, in the manner of the scripts deposited with the series' papers, by \texttt{verify\_state\_selection.py} \cite{ButlerVerifySS}, deposited alongside and using the series' shared library \texttt{GA.py}. Forty-one checks, no floating point, nonzero exit on any failure. Where an exponential occurs it is carried as an exact rational variable, $x = e^{-\beta\omega} \in \mathbb{Q}$, and never evaluated numerically.

Coverage. Theorem \claimref{singularity.descent-parity-average}: the identity $E(x) = \tfrac12(x + \sigma x \sigma)$ on a generic rational matrix; idempotence; the conditional-expectation property $E(axb) = aE(x)b$ for even $a, b$; the range computed as the even span through $E(1) = 1$ and $E(\sigma) = \sigma$; the kernel computed as the odd span through $E(v) = E(v^{*}) = 0$ together with the exhaustive statement that $E$ kills exactly the off-diagonal part; and the hyperbolic atom's CAR with $\sigma = e_0e_1$ blade-exactly in the shared Clifford engine. Theorem \claimref{singularity.descended-form-state-independent}: for a density matrix with nonzero coherences, $E(\rho)$ is diagonal, is a trace-one state, and equals $\operatorname{diag}(1, x)/(1+x)$ at the $x$ the theorem names, with the injectivity of $x \mapsto p$ checked on a rational witness pair. Theorem \claimref{singularity.ascended-marginals-are-diagonal}: an even three-mode state, built as a rational mixture of two even pure states, is verified even by $\Gamma\rho\Gamma = \rho$, has all three single-mode marginals diagonal, and satisfies $\omega(v_k) = \omega(v_k^{*}) = 0$ at every mode; a parity-mixed control has marginal coherence $\tfrac{12}{25}$, so the premise is demonstrably doing work; and the model's pair state of \cite[\S 12]{ButlerT5}, controlled-$Z$ sign included, is verified even with all marginals diagonal. Theorem \claimref{singularity.kms-uniqueness-factor}: the KMS identity checked on all sixteen matrix-unit pairs for $\rho \propto \operatorname{diag}(1, \tfrac{16}{9})$; the converse checked by exhibiting a matrix-unit pair at which the tracial state fails it; and the commutation $[\rho, e^{\beta H}] = 0$ that the identity forces. Corollary \claimref{singularity.universality-temperature-under-g}: with weights $(1,2)$, equal inverse temperatures are the exact rational condition $x_2 = x_1^{2}$, the joint populations of the two-mode product are those of a single Gibbs state of $K_{\mathrm{geo}}$ exactly then, a witness pair is exhibited for which the condition fails, and the GMC state is verified to factorise. Theorem \claimref{singularity.rate-rigidity-temperature-not-algebra-intrinsic}: the diagonal unitary commutes with $K$ and fixes the Gibbs state exactly; the exchange unitary satisfies $XKX = -K$ and carries the $\beta$-Gibbs state to the $(-\beta)$ one; and the exchange is verified not to commute with $K$, so it is outside the flow-preserving group. Proposition \claimref{state-selection.euclidean-partner-curvature-selected}: $\sigma_r^{2} = +1$ and $(I_{4}\sigma_r)^{2} = -1$ blade-exactly in $\Cl(1,3)$; both members of the pair are shape-operator eigenvectors of eigenvalue $-2$; the rotor composition law $R(\tfrac35,\tfrac45)^{2} = R(-\tfrac{7}{25},\tfrac{24}{25})$; $R_{2\pi} = -1$ and $R_{4\pi} = +1$ obtained by squaring the quarter rotor; and the triviality of conjugation by $-1$ on a generic multivector. Theorem \claimref{singularity.exact-equilibrium-over-determines-boundary-modes}: the two-mode Gibbs product is a fixed point of $\EN$ and equals the tensor product of its own marginals, against an entangled even control that fails both and whose purity strictly drops under descent. Theorem \claimref{state-selection.partner-purification-are-canonical}: the thermofield vector purifies $\operatorname{diag}(\tfrac{9}{25}, \tfrac{16}{25})$; the angle satisfies $\tan^{2}\theta = \tfrac{16}{9} = e^{-\omega/T}$; the modular operator of \cite[Lem.~7.1]{ButlerT5} is recomputed as $\rho \otimes \bar\rho^{-1}$; and a unitary on the purifying factor alone leaves the marginal unchanged while changing the global vector. Proposition \claimref{singularity.number-diagonal-dynamics-models-scrambling-derived}: a controlled-$Z$ circuit on the model's four-mode ledger preserves every joint-number probability and every single-mode marginal, commutes with the total parity, and does change the joint coherence, so it writes exactly where the descent cannot read; while an orthogonal, parity-preserving hopping rotation between two modes changes the marginal populations, exhibiting exactly what (L$_E$) excludes.

## technical
pending

## lay
pending

## one-liner
pending
