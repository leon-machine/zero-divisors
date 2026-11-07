---
id: singularity.two-levels-finite-model
kind: claim
version: 6
title: The two levels of the finite model
status: proved
region: singularity
subject: entropy
tags: [finite-models, descent-map, radiation-spectrum, entanglement]
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
about:
- obj.singularity.multi-mode-descent
- obj.singularity.grading-parity-automorphism
derivations:
- name: main
  uses:
  - singularity.deficit-carried-quanta-correlations@5
  - singularity.deficit-theorem-cost-descent-exactly@4
  - singularity.purity-correlation-transfer-recovery@3
  - singularity.parity-protection@2
  - singularity.p-reduced-metric-level-reading-many@7
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:12.5
- kind: check
  ref: check.py::check_ascended_and_descended_ledgers
- kind: check
  ref: check.py::check_deficit_located_and_message_not_descending
- kind: check
  ref: check.py::check_records_survive_inter_pair_destroyed
locators:
  paper: T05
  number: Prop 12.5
  label: prop:twoledgers
  line: 2411
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the two ledgers of the full run: purities, the printed value, S(E rho_R) = S_th, monotone descent, the deficit, annihilated correlators, records and factorisation. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  env: proposition
  context_refs:
  - singularity.p-reduced-metric-level-reading-many
  - singularity.parity-protection
  typing:
    by: ai-typing-pass
    added:
    - singularity.parity-protection
    - singularity.p-reduced-metric-level-reading-many
    note: 'Added parity protection, cited with the correlation corollary for the equal single-qubit marginals,
      and the reduced (P_loc) proposition, which the statement uses to equate metric-level measurements
      with joint-number-diagonal observables (the latter is a judgement call); the paper says Hawking''s
      curve is recovered here, but Hawking''s result is not an imported claim in the store, so no standard
      route was added. Levels pass: conditions already kept.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - singularity.p-reduced-metric-level-reading-many
    - singularity.parity-protection
---

## formal
In the full model run of Section \ref{subsec:ledger} ($n = 4$ pairs, $N_{\max} = 2$), write $\rho_R$ for the state of the complete radiation at evaporation's end (all eight qubits) and $E := \EN$ for the joint-number dephasing. Then:
\begin{enumerate}
\item (Ascended level.) $\tr \rho_R^2 = 1$: $S_2(\rho_R) = 0$. The radiation is pure, and all information is internal to it (Proposition \claimref{singularity.purity-correlation-transfer-recovery}).
\item (Descended level.) Exactly,
\[
\tr\bigl(E\rho_R\bigr)^2 \;=\; \prod_{k=1}^{4}\bigl(c_k^4 + s_k^4\bigr) \;=\; \frac{817544276833}{6972900390625},
\qquad
S_2(E\rho_R) = \log_2\frac{6972900390625}{817544276833} \approx 3.09 \ \text{bits},
\]
and the von Neumann entropy of $E\rho_R$ is $\sum_k H(c_k^2) = \Sth$ exactly, the full thermal accumulation. Stage by stage, the descended entropy is monotone non-decreasing: read at the $\Cl(1,3)$ level, the radiation's entropy only rises, with no falling branch and no return to zero. This is Hawking's curve, recovered as the wrong-level reading of a history whose ascended state is pure.
\item (The deficit, located.) $\rel{\rho_R}{E\rho_R} = S(E\rho_R) - S(\rho_R) = \Sth$: at completion the radiation's entire information content is the deficit, and the deficit is inter-quanta. Every single-qubit marginal is identical at the two levels (Corollary \claimref{singularity.deficit-carried-quanta-correlations} with Lemma \claimref{singularity.parity-protection}); the decoding correlators of Proposition \claimref{singularity.purity-correlation-transfer-recovery}, whose signatures $(\tfrac{24}{25}, \tfrac{168}{625})$ against $(\tfrac{168}{625}, \tfrac{24}{25})$ distinguish the scrambled from the unscrambled history in the completion, are annihilated exactly by $E$: both become $0$, in both histories, so the two descended histories are indistinguishable by any metric-level measurement, that is, by any joint-number-diagonal observable (Proposition \claimref{singularity.p-reduced-metric-level-reading-many}; under the total-parity grading alone the even correlator $X_{R_1}X_{L_1}Z_{L_2}$ would descend, which is exactly why the pointwise reading is the one the chain needs), and the message does not descend.
\item (What survives, and what is lost.) Descent preserves each intra-pair classical record exactly: the $(R_k, L_k)$ marginal of $E\rho_R$ is the perfectly correlated $\operatorname{diag}(c_k^2, 0, 0, s_k^2)$. And descent destroys every inter-pair correlation exactly: the joint distributions of $(R_k, R_l)$, $k \neq l$, factorise. What the metric level retains is the thermal populations together with the pairwise emission records; everything the scrambling wrote \emph{across} the pairs, which is where Proposition \claimref{singularity.purity-correlation-transfer-recovery} located the information, is erased.
\end{enumerate}

## technical
In the full model run with four pairs, let $\rho_R$ be the complete radiation at the end of evaporation and $E = \EN$ the joint-number dephasing. At the ascended level $\tr\rho_R^2 = 1$, so the radiation is pure. At the descended level $\tr(E\rho_R)^2 = \prod_k (c_k^4 + s_k^4)$, $S_2(E\rho_R) \approx 3.09$ bits, and $S(E\rho_R) = \Sth$ exactly, with the descended entropy non-decreasing stage by stage: Hawking's curve, as the metric-level reading of a pure history.

The deficit is $\rel{\rho_R}{E\rho_R} = \Sth$ and is inter-quanta: single-qubit marginals agree at both levels, and the decoding correlators are annihilated by $E$, so the scrambled and unscrambled histories cannot be told apart by any joint-number-diagonal observable. Descent keeps each pair's classical emission record and erases every inter-pair correlation.

## lay
The toy model can be read at two levels. At the full quantum level the radiation is pure and carries all the information. Read at the ordinary metric level, which keeps only occupation records, the same radiation looks thermal, its entropy only rises, and the trace of the scrambling disappears. This reproduces Hawking's picture of information loss as a reading at the wrong level.

## one-liner
In the full model the radiation is pure at the ascended level but has entropy $\Sth$ at the descended level, the deficit being exactly the inter-pair correlations that descent erases.
