---
id: synthesis.de-sitter-temperature-mirror-and-status
kind: claim
version: 3
title: The cosmological horizon's temperature in the mirror, and its status
status: proved
region: synthesis
subject: thermality
tags: [hawking-temperature, mirror-sector, frozen-point, undetermined-input, needs-continuum]
proposed_by:
  kind: ai
  session: de-sitter-temperature-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.cosmological-horizon-boundary-modes
derivations:
- name: main
  uses:
  - synthesis.de-sitter-temperature-frozen-point-norm@5
  - synthesis.cosmological-horizon-completed-pair@3
  - odd-extensions.two-towers-one-curved-universe@6
  - singularity.rate-rigidity-temperature-not-algebra-intrinsic@4
  - dark-energy.under-action-written-norm-parameter-laws@4
  assumes:
  - singularity.p-univalence@2
  - synthesis.r-lambda-regularity-cosmological-horizon@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_mirror_pair_same_rate_same_boost
- kind: check
  ref: check.py::check_conversion_factor_is_the_frozen_point_norm
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the mirror pair in the reversed form with the same rate and occupation boost, and kappa^2 = Q(I_Lambda) = H^2. Version 2 -> 3.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  note: Clauses (b) and (c) of the de Sitter temperature result, held apart so that the theorem's own premises are only (P) and (R_Lambda); the mirror clause brings in the premises of the two-towers theorem, the status clause those of the action as written.
  flow_note: phase flow e^{-i omega t} on the modes, converted at the rate of the rotor flow exp(t B_Lambda / 2).
---

## formal
Let $\Lambda > 0$ and let $T_{\Lambda} = \sqrt{Q(I_{\Lambda})}/2\pi$ be the temperature of Theorem \claimref{synthesis.de-sitter-temperature-frozen-point-norm}.
\begin{enumerate}
\item[(b)] The mirror's pair has the same rate and the same occupation boost, its ladder reversed (Theorem \claimref{synthesis.cosmological-horizon-completed-pair}(v)). So if (P) (Premise \claimref{singularity.p-univalence}) and (R$_{\Lambda}$) (Premise \claimref{synthesis.r-lambda-regularity-cosmological-horizon}) hold for the mirror's modes, which see the same Euclidean section because both towers are soldered to one manifold (Theorem \claimref{odd-extensions.two-towers-one-curved-universe}), the mirror's horizon temperature is the same $T_{\Lambda}$. This is a temperature of the horizon and says nothing about the ratio of the two sectors' plasma temperatures.
\item[(c)] The one conversion factor that the algebra does not supply (Theorem \claimref{singularity.rate-rigidity-temperature-not-algebra-intrinsic}) is here $\kappa_{\Lambda} = \sqrt{Q(I_{\Lambda})}$, the frozen point's norm, which under the action as written is a parameter of the laws (Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws}), so $T_{\Lambda}$ is undetermined within the series exactly as $\Lambda$ is.
\end{enumerate}

## technical
Two consequences of the cosmological horizon's temperature. First, the mirror world builds the same pair at the same horizon, with the roles of its two operators swapped, and both worlds share one spacetime. So if the same two premises hold for the mirror's modes, the mirror sees the same horizon temperature. This says nothing about how hot the mirror's own matter is compared with ours. Second, the only number the algebra cannot supply is the conversion of the flow parameter into time, and here that number is the frozen point's norm. Under the action as written that norm is a parameter of the laws, so the temperature is exactly as undetermined as the cosmological constant.

## lay
If the mirror world's quantum modes obey the same assumptions as ours, the mirror sees the cosmological horizon at the same temperature; this is about the horizon, not about how hot the mirror's own matter is. And the temperature's size is set by the same number as the cosmological constant, which the series' laws, as written, take as given rather than derive.

## one-liner
The mirror's modes see the same cosmological-horizon temperature under the same premises, and $T_{\Lambda}$ is as undetermined as $\Lambda$, its rate being the frozen point's norm.
