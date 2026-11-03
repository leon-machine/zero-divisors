---
id: obj.singularity.multi-mode-descent
kind: object
version: 1
title: The multi-mode descent
status: defined
region: singularity
subject: descent
tags: [descent-map]
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
locators:
  paper: T05
  number: Def 9.1
  label: def:multidescent
  line: 2065
extraction:
  env: definition
  context_refs:
  - singularity.descent-what-it-erases
  - singularity.p-reduced-metric-level-reading-many
  typing:
    by: ai-typing-pass
    note: definition only; no edges to review
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - singularity.deficit-carried-quanta-correlations
    - singularity.deficit-theorem-cost-descent-exactly
    - singularity.exact-equilibrium-over-determines-boundary-modes
    added_about: []
    verdict: connected
    note: A definition cannot carry uses or assumes; the added links are about edges from the claims whose
      statements use the defined notion.
---

## formal
For $N$ completed pairs $(v_k, v_k^*)$ with commuting occupation projectors $P_k := v_k^* v_k$, and for each $\varepsilon \in \{0,1\}^N$ the joint occupation projector $\Pi_\varepsilon := \prod_k \bigl(\varepsilon_k P_k + (1 - \varepsilon_k)(1 - P_k)\bigr)$ (orthogonal, complete: $\sum_\varepsilon \Pi_\varepsilon = 1$), the \emph{multi-mode descent} is the pinching
\[
\EN(x) \;:=\; \sum_{\varepsilon \in \{0,1\}^N} \Pi_\varepsilon\, x\, \Pi_\varepsilon ,
\]
the composition of the mode-wise maps of Proposition \claimref{singularity.descent-what-it-erases}. In the joint number representation, $\EN$ retains every matrix element diagonal in the joint occupation basis and erases every off-diagonal one: complete dephasing in the joint number basis. Its kernel is spanned by the operators carrying at least one off-diagonal mode factor, which is precisely the sector in which inter-mode coherence lies; its range is the algebra of joint-number-diagonal operators, the classical algebra of occupation records. That this range, and not the larger total-parity-even algebra, is the metric level on many modes is not a consequence of the grading: it is the composite argument of Proposition \claimref{singularity.p-reduced-metric-level-reading-many}, stated at the end of this step, where its effect is visible. One word of disambiguation, on which everything depends: ``pair'' here means one completed ladder pair, one \emph{mode}, in Rule 1's sense; the ``pairs'' of Section \ref{sec:model}'s model are Hawking pairs, each two modes, one radiation and one window, so the model's $n$ pairs are $2n$ modes and $\EN$ there pinches all $2n$, one $\sigma_k$ per mode and never one per Hawking pair (on that wrong reading $\sigma$ would be $Z_{R_k}Z_{L_k}$, the strictness witness would fail, and the deficit would be exactly zero).

## technical
For $N$ completed pairs with commuting occupation projectors $P_k = v_k^{*}v_k$, the joint occupation projectors $\Pi_\varepsilon$, $\varepsilon \in \{0,1\}^N$, are orthogonal and sum to the identity. The multi-mode descent is the pinching $\EN(x) = \sum_\varepsilon \Pi_\varepsilon\, x\, \Pi_\varepsilon$, the composite of the single-mode descents. In the joint number basis it keeps every diagonal matrix element and erases every off-diagonal one: its kernel is spanned by the operators with at least one off-diagonal mode factor, which is where inter-mode coherence lies, and its range is the algebra of joint-number-diagonal operators.

That this range, rather than the larger algebra that is even under total parity, is the metric level on many modes is not a consequence of the grading; it is argued separately. Here a "pair" means one completed ladder pair, that is one mode: a Hawking pair is two modes, and $\EN$ pinches each of them separately.

## lay
With many fermionic modes, the multi-mode descent keeps only the record of which modes are occupied and discards every quantum coherence, including coherence between different modes. What survives is a classical list of occupation records. A Hawking pair counts as two modes here, and each is treated on its own.

## one-liner
The multi-mode descent $\EN(x) = \sum_\varepsilon \Pi_\varepsilon x \Pi_\varepsilon$ pinches every mode in the joint occupation basis, keeping the classical algebra of occupation records and erasing all coherence.
