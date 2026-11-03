---
id: singularity.rate-models-kinematic-inputs-l-u
kind: claim
version: 2
title: 'The rate model''s kinematic inputs: (L), (U), (C), (I)'
status: postulate
region: singularity
subject: entropy
tags: [entropy-premises]
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
lineage:
  motivated_by:
  - singularity.assembled-page-curve-up-typicality
locators:
  paper: T05
  number: Premise 11.3
  label: prem:ratemodel
  line: 2243
extraction:
  env: premise
  context_refs:
  - sheaf.localised-transport
  - sheaf.one-sided-completion
  - sheaf.one-sided-completion-singularity
  - sheaf.schwarzschild-degeneration-boundary-tame
  - singularity.assembled-page-curve-up-typicality
  - singularity.chains-state-class-stability
  - singularity.modular-descent
  typing:
    by: ai-typing-pass
    note: Postulate; no edges.
---

## formal
\leavevmode
\begin{itemize}
\item[(L)] \emph{Localisation, derived in part.} By \cite[Thm.~4.4, Cor.~4.5, Thms 8.7, 8.12]{ButlerT4} and Step 4a, the completion installs q-number degrees of freedom exactly where division fails, which licenses the window mode space $L(t)$ inside the closure of the degenerate locus; the radiation $R(t)$ is a q-number sector on the model's own grounds, its quanta being the emitted modes carried off $E$ by the emission rather than outputs of the localisation theorems; and that these two exhaust the sectors is the model's exhaustiveness postulate. The total state space at each stage is $H_{L(t)} \otimes H_{R(t)}$.
\item[(U)] \emph{Purity.} The ascended description is globally pure, as in Fact \claimref{singularity.assembled-page-curve-up-typicality}(i), each step of the evolution unitary.
\item[(C)] \emph{Capacity.} $\dim H_{L(t)} = 2^{|W(t)|}$ exactly, the number $|W(t)|$ of window modes filling to the mode count $N_{\mathrm{6a}}$ of Step 6a and non-increasing thereafter; the Page reading $C(t) \approx S_{\mathrm{BH}}(M(t))$ is for the full window.
\item[(I)] \emph{Injection.} The $k$-th emitted quantum enters in a thermofield pair $c_k|00\rangle + s_k|11\rangle$ with a fresh window mode, the pair form and the marginals from Theorem \claimref{singularity.modular-descent} and Corollary \claimref{singularity.chains-state-class-stability}; its \emph{freshness}, the clause that the pair arrives uncorrelated with everything already present, comes from neither cited result (Corollary \claimref{singularity.chains-state-class-stability}(3) leaves exactly such correlations free) and is an independent assumption of the rate model, marked as such precisely as (L$_E$)'s never-return clause is. The quantum carries the marginal entropy $h_k := H(c_k^{2}) \leq \ln 2$, with $H(p) := -p\ln p - (1-p)\ln(1-p)$ the binary entropy in nats and equality exactly at the maximally entangled pair $c_k = s_k$; the thermal accumulation is $\Sth(t) := \sum_{k \leq t} h_k$.
\end{itemize}

## technical
Postulates of the rate model. (L): the state space at each stage is $H_{L(t)} \otimes H_{R(t)}$, a window mode space inside the closure of the degenerate locus and a radiation sector, the exhaustiveness of these two sectors being postulated. (U): the ascended description is globally pure and each step is unitary. (C): $\dim H_{L(t)} = 2^{|W(t)|}$ exactly, filling to the mode count $N_{\mathrm{6a}}$ and non-increasing afterwards.

(I): the $k$-th emitted quantum enters in a thermofield pair $c_k|00\rangle + s_k|11\rangle$ with a fresh window mode, uncorrelated with everything present, freshness being an independent assumption. It carries $h_k = H(c_k^2) \leq \ln 2$, and the thermal accumulation is $\Sth(t) = \sum_{k \leq t} h_k$.

## lay
These are the basic assumptions of the framework's simple model of black-hole evaporation. Everything lives in two places, the black hole's interior modes and the radiation; the total state stays pure; the interior has a definite capacity that only shrinks once full; and each emitted quantum arrives entangled with a fresh partner inside. The freshness of each partner is assumed rather than derived.

## one-liner
Postulates of the rate model: two sectors (L), global purity (U), window dimension $2^{|W(t)|}$ (C), and fresh thermofield injection (I).
