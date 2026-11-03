---
id: note.singularity.setting-model-run-exactly
kind: note
version: 1
title: The model, run exactly
status: setting
subject: entropy
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
comments_on:
- singularity.models-entropy-sequence-exactly
- singularity.eviction-window-thermal-product-radiation-entropy
- singularity.two-levels-finite-model
locators:
  paper: T05
  number: Setting
  section: 'The finite-mode model: the dissolution step by step'
  line: 2372
  subsection: The model, run exactly
---

## formal
The script runs the full model ($n = 4$ pairs, $N_{\max} = 2$, thermal angles from the rational triples $(c_k, s_k) = (\tfrac45, \tfrac35), (\tfrac45, \tfrac35), (\tfrac45, \tfrac35), (\tfrac{12}{13}, \tfrac{5}{13})$, a controlled-$Z$ between the two oldest window qubits before each eviction) and tabulates, after every event, the exact purity $\tr\rho_{R(t)}^{2}$ and the exact von Neumann entropy $S(\rho_{R(t)})$ of the radiation so far, together with the thermal accumulation and the capacity. Every entry of Table \ref{tab:model} is a rational number or an exact expression in the binary entropy $H(p)$ of a rational argument; the entropy columns are reported in bits, that is $H/\ln 2$ and $C/\ln 2 = |W|$, and the identities between the columns are verified as identities of formal logarithms; the decimals are for orientation only.

 \begin{tabular}{cccccccc}
\toprule
event & $|R|$ & window & $\tr\rho_R^{2}$ & $S_R = S_L$ (bits) & $\approx$ & $\Sth$ (bits) & $C$ (bits) \\
\midrule
1 & 1 & $\{L_1\}$ & $337/625$ & $h$ & $0.943$ & $h$ & 1 \\
2 & 2 & $\{L_1, L_2\}$ & $113569/390625$ & $2h$ & $1.885$ & $2h$ & 2 \\
3 & 4 & $\{L_2, L_3\}$ & $113569/390625$ & $2h$ & $1.885$ & $3h$ & 2 \\
4 & 6 & $\{L_3, L_4\}$ & $7198657/17850625$ & $h + h'$ & $1.547$ & $3h + h'$ & 2 \\
5 & 7 & $\{L_4\}$ & $21361/28561$ & $h'$ & $0.605$ & $3h + h'$ & 1 \\
6 & 8 & $\varnothing$ & $1$ & $0$ & $0$ & $3h + h'$ & 0 \\
\bottomrule
\end{tabular}

\emph{The finite-mode model, event by event, entropies in bits: $h = H(\tfrac{9}{25})/\ln 2 = H(\tfrac{16}{25})/\ln 2$ and $h' = H(\tfrac{25}{169})/\ln 2$ are the per-quantum entropies of the model's two kinds of pair, and $C$ is $|W|$. Events 1 and 2 are Phase I ($S_R = \Sth$ exactly); events 3 to 6 are Phase II, where $S_R = \sum_{k \in W}h_k$ lies strictly below the capacity whenever the window is nonempty, because no pair is maximally entangled, by exactly the shortfall Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy} quantifies. The descended reading of the same history, monotone with no falling branch, is Proposition \claimref{singularity.two-levels-finite-model}(2).}

## technical
pending

## lay
pending

## one-liner
pending
